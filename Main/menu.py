import os
import sys
import time
import random
import json
from pathlib import Path

from save import SaveManager
from language.localization import translate
from registry.generics_registry import gender_registry, affinity_registry, get_generic_option_by_display_name, normalize_generic_option
from utility.formatting import Formatting as Format

from player.player import Player
from creatures.species_registry import species_registry, get_species_by_display_name, normalize_species
from creatures.classes_registry import class_registry, get_class_by_display_name, normalize_player_class
from weapon.weapons import WeaponRegistry

SAVE_FOLDER = Path("savefiles")
SAVE_FOLDER.mkdir(exist_ok=True)
SAVE_SLOTS = ["save.json", "save_0.json", "save_1.json"]
SAVE_STATE = SAVE_FOLDER / "savestate.json"

print("SaveManager initialized and old saves migrated.")
print("Successfully Imported Save")

class StartMenu:
    def __init__(self):
        self.debug = False
        self.save_manager = SaveManager()
        self.world_seed = random.randint(1, 100000)
        self.current_slot = None

    def print_delayed(self, text, delay=0.01):
        """Print text with typewriter effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # newline

    def show_menu(self):
        menu_text = (
            "\n" +
            translate("ui.menu.start.new_game") + "|1| " +
            translate("ui.menu.start.continue") + "|2| " +
            translate("ui.menu.start.quit") + "|3|\n"
        )
        choice = input(menu_text + "> ")
        return choice

    def new_save(self):
        """Create a new save in an empty slot if available, otherwise ask for overwrite."""

        # Generate a new random world seed
        self.world_seed = random.randint(1, 100000)
        save_data = {
            "existing_save": True,
            "World_Seed": self.world_seed,
            "Debug": self.debug
        }

        # Get current save files (exclude debug and state)
        slots_info = [s for s in self.save_manager.slots_info() if s["name"] is not None]

        # Configurable max number of saves
        MAX_SAVES = 4

        if len(slots_info) < MAX_SAVES:
            # There’s room for a new save
            empty_slot = next((s for s in self.save_manager.slots_info() if not s["exists"]), None)

            if empty_slot:
                slot_choice = empty_slot["index"]
                self.print_delayed(
                    translate("ui.menu.start.using_empty_slot") + f" ({empty_slot['file'] or f'Slot {slot_choice}'})"
                )
            else:
                # All old slots may have been renamed or filled, but total < MAX_SAVES → pick next index
                slot_choice = len(slots_info)  # next free slot index
                self.print_delayed(
                    translate("ui.menu.start.using_empty_slot") + f" (slot {slot_choice})"
                )

        else:
            # No room → must offer overwrite
            self.print_delayed(translate("ui.menu.start.confirm_overwrite"))

            # Present all existing saves to overwrite
            menu_map = {}
            for menu_idx, s in enumerate(slots_info, start=1):
                menu_map[menu_idx] = s
                print(f"{menu_idx}. {s['file']} - {s['name']} Lv{s['level']} {s['gender']} "
                    f"{s['affinity']} {s['player_class']}")

            print("Cancel (0)")

            choice = input("> ").strip()
            if choice in ["0", "b", "B"]:
                self.print_delayed(translate("ui.menu.start.backing_out"))
                return None

            try:
                choice_idx = int(choice)
                if choice_idx not in menu_map:
                    raise ValueError
            except ValueError:
                self.print_delayed(translate("ui.menu.start.invalid_slot"))
                return None

            selected_slot = menu_map[choice_idx]
            slot_choice = selected_slot["index"]

            # Delete existing file so new save replaces it
            old_file = self.save_manager.save_dir / selected_slot["file"]
            if old_file.exists():
                old_file.unlink()

            self.print_delayed(f"Overwriting {selected_slot['file']}...")

        # Create a new Player and save immediately
        player = self.save_manager.create_new_save(slot_index=slot_choice, debug=self.debug)
        # After save, current_slot becomes the new/renamed filename
        self.current_slot = player.name
        self.print_delayed(translate("ui.menu.start.save_created") + f" ({self.current_slot})")

        return player
    def continue_save(self):
        """Continue from an existing save slot, letting the player choose."""
        slots_info = self.save_manager.slots_info()  # list of dicts with keys: name, level, index, file
        existing_slots = [s for s in slots_info if s["name"] is not None]

        if not existing_slots:
            self.print_delayed(translate("ui.menu.start.no_save_found"))
            return None

        # Show available slots
        self.print_delayed(translate("ui.menu.start.select_save"))
        for s in existing_slots:
            idx = s["index"] + 1

            try:
                gender_id = normalize_generic_option(gender_registry, s["gender"])
                gender_name = gender_registry[gender_id].display_name()
            except ValueError:
                gender_name = s.get("gender", "Unknown")

            try:
                species_id = normalize_species(s["species"])
                species_name = species_registry[species_id].display_name()
            except ValueError:
                species_name = s.get("species", "Unknown")

            try:
                affinity_id = normalize_generic_option(affinity_registry, s["affinity"])
                affinity_name = affinity_registry[affinity_id].display_name()
            except ValueError:
                affinity_name = s.get("affinity", "Unknown")

            try:
                class_id = normalize_player_class(s["player_class"])
                class_name = class_registry[class_id].display_name()
            except ValueError:
                class_name = s.get("player_class", "Unknown")

            # Display using translation key
            self.print_delayed(
                f"|{idx}| " +
                translate(
                    "ui.menu.start.save_slot_display",
                    name=s["name"],
                    level=s["level"],
                    gender=gender_name,
                    species=species_name,
                    affinity=affinity_name,
                    player_class=class_name
                )
            )

        self.print_delayed(translate("ui.menu.start.cancel_option") + " (0)")

        choice = input("> ").strip()
        if choice in ["0", "b", "B"]:
            self.print_delayed(translate("ui.menu.start.backing_out"))
            return None

        try:
            choice_idx = int(choice) - 1
            if choice_idx not in [s["index"] for s in existing_slots]:
                raise ValueError
        except ValueError:
            self.print_delayed(translate("menu.start.invalid_choice"))
            return None

        selected_slot = [s for s in slots_info if s["index"] == choice_idx][0]
        self.print_delayed(translate("ui.menu.start.loading_save") + f" ({selected_slot['file']})")
        
        player_instance = self.save_manager.load_player_by_filename(selected_slot['file'])
        return player_instance

    def enable_debug(self):
        self.debug = True
        self.save_manager.set_debug(True)
        self.print_delayed(translate("ui.menu.start.debug_enabled"))

    def run(self):
        """Main menu loop."""
        # Generate a new random seed for world generation
        self.world_seed = random.randint(1, 100000)

        while True:
            choice = self.show_menu()
            if choice == "1":  # New game
                player = self.new_save()
                if player:
                    return player
            elif choice == "2":  # Continue
                player = self.continue_save()
                if player:
                    return player
            elif choice == "3":  # Quit
                self.print_delayed(translate("ui.menu.start.quit_message"))
                sys.exit(0)
            elif choice.lower() == "debug":
                self.enable_debug()
            else:
                self.print_delayed(translate("ui.menu.start.invalid_choice"))

if __name__ == "__main__":
    menu = StartMenu()
    player_instance = menu.run()
    print(f"Loaded Player: {player_instance.name} (Lvl {player_instance.level})")