from main import ma
from marshmallow import fields

class ParticipantSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    address = fields.Str()
    phone = fields.Str()
    # Add other fields as needed

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)