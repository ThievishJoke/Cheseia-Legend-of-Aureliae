
import random
Princess_Spiders_Names = ["Lhilshu", "Issiesh", "Yarheqo", "En'qashe", "Naseth", "Sziaquth", "Kharzee", "Qhexhethoh", "Zievhi", "Sieca", "Klazhush", "Khashod", "An'qie", "Shezhalles", "Lhaqe", "Izocei", "Shreshir", "Shishri", "Khiaknus", "Shiaxhil", "Chechiqee", "Shocad", "Zhillush", "Nailus", "Zhiqareil", "Naikkiesh", "Zeezhorheed", "Chequs", "Neishozhia", "Zhanchelash", "Qiracei", "Sovexhai", "Shazsucis", "Khechien'qa", "Qivishel", "Klellosh", "Shiq'sho", "Rhizarhi", "Evish", "Riqshive", "Zhal'shal", "Zeen'qu", "Zichok'sie", "Secok'sith", "Lath'a"]
Slain_Bosses = []

##---------------------------------------------------------------- Boss Guide
#"" : {    --------------BOSS NAME
#    1 : {         --------------Variant (If any)
#    "Name" : (""), ---Name / Variant Name(If any)
#    "Description" : "", --------Desribe Boss's Backstory(If unique) / Lore
#    "Health" : 0, -------------HP
#    "Damage" : 0, -------------Physical Damage
#    "Magic Damage" : 0, -------Magic Damage
#    "Magic_Resistace" : 0, -----Resistance to Magic Damage
#    "Armor" : 0 ----------------Resistance to Physical Damage
#    },
#}

