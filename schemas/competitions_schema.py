from main import ma
from marshmallow import fields
from schemas.categories_schema import CategorySchema

# create the Competition Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CompetitionSchema(ma.Schema):
    # Fields to expose
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    prize = fields.Str()
    year = fields.Int()
    category_id = fields.Int(load_only = True)    
    category =  fields.Nested(CategorySchema, only=["title"])
    class Meta:
        fields = ("id", "title", "description", "prize", "year", "category_id", "category")


competition_schema = CompetitionSchema()
competitions_schema = CompetitionSchema(many=True)
