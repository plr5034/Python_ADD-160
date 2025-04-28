'''
sqlite lab 2
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/sqlite_lab2.py

The second Python Sqlite lab is a SQLite3 Todo List Application

Create a method called change_priority, responsible for updating task 
priority. The method should get the id of the task from the user and its new
priority (greater than or equal to 1).  Create a method called delete_task,
responsible for deleting single tasks. The method should get the task id from
the user.

Implement a simple menu consisting of the following options:

1. Show Tasks 
2. Add Task 
3. Change Priority 
4. Delete Task
5. Exit

where:

- Show Tasks (calls the show_tasks method)
- Add Task (calls the add_task method)
- Change Priority (calls the change_priority method)
- Delete Task (calls the delete_task method)
- Exit (interrupts program execution)

The program should obtain one of these options from the user, and then call the
appropriate method of the TODO object. Choosing option 5 must terminate the
program. A menu should be displayed in an infinite loop so that the user can
choose an option multiple times.

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

    def add_task(self):
        '''
        Add a new task to the database
        args:
            None
        return:
            None
        '''
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()
    
    def change_priority(self):
        '''
        Change the priority of an existing task
        args:
            None
        return:
            None
        '''
        print()
        task_id = int(input('Enter task ID to change priority: '))
        new_priority = int(input('Enter new priority: '))
        self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (new_priority, task_id))
        self.conn.commit()

    def delete_task(self):
        '''
        Delete a task from the database
        
        TODO: validate task_id is in the database

        args:
            task_id (int): the id of the task to delete
        return: 
            None
        '''
        print()
        task_id = input('Enter task ID to delete: ')
        try:
            task_id = int(task_id)
        except ValueError:
            print('Invalid input. Please enter a number.')
            return 0
        self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()

    def terminate(self):
        '''
        Close the database connection

        args:
            None
        return:
            None
        '''
        self.conn.close()

    def show_menu(self):
        '''
        Create a menu to show users options for the database`

        args:
            None
        return:
            None
        '''
        print()
        print('1. Show Tasks')
        print('2. Add Task')
        print('3. Change Priority')
        print('4. Delete Task')
        print('5. Exit')
        print()
        print('Select an option: ')
        menu_input = (input())
        try:
            menu_input = int(menu_input)
        except ValueError:
            print('Invalid input. Please enter a number.')
            return 0
        return menu_input

# Main program
# Create a new Todo object
# and display the menu

app = Todo()
looping = True
while looping:
    myselection = app.show_menu()
    if myselection == 1:
        app.show_tasks()
    elif myselection == 2:
        app.add_task()
    elif myselection == 3:
        app.change_priority()
    elif myselection == 4:
        app.delete_task()
    elif myselection == 5:
        app.terminate()
        looping = False
    else:
        print('Invalid selection')
