'''
docstring.py
Name: Paul Ring
github link:https://github.com/plr5034/Python_ADD-160/blob/main/docstring.py

Objective:
==========
This is a simple calculator class that performs basic arithmetic operations.
Includes only methods for
- addition
- subtraction
- multiplication
- division.

And like a calulator, it can clear the current value and return the current
value.
'''
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num

    def subtract(self, num):
        self.value -= num

    def multiply(self, num):
        self.value *= num

    def divide(self, num):
        if num != 0:
            self.value /= num
        else:
            raise ValueError("Cannot divide by zero")

    def clear(self):
        self.value = 0

    def get_value(self):
        return self.value

'''
This main section is for testing the Calculator class.  Tests each of the
operations as well as the exception handling for division by zero.

'''

def main():
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
