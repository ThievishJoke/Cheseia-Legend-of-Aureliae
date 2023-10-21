import re


class Species:
    def __init__(self, name, base_health, base_mana, base_magic_dmg, base_magic_resist, base_armor,
                 passive_abilities: list, base_movement,
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
        self.base_movement = base_movement


class Class:
    def __init__(self, name, bonus_dmg, bonus_mana, bonus_magic_dmg, bonus_health, bonus_magic_resist, bonus_armor,
                 passive_abilities: list, bonus_movement):
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.bonus_mana = bonus_mana
        self.bonus_magic_dmg = bonus_magic_dmg
        self.bonus_health = bonus_health
        self.bonus_magic_resist = bonus_magic_resist
        self.bonus_armor = bonus_armor
        self.passive_abilities = passive_abilities
        self.bonus_movement = bonus_movement


class Item:
    def __init__(self, name, inventory_name: str):
        self.name = name
        self.inventory_name = inventory_name


class equipable(Item):
    def __init__(self, durability, current_durability, name, inventory_name: str, enchantment: list):
        super().__init__(name, inventory_name)
        self.max_durability = durability
        self.current_durability = current_durability
        self.enchantments = enchantment

    def update_durability(self, durability):  # simple updating function when in use
        self.current_durability = durability


class Inventory:
    def __init__(self, seed: str):
        self.seed = seed

    def add_item(self, item: Item, amount):
        # find if already exists in inventory and add if it is there

        x = re.findall(r"(\d+{})".format(item.inventory_name), self.seed)
        if not x:
            # if not, lets append it to the inventory string
            self.seed = self.seed + str(amount) + item.inventory_name
            return
        inv_name = re.split(r"([a-zA-Z]+)", x[0])
        if inv_name[1] == item.inventory_name:
            number = int(inv_name[0]) + amount
            change = str(number) + inv_name[1]
            self.seed = re.sub(x[0], change, self.seed)
            return

    def remove_item(self, item: Item, amount):
        # look for item in inventory and remove if you have enough to remove if not enough or none exist then return
        # None

        x = re.findall(r"(\d+{})".format(item.inventory_name), self.seed)
        if not x:
            return None  # didn't find in inventory
        inv_name = re.split(r"([a-zA-Z]+)", x[0])
        if inv_name[1] == item.inventory_name:
            if int(inv_name[0]) >= amount >= 0:
                number = int(inv_name[0]) - amount
                if number > 0:
                    change = str(number) + inv_name[1]
                else:  # if its 0 then we need to remove the item from the inventory
                    change = ""
                self.seed = re.sub(x[0], change, self.seed)
                return 1  # 1 means success


class Player:
    def __init__(self, species, name, location, affinity, gender, extra_passives: list, Class,
                 inventory=Inventory("NNNNNNNNNN")):
        # nerd shit
        self.species = species  # so I could inherit everything from species without being a subclass of it
        self.cords = location
        # self.city = do the things where you find where you are
        # self.region =
        # self.closest_checkpoint = I assume to be defined once a map class is created
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
        self.inventory = inventory  # we will need to load the inventory dipshit why did you think making it
        # blank is a good idea
        self.move = species.base_movement + Class.bonus_movement

    def transfer_inventory(self, inv: Inventory, action, item: Item,
                           amount):  # function to transfer item from a player inv
        # to another one or reverse
        #  action is a string that is either T for take or G for give
        # based on the action we either check the player first or the other inventory first
        if action == "T":
            #  if we are taking items from an inventory we should check if it ahs the amount we want to take first
            x = re.findall(r"(\d+{})".format(item.inventory_name), inv.seed)
            if not x:
                return None  # didn't find in inventory
            inv_name = re.split(r"([a-zA-Z]+)", x[0])
            if inv_name[1] == item.inventory_name:
                if int(inv_name[0]) >= amount >= 0:  # if found, and we are taking a normal amount then just remove
                    # and add :>
                    inv.remove_item(item, amount)
                    self.inventory.add_item(item, amount)
                    return 1
                else:  # if you wanted to take more then there is in the inv then return None
                    return None
        elif action == "G":
            #  same but in reverse now
            x = re.findall(r"(\d+{})".format(item.inventory_name), self.inventory.seed)
            if not x:
                return None  # didn't find in inventory
            inv_name = re.split(r"([a-zA-Z]+)", x[0])
            if inv_name[1] == item.inventory_name:
                if int(inv_name[0]) >= amount >= 0:  # if found, and we are taking a normal amount then just remove and
                    # add :>
                    self.inventory.remove_item(item, amount)
                    inv.add_item(item, amount)
                    return 1
                else:
                    return None

    def move(self, location: list[int, int]):  # take pos and use current position plus moves to move in that direction
        # do diagonal moves count as one or 2 moves?
        pass

    def equip(self, item: Item):
        # I will handle main equipment as what is the first thing that is in your inventory seed
        # as per armor I think it should follow the rest of the letters and if there is no valid armor in those slots
        # the default will be NN which will stand for None
        # I will have to implement Binary search or some other searching algorythm to make looking for items in lists
        # fast
        # I guess I will do the thing that will equip to hand
        if item.equipable is None:
            pass
        else:
            # first we look for this item
            x = re.search(r"(\d+{})".format(item.inventory_name), self.inventory.seed)
            if not x:  # thinking about this when we have a UI it's not needed but still adding a measure just in case
                return None  # didn't find in inventory
