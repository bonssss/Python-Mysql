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
    
    def get_name(self, name):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM demo WHERE name = %s", (name,))
                return cursor.fetchall()
        finally:
            self.conn_obj.close()
    
    def get_orderBy(self, order_by="name"):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM demo ORDER BY {order_by} Desc")
                return cursor.fetchall()
        finally:
            self.conn_obj.close()
            
    def delete_user(self, user_id):
        try:
            with self.conn.cursor() as cursor:
                # Fetch user before deleting
                cursor.execute("SELECT * FROM demo WHERE id = %s", (user_id,))
                user = cursor.fetchone()

                if not user:
                    print("❌ User not found.")
                    return None

                cursor.execute("DELETE FROM demo WHERE id = %s", (user_id,))
                self.conn.commit()
                print(f"✅ User with ID '{user_id}' deleted.")
                return user
        except Exception as e:
            print(f"❌ Error deleting user: {e}")
            return None
    
    def update_user(self, user_id, name=None, email=None):
        try:
            with self.conn.cursor() as cursor:
                # Fetch user before updating
                cursor.execute("SELECT * FROM demo WHERE id = %s", (user_id,))
                user = cursor.fetchone()

                if not user:
                    print("❌ User not found.")
                    return None

                if name:
                    cursor.execute("UPDATE demo SET name = %s WHERE id = %s", (name, user_id))
                if email:
                    cursor.execute("UPDATE demo SET email = %s WHERE id = %s", (email, user_id))
                
                self.conn.commit()
                print(f"✅ User with ID '{user_id}' updated.")
                return self.get_name(user[1])  # Return updated user details
        except Exception as e:
            print(f"❌ Error updating user: {e}")
            return None
