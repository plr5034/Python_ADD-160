'''
Homework2
Name: Paul Ring
github link:https://github.com/plr5034/Python_ADD-160/blob/main/homework2.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

'''
The Bank Account Class will be the Parent Class that the Savings and Checking Account Children classes will inherit from.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        # initializing attributes for Bank_Account
        # The constructor has two input variables, the name of the account and the starting amount. 
        # Assign each of these values to instance variables.
        self.name=name
        self.account = starting_amount
    
    def __repr__(self):
        # your code here
        return f"Bank_Account(name='{self.name}', Account Balance={self.account}"
    
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
    '''
    i. make a constructor for the savings account class. The constructor will take the account holder's name, the balance, and the interest rate as parameters. (Don't forget to include self).
    ii. Make the __repr__ function. Sample output: SavingsAccount(account_holder='bob', balance=100, interest_rate=1.0%)
    iii. Make the __str__ function. Sample output: Savings Account - bob: Balance = $100.00, Interest Rate =1.0%
    iv. make the apply_interest function. This function's only parameter is self. Apply the interest equation and add the interest to the balance.
        Equation: interest = balance * (interest_rate/100)
    '''

    def __init__(self, name,starting_amount,interest_rate):
        super().__init__(name,starting_amount)
        self.interest_rate=interest_rate
    
    def __repr__(self):
        return f"SavingsAccount(account_holder='{self.name}', balance={self.account}, interest_rate={self.interest_rate}%"
        
    
    def __str__(self):
        '''
            return f" Savings Account - {self.name}\n Balance = ${self.account:.2f}\n Interest Rate ={self.interest_rate}%\n\n"    
        '''
        return f" Savings Account - {self.name}: Balance = ${self.account:.2f}, Interest Rate ={self.interest_rate}%"

    def apply_interest(self):
        interest = self.account * (self.interest_rate/100)
        self.account += interest
        print(f"Interest applied. New balance: {self.account}")

class CheckingAccount(Bank_Account):
    '''
    i. make a constructor for the savings account class. The constructor will take the account holder's name, the balance, and the overdraft limit as parameters. (Don't forget to include self).
    ii. Make the __repr__ function. Sample output: CheckingAccount(account_holder='bob', balance=100, overdraft_limit=100.0)
    iii. Make the __str__ function. Sample output: Checking Account - bob: Balance = $100.00, Overdraft Limit =$100.00
    iv. make the withdraw function. This function's only parameter is withdraw and self. A bank user is allowed to withdraw money in the following conditions:
    if the amount of money withdrew is less than zero, then print the message "Withdrawal amount must be positive."
      if the amount of money withdrew is greater than the balance and the overdraft limit, then print the message "Withdrawal exceeds overdraft limit."
      Otherwise, withdraw the amount from the balance and print the new balance. 
    '''

    def __init__(self, name,starting_amount,overdraft_limit):
        super().__init__(name,starting_amount)
        self.overdraft_limit=overdraft_limit

    def __repr__(self):
        return f"CheckingAccount(account_holder='{self.name}', balance={self.account}, overdraft_limit={self.overdraft_limit}%"
        
    def __str__(self):
        return f" Checking Account - {self.name}: Balance = ${self.account:.2f}, Overdraft Limit ={self.overdraft_limit}%"



if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))
