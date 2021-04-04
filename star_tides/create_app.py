from flask import Flask
from star_tides.services.sql.database import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'

    # from star_tides.services.sql.database.models import models
    db.init_app(app)

    from star_tides.services.sql.database.models.UserModel import UserModel

    @app.route('/')
    def foo():
        user = UserModel(
            first_name = "Evan",
            last_name = "K",
            email="foo"
        )

        db.session.add(user)
        db.session.commit()

        return str(user.id)

    return app


