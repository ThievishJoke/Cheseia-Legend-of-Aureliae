import pathlib
import os
import json

save_folder = pathlib.Path("savefiles")
save_folder.mkdir(parents=True, exist_ok=True)

# File names
savestate = "savestate.json"
savestate_path = save_folder / savestate

game_save = "save.json"
game_save_path = save_folder / game_save

def save_game(player, filename="save", save_debug=False):
    os.makedirs("savefiles", exist_ok=True)

    # Serialize player object to dict and then to JSON
    player_data = player.to_dict()
    save_path = save_folder / f"{filename}.json"

    # Write the main save file
    with open(save_path, "w") as f:
        json.dump(player_data, f, indent=2)

    # Optionally save a debug version
    if save_debug:
        debug_path = save_folder / f"debug_{filename}.json"
        with open(debug_path, "w") as f:
            json.dump(player_data, f, indent=2)

    print(f"Game saved to '{save_path}' and debug JSON created.")

def load_save(filename="save"):
    save_path = save_folder / f"{filename}.json"

    if not save_path.exists():
        print(f"Save file '{save_path}' not found.")
        return None

    try:
        with open(save_path, "r") as f:
            player_data = json.load(f)
        print(f"Game loaded from '{save_path}'.")
        return player_data
    except Exception as e:
        print(f"Error loading game: {e}")
        return None

print("Successfully Imported Save")

