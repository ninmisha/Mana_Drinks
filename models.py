from flask_login import UserMixin
from bson.objectid import ObjectId

class User(UserMixin):
    def __init__(self, user_data):
        self.user_data = user_data

    def get_id(self):
        return str(self.user_data.get('_id'))

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def email(self):
        return self.user_data.get('email')

    @property
    def name(self):
        return self.user_data.get('name') 