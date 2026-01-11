from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

dire_base_stats = {
    "max_health": 45,
    "health": 45,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Earth",
    "attack_power": 15,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 45,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

dire_enemies = register_species_archetypes("dire", dire_base_stats)
