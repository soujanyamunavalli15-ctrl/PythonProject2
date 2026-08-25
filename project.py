import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])


# Add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


# Display all students
def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n===== STUDENT DETAILS =====")
        for row in reader:
            print(" | ".join(row))


# Search student
def search_student():
    roll = input("Enter Roll Number to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                print("\nStudent Found!")
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                return

    print("Student not found!")


# Delete student
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    students = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    found = False

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["Roll Number", "Name", "Marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            if student["Roll Number"] == roll:
                found = True
            else:
                writer.writerow(student)

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found!")


# Main menu
create_file()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")