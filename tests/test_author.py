import pytest
from flask.testing import FlaskClient
from app import create_app, db
from app.models import Author

@pytest.fixture
def client():
    app = create_app('config.TestingConfig')

    # create test client
    testing_client: FlaskClient
    with app.test_client() as client:
        with app.app_context():
            # create the database and tables testing
            db.create_all()

            author = Author(id="e5a47420-5dbc-491d-9a3d-7ae76d1c92e7",
                            name="Donny Dhirgantoro",
                            bio="Test bio",
                            birth_date="1978-10-27")
            db.session.add(author)
            db.session.commit()

            # seed the database with initial test data
            yield client

            # drop all tables after test
            db.session.remove()
            db.drop_all()


def test_get_all_authors(client):
    response = client.get('/api/authors')
    assert response.status_code == 200
    assert response.json[0]['name'] == 'Donny Dhirgantoro'


def test_create_author(client):
    response = client.post('/api/authors', json={'name': 'Test Author', 'bio': 'Test bio', 'birth_date': '1980-10-15'})
    assert response.status_code == 201
    assert response.json['name'] == 'Test Author'


def test_get_author_by_id(client):
    response = client.get('/api/authors/e5a47420-5dbc-491d-9a3d-7ae76d1c92e7')
    assert response.status_code == 200
    assert response.json['name'] == 'Donny Dhirgantoro'


def test_no_author_by_id(client):
    response = client.get('/api/authors/e5a47420-5dbc-491d-9a3d-7ae76d1c92e8')
    assert response.status_code == 404


def test_update_author(client):
    # create author
    create_response = client.post('/api/authors',
                                  json={'name': 'Test Author', 'bio': 'Test bio', 'birth_date': '1980-10-15'})
    author_id = create_response.json['id']

    # Update created author
    update_response = client.put(f'/api/authors/{author_id}', json={'name': 'Updated Author'})
    assert update_response.status_code == 200
    assert update_response.json['name'] == 'Updated Author'


def test_delete_author(client):
    # create author
    create_response = client.post('/api/authors',
                                  json={'name': 'Test Author', 'bio': 'Test bio', 'birth_date': '1985-05-05'})
    author_id = create_response.json['id']

    # Delete created author
    delete_response = client.delete(f'/api/authors/{author_id}')
    assert delete_response.status_code == 200

    # negative scenario
    check_response = client.get(f'/api/authors/{author_id}')
    assert check_response.status_code == 404