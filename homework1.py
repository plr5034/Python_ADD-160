'''
Homework1
Name: Paul Ring
github link: 
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        # initializing attributes for Bank_Account


        pass
    
    def __repr__(self):
        # printable representation of the object.   Formatting is not its virtue.  This is more for troubleshooting
        return 
    
    def __str__(self):
        # Pretty Print version of the object.   Good for user, more easily readable.
        return 
    
    def deposit(self,amount):
        # your code here
        pass
    
    def withdraw(self,amount):
        pass

    
    def check_balance(self):
        pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))