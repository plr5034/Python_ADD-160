'''
Assignment API 1.5 XML Read and Write`
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/read_write_xml.py

Read an XML file and display its contents using Python.
Prompt the user to add a new record to the XML file.
Write the updated XML back to a file.

1) Read an XML file and display its contents:
    * ET.parse('customer_list.xml'): Loads and parses the XML file.
    * root.findall('customer'): Finds all customer elements in the XML tree.
    * customer.find('id').text: Accesses the text of a specific child element.
2) Prompt the user to add a new record to the XML file:
    * ET.Element('customer'): Creates a new customer element.
    * ET.SubElement: Adds child elements to the new customer.
    * root.append(new_customer): Appends the new customer to the root element.
3) Write the updated XML back to a file:
    * tree.write('customer_list.xml'): Writes the updated XML tree back to the file.
'''

import xml.etree.ElementTree as ET

# Step 1: Load and parse the XML file
tree = ET.parse('customer_list.xml') # wrong file name initially, created after append
# tree = ET.parse('customers.xml')
root = tree.getroot()

# Step 2: Display the data
print("Customer Records:")
for customer in root.findall('customer'):
    print(f"ID: {customer.find('id').text}")
    print(f"First Name: {customer.find('first').text}")
    print(f"Last Name: {customer.find('last').text}")
    print(f"Address: {customer.find('address').text}")
    print(f"Phone: {customer.find('phone').text}")
    print(f"Email: {customer.find('email').text}")
    print()

    # Ask the user if they want to add a new customer
add_record = input("Would you like to add a new customer? (yes/no): ").strip().lower()

if add_record == 'yes':
    # Step 1: Collect user input
    customer_id = input("Enter customer ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    # Step 2: Create a new customer element
    new_customer = ET.Element('customer')
    ET.SubElement(new_customer, 'id').text = customer_id
    ET.SubElement(new_customer, 'first').text = first_name
    ET.SubElement(new_customer, 'last').text = last_name
    ET.SubElement(new_customer, 'address').text = address
    ET.SubElement(new_customer, 'phone').text = phone
    ET.SubElement(new_customer, 'email').text = email

    # Step 3: Append the new customer to the root
    root.append(new_customer)

    # Step 4: Write the updated XML back to the file
    # tree.write('customer_list.xml')
    print("New customer added successfully!")