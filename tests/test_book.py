import json
from http.client import responses

import pytest
from flask.testing import FlaskClient
from app import create_app, db
from app.models import Author, Book

@pytest.fixture
def client():
    app = create_app('config.TestingConfig')

    # create test client
    testing_client: FlaskClient
    with app.test_client() as client:
        with app.app_context():
            # create the database and tables testing
            db.create_all()

            # Seed data for author and book
            author = Author(id="e5a47420-5dbc-491d-9a3d-7ae76d1c92e7",
                            name="Donny Dhirgantoro",
                            bio="Test bio",
                            birth_date="1978-10-27")
            db.session.add(author)

            book = Book(
                    id="123e4567-e89b-12d3-a456-426614174000",  # UUID buku
                    title="5 cm",
                    description="kisah persahabatan 5 orang yang menaklukan mahameru",
                    published_date="2015-08-17",
                    author_id=author.id  # Foreign key ke author
            )
            db.session.add(book)
            db.session.commit()

            # seed the database with initial test data
            yield client

            # drop all tables after test
            db.session.remove()
            db.drop_all()


def test_create_book(client):
    new_book = {
        "title": "10 cm",
        "description": "kisah persahabatan 10 orang yang menaklukan everest",
        "published_date": "2015-08-17",
        "author_id": "e5a47420-5dbc-491d-9a3d-7ae76d1c92e7"
    }
    response = client.post('/api/books',
                           data=json.dumps(new_book),
                           content_type='application/json')
    assert response.status_code == 201
    assert response.json['title'] == new_book['title']
    assert response.json['author_id'] == new_book['author_id']
    assert response.json['description'] == new_book['description']


def test_get_all_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert len(response_data) > 0
    assert response_data[0]['title'] == "5 cm"


def test_get_book_by_id(client):
    response = client.get('/api/books/123e4567-e89b-12d3-a456-426614174000')
    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert len(response_data) > 0
    assert response_data['title'] == "5 cm"


def test_no_book_by_id(client):
    response = client.get('/api/books/123e4567-e89b-12d3-a456-426614174001')
    assert response.status_code == 404


def test_get_book_by_author_id(client):
    response = client.get('/api/authors/e5a47420-5dbc-491d-9a3d-7ae76d1c92e7/books')
    assert response.status_code == 200
    assert response.json[0]['title'] == "5 cm"


def test_update_book(client):
    updated_book = {
        "title": "5 cm - extended version",
        "description": "A new version of the book",
        "published_date": "2024-05-10",
        "author_id": "e5a47420-5dbc-491d-9a3d-7ae76d1c92e7"
    }

    # Update created book
    update_response = client.put('/api/books/123e4567-e89b-12d3-a456-426614174000',
                                 data=json.dumps(updated_book),
                                 content_type='application/json')
    assert update_response.status_code == 200

    response_data = json.loads(update_response.data)
    assert response_data['title'] == '5 cm - extended version'


def test_delete_book(client):
    # Delete created book
    delete_response = client.delete('/api/books/123e4567-e89b-12d3-a456-426614174000')
    assert delete_response.status_code == 200

    # negative scenario
    check_response = client.get('/api/books/123e4567-e89b-12d3-a456-426614174000')
    assert check_response.status_code == 404