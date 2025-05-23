from rarity.WeaponRarities import index_rarity_by_name, calculate_bonus
import json

material = {

    # Wood

    # ORE

    # Alloys

    "Fae-Gold": {
        "Description": "A shimmering alloy created by combining Fae Ore and Gold. It harnesses the enchanting qualities of Fae Ore and the precious nature of gold, resulting in a material that enhances magical abilities, offers protection against magical attacks, and radiates a captivating aura.",
    },
    "Luminite Steel": {
        "Description": "An alloy created by combining Radiant Ore and Iron. It infuses the radiant properties of Radiant Ore with the strength and versatility of iron, resulting in a metal that is highly resistant to dark magic and possesses excellent durability and workability.",
    },
    "Celestial Silver": {
        "Description": "An alloy created by combining Celestite Ore and Silver. It combines the celestial essence of Celestite Ore with the purity and mystical properties of silver, resulting in a material that can repel dark forces, enhance magical abilities, and channel divine energy.",
    },
    "Prismatic Bronze": {
        "Description": "An alloy created by combining Prismium and Bronze. It blends the refractive qualities of Prismium with the durability and versatility of bronze, resulting in a metal that can refract and manipulate light, offering improved magical conductivity and resistance.",
    },
    "Stormglass": {
        "Description": "An alloy created by combining Stormite and Glass. It combines the storm-charged nature of Stormite with the transparency and fragility of glass, resulting in a material that can store and discharge electrical energy, while also allowing the user to see and interact with storms on a mystical level.",
    },
    "Umbral Silversteel": {
        "Description": "An alloy created by combining Umbrite Ore, Silver, and Steel. It combines the shadow-absorbing properties of Umbrite Ore with the mystical and antimagic qualities of silver, as well as the strength and versatility of steel, resulting in a metal that can nullify magic, absorb shadows, and provide exceptional durability.",
    },
    "Solium Crystal": {
        "Description": "An alloy created by combining Solwood and Crystal Quartz. It fuses the radiant and light-enhancing properties of Solwood with the clarity and amplification qualities of Crystal Quartz, resulting in a material that can channel solar energy, enhance magical effects, and provide protection against light-based attacks."
    },
    "Voidsteel": {
        "Description": "An alloy created by combining Voidstone and Steel. It merges the dark and void-manipulating properties of Voidstone with the strength and durability of steel, resulting in a metal that can cut through magical barriers, resist magical attacks, and disrupt magical energy."
    },
    "Ethereal Mithril": {
        "Description": "An alloy created by combining Spirit Ore and Mithril. It combines the ethereal and spiritual properties of Spirit Ore with the lightweight and versatile nature of mithril, resulting in a metal that enhances spiritual connections, grants agility and flexibility, and provides protection against supernatural entities."
    },
    "Starfire Titanium": {
        "Description": "An alloy created by combining Starfall and Titanium. It incorporates the celestial energy and radiant qualities of Starfall with the strength and lightness of titanium, resulting in a material that can harness stellar energy, enhance magical abilities, and offer exceptional durability."
    },
    "Faesilk Steel": {
        "Description": "An alloy created by combining Fae Ore and Steel. It combines the enchanting properties of Fae Ore with the strength and utility of steel, resulting in a metal that possesses enhanced magical conductivity, resists enchantments, and can be shaped into intricate and durable structures."
    },
    "Emberleaf Bronze": {
        "Description": "An alloy created by combining Blazeite Ore and Bronze. It merges the fiery properties of Blazeite Ore with the durability and versatility of bronze, resulting in a metal that can withstand high temperatures, enhance fire-based abilities, and resist heat-based attacks."
    },
    "Seashimmer Pearlsteel": {
        "Description": "An alloy created by combining Seashine Ore and Pearlescent. It combines the oceanic essence and conductivity of Seashine Ore with the ir"
    },
    "Quartzite Ebonsteel": {
        "Description": "An alloy created by combining Quartzite and Ebonite Ore. It blends the amplification and purifying properties of Quartzite with the dark and resilient qualities of Ebonite Ore, resulting in a metal that enhances magical effects, provides protection against dark forces, and has a high resistance to magical corruption."
    },
    "Hematite Carnalite": {
        "Elemental Affinity": "Blood",
        "Description": "An alloy created by combining Hematite Ore and Carnelian Ore. It combines the grounding and protective properties of Hematite Ore with the passionate and vitalizing qualities of Carnelian Ore, resulting in a metal that enhances physical strength and endurance, stimulates passion and courage, and provides a strong defense against negative energies."
    },
    "Spiritwood Ash": {
        "Elemental Affinity": ("Natural", "Soul"),
        "Description": "An alloy created by combining Spiritbark and Ashwood. It merges the ethereal and soulful properties of Spiritbark with the resilience and natural qualities of Ashwood, resulting in a wood material that enhances spiritual connections, wards off dark forces, and possesses exceptional durability and resistance to magical influences."
    },
    "Starfall Silverleaf": {
        "Elemental Affinity": "Lunar",
        "Description": "An alloy created by combining Starfall and Silverleaf. It combines the celestial energy and radiant qualities of Starfall with the shimmering and malleable properties of Silverleaf, resulting in a material that can harness stellar energy, reflect and amplify magical effects, and possesses remarkable flexibility and craftsmanship."
    },
    "Necrotite Obsidian": {
        "Elemental Affinity": "Soul",
        "Description": "An alloy created by combining Necrotite Ore and Obsidian. It fuses the life-draining and necrotic properties of Necrotite Ore with the sharpness and darkness-absorbing qualities of Obsidian, resulting in a material that can inflict and absorb life force, cut through magical barriers, and resist dark magic."
    },
    "Vitae Crimsonsteel": {
        "Elemental Affinity": "Blood",
        "Description": "An alloy created by combining Vitae Ore and Crimsonite Ore. It combines the life-infusing and vitalizing properties of Vitae Ore with the intense and fiery qualities of Crimsonite Ore, resulting in a metal that enhances healing abilities, grants increased vitality and regeneration, and can withstand high temperatures."
    },
    "Selene Moonglow": {
        "Elemental Affinity": "Lunar",
        "Description": "An alloy created by combining Selene Ore and Moonglow Opal. It combines the lunar essence and enchanting properties of Selene Ore with the shimmering and otherworldly qualities of Moonglow Opal, resulting in a material that enhances moon-based magic, grants heightened intuition and perception, and emits a soothing, ethereal glow in the dark."
    },
}

