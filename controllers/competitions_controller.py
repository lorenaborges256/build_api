from flask import Blueprint, jsonify, request, abort
from main import db
from models.competitions import Competition
from models.categories import Category
from models.participants import Participant
from models.participations import Participation
from schemas.competitions_schema import competition_schema, competitions_schema
from schemas.categories_schema import category_schema, categories_schema
from schemas.participations_schema import participation_schema

competitions = Blueprint('competitions', __name__, url_prefix="/competitions")

# The GET routes endpoint
@competitions.route("/", methods=["GET"])
def get_competitions():
    # get all the competitions from the database table
    stmt = db.select(Competition)
    competitions_list = db.session.scalars(stmt)
    # Convert the competitions from the database into a JSON format and store them in result
    result = competitions_schema.dump(competitions_list)
    # return the data in JSON format
    return jsonify(result)

# The GET competition routes endpoint
@competitions.route("/<int:id>/", methods=["GET"])
def get_competition(id):
    stmt = db.select(Competition).filter_by(id=id)
    competition = db.session.scalar(stmt)
    #return an error if the competition doesn't exist
    if not competition:
        return abort(400, description= "Competition does not exist")
    # Convert the competitions from the database into a JSON format and store them in result
    result = competition_schema.dump(competition)
    # return the data in JSON format
    return jsonify(result)

@competitions.route("/search", methods=["GET"])
def search_competitions():
     # create an empty list in case the query string is not valid
    competitions_list = []
    # search by year
    if request.args.get('year'):
        # find the competition by filtering by the year
        stmt = db.select(Competition).filter_by(year= request.args.get('year'))
        competitions_list = db.session.scalars(stmt)
    # search by prize instead of year
    elif request.args.get('prize'):
        # find the competition by filtering by the prize
        stmt = db.select(Competition).filter_by(prize= request.args.get('prize'))
        competitions_list = db.session.scalars(stmt)

    result = competitions_schema.dump(competitions_list)
    # return the data in JSON format
    return jsonify(result)

@competitions.route("/categories", methods=["GET"])
def get_categories():
    # get all the categories from the database table
    stmt = db.select(Category)
    categories_list = db.session.scalars(stmt)
    # Convert the categories from the database into a JSON format and store them in result
    result = categories_schema.dump(categories_list)
    # return the data in JSON format
    return jsonify(result)

# The POST route endpoint
@competitions.route("/", methods=["POST"])
def create_competition():
    # Create a new competition
    competition_fields = competition_schema.load(request.json)

    new_competition = Competition()
    new_competition.title = competition_fields["title"]
    new_competition.description = competition_fields["description"]
    new_competition.prize = competition_fields["prize"]
    new_competition.year = competition_fields["year"]
    # add category's id
    new_competition.category_id = competition_fields["category_id"]
    # add to the database and commit
    db.session.add(new_competition)
    db.session.commit()
    # return the competition in the response
    return jsonify(competition_schema.dump(new_competition))

#POST a new participation
@competitions.route("/<int:id>/participations", methods=["POST"])
# competition id required to assign the participation to a competition
def post_participation(id):
    # Create a new participation
    participation_fields = participation_schema.load(request.json)

    # get the participant id from the request body
    participant_id = participation_fields["participant_id"]
    # Find it in the db
    stmt = db.select(Participant).filter_by(id=participant_id)
    participant = db.session.scalar(stmt)
    # Make sure it is in the database
    if not participant:
        return abort(400, description="Invalid participant")

    # find the competition
    stmt = db.select(Competition).filter_by(id=id)
    competition = db.session.scalar(stmt)
    # return an error if the competition doesn't exist
    if not competition:
        return abort(400, description= "Competition does not exist")
    # create the participation with the given values
    new_participation = Participation()
    new_participation.participant_id = participation_fields["participant_id"]
    # Use the competition gotten by the id of the route
    new_participation.competition = competition
    # add to the database and commit
    db.session.add(new_participation)
    db.session.commit()
    # return the card in the response
    return jsonify(participation_schema.dump(new_participation))

# The DELETE route endpoint
@competitions.route("/<int:id>/", methods=["DELETE"])
def delete_competition(id):
    # find the competition
    stmt = db.select(Competition).filter_by(id=id)
    competition = db.session.scalar(stmt)
    # return an error if the competition doesn't exist
    if not competition:
        return abort(400, description= "Competition doesn't exist")
    # Delete the competition from the database and commit
    db.session.delete(competition)
    db.session.commit()
    # return the competition in the response
    return jsonify(competition_schema.dump(competition))

# The POST route endpoint
@competitions.route("/<int:id>/", methods=["PUT"])
def update_competition(id):
    # Create a new competition
    competition_fields = competition_schema.load(request.json)

    # find the competition
    stmt = db.select(Competition).filter_by(id=id)
    competition = db.session.scalar(stmt)

    # return an error if the competition doesn't exist
    if not competition:
        return abort(400, description= "Competition does not exist")
    # update the competition details with the given values
    competition.title = competition_fields["title"]
    competition.description = competition_fields["description"]
    competition.prize = competition_fields["prize"]
    competition.year = competition_fields["year"]
    # add to the database and commit
    db.session.commit()
    #return the competition in the response
    return jsonify(competition_schema.dump(competition))

# edit a participation
@competitions.route("/<int:competition_id>/participations/<int:participation_id>", methods=["PUT"])
def update_participation(competition_id, participation_id):
    participation_fields = participation_schema.load(request.json)

    # get the participant id from the request body
    participant_id = participation_fields["participant_id"]
    # Find it in the db
    stmt = db.select(Participant).filter_by(id=participant_id)
    participant = db.session.scalar(stmt)
    # Make sure it is in the database
    if not participant:
        return abort(400, description="Invalid participant")

    # find the competition
    stmt = db.select(Competition).filter_by(id=competition_id)
    competition = db.session.scalar(stmt)
    # return an error if the competition doesn't exist
    if not competition:
        return abort(400, description= "Competition does not exist")
    
    # Check if the participant has participated in the competition or not
    stmt = db.select(Participation).filter_by(id=participation_id)
    existing_participation = db.session.scalar(stmt)

    if not existing_participation:
        return abort(400, description= "Participation doesn't exist")

    # update the participation details with the given values
    existing_participation.rank = participation_fields["rank"]
    # add to the database and commit
    db.session.add(existing_participation)
    db.session.commit()
    # return the card in the response
    return jsonify(participation_schema.dump(existing_participation))

