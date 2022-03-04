init python:
    def invoke_game_menu():
        if not mouse_visible: return
        _invoke_game_menu()

    config.underlay[0].keymap['game_menu'] = invoke_game_menu


screen navigation():
    tag menu
    modal True

    add '9i/interface/mainmenu/vignette.png' at navbackground
    add '9i/interface/mainmenu/flourish.png' at navflourish
    add '9i/interface/mainmenu/logo.png' at navbackground1

    imagebutton xpos 1080 ypos 210:
        at navlayer4
        idle '9i/interface/mainmenu/BACK.png'
        hover '9i/interface/mainmenu/BACK-g.png'
        action [Play('sound', '9i/interface/open.ogg'), MenuReturn()]
        hovered Play('sound', '9i/interface/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 1155 ypos 300:
        at navlayer4
        idle '9i/interface/mainmenu/SAVE.png'
        hover '9i/interface/mainmenu/SAVE-g.png'
        action [Show('save'), Play('sound', '9i/interface/open.ogg')]
        hovered Play('sound', '9i/interface/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 1200 ypos 405:
        at navlayer4
        idle '9i/interface/mainmenu/LOAD.png'
        hover '9i/interface/mainmenu/LOAD-g.png'
        action [Show('load'), Play('sound', '9i/interface/open.ogg')]
        hovered Play('sound', '9i/interface/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 1223 ypos 525:
        at navlayer4
        idle '9i/interface/mainmenu/ENCYCLOPEDIA.png'
        hover '9i/interface/mainmenu/ENCYCLOPEDIA-g.png'
        action [Show("encyclopedia"), Play("sound", "9i/interface/open.ogg")]
        hovered Play('sound', '9i/interface/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 1208 ypos 638:
        at navlayer4
        idle '9i/interface/mainmenu/SETTINGS.png'
        hover '9i/interface/mainmenu/SETTINGS-g.png'
        action [Show('preferences'), Play('sound', '9i/interface/open.ogg')]
        hovered Play('sound', '9i/interface/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 1163 ypos 750:
        at navlayer4
        idle '9i/interface/mainmenu/TITLE.png'
        hover '9i/interface/mainmenu/TITLE-g.png'
        if persistent.now_story != "序章":
            action [MainMenu(confirm=True), Play('sound', '9i/interface/alert.ogg')]
        hovered Play('sound', '9i/interface/select.wav', fadein=0.2, fadeout=0.2)
    imagebutton xpos 1088 ypos 833:
        at navlayer4
        idle '9i/interface/mainmenu/QUICK.png'
        hover '9i/interface/mainmenu/QUICK-g.png'
        action [Quit(confirm=True), Play('sound', '9i/interface/alert.ogg')]
        hovered Play('sound', '9i/interface/select.wav', fadein=0.2, fadeout=0.2)

    key 'game_menu' action MenuReturn()
    label _("{#nav}MENU") style "caption_label" at caption_inter

transform navbackground:
    alpha 0
    ease 0.2 alpha 1.0
    on hide:
        ease 0.2 alpha 0


transform navflourish:
    zoom 0.9 alpha 0 xalign 0.5 yalign 0.5
    ease 0.1 zoom 1.0 alpha 1.0
    on hide:
        ease 0.2 zoom 0.9 alpha 0


transform navbackground1:
    alpha 1.0
    ease 1.5 alpha 0.3
    ease 1.5 alpha 1.0
    repeat
    on hide:
        ease 0.2 alpha 0


transform navlayer4:
    xoffset -20 alpha 0
    ease 0.2 xoffset 0 alpha 1.0
    on hide:
        ease 0.2 xoffset -20 alpha 0


style caption_label is default:
    xpos int(scale(-0.5))
    ypos scale(-1)
    xsize scale(663)
    ysize int(scale(226.5))
    background imagescale(1080)("9i/interface/menu caption.png")

transform caption_inter:
    on show:
        subpixel True
        yanchor 1.0
        power_in_time_warp_real 0.5 yanchor 0.0

style caption_label_text is text:
    xcenter int(scale(336.5))
    ycenter scale(63)
    font "9i/fonts/FOT-SkipStd-B.otf"
    size scale(36)
    color "#f1cf7b"
    outlines [(0, "#050b29", scale(1.5), scale(1.5))]


screen replay_navigation():
    on "show" action Confirm(
        prompt=layout.END_REPLAY,
        no_action=Return(),
        yes_action=EndReplay(confirm=False))
    on "update" action Return()


init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    @renpy.pure
    class MenuReturn(renpy.ui.Action):
        """Convenience action to close a menu screen.
        """
        def __call__(self):
            current_screen = renpy.current_screen()
            
            
            if renpy.context()._main_menu:
                return renpy.run(Hide(current_screen.screen_name[0]))
            
            # elif not current_screen.scope.get('standalone'):
            #     return renpy.run(Show(_game_menu_screen))
            
            elif renpy.context()._menu:
                return renpy.run(Return())
            
            else:
                return renpy.run(Hide(current_screen.screen_name[0]))
