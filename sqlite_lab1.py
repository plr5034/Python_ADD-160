'''
sqlite lab 1
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/sqlite_lab1.py

The First Python Sqlite lab creates some SQLite3 Todo List Application functions

Our TODO application requires you to add a little security and display the data
saved in the database. Your task is to implement the following functionalities:

Create a find_task method, which takes the task name as its argument. The 
method should return the record found or None otherwise. Block the ability
to enter an empty task (the name cannot be an empty string). Block the ability
to enter a task priority less than 1.  Use the find_task method to block the
ability to enter a task with the same name. Create a method called show_tasks,
responsible for displaying all tasks saved in the database.

Test data:

Example input:
Enter task name: My first task
Enter priority: 1

Example output:
(1, 'My first task', 1)

Example input:
Enter task name: My second task
Enter priority: 2

Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)

Example input:
Enter task name: My first task
Enter priority: 1

Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)

'''
import sqlite3

class Todo:
    '''
    Todo class to manage a simple todo list using SQLite3
    '''

    def __init__(self):
        '''
        Initialize the Todo class and create a database connection
        '''
        # Connect to the SQLite database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()
        
    def create_task_table(self):
        '''
        Create the tasks table if it doesn't exist
        args:
            None
        return:
            None
        '''
        # Create a table to store tasks
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')
    def add_task(self):
        '''
        Add a new task to the database
        args:
            None
        return:
            None
        '''
        task_name = input('Enter task name: ')
        task_priority = int(input('Enter priority: '))
        
        # Check for empty task name and priority less than 1
        if task_name == '':
            print('Task name cannot be empty')
            return
        elif task_priority < 1:
            print('Task priority must be greater than 0')
            return
        
        # Check for duplicate task names
        if self.find_task(task_name) is not None:
            print('Task with this name already exists')
            return
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (task_name, task_priority))
        self.conn.commit()
    
    def show_tasks(self):
        '''
        Display all tasks in the database
        args:
            None
        return:
            None
        '''
        c = self.conn.cursor()
        for row in c.execute('SELECT * FROM tasks'):
            print(row)

    def find_task(self, my_task_name):
        '''
        Find a task by its name
        args:
            task_name: The name of the task to find
        return:
            The task record if found, None otherwise
        '''
        my_cursor = self.conn.cursor()
        my_cursor.execute('SELECT * FROM tasks WHERE name = ?', (my_task_name,))
        return my_cursor.fetchone()

#     input validation

app = Todo()
print()
app.add_task()
print()
app.show_tasks()
