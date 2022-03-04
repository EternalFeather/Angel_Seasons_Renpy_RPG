
label second_menu:
    
    $ suppress_overlay = True
    stop music fadeout 4.0
    scene black 
    with Dissolve(8.0)
    pause 3.0 hard

    play music "music/gal.ogg" fadeout 4.0 fadein 3.0
    show sec_menu_bg
    show screen second_menu

    $ renpy.block_rollback()
    $ _rollback = False

    $ ui.interact()


screen second_menu():
    $ continue_slot = renpy.newest_slot("(?!_reload)")

    imagebutton xalign 0.1 yalign 0.16:
        idle 'title/system/start/ssel_ps1_idle.png'
        hover 'title/system/start/ssel_ps1_hover.png'
        selected_idle 'title/system/start/ssel_ps1_hover.png'
        action [Hide('second_menu', transition=Dissolve), Stop("music", fadeout=4.0), Jump('day201'), Play('sound', 'sound/system/start.wav')] 
        hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
        at gui_slide_down(3.0)

    if persistent.youjia == True:
        imagebutton xalign 0.5 yalign 0.16:
            idle 'title/system/start/ssel_ps5_idle.png'
            hover 'title/system/start/ssel_ps5_hover.png'
            selected_idle 'title/system/start/ssel_ps5_hover.png'
            action [Hide('second_menu', transition=Dissolve), Stop("music", fadeout=4.0), Jump('day207'), Play('sound', 'sound/system/start.wav')] 
            hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_down(3.1)
    else:
        imagebutton xalign 0.5 yalign 0.16:
            idle 'title/system/start/ssel_ps5_locked.png'
            at gui_slide_down(3.1)

    if persistent.szl_ling == True:
        imagebutton xalign 0.9 yalign 0.16:
            idle 'title/system/start/ssel_ps4_idle.png'
            hover 'title/system/start/ssel_ps4_hover.png'
            selected_idle 'title/system/start/ssel_ps4_hover.png'
            action [Hide('second_menu', transition=Dissolve), Stop("music", fadeout=4.0), Jump('day209'), Play('sound', 'sound/system/start.wav')] 
            hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_down(3.2)
    else:
        imagebutton xalign 0.9 yalign 0.16:
            idle 'title/system/start/ssel_ps4_locked.png'
            at gui_slide_down(3.2)

    if persistent.lihuaxi == True:
        imagebutton xalign 0.1 yalign 0.57:
            idle 'title/system/start/ssel_ps6_idle.png'
            hover 'title/system/start/ssel_ps6_hover.png'
            selected_idle 'title/system/start/ssel_ps6_hover.png'
            action [Hide('second_menu', transition=Dissolve), Stop("music", fadeout=4.0), Jump('day216'), Play('sound', 'sound/system/start.wav')] 
            hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_down(3.3)
    else:
        imagebutton xalign 0.1 yalign 0.57:
            idle 'title/system/start/ssel_ps6_locked.png'
            at gui_slide_down(3.3)

    if persistent.liuli == True:
        imagebutton xalign 0.5 yalign 0.57:
            idle 'title/system/start/ssel_ps3_idle.png'
            hover 'title/system/start/ssel_ps3_hover.png'
            selected_idle 'title/system/start/ssel_ps3_hover.png'
            action [Hide('second_menu', transition=Dissolve), Stop("music", fadeout=4.0), Jump('day219'), Play('sound', 'sound/system/start.wav')] 
            hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_down(3.4)
    else:
        imagebutton xalign 0.5 yalign 0.57:
            idle 'title/system/start/ssel_ps3_locked.png'
            at gui_slide_down(3.4)

    if persistent.xifeier == True:
        imagebutton xalign 0.9 yalign 0.57:
            idle 'title/system/start/ssel_ps2_idle.png'
            hover 'title/system/start/ssel_ps2_hover.png'
            selected_idle 'title/system/start/ssel_ps2_hover.png'
            action [Hide('second_menu', transition=Dissolve), Stop("music", fadeout=4.0), Jump('day226'), Play('sound', 'sound/system/start.wav')] 
            hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_down(3.5)
    else:
        imagebutton xalign 0.9 yalign 0.57:
            idle 'title/system/start/ssel_ps2_locked.png'
            at gui_slide_down(3.5)
    
    if persistent.lisite == True:
        imagebutton xalign 0.18 yalign 0.91:
            idle 'title/system/start/ssel_ps8_idle.png'
            hover 'title/system/start/ssel_ps8_hover.png'
            selected_idle 'title/system/start/ssel_ps8_hover.png'
            action [Hide('second_menu', transition=Dissolve), Stop("music", fadeout=4.0), Jump('day223'), Play('sound', 'sound/system/start.wav')] 
            hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_down(3.6)
    else:
        imagebutton xalign 0.18 yalign 0.91:
            idle 'title/system/start/ssel_ps8_locked.png'
            at gui_slide_down(3.6)

    if persistent.lingyin == True:
        imagebutton xalign 0.76 yalign 0.95:
            idle 'title/system/start/ssel_ps7_idle.png'
            hover 'title/system/start/ssel_ps7_hover.png'
            selected_idle 'title/system/start/ssel_ps7_hover.png'
            action [Hide('second_menu', transition=Dissolve), Stop("music", fadeout=4.0), Jump('day206'), Play('sound', 'sound/system/start.wav')] 
            hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_down(3.7)
    else:
        imagebutton xalign 0.76 yalign 0.95:
            idle 'title/system/start/ssel_ps7_locked.png'
            at gui_slide_down(3.8)

    imagebutton xalign 0.95 yalign 0.85:
        idle 'title/system/start/title_logo_idle.png'
        hover 'title/system/start/title_logo_hover.png'
        selected_idle 'title/system/start/title_logo_hover.png'
        action NullAction()
        # action [Hide('second_menu', transition=Dissolve), Jump('day301'), Play('sound', 'sound/system/start.wav')] 
        hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
        at gui_slide_down(3.9)

    imagebutton xalign 0.95 yalign 0.95:
        idle 'title/system/start/titleback_idle.png'
        hover 'title/system/start/titleback_hover.png'
        selected_idle 'title/system/start/titleback_hover.png'
        action [MainMenu(confirm=True), Play('sound', 'sound/system/select.ogg')] 
        hovered Play('sound', 'sound/system/hover.wav', fadein=0.2, fadeout=0.2)
        at gui_slide_down(4.0)

    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()

init:
    image sec_menu_bg:
        "title/system/second_menu.png"
        imagescale(1080)
        on show:
            alpha 0
            linear 2.0 alpha 1
        on hide:
            linear 2.0 alpha 0

