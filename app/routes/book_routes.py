from flask import Blueprint, request, jsonify, abort
from app.services.book_services import BookService
from app.services.author_services import AuthorService
from ..schemas import BookSchema
from marshmallow import ValidationError

book_bp = Blueprint('book', __name__)

# Schema initialization
book_schema = BookSchema()
books_schema = BookSchema(many=True)


# get all books
@book_bp.route('/books', methods=['GET'])
def get_books():
    books = BookService.get_all_books()
    result = books_schema.dump(books)
    return jsonify(result), 200


# get book by id
@book_bp.route('/books/<uuid:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = BookService.get_book_by_id(book_id)
    if not book:
        abort(404, "Book not found")

    result = book_schema.dump(book)
    return jsonify(result), 200


# create new book
@book_bp.route('/books', methods=['POST'])
def create_book():
    try:
        # Validate the request payload against the schema
        data = book_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if the author exists
    author = AuthorService.get_author_by_id(data['author_id'])
    if not author:
        abort(404, "Author not found")

    new_book = BookService.create_book(data)
    return jsonify(book_schema.dump(new_book)), 201


# update book
@book_bp.route('/books/<uuid:book_id>', methods=['PUT'])
def update_book(book_id):
    book = BookService.get_book_by_id(book_id)
    if not book:
        abort(404, "Book not found")

    try:
        # Validate the request payload
        data = book_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if the author exists
    author = AuthorService.get_author_by_id(data['author_id'])
    if not author:
        abort(404, "Author not found")

    BookService.update_book(book, data)
    return jsonify(book_schema.dump(book)), 200


# delete book
@book_bp.route('/books/<uuid:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = BookService.get_book_by_id(book_id)
    if not book:
        abort(404, "Book not found")

    BookService.delete_book(book)
    return jsonify({"message": "Book deleted successfully"}), 200


# get all books by a specific author
@book_bp.route('/authors/<uuid:author_id>/books', methods=['GET'])
def get_books_by_author(author_id):
    # Check if the author exists
    author = AuthorService.get_author_by_id(author_id)
    if not author:
        abort(404, "Author not found")

    books = BookService.get_book_by_author(author_id)

    if not books:
        abort(404, "book not found")

    result = books_schema.dump(books)
    return jsonify(result), 200