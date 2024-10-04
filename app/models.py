import uuid
from . import db
# from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy import ForeignKey


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    published_date = db.Column(db.Date, nullable=True)
    author_id = db.Column(db.String(50), ForeignKey('author.id'), nullable=False)