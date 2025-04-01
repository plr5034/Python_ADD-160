'''
Assignment 1.3: Personal Information Data File Using JSON
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_1.3_json.py

Objective: Demonstrate the use of the JSON module in Python to store and 
retrieve personal information.   Specifically, create a Python program that:

1) Takes user input for personal information
    Name
    Age
    Address
    Phone number
    Email address
2) Stores the data in a dictionary 
3) convert it to a JSON string using json.dumps()
4) Saves the JSON string to a file named personal_info.json
5) Reads the file back into a Python object using json.load() and print the 
data
'''

# Import the json library
import json

# variables
file_contacts = "personal_info.json"

# 1) Take user input for personal information
# TODO: Add input validation!!
print("\nThis program will create a contact entry from your information...\n")
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your street address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zip_code = input("Enter your zip code: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")

# 2 Store the data in a python dictionary
contact = {
    "name": name,
    "age": age,
    "address": address,
    "city": city,
    "state": state,
    "zip": zip_code,
    "phone": phone,
    "email": email
}

# 3) convert it to a JSON string using json.dumps()
contact_json = json.dumps(contact, indent=4) #indent=4 for pretty printing
print() # Print blank line for readability
print("JSON string:", contact_json)
print() # Print blank line for readability

# 4) Saves the JSON string to a file named personal_info.json
with open(file_contacts, 'w', encoding='utf-8') as file:
    file.write(contact_json)

# 5) Reads the file back into a Python object using json.load() and print the
#  data
with open(file_contacts, 'r', encoding='utf-8') as file:
    loaded_contact = json.load(file)
print("Loaded contact data:")
for key, value in loaded_contact.items():
    print(f"{key}: {value}")
# End of program