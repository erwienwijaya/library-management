from app.models import Book
from app import db

class BookRepository:
    @staticmethod
    def get_all():
        return Book.query.all()

    @staticmethod
    def get_by_id(book_id):
        return db.session.get(Book, book_id)
        # return Book.query.get(book_id)

    @staticmethod
    def get_by_author(author_id):
        return Book.query.filter_by(author_id=str(author_id)).all()

    @staticmethod
    def save(book):
        db.session.add(book)
        db.session.commit()

    @staticmethod
    def delete(book):
        db.session.delete(book)
        db.session.commit()
