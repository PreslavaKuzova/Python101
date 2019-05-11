import sqlite3
from prettytable import PrettyTable

class Column:
    def __init__(self, column_name = '', column_type = '', unique = False, 
    foreign_key = None, references = None, reference_col = None):
        self.column_name = column_name
        self.column_type = column_type
        self.unique = unique
        self.foreign_key = foreign_key
        self.references = references
        self.reference_col = reference_col
       
    @property
    def unique_str(self):
        if self.unique:
            return 'UNIQUE'
        return ''

    def as_sql(self):
        return f"{self.column_name} {self.column_type} {self.unique_str}"

    def foreign_key_as_sql(self):
        return f"FOREIGN KEY ({self.foreign_key}) REFERENCES {self.references}({self.reference_col})"
            
class Table:
    def __init__(self, table_name, columns):
        self.table_name = table_name
        self.columns = columns

    def column_str(self):
        col_str = []

        for column in self.columns:
            if column.foreign_key != None:
                col_str.append(column.foreign_key_as_sql())
            else:
                col_str.append(column.as_sql())
        
        return ', '.join(col_str)

    def create(self, cursor):
        column_str = self.column_str()
        create_table = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name}
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {column_str}
                );
        """
        cursor.execute(create_table)

    def column_names(self):
        return [column.column_name for column in self.columns if column.column_name != '']

    def column_names_str(self):
        return ', '.join(self.column_names())

    def fetch_all(self, cursor):
        column_names_str = self.column_names_str()
        query = f"""
        SELECT {column_names_str} FROM {self.table_name}
        """
        cursor.execute(query)
        return cursor.fetchall()

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_table(self, table):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        table.create(cursor)

        connection.commit()
        connection.close()

    def fetch_all_from_table(self, table):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        result = table.fetch_all(cursor)

        connection.commit()
        connection.close()

        return result

def initialization(database):
    base_user = Table('BaseUser', 
        [   
            Column('user_name', 'text', True), 
            Column('email', 'text'),
            Column('phone_number', 'integer'), 
            Column('address', 'text')
        ]
    )

    client = Table('Client', 
        [
            Column('base_id', 'integer', True),
            Column(foreign_key = 'base_id', references = 'BaseUser', reference_col = 'id')

        ]
    )

    mechanic = Table('Mechanic', 
        [
            Column('base_id', 'integer', True),
            Column('title', 'text'),
            Column(foreign_key = 'base_id', references = 'BaseUser', reference_col = 'id')
        ]
    )

    service = Table('Service', 
        [
            Column('name', 'text')
        ]
    )

    vehicle = Table('Vehicle', 
        [
            Column('category', 'text'),
            Column('make', 'text'),
            Column('model', 'text'),
            Column('register_number', 'text'),
            Column('gear_box', 'text'),
            Column('owner', 'integer'),
            Column(foreign_key = 'owner', references = 'Client', reference_col = 'base_id')
        ]
    )

    mechanic_service = Table('MechanicService', 
        [
            Column('mechanic_id', 'integer', True),
            Column('service_id', 'integer', True), 
            Column(foreign_key = 'mechanic_id', references = 'Mechanic', reference_col = 'base_id'),
            Column(foreign_key = 'service_id', references = 'Service', reference_col = 'id')

        ]
    )

    repair_hour = Table('RepairHour', 
        [
            Column('date', 'text'),
            Column('start_hour', 'text'),
            Column('vehicle', 'text'),
            Column('bill', 'real'),
            Column('mechanic_service', 'text'),
            Column(foreign_key = 'vehicle', references = 'Vehicle', reference_col = 'id'),
            Column(foreign_key = 'mechanic_service', references = 'MechanicService', reference_col = 'id')
        ]    
    )

    database.create_table(base_user)
    database.create_table(client)
    database.create_table(mechanic)
    database.create_table(service)
    database.create_table(mechanic_service)
    database.create_table(vehicle)
    database.create_table(repair_hour)

def insert_base_user(database, username, email, phone, address):
    connection = sqlite3.connect(database.db_name)
    cursor = connection.cursor()
    
    cursor.execute(
        """
            INSERT INTO BaseUser (user_name, email, phone_number, address)
            VALUES ('{user_name}', '{email}', '{phone_number}', '{address}')
        """.format(user_name = username, email = email, phone_number = phone, address = address)
    )

    connection.commit()
    connection.close()

def base_user_existence(database, username):
    connection = sqlite3.connect(database.db_name)
    cursor = connection.cursor()

    cursor.execute(
        """
            SELECT * 
            FROM BaseUser
            WHERE user_name LIKE '{name}'
        """.format(name = username)
    )

    result = cursor.fetchone()

    connection.close()
    return True if result != None else False

def get_id_from_table(database, table_name, username):
    connection = sqlite3.connect(database.db_name)
    cursor = connection.cursor()

    cursor.execute(
        """
            SELECT id 
            FROM '{table_name}'
            WHERE user_name LIKE '{name}'
        """.format(table_name = table_name, name = username)
    )

    result = cursor.fetchone()

    connection.close()
    return int(result[0])

def connect_base_user_with_client_or_mechanic(database, username, title = None):
    connection = sqlite3.connect(database.db_name)
    cursor = connection.cursor()
    
    if title != None:
        cursor.execute(
            """
                INSERT INTO Mechanic (base_id, title)
                VALUES ('{base_id}', '{title}')
            """.format(base_id = get_id_from_table(database,'BaseUser', username), title = title)
        )
    else:
        cursor.execute(
            """
                INSERT INTO Client (base_id)
                VALUES ('{base_id}')
            """.format(base_id = get_id_from_table(database, 'BaseUser', username))
        )

    connection.commit()
    connection.close()

def list_all_free_hours(database, date = None):
    connection = sqlite3.connect(database.db_name)
    cursor = connection.cursor()

    if date != None:
        cursor.execute(
            """
                SELECT id, date, start_hour 
                FROM RepairHour
                WHERE date LIKE '%{date}%';
            """.format(date = date)
        )
    else:
        cursor.execute(
            """
                SELECT id, date, start_hour 
                FROM RepairHour;
            """
        )

    result = cursor.fetchall()

    connection.close()
    return result

def add_vehicle(database, username):
    connection = sqlite3.connect(database.db_name)
    cursor = connection.cursor()

    cursor.execute(
        """
            SELECT Client.id 
            FROM Client
            JOIN BaseUser
            ON Client.base_id = BaseUser.id 
            WHERE user_name = '{username}';
        """.format(username = username)
    )

    owner_id = int(cursor.fetchone()[0])

    category = input("Vehicle category: ")
    make = input("Vehicle make: ")
    model = input("Vehicle model: ")
    register_number = input("Vehicle register number: ")
    gear_box = input("Vehicle gear_box: ")
    
    cursor.execute(
        """
            INSERT INTO Vehicle (category, make, model, register_number, gear_box, owner)
            VALUES ('{category}', '{make}', '{model}', '{register_number}', '{gear_box}', '{owner}');
        """.format(category = category, make = make, model = model, register_number = register_number, gear_box = gear_box, owner = owner_id)
    )
    
    connection.commit()
    connection.close()

def login(database):
    
    print("Hello!")
    username = input("Provide username: ")
    connection = sqlite3.connect(database.db_name)
    cursor = connection.cursor()

    result = base_user_existence(database, username)

    if not result:
        print("Unknown user!\nWould you like to create a new user?")
        
        while(True):
            response = input("Answer y/n: ")
            
            if response in ['yes', 'y']:
                
                occupation = input("Are you a client or a mechanic? ")
                email = input("Provide email address: ")
                phone_number = input("Provide phone number: ")
                address = input("Provide address: ")
                
                insert_base_user(database, username, email, phone_number, address)

                if occupation == "mechanic":
                    title = input("Provide title: ")
                    connect_base_user_with_client_or_mechanic(database, username, title)
                else:
                    connect_base_user_with_client_or_mechanic(database, username)

                print(f"\nThank you, {username}!\nNext time you try to login, please use your username!")

                return username
            
            elif response in ['no', 'n']:
                return False
            else:
                print("Unknown response, please answear again.")
    else:
        return username

def print_menu():
    print("""
    You can choose from the following menu:
    1. List all free hours
    2. List free hours by date
    3. Save a repair hour
    4. Update repair hour by hour_id
    5. Delete repair hour by hour_id
    6. Add vehicle
    7. Update vehicle by vehicle_id
    8. Delete vehicle by vehicle_id
    9. Display all the options again
    0. Exit 
    """)
  
def main():
    database = Database('management.db')
    initialization(database)

    user = login(database)
    if(user):
        print_menu()
        choice = int(input("Choose an option: "))
        while(choice):
            if choice == 1:
                t = PrettyTable(['id', 'Date', 'Hour'])
                for hour in list_all_free_hours(database):
                    t.add_row(hour)
                print(t)
            elif choice == 2:
                date = input("Insert a date: ")
                t = PrettyTable(['id', 'Date', 'Hour'])
                for hour in list_all_free_hours(database, date):
                    t.add_row(hour)
                print(t)
            elif choice == 3:
                # coming soon
                pass
            elif choice == 4:
                # coming soon
                pass
            elif choice == 5:
                # coming soon
                pass
            elif choice == 6:
                add_vehicle(database, user)
            elif choice == 7:
                # coming soon
                pass
            elif choice == 8:
                # coming soon
                pass
            elif choice == 9:
                print_menu()
            else:
                print("Invalid input, try again!")
            
            choice = int(input("\nChoose an option: "))

if __name__ == '__main__':
    main()
