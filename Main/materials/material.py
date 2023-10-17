
class material: # Defines A material
    def __init__(self, name, is_sellable, is_rewardable, is_craftable): #Initiate material
        self.name = name
        self.is_sellable = is_sellable
        self.is_rewardable = is_rewardable
        self.is_craftable = is_craftable

    def craft(self):
        if self.is_sellable == True:
            pass

class raw_material(material):
    def __init__(self, mining_lvl = 1, bonus_percent = 0):
        self.mining_lvl = mining_lvl
        self.bonus_percent = bonus_percent
    pass

class metal(raw_material):
    pass

class natural(raw_material):
    pass

class refined_material():
    pass

