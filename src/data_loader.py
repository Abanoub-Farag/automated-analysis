import pandas as pd
import os
import json

def load_data(path: str) -> pd.DataFrame:
    _, ext = os.path.splitext(path)
    ext = ext.lower()
    
    # csv
    if ext == '.csv':
        return pd.read_csv(path)
    
    # excel
    excel_formats = ['.xlsx', '.xls', '.xlsb', '.xlsm', '.ods']
    if ext in excel_formats:
        return pd.read_excel(path)
    
    # josn
    # if ext == '.json':
    #     with open(path, 'r', encoding='utf-8') as f:
    #         data = json.load(f)
    #     try:
    #         if isinstance(data, list):
    #             return pd.DataFrame(data)
        
    #         if isinstance(data, dict):
    #             return pd.DataFrame.from_dict(data, orient='index')
            
    #         else: return pd.json_normalize(data)
            
    #     except json.JSONDecodeError:
    #         return pd.read_json(path, lines=True)
    if ext == '.json':
        try:
            return pd.read_json(path)
        
        except ValueError as e:
            try:
                return pd.read_json(path, orient='records')
            except ValueError:
                pass 
            
            return pd.read_json(path, lines=True)

    # unsupported files
    raise ValueError(f"File format '{ext}' is not supported.")