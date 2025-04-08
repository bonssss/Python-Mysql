# user_repository.py
from db_connection import MySQLConnection

class UserRepository:
    def __init__(self):
        self.conn_obj = MySQLConnection(database="test")
        self.conn = self.conn_obj.connect()

    def add_user(self, name, email):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("INSERT INTO demo (name, email) VALUES (%s, %s)", (name, email))
                self.conn.commit()
                print(f"✅ User '{name}' added.")
        except Exception as e:
            print(f"❌ Error adding user: {e}")

    def get_all_users(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM demo")
                return cursor.fetchall()
        finally:
            self.conn_obj.close()
