# Base Material class (unchanged)
class Material:
    def __init__(self, name):
        self.name = name

# RawMaterial class (with description)
class RawMaterial:
    def __init__(self, material, affinity, mining_lvl=1, bonus_percent=0, description=None):
        self.material = material
        self.name = material.name  # Share the same name as the base material
        self.affinity = affinity
        self.mining_lvl = mining_lvl
        self.bonus_percent = bonus_percent
        self.description = description

        # Register this material only if it's the first one of its kind
        if not MaterialRegistry.is_material_registered(self.name):
            MaterialRegistry.register_material(self.material)

    def __str__(self):
        return (f"{self.name} (Affinity: {self.affinity}, Mining Level: {self.mining_lvl}, "
                f"Bonus: {self.bonus_percent}%)\nDescription: {self.description}")

# RefinedMaterial class
class RefinedMaterial:
    def __init__(self, material, affinity, mining_lvl=1, bonus_percent=0, refining_level=1, description=None):
        self.material = material
        self.name = material.name  # Share the same name as the base material
        self.affinity = affinity
        self.mining_lvl = mining_lvl
        self.bonus_percent = bonus_percent
        self.refining_level = refining_level  # Added refining_level attribute
        self.description = description

        # Register the refined material, ensuring it hasn't been registered already
        if not MaterialRegistry.is_material_registered(self.name):
            MaterialRegistry.register_material(self.material)

    def __str__(self):
        return (f"Refined {self.name} (Refining Level: {self.refining_level}, "
                f"Affinity: {self.affinity}, Mining Level: {self.mining_lvl}, "
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
    material=Material("Iron Ore"),
    affinity="None",
    mining_lvl=1,
    bonus_percent=0,
    description="A common ore used as a cornerstone in metallurgy and construction."
)

blazeite_ore = RawMaterial(
    material=Material("Blazeite Ore"),
    affinity="Fire",
    mining_lvl=1,
    bonus_percent=0,
    description="A fiery and volatile ore that burns with intense heat and can be used to imbue weapons with fire elemental power."
)

seashine_ore = RawMaterial(
    material=Material("Seashine Ore"),
    affinity="Aqua",
    mining_lvl=1,
    bonus_percent=0,
    description="A luminescent ore that can be found in shallow waters, often used to make underwater lights."
)

quartzite_ore = RawMaterial(
    material=Material("Quartzite Ore"),
    affinity="Earth",
    mining_lvl=1,
    bonus_percent=0,
    description="A hard, translucent ore found in underground mines, used to create powerful, long-lasting batteries."
)

fae_ore = RawMaterial(
    material=Material("Fae Ore"),
    affinity="Natural",
    mining_lvl=1,
    bonus_percent=0,
    description="A glowing green ore found in enchanted glades, rumored to transport users to other dimensions."
)

stormite_ore = RawMaterial(
    material=Material("Stormite Ore"),
    affinity="Air",
    mining_lvl=1,
    bonus_percent=0,
    description="A dark, stormy ore found during thunderstorms, used to create items generating powerful gusts of wind."
)

thunderstone_ore = RawMaterial(
    material=Material("Thunderstone Ore"),
    affinity="Lightning",
    mining_lvl=1,
    bonus_percent=0,
    description="An ore that generates lightning bolts when struck, used to create items that grant control over electricity."
)

radiant_ore = RawMaterial(
    material=Material("Radiant Ore"),
    affinity="Light",
    mining_lvl=1,
    bonus_percent=0,
    description="A glittering ore found in bright light, used to imbue weapons with the power of the sun."
)

prismium_ore = RawMaterial(
    material=Material("Prismium Ore"),
    affinity="Light",
    mining_lvl=1,
    bonus_percent=0,
    description="A rainbow-colored ore used to create items that refract light and produce dazzling displays."
)

starsteel_ore = RawMaterial(
    material=Material("Starsteel Ore"),
    affinity="Light",
    mining_lvl=1,
    bonus_percent=0,
    description="A rare ore said to have fallen from the heavens, used to forge weapons with incredible precision."
)

ebonite_ore = RawMaterial(
    material=Material("Ebonite Ore"),
    affinity="Dark",
    mining_lvl=1,
    bonus_percent=0,
    description="A jet-black ore used to create weapons that absorb the life force of enemies."
)

