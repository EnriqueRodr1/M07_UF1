import conection

def read_users():

    conection = conection.connect_db
    cursor = conection.cursor()

    sql_read_users = "SELECT * FROM users"

    cursor.execute(sql_read_users)

    users = cursor.fetchall()


    return users
