
#NOTES:
#- Cords Are Not Done

#--------------------------------------------------------------------------------------------------- Debug Check
import json
import pathlib

savestate = "savestate.json"
savestate_path = savestate if pathlib.Path.cwd() else None
game_save = "save.json"
game_save_path = game_save if pathlib.Path.cwd() else None

with open(savestate_path, "r") as f:
    Aureliae_savestate_load = json.load(f)
    AureliaeLore = json.dumps(Aureliae_savestate_load, indent=2)#Lore Sheet
    if ((Aureliae_savestate_load["Debug"]) == True):
        debug = True
    else:
        debug = False
if (debug == True):
    print(Aureliae_savestate_load["Debug"])
#--------------------------------------------------------------------------------------------------- Location Types

df = " Dense Forest"
f = " Forest"
l = " Lake/Ocean"
i = " Island"
ile = " Isle"
cc = " Capital City"
c = " City"
t = " Town"
tu = " Tundra"
g = " Grove"
ca = " Cave"
d = " Den"
p = " Plain/Meadow"
fo = " Fortress"
co = " Coast"
oR = " Orchard"
o = " Open"
m = " Mountain"
mr = " Marsh"
r = " River"
v = " Valley"
pl = " Plateau"
dun = " Dungeon"
ru = " Ruin"
q = " ?"
#--------------------------------------------------------------------------------------------------- Regions
Regions = ["Puregarde", "Starmoor", "Frostmord", "Shimmergarde", "Dimhollow", "Ebonmeadow", "Duskgrove", "Dawngrove", "The Subterrane", "The Subterrane Sea", "North Sea", "South Sea", "The Welkin"]
#--------------------------------------------------------------------------------------------------- Regional Locations

