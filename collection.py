print("Welcome to student data organizer")
print("Select an option")
print("1. Add Student")
print("2. Display All Students")
print("3. Update Student Information")
print("4. Delete Student")
print("5. Enter Your subjects")
print("6. Exit")

choice = input("Enter your choice: ")

# Using list to store student data
students = [
    { "student_id": 101, 
     "student_name": "Romil", 
     "student_age": 26, 
     "Grade": "A", 
     "subjects": ["JavaScript", "Java", "HTML", "CSS"]},
    { "student_id": 102, 
     "student_name": "Keyur", 
     "student_age": 20, 
     "Grade": "D", 
     "subjects": ["JavaScript", "Java", "HTML", "CSS"]},
    { "student_id": 103, 
     "student_name": "Ayush", 
     "student_age": 23, 
     "Grade": "A", 
     "subjects": ["JavaScript", "Java", "HTML", "CSS"]}
]

students.append({"student_id": 104, "student_name": "Rushi", 
"student_age": 18, "Grade": "E", "subjects": ["JavaScript", "Java", "HTML", "CSS"]})
students.append({"student_id": 105, "student_name": "Bandhan", 
"student_age": 16, "Grade": "B", "subjects": ["JavaScript", "Java", "HTML", "CSS"]})

# Tuples (immutable data)
student_ids = (101, 102, 103, 104, 105)
print(student_ids[1:5])

# Set of subjects
subjects = {"JavaScript", "Java", "HTML", "CSS"}
print(subjects)

print("Thank you for using the data organizer!")