def weapon_types(weapon_shape):
    if weapon_shape == "Stick":
        return weapon_shape
    if weapon_shape == "Sword":
        return weapon_shape
    if weapon_shape == "Club":
        return weapon_shape


def create_weapon(name, special_name, weapon_shape, dmg, rarity_name, material_type, tooltip, is_single_handed,
    is_two_handed, is_enchanted, enhancements_capped, max_enhancements=99999):
    rarity_index = index_rarity_by_name(rarity_name)
    dmg_bonus, legendary_bonus, legendary_bonus_mult = calculate_bonus(rarity_index)

    weapon_xp = 0
    weapon_lvl = 0
    weapon_xp_nxt_lvl = 0

    if special_name is True:
        name = (name)
    else:
        name = (f"{material_type} {weapon_shape}")
    material_type = material[material_type]

    weapon_dict = {
        "Name": name,
        "Dmg": dmg,
        "Material Type": material_type,
        "Weapon Xp": weapon_xp,
        "Weapon Lvl": weapon_lvl,
        "Weapon Next Lvl": int(150 * (1.35 * 1)),
        "Rarity": rarity_name,
        "Dmg Bonus": dmg_bonus,
        "Legendary Bonus": legendary_bonus,
        "Legendary Bonus Mult": legendary_bonus_mult,
        "Tooltip": tooltip,
        "Single Handed": is_single_handed,
        "Two Handed": is_two_handed,
        "Is Enchanted": is_enchanted,
        "Enhanced Count": 0,
        "Enhancements capped": enhancements_capped,
        "Max Enhancements": max_enhancements
    }

    return weapon_dict


# Example
wood_stick_tooltip = "A pretty pathetic wood stick, 'should probably find something better'"
wood_stick = create_weapon("Wood Stick", True, "Stick", 5, "very common", "Wood", wood_stick_tooltip, 1, 0, 0, True, 5)
faeroot_katana_tooltip = "A pretty decent blade"
shinaie_katana = create_weapon("Katana", False, "Katana", 5, "rare", material["Faeroot"]["Name"],
    faeroot_katana_tooltip, 1, 0, 0, False)
weapons_list = [wood_stick, shinaie_katana]
formatted_dict = json.dumps(weapons_list, indent=4)
print(formatted_dict)

# weapon_current_lvl = 1
# weapon_xp_nxt_lvl = 0
# weapon_xp = 0
# wood_stick = {
#    "Name" : "Wood Stick",
#    "Dmg" : 5,
#    "Material Type" : material["wood"],
#    "Weapon Xp" : weapon_xp,
#    "Weapon Lvl" : weapon_xp_nxt_lvl,
#    "Weapon Next Lvl" : int(150*(1.35*weapon_current_lvl)),
#    "Rarity" : RARITIES["Very Common"],
#    "Tooltip" : "A pretty pathetic wood stick, 'should probably find something better' ",
#    "Single Handed" : 1,
#    "Two Handed" : 0,
#    "Is Enchanted" : 0,
#    "Enhanced Count" : 0,
#    "Enhancements capped" : 1,
#    "Max Enhancements" : 10
# }
#
# weapon_material = ''
# club = {
#    "Weapon Material" : weapon_material,
#    "Name" : "Club of {weapon_material}",
#    "Dmg" : 5,
#    "Single Handed" : True,
#    "Two Handed" : False,
#    "Rarity" : "Common",
#    "Tooltip" : "A Blunt Weapon That Is Swung"
# }
# starting_weapon = wood_stick

