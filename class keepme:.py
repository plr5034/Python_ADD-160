from functools import wraps

class RunMe():
    def __init__(self, num_times):
        self.num_times = num_times
        if self.num_times < 1:
            print ("Input needs to be a positive number!")
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(self.num_times):
                print(f'Running {i} of {self.num_times}')
                return func(*args, **kwargs)
        return wrapper

@RunMe(5)
def sound():
    print("Quack!")

sound()  # Output: Prefix: sound
         #         Quack!