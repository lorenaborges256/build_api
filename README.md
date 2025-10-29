# build_api
Mini Learning Management System - JAN 2025

to access postgres sudo -u postgres psql
\l list databases created

# Agenda for Mini Project Module 4 until deployment

Creating a mini LMS (Learning Management System)

Revisions from the previous class - Creating a Flask App, Connecting to Github 


Installing required packages 
Pip install flask psycopg2-binary flask-sqlalchemy marshmallow-sqlalchemy python-dotenv 

Create a requirements.txt file after that. 
Pip freeze > requirements.txt

Adding files to gitignore  (imp to remember)
venv/ 
.flaskenv/
.env/
__pycache__/


Two ways to create the project
First create repo and add all folders - push after each commit 
Create folder and files first—later connect with githib repo and push


Some Terms and Links

Flask psycopg2-binary  
(PostgreSQL database adapter for the Python programming language) https://pypi.org/project/psycopg2-binary/

psycopg2 is a popular and efficient Python adapter for connecting to and interacting with PostgreSQL databases. It allows Python programs to run SQL commands, fetch query results, manage transactions, and access a wide range of PostgreSQL features. 

Flask-sqlalchemy 
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. https://flask-sqlalchemy.readthedocs.io/en/stable/

Marshmallow: 
marshmallow is an ORM/ODM/framework-agnostic library for converting complex data types, such as objects, to and from native Python data types.
https://marshmallow.readthedocs.io/en/latest/

What is ORM/ODM
An ORM (Object-Relational Mapper) is a technique for interacting with relational databases (like SQL) using objects, while an ODM (Object-Document Mapper) is used for document databases (like MongoDB). A framework is a collection of libraries, tools, and code structures that provides a foundational structure for building applications, and it can incorporate ORM or ODM libraries to handle database interactions. 

Python dotenv
https://pypi.org/project/python-dotenv/
python-dotenv reads key-value pairs from a .env file and can set them as environment variables.

Flask Application Factory
Blue print 
A function wrapup  - only runs when called (so it helps in resource management in serves and applications)

Setting up .env file 

# Replace the values with what you define in your application
DATABASE_URI=database+driver://username:password@server:port/databasename
