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

    def fetch_all_data(self, cursor, *data, **criteria):
        column_names_str = self.column_names_str()

        query = f"""
        SELECT {column_names_str} FROM {self.table_name}
        """
        cursor.execute(query)
        return cursor.fetchall()

    def fetch_particular_data(self, database, all, *data, **criteria):
            connection = sqlite3.connect(database.db_name)
            cursor = connection.cursor()   

            criteria_str = " AND ".join([f"{key} LIKE '%{value}%'" for key, value in criteria.items()])
            data_str = ', '.join([data for data in data])

            if criteria == {}:
                query = f"""
                    SELECT {data_str} 
                    FROM {self.table_name};
                """
            else:
                query = f"""
                    SELECT {data_str} 
                    FROM {self.table_name}
                    WHERE {criteria_str};
                """

            cursor.execute(query)

            if all:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()

            connection.close()
            return result
    
    def fetch_particular_data_join(self, database, table, all, *data, **criteria):
        connection = sqlite3.connect(database.db_name)
        cursor = connection.cursor()   
        
        criteria_str = f"{next(iter(criteria))} = {next(iter(criteria.values()))}"
        criteria.pop(next(iter(criteria)))

        where_str = " AND ".join([f"{key} LIKE '%{value}%'" for key, value in criteria.items()])
        data_str = ', '.join([data for data in data])

        query = f"""
            SELECT {data_str} 
            FROM {self.table_name}
            JOIN {table.table_name}
            ON {criteria_str}
            WHERE {where_str};
        """
        cursor.execute(query)

        if all:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()

        connection.close()
        
        return result
        
    def insert(self, database, *values):
        connection = sqlite3.connect(database.db_name)
        cursor = connection.cursor()
        
        query = f""" 
            INSERT INTO {self.table_name} ({self.column_names_str()})
            VALUES ({', '.join([f"'{value}'" for value in values])})
        """

        cursor.execute(query)

        connection.commit()
        connection.close()

    def update(self, database, **criteria):
        connection = sqlite3.connect(database.db_name)
        cursor = connection.cursor()
        
        values_str = f"{next(iter(criteria))} = {next(iter(criteria.values()))}"
        criteria.pop(next(iter(criteria)))

        where_str = " AND ".join([f"{key} LIKE '%{value}%'" for key, value in criteria.items()])

        query = f""" 
            UPDATE {self.table_name} 
            SET {values_str}
            WHERE {where_str}
        """

        cursor.execute(query)

        connection.commit()
        connection.close()

class Database:
    def __init__(self, db_name,):
        self.db_name = db_name
        self.tables = []

    def create_table(self, table):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        table.create(cursor)
        self.tables.append(table)

        connection.commit()
        connection.close()

    def fetch_all_from_table(self, table):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        result = table.fetch_all(cursor)

        connection.commit()
        connection.close()

        return result

    def return_table_by_name(self, name):
        for table in self.tables:
            if table.table_name == name:
                return table

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

def login(database):
    
    connection = sqlite3.connect(database.db_name)
    cursor = connection.cursor()

    print("Hello!")
    username = input("Provide username: ")

    #those are the tables we need in the login
    base_user = database.return_table_by_name('BaseUser')
    client = database.return_table_by_name('Client')
    mechanic = database.return_table_by_name('Mechanic')

    #we check for the existence of a user with such username
    result = base_user.fetch_particular_data(database, False, '*', user_name = username)
    
    if result == None:
        print("Unknown user!\nWould you like to create a new user?")
        
        while(True):
            response = input("Answer y/n: ")
            
            if response in ['yes', 'y']:
                occupation = input("Are you a client or a mechanic? ")
                email = input("Provide email address: ")
                phone_number = input("Provide phone number: ")
                address = input("Provide address: ")
                
                #inserting the data in BaseUser
                base_user.insert(database, username, email, phone_number, address)

                #as we need to connect two tables, we need to fetch the id from BaseUser
                id_to_connect = base_user.fetch_particular_data(database, False, 'id', user_name = username)

                if occupation == "mechanic":
                    title = input("Provide title: ")
                    mechanic.insert(database, id_to_connect[0], title)
                else:
                    client.insert(database, id_to_connect[0])

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

    #tables that are in the database
    vehicle = database.return_table_by_name('Vehicle')
    client = database.return_table_by_name('Client')
    base_user = database.return_table_by_name('BaseUser')
    repair_hour = database.return_table_by_name('RepairHour')

    user = login(database)
    if(user):
        
        client_id = client.fetch_particular_data_join(database, base_user, False, 
        'Client.id', base_id = 'BaseUser.id', user_name = user)[0][0]
        
        print_menu()
        choice = int(input("Choose an option: "))
        
        while(choice):
            if choice == 1:    
                t = PrettyTable(['id', 'Date', 'Hour'])
                for row in repair_hour.fetch_particular_data(database, True, 'id', 'date', 'start_hour'):
                    t.add_row(row)
                print(t)

            elif choice == 2:
                date = input("Insert a date: ")
                t = PrettyTable(['id', 'Date', 'Hour'])
                for row in repair_hour.fetch_particular_data(database, True, 'id', 'date', 'start_hour', date = date):
                    t.add_row(row)
                print(t)

            elif choice == 3:
                print("List of your vehicles: ")
                t = PrettyTable(['id', 'Make', 'Model', 'Register number'])
                
                for row in vehicle.fetch_particular_data(database, True, 'id', 'make', 'model', 'register_number', 
                owner = client_id):
                    t.add_row(row)
                print(t)

                vehicle = input("Please select the id of the vehicle you want to repair: ")
                hour = input("Please select the id of the repair hour you want to save: ")

                repair_hour.update(database, vehicle = vehicle, id = hour)
            
            elif choice == 4:
                # coming soon
                pass
            elif choice == 5:
                # coming soon
                pass
            elif choice == 6:

                category = input("Vehicle category: ")
                make = input("Vehicle make: ")
                model = input("Vehicle model: ")
                register_number = input("Vehicle register number: ")
                gear_box = input("Vehicle gear_box: ")
                
                vehicle.insert(database, category, make, model, register_number, gear_box, client_id[0])

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
