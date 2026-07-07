# Student Marks 

#Count the Number of Student
NumofStudents = int(input("Enter Total students: "))

#Data Storage
studentData = []

#Inserting Data
for i in range(NumofStudents):
    print(f"Enter the Data of Student {i+1}")
    name = input("Name: ")
    roll_no = int(input("Roll Number: "))
    marks = int(input("Marks: "))

    if marks >95:
        grade = "A"
    elif marks > 80:
        grade = "B"
    elif marks > 60:
        grade = "C"
    elif marks > 33:
        grade = "D"
    else:
        grade = "F"

    students = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grades": grade
    }

    studentData.append(students)

#Data Printing
print("All students Data: \n")

for s in studentData:
    print(f"{s['name']} - Roll Number: {s['roll_no']} - Marks: {s['marks']} - Grades: {s['grades']}")

#Passed Students
print("\n student who are Passed: ")

for s in studentData:
    if s['marks'] >= 33:
        print(f"{s['name']} - Marks: {s['marks']}")

