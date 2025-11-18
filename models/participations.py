from main import db

class Participation(db.Model):
    # define the table name for the db
    __tablename__= "participations"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    rank = db.Column(db.Integer)
    competition_id = db.Column(db.Integer, db.ForeignKey("competitions.id"), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey("participants.id"), nullable=False)
    competition = db.relationship(
        "Competition",
        back_populates="participations"
    )
    participant = db.relationship(
        "Participant",
        back_populates="participations"
    )