from material.materials import MaterialRegistry  # Import registry to fetch materials
from rarity.rarities import Rarity  # Import rarities
from effects.perks import Perk  # Import perks

# Base class for wearable items
class Wearable:
    def __init__(self, name, material, physical_resistance, magical_resistance, weight, mana_bonus,
                 skill_requirement, perks, rarity, craftable):
        self.name = name
        self.material = material
        self.physical_resistance = physical_resistance
        self.magical_resistance = magical_resistance
        self.weight = weight
        self.mana_bonus = mana_bonus
        self.skill_requirement = skill_requirement
        self.perks = perks  # List of Perk enums or strings
        self.rarity = rarity
        self.craftable = craftable

    def __str__(self):
        return (f"{self.name} ({self.rarity.name})\n"
                f"Material: {self.material.name}, Armor: {self.physical_resistance}/{self.magical_resistance}, "
                f"Weight: {self.weight}, Mana Bonus: {self.mana_bonus}, "
                f"Skill Req: {self.skill_requirement}, Craftable: {self.craftable}\n"
                f"Perks: {', '.join(perk.name for perk in self.perks)}")

# Armor subclass with fragment slots
class Armor(Wearable):
    def __init__(self, name, material, physical_resistance, magical_resistance, weight, mana_bonus,
                 skill_requirement, perks, rarity, craftable, slots):
        super().__init__(name, material, physical_resistance, magical_resistance, weight, mana_bonus,
                         skill_requirement, perks, rarity, craftable)
        self.slots = slots

    def __str__(self):
        base = super().__str__()
        return f"{base}, Fragment Slots: {self.slots}"

# Example Armor using Iron Ore
def create_armor_example():
    # Fetch material from registry
    refined_iron = MaterialRegistry.get_material("Refined Iron")

    if not refined_iron:
        raise ValueError("Material 'Iron Ore' is not registered!")

    # Create an armor piece using the fetched material
    iron_armor = Armor(
        name="Iron Chestplate",
        material=refined_iron,  # Use the material retrieved from registry
        physical_resistance=50,
        magical_resistance=20,
        weight=30,
        mana_bonus=0,
        skill_requirement=10,
        perks=[],  # No perks for now
        rarity=Rarity.get_rarity_by_name("common"),  # Dynamically fetch rarity by name
        craftable=True,
        slots=2
    )

    print(iron_armor)


# Run example
#if __name__ == "__main__":
#    create_armor_example()
create_armor_example()
