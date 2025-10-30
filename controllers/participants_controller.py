from flask import Blueprint, jsonify, request, abort
from main import db
from models.participants import Participant
from schemas.participants_schema import participant_schema, participants_schema

participants = Blueprint('participants', __name__, url_prefix="/participants")

# The GET routes endpoint
@participants.route("/", methods=["GET"])
def get_participants():
    # get all the participants from the database table
    stmt = db.select(Participant)
    participants_list = db.session.scalars(stmt)
    # Convert the participants from the database into a JSON format and store them in result
    result = participants_schema.dump(participants_list)
    # return the data in JSON format
    return jsonify(result)

# The POST route endpoint
@participants.route("/", methods=["POST"])
def create_participant():
    # Create a new participant
    participant_fields = participant_schema.load(request.json)

    new_participant = Participant()
    new_participant.name = participant_fields["name"]
    new_participant.address = participant_fields["address"]
    new_participant.phone = participant_fields["phone"]
    # add to the database and commit
    db.session.add(new_participant)
    db.session.commit()
    # return the participant in the response
    return jsonify(participant_schema.dump(new_participant))


# The DELETE route endpoint
@participants.route("/<int:id>/", methods=["DELETE"])
def delete_participant(id):
    # find the participant
    stmt = db.select(Participant).filter_by(id=id)
    participant = db.session.scalar(stmt)
    # return an error if the participant doesn't exist
    if not participant:
        return abort(400, description= "Participant doesn't exist")
    # Delete the participant from the database and commit
    db.session.delete(participant)
    db.session.commit()
    # return the participant in the response
    return jsonify(participant_schema.dump(participant))