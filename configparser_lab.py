'''
configparser lab
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/configparser_lab.py

This application will read in the mess.ini file and create two files named 
prod_config.ini and dev_config.ini. The prod_config.ini file should only 
contain sections for the production environment, while dev_config.ini should
only contain sections for the development environment.

To distinguish between the environments, use the env option added to all 
sections in the mess.ini file. The env option should be removed from the
sections before moving them to the files.

The script will  be one class named ConfigSeparator. 
The class will have the following methods:

* read_config: Reads the configuration file and returns a ConfigParser object.
* separate_config: Separates the configuration sections based on env.  Will 
separate the sections into two ConfigParser objects, one for production and
one for development.
* write_config: Writes the separated configuration sections to the appropriate
files.

Expected result
The prod_config.ini file:

[sentry]
key = key
secret = secret

[github]
user = user
password = password


The dev_config.ini file:

[mariadb]
host = localhost
name = hello
user = user
password = password

[redis]
host = localhost
port = 6379
db = 0
'''

import configparser

class ConfigSeparator:
    """
    Class to separate configuration sections based on environment.
    aka env area of the original file
    """

    def __init__(self, input_file):
        """
        Initialize the ConfigSeparator with the input file path.
        
        Args:
            input_file (str): Path to the input configuration file.
        """
        self.input_file = input_file

    def read_config(self):
        '''
        Read the configuration file and return a ConfigParser object.
        
        args:
            None
        returns:
            config (ConfigParser): ConfigParser object with the configuration.
        '''
        config = configparser.ConfigParser()
        try:
            with open(self.input_file, 'r', encoding="utf-8") as file:
                config.read_file(file)
                return config
        except FileNotFoundError:
            print(f"Error: File not found: {self.input_file}")
            return None
        except configparser.Error as e:
            print(f"Error reading configuration file: {e}")
            return None

    def separate_config(self, config):
        '''
        Separate the configuration sections based on the environment.
        
        args:
            config (ConfigParser): ConfigParser object with the configuration.
        returns:
            prod_config (ConfigParser): ConfigParser object for 
            the production environment.
            dev_config (ConfigParser): ConfigParser object for the
            development environment.
        '''
        my_prod_config = configparser.ConfigParser()
        my_dev_config = configparser.ConfigParser()

        for section in config.sections():
            env = config.get(section, 'env')
            if env == 'prod':
                my_prod_config[section] = {
                    key_config: value_config for key_config,
                    value_config in config.items(section) if key_config != 'env'}
            elif env == 'dev':
                my_dev_config[section] = {
                    key_config: value_config for key_config,
                    value_config in config.items(section) if key_config != 'env'}
        return my_prod_config, my_dev_config

    def write_config(self, config, output_file):
        '''
        Write the configuration sections to a file.
        
        args:
            config (ConfigParser): ConfigParser object with the configuration.
            output_file (str): Path to the output configuration file.
        returns:
            None
        '''
        with open(output_file, 'w', encoding="utf-8") as configfile:
            config.write(configfile)
        print(f"Configuration written to {output_file}")

if __name__ == "__main__":
    # Define the input and output file names
    PROD_CONFIG_FILE = 'prod_config.ini'
    DEV_CONFIG_FILE = 'dev_config.ini'
    INPUT_CONFIG_FILE = 'mess.ini'

    separator = ConfigSeparator(INPUT_CONFIG_FILE)
    
    # Read the configuration file
    orig_config = separator.read_config()
    if orig_config is not None:
        # Separate the configuration sections
        prod_config, dev_config = separator.separate_config(orig_config)
        
        # Write the separated configurations to two new files
        separator.write_config(prod_config, PROD_CONFIG_FILE)
        separator.write_config(dev_config, DEV_CONFIG_FILE)
        SystemExit(0)
    else:
        print("Failed to read the configuration file.")
        SystemExit(1)
