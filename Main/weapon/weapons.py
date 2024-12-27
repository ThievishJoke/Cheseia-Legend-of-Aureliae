from material.materials import MaterialRegistry  # Import Material Registry
from rarity.rarities import Rarity  # Import Rarity Registry
from effects.perks import Perk  # Import Perk for perks functionality

class Weapon:
    def __init__(self, name, material, weapon_range, weapon_type, affinity, damage_type,
                 is_two_handed:bool, damage_amount, weight, mana_bonus,
                 skill_requirement, perks, rarity_name, craftable):
        self.name = name
        self.material = material  # Material object from MaterialRegistry
        self.range = weapon_range  # Numeric range value
        self.weapon_type = weapon_type  # e.g., Sword, Bow, Staff, etc.
        self.affinity = affinity  # Affinity (if any, e.g., Fire, Water)
        self.damage_type = damage_type  # Damage type: Piercing, Slashing, Bludgeoning, Magic (+ affinity if applicable)
        self.is_two_handed = is_two_handed
        self.damage_amount = damage_amount
        self.weight = weight  # Weapon weight
        self.mana_bonus = mana_bonus  # Bonus to mana
        self.skill_requirement = skill_requirement  # Required skill level to use the weapon
        self.perks = perks  # List of perks associated with the weapon
        self.rarity = Rarity.get_rarity_by_name(rarity_name)  # Rarity object from Rarity Registry
        self.craftable = craftable  # Boolean indicating if the weapon can be crafted

        WeaponRegistry.register_weapon(self)

    def __str__(self):
        perks_str = ', '.join(perk.name for perk in self.perks) if self.perks else "None"
        return (f"{self.name} ({self.rarity.name})\n"
                f"Material: {self.material.name}, Type: {self.weapon_type}, Affinity: {self.affinity}, "
                f"Damage Type: {self.damage_type}\n"
                f"Range: {self.range}, Weight: {self.weight}, Mana Bonus: {self.mana_bonus}\n"
                f"Skill Requirement: {self.skill_requirement}, Craftable: {self.craftable}\n"
                f"Perks: {perks_str}")

class WeaponRegistry:
    _weapons = {}

    @classmethod
    def register_weapon(cls, weapon):
        if not isinstance(weapon, Weapon):
            raise TypeError("Only Weapon instances can be registered.")
        if weapon.name in cls._weapons:
            raise ValueError(f"A weapon with the name '{weapon.name}' is already registered.")
        cls._weapons[weapon.name] = weapon

    @classmethod
    def get_weapon_by_name(cls, name):
        return cls._weapons.get(name, None)

    @classmethod
    def list_all_weapons(cls):
        return list(cls._registry.values())

iron_long_sword = Weapon(

    name="Iron Long Sword",
    material=MaterialRegistry.get_material("Refined Iron"),
    weapon_range=1,
    weapon_type="Sword",
    affinity=None,
    damage_type="Slashing",
    is_two_handed=False,
    damage_amount=25,
    weight=10,
    mana_bonus=0,
    skill_requirement=5,
    perks="",
    rarity_name="common",
    craftable=True

)

print("Successfully Imported Weapons")