from language.localization import translate

class PlayerClass:
    def __init__(self, 
                 id: str, 
                 name: str, 
                 name_key: str, 
                 description_key: str, 
                 bonus_dmg: int, 
                 bonus_mana: int, 
                 bonus_magic_dmg: int, 
                 bonus_health: int, 
                 bonus_magic_resist: int, 
                 bonus_armor: int,
                 passive_abilities: list, 
                 bonus_speed: int):
        self.id = id.lower()
        self.name = name
        self.name_key = name_key
        self.description_key = description_key
        self.bonus_dmg = bonus_dmg
        self.bonus_mana = bonus_mana
        self.bonus_magic_dmg = bonus_magic_dmg
        self.bonus_health = bonus_health
        self.bonus_magic_resist = bonus_magic_resist
        self.bonus_armor = bonus_armor
        self.passive_abilities = passive_abilities
        self.bonus_speed = bonus_speed
        
    def display_name(self) -> str:
        """Return the translated name."""
        return translate(self.name_key)

    def display_description(self) -> str:
        """Return the translated description."""
        return translate(self.description_key)

print("Successfully Imported Classes")