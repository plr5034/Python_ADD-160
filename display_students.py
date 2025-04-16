'''
Assignment API 1.7 CRUD
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/display_students.py

Create a Python program that uses the requests library to perform CRUD 
operations on a JSON API.

You will follow along with the tutorial on CRUD at the Python institute.
You need to modify to work with the students.json file so that you cannot
just copy and paste and must think about how to modify the code.

Specifically the script will demonstrate:

1) List all entries
2) Select an entry by ID
3) Sort the entries by an attribute (last name)
4) Add an entry (add all fields)
5) Delete an entry (delete by ID)

NOTES: While trying to get this to work, I initially had issues with selecting
an entry by ID and deleting an entry by ID.  The key to the fix was realizing
that the "id" field was required in the JSON file.  I had to add the "id" field.
I discovered this by looking at the JSON file aftre I added a new entry.  The new 
entry had the "id" field in it as well as the other fields.

I changed the student.json file to include the "id" field.   Once this was done,
I was able to select an entry by ID and delete an entry by ID.

Bottome line, need to use the updated students.json file with the "id" field.
'''
import requests
import json

# variables
quit = False
mytimeout = 10

# Define field names and column widths
field_names = ["id", "studentid", "firstName", "lastName", "phone", "email"]
column_widths = [5, 12, 15, 15, 15, 25]

def print_headers():
    """Print table headers."""
    headers = [name.ljust(width) for name, width in zip(field_names, column_widths)]
    print(" | ".join(headers))
    print("-" * (sum(column_widths) + (len(column_widths) - 1) * 3))

def print_student(student):
    """Print a student's details."""
#    row = [str(student[field]).ljust(width) for field, width in zip(field_names, column_widths)]
    row = [str(student[field]).ljust(width) for field, width in zip(field_names, column_widths)]
    print(" | ".join(row))

def display_students(data):
    """Display the student data in a formatted table."""
    print_headers()
    for student in data:
        print_student(student)

def menu():
    """Display the menu and get user choice."""
    print("\nMenu:")
    print("1. Show all students")
    print("2. Show students by ID")
    print("3. Show students in alphabetical order by last name")
    print("4. Add a student")
    print("5. Delete a student")
    print("6. Quit")
    print("")
    choice = input("Please enter your choice: ")
    print("")
    return choice

def show_students():
    """Fetch and display all students."""
    try:
        response = requests.get("http://localhost:3000/students", timeout=mytimeout)
        response.raise_for_status()
        students = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    else:
        if students:
            display_students(students)
        else:
            print("No student data found.")

def show_students_by_id(ID):
    """Fetch and display a student by ID."""
    print()
    try:
        response = requests.get(f"http://localhost:3000/students/{ID}", timeout=mytimeout)
        response.raise_for_status()
        student = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("Enter a valid ID")
    else:
        if student:
            display_students([student])
        else:
            print("No student data found.")

def sort_students_by_last_name():
    """Fetch and display students sorted by last name."""
    try:
            response = requests.get("http://localhost:3000/students?_sort=lastName", timeout=mytimeout)
            response.raise_for_status()
            students = response.json()
    except requests.RequestException as e:
        print(f"Error: {e}")
    else:
        if students:
            display_students(students)
        else:
            print("No student data found.")
# Add a student
def add_student(student):
    """Add a new student."""
    try:
        response = requests.post("http://localhost:3000/students", json=student, timeout=mytimeout)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    else:
        print("")
        print("Student added successfully.")

def delete_student(ID):
    """Delete a student by ID."""
    try:
        response = requests.delete(f"http://localhost:3000/students/{ID}", timeout=mytimeout)
        if response.status_code == 200 or response.status_code == 204:
            print("")
            print("Student deleted successfully.\n")
        else:
            print("")
            print(f"Failed to delete student. Status code: {response.status_code}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Main program loop

while not quit:
    # print menu
    mychoice = menu()
    if mychoice == '1':
        show_students()
    elif mychoice == '2':
        student_id = input("Enter ID to select student record: ")
        show_students_by_id(student_id)
    elif mychoice == '3':
        sort_students_by_last_name()
    elif mychoice == '4': # Add a student
        new_student = {
            "id": input("Enter ID: "),
            "studentid": input("Enter studentid: "),
            "firstName": input("Enter first name: "),
            "lastName": input("Enter last name: "),
            "phone": input("Enter phone number: "),
            "email": input("Enter email address: ")
        }
        add_student(new_student)
    elif mychoice == '5':
        # Delete a student
        student_id = input("Enter student ID to delete: ")
        delete_student(student_id)
    elif mychoice == '6':
        quit = True
    else:
        print("Invalid choice. Please try again.")
# Close the program
