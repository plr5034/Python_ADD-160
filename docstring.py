'''
docstring.py
Name: Paul Ring
github link:https://github.com/plr5034/Python_ADD-160/blob/main/docstring.py
'''
class Calculator:
    '''
    Simple calculator class that performs basic arithmetic operations.
    Includes only methods for
    - addition
    - subtraction
    - multiplication
    - division.

    And like a calulator, it can clear the current value and return the current
    value.
    '''

    def __init__(self, value=0):
        '''
        Class initializer that sets the initial value of the calculator to 0
        '''
        self.value = value

    def add(self, num):
        '''
        method to add a number to the current value

        Args:
            num:  number to add to the current value
        
        Returns: 
            None
        '''
        self.value += num

    def subtract(self, num):
        '''
        method to subtract a number from the current value

        Args:
            num: number to subtract from the current value
        
        Returns:
            None
        '''
        self.value -= num

    def multiply(self, num):
        '''
        method to multiply a number to the current value

        Args:
            num: number to multiply to the current value
        
        Returns:
            None
        '''
        self.value *= num

    def divide(self, num):
        '''
        method to divide a number into the current value

        Args:
            num: number to divide into current value
        
        Returns:
            None
        
        Raises:
            ValueError: if num is 0
        '''
        if num != 0:
            self.value /= num
        else:
            raise ValueError("Cannot divide by zero")

    def clear(self):
        '''
        method to clear the current value

        Args:
            None
        
        Returns:
            None
        '''
        self.value = 0

    def get_value(self):
        '''
        method to return the current value of the calculator

        Args:
            None
        
        Returns:
            calculator value

        '''
        return self.value

def main():
    '''
    This main section is for testing the Calculator class.  Tests each of the
    operations as well as the exception handling for division by zero.
    '''
    
    calc = Calculator()
    calc.add(10)
    calc.subtract(2)
    calc.multiply(5)
    try:
        calc.divide(0)
    except ValueError as e:
        print(e)
    calc.divide(4)
    print(f"Final value: {calc.get_value()}")

if __name__ == "__main__":
    main()
