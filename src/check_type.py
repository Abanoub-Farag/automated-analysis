import pandas as pd
import datetime, time

# check if a value is int or not
def is_int(x):
    try:
        return float(x).is_integer()
    
    except (ValueError, TypeError):
        return False

# check if a value is a float or not
def is_float(x):
    try:
        val = float(x)
        return not val.is_integer()
    except (ValueError, TypeError):
        return False

# check if a value is a date or not
def is_date(x):
    if isinstance(x, datetime.date):
        return True
    try:
        time.strptime(str(x), "%Y-%m-%d")
        return True
    except ValueError:
        return False


# check if a value is a time or not
def is_time(x):
    try:
        time.strptime(str(x), "%H:%M:%S")
        return True
    except ValueError:
        return False
    

# check if a value is a timestamp or not
def is_timestamp(x):
    if isinstance(x, (pd.Timestamp, datetime.datetime)):
        return True
    try:
        time.strptime(str(x), "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False