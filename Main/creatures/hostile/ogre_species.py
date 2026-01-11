from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

ogre_base_stats = {
    "max_health": 80,
    "health": 80,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Earth",
    "attack_power": 25,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 90,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

ogre_enemies = register_species_archetypes("ogre", ogre_base_stats)
