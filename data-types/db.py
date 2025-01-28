# Import the required library
import pymysql

# Print a message to confirm the library is imported
print("Connector imported successfully.")

# Connect to the MySQL server and specify the database
connection = pymysql.connect(
    host="localhost",    # Server address
    user="root",         # MySQL username
    password="wanjiru254",  # MySQL password
    database="zinduaschool"  # The database to connect to
)

# Create a cursor object
mycursor = connection.cursor()

# SQL query to insert data into 'students' table
# sql = "INSERT INTO students (name, course, phone) VALUES (%s, %s, %s)"

# values = ("Ann", "Data analyst", "0778900965")

# # Execute the query with values
# mycursor.execute(sql, values)

# # Commit the changes to the database
# connection.commit()

# # Print how many records were inserted
# print(mycursor.rowcount, "record inserted.")

# # Close the connection
# connection.close()
mycursor.execute("SELECT * FROM students WHERE id = 2")

results = mycursor.fetchone()

print(results)