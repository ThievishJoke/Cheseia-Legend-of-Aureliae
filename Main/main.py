import pathlib
from creatures.species import Species
import creatures.species_registry
from effects.perks import Perk
import save
from material.materials import MaterialRegistry
from player.player_class_registry import PlayerClass, get_player_class
from player.player import Player
from creatures.enemy_npc import Enemy, EnemyRegistry
from combat.combat import Combat
from weapon.weapons import Weapon, WeaponRegistry
import json
import os

print(EnemyRegistry.list_enemies()) 
print("\n")

# Paths
save_path = "savefiles/save.json"
debug_path = "savefiles/debug_save.json"

# Flag
experimentals = True  # Whether to ask for a surname

#species = creatures.species_registry.get_species("Human")  # Default to Human if invalid input
#print(Species.to_dict(species))

def create_new_player():
    player_builder = False
    player_username = ""
    player_sir_name = None
    player_gender = ""
    player_class_input = ""
    elemental_aff = ""

    while not player_builder:
        player_username = input("Insert A Name \n> ")

        if experimentals:
            ask_player_sir_name = input("Do You Want A Sir Name? \n Yes |1| | No |0| \n> ")
            player_sir_name = input("Insert A Sir Name \n> ") if ask_player_sir_name == "1" else None

        # Choose Species
        species_input = input("Choose a species: Human, Lamia, Kitsune, Orc, Spider, Dire\n> ")
        species = creatures.species_registry.get_species(species_input)  # This will return None if not found
        
        if species is None:
            print("Invalid species chosen, defaulting to Human.")
            species = creatures.species_registry.get_species("Human")  # Default to Human if invalid input
        
        player_gender = input("Male | Female | Other \n> ")
        while player_gender not in ["Male", "Female", "Other"]:
            player_gender = input("Please choose: Male | Female | Other \n> ")

        player_class_input = input("Warrior | Thief | Bard | Mage | Paladin | Healer | Ranger | Fighter \n> ")
        while player_class_input not in ["Warrior", "Thief", "Bard", "Mage", "Paladin", "Healer", "Ranger", "Fighter"]:
            player_class_input = input("Choose a valid class \n> ")

        player_class = get_player_class(player_class_input)

        elemental_aff = input("Fire, Aqua, Earth, Air, Lightning, Light, Dark, Eclipse, Lunar, Soul, Blood \n> ")
        while elemental_aff not in ["Fire", "Aqua", "Earth", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]:
            elemental_aff = input("Please choose a valid element \n> ")

        player_builder = True

    refined_iron = MaterialRegistry.get_material("Refined Iron")
    perk_list = []

    # Starting weapon
    starting_weapon = Weapon(
        name="Iron Sword",
        material=refined_iron,
        weapon_range=1,
        weapon_type="Sword",
        affinity="Fire",
        damage_type="Slashing",
        is_two_handed=False,
        damage_amount=5,
        weight=5,
        mana_bonus=0,
        skill_requirement=5,
        perks=perk_list,
        rarity_name="Common",
        craftable=True
    )

    # Player instance
    player = Player(
        species,
        player_username,
        [0, 0],
        elemental_aff,
        player_gender,
        [WeaponRegistry.get_weapon_by_name("Iron Long Sword")],
        player_class
    )

    print(f"Player {player.name} created with the following details:")
    print(f"Class: {player.player_class.name}")
    print(f"Affinity: {player.affinity}")
    print(f"Health: {player.health}/{player.max_health}")
    print(f"Mana: {player.mana}/{player.max_mana}")
    print(f"Magic Resist: {player.magic_resist}")
    print(f"Armor: {player.armor}")
    print(f"Speed: {player.speed}")

    return player


# Main check: Load or Create Player
print("Checking for existing saves...")

def startup_load_save():
  if os.path.exists(save_path):
      print("Save file found.")
      with open(save_path, "r") as f:
          Aureliae_savestate_load = json.load(f)
          debug = Aureliae_savestate_load.get("Debug", False)
          if debug:
              print("Debug mode enabled.")

          # Reconstruct full Player object from saved dict
          player = Player.from_dict(Aureliae_savestate_load)
  else:
      print("Save file not found.")
      player = create_new_player()
      save.save_game(player)

# Initialize combat with Player object
#combat = Combat(player, EnemyRegistry.get_enemy("Kitsune Warrior"))
#combat.start_combat()