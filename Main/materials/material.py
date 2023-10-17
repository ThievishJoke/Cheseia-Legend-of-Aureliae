


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
    def __init__(self):
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

iron_ore = raw_metals(raw_material(material("iron ore", True, True, False), "None", 1, 0), "ahh good old iron")
blazeite = raw_metals(raw_material(material("blazeite ore", True, True, False), "Fire", 1, 0), "a fiery and volatile ore that burns with intense heat and can be used to imbue weapons with fire elemental power.")
isinstance(iron_ore, raw_metals)
