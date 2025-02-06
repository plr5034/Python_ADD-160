"""
Homework:  Zen of Python
Name: Paul Ring
github link:https://github.com/plr5034/Python_ADD-160/blob/main/zen.py

Take provided code and update to address the following issues:

1) Make Names Meaningful:
Replace single-letter variables with meaningful names.
Rename the function to reflect its purpose.
2) Add Comments:
Explain the purpose of the function.
Describe the purpose of each major block of code.
3) Improve Spacing and Indentation:
Ensure consistent use of indentation (4 spaces per level).
Add blank lines to separate different parts of the code.
4) Simplify the Code:
Reduce nesting levels by refactoring the logic.
Simplify conditionals where possible.
5) Add Docstrings:
Add a docstring to the function to describe its behavior.
6) Handle Errors Gracefully:
Add error handling for unexpected inputs.
 
"""

def integer_play(first_int, second_int):
    '''
    function that takes two integers and returns the following:
      1) If one of them is zero, return "Zero found".
      2) If both are positive, print the larger integer the smaller number of
        times.
      3) If one was negative, return the difference between the two.  Subtracting
       the larger of the two numbers from the smaller.
        
        Was the intent of the 1st and third tests to print or return?   Consistency 
        would have printed all the outputs, or returned all the outputs.
    '''

    '''
    Prior to starting, test the function inputs and validate they are integers,
    If not, return an error message and end the function
    '''
    if not isinstance(first_int, int) or not isinstance(second_int, int):
        return "Error: Both inputs must be integers."
    else:
        '''
        Test to see if either input variable is zero, if it is, 
        return "Zero found"
        '''
        if first_int == 0 or second_int == 0:
            return "Zero found"
        
            '''
            Test to see if both input variables are positive, if they are, print
            the larger integer of the two integers, the smaller amount of times
            '''
        elif first_int > 0 and second_int > 0:
            if first_int > second_int:
                for i in range(second_int):
                    print(first_int)
            else:
                for j in range(first_int):
                    print(second_int)
            '''
            Depending on which of the two are negative numbers, return the difference
            having the larger of the two numbers subtracted from the smaller
            '''
        else:
            if first_int < second_int:
                return first_int - second_int
            else:
                return second_int - first_int 

'''
Test cases can be removed from finished code, but here for validation of logic
'''

integer_play(1, 2)
print()

integer_play(5,3)
print()

x = integer_play(0, 2)
print(x)
print()

y = integer_play(2,-3)
print(y)
print()

z = integer_play(-2,4)
print(z)
print()

xx = integer_play(2,-8)
print(xx)
print()

yy = integer_play(1.1,2.2)
print(yy)
print()