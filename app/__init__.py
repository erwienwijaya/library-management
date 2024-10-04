from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

db = SQLAlchemy()

def create_app(config_class):
    pymysql.install_as_MySQLdb()

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    Migrate(app, db)

    from .routes.author_routes import author_bp
    app.register_blueprint(author_bp, url_prefix='/api')

    from .routes.book_routes import book_bp
    app.register_blueprint(book_bp, url_prefix='/api')

    return app