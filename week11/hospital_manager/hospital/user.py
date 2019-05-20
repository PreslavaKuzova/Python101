import sys
from utils.hospital_errors import *
from database_layer.database import *

class User:
    db = Database()
    def __init__(self, username, password, status = None, full_name = None):
        self.username = username
        self.password = password
        self._status = status
        self.full_name = full_name

    @classmethod
    def find(cls, username, password = None):

        result = cls.db.find_user(username, password)
        if result:
            return cls(username, password, result[3], result[4])
    
    @classmethod
    def create_new_user(cls, username, hashed_pass, title, full_name):
        cls.db.create_new_user(username, hashed_pass, title, full_name)
        return cls(username, hashed_pass, title, full_name)

    @classmethod
    def delete_user(cls, username):
        cls.db.delete_user_by_username(username)

    @property
    def status(self):
        return self._status

class Patient:
    db = Database()
    def __init__(self, condition, age):
        self.condition = condition
        self.age = age

    @classmethod
    def create_new_patient(cls, username, condition, age):
        cls.db.create_new_patient(username, condition, age)
        return cls(condition, age)

class Doctor:
    db = Database()
    def __init__(self, position):
        self.position = position

    @classmethod
    def create_new_doctor(cls, username, position):
        cls.db.create_new_patient(username, position)
        return cls(position)