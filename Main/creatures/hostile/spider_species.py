from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry

spider_species = EnemySpecies(
    id="spider",
    name="Spider",
    name_key="creatures.species.spider.name",
    description_key="creatures.species.spider.description",
    base_stats={
        "max_health": 12,
        "health": 12,
        "max_mana": 0,
        "mana": 0,
        "affinity": "Earth",
        "attack_power": 4,
        "physical_resistance": 0,
        "magical_resistance": 0,
        "weapons": [],
        "inventory": [],
        "xp_reward": 50,
        "description": "",
    }
)

EnemyType(
    id="widower_arachnid",
    species="spider",
    name="Widower Arachnid",
    name_key="creatures.enemies.widower_arachnid.name",
    description_key="creatures.enemies.widower_arachnid.description",
    overrides={
        "max_health": 15,
        "health": 15,
        "attack_power": 10,
        "affinity": "Soul",
        "description": ".",
    }
)

EnemyType(
    id="giant_spider",
    species="spider",
    name="Giant Spider",
    name_key="creatures.enemies.giant_spider.name",
    description_key="creatures.enemies.giant_spider.description",
    overrides={
        "max_health": 15,
        "health": 15,
        "attack_power": 10,
        "affinity": "Soul",
        "description": ".",
    }
)

EnemyType(
    id="death_widow",
    species="spider",
    name="Death Widow",
    name_key="creatures.enemies.death_widow.name",
    description_key="creatures.enemies.death_widow.description",
    overrides={
        "max_health": 20,
        "health": 20,
        "attack_power": 12,
        "affinity": "Earth",
        "description": ".",
    }
)

EnemyType(
    id="moth_spiderling",
    species="spider",
    name="Moth Spiderling",
    name_key="creatures.enemies.moth_spiderling.name",
    description_key="creatures.enemies.moth_spiderling.description",
    overrides={
        "max_health": 20,
        "health": 20,
        "attack_power": 15,
        "affinity": "Air",
        "description": ".",
    }
)

EnemyType(
    id="crimson_brood",
    species="spider",
    name="Crimson Brood",
    name_key="creatures.enemies.crimson_brood.name",
    description_key="creatures.enemies.crimson_brood.description",
    overrides={
        "max_health": 25,
        "health": 25,
        "attack_power": 30,
        "affinity": "Soul",
        "description": ".",
    }
)

EnemyType(
    id="wolf_spider",
    species="spider",
    name="Wolf Spider",
    name_key="creatures.enemies.wolf_spider.name",
    description_key="creatures.enemies.wolf_spider.description",
    overrides={
        "max_health": 20,
        "health": 20,
        "attack_power": 17,
        "affinity": "Soul",
        "description": ".",
    }
)

EnemyType(
    id="frostbite_spider",
    species="spider",
    name="Frostbite Spider",
    name_key="creatures.enemies.frostbite_spider.name",
    description_key="creatures.enemies.frostbite_spider.description",
    overrides={
        "max_health": 30,
        "health": 30,
        "attack_power": 25,
        "affinity": "Aqua",
        "description": ".",
    }
)

widower_arachnid_spider = EnemyType.get_type("widower_arachnid").create_enemy()
giant_spider = EnemyType.get_type("giant_spider").create_enemy()
death_widow_spider = EnemyType.get_type("death_widow").create_enemy()
moth_spiderling_spider = EnemyType.get_type("moth_spiderling").create_enemy()
crimson_brood_spider = EnemyType.get_type("crimson_brood").create_enemy()
wolf_spider = EnemyType.get_type("wolf_spider").create_enemy()
frostbite_spider = EnemyType.get_type("frostbite_spider").create_enemy()

EnemyRegistry.register_enemy(widower_arachnid_spider)
EnemyRegistry.register_enemy(giant_spider)
EnemyRegistry.register_enemy(death_widow_spider)
EnemyRegistry.register_enemy(moth_spiderling_spider)
EnemyRegistry.register_enemy(crimson_brood_spider)
EnemyRegistry.register_enemy(wolf_spider)
EnemyRegistry.register_enemy(frostbite_spider)
