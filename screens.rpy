

init python:
    def mbox(hide=0):
        if config.skipping != "fast":
            if hide==0:
                renpy.show_screen(
                    "say", who="", what="", show=True, _transient = True)
                renpy.pause(.5, hard=True)
            elif hide==1:
                renpy.show_screen(
                    "say", who="", what="", show=False, _transient = True)
                renpy.hide_screen("say")
                renpy.pause(.5, hard=True)


transform mboxshow:
    alpha 0 yoffset 32
    easein .3 alpha 1.0 yoffset 0
transform mboxhide:
    on hide:
        easeout .3 yoffset 32 alpha 0



screen say:

    zorder -1

    default side_image = None
    default two_window = False
    default show = None


    if show:
        window:
            id 'window'
            at mboxshow


    elif show == False:
        window:
            id 'window'
            at mboxhide


    if two_window:


        if who:
            window:
                background 'ui/adv_txtbox2.png'
                frame:
                    ypos -88
                    xpos -183
                    xminimum 300
                    xmaximum 300
                    background None

                    text who:
                        xalign 0.5
                        yalign 0.5
                        id 'who'

                frame:
                    background None
                    ypos -20
                    xpos 0
                    xmaximum 745

                    text what id 'what'
    else:

        window:
            background 'ui/adv_txtbox.png'

            frame:
                background None
                ypos -20
                xpos 0
                xmaximum 745

                text what id 'what'

    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


    use quick_menu




screen choice:

    zorder -1
    window at choicein:
        style 'menu_window'

        vbox:
            style 'menu'
            spacing 30

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style 'menu_choice_button'

                        text caption style 'menu_choice'
                else:

                    text caption style 'menu_caption'

transform choicein:
    zoom 1.2 alpha 0
    ease 0.2 zoom 1.0 alpha 1.0
    on hide:
        ease 0.2 zoom 1.2 alpha 0
        

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_window.xalign = 0.5
    style.menu_window.yalign = 0.5
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.background = Frame("ui/sel_bunner1.png", 128, 1)
    style.menu_choice_button.hover_background = Frame("ui/sel_bunner2.png", 128, 1)
    style.menu_choice_button.top_margin = 10
    style.menu_choice_button.top_padding = 10
    style.menu_choice_button.bottom_margin = 20
    style.menu_choice_button.bottom_padding = 10
    style.menu_choice_button.activate_sound = "se_sys/menu1.wav"
    style.menu_choice_button.xminimum = 552
    style.menu_choice_button.yminimum = 45

    style.menu_choice.text_align = 0.5
    style.menu_choice.color = "#4f4f4f"
    style.menu_choice.drop_shadow = None
    style.menu_choice.hover_color = "#000000"
    style.menu_choice.selected_color = "#000000"



screen input:

    zorder -1
    window:
        has vbox

        text prompt
        input id 'input'

    use quick_menu



screen nvl:
    default in_prologue = False

    if in_prologue:
        $ nvl_window = 'prologue_nvl_window'
    else:
        $ nvl_window = 'nvl_window'

    zorder -1
    if in_prologue:
        key 'game_menu' action Hide('nonexistent_screen')
    window:
        style nvl_window

        has vbox:
            style 'nvl_vbox'


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id 'menu'

                for caption, action, chosen in items:

                    if action:

                        button:
                            style 'nvl_menu_choice_button'
                            action action

                            text caption style 'nvl_menu_choice'
                    else:


                        text caption style 'nvl_dialogue'

    add SideImage() xalign 0.0 yalign 1.0

    if not in_prologue:
        use quick_menu

style prologue_nvl_window take nvl_window background None


