'''
Homework5
Name:Paul Ring 
github link:https://github.com/plr5034/Python_ADD-160/blob/main/homework5.py
Note: Remember to use comments for each function.
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.


Objective
In this assignment, you will create a new abstract class for a different type
of business, such as a bakery. You will include options for size, flavor, and
add-ins. Then, you will implement this abstract class for two specific items
(e.g., a croissant and a muffin). This exercise will help you understand how
to design and use abstract classes in Python.

Instructions
1) Define an Abstract Class:
Create an abstract class for your chosen business. This class should be a
blueprint for specific items in that business.
Include the following attributes in your abstract class:
    * Size: Different sizes for the item (e.g., small, medium, large).
    * Flavor: Different flavors for the item (e.g., chocolate, vanilla).
    * Add-ins: Additional options that can be added to the item (e.g., 
    nuts, fruit).
Define abstract methods for:
    * Adding the add-ins.
    * Providing a description of the item.

2) Implement the Abstract Class:
Create two specific classes that inherit from the abstract class. For example,
if you chose a bakery, you might create a Croissant class and a Muffin class.
Override the abstract methods in each specific class to provide functionality
for adding add-ins and providing a description.

3) Testing:
In your main program, create instances of your specific classes.
Call the methods to add add-ins and print descriptions for each instance to
ensure they work correctly.

'''

from abc import abstractmethod

class BakeryItem:
    '''Abstract class representing a bakery item.

    Include the following attributes in your abstract class:
        Size: Different sizes for the item (e.g., small, medium, large).
        Flavor: Different flavors for the item (e.g., chocolate, vanilla).
        Add-ins: Additional options that can be added to the item (e.g., nuts,
         fruit).
    '''
    
    def __init__(self, size, flavor):
        self.size = size
        self.flavor = flavor
        self.add_ins = [] # List of add-ins
    
    @abstractmethod
    def add_add_ins(self, add_in):
        '''Abstract method to add an ingredient to the item.
        '''

    @abstractmethod
    def get_description(self):
        '''Abstract method to get the item description.
        '''
        
class Croissant(BakeryItem):
    '''Concrete class representing a croissant.'''

    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    def add_add_ins(self, add_in):
        '''Add an ingredient to the croissant.'''
        self.add_ins.append(add_in)
        ''' Since add_ins is a list, we need to join them together if more
        than one
        '''
        print (f"Added {', '.join(self.add_ins)} to the croissant.")
            
    def get_description(self):
        '''Print out what makes this particular croissant.  Since add_ins is a
         list, we need to join them together.'''
        return f"{self.size} {self.flavor} croissant with {', '.join(self.add_ins)}."

class Muffin(BakeryItem):
    '''Concrete class representing a muffin'''
    def __init__(self, size, flavor):
        super().__init__(size, flavor)  
    
    def add_add_ins(self, add_in):
        self.add_ins.append(add_in)
        ''' Since add_ins is a list, we need to join them together if more
        than one
        '''        
        print (f"Added {', '.join(self.add_ins)} to the muffin.")  
    
    def get_description(self):
        '''Print out what makes this particular muffin.  Since add_ins is a
         list, we need to join them together.'''
        return f"{self.size} {self.flavor} muffin with {', '.join(self.add_ins)}."

class Scone(BakeryItem):
    '''Print out what makes this particular scone'''
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    def add_add_ins(self, add_in):
        self.add_ins.append(add_in)
        ''' Since add_ins is a list, we need to join them together if more
        than one
        '''    
        print (f"Added {', '.join(self.add_ins)} to the scone.")  

    def get_description(self):
        '''Print out what makes this particular scone.  Since add_ins is a
         list, we need to join them together.'''
        print(f"{self.size} {self.flavor} scone with {', '.join(self.add_ins)}.")

'''
Used this to test more that one add_in in the list.   Uncomment to run test.
'''

# scone = Scone("small", "chocolate")
# scone.add_add_ins("Almonds, Raisins")
# scone.get_description()


'''
Testing the classes w/ predified test cases.   Do not remove the test cases.
'''
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest5.py'))

