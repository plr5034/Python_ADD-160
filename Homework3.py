#	
# Objective: Create a Python function that simulates a conference sign-up process, accepting any number of participants and their contact details. 
# The function should print a summary of the participants and their contact details. No Doctest for this one. I want you to be able to play
# with the *args and **kwargs functionality.
#
# Assignment Instructions
# Create a Python function named conference_signup that accepts any number of participant names using *args and their contact details (email and phone) using **kwargs.
# Inside the function, print a summary of the participants and their contact details in a clear and organized format.
# Ensure that your function handles cases where no participants or no contact details are provided gracefully.
# Test your function with sample data to ensure it works correctly.
# 


Use the following three lines to create a dividing line of
length 50 tabs, though  can be changed here
		#	

def conference_signup(*participants, **contact_details):

		#	
		#	Creating a function to use throughout the function to provide some pretty printing, in this
        #   case, a dividing line :)
        #   will have a default vaulue of 50, but can be changed if another value is passed.
        #


    def dividing_line(mylength = 50):
        print("-" * mylength)
       
		#	
        # Print a header to beging the signup list.   Put a dividing line between it and the rest of the list
        #

    print("Conference Participants and Their Contact Details:")
    dividing_line(mylength)


		#	First check the input list to see if there are any partticipants with no participant details
		#	and print those at the top of the list

    if participants:
        for participant in participants:
            print(f"Name: {participant}\nEmail: N/A\nPhone: N/A")
            dividing_line(mylength)
    else:

		#	
		#	Not sure what to do if there are no participants only
		#	Could just do away with the else and print nothing.   There is no requirement either way
        # 

        print("No Particpants without Contact information provided.")
        dividing_line(mylength)
        print()

		#	Next check for participants WITH some or all the contact information.   Some may not have
		# 	an email or phone, so print N/A in that case.


    if contact_details:
        for participant, details in contact_details.items():
            email = details.get('email', 'N/A')
            phone = details.get('phone', 'N/A')
            print(f"Name: {participant}\nEmail: {email}\nPhone: {phone}")
            dividing_line(mylength)
    else:

		#  	Again, no specific requirement on what to do if no participant with contract information 
		#  	is provided, so providing this information

        print("No Participants with Contact information provided.")

	#
	#	Test data to validate script
	#

conference_signup (
    "Sam", "Fred"
)

print()
print()

conference_signup (
    "Sam", "Fred",
    Alice={'email': 'alice@example.com', 'phone': '123-456-7890'},
    Bob={'email': 'bob@example.com','phone': '987-654-3210'},
    Charlie={'email': 'charlie@example.com'}
)

print()
print()

conference_signup (
    Alice={'email': 'alice@example.com', 'phone': '123-456-7890'},
    Bob={'email': 'bob@example.com','phone': '987-654-3210'},
    Charlie={'email': 'charlie@example.com'}
)

print()
print()

conference_signup (
    "Sam",
    Alice={'email': 'alice@example.com', 'phone': '123-456-7890'},
    Bob={'phone': '987-654-3210'},
    Charlie={'email': 'charlie@example.com'}
)