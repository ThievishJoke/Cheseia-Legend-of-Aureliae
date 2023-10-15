import json
from msvcrt import kbhit
from typing import Literal

innkeepers = {
    "Location" : { #Towns
        "Springbrook" : { #Puregarde
            "Innkeeper" : {
                "Name" : "Koena",
                "Gender" : "Female",
            },
        },
        "Maplepeak" : {
            "Innkeeper" : {
                "Name" : "Miku",
                "Gender" : "Female",
            },
        },
        "Lita" : {
            "Innkeeper" : {
                "Name" : "Sachi",
                "Gender" : "Female",
            },
        },
        "Sarlès" : { #Starmoor
            "Innkeeper" : {
                "Name" : "Yukino",
                "Gender" : "Female",
            },
        },
        "Tricmery" : {
            "Innkeeper" : {
                "Name" : "Juri",
                "Gender" : "Female",
            },
        },
        "Sakurawood" : { #Frostmord
            "Innkeeper" : {
                "Name" : "Erika",
                "Gender" : "Female",
            },
        },
        "Sroupfast" : {
            "Innkeeper" : {
                "Name" : "Ao",
                "Gender" : "Female",
            },
        },
        "Ushashire" : {
            "Innkeeper" : {
                "Name" : "Ami",
                "Gender" : "Female",
            },
        },
        "Oredale" : {
            "Innkeeper" : {
                "Name" : "Fusami",
                "Gender" : "Female",
            },
        },
        "Springarde" : { #Shimmergarde
            "Innkeeper" : {
                "Name" : "Asuka",
                "Gender" : "Female",
            },
        },
        "Ayraka" : {
            "Innkeeper" : {
                "Name" : "Misato",
                "Gender" : "Female",
            },
        },
        "Grimmere" : {
            "Innkeeper" : {
                "Name" : "Anika",
                "Gender" : "Female",
            },
        },
        "Yloria" : {
            "Innkeeper" : {
                "Name" : "Annemari",
                "Gender" : "Female",
            },
        },
        "Klosa" : { #000
            "Innkeeper" : {
                "Name" : "Katsuko",
                "Gender" : "Female",
            },
        },
        "Jeim" : {
            "Innkeeper" : {
                "Name" : "Maki",
                "Gender" : "Female",
            },
        },
        "Zaidale" : {
            "Innkeeper" : {
                "Name" : "Mayumi",
                "Gender" : "Female",
            },
        },
        "Mutetide" : { #Dimhollow
            "Innkeeper" : {
                "Name" : "Midori",
                "Gender" : "Female",
            },
        },
        "Shadowbourne" : {
            "Innkeeper" : {
                "Name" : "Misa",
                "Gender" : "Female",
            },
        },
        "Flaset" : { #Ebonmeadow
            "Innkeeper" : {
                "Name" : "Remi",
                "Gender" : "Female",
            },
        },
        "Mossmaund" : {
            "Innkeeper" : {
                "Name" : "Rieko",
                "Gender" : "Female",
            },
        },
        "Adenaham" : {
            "Innkeeper" : {
                "Name" : "Bertwalda",
                "Gender" : "Female",
            },
        },
        "Asheigh" : {
            "Innkeeper" : {
                "Name" : "Brigitte",
                "Gender" : "Female",
            },
        },
        "Vinmur" : { #Duskgrove
            "Innkeeper" : {
                "Name" : "Crescentia",
                "Gender" : "Female",
            },
        },
        "Iyrovine" : {
            "Innkeeper" : {
                "Name" : "Dina",
                "Gender" : "Female",
            },
        },
        "Tassis" : { #Dawngove
            "Innkeeper" : {
                "Name" : "Linus",
                "Gender" : "Male",
            },
        },
        "Besanluire" : {
            "Innkeeper" : {
                "Name" : "August",
                "Gender" : "Male",
            },
        },
        "Silvermount" : {
            "Innkeeper" : {
                "Name" : "Herwarth",
                "Gender" : "Male",
            },
        },
    }
}
#        "Maplepeak" : {
#
#        },
#        "Maplepeak" : {
#
#        },
#        "Maplepeak" : {
#
#        },
#        "Maplepeak" : {
#
#        },
#        "Maplepeak" : {
#        },

#debug_check
def save():
    global player_info
    with open("save.json", "r") as f:
        player_info = json.load(f)
        player_sheet = json.dumps(player_info, indent=2)
    with open("save.json", "w") as f:
        json.dump(player_info, f, indent=2)
        json_save_data = json.dumps(player_info, indent=2)

    with open("savestate.json", "r") as f:
        save_state = json.load(f)
        debug = json.dumps(save_state, indent=2)#Save State
        #print(debug)
        if (save_state["Debug"] == True):
            print(debug)
        if (save_state["existing_save"] == False):
            with open("innkeepers.json", "w") as k:
                json.dump(innkeepers, k, indent=2)
                innmaid = json.dumps(innkeepers, indent=2)
            if (save_state["Debug"] == True):
                print(innmaid)

