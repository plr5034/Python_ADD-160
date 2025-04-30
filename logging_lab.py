'''
logging lab
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/logging_lab.py

This program that will simulate the recording of battery temperatures with
an interval of one minute. The simulation should contain 60 logs (the last 
hour).

To simulate temperatures, use one of the available random functions in 
Python. Temperatures should be drawn in the range of 20–40 degrees Celsius,
and then saved in the following format:

LEVEL_NAME – TEMPERATURE_IN_CELSIUS UNIT => DEBUG – 20 C

The drawn temperatures should be assigned to the appropriate level depending
on their value:

DEBUG = TEMPERATURE_IN_CELSIUS < 30
WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
CRITICAL = TEMPERATURE_IN_CELSIUS > 35

Put all logs in the battery_temperature.log file. The task will be completed
when you implement your own handler and formatter.

NOTE: Ran into a lot of issues with the handler.  Was getting multiple log 
entries for each temp generated.  Interesting thing was the number increase 
with the index.  So, by the last entry, there were 60 entries!  Didn't see
any mention of clearing the handler in the Python Institue course.  Found a
couple of references to duplicate entries due to not clearing the handler.  
I.E.:
https://santos-k.medium.com/solving-duplicate-log-entries-issue-in-python-logging-d4b1cad8e588
'''
import logging
import random

class MyLogger():
    '''
    Class to create a logger
    '''
    def __init__(self):
        pass

    def log_entry(self, level, mytemp, my_log_name):
        '''
        Function to log the temperature and level name
        args:
            level (str): level name
            mytemp (int): temperature in Celsius
            my_log_name (str): log file name
        returns:
            Makes log entry
        '''

        # debug message
#        print(f'Index: {index} - Level: {level} - Temperature: {mytemp} C')

        # log format
        FORMAT = '%(levelname)s - %(message)s'
        # create logger
#        logger = logging.getLogger(__name__)
        logger = logging.getLogger('BatteryTemperature')
        # set level
        logger.setLevel(logging.DEBUG)
        # check if handler already exists, if so remove it
        # else will get duplicate log entries
        if logger.hasHandlers():
            # remove all handlers
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)
        # create file handler - logs append not overwrite, so mode='a'
        handler = logging.FileHandler(my_log_name, mode='a')
        # set level
        handler.setLevel(logging.DEBUG)
         # create formatter
        formatter = logging.Formatter(FORMAT)
        # add formatter to handler
        handler.setFormatter(formatter)
        # add handler to logger
        logger.addHandler(handler)
#        print(f'Level: {level} - Temperature: {mytemp} C') # debug message
            # set level name
        if level == 'DEBUG':
            logger.debug("%s C", mytemp)
        elif level == 'WARNING':
            logger.warning("%s C", mytemp)
        elif level == 'CRITICAL':
            logger.critical("%s C", mytemp)
        else:
            logger.error("Error in log entry")

# this secion will be used to simulate the temperature
# loop for 60 minutes

if __name__ == '__main__':
    # create logger
    mylog = MyLogger()

    # constants and variables
    LOG_NAME = 'battery_temperature.log'
    START = 1
    MAXLEN = 60

    for index in range(START, MAXLEN + 1):
        # random temperature between 20 and 40
        temp_c = random.randint(20, 40)
        # set level name
        if temp_c < 30:
            level_name = 'DEBUG'
        elif temp_c >= 30 and temp_c <= 35:
            level_name = 'WARNING'
        else:
            level_name = 'CRITICAL'
        # print("making log entry:", index) # debug message to console
        # log entry
        mylog.log_entry(level_name, temp_c, LOG_NAME)
