label main_menu:
    if not persistent.break_title:
        scene black
        with None

        $ camera_reset()
        $ season, time = get_title_attrs()
        play music main_menu_op2 fadein 2.0
        
        show set main_menu expression "[season] [time]"
        show expression mmflcam as mmflcam onlayer texture
        $ mmflcam.move(0, 0, 400)
        $ mmflcam.move(0, 0, 100, duration=3.0)
        show black onlayer texture with None
        hide black onlayer texture
        $ renpy.transition(slowdissolve, layer='texture')

        show system mm shadow as shadow onlayer texture
        pause 2.1
        show system mm logo white as logo onlayer texture
        pause 1.9
        show expression "title/copyright.png" onlayer screens at mainlogoslide
        show screen main_menu

        if persistent._in_replay is not None:
            $ Show("gallery")()
            $ persistent._in_replay = None
    else:
        $ persistent.break_title = False
        show movie onlayer texture
        play movie "video/prologue06.mp4" loop
        $ renpy.music.play("video/prologue06.mp3", synchro_start='movie', loop=False)
        $ _window_animation = 'in'
        show expression "title/ms2_faultms2logo.png" onlayer screens at mainlogoslide
        pause 11.5 hard
        show screen break_menu
    while True:
        $ ui.interact(mouse='screen')