# Weapons

##--------------------------------------------------------------------------------------------------- Beginner Enimies
# Weapons_Stats = {
#    "Weapons" : {
#        "Club" : {
#        "Name" : "Club",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Blunt Weapon That Is Swung."
#        },
#        "Shiv" : {
#        "Name" : "Shiv",
#        "Dmg" : 8,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Shiv Made From A Readily Avaliable Materials."
#        },
#        "Cleaver" : {
#        "Name" : "Cleaver",
#        "Dmg" : 11,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Cleaver Poorly Made Of ."
#        },
#        "Short Sword" : {
#        "Name" : "Short Sword",
#        "Dmg" : 14,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Short Sword Made From A Carved Peice Of ."
#        },
#        "Longsword" : {
#        "Name" : "Longsword",
#        "Dmg" : 14,
#        "Sinlge Handed" : False,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A Club Made From A Carved Peice Of ."
#        },
#        "Gladius" : {
#        "Name" : "Gladius",
#        "Dmg" : 15,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A gladius Made From A Carved Peice Of . It's I Often A Toy Weapon Given To The Children Of Soldiers."
#        },
#        "Jian" : {
#        "Name" : "Jian",
#        "Dmg" : 15,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Jian Made From A Carved Peice Of ."
#        },
#        "War Axe" : {
#        "Name" : "War Axe",
#        "Dmg" : 16,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A War Axe Made From A Carved Peice Of . Blacksmiths Make These Before Designing A New Weapon As Sort Of A Prototype."
#        },
#        "War Hammer" : {
#        "Name" : "War Hammer",
#        "Dmg" : 17,
#        "Sinlge Handed" : False,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A War Axe Made From A Carved Peice Of . Blacksmiths Make These Before Designing A New Weapon As Sort Of A Prototype."
#        },
#        "Greatsword" : {
#        "Name" : "Greatsword",
#        "Dmg" : 17,
#        "Sinlge Handed" : False,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A Greatsword Made From A Carved Peice Of . Blacksmiths Make These Before Designing A New Weapon As Sort Of A Prototype."
#        },
#        "Ninjato" : {
#        "Name" : "Ninjato",
#        "Dmg" : 17,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Ninjato Made From A Carved Peice Of ."
#        },
#        "Cutlass" : {
#        "Name" : "Cutlass",
#        "Dmg" : 17,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Cutlass Made From A Carved Peice Of ."
#        },
#        "Kodachi" : {
#        "Name" : "Kodachi",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Kodachi Made From A Carved Peice Of ."
#        },
#        "Broadsword" : {
#        "Name" : "Broadsword",
#        "Dmg" : 5,
#        "Sinlge Handed" : False,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A Broadsword Made From A Carved Peice Of ."
#        },
#        "Sabre" : {
#        "Name" : "Sabre",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Sabre Made From A Carved Peice Of ."
#        },
#        "Claymore" : {
#        "Name" : "Claymore",
#        "Dmg" : 5,
#        "Sinlge Handed" : False,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A Claymore Made From A Carved Peice Of ."
#        },
#        "Scimitar" : {
#        "Name" : "Scimitar",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Scimitar Made From A Carved Peice Of ."
#        },
#        "Kriegsmesser" : {
#        "Name" : "Kriegsmesser",
#        "Dmg" : 5,
#        "Sinlge Handed" : False,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A Kriegsmesser Made From A Carved Peice Of ."
#        },
#        "Rapier" : {
#        "Name" : "Rapier",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Rapier Made From A Carved Peice Of ."
#        },
#        "Odachi" : {
#        "Name" : "Odachi",
#        "Dmg" : 5,
#        "Sinlge Handed" : False,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A Odachi Made From A Carved Peice Of ."
#        },
#        "Katana" : {
#        "Name" : "Katana",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A Longsword With A Square Guard And Is Single Sided."
#        },
#        "Tachi" : {
#        "Name" : "Tachi",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Shortsword Sheathed On The Lower Back And Is Single Sided."
#        },
#        "Zweihander" : {
#        "Name" : "Zweihander",
#        "Dmg" : 5,
#        "Sinlge Handed" : False,
#        "Two Handed" : True,
#        "Rarity" : "Common",
#        "Tooltip" : "A Zweihander Is Much Larger Longsword. Due To Its Large Size Isn't Sheathed, But Rather Carried Across The Shoulder"
#        },
#        "Machete" : {
#        "Name" : "Machete",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Broad Blade Used Either As An Aricultural Implement Similar To An Axe, Or In Combat Like A Long-Bladed Knife."
#        },
#        "Shiny Sword" : {
#        "Name" : "Shiny  Sword",
#        "Dmg" : 5,
#        "Sinlge Handed" : True,
#        "Two Handed" : False,
#        "Rarity" : "Common",
#        "Tooltip" : "A Weapon Crafted From Rare Shinies."
#        }
#    },
# }

# print(starting_weapon["Name"])
