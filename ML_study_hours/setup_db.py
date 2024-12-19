import sqlite3

connection = sqlite3.connect('study_data.db')

cursor = connection.cursor()

print("Connected to SQlite database!")


#creating a table for study hours
cursor.execute('''
CREATE TABLE IF NOT EXISTS study_hours (
    id INTEGER PRIMARY KEY,
    week INTEGER,
    day TEXT,
    hours INTEGER
);
''')

#save changes and close connection
connection.commit()
connection.close()

print("Table created and database connection closed!")