bosses = {
    "Rat Horde" : {
        "Name" : ("Rat Horde"),
        "Description" : "",
        "Health" : 35,
        "Damage" : 15,
        "Magic Damage" : 0,
        "Magic_Resistace" : 0,
        "Armor" : 0
    }, #End of Rat
    "Slime" : {
        1 : {
            "Mega Slime" : {
                "Name" : ("Mega Slime"),
                "Description" : "",
                "Health" : 35,
                "Damage" : 10,
                "Magic Damage" : 5,
                "Magic_Resistace" : 0,
                "Armor" : 0
            }
        }
    }, #End of Slime
    "Spider" : {
        1 : { #Princesses
            "Princess Spiders" : {
                1 : {
                    "Name" : ("Daughters of Yi'Si The Grand Spider Empress"),
                    "Description" : "",
                    "Health" : 120,
                    "Damage" : 15,
                    "Magic Damage" : 5,
                    "Magic_Resistace" : 0,
                    "Armor" : 15
                },
            },
        },
        2 : { #Crimson Brood Mother
            "Mother Of The Crimson Broods" : {
                "Name" : ("Hel'Eda"),
                "Description" : "",
                "Health" : 150,
                "Damage" : 30,
                "Magic Damage" : 10,
                "Magic_Resistace" : 0,
                "Armor" : 21
            },
        },
        3 : { #Heiresses Of Yi'Si
            "Heiresses" : {
                1 : {
                    "Cho'Leekiah" : {
                        "Name" : ("Cho'Leekiah First Daughter Of Yi'Si The Grand Drider Empress"),
                        "Description" : "",
                        "Health" : 150,
                        "Damage" : 30,
                        "Magic Damage" : 20,
                        "Magic_Resistace" : 15,
                        "Armor" : 30
                    }
                },
                2 : {
                    "Rek'Ka" : {
                        "Name" : ("Rek'Ka Second Daughter Of Yi'Si The Grand Drider Empress"),
                        "Description" : "",
                        "Health" : 400,
                        "Damage" : 35,
                        "Magic Damage" : 15,
                        "Magic_Resistace" : 10,
                        "Armor" : 35
                    }
                },
            },
        }
    }, #End of Spider
    "Reptile" : {
        "Naga" : {
        },
        "Dragon" : {
            "Zombie" : {
                "Headless" : {
                    "Name" : ("Zephyrinis The Headless Dragon"),
                    "Description" : ""
                    "Residence: Unknown ",
                    "Health" : 1125,
                    "Damage" : 40,
                    "Magic Damage" : 130,
                    "Magic Resistance" : 150,
                    "Armor" : 0,
                },
            },
            "Soul" : { #Soul Dragon
                1 : { #Wise
                    "Wise" : {
                        "Name" : ("Arigannia The Wise Dragon"),
                        "Description" : ""
                        "Residence: Unknown ",
                        "Health" : 945,
                        "Damage" : 0,
                        "Magic Damage" : 170,
                        "Magic Resistance" : 20,
                        "Armor" : 90,
                    },
                },
                2 : { #Light and Dark
                    "Licht" : {
                        "Name" : ("Ahreavea Auf Fuurdrache Auf Der Licht Und Wahrheiten"),
                        "Description" : ""
                        "Residence: Unknown ",
                        "Health" : 1325,
                        "Damage" : 0,
                        "Magic Damage" : 190,
                        "Magic Resistance" : 90,
                        "Armor" : 45,
                    },
                    "Leere" : {
                        "Name" : ("Zepharon Der Fuurdrache Auf Der Dunkel Und Ideale"),
                        "Description" : ""
                        "Residence: Unknown ",
                        "Health" : 1325,
                        "Damage" : 0,
                        "Magic Damage" : 190,
                        "Magic Resistance" : 45,
                        "Armor" : 90,
                    }
                }
            }
        },
        "Drake" : {
            "Mecha" : {
                "Name" : ("Hologannia The Mecha Dragon"),
                "Description" : ""
                "Residence: Unknown ",
                "Health" : 945,
                "Damage" : 65,
                "Magic Damage" : 60,
                "Magic Resistance" : 30,
                "Armor" : 40,
            },
        },
        "Hydra" : {
            "Undead" : { #Multihead Undying
                "Multi-Head" : {
                    "Name" : ("Zeveronoh The Twenty Headed Hydra"),
                    "Description" : ""
                    "Residence: Unknown ",
                    "Health" : 1145,
                    "Damage" : 130,
                    "Magic Damage" : 130,
                    "Magic Resistance" : 90,
                    "Armor" : 90,
                },
                "Undying" : {
                    "Name" : ("Heveron The Undying Hydra"),
                    "Description" : ""
                    "Residence: Unknown ",
                    "Health" : 935,
                    "Damage" : 20,
                    "Magic Damage" : 20,
                    "Magic Resistance" : 45,
                    "Armor" : 90,
                },
            },
            "Locational" : {
                "North" : {
                    "Name" : ("Futeritha The Sea Hydra Of The North"),
                    "Description" : ""
                    "Residence: Unknown ",
                    "Health" : 888,
                    "Damage" : 70,
                    "Magic Damage" : 80,
                    "Magic Resistance" : 35,
                    "Armor" : 35,
                },
                "South" : {
                    "Name" : ("Keisehtagnnia The Sea Hydra Of The South"),
                    "Description" : ""
                    "Residence: Unknown ",
                    "Health" : 999,
                    "Damage" : 50,
                    "Magic Damage" : 80,
                    "Magic Resistance" : 45,
                    "Armor" : 35,
                },
            }
        }
    }, #End of Reptile
    "Human" : {
#        "Hybrid" : { #Un-used
#            1 : { #Kistune
#            },
#            2 : { #Lamia
#            },
#            2 : { #Changeling
#            },
#        },
#        "Pirate" : { #Un-used
#            1 : { #Deckhand
#            },
#            2 : { #Gunslinger
#            },
#            3 : { #First Mate
#            },
#            4 : { #Quartermaster
#            },
#            5 : { #Powder Monkey
#            },
#            6 : { #Captian
#            },
#        },
        "Bandit" : {
            1 : { #Bandit
                "Name" : ("Bandit"),
                "Description" : "",
                1 : {
                    "Name" : ("Foolish Valatina"),
                    "Description" : "",
                    "Health" : 265,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic Resistance" : 0, 
                    "Armor" : 12,
                },
                2 : {
                    "Name" : ("Angel Eyes Ruby"),
                    "Description" : "",
                    "Health" : 255,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic Resistance" : 0, 
                    "Armor" : 13,
                },
                3 : {
                    "Name" : ("Carlo Choinz"),
                    "Description" : "",
                    "Health" : 255,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic Resistance" : 0, 
                    "Armor" : 13,
                },
                4 : {
                    "Name" : ("Angel Eyes Ruby"),
                    "Description" : "",
                    "Health" : 255,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic Resistance" : 0, 
                    "Armor" : 13,
                },
            },
            2 : { #Bandit Chief
                "Name" : ("Bandit Chief"),
                "Description" : "",
                "Rogue" : {
                    "Name" : ("Bandit Chief, Ayana The Rogue"),
                    "Description" : "",
                    "Health" : 275,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic Resistance" : 0, 
                    "Armor" : 19,
                },
            },
        },
        1 : { #Prowler #1
            "Name" : ("Prowler"),
            "Description" : "",
            "Leila" : {
                "Name" : ("Prowler Leila"),
                "Description" : "",
                "Health" : 240,
                "Damage" : 50,
                "Magic Damage" : 0,
                "Magic Resistance" : 0, 
                "Armor" : 16,
            },
        },
        2 : { #Assassin #4
            "Name" : ("Assassin"),
            "Description" : "",
            "Selena" : {
                "Name" : ("Whispering Selena"),
                "Description" : "",
                "Health" : 230,
                "Damage" : 41,
                "Magic Damage" : 9,
                "Magic Resistance" : 0, 
                "Armor" : 0,
            },
        },
#        8 : { #Pickpocket #1 #Un-used
#        },
#        9 : { #Myrmidon #3   #Un-used
#        },
    }, #End of Human
    "Demon" : {
        "Pure" : {
#            1 : { #Demon #1 #Un-used
#                "Name" : ("Demon"),
#                "Description" : "",
#                "Health" : 73,
#                "Damage" : 24,
#                "Magic Damage" : 0,
#                "Magic Resistance" : 35,
#                "Armor" : 20
#            },
            1 : { #Arch Demon #2
                "Name" : ("Arch Demon"),
                "Description" : "",
                1 : {
                    "Name" : ("Xal Genoth The Arch Demon"),
                    "Description" : "",
                    "Health" : 400,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 15
                },
                2 : {
                    "Name" : ("Drog Thithoz The Arch Demon"),
                    "Description" : "",
                    "Health" : 400,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 15
                },
                3 : {
                    "Name" : ("Xuronuth The Arch Demon"),
                    "Description" : "",
                    "Health" : 400,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 15
                },
            },
#            3 : { #Devil #Un-used
#                "Name" : ("Devil"),
#                "Description" : "",
#                "Health" : 91,
#                "Damage" : 26,
#                "Magic Damage" : 0,
#                "Magic Resistance" : 20,
#                "Armor" : 15
#            },
#            4 : { #Blood Devil #Un-used
#                "Name" : ("Blood Devil"),
#                "Description" : "",
#                "Health" : 91,
#                "Damage" : 0,
#                "Magic Damage" : 26,
#                "Magic Resistance" : 15,
#                "Armor" : 33
#            },
#            5 : { #Incubi #Un-used
#                "Name" : ("Incubi"),
#                "Description" : "",
#                "Health" : 132,
#                "Damage" : 0,
#                "Magic Damage" : 32,
#                "Magic Resistance" : 35,
#                "Armor" : 22
#            },
#            6 : { #Succubi #Un-used
#                "Name" : ("Succubi"),
#                "Description" : "",
#                "Health" : 135,
#                "Damage" : 0,
#                "Magic Damage" : 30,
#                "Magic Resistance" : 32,
#                "Armor" : 29
#            },
#        },
#        "Hybrid" : {
#            1 : { #Dire #Un-used
#                "Name" : ("Dire"),
#                "Description" : "",
#                "Health" : 170,
#                "Damage" : 37,
#                "Magic Damage" : 0,
#                "Magic Resistance" : 23,
#                "Armor" : 11
#            },
#            2 : { #Cambion #Un-used
#                "Name" : ("Cambion"),
#                "Description" : "",
#                "Health" : 136,
#                "Damage" : 35,
#                "Magic Damage" : 0,
#                "Magic Resistance" : 20,
#                "Armor" : 12
#            },
#            3 : { #Demon Halfling #Un-used
#                "Name" : ("Demon Halfling"),
#                "Description" : "",
#                "Health" : 53,
#                "Damage" : 23,
#                "Magic Damage" : 0,
#                "Magic Resistance" : 12,
#                "Armor" : 9
#            }
        },
    },
    "Monsters" : {
        1 : { #Named Giants
            "Named Giant" : {
                1 : {
                    "Name" : ("Shetulutushois The Giant"),
                    "Description" : "",
                    "Health" : 335,
                    "Damage" : 50,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 15
                },
            },
        },
        2 : { #Named Orge
            "Named Orge" : {
                1 : {
                    "Name" : ("Trogekurk The Orge Of Lost Spredigen"),
                    "Description" : "",
                    "Health" : 300,
                    "Damage" : 45,
                    "Magic Damage" : 0,
                    "Magic_Resistace" : 0,
                    "Armor" : 15
                },
            },
        },
    } #End of Monster
}

