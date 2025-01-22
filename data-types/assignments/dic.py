students = {
    "ann": [69, 78, 90, 56, 76],
    "amos": [89, 98, 80, 66, 76],
    "mercy": [79, 78, 90, 56, 76],
    "julia": [59, 78, 70, 76, 96],
    "marco": [86, 88, 90, 66, 76],
}
total = {}  # Initialize as a dictionary
best_mark = 0  # Initialize best_mark to a very low value
best_name = ""  # Initialize best_name as an empty string

for name, marks in students.items():
    average = sum(marks) / len(marks)  # Calculate average
    total[name] = average  # Store in the dictionary

    if average > best_mark:
        best_mark = average
        best_name = name

print(total)  # Print all students' averages
print(f"The student with the best average is {best_name} with a score of {best_mark:.2f}.")
