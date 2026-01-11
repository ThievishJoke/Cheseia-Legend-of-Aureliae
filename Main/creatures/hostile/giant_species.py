from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

giant_base_stats = {
    "max_health": 120,
    "health": 120,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Earth",
    "attack_power": 35,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 120,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

giant_enemies = register_species_archetypes("giant", giant_base_stats)
