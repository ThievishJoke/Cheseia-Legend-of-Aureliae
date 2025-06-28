class Species:
    def __init__(self, name, base_health, base_max_health, base_mana, base_max_mana, base_magic_dmg, base_magic_resist,
                 base_armor, passive_abilities: list, base_dmg, base_speed):
        self.name = name
        self.base_health = base_health  # Current health
        self.base_max_health = base_max_health  # Maximum health
        self.base_mana = base_mana  # Current mana
        self.base_max_mana = base_max_mana  # Maximum mana
        self.base_magic_dmg = base_magic_dmg  # Magic damage output
        self.base_magic_resist = base_magic_resist  # Magic resistance
        self.base_armor = base_armor  # Physical armor
        self.passive_abilities = passive_abilities  # List of passive abilities
        self.base_dmg = base_dmg  # Base physical damage
        self.base_speed = base_speed  # Movement speed

    def to_dict(self):
        return {
            "name": self.name,
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