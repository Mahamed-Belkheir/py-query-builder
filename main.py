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


class Query:
    
    def __init__(self):
        self.columns = []
        self.table = ""
        self.conditions = []
        self.values = []
        self.add_condition = "AND"
        self.type = ""
        self.direction = ""
        self.builds = {}
        self.builds['SELECT'] = {
            "start": self._select_start,
            "target": self._select_target,
            "payload": self._select_payload
        }
        self.builds['INSERT'] = {
            "start": self._insert_start,
            "target": self._insert_target,
            "payload": self._insert_payload
        }

    def select_(self, *columns):
        if (len(columns) < 1):
            self.columns = "*"
        else:
            self.columns = columns
        self.type = "SELECT"
        self.direction = "FROM"
        return self

    def from_ (self, table):
        self.table = table
        return self
    
    def into_(self, table):
        return self.from_(table)

    def insert_(self, *columns):
        self.select_(*columns)
        self.type = "INSERT"
        self.direction = "INTO"
        return self

    def values_(self, *values):
        self.values.append(values)
        return self

    def where_ (self, **conditions):
        self.conditions.append({
            "type": self.add_condition,
            "conditions": conditions
        })
        return self

    def or_ (self):
        self.add_condition = "OR"
        return self

    def and_(self):
        self.add_condition = "AND"
        return self

    def build_ (self):
        build = self.builds[self.type]
        return f"{build['start']()} {build['target']()} {build['payload']()}"

    def _select_start(self):
        return f"SELECT {keys_only(self.columns)}"

    def _select_target(self):
        return f"FROM {self.table}"

    def _select_payload(self):
        string = keys_and_values(**self.conditions[0]["conditions"])
        
        for conds in self.conditions[1:]:
            string += " "+conds["type"]+" "
            string += keys_and_values(**conds["conditions"])
            
        return f"WHERE {string}"

    def _insert_start(self):
        return f"INSERT ({keys_only(self.columns)})"

    def _insert_target(self):
        return f"INTO {self.table}"

    def _insert_payload(self):
        string = f"VALUES ({keys_only(self.values[0])}),"

        for inputs in self.values[1:]:
            string += f"({keys_only(inputs)}),"

        return string[:-1:]
    

q = Query()

print(q.select_().from_('Users').where_(id="1", name="moh").or_().where_(id="2").build_())
print(q.insert_("id, name").into_("Houses").values_("1", "Red Villa").values_("2", "Big Flat").values_("3", "cottage in the woods").build_())
