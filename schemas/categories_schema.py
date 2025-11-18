from main import ma
from marshmallow import fields

# create the Category Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CategorySchema(ma.Schema):
    # Fields to expose
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()

# single category schema, when one category needs to be retrieved
category_schema = CategorySchema()
# multiple category schema, when many categories need to be retrieved
categories_schema = CategorySchema(many=True)