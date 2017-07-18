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
    imp.reload(ultra_viking)
else:
    from . import silhouette_mode
    from . import loom
    from . import ultra_viking

import bpy

addon_keymaps = []

def menu_func(self, context):
    self.layout.operator(ultra_viking.ToggleSelectSync.bl_idname)

def register():
    # register
    bpy.utils.register_module(__name__)
    bpy.types.IMAGE_MT_select.append(menu_func)
    
    # handle keymaps
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Ultra Viking", space_type="IMAGE_EDITOR")

    kmi = km.keymap_items.new(ultra_viking.ToggleSelectSync.bl_idname, "BUTTON5MOUSE", "PRESS")
    kmi.active = True

    addon_keymaps.append(km)


def unregister():
    # unregister
    bpy.utils.unregister_module(__name__)
    bpy.types.IMAGE_MT_select.remove(menu_func)
    
    # handle keymaps
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    
    del addon_keymaps[:]


if __name__ == "__main__":
    register()
