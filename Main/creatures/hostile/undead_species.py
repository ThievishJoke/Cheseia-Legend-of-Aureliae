from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

undead_base_stats = {
    "max_health": 40,
    "health": 40,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Dark",
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

undead_enemies = register_species_archetypes("undead", undead_base_stats)
