from flask import Blueprint
from star_tides.api.controllers.auth_controller import LoginController, CreateUserController


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=["POST"])
def login():
    response = LoginController().execute()
    return str(response)

@auth.route('/new/user', methods=["POST"])
def create_user():
    response = CreateUserController().execute()
    return response


