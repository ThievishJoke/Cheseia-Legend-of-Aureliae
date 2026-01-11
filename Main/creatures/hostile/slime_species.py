from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry

EnemySpecies(
    id="slime",
    name="Slime",
    name_key="creatures.species.slime.name",
    description_key="creatures.species.slime.description",
    base_stats={
        "max_health": 12,
        "health": 12,
        "max_mana": 0,
        "mana": 0,
        "affinity": "Water",
        "attack_power": 4,
        "physical_resistance": 0,
        "magical_resistance": 0,
        "weapons": [],
        "inventory": [],
        "xp_reward": 25,
        "description": "A wobbly blob of goo.",
    }
)
# Subtypes
EnemyType(
    id="green_slime",
    species="slime",
    name="Green",
    name_key="creatures.enemies.green_slime.name",
    description_key="creatures.enemies.green_slime.description",
    overrides={
        "health": 14,
        "max_health": 14,
        "attack_power": 5,
        "xp_reward": 25,
        "base_level": 1,
        "loot_table": [],
        "description": "A weak green slime that jiggles angrily."
    }
)

EnemyType(
    id="red_slime",
    species="slime",
    name="Red",
    name_key="creatures.enemies.red_slime.name",
    description_key="creatures.enemies.red_slime.description",
    overrides={
        "health": 18,
        "max_health": 18,
        "attack_power": 7,
        "xp_reward": 35,
        "base_level": 2,
        "loot_table": [],
        "description": "A fiery red slime with an acidic temperament."
    }
)

EnemyType(
    id="blue_slime",
    species="slime",
    name="Blue",
    name_key="creatures.enemies.blue_slime.name",
    description_key="creatures.enemies.blue_slime.description",
    overrides={
        "health": 20,
        "max_health": 20,
        "attack_power": 6,
        "xp_reward": 30,
        "base_level": 2,
        "loot_table": [],
        "description": "A chill blue slime that radiates cold energy."
    }
)


green_slime = EnemyType.get_type("green_slime").create_enemy()
red_slime = EnemyType.get_type("red_slime").create_enemy()
blue_slime = EnemyType.get_type("blue_slime").create_enemy()

EnemyRegistry.register_enemy(green_slime)
EnemyRegistry.register_enemy(red_slime)
EnemyRegistry.register_enemy(blue_slime)