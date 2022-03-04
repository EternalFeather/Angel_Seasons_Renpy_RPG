python early in investigation:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    class InvestigationWrapper(renpy.display.layout.MultiBox):
        """
        Wrapper container that forwards input its children receive to the
        camera, so camera inputs function normally when the mouse is over it.
        """
        
        def __init__(self, tag, layer, *args, **kwargs):
            super(InvestigationWrapper, self).__init__(
                layout = "fixed",
                fit_first = True,
                *args,
                **kwargs)
            self.tag = tag
            self.layer = layer
        
        def event(self, ev, x, y, st):
            global _wrapper_click

            if renpy.map_event(ev, "mousedown_3"):
                _deferred_events.append(ev)
                _wrapper_click = ((self.tag, self.layer), ev.pos)
                renpy.timeout(0)
            
            elif renpy.map_event(ev, "mouseup_3"):
                _deferred_events.append(ev)
                renpy.timeout(0)
                
                
                
                
                if _wrapper_click is None: return None
                
                wrapper, (x0, y0) = _wrapper_click
                if wrapper != (self.tag, self.layer): return None
                
                _wrapper_click = None

                dx, dy = (abs(ev.pos[0] - x0), abs(ev.pos[1] - y0))
                if dx > CLICK_ZONE or dy > CLICK_ZONE: return None
            
            return super(InvestigationWrapper, self).event(ev, x, y, st)
        
        def __repr__(self):
            return "<{} ({} onlayer {}) at {}>".format(
                self.__class__.__name__, self.tag, self.layer, id(self))

    renpy.register_sl_displayable(
        "ivmwrapper",
        InvestigationWrapper,
        "ivmwrapper",
        nchildren = "many").add_positional("tag").add_positional("layer")

default investigation._deferred_events = list()
default investigation._wrapper_click = None

define investigation.CLICK_ZONE = 1.0

style ivmwrapper is default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
