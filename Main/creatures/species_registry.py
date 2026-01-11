from creatures.species import Species

human_species = Species(
    id="human",
    name="Human",
    name_key="creatures.species.human.name",
    description_key="creatures.species.human.description",
    base_health=100,
    base_max_health=100,
    base_mana=50,
    base_max_mana=50,
    base_magic_dmg=10,
    base_magic_resist=15,
    base_armor=0,
    passive_abilities=[],
    base_dmg=12,
    base_speed=10
)
lamia_species = Species(
    id="lamia",
    name="Lamia",
    name_key="creatures.species.lamia.name",
    description_key="creatures.species.lamia.description",
    base_health=110,
    base_max_health=110,
    base_mana=50,
    base_max_mana=50,
    base_magic_dmg=10,
    base_magic_resist=5,
    base_armor=5,
    passive_abilities=[],
    base_dmg=12,
    base_speed=10
)
kitsune_species = Species(
    id="kitsune",
    name="Kitsune",
    name_key="creatures.species.kitsune.name",
    description_key="creatures.species.kitsune.description",
    base_health=100,
    base_max_health=100,
    base_mana=100,
    base_max_mana=100,
    base_magic_dmg=10,
    base_magic_resist=5,
    base_armor=5,
    passive_abilities=[],
    base_dmg=12,
    base_speed=10
)
orc_species = Species(
    id="orc",
    name="Orc",
    name_key="creatures.species.orc.name",
    description_key="creatures.species.orc.description",
    base_health=120,
    base_max_health=120,
    base_mana=50,
    base_max_mana=50,
    base_magic_dmg=10,
    base_magic_resist=-10,
    base_armor=20,
    passive_abilities=[],
    base_dmg=15,
    base_speed=10
)
drider_species = Species(
    id="drider",
    name="Drider",
    name_key="creatures.species.drider.name",
    description_key="creatures.species.drider.description",
    base_health=95,
    base_max_health=95,
    base_mana=50,
    base_max_mana=50,
    base_magic_dmg=10,
    base_magic_resist=0,
    base_armor=0,
    passive_abilities=[],
    base_dmg=20,
    base_speed=10
)
dire_species = Species(
    id="dire",
    name="Dire",
    name_key="creatures.species.dire.name",
    description_key="creatures.species.dire.description",
    base_health=110,
    base_max_health=110,
    base_mana=100,
    base_max_mana=100,
    base_magic_dmg=20,
    base_magic_resist=0,
    base_armor=0,
    passive_abilities=[],
    base_dmg=10,
    base_speed=10
)

species_registry = {
    "human": human_species,
    "lamia": lamia_species,
    "kitsune": kitsune_species,
    "orc": orc_species,
    "drider": drider_species,
    "dire": dire_species
    # Add defined species here, "Lamia": lamia_species
}

def get_species_by_id(species_id: str) -> Species | None:
    """Returns the Species object based on the input species name"""
    return species_registry.get(species_id.lower())

def get_species_by_display_name(display_name: str) -> Species | None:
    display_name_lower = display_name.lower()
    for s in species_registry.values():
        if s.display_name().lower() == display_name_lower:
            return s
    return None

def normalize_species(value: str) -> str:
    value = value.lower()

    if value in species_registry:
        return value

    s = get_species_by_display_name(value)
    if s:
        return s.id

    raise ValueError(f"Unknown species: {value}")