import bpy

# キーマップを保存するリスト
addon_keymaps = []

def register():
    # キーマップの登録
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        # 例: F5 でパイメニューを呼び出す
        kmi = km.keymap_items.new('wm.call_menu_pie', 'F5', 'PRESS')
        kmi.properties.name = "VIEW3D_MT_PIE_b3d_toys"
        addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()