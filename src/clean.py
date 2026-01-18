import pandas as pd
from src import check_type as ch
from src import inference, metadata
import json, datetime, time

# data types cleaning function
def types_clean(df:pd.DataFrame)->pd.DataFrame:

    # tmp = 0

    for column in df.columns:
        valid_cells = df[column].dropna()
        
        if valid_cells.empty:
            continue
            
        first_cell = valid_cells.iloc[0]

        dtype = "object"

        # int
        if ch.is_int(first_cell):
            df[column] = df[column].astype('int64')
            # print('int!'); tmp += 1 
            dtype = "int64"

        # float
        elif ch.is_float(first_cell):
            df[column] = df[column].astype('float64')
            # print('float!'); tmp += 1
            dtype = "float64"

        # date
        elif ch.is_date(first_cell):
            df[column] = pd.to_datetime(df[column], format="%Y-%m-%d", errors='coerce')
            # print('date!'); tmp += 1 
            dtype = "date"
        
        # time
        elif ch.is_time(first_cell):
            df[column] = pd.to_datetime(df[column], format="%H:%M:%S", errors='coerce')
            # print('time!'); tmp += 1 
            dtype = "time"

        # timestamp
        elif ch.is_timestamp(first_cell):
            df[column] = pd.to_datetime(df[column], format="%Y-%m-%d %H:%M:%S", errors='coerce')
            # print('timestamp!'); tmp += 1 
            dtype = "timestamp"

        else:
            dtype = "string"
        
        info = {"dtype": dtype}

        metadata.add(column, info, '../metadata.json')

        """
            if there is a column typed time 
            and it's date in other column
            obviously we should combine them
            but not now
        """

        # object will remain as it is 

        # print(tmp)
    return df 

# Clean duplicated values
def duplicates(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:

        # if it's id so we need to delete any duplicates
        if metadata.get(col, "business_type") == "id":
            df = df.drop_duplicates(subset=[col], keep='first')
            # print('done id hehe')


    return df