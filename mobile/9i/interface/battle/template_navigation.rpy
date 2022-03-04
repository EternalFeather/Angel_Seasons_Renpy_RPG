
screen template_navigation_back(back_action=Return()):
    frame:
        xalign 0.98
        yalign 0.98

        has vbox
        imagebutton: 
            activate_sound "9i/interface/click2.ogg"
            xpadding 20 ypadding 20
            idle "9i/interface/battle/system/back.png"
            hover im.MatrixColor("9i/interface/battle/system/back.png", im.matrix.tint(1, 0, 0.5))
            action back_action
