import json
import random

def generate_bartender():
    # List of male first names
  male_first_names = ["Adam", "Brian", "Charlie", "David", "Ethan", "Frank", "George", "Henry", "Isaac", "Jack", "Kevin", "Liam", "Michael", "Nathan", "Owen", "Patrick", "Quinn", "Richard", "Steven", "Thomas", "Urban", "Victor", "William", "Xander", "Yvon", "Zachary"]
  
  # List of female first names
  female_first_names = ["Abigail", "Alice", "Amelia", "Anastasia", "Angelina", "Anna", "Aria", "Ashley", "Ava", "Avery", "Beatrice", "Bella", "Brooke", "Camila", "Caroline", "Chloe", "Clara", "Daisy", "Ella", "Elizabeth", "Emily", "Emma", "Eva", "Faith", "Fiona", "Gabrielle", "Hailey", "Hannah", "Harper", "Isabella", "Jenna", "Jessica", "Jocelyn", "Jordan", "Kaitlyn", "Kayla", "Keira", "Kimberly", "Kira", "Lila", "Lily", "Madison", "Maria", "Mary", "Maya", "Melanie", "Mia", "Michelle", "Miranda", "Natalie", "Nicole", "Olivia", "Paige", "Penelope", "Rachel", "Rebecca", "Rose", "Ruby", "Sadie", "Samantha", "Sara", "Sarah", "Scarlett", "Sofia", "Sophia", "Stella", "Summer", "Sydney", "Taylor", "Victoria", "Violet", "Willow", "Zoe", "Zara", "Akiko", "Aiko", "Akemi", "Akira", "Chie", "Chika", "Eiko", "Etsuko", "Fumiko", "Hana", "Haruka", "Hatsue", "Hideko", "Hikari", "Hiromi", "Hisako", "Hitomi", "Ichiko", "Inez", "Izumi", "Junko", "Kaoru", "Katsue", "Kayoko", "Kazue", "Kazuko", "Keiko", "Kumiko", "Kyoko", "Mai", "Makiko", "Mami", "Mariko", "Masako", "Mayumi", "Mieko", "Mika", "Miki", "Miyako", "Natsue", "Natsuko", "Nobue", "Nobuko", "Noriko", "Reiko", "Rin", "Risa", "Rumi", "Sachiko", "Sadako", "Sakiko", "Sakura", "Sanae", "Saori", "Sayako", "Sayuri", "Shizue", "Shizuko", "Sumiko", "Takako", "Tamae", "Tamako", "Tami", "Tomiko", "Tomo", "Tomoe", "Yasu", "Yasuko", "Yoko", "Yoshiko", "Yumiko", "Yuriko", "Yuu"]

  # List of non-binary first names
  non_binary_first_names = ["Alex", "Casey", "Drew", "Eli", "Gem", "Hunter", "Jade", "Kai", "Lena", "Maddy", "Nix", "Ollie", "Quinn", "Rory", "Sam", "Tay", "Violet", "Wren", "Xander", "Yara", "Zander"]
  
  first_names = (male_first_names + female_first_names + non_binary_first_names)
  
  #print(first_names)
  
  # List of fantasy last names
  fantasy_last_names = ["Thornblade", "Moonwhisper", "Stormcaller", "Fireheart", "Duskweaver", "Goldenthorn", "Darkwater", "Shadowfrost", "Skydancer", "Stonefist", "Wildfire", "Moonstrike", "Sunblade", "Stormsong", "Goldeneyes", "Frostwolf", "Duskshadow", "Starsong", "Moonfang", "Thunderstrike", "Lionheart", "Eagleclaw", "Stormblade", "Goldenglow", "Frosttiger", "Inugami", "Kamishiro", "Karyu", "Kazahana", "Kirigakure", "Kirishima", "Kitsune", "Kogane", "Kosaki", "Kurama", "Kusanagi", "Makoto", "Miki", "Minamoto", "Miyamoto", "Mizushima", "Mokuzai", "Mori", "Murasaki", "Nakamura", "Naruto", "Natsume", "Niji", "Oda", "Okamura", "Okumura", "Ookami", "Ookun", "Ootori", "Reiji", "Sakura", "Sakurako", "Sasori", "Satori", "Satoshi", "Sawa", "Shiina", "Shiro", "Takamasa", "Takara", "Takeda", "Takumi", "Tatsumaki", "Touko", "Touma", "Tsubasa", "Uchiha", "Ushijima", "Yamamoto", "Yamato", "Yasutomo", "Yuu"]
  
  # List of personalities
  personalities = ["Kind", "Friendly", "Outgoing", "Loyal", "Generous", "Helpful", "Selfish", "Greedy", "Vengeful", "Manipulative", "Deceitful", "Vicious", "Cruel", "Hateful", "Jealous", "Envious", "Mischievous", "Playful", "Curious", "Clever", "Witty", "Intelligent", "Logical", "Selfish", "Greedy", "Vengeful", "Manipulative", "Deceitful", "Vicious"]
  
  # List of hair colors
  hair_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White", "Gray", "Brown", "Crimson", "Turquoise", "Teal", "Lime", "Magenta", "Cyan", "Olive", "Maroon", "Navy", "Aqua", "Gold", "Silver", "Platinum"]
  
  # List of skin colors
  normal_skin_colors = ["Pale", "Fair", "Light", "Medium", "Tan", "Olive", "Dark", "Ebony", "Brown", "Beige"]
  
  fantasy_skin_colors = ["alabaster", "bronze", "copper", "gold", "platinum", "silver", "amber", "coral", "ivory", "lavender", "magenta", "maroon", "olive", "onyx", "peach", "periwinkle", "pink", "purple", "red", "salmon", "sienna", "turquoise", "violet", "white"]
  
  all_skin_colors = normal_skin_colors + fantasy_skin_colors
  
  # List of eye colors
  eye_colors = ["Amber", "Aquamarine", "Black", "Blue", "Brown", "Chartreuse", "Copper", "Crimson", "Gold", "Gray", "Green", "Hazel", "Indigo", "Lavender", "Maroon", "Navy Blue", "Olive", "Orange", "Pink", "Violet"]
  
  # List of sexualities
  sexualities = ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Asexual"]
  
  # List of fantasy meal specialties
  fantasy_meal_specialties = ["dragon steak", "unicorn ribeye", "griffon wings", "phoenix stir fry", "mermaid sushi", "minotaur burgers", "satyr gyros", "centaur tacos", "pegasus quesadillas", "siren oyster shooters", "gorgon eggs", "harpy nachos", "dryad salad", "nymph fruit platter", "faun sandwiches", "triton seafood platter"]
  
  # List of beer specialties
  beer_specialties = ["ale", "lager", "stout", "pilsner", "wheat beer", "pale ale"]
  
  # List of species
  species = ["Human", "Hybrid", "Demon", "Drider", "Merfolk", "Kobold"]

  # Select a species
  species = random.choice(species)
  if species == "Hybrid":
    species = ["Kitsune", "Lamia", "Changeling"]
    species = random.choice(species)
  else:
    pass

  # List of Tavern architecture types
  tavern_architecture_types = ["Human fantasy", "Elven" , "Demonic", "Drider", "Merfolk", "Kobold"]
  
  # List of RPG classes
  rpg_classes = ["Warrior" , "Thief" , "Bard" , "Mage" , "Paladin" , "Healer" , "Ranger" , "Fighter"]
  
  # List of elemental affinities
  elemental_affinities = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
  
  # List of passive abilities
  passive_abilities = ["improved strength", "improved agility", "improved endurance", "improved intelligence", "improved wisdom", "improved charisma"]
  
  # Determine the bartender's gender
  gender = random.choice(["Male", "Female", "Non-Binary"])
  
  # Select a first name based on the bartender's gender
  if gender == "male":
    first_name = random.choice(male_first_names)
  elif gender == "female":
    first_name = random.choice(female_first_names)
  else:
    first_name = random.choice(non_binary_first_names)
  
  # Select a fantasy last name
  last_name = random.choice(fantasy_last_names)
  
  # Generate the bartender's fantasy name
  fantasy_name = first_name + " " + last_name
  
  # Select a personality
  personality = random.choice(personalities)
  
  # Generate the bartender's height
  height = random.uniform(1.5, 2)

  # Select a hair color
  hair_color = random.choice(hair_colors)
  
  # Select a skin color
  skin_color = random.choice(all_skin_colors)
  
  # Select an eye color
  eye_color = random.choice(eye_colors)
  
  # Select a sexuality
  sexuality = random.choice(sexualities)
  
  # Select a fantasy meal specialty
  fantasy_meal_specialty = random.choice(fantasy_meal_specialties)
  
  # Select a beer specialty
  beer_specialty = random.choice(beer_specialties)
  
  # Generate the bartender's full spouse name
  spouse_first_name = random.choice(first_names)
  spouse_last_name = random.choice(fantasy_last_names)
  spouse_full_name = spouse_first_name + " " + spouse_last_name

  # Generate the bartender's age
  if species == "Human":
    age = random.randint(21, 60)
  elif species == "Kitsune":
    age = random.randint(21, 1200)
  elif species == "Lamia":
    age = random.randint(21, 80)
  elif species == "Changeling":
    age = random.randint(21, 200)
  if species == "Demon":
    age = random.randint(21, 1900)
  if species == "Drider":
    age = random.randint(21, 50)
  if species == "Merfolk":
    age = random.randint(21, 40)
  if species == "Kobold":
    age = random.randint(18, 30)

  # Select a Tavern architecture type based on the bartender's species
  if species == "Human":
    Tavern_architecture_type = random.choice(tavern_architecture_types[:(random.randint(1,2))])
  elif species == "Hybrid":
    if species == "Kitsune":
      Tavern_architecture_type = random.choice(tavern_architecture_types[:(random.randint(1,2))])
    if species == "Lamia":
      Tavern_architecture_type = random.choice(tavern_architecture_types[:(random.randint(1,2))])
    if species == "Changeling":
      Tavern_architecture_type = tavern_architecture_types[1]
  elif species == "Demon":
    Tavern_architecture_type = tavern_architecture_types[2]
  elif species == "Drider":
    Tavern_architecture_type = tavern_architecture_types[3]
  elif species == "Merfolk":
    Tavern_architecture_type = tavern_architecture_types[4]
  elif species == "Kobold":
    Tavern_architecture_type = tavern_architecture_types[5]
  else:
    Tavern_architecture_type = random.choice(tavern_architecture_types)
  
  # Select an RPG class
  rpg_class = random.choice(rpg_classes)
  
  # Select an elemental affinity
  elemental_affinity = random.choice(elemental_affinities)
  
  # Generate the bartender's max HP
  max_hp = random.randint(100, 200)
  
  # Generate the bartender's current HP (slightly less than max HP)
  hp = random.randint(80, max_hp - 20)
  
  # Generate the bartender's damage
  dmg = random.randint(5, 20)
  
  # Generate the bartender's stamina
  stamina = random.randint(100, 200)
  
  # Generate the bartender's magic damage
  magic_dmg = random.randint(5, 20)
  
  # Generate the bartender's mana
  mana = random.randint(100, 200)
  
  # Generate the bartender's spell mana
  spell_mana = random.randint(50, 100)
  
  # Generate the bartender's magic resistance
  magic_resistance = random.randint(5, 15)
  
  # Generate the bartender's armor
  armor = random.randint(5, 15)
  
  # Generate the bartender's Aureliaen Gold Coin count
  agc_count = random.randint(100, 500)
  
  # Generate the bartender's gem count
  gem_count = random.randint(10, 50)
  
  # Generate the bartender's elemental gem count
  elemental_gem_count = random.randint(5, 20)
  
  # Generate the bartender's potion count
  potion_count = random.randint(3, 10)

  # Create the bartender object
  bartender = {
    "Name" : fantasy_name,
    "Personality" : personality,
    "Age" : age,
    "Height" : height,
    "Hair Color" : hair_color,
    "Skin Color" : skin_color,
    "Eye Color" : eye_color,
    "Gender" : gender,
    "Sexuality" : sexuality,
    "Fantasy Meal Specialty" : fantasy_meal_specialty,
    "Beer Specialty" : beer_specialty,
    "Spouse" : spouse_full_name,
    "Species" : species,
    "Tavern Architecture Type" : Tavern_architecture_type,
    "Class" : rpg_class,
    "Elemental Affinity" : elemental_affinity,
    "Max HP" : max_hp,
    "HP" : hp,
    "Damage" : dmg,
    "Stamina" : stamina,
    "Magic Damage" : magic_dmg,
    "Mana" : mana,
    "Spell Mana" : spell_mana,
    "Magic Resistance" : magic_resistance,
    "Armor" : armor,
    "Aureliaen Gold Coins" : agc_count,
    "Gems" : gem_count,
    "Elemental Gems" : elemental_gem_count,
    "Potions" : potion_count,
    "Passive Ability" : random.choice(passive_abilities)
  }
  
  return bartender

