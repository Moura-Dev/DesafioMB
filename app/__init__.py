from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from logging import FileHandler, WARNING

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    file_handler = FileHandler("errorlog.txt")
    file_handler.setLevel(WARNING)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://moura:itnisan19@localhost/api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes import main

    app.register_blueprint(main)
    app.logger.addHandler(file_handler)

    return app


if __name__ == "__main__":
    create_app()
