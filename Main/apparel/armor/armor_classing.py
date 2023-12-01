#import materials.material
#import rarity.item_rarities

class Armor:
    def __init__(self, name, defense=0, magic_resistance=0):
        self.name = name
        self.defense = defense
        self.magic_resistance = magic_resistance

    def get_info(self):
        return f"{self.name} - \n Defense: {self.defense}\n Magic Resistance: {self.magic_resistance}"

#def Armor_Weight():
    #light sacrafices defense for extra mobility
    
    #chain ?
    #mixed ?
    #extra light plated for good defense and good mobility (always requires a special skill)
    #light plated for defense for decent mobility
    #heavy plated opposite of light

    #modify player bonus movement
    #update bonus movement after unequiping
    
    
class Helmet(Armor):
    def __init__(self, name, defense, magic_resistance, material, armor_weight_class, armor_skill_req, armor_perks, rarity, is_craftable=True):
        super().__init__(name, defense, magic_resistance)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.rarity = rarity
        self.is_craftable = is_craftable
        #class details
    
    def get_info(self):
        return f"- {super().get_info()}\n Material: {self.material}\n Armor Weight: {self.armor_weight_class}\n Skill(s) Required: {self.armor_skill_req}\n Armor Perks: {self.armor_perks}\n Rarity: {self.rarity}\n Is Craftable: {self.is_craftable}\n"

class ChestPiece(Armor):
    def __init__(self, name, defense, magic_resistance, material, armor_weight_class, armor_skill_req, armor_perks, rarity, is_craftable=True):
        super().__init__(name, defense, magic_resistance)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.rarity = rarity
        self.is_craftable = is_craftable
        #class details
    
    def get_info(self):
        return f"- {super().get_info()}\n Material: {self.material}\n Armor Weight: {self.armor_weight_class}\n Skill(s) Required: {self.armor_skill_req}\n Armor Perks: {self.armor_perks}\n Rarity: {self.rarity}\n Is Craftable: {self.is_craftable}\n"

class Glove(Armor):
    def __init__(self, name, defense, magic_resistance, material, armor_weight_class, armor_skill_req, armor_perks, rarity, is_craftable=True):
        super().__init__(name, defense, magic_resistance)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.rarity = rarity
        self.is_craftable = is_craftable
        #class details
    
    def get_info(self):
        return f"- {super().get_info()}\n Material: {self.material}\n Armor Weight: {self.armor_weight_class}\n Skill(s) Required: {self.armor_skill_req}\n Armor Perks: {self.armor_perks}\n Rarity: {self.rarity}\n Is Craftable: {self.is_craftable}\n"

class Gauntlet(Armor):
    def __init__(self, name, defense, magic_resistance, material, armor_weight_class, armor_skill_req, armor_perks, rarity, is_craftable=True):
        super().__init__(name, defense, magic_resistance)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.rarity = rarity
        self.is_craftable = is_craftable
        #class details
    
    def get_info(self):
        return f"- {super().get_info()}\n Material: {self.material}\n Armor Weight: {self.armor_weight_class}\n Skill(s) Required: {self.armor_skill_req}\n Armor Perks: {self.armor_perks}\n Rarity: {self.rarity}\n Is Craftable: {self.is_craftable}\n"
    
class Leggings(Armor):
    def __init__(self, name, defense, magic_resistance, material, armor_weight_class, armor_skill_req, armor_perks, rarity, is_craftable=True):
        super().__init__(name, defense, magic_resistance)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.rarity = rarity
        self.is_craftable = is_craftable
        #class details
    
    def get_info(self):
        return f"- {super().get_info()}\n Material: {self.material}\n Armor Weight: {self.armor_weight_class}\n Skill(s) Required: {self.armor_skill_req}\n Armor Perks: {self.armor_perks}\n Rarity: {self.rarity}\n Is Craftable: {self.is_craftable}\n"

class Boots(Armor):
    def __init__(self, name, defense, magic_resistance, material, armor_weight_class, armor_skill_req, armor_perks, rarity, is_craftable=True):
        super().__init__(name, defense, magic_resistance)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.rarity = rarity
        self.is_craftable = is_craftable

        #class details
    
    def get_info(self):
        return f"- {super().get_info()}\n Material: {self.material}\n Armor Weight: {self.armor_weight_class}\n Skill(s) Required: {self.armor_skill_req}\n Armor Perks: {self.armor_perks}\n Rarity: {self.rarity}\n Is Craftable: {self.is_craftable}\n"

helmet = Helmet("Celestite Helmet", 10, 10, "Celestite", "Heavy", "None", "None", "Rare", True)
print(helmet.get_info())