from creatures.enemy_npc import EnemyRegistry
import importlib
import pkgutil
from creatures import hostile

# Dynamically import all modules in creatures.hostile
for loader, module_name, is_pkg in pkgutil.iter_modules(hostile.__path__):
    full_module_name = f"{hostile.__name__}.{module_name}"
    importlib.import_module(full_module_name)

# At this point, all enemies defined in the hostile modules are registered automatically
#print("Registered enemies:", EnemyRegistry.list_enemies())