
screen _image_selecter(default, string=""):
    key "game_menu" action Return("")
    zorder 20
    $ default_set = set(default)
    for e in default:
        $ string += e + " "
    frame:
        background "#0006"
        xalign 1.
        has vbox
        label "Type a image name"

        input default string
        if default:
            $ s = set()
            for name in renpy.display.image.images:
                $ name_set = set(name)
                if default_set < name_set:
                    $ s.update(name_set-default_set)
                elif default_set == name_set:
                    $ s.update(default_set)
        else:
            $ s = {name[0] for name in renpy.display.image.images}
        viewport:
            mousewheel True
            xmaximum 400


            scrollbars "both"
            has vbox:
                style_group "image_selecter"
            for tag in tuple(s):
                textbutton tag action Return(default + (tag, )) hovered _viewers.ShowImage(default, tag) unhovered Function(renpy.hide, "preview", layer="screens")










init:
    style image_selecter_button is button:
        size_group "image_selecter"
        idle_background None
    style image_selecter_button_text is button_text xalign .0

init python:
    @renpy.pure
    class _ImageInputValue(ScreenVariableInputValue, FieldEquality):
        
        def __init__(self, variable, default=True):
            super(_ImageInputValue, self).__init__(variable, default, returnable=True)
        
        def set_text(self, s):
            if s and s[-1] == " ":
                for n in renpy.display.image.images:
                    if set(n) == set(name.split()):
                        self.state[layer][name] = {}
                        renpy.show(name, layer=layer)
                        for p, d in self.props:
                            self.state[layer][name][p] = self.get_property(layer, name.split()[0], p, False)
                        all_keyframes[(name, layer, "xpos")] = [(self.state[layer][name]["xpos"], 0, None)]
                        remove_list = [n_org for n_org in self.state_org[layer] if n_org.split()[0] == n[0]]
                        for n_org in remove_list:
                            del self.state_org[layer][n_org]
                            transform_viewer.remove_keyframes(n_org, layer)
                        sort_keyframes()
                        renpy.show_screen("_action_editor", tab="images", layer=layer, name=name)
                        return
                default = tuple(s.split())
                renpy.show_screen("_image_selecter", default=default)
            super(_ImageInputValue, self).set_text(s)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