print(bosses["Spider"][1]["Princess Spiders"][1])

##Bosses
#--Complete--#bosses_group_misc =  ["Rat_Horde", "God_Slime"]
#--Complete--#bosses_group_spider = ["Heleda_Mother_Of_The_Crimson_Broods", (Princess_Spiders, "Daughter_Of_Yisi_The_Grand_Spider_Empress"), "Rekka_Daughter_Of_Yisi_The_Grand_Spider_Empress", "Choleekiah'sol_Heiress_Of_The_Grand_Spider_Empress"]
#--Complete--#Princess_Spiders = ["Lhilshu"(Done), "Issiesh", "Yarheqo", "En'qashe", "Naseth", "Sziaquth", "Kharzee", "Qhexhethoh", "Zievhi", "Sieca", "Klazhush", "Khashod", "An'qie", "Shezhalles", "Lhaqe", "Izocei", "Shreshir", "Shishri", "Khiaknus", "Shiaxhil", "Chechiqee", "Shocad", "Zhillush", "Nailus", "Zhiqareil", "Naikkiesh", "Zeezhorheed", "Chequs", "Neishozhia", "Zhanchelash", "Qiracei", "Sovexhai", "Shazsucis", "Khechien'qa", "Qivishel", "Klellosh", "Shiq'sho", "Rhizarhi", "Evish", "Riqshive", "Zhal'shal", "Zeen'qu", "Zichok'sie", "Secok'sith", "Lath'a"]

