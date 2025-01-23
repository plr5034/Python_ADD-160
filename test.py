'''
Homework1
Name: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/homework1.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        # initializing attributes for Bank_Account
        # The constructor has two input variables, the name of the account and the starting amount. 
        # Assign each of these values to instance variables.

        self.accountName = name
        self.starting_amount = starting_amount

        pass
    
    def __repr__(self):
        # printable representation of the object.   Formatting is not its virtue.  This is more for troubleshooting
        # for the homework, sample output should look like:
        #         Bank_Account(name='Bob',  Account Balance=12457.22)
        return f"Bank_Account*(name={self.accountName}),(Account Balance={self.starting_amount})"
    
    def __str__(self):
        # Pretty Print version of the object.   Good for user, more easily readable.
        return f"Bank_Account*(name={self.accountName}),(Account Balance={self.starting_amount})"
    
    def deposit(self,amount):
        # your code here
        pass
    
    def withdraw(self,amount):
        pass

    
    def check_balance(self):
        pass
