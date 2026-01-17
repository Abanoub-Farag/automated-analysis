import pandas as pd

def shape(df:pd.DataFrame):
    return df.shape

def description(df:pd.DataFrame):
    return df.describe()

def info(df:pd.DataFrame):
    return df.info()

def dtypes(df:pd.DataFrame):
    return df.dtypes