## Generate a random bartender
#random_bartender = generate_bartender()
#
#
#for key, value in random_bartender.items():
#  print(key + ": " + str(value))

# Print the bartender's information
print("\n")
apple = 1
while apple != 16:
  print(apple)
  random_bartender = generate_bartender()
  for key, value in random_bartender.items():
    print(key + ": " + str(value))
  print("\n")
  apple = apple + 1

#kistune_female_names = ["Akiko", "Akira", "Amane", "Ami", "Aya", "Ayaka", "Ayane", "Chie", "Chika", "Eiko", "Emi", "Hana", "Haruka", "Hikari", "Hinata", "Honoka", "Kaoru", "Kasumi", "Kayo", "Kazumi", "Kazuko", "Kazumi", "Kikyo", "Kiyoko", "Koharu", "Kumiko", "Mai", "Makoto", "Mana", "Mariko", "Megumi", "Misaki", "Mitsuko", "Nanako", "Nao", "Natsuko", "Nobuko", "Noriko", "Reika", "Reiko", "Riko", "Rin", "Rumi", "Sachiko", "Sakura", "Saki", "Sakiko", "Sakurako", "Sanae", "Satoko", "Sayuri", "Setsuko", "Shizuka", "Takako", "Tamiko", "Tomiko", "Yoshiko", "Yukiko", "Yumiko"]
#
#kistune_male_names = ["Akira", "Atsushi", "Daisuke", "Eiji", "Goro", "Haruto", "Hayato", "Hideki", "Hiroki", "Hisashi", "Ichiro", "Jiro", "Jun", "Kazuhiko", "Kazuki", "Ken", "Kenichi", "Kensuke", "Kota", "Makoto", "Masaru", "Masashi", "Minoru", "Noboru", "Norihiro", "Ryo", "Ryoichi", "Shin", "Shinichi", "Shota", "Shun", "Takashi", "Tatsuo", "Tetsuro", "Tomoyuki", "Toshihiro", "Toshio", "Yasushi", "Yoshikazu", "Yoshimasa", "Yoshinobu", "Yoshio", "Yoshitaka", "Yuichi", "Yuji", "Yusuke", "Yutaka"]
#
#kistune_non_binary_names = ["Aki", "Chiaki", "Haru", "Kana", "Kanako", "Kazu", "Mika", "Miki", "Minako", "Natsu", "Rina", "Ryo", "Sora", "Takeshi", "Yuki", "Yuko"]
#
#lamia_female_names = ["Aiko", "Akira", "Arisa", "Asuka", "Chiaki", "Chie", "Emi", "Eri", "Hana", "Haruka", "Hikari", "Hinata", "Honoka", "Ichigo", "Kaoru", "Kasumi", "Kayo", "Kazumi", "Kazuko", "Kikyo", "Kiyoko", "Koharu", "Kumiko", "Mai", "Makoto", "Mana", "Mariko", "Megumi", "Misaki", "Mitsuko", "Nanako", "Nao", "Natsuko", "Nobuko", "Noriko", "Reika", "Reiko", "Riko", "Rin", "Rumi", "Sachiko", "Sakura", "Saki", "Sakiko", "Sakurako", "Sanae", "Satoko", "Sayuri", "Setsuko", "Shizuka", "Takako", "Tamiko", "Tomiko", "Yoshiko", "Yukiko", "Yumiko"]
#
#lamia_male_names = ["Akira", "Atsushi", "Daisuke", "Eiji", "Goro", "Haruto", "Hayato", "Hideki", "Hiroki", "Hisashi", "Ichiro", "Jiro", "Jun", "Kazuhiko", "Kazuki", "Ken", "Kenichi", "Kensuke", "Kota", "Makoto", "Masaru", "Masashi", "Minoru", "Noboru", "Norihiro", "Ryo", "Ryoichi", "Shin", "Shinichi", "Shota", "Shun", "Takashi", "Tatsuo", "Tetsuro", "Tomoyuki", "Toshihiro", "Toshio", "Yasushi", "Yoshikazu", "Yoshimasa", "Yoshinobu", "Yoshio", "Yoshitaka", "Yuichi", "Yuji", "Yusuke", "Yutaka"]
#
#lamia_non_binary_names = ["Aki", "Chiaki", "Haru", "Kana", "Kanako", "Kazu", "Mika", "Miki", "Minako", "Natsu", "Rina", "Ryo", "Sora", "Takeshi", "Yuki", "Yuko"]
#
#changeling_female_names = ["Aiko", "Akira", "Arisa", "Asuka", "Chiaki", "Chie", "Emi", "Eri", "Hana", "Haruka", "Hikari", "Hinata", "Honoka", "Ichigo", "Kaoru", "Kasumi", "Kayo", "Kazumi", "Kazuko", "Kikyo", "Kiyoko", "Koharu", "Kumiko", "Mai", "Makoto", "Mana", "Mariko", "Megumi", "Misaki", "Mitsuko", "Nanako", "Nao", "Natsuko", "Nobuko", "Noriko", "Reika", "Reiko", "Riko", "Rin", "Rumi", "Sachiko", "Sakura", "Saki", "Sakiko", "Sakurako", "Sanae", "Satoko", "Sayuri", "Setsuko", "Shizuka", "Takako", "Tamiko", "Tomiko", "Yoshiko", "Yukiko", "Yumiko"]
#
#changeling_male_names = ["Akira", "Atsushi", "Daisuke", "Eiji", "Goro", "Haruto", "Hayato", "Hideki", "Hiroki", "Hisashi", "Ichiro", "Jiro", "Jun", "Kazuhiko", "Kazuki", "Ken", "Kenichi", "Kensuke", "Kota", "Makoto", "Masaru", "Masashi", "Minoru", "Noboru", "Norihiro", "Ryo", "Ryoichi", "Shin", "Shinichi", "Shota", "Shun", "Takashi", "Tatsuo", "Tetsuro", "Tomoyuki", "Toshihiro", "Toshio", "Yasushi", "Yoshikazu", "Yoshimasa", "Yoshinobu", "Yoshio", "Yoshitaka", "Yuichi", "Yuji", "Yusuke", "Yutaka"]
#
#changeling_non_binary_names = ["Aki", "Chiaki", "Haru", "Kana", "Kanako", "Kazu", "Mika", "Miki", "Minako", "Natsu", "Rina", "Ryo", "Sora", "Takeshi", "Yuki", "Yuko"]
#
#demon_female_names = ["Aiko", "Akira", "Arisa", "Asuka", "Chiaki", "Chie", "Emi", "Eri", "Hana", "Haruka", "Hikari", "Hinata", "Honoka", "Ichigo", "Kaoru", "Kasumi", "Kayo", "Kazumi", "Kazuko", "Kikyo", "Kiyoko", "Koharu", "Kumiko", "Mai", "Makoto", "Mana", "Mariko", "Megumi", "Misaki", "Mitsuko", "Nanako", "Nao", "Natsuko", "Nobuko", "Noriko", "Reika", "Reiko", "Riko", "Rin", "Rumi", "Sachiko", "Sakura", "Saki", "Sakiko", "Sakurako", "Sanae", "Satoko", "Sayuri", "Setsuko", "Shizuka", "Takako", "Tamiko", "Tomiko", "Yoshiko", "Yukiko", "Yumiko"]
#
#demon_male_names = ["Akira", "Atsushi", "Daisuke", "Eiji", "Goro", "Haruto", "Hayato", "Hideki", "Hiroki", "Hisashi", "Ichiro", "Jiro", "Jun", "Kazuhiko", "Kazuki", "Ken", "Kenichi", "Kensuke", "Kota", "Makoto", "Masaru", "Masashi", "Minoru", "Noboru", "Norihiro", "Ryo", "Ryoichi", "Shin", "Shinichi", "Shota", "Shun", "Takashi", "Tatsuo", "Tetsuro", "Tomoyuki", "Toshihiro", "Toshio", "Yasushi", "Yoshikazu", "Yoshimasa", "Yoshinobu", "Yoshio", "Yoshitaka", "Yuichi", "Yuji", "Yusuke", "Yutaka"]
#
#demon_non_binary_names = ["Aki", "Chiaki", "Haru", "Kana", "Kanako", "Kazu", "Mika", "Miki", "Minako", "Natsu", "Rina", "Ryo", "Sora", "Takeshi", "Yuki", "Yuko"]

