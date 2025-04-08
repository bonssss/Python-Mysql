# main.py
from db_initializer import DBInitializer
from user_repository import UserRepository

# Step 1: Create DB and Tables
# init = DBInitializer()
# init.create_database("test")
# init.create_tables()

# Step 2: Use User Repository
repo = UserRepository()
repo.add_user("Bo", "bonsa@exple.com")
demo = repo.get_all_users()
print("📋 Users:", demo)
