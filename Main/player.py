"""
here will be the file that will define all player logic
17th of october: all the goals have been achieved
18th of october: start working on races and making JSON's <too many fucking definitions with no functions yayyyyy >
"""
import re


class Species:
    def __init__(self, name, base_health, base_mana, base_magic_dmg, base_magic_resist, base_armor,
                 passive_abilities: list,
                 stamina, base_dmg):
        self.name = name
        self.baseHealth = base_health
        self.baseMana = base_mana
        self.base_magic_dmg = base_magic_dmg
        self.base_magic_resist = base_magic_resist
        self.base_armor = base_armor
        self.passive_abilities = passive_abilities
        self.stamina = stamina
        self.base_dmg = base_dmg


class Class:
    def __init__(self, name, bonus_dmg, bonus_mana, bonus_magic_dmg, bonus_health, bonus_magic_resist, bonus_armor,
                 passive_abilities: list):
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.bonus_mana = bonus_mana
        self.bonus_magic_dmg = bonus_magic_dmg
        self.bonus_health = bonus_health
        self.bonus_magic_resist = bonus_magic_resist
        self.bonus_armor = bonus_armor
        self.passive_abilities = passive_abilities


class Item:
    def __init__(self, name, inventory_name: str):
        self.name = name
        self.inventory_name = inventory_name


class Inventory:
    def __init__(self, seed: str):
        self.seed = seed

    def add_item(self, item: Item, amount):
        # find if already exists in inventory and add if it is there
        x = re.findall(r"(\d+[a-zA-z]+)", self.seed)
        for each_item in x:
            inv_name = re.split(r"([a-zA-Z]+)", each_item)
            if inv_name[1] == item.inventory_name:
                number = int(inv_name[0]) + amount
                change = str(number) + inv_name[1]
                self.seed = re.sub(each_item, change, self.seed)
                return  # if found and applied change then we are done!
        # if not, lets append it to the inventory string
        self.seed = self.seed + str(amount) + item.inventory_name

    def remove_item(self, item: Item, amount):
        # look for item in inventory and remove if you have enough to remove if not enough or none exist then return
        # None
        x = re.findall(r"(\d+[a-zA-z]+)", self.seed)
        for each_item in x:
            inv_name = re.split(r"([a-zA-Z]+)", each_item)
            if inv_name[1] == item.inventory_name:
                if int(inv_name[0]) >= amount:
                    number = int(inv_name[0]) - amount
                else:
                    return None  # return None if you don't have enough
                change = str(number) + inv_name[1]
                self.seed = re.sub(each_item, change, self.seed)
                pass
        return None  # if it gets to this point, that means we looped through the entire inventory and didn't find it


class Player:
    def __init__(self, species, name, location, affinity, gender, extra_passives: list, Class):
        # nerd shit
        self.species = species  # so I could inherit everything from species without being a subclass of it
        self.cords = location
        # self.city = do the things where you find where you are
        # self.region =
        self.affinity = affinity
        self.Class = Class
        extra_passives.extend(Class.passive_abilities)
        extra_passives.extend(species.passive_abilities)
        extra_passives = filter(None, extra_passives)
        # the shit we care about(actual stats)
        self.name = name
        self.gender = gender
        self.passive_abilities = extra_passives
        self.Health = species.baseHealth + Class.bonus_health
        self.armor = species.base_armor + Class.bonus_armor
        self.mana = species.baseMana + Class.bonus_mana
        self.magic_resist = species.base_magic_resist + Class.bonus_magic_resist
        self.inventory = Inventory("")  # empty seed is empty inventory


a = Species("cat person", 100, 50, 10, 5, 2, [None], 80, 5)

c = Class("knight", 2, 3, 0, 4, 0, 5, ["for the glory"])

b = Player(a, "Lina", [0, 0], "idk some magic shit", "female", ["cute", "funny"], c)

invn = Inventory("34io")
itm = Item("iron ore", "io")
invn.add_item(itm, 10)
invn.remove_item(itm, 50)
if invn.remove_item(itm, 50) is None:
    print("failed to remove item you don't have enough!")
print(invn.seed)
