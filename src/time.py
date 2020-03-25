from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

def today(format = "%m/%d/%Y"):
    """Returns today as a string with an optional parameter called format.
       Parameters:
           format: The way you want to display the data, 
           as default the same format as datetime. Optional.
                   As a default, it starts with a %m/%d/%Y format.
                   
       Output: String
    """
    return date.today().strftime(format)

def strToDate(date, format = "%m/%d/%Y"):
    """Converts a String into a Date.
       Parameters:
           date: A date as a string.
           format: The way you want to display the data,
           as default the same format as datetime. Optional.
                   As a default, it starts with a %m/%d/%Y format.
                   
       Output: Date
    """
    try:
        return datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Incorrect date format, should be", format)

def dateToStr(date, format = "%m/%d/%Y"):
    """Converts a Date into a String.
       Parameters:
           date: A date as a Date.
           format: The way you want to display the data, 
           as default the same format as datetime. Optional.
                   As a default, it starts with a %m/%d/%Y format.
                   
       Output: String
    """
    try:
        return datetime.strftime(date, format)
    except ValueError:
        raise ValueError("Incorrect date format, should be", format)
        
def nextDay(day, format = "%m/%d/%Y"):
    """Returns next day by full nume.
       Example: nextDay("Friday")
       Parameters:
           day: Day of the week as a string. For example, friday. The function is not case sensitive.
           format: The way you want to display the data, 
           as default the same format as datetime. Optional.
                   As a default, it starts with a %m/%d/%Y format.
       
       Output: String
    """
    try:
        date = datetime.now()

        while(date.strftime("%A").lower() != str(day).lower()):
            date += timedelta(1)

        return date.strftime(format)
    except ValueError:
        raise ValueError("Incorrect date format, should be", format)

def prevDay(day, format = "%m/%d/%Y"):
    """Returns previous day by full nume.
       Example: prevDay("Friday")
       Parameters :
           day    : Day of the week as a string. For example, friday. The function is not case sensitive.
           format : The way you want to display the data, 
           as default the same format as datetime. Optional.
                    As a default, it starts with a %m/%d/%Y format.
       
       Output: String
    """
    try:
        date = datetime.now()

        while(date.strftime("%A").lower() != str(day).lower()):
            date -= timedelta(1)

        return date.strftime(format)
    except ValueError:
        raise ValueError("Incorrect date format, should be", format)

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
       
       Output: String
    """
    try:
        date = (datetime.strptime(date, format) if type(date) == str else (date if type(date) == datetime else None))
        
        if date:
            return (date + timedelta(days=+days, weeks=+weeks) + relativedelta(months=+months, years=+years)).strftime("%m/%d/%Y")
        else:
            raise TypeError("Given date", date, "is not of type String or Date.")
    except ValueError:
        raise ValueError("Incorrect date format, should be", format)

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
       
       Output: String
    """
    try:
        date = (datetime.strptime(date, format) if type(date) == str else (date if type(date) == datetime else None))
        
        if date:
            return (date - timedelta(days=+days, weeks=+weeks) - relativedelta(months=+months, years=+years)).strftime("%m/%d/%Y")
        else:
            raise TypeError("Given date", date, "is not of type String or Date.")
    except ValueError:
        raise ValueError("Incorrect date format, should be", format)