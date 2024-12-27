# Rarities definition
RARITIES = [
    "very common",
    "common",
    "uncommon",
    "rare",
    "very rare",
    "legendary",
    "mythical",
    "unique"
]

# Function to index rarity by name
def index_rarity_by_name(rarity_name):
    """
    Converts a rarity name to its index in the RARITIES list.
    Defaults to 0 (very common) if the name is not found.
    """
    if rarity_name in RARITIES:
        return RARITIES.index(rarity_name)
    else:
        return 0  # Default to "very common" if not found

# Function to calculate bonus values based on rarity
def calculate_bonus(rarity_index):
    """
    Calculates damage and legendary bonuses based on rarity index.
    """
    dmg_bonus = 0
    legendary_bonus = 1
    legendary_bonus_mult = 1

    if rarity_index >= 6:  # Legendary and above
        legendary_bonus = 5 + 5 * ((rarity_index - 6) // 2)
        legendary_bonus_mult = 2
    else:
        bonus_values = [0, 10, 15, 20, 40, 60]  # Bonuses for rarities 0-5
        if rarity_index <= len(bonus_values) - 1:
            dmg_bonus = bonus_values[rarity_index]
        else:
            dmg_bonus = 100 * (2 ** (rarity_index - 6))  # Scaling bonus for rarities higher than 7

    return dmg_bonus, legendary_bonus, legendary_bonus_mult


# Rarity class for integration
class Rarity:
    def __init__(self, name):
        self.name = name
        self.index = index_rarity_by_name(name)
        self.dmg_bonus, self.legendary_bonus, self.legendary_bonus_mult = calculate_bonus(self.index)

    def __str__(self):
        return (f"Rarity: {self.name} (Index: {self.index}), "
                f"Damage Bonus: {self.dmg_bonus}, Legendary Bonus: {self.legendary_bonus}, "
                f"Multiplier: {self.legendary_bonus_mult}")
    
    @classmethod
    def get_rarity_by_name(cls, rarity_name):
        """
        Class method to get a Rarity object by its name.
        """
        return cls(rarity_name)
    
    @classmethod
    def get_rarity_by_index(cls, rarity_index):
        """
        Class method to get a Rarity object by its index.
        """
        if 0 <= rarity_index < len(RARITIES):
            return cls(RARITIES[rarity_index])
        else:
            return cls("very common")  # Default to "very common" if index is out of range

print("Successfully Imported Rarities")