#--Complete--#bosses_group_monster = ["Shetulutushois_The_Giant"]
#--Complete--#bosses_group_demon = ["Xal'genoth_The_Arch_Demon", "Drog'thithoz_The_Arch_Demon", "Xuronuth_The_Arch_Demon"]
#--Complete--#bosses_group_human = ["Foolish_Valentina", "Angel_Eyes_Ruby", "Prowler_Leila", "Whispering_Selena", "Bandit_Chief_Ayana_The_Rogue", "Carlo_Choinz"]

##---------------------------------------------------------------- Uninplemented

#--Incomplete--#Fire_Souls = ["Spark", "Flashfire", "Tempris", "Cole", "Boyle", "Flarion", "Incedis", "Incendius", "Claire"]
#--Incomplete--#Aqua_Souls = ["Vapora", "Neptulus", "Salis", "Tempest", "Tempestus", "Tsunis", "Aquara"]
#--Incomplete--#Earth_Souls = ["Exto", "Sumus", "Tera", "Cobbles", "Basselt", "Grine", "Core"]
#--Incomplete--#Air_Souls = ["Sono", "Chinook", "Avian", "Voxis", "Whiff", "Mistral", "Janna", "Cerulle", "Tropos", "Astra"]
#--Incomplete--#Lightning_Souls = ["Galva", "Volt", "Watt", "Gurate", "Farad", "Volta", "Thun", "Galvan"]
#--Incomplete--#bosses_group_soul = [((Fire_Souls), "The_Soul_Of_Fire"), ((Aqua_Souls), "The_Soul_Of_Water"), ((Earth_Souls), "The_Soul_Earth"), ((Air_Souls), "The_Soul_Of_Air"), ((Lightning_Souls), "The_Soul_Of_Lightning")]
#--Incomplete--#bosses_group_golems = ["Blitz_The_Great_Steam_Golem", "Monah_The_Malfuctioning_Steam_Golem", "Drulbamm_The_Obsidian_Rock_Golem", "Yeshai_The_Diamond_Crystal_Golem", ""]

