
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

# Example rarity name
#rarity_name = "legendary"
#rarity_index = index_rarity_by_name(rarity_name)

# Calculate bonus values for the given rarity
#dmg_bonus, legendary_bonus, legendary_bonus_mult = calculate_bonus(rarity_index)

# Example Use
# Defines the weapon dictionary with bonus values
#weapon_xp = 0
#weapon_xp_nxt_lvl = 10
#material = {"wood": "Wood"}
#wood_stick = {
#    "Name": "Wood Stick",
#    "Dmg": 5 + dmg_bonus,  # Include the damage bonus
#    "Material Type": material["wood"],
#    "Weapon Xp": weapon_xp,
#    "Weapon Lvl": weapon_xp_nxt_lvl,
#    "Weapon Next Lvl": int(150 * (1.35 * 1)),
#    "Rarity": RARITIES[rarity_index],
#    "Dmg Bonus": dmg_bonus,  # Scaling Dmg based on rarity
#    "Legendary Bonus": legendary_bonus,  # Additive Dmg based on if its legendary or higher
#    "Legendary Multiplier Bonus": legendary_bonus_mult, # Doubles the Dmg if Legendary rarity or higher
#    "Tooltip": "A pretty pathetic wood stick, 'should probably find something better'",
#    "Single Handed": 1,
#    "Two Handed": 0,
#    "Is Enchanted": 0,
#    "Enhanced Count": 0,
#    "Enhancements capped": 1,
#    "Max Enhancements": 10
#}
#
#print(wood_stick)