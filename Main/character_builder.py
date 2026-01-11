from language.localization import translate
from creatures.species_registry import species_registry, get_species_by_id, get_species_by_display_name
from creatures.classes_registry import class_registry, get_player_class, get_class_by_display_name
from player.player import Player
from weapon.weapons import Weapon, WeaponRegistry
from registry.generics_registry import gender_registry, affinity_registry, get_generic_option_by_display_name

# Flag
experimentals = False

def create_new_player():
    player_builder = False
    player_username = ""
    player_sir_name = None
    player_gender = ""
    player_class = None
    species = None
    elemental_aff_key = None

    while True:
        # name
        player_username = input(translate("ui.character_creator.insert_name") + "\n> ").title()
        print(player_username)

        if experimentals:
            ask_player_sir_name = input(translate("ui.character_creator.ask_sir_name") + " (1 for yes)\n> ")
            if ask_player_sir_name.strip() == "1":
                player_sir_name = input(translate("ui.character_creator.insert_sir_name") + "\n> ")

        # species selection
        def choose_species(current=None):
            species_list = list(species_registry.values())
            
            while True:
                print(translate("ui.character_creator.available_species"))
                
                for idx, s in enumerate(species_list, start=1):
                    print(f"{idx}) {s.display_name()}: {translate(s.description_key)}")
                print(f"|0| {translate('ui.character_creator.return')}")    

                species_input = input(
                    f"{translate('ui.character_creator.choose_species')}\n> ")
                
                if species_input == "0":
                    return current

                if not species_input.isdigit():
                    print(translate("ui.character_creator.invalid_species"))
                    continue

                index = int(species_input) - 1
                if index < 0 or index >= len(species_list):
                    print(translate("ui.character_creator.invalid_species"))
                    continue

                species = species_list[index]

                confirm = input(
                    f"{translate('ui.character_creator.confirm_choice', name=species.display_name(), description=translate(species.description_key))} (y/n)\n> "
                )

                if confirm.lower() == "y":
                    return species
        
        # gender selection
        def choose_gender(current=None):
            gender_list = list(gender_registry.values())

            while True:
                print(translate("ui.character_creator.available_genders"))

                for idx, g in enumerate(gender_list, start=1):
                    print(f"{idx}) {g.display_name()}")

                print(f"0) {translate('ui.character_creator.return')}")

                choice = input(
                    f"{translate('ui.character_creator.choose_gender')}\n> "
                )

                # go back
                if choice == "0":
                    return current

                if not choice.isdigit():
                    print(translate("ui.character_creator.invalid_gender"))
                    continue

                index = int(choice) - 1
                if index < 0 or index >= len(gender_list):
                    print(translate("ui.character_creator.invalid_gender"))
                    continue

                gender_option = gender_list[index]
                gender = gender_option.id

                confirm = input(
                    f"{translate('ui.character_creator.confirm_choice', name=gender_option.display_name(), description='')} (y/n)\n> "
                )

                if confirm.lower() == "y":
                    return gender

        # class selection
        def choose_class(current=None):
            class_list = list(class_registry.values())

            while True:
                print(translate("ui.character_creator.available_classes"))

                for idx, c in enumerate(class_list, start=1):
                    print(f"{idx}) {c.display_name()}: {translate(c.description_key)}")

                print(f"0) {translate('ui.character_creator.return')}")

                choice = input(f"{translate('ui.character_creator.choose_class')}\n> ")

                if choice == "0":
                    return current

                if not choice.isdigit():
                    print(translate("ui.character_creator.invalid_class"))
                    continue

                index = int(choice) - 1
                if index < 0 or index >= len(class_list):
                    print(translate("ui.character_creator.invalid_class"))
                    continue

                player_class = class_list[index]

                confirm = input(
                    f"{translate('ui.character_creator.confirm_choice', name=player_class.display_name(), description=translate(player_class.description_key))} (y/n)\n> "
                )

                if confirm.lower() == "y":
                    return player_class

        # element selection
        def choose_affinity(current=None):
            affinity_list = list(affinity_registry.values())

            while True:
                print(translate("ui.character_creator.available_elements"))

                for idx, a in enumerate(affinity_list, start=1):
                    print(f"{idx}) {a.display_name()}")

                print(f"0) {translate('ui.character_creator.return')}")

                choice = input(f"{translate('ui.character_creator.choose_element')}\n> ")

                if choice == "0":
                    return current

                if not choice.isdigit():
                    print(translate("ui.character_creator.invalid_element"))
                    continue

                index = int(choice) - 1
                if index < 0 or index >= len(affinity_list):
                    print(translate("ui.character_creator.invalid_element"))
                    continue

                affinity = affinity_list[index].id

                confirm = input(
                    f"{translate('ui.character_creator.confirm_choice', name=affinity_registry[affinity].display_name(), description='')} (y/n)\n> "
                )

                if confirm.lower() == "y":
                    return affinity

        species = choose_species()
        gender = choose_gender()
        player_class = choose_class()
        elemental_aff = choose_affinity()

        # starting weapon setup
        starting_weapon = WeaponRegistry.get_weapon_by_name("Iron Long Sword")

        # player instance
        player = Player(
            species=species,
            name=player_username,
            affinity=elemental_aff,
            gender=gender,
            inventory=[starting_weapon],
            player_class=player_class
        )

        # summary
        print(
            translate("ui.character_creator.player_created_summary", name=player.name), ":\n" +
            translate("ui.character_creator.species", species=player.species.display_name()) + "\n" +
            translate("ui.character_creator.class_name", class_name=player.player_class.display_name()) + "\n" +
            translate("ui.character_creator.affinity", affinity=affinity_registry[player.affinity].display_name()) + "\n" +
            translate("ui.character_creator.health", health=player.health) + "\n" +
            translate("ui.character_creator.max_health", max_health=player.max_health) + "\n" +
            translate("ui.character_creator.mana", mana=player.mana) + "\n" +
            translate("ui.character_creator.max_mana", max_mana=player.max_mana) + "\n" +
            translate("ui.character_creator.armor", armor=player.armor) + "\n" +
            translate("ui.character_creator.magic_resist", magic_resist=player.magic_resist) + "\n" +
            translate("ui.character_creator.speed", speed=player.speed)
        )

        final_confirm = input(
            translate("ui.character_creator.confirm_final_character") + " (y/n)\n> "
        )

        # confirm all
        if final_confirm.lower() == "y":
            break  # accept character
        else:
            print(translate("ui.character_creator.restart_creation"))
            continue  # reset play creation
    return player