define persistent.reduce_sprite_res = True

init -900 python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals



    def pick_actor_path(default, low):
        return default if not persistent.reduce_sprite_res else low

    def scale_sprite_zoom(z):
        return scale(
            z
            if not persistent.reduce_sprite_res
            else z * 2)

    def scale_sprite_offset(x, y):
        return (
            (x, y)
            if not persistent.reduce_sprite_res
            else (absolute(x / 2), absolute(y / 2)))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
