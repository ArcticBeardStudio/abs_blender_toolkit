# MIT License Copyright Arctic Beard Studio 2017

bl_info = {
    "name": "Arctic Beard Studio Toolkit",
    "author": "Henrik Melsom",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "location": "",
    "description": "Arctic Beard Studio in-house toolkit, because you're worth it!",
    "warning": "",
    "wiki_url": "",
    "category": "System"
}
abs_idbase = "arctic_beard_studio"

import bpy


class Storage:
    is_silhoutte_mode = False
    prev_viewport_shade = None
    silhouette_material = None


class Align(bpy.types.Operator):
    """I heard you like aligning stuff, so i wrote this function so you can align stuff to other stuff."""
    bl_idname = abs_idbase + ".align"
    bl_label = "Align"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.report({"INFO"}, "Shit just got aligned! *harkle*... actually this is just a dummy function... #sadface :(")
        return {"FINISHED"}


class SilhouetteMode(bpy.types.Operator):
    """Wanna know what your silhouette looks like? CLICK THIS AND FIND OUT!"""
    bl_idname = abs_idbase + ".silhouette_mode"
    bl_label = "Toggle Silhouette"
    bl_options = {"REGISTER"}

    # Init some properties on the scene so we can store our current state
    bpy.types.Scene.is_silhoutte_mode = bpy.props.BoolProperty()
    bpy.types.Scene.prev_viewport_shade = bpy.props.StringProperty()
    bpy.types.Scene.silhouette_material = bpy.props.StringProperty()
    bpy.types.Scene.prev_materials = bpy.props.StringProperty()

    def execute(self, context):
        # Get some references
        scene = context.scene
        space = context.space_data
        object = context.object

        # Are we in the right place?
        if space.type != "VIEW_3D":
            self.report({"ERROR"}, "Must be in 3D view")
            return {"FINISHED"}

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
            return {"FINISHED"}
        
        # Ok, we're not in silhoutte mode. Get to it!
        material = None
        if bpy.data.materials[scene.silhouette_material]:
            material = bpy.data.materials[scene.silhouette_material]
        else:
            material = bpy.data.materials.new("SilhoutteMaterial")
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
        self.report({"INFO"}, "Set course for mark 3, 2, 4. Silhoutte Mode, ENGAGE!")
        return {"FINISHED"}


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
