from main import ma

# create the Competition Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CompetitionSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "prize", "year")

# single competition schema, when one competition needs to be retrieved
competition_schema = CompetitionSchema()
# multiple competition schema, when many competitions need to be retrieved
competitions_schema = CompetitionSchema(many=True)