screen main_menu():

    $ continue_slot = renpy.newest_slot("(?!_reload)")
    frame style_prefix "mm":
        has vbox at mm_buttons_inter
        textbutton _("{#mm}追忆之庭"):
            if any([param in ["春之章", "夏之章", "秋之章", "冬之章", "最终战"] for param in persistent.stories]):
                action [
                    Hide('main_menu', transition=Dissolve), 
                    Start('anthor'), 
                    Play('sound', 'se_sys/start.wav')
                ]
                hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.0)
        
        if persistent.now_story == "秋之章":
            textbutton _("{#mm}预告"):
                action [Hide('main_menu', transition=Dissolve), Stop("music", fadeout=4.0), Play('sound', 'sound/first_game_start.wav', fadein=0.2, fadeout=0.2), Start("prelabel")]
                hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
                at gui_slide_left(.1)
        elif persistent.now_story == "冬之章":
            textbutton _("{#mm}冬之章"):
                action [Hide('main_menu', transition=Dissolve), Stop("music", fadeout=4.0), Play('sound', 'sound/first_game_start.wav', fadein=0.2, fadeout=0.2), Start("second_menu")]
                hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
                at gui_slide_left(.1)
        elif persistent.now_story == "夏之章":
            textbutton _("{#mm}夏之章"):
                action [Hide('main_menu', transition=Dissolve), Stop("music", fadeout=4.0), Start("day01")]
                hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
                at gui_slide_left(.1)
        textbutton _("{#mm}载入"):
            action [Show("load"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.2)
        textbutton _("{#mm}图鉴"):
            action [Show("encyclopedia"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.3)
        textbutton _("{#mm}画廊"):
            action [Show("gallery"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.4)
        textbutton _("{#mm}设置"):
            action [Show("preferences"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.5)
        textbutton _("{#mm}退出"):
            action [Hide("main_menu"), Quit(confirm=True)]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.6)

    add "particles"
    timer 60 action UpdateTitleSet() repeat

screen break_menu():
    button style "default" xoffset -65 at mm_show:

        add imagescale(1104)("title/undo.png")
        action [
            Stop("music", fadeout=2.0),
            Stop("movie"),
            Function(renpy.load, persistent.restart_place)
        ]
        focus_mask True

init:
    transform mm_show:
        alpha 0
        linear 0.3 alpha 1
    transform mm_dissolve(old_widget, new_widget):
        delay 30
        contains:
            new_widget
            events True
            alpha 0
            linear 10 alpha 1
        contains:
            old_widget
            events False
            10
            linear 20 alpha 0
    transform mm_buttons_inter:
        alpha 0
        linear 0.3 alpha 1

    image system mm shadow:
        "title/shadow.png"
        imagescale(540)
        subpixel True
        transform_anchor True
        xcenter 0.5
        ycenter 0.5
        alpha 0
        linear 1.5 alpha 1
    image system mm logo white:
        "title/stp logo white.png"
        imagescale(1080)
        subpixel True
        transform_anchor True
        xcenter 0.5
        ycenter 0.3
        alpha 0
        additive 1
        zoom 1.08
        parallel:
            linear 0.3 alpha 1
        parallel:
            ease 1.5 additive 0
        parallel:
            easein_cubic 1.0 zoom 1.0

    style mm_frame is default:
        xcenter 0.5
        ypos scale(990)
        yanchor 1.0
    style mm_vbox is vbox:
        xcenter 0.5
        ycenter 0.5
        spacing scale(3)
    style mm_button is default:
        xsize int(scale(316.5))
        ysize int(scale(48.5))
        hover_background imagescale(1080)("title/button hover.png")
    style mm_button_text is text:
        xcenter 0.5
        ycenter 0.5
        # font "9i/fonts/FOT-SkipStd-B.otf"
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(32)
        color "#fff"
        insensitive_color "#998"
        outlines [(scale(2.5), "#3f251d", scale(0.0), scale(1.5))]
        hover_outlines [(scale(2.5), "#e3a234", scale(0.0), scale(1.5))]

init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    @renpy.pure
    class UpdateTitleSet(renpy.ui.Action):
        def __call__(self):
            current_attrs = (
                renpy.game.context().images.get_attributes(
                    layer='b1',
                    tag='main_menu-bg'))
            
            attrs = get_title_attrs()
            
            if current_attrs == attrs: return
            
            sets.registry['main_menu'].show(attrs)
            
            for layer in renpy.store._3d_layers:
                renpy.transition(mm_dissolve, layer=layer)
            
            renpy.restart_interaction()

    def get_title_attrs():
        import datetime
        
        MAR_EQUINOX = (3, 20)
        JUN_SOLSTICE = (6, 21)
        SEP_EQUINOX = (9, 22)
        DEC_SOLSTICE = (12, 21)
        
        MORNING_START = datetime.time(6)
        AFTERNOON_START = datetime.time(15, 30)
        NIGHT_START = datetime.time(19, 30)
        
        now = datetime.datetime.now()
        datenow, timenow = (now.date(), now.time())
        doy = (datenow.month, datenow.day)
        
        season = 'summer'
        
        time = None
        if MORNING_START <= timenow < AFTERNOON_START:
            time = 'day'
        elif AFTERNOON_START <= timenow < NIGHT_START:
            time = 'evening'
        else:
            time = 'night'
        
        return (season, time)

    def mm_freelook_x_express(st, at):
        df = int(st * 60) - mmflcam.xf
        for i in xrange(df):
            mmflcam.xo = mmflcam.xo + (mmflcam.xo1 - mmflcam.xo) * 0.05
        mmflcam.xf += df
        return mmflcam.xo

    def mm_freelook_y_express(st, at):
        df = int(st * 60) - mmflcam.yf
        for i in xrange(df):
            mmflcam.yo += (mmflcam.yo1 - mmflcam.yo) * 0.05
        mmflcam.yf += df
        return mmflcam.yo

    def mm_freelook_z_express(st, at):
        df = int(st * 60) - mmflcam.zf
        for i in xrange(df):
            mmflcam.zo += (mmflcam.zo1 - mmflcam.zo) * 0.05
        mmflcam.zf += df
        return mmflcam.zo

    mmflcam = camera.FreeLookCamera(
        xspan=scale(240),
        yspan=scale(135),
        zspan=scale(75),
        x_express=mm_freelook_x_express,
        y_express=mm_freelook_y_express,
        z_express=mm_freelook_z_express)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
