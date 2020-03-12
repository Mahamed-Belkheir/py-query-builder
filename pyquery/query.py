from .builders import builds

class Query:
    
    def __init__(self):
        self.data = {
            "columns": [],
            "table": "",
            "conditions": [],
            "values": [],
            "add_condition": "AND",
            "type": "",
            "direction": ""
        }

        self.builds = builds

    def select_(self, *columns):
        if (len(columns) < 1):
            self.data["columns"] = "*"
        else:
            self.data["columns"] = columns
        self.data["type"] = "SELECT"
        self.data["direction"] = "FROM"
        return self

    def from_ (self, table):
        self.data["table"] = table
        return self
    
    def into_(self, table):
        return self.from_(table)

    def insert_(self, *columns):
        self.select_(*columns)
        self.data["type"] = "INSERT"
        self.data["direction"] = "INTO"
        return self

    def values_(self, *values):
        self.data["values"].append(values)
        return self

    def where_ (self, **conditions):
        self.data["conditions"].append({
            "type": self.data["add_condition"],
            "conditions": conditions
        })
        return self

    def or_ (self):
        self.data["add_condition"] = "OR"
        return self

    def and_(self):
        self.data["add_condition"] = "AND"
        return self

    def build_ (self):
        build = self.builds[self.data["type"]]
        data = self.data
        return f"{build['start'](**data)} {build['target'](**data)} {build['payload'](**data)}"


    