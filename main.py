from src.query import Query  

q = Query()

print(q.select_().from_('Users').where_(id="1", name="moh").or_().where_(id="2").build_())
print(q.insert_("id, name").into_("Houses").values_("1", "Red Villa").values_("2", "Big Flat").values_("3", "cottage in the woods").build_())
