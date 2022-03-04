

init -2000 python:
    def _open_image_viewer():
        if not renpy.config.developer:
            return
        default = ()
        while True:
            name = renpy.invoke_in_new_context(renpy.call_screen, "_image_selecter", default=default)
            if isinstance(name, tuple): 
                default = tuple(set(name))
            elif name: 
                default = tuple(name.split())
            else:
                renpy.notify("Please type image name")
                return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
