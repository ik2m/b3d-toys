_needs_reload = "bpy" in locals()


import bpy
from . import auto_collection_color, op, ui

if _needs_reload:
    import importlib
    for mod in [auto_collection_color, op, ui]:
        importlib.reload(mod)
    print("Add-on Reloaded")

def register():
    for cls in ui.classes:
        bpy.utils.register_class(cls)
    for cls in op.classes:
        bpy.utils.register_class(cls)
    auto_collection_color.register()
    bpy.types.TOPBAR_HT_upper_bar.prepend(ui.file_menu_drawer)


def unregister():
    bpy.types.TOPBAR_HT_upper_bar.remove(ui.file_menu_drawer)
    auto_collection_color.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)