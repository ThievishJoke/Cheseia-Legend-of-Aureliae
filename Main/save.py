import pathlib
import os
import json
import random
from player.player import Player
from character_builder import create_new_player

# Setup save folder
save_folder = pathlib.Path("savefiles")
save_folder.mkdir(parents=True, exist_ok=True)

# Default save filenames
savestate_file = "savestate.json"
save_file = "save.json"
save_0_file = "save_0.json"
save_1_file = "save_1.json"
save_2_file = "save_2.json"
save_3_file = "save_3.json"

save_path = save_folder / save_file
debug_path = save_folder / f"debug_{save_file}"

class SaveManager:
    def __init__(self, save_dir="savefiles"):
        self.save_dir = pathlib.Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

        # Use fixed save slot filenames
        self.slot_files = [save_file, save_0_file, save_1_file, save_2_file, save_3_file]  # <-- rename from self.slots
        self.state_file = self.save_dir / savestate_file

        # Load savestate
        self.state = self.load_state() or {"Debug": False, "World_Seed": random.randint(1, 100000)}
        self.debug = self.state.get("Debug", False)

    def save_player(self, player: Player, slot_index=0, debug=False, mirror_default=False, rename_to_name=False):
        """Save a Player to a slot and optionally save a debug copy."""
        if slot_index < 0 or slot_index >= len(self.slot_files):
            raise ValueError("Invalid save slot index.")
        
        if rename_to_name:
            slot_file = self.save_dir / self.generate_unique_save_filename(player.name)
        else:
            slot_file = self.save_dir / self.slot_files[slot_index]

        player_dict = player.to_dict()

        # Write main save file
        with open(slot_file, "w") as f:
            json.dump(player_dict, f, indent=2)

        # Optional debug save
        if debug or self.debug:
            debug_file = self.save_dir / f"debug_{slot_file.name}"
            with open(debug_file, "w") as f:
                json.dump(player_dict, f, indent=2)

        # Optional mirror to default save.json
        if mirror_default and slot_index == 0:
            default_file = self.save_dir / "save.json"
            with open(default_file, "w") as f:
                json.dump(player_dict, f, indent=2)

        print(f"Saved '{player.name}' to slot {slot_index} ({slot_file})")

    def load_player(self, slot_index=0):
        if slot_index < 0 or slot_index >= len(self.slot_files):
            raise ValueError("Invalid save slot index.")
        slot_file = self.save_dir / self.slot_files[slot_index]
        if not slot_file.exists():
            print(f"Save slot {slot_index} is empty.")
            return None

        with open(slot_file, "r") as f:
            data = json.load(f)
        player = Player.from_dict(data)

        if self.debug:
            print(f"\n-Debug Load- Player slot {slot_index}:\n{json.dumps(data, indent=2)}\n-Debug-\n")

        print(f"Loaded '{player.name}' from slot {slot_index}")
        return player

    def create_new_save(self, slot_index=0, debug=False):
        player = create_new_player()
        self.save_player(player, slot_index=slot_index, debug=debug, rename_to_name=True)
        return player

    def set_debug(self, enabled=True):
        self.debug = enabled
        self.state["Debug"] = enabled
        self.save_state(self.state)

    def save_state(self, state_dict):
        with open(self.state_file, "w") as f:
            json.dump(state_dict, f, indent=2)

    def load_state(self):
        if self.state_file.exists():
            with open(self.state_file, "r") as f:
                return json.load(f)
        return None
    
    def slots_info(self):
        """
        Return info about each save file in the save folder.
        Detects all JSON save files, including renamed ones.
        """
        slot_info = []

        # Scan all JSON files in save folder
        for idx, path in enumerate(sorted(self.save_dir.glob("*.json"))):
            # Skip savestate or debug files
            if path.name.startswith("debug_") or path.name == savestate_file:
                continue

            if path.exists():
                try:
                    with open(path, "r") as f:
                        data = json.load(f)
                    slot_info.append({
                        "index": idx,
                        "file": path.name,
                        "name": data.get("name"),
                        "level": data.get("level"),
                        "species": data.get("species"),
                        "affinity": data.get("affinity"),
                        "gender": data.get("gender"),
                        "player_class": data.get("player_class"),
                        "exists": True
                    })
                except Exception:
                    # In case file Corruption
                    slot_info.append({
                        "index": idx,
                        "file": path.name,
                        "name": None,
                        "level": None,
                        "species": None,
                        "affinity": None,
                        "gender": None,
                        "player_class": None,
                        "exists": True
                    })
        return slot_info
    
    def load_player_by_filename(self, filename):
        path = self.save_dir / filename
        if not path.exists():
            print(f"Save file {filename} does not exist.")
            return None
        with open(path, "r") as f:
            data = json.load(f)
        player = Player.from_dict(data)
        if self.debug:
            print(f"\n-Debug Load- Player '{player.name}' from {filename}:\n{json.dumps(data, indent=2)}\n-Debug-\n")
        print(f"Loaded '{player.name}' from {filename}")
        return player
    
    def migrate_old_saves(self):
        """
        Migrate existing save files to follow the new naming convention:
        - Renames save.json, save_0.json, etc. to PlayerName.json
        - Adds _1, _2 if multiple saves have the same name
        - Skips debug and savestate files
        """
        renamed_count = 0
        for path in self.save_dir.glob("*.json"):
            if path.name.startswith("debug_") or path.name == "savestate.json":
                continue  # skip debug/state files

            # Load player data
            try:
                with open(path, "r") as f:
                    data = json.load(f)
            except Exception:
                print(f"[WARN] Could not read {path.name}, skipping.")
                continue

            player_name = data.get("name")
            if not player_name:
                continue  # skip files with no player name

            # Generate unique filename based on player name
            new_filename = self.generate_unique_save_filename(player_name)
            new_path = self.save_dir / new_filename

            if path != new_path:
                path.rename(new_path)
                print(f"[MIGRATE] Renamed {path.name} -> {new_filename}")
                renamed_count += 1

        print(f"[MIGRATE] Migration complete. {renamed_count} files renamed.")

    def generate_unique_save_filename(self, name):
        """
        Return a unique save filename for a player, e.g., 'Flora.json', 'Flora_1.json', etc.
        """
        base_name = f"{name}.json"
        path = self.save_dir / base_name
        counter = 1
        while path.exists():
            base_name = f"{name}_{counter}.json"
            path = self.save_dir / base_name
            counter += 1
        return base_name
    
save_manager = SaveManager()
save_manager.migrate_old_saves()
print("SaveManager initialized and old saves migrated.")

print("Successfully Imported Save")