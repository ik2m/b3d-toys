_needs_reload = "bpy" in locals()


import bpy
from . import auto_collection_color, op, ui, km

if _needs_reload:
    import importlib
    for mod in [auto_collection_color, op, ui, km]:
        importlib.reload(mod)
    print("Add-on Reloaded")

def register():
    op.register()
    ui.register()
    km.register()
    auto_collection_color.register()



def unregister():
    auto_collection_color.unregister()
    km.unregister()
    ui.unregister()
    op.unregister()