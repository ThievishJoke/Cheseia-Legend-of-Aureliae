from creatures.species import Species

human_species = Species(
    name="Human",
    base_health=100,
    base_max_health=100,
    base_mana=50,
    base_max_mana=50,
    base_magic_dmg=10,
    base_magic_resist=5,
    base_armor=5,
    passive_abilities=[],
    base_dmg=12,
    base_speed=10
)

# Define other species in a similar manner
# You can expand it later by adding Lamia, Kitsune, etc.

species_registry = {
    "Human": human_species,
    # Add other species here once defined, like "Lamia": lamia_species
}

# Method to get species from the registry
def get_species(species_name):
    return species_registry.get(species_name, None)