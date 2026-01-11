from copy import deepcopy
import random
from language.localization import translate
class Enemy:
    def __init__(self, 
                 id: str,
                 name: str, 
                 max_health: int,  
                 health: int,  
                 max_mana: int,  
                 mana: int,  
                 affinity: str, 
                 attack_power: int,  
                 physical_resistance: int, 
                 magical_resistance: int, 
                 weapons=None,
                 inventory=None,
                 xp_reward=0, 
                 description=None,
                 base_level=1,
                 loot_table=None):
        self.id = id.lower()
        self.name = name
        self.max_health = max_health
        self.health = health
        self.max_mana = max_mana
        self.mana = mana
        self.affinity = affinity
        self.attack_power = attack_power
        self.physical_resistance = physical_resistance
        self.magical_resistance = magical_resistance
        self.weapons = weapons if weapons else []  # List of Weapon objects (default empty)
        self.inventory = inventory if inventory else []  # List of Item objects (default empty)
        self.xp_reward = xp_reward
        self.description = description
        self.base_level = base_level
        self.loot_table = loot_table if loot_table else []  # List of Loot objects (default empty)

    def __str__(self):
        return f"{self.name} (HP: {self.health}/{self.max_health}, MP: {self.mana}/{self.max_mana})"

    __repr__ = __str__  

    @property
    def is_alive(self):
        """Returns True if the enemy's health is greater than 0, otherwise False."""
        return self.health > 0

    def attack(self, player, weapon=None):
        base_damage = self.attack_power
        if weapon:
            base_damage += weapon.damage_amount
            if weapon.damage_type == "magic":
                base_damage += getattr(self, "base_magic_dmg", 0)

        # --- Damage variance
        variance = random.uniform(0.75, 1.15)
        damage = int(base_damage * variance)

        # --- Apply player's resistance
        if weapon and weapon.damage_type == "magic":
            damage_amount = max(damage - player.magic_resist, 0)
        else:
            damage_amount = max(damage - player.armor, 0)
      
        player.take_damage(damage_amount)
        return damage_amount

    def take_damage(self, damage):
        if isinstance(damage, str):  # Check for potential string input
            print(f"Error: Damage should be an integer, not {type(damage)}")
        else:
            self.health -= damage
            if self.health < 0:
                self.health = 0
            print(f"{self.name} took {damage} damage. Health: {self.health}/{self.max_health}")

    def roll_loot(self):
        """
        Returns a list of items dropped by this enemy based on their loot table.
        Could support multiple drops with probability.
        """
        dropped = []
        for item, weight in self.loot_table:
            if random.random() < weight:
                dropped.append(item)
        return dropped

class EnemySpecies:
    """Defines a base enemy species"""

    _species_registry: dict[str, "EnemySpecies"] = {}

    def __init__(
        self,
        id: str,
        name: str,
        base_stats: dict,
        name_key: str | None = None,
        description_key: str | None = None,
    ):
        self.id = id.lower()
        self._name = name
        self.name_key = name_key
        self.description_key = description_key
        self.base_stats = base_stats

        if self.id in EnemySpecies._species_registry:
            raise ValueError(f"Species ID '{self.id}' already registered!")

        EnemySpecies._species_registry[self.id] = self

    # ---- Display / translation layer ----

    def display_name(self) -> str:
        """
        Returns the translated display name.
        Hook this into your localization system later.
        """
        if self.name_key:
            return translate(self.name_key)  # your i18n hook
        return self._name
    
    def display_description(self) -> str:
        if self.description_key:
            return translate(self.description_key)
        return self.base_stats.get("description", "")

    # ---- Registry lookups ----

    @classmethod
    def get_species(cls, species_id: str) -> "EnemySpecies | None":
        return cls._species_registry.get(species_id.lower())

    @classmethod
    def get_species_by_display_name(cls, display_name: str) -> "EnemySpecies | None":
        display_name_lower = display_name.lower()
        for species in cls._species_registry.values():
            if species.display_name().lower() == display_name_lower:
                return species
        return None

    @classmethod
    def normalize_species(cls, value: str) -> str:
        """
        Normalize arbitrary input into a canonical species ID.
        Accepts ID or display name.
        """
        value = value.lower()

        # Already an ID
        if value in cls._species_registry:
            return value

        # Try display name
        species = cls.get_species_by_display_name(value)
        if species:
            return species.id

        raise ValueError(f"Unknown enemy species: {value}")

    @classmethod
    def list_species(cls) -> list[str]:
        return list(cls._species_registry.keys())
    
