# main.py
from db_initializer import DBInitializer
from user_repository import UserRepository

# Step 1: Create DB and Tables
# init = DBInitializer()
# init.create_database("test")
# init.create_tables()

# Step 2: Use User Repository
repo = UserRepository()
# repo.add_user("to", "na@exple.com")
# demo = repo.get_all_users()
# email = repo.get_name("Bo")
# print("📋 Users:", demo)
# print("📧 Email:", email)

#order by
# ordered = repo.get_orderBy("name")
# print("📋 Ordered Users by name:", ordered)

#delete user

# deleted = repo.delete_user(4)
# print("✅ User deleted:", deleted)


#update user
update=repo.update_user(5,'hello','hel@gmail.com')
print("✅ User updated:", update)