
init -1 python:
    def support(heroine):
        renpy.music.play("9i/interface/battle/battle_music/comlink_online.ogg", channel="audio")
        renpy.call_screen("battle_start_support", heroine)
        return


screen battle_start_support(image_name=None):
    frame at heroine_support_bg:
        background None
        foreground None

        add "support_bg_" + image_name.support_color:
            yalign 0.5
        add "slices_" + image_name.support_color + "_1"
        add "slices_" + image_name.support_color + "_2"
        add "slices_" + image_name.support_color + "_3"
        add "slices_" + image_name.support_color + "_4"

    if image_name.support_direct == "left":
        frame at heroine_support_sprite_left:
            background None
            foreground None
            add "support_effect_" + image_name.objectname.replace("_mirror", "")
    else:
        frame at heroine_support_sprite_right:
            background None
            foreground None
            add "support_effect_" + image_name.objectname.replace("_mirror", "")

    timer 2.0 action Return()


transform heroine_support_bg:
    on show:
        alpha 0.0 xanchor 0.0 xpos 1.0 yalign 0.5
        easein 0.4 xanchor 1.05 alpha 1.0
        pause 2.0
    on hide:
        alpha 1.0 xanchor 0.0 xpos 0.0 yalign 0.5
        easeout 0.4 xanchor 0.5 alpha 0.0


transform heroine_support_sprite_right:
    on show:
        alpha 1.0 xanchor 0.0 xpos 0.98 yanchor 1.0 ypos 1.05
        easein 0.8 xanchor 1.0
        pause 2.0
    on hide:
        alpha 1.0 xanchor 0.0 xpos 0.02 yanchor 1.0 ypos 1.05
        easeout 0.6 xanchor 1.0 xpos -0.5


transform heroine_support_sprite_left:
    on show:
        alpha 1.0 xanchor 1.0 xpos 0.1 yanchor 1.0 ypos 1.05
        easein 0.8 xanchor 0.0
        pause 2.0
    on hide:
        alpha 1.0 xanchor 1.0 xpos 0.9 yanchor 1.0 ypos 1.05
        easeout 0.8 xanchor 0.0 xpos 1.5
