import sys
import getpass
from controllers.main_controller import MainController
from interface.main_menu import MainMenu
from utils.hospital_errors import *
from database_layer.database import *
from utils.hospital_constants import *

class StartMenu:

    db = Database()

    @classmethod
    def run(cls):
        print(HospitalConstants.start_menu_options)
        start_option = input("Option: ")

        if start_option == '1':
            
            # it is okay to actually make the sign in method to return true or false
            # we can make it return either the whole object, the title (doctor or patient) ot None
            
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            
            try:
                current_user = MainController.sign_in(username, password)
            except InvalidPasswordError:
                print("Password does not match criteria!")
                sys.exit(1)
            else:
                if current_user:
                    MainMenu.show_options(current_user)
                else:
                    print("Wrong username or password!")
                    sys.exit(1)

        elif start_option == '2':
            print("Are you a doctor or a patient?")
            title = input("Position: ")
            
            if title not in ["doctor", "patient"]:
                print("Unknown positon! Try again!")
                sys.exit(1)

            username = input("Username: ")
            full_name = input("Full name: ")
            password = getpass.getpass("Password: ")
            verification_password = getpass.getpass("Repeat password: ")

            try:
                user = MainController.sign_up(username, password, verification_password, title, full_name)
                
                user_info = {}
                if title == "doctor":
                    position = input("Enter your position: ")
                    user_info.update({"position" : position})

                elif title == "patient":
                    condition = input("Enter your condition: ")
                    age = input("Enter your age: ")
                    user_info.update({"condition" : condition, "age" : age})

                current_user = MainController.connect_tables(title, username, user_info)
            
            except UserAlreadyExistsError:
                print("Sign up failed! Username already taken!")
                sys.exit(1)
            except DatabaseConnectionError:
                print("Sign up failed! Try again!")
                sys.exit(1)
            except PasswordsDontMatchError:
                print("Sign up failed! Passwords don\'t match! ")
                sys.exit(1)
            except InvalidPasswordError:
                print("Passwords does not match criteria!")
                sys.exit(1)
            else:
                print("I am here", current_user.__dict__)
                MainMenu.show_options(title)
        
        else:
            sys.exit(1)