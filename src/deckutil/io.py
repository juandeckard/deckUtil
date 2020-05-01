"""A module designed to make input more standarized with error handling included."""

__version__ = '0.1'                    # Version

# Imports
from json import load
from pandas import read_excel, read_csv
from xlrd import XLRDError

def readExcel(filename, sheet_name, header_row = 1, columns = None, location = "./io/input/"):
    """Lets you read any excel files and returns a dataframe.
       Parameters:
            filename    : Name of the file, no termination.
            sheet_name  : Name of the sheet to read.
            header_row  : Row where the header is, starting at 0. Optional.
                          As default 1.
            columns     : An array of strings, with the names of
                          the headers you want to read. Optional.
            location    : A string with the location of the file. Optional.
                Example : "./io/input/folders/to/your/file/"
                
       Example 1: This example can be found inside the Input Sandbox. This is a very basic
                 definition.
                
                     df = readExcel("pismo","Main",1,location = "./io/input/examples/")
                
       Example 2: This example shows how to use column selection. In this case, we will only
                 select the index and date columns from the sheet.
       
                     df = readExcel("pismo","Main",1,columns = ["index","date"],location = "./io/input/examples/")
                
       Output: Dataframe 
    """
    try:
        if type(header_row) == int: # Check for header_row type consistancy
                                    # Return a DataFrame if everything goes well.
            return read_excel(location + filename + ".xlsx", sheet_name = sheet_name, header = header_row - 1, usecols = columns) 
        else:                       # Raise error if type is not int.
            raise TypeError("Parameter header_row type " + type(header_row) + " most be int.")
    except FileNotFoundError:       # Raise error if file was not found.
        raise FileNotFoundError("Can't find the file with name " + location + filename + ".xlsx.")
    except XLRDError:               # Raise error if sheet was not found.
        raise XLRDError("Sheet " + sheet_name + " not found.")
    except Exception as ex:         # Raise general error from the standard error of read_excel.
        raise ValueError("Columns parameter got an unexpected value with the following error: " + ex)
        
def readJSON(filename, location = "./io/input/"):
    """Lets you read any json files and returns a python dict. 
       Parameters:
           filename    : Name of the file, no termination.
           location    : Location of the file. Optional.
               Example : "./io/input/folders/to/your/file/"
       
       Example: The following example can be found at the Input Sandbox section. It reads some random JSON file.
       
                    dict = readJSON("json","./io/input/examples/")
       
       Output: dict
    """
    try:
        with open(location + filename + '.json') as f: # Try to open file
            return load(f)                             # If the file could be opened, return the content as a dict.
    except FileNotFoundError:                          # Raise error if file not found.
        raise ("Can't find the file at " + location + filename + ".json.")
    except Exception as e:                             # Raise general error from load standard error.
        raise 
                
def readCSV(filename, header = None, columns = None, location = "./io/input/"):
    """Lets you read any CSV file and returns a dataframe.
       Parameters:
           filename    : Name of the file, no termination.
           header      : Row where the header is, starting at 0. Optional.
           columns     : An array of strings, with the names of
                         the headers you want to read. Optional.
           location    : Location of the file. Optional.
               Example : "./io/input/folders/to/your/file/"
       
       Example 1: The following example can be found at the Input Sandbox section. It reads some random CSV file.
       
                      csv = readCSV("csv", location = "./io/input/examples/")
       
       Example 2: The following is exactly the same as example 1, but selects only two columns.
       
                      csv = readCSV("csv", location  = "./io/input/examples/", columns = ["rooms", "bathrooms"])
       
       Output: Dataframe
    """
    try:
        if type(header) == int: # Check if header is an int, return read_csv with header.
            return read_csv(location + filename + ".csv", header = header - 1, usecols = columns)
        elif header == None:    # Check if there is no header, return basic read_csv.
            return read_csv(location + filename + ".csv", usecols = columns)
        else:                   # Raise error with header type.
            raise TypeError("Type of header most be int or None value, got " + type(header) +".")
    except FileNotFoundError:   # Raise error if file not found.
        raise ("Can't find the file at " + location + filename + ".csv.")
    except Exception as e:      # Raise general error from load standard error.
        raise