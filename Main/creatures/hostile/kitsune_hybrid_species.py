from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

kitsune_hybrid_base_stats = {
    "max_health": 45,
    "health": 45,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Fire",
    "attack_power": 14,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 50,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

kitsune_hybrid_enemies = register_species_archetypes("kitsune_hybrid", kitsune_hybrid_base_stats)
