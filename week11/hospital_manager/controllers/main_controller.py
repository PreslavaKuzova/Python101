import os
import hashlib
import binascii
from hospital.user import *
from hospital.patient import *
from hospital.doctor import *
from utils.hospital_errors import *

class MainController:

    @classmethod
    def sign_in(cls, username, password):
        if cls._validate_password(password):
            result = User.find_password(username)
            
            if result:
                hashed_password = result[0]
                if(cls._do_passwords_match(hashed_password, password)):

                    current_user = User.find(username, hashed_password)
                    return current_user
            else:
                raise DatabaseConnectionError
        else:
            raise InvalidPasswordError

    @classmethod
    def sign_up(cls, username, password, validation_password, title, full_name):
        if(cls._validate_password(password) and cls._validate_password(validation_password)):
            
            hashed_pass = cls._hash_password(password)

            if cls._do_passwords_match(hashed_pass, validation_password):
                if User.find(username):
                    raise UserAlreadyExistsError

                return User.create_new_user(username, hashed_pass, title, full_name)
            
            else:
                raise PasswordsDontMatchError
        else:
            raise InvalidPasswordError

    @classmethod
    def connect_tables(cls, table, username, user_info):
        if table == "patient":
            return Patient.create_new_patient(username, **user_info)
        else: 
            return Doctor.create_new_doctor(username, **user_info)

    @classmethod
    def show_members(cls, current_user):
        if current_user.is_doctor:
            return cls.show_patients(current_user)
            #  [Patient('Roza'), Patient('Mimi')]
        else:
            return cls.show_doctors(current_user)

    @staticmethod
    def _hash_password(password):
        #here we are hashing our password using salt
        
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def _do_passwords_match(password, validation):
        salt = password[:64]
        password = password[64:]
        
        pwdhash = hashlib.pbkdf2_hmac('sha512', validation.encode('utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        
        return pwdhash == password

    @staticmethod
    def _validate_password(password):
        # we want to validate that the password contains at leats one uppercase letter,
        # one number and one special symbol
        
        special_character = '[@_!#$%^&*()<>?/\|}{~:]'
        rules = [lambda s: any(x.isupper() for x in s), # must have at least one uppercase
                lambda s: any(x.islower() for x in s),  # must have at least one lowercase
                lambda s: any(x.isdigit() for x in s),  # must have at least one digit
                lambda s: any(x in special_character for x in s),
                lambda s: len(s) >= 8                   # must be at least 8 characters long
            ]

        if all(rule(password) for rule in rules):
            return True

        return False