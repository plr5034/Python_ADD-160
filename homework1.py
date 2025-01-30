'''
Homework1
Name: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/homework1.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.

Updates to file based on feedback from Prof: remove pass from real def's (vs empty ones) and don't need to have self.account first be an int.
Though, at some point, probably need to format to looks like a dollar amount format.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        # initializing attributes for Bank_Account
        # The constructor has two input variables, the name of the account and the starting amount. 
        # Assign each of these values to instance variables.
        # NOTE: remember to change type to int for the starting amount.  This will prevent errors later on.

        self.accountName = name
        self.account = int(starting_amount)
    
    def __repr__(self):
        # printable representation of the object.   Formatting is not its virtue.  This is more for troubleshooting
        # for the homework, sample output should look like:
        #         Bank_Account(name='Bob',  Account Balance=12457.22)

        return f"Bank_Account(name='{self.accountName}', Account Balance={self.account})"
    
    def __str__(self):
        # Pretty Print version of the object.   Good for user, more easily readable.

        return f"Account Name: {self.accountName}\nAccount Balance: {self.account}"
    
    def deposit(self,amount):
        # Deposit function 
        # If the amount deposited is greater than zero, add it to the account. 
        # Otherwise, don't allow the amount to change. 

        if amount > 0:
            self.account += amount
            print (f"{amount} deposited. New balance: {self.account}")
        else:
            print ("Please deposit a positive number.")

    def withdraw(self,amount):
        # Withdraw function 
        # If the amount withdrawn is greater than zero and it doesn't overdraw the account, 
        # allow the amount to be withdrawn. Otherwise, don't allow the withdraw.

        if amount > 0 and amount <= self.account:
            self.account -= amount
            print(f"{amount} withdrawn. New balance: {self.account}")
        elif amount > self.account:
            print("Insufficient funds.")
        else:
            print("Please withdraw an amount greater than zero.")
    
    def check_balance(self):
        # Check_balance function 
        # This function will print out the balance of the account holder.      

        print(f"Balance: {self.account}")  

# The following code shouldn't be changed as it runs the automated checking

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))
