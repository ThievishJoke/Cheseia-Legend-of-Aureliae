import json


class item:
    def __init__(self, name: str, description: str, value: int, id: str, category: [str]):
        self.name = name
        self.description = description
        self.value = value
        self.id = id
        self.category = category

    def get_item(self):
        #look at json file of all items and based on id find the class of the item
        #will be a function to load items from all inventories, chests and the like into things the game can use
        pass

    def fav_item(self):
        #if is already favorited then will clear it, otherwise will add it :>
        for each in self.category:
            if each == "favorite":
                self.category.pop(each)
                pass
        self.category.append("favorite")


class unstackable(item):
    def __init__(self, name: str, description: str, value: int, id: str, category: str):
        super().__init__(name, description, value, id, category)
        # go through all the itmes with number values in the entire game that are loaded in somwhere and decide
        # what nuber to give

        self.ID = id

class inventory:
    def __init__(self):
        self.list = []
        #fuck idk how i define a general inventory i will have to think about this, maybe make a few files and when you
        #make a new inv then you need to decide which file it uses?
        pass

    def save_inv(self):
        #load list to file
        pass

    def load_inv(self):
        #load list from file to here
        pass