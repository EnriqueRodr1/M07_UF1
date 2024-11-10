from connection import connect

def read_products():
    conn = connect()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
