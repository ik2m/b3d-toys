import bpy
import bmesh
from collections import defaultdict

class UV_OT_AlignIslandsX(bpy.types.Operator):
    bl_idname = "uv.ik2m_align_islands_x"
    bl_label = "Align Islands X=0.5"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if context.mode != 'EDIT_MESH' or context.edit_object is None:
            return False

        # UV選択モードがアイランドモードかチェック
        tool_settings = context.scene.tool_settings
        if tool_settings.uv_select_mode != 'ISLAND':
            return False

        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        #アクティブなUVレイヤー
        uv_layer = bm.loops.layers.uv.active

        if not uv_layer:
            return False

        # UVが選択されているかチェック
        for f in bm.faces:
            if f.select:
                for loop in f.loops:
                    if loop[uv_layer].select:
                        return True

        return False

    def execute(self, context):
        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        uv_layer = bm.loops.layers.uv.active

        # UV選択されているループを収集
        def get_selected_uv_loops():
            """UVエディタで選択されているループを取得"""
            selected_loops = []
            for face in bm.faces:
                for loop in face.loops:
                    if loop[uv_layer].select:
                        selected_loops.append(loop)
            return selected_loops

        # UVアイランドを検出
        def get_uv_islands_from_selection():
            """選択されたUVからアイランドを検出"""
            selected_loops = get_selected_uv_loops()
            if not selected_loops:
                return []

            # 選択されているループが属する面を収集
            selected_faces = set(loop.face for loop in selected_loops)

            islands = []
            visited_faces = set()

            for start_face in selected_faces:
                if start_face in visited_faces:
                    continue

                # アイランドを構築
                island = set()
                stack = [start_face]

                while stack:
                    face = stack.pop()
                    if face in island or face not in selected_faces:
                        continue

                    island.add(face)

                    # UV縫い目でない隣接面を追加
                    for edge in face.edges:
                        if not edge.seam:
                            for linked_face in edge.link_faces:
                                if linked_face in selected_faces and linked_face not in island:
                                    stack.append(linked_face)

                if island:
                    visited_faces.update(island)
                    islands.append(island)

            return islands

        islands = get_uv_islands_from_selection()

        if not islands:
            self.report({'WARNING'}, "No UV islands selected")
            return {'CANCELLED'}

        # 各アイランドごとに処理
        for island in islands:
            # このアイランドの選択されているUVのみを収集
            uvs = [loop[uv_layer].uv for face in island for loop in face.loops
                   if loop[uv_layer].select]

            if not uvs:
                continue

            # X方向の中心を計算
            center_x = sum(uv.x for uv in uvs) / len(uvs)

            # 移動量を計算
            offset_x = 0.5 - center_x

            # このアイランドの選択UVを移動
            for uv in uvs:
                uv.x += offset_x

        bmesh.update_edit_mesh(me)
        return {'FINISHED'}

classes = [UV_OT_AlignIslandsX]