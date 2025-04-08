import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Test@123",
    database="test"  # Make sure to replace with your actual database name
)

print("Connected to MySQL Server successfully!")
print(mydb)

cursor = mydb.cursor()
cursor.execute("Show databases;")  # Corrected the SQL command to show tables
for x in cursor:
    print(x)  # This will print the cursor object to show that it's working

#insert into users (name, age) values ('John Doe', 30);
cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'abc@gmail.com');")


# Execute the query
cursor.execute("SELECT * FROM users;")

# Fetch all rows from the executed query
users = cursor.fetchall()

# Print the rows
for user in users:
    print(user)

# Commit the transaction
mydb.commit()

# Delete a record


# Close the cursor and connection
cursor.close()
mydb.close()