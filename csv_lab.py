'''
csv lab
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/csv_lab.py

create a class called PhoneContact representing a single contact. The
PhoneContact class should contain the name and phone properties

create a class called Phone that will store your contacts.
First implement the method called load_contacts_from_csv, responsible
for reading data from the CSV file into the class property called contacts.
The contacts property should contain a list of PhoneContact objects;
add to the Phone class a method called search_contacts, which accepts any
phrase entered by the user from the keyboard, and then based on it perform
a search for all matching contacts (case insensitive). If there are no results,
print the message: "No contacts found".

The search should be performed on all of the contact information, even partially.
The search should be case insensitive.
'''
import csv

class PhoneContact:
    '''
    Class representing a single contact with name and phone number.
    '''
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

class Phone:
    '''
    Class representing a phone book that stores contacts.
    '''
    def __init__(self):
        self.contacts = []

    def load_contacts_from_csv(self, filename):
        '''
        Load contacts from a CSV file into the contacts list.
        The CSV file should have a header with 'Name' and 'Phone' columns.
        
        args:
            filename (str): The name of the CSV file to read contacts from.
        returns:
            None
        '''
        try:
            with open(filename, newline='') as csvfile:
                fieldnames = ['Name', 'Phone']
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    # Ensure there are at least two columns; Name and Phone
                    # and that they are not empty
                    if len(row) >= 2:
                        # Need to skip the header row
                        if row['Name'] == 'Name' and row['Phone'] == 'Phone':
                            continue
                        # Create a PhoneContact object and add it to the list
                        contact = PhoneContact(row['Name'], row['Phone'])
                        print(f"Loaded contact: {contact}")
                        self.contacts.append(contact)
                    else:
                        print("Invalid contact format in CSV file.")

        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search_contacts(self, phrase):
        '''
        Search for contacts containing the given phrase in their name or phone number.
        
        args:
            phrase (str): The phrase to search for in contacts.
        returns:
            Prints matching contacts or a message if none are found to console.
        '''
        found = False
        print(f"Searching for contacts containing: '{phrase}'")
        for contact in self.contacts:
            if (phrase.lower() in contact.name.lower()) or (phrase.lower() in contact.phone.lower()):
                print(contact)
                found = True
        if found is not True:
            print("No contacts found.")

# Example usage
if __name__ == "__main__":
    phone = Phone()
    phone.load_contacts_from_csv('contacts.csv')
    print()
    search_phrase = input("Enter the phrase to search for: ")
    print()
    phone.search_contacts(search_phrase)