class EnemyType:
    """Defines a subtype of an EnemySpecies (like 'green slime')."""

    _type_registry: dict[str, "EnemyType"] = {}

    def __init__(
        self,
        id: str,
        species: str,
        name: str,
        overrides: dict | None = None,
        name_key: str | None = None,
        description_key: str | None = None,
    ):
        species_id = EnemySpecies.normalize_species(species)
        species_obj = EnemySpecies.get_species(species_id)

        self.id = id.lower()
        self.name = name
        self.name_key = name_key
        self.description_key = description_key
        self.species_id = species_id
        self.species = species_obj

        self.stats = deepcopy(species_obj.base_stats)
        if overrides:
            self.stats.update(overrides)

        if self.id in EnemyType._type_registry:
            raise ValueError(f"EnemyType ID '{self.id}' already registered!")

        EnemyType._type_registry[self.id] = self

    def create_enemy(self, display_name=None):
        final_name = display_name or f"{self.name} {self.species.display_name()}"

        return Enemy(
            id=final_name.lower(),
            name=final_name,
            **self.stats
        )
    
    def display_name(self) -> str:
        if self.name_key:
            return translate(self.name_key)
        return f"{self.name} {self.species.display_name()}"

    def display_description(self) -> str:
        if self.description_key:
            return translate(self.description_key)
        return self.stats.get("description", "")

    def create_enemy(self, display_name=None):
        final_name = display_name or self.display_name()

        return Enemy(
            id=self.id,
            name=final_name,
            **self.stats
        )

    @classmethod
    def get_type(cls, type_id: str) -> "EnemyType | None":
        return cls._type_registry.get(type_id.lower())

    @classmethod
    def list_types(cls) -> list[str]:
        return list(cls._type_registry.keys())

class EnemyRegistry:
    _enemies: dict[str, Enemy] = {}

    @classmethod
    def register_enemy(cls, enemy: Enemy):
        """
        Registers an enemy in the registry.
        """
        if enemy.id in cls._enemies:
            raise ValueError(f"Enemy ID '{enemy.id}' is already registered!")
        cls._enemies[enemy.id] = enemy

    @classmethod
    def get_enemy(cls, enemy_type_id: str):
        """
        Retrieves an enemy by name.
        Returns None if the enemy is not found.
        """
        enemy_type = EnemyType.get_type(enemy_type_id)
        if enemy_type is None:
            return None
        return enemy_type.create_enemy()
    
    @classmethod
    def is_enemy_registered(cls, name):
        """
        Checks if an enemy with the given name is registered.
        """
        return name in cls._enemies

    @classmethod
    def list_enemies(cls):
        """
        Returns a list of all registered enemy names.
        """
        return list(cls._enemies.keys())

    @classmethod
    def remove_enemy(cls, name):
        """
        Removes an enemy from the registry by name.
        Raises a KeyError if the enemy is not found.
        """
        if name not in cls._enemies:
            raise KeyError(f"Enemy '{name}' is not registered!")
        del cls._enemies[name]

def create_enemy(specie, type_name, overrides=None, display_name=None):
    """
    Create and register an enemy with optional overrides, base level, and loot table.

    Example usage:
    >>> enemy1 = create_enemy("Slime", "Green Slime", overrides={"max_health": 70, "health": 70})
    >>> enemy2 = create_enemy(
    ...     "Spider",
    ...     "Venom Arachnid",
    ...     display_name="Venomous Arachnid",
    ...     overrides={"base_level": 5, "loot_table": [(health_potion, 0.5)]}
    ... )
    """

    # Normalize species (accepts ID or display name)
    species_id = EnemySpecies.normalize_species(specie)

    # Prepare normalized type_name for matching
    type_name_norm = type_name.replace("_", " ").strip().lower()

    # Find matching EnemyType by species + name
    enemy_type = None
    for et in EnemyType._type_registry.values():
        if et.species_id != species_id:
            continue

        full_name_norm = f"{et.name} {et.species.display_name()}".replace("_", " ").strip().lower()

        if et.name.lower() == type_name_norm or full_name_norm == type_name_norm:
            enemy_type = et
            break

    if not enemy_type:
        raise ValueError(f"EnemyType '{type_name}' not found for species '{specie}'")

    # Create enemy from type
    enemy = enemy_type.create_enemy(display_name=display_name)

    # Apply per-instance overrides (do NOT mutate the type)
    if overrides:
        for key, value in overrides.items():
            if not hasattr(enemy, key):
                raise AttributeError(f"Enemy has no attribute '{key}'")
            setattr(enemy, key, value)

    # Register and return
    EnemyRegistry.register_enemy(enemy)
    return enemy

              
