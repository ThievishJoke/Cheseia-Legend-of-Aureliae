class Perk:
    """
    Base class for all perks. Each perk can have unique effects by overriding methods or adding attributes.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def apply_effect(self, target):
        """
        Apply the perk's effect to a target (e.g., an Armor, character, or item).
        Override this method in subclasses for custom behavior.
        """
        pass

    def __str__(self):
        return f"Perk: {self.name} - {self.description}"