##debug_check
#def save():
#    global player_info
#    with open("save.json", "r") as f:
#        player_info = json.load(f)
#        player_sheet = json.dumps(player_info, indent=2)
#    with open("save.json", "w") as f:
#        json.dump(player_info, f, indent=2)
#        json_save_data = json.dumps(player_info, indent=2)
#
#    with open("savestate.json", "r") as f:
#        save_state = json.load(f)
#        debug = json.dumps(save_state, indent=2)#Save State
#        #print(debug)
#        if (save_state["Debug"] == True):
#            print(debug)
#
#def tavern_actions():
#    global player_info
#    with open("save.json", "r") as f:
#        player_info = json.load(f)
#        player_sheet = json.dumps(player_info, indent=2)#Player Sheet
#        #print(player_sheet)
#    print("Would You Like To Eat At The", player_info["Location"], "Tavern\n")
#    tavern_eat = int(input("Yes |1| No |2| \n"))
#    if (tavern_eat == 1):
#        if (int(player_info["Aureliaen Gold Coins"]) < 10):
#            pass
#        if (int(player_info["Aureliaen Gold Coins"]) >= 10):
#            if (int(player_info["Spell Mana"]) != int(player_info["Mana"])):
#                player_info["Aureliaen Gold Coins"] = int(player_info["Aureliaen Gold Coins"] - 10)
#                print("Remaining Coins", int(player_info["Aureliaen Gold Coins"]))
#                print("You Get A Freshly Made Meal, And Your Meal Has Fully Restored Your Mana")
#                player_info["Spell Mana"] = player_info["Mana"]
#                with open("save.json", "w") as f:
#                    json.dump(player_info, f, indent=2)
#                    json_save_data = json.dumps(player_info, indent=2)
#            else:
#                print("Your Already Well Fed")
#                pass
#    if (tavern_eat == 2):
#        pass
#
#save()
#tavern_actions()