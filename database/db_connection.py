import mysql.connector


def create_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="lavanya@19",
        database="smart_data_analytics"
    )

    return connection