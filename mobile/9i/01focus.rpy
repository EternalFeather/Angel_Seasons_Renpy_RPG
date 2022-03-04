

python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def key_handler(ev):
        from renpy.display.behavior import map_event
        from renpy.display.focus import focus_nearest, focus_ordered
        from renpy.display.focus import horiz_line_dist, verti_line_dist
        
        if renpy.game.preferences.self_voicing:
            if map_event(ev, 'focus_right') or map_event(ev, 'focus_down'):
                return focus_ordered(1)
            
            if map_event(ev, 'focus_left') or map_event(ev, 'focus_up'):
                return focus_ordered(-1)
        
        else:
            if map_event(ev, 'focus_right'):
                return focus_nearest(0.9, 0.1, 0.9, 0.9,
                                     0.1, 0.1, 0.1, 0.9,
                                     verti_line_dist,
                                     lambda old, new : old.x < new.x,
                                     -1, 0, 0, 0)
            if map_event(ev, 'focus_left'):
                return focus_nearest(0.1, 0.1, 0.1, 0.9,
                                     0.9, 0.1, 0.9, 0.9,
                                     verti_line_dist,
                                     lambda old, new : new.x < old.x,
                                     1, 0, 1, 0)
            if map_event(ev, 'focus_up'):
                return focus_nearest(0.1, 0.1, 0.9, 0.1,
                                     0.1, 0.9, 0.9, 0.9,
                                     horiz_line_dist,
                                     lambda old, new : new.y < old.y,
                                     0, 1, 0, 1)
            if map_event(ev, 'focus_down'):
                return focus_nearest(0.1, 0.9, 0.9, 0.9,
                                     0.1, 0.1, 0.9, 0.1,
                                     horiz_line_dist,
                                     lambda old, new : old.y < new.y,
                                     0, -1, 0, 0)
    renpy.display.focus.key_handler = key_handler
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
