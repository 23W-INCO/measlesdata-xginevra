import json
import sqlite3
from fhir.resources.bundle import Bundle
import pathlib


class JsonInDatabaseTranformer:
    def __init__(self):
        pass

    def create_table(self, cursor):
        # Drop the table if it exists
        cursor.execute('DROP TABLE IF EXISTS measles_data;')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS measles_data(
                id INTEGER PRIMARY KEY,
                location TEXT,
                population INT,
                cases INT,
                vaccination_rate DECIMAL,
                cases_100000 DECIMAL
            );
        ''')

    def insert_data(self, cursor, location, data):
        location = location.split("/")[1]
        population = int(data['Population'])
        cases = int(data['Measles Cases'])
        if "Vaccination Rate" in data:
            vacation_r = float(data['Vaccination Rate'])
        else:
            vacation_r = "N.A"
        if 'Per 100,000' in data:
            cases_100000 = float(data['Per 100,000'])
        else:
            cases_100000 = "N.A"
        cursor.execute('''
            INSERT INTO measles_data (location, population, cases, vaccination_rate, cases_100000)
            VALUES (?, ?, ?, ?, ?);
        ''', (location, population, cases, vacation_r, cases_100000))

    def push_json_data_in_db(self, json_path):
        database_file = 'data_for_web_application.db'

        # Connect to the SQLite database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # # Create the table if it doesn't exist, not needed
        # self.create_table(cursor)

        # Insert data into the table
        # Read data from the JSON file
        filename = pathlib.Path(json_path)
        pat = Bundle.parse_file(filename)
        for obs in pat.entry:
            location = obs.resource.subject.reference
            data_dict = {}
            for compons in obs.resource.component:
                data_dict[compons.code.text] = compons.valueQuantity.value

            self.insert_data(cursor, location, data_dict)

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

    def push_json_data_in_fresh_db(self, json_path):
        database_file = 'data_for_web_application.db'

        # Connect to the SQLite database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # Create the table if it doesn't exist
        self.create_table(cursor)

        # Insert data into the table
        # Read data from the JSON file
        filename = pathlib.Path(json_path)
        pat = Bundle.parse_file(filename)
        for obs in pat.entry:
            location = obs.resource.subject.reference
            data_dict = {}
            for compons in obs.resource.component:
                data_dict[compons.code.text] = compons.valueQuantity.value

            self.insert_data(cursor, location, data_dict)

        # Commit the changes and close the connection
        connection.commit()
        connection.close()


if __name__ == "__main__":
    json_in_db = JsonInDatabaseTranformer()
    json_in_db.push_json_data_in_db()
