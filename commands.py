from main import db
from flask import Blueprint
from models.competitions import Competition
from models.participants import Participant
from models.categories import Category
from models.participations import Participation

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands .cli.command("seed")
def seed_db():
    category1 = Category(
        title="sports",
        description="physical/athletic sports"
    )
    db.session.add(category1)

    category2 = Category(
        title="quiz",
        description="different types of quiz competitions"
    )
    db.session.add(category2)
    # commit the changes
    db.session.commit()

    # create the Competition object
    competition1 = Competition(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title="FIFA World Cup",
        description="The world cup of football",
        prize="20 million",
        year=2024,
        category_id=category1.id
    )
    # Add the object as a new row to the table
    db.session.add(competition1)

    competition2 = Competition(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title="Australian Football League",
        description="The league for Australian Football",
        prize="10 million",
        year=2020,
        category=category1
    )
    # Add the object as a new row to the table
    db.session.add(competition2)


    participant1 = Participant(
        name="Participant 1",
        address="One Street, Suburb1",
        phone="0412345678"
    )
    db.session.add(participant1)

    participant2 = Participant(
        name="Participant 2",
        address="Two Street, Suburb2",
        phone="0487654321"
    )
    db.session.add(participant2)
    # commit the changes
    db.session.commit()

    participation1 = Participation(
        rank=1,
        competition=competition1,
        participant=participant1
    )
    db.session.add(participation1)

    participation2 = Participation(
        rank=7,
        competition=competition1,
        participant=participant2
    )
    db.session.add(participation2)


        
    # commit the changes
    db.session.commit()
    print("Table seeded")

@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")
    