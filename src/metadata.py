import json, os
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return super(NpEncoder, self).default(obj)

def add(col_name: str, info: dict, path: str = '../metadata.json'):
    """
        Reads the JSON file, updates the 
        specific column info, and saves it back.
    """
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {"columns" : {}}
    
    else:
        data = {"columns" : {}}
    
    if "columns" not in data:
        data["columns"] = {}


    if col_name in data["columns"]:
        data["columns"][col_name].update(info)

    else:
        data["columns"][col_name] = info

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, cls=NpEncoder, indent=4)



def get(col_name: str = None, key: str = None, path: str = '../metadata.json'):
    if not os.path.exists(path):
        print(f"Error: Metadata file not found at {path}")
        return None
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return None
    
    if col_name not in data.get("columns", {}):
        return None
    
    col_data = data["columns"][col_name]
    return col_data.get(key) if key else None