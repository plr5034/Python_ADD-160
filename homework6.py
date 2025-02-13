'''
Homework6
Name:Paul Ring 
github link:https://github.com/plr5034/Python_ADD-160/blob/main/homework6.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.

Objective
By the end of this assignment, students will be able to:

Understand and implement the concepts of inheritance and composition in 
Python

Create a smart home system with multiple device classes

Demonstrate how inheritance and composition can be used together in a single
program

Instructions
Create a base class called Device that includes common attributes and methods
for all devices in the smart home system. Create an instance variable that
stores the name of the device and another that stores the status of the
device. In this case, the status is whether the device is on or off. Then, 
write code for a function that turns on and turns off a device. 

Sample Output:
When calling the turn_on function: Device1 is now ON. 
When calling the turn_off function: Device1 is now OFF

Create a subclass called Light that inherits from Device. Create an instance
variable for the brightness. Create a function called set_brightness. If the
brightness is between 0 and 100, change the brightness to the specified level.
Otherwise, say the input is invalid. 

Sample outputs: 
if brightness level is between 0 and 100: Device1 brightness set to 30. 
otherwise: Invalid brightness level. Must be between 0 and 100.

Create additional subclasses for specific types of lights, such as LEDLight
and SmartBulb, that inherit from Light. For the LEDLight subclass, create an
instance variable for the color of the light. In the set_color function, allow
the user to overwrite the color instance variable and display a message. 

Sample output: Device3 color changed to Blue. 

For the SmartBulb class, create an instance variable to store the brightness
and whether or not the bulb is in smart_mode (two instance variables total).
In the function enable_smart_mode, change the value of the smart_mode 
instance variable to true and print the message "Device4 smart mode enabled."
Similarly, in the function disable_smart_mode, change the instance variable
to false and print the message "Device4 smart mode disabled.". 

Remember: the SmartBulb inherits the Light class. This means I should be able
to call Light methods using the SmartBulb class. This test case will be used
in the doctest.

Test your program using the doctest before handing it in.
'''

class Device:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"

#    def change_dev_status(self, status):
#            self.status = status
#            print(f"{self.name} is now {self.status}")

    def turn_on(self):
        self.status = "ON"
        print(f"{self.name} is now {self.status}.")

    def turn_off(self):
        self.status = "OFF"
        print (f"{self.name} is now {self.status}.")

'''
The Light class inherits from Device class.
What is unique about this class is that it has a brightness level.  So, this
class will have a brightness instance variable.  

The set_brightness function will allow the user to change the brightness
level.  If the brightness level is between 0 and 100, change the brightness
to the specified level.  Else, let the user know the input is not invalid.

Sample outputs: if brightness level is between 0 and 100: Device1 brightness
set to 30. otherwise: Invalid brightness level. Must be between 0 and 100.
'''

class Light(Device):
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self.brightness = brightness
    
    def set_brightness(self, level):
        '''
        Test that level will be in a valid range
        '''
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.name} brightness set to {self.brightness}.")
        else:
            print("Invalid brightness level. Must be between 0 and 100.")

'''
The LEDLight class inherits from Light class.   So, this will inherit the 
device state and the light brightness level.
What is unique about this class is that it have a color.  This class will
have a color instance variable.  

The set_color function will allow the user to  allow the user to overwrite
the color instance variable and display a message.  While not part of the
original requirements, it would be good to have a valid list of colors to
check against.  If the color is not in the list, let the user know the input
is not invalid.

Sample output: Device3 color changed to Blue.
'''

class LEDLight(Light):
    def __init__(self, name, brightness=50, color="White"):
        super().__init__(name, brightness)
        self.color = color
        self.valid_colors = ["White", "Red", "Green", "Blue", "Yellow", "Purple"]

    def set_color(self, color):
        self.color = color
        if self.color in self.valid_colors:
            print (f"{self.name} color changed to {self.color}.")
        else:
            print (f"{self.color} is not a valid color.  Please use one of the following {self.valid_colors}.")

'''
The SmartBulb class also inherits from Light class.   So, again will inherit 
the device state and the light brightness level.
What is unique about this class is that it have a mode.  This class will
have a self.smart_mode instance variable.  

There are two functions that will allow the user to change the mode.  The
enable_smart_mode function will change the value of the smart_mode instance
to True and print the message "Device4 smart mode enabled.".  While the
disable_smart_mode function will change the value of the smart_mode instance
to False and print the message "Device4 smart mode disabled.".

Sample output: "Device4 smart mode enabled." or "Device4 smart mode disabled."
'''

class SmartBulb(Light):
    def __init__(self, name, brightness=50, smart_mode=False):
        super().__init__(name, brightness)
        self.smart_mode = smart_mode
    
    def enable_smart_mode(self):
        self.smart_mode = True 
        print(f"{self.name} smart mode enabled.")
    
    def disable_smart_mode(self):
        self.smart_mode = False
        print(f"{self.name} smart mode disabled.")

if __name__ == "__main__":
    import doctest
#    print(doctest.testfile('my_doctest.py'))
    print(doctest.testfile('testdoc6.py'))

