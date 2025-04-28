'''
XML lab 1
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/xml_lab1.py

Python XML lab reads an XML file and parses it to extract weather information.

Create a class named TemperatureConverter and its convert_celsius_to_fahrenheit
method. The convert_celsius_to_fahrenheit method should convert the temperature
from Celsius to Fahrenheit. Use the following formula:

F = 9/5 * C + 32.

Create a class named ForecastXmlParser and its parse method responsible for
reading data from forecast.xml. Use the TemperatureConverter class to convert
the temperature from Celsius to Fahrenheit (rounded to one decimal place). The
parse method should print the following results:

Monday: 28 Celsius, 82.4 Fahrenheit
Tuesday: 27 Celsius, 80.6 Fahrenheit
Wednesday: 28 Celsius, 82.4 Fahrenheit
Thursday: 29 Celsius, 84.2 Fahrenheit
Friday: 29 Celsius, 84.2 Fahrenheit
Saturday: 32 Celsius, 89.6 Fahrenheit
Sunday: 33 Celsius, 91.4 Fahrenheit

'''
class TemperatureConverter:
    '''
        Convert the temperature from Celsius to Fahrenheit (rounded to one
        decimal place)
    '''

    def __init__(self, temp_celsius):
        self.celsius = int(temp_celsius)

    def convert_celsius_to_fahrenheit(self):
        '''
            Convert the temperature from Celsius to Fahrenheit

            args:
                None
            return:
                Temperature in Fahrenheit
        '''
        return round((self.celsius * 9 / 5) + 32, 1)

class ForecastXmlParser:
    '''
        Parse the XML data from the a file and print the weather
        information to the console.
        The XML data is expected to be in the following format:
        <data>
            <item>
                <day>
                <temperature_in_celsius>20</temperature_in_celsius>
    '''

    def __init__(self, xml_data_file):
        self.xml_data_file = xml_data_file
        self.day_index = 0
        self.temperature_in_celsius_index = 1

    def parse(self):
        '''
            Parse the XML data and print the weather information
        
            args:
                None
            return:
                Print the weather information to the console
        '''
        # Parse the XML data

        import xml.etree.ElementTree as ET

        tree = ET.parse(self.xml_data_file)

        root = tree.getroot()

        for item in root:
            converted_temp = TemperatureConverter(item[1].text)
            new_temp = converted_temp.convert_celsius_to_fahrenheit()
            print(f'{item[self.day_index].text}: {item[self.temperature_in_celsius_index].text}° Celsius, {new_temp}° Fahrenheit')

# run the script
if __name__ == '__main__':
    import sys
    import os

    # Check if the XML file exists
    if not os.path.exists('forecast.xml'):
        print('The forecast.xml file does not exist.')
        sys.exit(1)

    # Parse the XML data
    parser = ForecastXmlParser('forecast.xml')
    parser.parse()
