
init -10:
    transform gui_shine:
        additive 1.0 alpha 0.5
        block:
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.5
            repeat

    transform gui_dissolve_left:
        xoffset -32 alpha 0.0
        easein_quint 0.25 xoffset 0 alpha 1.0
        on hide:
            easeout_quint 0.25 xoffset -32 alpha 0.0

    transform gui_dissolve_right:
        xoffset 32 alpha 0.0
        easein_quint 0.25 xoffset 0 alpha 1.0
        on hide:
            easeout_quint 0.25 xoffset 32 alpha 0.0

    transform nav_dissolve_top:
        on show:
            yoffset -32 alpha 0.0
            easein_quint 0.25 yoffset 0 alpha 1.0
        on hide:
            easeout_quint 0.25 yoffset -32 alpha 0.0

    transform gui_dissolve:
        alpha 0.0
        easein_quint 0.25 alpha 1.0
        on hide:
            easeout_quint 0.25 alpha 0.0

    transform nav_dissolve_left:
        on show:
            xoffset -32 alpha 0.0
            easein_quint 0.25 xoffset 0 alpha 1.0
        on hide:
            easeout_quint 0.25 xoffset -32 alpha 0.0

    transform gui_dissolve_top:
        yoffset -32 alpha 0.0
        easein_quint 0.25 yoffset 0 alpha 1.0
        on hide:
            easeout_quint 0.25 yoffset -32 alpha 0.0

    transform gui_dissolve_bottom:
        yoffset 32 alpha 0.0
        easein_quint 0.25 yoffset 0 alpha 1.0
        on hide:
            easeout_quint 0.25 yoffset 32 alpha 0.0

init:
    transform aero_inter:
        on show:
            alpha 0
            linear 0.3 alpha 1
        on replace:
            alpha 0
            linear 0.3 alpha 1
        on replaced:
            linear 0.3 alpha 0
        on hide:
            linear 0.3 alpha 0
    transform aero_base:
        alpha 0.75
    transform aero_ring_rotate(d, t):
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom 1.5
        easeout 0.25 zoom 1.0
        block:
            rotate 0.0
            linear t rotate (d * 360.0)
            repeat
    transform aero_selection_show(i, n):
        subpixel True
        xcenter 0.5
        ycenter 0.5
        rotate (aero.get_button_angle(i, n) - 20.0)
        zoom 1.5
        parallel:
            power_in_time_warp_real 0.75 rotate aero.get_button_angle(i, n)
        parallel:
            easeout 0.25 zoom 1.0
    transform aero_selection_replace(i, n):
        xcenter 0.5
        ycenter 0.5
        zoom 1.0
        power_in_time_warp_real 0.5 rotate aero.get_button_angle(i, n)
    transform aero_button(i, n):
        subpixel True
        anchor (0.5, 0.5)
        around (0.5, 0.5)
        alpha 0 angle aero.get_button_angle(i, n) radius 0.27
        0.15
        parallel:
            linear 0.15 alpha 1
        parallel:
            power_in_time_warp_real 0.3 radius 0.3
    style aero_text is text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(29)
        outlines [(scale(1.0), "#000")]
        color "#ddd"
    style aero_frame is default:
        xcenter 0.5
        ycenter 0.5
    style aero_fixed is fixed:
        fit_first True
    style aero_button is default:
        xcenter 0.5
        xmargin scale(-7)
        ymargin scale(-7)
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"
    style aero_button_text is aero_text:
        outlines [
            (scale(1.0), "#000"),
            (scale(6.0), "#0000")
        ]
        hover_color "#fff"
        hover_outlines [
            (scale(1.0), "#169c5f"),
            (scale(6.0), "#0000")
        ]
        selected_outlines [
            (scale(6.0), "#124e4607"),
            (scale(5.0), "#124e460f"),
            (scale(4.0), "#124e461f"),
            (scale(3.0), "#124e462f"),
            (scale(2.0), "#124e463f"),
            (scale(1.0), "#124e46")
        ]
        selected_color "#c5c4c2"
        selected_hover_outlines [
            (scale(6.0), "#124e460f"),
            (scale(5.0), "#124e461f"),
            (scale(4.0), "#124e463f"),
            (scale(3.0), "#124e465f"),
            (scale(2.0), "#124e467f"),
            (scale(1.0), "#169c5f")
        ]
        selected_hover_color "#fff"
            

transform walkin_l(x=0.5, y=0.5):
    alpha 0.0 additive 0.0 xpos x ypos y xoffset -16 yoffset 0
    easein 0.25 alpha 1.0 xoffset 0

transform show_state(x=0.5, y=0.7):
    alpha 0.0 anchor (0.5, 0.5) xpos x ypos y yoffset 6 additive 0.25
    easein 0.25 alpha 0.95 yoffset 0
    linear 0.5 yoffset -6
    linear 0.25 yoffset -9 alpha 0
    on hide:
        linear 0.25 yoffset -9 alpha 0

transform flash_enemy(x=0.5):
    alpha 1.0 pos (x, 0.45) zoom 0.8
    easeout 0.25 alpha 0.0 zoom 0.9 additive 1.0

transform zoomshining:
    zoom 1.04 additive 1.0 alpha 0.0
    block:
        ease 1.5 alpha 1.0
        ease 1.5 alpha 0.0
        repeat

transform shake(t=0.4, dist=128):
    alpha 1.0
    function renpy.curry(_shake_function)(dt=t, dist=dist)

transform adjust:
    xoffset 0 yoffset 0 alpha 1.0

transform hide_out:
    adjust
    on hide:
        easeout 0.25 alpha 0.0 xoffset 32

