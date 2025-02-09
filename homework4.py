'''
Homework4
Name:Paul Ring 
github link:https://github.com/plr5034/Python_ADD-160/blob/main/homework4.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.

1) Create a Class
Identify that the homework file has the Car class.

2) Define Instance Variables
Inside the class, define the __init__ method to initialize instance variables.
Create at least two instance variables to store specific information about the
object.
3) Implement Instance Methods
Define at least one instance method that operates on instance variables.
Ensure the method modifies or utilizes instance variables in some way.
Remember to include self as the first parameter.
4) Implement Class Methods
Use the @classmethod decorator to define at least one class method.
Ensure the method modifies or utilizes class variables. In this case, define
a class variable that counts the total number of cars. Call it total_cars.
Remember to include cls as the first parameter.
5) Implement Static Methods
Use the @staticmethod decorator to define at least one static method.
Ensure the method performs a utility function related to the class but does
not modify instance or class variables. 
Static methods do not need self or cls parameters.
6) Doctest
The static method, class method, and instance method are tested in the doctest.
Ensure your code works with the doctest.
7) Test and Document
Test the program to ensure all methods work as expected.
Add comments to the code to explain what each method does and how it is used.
Write a brief explanation at the end of the program to summarize the 
differences between instance methods, class methods, and static methods.
This can be in a doc string comment """  between 3 sets of quotes. """
'''

class Car:
    ''' 
    Class attribute to count total number of cars, initialize to 0
    '''
    total_cars = 0    

    def __init__(self, brand, model):
        '''
        Initialize instance variables.  Could add more, like year, color, etc.
        But, would break doctest4.py.
        self.year = year
        self.color = color
        self.package = package
        They would need to be passed in the prarameter list, with brand & model.

        def __init__(self, brand, model, year, color, package):
        '''
        self.brand = brand
        self.model = model
    
    def display_info(self):
        '''
        Instance method to display car details.   Again, would need to update
        the info to look like:

        print(f"Car: {self.brand} {self.model} {self.year} {self.color} {self.package}")
        '''
        print(f"\'Car: {self.brand} {self.model}\'")
    
    @classmethod
    def update_total_cars(cls, count):
        '''
        Class method to update total number of cars.   Pretty simple.
        '''
        cls.total_cars += count
    
    @staticmethod
    def general_info():
        '''
        Static method providing general information about cars.
        '''
        print("\'Cars are a mode of transportation.\'")

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))

'''
Summary of the differences between instance methods, class methods, and static
methods.

Instance Methods:
Can access and modify both class attributes and instance attributes.
Starts with the keyword “def”. Its first parameter is the keyword “self”.
The self parameter binds the method to the instance object.

Class Methods:
Can access and modify class state and are bound to the class, which makes
them suitable for operations that involve the class itself.  Typically use
@classmethod decorator.  The first parameter of this class method is “cls”.
The “cls” keyword simply means “referring to the class.” 


Static Methods:
Do not access or modify class or instance state and are used for utility 
(or helper) functions that do not require access to the class or instance.
They add extra functionality to a class without accessing or modifying the
class state.

'''