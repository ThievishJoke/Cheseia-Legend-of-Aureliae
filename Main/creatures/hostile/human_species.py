from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

human_base_stats = {
    "max_health": 50,
    "health": 50,
    "max_mana": 0,
    "mana": 0,
    "affinity": "",
    "attack_power": 10,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 20,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

human_enemies = register_species_archetypes("human", human_base_stats)