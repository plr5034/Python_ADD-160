'''
Homework: decorator that logs the execution time of a function
Name: Paul Ring
github link:https://github.com/plr5034/Python_ADD-160/blob/main/timing_func.testdata.py
Create a new decorator: -> func_timer
Write a decorator that logs the execution time of a function. Apply this 
decorator to a few sample functions and measure their execution times. 
(Estimated time: 30 minutes)
'''

'''
There are a lot of built in time functions in python to choose from.
Review here:
    https://docs.python.org/3/library/time.html
'''

import time

def func_timer(func):
    def wrapper(*args, **kwargs):
        begin_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - begin_time
        print(f"The function '{func.__name__}' took {execution_time:.9f} seconds to execute.")
        return result
    return wrapper

'''
Test functions to show that the timer decorator works correctly.
'''

@func_timer
def test_function1(n):
    '''Test function that prints out the first n letters of the alphabet
        add test to validate n is between 1 & 26 :)
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if n > 26 or n <= 0:
        print('n has to be greater than 0 and less than 27')
    else:
        for i in range(n):
            print(alphabet[i], end=' ')
        print()
    return

@func_timer
def test_function2(n):
    '''Test function that adds the first n numbers'''
    total = 0
    for i in range(n):
        total += i
    print(total)
    return total

func_timer(test_function1(12))
func_timer(test_function1(27))
func_timer(test_function2(11))


