import json
import main.weapon_gen as wepn
import main.locations.locations as loci
import main.creatures.hostile.enemies as enem
import random
import main.combat.encounter as ectr
import pathlib
import math
import time
import sys

#--------------------------------------------------------------------------------------------------- Save Functions

savestate = "savestate.json"
savestate_path = savestate if pathlib.Path.cwd() else None
game_save = "save.json"
game_save_path = game_save if pathlib.Path.cwd() else None

with open(savestate_path, "r") as f:
    Aureliae_savestate_load = json.load(f)
    AureliaeLore = json.dumps(Aureliae_savestate_load, indent=2)#Lore Sheet
    if ((Aureliae_savestate_load["Debug"]) == True):
        debug = True
    else: debug = False
if (debug == True):
    print(Aureliae_savestate_load["Debug"])

def newstart():
    global saved_data
    #set save default save state
    current_lvl = 1
    xp_nxt_lvl = 0
    player_xp = 0
    player_builder = False
    experimentals = False
    while (player_builder == False):
        player_username = input("Insert A Name \n" + "> ") #Player Name
        if experimentals == True:
            ask_player_sir_name = input("Do You Want A Sir Name? \n Yes |1| | No |0|")
            if ask_player_sir_name == 1:
                player_sir_name = input("Insert A Sir Name \n" + "> ")
            elif ask_player_sir_name != 1 or ask_player_sir_name == 0:
                player_sir_name = None
        player_gender = input ("Male | Female | Other \n" + "> ") # Gender/Sex
        gender_check = False
        player_genders = ["Male", "Female", "Other"]
        while (gender_check == False):
            if player_gender in player_genders:
                gender_check = True
            elif player_gender not in player_genders:
                player_gender = input ("Male | Female | Other \n" + "> ") # Typo Protection

        player_class = input("Warrior | Thief | Bard | Mage | Paladin | Healer | Ranger | Fighter \n" + "> ") # Player Classes
        class_check = False
        player_class_list = ["Warrior", "Thief", "Bard", "Mage", "Paladin", "Healer", "Ranger", "Fighter"]
        while (class_check == False):
            if player_class in player_class_list:
                class_check = True
            elif player_class not in player_class_list:
                player_class = input("Warrior | Thief | Bard | Mage | Paladin | Healer | Ranger | Fighter \n" + "> ") # Typo Protection

        elemental_aff = input("Fire, Aqua, Earth, Air, Lightning \n" + "> ")# Elemental Affinity
        affininity_check = False
        elemental_aff_list = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
        while (affininity_check == False):
            if elemental_aff in elemental_aff_list:
                player_builder = True
                affininity_check = True
            elif elemental_aff not in elemental_aff_list:
                elemental_aff = input("Fire, Aqua, Earth, Air, Lightning \n" + "> ") # Typo Protection

    #player_info
    saved_data = {
        "PlayerName" : player_username, #username
        "Titles" : "",
        "Gender" : player_gender, #gender/sex
        "Class" : player_class, #class
        "Region" : "Puregarde",
        "Location" : "Loch Cudgami",
        "Cord" : (-2,10),
        "Elemental Affinity" : elemental_aff,
        "Max Hp" : 20,
        "Hp" : 20,
        "Bonus Physical Critical Hit Rate" : 0,
        "Bonus Magic Critical Hit Rate" : 0,
        "Dmg" : 5,
        "Stamina" : 100,
        "Magic Dmg" : 0,
        "Mana" : 100,
        "Spell Mana" : 100,
        "Magic Resistance" : 0,
        "Armor" : 0,
        "Player Xp" : player_xp, #xp points
        "Current Lvl" : current_lvl, #player level
        "Xp Needed" : int(80*(1.5*current_lvl)), #xp needed
        "Total Xp" : 0,
        "Perk Points" : 0,
        "Aureliaen Gold Coins" : 0,
        "Gem Count" : 0,
        "Elemental Gem" : 0,
        "Potion Count" : 0,
        "Passive Abilities" : {
        },
        "Current Weapon" : wepn.starting_weapon,
        "Inventory" : {
            "Weapons" : "",
            "Materials" : "",
            "Collectables" : "",
            "Key Items" : "",
        }
    }
    #class stats
    if (player_class == "Warrior"):
        saved_data["Max Hp"] = 35
        saved_data["Hp"] = 35
        saved_data["Armor"] = 2
        saved_data["Magic Resistance"] = 4
        saved_data["Spell Mana"] = saved_data["Mana"]
        saved_data["Aureliaen Gold Coins"] = 25
        saved_data["Mana"] = 15
    if (player_class == "Thief"):
        saved_data["Stamina"] = 120
        saved_data["Spell Mana"] = saved_data["Mana"]
        saved_data["Aureliaen Gold Coins"] = 75
    if (player_class == "Bard"):
        saved_data["Stamina"] = 120
        saved_data["Mana"] = 135
        saved_data["Spell Mana"] = saved_data["Mana"]
        saved_data["Aureliaen Gold Coins"] = -50
    if (player_class == "Mage"):
        saved_data["Max Hp"] = 15
        saved_data["Hp"] = 15
        saved_data["Mana"] = 180
        saved_data["Spell Mana"] = saved_data["Mana"]
        saved_data["Magic Dmg"] = 8
    if (player_class == "Paladin"):
        saved_data["Armor"] = 3
        saved_data["Mana"] = 120
        saved_data["Spell Mana"] = saved_data["Mana"]
        saved_data["Aureliaen Gold Coins"] = 200
        if (elemental_aff == "Light"):
            saved_data["HP"] = 30
            saved_data["Magic Dmg"] = 2
        else:
            pass
    if (player_class == "Healer"):
        saved_data["Magic Dmg"] = 2
        saved_data["Stamina"] = 80
        saved_data["Mana"] = 160
        saved_data["Spell Mana"] = saved_data["Mana"]
        saved_data["Aureliaen Gold Coins"] = 50
        if (elemental_aff == "Light"):
            saved_data["Region"] = "Shimmergarde"
            saved_data["Location"] = "Lrimmere"
            saved_data["Max Hp"] = 25
            saved_data["Hp"] = 25
            saved_data["Magic Dmg"] = 2.5
            saved_data["Stamina"] = 50
            saved_data["Mana"] = 200
            saved_data["Spell Mana"] = saved_data["Mana"]
            saved_data["Armor"] = -1
            saved_data["Aureliaen Gold Coins"] = 100
        if (elemental_aff == "Dark"):
            saved_data["Region"] = "Ebonmeadow"
            saved_data["Location"] = "Asheigh"
            saved_data["Max Hp"] = 35
            saved_data["Hp"] = 35
            saved_data["Dmg"] = 8
            saved_data["Magic Dmg"] = 5
            saved_data["Stamina"] = 85
            saved_data["Mana"] = 130
            saved_data["Spell Mana"] = saved_data["Mana"]
            saved_data["Armor"] = 1
            saved_data["Aureliaen Gold Coins"] = 0
        elif (elemental_aff == "Soul"):
            saved_data["Max Hp"] = 25
            saved_data["Hp"] = 25
            saved_data["Magic Dmg"] = 4
        elif (elemental_aff == "Blood"):
            saved_data["Location"] = "Maplepeak"
            saved_data["Max Hp"] = 40
            saved_data["Hp"] = 40
            saved_data["Magic Dmg"] = 3.5
        else:
            pass
    if (player_class == "Ranger"):
        saved_data["Hp"] = 20
        saved_data["Dmg"] = 8
    if (player_class == "Fighter"):
        saved_data["Hp"] = 50
        saved_data["Dmg"] = 7
    else:
        pass
    if (saved_data["Region"] == "Puregarde"):
        saved_data["Cord"] = loci.RD_Puregarde["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "Starmoor"):
        saved_data["Cord"] = loci.RD_Starmoor["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "Frostmord"):
        saved_data["Cord"] = loci.RD_Frostmord["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "Shimmergarde"):
        saved_data["Cord"] = loci.RD_Shimmergarde["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "Dimhollow"):
        saved_data["Cord"] = loci.RD_Dimhollow["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "Ebonmeadow"):
        saved_data["Cord"] = loci.RD_Ebonmeadow["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "Duskgrove"):
        saved_data["Cord"] = loci.RD_Duskgrove["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "Dawngrove"):
        saved_data["Cord"] = loci.RD_Dawngrove["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "The Subterrane"):
        saved_data["Cord"] = loci.RD_TheSubterrane["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "The Subterrane Sea"):
        saved_data["Cord"] = loci.RD_TheSubterraneSea["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "North Sea"):
        saved_data["Cord"] = loci.RD_NorthSea["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "South Sea"):
        saved_data["Cord"] = loci.RD_SouthSea["Name"][saved_data["Location"]]["Cords"]
    elif (saved_data["Region"] == "The Welkin"):
        saved_data["Cord"] = loci.RD_TheWelkin["Name"][saved_data["Location"]]["Cords"]
    #the player save
    with open(game_save, "w") as f:
        json.dump(saved_data, f, indent=2)
        json_save_data = json.dumps(saved_data, indent=2)
        #print(json_save_data)
    print("\nNew Game Started")

askstart = int(input("\nCheseia: Legend of Areliee\n\nNew Game|1| Continue|2| Quit|3| \n" + "> ")) #|4| Enable Debug Continue Previous Save

if (askstart == 1):
    #new save/overwrite old save
    newstartconf = int(input("Are You Sure?\nThis Will Overwrite Any Previous Saves?\nTHE GAME WILL AUTOMATICALLY QUIT IF NOT\nYes|1| No|2| \n" + "> ")) 
    if (newstartconf == 1): #Write Newsave/Overwrite Existing
        #Set False
        newsave = {
            "existing_save": False,
            "World_Seed": (random.randint(1,100000)),
            "Debug": False,
        }
        with open(savestate, "w") as n:
            json.dump(newsave, n, indent=2)
            json_save_state_dat = json.dumps(newsave, indent=2)
        newstart() #function
        #Set True
        newsave = {
            "existing_save": True,
            "World_Seed": (random.randint(1,100000)), #New Seed
            "Debug": False,
        }
        with open(savestate, "w") as n:
            json.dump(newsave, n, indent=2)
            json_save_state_dat = json.dumps(newsave, indent=2)
        with open(game_save, "r") as f: #Load Created Newly Created Save
            player_info = json.load(f)
            player_sheet = json.dumps(player_info, indent=2)#Player Sheet
            #print(player_sheet) 
    elif (newstartconf == 2): #Cancel Overwrite
        quit

elif (askstart == 2):
    #load old save
    with open(game_save, "r") as f:
        player_info = json.load(f)
        player_sheet = json.dumps(player_info, indent=2)#Player Sheet
        if (debug == True):
            print("\n-Debug- \n", player_sheet, "\n-Dubug-\n") 
    menu_txt_1a = ("\nWelcome Back ", player_info["PlayerName"], "\n")
    for character in menu_txt_1a:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

elif (askstart == 3):
    #quit
    print("\nLater")
    quit
    pass

elif (askstart == 4): #Enable All Debugging On Outisde Scripts & Reset Seed
    newsave = {
        "existing_save": True,
        "World_Seed": (random.randint(1,100000)), #New Seed
        "Debug": True,
    }
    with open(savestate, "w") as n:
        json.dump(newsave, n, indent=2)
        json_save_state_dat = json.dumps(newsave, indent=2)
    #load old save
    with open(game_save, "r") as f:
        player_info = json.load(f)
        player_sheet = json.dumps(player_info, indent=2)#Player Sheet
        if (debug == True):
            print("\n-Debug- \n", player_sheet, "\n-Dubug-\n") 
    menu_txt_1b = ("\nWelcome Back ", player_info["PlayerName"], "\n")
    for character in menu_txt_1b:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

#--------------------------------------------------------------------------------------------------- Game Functions
#print(wepn.material.items())

if (debug == True):
    for key, val in wepn.material.items():
        print("-Debug-", key, val) 

    print("")
    for key, val in wepn.rarity.items():
        print("-Debug-", key, val) 

    print("")
    for key, val in wepn.wood_stick.items():
        print("-Debug-", key, val)

    print("")

def phy_dmg_cal():
    global total_dmg
    Enchanted_multiplyer = 1
    extra_dmg_per_enhancement = 5
    Enchanted_bonus = 0
    crit = 1
    
    #print(player_info["Current Weapon"])
    #for key,val in wepn.wood_stick.items():
    #    print(key,val)
    #print(player_info["Current Weapon"]["Dmg"])

    if ((player_info["Current Weapon"]["Is Enchanted"]) == 1):
        Enchanted = True
        if Enchanted is True :
            Enchanted_bonus = 5
            Enchanted_multiplyer = 2

    val_base_dmg = (player_info["Current Weapon"]["Dmg"])

    val_enhancement_count = (player_info["Current Weapon"]["Enhanced Count"])

    rarity = (player_info["Current Weapon"]["Rarity"])
    val_legendary_dmg_bonus = (player_info["Current Weapon"]["Rarity"]["Dmg Bonus"])
    val_legendary_dmg_bonus_base = (player_info["Current Weapon"]["Rarity"]["legendary_bonus"])
    val_legendary_dmg_mult = (player_info["Current Weapon"]["Rarity"]["legendary_bonus_mult"])
    bonus_physical_crit_rate = (player_info["Bonus Physical Critical Hit Rate"])

    base_pysical_crit_rate = .0626

    total_physical_crit_rate = base_pysical_crit_rate + bonus_physical_crit_rate

    phy_crit_roll = random.random()
    if (phy_crit_roll <= total_physical_crit_rate):
        print("You Crit!")
        crit = 2

    current_wpnlvl_bonus = wepn.weapon_current_lvl

    base_dmg = val_base_dmg + val_enhancement_count - 1 + val_legendary_dmg_bonus_base

    wpnlevel = current_wpnlvl_bonus

    secondary_base = (val_base_dmg - 1 + wpnlevel)

    enhancement_bonus = val_enhancement_count * extra_dmg_per_enhancement

    bonus_dmg = (enhancement_bonus+(Enchanted_bonus) * (Enchanted_multiplyer))
    legendary_dmg_bonus = bonus_dmg + val_legendary_dmg_bonus
    total_dmg = ((base_dmg + legendary_dmg_bonus) * val_legendary_dmg_mult) * crit

    if (debug == True):
        print("-Debug- Crit:", crit)
        print("-Debug- Wpn Base Dmg:",val_base_dmg)
        print("-Debug- Enhancement Count:",val_enhancement_count)
        print("-Debug- Current Wpn Lvl:",current_wpnlvl_bonus)
        print("-Debug- Base Dmg:", base_dmg, "=", "( (Player Base Dmg)", val_base_dmg, "+ (Enhancement Count)", val_enhancement_count, "- 1 + (Legendary Base Dmg Bonus)",val_legendary_dmg_bonus_base, ")")
        print("-Debug- Wpn Level Bonus:",wpnlevel)
        print("-Debug- Secondary Base:",secondary_base, "= ( (Player Base Dmg)", val_base_dmg, "- 1 + (Wpn Level)", wpnlevel, ")")
        print("-Debug- enhancement_bonus:",enhancement_bonus, "= ( (Enhancement Count)", val_enhancement_count, "* (Dmg Per Enhancement)", extra_dmg_per_enhancement, ")")
        print("-Debug- Bonus On Base:",bonus_dmg, "= ( [ (Enhancement Bonus) +", enhancement_bonus,"(Enchanted Bonus)", Enchanted_bonus,"] * (Enchanted Multiplyer) (", Enchanted_multiplyer, ") )")
        print("-Debug- Legendary Multiplyer:", val_legendary_dmg_mult)
        print("-Debug- Bonus + Legendary Bonus:",legendary_dmg_bonus)
        print("-Debug- Total Dmg:",total_dmg, "= ( [", "(Player Base Dmg)", base_dmg, "+", "(Legendary Dmg Bonus)", legendary_dmg_bonus, "] * (Legendary Dmg Mult) (", val_legendary_dmg_mult,") )", "\n")
    print("\nBase Dmg: ", base_dmg, "\nBonus Dmg: ", bonus_dmg, "\nTotal Dmg: ", total_dmg, "\n", "-"*(len("Total Dmg: ") + len({str(total_dmg)})), sep='')

if (askstart <= 2 or askstart == 4):
    spell_mana = player_info["Spell Mana"]
    max_hp = player_info["Max Hp"]
    current_hp = max_hp

def magic_cal():
    global spell_mana
    global spell_type
    global total_magic_dmg
    global magical_armor
    global magic_heal_amount
    player_info["Class"]
    player_class = player_info["Class"]
    if (debug == True):
        print(player_class)
    if (player_class == "Bard"):
        bard_spells = True
        if (debug == True):
            print("-Debug- Bard Spells: ", bard_spells)
    elif (player_class == "Mage"):
        mage_spells = True
        if (debug == True):
            print("-Debug- Mage Spells: ", mage_spells)
    elif (player_class == "Paladin"):
        paladin_spells = True
        if (debug == True):
            print("-Debug- Paladin Spells: ", paladin_spells)
    elif (player_class == "Healer"):
        healer_spells = True
        if (debug == True):
            print("-Debug- Healer Spells: ", healer_spells)
    else:
        common_spells = True
    spell_type = int(input("Attack |1|, Defense |2|, Support |3| \n" + "> "))
    Mana_base = player_info["Mana"]
    val_magic_dmg = player_info["Magic Dmg"]
    Mana_scaling = int(Mana_base * .0625)
    Scaled_magic_dmg = Mana_scaling + val_magic_dmg
    attack_element = player_info["Elemental Affinity"]
    defensive_element = player_info["Elemental Affinity"]
    support_element = player_info["Elemental Affinity"]
    bard_spell_list = {
        "Confusion"
        "Deja Vu"
        "Allegro"
        "Cacophonous Call"
        "Delay Poison"
        "Distressing Tone"
        "Glitter Dust"
        "Foreboding Mist"
        "Oppressive Boredom"
        "Rage"
        "Confidence"
    }
    mage_spell_list = {
        ""
    }
    paladin_spell_list = {
        "Healing Hand"
        "Grace"
    }
    healer_spell_list = {
        "Empower"
        "Heal"
        ""
    }
    attack_element_bonuses = { #Attack Bonus ++ ("Fire", "Earth", "Lightning", "Dark", "Soul", "Blood")
        "Fire" : 2,
        "Aqua" : 1.25,
        "Earth" : 1.75,
        "Natural" : 1,
        "Air" : 1.25,
        "Lightning" : 1.75,
        "Light" : 1,
        "Dark" : 1.5,
        "Eclipse" : 1.15,
        "Lunar" : 1.15,
        "Soul" : 1.35,
        "Blood" : 1.666,
        }
    defensive_element_bonuses = { #Defense Bonus ++ ("Aqua", "Earth", "Air", "Light", "Soul") Defense Bonus - ("Dark")
        "Fire" : 1,
        "Aqua" : 1.5,
        "Earth" : 1.980665,
        "Natural" : 1,
        "Air" : 1.5,
        "Lightning" : 1,
        "Light" : 1.5,
        "Dark" : 0.5,
        "Eclipse" : 1,
        "Lunar" : 1,
        "Soul" : 1.5,
        "Blood" : 1,
    }
    support_element_bonuses = { #Support Bonus ++ ("Aqua", "Natural", "Air", "Lightning", "Light", "Soul", "Blood") Support Bonus + ("Eclispe", "Lunar") Support Bonus - ("Dark")
        "Fire" : {
            "Positive" : 0.5,
            "Spell Mana Cost" : -20,
        },
        "Aqua" : 1.15,
        "Earth" : 1,
        "Natural" : 1.777,
        "Air" : 1.25,
        "Lightning" : 1.75,
        "Light" : {
            "Positive" : 4,
            "Spell Mana Cost" : -5,
        },
        "Dark" : {
            "Negetive" : 0.25,
            "Spell Mana Cost" : -30,
        },
        "Eclipse" : 1.15,
        "Lunar" : 1.15,
        "Soul" : {
            "Positive" : 2,
            "Spell Mana Cost" : -7,
        },
        "Blood" : 3,
    }
    def total_magic_dmg():
        global Scaled_magic_dmg
        global player_magic_bonus_mult
        global total_magic_dmg

        bonus_magical_crit_rate = (player_info["Bonus Magical Critical Hit Rate"])
        base_magical_crit_rate = .0722
        total_magical_crit_rate = base_magical_crit_rate + bonus_magical_crit_rate
        magic_crit_roll = random.random()
        if (magic_crit_roll <= total_magical_crit_rate):
            print("You Crit!")
            crit = 2

        total_magic_dmg = Scaled_magic_dmg*player_magic_bonus_mult
        total_magic_dmg = round(total_magic_dmg * crit)
        print("\nAttack Element", attack_element)
    if (spell_type == 1):
        print("\n'You Cast An Attack Spell'")
        player_magic_bonus_mult = attack_element_bonuses.get(attack_element, 1)
        total_magic_dmg()
        spell_mana = spell_mana - 10
        if (debug == True):
            print("-Debug- Mana Base", Mana_base,"\nBase Damage", player_info["Magic Dmg"],"\nMana Scaling", Mana_scaling,"\nScaled Magic Damage", Scaled_magic_dmg, "\nPlayer Magic Bonus Multiplyer", player_magic_bonus_mult,"\nTotal Magic Damage", total_magic_dmg, "\nSpell Mana", spell_mana)
        if (debug == False):
            print("Magic Damage", total_magic_dmg, "\nRemaining Mana", spell_mana, "\n")

    elif(spell_type == 2):
        print("Defense")
        player_magic_bonus_mult = defensive_element_bonuses.get(defensive_element, 1)
        total_magic_dmg = Scaled_magic_dmg*player_magic_bonus_mult
        magical_armor = round(total_magic_dmg)
        spell_mana = spell_mana - 10
        
        if (debug == True):
            print("-Debug- Mana Base", Mana_base,"\nBase Damage", player_info["Magic Dmg"],"\nMana Scaling", Mana_scaling,"\nScaled Magic Damage", Scaled_magic_dmg, "\nPlayer Magic Bonus Multiplyer", player_magic_bonus_mult,"\nTotal Magical Armor", magical_armor, "\nSpell Mana", spell_mana,"\n")
        if (debug == False):
            print("Base Magical Armor", magical_armor, "\nRemaining Mana", spell_mana, "\n")

    elif(spell_type == 3):
        print("Support")
        def magic_heal_amount():
            global total_magic_dmg
            global Scaled_magic_dmg
            global player_magic_bonus_mult
            global magic_heal_amount
            total_magic_dmg = Scaled_magic_dmg*player_magic_bonus_mult
            magic_heal_amount = round(total_magic_dmg/2)
            print(support_element)
            for support_elements in support_element_bonuses():
                for support_elements_stats in support_element_bonuses():
                    if support_elements_stats == "Positive":
                        player_magic_bonus_mult = support_elements_stats.get["Positive"]
                        spell_mana_cost = support_elements_stats.get["Spell Mana Cost"]
                        print("POS")
                    if support_elements_stats == "Negetive":
                        player_magic_bonus_mult = support_elements_stats.get["Negetive"]
                        spell_mana_cost = support_elements_stats.get["Spell Mana Cost"]
                        print("APOS")
                    else:
                        player_magic_bonus_mult = support_element_bonuses.get(support_element, 1)
                        spell_mana_cost = 10
            magic_heal_amount()
            spell_mana = spell_mana - spell_mana_cost
        if (debug == True):
            print("-Debug- Mana Base", Mana_base,"\nBase Heal", player_info["Magic Dmg"],"\nMana Scaling", Mana_scaling,"\nScaled Magic Heal", Scaled_magic_dmg, "\nPlayer Magic Bonus Multiplyer", player_magic_bonus_mult,"\nTotal Magic Healing", magic_heal_amount, "\nSpell Mana", spell_mana,"\n")
        if (debug == False):
             print("Base Magic Heal", magic_heal_amount, "\nRemaining Mana", spell_mana, "\n")
    #if (spell_element == player_info["Elemental Affinity"]):
    #    affinity_bonus = 1.215    
    #print("((Mana * .0625)magic dmg)*elemental affinity bonus1.215")

def Inventory_combat():
    global spell_mana
    global max_hp
    global current_hp
    global armor
    inv_actiontype = int(input("Potions |1|, Items|2|, Back|3|\n" + "> "))
    if (inv_actiontype == 1):
        #current_hp = 10
        #spell_mana = 155
        hp_recovered = 10*int(player_info["Current Lvl"])
        mana_recovered = 5*int(player_info["Current Lvl"])
        if (hp_recovered >= 30):
            hp_recovered = int(hp_recovered%2)
        if (mana_recovered >= 20):
            mana_recovered = int(mana_recovered%2)
        if (debug == True):
            print("-Debug- Heal amount", hp_recovered, "\n-Debug- Mana Recovered", mana_recovered)
        print("\nUse A Potion?")
        pot_use = int(input("Yes |1| No |2|\n" + "> "))
        if (pot_use == 1):
            #player_info["Potion Count"] = int(player_info["Potion Count"]) + 1 "Add Potions"
            if (int(player_info["Potion Count"]) == 0):
                print("You Lack The Heals\n")
                pass
            elif(int(player_info["Potion Count"]) > 0):
                player_info["Potion Count"] = int(player_info["Potion Count"]) - 1
                #current_hp != current_hp > max_hp
                current_hp = current_hp+hp_recovered
                if (current_hp > max_hp):
                    if (current_hp >= max_hp):
                        print("Connot Overheal, Your Current Max Hp is", max_hp)
                        if (debug == True):
                            print("-Dubug- Current Hp", current_hp, "Max Hp", max_hp)
                        current_hp = max_hp
                        pass
                    else:
                        current_hp = max_hp
                else:
                    print("\nYou healed", hp_recovered, "Hp", "\nCurrent Hp", current_hp, "\nMax Hp", max_hp)
                #spell_mana != spell_mana > int(player_info["Mana"])
                spell_mana = spell_mana+mana_recovered
                if (spell_mana > int(player_info["Mana"])):
                    if (spell_mana >= int(player_info["Mana"])):
                        print("Connot Overload Mana, Your Current Max Mana is", int(player_info["Mana"]))
                        if (debug == True):
                            print("-Debug- Spell Mana", spell_mana)
                        spell_mana = int(player_info["Mana"])
                        pass
                    else:
                        spell_mana = int(player_info["Mana"])
                else:
                    print("\nYou Recovered", mana_recovered, "Mana", "\nCurrent Mana", spell_mana, "\nMax Mana", int(player_info["Mana"]))
                if (debug == True):
                        print("-Debug- Current Hp", current_hp, "\n-Debug- Max Hp", max_hp, "\n-Debug- Spell Mana", spell_mana, "\n-Debug- Current Max Mana", int(player_info["Mana"]))
        if (pot_use == 2):
            inv_actiontype = 3
        else:
            pass
    if (inv_actiontype == 2):
        print(player_info["Inventory"])
        pass
        combat_action()
    if (inv_actiontype >= 3):
        pass
        combat_action()

def combat_action():
    global turn_order_loop
    global actiontype
    actiontype = int(input("\n'Physical |1|, Magic |2|, Inventory |3|, Escape |4|' \n" + "> "))
    if (actiontype == 1):
        phy_dmg_cal()
    if (actiontype == 2):
        magic_cal()
    if (actiontype == 3):
        Inventory_combat()
    if (actiontype == 4):
        escape_chance = random.randint(1,10)
        if (escape_chance >= 3):
            print("You Successfully Escaped!")
            turn_order_loop = turn_order_loop + 1
            if (debug == True):
                print("-Debug- Escape Chance", escape_chance)
            quit
        elif(escape_chance <= 2):
            print("You Failed To Escape!")
            if (debug == True):
                print("-Debug- Escape Chance", escape_chance)
    if(actiontype > 4):
        actiontype = int(input("\nPhysical |1|, Magic |2|, Inventory |3|, Escape |4| \n" + "> "))

def save_game():
    with open(game_save, "w") as f:
        json.dump(player_info, f, indent=2)
        json_save_data = json.dumps(player_info, indent=2)
        if (debug == True):
            print(json_save_data)
        print("Game Saved!")

def group_enemies_by_location(location):
    grouped_enemies = {}

    for enemy_type in enem.enemies:
        for enemy_subtype in enem.enemies[enemy_type]:
            enemy_details = enem.enemies[enemy_type][enemy_subtype]
            location_type = enemy_details.get("Location Type")
            enemy_name = enemy_details.get("Name")

            if location_type and enemy_name:
                if isinstance(location_type, (tuple, list)):
                    if location not in location_type:
                        continue
                else:
                    if location != location_type:
                        continue

                if enemy_type in grouped_enemies:
                    grouped_enemies[enemy_type].append(enemy_name)
                else:
                    grouped_enemies[enemy_type] = [enemy_name]
    if debug == True:
        print("-Debug-", grouped_enemies, "\n")
    return grouped_enemies

def get_random_enemy_from_location(location):
    # Get the player's level
    player_level = player_info["Current Lvl"]

    # Group enemies by location
    enemies_in_location = group_enemies_by_location(location)

    # Create a list of enemy types, each repeated a number of times equal to its frequency
    enemy_types = []
    for enemy_type, enemy_names in enemies_in_location.items():
        for enemy_name in enemy_names:
            # Find the enemy details
            for subtype, details in enem.enemies[enemy_type].items():
                if details["Name"] == enemy_name:
                    # Check if the player's level is high enough to encounter this enemy
                    level_requirement = details.get("Level Requirement", 0)  # Default level requirement is 0 if not specified
                    if player_level < level_requirement:
                        continue
                    # Add the enemy type to the list a number of times equal to its frequency
                    frequency = details.get("Frequency", 1)  # Default frequency is 1 if not specified
                    enemy_types.extend([enemy_name]*frequency)

    # Choose a random enemy type from the list, taking frequency into account
    if enemy_types:  # Check if there are any enemy types in the list
        enemy_name = random.choice(enemy_types)

        # Retrieve the enemy details from the original enemies dictionary
        for enemy_type in enem.enemies:
            for subtype, details in enem.enemies[enemy_type].items():
                if details["Name"] == enemy_name:
                    return details

    return None  # Return None if no matching enemy was found Usage # "random_enemies_in_(*Type of Location)" = get_random_enemy_from_location("*Type of Location")

def enemy_encounter(): #Determines enemies encounter by current region/location/both
    global current_enemy
    global player_region
    global player_location
    global location_type
    encounter_types = ["Dense Forest", "Forest", "Lake/Ocean", "Island", "Isle", "Capital City", "City", "Town", "Tundra", "Grove", "Cave", "Den", "Plain/Meadow", "Fortress", "Coast", "Orchard", "Open", "Mountain", "Marsh", "River", "Valley", "Plateau", "Dungeon", "Ruin", "?"]
    #for location_type in encounter_types:
    #    encounter = encounter_types.pop(0)
    #    print("\n", encounter, "\n", "-"*len(encounter), sep='')
    #    random_enemies = get_random_enemy_from_location(encounter)
    #    print(random_enemies)
    player_region = player_info["Region"]#players current region
    player_location = player_info["Location"]#players current location
    def smeckles():
        global player_region
        global player_location
        global current_enemy
        if debug is True:
            print(player_region, player_location)
            print(loci.ca)
            print(region["Name"][player_location]["Location Type"])
        if (loci.df in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Dense Forest")
            encounter_type = "Dense Forest"
            if "Dense Forest" in enem.enemies:
                print("Ok")
        if (loci.f in region["Name"][player_location]["Location Type"]):
            print("Encoutner Type Forest")
            encounter_type = "Forest"
        if (loci.l in region["Name"][player_location]["Location Type"]):
            if debug == True:
                print("Encounter Type Lake/Ocean")
            print("Your Located By A Lake")
            encounter_type = "Lake/Ocean"
            random_enemies = get_random_enemy_from_location(encounter_type)
            current_enemy = random_enemies
            return current_enemy
        if (loci.i in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Island")
            encounter_type = "Island"
        if (loci.ile in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Isle")
            encounter_type = "Isle"
        if (loci.cc in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Capital City")
            encounter_type = "Capital City"
        if (loci.c in region["Name"][player_location]["Location Type"]):
            print("Encounter Type City")
            encounter_type = "City"
        if (loci.t in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Town")
            encounter_type = "Town"
        if (loci.tu in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Tundra")
            encounter_type = "Tundra"
        if (loci.g in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Grove")
            encounter_type = "Grove"
        if (loci.ca in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Cave")
            encounter_type = "Cave"
        if (loci.d in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Den")
            encounter_type = "Den"
        if (loci.p in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Plain/Meadow")
            encounter_type = "Plain/Meadow"
        if (loci.fo in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Fortress")
            encounter_type = "Fortress"
        if (loci.co in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Coast")
            encounter_type = "Coast"
        if (loci.oR in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Orchard")
            encounter_type = "Orchard"
        if (loci.o in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Open")
            encounter_type = "Open"
        if (loci.m in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Mountain")
            encounter_type = "Mountain"
        if (loci.mr in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Marsh")
            encounter_type = "Marsh"
        if (loci.r in region["Name"][player_location]["Location Type"]):
            print("Encounter Type River")
            encounter_type = "River"
        if (loci.v in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Valley")
            encounter_type = "Valley"
        if (loci.pl in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Plateau")
            encounter_type = "Plateau"
        if (loci.dun in region["Name"][player_location]["Location Type"]):
            print("Encounter Type Dungeon")
            encounter_type = "Dungeon"
    if (player_region == "Puregarde"):#checks players current region 
        #print("\nIn Puregarde\n")
        region = loci.RD_Puregarde
        smeckles()
    #--------------------------------------------------------------------------------------------------- Starmoor
    if (player_region == "Starmoor"):#checks players current region
        #print("\nIn Starmoor\n") 
        region = loci.RD_Starmoor
        smeckles()
    #--------------------------------------------------------------------------------------------------- Frostmord
    if (player_region == "Frostmord"):#checks players current region
        #print("\nIn Frostmord\n")
        region = loci.RD_Frostmord
        smeckles()
    #--------------------------------------------------------------------------------------------------- Shimmergarde
    if (player_region == "Shimmergarde"):#checks players current region
        #print("\nIn Shimmergarde\n")
        region = loci.RD_Shimmergarde
        smeckles()
    #--------------------------------------------------------------------------------------------------- Dimhollow
    if (player_region == "Dimhollow"):#checks players current region1
        #print("\nIn Dimhollow\n")
        region = loci.RD_Dimhollow
        smeckles()
    #--------------------------------------------------------------------------------------------------- Ebonmeadow
    if (player_region == "Ebonmeadow"):#checks players current region
        #print("\nIn Ebonmeadow\n")
        region = loci.RD_Ebonmeadow
        smeckles()
    #--------------------------------------------------------------------------------------------------- Duskgrove
    if (player_region == "Duskgrove"):#checks players current region
        #print("\nIn Duskgrove\n")
        region = loci.RD_Duskgrove
        smeckles()
    #--------------------------------------------------------------------------------------------------- Dawngrove
    if (player_region == "Dawngrove"):#checks players current region
        #print("\nIn Dawngrove\n")
        region = loci.RD_Dawngrove
        smeckles()
    #--------------------------------------------------------------------------------------------------- The Subterrane
    if (player_region == "Subterrane"):#checks players current region
        #print("\nIn The Subterrane\n")
        region = loci.RD_TheSubterrane
        smeckles()
    #--------------------------------------------------------------------------------------------------- The Subterrane Sea
    if (player_region == "The Subterrane Sea"):#checks players current region
        #print("\nIn The Subterrane Sea\n")
        region = loci.RD_TheSubterraneSea
        smeckles()
    #--------------------------------------------------------------------------------------------------- North Sea
    if (player_region == "North Sea"):#checks players current region
        #print("\nIn North Sea\n")
        region = loci.RD_SouthSea
        smeckles()
    #--------------------------------------------------------------------------------------------------- South Sea
    if (player_region == "South Sea"):#checks players current region
        #print("\nIn South Sea\n")
        region = loci.RD_SouthSea
        smeckles()
    #--------------------------------------------------------------------------------------------------- The Welkin
    if (player_region == "Welkin"):#checks players current region
        #print("\nIn Welkin\n")
        region = loci.RD_TheWelkin
        smeckles()
    else:
        pass

def get_mob_info(): #Uses function enemy_encounter to determine what enemy stats it should grab, and scales them with player
    global enemy_name
    global current_enemy
    global enemy_health
    global enemy_damage
    global enemy_magic_damage
    global enemy_magic_resistance
    global enemy_armor
    level_difference = player_info["Current Lvl"] - current_enemy["Level Requirement"]
    if level_difference >= 5:
        scale_factor = level_difference // 5
        scaled_enemy = current_enemy.copy()
        
        scaled_enemy["Health"] *= 1 + 0.1 * scale_factor
        scaled_enemy["Damage"] *= 1 + 0.1 * scale_factor
        scaled_enemy["Magic Damage"] *= 1 + 0.1 * scale_factor
        #Other Stats
        
        current_enemy = scaled_enemy
        print("Current Enemy", current_enemy)
    enemy_name = current_enemy["Name"]
    enemy_health = current_enemy["Health"]
    enemy_damage = current_enemy["Damage"]
    enemy_magic_damage = current_enemy["Magic Damage"]
    enemy_magic_resistance = current_enemy["Magic Resistance"]
    enemy_armor = current_enemy["Armor"]
    print("You Encountered A" ,enemy_name)

def combat_rewards():
    stat_total = (current_enemy["Health"] + current_enemy["Damage"] + current_enemy["Magic Damage"] + current_enemy["Magic Resistance"] + current_enemy["Armor"])
    xp_reward = stat_total
    print(xp_reward, "XP Was Earned")

def enemy_action(): #Enemies possable actions and determines how much dmg they deal to the player
    global current_enemy
    global current_hp
    global enemy_health
    global enemy_damage
    global armor
    base_armor = player_info["Armor"]
    armor = base_armor #+ magical_armor
    total_enemy_damage = round(enemy_damage+1-((armor)*.5))
    if(total_enemy_damage <= 0):
        total_enemy_damage = 1
    current_hp = (current_hp - total_enemy_damage)
    #print(total_enemy_damage)
    if(current_hp < 0):
        current_hp = 0
    print("The Enemy Takes Action!", "\nThey Dealt", total_enemy_damage, "Damage!", "\nYou Have", current_hp, "Health Remaining")

def turn_effects(): #checks for player/enemy passive/effects that take place between player and enemy turns
    global current_hp
    global max_hp
    global current_enemy
    global enemy_health
    global enemy_damage
    global armor
    base_armor = player_info["Armor"]
    if (player_info["Passive Abilities"] == True):
        if (player_info["Passive Abilities"].has_key("Healing")):
            current_hp = ((current_hp + 10) <= max_hp)
            if (debug == True):
                print("-Debug- Current Hp:", current_hp)
        if (player_info["Passive Abilities"].has_key("Fortify")):
            armor = round((base_armor + 1.75))
            if (debug == True):
                print("-Debug- Armor:", armor)

def Turn_Order(): #The order in which normal fights take place
    global turn_order_loop
    global current_enemy
    global current_hp
    global max_hp
    global armor
    global current_enemy
    global enemy_health
    global enemy_damage
    global actiontype
    global total_dmg
    global total_magic_dmg
    global magical_armor
    armor = player_info["Armor"]
    turn_order_loop = 1
    while(turn_order_loop < 2):
        print("\nYou Ready An Action")
        combat_action()
        #print("Order Loop Value", turn_order_loop)
        if (actiontype == 1):
            enemy_health = (enemy_health - total_dmg)
            print("")
            if (enemy_health < 0):
                enemy_health = 0
            print(enemy_name, "Hp", enemy_health, "\n")
            if (enemy_health <= 0):
                kill_flavor_text = ["Has Been Defeated!", "Has Been Slain!", "Has Been Killed!", "Was Destroyed!", "Perished", "Died!"]
                print(enemy_name, random.choice(kill_flavor_text))
                combat_rewards()
                turn_order_loop = turn_order_loop + 2
            elif (current_hp <= 0):
                Death_Menu()
                turn_order_loop = turn_order_loop + 2
        if (actiontype == 2):
            if (spell_type == 1):
                enemy_health = (enemy_health - total_magic_dmg)
                if (enemy_health < 0):
                    enemy_health = 0
                print("Enemy Hp: ", enemy_health)
                if (enemy_health <= 0):
                    print(enemy_name,"Has Been Defeated")
                    combat_rewards()
                    turn_order_loop = turn_order_loop + 2
                elif (current_hp <= 0):
                    print(player_info["PlayerName"],"Has Fallen")
                    turn_order_loop = turn_order_loop + 2
            if (spell_type == 2):
                magical_armor = magical_armor
                print("You Gained", armor, "More Armor\n")
            if (spell_type == 3):
                
                print(enemy_name,"Enemy Hp: ", enemy_health, "\nYour Hp", current_hp)
        if (actiontype == 3):
            ""
        if (actiontype == 4):
            ""
        
        if(turn_order_loop <= 2):
            #print("Order Loop Value", turn_order_loop)
            turn_effects()
            enemy_action()
            if (current_hp <= 0):
                Death_Menu()
                turn_order_loop = turn_order_loop + 2
        elif(turn_order_loop == 2):
            pass

def Death_Menu(): #* Incomplete
    print(player_info["PlayerName"],"Has Fallen")
    print(" _____ ")
    print("|     |", "| |",  "|--|",  "|  |", " |-> ", "-", "|--","|-> ") 
    print("|() ()|", " | ",  "|  |",  "|  |", " |  |", "|", "|- ","|  |")
    print(" ^> <^ ", " | ",  "|--|",  "|--|", " |-> ", "|", "|--","|-> ") 
    print("  |||  ")

def Combat_Order():
    player_action_complete = False
    player_enemy_combat = True
    while player_enemy_combat == True:
        print("\n You Ready Yourself")
        combat_action()
        if debug == True:
            print("Combat Order Loop", player_action_complete)
        if (actiontype == 1):
            enemy_health = (enemy_health - total_dmg)
            print("")
            if (enemy_health < 0):
                enemy_health = 0
            print(enemy_name, enemy_health)
            if (enemy_health <= 0):
                print(enemy_name,"Has Been Defeated")
                player_action_complete = True
            elif (current_hp <= 0 ):
                Death_Menu()
                player_action_complete = True
        if (actiontype == 2):
            if (spell_type == 1):
                enemy_health = (enemy_health - total_magic_dmg)
                if (enemy_health < 0):
                    enemy_health = 0
                print("Enemy Hp: ", enemy_health)
                if (enemy_health <= 0):
                    print(enemy_name,"Has Been Defeated")
                    player_action_complete = True
                elif (current_hp <= 0):
                    print(player_info["PlayerName"],"Has Fallen")
                    player_action_complete = True
                    player_enemy_combat = False
            if (spell_type == 2):
                magical_armor = magical_armor
                print("You Gained", armor, "More Armor\n")
            if (spell_type == 3):
                print(enemy_name,"Enemy Hp: ", enemy_health, "\nYour Hp", current_hp)
        if (actiontype == 3):
            ""
        if (actiontype == 4):
            ""
        
        if(player_enemy_combat == True):
            #print("Order Loop Value", turn_order_loop)
            turn_effects()
            enemy_action()
            if (current_hp <= 0):
                print(player_info["PlayerName"],"Has Fallen")
                Death_Menu()
                player_action_complete = True
        elif(turn_order_loop == 2):
            pass

#Insert Rest Function Here

def Inventory_pause():
    global spell_mana
    global max_hp
    global current_hp
    global armor
    inv_actiontype = int(input("Potions |1|, Items|2|, Back|3|\n" + "> "))
    if (inv_actiontype == 1):
        #current_hp = 10
        #spell_mana = 155
        hp_recovered = 10*int(player_info["Current Lvl"])
        mana_recovered = 5*int(player_info["Current Lvl"])
        if (hp_recovered >= 30):
            hp_recovered = int(hp_recovered%2)
        if (mana_recovered >= 20):
            mana_recovered = int(mana_recovered%2)
        if (debug == True):
            print("-Debug- Heal amount", hp_recovered, "\n-Debug- Mana Recovered", mana_recovered)
        print("\nUse A Potion?")
        pot_use = int(input("Yes |1| No |2|\n" + "> "))
        if (pot_use == 1):
            #player_info["Potion Count"] = int(player_info["Potion Count"]) + 1 "Add Potions"
            if (int(player_info["Potion Count"]) == 0):
                print("You Lack The Heals\n")
                pass
            elif(int(player_info["Potion Count"]) > 0):
                player_info["Potion Count"] = int(player_info["Potion Count"]) - 1
                #current_hp != current_hp > max_hp
                current_hp = current_hp+hp_recovered
                if (current_hp > max_hp):
                    if (current_hp >= max_hp):
                        print("Connot Overheal, Your Current Max Hp is", max_hp)
                        if (debug == True):
                            print("-Dubug- Current Hp", current_hp, "Max Hp", max_hp)
                        current_hp = max_hp
                        pass
                    else:
                        current_hp = max_hp
                else:
                    print("\nYou healed", hp_recovered, "Hp", "\nCurrent Hp", current_hp, "\nMax Hp", max_hp)
                #spell_mana != spell_mana > int(player_info["Mana"])
                spell_mana = spell_mana+mana_recovered
                if (spell_mana > int(player_info["Mana"])):
                    if (spell_mana >= int(player_info["Mana"])):
                        print("Connot Overload Mana, Your Current Max Mana is", int(player_info["Mana"]))
                        if (debug == True):
                            print("-Debug- Spell Mana", spell_mana)
                        spell_mana = int(player_info["Mana"])
                        pass
                    else:
                        spell_mana = int(player_info["Mana"])
                else:
                    print("\nYou Recovered", mana_recovered, "Mana", "\nCurrent Mana", spell_mana, "\nMax Mana", int(player_info["Mana"]))
                if (debug == True):
                        print("-Debug- Current Hp", current_hp, "\n-Debug- Max Hp", max_hp, "\n-Debug- Spell Mana", spell_mana, "\n-Debug- Current Max Mana", int(player_info["Mana"]))
        if (pot_use == 2):
            inv_actiontype = 3
        else:
            pass
    if (inv_actiontype == 2):
        print(player_info["Inventory"])
    if (inv_actiontype >= 3):
        pass

def Innermission():
    hold = 0
    while (hold != 1):
        intermission_act = int(input("Quick Inventory |1|, Save |2|, Inventory |3|, Quit |4|\n" + "> "))
        if (intermission_act == 1):
            print(player_info["Inventory"])
        if (intermission_act == 2):
            save_game()
        if (intermission_act == 3):
            Inventory_pause()
        if (intermission_act == 4):
            hold = hold + 1
            quit

#Travel Function Here

#--------------------------------------------------------------------------------------------------- Gameplay
def hai():
    print("Hai Hai")

if (askstart <= 2 or askstart == 4):
    enemy_encounter()
    get_mob_info()
    Turn_Order()

#SAVE----
#with open(game_save, "w") as f:
#    json.dump(player_info, f, indent=2)
#    json_save_data = json.dumps(player_info, indent=2)
#    print(json_save_data)

print("\n'End of Script'")