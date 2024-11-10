import psycopg2

def connect():
    try:
        connection = psycopg2.connect(
            database="BBDDPostgres",
            user="enrique",
            password="Reyney15",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
