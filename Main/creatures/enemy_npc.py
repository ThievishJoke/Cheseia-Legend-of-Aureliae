class Enemy:
    def __init__(self, name, max_health, health, max_mana, mana, 
                 affinity,
                 attack_power, physical_resistance, magical_resistance, 
                 weapons=None, inventory=None,
                 xp_reward=0, description=None):
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

    @property
    def is_alive(self):
        """Returns True if the enemy's health is greater than 0, otherwise False."""
        return self.health > 0

    def attack(self, player, weapon=None):
        """Handles the enemy's attack."""
        if weapon:
            damage = self.attack_power + weapon.damage_amount
            if weapon.damage_type == "magic":
                damage += self.base_magic_dmg  # If the weapon is magic, apply magic damage
        else:
            damage = self.attack_power  # Just use the attack power for regular attacks
        
        # Apply the player's resistance (magic vs physical)
        if weapon and weapon.damage_type == "magic":
            damage = max(damage - player.magic_resist, 0)
        else:
            damage = max(damage - player.armor, 0)
        
        # Deal damage to the player
        player.take_damage(damage)
        return damage

    def take_damage(self, damage):
        if isinstance(damage, str):  # Check for potential string input
            print(f"Error: Damage should be an integer, not {type(damage)}")
        else:
            self.health -= damage
            if self.health < 0:
                self.health = 0
            print(f"{self.name} took {damage} damage. Health: {self.health}/{self.max_health}")

class EnemyRegistry:
    _enemies = {}

    @classmethod
    def register_enemy(cls, enemy):
        """
        Registers an enemy in the registry.
        """
        if enemy.name in cls._enemies:
            raise ValueError(f"Enemy '{enemy.name}' is already registered!")
        cls._enemies[enemy.name] = enemy

    @classmethod
    def get_enemy(cls, name):
        """
        Retrieves an enemy by name.
        Returns None if the enemy is not found.
        """
        return cls._enemies.get(name)

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

def create_enemy(specie, type_name, overrides=None):
    """Create and register an enemy with optional overrides."""
    base_stats = {
        "max_health": 65,
        "health": 65,
        "max_mana": 0,
        "mana": 0,
        "affinity": "",
        "attack_power": 20,
        "physical_resistance": 0,
        "magical_resistance": 0,
        "weapons": [],
        "inventory": [],
        "xp_reward": 50,
        "description": f"A {specie.lower()} {type_name.lower()} prowling the lands.",
    }
    # Apply overrides if provided
    if overrides:
        base_stats.update(overrides)

    # Create and register the enemy
    enemy = Enemy(name=f"{specie} {type_name}", **base_stats)
    EnemyRegistry.register_enemy(enemy)
    return enemy