def inn_actions():
    save()
    global player_info
    global innkeepers
    with open("save.json", "r") as f:
        player_info = json.load(f)
        player_sheet = json.dumps(player_info, indent=2)#Player Sheet
        #print(player_sheet)
    
    #if(player_info["Location"] == "Springbrook"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Springbrook"])
    
    #if(player_info["Location"] == "Maplepeak"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Maplepeak"])
    
    #if(player_info["Location"] == "Lita"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Lita"])
    
    #if(player_info["Location"] == "Sarlès"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Sarlès"])
    
    #if(player_info["Location"] == "Tricmery"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Tricmery"])
    
    #if(player_info["Location"] == "Sakurawood"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Sakurawood"])
    
    #if(player_info["Location"] == "Sroupfast"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Sroupfast"])
    
    #if(player_info["Location"] == "Ushashire"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Ushashire"])
    
    #if(player_info["Location"] == "Oredale"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Oredale"])
    
    #if(player_info["Location"] == "Springarde"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Springarde"])
    
    #if(player_info["Location"] == "Ayraka"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Ayraka"])
    
    #if(player_info["Location"] == "Grimmere"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Grimmere"])
    
    #if(player_info["Location"] == "Yloria"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Yloria"])
    
    #if(player_info["Location"] == "Klosa"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Klosa"])
    
    #if(player_info["Location"] == "Jeim"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Jeim"])
    
    #if(player_info["Location"] == "Zaidale"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Zaidale"])
    
    #if(player_info["Location"] == "Mutetide"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Mutetide"])
    
    #if(player_info["Location"] == "Shadowbourne"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Shadowbourne"])
    
    #if(player_info["Location"] == "Flaset"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Flaset"])
    
    #if(player_info["Location"] == "Mossmaund"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Mossmaund"])
    
    #if(player_info["Location"] == "Adenaham"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Adenaham"])
    
    #if(player_info["Location"] == "Asheigh"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Asheigh"])
    
    #if(player_info["Location"] == "Vinmur"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Vinmur"])
    
    #if(player_info["Location"] == "Iyrovine"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Iyrovine"])
    
    #if(player_info["Location"] == "Tassis"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Tassis"])
    
    #if(player_info["Location"] == "Besanluire"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Besanluire"])
    
    #if(player_info["Location"] == "Silvermount"):
    #    print(player_info["Location"])
    #    print(innkeepers["Location"]["Silvermount"])
    

    print("Would You Like To Spend The Night At The", player_info["Location"], "Inn\n")
    inn_rest = int(input("Yes |1| No |2| \n"))
    if (inn_rest == 1):
        if (int(player_info["Aureliaen Gold Coins"]) < 10):
            pass
        if (int(player_info["Aureliaen Gold Coins"]) >= 10):
            if (int(player_info["Hp"]) != int(player_info["Max Hp"])):
                player_info["Aureliaen Gold Coins"] = int(player_info["Aureliaen Gold Coins"] - 10)
                print("Remaining Coins", int(player_info["Aureliaen Gold Coins"]))
                print("You Get Peaceful Sleep, And Your Sleep Has Fully Restored Your Hp")
                player_info["Hp"] = player_info["Max Hp"]
                with open("save.json", "w") as f:
                    json.dump(player_info, f, indent=2)
                    json_save_data = json.dumps(player_info, indent=2)
            else:
                print("You Already Feel Well")
                pass
    if (inn_rest == 2):
        pass

inn_actions()

#Springbrook        #Springbrook
#Maplepeak          #Maplepeak
#Lita               #Lita
#Sarlès             #Sarlès
#Tricmery           #Tricmery
#Sakurawood         #Sakurawood
#Sroupfast          #Sroupfast
#Ushashire          #Ushashire
#Oredale            #Oredale
#Springarde         #Springarde
#Ayraka             #Ayraka
#Grimmere           #Grimmere
#Yloria             #Yloria
#Klosa              #Klosa
#Jeim               #Jeim
#Zaidale            #Zaidale
#Mutetide           #Mutetide
#Shadowbourne       #Shadowbourne
#Flaset             #Flaset
#Mossmaund          #Mossmaund
#Adenaham           #Adenaham
#Asheigh            #Asheigh
#Vinmur             #Vinmur
#Iyrovine           #Iyrovine
#Tassis             #Tassis
#Besanluire         #Besanluire
#Silvermount        #Silvermount


