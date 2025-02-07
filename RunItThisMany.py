'''
Homework: parameterized decorator
Name: Paul Ring
github link:https://github.com/plr5034/Python_ADD-160/blob/main/RunItThisMany.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.

Create a parameterized decorator:
Write a decorator that takes an argument specifying the number of times the 
decorated function should be executed. Apply it to a function and test with
different argument values. (Estimated time: 1 hour 30 minutes)
'''

class RunItThisMany:
    '''
    This class is a decorator that runs a function a specified number of times:
        num_times is the variable passed for the number of tries
    '''
    def __init__(self, num_times): 
        self.num_times = num_times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.num_times):
                print(f'Running {i + 1} of {self.num_times}')
                '''
                Had issues getting this to run the required number of times.
                Had to remove the return statement from function.
                '''
                func(*args, **kwargs)
        return wrapper

@RunItThisMany(12)
def sound():
    print("Quack!")

sound()