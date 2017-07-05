# Copyright Arctic Beard Studio 2017

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

import bpy


class Align(bpy.types.Operator):
    """I heard you like aligning stuff, so i wrote this function so you can align stuff to other stuff."""
    bl_idname = "arctic_beard_studio.align"
    bl_label = "Align"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("Shit just got aligned! *harkle*... actually this is just a dummy function... #sadface :(")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(Align)


def unregister():
    bpy.utils.unregister_class(Align)


if __name__ == "__main__":
    register()
