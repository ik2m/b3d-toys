import bpy
import bmesh
from collections import defaultdict

class UV_OT_AlignIslandsX(bpy.types.Operator):
    bl_idname = "uv.ik2m_align_islands_x"
    bl_label = "Align Islands X=0.5"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        uv_layer = bm.loops.layers.uv.verify()

        # islandごとにUVループを収集
        islands = []
        visited_faces = set()

        def collect_island(start_face):
            stack = [start_face]
            island_faces = set()
            while stack:
                f = stack.pop()
                if f in island_faces:
                    continue
                island_faces.add(f)
                for e in f.edges:
                    linked = [lf for lf in e.link_faces if lf not in island_faces]
                    stack.extend(linked)
            return island_faces

        for f in bm.faces:
            if f.select and f not in visited_faces:
                island = collect_island(f)
                visited_faces |= island
                islands.append(island)

        if not islands:
            self.report({'WARNING'}, "No UV islands selected")
            return {'CANCELLED'}

        # 各アイランドごとに処理
        for island in islands:
            uvs = [l[uv_layer].uv for f in island if f.select for l in f.loops]
            if not uvs:
                continue

            # X方向の中心を計算
            center_x = sum(uv.x for uv in uvs) / len(uvs)

            # 移動量を計算
            offset_x = 0.5 - center_x

            for uv in uvs:
                uv.x += offset_x

        bmesh.update_edit_mesh(me)
        return {'FINISHED'}

classes = [UV_OT_AlignIslandsX]