#aList = ["Snake", "Spider", "Mouse", "Walking Corpse", "Skeleton", "Ghoul", 
#         "Banshee", "Ghost", "Soul", "Wolf", "Jackel", "Dahrk Hound"]
#enem_sub_types = ["Pirate Deckhand", "Pirate Gunslinger", "Pirate First Mate", "Pirate Quartermaster", 
#                  "Pirate Powder Monkey", "Pirate Captian", "Pirate Grunt", "Bandit Chief",
#                  "Cultist Grunt", "Cultist Wizard", "Cultist Priest", "Cultist Grand Wizard", 
#                  "Arch Demon", "Blood Demon", "Succubi Demon",
#                  "Incubi Demon", "Beserking Ghoul", "Revenant", "Forest Banshee", "Ghrotto Banshee", 
#                  "Fortress Banshee", "Ghost Shade", "Ghost Shadow", "Ghost Wisp", "Fire Soul", "Aqua Soul",
#                  "Earth Soul", "Air Soul", "Lightning Soul", "Light Soul", "Brown Wolf", "Snow Wolf", "Gray Wolf", 
#                  "Dire Wolf", ]

enemy_type_overrides = {
    "pickpocket": {"max_health": 70, "health": 70},
    "prowler": {"max_health": 70, "health": 70},
    "myrmidon": {"max_health": 70, "health": 70},
    "assassin": {"max_health": 70, "health": 70},
    "warrior": {"max_health": 70, "health": 70},
    "bandit": {"max_health": 70, "health": 70},
    "bandit_chief": {"max_health": 85, "health": 85},
}

def register_species_archetypes(species_id: str, base_stats: dict, name_prefix=None):
    """
    Generic helper to register a species and all its archetypes.
    
    Args:
        species_id: ID for the species (e.g., "human", "drider")
        base_stats: dict of base stats for the species
        name_prefix: Optional display name prefix for archetypes
    Returns:
        list of instantiated Enemy objects
    """
    from creatures.enemy_npc import EnemySpecies, EnemyType, EnemyRegistry, enemy_type_overrides

    name_prefix = name_prefix or species_id.replace("_", " ").title()
    
    # species
    species_obj = EnemySpecies(
        id=species_id,
        name=name_prefix,
        base_stats=base_stats,
        name_key=f"creatures.species.{species_id}.name",
        description_key=f"creatures.species.{species_id}.description"
    )

    # archetypes
    registered_enemies = []
    for archetype_name, overrides in enemy_type_overrides.items():
        type_id = f"{species_id}_{archetype_name}"

        # Create EnemyType
        EnemyType(
            id=type_id,
            species=species_id,
            name=archetype_name.replace("_", " ").title(),
            overrides=overrides
        )

        # Instantiate the enemy and register it
        enemy_instance = EnemyType.get_type(type_id).create_enemy()
        EnemyRegistry.register_enemy(enemy_instance)
        registered_enemies.append(enemy_instance)

    return registered_enemies

print("Successfully Imported Enemies")

