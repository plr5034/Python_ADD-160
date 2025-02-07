'''
Homework: decorator that logs the execution time of a function
Name: Paul Ring
github link:https://github.com/plr5034/Python_ADD-160/blob/main/timing_func.py
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
