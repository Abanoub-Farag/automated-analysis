import pandas as pd
import numpy as np
from src import check_type as ch
import re
from src import metadata

def is_pk(values: pd.Series)->bool:
    """
        values is a pandas series
        for a full column values
    """

    """
        Check if a column is an ID based
        on Uniqueness Ratio and Data Type.
    """

    valid = values.dropna()

    if valid.empty: 
        # print('all is nan!!!'); 
        return False

    type_:bool = (pd.api.types.is_integer_dtype(valid) or
                   pd.api.types.is_string_dtype(valid) or
                   pd.api.types.is_object_dtype(valid))

    # id is either object or INT
    if not type_:
        # print('type!!!!')
        return False

    """
        Calculating the uniqueness ratio
        to decide wheater it's id or not
    """
    n_unique = valid.nunique()
    n_total = len(valid)
    ratio = n_unique / n_total

    print(ratio)

    # unique values are equals to the legnth
    like_id = _look_like_pk(values.name)

    if ratio >= 0.95 and like_id:
        business_type = 'id'
        info = {"business_type" : business_type}
        metadata.add(values.name, info)
        return True

    return False







def _look_like_pk(col_name: str):
    maybe = [r'id', r'code', r'primary_key',
             r'pk', r'identity', r'unique',
             r'serial', r'\bkey\b', r'sku']
    
    pattern = r'|'.join(maybe)

    return bool(re.search(pattern, col_name, re.IGNORECASE))