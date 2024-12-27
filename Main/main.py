from creatures.species import Species
from effects.perks import Perk
from material.materials import MaterialRegistry
from player.player_class_registry import PlayerClass, get_player_class
from player.player import Player
from creatures.enemy_npc import Enemy, EnemyRegistry
from combat.combat import Combat
from weapon.weapons import Weapon, WeaponRegistry

print(EnemyRegistry.list_enemies()) 
print("\n")

# Define variables for the player creation process
player_builder = False
experimentals = True  # Set this flag based on whether you want to include surname asking
player_username = ""
player_sir_name = None
player_gender = ""
player_class = ""
elemental_aff = ""

# Player creation process
player_builder = False
experimentals = True  # Set this flag based on whether you want to include surname asking
player_username = ""
player_sir_name = None
player_gender = ""
player_class_input = ""
elemental_aff = ""

# Player creation loop
while not player_builder:
    player_username = input("Insert A Name \n" + "> ")  # Player Name

    # Ask for surname if experimentals is True
    if experimentals:
        ask_player_sir_name = input("Do You Want A Sir Name? \n Yes |1| | No |0|")
        if ask_player_sir_name == "1":
            player_sir_name = input("Insert A Sir Name \n" + "> ")
        elif ask_player_sir_name == "0":
            player_sir_name = None

    # Ask for gender and validate
    player_gender = input("Male | Female | Other \n" + "> ")  # Gender/Sex
    gender_check = False
    player_genders = ["Male", "Female", "Other"]
    while not gender_check:
        if player_gender in player_genders:
            gender_check = True
        else:
            player_gender = input("Male | Female | Other \n" + "> ")  # Typo protection

    # Ask for player class and validate
    player_class_input = input("Warrior | Thief | Bard | Mage | Paladin | Healer | Ranger | Fighter \n" + "> ")  # Player Classes
    class_check = False
    player_class_list = ["Warrior", "Thief", "Bard", "Mage", "Paladin", "Healer", "Ranger", "Fighter"]
    while not class_check:
        if player_class_input in player_class_list:
            class_check = True
        else:
            player_class_input = input("Warrior | Thief | Bard | Mage | Paladin | Healer | Ranger | Fighter \n" + "> ")  # Typo protection

    # Fetch the PlayerClass from the registry
    player_class = get_player_class(player_class_input)

    # Ask for elemental affinity and validate
    elemental_aff = input("Fire, Aqua, Earth, Air, Lightning, Light, Dark, Eclipse, Lunar, Soul, Blood \n" + "> ")  # Elemental Affinity
    affininity_check = False
    elemental_aff_list = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
    while not affininity_check:
        if elemental_aff in elemental_aff_list:
            affininity_check = True
            player_builder = True  # Only set player_builder to True when input is valid
        else:
            elemental_aff = input("Fire, Aqua, Earth, Air, Lightning, Light, Dark, Eclipse, Lunar, Soul, Blood \n" + "> ")  # Typo protection

# Now that the player is built, you can create a Player object
# Assume `Species` and `PlayerClass` are already defined and imported.
species = Species(
    name=player_username, 
    base_health=100, 
    base_max_health=200, 
    base_mana=50, 
    base_max_mana=100, 
    base_magic_dmg=20, 
    base_magic_resist=0, 
    base_armor=0, 
    passive_abilities=["resilient", "quick"], 
    base_dmg=15, 
    base_movement=10
)

refined_iron = MaterialRegistry.get_material("Refined Iron")

# Define some example perks (Perks should be defined elsewhere in your code)
# Assuming you have a perk "Sharpened" in your Perk registry
perk_list = []  # Example perk, replace with actual Perk objects

starting_weapon = Weapon(
    name="Iron Sword",                     # Weapon Name
    material=refined_iron,                 # Material (Steel, fetched from MaterialRegistry)
    weapon_range=1,                        # Weapon Range (e.g., 1 for melee weapons like swords)
    weapon_type="Sword",                   # Weapon Type (e.g., Sword)
    affinity="Fire",                       # Elemental Affinity (e.g., Fire, if applicable)
    damage_type="Slashing",                # Damage Type (e.g., Slashing for swords)
    is_two_handed=False,
    damage_amount=5,
    weight=5,                              # Weight of the weapon (e.g., 5 units)
    mana_bonus=0,                          # Mana bonus (e.g., 0 for non-magical weapons)
    skill_requirement=5,                   # Skill Requirement (e.g., skill level 5 to equip)
    perks=perk_list,                       # Perks associated with the weapon (e.g., Sharpened)
    rarity_name="Common",                  # Rarity (e.g., Common, fetched from Rarity registry)
    craftable=True                         # Whether the weapon is craftable
)

# Create player instance
player = Player(
    species,                               # The species of the player
    player_username,                       # Player username
    [0, 0],                                # Player position (x, y)
    elemental_aff,                         # Elemental Affinity
    player_gender,                         # Player gender
    [WeaponRegistry.get_weapon_by_name("Iron Long Sword")],                     # Player's inventory with the starting weapon
    player_class                           # Player class
)

# Print player details for debugging (optional)
print(f"Player {player.name} created with the following details:")
print(f"Class: {player.player_class.name}")
print(f"Affinity: {player.affinity}")
print(f"Health: {player.health}/{player.max_health}")
print(f"Mana: {player.mana}/{player.max_mana}")
print(f"Magic Resist: {player.magic_resist}")
print(f"Armor: {player.armor}")
print(f"Movement: {player.movement}")

short_sword = Weapon(
    name="Iron Short Sword",                     # Weapon Name
    material=refined_iron,                 # Material (Steel, fetched from MaterialRegistry)
    weapon_range=1,                        # Weapon Range (e.g., 1 for melee weapons like swords)
    weapon_type="Sword",                   # Weapon Type (e.g., Sword)
    affinity="Fire",                       # Elemental Affinity (e.g., Fire, if applicable)
    damage_type="Slashing",                # Damage Type (e.g., Slashing for swords)
    is_two_handed=False,
    damage_amount=5,
    weight=5,                              # Weight of the weapon (e.g., 5 units)
    mana_bonus=0,                          # Mana bonus (e.g., 0 for non-magical weapons)
    skill_requirement=5,                   # Skill Requirement (e.g., skill level 5 to equip)
    perks=perk_list,                       # Perks associated with the weapon (e.g., Sharpened)
    rarity_name="Common",                  # Rarity (e.g., Common, fetched from Rarity registry)
    craftable=True                         # Whether the weapon is craftable
)

# Initialize combat
combat = Combat(player, EnemyRegistry.get_enemy("Green Slime"))
combat.start_combat()  # Start the combat loop