#--------------------------------------------------------------------------------------------------- Puregarde * (Needs additional dungeon locations/info)
R_Puregarde = [("Loch Cudgami",(l)), ("Springbrook",(cc)), ("Maplepeak",(t)), ("Grassreach",(p)), ("Pureland",(p)), ("Lita",(t)), ("Vuby",(d))]
#Plains >()
#--------------------------------------------------------------------------------------------------- Starmoor * (Needs additional dungeon locations/info)
R_Starmoor = [("Auriville",(cc)), ("Sarlès",(v+t)), ("Rosevalle",v), ("Inashull",(d)), ("Ichoset",(v+ca)), ("Shosa",(v+c)), ("Sudense",(f)), ("Sudense City",(m+df+c)), ("Basinmore",(fo)), ("Sunpeak",(m+fo)),
("Akhora",(pl)), ("Tricmery",(pl+t)), ("Valenzon",(ca)), ("Smoothgrave",(pl+l)), ("Epadena Forest",(df)), ("Epadena Ruins",(df+ru)), ("Ocolis",(r))]
#Mountainous Valley >()
#--------------------------------------------------------------------------------------------------- Frostmord * (Needs additional dungeon locations/info)
R_Frostmord = ["Snowbay"+(co), ("Frostmeadow",(p+tu)), "Sakurawood"+(t), ("Sroupfast",(ca+t)), "Icereach"+(o), "Ushashire"+(t), "Kiangend"+(c), "Frostpass"+(tu),
("Frostcross",(f+tu)), ("Frosthallow",(f+tu)), "Frostgate"+(r), "Lagooncall"+(l), "Oredale"+(t), ("Roimont",(fo+tu))]
#Tundra >()
#--------------------------------------------------------------------------------------------------- Shimmergarde * (Needs additional dungeon locations/info)
R_Shimmergarde = ["Westide"+(c), "Clalimar"+(ca), "Slarc"+(fo), "Silkmere"+(g), "Springarde"+(t), "Elderforest"+(f), "Steelshear"+(m), "Ayraka"+(ca+t),
"Magehost"+(ca), "Lrimmere"+(i+t), "Tringate"+(r), "Vluxstin"+(v), "Atheledo"+(pl), "Yloria"+(t), "Klosa"+(t), "Glouis"+(g), "Remmont"+(p), "Jeim"+(df+t), "Zaidale"+(f+t)]
#Forested Plateau >()
#--------------------------------------------------------------------------------------------------- Dimhollow * (Needs additional dungeon locations/info)
R_Dimhollow = ["Bleakwood"+(df), "Mutetide"+(f+t), "Darkfront"+(g), "Spearlost"+(ca), "Shroudmire"+(mr+co), "Ghostpass"+(v+ca), "Shadowbourne"+(t), "Nightmire"+(mr+ca), "Bleakgrave"+(fo), "Ekloit"+(mr+c) ]
#Coastal Marsh/Swamp >()
#--------------------------------------------------------------------------------------------------- Ebonmeadow * (Needs additional dungeon locations/info)
R_Ebonmeadow = ["Kliachester"+(p+fo), "Kilpond"+(l), "Kilstall"+(r), "Demonhall"+(p+d), "Deadburn"+(o+p), "Bonegrove"+(f+g), "Flaset"+(p+t), "Mossmaund"+(r+t), "Drord"+(r+l+c), "Adenaham"+(t), "Asheigh"+(f+t) ]
#Meadow/lake/river/forest >()
#--------------------------------------------------------------------------------------------------- Duskgrove * (Needs additional dungeon locations/info)
R_Duskgrove = ["Killhollow"+(d), "Vinmur"+(t), "Lakeside"+(l+c), "Eastborough"+(df+d), "Clalles"+(c), "Thornmeadow"+(p), "Cursegate"+(fo), "Iyrovine"+(t) ]
#Grove/DenseForest/Dark/Lake/Dungeon >()
#--------------------------------------------------------------------------------------------------- Dawngrove * (Needs additional dungeon locations/info)
R_Dawngrove = ["Tassis"+(t), "Sunhollow"+(d), "Besanluire"+(t), "Silvermount"+(df+t), "Qaxtin"+(c), "Qrokving"+(l+dun), "Tradespell"+(df+dun), "Bridegalley"+(l+c)]
#Grove/DenseForest/Light/Lake/Coastal/Dungeon >()
#--------------------------------------------------------------------------------------------------- The Subterrane (Needs additional dungeon locations/info/location discriptors)
R_The_Subterrane = ["Crystalshear", "Lovlimar", "Midkeep", "Uwruorith", "Galo's Bridge", "Draguiseau", "Dragonborough", "Dusthollow", "Ordville", "Spirithorn", "Deeprest" ]
#Undergound/Nether Realm/Dungeon >
#--------------------------------------------------------------------------------------------------- The Subterrane Sea (Needs additional dungeon locations/info)
R_The_Subterrane_Sea = ["",]
#Underground Sea/Nether Realm Sea/Dungeon >
#--------------------------------------------------------------------------------------------------- North Sea (Needs additional dungeon locations/info)
R_North_Sea = ["Shellcrest"+(i+c), "Demongulf"+(i+dun), "Smallwater"+(i), "Smallpost"+(i+t), "Zuron"+(i), "Ekhoit"+(i), "Arcdiff"+(ile), "Huvine"+(i), "Adamore"+(i+fo)]
#Ocean >
#--------------------------------------------------------------------------------------------------- South Sea (Needs additional dungeon locations/info)
R_South_Sea = ["Wildtide", "Stormcoast", "Dragonwharf", "Arrowbreach", "Wego", "Cragcoast", "Brinevale", "Ansmore" ]
#Ocean >
#--------------------------------------------------------------------------------------------------- The Welkin * (Needs additional dungeon locations/info)
R_The_Welkin = ["Levatoise"+(i+c), "Plailliers"+(l), "Eaglerest"+(i+t), "Angeo"+(i+fo+dun), "Ulphia"+(ca+dun), "Isonrith"+(l+dun), "Kredo"+(ile), "Uyoxedo"+(i+t), "Cosmic Anomaly"+(q)]
#Sky Realm >
#-------------------------------------------------------------------------------------------------- Dictionaries
SubR = ''
World_Locations = {
    "Regions": {
    "Names" : {
        "Puregarde" : {
            "contains_cc" : True,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "Starmoor" : {
            "contains_cc" : True,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "Frostmord" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "Shimmergarde" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "Dimhollow" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "Ebonmeadow" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "Duskgrove" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "Dawngrove" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "The Subterrane" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "The Subterrane Sea" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "North Sea" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "South Sea" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
        "The Welkin" : {
            "contains_cc" : False,
            "contains_dun" : True,
            "Subregions" : {
            }
        },
    }
    }
}
'''print(World_Locations)
'''
def nested_dict_values_iterator(dict_obj):
    for value in dict_obj.values():
        if isinstance(value,dict):
            for v in nested_dict_values_iterator(value):
                yield v
        else:
            yield value
'''
for value in nested_dict_values_iterator(World_Locations) :
    print(value)'''

'''def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(multiplier) / multiplier
round_up()'''

Regional_Info = []
Regions2 = Regions.copy()
if (debug == True):
    print(Regions2)
for le in Regions2:
    if (debug == True):
        print(le, "\n^ Items in Regions2")
    Regions2.pop(0)
    if (debug == True):
        print(Regions2, "\n^ Regions2")
    Regional_Info.append(le)
    x = len(Regional_Info)
    if (debug == True):
        print("The Length of Regional_info is: ", x)
        print(Regional_Info, "\n^ Regional Info---")
        print(Regional_Info, "\n^ Regional_Info")


'''for l_id,value in enumerate(nested_dict_values_iterator(World_Locations), start=2):
    if (l_id >= 1):
        l_id = l_id//2
    print(Regional_Info,"\n", l_id, "\n", value)'''

print('')

'''for x,item in World_Locations["Regions"]["Names"]["Subregions"]:
    print(value)'''
#--------------------------------------------------------------------------------------------------- Puregarde
RD_Puregarde = {
    "Name" : {
    "Loch Cudgami" : {
        "Name" : "Loch Cudgami",
        "ID" : "1",
        "Location Type" : l,
        "Region" : "Puregarde",
        "Cords" : (-2,10),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Springbrook" : {
        "Name" : "Springbrook",
        "ID" : "2",
        "Location Type" : cc,
        "Region" : "Puregarde",
        "Cords" : (2,13),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Maplepeak" : {
        "Name" : "Maplepeak",
        "ID" : "3",
        "Location Type" : t,
        "Region" : "Puregarde",
        "Cords" : (0,4),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Grassreach" : {
        "Name" : "Grassreach",
        "ID" : "4",
        "Location Type" : p,
        "Region" : "Puregarde",
        "Cords" : (5,10),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Springbrook" : {
        "Name" : "Springbrook",
        "ID" : "5",
        "Location Type" : t,
        "Region" : "Puregarde",
        "Cords" : (6,10),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Lita" : {
        "Name" : "Lita",
        "ID" : "6",
        "Location Type" : t,
        "Region" : "Puregarde",
        "Cords" : (-12,26),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Vuby" : {
        "Name" : "Vuby",
        "ID" : "7",
        "Location Type" : d,
        "Region" : "Puregarde",
        "Cords" : (-6,4),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    }
}


#--------------------------------------------------------------------------------------------------- Starmoor
RD_Starmoor = {
    "Name" : {
    "Auriville" : {
        "Name" : "Auriville",
        "ID" : "1",
        "Location Type" : cc,
        "Region" : "Starmoor",
        "Cords" : [0,0],
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Sarlès" : {
        "Name" : "Sarlès",
        "ID" : "2",
        "Location Type" : (v, t),
        "Region" : "Starmoor",
        "Cords" : [0.75,2.5],
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Rosevalle" : {
        "Name" : "Rosevalle",
        "ID" : "3",
        "Location Type" : v,
        "Region" : "Starmoor",
        "Cords" : [3,-1],
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Inashull" : {
        "Name" : "Inashull",
        "ID" : "4",
        "Location Type" : d,
        "Region" : "Starmoor",
        "Cords" : [2, -2],
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Ichoset" : {
        "Name" : "Ichoset",
        "ID" : "5",
        "Location Type" : (v, ca),
        "Region" : "Starmoor",
        "Cords" : [2,0.5],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Shosa" : {
        "Name" : "Shosa",
        "ID" : "6",
        "Location Type" : (v, c),
        "Region" : "Starmoor",
        "Cords" : [4,-4],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Sudense" : {
        "Name" : "Sudense",
        "ID" : "7",
        "Location Type" : f,
        "Region" : "Starmoor",
        "Cords" : [4,3.25],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Sudense City" : {
        "Name" : "Sudense",
        "ID" : "7",
        "Location Type" : (m, df, c),
        "Region" : "Starmoor",
        "Cords" : [4,3.25],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Basinmore" : {
        "Name" : "Basinmore",
        "ID" : "8",
        "Location Type" : fo,
        "Region" : "Starmoor",
        "Cords" : [-1,-1.75],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Sunpeak" : {
        "Name" : "Sunpeak",
        "ID" : "9",
        "Location Type" : (m, fo),
        "Region" : "Starmoor",
        "Cords" : [4,-2.5],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Akhora" : {
        "Name" : "Akhora",
        "ID" : "10",
        "Location Type" : pl,
        "Region" : "Starmoor",
        "Cords" : [10.5,-.75],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Tricmery" : {
        "Name" : "Tricmery",
        "ID" : "11",
        "Location Type" : (pl, t),
        "Region" : "Starmoor",
        "Cords" : [11.5,-2],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Valenzon" : {
        "Name" : "Valenzon",
        "ID" : "12",
        "Location Type" : ca,
        "Region" : "Starmoor",
        "Cords" : [-15,-3.75],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Smoothgrave" : {
        "Name" : "Smoothgrave",
        "ID" : "13",
        "Location Type" : (pl, l),
        "Region" : "Starmoor",
        "Cords" : [10.75,-1.95],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Epadena Forest" : {
        "Name" : "Epadena Forest",
        "ID" : "14a",
        "Location Type" : df,
        "Region" : "Starmoor",
        "Cords" : [-8.75,1],
        "Temp War" : False,
        "Temp Cold" : False
    },
    "Epadena Ruins" : {
        "Name" : "Epadena Ruins",
        "ID" : "14b",
        "Location Type" : (df, ru),
        "Region" : "Starmoor",
        "Cords" : [-9,1],
        "Temp War" : False,
        "Temp Cold" : True,
    },
    "Ocolis" : {
        "Name" : "Ocolis",
        "ID" : "15",
        "Location Type" : r,
        "Region" : "Starmoor",
        "Cords" : [1,0],
        "Temp War" : False,
        "Temp Cold" : False
    },
    }
}

#--------------------------------------------------------------------------------------------------- Frostmord
RD_Frostmord = {
    "Name" : {
    "Snowbay" : {
        "Name" : "Snowbay",
        "ID" : "1",
        "Location Type" : co,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Frostmeadow" : {
        "Name" : "Frostmeadow",
        "ID" : "2",
        "Location Type" : p,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Sakurawood" : {
        "Name" : "Sakurawood",
        "ID" : "3",
        "Location Type" : t,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Sroupfast" : {
        "Name" : "Sroupfast",
        "ID" : "4",
        "Location Type" : ca+t,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Icereach" : {
        "Name" : "Icereach",
        "ID" : "5",
        "Location Type" : o,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Ushashire" : {
        "Name" : "Ushashire",
        "ID" : "6",
        "Location Type" : t,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Kiangend" : {
        "Name" : "Kiangend",
        "ID" : "7",
        "Location Type" : c,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Frostpass" : {
        "Name" : "Frostpass",
        "ID" : "8",
        "Location Type" : tu,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Frostcross" : {
        "Name" : "Frostcross",
        "ID" : "9",
        "Location Type" : f,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Frosthallow" : {
        "Name" : "Frosthallow",
        "ID" : "10",
        "Location Type" : f,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Frostgate" : {
        "Name" : "Frostgate",
        "ID" : "11",
        "Location Type" : r,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Lagooncall" : {
        "Name" : "Lagooncall",
        "ID" : "12",
        "Location Type" : l,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Oredale" : {
        "Name" : "Oredale",
        "ID" : "13",
        "Location Type" : t,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Roimont" : {
        "Name" : "Roimont",
        "ID" : "14",
        "Location Type" : fo,
        "Region" : "Frostmord",
        "Cords" : (0,0),
        "Temp War" : False,
        "Temp Cold" : True
    }
    }
}

#--------------------------------------------------------------------------------------------------- Shimmergarde
RD_Shimmergarde = {
    "Name" : {
    "Westide" : {
        "Name" : "Westide",
        "ID" : "1",
        "Location Type" : c,
        "Region" : "Shimmergarde",
        "Cords" : (13,-4),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Clalimar" : {
        "Name" : "Clalimar",
        "ID" : "2",
        "Location Type" : ca,
        "Region" : "Shimmergarde",
        "Cords" : (6,-3.5),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Slarc" : {
        "Name" : "Slarc",
        "ID" : "3",
        "Location Type" : fo,
        "Region" : "Shimmergarde",
        "Cords" : (7,-6.75),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Silkmere" : {
        "Name" : "Silkmere",
        "ID" : "4",
        "Location Type" : g,
        "Region" : "Shimmergarde",
        "Cords" : (9.5,-5),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Springarde" : {
        "Name" : "Springarde",
        "ID" : "5",
        "Location Type" : t,
        "Region" : "Shimmergarde",
        "Cords" : (11.75,-8.25),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Elderforest" : {
        "Name" : "Elderforest",
        "ID" : "6",
        "Location Type" : df,
        "Region" : "Shimmergarde",
        "Cords" : (10,-7),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Steelshear" : {
        "Name" : "Steelshear",
        "ID" : "7",
        "Location Type" : m,
        "Region" : "Shimmergarde",
        "Cords" : (8.5,-2),
        "Temp War" : False,
        "Temp Cold" : True
    },
    "Ayraka" : {
        "Name" : "Ayraka",
        "ID" : "8",
        "Location Type" : ca+t,
        "Region" : "Shimmergarde",
        "Cords" : (9,-2.25),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Magehost" : {
        "Name" : "Magehost",
        "ID" : "9",
        "Location Type" : ca,
        "Region" : "Shimmergarde",
        "Cords" : (7,-2.75),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Lrimmere" : {
        "Name" : "Lrimmere",
        "ID" : "10",
        "Location Type" : i+t,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Tringate" : {
        "Name" : "Tringate",
        "ID" : "11",
        "Location Type" : r,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Vluxstin" : {
        "Name" : "Vluxstin",
        "ID" : "12",
        "Location Type" : v,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Atheledo" : {
        "Name" : "Atheledo",
        "ID" : "13",
        "Location Type" : pl,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Yloria" : {
        "Name" : "Yloria",
        "ID" : "14",
        "Location Type" : t,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Klosa" : {
        "Name" : "Klosa",
        "ID" : "15",
        "Location Type" : t,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Glouis" : {
        "Name" : "Glouis",
        "ID" : "16",
        "Location Type" : g,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Remmont" : {
        "Name" : "Remmont",
        "ID" : "17",
        "Location Type" : p,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Jeim" : {
        "Name" : "Jeim",
        "ID" : "18",
        "Location Type" : df+t,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    "Zaidale" : {
        "Name" : "Zaidale",
        "ID" : "19",
        "Location Type" : f+t,
        "Region" : "Shimmergarde",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False
    },
    }
}

#--------------------------------------------------------------------------------------------------- Dimhollow
RD_Dimhollow = {
    "Name" : {
    "Bleakwood" : {
        "Name" : "Bleakwood",
        "ID" : "1",
        "Location Type" : df,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp War" : True,
        "Temp Cold" : False,
    },
    "Mutetide" : {
        "Name" : "Mutetide",
        "ID" : "2",
        "Location Type" : f+t,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False,
    },
    "Darkfront" : {
        "Name" : "Darkfront",
        "ID" : "3",
        "Location Type" : g,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False,
    },
    "Spearlost" : {
        "Name" : "Spearlost",
        "ID" : "4",
        "Location Type" : ca,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False,
    },
    "Shroudmire" : {
        "Name" : "Shroudmire",
        "ID" : "5",
        "Location Type" : mr+co,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False,
    },
    "Ghostpass" : {
        "Name" : "Ghostpass",
        "ID" : "6",
        "Location Type" : (v, ca),
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False,
    },
    "Shadowbourne" : {
        "Name" : "Shadowbourne",
        "ID" : "7",
        "Location Type" : t,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False,
    },
    "Nightmire" : {
        "Name" : "Nightmire",
        "ID" : "8",
        "Location Type" : mr+ca,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False,
    },
    "Bleakgrave" : {
        "Name" : "Bleakgrave",
        "ID" : "9",
        "Location Type" : fo,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False,
    },
    "Ekloit" : {
        "Name" : "Ekloit",
        "ID" : "10",
        "Location Type" : mr+c,
        "Region" : "Dimhollow",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False,
    },
    }
}

#--------------------------------------------------------------------------------------------------- Ebonmeadow
RD_Ebonmeadow = {
    "Name" : {
    "Kliachester" : {
        "Name" : "Kliachester",
        "ID" : "1",
        "Location Type" : c,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Kilpong" : {
        "Name" : "Kilpong",
        "ID" : "2",
        "Location Type" : l,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Kilstall" : {
        "Name" : "Kilstall",
        "ID" : "3",
        "Location Type" : r,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Demonhall" : {
        "Name" : "Demonhall",
        "ID" : "4",
        "Location Type" : p+d,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Deadburn" : {
        "Name" : "Deadburnn",
        "ID" : "5",
        "Location Type" : o+p,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Bonegrove" : {
        "Name" : "Bonegrove",
        "ID" : "6",
        "Location Type" : f+g,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Flaset" : {
        "Name" : "Flaset",
        "ID" : "7",
        "Location Type" : p+t,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Mossmaund" : {
        "Name" : "Mossmaund",
        "ID" : "8",
        "Location Type" : r+t,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Drord" : {
        "Name" : "Drord",
        "ID" : "9",
        "Location Type" : r+l+c,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Adenaham" : {
        "Name" : "Adenaham",
        "ID" : "10",
        "Location Type" : t,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Asheigh" : {
        "Name" : "Asheigh",
        "ID" : "11",
        "Location Type" : f+t,
        "Region" : "Ebonmeadow",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    }
}

#--------------------------------------------------------------------------------------------------- Duskgrove
RD_Duskgrove = {
    "Name" : {
    "Killhollow" : {
        "Name" : "Killhollow",
        "ID" : "1",
        "Location Type" : d,
        "Region" : "Duskgrove",
        "Cords" : (4,-19),
        "Temp Warm" : False,
        "Temp Cold" : True
    },
    "Vinmur" : {
        "Name" : "Vinmur",
        "ID" : "2",
        "Location Type" : t,
        "Region" : "Duskgrove",
        "Cords" : (7,-21),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Lakeside" : {
        "Name" : "Lakeside",
        "ID" : "3",
        "Location Type" : l+c,
        "Region" : "Duskgrove",
        "Cords" : (10,-18),
        "Temp Warm" : False,
        "Temp Cold" : True
    },
    "Eastborough" : {
        "Name" : "Eastborough",
        "ID" : "4",
        "Location Type" : df+d,
        "Region" : "Duskgrove",
        "Cords" : (8,-19),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Clalles" : {
        "Name" : "Clalles",
        "ID" : "5",
        "Location Type" : c,
        "Region" : "Duskgrove",
        "Cords" : (6,-18),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Thornmeadow" : {
        "Name" : "Thornmeadow",
        "ID" : "6",
        "Location Type" : p,
        "Region" : "Duskgrove",
        "Cords" : (6,-20),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    "Cursegate" : {
        "Name" : "Cursegate",
        "ID" : "7",
        "Location Type" : fo,
        "Region" : "Duskgrove",
        "Cords" : (7,-19),
        "Temp Warm" : False,
        "Temp Cold" : True
    },
    "Iyrovine" : {
        "Name" : "Iyrovine",
        "ID" : "8",
        "Location Type" : t,
        "Region" : "Duskgrove",
        "Cords" : (3,-10),
        "Temp Warm" : False,
        "Temp Cold" : True
    },
    }
}

#--------------------------------------------------------------------------------------------------- Dawngrove
RD_Dawngrove = {
    "Name" : {
    "Tassis" : {
        "Name" : "Tassis",
        "ID" : "1",
        "Location Type" : t,
        "Region" : "Dawngrove",
        "Cords" : (12,4),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Sunhollow" : {
        "Name" : "Sunhollow",
        "ID" : "2",
        "Location Type" : d,
        "Region" : "Dawngrove",
        "Cords" : (14,6),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Besanluire" : {
        "Name" : "Besanluire",
        "ID" : "3",
        "Location Type" : t,
        "Region" : "Dawngrove",
        "Cords" : (14,4),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Silvermount" : {
        "Name" : "Silvermount",
        "ID" : "4",
        "Location Type" : df+t,
        "Region" : "Dawngrove",
        "Cords" : (13,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Qaxtin" : {
        "Name" : "Qaxtin",
        "ID" : "5",
        "Location Type" : c,
        "Region" : "Dawngrove",
        "Cords" : (12,6),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Qrokving" : {
        "Name" : "Qrokving",
        "ID" : "6",
        "Location Type" : l+dun,
        "Region" : "Dawngrove",
        "Cords" : (15,-3),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Tradespell" : {
        "Name" : "Tradespell",
        "ID" : "7",
        "Location Type" : df+dun,
        "Region" : "Dawngrove",
        "Cords" : (13,3),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Bridegalley" : {
        "Name" : "Bridegalley",
        "ID" : "8",
        "Location Type" : l+c,
        "Region" : "Dawngrove",
        "Cords" : (16,4),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    }
}

#--------------------------------------------------------------------------------------------------- The Subterrane
RD_TheSubterrane = {
    "Name" : {
    "Crystalshear" : {
        "Name" : "Crystalshear",
        "ID" : "1",
        "Location Type" : c,
        "Region" : "The Subterrane",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : True
    },
    }
}

#--------------------------------------------------------------------------------------------------- The Subterrane Sea
RD_TheSubterraneSea = {
    "Name" : {
    "tmp" : {
        "Name" : "tmp",
        "ID" : "1",
        "Location Type" : c,
        "Region" : "The Subterrane Sea",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : True
    },
    }
}

#--------------------------------------------------------------------------------------------------- North Sea
RD_NorthSea = {
    "Name" : {
    "tmp" : {
        "Name" : "tmp",
        "ID" : "1",
        "Location Type" : c,
        "Region" : "North Sea",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    }
}

#--------------------------------------------------------------------------------------------------- South Sea
RD_SouthSea = {
    "Name" : {
    "tmp" : {
        "Name" : "tmp",
        "ID" : "1",
        "Location Type" : c,
        "Region" : "South Sea",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False,
    },
    }
}

#--------------------------------------------------------------------------------------------------- The Welkin
RD_TheWelkin = {
    "Name" : {
    "Levatoise" : {
        "Name" : "Levatoise",
        "ID" : "1",
        "Location Type" : i+c,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Plailliers" : {
        "Name" : "Plailliers",
        "ID" : "2",
        "Location Type" : l,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Eaglerest" : {
        "Name" : "Eaglerest",
        "ID" : "3",
        "Location Type" : i+t,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Angeo" : {
        "Name" : "Angeo",
        "ID" : "4",
        "Location Type" : i+fo+dun,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Ulphia" : {
        "Name" : "Ulphia",
        "ID" : "5",
        "Location Type" : ca+dun,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Isonrith" : {
        "Name" : "Isonrith",
        "ID" : "6",
        "Location Type" : l+dun,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Kredo" : {
        "Name" : "Kredo",
        "ID" : "7",
        "Location Type" : ile,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Uyoxedo" : {
        "Name" : "Uyoxedo",
        "ID" : "8",
        "Location Type" : i+t,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : True,
        "Temp Cold" : False
    },
    "Cosmic Anomaly" : {
        "Name" : "Cosmic Anomaly",
        "ID" : "9",
        "Location Type" : q,
        "Region" : "The Welkin",
        "Cords" : (0,0),
        "Temp Warm" : False,
        "Temp Cold" : False
    },
    }
}

#individual location from dict. + and addition info
"""print(RD_Shimmergarde["Clalimar"]["Region"])"""

def Regions_Dat():
    global x
    global Regions
    print("Regions\n", "")
    for (x,item) in enumerate(Regions, start = 1):
        print(x, ":", item)
    print("")
    

def Location_Dat():
    global df
    global f
    global l
    global i
    global ile
    global cc
    global c
    global t
    global tu
    global g
    global ca
    global d
    global p
    global fo
    global co
    global oR
    global o
    global m
    global mr
    global r
    global v
    global pl
    global dun
    global ru
    global q
    global l_id
    global l_info
    global key
    global RD_Puregarde
    global RD_Starmoor
    global RD_Frostmord
    global RD_Shimmergarde
    global RD_Dimhollow
    global RD_Ebonmeadow
    global RD_Duskgrove
    global RD_Dawngrove
    global RD_TheSubterrane
    global RD_TheSubterraneSea
    global RD_NorthSea
    global RD_SouthSea
    global RD_TheWelkin

    chk_loc_dat = int(input("Enter A Region # "))

    if (chk_loc_dat == 1):
        for l_id, l_info in RD_Puregarde.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])

    if (chk_loc_dat == 2):
        for l_id, l_info in RD_Starmoor.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])

    if (chk_loc_dat == 3):
        for l_id, l_info in RD_Frostmord.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])

    if (chk_loc_dat == 4):
        for l_id, l_info in RD_Shimmergarde.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])
    
    if (chk_loc_dat == 5):
        for l_id, l_info in RD_Dimhollow.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])
    
    if (chk_loc_dat == 6):
        for l_id, l_info in RD_Ebonmeadow.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])
    
    if (chk_loc_dat == 7):
        for l_id, l_info in RD_Duskgrove.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])
    
    if (chk_loc_dat == 8):
        for l_id, l_info in RD_Dawngrove.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])
    
    if (chk_loc_dat == 9):
        for l_id, l_info in RD_TheSubterrane.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])

    if (chk_loc_dat == 10):
        for l_id, l_info in RD_TheSubterraneSea.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])
    
    if (chk_loc_dat == 11):
        for l_id, l_info in RD_NorthSea.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])
    
    if (chk_loc_dat == 12):
        for l_id, l_info in RD_SouthSea.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])
    
    if (chk_loc_dat == 13):
        for l_id, l_info in RD_TheWelkin.items():
            print("\nLocation ID:", l_id)
            for key in l_info:
                print(key + ':', l_info[key])

