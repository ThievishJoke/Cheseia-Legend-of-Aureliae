from creatures.classes import PlayerClass

warrior_class = PlayerClass(
    id="warrior",
    name="Warrior",
    name_key="creatures.classes.warrior.name",
    description_key="creatures.classes.warrior.description",
    bonus_dmg=10, 
    bonus_mana=30, 
    bonus_magic_dmg=5, 
    bonus_health=50, 
    bonus_magic_resist=5, 
    bonus_armor=20,
    passive_abilities=[],
    bonus_speed=3
)
fighter_class = PlayerClass(
    id="fighter",
    name="Fighter",
    name_key="creatures.classes.fighter.name",
    description_key="creatures.classes.fighter.description",
    bonus_dmg=10, 
    bonus_mana=30, 
    bonus_magic_dmg=5, 
    bonus_health=50, 
    bonus_magic_resist=5, 
    bonus_armor=20,
    passive_abilities=[],
    bonus_speed=3
)
mage_class = PlayerClass(
    id="mage",
    name="Mage",
    name_key="creatures.classes.mage.name",
    description_key="creatures.classes.mage.description",
    bonus_dmg=5, 
    bonus_mana=50, 
    bonus_magic_dmg=20, 
    bonus_health=30, 
    bonus_magic_resist=10, 
    bonus_armor=5,
    passive_abilities=[],
    bonus_speed=2
)
bard_class = PlayerClass(
    id="bard",
    name="Bard",
    name_key="creatures.classes.bard.name",
    description_key="creatures.classes.bard.description",
    bonus_dmg=7, 
    bonus_mana=40, 
    bonus_magic_dmg=10, 
    bonus_health=40, 
    bonus_magic_resist=5, 
    bonus_armor=10,
    passive_abilities=[],
    bonus_speed=4
)
thief_class = PlayerClass(
    id="thief",
    name="Thief",
    name_key="creatures.classes.thief.name",
    description_key="creatures.classes.thief.description",
    bonus_dmg=15,
    bonus_mana=10,
    bonus_magic_dmg=2,
    bonus_health=60,
    bonus_magic_resist=5,
    bonus_armor=15,
    passive_abilities=[],
    bonus_speed=3
)
paladin_class = PlayerClass(
    id="paladin",
    name="Paladin",
    name_key="creatures.classes.paladin.name",
    description_key="creatures.classes.paladin.description",
    bonus_dmg=10,
    bonus_mana=25,
    bonus_magic_dmg=6,
    bonus_health=50,
    bonus_magic_resist=10,
    bonus_armor=12,
    passive_abilities=[],
    bonus_speed=2
)
healer_class = PlayerClass(
    id="healer",
    name="Healer",
    name_key="creatures.classes.healer.name",
    description_key="creatures.classes.healer.description",
    bonus_dmg=2,
    bonus_mana=60,
    bonus_magic_dmg=12,
    bonus_health=40,
    bonus_magic_resist=12,
    bonus_armor=4,
    passive_abilities=[],
    bonus_speed=4
)
ranger_class = PlayerClass(
    id="ranger",
    name="Ranger",
    name_key="creatures.classes.ranger.name",
    description_key="creatures.classes.ranger.description",
    bonus_dmg=12,
    bonus_mana=20,
    bonus_magic_dmg=5,
    bonus_health=45,
    bonus_magic_resist=6,
    bonus_armor=8,
    passive_abilities=[],
    bonus_speed=6
)

class_registry = {
    "warrior": warrior_class,
    "fighter": fighter_class,
    "mage": mage_class,
    "bard": bard_class,
    "thief": thief_class,
    "paladin": paladin_class,
    "healer": healer_class,
    "ranger": ranger_class
}

def get_player_class(class_id: str) -> PlayerClass:
    """Returns the PlayerClass object based on the input class name"""
    return class_registry.get(class_id)

def get_class_by_display_name(display_name: str) -> PlayerClass | None:
    """Return the PlayerClass object by matching the translated display name."""
    display_name_lower = display_name.lower()
    for cls in class_registry.values():
        if cls.display_name().lower() == display_name_lower:
            return cls
    return None

def normalize_player_class(value: str) -> str:
    value = value.lower()

    if value in class_registry:
        return value

    cls = get_class_by_display_name(value)
    if cls:
        return cls.id

    raise ValueError(f"Unknown class: {value}")