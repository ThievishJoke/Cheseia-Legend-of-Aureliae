from material.materials import MaterialRegistry  # Import Material Registry
from rarity.rarities import Rarity  # Import Rarity Registry
from effects.perks import Perk  # Import Perk for perks functionality

class Weapon:
    def __init__(self, name, material, weapon_range, weapon_type, affinity, damage_type,
                 is_two_handed: bool, damage_amount, weight, mana_bonus,
                 skill_requirement, perks, rarity_name, craftable, register=True,
                 crit_bonus=0.0, crit_mult_bonus=0.0):
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

        # --- Weapon-specific crit bonuses ---
        self.crit_bonus = crit_bonus            # Additional crit chance (e.g., 0.05 = +5%)
        self.crit_mult_bonus = crit_mult_bonus  # Additional crit multiplier (e.g., 0.25 = +0.25×)

        if register:
            WeaponRegistry.register_weapon(self)

    def __str__(self):
        perks_str = ', '.join(perk.name for perk in self.perks) if self.perks else "None"
        return (f"{self.name} ({self.rarity.name})\n"
                f"Material: {self.material.name if self.material else 'None'}, Type: {self.weapon_type}, Affinity: {self.affinity}, "
                f"Damage Type: {self.damage_type}\n"
                f"Range: {self.range}, Weight: {self.weight}, Mana Bonus: {self.mana_bonus}\n"
                f"Skill Requirement: {self.skill_requirement}, Craftable: {self.craftable}\n"
                f"Critical Bonus: {self.crit_bonus}, Critical Multiplier: {self.crit_mult_bonus}\n"
                f"Perks: {perks_str}")
    
    def to_dict(self):
        return {
            "name": self.name,
            "material": self.material.name if self.material else None,
            "weapon_range": self.range,
            "weapon_type": self.weapon_type,
            "affinity": self.affinity,
            "damage_type": self.damage_type,
            "is_two_handed": self.is_two_handed,
            "damage_amount": self.damage_amount,
            "weight": self.weight,
            "mana_bonus": self.mana_bonus,
            "skill_requirement": self.skill_requirement,
            "perks": [perk.name for perk in self.perks] if self.perks else [],
            "rarity_name": self.rarity.name if self.rarity else None,
            "craftable": self.craftable,
            "crit_bonus": self.crit_bonus,
            "crit_mult_bonus": self.crit_mult_bonus
        }

    @classmethod
    def from_dict(cls, data):
        # Get material object if material name exists
        material = MaterialRegistry.get_material(data["material"]) if data.get("material") else None
        # Get list of perk objects if perks exist
        perks = [Perk.get_perk_by_name(p) for p in data.get("perks", [])] if data.get("perks") else []
        rarity_name = data.get("rarity_name", "common")

        return cls(
            name=data["name"],
            material=material,
            weapon_range=data["weapon_range"],
            weapon_type=data["weapon_type"],
            affinity=data["affinity"],
            damage_type=data["damage_type"],
            is_two_handed=data["is_two_handed"],
            damage_amount=data["damage_amount"],
            weight=data["weight"],
            mana_bonus=data["mana_bonus"],
            skill_requirement=data["skill_requirement"],
            perks=perks,
            rarity_name=rarity_name,
            craftable=data["craftable"],
            register=False,
            crit_bonus=["crit_bonus"],
            crit_mult_bonus=["crit_mult_bonus"]
        )
    
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
        return list(cls._weapons.values())

# Example weapon
iron_long_sword = Weapon(
    name="Iron Long Sword",
    material=MaterialRegistry.get_material("Refined Iron"),
    weapon_range=1,
    weapon_type="Sword",
    affinity=None,
    damage_type="Slashing",
    is_two_handed=False,
    damage_amount=10,
    weight=10,
    mana_bonus=0,
    skill_requirement=5,
    perks=[],
    rarity_name="common",
    craftable=True,
    crit_bonus=0.01,
    crit_mult_bonus=1.5
)

print("Successfully Imported Weapons")
