"""A module designed to help transform datastructures from one to another."""

__version__ = '0.1'

from xml.etree.ElementTree import Element, SubElement
from json import dumps, loads
from datetime import datetime

def jsonToXML(json, tag = "XML_Object", write=False, filename = "output"):
    """A basic tool to convert from JSON to XML. This tool MIGHT not take into account all possible scenarios,
    but should for most cases. Supports nested objects
       Parameters:
           json     : The JSON object/dict you want to transform. 
                      Note that since JSON objects are parsed as dict, both should work.
           tag      : The tag is the name of the object. XML_Object as default
           write    : A True or False value, if False, it will return instead of writing.
           filename : Name of the file, no termination. Default is output.xml.
       
       Example: An example of how to transform a random JSON file into an XML object. readJSON can be found at input.py for more information.
       
                    json_file  = readJSON("jason","./io/input/examples/")
                    
                    xml_object = jsonToXML(json_file)
       
       Output: If write=True, a file at io/output/ else, ElementTree.Element
    """
    root         = Element(tag)                # Makes a root with a tag that is going to be the title of the object.
    elements     = []
    keys, values = json.keys(), json.values()  # Unpack keys and values.
    
    for key, value in zip(keys, values):
        if type(value) == dict:                # Check if it's nested object
            root.append(jsonToXML(value, key)) # We use recursion to get nested objects.
        else:                                  # Else it's an attribute.
            elements.append(SubElement(root, key))
            elements[-1].text = str(value)
    if write:                                  # Check if the write flag is True
        try:
            # Try to write xml file.
            root.write(open('./io/output/' + filename + '.xml', 'w'), encoding='unicode')
        except:
            raise
    else:   # If not going to write, just return the root.
        return root
    
def jsonToString(json):
    """A basic tool to convert from JSON to String.
       Parameters:
           json  : The JSON object/dict you want to transform. 
                   Note that since JSON objects are parsed as dict, both should work.
       
       Example   : Turns a random dict into a string.
                       
                       json_file  = readJSON("jason","./io/input/examples/")
                       
                       string = jsonToString(json_file)
                       
       Output    : String
    """
    if type(json) == dict:     # Do type validation for dict
        try:
            return dumps(json) # Turn dict to string
        except Exception:      # Raise general exception
            raise Exception("Couldn't parse the JSON into a String.")
    else:                        # Raise error if type is not json
        raise TypeError("Type of string most be str, not " + type(json) + ".")
            
def stringToJSON(string):
    """A basic tool to convert from String to JSON.
       Parameters :
           string : The JSON as a string.
               Example: '{ "name":"John", "age":30, "city":"New York"}'
               
       Example    : Turns a string that looks like a JSON into a dict.
       
                        string = '{ "name":"John", "age":30, "city":"New York"}'
                        
                        dict   = stringToJSON(string)
               
       Output     : dict
    """
    if type(string) == str:
        try:
            return loads(string) # Parse string to dict
        except:                  # Raise general exception
            raise
    else:                        # Raise error if type is not string
        raise TypeError("Type of string most be str, not " + type(string) + ".")
        
def strToDate(date, format = "%m/%d/%Y"):
    """Converts a String into a Date.
       Parameters:
           date: A date as a string.
           format: The way you want to display the data,
           as default the same format as datetime. Optional.
                   As a default, it starts with a %m/%d/%Y format.
                   
       Example: Change str 01/01/2000 to Datetime.
       
                    date = strToDate("01/01/2000")
       
       Output: Date
    """
    try:
        return datetime.strptime(date, format)
    except ValueError: # Raise error if format is wrong.
        raise ValueError("Incorrect date format " + format + ".")

def dateToStr(date, format = "%m/%d/%Y"):
    """Converts a Date into a String.
       Parameters:
           date: A date as a Date.
           format: The way you want to display the data, 
           as default the same format as datetime. Optional.
                   As a default, it starts with a %m/%d/%Y format.
                   
       Example: Changes Datetime to str.
       
                    str = dateToStr(datetime.now())
       
       Output: String
    """
    try:
        return datetime.strftime(date, format)
    except ValueError: # Raise error if format is wrong.
        raise ValueError("Incorrect date format " + format + ".")