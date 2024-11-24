from material.materials import Material
from rarity.rarities import Rarity
from effects.perks import Perk

# Base class for wearable items
class Wearable:
    def __init__(self, name, material, physical_armor, magical_armor, weight, mana_bonus,
                 skill_requirement, perks, rarity, craftable):
        self.name = name
        self.material = material
        self.physical_armor = physical_armor
        self.magical_armor = magical_armor
        self.weight = weight
        self.mana_bonus = mana_bonus
        self.skill_requirement = skill_requirement
        self.perks = perks  # List of Perk enums or strings
        self.rarity = rarity
        self.craftable = craftable

    def __str__(self):
        return (f"{self.name} ({self.rarity.name})\n"
                f"Material: {self.material.name}, Armor: {self.physical_armor}/{self.magical_armor}, "
                f"Weight: {self.weight}, Mana Bonus: {self.mana_bonus}, "
                f"Skill Req: {self.skill_requirement}, Craftable: {self.craftable}\n"
                f"Perks: {', '.join(perk.name for perk in self.perks)}")

# Armor subclass with fragment slots
class Armor(Wearable):
    def __init__(self, name, material, physical_armor, magical_armor, weight, mana_bonus,
                 skill_requirement, perks, rarity, craftable, slots):
        super().__init__(name, material, physical_armor, magical_armor, weight, mana_bonus,
                         skill_requirement, perks, rarity, craftable)
        self.slots = slots

    def __str__(self):
        base = super().__str__()
        return f"{base}, Fragment Slots: {self.slots}"

# Jewelry subclass with fragment slots
class Jewelry(Wearable):
    def __init__(self, name, material, physical_armor, magical_armor, weight, mana_bonus,
                 skill_requirement, perks, rarity, craftable, slots):
        super().__init__(name, material, physical_armor, magical_armor, weight, mana_bonus,
                         skill_requirement, perks, rarity, craftable)
        self.slots = slots

    def __str__(self):
        base = super().__str__()
        return f"{base}, Fragment Slots: {self.slots}"

# Arm Bands and Belts with material bonuses
class MaterialBonusWearable(Wearable):
    def __init__(self, name, material, physical_armor, magical_armor, weight, mana_bonus,
                 skill_requirement, perks, rarity, craftable):
        super().__init__(name, material, physical_armor, magical_armor, weight, mana_bonus,
                         skill_requirement, perks, rarity, craftable)
        self.material_bonus = self.calculate_material_bonus()

    def calculate_material_bonus(self):
        # Example bonuses based on material; replace with logic as needed
        material_bonuses = {
            Material.IRON: {"strength": 5},
            Material.STEEL: {"strength": 10},
            Material.GOLD: {"luck": 15},
            Material.MITHRIL: {"magic": 20},
        }
        return material_bonuses.get(self.material, {})

    def __str__(self):
        base = super().__str__()
        return f"{base}, Material Bonus: {self.material_bonus}"

# Example usage
if __name__ == "__main__":
    helmet = Armor(
        name="Iron Helmet",
        material=Material.IRON,
        physical_armor=10,
        magical_armor=2,
        weight=5,
        mana_bonus=0,
        skill_requirement=5,
        perks=[Perk.FIRE_RESISTANCE],
        rarity=Rarity.COMMON,
        craftable=True,
        slots=1
    )
#    ring = Jewelry(
#        name="Gold Ring",
#        material=Material.GOLD,
#        physical_armor=1,
#        magical_armor=5,
#        weight=1,
#        mana_bonus=10,
#        skill_requirement=3,
#        perks=[Perk.MANA_REGEN],
#        rarity=Rarity.RARE,
#        craftable=False,
#        slots=2
#    )
#    belt = MaterialBonusWearable(
#        name="Steel Belt",
#        material=Material.STEEL,
#        physical_armor=5,
#        magical_armor=3,
#        weight=3,
#        mana_bonus=0,
#        skill_requirement=4,
#        perks=[Perk.HEALTH_REGEN],
#        rarity=Rarity.UNCOMMON,
#        craftable=True
#    )
#
    print(helmet)
#    print(ring)
#    print(belt)
