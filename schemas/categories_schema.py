from main import ma
from marshmallow import fields

# create the Category Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CategorySchema(ma.Schema):
    ordered = True
    # Fields to expose
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    competitions = fields.List(fields.Nested("CompetitionSchema", exclude=["category", "id", "prize", "description"]))
    class Meta:
        fields = ("id", "title", "description", "competitions")

# single category schema, when one category needs to be retrieved
category_schema = CategorySchema()
# multiple category schema, when many categories need to be retrieved
categories_schema = CategorySchema(many=True)