#Enemy Dictionary
enemies = {
    
    "Reptile" : { #Reptile
        1 : { #Wild Snake
            "Name" : ("Wild Snake"),
            "Health" : 10,
            "Damage" : 5,
            "Magic Damage" : 15,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("Isle", "Island", "Forest", "Lake/Ocean", "Cave", "Plain/Meadow", "Open", "Mountain", "Marsh", "River", "Valley"),
            "Frequency" : 9,
            "Level Requirement" : 0,
        },
        2 : { #Savage Alligator
            "Name" : ("Savage Alligator"),
            "Health" : 15,
            "Damage" : 30,
            "Magic Damage" : 15,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("Marsh", "River"),
            "Frequency" : 1,
            "Level Requirement" : 0,
        },
        3 : { #Silver Serpent
            "Name" : ("Silver Serpent"),
            "Health" : 15,
            "Damage" : 10,
            "Magic Damage" : 15,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("River", "Orchard", "Isle"),
            "Frequency" : 1,
            "Level Requirement" : 0,
        },
        4 : { #Drake
            "Name" : ("Drake"),
            "Description" : "",
            "Health" : 375,
            "Damage" : 125,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("Coast"),
            "Frequency" : 3,
            "Level Requirement" : 30,
        },
        5 : { #Flying Serpent
            "Name" : ("Flying Serpent"),
            "Description" : "A Massive Legless, Flying Reptile. ",
            "Health" : 350,
            "Damage" : 115,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
        6 : { #Nogard
            "Name" : ("Nogard"),
            "Description" : "",
            "Health" : 400,
            "Damage" : 130,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("Cave", "Plateau", "Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 20,
        },
        7 : { #Hydra
            "Name" : ("Hydra"),
            "Description" : "",
            "Health" : 420,
            "Damage" : 130,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("Dungeon"),
            "Frequency" : 1,
            "Level Requirement" : 26,
        },
    },
    "Naga" : { #Naga
        "1" : { #Sea Naga
            "Name" : ("Sea Naga"),
            "Health" : 70,
            "Damage" : 25,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("Lake/Ocean", "Island", "Marsh", "River", "Coast"),
            "Frequency" : 1,
            "Level Requirement" : 12,
        },
        "2" : { #Forest Naga
            "Name" : ("Forest Naga"),
            "Health" : 80,
            "Damage" : 25,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Location Type" : ("Dense Forest", "Grove", "Forest"),
            "Frequency" : 3,
            "Level Requirement" : 12,
        },
    },
    "Wyrm" : { #Wyrm
        "1" : {
            "Name" : "Oasis Wyrm",
            "Desription" : "",
            "Location Type" : ("?"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "2" : {
            "Name" : "Steppe Wyrm",
            "Desription" : "",
            "Location Type" : ("Plateau", "Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "3" : {
            "Name" : "Plains Wyrm",
            "Desription" : "",
            "Location Type" : ("Plain/Meadow"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "4" : {
            "Name" : "Plateuaus Wyrm",
            "Desription" : "",
            "Location Type" : ("Plateau"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "5" : {
            "Name" : "Forest Wyrm",
            "Desription" : "",
            "Location Type" : ("Forest"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "6" : {
            "Name" : "Jungle Wyrm",
            "Desription" : "",
            "Location Type" : ("Dense Forest"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "7" : {
            "Name" : "Mountain Wyrm",
            "Desription" : "",
            "Location Type" : ("Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 30,
            "Frequency" : 1,
            "Level Requirement" : 20,
        },
        "8" : {
            "Name" : "Valley Wyrm",
            "Desription" : "",
            "Location Type" : ("Valley"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "9" : {
            "Name" : "Sky Wyrm",
            "Desription" : "",
            "Location Type" : ("?"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "10" : {
            "Name" : "Marsh Wyrm",
            "Desription" : "",
            "Location Type" : ("Marsh"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "11" : {
            "Name" : "Tundra Wyrm",
            "Desription" : "",
            "Location Type" : ("Tundra"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "12" : {
            "Name" : "Ocean Wyrm",
            "Desription" : "",
            "Location Type" : ("Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "13" : {
            "Name" : "Sea Wyrm",
            "Desription" : "",
            "Location Type" : ("Coast"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "14" : {
            "Name" : "Lake Wyrm",
            "Desription" : "",
            "Location Type" : ("Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "15" : {
            "Name" : "River Wyrm",
            "Desription" : "",
            "Location Type" : ("River"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
        "16" : {
            "Name" : ("Infant Wyrm"),
            "Description" : "",
            "Health" : 50,
            "Damage" : 5,
            "Magic Damage" : 0,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Cave"),
            "Frequency" : 1,
            "Level Requirement" : 30,
        },
    },
    

    "Sea Creatures": {
        1 : { #Titan
            "Titan" : {
                "Name" : ("Titan"),
                "Description" : "",
                "Health" : 250,
                "Damage" : 35,
                "Magic Damage" : 0,
                "Magic_Resistace" : 0,
                "Armor" : 0
            },
        },
        3 : { #Spirit
            "Spirit" : {
                1 : { #Oceanid
                    "Name" : ("Oceanid"),
                    "Description" : "",
                    "Health" : 75,
                    "Damage" : 25,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 0 
                },
                2 : { #Undine
                    "Name" : ("Undine"),
                    "Description" : "",
                    "Health" : 75,
                    "Damage" : 25,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 0 
                },
            },
        },
        4 : { #Fish
            "Fish" : {
                1 : { #Shark
                    "Name" : ("Shark"),
                    "Description" : "",
                    "Health" : 110,
                    "Damage" : 35,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 0 
                },
                2 : { #
                    "Name" : (""),
                    "Description" : "",
                    "Health" : 0,
                    "Damage" : 0,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 0 
                },
            },
        },
    },
    "Land Creatures/Monsters" : {
        1 : { #Mammals
            "Mammals" : {
                1 : { #Deer
                    "Deer" : {
                        1 : { #Deer
                            "Name" : ("Deer"),
                            "Description" : "",
                            "Health" : 25,
                            "Damage" : 5,
                            "Magic Damage" : 0,
                            "Magic_Resistace" : 0,
                            "Armor" : 0 
                        },
                        2 : { #Faun
                            "Name" : ("Faun"),
                            "Description" : "",
                            "Health" : 20,
                            "Damage" : 5,
                            "Magic Damage" : 0,
                            "Magic_Resistace" : 0,
                            "Armor" : 0 
                        },
                        3 : { #Elk
                            "Name" : ("Elk"),
                            "Description" : "",
                            "Health" : 40,
                            "Damage" : 5,
                            "Magic Damage" : 0,
                            "Magic_Resistace" : 0,
                            "Armor" : 0 
                        },
                    },
                },
                2 : { #Rat
                        "Name" : ("Rats"),
                        "Description" : "",
                        "Health" : 5,
                        "Damage" : 5,
                        "Magic Damage" : 0,
                        "Magic_Resistace" : 0,
                        "Armor" : 0
                        },
                },
            },
        2 : { #ENT
            "Ent" : {
                1 : { #Ent
                    "Name" : ("Ent"),
                    "Description" : "",
                    "Health" : 150,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 0,
                    "Armor" : 5
                },
                2 : { #Towering Ent
                    "Name" : ("Towering Ent"),
                    "Description" : "",
                    "Health" : 175,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 0,
                    "Armor" : 40 
                },
                3 : { #Oak Wood Ent
                    "Name" : ("Oak Wood Ent"),
                    "Description" : "",
                    "Health" : 200,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 15,
                    "Armor" : 10
                },
                4 : { #Birch Wood Ent
                    "Name" : ("Birch Wood Ent"),
                    "Description" : "",
                    "Health" : 230,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 20,
                    "Armor" : 20
                },
                5 : { #Baarker Wood Ent
                    "Name" : ("Baarker Wood Ent"),
                    "Description" : "",
                    "Health" : 250,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 15,
                    "Armor" : 15 
                },
                6 : { #Iron Wood Ent
                    "Name" : ("Iron Wood Ent"),
                    "Description" : "",
                    "Health" : 255,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 5,
                    "Armor" : 20
                },
                7 : { #Silver Wood Ent
                    "Name" : ("Silver Wood Ent"),
                    "Description" : "",
                    "Health" : 260,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 5,
                    "Armor" : 30
                },
                8 : { #Golden Wood Ent
                    "Name" : ("Golden Wood Ent"),
                    "Description" : "",
                    "Health" : 275,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 40,
                    "Armor" : 10
                },
                9 : { #Rose Wood Ent
                    "Name" : ("Rose Wood Ent"),
                    "Description" : "",
                    "Health" : 290,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 50,
                    "Armor" : 0
                },
                10 : { #Diamond Wood Ent
                    "Name" : ("Diamond Wood Ent"),
                    "Description" : "",
                    "Health" : 300,
                    "Damage" : 0,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 0,
                    "Armor" : 45
                },
            },
        },
        3 : { #Mysticals
            "Mysticals" : {
                1 : { #Nymph
                    "Nymph" : {
                        1 : { #Blue Nymph
                            "Name" : ("Blue Nymph"),
                            "Description" : "",
                            "Health" : 30,
                            "Damage" : 0,
                            "Magic Damage" : 10,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                        2 : { #Red Nymph
                            "Name" : ("Red Nymph"),
                            "Description" : "",
                            "Health" : 30,
                            "Damage" : 0,
                            "Magic Damage" : 10,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                        3 : { #Yellow Nymph
                            "Name" : ("Yellow Nymph"),
                            "Description" : "",
                            "Health" : 30,
                            "Damage" : 0,
                            "Magic Damage" : 10,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                        4 : { #Elegant Nymph
                            "Name" : ("Elegant Nymph"),
                            "Description" : "",
                            "Health" : 30,
                            "Damage" : 0,
                            "Magic Damage" : 10,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                        5 : { #Shining Nymph
                            "Name" : ("Shining Nymph"),
                            "Description" : "",
                            "Health" : 30,
                            "Damage" : 0,
                            "Magic Damage" : 10,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                    },
                },
                2 : { # Spriggan
                    "Spriggan" : {
                        1 : {
                            "Name" : ("Spriggan"),
                            "Description" : "",
                            "Health" : 75,
                            "Damage" : 12,
                            "Magic Damage" : 13,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                    },
                },
                3 : { # Dryad
                        "Dryad" : {
                            1 : {
                                "Name" : ("Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                                },
                            },
                            2 : {
                                "Name" : ("Oak Wood Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                            3 : {
                                "Name" : ("Birch Wood Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                            4 : {
                                "Name" : ("Baarker Wood Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                            5 : {
                                "Name" : ("Iron Wood Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                            6 : {
                                "Name" : ("Silver Wood Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                            7 : {
                                "Name" : ("Golden Wood Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                            8 : {
                                "Name" : ("Rose Wood Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                            9 : {
                                "Name" : ("Diamond Wood Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 5,
                                "Magic Damage" : 20,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                            10 : {
                                "Name" : ("Dryad"),
                                "Description" : "",
                                "Health" : 75,
                                "Damage" : 10,
                                "Magic Damage" : 15,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                            },
                        },
                4 : { # Forest Spirit
                    "Forest Spirit" : {
                        1 : { #Forest Sylph
                                "Name" : ("Forest Sylph"),
                                "Description" : "",
                                "Health" : 5,
                                "Damage" : 0,
                                "Magic Damage" : 5,
                                "Magic_Resistace" : 0,
                                "Armor" : 0
                                },
                        2 : { #Forest Undine
                            "Name" : ("Forest Undine"),
                            "Description" : "",
                            "Health" : 65,
                            "Damage" : 5,
                            "Magic Damage" : 10,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                    },
                },
                5 : { # Fairy
                    "Fairy" : {
                        1 : { #Fairy
                            "Name" : ("Fairy"),
                            "Description" : "",
                            "Health" : 5,
                            "Damage" : 0,
                            "Magic Damage" : 5,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                    },
                },
                6 : { # Golem
                    "Golem" : {
                        1 : { #Rock Golem
                            "Name" : ("Rock Golem"),
                            "Description" : "",
                            "Health" : 100,
                            "Damage" : 10,
                            "Magic Damage" : 25,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                        2 : { #Steam Golem
                            "Name" : ("Steam Golem"),
                            "Description" : "",
                            "Health" : 100,
                            "Damage" : 10,
                            "Magic Damage" : 25,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                        3 : { #Crystal Golem
                            "Name" : ("Crystal Golem"),
                            "Description" : "",
                            "Health" : 100,
                            "Damage" : 10,
                            "Magic Damage" : 25,
                            "Magic_Resistace" : 0,
                            "Armor" : 0
                        },
                    },
                },
            },
        },
        4 : { #Monters
            1 : { #Frohst
                "Name" : ("Frohst"),
                "Description" : "",
                "Health" : 90,
                "Damage" : 0,
                "Magic Damage" : 3,
                "Magic_Resistace" : 0,
                "Armor" : 0
            },
            2 : { #Mimic
                "Name" : ("Mimic"),
                "Description" : "",
                "Health" : 50,
                "Damage" : 20,
                "Magic Damage" : 0,
                "Magic_Resistace" : 0,
                "Armor" : 0
            },
            4 : { #Giant
                "Name" : ("Giant"),
                "Description" : "",
                "Health" : 65,
                "Damage" : 20,
                "Magic Damage" : 0,
                "Magic_Resistace" : 0,
                "Armor" : 0
            },
        },
    },#<--End of Land Creatures/Monsters
}#END