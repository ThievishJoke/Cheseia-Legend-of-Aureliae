import pathlib
from combat.precedural_combat import EncounterGenerator
from creatures.species import Species
from effects.perks import Perk
import save as save
from material.materials import MaterialRegistry
from creatures.species_registry import species_registry, get_species_by_id, get_species_by_display_name
from creatures.classes_registry import class_registry, get_player_class, get_class_by_display_name
from player.player import Player
from creatures.enemy_npc import Enemy, EnemyRegistry
from combat.combat import Combat
from weapon.weapons import Weapon, WeaponRegistry
from utility.formatting import Formatting as Format
import json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from language.localization import translate
from language.localization import list_missing_translations
from dialogue.dialogue_registry import get_dialogue
from save import save_manager
from menu import StartMenu 

list_missing_translations()
#print("DEBUG:main.py", EnemyRegistry.list_enemies()) 
print("\n")

#species = creatures.species_registry.get_species("Human")  # Default to Human if invalid input
#print(Species.to_dict(species))

from language.localization import translate

# Main check: Load or Create Player
print("Checking for existing saves...")

menu = StartMenu()
player_instance = menu.run()  # Returns a Player instance

print(f"\nWelcome, {player_instance.name}!\nLevel: {player_instance.level}, Class: {player_instance.player_class.name}")

# 2️⃣ Example: start a test encounter
location = "forest"
difficulty = "easy"
#
print("\n= Test Random Procedural Encounter =")
print(f"Location: {location}, Difficulty: {difficulty}")
#
enemy_group = EncounterGenerator.generate_group(
    player_instance,
    location_id=location,
    difficulty=difficulty
)
#
print("\nGenerated enemies:")
encounter = enemy_group if isinstance(enemy_group, list) else [enemy_group]
for enemy in encounter:
    print(f"{enemy.name} (HP2: {enemy.health}/{enemy.max_health}, Attack: {enemy.attack_power}, XP: {enemy.xp_reward})")
#
combat = Combat(player_instance, enemy_group)
combat.start_combat()

print(f"\n {Format.BOLD}Test Dialogue ")
npc = get_dialogue("aureliae")
npc.talk(player_instance)

npc = get_dialogue("guard_darel")
npc.talk(player_instance)