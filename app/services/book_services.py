from app.repositories.book_repository import BookRepository
from app.models import Book

class BookService:
    @staticmethod
    def get_all_books():
        return BookRepository.get_all()

    @staticmethod
    def get_book_by_id(book_id):
        return BookRepository.get_by_id(book_id)

    @staticmethod
    def get_book_by_author(author_id):
        return BookRepository.get_by_author(author_id)

    @staticmethod
    def create_book(data):
        new_book = Book(**data)
        BookRepository.save(new_book)
        return new_book

    @staticmethod
    def update_book(book, data):
        for key, value in data.items():
            setattr(book, key, value)
        BookRepository.save(book)

    @staticmethod
    def delete_book(book):
        BookRepository.delete(book)

