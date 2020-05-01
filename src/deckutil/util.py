"""A module designed to keep a few functions that have no category."""

__version__ = '0.1'

from pandas import DataFrame
from src.exceptions import EmptyListError

def sortByList(List, Data, Index = 0):
    """Sorts DataFrames, List of Lists or List of Tuples in relation to a List.
       Parameters:
           List  : The List you want to order the items from Data as.
           Data  : The DataFrame, List of Lists or List of Tuple you want to organize by that List.
           Index : The Index inside the Dataframe, List or Tuple that you want to organize. Optional.
                   Defaults to 0.
                   
       Example   : We will wort one list in relation to another. In this case, we will sort listb in relation to lista. It will en up reverting the list.
       
                       lista = [4,3,2,1,0]
                       listb = [[0,9],[1,52],[2,41],[3,2],[4,12]]
                       
                       sorted_list = sortByList(lista, listb)
                       
       Output    : Dataframe, List of Lists or List of Tuples
    """
    if type(Data) == DataFrame:                                 # Check if DataFrame
        try:
            return Data.reindex(List)                           # If DataFrame, reindex
        except:                                                 # Raise standard error if something happens.
            raise RuntimeError("Couldn't resize the DataFrame with the given list.")
    elif type(Data) == list:                                    # Check if Data is a list.
        if len(Data)>0:                                         # Check if Data is not an empty list.
            if type(Data[0]) == list or type(Data[0]) == tuple: # Check if elements are lists or tuples.
                                                                # Return sorted list.
                return [tuple for x in List for tuple in Data if tuple[Index] == x]
            else:                                               # Raise error if data is not supported.
                raise TypeError("This function doesn't support " + type(Data[0]) + " type.")
        else:
            raise EmptyListError                                # Raise error if list is empty.
            
def describeData(data, columns=None):
    """Shows significant data about a DataFrame, List of Lists or List of Tuples.
       Parameters  :
           data    : Data to be used, either a DataFrame, a List of Lists or a List of Tuples.
           columns : Column names for the data. Optional, not needed if using DataFrames.
           
       Example     : In this case from the Sandbox, we can get a description of our data.
       
                         data    = [[0, 1, 2],[3, 4, 5]]
                         columns = ["col1", "col2", "col3"]
                         
                         describeData(l,c)
           
       Output      : DataFrame
    """
    if type(data) == DataFrame:
        return data.describe()
    elif type(data) == list:
        if len(data) > 0: # Check that list is not empty
            if type(data[0]) == list:
                if columns == None: # Check if columns can be ignored
                    return DataFrame(data).describe()
                else:               # If columns are given, use them to name the data.
                    if len(data[0]) == len(columns):
                        return (DataFrame(data, columns=columns)).describe()
                    else: # Raise error if there is a column mismatch.
                        raise ValueError("Size of columns should match size of data, but size " + len(data[0]) + " does not match with " + len(columns) + ".")
            elif type(data[0]) == tuple:
                return DataFrame(data, columns=columns).describe()
            else: # Raise error if inner elements are not supported.
                raise TypeError("Type of inner data " + type(data[0]) + " not supported.")
        else: # Raise error if data is empty.
            raise EmptyListError
    else: # Raise error if data is not a list of lists, list of tuples or Dataframe
        raise TypeError("Type of outer data " + type(data) + " not supported.")

def dataInfo(data,columns=None):
    """Displays technical data about the DataFrame, List of Lists or List of Tuples.
       Parameters  : 
           data    : Data to be used, either a DataFrame, a List of Lists or a List of Tuples.
           columns : Column names for the data. Optional, not needed if using DataFrames.
           
       Example     : In this case from the Sandbox, we can get info about our data.
       
                         data    = [[0, 1, 2],[3, 4, 5]]
                         columns = ["col1", "col2", "col3"]
                         
                         dataInfo(l,c)
           
       Output      : None
    """
    if type(data) == DataFrame:
        data.info()
    elif type(data) == list:
        if len(data) > 0: # Check that list is not empty
            if type(data[0]) == list or type(data[0]) == tuple:
                if columns == None: # Check if columns can be ignored
                    DataFrame(data).info()
                else:               # If columns are given, use them to name the info.
                    if len(data[0]) == len(columns):
                        DataFrame(data, columns=columns).info()
                    else: # Raise error if there is a column mismatch.
                        raise ValueError("Size of columns should match size of data, but size " + len(data[0]) + " does not match with " + len(columns) + ".")
            else: # Raise error if inner elements are not supported.
                raise TypeError("Type of inner data " + type(data[0]) + " not supported.")
        else: # Raise error if data is empty.
            raise EmptyListError
    else: # Raise error if data is not a list of lists, list of tuples or Dataframe
        raise TypeError("Type of outer data " + type(data) + " not supported.")