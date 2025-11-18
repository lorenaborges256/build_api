from marshmallow import fields
from main import ma

# create the Participation Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class ParticipationSchema(ma.Schema):
    competition =  fields.Nested("CompetitionSchema", only=["title", "year"])
    participant =  fields.Nested("ParticipantSchema", only=["name", "address"])
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "prize", "year", "competition", "participant")

# single participation schema, when one participation needs to be retrieved
participation_schema = ParticipationSchema()
# multiple participation schema, when many participations need to be retrieved
participations_schema = ParticipationSchema(many=True)