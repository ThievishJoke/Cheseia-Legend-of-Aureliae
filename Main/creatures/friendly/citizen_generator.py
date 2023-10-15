
import random
import json
import pathlib
import main.locations.locations as loci

enable_overwrite = True
range_val = 25

def Human_Gen():
    human_list = []
    human_male_first_names = ["Adam", "Brian", "Charlie", "David", "Ethan", "Frank", "George", "Henry", "Isaac", "Jack", "Kevin", "Liam", "Michael", "Nathan", "Owen", "Patrick", "Quinn", "Richard", "Steven", "Thomas", "Urban", "Victor", "William", "Xander", "Yvon", "Zachary"]
    human_female_first_names = ["Abigail", "Alice", "Amelia", "Anastasia", "Angelina", "Anna", "Aria", "Ashley", "Ava", "Avery", "Beatrice", "Bella", "Brooke", "Camila", "Caroline", "Chloe", "Clara", "Daisy", "Ella", "Elizabeth", "Emily", "Emma", "Eva", "Faith", "Fiona", "Gabrielle", "Hailey", "Hannah", "Harper", "Isabella", "Jenna", "Jessica", "Jocelyn", "Jordan", "Kaitlyn", "Kayla", "Keira", "Kimberly", "Kira", "Lila", "Lily", "Madison", "Maria", "Mary", "Maya", "Melanie", "Mia", "Michelle", "Miranda", "Natalie", "Nicole", "Olivia", "Paige", "Penelope", "Rachel", "Rebecca", "Rose", "Ruby", "Sadie", "Samantha", "Sara", "Sarah", "Scarlett", "Sofia", "Sophia", "Stella", "Summer", "Sydney", "Taylor", "Victoria", "Violet", "Willow", "Zoe", "Zara", "Akiko", "Aiko", "Akemi", "Akira", "Chie", "Chika", "Eiko", "Etsuko", "Fumiko", "Hana", "Haruka", "Hatsue", "Hideko", "Hikari", "Hiromi", "Hisako", "Hitomi", "Ichiko", "Inez", "Izumi", "Junko", "Kaoru", "Katsue", "Kayoko", "Kazue", "Kazuko", "Keiko", "Kumiko", "Kyoko", "Mai", "Makiko", "Mami", "Mariko", "Masako", "Mayumi", "Mieko", "Mika", "Miki", "Miyako", "Natsue", "Natsuko", "Nobue", "Nobuko", "Noriko", "Reiko", "Rin", "Risa", "Rumi", "Sachiko", "Sadako", "Sakiko", "Sakura", "Sanae", "Saori", "Sayako", "Sayuri", "Shizue", "Shizuko", "Sumiko", "Takako", "Tamae", "Tamako", "Tami", "Tomiko", "Tomo", "Tomoe", "Yasu", "Yasuko", "Yoko", "Yoshiko", "Yumiko", "Yuriko", "Yuu"]    
    human_non_binary_first_names = ["Alex", "Casey", "Drew", "Eli", "Gem", "Hunter", "Jade", "Kai", "Lena", "Maddy", "Nix", "Ollie", "Quinn", "Rory", "Sam", "Tay", "Violet", "Wren", "Xander", "Yara", "Zander"]
    human_fantasy_last_names = ["Thornblade", "Moonwhisper", "Stormcaller", "Fireheart", "Duskweaver", "Goldenthorn", "Darkwater", "Shadowfrost", "Skydancer", "Stonefist", "Wildfire", "Moonstrike", "Sunblade", "Stormsong", "Goldeneyes", "Frostwolf", "Duskshadow", "Starsong", "Moonfang", "Thunderstrike", "Lionheart", "Eagleclaw", "Stormblade", "Goldenglow", "Frosttiger", "Inugami", "Kamishiro", "Karyu", "Kazahana", "Kirigakure", "Kirishima", "Kitsune", "Kogane", "Kosaki", "Kurama", "Kusanagi", "Makoto", "Miki", "Minamoto", "Miyamoto", "Mizushima", "Mokuzai", "Mori", "Murasaki", "Nakamura", "Naruto", "Natsume", "Niji", "Oda", "Okamura", "Okumura", "Ookami", "Ookun", "Ootori", "Reiji", "Sakura", "Sakurako", "Sasori", "Satori", "Satoshi", "Sawa", "Shiina", "Shiro", "Takamasa", "Takara", "Takeda", "Takumi", "Tatsumaki", "Touko", "Touma", "Tsubasa", "Uchiha", "Ushijima", "Yamamoto", "Yamato", "Yasutomo", "Yuu"]
    personalities = ["Kind", "Friendly", "Outgoing", "Loyal", "Generous", "Helpful", "Selfish", "Greedy", "Vengeful", "Manipulative", "Vicious", "Cruel", "Hateful", "Jealous", "Envious", "Mischievous", "Playful", "Curious", "Clever", "Witty", "Intelligent", "Logical", "Selfish", "Deceitful"]
    hair_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White", "Gray", "Brown", "Crimson", "Turquoise", "Teal", "Lime", "Magenta", "Cyan", "Olive", "Maroon", "Navy", "Aqua", "Gold", "Silver", "Platinum"]
    # List of skin colors
    normal_skin_colors = ["Pale", "Fair", "Light", "Medium", "Tan", "Olive", "Dark", "Ebony", "Brown", "Beige"]
    fantasy_skin_colors = ["Alabaster", "Bronze", "Copper", "Gold", "Platinum", "Silver", "Amber", "Coral", "Ivory", "Lavender", "Magenta", "Maroon", "Olive", "Onyx", "Peach", "Periwinkle", "Pink", "Purple", "Red", "Salmon", "Sienna", "Turquoise", "Violet", "White"]
    all_skin_colors = normal_skin_colors + fantasy_skin_colors
    # create a list of possible eye colors
    eye_colors = ["Amber", "Aquamarine", "Black", "Blue", "Brown", "Chartreuse", "Copper", "Crimson", "Gold", "Gray", "Green", "Hazel", "Indigo", "Lavender", "Maroon", "Navy Blue", "Olive", "Orange", "Pink", "Violet"]
    # create a list of possible RPG classes
    rpg_classes = ["Warrior" , "Thief" , "Bard" , "Mage" , "Paladin" , "Healer" , "Ranger" , "Fighter"]
    # create a list of possible genders
    genders = ["Male", "Female", "Non-Binary"]
    # create a list of possible sexualities
    sexualities = ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Asexual"]
    # create a list of possible elemental affinities
    elemental_affinities = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
    passive_abilities = ["Improved strength", "Improved agility", "Improved endurance", "Improved intelligence", "Improved wisdom", "Improved charisma"]
        # create a function to generate a random human
    def generate_human_features():
        global human
        global enable_overwrite
        personality = random.choice(personalities)
        # randomly select if the human is multicolored
        is_multicolored = random.choice([True, False])
        # if the Human is multicolored, randomly select additional fur colors
        if is_multicolored:
            additional_hair_color_count = random.randint(1,3)
            additional_hair_colors = random.sample(hair_colors, additional_hair_color_count)
        else:
            additional_hair_colors = None
        # randomly select an eye color
        eye_color = random.choice(eye_colors)
        # randomly select if heterochromic
        heterochromia = random.choice([True, False])
        # choose another random color
        if heterochromia == True:
            second_eye_color = random.choice(eye_colors)
        elif heterochromia != True:
            second_eye_color = "None"
        # randomly select a height between 1 and 2 meters
        height = random.uniform(1.5, 2)

        # Select a hair color
        hair_color = random.choice(hair_colors)

        # Select a skin color
        skin_color = random.choice(all_skin_colors)

        # randomly select a gender
        gender = random.choice(genders)

        # Select a first name based on the bartender's gender
        if gender == "male":
            first_name = random.choice(human_male_first_names)
        elif gender == "female":
            first_name = random.choice(human_female_first_names)
        else:
            first_name = random.choice(human_non_binary_first_names)
        # randomly select a sexuality
        def random_sexuality():
            global sexuality
            sexuality = random.choice(sexualities)
            if gender == "Male":
                if sexuality == "Lesbian":
                    return random_sexuality()
            elif gender == "Female":
                if sexuality == "Gay":
                    return random_sexuality()
            else:
                return sexuality
        random_sexuality()
        has_spouse = random.choice([True, False])
        # Generate the Human's full spouse name
        male_female_first_names = human_male_first_names + human_female_first_names
        any_first_name = human_male_first_names + human_female_first_names + human_non_binary_first_names
        if has_spouse == True:
            if sexuality == ("Straight"):
                if gender == ("Male"):
                    spouse_first_name = random.choice(human_female_first_names)
                    spouse_last_name = random.choice(human_fantasy_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                if gender == ("Female"):
                    spouse_first_name = random.choice(human_male_first_names)
                    spouse_last_name = random.choice(human_fantasy_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                elif gender == ("Non-Binary"):
                    spouse_full_name = "None"
                    name = first_name + " " + random.choice(human_fantasy_last_names)
            if sexuality == ("Gay"):
                spouse_first_name = random.choice(human_male_first_names)
                spouse_last_name = random.choice(human_fantasy_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Lesbian"):
                spouse_first_name = random.choice(human_female_first_names)
                spouse_last_name = random.choice(human_fantasy_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Bisexual"):
                spouse_first_name = random.choice(male_female_first_names)
                spouse_last_name = random.choice(human_fantasy_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Pansexual"):
                spouse_first_name = random.choice(any_first_name)
                spouse_last_name = random.choice(human_fantasy_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Asexual"):
                spouse_full_name = "None"
                name = first_name + " " + random.choice(human_fantasy_last_names)
        elif has_spouse == False:
            spouse_full_name = "None"
            name = first_name + " " + random.choice(human_fantasy_last_names)

        # randomly select an age between 16 and 99 years
        age = random.randint(16, 99)

        # Randomly Select An Elemental Affinity
        elemental_affinity = random.choice(elemental_affinities)

        # Randomly Select An RPG lass
        rpg_class = random.choice(rpg_classes)

        # Generate the human's max HP
        max_hp = random.randint(100, 200)

        # Generate the human's current HP (slightly less than max HP)
        hp = random.randint(80, max_hp - 20)

        # Generate the human's damage
        dmg = random.randint(5, 20)

        # Generate the human's stamina
        stamina = random.randint(100, 200)

        # Generate the human's magic damage
        magic_dmg = random.randint(5, 20)

        # Generate the human's mana
        mana = random.randint(100, 200)

        # Generate the human's spell mana
        spell_mana = random.randint(50, 100)

        # Generate the human's magic resistance
        magic_resistance = random.randint(5, 15)

        # Generate the human's armor
        armor = random.randint(5, 15)

        # Generate the human's Aureliaen Gold Coin count

        def random_integer():
            global num
            num = random.randint(0, 1000)
            if (num > 100 and num < 400) or (num > 500 and num < 948):
                return num
            else:
                return random_integer()
        random_integer()
        agc_count = int(num)

        # Generate the human's gem count
        gem_count = random.randint(10, 50)

        # Generate the human's elemental gem count
        elemental_gem_count = random.randint(5, 20)

        # Generate the human's potion count
        potion_count = random.randint(3, 10)
        # Generate Id
        id_number = 1
        for x in human_list:
            id_number = id_number + 1
        # code for generating a human
        # create a dictionary to store the human's attributes
        human = {
            "Id" : id_number,
            "Name" : name,
            "Personality" : personality,
            "Age": age,
            "Height" : height,
            "Hair Color" : hair_color,
            "Skin Color" : skin_color,
            "Eye Color" : eye_color,
            "Heterochromia" : heterochromia,
            "Second Eye Color" : second_eye_color,
            "Is multicolored" : is_multicolored,
            "Additional Hair Colors" : additional_hair_colors,
            "Gender" : gender,
            "Sexuality": sexuality,
            "Spouse" : spouse_full_name,
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
        human_list.append(human)
    # function to save the human list to a json file
    def save_to_json():
        with open("data_humans.json", "w+") as json_file:
            json.dump(human_list, json_file, indent=2)
    if enable_overwrite is True:
        # generate a new human and save it to the json file
        overwrite = input("\nOverwrite? \nYes / No \n")
        overwrite = overwrite.title()
        if (overwrite == "Yes"):
            for i in range(range_val):
                human = generate_human_features()
                save_to_json()
    with open("data_humans.json", "r") as f:
        human_data = json.load(f)
    generator_checker = False
    if generator_checker is True:
        id_num = int(input("\nId Number 1-{} \n".format(range_val)))
        id_num = int(id_num - 1)
        human = human_data[id_num]
        print("")
        for key, value in human.items():
            print(key + ':', value)

def Lamia_Gen():
    lamia_list = []
    lamia_female_names = ["Aiko", "Akira", "Arisa", "Asuka", "Chiaki", "Chie", "Emi", "Eri", "Hana", "Haruka", "Hikari", "Hinata", "Honoka", "Ichigo", "Kaoru", "Kasumi", "Kayo", "Kazumi", "Kazuko", "Kikyo", "Kiyoko", "Koharu", "Kumiko", "Mai", "Makoto", "Mana", "Mariko", "Megumi", "Misaki", "Mitsuko", "Nanako", "Nao", "Natsuko", "Nobuko", "Noriko", "Reika", "Reiko", "Riko", "Rin", "Rumi", "Sachiko", "Sakura", "Saki", "Sakiko", "Sakurako", "Sanae", "Satoko", "Sayuri", "Setsuko", "Shizuka", "Takako", "Tamiko", "Tomiko", "Yoshiko", "Yukiko", "Yumiko"]
    lamia_male_names = ["Akira", "Atsushi", "Daisuke", "Eiji", "Goro", "Haruto", "Hayato", "Hideki", "Hiroki", "Hisashi", "Ichiro", "Jiro", "Jun", "Kazuhiko", "Kazuki", "Ken", "Kenichi", "Kensuke", "Kota", "Makoto", "Masaru", "Masashi", "Minoru", "Noboru", "Norihiro", "Ryo", "Ryoichi", "Shin", "Shinichi", "Shota", "Shun", "Takashi", "Tatsuo", "Tetsuro", "Tomoyuki", "Toshihiro", "Toshio", "Yasushi", "Yoshikazu", "Yoshimasa", "Yoshinobu", "Yoshio", "Yoshitaka", "Yuichi", "Yuji", "Yusuke", "Yutaka"]
    lamia_non_binary_names = ["Aki", "Chiaki", "Haru", "Kana", "Kanako", "Kazu", "Mika", "Miki", "Minako", "Natsu", "Rina", "Ryo", "Sora", "Takeshi", "Yuki", "Yuko"]
    lamia_last_names = ["Crimson", "Serpentine", "Blackscale", "Lunar", "Ember", "Viper", "Abyssal", "Fang", "Dragonfire", "Cobra", "Sandswept", "Abyss", "Crowned", "Siren", "Razorspine", "Dragonheart", "Duskscale", "Ashen", "Bloodclaw", "Flamefang", "Nightshade", "Scorchscale", "Sable", "Siren's Song", "Carnage", "Shadowscale", "Thunderstrike", "Crimsonfang", "Dragon's Bane", "Stormscale", "Eclipse"]
    # Skin Colors
    normal_skin_colors = ["Pale", "Fair", "Light", "Medium", "Tan", "Olive", "Dark", "Ebony", "Brown", "Beige"]
    fantasy_skin_colors = ["Alabaster", "Bronze", "Copper", "Gold", "Platinum", "Silver", "Amber", "Coral", "Ivory", "Lavender", "Magenta", "Maroon", "Olive", "Onyx", "Peach", "Periwinkle", "Pink", "Purple", "Red", "Salmon", "Sienna", "Turquoise", "Violet", "White"]
    all_skin_colors = normal_skin_colors + fantasy_skin_colors
    # Hair Colors
    hair_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White", "Gray", "Brown", "Crimson", "Turquoise", "Teal", "Lime", "Magenta", "Cyan", "Olive", "Maroon", "Navy", "Aqua", "Gold", "Silver", "Platinum"]
    # Scale Colors
    scale_colors = ["Bronze", "Copper", "Gold", "Silver", "Amber", "Emerald Green", "Ebony Black"]
    secondary_scale_color = ["Pink", "Pearl White", "Smoke Black", "Everglade Green"]
    # Eye Colors
    eye_colors = ["Amber", "Aquamarine", "Black", "Blue", "Brown", "Chartreuse", "Copper", "Crimson", "Gold", "Gray", "Green", "Hazel", "Indigo", "Lavender", "Maroon", "Navy Blue", "Olive", "Orange", "Pink", "Violet"]
    # Class
    rpg_classes = ["Warrior" , "Thief" , "Bard" , "Mage" , "Paladin" , "Healer" , "Ranger" , "Fighter"]
    # Gender
    genders = ["Male", "Female", "Non-Binary"]
    # Sexuality
    sexualities = ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Asexual"]
    # Elemental Affinities
    elemental_affinities = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
    passive_abilities = ["improved strength", "improved agility", "improved endurance", "improved intelligence", "improved wisdom", "improved charisma"]
    # Personality
    personalities = ["Kind", "Friendly", "Outgoing", "Loyal", "Generous", "Helpful", "Selfish", "Greedy", "Vengeful", "Manipulative", "Vicious", "Cruel", "Hateful", "Jealous", "Envious", "Mischievous", "Playful", "Curious", "Clever", "Witty", "Intelligent", "Logical", "Selfish", "Deceitful"]
    def generate_lamia_features():
        global lamia
        global enable_overwrite
        # Random Personality
        personality = random.choice(personalities)
        # Random Scale Color
        scale_color = random.choice(scale_colors)
        # Random Multicolor
        is_multicolored = random.choice([True, False])
        # If The Lamia Is Multicolored, Randomly Select Additional Scale Colors
        if is_multicolored:
            additional_scale_color_count = random.randint(1,3)
            additional_scale_colors = random.choice(secondary_scale_color)
        else:
            additional_scale_colors = None
        # Randomly Selects An Eye Color
        eye_color = random.choice(eye_colors)
        # Randomly Select If Heterochromic
        heterochromia = random.choice([True, False])
        # Radnom Second Eye Color
        if heterochromia == True:
            second_eye_color = random.choice(eye_colors)
        elif heterochromia != True:
            second_eye_color = "None"
        # Randomly Select If The Lamia Has Claws
        has_claws = random.choice([True, False])
        if has_claws is True:
            lamia_claw_lengths = ["Stubby", "Short", "Medium", "Long", "Extra Long", "Extremely Long"]
            lamia_claw_length = random.choice(lamia_claw_lengths)
        else:
            lamia_claw_length = "None"
        # Randomly Select If The Lamia Is Fanged
        is_fanged = random.choice([True, False])
        # Randomly Select A Height Between 1 And 2 Meters
        height = random.uniform(1.5, 2)
        # Select A Hair Color
        hair_color = random.choice(hair_colors)
        # Select A Skin Color
        skin_color = random.choice(all_skin_colors)
        # Randomly Select A Gender
        gender = random.choice(genders)
        # Select A First Name Based On The Lamia's Gender
        if gender == "male":
            first_name = random.choice(lamia_male_names)
        elif gender == "female":
            first_name = random.choice(lamia_female_names)
        else:
            first_name = random.choice(lamia_non_binary_names)
        # randomly select a sexuality
        def random_sexuality():
            global sexuality
            sexuality = random.choice(sexualities)
            if gender == "Male":
                if sexuality == "Lesbian":
                    return random_sexuality()
            elif gender == "Female":
                if sexuality == "Gay":
                    return random_sexuality()
            else:
                return sexuality
        random_sexuality()
        # Radomly Choose If A Spouse
        has_spouse = random.choice([True, False])
        # Generate the Lamia's full spouse name
        male_female_first_names = lamia_male_names + lamia_female_names
        any_first_name = lamia_male_names + lamia_female_names + lamia_non_binary_names
        if has_spouse == True:
            if sexuality == ("Straight"):
                if gender == ("Male"):
                    spouse_first_name = random.choice(lamia_female_names)
                    spouse_last_name = random.choice(lamia_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                if gender == ("Female"):
                    spouse_first_name = random.choice(lamia_male_names)
                    spouse_last_name = random.choice(lamia_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                elif gender == ("Non-Binary"):
                    spouse_full_name = "None"
                    name = first_name + " " + random.choice(lamia_last_names)
            if sexuality == ("Gay"):
                spouse_first_name = random.choice(lamia_male_names)
                spouse_last_name = random.choice(lamia_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Lesbian"):
                spouse_first_name = random.choice(lamia_female_names)
                spouse_last_name = random.choice(lamia_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Bisexual"):
                spouse_first_name = random.choice(male_female_first_names)
                spouse_last_name = random.choice(lamia_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Pansexual"):
                spouse_first_name = random.choice(any_first_name)
                spouse_last_name = random.choice(lamia_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Asexual"):
                spouse_full_name = "None"
                name = first_name + random.choice(lamia_last_names)
        elif has_spouse == False:
            spouse_full_name = "None"
            name = first_name + " " + random.choice(lamia_last_names)
        # Random Age
        age = random.randint(16, 140)
        # Randomly Select An Elemental Affinity
        elemental_affinity = random.choice(elemental_affinities)
        # Randomly Select An Class
        rpg_class = random.choice(rpg_classes)
        # Generate the Lamia's max HP
        max_hp = random.randint(100, 200)
        # Generate the Lamia's current HP (slightly less than max HP)
        hp = random.randint(80, max_hp - 20)
        # Generate the Lamia's damage
        dmg = random.randint(5, 20)
        # Generate the Lamia's stamina
        stamina = random.randint(100, 200)
        # Generate the Lamia's magic damage
        magic_dmg = random.randint(5, 20)
        # Generate the Lamia's mana
        mana = random.randint(100, 200)
        # Generate the Lamia's spell mana
        spell_mana = random.randint(50, 100)
        # Generate the Lamia's magic resistance
        magic_resistance = random.randint(5, 15)
        # Generate the Lamia's armor
        armor = random.randint(5, 15)
        # Generate the Lamia's Aureliaen Gold Coin count
        def random_integer():
            global num
            num = random.randint(0, 1000)
            if (num > 100 and num < 400) or (num > 500 and num < 948):
                return num
            else:
                return random_integer()
        random_integer()
        agc_count = int(num)
        # Generate the Lamia's gem count
        gem_count = random.randint(10, 50)
        # Generate the Lamia's elemental gem count
        elemental_gem_count = random.randint(5, 20)
        # Generate the Lamia's potion count
        potion_count = random.randint(3, 10)
        # Generate Id
        id_number = 1
        for x in lamia_list:
            id_number = id_number + 1
        # Code For Generating A Lamia
        # Create A Dictionary To Store The Lamia's attributes
        lamia = {
            "Id" : id_number,
            "Name" : name,
            "Personality" : personality,
            "Age": age,
            "Height" : height,
            "Fur Color" : scale_color,
            "Hair Color" : hair_color,
            "Skin Color" : skin_color,
            "Eye Color" : eye_color,
            "Heterochromia" : heterochromia,
            "Second Eye Color" : second_eye_color,
            "Is multicolored" : is_multicolored,
            "Additional Scale Colors" : additional_scale_colors,
            "Has Claws" : has_claws,
            "Claw Length" : lamia_claw_length,
            "Is Fanged" : is_fanged,
            "Gender" : gender,
            "Sexuality": sexuality,
            "Spouse" : spouse_full_name,
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
        lamia_list.append(lamia)
    # Function To Save The Lamia List To A Json File
    def save_to_json():
        with open("data_lamia.json", "w+") as json_file:
            json.dump(lamia_list, json_file, indent=2)
    if enable_overwrite is True:
        # Generate A New Lamia And Save It To The Json File
        overwrite = input("\nOverwrite? \nYes / No \n")
        overwrite = overwrite.title()
        if (overwrite == "Yes"):
            for i in range(range_val):
                lamia = generate_lamia_features()
                save_to_json()
    with open("data_lamia.json", "r") as f:
        lamia_data = json.load(f)
    generator_checker = False
    if generator_checker is True:
        id_num = int(input("\nId Number 1-{} \n".format(range_val)))
        id_num = int(id_num - 1)
        lamia = lamia_data[id_num]
        print("")
        for key, value in lamia.items():
            print(key + ':', value)

def Changeling_Gen():
    changeling_list = []
    changeling_female_names = ["Aiko", "Akira", "Arisa", "Asuka", "Chiaki", "Chie", "Emi", "Eri", "Hana", "Haruka", "Hikari", "Hinata", "Honoka", "Ichigo", "Kaoru", "Kasumi", "Kayo", "Kazumi", "Kazuko", "Kikyo", "Kiyoko", "Koharu", "Kumiko", "Mai", "Makoto", "Mana", "Mariko", "Megumi", "Misaki", "Mitsuko", "Nanako", "Nao", "Natsuko", "Nobuko", "Noriko", "Reika", "Reiko", "Riko", "Rin", "Rumi", "Sachiko", "Sakura", "Saki", "Sakiko", "Sakurako", "Sanae", "Satoko", "Sayuri", "Setsuko", "Shizuka", "Takako", "Tamiko", "Tomiko", "Yoshiko", "Yukiko", "Yumiko"]
    changeling_male_names = ["Akira", "Atsushi", "Daisuke", "Eiji", "Goro", "Haruto", "Hayato", "Hideki", "Hiroki", "Hisashi", "Ichiro", "Jiro", "Jun", "Kazuhiko", "Kazuki", "Ken", "Kenichi", "Kensuke", "Kota", "Makoto", "Masaru", "Masashi", "Minoru", "Noboru", "Norihiro", "Ryo", "Ryoichi", "Shin", "Shinichi", "Shota", "Shun", "Takashi", "Tatsuo", "Tetsuro", "Tomoyuki", "Toshihiro", "Toshio", "Yasushi", "Yoshikazu", "Yoshimasa", "Yoshinobu", "Yoshio", "Yoshitaka", "Yuichi", "Yuji", "Yusuke", "Yutaka"]
    changeling_non_binary_names = ["Aki", "Chiaki", "Haru", "Kana", "Kanako", "Kazu", "Mika", "Miki", "Minako", "Natsu", "Rina", "Ryo", "Sora", "Takeshi", "Yuki", "Yuko"]
    changeling_last_names = ["Moon", "Star", "Shadow", "Wild", "Dream", "Mist", "Oak", "Willow", "Moth", "Butterfly", "Thorn", "Rose", "Gem", "Pearl", "Storm", "Thunder", "Rain", "River", "Ocean", "Lily", "Lotus", "Rosewood", "Petal", "Bloom", "Sprout", "Grow", "Harvest", "Autumn", "Winter", "Spring", "Summer", "Sky", "Stormy", "Frost", "Snow", "Ice", "Sun", "Sable", "Moonbeam", "Shimmer", "Twilight", "Eclipse", "Aurora", "Nebula", "Cosmic", "Stellar", "Nimble", "Leaf", "Bramble", "Root", "Branch", "Vine", "Bloom", "Seed"]
    personalities = ["Kind", "Friendly", "Outgoing", "Loyal", "Generous", "Helpful", "Selfish", "Greedy", "Vengeful", "Manipulative", "Vicious", "Cruel", "Hateful", "Jealous", "Envious", "Mischievous", "Playful", "Curious", "Clever", "Witty", "Intelligent", "Logical", "Selfish", "Deceitful"]
    # Create A List Of Possible Wing Colors
    changeling_wing_colors = ["Pastel Pink", "Pastel Blue", "Pastel Purple", "Pastel Green", "Pastel Yellow", "Pastel Orange", "Pastel Peach", "Pastel Lavender", "Pastel Coral", "Pastel Mint", "Pastel Sky Blue", "Pastel Rose", "Pastel Lemon", "Pastel Coral Pink", "Pastel Periwinkle", "Pastel Seafoam", "Pastel Sage", "Pastel Dusty Rose", "Pastel Aqua", "Pastel Violet", "Pastel Light Blue", "Pastel Apricot", "Pastel Seafoam Green", "Pastel Light Pink", "Pastel Light Purple", "Pastel Light Green"]
    # Create A List Of Possible Wing Patterns
    changeling_wing_patterns = ["Solid", "Striped", "Spotted", "Speckled", "Swirled", "Marbled", "Veined", "Ribboned", "Netted", "Lace", "Checkered", "Dappled", "Stippled", "Mosaic", "Filigree", "Embroidered", "Damask", "Argyle", "Plaid", "Houndstooth", "Herringbone", "Polka Dot", "Gingham", "Tartan", "Jacquard", "Camo", "Brocade", "Quilted", "Trellis", "Fretwork", "Lattice", "Maze", "Labyrinth", "Diamond", "Geometric"]
    # Create A List Of Possible Wing Shapes
    changeling_wing_shapes = ["Butterfly", "Bat", "Bird", "Angel", "Demon", "Dragon", "Faerie", "Insect", "Moth", "Owl", "Pegasus", "Phoenix", "Unicorn", "Wyvern", "Gargoyle", "Griffin", "Harpy", "Hydra", "Kraken", "Minotaur", "Nephilim", "Roc", "Sphinx", "Tengu", "Valkyrie", "Yokai", "Zephyr", "Celestial", "Infernal", "Nebula", "Stellar", "Meteor", "Eclipse", "Orbital", "Cosmic", "Galactic", "Planetary", "Solar", "Lunar", "Comet", "Aurora", "Nova"]
    # A List Of Possible Wing Glow
    changeling_wing_glow_brightness = ["Dim", "Moderate", "Bright", "Radiant", "Glimmering", "Luminous", "Shimmering", "Gleaming", "Resplendent", "Glowing", "Burning", "Blazing", "Flaming", "Incandescent", "Scintillating", "Flickering", "Twinkling", "Sparkling", "Glittering", "Shining", "Dazzling", "Radiating", "Illuminated", "Lit", "Glistening", "Glossy", "Polished", "Mirrored", "Reflective", "Brightening", "Brightened", "Brightest", "Radiantly", "Radiantness", "Radiance", "Radiantness"]
    # A List Of Possible Wing Sizes
    changeling_wing_sizes = ["Tiny", "Small", "Medium", "Large", "Extra Large", "Giant"]
    # A List Of Possible Skin Tones
    changeling_skin_tones = ["Pale", "Fair", "Porcelain", "Ivory", "Ethereal", "Luminous", "Radiant", "Opalescent", "Pearlescent", "Glimmering", "Shimmering", "Glowing", "Radiant", "Iridescent", "Lustrous", "Gleaming", "Serene", "Peaceful", "Elegant", "Graceful", "Exquisite", "Delicate", "Fine", "Lavender", "Lilac", "Lily", "Alabaster", "Moonstone", "Silvery", "Mint", "Pearl"]
    # A List Of Possilbe Hair Colors
    changeling_hair_colors = ["Fire Blonde", "Aqua Blonde", "Earth Blonde", "Natural Blonde", "Air Blonde", "Lightning Blonde", "Light Blonde", "Dark Blonde", "Eclipse Blonde", "Lunar Blonde", "Soul Blonde", "Blood Blonde"]
    # A List Of Possible Hair Styles
    female_changeling_hair_styles = ["Long and Wavy", "Short and Spiky", "Pixie Cut", "Bob", "Braided", "Long Curls", "Half Up Half Down", "Ponytail", "Bun", "Updo", "Messy Bun", "Braided Updo", "Fishtail Braid", "French Braid", "Cornrows", "Loose Waves", "Sleek and Straight", "Afro", "Twisted Locks", "Dreadlocks", "Bantu Knots", "Faux Hawk", "Mohawk", "Frohawk", "Cornrow Braids", "Box Braids", "Senegalese Twists", "Kinky Twists", "Marley Twists", "Havana Twists", "Jumbo Twists"]
    male_changeling_hair_styles = ["Buzz Cut", "Crew Cut", "Slick Back", "Spiky Top", "Pompadour", "Fade", "Undercut", "Side Part", "Slicked Side Part", "Shaved Sides", "Caesar Cut", "Short Afro", "Short Dreadlocks", "Short Braids", "Short Twists", "Short Marley Twists", "Short Kinky Twists", "Short Havana Twists", "Short Jumbo Twists", "Short Senegalese Twists", "Short Box Braids", "Short Faux Hawk", "Short Mohawk", "Short Frohawk"]
    # A List Of Possible Eye Colors
    changeling_eye_colors = ["Ice Blue", "Sky Blue", "Electric Blue", "Ocean Blue", "Midnight Blue", "Turquoise Blue", "Aqua Blue", "Lunar Blue", "Snowflake Blue", "Glow Blue", "Radiant Blue", "Shadow Blue", "Ghost Blue", "Mint Blue", "Celestial Blue", "Pearl White", "Diamond White", "Glow White", "Radiant White", "Ghost White", "Angel White", "Snow White", "Moonstone White", "Starry White", "Heavenly White", "Blizzard White"]
    # A List Of Possible RPG Classes
    rpg_classes = ["Warrior", "Thief", "Mage", "Paladin", "Healer", "Fighter"]
    # A List Of Possible Genders
    genders = ["Male", "Female", "Non-Binary"]
    # A List Of Possible Sexualities
    sexualities = ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Asexual"]
    # create a list of possible elemental affinities
    elemental_affinities = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
    passive_abilities = ["improved strength", "improved agility", "improved endurance", "improved intelligence", "improved wisdom", "improved charisma"]
    # A Function To Generate A Random Changeling
    def generate_changeling_features():
        global changeling
        global enable_overwrite
        # Random Personality
        personality = random.choice(personalities)
        # Random Wing Color
        wing_color = random.choice(changeling_wing_colors)
        # Random Wing Pattern
        wing_pattern = random.choice(changeling_wing_patterns)
        # Random Wing Shape
        wing_shape = random.choice(changeling_wing_shapes)
        # Random Wing Glow
        wing_glow = random.choice([True, False])
        if wing_glow:
            changeling_wing_glow = random.choice(changeling_wing_glow_brightness)
        else:
            changeling_wing_glow = "None"
        # Random Wing Size
        wing_size = random.choice(changeling_wing_sizes)
        # Random Skin Tone
        skin_color = random.choice(changeling_skin_tones)
        # Random Hair Color
        hair_color = random.choice(changeling_hair_colors)
        # Random Eye Color
        eye_color = random.choice(changeling_eye_colors)
        heterochromia = random.choice([True, False])
        if heterochromia == True:
            second_eye_color = random.choice(changeling_eye_colors)
        elif heterochromia != True:
            second_eye_color = "None"
        # Random Gender
        gender = random.choice(genders)
        # Random Hair Style
        if gender == "Male":
            hair_style = random.choice(male_changeling_hair_styles)
        elif gender == "Female":
            hair_style = random.choice(female_changeling_hair_styles)
        elif gender == "Non-Binary":
            hair_styles = male_changeling_hair_styles + female_changeling_hair_styles
            hair_style = random.choice(hair_styles)
        # Random Height
        height = random.uniform(1.5, 2)
        # Random First Name Based On Gender
        if gender == "male":
            first_name = random.choice(changeling_male_names)
        elif gender == "female":
            first_name = random.choice(changeling_female_names)
        else:
            first_name = random.choice(changeling_non_binary_names)
        # Random Sexuality
        def random_sexuality():
            global sexuality
            sexuality = random.choice(sexualities)
            if gender == "Male":
                if sexuality == "Lesbian":
                    return random_sexuality()
            elif gender == "Female":
                if sexuality == "Gay":
                    return random_sexuality()
            else:
                return sexuality
        random_sexuality()
        has_spouse = random.choice([True, False])
        # Generate The Changeling's Full Spouse Name
        male_female_first_names = changeling_male_names + changeling_female_names
        any_first_name = changeling_male_names + changeling_female_names + changeling_non_binary_names
        if has_spouse == True:
            if sexuality == ("Straight"):
                if gender == ("Male"):
                    spouse_first_name = random.choice(changeling_female_names)
                    spouse_last_name = random.choice(changeling_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                if gender == ("Female"):
                    spouse_first_name = random.choice(changeling_male_names)
                    spouse_last_name = random.choice(changeling_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                elif gender == ("Non-Binary"):
                    spouse_full_name = "None"
                    name = first_name + " " + random.choice(changeling_last_names)
            if sexuality == ("Gay"):
                spouse_first_name = random.choice(changeling_male_names)
                spouse_last_name = random.choice(changeling_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Lesbian"):
                spouse_first_name = random.choice(changeling_female_names)
                spouse_last_name = random.choice(changeling_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Bisexual"):
                spouse_first_name = random.choice(male_female_first_names)
                spouse_last_name = random.choice(changeling_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Pansexual"):
                spouse_first_name = random.choice(any_first_name)
                spouse_last_name = random.choice(changeling_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Asexual"):
                spouse_full_name = "None"
                name = first_name + " " + random.choice(changeling_last_names)
        elif has_spouse == False:
            spouse_full_name = "None"
            #Name Combo
            name = first_name + " " + random.choice(changeling_last_names)
        # randomly select an age between 16 and 200 years
        age = random.randint(16, 200)
        # Randomly Select An Elemental Affinity
        elemental_affinity = random.choice(elemental_affinities)
        # Randomly Select An RPG lass
        rpg_class = random.choice(rpg_classes)
        # Generate the Changeling's max HP
        max_hp = random.randint(100, 200)
        # Generate the Changeling's current HP (slightly less than max HP)
        hp = random.randint(80, max_hp - 20)
        # Generate the Changeling's damage
        dmg = random.randint(5, 20)
        # Generate the Changeling's stamina
        stamina = random.randint(100, 200)
        # Generate the Changeling's magic damage
        magic_dmg = random.randint(5, 20)
        # Generate the Changeling's mana
        mana = random.randint(100, 200)
        # Generate the Changeling's spell mana
        spell_mana = random.randint(50, 100)
        # Generate the Changeling's magic resistance
        magic_resistance = random.randint(5, 15)
        # Generate the Changeling's armor
        armor = random.randint(5, 15)
        # Generate the Changeling's Aureliaen Gold Coin count
        def random_integer():
            global num
            num = random.randint(0, 1000)
            if (num > 100 and num < 400) or (num > 500 and num < 948):
                return num
            else:
                return random_integer()
        random_integer()
        agc_count = int(num)
        # Generate the Changeling's gem count
        gem_count = random.randint(10, 50)
        # Generate the Changeling's elemental gem count
        elemental_gem_count = random.randint(5, 20)
        # Generate the Changeling's potion count
        potion_count = random.randint(3, 10)
        # Generate Id
        id_number = 1
        for x in changeling_list:
            id_number = id_number + 1
        # Code For Generating A Changeling
        # Create A Dictionary To Store The Changeling's Attributes
        changeling = {
            "Id" : id_number,
            "Name" : name,
            "Personality" : personality,
            "Age": age,
            "Height" : height,
            "Hair Color" : hair_color,
            "Hair Style" : hair_style,
            "Skin Color" : skin_color,
            "Eye Color" : eye_color,
            "Wing Color" : wing_color,
            "Wing Pattern" : wing_pattern,
            "Wing Shape" : wing_shape,
            "Wing Size" : wing_size,
            "Wing Glow" : changeling_wing_glow,
            "Heterochromia" : heterochromia,
            "Second Eye Color" : second_eye_color,
            "Gender" : gender,
            "Sexuality": sexuality,
            "Spouse" : spouse_full_name,
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
        changeling_list.append(changeling)
    # function to save the changeling list to a json file
    def save_to_json():
        with open("data_changeling.json", "w+") as json_file:
            json.dump(changeling_list, json_file, indent=2)
    if enable_overwrite is True:
        # generate a new changeling and save it to the json file
        overwrite = input("\nOverwrite? \nYes / No \n")
        overwrite = overwrite.title()
        if (overwrite == "Yes"):
            for i in range(range_val):
                changeling = generate_changeling_features()
                save_to_json()
    with open("data_changeling.json", "r") as f:
        changeling_data = json.load(f)
    generator_checker = False
    if generator_checker is True:
        id_num = int(input("\nId Number 1-{} \n".format(range_val)))
        id_num = int(id_num - 1)
        changeling = changeling_data[id_num]
        print("")
        for key, value in changeling.items():
            print(key + ':', value)

def Kitsune_Gen():
    debug = True
    kitsune_list = []
    kitsune_female_names = ["Akiko", "Akira", "Amane", "Ami", "Aya", "Ayaka", "Ayane", "Chie", "Chika", "Eiko", "Emi", "Hana", "Haruka", "Hikari", "Hinata", "Honoka", "Kaoru", "Kasumi", "Kayo", "Kazumi", "Kazuko", "Kazumi", "Kikyo", "Kiyoko", "Koharu", "Kumiko", "Mai", "Makoto", "Mana", "Mariko", "Megumi", "Misaki", "Mitsuko", "Nanako", "Nao", "Natsuko", "Nobuko", "Noriko", "Reika", "Reiko", "Riko", "Rin", "Rumi", "Sachiko", "Sakura", "Saki", "Sakiko", "Sakurako", "Sanae", "Satoko", "Sayuri", "Setsuko", "Shizuka", "Takako", "Tamiko", "Tomiko", "Yoshiko", "Yukiko", "Yumiko"]
    kitsune_male_names = ["Akira", "Atsushi", "Daisuke", "Eiji", "Goro", "Haruto", "Hayato", "Hideki", "Hiroki", "Hisashi", "Ichiro", "Jiro", "Jun", "Kazuhiko", "Kazuki", "Ken", "Kenichi", "Kensuke", "Kota", "Makoto", "Masaru", "Masashi", "Minoru", "Noboru", "Norihiro", "Ryo", "Ryoichi", "Shin", "Shinichi", "Shota", "Shun", "Takashi", "Tatsuo", "Tetsuro", "Tomoyuki", "Toshihiro", "Toshio", "Yasushi", "Yoshikazu", "Yoshimasa", "Yoshinobu", "Yoshio", "Yoshitaka", "Yuichi", "Yuji", "Yusuke", "Yutaka"]
    kitsune_non_binary_names = ["Aki", "Chiaki", "Haru", "Kana", "Kanako", "Kazu", "Mika", "Miki", "Minako", "Natsu", "Rina", "Ryo", "Sora", "Takeshi", "Yuki", "Yuko"]
    kitsune_last_names = ["Akiyama", "Fujimoto", "Hirano", "Ichikawa", "Ikeda", "Inoue", "Iwasaki", "Kawamura", "Kobayashi", "Kudo", "Matsumoto", "Miyamoto", "Nakamura", "Nakano", "Narita", "Nishimura", "Ogawa", "Ohno", "Okada", "Okamoto", "Oshima", "Sakamoto", "Sasaki", "Shimizu", "Sugimoto", "Suzuki", "Takahashi", "Takano", "Takayama", "Tanaka", "Tamura", "Ueda", "Watanabe", "Yamada", "Yamaguchi", "Yamamoto", "Yamashita", "Yoshida", "Yoshimoto", "Yoshimura", "Yoshizawa", "Yukimura", "Yunoki", "Zennosuke"]
    personalities = ["Kind", "Friendly", "Outgoing", "Loyal", "Generous", "Helpful", "Selfish", "Greedy", "Vengeful", "Manipulative", "Vicious", "Cruel", "Hateful", "Jealous", "Envious", "Mischievous", "Playful", "Curious", "Clever", "Witty", "Intelligent", "Logical", "Selfish", "Deceitful"]
    # create a list of possible fur colors
    fur_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White", "Gray", "Brown", "Crimson", "Turquoise", "Teal", "Lime", "Magenta", "Cyan", "Olive", "Maroon", "Navy", "Aqua", "Gold", "Silver", "Platinum"]
    # create a list of possible fur patterns
    fur_patterns = ["Solid", "Spotted", "Striped", "Splotchy", "Speckled", "Patches", "Mottled", "Marbled", "Freckled", "Blotchy", "Brindle", "Swirled", "Rosetted", "Saddled", "Ticked"]
    hair_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White", "Gray", "Brown", "Crimson", "Turquoise", "Teal", "Lime", "Magenta", "Cyan", "Olive", "Maroon", "Navy", "Aqua", "Gold", "Silver", "Platinum"]
    tail_types = ["Smooth", "Bushy", "Fluffy", "Tufted", "Knotted", "Twisted", "Braided", "Curled", "Wavy"]
    tail_lengths = ["Short", "Long", "Lengthy", "Flowing"]
    tail_gradients = ["Blended", "Transitioning"]
    tail_sparkles = ["Subtle Sparkle", "Shimmer", "Glistening", "Prismatic Shimmer"]
    tail_translucences = ["Pattern", "Color", "Gradient", "Pattern & Color"]
    # A List Of Possible Skin Tones
    normal_skin_colors = ["Pale", "Fair", "Light", "Medium", "Tan", "Olive", "Dark", "Ebony", "Brown", "Beige"]
    fantasy_skin_colors = ["Alabaster", "Bronze", "Copper", "Gold", "Platinum", "Silver", "Amber", "Coral", "Ivory", "Lavender", "Magenta", "Maroon", "Olive", "Onyx", "Peach", "Periwinkle", "Pink", "Purple", "Red", "Salmon", "Sienna", "Turquoise", "Violet", "White"]
    all_skin_colors = normal_skin_colors + fantasy_skin_colors
    # A List Of Possible Eye Colors
    eye_colors = ["Amber", "Aquamarine", "Black", "Blue", "Brown", "Chartreuse", "Copper", "Crimson", "Gold", "Gray", "Green", "Hazel", "Indigo", "Lavender", "Maroon", "Navy Blue", "Olive", "Orange", "Pink", "Violet"]
    # A List Of Possible RPG Classes
    rpg_classes = ["Warrior" , "Thief" , "Bard" , "Mage" , "Paladin" , "Healer" , "Ranger" , "Fighter"]
    # A List Of Possible Genders
    genders = ["Male", "Female", "Non-Binary"]
    # A List Of Possible Sexualities
    sexualities = ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Asexual"]
    # create a list of possible elemental affinities
    elemental_affinities = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
    passive_abilities = ["improved strength", "improved agility", "improved endurance", "improved intelligence", "improved wisdom", "improved charisma"]
    # create a function to generate a random Kitsune
    def generate_kitsune_features():
        global kitsune
        global enable_overwrite
        # Random Personality
        personality = random.choice(personalities)
        # Random Fur Color
        fur_color = random.choice(fur_colors)
        # Random Multicolor
        is_multicolored = random.choice([True, False])
        # If The Kitsune Is Multicolored, Randomly Select Additional Fur Colors
        if is_multicolored:
            additional_fur_color_count = random.randint(1,3)
            additional_fur_colors = random.sample(fur_colors, additional_fur_color_count)
        else:
            additional_fur_colors = None
        # randomly select a fur pattern
        fur_pattern = random.choice(fur_patterns)
        # randomly select an eye color
        eye_color = random.choice(eye_colors)
        # randomly select if heterochromic
        heterochromia = random.choice([True, False])
        # choose another random color
        if heterochromia == True:
            second_eye_color = random.choice(eye_colors)
        elif heterochromia != True:
            second_eye_color = "None"
        tail_type = random.choice(tail_types)
        # randomly select tail length
        tail_length = random.choice(tail_lengths)
        # randonly choose if there is a gradient and or sparkle
        if is_multicolored == True:
            has_gradient = random.choice([True, False])
            if has_gradient == True:
                tail_gradient = random.choice(tail_gradients)
            if has_gradient == False:
                tail_gradient = "None"
        elif is_multicolored == False:
            has_gradient = False
            tail_gradient = "None"
        has_sparkle = random.choice([True, False])
        if has_sparkle == True:
            tail_sparkle = random.choice(tail_sparkles)
        if has_sparkle != True:
            tail_sparkle = "None"
        
        # randomly choose if there is a translucence tail trait
        has_translucence = random.choice([True, False])
        if has_translucence == True:
            tail_translucence = random.choice(tail_translucences)
            if has_gradient == False:
                tail_translucence != "Gradient"
                tail_translucence = random.choice(["Pattern", "Color"])
        if has_translucence != True:
            tail_translucence = "None"
        # randomly select a tail count between 0 and 15
        tail_count = random.randint(0, 15)
        if tail_count < 10 and tail_count >= 5:
            tail_count = tail_count + (random.randint(0, 4))
            if debug == True and tail_count != 5:
                print("base 5 tail count boosted")
        elif tail_count == 10:
            tail_count = tail_count + (random.randint(0, 5))
            if debug == True and tail_count != 10:
                print("base 10 tail count boosted")
        elif tail_count == 15:
            tail_count = tail_count + (random.randint(0, 10))
            if debug == True and tail_count != 15 and tail_count != 25:
                print("base 15 tail count boosted")
            elif tail_count == 25:
                tail_count = tail_count + (random.randint(0,30))
                if debug == True and tail_count !=25:
                    print("base 25 tail count boosted")
        tail_glow = random.choice([True, False])
        # randomly select if the Kitsune has claws
        has_claws = random.choice([True, False])
        if has_claws is True:
            kitsune_claw_lengths = ["Short", "Medium", "Long", "Extra Long"]
            kitsune_claw_length = random.choice(kitsune_claw_lengths)
        else:
            kitsune_claw_length = "None"
        # randomly select if the Kitsune is fox fanged
        is_fanged = random.choice([True, False])
        # randomly select a height between 1 and 2 meters
        height = random.uniform(1.5, 2)
        # Select a hair color
        hair_color = random.choice(hair_colors)
        # Select a skin color
        skin_color = random.choice(all_skin_colors)
        # randomly select a gender
        gender = random.choice(genders)
        # Select a first name based on the kitsune's gender
        if gender == "male":
            first_name = random.choice(kitsune_male_names)
        elif gender == "female":
            first_name = random.choice(kitsune_female_names)
        else:
            first_name = random.choice(kitsune_non_binary_names)
        # randomly select a sexuality
        def random_sexuality():
            global sexuality
            global sexual_pref
            sexuality = random.choices(sexualities, weights=(87.2, 5.25, 5.25, 2.1, 0.1, 0.1), k=1)
            sexual_pref = random.choice(sexuality)
            if gender == "Male":
                if sexual_pref == "Lesbian":
                    return random_sexuality()
            elif gender == "Female":
                if sexual_pref == "Gay":
                    return random_sexuality()
            else:
                return sexual_pref
        random_sexuality()
        has_spouse = random.choice([True, False])
        # Generate the Kitsune's full spouse name
        male_female_first_names = kitsune_male_names + kitsune_female_names
        any_first_name = kitsune_male_names + kitsune_female_names + kitsune_non_binary_names
        if has_spouse == True:
            if sexual_pref == ("Straight"):
                if gender == ("Male"):
                    spouse_first_name = random.choice(kitsune_female_names)
                    spouse_last_name = random.choice(kitsune_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                if gender == ("Female"):
                    spouse_first_name = random.choice(kitsune_male_names)
                    spouse_last_name = random.choice(kitsune_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                elif gender == ("Non-Binary"):
                    spouse_full_name = "None"
                    name = first_name + " " + random.choice(kitsune_last_names)
            if sexual_pref == ("Gay"):
                spouse_first_name = random.choice(kitsune_male_names)
                spouse_last_name = random.choice(kitsune_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexual_pref == ("Lesbian"):
                spouse_first_name = random.choice(kitsune_female_names)
                spouse_last_name = random.choice(kitsune_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexual_pref == ("Bisexual"):
                spouse_first_name = random.choice(male_female_first_names)
                spouse_last_name = random.choice(kitsune_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexual_pref == ("Pansexual"):
                spouse_first_name = random.choice(any_first_name)
                spouse_last_name = random.choice(kitsune_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexual_pref == ("Asexual"):
                spouse_full_name = "None"
                name = first_name + " " + random.choice(kitsune_last_names)
        elif has_spouse == False:
            spouse_full_name = "None"
            #Name Combo
            name = first_name + " " + random.choice(kitsune_last_names)
        # randomly select an age between 16 and 99 years
        age = random.randint(16, 99)
        # add the age based on the tail count (each tail adds 100 years)
        age += tail_count * 100
        # Randomly Select An Elemental Affinity
        elemental_affinity = random.choice(elemental_affinities)
        # Randomly Select An RPG lass
        rpg_class = random.choice(rpg_classes)
        # Generate the Kitsune's max HP
        max_hp = random.randint(100, 200)
        # Generate the Kitsune's current HP (slightly less than max HP)
        hp = random.randint(80, max_hp - 20)
        # Generate the Kitsune's damage
        dmg = random.randint(5, 20)
        # Generate the Kitsune's stamina
        stamina = random.randint(100, 200)
        # Generate the Kitsune's magic damage
        magic_dmg = random.randint(5, 20)
        # Generate the Kitsune's mana
        mana = random.randint(100, 200)
        # Generate the Kitsune's spell mana
        spell_mana = random.randint(50, 100)
        # Generate the Kitsune's magic resistance
        magic_resistance = random.randint(5, 15)
        # Generate the Kitsune's armor
        armor = random.randint(5, 15)
        # Generate the Kitsune's Aureliaen Gold Coin count
        def random_integer():
            global num
            num = random.randint(0, 1000)
            if (num > 100 and num < 400) or (num > 500 and num < 948):
                return num
            else:
                return random_integer()
        random_integer()
        agc_count = int(num)
        # Generate the Kitsune's gem count
        gem_count = random.randint(10, 50)
        # Generate the Kitsune's elemental gem count
        elemental_gem_count = random.randint(5, 20)
        # Generate the Kitsune's potion count
        potion_count = random.randint(3, 10)
        # Generate Id
        id_number = 1
        for x in kitsune_list:
            id_number = id_number + 1
        # Code For Generating A Kitsune
        # Create A Dictionary To Store The Kitsune's Attributes
        kitsune = {
            "Id" : id_number,
            "Name" : name,
            "Personality" : personality,
            "Age": age,
            "Height" : height,
            "Fur Color" : fur_color,
            "Hair Color" : hair_color,
            "Skin Color" : skin_color,
            "Eye Color" : eye_color,
            "Heterochromia" : heterochromia,
            "Second Eye Color" : second_eye_color,
            "Is multicolored" : is_multicolored,
            "Additional Fur Colors" : additional_fur_colors,
            "Fur Pattern" : fur_pattern,
            "Tail Type" : tail_type,
            "Tail Length" : tail_length,
            "Tail Gradient" : tail_gradient,
            "Tail Sparkle" : tail_sparkle,
            "Tail Translucence" : tail_translucence,
            "Tail Count" : tail_count,
            "Tail Glow" : tail_glow,
            "Has Claws" : has_claws,
            "Claw Length" : kitsune_claw_length,
            "Is Fox Fanged" : is_fanged,
            "Gender" : gender,
            "Sexuality": sexuality,
            "Spouse" : spouse_full_name,
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
        kitsune_list.append(kitsune)
    # function to save the kitsune list to a json file
    def save_to_json():
        with open("data_kitsune.json", "w+") as json_file:
            json.dump(kitsune_list, json_file, indent=2)
    if enable_overwrite is True:
        # generate a new kitsune and save it to the json file
        overwrite = input("\nOverwrite? \nYes / No \n")
        overwrite = overwrite.title()
        if (overwrite == "Yes"):
            for i in range(range_val):
                kitsune = generate_kitsune_features()
                save_to_json()
    with open("data_kitsune.json", "r") as f:
        kitsune_data = json.load(f)
    generator_checker = True
    if generator_checker is True:
        id_num = int(input("\nId Number 1-{} \n".format(range_val)))
        id_num = int(id_num - 1)
        kitsune = kitsune_data[id_num]
        print("")
        for key, value in kitsune.items():
            print(key + ':', value)

def Demon_Gen():
    demon_list = []
    demon_female_names = ["Aiko", "Akira", "Arisa", "Asuka", "Chiaki", "Chie", "Emi", "Eri", "Hana", "Haruka", "Hikari", "Hinata", "Honoka", "Ichigo", "Kaoru", "Kasumi", "Kayo", "Kazumi", "Kazuko", "Kikyo", "Kiyoko", "Koharu", "Kumiko", "Mai", "Makoto", "Mana", "Mariko", "Megumi", "Misaki", "Mitsuko", "Nanako", "Nao", "Natsuko", "Nobuko", "Noriko", "Reika", "Reiko", "Riko", "Rin", "Rumi", "Sachiko", "Sakura", "Saki", "Sakiko", "Sakurako", "Sanae", "Satoko", "Sayuri", "Setsuko", "Shizuka", "Takako", "Tamiko", "Tomiko", "Yoshiko", "Yukiko", "Yumiko"]
    demon_male_names = ["Akira", "Atsushi", "Daisuke", "Eiji", "Goro", "Haruto", "Hayato", "Hideki", "Hiroki", "Hisashi", "Ichiro", "Jiro", "Jun", "Kazuhiko", "Kazuki", "Ken", "Kenichi", "Kensuke", "Kota", "Makoto", "Masaru", "Masashi", "Minoru", "Noboru", "Norihiro", "Ryo", "Ryoichi", "Shin", "Shinichi", "Shota", "Shun", "Takashi", "Tatsuo", "Tetsuro", "Tomoyuki", "Toshihiro", "Toshio", "Yasushi", "Yoshikazu", "Yoshimasa", "Yoshinobu", "Yoshio", "Yoshitaka", "Yuichi", "Yuji", "Yusuke", "Yutaka"]
    demon_non_binary_names = ["Aki", "Chiaki", "Haru", "Kana", "Kanako", "Kazu", "Mika", "Miki", "Minako", "Natsu", "Rina", "Ryo", "Sora", "Takeshi", "Yuki", "Yuko"]
    demon_last_names = ["#%#(*@", "#*@@#%"]
    personalities = ["Kind", "Friendly", "Outgoing", "Loyal", "Generous", "Helpful", "Selfish", "Greedy", "Vengeful", "Manipulative", "Vicious", "Cruel", "Hateful", "Jealous", "Envious", "Mischievous", "Playful", "Curious", "Clever", "Witty", "Intelligent", "Logical", "Selfish", "Deceitful"]
    tail_types = ["Smooth", "Knotted", "Twisted", "Curled"]
    # A List Of Possible Skin Tones
    skin_tones = ["Ebony", "Maroon", "Apple Red", "Red Copper", "Salmon"]
    # Hair
    demon_hair_colors = ["red", "black", "white", "blonde", "green", "purple", "blue", "pink", "silver", "gold"]
    # A List Of Possible Eye Colors
    eye_colors = ["Amber", "Aquamarine", "Black", "Blue", "Brown", "Chartreuse", "Copper", "Crimson", "Gold", "Gray", "Green", "Hazel", "Indigo", "Lavender", "Maroon", "Navy Blue", "Olive", "Orange", "Pink", "Violet"]
    # A List Of Possible RPG Classes
    rpg_classes = ["Warrior" , "Thief" , "Bard" , "Mage" , "Paladin" , "Healer" , "Ranger" , "Fighter"]
    # A List Of Possible Genders
    genders = ["Male", "Female", "Non-Binary"]
    # A List Of Possible Sexualities
    sexualities = ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Asexual"]
    # create a list of possible elemental affinities
    elemental_affinities = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
    passive_abilities = ["improved strength", "improved agility", "improved endurance", "improved intelligence", "improved wisdom", "improved charisma"]
    # create a function to generate a random Demon
    def generate_demon_features():
        global demon
        global enable_overwrite
        # Random Personality
        personality = random.choice(personalities)
        # Hair
        hair_color = random.choice(demon_hair_colors)
        # randomly select an eye color
        eye_color = random.choice(eye_colors)
        # randomly select if heterochromic
        heterochromia = random.choice([True, False])
        # choose another random color
        if heterochromia == True:
            second_eye_color = random.choice(eye_colors)
        elif heterochromia != True:
            second_eye_color = "None"
        # Random Tail Type
        tail_type = random.choice(tail_types)
        # randomly select a height between 1 and 2 meters
        height = random.uniform(1.5, 2)
        # Select a skin color
        skin_color = random.choice(skin_tones)
        # randomly select a gender
        gender = random.choice(genders)
        # Select a first name based on the kitsune's gender
        if gender == "male":
            first_name = random.choice(demon_male_names)
        elif gender == "female":
            first_name = random.choice(demon_female_names)
        else:
            first_name = random.choice(demon_non_binary_names)
        # randomly select a sexuality
        def random_sexuality():
            global sexuality
            sexuality = random.choice(sexualities)
            if gender == "Male":
                if sexuality == "Lesbian":
                    return random_sexuality()
            elif gender == "Female":
                if sexuality == "Gay":
                    return random_sexuality()
            else:
                return sexuality
        random_sexuality()
        has_spouse = random.choice([True, False])
        # Generate the Kitsune's full spouse name
        male_female_first_names = demon_male_names + demon_female_names
        any_first_name = demon_male_names + demon_female_names + demon_non_binary_names
        if has_spouse == True:
            if sexuality == ("Straight"):
                if gender == ("Male"):
                    spouse_first_name = random.choice(demon_female_names)
                    spouse_last_name = random.choice(demon_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                if gender == ("Female"):
                    spouse_first_name = random.choice(demon_male_names)
                    spouse_last_name = random.choice(demon_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                elif gender == ("Non-Binary"):
                    spouse_full_name = "None"
                    name = first_name + " " + random.choice(demon_last_names)
            if sexuality == ("Gay"):
                spouse_first_name = random.choice(demon_male_names)
                spouse_last_name = random.choice(demon_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Lesbian"):
                spouse_first_name = random.choice(demon_female_names)
                spouse_last_name = random.choice(demon_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Bisexual"):
                spouse_first_name = random.choice(male_female_first_names)
                spouse_last_name = random.choice(demon_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Pansexual"):
                spouse_first_name = random.choice(any_first_name)
                spouse_last_name = random.choice(demon_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Asexual"):
                spouse_full_name = "None"
                name = first_name + " " + random.choice(demon_last_names)
        elif has_spouse == False:
            spouse_full_name = "None"
            #Name Combo
            name = first_name + " " + random.choice(demon_last_names)
        # randomly select an age between 16 and 99 years
        age = random.randint(16, 99)
        # Randomly Select An Elemental Affinity
        elemental_affinity = random.choice(elemental_affinities)
        # Randomly Select An RPG lass
        rpg_class = random.choice(rpg_classes)
        # Generate the Demon's max HP
        max_hp = random.randint(100, 200)
        # Generate the Demon's current HP (slightly less than max HP)
        hp = random.randint(80, max_hp - 20)
        # Generate the Demon's damage
        dmg = random.randint(5, 20)
        # Generate the Demon's stamina
        stamina = random.randint(100, 200)
        # Generate the Demon's magic damage
        magic_dmg = random.randint(5, 20)
        # Generate the Demon's mana
        mana = random.randint(100, 200)
        # Generate the Demon's spell mana
        spell_mana = random.randint(50, 100)
        # Generate the Demon's magic resistance
        magic_resistance = random.randint(5, 15)
        # Generate the Demon's armor
        armor = random.randint(5, 15)
        # Generate the Demon's Aureliaen Gold Coin count
        def random_integer():
            global num
            num = random.randint(0, 1000)
            if (num > 100 and num < 400) or (num > 500 and num < 948):
                return num
            else:
                return random_integer()
        random_integer()
        agc_count = int(num)
        # Generate the Demon's gem count
        gem_count = random.randint(10, 50)
        # Generate the Demon's elemental gem count
        elemental_gem_count = random.randint(5, 20)
        # Generate the Demon's potion count
        potion_count = random.randint(3, 10)
        # Generate Id
        id_number = 1
        for x in demon_list:
            id_number = id_number + 1
        # Code For Generating A Demon
        # Create A Dictionary To Store The Demon's Attributes
        demon = {
            "Id" : id_number,
            "Name" : name,
            "Personality" : personality,
            "Age": age,
            "Height" : height,
            "Hair Color" : hair_color,
            "Skin Color" : skin_color,
            "Eye Color" : eye_color,
            "Heterochromia" : heterochromia,
            "Second Eye Color" : second_eye_color,
            "Tail Type" : tail_type,
#            "Has Claws" : has_claws,
#            "Claw Length" : demon_claw_length,
#            "Is Fanged" : is_fanged,
            "Gender" : gender,
            "Sexuality": sexuality,
            "Spouse" : spouse_full_name,
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
        demon_list.append(demon)
    # function to save the demon list to a json file
    def save_to_json():
        with open("data_demon.json", "w+") as json_file:
            json.dump(demon_list, json_file, indent=2)
    if enable_overwrite is True:
        # generate a new demon and save it to the json file
        overwrite = input("\nOverwrite? \nYes / No \n")
        overwrite = overwrite.title()
        if (overwrite == "Yes"):
            for i in range(range_val):
                demon = generate_demon_features()
                save_to_json()
    with open("data_demon.json", "r") as f:
        demon_data = json.load(f)
    generator_checker = False
    if generator_checker is True:
        id_num = int(input("\nId Number 1-{} \n".format(range_val)))
        id_num = int(id_num - 1)
        demon = demon_data[id_num]
        print("")
        for key, value in demon.items():
            print(key + ':', value)

def Drider_Gen():
    drider_list = []
    #--------------Names
    drider_female_names = ['Aria', 'Beth', 'Clara', 'Diana', 'Ella', 'Fae', 'Gwen', 'Hazel', 'Iris', 'Jade', 'Kaitlyn', 'Lila', 'Mia', 'Natalie', 'Olivia', 'Paige', 'Quinn', 'Rae', 'Sophia', 'Taryn', 'Ursula', 'Violet', 'Willow', 'Xandra', 'Ylva', 'Zara']
    drider_male_first_names = ['Arakel', 'Armen', 'Balthazar', 'Basir', 'Cernunnos', 'Erevan', 'Gorx', 'Hiram', 'Illidan', 'Krios', 'Lysandros', 'Mordekai', 'Nergal', 'Othniel', 'Petr', 'Qamar', 'Rhadamanthys', 'Samael', 'Thamuz', 'Uriel', 'Vepar', 'Wyrm', 'Xerxes', 'Ymir', 'Zarek']
    drider_non_binary_names = ["Arix", "Chryl", "Dael", "Erys", "Fynn", "Gael", "Hux", "Iyra", "Jax", "Kael", "Lyr", "Myrx", "Nix", "Orys", "Pyra", "Qael", "Rhyx", "Syr", "Tyrn", "Uryx", "Vyx", "Wael", "Xyr", "Yrn", "Zael"]
    drider_last_names = ["Arachne", "Webber", "Spinneret", "Cocoon", "Venom", "Silk", "Chitin", "Crawler", "Hunter", "Prey", "Trapper", "Capturer", "Fang", "Claw", "Bite", "Sting", "Insect", "Spider", "Web", "Prey", "Lurker", "Shadow", "Silencer", "Stalker", "Predator", "Killer", "Pouncer", "Jumper", "Leaper", "Glimmer", "Glow", "Shimmer", "Glimpse", "Glint", "Gleam", "Sparkle", "Twinkle", "Shine", "Luster", "Radiance", "Glitter", "Glimmer"]
    # A List Of Possible Personalities
    drider_personalities = ["Gregarious", "Reserved", "Assertive", "Submissive", "Cunning", "Naive", "Honest", "Deceptive", "Compassionate", "Heartless", "Loyal", "Unreliable", "Generous", "Stingy", "Adventurous", "Cautious", "Curious", "Indifferent"]
    #--------------Skin/Skin Tone
    drider_skin_tones = ["Ash", "Ebony", "Charcoal", "Sable", "Obsidian", "Onyx", "Midnight", "Jet", "Raven", "Soot"]
    drider_skin_shine = ["Matte", "Satin", "Glossy", "Shimmer", "Silk", "Pearl", "Lustrous", "Gleaming", "Radiant", "Shine"]
    #--------------Eyes
    drider_eye_colors = ["Golden", "Silver", "Bronze", "Copper", "Emerald", "Sapphire", "Amethyst", "Topaz", "Ruby", "Diamond"]
    drider_eye_glow_colors = ["Green", "Red", "Blue", "Purple", "Yellow", "Orange", "Pink", "Turquoise", "Crimson", "Electric Blue"]
    drider_eye_shapes = ["Round", "Almond", "Slanted"]
    drider_eye_glow_brightness = ["Dim", "Muted", "Bright", "Intense", "Blinding"]
    #--------------Scales
    drider_scale_colors = ["Scarlet", "Violet", "Gold", "Silver", "Rose", "Emerald", "Sapphire", "Amethyst", "Turquoise", "Cobalt"]
    drider_scale_undertones = ["Crimson", "Violet", "Gold", "Silver", "Rose", "Emerald", "Sapphire", "Amethyst", "Turquoise", "Cobalt"]
    drider_scale_patterns = ["Spotted", "Striped", "Dotted", "Mottled", "Marbled", "Veined", "Swirled", "Branched", "Lined"]
    drider_scale_textures = ["Smooth", "Rough", "Bumpy", "Sleek", "Fuzzy", "Soft", "Velvet", "Silky", "Glossy"]
    drider_scale_heights = ["Thigh", "Upper Thigh", "Hip", "Abdomen", "Chest"]
    drider_scale_lower_heights = ["Above the shin", "Mid-shin", "Lower shin", "Above the calf", "Mid-calf", "Lower calf", "Above the knee", "Mid-thigh", "Lower thigh"]
    drider_scale_sizes = ["Small", "Small-Medium", "Medium"]
    drider_scale_shapes = ["Smooth", "Rounded", "Sharp", "Serrated", "Flattened", "Wavy", "Spiky", "Pointed", "Ridged"]
    drider_scale_body_patterns = ["Striped", "Spotted", "Dotted", "Mottled", "Marbled", "Veined", "Swirled", "Branched", "Lined"]
    #--------------Claws
    drider_claw_colors = ["Silver", "Bronze", "Copper", "Black", "Golden", "Emerald", "Sapphire", "Amethyst", "Turquoise", "Crimson"]
    drider_claw_alt_colors = ["Silver", "Bronze", "Copper", "Black", "Golden", "Emerald", "Sapphire", "Amethyst", "Turquoise", "Crimson"]
    drider_claw_serration_levels = ["Smooth", "Tiny", "Small", "Moderate", "Sharp", "Serrated", "Razor"]
    drider_claw_lengths = ["Small", "Small-Medium", "Medium"]
    #--------------Fangs
    drider_fang_colors = ["Silver", "Bronze", "Copper", "Black", "Golden", "Emerald", "Sapphire", "Amethyst", "Turquoise", "Crimson"]
    #--------------Hair
    drider_hair_colors = ["Black", "Silver", "Blonde", "Red", "Brown", "Green", "Blue", "Purple", "Yellow", "Orange"]
    drider_hair_undertones = ["Violet", "Gold", "Silver", "Rose", "Emerald", "Sapphire", "Amethyst", "Turquoise", "Cobalt", "Crimson"]
    drider_hair_lengths = ["Medium", "Long", "Very Long"]
    #--------------Spider Legs (On back)
    drider_leg_colors = ["Ebony", "Chestnut", "Dark Brown", "Tan", "Golden", "Honey", "Cinnamon", "Rust", "Red", "Burgundy", "Maroon", "Dark Red"]
    drider_leg_alt_colors = ["Onyx", "Mahogany", "Sienna", "Caramel", "Amber", "Sable", "Auburn", "Crimson", "Scarlet", "Brick", "Coral", "Cherry"]
    drider_height_leg_lengths = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
    #--------------Ears (Elven Shape)
    drider_ear_lengths = ["Small", "Small-Medium", "Medium"]
    drider_earings = ["None"]
    #--------------Pet/Minion
    drider_spider_pet_types = ["crimson", "wolf", "frostbite", "widower", "moth"]
    # A List Of Possible RPG Classes
    rpg_classes = ["Warrior" , "Thief" , "Bard" , "Mage" , "Paladin" , "Healer" , "Ranger" , "Fighter"]
    # A List Of Possible Genders
    genders = ["Male", "Female", "Non-Binary"]
    # A List Of Possible Sexualities
    sexualities = ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Asexual"]
    # create a list of possible elemental affinities
    elemental_affinities = ["Fire", "Aqua", "Earth", "Natural", "Air", "Lightning", "Light", "Dark", "Eclipse", "Lunar", "Soul", "Blood"]
    # Drider Specific Passives
    drider_passive_abilities = ["Stealth", "Speed", "Agility", "Night Vision", "Poison Resistance", "Web Weaving", "Climbing", "Spider Sense", "Enhanced Strength", "Enhanced Senses", "Silent Movement", "Tough Exoskeleton", "Poison Secretion", "Sticky Webbing", "Spinneret Control", "Claws", "Fangs", "Sharp Vision", "Compound eyes", "Immortality (limited)", "Regeneration (limited)"]
    def drider_outfit():
        #list of materials
        mat_silken = "Silken"
        mat_rusted = "Rusted"
        mat_leather = "Leather"
        mat_chitin = "Chitinous"
        mat_keratin = "Keratinous"
        drider_armor_materials = [mat_silken, mat_rusted, mat_leather, mat_chitin, mat_keratin]
        #list of armor pieces
        head_armor = ["Helm", "Mask", "Hood", "None"]
        chest_armor = ["Chest Plate", "Robe", "Cuirass", "None"]
        shoulder_armor = ["Shoulder Pads", "Pauldron", "None"]
        glove_armor = ["Gauntlets", "Bracers", "Vambrace", "Wrist Guard", "None"]
        leg_armor = ["Greaves", "Thigh Plate", "Shin Guard", "None"]
        foot_armor = ["Sabatons", "Plate Boots", "Boots", "None"]
        asthetic_armor = ["Cape", "Cloak", "Mantle", "None"]
        drider_clothing_materials = ["Silk", "Velvet", "Cotton", "Linen", "Wool", "Satin"]
        drider_clothing_types = ["Tunic & Trousers", "Robe", "Vest & Trousers", "Dress", "Tunic & Skirt", "Corset Dress"]
        helm_drider_armor_variations = []
        shoulder_drider_armor_variations = []
        glove_drider_armor_variations = []
        leg_drider_armor_variations = []
        vanity_drider_armor_variations = []
        for armor in head_armor:
            if armor == "None":
                pass
            else:
                for material in drider_armor_materials:
                    helm_drider_armor_variations.append(f"{material} {armor}")
                for material_1 in drider_armor_materials:
                    for material_2 in drider_armor_materials:
                        if material_1 != material_2:
                            helm_drider_armor_variations.append(f"{material_1} and {material_2} {armor}")
                for material_3 in drider_armor_materials:
                    if material_2 != material_3 and material_1 != material_3 and material_2 != material_1:
                        helm_drider_armor_variations.append(f"{material_1}, {material_2}, and {material_3} {armor}")
        #print(helm_drider_armor_variations)
        helmet = random.choice(helm_drider_armor_variations)
        #print("Material Randomizer Helmet: ", helmet)
        for armor in shoulder_armor:
            if armor == "None":
                pass
            else:
                for material in drider_armor_materials:
                    shoulder_drider_armor_variations.append(f"{material} {armor}")
                for material_1 in drider_armor_materials:
                    for material_2 in drider_armor_materials:
                        if material_1 != material_2:
                            shoulder_drider_armor_variations.append(f"{material_1} and {material_2} {armor}")
                for material_3 in drider_armor_materials:
                    if material_2 != material_3 and material_1 != material_3 and material_2 != material_1:
                        shoulder_drider_armor_variations.append(f"{material_1}, {material_2}, and {material_3} {armor}")
        #print(shoulder_drider_armor_variations)
        shoulder = random.choice(shoulder_drider_armor_variations)
        #print("Material Randomizer Shoulder: ", shoulder)
        for armor in glove_armor:
            if armor == "None":
                pass
            else:
                for material in drider_armor_materials:
                    glove_drider_armor_variations.append(f"{material} {armor}")
                for material_1 in drider_armor_materials:
                    for material_2 in drider_armor_materials:
                        if material_1 != material_2:
                            glove_drider_armor_variations.append(f"{material_1} and {material_2} {armor}")
                for material_3 in drider_armor_materials:
                    if material_2 != material_3 and material_1 != material_3 and material_2 != material_1:
                        glove_drider_armor_variations.append(f"{material_1}, {material_2}, and {material_3} {armor}")
        #print(glove_drider_armor_variations)
        glove = random.choice(glove_drider_armor_variations)
        #print("Material Randomizer Glove: ", glove)
        for armor in leg_armor:
            if armor == "None":
                pass
            else:
                for material in drider_armor_materials:
                    leg_drider_armor_variations.append(f"{material} {armor}")
                for material_1 in drider_armor_materials:
                    for material_2 in drider_armor_materials:
                        if material_1 != material_2:
                            leg_drider_armor_variations.append(f"{material_1} and {material_2} {armor}")
                for material_3 in drider_armor_materials:
                    if material_2 != material_3 and material_1 != material_3 and material_2 != material_1:
                        leg_drider_armor_variations.append(f"{material_1}, {material_2}, and {material_3} {armor}")
        #print(leg_drider_armor_variations)
        leg = random.choice(leg_drider_armor_variations)
        #print("Material Randomizer Leg: ", leg)
        for armor in asthetic_armor:
            if armor == "None":
                pass
            else:
                for material in drider_armor_materials:
                    while material == mat_rusted or material == mat_chitin or material == mat_keratin:
                        random_index = random.randint(0,2)
                        material = (drider_armor_materials[random_index])
                    vanity_drider_armor_variations.append(f"{material} {armor}")
                for material_1 in drider_armor_materials:
                    for material_2 in drider_armor_materials:
                        if material_1 != material_2:
                            while (material_1 == mat_rusted and material_2 == mat_chitin) or (material_1 == mat_rusted and material_2 == mat_keratin) or material_1 == mat_keratin and material_2 == mat_chitin:
                                random_index = random.randint(0,2)
                                material_1 = (drider_armor_materials[random_index])
                            vanity_drider_armor_variations.append(f"{material_1} and {material_2} {armor}")
                for material_3 in drider_armor_materials:
                    if material_2 != material_3 and material_1 != material_3 and material_2 != material_1:
                        vanity_drider_armor_variations.append(f"{material_1}, {material_2}, and {material_3} {armor}")
        #print(vanity_drider_armor_variations)
        vanity = random.choice(vanity_drider_armor_variations)
        #print("Material Randomizer Vanity: ", vanity)
        #randomly select armor pieces from each list
        #-------------------------------------------------------
        armor_clothing_material = random.choice(drider_armor_materials)
        selected_head_armor = random.choice(head_armor)
        if selected_head_armor == "None":
            head_material = "None"
            helmet = ("Head Armor: None")
        else:
            head_material = armor_clothing_material
            helmet = (f"Head Armor: {helmet}")
        #-------------------------------------------------------
        selected_chest_armor = random.choice(chest_armor)
        if selected_chest_armor == "None":
            selected_chest_armor = random.choice(drider_clothing_types)
            chest_material = random.choice(drider_clothing_materials)
            chest = (f"Chest Armor: {chest_material} {selected_chest_armor}")
        else:
            chest_material = armor_clothing_material
            chest = (f"Chest Armor: {chest_material} {selected_chest_armor}")
        #-------------------------------------------------------
        selected_shoulder_armor = random.choice(shoulder_armor)
        if selected_shoulder_armor == "None":
            shoulder_material = "None"
        else:
            shoulder_material = armor_clothing_material
            if selected_shoulder_armor == "Robe":
                random_index = random.randint(0,2)
                shoulder_material = (drider_armor_materials[random_index])
            shoulder = (f"Shoulder Armor: {shoulder}")
        #-------------------------------------------------------
        selected_glove_armor = random.choice(glove_armor)
        if selected_glove_armor == "None":
            glove_material = "None"
        else:
            glove_material = armor_clothing_material
            glove = (f"Glove Armor: {glove}")
        #-------------------------------------------------------
        selected_leg_armor = random.choice(leg_armor)
        if selected_leg_armor == "None":
            leg_material = "None"
        else:
            leg_material = armor_clothing_material
            leg = (f"Leg Armor: {leg}")
        #-------------------------------------------------------
        selected_foot_armor = random.choice(foot_armor)
        if selected_foot_armor == "None":
            selected_foot_armor = "Boot"
            foot_material = mat_leather
            foot = (f"Foot Armor: {foot_material} {selected_foot_armor}")
        else:
            foot_material = armor_clothing_material
            foot = (f"Foot Armor: {foot_material} {selected_foot_armor}")
        #-------------------------------------------------------
        selected_asthetic_armor = random.choice(asthetic_armor)
        if selected_asthetic_armor == "None":
            asthetic_material = "None"
            vanity = ("Aesthetic Armor: None")
        elif selected_asthetic_armor != "None":
            asthetic_material = armor_clothing_material
            while asthetic_material == "Scrap Iron" or asthetic_material == "Chitin" or asthetic_material == "Keratin":
                random_index = random.randint(0,2)
                asthetic_material = (drider_armor_materials[random_index])
            vanity = (f"Aesthetic Armor: {vanity}")
        #-------------------------------------------------------
        if selected_head_armor == "None" and head_material == "None":
            helmet = ("Head Armor: None")
        if selected_shoulder_armor == "None" and shoulder_material == "None":
            shoulder = ("Shoulder Armor: None")
        if selected_glove_armor == "None" and glove_material == "None":
            glove = ("Glove Armor: None")
        if selected_leg_armor == "None" and leg_material == "None":
            leg = ("Leg Armor: None")
        if asthetic_armor == "None" and asthetic_material == "None":
            vanity = (f"Aesthetic Armor: {asthetic_material} {selected_asthetic_armor}")

        #print the chosen armor pieces and their respective materials
        #print(helmet)
        #print(chest)
        #print(shoulder)
        #print(glove)
        #print(leg)
        #print(foot)
        #print(vanity)
        outfit = [helmet, chest, shoulder, glove, leg, foot, vanity]
        return outfit
    gen_outfit = drider_outfit()
    # create a function to generate a random Drider
    def generate_drider_features():
        global drider
        global enable_overwrite
        # Random Personality
        personality = random.choice(drider_personalities)
        # Select a skin color
        skin_color = random.choice(drider_skin_tones)
        skin_shine = random.choice(drider_skin_shine)
        # randomly select an eye color
        eye_color = random.choice(drider_eye_colors)
        eye_glow_color = random.choice(drider_eye_glow_colors)
        eye_shape = random.choice(drider_eye_shapes)
        eye_glow_brightness = random.choice(drider_eye_glow_brightness)
        # randomly select if heterochromic
        heterochromia = random.choice([True, False])
        if heterochromia == True:
            second_eye_color = random.choice(drider_eye_colors)
        elif heterochromia != True:
            second_eye_color = "None"
        # Scales
        scale_color = random.choice(drider_scale_colors)
        scale_undertone = random.choice(drider_scale_undertones)
        scale_pattern = random.choice(drider_scale_patterns)
        scale_texture = random.choice(drider_scale_textures)
        scale_height = random.choice(drider_scale_heights)
        scale_lower_height = random.choice(drider_scale_lower_heights)
        scale_size = random.choice(drider_scale_sizes)
        scale_shape = random.choice(drider_scale_shapes)
        scale_body_pattern = random.choice(drider_scale_body_patterns)
        # Claws
        has_claws = random.choice([True, False])
        if has_claws is True:
            claw_color = random.choice(drider_claw_colors)
            claw_alt_color = random.choice(drider_claw_alt_colors)
            claw_serration = random.choice(drider_claw_serration_levels)
            claw_length = random.choice(drider_claw_lengths)
        else:
            claw_color = "None"
            claw_alt_color = "None"
            claw_serration = "None"
            claw_length = "None"
        # Fangs
        fang_color = random.choice(drider_fang_colors)
        # Height
        height = random.uniform(1.5, 2)
        # Hair
        hair_color = random.choice(drider_hair_colors)
        hair_undertone = random.choice(drider_hair_undertones)
        hair_length = random.choice(drider_hair_lengths)
        # Spider Legs
        leg_color = random.choice(drider_leg_colors)
        leg_alt_color = random.choice(drider_leg_alt_colors)
        leg_length = random.choice(drider_height_leg_lengths)
        # Outfit
        outfit = gen_outfit
        # Ears
        ear_length = random.choice(drider_ear_lengths)
        earings = random.choice(drider_earings)
        #Pet/Mini
        pet = random.choice(drider_spider_pet_types)
        # randomly select a gender
        gender = random.choice(genders)
        # Select a first name based on the Drider's gender
        if gender == "male":
            first_name = random.choice(drider_male_first_names)
        elif gender == "female":
            first_name = random.choice(drider_female_names)
        else:
            first_name = random.choice(drider_non_binary_names)
        # randomly select a sexuality
        def random_sexuality():
            global sexuality
            sexuality = random.choice(sexualities)
            if gender == "Male":
                if sexuality == "Lesbian":
                    return random_sexuality()
            elif gender == "Female":
                if sexuality == "Gay":
                    return random_sexuality()
            else:
                return sexuality
        random_sexuality()
        has_spouse = random.choice([True, False])
        # Generate the Drider's full spouse name
        male_female_first_names = drider_male_first_names + drider_female_names
        any_first_name = drider_male_first_names + drider_female_names + drider_non_binary_names
        if has_spouse == True:
            if sexuality == ("Straight"):
                if gender == ("Male"):
                    spouse_first_name = random.choice(drider_female_names)
                    spouse_last_name = random.choice(drider_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                if gender == ("Female"):
                    spouse_first_name = random.choice(drider_male_first_names)
                    spouse_last_name = random.choice(drider_last_names)
                    spouse_full_name = spouse_first_name + " " + spouse_last_name
                    name = first_name + " " + spouse_last_name
                elif gender == ("Non-Binary"):
                    spouse_full_name = "None"
                    name = first_name + " " + random.choice(drider_last_names)
            if sexuality == ("Gay"):
                spouse_first_name = random.choice(drider_male_first_names)
                spouse_last_name = random.choice(drider_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Lesbian"):
                spouse_first_name = random.choice(drider_female_names)
                spouse_last_name = random.choice(drider_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Bisexual"):
                spouse_first_name = random.choice(male_female_first_names)
                spouse_last_name = random.choice(drider_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Pansexual"):
                spouse_first_name = random.choice(any_first_name)
                spouse_last_name = random.choice(drider_last_names)
                spouse_full_name = spouse_first_name + " " + spouse_last_name
                name = first_name + " " + spouse_last_name
            if sexuality == ("Asexual"):
                spouse_full_name = "None"
                name = first_name + " " + random.choice(drider_last_names)
        elif has_spouse == False:
            spouse_full_name = "None"
            #Name Combo
            name = first_name + " " + random.choice(drider_last_names)
        # randomly select an age between 16 and 99 years
        age = random.randint(16, 99)
        # Randomly Select An Elemental Affinity
        elemental_affinity = random.choice(elemental_affinities)
        # Randomly Select An RPG lass
        rpg_class = random.choice(rpg_classes)
        # Generate the Drider's max HP
        max_hp = random.randint(100, 200)
        # Generate the Drider's current HP (slightly less than max HP)
        hp = random.randint(80, max_hp - 20)
        # Generate the Drider's damage
        dmg = random.randint(5, 20)
        # Generate the Drider's stamina
        stamina = random.randint(100, 200)
        # Generate the Drider's magic damage
        magic_dmg = random.randint(5, 20)
        # Generate the Drider's mana
        mana = random.randint(100, 200)
        # Generate the Drider's spell mana
        spell_mana = random.randint(50, 100)
        # Generate the Drider's magic resistance
        magic_resistance = random.randint(5, 15)
        # Generate the Drider's armor
        armor = random.randint(5, 15)
        # Generate the Drider's Aureliaen Gold Coin count
        def random_integer():
            global num
            num = random.randint(0, 1000)
            if (num > 100 and num < 400) or (num > 500 and num < 948):
                return num
            else:
                return random_integer()
        random_integer()
        agc_count = int(num)
        # Generate the Drider's gem count
        gem_count = random.randint(10, 50)
        # Generate the Drider's elemental gem count
        elemental_gem_count = random.randint(5, 20)
        # Generate the Drider's potion count
        potion_count = random.randint(3, 10)
        # Generate Id
        id_number = 1
        for x in drider_list:
            id_number = id_number + 1
        # Code For Generating A Drider
        # Create A Dictionary To Store The Drider's Attributes
        drider = {
            "Id" : id_number,
            "Name" : name,
            "Personality" : personality,
            "Age": age,
            "Height" : height,
            "Hair Color" : hair_color,
            "Hair Undertone" : hair_undertone,
            "Hair Length" : hair_length,
            "Skin Color" : skin_color,
            "Skin Shine" : skin_shine,
            "Eye Color" : eye_color,
            "Eye Glow Color" : eye_glow_color,
            "Eye Shape" : eye_shape,
            "Glow Brightness" : eye_glow_brightness,
            "Heterochromia" : heterochromia,
            "Second Eye Color" : second_eye_color,
            "Ear length" : ear_length,
            "Earings" : earings,
            "Scale Color" : scale_color,
            "Scale Undertone" : scale_undertone,
            "Scale Pattern" : scale_pattern,
            "Scale Texture" : scale_texture,
            "Scale Higher" : scale_height,
            "Scale Lower" : scale_lower_height,
            "Scale Size" : scale_size,
            "Scale Shape" : scale_shape,
            "Scale Body Pattern" : scale_body_pattern,
            "Has Claws" : has_claws,
            "Claw Color" : claw_color,
            "Claw Alternate Color" : claw_alt_color,
            "Claw Serration" : claw_serration,
            "Claw Length" : claw_length,
            "Fang Color" : fang_color,
            "Spider Leg Color" : leg_color,
            "Spider Leg Alternate Color" : leg_alt_color,
            "Spider Leg Length" : leg_length,
            "Helmet" : outfit[0],
            "Chest" : outfit[1],
            "Shoulder" : outfit[2],
            "Glove" : outfit[3],
            "Leg" : outfit[4],
            "Foot" : outfit[5],
            "Vanity" : outfit[6],
            "Pet" : pet,
            "Gender" : gender,
            "Sexuality": sexuality,
            "Spouse" : spouse_full_name,
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
            "Passive Ability" : random.choice(drider_passive_abilities)
        }
        drider_list.append(drider)
    # function to save the Drider list to a json file
    def save_to_json():
        with open("data_drider.json", "w+") as json_file:
            json.dump(drider_list, json_file, indent=2)
    if enable_overwrite is True:
        # generate a new Drider and save it to the json file
        overwrite = input("\nOverwrite? \nYes / No \n")
        overwrite = overwrite.title()
        if (overwrite == "Yes"):
            for i in range(range_val):
                drider = generate_drider_features()
                save_to_json()
    with open("data_drider.json", "r") as f:
        drider_data = json.load(f)
    generator_checker = False
    if generator_checker is True:
        id_num = int(input("\nId Number 1-{} \n".format(range_val)))
        id_num = int(id_num - 1)
        drider = drider_data[id_num]
        print("")
        for key, value in drider.items():
            print(key + ':', value)

def Merfolk_Gen():
    merfolk_list = []
    merfolk_female_first_names = ["Aria", "Nereida", "Lorelei", "Naiad", "Nymphe", "Marina", "Aurelia", "Ondine", "Calypso", "Thalassa", "Amphitrite", "Ianthe", "Eurydice", "Galatea", "Myrtilla", "Hesperis", "Oceanid", "Sirene", "Sylph", "Ursula", "Venus", "Celeste", "Luna", "Aurora", "Tethys", "Dawn", "Effie", "Rosalind", "Tritonia"]
    merfolk_male_first_names = ["Aiden", "Bryson", "Calum", "Darian", "Ethan", "Finn", "Gael", "Hayden", "Isaac", "Jaxon", "Kane", "Landon", "Mason", "Nash", "Owen", "Paxon", "Quinn", "Raiden", "Sawyer", "Tyson", "Uriah", "Vaughn", "Wyatt", "Xander", "Yarrow", "Zachary"]
    merfolk_nonbinary_names = ["Aquaria", "Coraline", "Nereid", "Marin", "Aster", "Lunaris", "Elysium", "Zephyr", "Aura", "Oceanus", "Nautilus", "Nereus", "Tidal", "Riptide", "Stream", "Spray", "Waves", "Foam", "Current"]
    merfolk_last_names = ["Oceanheart", "Waveweaver", "Sea sprite", "Sea foam", "Coral reef", "Moonlight", "Seashell", "Starfish", "Tidalwave", "Marine", "Aquamarine", "Oceanview", "Sea serpent", "Saltwater", "Siren", "Seaglass", "Sharkfin", "Whale song", "Nautical", "Seahorse", "Seastar", "Wavecrest", "Dolphin", "Lagoon", "Shoreline", "Mermaid's kiss", "Anchor", "Waverider", "Ocean breeze", "Beachcomber", "Tsunami", "Sea breeze", "Shark tooth", "Seaside", "Sea creature", "Sea treasure", "Sea king", "Sea queen", "Sea deity", "Sea goddess", "Sea prince", "Sea princess"]

def Kobold_Gen():
    kobold_list = []
    kobold_male_names = ["Gorn", "Nash", "Kron", "Gash", "Bash", "Frost", "Grim", "Grin", "Horn", "Jash", "Kash", "Morn", "Rash", "Tash", "Vorn", "Zorn", "Gornk", "Kornk", "Lornk", "Mornk", "Pornk", "Sornk", "Wornk", "Zornk"]
    kobold_female_first_names = ["Gretchen", "Kassia", "Nyx", "Ness", "Sariel", "Nessie", "Lilith", "Zara", "Luna", "Ariana", "Ana", "Freya", "Eris", "Sable", "Selene", "Wyn", "Fawn", "Eve", "Ivy", "Rue", "Willow", "Lena", "Aria", "Lily"]
    kobold_non_binary_names = ["Korbin", "Kir", "Bin", "Kirbin", "Bir", "Binkor", "Kirb", "Kor", "Birbin", "Binkir", "Korbir", "Kirbir", "Birb", "Korb", "Binkorb"]
    kobold_last_names = ["Goblinclaw", "Rockfist", "Dwarfstealer", "Dragonrider", "Underfoot", "Miner", "Digger", "Cavecrawler", "Torchbearer", "Shadowdweller", "Gemseeker", "Lavaheart", "Firebreather", "Tunnelrunner", "Mountainmaster", "Hoardshank", "Stoneroller", "Goblinslayer", "Dragonfriend", "Deepdelver"]\

print("\nHuman Gen")
Human_Gen()
print("\nLamia Gen")
Lamia_Gen()
print("\nChangeling Gen")
Changeling_Gen()
print("\nKitsune Gen")
Kitsune_Gen()
print("\nDemon Gen")
Demon_Gen()
print("\nDrider Gen")
Drider_Gen()
print("\nMerfolk Gen")
#Merfolk_Gen()
print("\nKobold Gen")
#Kobold_Gen()