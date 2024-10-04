# Library Management

## Description
<div style="text-align: justify;">
This project is a Library Management System built with Python, Flask and MariaDB. The project follows SOLID principles to ensure maintainability and scalability. Key design patterns implemented include separating logic into Repositories, Routes, Services (business logic), Models, and Schemas. This separation enables cleaner code, better unit testing, and easier updates.
</div>

## Requirements
- Python 3.12 or higher
- Flask ver. 3
- MariaDB ver. 10.3 or higher
- Virtual environment or pipenv

## Installation
Follow these steps to set up the project on your local machine:

1. Clone the Repository
```bash
  git clone https://github.com/erwienwijaya/library-management.git
  cd library-management
```
2. Set Up Virtual Environment
```bash
    # for Linux/MacOS
    python3.12 -m venv venv
    source venv/bin/activate
    
    #for windows
    python3 -m venv venv
    venv\Scripts\activate
```
3. Install Dependencies
```bash
   pip install -r requirements.txt 
```
4. Duplicated File .env-sample Change to .env
```bash
# Update the database configuration in the project’s environment variables
DATABASE_URL_DEV=mysql://user:password@host:3306/dbname
DATABASE_URL_TEST=mysql://user:password@host:3306/dbname
SECRET_KEY=ini-rahasia-kita
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
```
5. Configure MariaDB Database (ensure your MariaDb already installed and running)
```bash
    # create db for development
    CREATE DATABASE library_db
    
    # create db for testing
    CREATE DATABASE library_test
```
6. Run Database Migrations 
```bash
    flask db init
    flask db migrate -m "first migrate"
    flask db upgrade 
```
7. Seed Initial Data (Optional)
```bash
    # if you had issues check with flask --help
    flask seed_data  
```

## How to Run
To start the application for the first time, follow these steps:
1. Activate the virtual environment (if not already activated):
```bash
  # for Linux/MacOS
  source venv/bin/activate
    
  #for windows
  venv\Scripts\activate
```
2. Start the Flask development server:
```bash
    flask run
```

## Accessing Endpoints
You can access the API endpoints via a REST client like Postman or cURL.

### Author:
#### Get All Author
```http request
GET /api/authors
```
#### Get Author By Author_id
```http request
GET /api/authors/${author_id}
```
#### Add New Author
```http request
POST /api/authors
```
#### Update an Author
```http request
PUT /api/authors/${author_id}
```
#### Delete an Author
```http request
DELETE /api/authors/${author_id}
```

### Book:
#### Get All Book
```http request
GET /api/books
```
#### Get Book By Book_id
```http request
GET /api/books/${book_id}
```
#### Get Book By author_id
```http request
GET /api/authors/${author_id}/books
```
#### Add New Book
```http request
POST /api/books
```
#### Update a Book
```http request
PUT /api/books/${book_id}
```
#### Delete a Book
```http request
DELETE /api/books/${book_id}
```

## Example cURL Command:
```bash
    curl -X GET http://127.0.0.1:5000/api/books
```
## Running Unit Test
To run unit tests, execute the following command from the project root directory:
```bash
    # for Linux/MacOS
    PYTHONPATH=./ pytest -v
```
This will automatically discover and run all unit tests defined under the tests/ directory.

## Author
- [@erwienwijaya](https://www.github.com/erwienwijaya)