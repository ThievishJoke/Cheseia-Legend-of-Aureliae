from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

changeling_base_stats = {
    "max_health": 40,
    "health": 40,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Air",
    "attack_power": 12,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 40,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

changeling_enemies = register_species_archetypes("changeling", changeling_base_stats)
