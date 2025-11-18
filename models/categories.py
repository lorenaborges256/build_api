from main import db

class Category(db.Model):
    # define the table name for the db
    __tablename__= "categories"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    title = db.Column(db.String())
    description = db.Column(db.String())
    competitions = db.relationship(
        "Competition",
        back_populates="category",
        cascade="all, delete"
    )