# db_initializer.py
from db_connection import MySQLConnection

class DBInitializer:
    def __init__(self):
        self.conn_obj = MySQLConnection(database=None)
        self.conn = self.conn_obj.connect()

    def create_database(self, db_name):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"✅ Database '{db_name}' created or already exists.")
        finally:
            self.conn_obj.close()

    def create_tables(self):
        self.conn_obj = MySQLConnection(database="test")
        self.conn = self.conn_obj.connect()

        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS demo (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100),
                        email VARCHAR(100) UNIQUE
                    )
                """)
                print("✅ Table 'demo' created or already exists.")
                self.conn.commit()
        finally:
            self.conn_obj.close()
