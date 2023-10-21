


class material: # Defines A material
    def __init__(self, name, is_sellable, is_rewardable, is_craftable): #Initiate material
        self.name = name
        self.is_sellable = is_sellable
        self.is_rewardable = is_rewardable
        self.is_craftable = is_craftable

    def craft(self):
        if self.is_craftable == True:
            pass

class raw_material(material):
    def __init__(self, material, affinity, mining_lvl = 1, bonus_percent = 0):
        self.material = material
        self.affinity = affinity #The Elemental affinity the refined material has
        self.mining_lvl = mining_lvl
        self.bonus_percent = bonus_percent
    def print_material(self):
        print(self.material.name)
        print(self.material.is_sellable)
        print(self.material.is_rewardable)
        print(self.material.is_craftable)
        print(self.mining_lvl)
        print(self.bonus_percent)

class raw_metals(raw_material):
    def __init__(self, description):
        self.description = description
        pass

class raw_naturals(raw_material):
    def __init__(self, description):
        self.description = description
        pass

class raw_resources(raw_material):
    def __init__(self, description):
        self.description = description
        pass

class refined_materials(raw_metals, raw_naturals):
    def __init__(self, is_metal, is_natural, crafting_lvl = 1, bonus_percent = 0):
        self.is_metal = is_metal
        self.is_natural = is_natural
        self.crafting_lvl = crafting_lvl
        self.bonus_percent = bonus_percent
    
    def smelt(self):
        if(self.is_metal == True): #check if material is metal
            pass

        #if(self.crafting_lvl == required_lvl): #craft item you meet lvl requirement
        #    pass
        pass

    def refine(self):
        if(self.is_natural == True): #check if material is metal
            pass

        #if(self.crafting_lvl == required_lvl): #craft item you meet lvl requirement
        #    pass
        pass

    def print_material(self):
        print(material.name)
        print(material.is_sellable)
        print(material.is_rewardable)
        print(material.is_craftable)
        print(self.affinity)
        print(self.crafting_lvl)
        print(self.bonus_percent)

#Raw metals

iron_ore = raw_metals(raw_material(material("iron ore", True, True, False), "None", 1, 0),
    "ahh good old iron.")
blazeite_ore = raw_metals(raw_material(material("blazeite ore", True, True, False), "Fire", 1, 0),
    "a fiery and volatile ore that burns with intense heat and can be used to imbue weapons with fire elemental power.")
seashine_ore = raw_metals(raw_material(material("seashine ore", True, True, False), "Aqua", 1, 0),
    "a luminescent ore that can be found in shallow waters, it is often used to make underwater lights.")
quartzite_ore = raw_metals(raw_material(material("quartzite ore", True, True, False), "Earth", 1, 0),
    "a hard, translucent ore that can be found in underground mines and can be used to create powerful, long-lasting batteries.")
fae_ore = raw_metals(raw_material(material("fae ore", True, True, False), "Natural", 1, 0),
    "a glowing green ore that can be found within enchanted glades, it is said to have the power to transport the user to other dimensions.")
stormite_ore = raw_metals(raw_material(material("stormite ore", True, True, False), "Air", 1, 0),
    "a dark, stormy ore that can be found during thunderstorms, it can be used to create items that generate powerful gusts of wind.")
thunderstone_ore = raw_metals(raw_material(material("thunderstone ore", True, True, False), "Lightning", 1, 0),
    "an ore that generates lightning bolts when struck, it can be used to create items that grant the user control over electricity.")
radiant_ore = raw_metals(raw_material(material("radiant ore", True, True, False), "Light", 1, 0),
    "a glittering ore that can be found in the presence of bright light, it can be used to imbue weapons with the power of the sun.")
prismium_ore = raw_metals(raw_material(material("prismium ore", True, True, False), "Light", 1, 0),
    "a rainbow-colored ore that can be used to create items that refract light and create dazzling displays.")
starsteel_ore = raw_metals(raw_material(material("starsteel ore", True, True, False), "Light", 1, 0),
    "a rare and precious ore that is said to have fallen from the heavens, it can be used to create weapons with incredible accuracy and precision.")
ebonite_ore = raw_metals(raw_material(material("ebonite ore", True, True, False), "Dark", 1, 0),
    "a jet-black ore that can be used to create weapons that absorb the life force of enemies.")
umbrite_ore = raw_metals(raw_material(material("umbrite ore", True, True, False), "Eclipse", 1, 0),
    "an ore that can only be found during eclipses, it can be used to create items that grant the user the power of darkness and light.")
celestite_ore = raw_metals(raw_material(material("celestite ore", True, True, False), "Lunar", 1, 0),
    "a pale blue ore that can be found within the stars, it can be used to create items that grant the user the power of the heavens.")
