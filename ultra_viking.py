import bpy

class VertexSnapIsland(bpy.types.Operator):
    """Sets everything up for easyily snapping islands to vertices."""
    bl_idname = "uv.vertex_snap_island"
    bl_label = "Vertex Snap Island"
    bl_options = {"REGISTER", "UNDO"}

    grow_iterations = bpy.props.IntProperty()

    def invoke(self, context, event):
        self.grow_iterations = 100
        return self.execute(context)

    def execute(self, context):
        bpy.ops.uv.snap_cursor(target="SELECTED")
        for i in range(self.grow_iterations):
            bpy.ops.uv.select_more()
        return {"FINISHED"}

class ToggleSelectSync(bpy.types.Operator):
    """Toggles UV select sync between 2D and 3D view."""
    bl_idname = "uv.toggle_select_sync"
    bl_label = "Toggle Select Sync"
    bl_options = {"REGISTER"}

    def execute(self, context):
        context.scene.tool_settings.use_uv_select_sync = not context.scene.tool_settings.use_uv_select_sync
        return {"FINISHED"}