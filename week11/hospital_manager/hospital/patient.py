from utils.hospital_errors import *
from database_layer.database import *

class Patient:
    db = Database()
    def __init__(self, condition, age):
        self.condition = condition
        self.age = age

    @classmethod
    def create_new_patient(cls, username, condition, age):
        cls.db.create_new_patient(username, condition, age)
        return cls(condition, age)
