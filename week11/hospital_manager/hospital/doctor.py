from utils.hospital_errors import *
from database_layer.database import *

class Doctor:

    db = Database()
    def __init__(self, position):
        self.position = position

    @classmethod
    def create_new_doctor(cls, username, position):
        cls.db.create_new_doctor(username, position)
        return cls(position)
    