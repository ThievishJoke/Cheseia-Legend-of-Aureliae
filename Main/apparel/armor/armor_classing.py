import materials.material
import rarity.item_rarities

class Armor:
    def __init__(self, name, defense, magic_resistance):
        self.name = name
        self.defense = defense
        self.defense = magic_resistance

    def get_info(self):
        return f"{self.name} - Defense: {self.name}, Magic Resistance: {self.magic_resistance}"

#def Armor_Weight():
    #light sacrafices defense for extra mobility
    #chain ?
    #mixed ?
    #extra light plated for good defense and good mobility (always requires a special skill)
    #light plated for defense for decent mobility
    #heavy plated opposite of light
    
    
class Helmet(Armor):
    def __init__(self, name, material, armor_weight_class, armor_skill_req, armor_perks, is_craftable, rarity):
        super().__init__(name, defense=0, magic_resistance=0)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.is_craftable = is_craftable
        self.rarity = rarity

        #class details
    
    def get_info(self):
        return f"{super().get_info()}, \
            Material: {self.material}, \
            Armor Weight: {self.armor_weight_class}, \
            Skill(s) Required: {self.armor_skill_req}, \
            Armor Perks: {self.armor_perks}, \
            Is Craftable: {self.is_craftable} \
            Rarity: {self.rarity}"

class ChestPiece(Armor):
    def __init__(self, name, material, armor_weight_class, armor_skill_req, armor_perks, is_craftable, rarity):
        super().__init__(name, defense=0, magic_resistance=0)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.is_craftable = is_craftable
        self.rarity = rarity

        #class details
    
    def get_info(self):
        return f"{super().get_info()}, \
            Material: {self.material}, \
            Armor Weight: {self.armor_weight_class}, \
            Skill(s) Required: {self.armor_skill_req}, \
            Armor Perks: {self.armor_perks}, \
            Is Craftable: {self.is_craftable} \
            Rarity: {self.rarity}"

class Glove(Armor):
    def __init__(self, name, material, armor_weight_class, armor_skill_req, armor_perks, is_craftable, rarity):
        super().__init__(name, defense=0, magic_resistance=0)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.is_craftable = is_craftable
        self.rarity = rarity

        #class details
    
    def get_info(self):
        return f"{super().get_info()}, \
            Material: {self.material}, \
            Armor Weight: {self.armor_weight_class}, \
            Skill(s) Required: {self.armor_skill_req}, \
            Armor Perks: {self.armor_perks}, \
            Is Craftable: {self.is_craftable} \
            Rarity: {self.rarity}"

class Gauntlet(Armor):
    def __init__(self, name, material, armor_weight_class, armor_skill_req, armor_perks, is_craftable, rarity):
        super().__init__(name, defense=0, magic_resistance=0)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.is_craftable = is_craftable
        self.rarity = rarity

        #class details
    
    def get_info(self):
        return f"{super().get_info()}, \
            Material: {self.material}, \
            Armor Weight: {self.armor_weight_class}, \
            Skill(s) Required: {self.armor_skill_req}, \
            Armor Perks: {self.armor_perks}, \
            Is Craftable: {self.is_craftable} \
            Rarity: {self.rarity}"
    
class Leggings(Armor):
    def __init__(self, name, material, armor_weight_class, armor_skill_req, armor_perks, is_craftable, rarity):
        super().__init__(name, defense=0, magic_resistance=0)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.is_craftable = is_craftable
        self.rarity = rarity

        #class details
    
    def get_info(self):
        return f"{super().get_info()}, \
            Material: {self.material}, \
            Armor Weight: {self.armor_weight_class}, \
            Skill(s) Required: {self.armor_skill_req}, \
            Armor Perks: {self.armor_perks}, \
            Is Craftable: {self.is_craftable} \
            Rarity: {self.rarity}"

class Boots(Armor):
    def __init__(self, name, material, armor_weight_class, armor_skill_req, armor_perks, is_craftable, rarity):
        super().__init__(name, defense=0, magic_resistance=0)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.is_craftable = is_craftable
        self.rarity = rarity

        #class details
    
    def get_info(self):
        return f"{super().get_info()}, \
            Material: {self.material}, \
            Armor Weight: {self.armor_weight_class}, \
            Skill(s) Required: {self.armor_skill_req}, \
            Armor Perks: {self.armor_perks}, \
            Is Craftable: {self.is_craftable} \
            Rarity: {self.rarity}"