adict = {
    "Apple" : {
    "Name" : "Apple",
    "Color" : "Red",
    "Taste" : "Sweet",
    "Shape" : "Round"
    },
    "Banana" : {
    "Name" : "Banana",
    "Color" : "Yellow",
    "Taste" : "Mellow",
    "Shape" : "Creseant"
    },
    "Orange" : {
    "Name" : "Orange",
    "Color" : "Orange",
    "Taste" : "Sweet",
    "Shape" : "Ball"
    }
}

'''for l_id, l_info in adict.items():
    print("\nLocation ID:", l_id)
for key,value in adict.items():
    print(l_id, value)
'''

'''bitch = ("dic", "cheese", "pen")
for (i, item) in enumerate("dic", start=1):
    print(i, item)'''

fuckery = {
    "curses": {
    "damn" : ["1","2","3"],
    "fuck" : ["4","5","6"],
    "shit" : ["7","8","9"]
    },
}

for (l_id, l_info) in fuckery["curses"].items():
    print("\nLocation ID:", l_id)
    for key in enumerate(l_info, start = 1):
        print(key, ":", l_info, ': ' + l_id)

'''def nested_dict_values_iterator(dict_obj):
    for value in dict_obj.values():
        if isinstance(value,dict):
            for v in nested_dict_values_iterator(value):
                yield v
        else:
            yield value

for value in nested_dict_values_iterator(adict) :
    print(value)'''

'''def nested_dict_values_iterator(dict_obj):
    for value in dict_obj.values():
        if isinstance(value,dict):
            for v in nested_dict_values_iterator(value):
                yield v
        else:
            if isinstance(value,dict):
                for x in nested_dict_values_iterator(value):
                    yield x
            else:
                yield value

for value in nested_dict_values_iterator(adict) :
    print(value)'''

#inventory
inventory = {}

def add_item(item, quantity):
  if item in inventory:
    inventory[item] += quantity
  else:
    inventory[item] = quantity

def remove_item(item, quantity):
  if item in inventory:
    inventory[item] -= quantity
    if inventory[item] <= 0:
      del inventory[item]
  else:
    print("Item not in inventory.")

def display_inventory():
  print("Current inventory:")
  for item, quantity in inventory.items():
    print(f"{item}: {quantity}")

add_item("apples", 10)
add_item("oranges", 5)
add_item("bananas", 8)
display_inventory()

remove_item("oranges", 3)
display_inventory()

#locations
locations = ["Paris", "London", "New York", "Tokyo", "Sydney"]

print("Please select a location from the following list:")
for i, location in enumerate(locations):
  print(f"{i+1}. {location}")

selected = int(input())

if selected > 0 and selected <= len(locations):
  print(f"You selected: {locations[selected-1]}")
else:
  print("Invalid selection.")