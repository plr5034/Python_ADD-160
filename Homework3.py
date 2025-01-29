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

def conference_signup(*args, **kwargs):
    if not args and not kwargs:
        print("No participants or contact details provided.")
        return

    print("Conference Sign-Up Summary:")
    print("-" * 30)

    if args:
        print("Participants:")
        for participant in args:
            print(f" - {participant}")
    else:
        print("No participants provided.")

    if kwargs:
        print("\nContact Details:")
        for participant, details in kwargs.items():
            email = details.get('email', 'N/A')
            phone = details.get('phone', 'N/A')
            print(f" - {participant}: Email: {email}, Phone: {phone}")
    else:
        print("No contact details provided.")

conference_signup("John Doe", "Jane Smith", email="j.doe@gmail.com", phone="123-456-7890", email="janes@aol.com", phone="987-654-3210")
