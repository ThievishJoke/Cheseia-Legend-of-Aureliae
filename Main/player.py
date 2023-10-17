"""
here will be the file that will define all player logic
17th of october: making the player class basics and trying to make an inventory system for the player
the idea for the inventory is as follows: 
- I wanted to make an inventory class that will work more or less the same for all the things that have one
  with the player and player stashes (idk if they will be added or not) to be always saved in the save of the game
  and called for when needed (when crafting or when opening up the inventory)
  npc inventories are another thing, I don't want to have them loaded on the RAM for the entire game so a similar
  thing of loading on interaction will be made, I think for example shops will have a loot table to get what they
  sell and after its loaded they get a seed of sorts that will be placed in a JSON file with their npc ID
  so when you go to interact with them, they can decipher the seed and load the inventory meaning you need to keep
  track of fewer things in the save file, that should be simple.
  a similar system can be used to the players inventory whe I think about it, more heavy on the cpu but less ram usage
  I mean come on how hard would it be to decipher the first letter of an item and a number lol
  as per saving prices that will come later, today I focus on the player and try to make a general inventory class
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
        for item in x:
            inv_name = re.split(r"([a-zA-Z]+)", item)
            if inv_name[1] == item.inventory_name:
                number = int(inv_name[0]) + amount
                change = str(number) + inv_name[1]
                self.seed = re.sub(item, change, self.seed)
                break
        # if not lets just append it to the inventory string
        self.seed = self.seed + str(amount) + item.inventory_name

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
        self.inventory = ""  # empty seed is empty inventory


a = Species("cat person", 100, 50, 10, 5, 2, [None], 80, 5)

c = Class("knight", 2, 3, 0, 4, 0, 5, ["for the glory"])

b = Player(a, "Lina", [0, 0], "idk some magic shit", "female", ["cute", "funny"], c)
