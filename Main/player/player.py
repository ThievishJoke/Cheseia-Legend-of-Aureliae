from creatures.species import Species  # Correct import for Species class
from player.player_class_registry import get_player_class

class Player:
    def __init__(self, species, name, position, affinity, gender, inventory, player_class):
        self.name = name
        self.species = species
        self.position = position
        self.affinity = affinity
        self.gender = gender
        self.inventory = inventory  # Inventory includes weapons
        self.player_class = player_class
        
        # Health and Mana setup
        self.max_health = species.base_max_health + player_class.bonus_health
        self.health = self.max_health
        self.max_mana = species.base_max_mana + player_class.bonus_mana
        self.mana = self.max_mana
        self.armor = species.base_armor + player_class.bonus_armor
        self.magic_resist = species.base_magic_resist + player_class.bonus_magic_resist
        self.dmg = species.base_dmg + player_class.bonus_dmg
        self.movement = species.base_movement + player_class.bonus_movement
        self.passive_abilities = species.passive_abilities + player_class.passive_abilities
        self.is_alive = True  # Assuming the player is alive at the start
        
        # Ensure player starts with health and mana at max
        self.health = self.max_health
        self.mana = self.max_mana

        # Example of how the affinity might influence the player's stats:
        self.apply_affinity_effects()

    def apply_affinity_effects(self):
        """
        Applies the effects of the player's elemental affinity to their stats.
        """
        affinity_effects = {
            "Fire": {"magic_dmg": 10, "magic_resist": 5},
            "Aqua": {"magic_dmg": 8, "magic_resist": 6},
            "Earth": {"magic_dmg": 6, "magic_resist": 8},
            "Air": {"magic_dmg": 7, "magic_resist": 7},
            "Lightning": {"magic_dmg": 12, "magic_resist": 4},
            "Light": {"magic_dmg": 9, "magic_resist": 5},
            "Dark": {"magic_dmg": 8, "magic_resist": 6},
            "Eclipse": {"magic_dmg": 10, "magic_resist": 5},
            "Lunar": {"magic_dmg": 9, "magic_resist": 5},
            "Soul": {"magic_dmg": 8, "magic_resist": 7},
            "Blood": {"magic_dmg": 7, "magic_resist": 8},
        }

        # Apply affinity bonuses to magic damage and magic resistance
        if self.affinity in affinity_effects:
            effects = affinity_effects[self.affinity]
            self.base_magic_dmg = self.species.base_magic_dmg + effects["magic_dmg"]
            self.base_magic_resist = self.species.base_magic_resist + effects["magic_resist"]
        else:
            print(f"Warning: Affinity '{self.affinity}' is not recognized. No effects applied.")

    def attack(self, enemy, weapon):
        # Assuming weapon.damage_amount is an integer
        base_damage = weapon.damage_amount
        damage_amount = int(base_damage)  # Ensure it's an integer

        # Example: Bonus damage if the player's affinity matches the weapon's affinity
        if self.affinity == weapon.affinity:
            damage_amount += 5  # Bonus damage for affinity match

        # Print the damage dealt to the enemy
        #print(f"You dealt {damage_amount} {weapon.damage_type} damage to {enemy.name}!")

        # Now, apply the damage to the enemy by calling their take_damage method
        enemy.take_damage(damage_amount)

        return damage_amount
            
    def take_damage(self, damage):
        # Reduce current health by damage
        self.health = max(self.health - damage, 0)

    def heal(self, amount):
        # Heal but do not exceed max health
        self.health = min(self.health + amount, self.max_health)

    def use_mana(self, amount):
        # Decrease mana but do not go below 0
        self.mana = max(self.mana - amount, 0)

    def regenerate_mana(self, amount):
        # Regenerate mana but do not exceed max mana
        self.mana = min(self.mana + amount, self.max_mana)

print("Successfully Imported Player")