from main import ma

# create the Category Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CategorySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description")

# single category schema, when one category needs to be retrieved
category_schema = CategorySchema()
# multiple category schema, when many categories need to be retrieved
categories_schema = CategorySchema(many=True)