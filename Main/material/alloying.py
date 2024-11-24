#from Main.materials.material import refined_materials
#from Main.rarity.item_rarities import RARITIES
import time

class Alloy_Material():#reference refined_materials
    #def validate_rarity(rarity):
    #    pass
    #    #check if rarity is valid
    #    if rarity != RARITIES():
    #        return "Error: Rarity Not valid"
    #    else:
    #        return rarity
    
    def __init__(self, name, rarity, description, affinity, alloy_passive, alloy_lvl = 1, crafting_time = 3):
        self.name = name
        self.rarity = rarity
        self.description = description
        self.affinity = affinity
        self.alloy_passive = alloy_passive
        self.alloy_lvl = alloy_lvl
        self.crafting_time = crafting_time
        self.craftable_smelting_alloys = {
            #list of craftable alloys and recipes
            "Steel": {"Iron": 3, "Coal": 1},
        }
        self.craftable_mending_alloys = {
            #list of craftable alloys and recipes
            "Spiritwood Ash": {"Spiritwood": 2, "Ashwood": 3}
        }

    def animate_crafting(alloy_type, crafting_time, bar_width=10):
        if alloy_type == ("Smelting"):
            print(f"{alloy_type}", end='', flush=True)

            for i in range(crafting_time * 4):
                time.sleep(0.125)
                progress = int((i + 1) / 4 / crafting_time * bar_width)
                bar = "■" * progress + "-" * (bar_width - progress)
                print("\r[{}] {}%".format(bar, int(((i + 1) / 4 / crafting_time) * 100)), end='', flush=True)


        if alloy_type == ("Mending"):
            print(f"{alloy_type}", end='', flush=True)

            for i in range(crafting_time * 4):
                time.sleep(0.125)
                progress = int((i + 1) / 4 / crafting_time * bar_width)
                bar = "■" * progress + "-" * (bar_width - progress)
                print("\r[{}] {}%".format(bar, int(((i + 1) / 4 / crafting_time) * 100)), end='', flush=True)
    
    def smelt_alloy(self, name, alloy_input_materials, alloy_output_material_amount): #combing two or more refined metals
        #smelt alloy logic
        if name in self.craftable_smelting_alloys:
            #check player alloying lvl
            if player_alloy_lvl >= self.alloy_lvl:
                #check for input availability
                for material, amount in alloy_input_materials.items():
                    if not self.check_material_availability(material, amount):
                        print(f"Not enough {material} to create {name}.")
                        return

                #if successful
                Alloy_Material.animate_crafting("Smelting", self.crafting_time)

                #update inventory (:3)
                print(f"\n{name} Smelting Succesful! {alloy_output_material_amount} {name} created.")

                #possibly reprompt smelting
            else:
                print(f"Smelting failed, alloying level too low to Smelt {name}")
        else:
            print(f"{name} Error: Alloy not a craftable")

    def mend_alloy(self, name, alloy_input_materials, alloy_output_material_amount): #combining two or more refined natural materials
        #mending logic
        if name in self.craftable_mending_alloys:
            #check player alloying lvl
            if player_alloy_lvl >= self.alloy_lvl:
                #check for input availability
                for material, amount in alloy_input_materials.items():
                    if not self.check_material_availability(material, amount):
                        print(f"Not enough {material} to create {name}.")
                        return
                
                #if successful
                Alloy_Material.animate_crafting("Mending", self.crafting_time)

                #update inventory (:3)
                print(f"\n{name} Mending Succesful! {alloy_output_material_amount} {name} created.")

                #possibly reprompt mending
            else:
                print(f"Mending failed, alloying level too low to mend {name}")
        else:
            print(f"{name} Error: Alloy not a craftable")

    def check_material_availability(self, material, amount):
            #check player alloying lvl (:3)
            #return false if not high enough
            #return true if skill is high enough

            #check player inventory (:3)
            #return false if not available
            return True

    def get_info(self):
        return f"\n- Material: {self.name} - \n Material Rarity: {self.rarity}\n Description: {self.description}\n Material Affinity: {self.affinity}\n Material Passive: {self.alloy_passive}\n Alloy Crafting Level: {self.alloy_lvl}\n"

#need to check the players actual alloy stat this is merely an example
player_alloy_lvl = 3

STEEL = Alloy_Material("Steel", "Common", "Iron & Coal Alloy", None, None, 1, 3)

print(STEEL.get_info())

input_materials = {"Iron": 3, "Coal": 1}
output_material_amount = 1

STEEL.smelt_alloy("Steel", alloy_input_materials=input_materials, alloy_output_material_amount=output_material_amount)
#-----------------------------
SPIRITWOOD = Alloy_Material("Spiritwood Ash", "Uncommon", "Spiritwood & Ashwood Mend", None, None, 2, 10)

print(SPIRITWOOD.get_info())

input_materials = {"Spiritwood": 2, "Ashwood": 3}
output_material_amount = 2

SPIRITWOOD.mend_alloy("Spiritwood Ash", alloy_input_materials=input_materials, alloy_output_material_amount=output_material_amount)
