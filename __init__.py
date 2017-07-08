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
    "category": "Toolkit"
}

if "bpy" in locals():
    import imp
    imp.reload(silhouette_mode)
    imp.reload(loom)
else:
    from . import silhouette_mode
    from . import loom

import bpy

def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
