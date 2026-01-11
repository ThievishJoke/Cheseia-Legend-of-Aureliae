from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

goblin_base_stats = {
    "max_health": 25,
    "health": 25,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Earth",
    "attack_power": 8,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 20,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

goblin_enemies = register_species_archetypes("goblin", goblin_base_stats)
