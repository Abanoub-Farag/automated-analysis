import pandas as pd
import datetime, time

# check if a value is int or not
def _is_int(x):
    try:
        return float(x).is_integer()
    
    except (ValueError, TypeError):
        return False

# check if a value is a float or not
def _is_float(x):
    try:
        val = float(x)
        return not val.is_integer()
    except (ValueError, TypeError):
        return False

# check if a value is a date or not
def _is_date(x):
    if isinstance(x, (pd.Timestamp, datetime.date, datetime.datetime)):
        return True
    try:
        time.strptime(str(x), "%Y-%m-%d")
        return True
    except ValueError:
        return False


# check if a value is a time or not
def _is_time(x):
    try:
        time.strptime(str(x), "%H:%M:%S")
        return True
    except ValueError:
        return False
    

# check if a value is a timestamp or not
def _is_timestamp(x):
    if isinstance(x, (pd.Timestamp, datetime.datetime)):
        return True
    try:
        time.strptime(str(x), "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False

# main function 
def types_clean(df:pd.DataFrame)->pd.DataFrame:

    tmp = 0

    for column in df.columns:
        valid_cells = df[column].dropna()
        
        if valid_cells.empty:
            continue
            
        first_cell = valid_cells.iloc[0]

        # int
        if _is_int(first_cell):
            df[column] = df[column].astype('int64')
            print('int!'); tmp += 1 

        # float
        if _is_float(first_cell):
            df[column] = df[column].astype('float64')
            print('float!'); tmp += 1 

        # date
        elif _is_date(first_cell):
            
            df[column] = pd.to_datetime(df[column], format="%Y-%m-%d", errors='coerce')
            print('date!'); tmp += 1 
        
        # time
        elif _is_time(first_cell):
            df[column] = pd.to_datetime(df[column], format="%H:%M:%S", errors='coerce')
            print('time!'); tmp += 1 

        # timestamp
        elif _is_timestamp(first_cell):
            df[column] = pd.to_datetime(df[column], format="%Y-%m-%d %H:%M:%S", errors='coerce')
            print('timestamp!'); tmp += 1 

        """
            if there is a column typed time 
            and it's date in other column
            obviously we should combine them
            but not now
        """

        print(tmp)
    return df  