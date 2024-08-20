from flask_sqlalchemy import SQLAlchemy
from extensions import db

db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70))
    # books = db.relationship('Books', backref= "author")
    # user = db.relationship('Users', backref='author')

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70))
    author_id = db.Column(db.Integer(), db.ForeignKey('author.id'))

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_one_id = db.Column(db.Integer(), db.ForeignKey('author.id'))
    user_two_id = db.Column(db.Integer(), db.ForeignKey('author.id'))

