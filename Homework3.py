'''
Objective: Create a Python function that simulates a conference sign-up process, accepting any number of participants and their contact details. 
The function should print a summary of the participants and their contact details. No Doctest for this one. I want you to be able to play
with the *args and **kwargs functionality.

Assignment Instructions
Create a Python function named conference_signup that accepts any number of participant names using *args and their contact details (email and phone) using **kwargs.
Inside the function, print a summary of the participants and their contact details in a clear and organized format.
Ensure that your function handles cases where no participants or no contact details are provided gracefully.
Test your function with sample data to ensure it works correctly.
'''

'''
Use the following three lines to create a dividing line of
length 50 tabs, though  can be changed here
'''

mylength = 50
def dividing_line(mylength):
    print("-" * mylength)

def conference_signup(*contacts, **contact_details):

    '''
    If no data provided, do nothing and exit; actually tested this, and there is an error if nothing or an empty
    * or ** are provided, so this is not necessary
    '''
    
    if not contacts and not contact_details:
        print("No participants or contact details provided.")
        return

    print("Conference Participants and Their Contact Details:")
    dividing_line(mylength)

    if contact_details:
        for participant, details in contact_details.items():
            if participant == " ":
                participant = "N/A" 
            email = details.get('email', 'N/A')
            phone = details.get('phone', 'N/A')
            print(f"Name: {participant}\nEmail: {email}\nPhone: {phone}")
            dividing_line(mylength)
    else:
        print("No contact details provided.")
dividing_line(mylength)

'''
Test Cases to validate script
'''

contacts = ["Alice", "Bob", "Charlie",""]
contact_details = {
    "Alice":{"email":"alice@example.com", "phone": "123-456-7890"},    
    "Bob": {"email":"bob@example.com", "phone": "987-654-3210"},
    "Charlie": {"email":"charlie@example.com"},
    " ": { "phone": "555-555-5555"}}
conference_signup(*contacts, **contact_details)