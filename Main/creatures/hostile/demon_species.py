from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

demon_base_stats = {
    "max_health": 60,
    "health": 60,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Dark",
    "attack_power": 20,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 80,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

demon_enemies = register_species_archetypes("demon", demon_base_stats)
