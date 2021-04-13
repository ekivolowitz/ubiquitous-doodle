from flask import Flask
from star_tides.services.sql.database import db
from mongoengine import connect, Document, StringField
from star_tides.services.mongo.models.UserModel import User


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
    # app.config['MONGODB_SETTINGS'] = {
    #     "db" : "star_tides",
    #     "host" : "mongodb://mongodb_container",
    #     "port" : 27017,
    #     "username" : " evan",
    #     "password" : "password",
    #     "authentication_source" : "star_tides"
    # }

    from star_tides.services.sql.database.models import ALL_MODELS
    db.init_app(app)

    connect(
        username='evan',
        password='password',
        host='mongodb://mongodb_container:27017/star_tides?authSource=star_tides'
    )

    from star_tides.services.sql.database.models.UserModel import UserModel

    @app.route('/')
    def foo():
        user = UserModel(
            first_name = "Evan",
            last_name = "K",
            email="foo@barbas.com"
        )
        #
        mdb_user = User(first_name="Foobar", last_name="Shabam", email="shmoili@tabouli.com")
        mdb_user.save()
        db.session.add(user)
        db.session.commit()

        return str(f"Postgres user: {user.id}\nMongo User: {mdb_user.email}")
        # numShmoilis = 0
        # for user in User.objects:
        #     if user.first_name == "Foobar":
        #         numShmoilis += 1
        # return f"There are {numShmoilis} Foobar Shabams"
    return app


