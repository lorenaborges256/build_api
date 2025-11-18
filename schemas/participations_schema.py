from marshmallow import fields
from main import ma

# create the Participation Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class ParticipationSchema(ma.Schema):
    id = fields.Int()
    competition_id = fields.Int(load_only = True)
    participant_id = fields.Int(load_only = True)
    rank = fields.Int()
    competition =  fields.Nested("CompetitionSchema", only=["title", "year"])
    participant =  fields.Nested("ParticipantSchema", only=["name", "address"])
    class Meta:
        # Fields to expose
        fields = ("id", "rank", "competition_id", "participant_id", "competition", "participant")
        load_only = ("participant_id",)

# single participation schema, when one participation needs to be retrieved
participation_schema = ParticipationSchema()
# multiple participation schema, when many participations need to be retrieved
participations_schema = ParticipationSchema(many=True)