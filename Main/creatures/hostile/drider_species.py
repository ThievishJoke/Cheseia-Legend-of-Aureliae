from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry

drider_species = EnemySpecies(
    id="drider",
    name="Drider",
    name_key="creatures.species.drider.name",
    description_key="creatures.species.drider.description",
    base_stats={
        "max_health": 30,
        "health": 30,
        "max_mana": 0,
        "mana": 0,
        "affinity": "Earth",
        "attack_power": 15,
        "physical_resistance": 0,
        "magical_resistance": 0,
        "weapons": [],
        "inventory": [],
        "xp_reward": 50,
        "description": "",
    }
)

# Subtypes

EnemyType(
    id="weakened_drider",
    species="drider",
    name="Weakened",
    name_key="creatures.enemies.weakened_drider.name",
    description_key="creatures.enemies.weakened_drider.description",
    overrides={
        "max_health": 25,
        "health": 25,
        "attack_power": 15,
        "affinity": "",
        "description": ".",
    }
)

EnemyType(
    id="vigored_drider",
    species="drider",
    name="Vigored",
    name_key="creatures.enemies.vigored_drider.name",
    description_key="creatures.enemies.vigored_drider.description",
    overrides={
        "max_health": 50,
        "health": 50,
        "attack_power": 20,
        "affinity": "Aqua",
        "description": ".",
    }
)

EnemyType(
    id="solid_drider",
    species="drider",
    name="Solid",
    name_key="creatures.enemies.solid_drider.name",
    description_key="creatures.enemies.solid_drider.description",
    overrides={
        "max_health": 75,
        "health": 75,
        "attack_power": 30,
        "description": ".",
    }
)

EnemyType(
    id="drider_princess",
    species="drider",
    name="Princess",
    name_key="creatures.enemies.drider_princess.name",
    description_key="creatures.enemies.drider_princess.description",
    overrides={
        "max_health": 85,
        "health": 85,
        "attack_power": 7,
        "description": ".",
    }
)

EnemyType(
    id="drider_queen",
    species="drider",
    name="Queen",
    name_key="creatures.enemies.drider_queen.name",
    description_key="creatures.enemies.drider_queen.description",
    overrides={
        "max_health": 100,
        "health": 100,
        "attack_power": 65,
        "xp_reward": 150,
        "description": ".",
    }
)

weakened_drider = EnemyType.get_type("weakened_drider").create_enemy()
vigored_drider = EnemyType.get_type("vigored_drider").create_enemy()
solid_drider = EnemyType.get_type("solid_drider").create_enemy()
drider_princess = EnemyType.get_type("drider_princess").create_enemy()
drider_queen = EnemyType.get_type("drider_queen").create_enemy()

EnemyRegistry.register_enemy(weakened_drider)
EnemyRegistry.register_enemy(vigored_drider)
EnemyRegistry.register_enemy(solid_drider)
EnemyRegistry.register_enemy(drider_princess)
EnemyRegistry.register_enemy(drider_queen)
