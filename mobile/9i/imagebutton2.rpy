
init -10 python:
    class ImageButton2(renpy.Displayable):
        
        def __init__(self,
                     idle_image,
                     hover_image = None,
                     insensitive_image = None,
                     activate_image = None,
                     selected_idle_image = None,
                     selected_hover_image = None,
                     selected_insensitive_image = None,
                     selected_activate_image = None,
                     action=None,
                     hovered=None,
                     unhovered=None,
                     focus_mask=True,
                     **properties):
            super(ImageButton2, self).__init__(**properties)
            
            self.idle_image = idle_image
            self.hover_image = hover_image or idle_image
            self.insensitive_image = insensitive_image or idle_image
            self.activate_image = activate_image or self.hover_image
            
            self.selected_idle_image = selected_idle_image or idle_image
            self.selected_hover_image = selected_hover_image or self.hover_image
            self.selected_insensitive_image = selected_insensitive_image or self.insensitive_image
            self.selected_activate_image = selected_activate_image or self.activate_image
            
            self.idle_image = renpy.displayable(self.idle_image)
            self.hover_image = renpy.displayable(self.hover_image)
            self.insensitive_image = renpy.displayable(self.insensitive_image)
            self.activate_image = renpy.displayable(self.activate_image)
            
            self.selected_idle_image = renpy.displayable(self.selected_idle_image)
            self.selected_hover_image = renpy.displayable(self.selected_hover_image)
            self.selected_insensitive_image = renpy.displayable(self.selected_insensitive_image)
            self.selected_activate_image = renpy.displayable(self.selected_activate_image)
            
            self.action=action
            self.hovered=hovered
            self.unhovered = unhovered
            
            self.is_clicked = False
            self.is_hovered = False
            self.child = None
            self.focus_mask = focus_mask
        
        def render(self, width, height, st, at):
            
            if renpy.display.behavior.is_selected(self.action):
                if not renpy.display.behavior.is_sensitive(self.action):
                    self.child = self.selected_insensitive_image
                elif self.is_clicked:
                    self.child = self.selected_activate_image
                elif self.is_hovered:
                    self.child = self.selected_hover_image
                else:
                    self.child = self.selected_idle_image
            else:
                if not renpy.display.behavior.is_sensitive(self.action):
                    self.child = self.insensitive_image
                elif self.is_clicked:
                    self.child = self.activate_image
                elif self.is_hovered:
                    self.child = self.hover_image
                else:
                    self.child = self.idle_image
            
            
            child_render = renpy.render(self.child, width, height, st, at)
            
            
            self.width, self.height = child_render.get_size()
            
            
            render = renpy.Render(self.width, self.height)
            
            
            render.blit(child_render, (0, 0))
            
            self.child_render = child_render
            
            return render
        
        def event(self, ev, x, y, st):
            if (self.focus_mask and self.child_render.is_pixel_opaque(x, y)) or (not self.focus_mask and 0 < x and x < self.width and 0 < y and y < self.height):
                if renpy.display.behavior.is_sensitive(self.hovered) and not self.is_hovered:
                    self.is_hovered = True
                    renpy.run_action(self.hovered)
                    renpy.restart_interaction()
                    renpy.redraw(self, 0)
                elif renpy.map_event(ev, "mousedown_1"):
                    self.is_clicked = True
                    renpy.restart_interaction()
                    renpy.redraw(self, 0)
                elif renpy.map_event(ev, "mouseup_1"):
                    self.is_clicked = False
                    if renpy.display.behavior.is_sensitive(self.action):
                        renpy.run_action(self.action)
                    renpy.restart_interaction()
                    renpy.redraw(self, 0)
            else:
                if self.is_hovered:
                    self.is_hovered = False
                    if renpy.display.behavior.is_sensitive(self.unhovered):
                        renpy.run_action(self.unhovered)
                    renpy.restart_interaction()
                    renpy.redraw(self, 0)
                if self.is_clicked:
                    self.is_hovered = False
                    self.is_clicked = False
                    renpy.restart_interaction()
                    renpy.redraw(self, 0)
            
            
            return self.child.event(ev, x, y, st)
        
        def per_interact(self):
            renpy.redraw(self, 0)
        
        def visit(self):
            return [ self.child ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
