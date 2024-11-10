from connection import connect

def delete_product(id):
    conn = connect()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Product deleted successfully.")
