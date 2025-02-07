'''
Homework3
Name: Paul Ring 
github link:https://github.com/plr5034/Python_ADD-160/blob/main/homework3.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.

Define the Class-based Decorator:
Create a class called Decorator with an __init__ method that takes a function as an argument and stores it as an instance variable.

Implement the __call__ Method:
Define the __call__ hod should:

Call the stored function with its arguments.
Print the function with the following message: "Factorial product = {*result of product*}. Currently multiplying by {*current number in the loop*}" 
Note: The step above will make more sense when you read the rest of the assignment.
Return the result of the function call.
Create a Computationally Intensive Function:
Write a function that performs a computationally intensive task, such as calculating the factorial of a large number.

Apply the Decorator:
Apply the Decorator to the computationally intensive function using the @ syntax.

Test the Decorated Function:
Call the decorated function using the doctest.

Experiment with Different Functions:
Try applying the Decorator to other functions to see how it works with different computational tasks.

'''

class Decorator:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        ''' initiate counter each time through the call'''
        self.count = 0
        def wrapper(*args, **kwargs):
            result = self.func(*args, **kwargs)
            self.count += 1
            print(f'Factorial product = {result}. Currently multiplying by {self.count}')
            return result
        return wrapper (*args, **kwargs)
    
@Decorator
def factorial(n):
    '''Recursive function to find the factorial of an integer'''
    if n < 0:
        print ("Cannot use negative numbers")
    elif n == 1 or n == 0:
        return 1 #  factorial uses 1 for both the 0 & 1 indexes
    else:
        # recursive call to the function
        return (n * factorial(n-1))
        
'''
Do not remove the code below - used to test the above code
'''
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))

