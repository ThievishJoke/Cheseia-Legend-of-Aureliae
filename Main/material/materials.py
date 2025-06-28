from rarity.rarities import Rarity

class Material:
    def __init__(self, name):
        self.name = name

class RawMaterial:
    def __init__(self, material, rarity_name, affinity, mining_lvl=1, bonus_percent=0, description=None):
        self.material = material
        self.name = material.name
        self.rarity = Rarity.get_rarity_by_name(rarity_name)  # Fetch Rarity object by name
        self.affinity = affinity
        self.mining_lvl = mining_lvl
        self.bonus_percent = bonus_percent
        self.description = description

        # Register this material only if it's the first one of its kind
        if not MaterialRegistry.is_material_registered(self.name):
            MaterialRegistry.register_material(self.material)

    def __str__(self):
        return (f"{self.name} ({self.rarity.name})\n"
                f"Affinity: {self.affinity}, Mining Level: {self.mining_lvl}, "
                f"Bonus: {self.bonus_percent}%)\nDescription: {self.description}")

class RefinedMaterial:
    def __init__(self, material, rarity_name, affinity, refining_level=1, bonus_percent=0, description=None):
        self.material = material
        self.name = material.name
        self.rarity = Rarity.get_rarity_by_name(rarity_name)  # Fetch Rarity object by name
        self.affinity = affinity
        self.refining_level = refining_level  # Added refining_level attribute
        self.bonus_percent = bonus_percent
        self.description = description

        # Register the refined material, ensuring it hasn't been registered already
        if not MaterialRegistry.is_material_registered(self.name):
            MaterialRegistry.register_material(self.material)

    def __str__(self):
        return (f"{self.name} ({self.rarity.name})\n"
                f"Affinity: {self.affinity}, Refining Level: {self.refining_level}, "
                f"Bonus: {self.bonus_percent}%)\nDescription: {self.description}")

# MaterialRegistry
class MaterialRegistry:
    _materials = {}

    @classmethod
    def register_material(cls, material):
        if material.name in cls._materials:
            raise ValueError(f"Material '{material.name}' is already registered!")
        cls._materials[material.name] = material

    @classmethod
    def get_material(cls, name):
        return cls._materials.get(name)

    @classmethod
    def is_material_registered(cls, name):
        return name in cls._materials



# ------------------------------------------------------


# Raw Metals
iron_ore = RawMaterial(
    #name="Iron Ore",
    material=Material("Iron Ore"),
    rarity_name="common",  # Rarity is provided as a name
    affinity="None",
    mining_lvl=1,
    bonus_percent=0,
    description="A common ore used as a cornerstone in metallurgy and construction."
)

blazeite_ore = RawMaterial(
    #name="Blazeite Ore",
    material=Material("Blazeite Ore"),
    rarity_name="common",
    affinity="Fire",
    mining_lvl=1,
    bonus_percent=0,
    description="A fiery and volatile ore that burns with intense heat and can be used to imbue weapons with fire elemental power."
)

seashine_ore = RawMaterial(
    #name="Seashine Ore",
    material=Material("Seashine Ore"),
    rarity_name="common",
    affinity="Aqua",
    mining_lvl=1,
    bonus_percent=0,
    description="A luminescent ore that can be found in shallow waters, often used to make underwater lights."
)

quartzite_ore = RawMaterial(
    #name="Quartzite Ore",
    material=Material("Quartzite Ore"),
    rarity_name="common",
    affinity="Earth",
    mining_lvl=1,
    bonus_percent=0,
    description="A hard, translucent ore found in underground mines, used to create powerful, long-lasting batteries."
)

fae_ore = RawMaterial(
    #name="Fae Ore",
    material=Material("Fae Ore"),
    rarity_name="uncommon",  # Adjusted rarity for variety
    affinity="Natural",
    mining_lvl=1,
    bonus_percent=0,
    description="A glowing green ore found in enchanted glades, rumored to transport users to other dimensions."
)

