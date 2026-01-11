from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

kitsune_base_stats = {
    "max_health": 40,
    "health": 40,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Fire",
    "attack_power": 12,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 30,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

kitsune_enemies = register_species_archetypes("kitsune", kitsune_base_stats)
