from pymongo import MongoClient
# Replace <username>, <password>, and <cluster-url> with your actual connection string details
client = MongoClient("mongodb+srv://annmwas204:YilttLYZrGOI0Mjx@cluster0.lwxem.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# Connect to the 'school' database
db = client.school
# Access the 'students' collection
students_collection = db.students
result = students_collection.delete_one({"firstName": "John"})
print(f"Deleted {result.deleted_count} document(s)")
