class Species:
    def __init__(self, name, base_health, base_max_health, base_mana, base_max_mana, base_magic_dmg, base_magic_resist,
                 base_armor, passive_abilities: list, base_dmg, base_movement):
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
        self.base_movement = base_movement  # Movement speed

print("Successfully Imported Species")