screen main_menu tag menu:

    if persistent.gamecomplete == True and persistent.fanwai == False:
        
        imagebutton xalign 0.195 yalign 0.92:
            at buttonexpand1
            idle 'ui/title_start.png'
            hover 'ui/title2_start.png'
            selected_idle 'ui/title2_start.png'
            action [Hide('main_menu', transition=Dissolve), Start(), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.340 yalign 0.78:
            at buttonexpand5
            idle 'ui/title_continue0.png'
            hover 'ui/title_continue1.png'
            action [Hide('main_menu', transition=Dissolve), Start('anthor'), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.384 yalign 0.922:
            at buttonexpand2
            idle 'ui/title_continue.png'
            hover 'ui/title2_continue.png'
            action [Show('load'), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.590 yalign 0.928:
            at buttonexpand3
            idle 'ui/title_option.png'
            hover 'ui/title2_option.png'
            action [Show('preferences'), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.620 yalign 0.78:
            at buttonexpand6
            idle 'ui/title_album.png'
            hover 'ui/title_album1.png'
            action [Show('gallery'), Play("music", "bgm/700.ogg", if_changed = True)] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.792 yalign 0.925:
            at buttonexpand4
            idle 'ui/title_end.png'
            hover 'ui/title2_end.png'
            action [Quit(confirm=True), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)

        add 'ui/fanwai_logo.png' at mainlogoslide2
        add 'particles'

    elif persistent.gamecomplete == True and persistent.fanwai == True:

        imagebutton xalign 0.195 yalign 0.92:
            at buttonexpand1
            idle 'ui/title_start.png'
            hover 'ui/title2_start.png'
            selected_idle 'ui/title2_start.png'
            action [Hide('main_menu', transition=Dissolve), Start(), Play('sound', 'voice/yoshino_after.ogg')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.340 yalign 0.78:
            at buttonexpand5
            idle 'ui/title_continue0.png'
            hover 'ui/title_continue1.png'
            action [Hide('main_menu', transition=Dissolve), Start('anthor'), Play('sound', 'voice/yoshino_jump.ogg')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.384 yalign 0.922:
            at buttonexpand2
            idle 'ui/title_continue.png'
            hover 'ui/title2_continue.png'
            action [Show('load'), Play('sound', 'se_sys/hover.wav')] hovered Play('sound', 'voice/yoshino_load.ogg', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.590 yalign 0.928:
            at buttonexpand3
            idle 'ui/title_option.png'
            hover 'ui/title2_option.png'
            action [Show('preferences'), Play('sound', 'voice/yoshino_system.ogg')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.620 yalign 0.78:
            at buttonexpand6
            idle 'ui/title_album.png'
            hover 'ui/title_album1.png'
            action [Show('gallery'), Play("music", "bgm/700.ogg", if_changed = True)] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.792 yalign 0.925:
            at buttonexpand4
            idle 'ui/title_end.png'
            hover 'ui/title2_end.png'
            action [Quit(confirm=True), Play('sound', 'voice/yoshino_end.ogg')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)

        add 'ui/title_logo13.png' at mainlogoslide2  
        add 'particles'

    elif persistent.gamecomplete == False and persistent.fanwai == False:

        imagebutton xalign 0.195 yalign 0.92:
            at buttonexpand1
            idle 'ui/title_start.png'
            hover 'ui/title2_start.png'
            selected_idle 'ui/title2_start.png'
            action [Hide('main_menu', transition=Dissolve), Start(), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.384 yalign 0.922:
            at buttonexpand2
            idle 'ui/title_continue.png'
            hover 'ui/title2_continue.png'
            action [Show('load'), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.590 yalign 0.928:
            at buttonexpand3
            idle 'ui/title_option.png'
            hover 'ui/title2_option.png'
            action [Show('preferences'), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.620 yalign 0.78:
            at buttonexpand6
            idle 'ui/title_album.png'
            hover 'ui/title_album1.png'
            action [Show('gallery'), Play("music", "bgm/700.ogg", if_changed = True)] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
        imagebutton xalign 0.792 yalign 0.925:
            at buttonexpand4
            idle 'ui/title_end.png'
            hover 'ui/title2_end.png'
            action [Quit(confirm=True), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)

        add 'ui/logo.png' at mainlogoslide
        add 'ui/eternal.png' at eternal 
        add 'particles'

image bg s01 = "images/staff_bg1.bmp"
image bg s02 = "images/staff_bg2.bmp"
image bg s03 = "images/staff_bg3.bmp"
image bg s04 = "images/staff_bg4.bmp"
image bg s05 = "images/staff_bg5.bmp"
image bg s06 = "images/main1.png"
image bg s07 = "images/staff_01.bmp"

transform eternal:
    alpha 0.0 xalign 0.19 yalign 0.04
    easein 3.5 alpha 1.0 yalign 0.08

transform mainlogoslide:
    alpha 0.0 xalign 0.08 yalign 0.1
    easein 3.5 alpha 1.0 yalign 0.06

transform mainlogoslide2:
    alpha 0.0 xalign 0.08 yalign 0.1
    pause 3.0
    easein 3.5 alpha 1.0 yalign 0.06

transform buttonexpand2:
    alpha 0.0 xalign 0.384 yalign 0.922
    easein 3.0 alpha 1.0 yalign 0.902
    zoom 1.0
    on idle:
        ease 0.2 zoom 1.0
    on hover:
        ease 0.2 zoom 1.1

transform buttonexpand1:
    alpha 0.0 xalign 0.195 yalign 0.92
    easein 3.0 alpha 1.0 yalign 0.9
    zoom 1.0
    on idle:
        ease 0.2 zoom 1.0
    on hover:
        ease 0.2 zoom 1.1

transform buttonexpand3:
    alpha 0.0 xalign 0.590 yalign 0.928
    easein 3.0 alpha 1.0 yalign 0.908
    zoom 1.0
    on idle:
        ease 0.2 zoom 1.0
    on hover:
        ease 0.2 zoom 1.1

transform buttonexpand4:
    alpha 0.0 xalign 0.792 yalign 0.925
    easein 3.0 alpha 1.0 yalign 0.905
    zoom 1.0
    on idle:
        ease 0.2 zoom 1.0
    on hover:
        ease 0.2 zoom 1.1

transform buttonexpand5:
    alpha 0.0 xalign 0.340 yalign 0.78
    easein 3.0 alpha 1.0 yalign 0.76
    zoom 1.0
    on idle:
        ease 0.2 zoom 1.0
    on hover:
        ease 0.2 zoom 1.1

transform buttonexpand6:
    alpha 0.0 xalign 0.691 yalign 0.78
    easein 3.0 alpha 1.0 yalign 0.76
    zoom 1.0
    on idle:
        ease 0.2 zoom 1.0
    on hover:
        ease 0.2 zoom 1.1


label main_menu:

    if persistent.gamecomplete == True and persistent.fanwai == False:
        
        $ config.main_menu_music = "bgm/end.ogg"

    elif persistent.gamecomplete == False and persistent.fanwai == False:

        $ config.main_menu_music = "bgm/begin.ogg"

    elif persistent.gamecomplete == True and persistent.fanwai == True:

        $ config.main_menu_music = "bgm/op.ogg"


    if persistent.clear_game == False and persistent.gallery_unlocked == False and persistent.gamecomplete == False and persistent.fanwai == False:

        scene bg s01:
            crop(300,543,636,405)
            size(1280,720)

            linear 50.0 crop(0,300,1000,720)

    elif persistent.clear_game == False and persistent.gallery_unlocked == True and persistent.gamecomplete == False and persistent.fanwai == False:
        
        scene bg s02:
            crop(300,543,636,405)
            size(1280,720)

            linear 50.0 crop(0,300,1000,720)
       
    elif persistent.clear_game == True and persistent.gallery_unlocked == False and persistent.gamecomplete == False and persistent.fanwai == False:
        
        scene bg s03:
            crop(300,543,636,405)
            size(1280,720)

            linear 50.0 crop(0,300,1000,720)

    elif persistent.clear_game == True and persistent.gallery_unlocked == True and persistent.gamecomplete == False and persistent.fanwai == False:

        scene bg s04:
            crop(300,543,636,405)
            size(1280,720)

            linear 50.0 crop(0,300,1000,720)

    elif persistent.gamecomplete == True and persistent.fanwai == False:
        
        scene bg s05:
            crop(360,203,600,337)
            size(1280,720)

            linear 30.0 crop(0,0,960,540)
        
        #scene bg s05:
            #crop(200,100,1000,600)
            #size(1280,720)

            #linear 10.0 crop(0,0,1280,720)

    else:

        scene black
        pause 5.0
        scene bg s06 with slowerdissolve:
            crop(200,100,1000,600)
            size(1280,720)

            linear 10.0 crop(0,0,1280,720)



    pause 6.0

    show screen main_menu

    if persistent.fanwai == True:

        pause 1.0
        play sound "voice/yoshino_after.ogg"

    $ ui.interact()

# image Sociopath_timer = DelayRun(60*120, Function(custom_grant_achievement, "Sociopath"))

transform smaller:
    size (1280, 720)
    crop (0, 0, 800, 440)

transform bigger:

    size (1280, 720)
    crop (0, 0, 1600, 980)

transform bigger02:

    size (1280, 720)
    crop (0, 100, 1340, 754)

transform bigger03:

    crop (0, 50, 1600, 950)
    size (1280, 720)

transform bigger04:

    crop (0, 150, 1600, 750)
    size (1280, 720)

init python:
    g = Gallery()

    g.button("pic1")
    g.unlock_image("bg linggan")
    g.transform(smaller)
    g.unlock_image("bg linggan")
    g.transform(smaller)
    g.unlock_image("bg surprise01")
    g.transform(smaller)
    g.unlock_image("bg anger01")
    g.transform(smaller)
    g.unlock_image("bg normal01")
    g.transform(smaller)
    g.unlock_image("bg smile01")
    g.transform(smaller)
    g.unlock_image("bg happy01")
    g.transform(smaller)
    g.unlock_image("bg shame01")
    g.transform(smaller)
    g.unlock_image("bg shame02")
    g.transform(smaller)

    g.button("pic2")
    # g.image("bg ev_01")
    g.unlock_image("bg my_haibian")
    g.transform(smaller)
    g.unlock_image("bg my_huanghun2")
    g.transform(smaller)

    g.button("pic3")
    g.unlock_image("bg wunv_anger01")
    g.transform(bigger)
    g.unlock_image("bg wunv_happy01")
    g.transform(bigger)
    g.unlock_image("bg wunv_normal01")
    g.transform(bigger)
    g.unlock_image("bg wunv_shame01")
    g.transform(bigger)
    g.unlock_image("bg wunv_surprise01")
    g.transform(bigger)
    g.unlock_image("bg wunv_wunai01")
    g.transform(bigger)

    g.button("pic4")
    g.unlock_image("bg xz_shenshe01")
    g.transform(bigger)
    # g.image("bg xz_shenshe01")
    # g.image("bg cg_01_gallery_b")
    # g.image(im.Scale("images/eventcg/landing/bg.jpg", 1280, 720))

    g.button("pic5")
    g.unlock_image("bg huiyi_xinwei")
    g.transform(bigger)
    g.unlock_image("bg huiyi_sad")
    g.transform(bigger)

    g.button("pic6")
    g.unlock_image("bg xiaoshi_cry01")
    g.transform(smaller)
    g.unlock_image("bg xiaoshi_sad01")
    g.transform(smaller)
    g.unlock_image("bg xiaoshi_smile01")
    g.transform(smaller)

    g.button("pic7")
    g.unlock_image("bg KOMOMO_e06a")
    g.transform(bigger)
    g.unlock_image("bg KOMOMO_e06b")
    g.transform(bigger)
    g.unlock_image("bg KOMOMO_e06c")
    g.transform(bigger)
    g.unlock_image("bg KOMOMO_e06d")
    g.transform(bigger)
    g.unlock_image("bg KOMOMO_e06e")
    g.transform(bigger)

    g.button("pic8")
    g.unlock_image("bg xzh01")
    g.transform(bigger)
    g.unlock_image("bg xzh03")
    g.transform(bigger)
    g.unlock_image("bg xzh04")
    g.transform(bigger)
    g.unlock_image("bg xzh02")
    g.transform(bigger)

    g.button("pic9")
    g.unlock_image("bg xzh05")
    g.transform(bigger)
    g.unlock_image("bg xzh06")
    g.transform(bigger)
    g.unlock_image("bg xzh07")
    g.transform(bigger)
    g.unlock_image("bg xzh08")
    g.transform(bigger)
    g.unlock_image("bg xzh09")
    g.transform(bigger)
    g.unlock_image("bg xzh11")
    g.transform(bigger)
    g.unlock_image("bg xzh10")
    g.transform(bigger)
    g.unlock_image("bg xzh12")
    g.transform(bigger)
    g.unlock_image("bg xzh13")
    g.transform(bigger)
    g.unlock_image("bg xzh14")
    g.transform(bigger)
    g.unlock_image("bg xzh16")
    g.transform(bigger)
    g.unlock_image("bg xzh15")
    g.transform(bigger)

    g.button("pic10")
    g.unlock_image("bg xzh17")
    g.transform(bigger)
    g.unlock_image("bg xzh18")
    g.transform(bigger)
    g.unlock_image("bg xzh19")
    g.transform(bigger)
    g.unlock_image("bg xzh20")
    g.transform(bigger)
    g.unlock_image("bg xzh21")
    g.transform(bigger)
    g.unlock_image("bg xzh22")
    g.transform(bigger)
    g.unlock_image("bg xzh23")
    g.transform(bigger)
    g.unlock_image("bg xzh24")
    g.transform(bigger)
    g.unlock_image("bg xzh26")
    g.transform(bigger)
    g.unlock_image("bg xzh27")
    g.transform(bigger)
    g.unlock_image("bg xzh25")
    g.transform(bigger)
    g.unlock_image("bg xzh28")
    g.transform(bigger)

    g.button("pic11")
    g.unlock_image("bg MARE_e02a")
    g.transform(bigger)
    g.unlock_image("bg MARE_e02b")
    g.transform(bigger)
    g.unlock_image("bg MARE_e02c")
    g.transform(bigger)
    g.unlock_image("bg MARE_e02d")
    g.transform(bigger)
    

    g.button("pic12")
    g.unlock_image("bg MARE_e09a")
    g.transform(bigger)
    g.unlock_image("bg MARE_e09b")
    g.transform(bigger)
    g.unlock_image("bg MARE_e09c")
    g.transform(bigger)
    g.unlock_image("bg MARE_e09d")
    g.transform(bigger)
    g.unlock_image("bg MARE_e09e")
    g.transform(bigger)
    g.unlock_image("bg MARE_e09i")
    g.transform(bigger)
    g.unlock_image("bg MARE_e09j")
    g.transform(bigger)
    g.unlock_image("bg MARE_e09l")
    g.transform(bigger)
    g.unlock_image("bg MARE_e09m")
    g.transform(bigger)

    g.button("pic13")
    g.unlock_image("bg lisite")
    g.transform(bigger02)
    g.unlock_image("bg lisite02")
    g.transform(bigger02)

    g.button("pic14")
    g.unlock_image("bg xiangzi_a")
    g.transform(bigger)
    g.unlock_image("bg xiangzi_s") 
    g.transform(bigger)

    g.button("pic15")
    g.unlock_image("bg MARE_e03f")
    g.transform(bigger)
    g.unlock_image("bg MARE_e03h")
    g.transform(bigger)
    g.unlock_image("bg MARE_e03n")
    g.transform(bigger)

    g.button("pic16")
    g.unlock_image("bg lsth01")
    g.transform(bigger03)
    g.unlock_image("bg lsth02")
    g.transform(bigger03)

    g.button("pic17")
    g.unlock_image("bg lsth03")
    g.transform(bigger03)
    g.unlock_image("bg lsth04")
    g.transform(bigger03)
    g.unlock_image("bg lsth05")
    g.transform(bigger03)
    g.unlock_image("bg lsth06")
    g.transform(bigger03)
    g.unlock_image("bg lsth07")
    g.transform(bigger03)
    g.unlock_image("bg lsth08")
    g.transform(bigger03)
    g.unlock_image("bg lsth09")
    g.transform(bigger03)
    g.unlock_image("bg lsth10")
    g.transform(bigger03)
    g.unlock_image("bg lsth11")
    g.transform(bigger03)
    g.unlock_image("bg lsth12")
    g.transform(bigger03)
    g.unlock_image("bg lsth13")
    g.transform(bigger03)

    g.button("pic18")
    g.unlock_image("bg lsth14")
    g.transform(bigger03)
    g.unlock_image("bg lsth15")
    g.transform(bigger03)
    g.unlock_image("bg lsth16")
    g.transform(bigger03)
    g.unlock_image("bg lsth17")
    g.transform(bigger03)
    g.unlock_image("bg lsth18")
    g.transform(bigger03)
    g.unlock_image("bg lsth19")
    g.transform(bigger03)
    g.unlock_image("bg lsth20")
    g.transform(bigger03)
    g.unlock_image("bg lsth21")
    g.transform(bigger03)


    g.button("pic19")
    g.unlock_image("bg MARE_e05g")
    g.transform(bigger03)
    g.unlock_image("bg MARE_e05h")
    g.transform(bigger03)
    g.unlock_image("bg MARE_e05i")
    g.transform(bigger03)

    g.button("pic20")
    g.unlock_image("bg MARE_e07a")
    g.transform(bigger03)
    g.unlock_image("bg MARE_e07b")
    g.transform(bigger03)

    g.button("pic21")
    g.unlock_image("bg MARE_e11a")
    g.transform(bigger03)
    g.unlock_image("bg MARE_e11b")
    g.transform(bigger03)
    g.unlock_image("bg MARE_e11c")
    g.transform(bigger03)
    g.unlock_image("bg MARE_e11d")
    g.transform(bigger03)

    g.button("pic22")
    g.unlock_image("bg MARE_e06a")
    g.transform(bigger04)

    # g.button("pic23")
    # g.unlock("bg Ev_15")
    # g.image("Ev_15_sub")

    # g.button("pic24")
    # g.unlock_image("bg Ev_18") 


    g.transition = slowdissolve


screen gallery:

    modal True
    key "game_menu" action [Hide("gallery"), Play("sound", "se_sys/cancel.wav")]
    window id "gallery" at basicfade:
        xpadding 0
        ypadding 0

        add "images/system/gallery/gallery_bg.png"

        imagebutton auto "images/system/gallery/book_%s.png" action [Show("gallery_pics"), Play("sound", "se_sys/openbook.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.45 yalign 1.0
        imagebutton auto "images/system/gallery/audio_%s.png" action Show("music_room_one") hovered Play("sound", "se_sys/select.ogg") xalign 0.0 yalign 0.35

        imagebutton auto "images/system/gallery/title_screen_%s.png" xalign 0.97 yalign 0.95 action Hide("gallery") hovered Play("sound", "se_sys/select.ogg")


screen gallery_pics tag gallerysecond:
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")]

    add "images/system/gallery/vignette.png" at basicfade
    window id "gallery_pics" at galleryfade:
        xpadding 0
        ypadding 0
        background "images/system/gallery/book/bg_1.png"



        vbox xalign 0.27 yalign 0.47:
            spacing 20
            add g.make_button("pic1"  , "images/resized/1-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
            add g.make_button("pic2"  , "images/resized/1-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
            add g.make_button("pic3"  , "images/resized/1-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
            add g.make_button("pic4"  , "images/resized/1-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")

        vbox xalign 0.73 yalign 0.47:
            spacing 20
            add g.make_button("pic5"  , "images/resized/2-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
            add g.make_button("pic6"  , "images/resized/2-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
            add g.make_button("pic7"  , "images/resized/2-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
            add g.make_button("pic8"  , "images/resized/2-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")


        imagebutton auto "images/system/gallery/rightarrow_%s.png" action [Show("gallery_pics2"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.83 yalign 0.5

        imagebutton auto "images/system/gallery/gallery_%s.png" action None hovered Play("sound", "se_sys/select.ogg") xalign 0.04 yalign 0.15
        imagebutton auto "images/system/gallery/movie_%s.png" action [Show("gallery_movie"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.08 yalign 0.4
        imagebutton auto "images/system/gallery/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.98 yalign 0.8


screen gallery_pics1 tag gallerysecond:
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")]

    add "images/system/gallery/vignette.png" at vignettehide
    window id "gallery_pics1" at galleryhide:
        xpadding 0
        ypadding 0
        background None

        add "images/system/gallery/book/bg_1.png" at pageflip

        frame at galleryfade2:

            vbox xalign 0.27 yalign 0.47:
                spacing 20
                add g.make_button("pic1"  , "images/resized/1-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic2"  , "images/resized/1-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic3"  , "images/resized/1-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic4"  , "images/resized/1-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")

            vbox xalign 0.73 yalign 0.47:
                spacing 20
                add g.make_button("pic5"  , "images/resized/2-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic6"  , "images/resized/2-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic7"  , "images/resized/2-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic8"  , "images/resized/2-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")


            imagebutton auto "images/system/gallery/rightarrow_%s.png" action [Show("gallery_pics2"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.83 yalign 0.5

        imagebutton auto "images/system/gallery/gallery_%s.png" action None hovered Play("sound", "se_sys/select.ogg") xalign 0.04 yalign 0.15
        imagebutton auto "images/system/gallery/movie_%s.png" action [Show("gallery_movie"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.08 yalign 0.4
        imagebutton auto "images/system/gallery/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.98 yalign 0.8


screen gallery_pics2 tag gallerysecond:
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")]

    add "images/system/gallery/vignette.png" at vignettehide
    window id "gallery_pics2" at galleryhide:
        xpadding 0
        ypadding 0
        background None

        add "images/system/gallery/book/bg_1.png" at pageflip2

        frame at galleryfade2:

            vbox xalign 0.27 yalign 0.47:
                spacing 20
                add g.make_button("pic9"  , "images/resized/3-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic10" , "images/resized/3-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic11" , "images/resized/3-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic12" , "images/resized/3-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")

            vbox xalign 0.73 yalign 0.47:
                spacing 20
                add g.make_button("pic13" , "images/resized/4-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic14" , "images/resized/4-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic15" , "images/resized/4-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic16" , "images/resized/4-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")


            imagebutton auto "images/system/gallery/leftarrow_%s.png" action [Show("gallery_pics1"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.17 yalign 0.5
            imagebutton auto "images/system/gallery/rightarrow_%s.png" action [Show("gallery_pics3"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.83 yalign 0.5

        imagebutton auto "images/system/gallery/gallery_%s.png" action None hovered Play("sound", "se_sys/select.ogg") xalign 0.04 yalign 0.15
        imagebutton auto "images/system/gallery/movie_%s.png" action [Show("gallery_movie"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.08 yalign 0.4
        imagebutton auto "images/system/gallery/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.98 yalign 0.8


screen gallery_pics2alt tag gallerysecond:
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")]

    add "images/system/gallery/vignette.png" at vignettehide
    window id "gallery_pics2alt" at galleryhide:
        xpadding 0
        ypadding 0
        background None

        add "images/system/gallery/book/bg_1.png" at pageflip

        frame at galleryfade2:

            vbox xalign 0.27 yalign 0.47:
                spacing 20
                add g.make_button("pic9"  , "images/resized/3-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic10" , "images/resized/3-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic11" , "images/resized/3-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic12" , "images/resized/3-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")

            vbox xalign 0.73 yalign 0.47:
                spacing 20
                add g.make_button("pic13" , "images/resized/4-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic14" , "images/resized/4-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic15" , "images/resized/4-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic16" , "images/resized/4-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")


            imagebutton auto "images/system/gallery/leftarrow_%s.png" action [Show("gallery_pics1"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.17 yalign 0.5
            imagebutton auto "images/system/gallery/rightarrow_%s.png" action [Show("gallery_pics3"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.83 yalign 0.5

        imagebutton auto "images/system/gallery/gallery_%s.png" action None hovered Play("sound", "se_sys/select.ogg") xalign 0.04 yalign 0.15
        imagebutton auto "images/system/gallery/movie_%s.png" action [Show("gallery_movie"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.08 yalign 0.4
        imagebutton auto "images/system/gallery/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.98 yalign 0.8


screen gallery_pics3 tag gallerysecond:
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")]

    add "images/system/gallery/vignette.png" at vignettehide
    window id "gallery_pics3" at galleryhide:
        xpadding 0
        ypadding 0
        background None

        add "images/system/gallery/book/bg_1.png" at pageflip2

        frame at galleryfade2:

            vbox xalign 0.27 yalign 0.47:
                spacing 20
                add g.make_button("pic17" , "images/resized/5-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic18" , "images/resized/5-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic19" , "images/resized/5-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic20" , "images/resized/5-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")

            vbox xalign 0.73 yalign 0.47:
                spacing 20
                add g.make_button("pic21" , "images/resized/6-1.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                add g.make_button("pic22" , "images/resized/6-2.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                # add g.make_button("pic23" , "images/resized/6-3.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")
                # add g.make_button("pic24" , "images/resized/6-4.png", xalign=0.5 , yalign=0.5 , background=None , locked="images/resized/locked.png")


            imagebutton auto "images/system/gallery/leftarrow_%s.png" action [Show("gallery_pics2alt"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.17 yalign 0.5

        imagebutton auto "images/system/gallery/gallery_%s.png" action None hovered Play("sound", "se_sys/select.ogg") xalign 0.04 yalign 0.15
        imagebutton auto "images/system/gallery/movie_%s.png" action [Show("gallery_movie"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.08 yalign 0.4
        imagebutton auto "images/system/gallery/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.98 yalign 0.8


screen gallery_movie tag gallerysecond:
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")]

    add "images/system/gallery/vignette.png" at vignettehide
    window id "gallery_movie" at galleryhide:
        xpadding 0
        ypadding 0
        background None

        add "images/system/gallery/book/bg_1.png" at pageflip

        frame at galleryfade2:

            vbox xalign 0.27 yalign 0.47:
                spacing 20
                imagebutton auto "movies/thumbs/credit_roll_%s.png" action Replay("movie4")
                imagebutton auto "movies/thumbs/fault_prologue_%s.png" action Replay("movie5")

            vbox xalign 0.73 yalign 0.47:
                spacing 20
                imagebutton auto "movies/thumbs/aid_in_r_t_%s.png" action Replay("movie7")
                imagebutton auto "movies/thumbs/fault_ms1_op_%s.png" action Replay("movie2")

            imagebutton auto "images/system/gallery/rightarrow_%s.png" action [Show("gallery_movie2"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.83 yalign 0.5

        imagebutton auto "images/system/gallery/gallery_%s.png" action [Show("gallery_pics1"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.04 yalign 0.15
        imagebutton auto "images/system/gallery/movie_%s.png" action None hovered Play("sound", "se_sys/select.ogg") xalign 0.08 yalign 0.4
        imagebutton auto "images/system/gallery/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.98 yalign 0.8


screen gallery_movie2 tag gallerysecond:
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")]

    add "images/system/gallery/vignette.png" at vignettehide
    window id "gallery_movie2" at galleryhide:
        xpadding 0
        ypadding 0
        background None

        add "images/system/gallery/book/bg_1.png" at pageflip2

        frame at galleryfade2:

            vbox xalign 0.27 yalign 0.47:
                spacing 20
                imagebutton auto "movies/thumbs/1_%s.png" action Replay("movie7_1")
                imagebutton auto "movies/thumbs/2_%s.png" action Replay("movie7_2")

            vbox xalign 0.73 yalign 0.47:
                spacing 20
                imagebutton auto "movies/thumbs/3_%s.png" action Replay("movie7_3")
                imagebutton auto "movies/thumbs/4_%s.png" action Replay("movie7_4")

            imagebutton auto "images/system/gallery/leftarrow_%s.png" action [Show("gallery_movie"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.17 yalign 0.5

        imagebutton auto "images/system/gallery/gallery_%s.png" action [Show("gallery_pics1"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.04 yalign 0.15
        imagebutton auto "images/system/gallery/movie_%s.png" action None hovered Play("sound", "se_sys/select.ogg") xalign 0.08 yalign 0.4
        imagebutton auto "images/system/gallery/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/closebook.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.98 yalign 0.8


# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init python:


    mr = MusicRoom(fadeout=1.0, loop=True)


    # mr.add("audio/music/themes/zankyou.ogg", always_unlocked=True)
    mr.add("bgm/begin.ogg", always_unlocked=True)
    mr.add("bgm/end.ogg", always_unlocked=True)
    mr.add("bgm/01.ogg", always_unlocked=True)
    mr.add("bgm/02.ogg", always_unlocked=True)
    mr.add("bgm/03.ogg", always_unlocked=True)
    mr.add("bgm/04.ogg", always_unlocked=True)
    mr.add("bgm/05.ogg", always_unlocked=True)
    mr.add("bgm/06.ogg", always_unlocked=True)
    mr.add("bgm/07.ogg", always_unlocked=True)
    mr.add("bgm/08.ogg", always_unlocked=True)
    mr.add("bgm/09.ogg", always_unlocked=True)
    mr.add("bgm/10.ogg", always_unlocked=True)
    mr.add("bgm/11.ogg", always_unlocked=True)
    mr.add("bgm/12.ogg", always_unlocked=True)
    mr.add("bgm/13.ogg", always_unlocked=True)
    mr.add("bgm/14.ogg", always_unlocked=True)
    mr.add("bgm/15.ogg", always_unlocked=True)
    mr.add("bgm/16.ogg", always_unlocked=True)
    mr.add("bgm/17.ogg", always_unlocked=True)
    mr.add("bgm/18.ogg", always_unlocked=True)
    mr.add("bgm/19.ogg", always_unlocked=True)
    mr.add("bgm/20.ogg", always_unlocked=True)
    mr.add("bgm/21.ogg", always_unlocked=True)
    mr.add("bgm/22.ogg", always_unlocked=True)
    mr.add("bgm/23.ogg", always_unlocked=True)
    mr.add("bgm/24.ogg", always_unlocked=True)
    mr.add("bgm/25.ogg", always_unlocked=True)
    mr.add("bgm/26.ogg", always_unlocked=True)
    mr.add("bgm/27.ogg", always_unlocked=True)
    mr.add("bgm/28.ogg", always_unlocked=True)
    mr.add("bgm/29.ogg", always_unlocked=True)
    mr.add("bgm/30.ogg", always_unlocked=True)
    mr.add("bgm/31.ogg", always_unlocked=True)
    mr.add("bgm/32.ogg", always_unlocked=True)
    mr.add("bgm/33.ogg", always_unlocked=True)
    mr.add("bgm/34.ogg", always_unlocked=True)
    mr.add("bgm/35.ogg", always_unlocked=True)
    mr.add("bgm/36.ogg", always_unlocked=True)
    mr.add("bgm/38.ogg", always_unlocked=True)
    mr.add("bgm/42.ogg", always_unlocked=True)
    mr.add("bgm/34.ogg", always_unlocked=True)
    mr.add("bgm/600.ogg", always_unlocked=True)
    mr.add("bgm/601.ogg", always_unlocked=True)
    

# screen music_room:
    

screen music_room_one tag gallerysecond:

    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("music", "bgm/700.ogg", if_changed = True)]
    window id "musicroom_one" at galleryfade:
        xpadding 0
        ypadding 0
        background "images/system/gallery/music_bg.png"

        vbox xalign 0.2 yalign 0.55:
            spacing 8
            textbutton "Prelude~Memoria~" action mr.Play("bgm/begin.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Permanent snow dancing, poetry" action mr.Play("bgm/end.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Slope" action mr.Play("bgm/01.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Indian summer" action mr.Play("bgm/03.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Leakage on the leaves" action mr.Play("bgm/07.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Autumn rainy season" action mr.Play("bgm/20.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Beyond the sky" action mr.Play("bgm/25.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Swear to the starry sky" action mr.Play("bgm/22.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"


        vbox xalign 0.7 yalign 0.55:
            spacing 8
            textbutton "Sunday" action mr.Play("bgm/09.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Memory of the sky" action mr.Play("bgm/31.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Our future" action mr.Play("bgm/32.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Innocent love" action mr.Play("bgm/601.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Small heart" action mr.Play("bgm/21.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Matsurowanu girl" action mr.Play("bgm/13.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "YUME" action mr.Play("bgm/02.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "In the city" action mr.Play("bgm/30.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"


        imagebutton auto "images/system/gallery/music/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/cancel.wav")] hovered Play("sound", "se_sys/select.ogg") xalign 0.84 yalign 0.1
        imagebutton auto "images/system/gallery/rightarrow_%s.png" action [Show("music_room_two"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.75 yalign 0.5

        imagebutton auto "images/system/gallery/music/left_%s.png" action mr.Stop() hovered Play("sound", "se_sys/select.ogg") xalign 0.82 yalign 0.4
        imagebutton auto "images/system/gallery/music/right_%s.png" action mr.Next() hovered Play("sound", "se_sys/select.ogg") xalign 0.85 yalign 0.54

screen music_room_two tag gallerysecond:
    
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("music", "bgm/700.ogg", if_changed = True)]
    window id "musicroom_two" at galleryfade:
        xpadding 0
        ypadding 0
        background "images/system/gallery/music_bg.png"

        vbox xalign 0.2 yalign 0.55:
            spacing 8
            textbutton "The firefly" action mr.Play("bgm/06.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "On the fingertip" action mr.Play("bgm/600.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "~Gathering the stars of love~" action mr.Play("bgm/34.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "-Wish upon a shooting star-" action mr.Play("bgm/36.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Midnight Observatory" action mr.Play("bgm/42.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "The courage to release the girl" action mr.Play("bgm/15.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Be quiet campus" action mr.Play("bgm/19.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Happy Happy SchoolLife" action mr.Play("bgm/10.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
     

        vbox xalign 0.7 yalign 0.55:
            spacing 8
            textbutton "Amamiya in the garden of stars" action mr.Play("bgm/26.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Eternal recurrence" action mr.Play("bgm/29.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Up tempo" action mr.Play("bgm/18.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "QianBoism!" action mr.Play("bgm/08.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Charmed by a smile" action mr.Play("bgm/23.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Amamiya in Star Garden" action mr.Play("bgm/28.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Unidentified Flying Object" action mr.Play("bgm/16.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Natural girl" action mr.Play("bgm/05.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"


        imagebutton auto "images/system/gallery/music/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/cancel.wav")] hovered Play("sound", "se_sys/select.ogg") xalign 0.84 yalign 0.1
        imagebutton auto "images/system/gallery/leftarrow_%s.png" action [Show("music_room_one"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.08 yalign 0.5
        imagebutton auto "images/system/gallery/rightarrow_%s.png" action [Show("music_room_three"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.75 yalign 0.5
        imagebutton auto "images/system/gallery/music/left_%s.png" action mr.Stop() hovered Play("sound", "se_sys/select.ogg") xalign 0.82 yalign 0.4
        imagebutton auto "images/system/gallery/music/right_%s.png" action mr.Next() hovered Play("sound", "se_sys/select.ogg") xalign 0.85 yalign 0.54

screen music_room_three tag gallerysecond:
    
    modal True
    key "game_menu" action [Hide("gallerysecond"), Play("music", "bgm/700.ogg", if_changed = True)]
    window id "musicroom_three" at galleryfade:
        xpadding 0
        ypadding 0
        background "images/system/gallery/music_bg.png"

        vbox xalign 0.2 yalign 0.55:
            spacing 8
            textbutton "Mysterious Dream" action mr.Play("bgm/12.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Born in the same planet" action mr.Play("bgm/33.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Tears of love" action mr.Play("bgm/14.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Dark of sorrow" action mr.Play("bgm/24.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Moon on the water" action mr.Play("bgm/04.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Whisper…" action mr.Play("bgm/17.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"
            textbutton "Stand on the identity of midsummer!" action mr.Play("bgm/27.ogg") hovered Play("sound", "se_sys/select.ogg") style "music_button"

        imagebutton auto "images/system/gallery/music/back_%s.png" action [Hide("gallerysecond"), Play("sound", "se_sys/cancel.wav")] hovered Play("sound", "se_sys/select.ogg") xalign 0.84 yalign 0.1
        imagebutton auto "images/system/gallery/leftarrow_%s.png" action [Show("music_room_two"), Play("sound", "se_sys/68224__xtyl33__paper-double.ogg")] xalign 0.08 yalign 0.5
        
        imagebutton auto "images/system/gallery/music/left_%s.png" action mr.Stop() hovered Play("sound", "se_sys/select.ogg") xalign 0.82 yalign 0.4
        imagebutton auto "images/system/gallery/music/right_%s.png" action mr.Next() hovered Play("sound", "se_sys/select.ogg") xalign 0.85 yalign 0.54


init -2 python:

    style.music_button = Style(style.default)
    style.music_button.insensitive_background = ("images/system/gallery/music/button_idle.png")
    style.music_button.idle_background = ("images/system/gallery/music/button_idle.png")
    style.music_button.hover_background = ("images/system/gallery/music/button_hover1.png")
    style.music_button.selected_hover_background = ("images/system/gallery/music/button_hover1.png")
    style.music_button.selected_idle_background = ("images/system/gallery/music/button_hover1.png")
    style.music_button.xminimum = 450
    style.music_button.yminimum = 30
    style.music_button_text.color = "#003563"
    style.music_button_text.drop_shadow = None
    style.music_button_text.size = 20
    style.music_button_text.font = "Cochin.ttc"
    style.music_button_text.xalign = 1

#     modal True
#     key 'game_menu' action Hide('gallery')
#     window id 'gallery' at basicfade:
#         xpadding 0
#         ypadding 0
#         add 'ui/a_cg_s1.bmp'
#         add 'ui/title_logo2.png' at fpflourishlower2

#         imagebutton xalign 0.45 yalign 0.15:
#             at buttonexpand01
#             idle 'ui/page0_idle.png'
#             hover 'ui/page0_idle.png'
#             selected_idle 'ui/page0_hover.png'
#             action [FilePage('1'), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)

#         imagebutton xalign 0.7 yalign 0.15:
#             at buttonexpand02
#             idle 'ui/page1_idle.png'
#             hover 'ui/page1_idle.png'
#             selected_idle 'ui/page1_hover.png'
#             action [FilePage('3'), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)

#         imagebutton xalign 0.95 yalign 0.15:
#             at buttonexpand03
#             idle 'ui/gallery_return_idle.png'
#             hover 'ui/gallery_return_idle.png'
#             selected_idle 'ui/gallery_return_hover.png'
#             action [Hide('gallery'), Play('sound', 'se_sys/start.wav')] hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)

#         vbox at fpnavigation2:   
#             for i in range(1, 6):
#                 textbutton str(i):
#                     xalign 0.5
#                     action FilePage(i) style 'loadnavigation01'
#                 null width 10
#             null width 20
                

# transform fpflourishlower2:
#     alpha 0.5 yalign 0.12 xalign 0.1
#     ease 2.0 alpha 1.0 yalign 0.08
#     on hide:
#         ease 0.5 alpha 0.5 yalign 0.12

# transform fpnavigation2:
#     xalign 0.02 yalign 0.5 alpha 0
#     ease 2.0 xalign 0.05 alpha 1.0
#     on hide:
#         ease 0.5 xalign 0.02 alpha 0

# transform buttonexpand01:
#     alpha 0.0 xalign 0.45 yalign 0.12
#     easein 3.0 alpha 1.0 yalign 0.15
#     zoom 1.0
#     on idle:
#         ease 0.2 zoom 1.0
#     on hover:
#         ease 0.2 zoom 1.1

# transform buttonexpand02:
#     alpha 0.0 xalign 0.7 yalign 0.12
#     easein 3.0 alpha 1.0 yalign 0.15
#     zoom 1.0
#     on idle:
#         ease 0.2 zoom 1.0
#     on hover:
#         ease 0.2 zoom 1.1

# transform buttonexpand03:
#     alpha 0.0 xalign 0.95 yalign 0.12
#     easein 3.0 alpha 1.0 yalign 0.15
#     zoom 1.0
#     on idle:
#         ease 0.2 zoom 1.0
#     on hover:
#         ease 0.2 zoom 1.1

# init -2 python:
#     style.loadnavigation01 = Style(style.default)
#     style.loadnavigation01.background = None
#     style.loadnavigation01_text.idle_color = "#1b77f4"
#     style.loadnavigation01_text.hover_color = "#97c7fa"
#     style.loadnavigation01_text.selected_color = "#97c7fa"
#     style.loadnavigation01_text.font = "Cochin.ttc"
#     style.loadnavigation01_text.size = 34
#     style.loadnavigation01_text.drop_shadow = None
#     style.loadnavigation01.xalign = 0.09
#     style.loadnavigation01.yalign = 0.90

screen navigation:

    key 'game_menu' action Return()
    modal True

    add 'images/system/navmenu/background.png' at navbackground
    add 'images/system/navmenu/flourish.png' at navflourish
    if persistent.gamecomplete == True:
        add 'images/system/navmenu/logo2.png' at navbackground1
    else:
        add 'images/system/navmenu/logo.png' at navbackground1

    imagebutton xpos 720 ypos 140:
        at navlayer4
        idle 'images/system/navmenu/BACK.png'
        hover 'images/system/navmenu/BACK-g.png'
        action [Play('sound', 'se_sys/open.ogg'), Return()]
        hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 770 ypos 200:
        at navlayer4
        idle 'images/system/navmenu/SAVE.png'
        hover 'images/system/navmenu/SAVE-g.png'
        action [Show('save'), Play('sound', 'se_sys/open.ogg')]
        hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 800 ypos 270:
        at navlayer4
        idle 'images/system/navmenu/LOAD.png'
        hover 'images/system/navmenu/LOAD-g.png'
        action [Show('load'), Play('sound', 'se_sys/open.ogg')]
        hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 815 ypos 350:
        at navlayer4
        idle 'images/system/navmenu/ENCYCLOPEDIA.png'
        hover 'images/system/navmenu/ENCYCLOPEDIA-g.png'
        action [Show("encyclopedia"), Play("sound", "se_sys/open.ogg")]
        hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 805 ypos 425:
        at navlayer4
        idle 'images/system/navmenu/SETTINGS.png'
        hover 'images/system/navmenu/SETTINGS-g.png'
        action [Show('preferences'), Play('sound', 'se_sys/open.ogg')]
        hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 775 ypos 500:
        at navlayer4
        idle 'images/system/navmenu/TITLE.png'
        hover 'images/system/navmenu/TITLE-g.png'
        action [MainMenu(confirm=True), Play('sound', 'se_sys/alert.ogg')]
        hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 725 ypos 555:
        at navlayer4
        idle 'images/system/navmenu/QUICK.png'
        hover 'images/system/navmenu/QUICK-g.png'
        action [Quit(confirm=True), Play('sound', 'se_sys/alert.ogg')]
        hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)


label game_menu:
    show expression "#0000" with Dissolve(0.0001)
    if renpy.has_screen(_game_menu_screen):
        $ renpy.show_screen(_game_menu_screen)
        $ ui.interact()
        jump _noisy_return
    jump expression _game_menu_screen



transform navbackground:
    alpha 0
    ease 0.2 alpha 1.0
    on hide:
        ease 0.2 alpha 0

transform navbackground1:
    alpha 1.0
    ease 1.5 alpha 0.3
    ease 1.5 alpha 1.0
    repeat
    on hide:
        ease 0.2 alpha 0

transform navflourish:
    zoom 0.9 alpha 0 xalign 0.5 yalign 0.5
    ease 0.1 zoom 1.0 alpha 1.0
    on hide:
        ease 0.2 zoom 0.9 alpha 0

transform navlayer4:
    xoffset -20 alpha 0
    ease 0.2 xoffset 0 alpha 1.0
    on hide:
        ease 0.2 xoffset -20 alpha 0



screen file_picker:
    frame:
        xalign 0.76
        yalign 0.3
        has vbox

        grid 3 3:
            spacing 40
            for i in range(1, 10):
                vbox at fpbuttons:
                    null height 30

                    button:
                        style 'savebutton'
                        action [FileAction(i), Play('sound', 'se_sys/alert.ogg')]
                        key 'save_delete' action [FileDelete(i), Play('sound', 'se_sys/alert.ogg')]
                        hovered Play('sound', 'se_sys/select.wav')

                        add FileScreenshot(i) xalign 0.5 yalign 0.5
    frame:
        xalign 0.7
        yalign 0.91
        has vbox

        grid 3 3:
            spacing 200
            for i in range(1, 10):
                vbox at fpbuttons:
                    null height 8

                    $ description = '% 2s. %s\n%s' % (
                        FileSlotName(i, 3 * 3), 
                        FileTime(i, empty=_('')), 
                        FileSaveName(i))

                    text description style 'savedescription'

transform fpbuttons:
    alpha 0
    0.35
    ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0

init -2 python:

    style.savebutton = Style(style.default)
    style.savebutton.insensitive_background = ("ui/idle_bg.png")
    style.savebutton.idle_background = ("ui/idle_bg.png")
    style.savebutton.hover_background = ("ui/hovered_bg.png")
    style.savebutton.xmaximum = 259
    style.savebutton.ymaximum = 155
    style.savedescription = Style(style.default)

    style.savedescription.color = "#96d9e1"
    style.savedescription.size = 12
    style.savedescription.line_leading = 0
    style.savedescription.drop_shadow = None




screen save():

    modal True
    key 'game_menu' action Hide('save')
    window id 'save' at basicfade:
        xpadding 0
        ypadding 0
        add 'ui/save_bg.bmp'
        add 'ui/overlay.png' at fpoverlay
        add 'ui/flourish_lower.png' at fpflourishlower
        add 'ui/flourish_upper.png' at fpflourishupper
        add 'ui/save_text.png' at fptitletext

        vbox at fpnavigation:

            textbutton _('Auto'):
                action FilePage('auto') style 'savenavigation2'
            null width 20

            textbutton _('Quick'):
                action FilePage('quick') style 'savenavigation2'
            null width 20

            for i in range(1, 9):
                textbutton str(i):
                    xalign 0.5
                    action FilePage(i) style 'savenavigation'
                null width 10
            null width 20

        textbutton 'BACK' action Hide('save') style 'savenavigation' at fpback

        use file_picker


transform fpback:
    xalign 0.1 yalign 0.97 alpha 0
    ease 0.5 yalign 0.95 alpha 1.0
    on hide:
        ease 0.5 yalign 0.97 alpha 0

transform fptitletext:
    xalign 0.09 yalign 0.09 alpha 0
    ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0


transform basicfade:
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0

transform fpoverlay:
    alpha 0
    0.25
    ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0

transform fpflourishlower:
    alpha 0.5 yalign 1.1 xalign 1.0
    ease 0.5 alpha 1.0 yalign 1.0
    on hide:
        ease 0.5 alpha 0.5 yalign 1.1


transform fpflourishupper:
    alpha 0.5 yalign 0 xalign 0.01
    ease 0.5 alpha 1.0 yalign 0.05
    on hide:
        ease 0.5 alpha 0.5 yalign 0

transform fpnavigation:
    xalign 0.09 yalign 0.6 alpha 0
    ease 0.5 yalign 0.53 alpha 1.0
    on hide:
        ease 0.5 yalign 0.6 alpha 0

init -2 python: 

    style.savenavigation = Style(style.default)
    style.savenavigation.background = None
    style.savenavigation_text.idle_color = "#9cdce3"
    style.savenavigation_text.hover_color = "#FFFFFF"
    style.savenavigation_text.selected_color = "#FFFFFF"
    style.savenavigation_text.font = "Cochin.ttc"
    style.savenavigation_text.size = 34
    style.savenavigation_text.drop_shadow = None
    style.savenavigation.xalign = 0.09
    style.savenavigation.yalign = 0.90

    style.savenavigation2 = Style(style.default)
    style.savenavigation2.background = None
    style.savenavigation2_text.idle_color = "#9cdce3"
    style.savenavigation2_text.hover_color = "#FFFFFF"
    style.savenavigation2_text.selected_color = "#FFFFFF"
    style.savenavigation2_text.size = 28
    style.savenavigation2_text.drop_shadow = None
    style.savenavigation2.xalign = 0.5




screen load():

    modal True
    key 'game_menu' action Hide('load')
    window id 'load' at basicfade:
        xpadding 0
        ypadding 0
        add 'ui/load_bg.bmp'
        add 'ui/overlay.png' at fpoverlay
        add 'ui/flourish_lowerpurp.png' at fpflourishlower
        add 'ui/flourish_upper.png' at fpflourishupper
        add 'ui/load_text.png' at fptitletext

        vbox at fpnavigation:

            textbutton _('Auto'):
                action FilePage('auto') style 'loadnavigation2'
            null width 20

            textbutton _('Quick'):
                action FilePage('quick') style 'loadnavigation2'
            null width 20

            for i in range(1, 9):
                textbutton str(i):
                    xalign 0.5
                    action FilePage(i) style 'loadnavigation'
                null width 10
            null width 20

        textbutton 'BACK' action Hide('load') style 'loadnavigation' at fpback

        use file_picker

init -2 python:
    style.loadnavigation = Style(style.default)
    style.loadnavigation.background = None
    style.loadnavigation_text.idle_color = "#FFFFFF"
    style.loadnavigation_text.hover_color = "#c29ec4"
    style.loadnavigation_text.selected_color = "#c29ec4"
    style.loadnavigation_text.font = "Cochin.ttc"
    style.loadnavigation_text.size = 34
    style.loadnavigation_text.drop_shadow = None
    style.loadnavigation.xalign = 0.09
    style.loadnavigation.yalign = 0.90

    style.loadnavigation2 = Style(style.default)
    style.loadnavigation2.background = None
    style.loadnavigation2_text.idle_color = "#FFFFFF"
    style.loadnavigation2_text.hover_color = "#c29ec4"
    style.loadnavigation2_text.selected_color = "#c29ec4"
    style.loadnavigation2_text.size = 28
    style.loadnavigation2_text.drop_shadow = None
    style.loadnavigation2.xalign = 0.5






screen preferences() tag test:

    modal True
    zorder 1
    key 'game_menu' action Hide('preferences')
    window id 'preferences' at basicfade:
        xpadding 0
        ypadding 0
        add 'ui/pref_bg.png'
        add 'ui/flourish_lowerbw.png' at fpflourishlower
        add 'ui/flourish_upper1.png' at fpflourishuppersys
        add 'ui/preferences_text.png' at pftitletextsys

        add 'images/system/preferences/pref_boxes.png' at pfboxes
        vbox at pffade1:
            hbox:
                style 'preferences1'
                imagebutton auto 'images/system/preferences/window_%s.png' action Preference('display', 'window')
                imagebutton auto 'images/system/preferences/fullscreen_%s.png' action Preference('display', 'fullscreen')
            null height 45
            hbox:
                style 'preferences2'
                imagebutton auto 'images/system/preferences/fxon_%s.png' action Preference('transitions', 'all')
                imagebutton auto 'images/system/preferences/fxoff_%s.png' action Preference('transitions', 'none')
            null height 165
            hbox:
                style 'preferences3'
                imagebutton auto 'images/system/preferences/seenread_%s.png' action Preference('skip', 'seen')
                imagebutton auto 'images/system/preferences/alltext_%s.png' action Preference('skip', 'all')
            null height 50
            hbox:
                style 'preferences4'
                imagebutton auto 'images/system/preferences/stop_%s.png' action Preference('after choices', 'stop')
                imagebutton auto 'images/system/preferences/skip_%s.png' action Preference('after choices', 'skip')
            null height 70
            hbox:
                xpos 200
                style 'preferences5'
                # imagebutton auto 'images/system/preferences/en_%s.png' action Language("english")
                # imagebutton auto 'images/system/preferences/jp_%s.png' action Language(None)
                imagebutton auto 'images/system/preferences/18X_%s.png' action Start('H18')
                imagebutton auto 'images/system/preferences/G_%s.png' action Start('All')

        bar value Preference('text speed') xmaximum 450 at pfbarfade1
        vbox at pfbarfade2:
            spacing 105
            bar value Preference('music volume') xmaximum 450
            bar value Preference('sound volume') xmaximum 450
            bar value Preference('auto-forward time') xmaximum 450

        textbutton 'BACK' action Hide('preferences') style 'savepreferences' at fpbacksys

label H18:
    
    $ persistent.H = True
    $ config.window_title = u"The Seasons Of Angel - 18X"
    return

label All:
    
    $ persistent.H = False
    $ config.window_title = u"The Seasons Of Angel - General"
    return

transform pfbarfade1:
    xpos 120 ypos 345 alpha 0
    0.25
    ease 0.5 alpha 1.0
    on hide:
        0.5
        ease 0.5 alpha 0

transform pfbarfade2:
    xpos 700 ypos 220 alpha 0
    0.25
    ease 0.5 alpha 1.0
    on hide:
        0.5
        ease 0.5 alpha 0

transform fpflourishuppersys:
    alpha 0.5 yalign 0 xalign 0.515
    ease 0.5 alpha 1.0 yalign 0.1
    on hide:
        ease 0.5 alpha 0.5 yalign 0

transform pftitletextsys:
    xalign 0.5 yalign 0.12 alpha 0
    ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0

transform pfboxes:
    xalign 0.5 yalign 0.55 zoom 1.2 alpha 0
    ease 0.25 zoom 1.0 alpha 1.0
    on hide:
        ease 0.5 zoom 1.2 alpha 0

transform pffade1:
    xpos 310 ypos 180 alpha 0
    0.25
    ease 0.5 alpha 1.0
    on hide:
        0.5
        ease 0.5 alpha 0

transform fpbacksys:
    xalign 0.5 yalign 0.97 alpha 0
    ease 0.5 yalign 0.92 alpha 1.0
    on hide:
        ease 0.5 yalign 0.97 alpha 0


init -2:

    style pref_button size_group "pref"
    style pref_button xalign 1.0
    style pref_slider xmaximum 192
    style pref_slider xalign 1.0
    style soundtest_button xalign 1.0
    style preferences1:
        xoffset -30
        yoffset 2
        spacing 65
    style preferences2:
        xoffset -30
        yoffset 7
        spacing 120
    style preferences3:
        xoffset -30
        yoffset 7
        spacing 10
    style preferences4:
        xoffset -30
        yoffset 7
        spacing 20
    style preferences5:
        yoffset 10

init -2 python:

    style.savepreferences = Style(style.default)
    style.savepreferences.background = None
    style.savepreferences_text.idle_color = "#9cdce3"
    style.savepreferences_text.hover_color = "#FFFFFF"
    style.savepreferences_text.selected_color = "#FFFFFF"
    style.savepreferences_text.font = "Cochin.ttc"
    style.savepreferences_text.size = 34
    style.savepreferences_text.drop_shadow = None
    style.savepreferences.xalign = 0.5
    style.savepreferences.yalign = 0.92





screen yesno_prompt:

    modal True
    zorder 2
    key 'game_menu' action no_action

    window id 'yesno' at popup:
        style 'alertwindow'


    label _(message):
        style 'yesno_prompt'
        text_style 'yesno_prompt_text'

    
    imagebutton xpos 490 yalign 0.5:
            idle 'ui/menu_yes_1.png'
            hover 'ui/menu_yes_2.png'
            action [yes_action, Play('sound', 'se_sys/start.wav')]
            hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)

    imagebutton xpos 680 yalign 0.5:
            idle 'ui/menu_no_1.png'
            hover 'ui/menu_no_2.png'
            action [no_action, Play('sound', 'se_sys/cancel.wav')]
            hovered Play('sound', 'se_sys/hover.wav', fadein=0.2, fadeout=0.2)
            


transform popup:
    xalign 0.5 alpha 0.0 yalign 0.55
    ease 0.25 yalign 0.45 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0 yalign 0.55


screen quick_menu:


    on 'show' action If(in_quick_menu_area(), true=Show('actual_quick_menu', atl=quick_menu_show0), false=Show('actual_quick_menu', atl=quick_menu_hide0))
    on 'hide' action Hide('actual_quick_menu')
    mousearea:
        area (0, 680, 1280, 40)
        hovered [Show('actual_quick_menu', atl=quick_menu_show)]
        unhovered [Show('actual_quick_menu', atl=quick_menu_hide)]

screen actual_quick_menu:

    window:
        at atl
        style_group 'quick_menu'
        vbox:
            yalign 1.0
            add 'ui/quickmenu-top.png'
            add 'ui/qmenu-leftrightbars.png'

        imagebutton xpos 410 yalign 1.0:
            idle 'ui/quickmenu/fc_play_1.png'
            hover 'ui/quickmenu/fc_play_2.png'
            selected_idle 'ui/quickmenu/fc_play_3.png'
            action Preference('auto-forward', 'toggle')
            hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
        imagebutton xpos 460 yalign 1.0:
            idle 'ui/quickmenu/fc_skip_1.png'
            hover 'ui/quickmenu/fc_skip_2.png'
            selected_idle 'ui/quickmenu/fc_skip_3.png'
            action Skip()
            hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
        imagebutton xpos 510 yalign 1.0:
            idle 'ui/quickmenu/fc_save_1.png'
            hover 'ui/quickmenu/fc_save_2.png'
            action QuickSave()
            hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
        imagebutton xpos 570 yalign 1.0:
            idle 'ui/quickmenu/fc_qload_1.png'
            hover 'ui/quickmenu/fc_qload_2.png'
            action QuickLoad()
            hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
        imagebutton xpos 640 yalign 1.0:
            idle 'ui/quickmenu/fc_wincls_1.png'
            hover 'ui/quickmenu/fc_wincls_2.png'

            hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
        imagebutton xpos 710 yalign 1.0:
            idle 'ui/quickmenu/fc_system_1.png'
            hover 'ui/quickmenu/fc_system_2.png'
            action [Show('preferences'), Play('sound', 'se_sys/open.ogg')]
            hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
        imagebutton xpos 765 yalign 1.0:
            idle 'ui/quickmenu/fc_back_1.png'
            hover 'ui/quickmenu/fc_back_2.png'
            action [MainMenu(confirm=True), Play('sound', 'se_sys/alert.ogg')]
            hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)
        imagebutton xpos 830 yalign 1.0:
            idle 'ui/quickmenu/fc_lock_1.png'
            hover 'ui/quickmenu/fc_lock_2.png'
            action [Quit(confirm=True), Play('sound', 'se_sys/alert.ogg')]
            hovered Play('sound', 'se_sys/select.wav', fadein=0.2, fadeout=0.2)



init -2 python:

    config.default_afm_time = 10
    config.default_afm_enable = False

    def in_quick_menu_area():
        x, y = renpy.get_mouse_pos()
        if y >= 680:
            return True
        else:
            return False

transform quick_menu_show0:
    yoffset 0

transform quick_menu_show:
    ease .2 yoffset 0

transform quick_menu_hide:
    ease .2 yoffset 30

transform quick_menu_hide0:
    yoffset 30

screen disable_inputs:
    key 'K_RETURN' action Hide('nonexistent_screen')
    key 'K_KP_ENTER' action Hide('nonexistent_screen')
    key 'K_SPACE' action Hide('nonexistent_screen')

    key 'mousedown_4' action Hide('nonexistent_screen')
    key 'K_PAGEUP' action Hide('nonexistent_screen')
    key 'mousedown_5' action Hide('nonexistent_screen')
    key 'K_PAGEDOWN' action Hide('nonexistent_screen')

    key 'mouseup_3' action Hide('nonexistent_screen')
    key 'mouseup_1' action Hide('nonexistent_screen')

    key 'K_ESCAPE' action Return('smth')