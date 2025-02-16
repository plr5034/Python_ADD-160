'''
Homework7
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/homework7.py

Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.

Assignment: Create a Subclass of Python's Built-in str Class

Instructions for Creating the Queue Class
1. Define the Class
Use the class keyword followed by Queue to define the class.

2. Initialize the Queue
Define the __init__ method to initialize the queue.
Use a default argument lst=[] but avoid mutable defaults.

Convert lst into a list to ensure encapsulation (self.q = list(lst)).

3. Implement String Representation
Define __repr__ to return a string representation of the queue.

Use f-string or .format() to format the output.

4. Enqueue Method
Define enqueue(self, item) to add an item to the queue.

Use self.q.append(item) to modify the queue.

5. Dequeue Method
Define dequeue(self) to remove and return the first item.

Use self.q.pop(0) to remove the first item.

Ensure that the function returns the removed item.

6. Implement Indexing
Define __getitem__(self, index) to allow indexing.

Return the item at self.q[index].

7. Implement Length Retrieval
Define __len__(self) to return the queue length.

Use return len(self.q).

8. Implement Equality Check
Define __eq__(self, other) to compare two Queue instances.

Ensure that other is a Queue instance.

Compare self.q and other.q lists.

9. Implement Addition
Define __add__(self, other) to concatenate two queues.

Return a new Queue instance with combined elements (Queue(self.q + other.q)).

10. Ensure Proper Testing
Instantiate Queue objects and test each method.

Check for edge cases such as an empty queue or duplicate elements.

'''

class Queue(str):

    '''
    1. Define the Class
    Use the class keyword followed by Queue to define the class.
    Since Queue is a subclass of str, inherit from str.
    '''

    def __init__(self, lst=[]):
        '''
        2. Initialize the Queue
        Define the __init__ method to initialize the queue.
        Use a default argument lst=[] but avoid mutable defaults.
        mutable defaults example here:
        
            https://docs.python-guide.org/writing/gotchas/

        Convert lst into a list to ensure encapsulation (self.q = list(lst)).       

        Args:
            self: the object itself
            lst: the list to convert to a queue

        Returns:
            None 
        '''

        super().__init__() # call the parent class constructor; had origianlly passed *args, but got errors
        self.q = list(lst)

    def __repr__(self):
        '''
        3. Implement String Representation
        Define __repr__ to return a string representation of the queue.

        Use f-string or .format() to format the output.

        Args:
            self: the object itself

        Returns:
            f"Queue({self.q})": returns the queue as a string
        '''

        return f"Queue({self.q})"


    def enqueue(self,item): 
        '''
        4. Enqueue Method
        Define enqueue(self, item) to add an item to the queue.
        Would need to validate data either before this is called or
        within this method.

        Use self.q.append(item) to modify the queue.
        
        Args:
            self: the object itself
            item: the item to add to the queue

        Returns:
            self.q.append(item): returns the queue with the item added
        '''
        return (self.q.append(item))

    def dequeue(self): 
        '''
        5. Dequeue Method
        Define dequeue(self) to remove and return the first item.
    
        Use  self.q.pop(0) to remove the first item.
        Ensure that the function returns the removed item.

        Might be good to validate the list is NOT empty before
        calling this method.  If empty, let user know.
    
        Args:
            self: the object itself
            
        Returns:
            self.q.pop(0): returns the first item in the queue
        '''       

        if len(self.q) != 0:
            return (self.q.pop(0))
        else:
            return 
           # print("Queue is empty")
    

    def __getitem__(self,index):
        '''
        6. Implement Indexing
        Define __getitem__(self, index) to allow indexing.

        Return the item at self.q[index].
        
        Args:
            self: the object itself
            index: the index to get from the queue  
        
        Returns:
            self.q[index]: returns the item at the index in the queue
        '''

        return (self.q[index])
        

    def __len__(self): # get
        '''
        7. Implement Length Retrieval
        Define __len__(self) to return the queue length.

        Use return len(self.q).
        
        Args:
            self: the object itself
        
        Returns:
            len(self.q): returns the length of the queue
        '''

        return (len(self.q)) # return the length of the queue


    def __eq__(self,other):
        '''
        8. Implement Equality Check
        Define __eq__(self, other) to compare two Queue instances.

        Ensure that other is a Queue instance.
        Compare self.q and other.q lists.
        
        Args:
            self: the object itself
            other: the other object to compare to the queue 
        
        Returns:
            self.q == other.q: returns True if the queues are equal, else False
        '''

        if isinstance(other, Queue):
            return self.q == other.q
        else:
            return False
    

    def __add__(self,other):
        '''
        9. Implement Addition
        Define __add__(self, other) to concatenate two queues.
    
        Return a new Queue instance with combined elements (Queue(self.q + other.q)).    
        
        Args:
            self: the object itself
            other: the other object to add to the queue
            
        Returns:
            Queue(newq): returns a new Queue instance with combined elements
'''

        newq = self.q + other.q
        return Queue(newq) # return a new Queue instance with combined elements

    def __contains__(self, item):
        '''
        This wasn't in the original requirements provided, but the doctest indicated that
        the __contains__ method was needed as there were two tests that were implemented
        to show a success and a failure testing if something was in the queue.
        
        Args:
            item: the item to check if it is in the queue
        
        Returns:
            item in self.q: returns True if the item is in the queue, else False
        '''

        return item in self.q

    def __iter__(self):
        '''
        There was another test in doctest7.py that was testing the __iter__ method.  The
        following method was added to the Queue class to pass the doctest7 testing.
        
        Args:
            self: the object itself
        
        Returns:
            iter(self.q): returns the iterator of the queue
        '''
    
        return iter(self.q)

    # Test the Queue class
    # Do not remove the code below

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))
#    print(doctest.testfile('mydoctest7.py')) # used to test my questions

