from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

cambion_base_stats = {
    "max_health": 55,
    "health": 55,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Dark",
    "attack_power": 18,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 60,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

cambion_enemies = register_species_archetypes("cambion", cambion_base_stats)
