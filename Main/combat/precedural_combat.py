import random
import copy
import math

from creatures.enemy_npc import EnemyRegistry
import creatures.hostile.drider_species
import creatures.hostile.slime_species
import creatures.hostile.spider_species

class EncounterPool:
    def __init__(self, name, enemies, min_level=1, max_level=999):
        self.name = name
        self.enemies = enemies
        self.min_level = min_level
        self.max_level = max_level


LOCATION_POOLS = {
    "forest": EncounterPool(
        "Forest",
        enemies=[
            {"id": "green_slime", "weight": 4},
            {"id": "red_slime", "weight": 4},
            {"id": "giant_spider", "weight": 4},
        ],
        min_level=1,
        max_level=10,
    ),
    "underground_ruins": EncounterPool(
        "Underground Ruins",
        enemies=[
            {"id": "skeleton", "weight": 5, "tags": ["undead"]},
            {"id": "zombie", "weight": 3, "tags": ["undead"]},
            {"id": "solid_drider", "weight": 1, "tags": ["arachnid", "elite"]},
        ],
        min_level=5,
        max_level=20,
    ),
}

DIFFICULTY_MODIFIERS = {
    "easy": 0.8,
    "normal": 1.0,
    "hard": 1.25,
    "nightmare": 1.6,
    "legendary": 4,
}


def scale_enemy_stats(enemy, player_level, difficulty):
    """
    Scale enemy stats based on player level and difficulty.
    - Linear scaling for most levels
    - Periodic spikes for fun difficulty jumps
    - Exponential scaling past level 100
    """
    if enemy is None:
        raise ValueError("scale_enemy_stats called with enemy=None!")
    diff_mod = DIFFICULTY_MODIFIERS.get(difficulty, 1.0)
    base_level = getattr(enemy, "base_level", 1)
    level_factor = max(1.0, player_level / base_level)

    # Linear scaling up to level 100, exponential after
    if player_level <= 100:
        hp_scale = int(enemy.max_health * level_factor * diff_mod)
        atk_scale = int(enemy.attack_power * level_factor * diff_mod)
    else:
        # Exponential post-game scaling
        factor = (player_level / 100) ** 1.5
        hp_scale = int(enemy.max_health * level_factor * diff_mod * factor)
        atk_scale = int(enemy.attack_power * level_factor * diff_mod * factor)

    enemy.max_health = hp_scale
    enemy.health = enemy.max_health
    enemy.attack_power = atk_scale
    return enemy


REWARD_TABLE = {
    "default": {
        "xp": lambda enemy: enemy.xp_reward,
        "loot": lambda enemy: [],  # list of items
        "reputation": lambda enemy: 0,
        "perks": lambda enemy: None,
    },
    "undead": {
        "xp": lambda enemy: int(enemy.xp_reward * 1.2),
        "loot": lambda enemy: ["Bone Fragment"],
        "reputation": lambda enemy: 1,
    },
}


def generate_rewards(enemy):
    rewards = {"xp": 0, "loot": [], "reputation": 0, "perks": None}

    # apply default
    table = REWARD_TABLE["default"]
    for k in rewards:
        rewards[k] = table[k](enemy)

    # apply tag-based rewards
    # for tag in enemy.tags:
    #    if tag in REWARD_TABLE:
    #        table = REWARD_TABLE[tag]
    #        for k in rewards:
    #            result = table.get(k)
    #            if result:
    #                if k == "loot":
    #                    rewards[k] += result(enemy)
    #                else:
    #                    rewards[k] += result(enemy)

    return rewards


class EncounterGenerator:

    @staticmethod
    def scale_enemy_stats(enemy, player_level, difficulty):
        return scale_enemy_stats(
            enemy, player_level, difficulty
        )  # just call the module function

    @staticmethod
    def choose_enemy_from_pool(pool, player):
        # enforce level range
        if not (pool.min_level <= player.level <= pool.max_level):
            return None

        total = sum(e.get("weight", 1) for e in pool.enemies)
        roll = random.uniform(0, total)
        current = 0

        for entry in pool.enemies:
            current += entry.get("weight", 1)
            if roll <= current:
                enemy_id = entry["id"]
                enemy = EnemyRegistry.get_enemy(enemy_id)
                if enemy is None:
                    raise KeyError(
                        f"EnemyRegistry returned None for enemy_id='{enemy_id}'. "
                        f"Check EnemyType registration."
                    )
                return enemy

        raise RuntimeError("Weighted enemy selection failed unexpectedly")

    @staticmethod
    def generate(player, location_id, difficulty="normal"):
        pool = LOCATION_POOLS.get(location_id)
        if not pool:
            raise ValueError(f"No encounter pool for location '{location_id}'")

        enemy = EncounterGenerator.choose_enemy_from_pool(pool, player)

        if enemy is None:
            raise ValueError(
                f"No enemy available for location='{location_id}', "
                f"player_level={player.level}"
            )

        enemy = scale_enemy_stats(enemy, player.level, difficulty)

        return enemy

    @staticmethod
    def generate_group(player, location_id, difficulty="normal"):
        """Generate a multi-enemy encounter based on player level and difficulty."""
        pool = LOCATION_POOLS.get(location_id)
        if not pool:
            raise ValueError(f"Unknown location '{location_id}'")

        # Determine group size based on difficulty
        group_sizes = {
            "easy": (2, 3),
            "normal": (2, 4),
            "hard": (3, 4),
            "legendary": (3, 4),
            "boss": (1, 1),
        }

        min_group, max_group = group_sizes.get(difficulty, (1, 2))
        group_size = random.randint(min_group, max_group)

        enemies = []

        for _ in range(group_size):
            enemy = EncounterGenerator.choose_enemy_from_pool(pool, player)
            if enemy is None:
                continue

            EncounterGenerator.scale_enemy_stats(
                enemy, player.level, difficulty
            )

            enemies.append(enemy)

        #if not enemies:
        #    # fallback to a default enemy if the pool filtered everyone out
        #    enemy_instance = EnemyRegistry.get_enemy("Green Slime")
        #    EncounterGenerator.scale_enemy_stats(
        #        enemy_instance, player.level, difficulty
        #    )
        #    enemies.append(enemy_instance)

        return enemies


def weighted_choice(pool):
    """
    pool: list of (item, weight) tuples
    returns one item based on weight
    """
    total = sum(weight for item, weight in pool)
    r = random.uniform(0, total)
    upto = 0
    for item, weight in pool:
        if upto + weight >= r:
            return item
        upto += weight
    assert False, "Shouldn't get here"
