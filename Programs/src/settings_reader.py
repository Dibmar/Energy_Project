# This python program reads the config file (settings.json) located in src
import json

def read_config(path):
    """
                        ---What it does---
    Loads a json file and turns it into a dictionary.
                        
                        ---What it needs---
        - The path to the file (path) in string format
    
                        ---What it returns---
    A dictionary (settings) with the contents of the json loaded
    """
    try:
        with open(path, 'r+') as outfile:
            settings = json.load(outfile)
                            
            return settings
        
    except Exception as error:
        raise ValueError(error)