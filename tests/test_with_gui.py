import random
import time
import re
import math


class Species:
    def __init__(self, name, base_health, base_mana, base_magic_dmg, base_magic_resist, base_armor,
                 passive_abilities: list, base_movement, base_dmg):
        self.name = name
        self.baseHealth = base_health
        self.baseMana = base_mana
        self.base_magic_dmg = base_magic_dmg
        self.base_magic_resist = base_magic_resist
        self.base_armor = base_armor
        self.passive_abilities = passive_abilities
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


class Equipable(Item):
    def __init__(self, durability, current_durability, name, inventory_name: str, enchantment: list, slot: str, ID: int):
        super().__init__(name, inventory_name)
        self.max_durability = durability
        self.current_durability = current_durability
        self.enchantments = enchantment
        self.slot = slot
        self.ID = ID

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
    def __init__(self, species, name, location: list[int], affinity, gender, extra_passives: list, player_class,
                 inventory=Inventory("NNNNN")):
        # Initializing player attributes
        self.species = species
        self.cords = location
        self.affinity = affinity
        self.Class = player_class
        extra_passives.extend(Class.passive_abilities)
        extra_passives.extend(species.passive_abilities)
        extra_passives = list(filter(None, extra_passives))
        
        # Player stats
        self.name = name
        self.gender = gender
        self.passive_abilities = extra_passives
        self.health = species.baseHealth + Class.bonus_health
        self.armor = species.base_armor + Class.bonus_armor
        self.mana = species.baseMana + Class.bonus_mana
        self.magic_resist = species.base_magic_resist + Class.bonus_magic_resist
        self.inventory = inventory
        self.movement = species.base_movement + Class.bonus_movement

    def move(self, location: list[int]):
        # Move the player to a new location if within movement range
        distance = math.dist(self.cords, location)
        if distance <= self.movement:
            self.cords = location
            return True
        else:
            return False


class Goblin:
    def __init__(self):
        self.health = 30
        self.base_damage = 5

    def attack(self, player):
        critical_hit = random.randint(1, 10) == 1  # 10% chance for critical hit
        damage = self.base_damage * (3 if critical_hit else 1)
        player.health -= max(damage - player.armor, 0)  # Calculate damage after armor
        return damage, critical_hit


# Character Creation
def create_character():
    if True:  # Replace with actual condition to trigger character creation
        player_sir_name = None
        ask_player_sir_name = input("Do You Want A Sir Name? \n Yes |1| | No |0| ")
        if ask_player_sir_name == "1":
            player_sir_name = input("Insert A Sir Name \n" + "> ")
        elif ask_player_sir_name == "0":
            player_sir_name = None
        else:
            print("Invalid input. No sir name will be assigned.")
            player_sir_name = None

        # Gender
        player_gender = input("Male | Female | Other \n" + "> ")
        gender_check = False
        player_genders = ["Male", "Female", "Other"]
        while not gender_check:
            if player_gender in player_genders:
                gender_check = True
            else:
                player_gender = input("Invalid input. Please choose: Male | Female | Other \n" + "> ")

        # Class
        player_class_name = input("Warrior | Thief | Bard | Mage | Paladin | Healer | Ranger | Fighter \n" + "> ")
        class_check = False
        player_class_list = ["Warrior", "Thief", "Bard", "Mage", "Paladin", "Healer", "Ranger", "Fighter"]
        while not class_check:
            if player_class_name in player_class_list:
                class_check = True
            else:
                player_class_name = input("Invalid class. Please choose: Warrior | Thief | Bard | Mage | Paladin | Healer | Ranger | Fighter \n" + "> ")

        # Elemental Affinity
        elemental_aff = input("Fire, Aqua, Earth, Air, Lightning, Natural, Light, Dark, Eclipse, Lunar, Soul, Blood \n" + "> ")
        affinity_check = False
        elemental_aff_list = ["Fire", "Aqua", "Earth", "Air", "Lightning", "Natural", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
        while not affinity_check:
            if elemental_aff in elemental_aff_list:
                affinity_check = True
            else:
                elemental_aff = input("Invalid affinity. Please choose: Fire, Aqua, Earth, Air, Lightning, Natural, Light, Dark, Eclipse, Lunar, Soul, Blood \n" + "> ")

        print(f"Character Summary:")
        print(f"Name: {player_sir_name if player_sir_name else 'No Sir Name'}")
        print(f"Gender: {player_gender}")
        print(f"Class: {player_class_name}")
        print(f"Elemental Affinity: {elemental_aff}")

        # Return new player with default species and class values
        species = Species("Human", 100, 50, 10, 5, 5, [], 5, 5)  # Example species
        player_class = Class(player_class_name, 5, 5, 5, 20, 2, 2, [], 1)  # Example class
        return Player(species, player_sir_name, [0, 0], elemental_aff, player_gender, [], player_class)

# Main Game Loop
def game_loop():
    player = create_character()  # Create the player
    goblin = Goblin()

    while player.health > 0 and goblin.health > 0:
        print(f"\nYour Health: {player.health}")
        print(f"Goblin Health: {goblin.health}")
        action = input("Do you want to Attack (A) or Wait (W)? ").strip().lower()
        
        if action == 'a':
            # Attack the goblin
            damage = random.randint(1, player.Class.bonus_dmg)  # Assuming bonus_dmg is the base damage
            goblin.health -= damage
            print(f"You dealt {damage} damage to the goblin.")
        elif action == 'w':
            print("You chose to wait.")

        if goblin.health > 0:
            # Goblin's turn to attack
            player_locked_out = True  # Lock player from attacking
            print("The goblin attacks!")
            damage, critical = goblin.attack(player)
            crit_message = " (Critical Hit!)" if critical else ""
            print(f"The goblin dealt {damage} damage to you{crit_message}.")
            player_locked_out = False  # Unlock after goblin's attack

    if player.health <= 0:
        print("You have been defeated!")
    else:
        print("You have defeated the goblin!")

# Run the game
if __name__ == "__main__":
    game_loop()
