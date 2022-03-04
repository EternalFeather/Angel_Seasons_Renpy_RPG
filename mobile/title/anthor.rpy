
label anthor:

    $ _window_subtitle = ""
    $ suppress_overlay = True
    play sound "sound/first_game_start.wav"
    scene black with Dissolve(8.0, hard=True)

menu:
    
    " 丛雨（春之妖刀）篇":

        jump third_anthor_label

    " 莉斯特（夏之死神）篇 ":

        jump first_anthor_label

    " 真红（秋之双子）篇":

        jump forth_anthor_label

    " 希菲尔（冬之妖精）篇":

        jump second_anthor_label

    " 决战篇":

        jump final_battle_label


label first_anthor_label:
    if "夏之章" not in persistent.stories:
        bookmark
        "抱歉，请先通关（夏之死神）篇后才能开启回忆模式......"
        
        return

    $ renpy.block_rollback()
    scene black
    with None

    $ camera_reset()
    play music first_game fadein 2.0

    $ flcam.move(-2800, -4500, 1100)
    scene set only anthor_screen first
    with slowdissolve
    $ flcam.move(0, -1100, 0, duration=15.0, warper='ease_cubic')
    pause 13.0 hard

    show expression mmflcam as mmflcam onlayer texture
    $ renpy.transition(slowdissolve, layer='texture')

    show first mm shadow as shadow onlayer texture
    pause 1.5
    show first mm logo white as logo onlayer texture
    pause 1.0
    show screen first_anthor_screen

    $ ui.interact()


screen first_anthor_screen():
    $ continue_slot = renpy.newest_slot("(?!_reload)")
    frame style_prefix "first":
        has vbox at mm_buttons_inter
        textbutton _("{#first}重温夏日"):
            action [Hide('first_anthor_screen', transition=Dissolve), Stop("music", fadeout=4.0), Jump("day01")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.0)
        textbutton _("{#first}梦回故里"):
            action [Show("load"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.1)
        textbutton _("{#first}图鉴"):
            action [Show("encyclopedia"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.2)
        textbutton _("{#first}画廊"):
            action [Show("gallery"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.3)
        textbutton _("{#first}设置"):
            action [Show("preferences"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.4)
        textbutton _("{#first}返回"):
            action [MainMenu(confirm=True), Play('sound', 'sound/click_1.wav')]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.5)

    key "hide_windows" action NullAction()
    key "game_menu" action NullAction()


init:
    image first mm shadow:
        "title/shadow.png"
        imagescale(540)
        subpixel True
        transform_anchor True
        xcenter 0.8
        ycenter 0.5
        alpha 0
        linear 1.5 alpha 1

    image first mm logo white:
        "images/logo/logo_first.png"
        imagescale(1080)
        subpixel True
        transform_anchor True
        xcenter 0.8
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

    style first_frame is default:
        xcenter 0.8
        ypos scale(920)
        yanchor 1.0

    style first_vbox is vbox:
        xcenter 0.5
        ycenter 0.5
        spacing scale(3)

    style first_button is default:
        xsize int(scale(316.5))
        ysize int(scale(48.5))
        hover_background imagescale(1080)("title/button hover.png")
        
    style first_button_text is text:
        xcenter 0.5
        ycenter 0.5
        # font "9i/fonts/FOT-SkipStd-B.otf"
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(36)
        color "#fff"
        insensitive_color "#998"
        outlines [(scale(2.5), "#3f251d", scale(0.0), scale(1.5))]
        hover_outlines [(scale(2.5), "#e3a234", scale(0.0), scale(1.5))]


label second_anthor_label:
    if "冬之章" not in persistent.stories:
        bookmark
        "抱歉，请先通关（冬之妖精）篇后才能开启回忆模式......"

        return

    $ renpy.block_rollback()
    scene black
    with None

    $ camera_reset()
    play music second_game fadein 2.0

    $ flcam.move(4500, -5800, 1100)
    scene set only anthor_screen second
    with slowdissolve
    $ flcam.move(0, -2800, 0, duration=15.0, warper='ease_cubic')
    pause 13.0 hard

    show expression mmflcam as mmflcam onlayer texture
    $ renpy.transition(slowdissolve, layer='texture')

    show second mm shadow as shadow onlayer texture
    pause 1.5
    show second mm logo white as logo onlayer texture
    pause 1.0
    show screen second_anthor_screen

    $ ui.interact()


screen second_anthor_screen():
    $ continue_slot = renpy.newest_slot("(?!_reload)")
    frame style_prefix "second":
        has vbox at mm_buttons_inter
        textbutton _("{#second}重温冬日"):
            action [Hide('second_anthor_screen', transition=Dissolve), Stop("music", fadeout=4.0), Jump("day201")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.0)
        textbutton _("{#second}梦回故里"):
            action [Show("load"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.1)
        textbutton _("{#second}图鉴"):
            action [Show("encyclopedia"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.2)
        textbutton _("{#second}画廊"):
            action [Show("gallery"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.3)
        textbutton _("{#second}设置"):
            action [Show("preferences"), Play("sound", "sound/click_1.wav")]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.4)
        textbutton _("{#second}返回"):
            action [MainMenu(confirm=True), Play('sound', 'sound/click_1.wav')]
            hovered Play('sound', 'sound/button_hover.wav', fadein=0.2, fadeout=0.2)
            at gui_slide_left(.5)

    key "hide_windows" action NullAction()
    key "game_menu" action NullAction()


init:
    image second mm shadow:
        "title/shadow.png"
        imagescale(540)
        subpixel True
        transform_anchor True
        xcenter 0.2
        ycenter 0.5
        alpha 0
        linear 1.5 alpha 1

    image second mm logo white:
        "images/logo/logo_second.png"
        imagescale(1080)
        subpixel True
        transform_anchor True
        xcenter 0.2
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

    style second_frame is default:
        xcenter 0.2
        ypos scale(920)
        yanchor 1.0

    style second_vbox is vbox:
        xcenter 0.5
        ycenter 0.5
        spacing scale(3)

    style second_button is default:
        xsize int(scale(316.5))
        ysize int(scale(48.5))
        hover_background imagescale(1080)("title/button hover.png")
        
    style second_button_text is text:
        xcenter 0.5
        ycenter 0.5
        # font "9i/fonts/FOT-SkipStd-B.otf"
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(36)
        color "#fff"
        insensitive_color "#998"
        outlines [(scale(2.5), "#3f251d", scale(0.0), scale(1.5))]
        hover_outlines [(scale(2.5), "#e3a234", scale(0.0), scale(1.5))]


label third_anthor_label:
    bookmark
    # call movie4 from _call_movie4
    "抱歉，请先通关（春之妖刀）篇后才能开启回忆模式......"

    return


label forth_anthor_label:
    bookmark
    "抱歉，请先通关（秋之双子）篇后才能开启回忆模式......"

    return


label final_battle_label:
    bookmark
    "开启决战必须先通关（春、夏、秋、冬、决战）五个篇章后才能开启回忆模式......"

    return
