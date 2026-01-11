from apparel.accesory.accessories import Accessory
from apparel.armor.armors import Armor
from creatures.species_registry import get_species_by_id, get_species_by_display_name, normalize_species
from creatures.classes_registry import get_player_class, get_class_by_display_name, normalize_player_class
#from item.weapons_registry import get_weapon
from weapon.weapons import WeaponRegistry
from weapon.weapons import Weapon
import random
from utility.formatting import Formatting  
from language.localization import translate

class Player:
    def __init__(self, species, name, affinity, gender, inventory, player_class):
        self.name = name
        self.species = species
        #self.position = position
        self.affinity = affinity
        self.gender = gender
        self.aureliaen_coin = 0
        self.inventory = inventory  # Inventory includes weapons
        self.player_class = player_class

        self.equipment = {
            "weapon": None,
            "armor": None,
            "accessory": None
        }

        # Find first weapon-like object in inventory and equip it
        first_weapon = next(
            (item for item in self.inventory if getattr(item, "weapon_type", None) is not None),
            None
        )

        if first_weapon and self.equipment["weapon"] is None:
            self.equipment["weapon"] = first_weapon

        # Leveling
        self.level = 1
        self.xp = 0
        self.xp_to_next = self.calculate_xp_to_next(self.level)
        
        # Health and Mana setup
        self.max_health = species.base_max_health + player_class.bonus_health
        self.health = self.max_health
        self.max_mana = species.base_max_mana + player_class.bonus_mana
        self.mana = self.max_mana
        self.armor = species.base_armor + player_class.bonus_armor
        self.magic_resist = species.base_magic_resist + player_class.bonus_magic_resist
        self.dmg = species.base_dmg + player_class.bonus_dmg
        self.speed = species.base_speed + player_class.bonus_speed
        self.passive_abilities = species.passive_abilities + player_class.passive_abilities
        self.is_alive = True

        self.crit_chance = 0.01
        self.crit_mult = 1.5
        
        # Ensure player starts with health and mana at max
        self.health = self.max_health
        self.mana = self.max_mana

        self.apply_affinity_effects()

    def __str__(self):
      return f"{self.name} (HP: {self.health}/{self.max_health}, MP: {self.mana}/{self.max_mana})"

    __repr__ = __str__

    def apply_affinity_effects(self):
        """
        Applies the effects of the player's elemental affinity to their stats.
        """
        affinity_effects = {
        "fire": {"magic_dmg": 10, "magic_resist": 5},
        "aqua": {"magic_dmg": 8, "magic_resist": 6},
        "earth": {"magic_dmg": 6, "magic_resist": 8},
        "air": {"magic_dmg": 7, "magic_resist": 7},
        "lightning": {"magic_dmg": 12, "magic_resist": 4},
        "light": {"magic_dmg": 9, "magic_resist": 5},
        "dark": {"magic_dmg": 8, "magic_resist": 6},
        "eclipse": {"magic_dmg": 10, "magic_resist": 5},
        "lunar": {"magic_dmg": 9, "magic_resist": 5},
        "soul": {"magic_dmg": 8, "magic_resist": 7},
        "blood": {"magic_dmg": 7, "magic_resist": 8},
        }

        # Apply affinity bonuses to magic damage and magic resistance
        if self.affinity in affinity_effects:
            effects = affinity_effects[self.affinity]
            self.base_magic_dmg = self.species.base_magic_dmg + effects["magic_dmg"]
            self.base_magic_resist = self.species.base_magic_resist + effects["magic_resist"]
        else:
            print(f"Warning: Player Class Affinity '{self.affinity}' is not recognized. No effects applied.")

    def attack(self, enemy, weapon):
        base_damage = weapon.damage_amount

        # --- Damage variance (±15%)
        variance = random.uniform(0.75, 1.25)
        damage_amount = int(base_damage * variance)

        # --- Affinity bonus
        if self.affinity == weapon.affinity:
            damage_amount += 5  # Bonus damage for affinity match

        # --- Combined critical hit system (player + weapon)
        player_crit_chance = getattr(self, "crit_chance", 0.1)
        player_crit_mult = getattr(self, "crit_mult", 1.5)
        weapon_crit_chance = getattr(weapon, "crit_chance", 0.0)
        weapon_crit_mult = getattr(weapon, "crit_mult", 1.0)

        total_crit_chance = player_crit_chance + weapon_crit_chance
        total_crit_mult = player_crit_mult * weapon_crit_mult

        critical = False
        if random.random() < total_crit_chance:
            # --- Make crit hit as hard as possible
            damage_amount = int(base_damage * 1.25 * total_crit_mult)  # Max variance × crit
            critical = True
        else:
            # Keep variance if not crit
            damage_amount = int(base_damage * variance)

        # --- Apply damage to enemy
        enemy.take_damage(damage_amount)

        # --- Combat feedback
        if critical:
            print(f"{Formatting.GOLD}{Formatting.BOLD}CRITICAL STRIKE!{Formatting.RESET}")
        elif variance > 1.1:
            print(f"{Formatting.GREEN}A strong hit!{Formatting.RESET}")
        elif variance < 0.9:
            print(f"{Formatting.GRAY}A glancing blow...{Formatting.RESET}")

        return damage_amount
            
    def take_damage(self, damage):
        # Reduce current health by damage
        self.health = max(self.health - damage, 0)
        if self.health <= 0:
            self.is_alive = False

    def heal(self, amount):
        # Heal but do not exceed max health
        self.health = min(self.health + amount, self.max_health)

    def use_mana(self, amount):
        # Decrease mana but do not go below 0
        self.mana = max(self.mana - amount, 0)

    def regenerate_mana(self, amount):
        # Regenerate mana but do not exceed max mana
        self.mana = min(self.mana + amount, self.max_mana)

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "xp_to_next": self.xp_to_next,

            "species": self.species.name if hasattr(self.species, "name") else self.species,
            "affinity": self.affinity,
            "gender": self.gender,
            "player_class": self.player_class.name if hasattr(self.player_class, "name") else self.player_class,

            "aureliaen_coin": self.aureliaen_coin,

            "inventory": [item.to_dict() for item in self.inventory],

            "equipment": {
                "weapon": self.equipment["weapon"].to_dict() if self.equipment.get("weapon") else None,
                "armor": self.equipment["armor"].to_dict() if self.equipment.get("armor") else None,
                "accessory": self.equipment["accessory"].to_dict() if self.equipment.get("accessory") else None
            },

            "perks": getattr(self, "perks", {
                "unlocked": [],
                "points": 0
            })
        }
    
    @classmethod
    def from_dict(cls, data):
        # --- Required fields ---
        species = get_species_by_id(data["species"])
        raw_class = data.get("player_class", "")
        try:
            class_id = normalize_player_class(raw_class)
            player_class = get_player_class(class_id)
            if player_class is None:
                raise ValueError
        except Exception:
            raise ValueError(f"Invalid save: unknown player_class '{raw_class}'")

        # Inventory (Weapons & future items)
        inventory_items = []
        for item_data in data.get("inventory", []):
            # Detect weapon vs item vs future object types
            if item_data.get("weapon_type") is not None:
                inventory_items.append(Weapon.from_dict(item_data))
            else:
                # If you add non-weapon items later:
                pass
                #inventory_items.append(Item.from_dict(item_data))

        # --- Create the player instance ---
        player = cls(
            species,
            data["name"],
            data.get("affinity", "None"),
            data.get("gender", "Unknown"),
            inventory_items,
            player_class
        )

        # --- Restore basic progression ---
        player.level = data.get("level", 1)
        player.xp = data.get("xp", 0)
        player.xp_to_next = data.get(
            "xp_to_next",
            player.calculate_xp_to_next(player.level)
        )

        # --- Restore currency (single integer) ---
        player.aureliaen_coin = data.get("aureliaen_coin", 0)

        # --- Restore equipment (default None if missing) ---
        player.equipment = data.get("equipment", {
            "weapon": None,
            "armor": None,
            "accessory": None
        })

        # If equipment includes real items later:
        if isinstance(player.equipment.get("weapon"), dict):
            player.equipment["weapon"] = Weapon.from_dict(player.equipment["weapon"])

        if isinstance(player.equipment.get("armor"), dict):
            player.equipment["armor"] = Armor.from_dict(player.equipment["armor"])

        if isinstance(player.equipment.get("accessory"), dict):
            player.equipment["accessory"] = Accessory.from_dict(player.equipment["accessory"])

        # --- Restore perks ---
        player.perks = data.get("perks", {
            "unlocked": [],
            "points": 0
        })

        # --- Future-proof: world state, achievements, etc ---
        player.achievements = data.get("achievements", {})
        player.world_state = data.get("world_state", {
            "cleared_dungeons": [],
            "visited_locations": []
        })

        return player
    
    def add_currency(self, amount):
        self.aureliaen_coin += amount

    def add_item(self, item):
        self.inventory.append(item)

    def calculate_xp_to_next(self, level):
        """XP curve: 100 * (level^1.5)  (good scaling, not too fast)"""
        return int(100 * (level ** 1.5))

    def get_lvl(self):
        """Returns the player's current level."""
        return self.level

    def get_xp_to_lvl(self):
        """Returns how much XP is required to reach the next level."""
        return self.xp_to_next

    def add_xp(self, amount):
        """Add XP and handle leveling."""
        self.xp += amount
        print(f"\nYou gained {amount} XP!")

        # Level loop in case 1 big reward > multiple level-ups
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()

    def level_up(self):
        """Handles level-up logic: stat growth + notifications."""
        self.level += 1
        print(f"\n" + "="*30)
        print(f"   🎉 LEVEL UP! You are now level {self.level}! 🎉")
        print("="*30)

        # Increase stats on level up
        # Modify these however you like:
        self.max_health = int(self.max_health * 1.10)    # +10%
        self.max_mana = int(self.max_mana * 1.10)        # +10%
        self.dmg = int(self.dmg * 1.08)                  # +8%
        self.armor = int(self.armor * 1.05)              # +5%
        self.magic_resist = int(self.magic_resist * 1.05)

        # Restore health/mana on level
        self.health = self.max_health
        self.mana = self.max_mana

        # Recalculate next threshold
        self.xp_to_next = self.calculate_xp_to_next(self.level)

        # Optional hook: perks, stat choices, class advancements

    """
    @classmethod
    def from_dict(cls, data):
    # --- Species ---
    # If the save contains a translation key, convert it to the object
        species_name_or_key = data["species"]
        species = get_species_by_display_name(translate(species_name_or_key))
            # --- Player class ---
        class_name_or_key = data["player_class"]
        player_class = get_class_by_display_name(translate(class_name_or_key))

        # --- Inventory ---
        weapon_objs = [Weapon.from_dict(w) for w in data.get("inventory", [])]

        # --- Reconstruct Player ---
        return cls(
            species,
            data["name"],
            #data.get("position", [0,0]),  # uncomment if you store position
            data.get("affinity"),
            data.get("gender"),
            weapon_objs,
            player_class
        )
    """

print("Successfully Imported Player")