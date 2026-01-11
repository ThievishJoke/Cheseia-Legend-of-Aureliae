from language.localization import translate

class GenericOption:
    def __init__(self, id: str, name_key: str):
        self.id = id.lower()
        self.name_key = name_key

    def display_name(self) -> str:
        return translate(self.name_key)


# Gender options
gender_registry = {
    "female": GenericOption("female", "creatures.generic.gender.female"),
    "male": GenericOption("male", "creatures.generic.gender.male"),
    "other": GenericOption("other", "creatures.generic.gender.other")
}

# Elemental affinities
affinity_registry = {
    "fire": GenericOption("fire", "creatures.generic.affinity.fire"),
    "aqua": GenericOption("aqua", "creatures.generic.affinity.aqua"),
    "earth": GenericOption("earth", "creatures.generic.affinity.earth"),
    "air": GenericOption("air", "creatures.generic.affinity.air"),
    "lightning": GenericOption("lightning", "creatures.generic.affinity.lightning"),
    "light": GenericOption("light", "creatures.generic.affinity.light"),
    "dark": GenericOption("dark", "creatures.generic.affinity.dark"),
    "eclipse": GenericOption("eclipse", "creatures.generic.affinity.eclipse"),
    "lunar": GenericOption("lunar", "creatures.generic.affinity.lunar"),
    "soul": GenericOption("soul", "creatures.generic.affinity.soul"),
    "blood": GenericOption("blood", "creatures.generic.affinity.blood")
}

def get_generic_option_by_display_name(registry: dict, display_name: str) -> GenericOption | None:
    display_name_lower = display_name.lower()
    for option in registry.values():
        if option.display_name().lower() == display_name_lower:
            return option
    return None

def normalize_generic_option(registry: dict, value: str) -> str:
    value_lower = value.lower()
    if value_lower in registry:
        return value_lower

    option = get_generic_option_by_display_name(registry, value)
    if option:
        return option.id

    raise ValueError(f"Unknown generic option: {value}")
