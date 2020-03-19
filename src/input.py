import pandas as pd
import json
from xlrd import XLRDError

def readExcel(filename, sheet_name, header_row = 1, columns = None, location = "./io/input/"):
    """Lets you read any excel files and returns a dataframe.
       Parameters:
            filename    : Name of the file, no termination.
            sheet_name  : Name of the sheet to read.
            header_row  : Row where the header is, starting at 0.
            columns     : An array of strings, with the names of
                          the headers you want to read.
            location    : A string with the location of the file.
                Example : "./io/input/folders/to/your/file/"
                
       Output: Dataframe 
    """
    try:
        if type(header_row) == int:
            return pd.read_excel(location + filename + ".xlsx", sheet_name = sheet_name, header = header_row - 1, usecols = columns)
        else:
            print("Exception:","header_row type error.")
            return 3
    except Exception as e:
        if type(e) is FileNotFoundError:
            print("Exception:","Can't find the file with name", filename + ".")
            return 1
        elif type(e) is XLRDError:
            print("Exception:","Sheet",sheet_name,"not found.")
            return 2
        elif type(e) is ValueError:
            print("Exception:","columns parameter got an unexpected value with the followig error:")
            print(str(e) + '.')
            return 4
        else:
            print("Exception:","Something else haappened.", type(e))
            raise

def readJSON(filename, location = "./io/input/"):
    """Lets you read any json files and returns a python dict. 
       Parameters.
           filename: Name of the file, no termination.
           location: Location of the file
               Example : "./io/input/folders/to/your/file/"
       Output: dict
    """
    try:
        with open(location + filename + '.json') as f:
            return json.load(f)
    except Exception as e:
        if type(e) is FileNotFoundError:
            print("Can't find the file at",location + filename + ".json")
            return 1
        else:
            print(e)
            raise