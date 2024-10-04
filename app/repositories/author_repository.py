from app.models import Author
from app import db

class AuthorRepository:
    @staticmethod
    def get_all():
        return Author.query.all()


    @staticmethod
    def get_by_id(author_id):
        return db.session.get(Author, author_id)
        # depracated SQLAlchemy 2.0, don't use this code on below one
        # return Author.query.get_or_404(author_id)


    @staticmethod
    def get_by_name(name):
        return Author.query.filter_by(name=name).first()


    @staticmethod
    def save(author):
        db.session.add(author)
        db.session.commit()


    @staticmethod
    def delete(author_id):
        db.session.delete(author_id)
        db.session.commit()
