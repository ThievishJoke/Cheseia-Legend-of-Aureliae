from combat.precedural_combat import generate_rewards
from player.player import Player
from creatures.enemy_npc import Enemy
from save import save_manager
from utility.formatting import Formatting as Format


class Combat:
    def __init__(self, player, enemies):
        """
        enemies: either a single Enemy instance or a list of Enemy instances
        """
        self.player = player
        # Wrap single enemy in a list
        if isinstance(enemies, list):
            self.enemies = enemies
        else:
            self.enemies = [enemies]

    def combat_round(self):
        """Handles a single round of combat and returns the combat status."""
        # --- PLAYER STATUS ---
        print(
            f"\nYour turn! {self.player.name}'s Health: {self.player.health}/{self.player.max_health}, Mana: {self.player.mana}/{self.player.max_mana}"
        )

        # --- ENEMY STATUS (MULTI OR SINGLE) ---
        print("\nEnemies:")
        for idx, enemy in enumerate(self.enemies, 1):
            status = (
                "DEAD"
                if not enemy.is_alive
                else f"HP: {enemy.health}/{enemy.max_health}"
            )
            print(f"{idx}. {enemy.name} - {status}")

        # --- PLAYER ACTION ---
        while True:
            action = input("Choose your action (attack, defend, use item): ").lower()

            # ------------------------------------------------
            # ATTACK ACTION
            # ------------------------------------------------
            if action == "attack":
                if not self.player.inventory:
                    print("You have no weapons to attack with!")
                    continue

                # Choose enemy target
                while True:
                    try:
                        target_index = int(input("Choose target enemy (number): ")) - 1
                        target_enemy = self.enemies[target_index]

                        if not target_enemy.is_alive:
                            print("You cannot attack a dead enemy.")
                            continue

                        break
                    except (ValueError, IndexError):
                        print("Invalid enemy number.")

                # Choose weapon
                print("\nAvailable weapons:")
                for i, weapon in enumerate(self.player.inventory, 1):
                    print(f"{i}. {weapon.name} ({weapon.damage_type})")

                while True:
                    try:
                        choice = int(input("Choose a weapon (number): ")) - 1
                        weapon_choice = self.player.inventory[choice]
                        break
                    except (ValueError, IndexError):
                        print("Invalid choice. Please choose a valid weapon number.")

                # Deal damage
                damage = self.player.attack(target_enemy, weapon=weapon_choice)
                print(
                    f"\nYou dealt {damage} {weapon_choice.damage_type} damage to {target_enemy.name}!"
                )
                print(
                    f"{target_enemy.name}'s Health: {target_enemy.health}/{target_enemy.max_health}"
                )

                if not target_enemy.is_alive:
                    print(f"{target_enemy.name} has been defeated!")

                break  # End player turn

            # ------------------------------------------------
            # DEFEND ACTION
            # ------------------------------------------------
            elif action == "defend":
                print(
                    "You brace yourself for the next attack, reducing incoming damage!"
                )
                self.player.armor += 0.1
                print(f"Your armor is temporarily increased to {self.player.armor}")
                break

            # ------------------------------------------------
            # USE ITEM ACTION
            # ------------------------------------------------
            elif action == "use item":
                if not self.player.inventory:
                    print("You don't have any items!")
                    continue

                print("\nAvailable items:")
                for i, item in enumerate(self.player.inventory, 1):
                    print(f"{i}. {item.name}")

                while True:
                    try:
                        choice = int(input("Choose an item (number): ")) - 1
                        item_choice = self.player.inventory[choice]
                        break
                    except (ValueError, IndexError):
                        print("Invalid choice.")

                print(f"You used {item_choice.name}!")
                # TODO: Apply item effects here
                break

            else:
                print("Invalid action!")

        # --- CHECK IF ALL ENEMIES DEAD AFTER PLAYER TURN ---
        if not any(e.is_alive for e in self.enemies):
            return "enemies_dead"

        # ------------------------------------------------------------
        # ENEMY TURN (ALL LIVING ENEMIES ATTACK)
        # ------------------------------------------------------------
        print(f"\n{Format.YELLOW}Enemies' turn!{Format.RESET}")

        for enemy in self.enemies:
            if not enemy.is_alive:
                continue  # Dead enemies skip their turn

            print(f"{enemy.name}'s turn!")

            if enemy.inventory:
                weapon_choice = enemy.inventory[0]
                damage = enemy.attack(self.player, weapon=weapon_choice)
                print(
                    f"{Format.RED}{enemy.name} attacks with {weapon_choice.name} for {damage} damage!{Format.RESET}"
                )
            else:
                damage = enemy.attack(self.player)
                print(
                    f"{Format.RED}{enemy.name} attacks for {damage} damage!{Format.RESET}"
                )

            if not self.player.is_alive:
                print(f"\n{Format.RED}You were slain by {enemy.name}!{Format.RESET}")
                return "player_dead"

        return "continue"  # Combat continues

    def start_combat(self):
        """Starts the combat loop until one of the combatants is defeated."""
        if not self.player:
            raise ValueError("No player assigned to combat!")
        if not self.enemies or all(e is None for e in self.enemies):
            raise ValueError("No enemy assigned to combat!")

        print(
            f"\nCombat started! {self.player.name} vs {', '.join(e.name for e in self.enemies)}"
        )

        while True:
            # --- Execute a combat round ---
            status = self.combat_round()

            # --- Handle combat end statuses ---
            if status == "player_dead":
                print(f"\n{Format.RED}You have been slain!{Format.RESET}")
                break

            elif status == "enemies_dead":
                print("\nAll enemies have been defeated!")

                # --- Reward phase ---
                total_xp = 0
                total_currency = 0
                total_loot = []

                for enemy in self.enemies:
                    rewards = generate_rewards(enemy)  # Make sure Enemy class has this
                    total_xp += rewards.get("xp", 0)
                    total_currency += rewards.get("currency", 0)
                    total_loot.extend(rewards.get("loot", []))

                # Apply rewards
                print(
                    f"\n{Format.BOLD}{Format.DARK_GREEN}You gained {total_xp} XP and {total_currency} gold!{Format.RESET}"
                )
                self.player.add_xp(total_xp)
                self.player.add_currency(total_currency)

                # Add loot to inventory
                for item in total_loot:
                    self.player.add_item(item)
                    print(f"You received: {item}")

                # Handle level-ups if XP threshold reached
                while self.player.xp >= self.player.xp_to_next:
                    self.player.level_up()

                # Save progress
                save_manager.save_player(self.player, rename_to_name=True)
                break

            elif status == "continue":
                continue  # Go to next round

            else:
                print(f"[WARN] Unknown combat status: {status}")
                break


print("Successfully Imported Combat")
