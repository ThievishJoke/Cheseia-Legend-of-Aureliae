from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

merfolk_base_stats = {
    "max_health": 45,
    "health": 45,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Aqua",
    "attack_power": 14,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 40,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

merfolk_enemies = register_species_archetypes("merfolk", merfolk_base_stats)
