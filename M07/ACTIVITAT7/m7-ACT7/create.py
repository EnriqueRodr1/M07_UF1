from connection import connect

def create_product(name, description, price, quantity):
    conn = connect()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO products (name, description, price, quantity)
        VALUES (%s, %s, %s, %s)
        """, (name, description, price, quantity))
        conn.commit()
        cursor.close()
        conn.close()
        print("Product created successfully.")
