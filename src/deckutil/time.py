"""A module designed to work with datetime in a simplified manner."""

__version__ = '0.1'

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

def today(format = "%m/%d/%Y"):
    """Returns today as a string with an optional parameter called format.
       Parameters:
           format: The way you want to display the data, 
           as default the same format as datetime. Optional.
                   As a default, it starts with a %m/%d/%Y format.
                   
       Example: The following example gets you todays date on non-retarded format.
       
                    today = today("%d,%m,%Y")
                   
       Output: String
    """
    if type(format) == str: # Check if type of format is str, return todays date.
        return date.today().strftime(format)
    else:                   # Raise error if format is not a str.
        raise TypeError("Type of format needs to be str, not " + str(type(format)) + ".")
        
def nextDay(day, format = "%m/%d/%Y"):
    """Returns next day by full nume.
       Example: nextDay("Friday")
       Parameters:
           day: Day of the week as a string. For example, friday. The function is not case sensitive.
           format: The way you want to display the data, 
           as default the same format as datetime. Optional.
                   As a default, it starts with a %m/%d/%Y format.
       
       Example: This will get next monday date.
       
                    tomorrow = tomorrow("monday")
       
       Output: String
    """
    try:
        __date = datetime.now()                                   # Get todays date.

        while(__date.strftime("%A").lower() != str(day).lower()): # Loop until day name match.
            __date += timedelta(1)                                # Add a day.

        return __date.strftime(format)
    except ValueError:                                            # Raise error if format is incorrect.
        raise ValueError("Incorrect date format " + format + ".")

def prevDay(day, format = "%m/%d/%Y"):
    """Returns previous day by full nume.
       Example: prevDay("Friday")
       Parameters :
           day    : Day of the week as a string. For example, friday. The function is not case sensitive.
           format : The way you want to display the data, 
           as default the same format as datetime. Optional.
                    As a default, it starts with a %m/%d/%Y format.
       
       Example: This will get next friday date.
       
                    yesterday = yesterday("Friday")
       
       Output: String
    """
    try:
        __date = datetime.now()                                   # Get todays date.

        while(__date.strftime("%A").lower() != str(day).lower()): # Loop until day name match.
            __date -= timedelta(1)                                # Subtract a day.

        return __date.strftime(format)
    except ValueError:                                            # Raise error if format is incorrect.
        raise ValueError("Incorrect date format " + format + ".")

def addTime(date, days = 0, weeks = 0, months = 0, years = 0, format = "%m/%d/%Y"):
    """Adds time period to a given date.
       Parameters:
           date   : Date to transform. Can be a String or a Date.
           days   : Days to be added. Optional.
           weeks  : Weeks to be added. Optional.
           months : Months to be added, if you start at the 25th of March and add 3 months you will
                    end up in the 25th of June. Optional.
           years  : Years to be added. Optional.
           format : The way you want to display the data, 
           as default the same format as datetime. Optional.
                    As a default, it starts with a %m/%d/%Y format.
       
       Example: Lets add a few days, weeks, months and years.
       
                    newDate = addTime("01/01/2000",days = 4, weeks = 3, months = 10, years = 12)
       
       Output: String
    """
    try:
        date = (datetime.strptime(date, format) if type(date) == str else (date if type(date) == datetime else None)) # Normalize date input
        
        if date:
            return (date + timedelta(days=+days, weeks=+weeks) + relativedelta(months=+months, years=+years)).strftime("%m/%d/%Y")
        else:                      # Raise error if date type is not str or Datetime.
            raise TypeError("Given date " + date + " is not of type String or Date.")
    except ValueError:             # Raise error if format is incorrect.
        raise ValueError("Incorrect date format " + format + ".")

def subTime(date, days = 0, weeks = 0, months = 0, years = 0, format = "%m/%d/%Y"):
    """Subtracts time period to a given date.
       Parameters:
           date   : Date to transform. Can be a String or a Date.
           days   : Days to be subtracted. Optional.
           weeks  : Weeks to be subtracted. Optional.
           months : Months to be subtracted, 
           if you start at the 25th of March and subtract 3 months you will
                    end up in the 25th of December. Optional.
           years  : Years to be subtracted. Optional.
           format : The way you want to display the data, 
           as default the same format as datetime. Optional.
                    As a default, it starts with a %m/%d/%Y format.
       
       Example: Lets subtract a few days, weeks, months and years.
       
                    newDate = subTime("01/01/2000",days = 4, weeks = 3, months = 10, years = 12)
       
       Output: String
    """
    try:
        date = (datetime.strptime(date, format) if type(date) == str else (date if type(date) == datetime else None)) # Normalize date input
        
        if date:
            return (date - timedelta(days=+days, weeks=+weeks) - relativedelta(months=+months, years=+years)).strftime("%m/%d/%Y")
        else:                      # Raise error if date type is not str or Datetime.
            raise TypeError("Given date " + date + " is not of type String or Date.")
    except ValueError:             # Raise error if format is incorrect.
        raise ValueError("Incorrect date format " + format + ".")