#import materials.material
#import rarity.item_rarities

class Armor:
    def __init__(self, name, defense=0, magic_resistance=0, armor_weight_class="Light"):
        self.name = name
        self.defense = defense
        self.magic_resistance = magic_resistance
        self.armor_weight_class = armor_weight_class

    def get_info(self):
        return f"{self.name} - \n Defense: {self.defense}\n Magic Resistance: {self.magic_resistance}"

    def Armor_Weight(self, equip=True):
        if equip:
            # Logic for updating player 
            if self.armor_weight_class == "Light Fabric":
                # only natural + fabric
                # change player bonus movement by amount
                pass
            elif self.armor_weight_class == "Light Metal":
                # only metal or any alloy
                # change player bonus movement by amount
                pass
            elif self.armor_weight_class == "Chain":
                # only metal or smelt alloy
                # change player bonus movement by amount
                pass
            elif self.armor_weight_class == "Mixed":
                # can be any alloy
                # change player bonus movement by amount*
                # armor material specified amount*
                pass
            elif self.armor_weight_class == "Light Plate":
                # can be both any material
                # change player bonus movement by amount
                pass
            elif self.armor_weight_class == "Heavy Fabric":
                # only natural + fabric
                # change player bonus movement by amount
                pass
            elif self.armor_weight_class == "Heavy Chitan":
                # only natural
                # change player bonus movement by amount
                pass
            elif self.armor_weight_class == "Heavy Plate":
                # only metal and smelted alloy
                # change player bonus movement by amount
                pass
            return bonus_movement_modifier
        else:
            #update player bonus movement
            bonus_movement_modifier = 0
            return 
    
class Helmet(Armor):
    def __init__(self, name, defense, magic_resistance, material, armor_weight_class, armor_skill_req, armor_perks, rarity, is_craftable=True):
        super().__init__(name, defense, magic_resistance, armor_weight_class)
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
        super().__init__(name, defense, magic_resistance, armor_weight_class)
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
        super().__init__(name, defense, magic_resistance, armor_weight_class)
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
        super().__init__(name, defense, magic_resistance, armor_weight_class)
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
        super().__init__(name, defense, magic_resistance, armor_weight_class)
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
        super().__init__(name, defense, magic_resistance, armor_weight_class)
        self.material = material
        self.armor_weight_class = armor_weight_class
        self.armor_skill_req = armor_skill_req
        self.armor_perks = armor_perks
        self.rarity = rarity
        self.is_craftable = is_craftable
        #class details
    
    def get_info(self):
        return f"- {super().get_info()}\n Material: {self.material}\n Armor Weight: {self.armor_weight_class}\n Skill(s) Required: {self.armor_skill_req}\n Armor Perks: {self.armor_perks}\n Rarity: {self.rarity}\n Is Craftable: {self.is_craftable}\n"

material = "Celestite"
helmet = Helmet(f"{material} Helmet", 10, 10, f"{material}", "Heavy Plate", "None", "None", "Rare", True)
print(helmet.get_info())