from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

lamia_base_stats = {
    "max_health": 50,
    "health": 50,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Earth",
    "attack_power": 15,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 60,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

lamia_enemies = register_species_archetypes("lamia", lamia_base_stats)
