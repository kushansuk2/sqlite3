import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_insert_query = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (2, 'Mukul Kumar', 'mukul@gmail.com', '2020-10-01', 85000);"""
    cursor.execute(sqlite_insert_query)


    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while working with SQLite", error)
finally:
    if (sqliteConnection):
        print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
        sqliteConnection.close()
        print("sqlite connection is closed")
