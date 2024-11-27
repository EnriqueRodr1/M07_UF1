import mysql.connector
from mysql.connector import Error

# Configuración de la conexión a la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Reyney15',
    'database': 'fastapi_db',
    'charset': 'utf8mb4',  # Cambiar el conjunto de caracteres
    'collation': 'utf8mb4_general_ci',  # Opcional, dependiendo del cliente
}


def get_db_connection():
    """Establece y retorna una conexión a la base de datos."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise

def close_db_connection(connection):
    """Cierra una conexión existente a la base de datos."""
    if connection.is_connected():
        connection.close()
