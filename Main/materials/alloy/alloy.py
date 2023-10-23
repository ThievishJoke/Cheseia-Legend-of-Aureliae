from Main.materials.material import refined_materials
from rarity import RARITIES

print("hello")

class Alloy_Material(refined_materials):
    def validate_rarity(rarity):
        #check if rarity is valid
        if rarity != RARITIES():
            return "Error: Rarity Not valid"
        else:
            return rarity
    

    def __init__(self, name, rarity: validate_rarity(str()), description, affinity, alloy_passive, alloy_lvl = 1):
        self.name = name
        self.rarity = rarity
        self.description = description
        self.affinity = affinity
        self.alloy_passive = alloy_passive
        self.alloy_lvl = alloy_lvl
    def smelt_alloy(alloy_input_materials, alloy_output_meterial_ammount): #combing two or more refined metals
        #smelt alloy logic
        pass
    def mend_alloy(): #combining two or more refined naturals
        #mending logic
        pass


fae_gold = Alloy_Material("Fae-Gold", "rare", "A shimmering alloy created by combining Fae Ore and Gold. It harnesses the enchanting qualities of Fae Ore and the precious nature of gold, resulting in a material that enhances magical abilities, offers protection against magical attacks, and radiates a captivating aura.",
    "Natural", "Wish", 2)


isinstance(fae_gold, Alloy_Material)