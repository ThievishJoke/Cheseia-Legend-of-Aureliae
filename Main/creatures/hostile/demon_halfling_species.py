from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

demon_halfling_base_stats = {
    "max_health": 35,
    "health": 35,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Dark",
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

demon_halfling_enemies = register_species_archetypes("demon_halfling", demon_halfling_base_stats)