def choose_location():
    global df
    global f
    global l
    global i
    global ile
    global cc
    global c
    global t
    global tu
    global g
    global ca
    global d
    global p
    global fo
    global co
    global oR
    global o
    global m
    global mr
    global r
    global v
    global pl
    global dun
    global ru
    global q
    global l_id
    global l_info
    global key
    global RD_Puregarde
    global RD_Starmoor
    global RD_Frostmord
    global RD_Shimmergarde
    global RD_Dimhollow
    global RD_Ebonmeadow
    global RD_Duskgrove
    global RD_Dawngrove
    global RD_TheSubterrane
    global RD_TheSubterraneSea
    global RD_NorthSea
    global RD_SouthSea
    global RD_TheWelkin
    global chk_loc_nam
    global chk_reg_nam

    region_names = World_Locations["Regions"]["Names"]
    for x in list(region_names):
        print(x)
    chk_reg_nam = (input("\nChoose a Region \n" + "> "))
    chk_reg_nam = chk_reg_nam.title()
    if debug is True:
        print("region name", chk_reg_nam)
    pizza = 0
    while(pizza != 1):
        if chk_reg_nam == "Puregarde": #Puregarde
            print("You've selected Puregarde\n")
            location_names = RD_Puregarde["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "Starmoor": #Starmoor
            print("You've selected Starmoor\n")
            location_names = RD_Starmoor["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "Frostmord":
            print("You've selected Frostmord\n")
            location_names = RD_Frostmord["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "Shimmergarde":
            print("You've selected Shimmergarde\n")
            location_names = RD_Shimmergarde["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "Dimhollow":
            print("You've selected Dimhollow\n")
            location_names = RD_Dimhollow["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "Ebonmeadow":
            print("You've selected Ebonmeadow\n")
            location_names = RD_Ebonmeadow["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "Duskgrove":
            print("You've selected Duskgrove\n")
            location_names = RD_Duskgrove["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "Dawngrove":
            print("You've selected Dawngrove\n")
            location_names = RD_Dawngrove["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "The Subterrane":
            print("You've selected The Subterrane\n")
            location_names = RD_TheSubterrane["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "The Subterrane Sea":
            print("You've selected The Subterrane Sea\n")
            location_names = RD_TheSubterraneSea["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "North Sea":
            print("You've selected North Sea\n")
            location_names = RD_NorthSea["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "South Sea":
            print("You've selected South Sea\n")
            location_names = RD_SouthSea["Name"]
            for x in list(location_names):
                print(x)
            location_list = list(location_names)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        if chk_reg_nam == "The Welkin":
            print("You've selected The Welkin\n")
            location_names = RD_TheWelkin["Name"]
            for x in list(location_names):
                print(x)
            chk_loc_nam = (input("\nChoose a Location \n" + "> "))
            location_list = list(location_names)
            apple = 0
            while apple != 1:
                if (chk_loc_nam in location_list):
                    chk_loc_nam = chk_loc_nam.title()
                    if (debug == False):
                        print("\nYou Have Chosen To Travel Towards", chk_loc_nam)
                    if (debug == True):
                        print("\n-debug- File:", "location.py", "You Have Chosen To Travel Towards", chk_loc_nam)
                    apple = apple + 1
                    pizza = pizza + 1
                else:
                    print("Failed: Location not found")
                    chk_loc_nam = (input("\nChoose a Location \n" + "> "))
        elif(chk_reg_nam not in region_names):
            chk_reg_nam = (input("\nChoose a Region \n"))
            chk_reg_nam = chk_reg_nam.title()
            print("Region Not Found")
#choose_location()

your_joke = "shit"
if (debug == True):
    if your_joke == "shit":
        pass
    else:
        Regions_Dat()
        Location_Dat()
