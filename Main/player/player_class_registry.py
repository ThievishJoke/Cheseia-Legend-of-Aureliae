class PlayerClass:
    def __init__(self, name, bonus_dmg, bonus_mana, bonus_magic_dmg, bonus_health, bonus_magic_resist, bonus_armor,
                 passive_abilities: list, bonus_speed):
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.bonus_mana = bonus_mana
        self.bonus_magic_dmg = bonus_magic_dmg
        self.bonus_health = bonus_health
        self.bonus_magic_resist = bonus_magic_resist
        self.bonus_armor = bonus_armor
        self.passive_abilities = passive_abilities
        self.bonus_speed = bonus_speed

# Define the registry for all player classes
class_registry = {
    "Fighter": PlayerClass(
        name="Fighter", 
        bonus_dmg=10, 
        bonus_mana=30, 
        bonus_magic_dmg=5, 
        bonus_health=50, 
        bonus_magic_resist=5, 
        bonus_armor=20,
        passive_abilities=[],
        bonus_speed=3
    ),
    "Mage": PlayerClass(
        name="Mage", 
        bonus_dmg=5, 
        bonus_mana=50, 
        bonus_magic_dmg=20, 
        bonus_health=30, 
        bonus_magic_resist=10, 
        bonus_armor=5,
        passive_abilities=[],
        bonus_speed=2
    ),
    "Bard": PlayerClass(
        name="Bard", 
        bonus_dmg=7, 
        bonus_mana=40, 
        bonus_magic_dmg=10, 
        bonus_health=40, 
        bonus_magic_resist=5, 
        bonus_armor=10,
        passive_abilities=[],
        bonus_speed=4
    ),
    "Thief": PlayerClass(
        name="Thief",
        bonus_dmg=15,
        bonus_mana=10,
        bonus_magic_dmg=2,
        bonus_health=60,
        bonus_magic_resist=5,
        bonus_armor=15,
        passive_abilities=[],
        bonus_speed=3
    ),
    "Paladin": PlayerClass(
        name="Paladin",
        bonus_dmg=10,
        bonus_mana=25,
        bonus_magic_dmg=6,
        bonus_health=50,
        bonus_magic_resist=10,
        bonus_armor=12,
        passive_abilities=[],
        bonus_speed=2
    ),
    "Mage": PlayerClass(
        name="Mage",
        bonus_dmg=3,
        bonus_mana=70,
        bonus_magic_dmg=20,
        bonus_health=30,
        bonus_magic_resist=8,
        bonus_armor=3,
        passive_abilities=[],
        bonus_speed=4
    ),
    "Healer": PlayerClass(
        name="Healer",
        bonus_dmg=2,
        bonus_mana=60,
        bonus_magic_dmg=12,
        bonus_health=40,
        bonus_magic_resist=12,
        bonus_armor=4,
        passive_abilities=[],
        bonus_speed=4
    ),
    "Ranger": PlayerClass(
        name="Ranger",
        bonus_dmg=12,
        bonus_mana=20,
        bonus_magic_dmg=5,
        bonus_health=45,
        bonus_magic_resist=6,
        bonus_armor=8,
        passive_abilities=[],
        bonus_speed=6
    )
}

def get_player_class(class_name: str) -> PlayerClass:
    """Returns the PlayerClass object based on the input class name"""
    return class_registry.get(class_name)