import sqlite3
from utils.hospital_errors import *
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
            VALUES ({', '.join([f"'{value}'" for value in values])});
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
            WHERE {where_str};
        """

        cursor.execute(query)

        connection.commit()
        connection.close()

    def delete(self, database, **criteria):
        connection = sqlite3.connect(database.db_name)
        cursor = connection.cursor()
        
        where_str = " AND ".join([f"{key} LIKE '%{value}%'" for key, value in criteria.items()])

        query = f""" 
            DELETE FROM {self.table_name}
            WHERE {where_str};
        """

        cursor.execute(query)

        connection.commit()
        connection.close()

class Database:
    def __init__(self):
        self.db_name = "hospital.db"
        self.tables = []
        self._database_initialization()

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

    def _database_initialization(self):
        user = Table('User', 
            [   
                Column('username', 'text', True), 
                Column('password', 'text'),
                Column('title', 'text'),
                Column('full_name', 'text')     
            ]
        )

        doctor = Table('Doctor', 
            [
                Column('id_doctor', 'integer', True),
                Column('position', 'text'),
                Column(foreign_key = 'id_doctor', references = 'User', reference_col = 'id')

            ]
        )

        patient = Table('Patient', 
            [
                Column('id_patient', 'integer', True),
                Column('condition', 'text'),
                Column('age', 'integer'),
                Column(foreign_key = 'id_patient', references = 'User', reference_col = 'id')
            ]
        )

        slots = Table('Slots', 
            [
                Column('doctor_id', 'integer'),
                Column('start_hour', 'text'),
                Column('end_hour', 'text'),
                Column('date', 'text'),
                Column('status', 'text'),
                Column('room', 'text'),
                Column(foreign_key = 'id', references = 'Doctor', reference_col = 'id')
            ]
        )

        reserved_slots = Table('Reserved_slots', 
            [
                Column('id_patient', 'integer'),
                Column('id_slot', 'integer'),
                Column('status', 'text'),
                Column(foreign_key = 'id_patient', references = 'Patient', reference_col = 'base_id'),
                Column(foreign_key = 'id_slot', references = 'Slots', reference_col = 'id')
            ]
        )

        self.create_table(user)
        self.create_table(doctor)
        self.create_table(patient)
        self.create_table(slots)
        self.create_table(reserved_slots)

    def find_user(self, username, password):
        user_table = self.return_table_by_name("User")
        if password:
            return user_table.fetch_particular_data(self, False, "*", username = username, password = password)
        else:
            return user_table.fetch_particular_data(self, False, "*", username = username)

    def create_new_user(self, username, password, title, full_name):
        user_table = self.return_table_by_name("User")
        user_table.insert(self, username, password, title, full_name)

    def create_new_patient(self, username, condition, age):
        user_table = self.return_table_by_name("User")
        id = user_table.fetch_particular_data(self, False, "id", username = username)[0]
        patient_table = self.return_table_by_name("Patient")
        patient_table.insert(self, id, condition, age)

    def create_new_doctor(self, username, position):
        user_table = self.return_table_by_name("User")
        id = user_table.fetch_particular_data(self, False, "id", username = username)[0]
        doctor_table = self.return_table_by_name("Doctor")
        doctor_table.insert(self, id, position)

    def delete_user_by_username(self, username):
        user_table = self.return_table_by_name("User")
        user_table.delete(self, username = username)