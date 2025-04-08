import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class MySQLConnection:
    def __init__(self, host=None, user=None, password=None, database=None):
        # Use .env values if not provided explicitly
        self.host = host or os.getenv("DB_HOST")
        self.user = user or os.getenv("DB_USER")
        self.password = password or os.getenv("DB_PASSWORD")
        self.database = database or os.getenv("DB_NAME")
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