umbrite_ore = RawMaterial(
    material=Material("Umbrite Ore"),
    affinity="Eclipse",
    mining_lvl=1,
    bonus_percent=0,
    description="An ore found during eclipses, used to craft items harnessing the power of both darkness and light."
)

celestite_ore = RawMaterial(
    material=Material("Celestite Ore"),
    affinity="Lunar",
    mining_lvl=1,
    bonus_percent=0,
    description="A pale blue ore from the stars, used to create items granting celestial power."
)

selene_ore = RawMaterial(
    material=Material("Selene Ore"),
    affinity="Lunar",
    mining_lvl=1,
    bonus_percent=0,
    description="A rare ore found during lunar phases, used to craft items with tidal influence."
)

starfall_ore = RawMaterial(
    material=Material("Starfall Ore"),
    affinity="Lunar",
    mining_lvl=1,
    bonus_percent=0,
    description="An ore falling during meteor showers, used to create items harnessing the power of the stars."
)

necrotite_ore = RawMaterial(
    material=Material("Necrotite Ore"),
    affinity="Soul",
    mining_lvl=1,
    bonus_percent=0,
    description="A powerful ore found near death, used to craft items granting control over undead creatures."
)

anima_ore = RawMaterial(
    material=Material("Anima Ore"),
    affinity="Soul",
    mining_lvl=1,
    bonus_percent=0,
    description="A glowing ore found in places of great spiritual energy, granting power over the soul."
)

spirit_ore = RawMaterial(
    material=Material("Spirit Ore"),
    affinity="Soul",
    mining_lvl=1,
    bonus_percent=0,
    description="An ethereal ore from places of emotional significance, harnessing the power of the soul."
)

hematite_ore = RawMaterial(
    material=Material("Hematite Ore"),
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="A shimmering ore generating a red liquid when struck, used to create items granting immense strength."
)

crimsonite_ore = RawMaterial(
    material=Material("Crimsonite Ore"),
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="A red ore found in the presence of blood, granting power over bloodshed."
)

vitae_ore = RawMaterial(
    material=Material("Vitae Ore"),
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="A rare ore containing the essence of life, used to craft items for healing and resurrection."
)

carnelian_ore = RawMaterial(
    material=Material("Carnelian Ore"),
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="A dark red ore found near bloodshed, used to craft items granting speed and agility."
)
# ------------------------------------------------------
# Raw Naturals
ignitionrot = RawMaterial(
    material=Material("Ignitionrot"),
    affinity="Fire",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

ocean_breath = RawMaterial(
    material=Material("Ocean's Breath"),
    affinity="Aqua",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

stonebark_pine = RawMaterial(
    material=Material("Stonebark Pine"),
    affinity="Earth",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

gaea_embrace = RawMaterial(
    material=Material("Gaea's Embrace"),
    affinity="Earth",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

faeroot = RawMaterial(
    material=Material("Faeroot"),
    affinity="Natural",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

aetherwood = RawMaterial(
    material=Material("Aetherwood"),
    affinity="Air",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

shockedstump = RawMaterial(
    material=Material("Shockedstump"),
    affinity="Lightning",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

solwood = RawMaterial(
    material=Material("Solwood"),
    affinity="Light",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

cimmerian_mahogany = RawMaterial(
    material=Material("Cimmerian Mahogany"),
    affinity="Dark",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

shadowmire = RawMaterial(
    material=Material("Shadowmire"),
    affinity="Dark",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

nightfallen = RawMaterial(
    material=Material("Nightfallen"),
    affinity="Eclipse",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

celestiax = RawMaterial(
    material=Material("Celestiax"),
    affinity="Eclipse",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

moonshade = RawMaterial(
    material=Material("Moonshade"),
    affinity="Lunar",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

spiritbark = RawMaterial(
    material=Material("Spiritbark"),
    affinity="Soul",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

shadowrot = RawMaterial(
    material=Material("Shadowrot"),
    affinity="Soul",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

crimson_heart = RawMaterial(
    material=Material("Crimsonheart"),
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

vitalscar = RawMaterial(
    material=Material("Vitalscar"),
    affinity="Blood",
    mining_lvl=1,
    bonus_percent=0,
    description="None"
)

print("Successfully Imported Materials")
#print(iron_ore)

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