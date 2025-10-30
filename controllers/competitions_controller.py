from flask import Blueprint, jsonify, request, abort
from main import db
from models.competitions import Competition
from schemas.competitions_schema import competition_schema, competitions_schema

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
    # add to the database and commit
    db.session.add(new_competition)
    db.session.commit()
    # return the competition in the response
    return jsonify(competition_schema.dump(new_competition))


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