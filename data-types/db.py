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
#  sql = "INSERT INTO students (name, course, phone) VALUES (%s, %s, %s)"

#  values = ("Ann", "Data analyst", "0778900965")

#  students =[
#     "Ann", "Data analyst", "0778900965"
#     "Ann", "Data scienist", "0778900965"
#     "Ann", "fiancial analyst", "0778900965"
#     "Ann", "Analyst", "0778900965"
#     "Ann", "Data ", "0778900965"

#  ]

# # Execute the query with values
# mycursor.execute(sql, values)

# # Commit the changes to the database
#  connection.commit()

# # Print how many records were inserted
# print(mycursor.rowcount, "record inserted.")

# # Close the connection
# connection.close()
# mycursor.execute("SELECT * FROM students ORDER BY name")

# results = mycursor.fetchall()

# print(results)

# mycursor.execute("DELETE FROM students WHERE id = 1")
#  connection.commit()

# mycursor.execute("UPDATE students SET course = 'Blockchain' WHERE id = 2")

# connection.commit()