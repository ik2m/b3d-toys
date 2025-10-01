import bpy
from . import auto_collection_color
from .op import op_classes
from .ui import ui_classes


def register():
    for cls in ui_classes:
        bpy.utils.register_class(cls)
    for cls in op_classes:
        bpy.utils.register_class(cls)
    auto_collection_color.register()


def unregister():
    auto_collection_color.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
