from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

siren_base_stats = {
    "max_health": 40,
    "health": 40,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Aqua",
    "attack_power": 12,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 35,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

siren_enemies = register_species_archetypes("siren", siren_base_stats)
