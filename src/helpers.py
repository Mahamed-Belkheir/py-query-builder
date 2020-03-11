def keys_and_values(**kwargs):
    conditions = ""

    for condition in kwargs:
        conditions += condition + "=" + kwargs[condition]+" AND "

    return conditions[:-5:]

def keys_with_values(**kwargs):
    keys = ""
    values = ""
    for key, value in kwargs.items():
        keys += key +", "
        values += value +", "

    return keys[:-2:], values[:-2:]

def keys_only(args):
    keys = ""
    for key in args:
        keys += key + ", "

    return keys[:-2:]