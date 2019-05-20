class UserAlreadyExistsError(Exception):
    #raised them the user already exists
    pass

class DatabaseConnectionError(Exception):
    #raised when there is a problem with the database
    pass

class PasswordsDontMatchError(Exception):
    #raised when passwords do not match
    pass

class InvalidPasswordError(Exception):
    #raised when the password is not at least 8 charactes long, 
    #does not contain a special character, an uppercase or a number
    pass