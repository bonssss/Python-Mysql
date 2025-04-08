# db_connection.py
import pymysql

class MySQLConnection:
    def __init__(self, host="localhost", user="root", password="Test@123", database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print(f"✅ Connected to MySQL Server{' (with DB)' if self.database else ''}")
            return self.connection
        except pymysql.MySQLError as e:
            print(f"❌ Connection failed: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("🔒 Connection closed.")