selene_ore = raw_metals(raw_material(material("selene ore", True, True, False), "Lunar", 1, 0),
    "a rare and precious ore that can only be found during certain lunar phases, it can be used to create items that grant the user the power of the tides.")
starfall_ore = raw_metals(raw_material(material("starfall ore", True, True, False), "Lunar", 1, 0),
    "an ore that falls from the sky during meteor showers, it can be used to create items that grant the user the power of the stars.")
necrotite_ore = raw_metals(raw_material(material("necrotite ore", True, True, False), "Soul", 1, 0),
    "a powerful ore that can be found in the presence of death, it can be used to create items that grant the user control over undead creatures.")
anima_ore = raw_metals(raw_material(material("anima ore", True, True, False), "Soul", 1, 0),
    "a glowing ore that can be found within places of great spiritual energy, it can be used to create items that grant the user the power of the soul.")
spirit_ore = raw_metals(raw_material(material("spirit ore", True, True, False), "Soul", 1, 0),
    "an ethereal ore that can be found in places of great emotional significance, it can be used to create items that harness the power of the soul.")
hematite_ore = raw_metals(raw_material(material("starfall ore", True, True, False), "Blood", 1, 0),
    "a shimmering ore that generates a red liquid when struck, it can be used to create items that grant the user incredible strength.")
crimsonite_ore = raw_metals(raw_material(material("starfall ore", True, True, False), "Blood", 1, 0),
    "a red ore that can be found in the presence of blood.")
vitae_ore = raw_metals(raw_material(material("starfall ore", True, True, False), "Blood", 1, 0),
    "a rare and precious ore that contains the essence of life, it can be used to create items that grant the user the power to heal wounds and revive the dead.")
carnelian_ore = raw_metals(raw_material(material("starfall ore", True, True, False), "Blood", 1, 0),
    "a dark red ore that can be found in the presence of bloodshed, it can be used to create items that grant the user incredible speed and agility.")

#Raw Naturals

ignitionrot = raw_naturals(raw_material(material("ignitionrot", True, True, False), "Fire", 1, 0),
    "None")
ocean_breath = raw_naturals(raw_material(material("ocean's breath", True, True, False), "Aqua", 1, 0),
    "None")
stonebark_pine = raw_naturals(raw_material(material("stonebark pine", True, True, False), "Earth", 1, 0),
    "None")
gaea_embrace = raw_naturals(raw_material(material("gaea's embrace", True, True, False), "Earth", 1, 0),
    "None")
faeroot = raw_naturals(raw_material(material("faeroot", True, True, False), "Natural", 1, 0),
    "None")
aetherwood = raw_naturals(raw_material(material("aetherwood", True, True, False), "Air", 1, 0),
    "None")
shockedstump = raw_naturals(raw_material(material("shockedstump", True, True, False), "Lightning", 1, 0),
    "None")
solwood = raw_naturals(raw_material(material("solwood", True, True, False), "Light", 1, 0),
    "None")
cimmerian_mahogany = raw_naturals(raw_material(material("cimmerian mahogany", True, True, False), "Dark", 1, 0),
    "None")
shadowmire = raw_naturals(raw_material(material("shadowmire", True, True, False), "Dark", 1, 0),
    "None")
nightfallen = raw_naturals(raw_material(material("nightfallen", True, True, False), "Eclipse", 1, 0),
    "None")
celestiax = raw_naturals(raw_material(material("celestiax", True, True, False), "Eclipse", 1, 0),
    "None")
moonshade = raw_naturals(raw_material(material("moonshade", True, True, False), "Lunar", 1, 0),
    "None")
spiritbark = raw_naturals(raw_material(material("spiritbark", True, True, False), "Soul", 1, 0),
    "None")
shadowrot = raw_naturals(raw_material(material("shadowrot", True, True, False), "Soul", 1, 0),
    "None")
crimsonheart = raw_naturals(raw_material(material("crimsonheart", True, True, False), "Blood", 1, 0),
    "None")
vitalscar = raw_naturals(raw_material(material("vitalscar", True, True, False), "Blood", 1, 0),
    "None")

#Raw Resources

coal = raw_resources(raw_material(material("coal", True, True, False), "None", 1, 0), "we're cookin now")
leather = raw_resources(raw_material(material("leather", True, True, False), "None", 1, 0), "good old reliable, good for light/studded armor")
glass = raw_resources(raw_material(material("glass", True, True, False), "None", 1, 0), "transparent material, has many uses")
fiber = raw_resources(raw_material(material("fiber", True, True, False), "None", 1, 0), "long loose material")
fabric = raw_resources(raw_material(material("fabric", True, True, False), "None", 1, 0), "versatile material used for clothing and light equipment.")


isinstance(iron_ore, raw_metals)
