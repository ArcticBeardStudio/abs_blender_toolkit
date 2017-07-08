import bpy

class MarkEdgesForSewing(bpy.types.Operator):
    """Makes edges get sewn together when simulating."""
    bl_idname = "mesh.mark_edges_for_sewing"
    bl_label = "Mark Edges for Sewing"
    bl_options = {"REGISTER", "UNDO"}

    # Init properties
    vert_group_name = "LoomSewEdges"

    # Declare variables for storage
    source_verts = None
    target_verts = None

    def invoke(self, context, event):
        print("Loom::Marking::Invoke")
        context.window_manager.modal_handler_add(self)
        bpy.ops.mesh.select_all(action="DESELECT")
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        print(event.type)
        if event.type in {"LEFTMOUSE", "RET"}: # Apply
            self.execute(context)
            return {"FINISHED"}
        elif event.type == "ESC": # Cancel
            return {"CANCELLED"}

        return {"PASS_THROUGH"}

    def execute(self, context):
        print("Loom::Marking::Execute")
        return {"FINISHED"}