from flask import Blueprint
from star_tides.services.sql.database.models.UserModel import UserModel
from star_tides.services.mongo.models.UserModel import User
from star_tides.services.sql.database import db
from celery.result import AsyncResult
bp = Blueprint('bp', __name__)

# @bp.route('/<task_id>')
# def get_task(task_id):
#     from star_tides.create_app import create_celery_app
#     app = create_celery_app()
#     return (str(app.tasks))
    #
    #
    # res = AsyncResult(id=task_id, app=app)
    # return str(res.status)

@bp.route('/foo')
def index():

    from star_tides.core.tasks.test_action import add_numbers

    user = UserModel(
        first_name="Evan",
        last_name="K",
        email="foo@barbas.com"
    )
    #
    mdb_user = User(first_name="Foobar", last_name="Shabam", email="shmoili@tabouli.com")
    mdb_user.save()
    db.session.add(user)
    db.session.commit()

    result = add_numbers.delay(10, 10)


    return str(f"Postgres user: {user.id}\nMongo User: {mdb_user.email}. Your task id is {result.task_id}")
