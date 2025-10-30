from main import ma
from marshmallow import fields

class CompetitionSchema(ma.Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    prize = fields.Str()
    year = fields.Int()

competition_schema = CompetitionSchema()
competitions_schema = CompetitionSchema(many=True)
