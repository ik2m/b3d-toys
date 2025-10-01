import bpy

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


class UV_PT_IslandAlignPanel(bpy.types.Panel):
    bl_category = 'ik2m'
    bl_label = "ik2m"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'


    def draw(self, context):
        layout = self.layout
        layout.operator("uv.ik2m_align_islands_x", icon="ALIGN_CENTER")


ui_classes = (
    DevPanel,
    UV_PT_IslandAlignPanel,
)