##---------------------------------------------------------------- Canine(G1)
#Wolf_Pack_Hp = 220
#Wolf_Pack_Dmg = 35
#Dire_Wolf_Pack_Hp = 240
#Dire_Wolf_Pack_Dmg = 40
##---------------------------------------------------------------- Ghost(G2)
#Thignmara_The_Bleeding_Nightmare_Hp = 350
#Thignmara_The_Bleeding_Nightmare_Dmg = 45
#Nightmare_Of_Suelbrellik_Hp = 250
#Nightmare_Of_Suelbrellik_Dmg = 40
#Willia_The_Wisp_Hp = 320
#Willia_The_Wisp_Dmg = 40
#Shade_Of_Taorthtuc_Hp = 220
#Shade_Of_Taorthtuc_Dmg = 35
##---------------------------------------------------------------- Mammal(G3)
#Northern_Mammoth_Elk_Hp = 200
#Northern_Mammoth_Elk_Dmg = 15
#Colossal_Elk_Hp = 215
#Colossal_Elk_Dmg = 15
#Ancient_Frohst_Hp = 315
#Ancient_Frohst_Dmg = 40
#Ancient_Forest_Mecha_Hp = 1000
#Ancient_Forest_Mecha_Dmg = 100
##---------------------------------------------- Nymph(G4)
#Clethra_Speaker_Of_Freygrove_Forest_Hp = 125 
#Clethra_Speaker_Of_Freygrove_Forest_Dmg = 30
#Mi_The_Beauty_Of_Freygrove_Hp = 125
#Mi_The_Beauty_Of_Freygrove_Dmg = 30
#Nephiaha_Caretaker_Of_Freygrove_Forest_Hp = 125
#Nephiaha_Caretaker_Of_Freygrove_Forest_Dmg = 30
#Illonisah_Mother_Of_Freygrove_Forest_Hp = 130
#Illonisah_Mother_Of_Freygrove_Forest_Dmg = 30
##---------------------------------------------- Fairy(G5)
#Ayanna_Blackrose_The_Fairy_Hp = 10
#Ayanna_Blackrose_The_Fairy_Dmg = 15
#Celestia_Elmstone_The_Currupted_Fairy_Hp = 10
#Celestia_Elmstone_The_Currupted_Fairy_Dmg = 15
##---------------------------------------------- Sylph(G6)
#Feroa_Of_Duskgrove_Hp = 10
#Feroa_Of_Duskgrove_Dmg = 15
#Aoq_raie_Of_Duskgrove_Hp = 10
#Aoq_raie_Of_Duskgrove_Dmg = 15
#Inshiwochi_Of_Duskgrove_Hp = 10
#Inshiwochi_Of_Duskgrove_Dmg = 15
#Jiaena_Of_Duskgrove_Hp = 10
#Jiaena_Of_Duskgrove_Hp_Dmg = 15
#Helaniahia_The_Forest_Sylph_Hp = 10
#Helaniahia_The_Forest_Sylph_Dmg = 15
#Un_voshe_Of_Duskgrove_Hp = 10
#Un_voshe_Of_Duskgrove_Dmg = 15
#Aero_ohashio_Of_Dawngrove_Hp = 10
#Aero_ohashio_Of_Dawngrove_Dmg = 15
#Mesperiae_Of_Dawngrove_Hp = 10
#Mesperiae_Of_Dawngrove_Dmg = 15
#Raedon__The_Sky_Of_The_Forest_Hp = 10
#Raedon__The_Sky_Of_The_Forest_Dmg = 15
#Nimithiah_The_Forest_Sylph_Hp = 10
#Nimithiah_The_Forest_Sylph_Dmg = 15
#Nimith_Of_The_Undergound_Forest_Hp = 10
#Nimith_Of_The_Undergound_Forest_Dmg = 15
#Niera_Voshe_The_Wise_Sylph_Hp = 10
#Niera_Voshe_The_Wise_Sylph_Dmg = 15
#Feroa_ohashio_Of_Dawngrove_Hp = 10
#Feroa_ohashio_Of_Dawngrove_Dmg = 15
#Sithiasei_The_Forest_Sylph_Hp = 10
#Sithiasei_The_Forest_Sylph_Dmg = 15
#Sepharie_Of_Dawngrove_Hp = 10
#Sepharie_Of_Dawngrove_Dmg = 15
#Ohya_ahri_The_Forest_Sylph_Hp = 10
#Ohya_ahri_The_Forest_Sylph_Dmg = 15
#Uuoaeriannah_Of_Duskgrove_Hp = 10
#Uuoaeriannah_Of_Duskgrove_Dmg = 15
#Phieleeff_The_Forest_Sylph_Hp = 10
#Phieleeff_The_Forest_Sylph_Dmg = 15
#Aphlos_The_Of_Dawngrove_Hp = 10 
#Aphlos_The_Of_Dawngrove_Dmg = 15
#Zephyriah_The_Sky_Of_The_Forest_Hp = 10
#Zephyriah_The_Sky_Of_The_Forest_Dmg = 15
#Sheimo_Of_The_Underground_Forest_Hp = 10
#Sheimo_Of_The_Underground_Forest_Dmg = 15
##---------------------------------------------- Dryad(G7)
#Craderos_Crataehus_The_Elegent_Hp = 140
#Craderos_Crataehus_The_Elegent_Dmg = 30
#Baudien_Bauhinia_The_Inmovable_Hp = 145
#Baudien_Bauhinia_The_Inmovable_Dmg = 30
##---------------------------------------------- Spriggan(G8)
#Rosewood_Spriggan_Niartghin_Hp = 150
#Rosewood_Spriggan_Niartghin_Dmg = 30
#Goldenwood_Spriggan_Sadimghinian_Hp = 155
#Goldenwood_Spriggan_Sadimghinian_Dmg = 35
#Tundrawood_Spriggan_Oiatghinian_Hp = 150
#Tundrawood_Spriggan_Oiatghinian_Dmg = 30
#Baarkerwood_Spriggan_Rekraaghinian_Hp = 150
#Baarkerwood_Spriggan_Rekraaghinian_Dmg = 35
#Birchwood_Spriggan_Chirbghinian_Hp = 150
#Birchwood_Spriggan_Chirbghinian_Dmg = 30
#Diamondwood_Spriggan_Karrotghinian_Hp = 150
#Diamondwood_Spriggan_Karrotghinian_Dmg = 35
#Oakwood_Spriggan_Kaoghinian_Hp = 145
#Oakwood_Spriggan_Kaoghinian_Dmg = 25
#Silverwood_Spriggan_Revlisghinian_Hp = 155
#Silverwood_Spriggan_Revlisghinian_Dmg = 30
#Ironwood_Spriggan_Steelghinian_Hp = 155
#Ironwood_Spriggan_Steelghinian_Dmg = 30
##---------------------------------------------------------------- G9
#Ageless_Ghoul_Hp = 210
#Ageless_Ghoul_Dmg = 25
#Klosa_Daywalker_Hp = 210
#Klosa_daywalker_Dmg = 35
#Rotten_Draugr_Hp = 165
#Rotten_Draugr_Dmg = 20
#Restless_Draugr_Hp = 230
#Restless_Draugr_Dmg = 30
#Cheseian_Draugr_An_Undead_Knight_Hp = 250
#Cheseian_Draugr_An_Undead_Knight_Dmg = 35
#Resonating_Anomaly_Hp = 225
#Resonating_Anomaly_Dmg = 30
##---------------------------------------------------------------- G10
#Grand_Reaper_Riatoss_Hp = 230
#Grand_Reaper_Riatoss_Dmg = 35
#Areliees_The_Immortal_Dire_Hp = 5000
#Areliees_The_Immortal_Dire_Dmg = 500
##---------------------------------------------------------------- G11
#Alpha_Wyrm_Hp = 1000
#Alpha_Wyrm_Dmg = 35
##---------------------------------------------------------------- G12
#Kraken_Hp = 750
#Kraken_Dmg = 35
#Kehsnoff_Sailor_Of_The_North_Sea_Hp = 150
#Kehsnoff_Sailor_Of_The_North_Sea_Dmg = 25
##---------------------------------------------------------------- Souls(G13)
#Fire_Souls_Hp = 1035
#Fire_Souls_Dmg = 50
#Aqua_Souls_Hp = 1020
#Aqua_Souls_Dmg = 50
#Earth_Souls_Hp = 1050
#Earth_Souls_Dmg = 50
#Air_Souls_Hp = 990
#Air_Souls_Dmg = 50
#Lightning_Souls_Hp = 1005
#Lightning_Souls_Dmg = 50
##---------------------------------------------------------------- Golems(G14)
#Blitz_The_Great_Steam_Golem_Hp = 700
#Blitz_The_Great_Steam_Golem_Dmg = 50
#Monah_The_Malfuctioning_Steam_Golem_Hp = 425
#Monah_The_Malfuctioning_Steam_Golem_Dmg = 50
#Drulbamm_The_Obsidian_Rock_Golem_Hp = 750
#Drulbamm_The_Obsidian_Rock_Golem_Dmg = 50
#Yeshai_The_Diamond_Crystal_Golem_Hp = 700
#Yeshai_The_Diamond_Crystal_Golem_Dmg = 50