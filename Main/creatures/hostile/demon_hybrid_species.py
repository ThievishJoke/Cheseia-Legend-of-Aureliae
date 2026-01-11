from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry
from creatures.enemy_npc import register_species_archetypes

demon_hybrid_base_stats = {
    "max_health": 50,
    "health": 50,
    "max_mana": 0,
    "mana": 0,
    "affinity": "Dark",
    "attack_power": 17,
    "physical_resistance": 0,
    "magical_resistance": 0,
    "weapons": [],
    "inventory": [],
    "xp_reward": 55,
    "description": "",
    "base_level": 1,
    "loot_table": [],
}

demon_hybrid_enemies = register_species_archetypes("demon_hybrid", demon_hybrid_base_stats)