transform smallshake(dt=0.4, dist=102):
    function renpy.curry(_shake_function)(dt=dt,dist=dist)

transform sway_r(t=0.2):
    alpha 1.0
    ease t / 3 xoffset 96
    ease t * 2 / 3 xoffset 0

transform sway_l(t=.2):
    alpha 1.0
    ease t/3 xoffset -96
    ease t*2/3 xoffset 0

transform show_ability(x=0.5, y=0.2):
    alpha 0.5 anchor (0.5, 0.5) xpos x ypos y yoffset 0 zoom 3.0 additive 1.0
    easein 0.2 alpha 0.95 zoom 1.0 additive 0.25
    ease 0.05 yoffset -32
    ease 0.15 yoffset 0
    linear 0.3 alpha 0.0 additive 1.0

transform show_finish(x=0.5):
    alpha 0.5 anchor (0.5, 0.5) xpos x ypos 0.45 zoom 3.0 additive 1.0
    easein 0.2 alpha 0.95 zoom 1.1 additive 0.25
    linear 0.3 yoffset 0 zoom 1.0
    on hide:
        easeout 0.2 alpha 0 zoom 1.5 additive 1.0

transform show_player(x=0.5):
    on show:
        xpos x ypos 0.5 zoom 1.0 alpha 0.0 xoffset 32
        easein 0.25 alpha 1.0 xoffset 0
    on hide:
        easeout 0.25 alpha 0.0 xoffset 32
    on update:
        xpos x ypos 0.5 zoom 1.0 alpha 1.0

transform spellin(x=0.5):
    on show:
        anchor (0.5, 0.5) xpos x ypos 0.5 zoom 4.5 alpha 0.0 additive 1.0
        easein 0.2 zoom 1.5 alpha 0.75 additive 0.25
    on hide:
        easeout 0.2 zoom 4.5 alpha 0.0 additive 1.0

transform show_damage(x=0.5, y=0.5):
    alpha 0.5 anchor (0.5, 0.5) xpos x ypos y yoffset 0 zoom 3.0 additive 1.0
    easein 0.2 alpha 0.95 zoom 1.0 additive 0.25
    ease 0.05 yoffset -32
    ease 0.15 yoffset 0
    linear 0.75 alpha 0.0 additive 1.0

transform effect_enemy(x=0.5):
    anchor (0.5, 0.5) xpos x ypos 0.4 zoom 1.6 additive 0.5

transform flash_player(x=0.5):
    alpha 1.0 pos (x, 0.5) zoom 1.0
    easeout 0.25 alpha 0.0 zoom 1.13 additive 1.0

transform effect_player(x=0.5):
    anchor (0.5, 0.5) xpos x ypos 0.5 zoom 2.0 additive 0.5

transform show_skill(x=0.85, y=0.75):
    alpha 0.0 xoffset -16 align (0.5, 1.0) xpos x ypos y additive 1.0
    easein 0.2 alpha 1.0 xoffset 0 additive 0.15
    on hide:
        easeout 0.2 xoffset 16 alpha 0 additive 1.0

transform show_enemy(x=0.5):
    on show:
        xpos x ypos 0.45 zoom 0.8 alpha 0.0 xoffset -32
        easein 0.25 alpha 1.0 xoffset 0
    on hide:
        easeout 0.25 alpha 0.0 xoffset -32

transform smallfloating:
    block:
        easein 0.75 yoffset -8
        ease 1.5 yoffset 8
        easeout 0.75 yoffset 0
        repeat

transform position(x=0.5, y=0.5, t=0.5):
    on show:
        anchor(0.5, 0.5) xpos x ypos y
    on replace:
        ease t xpos x ypos y alpha 1.0

transform spellout(x=0.5):
    on show:
        anchor (0.5, 0.5) xpos x ypos 0.5 zoom 0.0 alpha 0.0 additive 1.0
        easein 0.2 zoom 1.5 alpha 0.75 additive 0.25
    on hide:
        easeout 0.2 zoom 0.0 alpha 0.0 additive 1.0

transform slide_flash_player(x=0.5):
    alpha 1.0 pos (x, 0.5) zoom 1.0 xoffset 32
    parallel:
        easein 0.25 xoffset 0
    parallel:
        easeout 0.25 alpha 0.0 zoom 1.13 additive 1.0

transform heroine_status_not_focus:
    zoom 1.6
    alpha 0.3


transform heroine_status_focus:
    alpha 1.0
    xalign 0.5
    zoom 1.0
    yalign 0.5


transform inventory_show_hide:
    on show:
        zoom 0.5
        alpha 0.0
        yoffset 50.0
        easein 0.5 zoom 0.7 alpha 1.0 yoffset 0
    on hide:
        zoom 0.7
        alpha 1.0
        yoffset 0.0
        easeout 0.5 zoom 0.5 alpha 0.0 yoffset 50.0


transform battle_equipment_chooser_show_hide:
    on show:
        zoom 0.5
        alpha 0.0
        yalign 1.0 xalign 0.5
        easein 0.5 zoom 0.7 alpha 1.0 yalign 0.5
    on hide:
        zoom 0.7
        alpha 1.0
        yalign 0.5 xalign 0.5
        easeout 0.5 zoom 0.5 alpha 0.0 yalign 1.0


transform battle_cardgame_show_hide:
    on show:
        zoom 0.7
        alpha 0.0
        yalign 1.0 xalign 0.5
        easein 0.5 zoom 1.0 alpha 1.0 yalign 0.5
    on hide:
        zoom 1.0
        alpha 1.0
        yalign 0.5 xalign 0.5
        easeout 0.5 zoom 0.7 alpha 0.8 yalign 1.0
