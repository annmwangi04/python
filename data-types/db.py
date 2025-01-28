import pymysql

print("Connector imported successfully.")

try:
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="wanjiru254"
    )
    print("Connection successful!")
except pymysql.MySQLError as err:
    print(f"Error: {err}")
