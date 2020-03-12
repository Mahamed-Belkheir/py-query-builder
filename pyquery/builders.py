from .helpers import keys_and_values, keys_with_values, keys_only

def select_start(**data):
    return f"SELECT {keys_only(data['columns'])}"

def select_target(**data):
    return f"FROM {data['table']}"

def select_payload(**data):
    string = keys_and_values(**data["conditions"][0]["conditions"])
    
    for conds in data["conditions"][1:]:
        string += " "+conds["type"]+" "
        string += keys_and_values(**conds["conditions"])
        
    return f"WHERE {string}"


def insert_start(**data):
    return f"INSERT ({keys_only(data['columns'])})"

def insert_target(**data):
    return f"INTO {data['table']}"

def insert_payload(**data):
    string = f"({keys_only(data['values'][0])}),"

    for inputs in data["values"][1:]:
        string += f"({keys_only(inputs)}),"

    return f"VALUES {string[:-1]}"


builds = {}
builds['SELECT'] = {
    "start": select_start,
    "target": select_target,
    "payload": select_payload
}
builds['INSERT'] = {
    "start": insert_start,
    "target": insert_target,
    "payload": insert_payload
}