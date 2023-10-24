

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
    if rarity_name in RARITIES:
        return RARITIES.index(rarity_name)
    else:
        return 0  # Default to very common if the name is not found

# Function to calculate bonus values
def calculate_bonus(rarity):
    dmg_bonus = 0
    legendary_bonus = 1
    legendary_bonus_mult = 1

    if rarity >= 6:  # Legendary and above
        legendary_bonus = 5 + 5 * ((rarity - 6) // 2)
        legendary_bonus_mult = 2
    else:
        if rarity >= 0:
            bonus_values = [0, 10, 15, 20, 40, 60]
            if rarity <= len(bonus_values) - 1:
                dmg_bonus = bonus_values[rarity]
            else:
                dmg_bonus = 100 * (2 ** (rarity - 6))  # Scaling bonus for rarities higher than 7

    return dmg_bonus, legendary_bonus, legendary_bonus_mult