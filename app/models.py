from datetime import datetime
from app import db

book_publisher = db.Table('book_publisher',
                            db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                            db.Column('publisher_id', db.Integer, db.ForeignKey('publisher.id')))

book_genre = db.Table('book_genre',
                db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')),
                db.Column('book_id', db.Integer, db.ForeignKey('book.id')))



class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), unique = True)
    author = db.Column(db.String(150), nullable = False)
    language = db.Column(db.String(100))
    country = db.Column(db.String(100))
    read_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    publisher = db.relationship('Publisher', secondary = book_publisher)
    genre = db.relationship('BookGenre', secondary=book_genre)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

class Series(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150))
    book = db.relationship('Book')



