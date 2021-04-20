from flask import Flask, render_template
from star_tides.services.sql.database import db
from mongoengine import connect
from celery import Celery
from star_tides.api.blueprint import bp
from star_tides.api.routes.auth_route import auth
from star_tides.config.settings import REDIS_URL
import os

def create_celery_app(app=None):

    app = app or create_app()

    celery = Celery(app.import_name, broker=REDIS_URL, backend=REDIS_URL, include=['star_tides.core.tasks'])

    return celery


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('star_tides.config.settings')

    from star_tides.services.sql.database.models import ALL_MODELS
    db.init_app(app)

    connect(
        username='evan',
        password='password',
        host='mongodb://mongodb_container:27017/star_tides?authSource=star_tides'
    )

    @app.route('/')
    def index():
        return render_template('index.html')

    app.register_blueprint(bp)
    app.register_blueprint(auth)

    return app


celery_app = create_celery_app()
