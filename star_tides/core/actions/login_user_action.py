from star_tides.core.actions.base_action import Action
from star_tides.services.mongo.models.UserModel import User
from star_tides.api.util.issue_jwt import create_jwt
import bcrypt
import time

from google.oauth2 import id_token
from google.auth.transport import requests
from flask import current_app


class LoginUserAction(Action):
    def __init__(self, username=None, password=None, token=None):
        self.username = username
        self.password = password
        self.token = token

    def run(self):
        now = int(time.time())
        if self.username and self.password:

            password = self.password.encode('utf-8')
            user = User.objects(email=self.username).first()

            if user is None:
                raise print(f"{self.__class__.__name__} User not found")

            if bcrypt.checkpw(password, user.password):
                return create_jwt(user.email)
            print(f"{self.__class__.__name__} Password not a match")
        elif self.token:
            idinfo = id_token.verify_oauth2_token(self.token, requests.Request(), current_app.config['CLIENT_ID'])
            # If the profile claims fields are in the token returned then nothing else is needed,
            # Otherwise


class CreateUserAction(Action):
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def run(self):
        salt = bcrypt.gensalt()
        self.password = self.password.encode('utf-8')

        hash = bcrypt.hashpw(self.password, salt)

        user = User(first_name=self.first_name, last_name=self.last_name, email=self.email, password=hash)
        user.save()

        return True


