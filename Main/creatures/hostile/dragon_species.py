from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry

EnemySpecies(
    id="dragon",
    name="Dragon",
    name_key="creatures.species.dragon.name",
    description_key="creatures.species.dragon.description",
    base_stats={
        "max_health": 500,
        "health": 500,
        "max_mana": 0,
        "mana": 0,
        "affinity": "",
        "attack_power": 0,
        "physical_resistance": 0,
        "magical_resistance": 0,
        "weapons": [],
        "inventory": [],
        "xp_reward": 100,
        "description": "A powerful dragon.",
    }
)

# Subtypes

EnemyType(
    id="fire_dragon",
    species="dragon",
    name="Fire",
    name_key="creatures.enemies.fire_dragon.name",
    description_key="creatures.enemies.fire_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 130,
        "magic_attack_power": 40,
        "magical_resistance": 10,
        "armor": 60,
        "description": "A blazing fire dragon."
    }
)

EnemyType(
    id="aqua_dragon",
    species="dragon",
    name="Aqua",
    name_key="creatures.enemies.aqua_dragon.name",
    description_key="creatures.enemies.aqua_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 70,
        "magic_attack_power": 100,
        "magical_resistance": 0,
        "armor": 55,
        "description": "A water dragon exhaling icy torrents."
    }
)

EnemyType(
    id="earth_dragon",
    species="dragon",
    name="Earth",
    name_key="creatures.enemies.earth_dragon.name",
    description_key="creatures.enemies.earth_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 170,
        "magic_attack_power": 0,
        "magical_resistance": -30,
        "armor": 120,
        "description": "A massive dragon of stone and minerals."
    }
)

EnemyType(
    id="air_dragon",
    species="dragon",
    name="Air",
    name_key="creatures.enemies.air_dragon.name",
    description_key="creatures.enemies.air_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 170,
        "magic_attack_power": 0,
        "magical_resistance": 0,
        "armor": 0,
        "description": "A swift dragon of the skies."
    }
)

EnemyType(
    id="lightning_dragon",
    species="dragon",
    name="Lightning",
    name_key="creatures.enemies.lightning_dragon.name",
    description_key="creatures.enemies.lightning_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 170,
        "magic_attack_power": 0,
        "magical_resistance": 0,
        "armor": 0,
        "description": "A dragon crackling with lightning."
    }
)

EnemyType(
    id="light_dragon",
    species="dragon",
    name="Light",
    name_key="creatures.enemies.light_dragon.name",
    description_key="creatures.enemies.light_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 170,
        "magic_attack_power": 0,
        "magical_resistance": 0,
        "armor": 0,
        "description": "A dragon radiating pure light."
    }
)

EnemyType(
    id="dark_dragon",
    species="dragon",
    name="Dark",
    name_key="creatures.enemies.dark_dragon.name",
    description_key="creatures.enemies.dark_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 170,
        "magic_attack_power": 0,
        "magical_resistance": 0,
        "armor": 0,
        "description": "A shadowy dragon from the depths."
    }
)

EnemyType(
    id="eclipse_dragon",
    species="dragon",
    name="Eclipse",
    name_key="creatures.enemies.eclipse_dragon.name",
    description_key="creatures.enemies.eclipse_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 170,
        "magic_attack_power": 0,
        "magical_resistance": 0,
        "armor": 0,
        "description": "A dragon of shadow and light."
    }
)

EnemyType(
    id="lunar_dragon",
    species="dragon",
    name="Lunar",
    name_key="creatures.enemies.lunar_dragon.name",
    description_key="creatures.enemies.lunar_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 170,
        "magic_attack_power": 0,
        "magical_resistance": 0,
        "armor": 0,
        "description": "A dragon under the moon's power."
    }
)

EnemyType(
    id="natural_dragon",
    species="dragon",
    name="Natural",
    name_key="creatures.enemies.natural_dragon.name",
    description_key="creatures.enemies.natural_dragon.description",
    overrides={
        "health": 100,
        "max_health": 100,
        "attack_power": 90,
        "magic_attack_power": 0,
        "magical_resistance": 0,
        "armor": 0,
        "description": "A fragile natural dragon."
    }
)

EnemyType(
    id="soul_dragon",
    species="dragon",
    name="Soul",
    name_key="creatures.enemies.soul_dragon.name",
    description_key="creatures.enemies.soul_dragon.description",
    overrides={
        "health": 200,
        "max_health": 200,
        "attack_power": 0,
        "magic_attack_power": 180,
        "magical_resistance": 0,
        "armor": 90,
        "description": "A dragon made of trapped souls."
    }
)

EnemyType(
    id="blood_dragon",
    species="dragon",
    name="Blood",
    name_key="creatures.enemies.blood_dragon.name",
    description_key="creatures.enemies.blood_dragon.description",
    overrides={
        "health": 500,
        "max_health": 500,
        "attack_power": 0,
        "magic_attack_power": 170,
        "magical_resistance": 0,
        "armor": 0,
        "description": "A dragon empowered by blood magic."
    }
)

fire_dragon = EnemyType.get_type("fire_dragon").create_enemy()
aqua_dragon = EnemyType.get_type("aqua_dragon").create_enemy()
earth_dragon = EnemyType.get_type("earth_dragon").create_enemy()
air_dragon = EnemyType.get_type("air_dragon").create_enemy()
lightning_dragon = EnemyType.get_type("lightning_dragon").create_enemy()
light_dragon = EnemyType.get_type("light_dragon").create_enemy()
dark_dragon = EnemyType.get_type("dark_dragon").create_enemy()
eclipse_dragon = EnemyType.get_type("eclipse_dragon").create_enemy()
lunar_dragon = EnemyType.get_type("lunar_dragon").create_enemy()
natural_dragon = EnemyType.get_type("natural_dragon").create_enemy()
soul_dragon = EnemyType.get_type("soul_dragon").create_enemy()
blood_dragon = EnemyType.get_type("blood_dragon").create_enemy()

EnemyRegistry.register_enemy(fire_dragon)
EnemyRegistry.register_enemy(aqua_dragon)
EnemyRegistry.register_enemy(earth_dragon)
EnemyRegistry.register_enemy(air_dragon)
EnemyRegistry.register_enemy(lightning_dragon)
EnemyRegistry.register_enemy(light_dragon)
EnemyRegistry.register_enemy(dark_dragon)
EnemyRegistry.register_enemy(eclipse_dragon)
EnemyRegistry.register_enemy(lunar_dragon)
EnemyRegistry.register_enemy(natural_dragon)
EnemyRegistry.register_enemy(soul_dragon)
EnemyRegistry.register_enemy(blood_dragon)