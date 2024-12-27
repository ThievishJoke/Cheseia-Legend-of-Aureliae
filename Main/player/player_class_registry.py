class PlayerClass:
    def __init__(self, name, bonus_dmg, bonus_mana, bonus_magic_dmg, bonus_health, bonus_magic_resist, bonus_armor,
                 passive_abilities: list, bonus_movement):
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.bonus_mana = bonus_mana
        self.bonus_magic_dmg = bonus_magic_dmg
        self.bonus_health = bonus_health
        self.bonus_magic_resist = bonus_magic_resist
        self.bonus_armor = bonus_armor
        self.passive_abilities = passive_abilities
        self.bonus_movement = bonus_movement

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
        passive_abilities=["battle_hardened", "strong"],
        bonus_movement=3
    ),
    "Mage": PlayerClass(
        name="Mage", 
        bonus_dmg=5, 
        bonus_mana=50, 
        bonus_magic_dmg=20, 
        bonus_health=30, 
        bonus_magic_resist=10, 
        bonus_armor=5,
        passive_abilities=["mana_regen", "arcane_mastery"],
        bonus_movement=2
    ),
    "Bard": PlayerClass(
        name="Bard", 
        bonus_dmg=7, 
        bonus_mana=40, 
        bonus_magic_dmg=10, 
        bonus_health=40, 
        bonus_magic_resist=5, 
        bonus_armor=10,
        passive_abilities=["musical_inspiration", "song_of_healing"],
        bonus_movement=4
    ),
    # Add more classes as needed
}

def get_player_class(class_name: str) -> PlayerClass:
    """Returns the PlayerClass object based on the input class name"""
    return class_registry.get(class_name)