stormite_ore = RawMaterial(
    #name="Stormite Ore",
    material=Material("Stormite Ore"),
    rarity_name="rare",  # Adjusted rarity
    affinity="Air",
    mining_lvl=2,  # Higher mining level
    bonus_percent=10,
    description="A dark, stormy ore found during thunderstorms, used to create items generating powerful gusts of wind."
)

thunderstone_ore = RawMaterial(
    #name="Thunderstone Ore",
    material=Material("Thunderstone Ore"),
    rarity_name="rare",
    affinity="Lightning",
    mining_lvl=2,
    bonus_percent=15,
    description="An ore that generates lightning bolts when struck, used to create items that grant control over electricity."
)

radiant_ore = RawMaterial(
    #name="Radiant Ore",
    material=Material("Radiant Ore"),
    rarity_name="very rare",  # Rare for luminous ores
    affinity="Light",
    mining_lvl=3,
    bonus_percent=20,
    description="A glittering ore found in bright light, used to imbue weapons with the power of the sun."
)

starsteel_ore = RawMaterial(
    #name="Starsteel Ore",
    material=Material("Starsteel Ore"),
    rarity_name="legendary",  # Adjusted for rarity significance
    affinity="Light",
    mining_lvl=4,
    bonus_percent=50,
    description="A rare ore said to have fallen from the heavens, used to forge weapons with incredible precision."
)

ebonite_ore = RawMaterial(
    #name="Ebonite Ore",
    material=Material("Ebonite Ore"),
    rarity_name="uncommon",
    affinity="Dark",
    mining_lvl=1,
    bonus_percent=0,
    description="A jet-black ore used to create weapons that absorb the life force of enemies."
)

umbrite_ore = RawMaterial(
    #name="Umbrite Ore",
    material=Material("Umbrite Ore"),
    rarity_name="uncommon",
    affinity="Eclipse",
    mining_lvl=1,
    bonus_percent=0,
    description="An ore found during eclipses, used to craft items harnessing the power of both darkness and light."
)

celestite_ore = RawMaterial(
    #name="Celestite Ore",
    material=Material("Celestite Ore"),
    rarity_name="uncommon",
    affinity="Lunar",
    mining_lvl=1,
    bonus_percent=0,
    description="A pale blue ore from the stars, used to create items granting celestial power."
)

selene_ore = RawMaterial(
    #name="Selene Ore",
    material=Material("Selene Ore"),
    rarity_name="common",
    affinity="Lunar",
    mining_lvl=1,
    bonus_percent=0,
    description="A rare ore found during lunar phases, used to craft items with tidal influence."
)

starfall_ore = RawMaterial(
    #name="Starfall Ore",
    material=Material("Starfall Ore"),
    rarity_name="common",
    affinity="Lunar",
    mining_lvl=1,
    bonus_percent=0,
    description="An ore falling during meteor showers, used to create items harnessing the power of the stars."
)

necrotite_ore = RawMaterial(
    #name="Necrotite Ore",
    material=Material("Necrotite Ore"),
    rarity_name="common",
    affinity="Soul",
    mining_lvl=1,
    bonus_percent=0,
    description="A powerful ore found near death, used to craft items granting control over undead creatures."
)

anima_ore = RawMaterial(
    #name="Anima Ore",
    material=Material("Anima Ore"),
    rarity_name="common",
    affinity="Soul",
    mining_lvl=1,
    bonus_percent=0,
    description="A glowing ore found in places of great spiritual energy, granting power over the soul."
)

spirit_ore = RawMaterial(
    #name="Spirit Ore",
    material=Material("Spirit Ore"),
    rarity_name="common",
    affinity="Soul",
    mining_lvl=1,
    bonus_percent=0,
    description="An ethereal ore from places of emotional significance, harnessing the power of the soul."
)

hematite_ore = RawMaterial(
    #name="Hematite Ore",
    material=Material("Hematite Ore"),
    rarity_name="common",
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="A shimmering ore generating a red liquid when struck, used to create items granting immense strength."
)

