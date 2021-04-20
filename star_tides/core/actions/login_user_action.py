from star_tides.core.actions.base_action import Action
from star_tides.services.mongo.models.UserModel import User
import bcrypt


class LoginUserAction(Action):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def run(self):
        password = self.password.encode('utf-8')
        user = User.objects(email=self.username).first()

        if bcrypt.checkpw(password, user.password):
            return True
        return False

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