green_slime = Enemy(
    name="Green Slime",
    max_health=10,
    health=10,
    max_mana=0,
    mana=0,
    affinity="Water",
    attack_power=5,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description="A small green blob of living goo"
)
red_slime = Enemy(
    name="Red Slime",
    max_health=15,
    health=15,
    max_mana=0,
    mana=0,
    affinity="Water",
    attack_power=7,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description="A small red blob of living goo"
)
widower_arachnid = Enemy(
    name="Widower Arachnid",
    max_health=15,
    health=15,
    max_mana=0,
    mana=0,
    affinity="Soul",
    attack_power=10,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
giant_spider = Enemy(
    name="Giant Spider",
    max_health=20,
    health=20,
    max_mana=0,
    mana=0,
    affinity="",
    attack_power=12,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
death_widow = Enemy(
    name="Death Widow",
    max_health=20,
    health=20,
    max_mana=0,
    mana=0,
    affinity="",
    attack_power=15,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
moth_spiderling = Enemy(
    name="Moth Spiderling",
    max_health=20,
    health=20,
    max_mana=0,
    mana=0,
    affinity="Water",
    attack_power=15,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
crimson_brood = Enemy(
    name="Crimson Brood",
    max_health=25,
    health=25,
    max_mana=0,
    mana=0,
    affinity="",
    attack_power=30,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
wolf_spider = Enemy(
    name="Wolf Spider",
    max_health=20,
    health=20,
    max_mana=0,
    mana=0,
    affinity="",
    attack_power=17,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
frostbite_spider = Enemy(
    name="Frostbite Spider",
    max_health=30,
    health=30,
    max_mana=0,
    mana=0,
    affinity="Aqua",
    attack_power=25,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)

weakend_drider = Enemy(
    name="Weakend Drider",
    max_health=25,
    health=25,
    max_mana=0,
    mana=0,
    affinity="",
    attack_power=15,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
vigored_drider= Enemy(
    name="Vidgored Drider",
    max_health=50,
    health=50,
    max_mana=0,
    mana=0,
    affinity="",
    attack_power=20,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
tenacious_drider = Enemy(
    name="Solid Drider",
    max_health=75,
    health=75,
    max_mana=0,
    mana=0,
    affinity="Earth",
    attack_power=30,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
drider_princess = Enemy(
    name="Drider Princess",
    max_health=85,
    health=85,
    max_mana=0,
    mana=0,
    affinity="",
    attack_power=7,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)
drider_queen = Enemy(
    name="Drider Queen",
    max_health=100,
    health=100,
    max_mana=0,
    mana=0,
    affinity="",
    attack_power=65,
    physical_resistance=0,
    magical_resistance=0,
    weapons=[],
    inventory=[],
    xp_reward=50,
    description=""
)

species = ["Human", "Drider", "Kitsune", "Demon", "Cambion", "Demon Halfling", "Lamia", "Changeling"]
enem_types = ["Pickpocket", "Prowler", 
              "Myrmidon", "Assassin", "Warrior", "Bandit", "Bandit Chief"]

'''for specie in species:
    for enem_type in enem_types:
        if enem_type == "Warrior":
            create_enemy(specie, enem_type, overrides={"max_health": 70, "health": 70})
        if enem_type == "Bandit":
            create_enemy(specie, enem_type, overrides={"max_health": 70, "health": 70})
        if enem_type == "Bandit Chief":
            create_enemy(specie, enem_type, overrides={"max_health": 85, "health": 85})
        else:
            create_enemy(specie, enem_type)'''

for specie in species:
    for enem_type in enem_types:
        if enem_type == "Pickpocket":
            create_enemy(specie, "Pickpocket", overrides={"max_health": 70, "health": 70})
        if enem_type == "Prowler":
            create_enemy(specie, "Prowler", overrides={"max_health": 70, "health": 70})
        if enem_type == "Myrmidon":
            create_enemy(specie, "Myrmidon", overrides={"max_health": 70, "health": 70})
        if enem_type == "Assassin":
            create_enemy(specie, "Assassin", overrides={"max_health": 70, "health": 70})
        if enem_type == "Warrior":
            create_enemy(specie, enem_type, overrides={"max_health": 70, "health": 70})
        if enem_type == "Bandit":
            create_enemy(specie, enem_type, overrides={"max_health": 70, "health": 70})
        if enem_type == "Bandit Chief":
            create_enemy(specie, enem_type, overrides={"max_health": 85, "health": 85})

EnemyRegistry.register_enemy(green_slime)
EnemyRegistry.register_enemy(red_slime)

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
    "Dragon" : {
        "1" : { #Fire Dragon
            "Name" : ("Fire Dragon"),
            #"Description" : "Fire Dragons Will Attack From Afar With Large Plumes Of Fire From Its Mouth. Lurks In Large Open Volcanic Caverns, Or Mountians." 
            #"Most Common Elemental Dragon. Connot Become A Powerful One"
            #"Immunity To Air, Pure Air Feeds Their Element Core, And They Will Burn Brighter And Hotter. Enpowering Them With A Super Powerful Fireball."
            #"It Said That A Large Thunder Of Fire Dragons Can Cause Catastrophic Volcanic Activity."
            #,
            "Health" : 500,
            "Damage" : 130,
            "Magic Damage" : 40,
            "Magic Resistance" : 10, 
            "Armor" : 60,
            "Powerful One" : False,
            "Location Type" : ("Valley", "Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "2" : { #Aqua Dragon
            "Name" : ("Aqua Dragon"),
            #"Description" : "Aqua Dragons Are Alike Fire Dragons In That Attack From Afar, But With Exhaling Scalding Hot Water. Resides Near And In Various Bodies Of Water. "
            #"Second Most Common Elemental Dragon. Are Capeable Of Becoming A Powerful One, But It Is EXTREMELY RARE. "
            #"Aqua Dragons Found In The Snowy Tundra Are More Adept At Cooling Water From Their Cores, And Instead Of Scalding Water, Exhale Icy Mist Or Entire Icicles. "
            #"It's Believed That A Single Enraged Aqua Dragon Can Cause Tarential Downpours, Flooding Low Basins, And Large Swaulthves Of Land Near Souces Of Water."
            #,
            "Health" : 500,
            "Damage" : 70,
            "Magic Damage" : 100,
            "Magic Resistance" : 0,
            "Armor" : 55,
            "Powerful One" : True,
            "Location Type" : ("River", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "3" : { #Earth Dragon
            "Name" : ("Earth Dragon"),
            #"Description" : "Earth Dragons Unlike A Lot Of Other Dragons Fight Close To The Ground, And Munipulate Their Surroundings With Force To Subdue Their Challengers. "
            #"Reside In Caverns, Caves, Mountaintops, And Deep Under The Planets Mantle. "
            #"Earth Dragons' Bodies Are Almalgomations Of Rare Minerals, And Metals. Due To This They Lack The Magical Scales Other Dragons Have To Protect Them From Magic. "
            #"Fourth Most Common Elemental Dragon. Earth Dragon Who Become Powerful Ones Can Be Unstoppable Behemiths With An Unparreleled Ability To Sustain Tons Of Damage. "
            #"Should A Earth Dragon Take Resedance Near You, It Can Offer Protection From Wyrms, And Other Large Monsters For Matalic Coins It Likes To Snack On. "
            #,
            "Health" : 500,
            "Damage" : 170,
            "Magic Damage" : 0,
            "Magic Resistance" : -30,
            "Armor" : 120,
            "Powerful One" : True,
            "Location Type" : ("Cave", "Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "4" : { #Air Dragon
            "Name" : ("Air Dragon"),
            "Description" : "",
            "Health" : 500,
            "Damage" : 170,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Powerful One" : True,
            "Location Type" : ("Meadow"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "5" : { #Lightning Dragon
            "Name" : ("Lightning Dragon"),
            "Description" : "",
            "Health" : 500,
            "Damage" : 170,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Powerful One" : False,
            "Location Type" : ("Marsh"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "6" : { #Light Dragon
            "Name" : ("Light Dragon"),
            "Description" : "",
            "Health" : 500,
            "Damage" : 170,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Powerful One" : True,
            "Location Type" : ("Forest", "Welkin"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "7" : { #Dark Dragon
            "Name" : ("Dark Dragon"),
            "Description" : "",
            "Health" : 500,
            "Damage" : 170,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Powerful One" : True,
            "Location Type" : ("The Subterrane"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "8" : { #Eclipse Dragon
            "Name" : ("Eclipse Dragon"),
            "Description" : "",
            "Health" : 500,
            "Damage" : 170,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Powerful One" : True,
            "Location Type" : ("Dense Forest"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "9" : { #Lunar Dragon
            "Name" : ("Lunar Dragon"),
            "Description" : "",
            "Health" : 500,
            "Damage" : 170,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Powerful One" : True,
            "Location Type" : ("Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "10" : { #Dragon
            "Name" : ("Natural Dragon"),
            #"Description" : "Natural Dragons Are . "
            #"They Can Also Be Summoned As A Result Of The Failed Attempt Of Reviving A Dead Dragon. "
            #"Being Barely 'Alive' As Its Is They Are Normally Really Frail. "
            #"A Natural Dragon Is A Fairly Rare Dragon Encounter. ",
            #"Natural Dragons Are Subservient To Humans And Demons As They Have A Cute Almost Pet Like Nature"
            #"Natural Dragons Do Small Tasks For Their Caretaker"
            "Health" : 100,
            "Damage" : 90,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Powerful One" : False,
            "Location Type" : ("Dense Forests", "Forest", "Town", "City", "Capital City"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "11" : { #Soul Dragon
            "Name" : ("Soul Dragon"),
            #"Description" : "A Soul Dragon Is The Collection Of Many Souls, And Have Varrying Magical Powers, Depending On Its Envirnment. "
            #"Residence: Unknown "
            #"Soul Dragons Are By Proxy Technically An Elemental Dragon By Only Being Able To Manafest One Of The Five Elemental Dragons Powers (A Powerful One Is An Execption Have More Than One). "
            #"Only In The Case Of Soul Dragons They Might Possiably Be Immune To Physical Attacks. A Powerful One Is Basically A Local God To Its Region, Muniplating Terrain, Influencing Fate, And Exerting Its Magical Authority. "
            #"Being Simply A Body Of Trapped Souls, Makes Them Common, But Still Significally Rarer Than The Normal Elemental Dragons. ",
            "Health" : 200,
            "Damage" : 0,
            "Magic Damage" : 180,
            "Magic Resistance" : 0,
            "Armor" : 90,
            "Powerful One" : True,
            "Location Type" : ("Ruin"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
        "12" : { #Blood Dragon
            "Name" : ("Blood Dragon"),
            #"Description" : "",
            "Health" : 500,
            "Damage" : 0,
            "Magic Damage" : 170,
            "Magic Resistance" : 0,
            "Armor" : 0,
            "Powerful One" : True,
            "Location Type" : ("City", "Capital City"),
            "Frequency" : 1,
            "Level Requirement" : 25,
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

    "Pirate" : {
        1 : { #Deckhand
            "Name" : ("Deckhand"),
            "Description" : "",
            "Health" : 50,
            "Damage" : 5,
            "Magic Damage" : 0,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
        2 : { #Gunslinger
            "Name" : ("Gunslinger"),
            "Description" : "",
            "Health" : 45,
            "Damage" : 20,
            "Magic Damage" : 0,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
        3 : { #First Mate
            "Name" : ("First Mate"),
            "Description" : "",
            "Health" : 60,
            "Damage" : 15,
            "Magic Damage" : 0,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
        4 : { #Quartermaster
            "Name" : ("Quartermaster"),
            "Description" : "",
            "Health" : 50,
            "Damage" : 10,
            "Magic Damage" : 0,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
        5 : { #Powder Monkey
            "Name" : ("Powder Monkey"),
            "Description" : "",
            "Health" : 40,
            "Damage" : 10,
            "Magic Damage" : 0,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
        6 : { #Captian
            "Name" : ("Captian"),
            "Description" : "",
            "Health" : 70,
            "Damage" : 25,
            "Magic Damage" : 0,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
    },
    
    "Cultist" : {
        1 : { #Cultist Grunt
            "Name" : ("Cultist Grunt"),
            "Description" : "",
            "Health" : 75,
            "Damage" : 0,
            "Magic Damage" : 15,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
        2 : { #Cultist Wizard
            "Name" : ("Cultist Wizard"),
            "Description" : "",
            "Health" : 90,
            "Damage" : 0,
            "Magic Damage" : 30,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
        3 : { #Cultist Grand Wizard
            "Name" : ("Cultist Grand Wizard"),
            "Description" : "",
            "Health" : 120,
            "Damage" : 0,
            "Magic Damage" : 50,
            "Magic Resistance" : 0, 
            "Armor" : 0,
            "Location Type" : ("Coast", "Lake/Ocean"),
            "Frequency" : 1,
            "Level Requirement" : 15,
        },
    },
    "Pure Demon" : {
        1 : { #Demon
            "Name" : ("Demon"),
            "Description" : "",
            "Health" : 73,
            "Damage" : 24,
            "Magic Damage" : 0,
            "Magic Resistance" : 35,
            "Armor" : 20,
            "Location Type" : ("Dense Forest", "City"),
        },
        2 : { #Arch Demon
            "Name" : ("Arch Demon"),
            "Description" : "",
            "Health" : 90,
            "Damage" : 28,
            "Magic Damage" : 0,
            "Magic Resistance" : 20,
            "Armor" : 15,
            "Location Type" : ("Dense Forest"),
        },
        3 : { #Devil
            "Name" : ("Devil"),
            "Description" : "",
            "Health" : 91,
            "Damage" : 26,
            "Magic Damage" : 0,
            "Magic Resistance" : 20,
            "Armor" : 15,
            "Location Type" : ("Dense Forest"),
        },
        4 : { #Blood Devil
            "Name" : ("Blood Devil"),
            "Description" : "",
            "Health" : 91,
            "Damage" : 0,
            "Magic Damage" : 26,
            "Magic Resistance" : 15,
            "Armor" : 33,
            "Location Type" : ("Dense Forest"),
        },
        5 : { #Incubi
            "Name" : ("Incubi"),
            "Description" : "",
            "Health" : 132,
            "Damage" : 0,
            "Magic Damage" : 32,
            "Magic Resistance" : 35,
            "Armor" : 22,
            "Location Type" : ("Dense Forest"),
        },
        6 : { #Succubi
            "Name" : ("Succubi"),
            "Description" : "",
            "Health" : 135,
            "Damage" : 0,
            "Magic Damage" : 30,
            "Magic Resistance" : 32,
            "Armor" : 29,
            "Location Type" : ("Dense Forest", "City"),
        },
    },
    "Demon Hybrid" : {
        1 : { #Dire
            "Name" : ("Dire"),
            "Description" : "",
            "Health" : 170,
            "Damage" : 37,
            "Magic Damage" : 0,
            "Magic Resistance" : 23,
            "Armor" : 11,
            "Location Type" : ("Dense Forest", "Capital City"),
        }
    },
    "Skeleton" : {
        1 : {
            "Name" : ("Common Skeleton"),
            "Description" : "",
            "Health" : 70,
            "Damage" : 25,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 5
        },
    },
    "Zombie" : {
        1 : { #Ghoul
            "Name" : ("Ghoul"),
            "Description" : "",
            "Health" : 70,
            "Damage" : 18,
            "Magic Damage" : 0,
            "Magic Resistance" : 12,
            "Armor" : 2
        },
        2 : { #Beserking Ghoul
            "Name" : ("Beserking Ghoul"),
            "Description" : "",
            "Health" : 90,
            "Damage" : 21,
            "Magic Damage" : 0,
            "Magic Resistance" : 4,
            "Armor" : 3
        },
        3 : { #Draugr
            "Name" : ("Draugr"),
            "Description" : "",
            "Health" : 60,
            "Damage" : 14,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 12
        },
        4 : { #Revenant
            "Name" : ("Revenant"),
            "Description" : "",
            "Health" : 70,
            "Damage" : 12,
            "Magic Damage" : 0,
            "Magic Resistance" : 0,
            "Armor" : 31
        },
    },
    "Banshee" : {
        1 : { #Grotto Banshee
            "Name" : ("Grotto Banshee"),
            "Description" : "",
            "Health" : 60,
            "Damage" : 0,
            "Magic Damage" : 19,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        2 : { #Forest Banshee
            "Name" : ("Forest Banshee"),
            "Description" : "",
            "Health" : 56,
            "Damage" : 0,
            "Magic Damage" : 15,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        3 : { #Fortress Banshee
            "Name" : ("Fortress Banshee"),
            "Description" : "",
            "Health" : 111,
            "Damage" : 0,
            "Magic Damage" : 21,
            "Magic_Resistace" : 0,
            "Armor" : 0
        }
    },
    "Ghost" : {
        "1" : { #Shade
            "Name" : ("Shade"),
            "Description" : "",
            "Health" : 56,
            "Damage" : 0,
            "Magic Damage" : 15,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        "2" : { #Shadow
            "Name" : ("Shadow"),
            "Description" : "",
            "Health" : 95,
            "Damage" : 0,
            "Magic Damage" : 17,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        "3" : { #Wisp
            "Name" : ("Wisp"),
            "Description" : "",
            "Health" : 45,
            "Damage" : 0,
            "Magic Damage" : 40,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
    },
    "Soul" : {
        1 : { #Fire
            "Name" : ("Fire"),
            "Description" : "",
            "Health" : 70,
            "Damage" : 0,
            "Magic Damage" : 15,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        2 : { #Aqua
            "Name" : ("Aqua"),
            "Description" : "",
            "Health" : 48,
            "Damage" : 0,
            "Magic Damage" : 6,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        3 : { #Earth
            "Name" : ("Earth"),
            "Description" : "",
            "Health" : 80,
            "Damage" : 0,
            "Magic Damage" : 8,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        4 : { #Air
            "Name" : ("Air"),
            "Description" : "",
            "Health" : 60,
            "Damage" : 0,
            "Magic Damage" : 5,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        5 : { #Lightning
            "Name" : ("Lightning"),
            "Description" : "",
            "Health" : 53,
            "Damage" : 0,
            "Magic Damage" : 10,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
        6 : { #Light
            "Name" : ("Light"),
            "Description" : "",
            "Health" : 45,
            "Damage" : 0,
            "Magic Damage" : 0,
            "Magic_Resistace" : 0,
            "Armor" : 0
        },
    },
    "Wolves" : {
        1 : { #Wolf
            "Name" : ("Wolf"),
            "Description" : "",
            "Health" : 30,
            "Damage" : 13,
            "Magic Damage" : 0,
            "Magic_Resistace" : 0,
            "Armor" : 0,
            "Location Type" : ("Valley", "Mountain", "Den"),
            "Frequency" : 1,
            "Level Requirement" : 0,
        },
        2 : { #Dire Wolf
            "Name" : ("Dire Wolf"),
            "Description" : "",
            "Health" : 122,
            "Damage" : 31,
            "Magic Damage" : 0,
            "Magic_Resistace" : 0,
            "Armor" : 0,
            "Location Type" : ("Mountain"),
            "Frequency" : 5,
            "Level Requirement" : 10,
        },
    },
    "Jackel" : {
        "1" : { #Jackel
            "Name" : ("Jackel"),
            "Description" : "",
            "Health" : 70,
            "Damage" : 23,
            "Magic Damage" : 0,
            "Magic_Resistace" : 0,
            "Armor" : 0,
            "Location Type" : ("Forest", "Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 25,
        },
    },
    "Dahrk Hound" : {
        "1" : {
            "Name" : ("Dahrk Hound"),
            "Description" : "",
            "Health" : 94,
            "Damage" : 3,
            "Magic Damage" : 0,
            "Magic_Resistace" : 0,
            "Armor" : 0,
            "Location Type" : ("Tundra", "Mountain"),
            "Frequency" : 1,
            "Level Requirement" : 0,
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
        2 : { #Merfolk
            "Merfolk" : {
                1 : { #Merfolk
                    1 : { #Female (Mermaid)
                        "Name" : ("Mermaid"),
                        "Description" : "",
                        "Health" : 70,
                        "Damage" : 25,
                        "Magic Damage" : 0,
                        "Magic_Resistace" : 0,
                        "Armor" : 0 
                    },
                    2 : { #Famale (Siren)
                        "Name" : ("Siren"),
                        "Description" : "",
                        "Health" : 70,
                        "Damage" : 25,
                        "Magic Damage" : 0,
                        "Magic_Resistace" : 0,
                        "Armor" : 0 
                    }
                },
                2 : { #Male (Merman)
                    "Name" : ("Merman"),
                    "Description" : "",
                    "Health" : 70,
                    "Damage" : 25,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 0
                },
                3 : { #Merfolk Gaurd
                    "Name" : ("Merfolk Gaurd"),
                    "Description" : "",
                    "Health" : 0,
                    "Damage" : 0,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 0 
                }
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
            3 : { #Orge
                "Name" : ("Orge"),
                "Description" : "",
                "Health" : 60,
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
            5 : { #Goblin
                "Name" : ("Goblin"),
                "Description" : "",
                "Health" : 10,
                "Damage" : 5,
                "Magic Damage" : 0,
                "Magic_Resistace" : 0,
                "Armor" : 0
            },
            6 : { #Kobold
                "Kobold" : {
                    1 : { #Kobolds
                        "Name" : ("Kobolds"),
                        "Description" : "",
                        "Health" : 10,
                        "Damage" : 4,
                        "Magic Damage" : 1,
                        "Magic_Resistace" : 0,
                        "Armor" : 0
                    },
                    2 : { #Kobold Knight
                        "Name" : ("Kobold Knight"),
                        "Description" : "",
                        "Health" : 40,
                        "Damage" : 10,
                        "Magic Damage" : 5,
                        "Magic_Resistace" : 0,
                        "Armor" : 0
                    }
                },
            },
        },
    },#<--End of Land Creatures/Monsters
}#END