crimsonite_ore = RawMaterial(
    #name="Crimsonite Ore",
    material=Material("Crimsonite Ore"),
    rarity_name="common",
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="A red ore found in the presence of blood, granting power over bloodshed."
)

vitae_ore = RawMaterial(
    #name="Vitae Ore",
    material=Material("Vitae Ore"),
    rarity_name="common",
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="A rare ore containing the essence of life, used to craft items for healing and resurrection."
)

carnelian_ore = RawMaterial(
    #name="Carnelian Ore",
    material=Material("Carnelian Ore"),
    rarity_name="common",
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="A dark red ore found near bloodshed, used to craft items granting speed and agility."
)
# ------------------------------------------------------
# Raw Naturals
#ignitionrot = RawMaterial(
#    material=Material("Ignitionrot"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Fire",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#ocean_breath = RawMaterial(
#    material=Material("Ocean's Breath"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Aqua",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#stonebark_pine = RawMaterial(
#    material=Material("Stonebark Pine"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Earth",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#gaea_embrace = RawMaterial(
#    material=Material("Gaea's Embrace"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Earth",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#faeroot = RawMaterial(
#    material=Material("Faeroot"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Natural",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#aetherwood = RawMaterial(
#    material=Material("Aetherwood"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Air",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#shockedstump = RawMaterial(
#    material=Material("Shockedstump"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Lightning",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#solwood = RawMaterial(
#    material=Material("Solwood"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Light",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#cimmerian_mahogany = RawMaterial(
#    material=Material("Cimmerian Mahogany"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Dark",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#shadowmire = RawMaterial(
#    material=Material("Shadowmire"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Dark",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#nightfallen = RawMaterial(
#    material=Material("Nightfallen"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Eclipse",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#celestiax = RawMaterial(
#    material=Material("Celestiax"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Eclipse",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#moonshade = RawMaterial(
#    material=Material("Moonshade"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Lunar",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#spiritbark = RawMaterial(
#    material=Material("Spiritbark"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Soul",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#shadowrot = RawMaterial(
#    material=Material("Shadowrot"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Soul",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#crimson_heart = RawMaterial(
#    material=Material("Crimsonheart"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Blood",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)
#
#vitalscar = RawMaterial(
#    material=Material("Vitalscar"),
#    rarity=Rarity.get_rarity_by_name("common"),
#    affinity="Blood",
#    mining_lvl=1,
#    bonus_percent=0,
#    description="None"
#)



#
##Raw Resources
#
#coal = raw_resources(raw_material(material("coal", True, True, False), "None", 1, 0), "we're cookin now")
#leather = raw_resources(raw_material(material("leather", True, True, False), "None", 1, 0), "good old reliable, good for light/studded armor")
#glass = raw_resources(raw_material(material("glass", True, True, False), "None", 1, 0), "transparent material, has many uses")
#fiber = raw_resources(raw_material(material("fiber", True, True, False), "None", 1, 0), "long loose material")
#fabric = raw_resources(raw_material(material("fabric", True, True, False), "None", 1, 0), "versatile material used for clothing and light equipment.")
#silk = raw_resources(raw_material(material("silk", True, "True", True), "None", 1, 0), "An expensive and higher quality fabric")
#

# Refined Metal
refined_iron = RefinedMaterial(
    #name="Refined Iron",
    material=Material("Refined Iron"),
    rarity_name="common",
    affinity="None",
    refining_level=1,
    bonus_percent=0,
    description="A common metal used in just about everything."
)

refined_blazeite = RefinedMaterial(
    material=Material("Refined Blazeite"),
    rarity_name="common",
    affinity="Fire",
    refining_level=1,
    bonus_percent=0,
    description="A fiery and volatile metal that burns with intense heat and can be used to imbue weapons with fire elemental power."
)

print("Successfully Imported Materials")
#print(refined_iron)