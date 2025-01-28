'''
Homework2
Name:
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        # your code here
        self.name=name
        self.account = starting_amount
    
    def __repr__(self):
        # your code here
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"
    
    def __str__(self):
        # your code here:
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"
    
    def deposit(self,amount):
        # your code here
        if amount>0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print(f"Please deposit a positive number.")
    
    def withdraw(self,amount):
        if amount>0:
            if self.account-amount>=0:
                self.account-=amount
                print(f"{amount} withdrawn. New balance: {self.account}")
            else:
                print(f"Insufficient funds.")
        else:
            print(f"Please withdraw an amount greater than zero.")

    
    def check_balance(self):
        """
        Check and return the balance of the account holder's account.
        """
        print(f"Balance: {self.account}")

class SavingsAccount(Bank_Account):
    pass

class CheckingAccount(Bank_Account):
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))