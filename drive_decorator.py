'''
Homework: Enhance the drive_decorator to log the time taken for each drive action
Name: Paul Ring
github link:https://github.com/plr5034/Python_ADD-160/blob/main/drive_decorator.py
Enhance the drive_decorator to log the time taken for each drive action. Use
the time module to capture the start and end times. 
(Estimated time: 45 minutes)
'''

'''
Importing the func_timer decorator fromt he timing_func file from the previous 
excercise to do the timing.
Use func_timer to time the drive_decorator decorator.
'''
from timing_func import *

def drive_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@func_timer 
@drive_decorator
def car(make, model):
    print(f"Driving a {make} {model}")


@func_timer 
@drive_decorator
def motorcycle(make):
    print(f"Riding a {make} motorcycle")

@func_timer 
@drive_decorator
def boat(make):
    print(f"Sailing a {make} boat")

# Test data and sample output
car('Toyota', 'Corolla')   # Output: Starting car with arguments ('Toyota', 'Corolla') {}
                           #         Driving a Toyota Corolla
                           #         Finished car

motorcycle('Harley')       # Output: Starting motorcycle with arguments ('Harley',) {}
                           #         Riding a Harley motorcycle
                           #         Finished motorcycle

boat('Yamaha')             # Output: Starting boat with arguments ('Yamaha',) {}
                           #         Sailing a Yamaha boat
                           #         Finished boat