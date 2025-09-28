import bpy
from . import auto_collection_color

class DevPanel(bpy.types.Panel):
    bl_category = "ik2m"
    bl_idname = "IK2M_PT_B3dToysPanel"
    bl_label = "for dev"
    bl_description = "開発に使うやつ"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    # bl_context = ""
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("script.reload", text="スクリプトリロード", icon="FILE_REFRESH")



classes = [DevPanel]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    auto_collection_color.register()


def unregister():
    auto_collection_color.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
