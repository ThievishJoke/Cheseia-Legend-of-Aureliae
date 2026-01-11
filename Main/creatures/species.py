from language.localization import translate
class Species:
    def __init__(self, 
                 id: str,
                 name: str, 
                 name_key: str, 
                 description_key: str, 
                 base_health: int, 
                 base_max_health: int, 
                 base_mana: int,
                 base_max_mana: int, 
                 base_magic_dmg: int, 
                 base_magic_resist: int, 
                 base_armor: int, 
                 passive_abilities: list,
                 base_dmg: int, 
                 base_speed: int):
        self.id = id.lower()
        self.name = name
        self.name_key = name_key
        self.description_key = description_key
        self.base_health = base_health
        self.base_max_health = base_max_health
        self.base_mana = base_mana
        self.base_max_mana = base_max_mana
        self.base_magic_dmg = base_magic_dmg
        self.base_magic_resist = base_magic_resist
        self.base_armor = base_armor
        self.passive_abilities = passive_abilities
        self.base_dmg = base_dmg
        self.base_speed = base_speed

    def display_name(self) -> str:
        """Return the translated name."""
        return translate(self.name_key)

    def display_description(self) -> str:
        """Return the translated description."""
        return translate(self.description_key)

    def to_dict(self):
        return {
            "name": self.name,
            "name_key": self.name_key,
            "description_key": self.description_key,
            "base_health": self.base_health,
            "base_max_health": self.base_max_health,
            "base_mana": self.base_mana,
            "base_max_mana": self.base_max_mana,
            "base_magic_dmg": self.base_magic_dmg,
            "base_magic_resist": self.base_magic_resist,
            "base_armor": self.base_armor,
            "passive_abilities": self.passive_abilities,
            "base_dmg": self.base_dmg,
            "base_speed": self.base_speed,
        }

    @classmethod
    def from_dict(cls, data):
        print(f"[DEBUG] from_dict called with: {type(data)} -> {data}")
        
        return cls(
            name=data["name"],
            base_health=data["base_health"],
            base_max_health=data["base_max_health"],
            base_mana=data["base_mana"],
            base_max_mana=data["base_max_mana"],
            base_magic_dmg=data["base_magic_dmg"],
            base_magic_resist=data["base_magic_resist"],
            base_armor=data["base_armor"],
            passive_abilities=data["passive_abilities"],
            base_dmg=data["base_dmg"],
            base_speed=data["base_speed"]
        )

print("Successfully Imported Species")