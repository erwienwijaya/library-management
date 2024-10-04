from flask import Blueprint, request, jsonify, abort
from app.services.author_services import AuthorService
from app.services.book_services import BookService
from ..schemas import AuthorSchema
from marshmallow import ValidationError

author_bp = Blueprint('api', __name__)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

# get all authors
@author_bp.route('/authors', methods=['GET'])
def get_authors():
    authors = AuthorService.get_all_authors()
    result = authors_schema.dump(authors)
    return jsonify(result), 200

# get author by id
@author_bp.route('/authors/<uuid:author_id>', methods=['GET'])
def get_author_by_id(author_id):
    author = AuthorService.get_author_by_id(author_id)
    if not author:
        abort(404, 'Author not found')

    result = author_schema.dump(author)
    return jsonify(result), 200

# create new author
@author_bp.route('/authors', methods=['POST'])
def create_author():
    try:
        # Validate the request payload against the schema
        data = author_schema.load(request.get_json())
    except ValidationError as err:
        return  jsonify(err.messages), 400

    new_author = AuthorService.create_author(data)
    return jsonify(author_schema.dump(new_author)), 201


# update author
@author_bp.route('/authors/<uuid:author_id>', methods=['PUT'])
def update_author(author_id):
    author = AuthorService.get_author_by_id(author_id)
    if not author:
        abort(404, 'Author not found')

    try:
        # Validate request payload
        data = author_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    AuthorService.update_author(author, data)
    return jsonify(author_schema.dump(author)), 200

# delete author
@author_bp.route('/authors/<uuid:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = AuthorService.get_author_by_id(author_id)
    if not author:
        abort(404, 'Author not found')

    book = BookService.get_book_by_author(author_id)

    if book:
        abort(406, 'can\'t allowed to delete, the books registered by author')

    AuthorService.delete_author(author)
    return jsonify({"message": "Author deleted successfully"}), 200


