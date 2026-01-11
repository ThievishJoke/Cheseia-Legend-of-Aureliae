from .aureliae_dialogue import AureliaeDialogue
from .guard_darel_dialogue import GuardDarelDialogue

DIALOGUE_REGISTRY = {
    "aureliae": AureliaeDialogue(),
    "guard_darel": GuardDarelDialogue(),
}

def get_dialogue(npc_id):
    return DIALOGUE_REGISTRY.get(npc_id.lower())