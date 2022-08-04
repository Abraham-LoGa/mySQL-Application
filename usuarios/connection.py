import mysql.connector

def do_connection():
    database=mysql.connector.connect(
        host='localhost',
        user='root',
        password = '',
        database='data_project',
        port=3306
    )

    cursor = database.cursor(buffered=True)

    return [database,cursor]
