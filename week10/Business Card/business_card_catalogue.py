import sqlite3

def create_user_table():
    connection = sqlite3.connect('business_users.db') #will create a table if it doesnt exist
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS User 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            full_name varchar(255),
            email varchar(255),
            age int NOT NULL,
            phone varchar(255) NOT NULL,
            additional_info TEXT,
            UNIQUE (full_name, email))  
        """
    )
    connection.commit()
    connection.close()

def insert_user():
    connection = sqlite3.connect('business_users.db')
    cursor = connection.cursor()
    
    name = input("Enter full unique name: ")
    email = input("Enter unique email: ")
    age = input("Enter user's age: ")
    phone = input("Enter user's phone: ")
    additional_info = input("Enter additional info: ")

    cursor.execute(
        """
        INSERT INTO User
            (full_name, email, age, phone, additional_info)
            VALUES ('{full_name}', '{email}', '{age}', '{phone}', '{additional_info}') 
        """.format(full_name = name, email = email, age = age, phone = phone, additional_info = additional_info)
    )
    
    connection.commit()
    connection.close()

def list_users():
    connection = sqlite3.connect('business_users.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM User")
    
    users = cursor.fetchall()

    connection.commit()
    connection.close()

    print('''
            ##############
            ###Contacts###
            ##############''')
    for user in users:
        print('1.ID:', user[0], 'Email:', user[2], 'Full name:', user[1])

def print_user_information(user_list):
    print('''
            Contact info:
            ###############
            ID: {id}
            Full name: {full_name}
            Email: {email}
            Age: {age}
            Phone: {phone}
            Additional info: {additional_info}
            ###############
    '''.format(id = user_list[0], full_name = user_list[1], email = user_list[2], age = user_list[3],
    phone = user_list[4], additional_info = user_list[5]))
    
def get_user_infomation():
    connection = sqlite3.connect('business_users.db')
    cursor = connection.cursor()
    
    full_name = input("Enter the name of the user you want to get the information about: ")

    cursor.execute(
        """
        SELECT * 
        FROM User
        WHERE full_name LIKE '{full_name}'
    
    """.format(full_name = full_name)
    )

    print_user_information(cursor.fetchone())

    connection.commit()
    connection.close()

def delete_user():
    connection = sqlite3.connect('business_users.db')
    cursor = connection.cursor()
    
    name = input("Enter the name of the user you want to delete: ")

    cursor.execute(
        """
        DELETE FROM User
        WHERE full_name = '{full_name}'
    """.format(full_name = name))

    connection.commit()
    connection.close()

    print('The contact is deleted successfully')

def help():
    print('''
                        #############
                        ###Options###
                        #############

    1. `add` - insert new business card
    2. `list` - list all business cards
    3. `delete` - delete a certain business card (`ID` is required)
    4. `get` - display full information for a certain business card (`ID` is required)
    5. `help` - list all available options
    0. `exit` - to stop the execution of the program
    
    ''')

def main():
    help()
    i = input("    Press the number of the command you want to execute: ")
    while(i != '0'):
        if i == '1':
            insert_user()
        if i == '2':
            list_users()
        if i == '3':
            delete_user()
        if i == '4':
            get_user_infomation()
        if i == '5':
            help()
        i = input("    Press the number of the command you want to execute: ")

if __name__ == "__main__":
    main()