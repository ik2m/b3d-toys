_needs_reload = "bpy" in locals()


import bpy
from . import auto_collection_color, op, ui

if _needs_reload:
    import importlib
    for mod in [auto_collection_color, op, ui]:
        importlib.reload(mod)
    print("Add-on Reloaded")

def register():
    op.register()
    ui.register()
    auto_collection_color.register()



def unregister():
    auto_collection_color.unregister()
    ui.unregister()
    op.unregister()