import bpy


# 3Dビューポートのパネル
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


# UVエディタのパネル
class UV_PT_IslandAlignPanel(bpy.types.Panel):
    bl_category = 'ik2m'
    bl_label = "ik2m"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'


    def draw(self, context):
        layout = self.layout
        layout.operator("uv.ik2m_align_islands_x", icon="ALIGN_CENTER")

# 画面上部のメニューのパネル
class IK2M_PT_file_popover(bpy.types.Panel):
    bl_label = "ik2m"
    bl_space_type = 'TOPBAR'
    bl_region_type = 'HEADER'
    bl_ui_units_x = 8

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("wm.ik2m_open_blend_file_dir", text="フォルダを開く", icon="FILEBROWSER")

        layout.separator()

        row = layout.row()
        row.operator("script.reload", text="スクリプトリロード", icon="FILE_REFRESH")


# 右上のメニュドロワー
def file_menu_drawer(self, context):
    if context.region.alignment == 'RIGHT':
        row= self.layout.row(align=True)
        row.popover(
            panel="IK2M_PT_file_popover",
            text="ik2m",
        )

classes = (
    DevPanel,
    UV_PT_IslandAlignPanel,
    IK2M_PT_file_popover
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_HT_upper_bar.prepend(file_menu_drawer)

def unregister():
    bpy.types.TOPBAR_HT_upper_bar.remove(ui.file_menu_drawer)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)