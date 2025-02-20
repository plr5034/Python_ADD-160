'''
Homework8
Name: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/homework8.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.

Objective: Given a balance and the amount that a user would like to withdraw,
write a function that catches usual exceptions when interacting with a bank.
Follow the step-by-step instructions to learn more.

Step-by-Step Directions
1) Define Custom Exceptions:
Create two custom exception classes by subclassing the Exception class. Name
them appropriately for the errors you want to handle. These have been named
for you in the homework file. You need to fill in the details.

2) First Level of Error Handling:
Write a try block where the InvalidAmountError is thrown when the amount given
in the function is not an integer or a float or the amount is less than zero.
Raise the first custom exception in this try block.

3) Second Level of Error Handling:
For the next exception, throw the InsufficientFundsError is the amount
withdrawn is greater than the balance.
'''

class InsufficientFundsError(Exception):
    '''
    InsufficientFundsError is the amount withdrawn is greater than the balance.

    Args: 
        Exception class

    Returns: 
        Prints the error message - 
    '''
    def __init__(self, message="Insufficient funds."):
        self.message = message
    
    def __str__(self):
        return f"InsufficientFundsError: {self.message}"

class InvalidAmountError(Exception):
    '''
    InvalidAmountError is thrown when the amount given
    in the function is not an integer or a float or the amount is less than
    zero.  Raise the first custom exception in this try block.

    Args: 
        Exception class

    Returns: 
        Prints the error message - 
    '''

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"InvalidAmountError: {self.message}"

# Function to withdraw money
def withdraw_money(balance, amount):
    '''
    Goal is to test:
    a) If the amount is a number or is a positive number
    b) If the amount is greater than the balance

    Args:
        balance: int or float, the amount in the account
        amount: int or float, the amount to be withdrawn

    Returns:
        None   
    '''
    try:
        if type(amount) not in [int, float] or amount < 0:
            raise InvalidAmountError("Amount must be a positive number.")
        elif amount > balance:
            raise InsufficientFundsError("Insufficient funds in account.")
        else:
            balance = balance - amount
#            print(f"Amount withdrawn: {amount}")
#            print(f"Remaining balance: {balance}")
            print(balance)
    except Exception as my_exception:
        print(my_exception)

'''
    Test Cases, do not modify
'''   
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py'))

