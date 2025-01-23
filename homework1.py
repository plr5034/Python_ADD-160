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
        self.balance = starting_amount

        pass
    
    def __repr__(self):
        # printable representation of the object.   Formatting is not its virtue.  This is more for troubleshooting
        # for the homework, sample output should look like:
        #         Bank_Account(name='Bob',  Account Balance=12457.22)
        return f"Bank_Account*(name={self.accountName}),(Account Balance={self.balance})"
    
    def __str__(self):
        # Pretty Print version of the object.   Good for user, more easily readable.
        return f"Account Name: {self.accountName}\nAccount Balance: {self.balance}"
    
    def deposit(self,amount):
        # Deposit function 
        # If the amount deposited is greater than zero, add it to the account. 
        # Otherwise, don't allow the amount to change. 
        if amount > 0:
            self.balance += amount
            print (f"{amount} deposited. New Balance: {self.balance}")
        else:
            print ("Please deposit a positive number.")
        pass
    
    def withdraw(self,amount):
        # Withdraw function 
        # If the amount withdrawn is greater than zero and it doesn't overdraw the account, 
        # allow the amount to be withdrawn. Otherwise, don't allow the withdraw.
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New Balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Please withdraw an amount greater than zero.")
        pass

    
    def check_balance(self):
        # Check_balance function 
        # This function will print out the balance of the account holder.      
        print(f"Balance: {self.balance}")  
        pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))