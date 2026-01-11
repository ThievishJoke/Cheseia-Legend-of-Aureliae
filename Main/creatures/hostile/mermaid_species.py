from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

mermaid_base_stats = {
    "max_health": 35,
    "health": 35,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Aqua",
    "attack_power": 10,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 30,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

mermaid_enemies = register_species_archetypes("mermaid", mermaid_base_stats)
