import bpy

# TODO: Add support for multiple materials post/pre mode change
class SilhouetteMode(bpy.types.Operator):
    """Wanna know what your silhouette looks like? CLICK THIS AND FIND OUT!"""
    bl_idname = "object.silhouette_mode"
    bl_label = "Toggle Silhouette"
    bl_options = {"REGISTER"}

    # Init some properties on the scene so we can store our current state
    bpy.types.Scene.is_silhoutte_mode = bpy.props.BoolProperty(options={"HIDDEN"})
    bpy.types.Scene.prev_viewport_shade = bpy.props.StringProperty(options={"HIDDEN"})
    bpy.types.Scene.silhouette_material = bpy.props.StringProperty(options={"HIDDEN"})
    bpy.types.Scene.prev_materials = bpy.props.StringProperty(options={"HIDDEN"})

    def execute(self, context):
        # Get some references
        scene = context.scene
        space = context.space_data
        object = context.object

        # Are we in the right place?
        if space.type != "VIEW_3D":
            self.report({"ERROR"}, "Must be in 3D view")
            return {"FINISHED"}

        # Must be in object mode for some functions
        prev_mode = context.active_object.mode
        bpy.ops.object.mode_set(mode="OBJECT")

        # Are we already in silhoutte mode?
        if (scene.is_silhoutte_mode):
            # Gentlemen, call the janitor it's time to clean up
            space.viewport_shade = scene.prev_viewport_shade
            
            for i in range(len(object.data.materials)):
                object.active_material_index = i
                bpy.ops.object.material_slot_remove()
            if scene.prev_materials in bpy.data.materials:
                object.data.materials.append(bpy.data.materials[scene.prev_materials])
            
            # Finish him!
            scene.is_silhoutte_mode = False
            self.report({"INFO"}, "Auto-bots rolled back from Silhouette Mode.")
            bpy.ops.object.mode_set(mode=prev_mode)
            return {"FINISHED"}
        
        # Ok, we're not in silhoutte mode. Get to it!
        material = None
        if scene.silhouette_material in bpy.data.materials:
            material = bpy.data.materials[scene.silhouette_material]
        else:
            material = bpy.data.materials.new("SilhouetteMaterial")
            material.diffuse_color = [0, 0, 0]
            material.use_shadeless = True
        
        
        if object.active_material:
            scene.prev_materials = object.active_material.name
        else:
            scene.prev_materials = ""
        for i in range(len(object.data.materials)):
            object.active_material_index = i
            bpy.ops.object.material_slot_remove()
        scene.silhouette_material = material.name
        object.data.materials.append(material)

        scene.prev_viewport_shade = space.viewport_shade # Store current
        space.viewport_shade = "MATERIAL" # Change current

        # Everything went okay? Well then we're in silhoutte mode!
        scene.is_silhoutte_mode = True
        self.report({"INFO"}, "Set course for Silhoutte Mode. ENGAGE!")
        bpy.ops.object.mode_set(mode=prev_mode)
        return {"FINISHED"}