import json

class item:
    def __init__(self, name: str, description: str, id: str, category: [str]):
        self.name = name
        self.description = description
        self.id = id
        self.category = category

    def fav_item(self):
        #if is already favorited then will clear it, otherwise will add it :>
        i = 0
        for each in self.category:
            if each == "favorite":
                self.category.pop(i)
                pass
            i += 1
        self.category.append("favorite")


    def get_stats(self):#when we want to use an item that is useable in things like combat
        #here we shall look for the relevent catagory!

        #im making it so several stats could exisit at once so you could load all of them into a list and retrn that
        #made for unstackables.... nad only them... dear god dont make me mix magic and other stuff

        #stats = []
        if "melee" in self.category:
            #go melee file and load the stats:
            #dmg, base_durability
            pass
        if "ranged" in self.category:
            #go ranged file and load the stats:
            #dmg, base_durability
            pass
        if "magic" in self.category:
            #go magic file and load the stats:
            #dmg, base_durability, effects
            pass
        if "armor" in self.category:
            #go armor file and load the stats:
            #base_durability, slot, dmg_reduction
            pass
        if "potion" in self.category:
            #go potion file and load the stats:
            #effects, uses
            pass
        if "unstackable" in self.category:
            #go unstackable file and load the stats:
            #durability
            pass
        #return stats

    def create_ustackable(self):
        #take an existing item and add a sub id to it to track it for later
        #check file for all sub ids
        pass

class inventory:
    def __init__(self, list: [item], id: str):
        self.list = list
        #well i figured it out, wrtoe it down iin the dev chan, might work on it between classes if i feel like it so we
        #could make SOME progress other then foundation building in this file

        # id is to know to whos inventory to allocate it
        pass

    def save_inv(self):
        #load list to file
        pass

    def load_inv(self):
        #load list from file to here
        pass

class person_inventory(inventory): #sec list is what is equiped, since its just an item list we can check the base stats
    #from the original id and current durability using the sub id, since its a string it a matter of splitting the _nums
    #from it ¯\_(ツ)_/¯

    #id is to know to whos inventory to allocate it
    def __init__(self, list: [item], equipment:[item], id: str):
        super.__init__(list, id)
        pass

    def save_person(self):
        #saves all the equipped items in a file
        pass
