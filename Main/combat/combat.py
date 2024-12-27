from player.player import Player
from creatures.enemy_npc import Enemy

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def combat_round(self):
        """Handles a single round of combat."""
        print(f"\nYour turn! {self.player.name}'s Health: {self.player.health}/{self.player.max_health}, Mana: {self.player.mana}/{self.player.max_mana}")
        print(f"{self.enemy.name}'s Health: {self.enemy.health}/{self.enemy.max_health}")

        action = input("Choose your action (attack, defend, use item): ").lower()

        if action == "attack":
            if self.player.inventory:  # Check if player has any items in inventory (including weapons)
                print("Available weapons:")
                for i, weapon in enumerate(self.player.inventory, 1):
                    print(f"{i}. {weapon.name} ({weapon.damage_type})")
                try:
                    choice = int(input("Choose a weapon (number): ")) - 1
                    weapon_choice = self.player.inventory[choice]
                    damage = self.player.attack(self.enemy, weapon=weapon_choice)
                    print(f"You dealt {damage} {weapon_choice.damage_type} damage to {self.enemy.name}!")
                    print(f"{self.enemy.name}'s Health: {self.enemy.health}/{self.enemy.max_health}")
                except (ValueError, IndexError):
                    print("Invalid choice. Please choose a valid weapon number.")
            else:
                print("You have no weapons to attack with!")

        elif action == "defend":
            print("You brace yourself for the next attack, reducing damage!")
            # Assuming physical_resistance is a temporary buff for the round:
            original_resistance = self.player.physical_resistance
            self.player.physical_resistance += 0.1  # Temporary increase in resistance for this round
            self.player.physical_resistance = max(0, self.player.physical_resistance)  # Ensure it's not negative
            print(f"Your defense is increased by 0.1! Current resistance: {self.player.physical_resistance}")

        elif action == "use item":
            if self.player.inventory:
                print("Available items:")
                for i, item in enumerate(self.player.inventory, 1):
                    print(f"{i}. {item.name}")
                try:
                    choice = int(input("Choose an item (number): ")) - 1
                    item_choice = self.player.inventory[choice]
                    print(f"You used {item_choice.name}!")
                    # Add item use logic here (e.g., healing, buffs)
                except (ValueError, IndexError):
                    print("Invalid choice. Please choose a valid item number.")
            else:
                print("You don't have any items yet!")

        else:
            print("Invalid action!")

        if not self.enemy.is_alive:
            print(f"\n{self.enemy.name} has been defeated!")
            return True  # Combat ended
        
        # Enemy's turn
        print(f"\n{self.enemy.name}'s turn!")
        if self.enemy.inventory:  # Check if enemy has weapons
            weapon_choice = self.enemy.inventory[0]  # Use first weapon in enemy's inventory
            damage = self.enemy.attack(self.player, weapon=weapon_choice)
            print(f"{self.enemy.name} dealt {damage} damage to you!")
        else:
            print(f"{self.enemy.name} attacks you with a basic attack!")
            damage = self.enemy.attack(self.player)
            print(f"{self.enemy.name} dealt {damage} damage to you!")

        if not self.player.is_alive:
            print(f"\nYou have been defeated by {self.enemy.name}!")
            return True  # Combat ended

        # Reset temporary buffs/debuffs (e.g., the player's armor/resistance)
        #self.player.physical_resistance = original_resistance  # Reset physical resistance after the round

        return False  # Combat continues

    def start_combat(self):
        """Starts the combat loop until one of the combatants is defeated."""
        print(f"\nCombat started! {self.player.name} vs {self.enemy.name}")
        
        while self.player.is_alive and self.enemy.is_alive:
            combat_end = self.combat_round()
            if combat_end:
                break  # Exit the loop if combat has ended

print("Successfully Imported Combat")