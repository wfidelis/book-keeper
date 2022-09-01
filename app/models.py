from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import app

#create a Flask object
db = SQLAlchemy(app)


#SQLAlchemy Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://fidelis:jemaidah5@localhost/booksdb'
app.config['SECRET_KEY'] = "x10\xcbb\x00\x94\xccA\xc8\x13\xfc\x89K"

book_publisher = db.Table('book_publisher', 
                            db.Column('book_id', db.Column(db.Integer, db.ForeignKey('book_id'))),
                            db.Column('publisher_id'), db.Column(db.Integer, db.ForeignKey('publisher.id')))

book_genre = db.Table('book_genre',
                db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')),
                db.Column('book_id', db.Integer, db.ForeignKey('book.id')))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), unique = True)
    author = db.Column(db.String(150), nullable = False)
    language = db.Column(db.Sring(100))
    country = db.Column(db.String(100))
    read_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.Datetime, onupdate=datetime.datetime.now)
    publisher = db.relationship('Publisher', secondary = book_publisher)
    genre = db.relationship('Genre', secondary=book_genre)
    series_id = db.Column(db.Integer, db.ForeignKey('series_id'))

class Publisher(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))

class Genre(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

class Series(db.model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150))
    book = db.relationship('Book')




