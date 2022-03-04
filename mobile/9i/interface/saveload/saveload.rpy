screen file_left_button(i):
    $ file_slot = FileSlotName(i, 8, auto="A", quick="Q")
    button action FileAction(i) style_prefix "file_left":
        key 'save_delete' action [FileDelete(i), Play('sound', '9i/interface/alert.ogg')]
        alternate [FileDelete(i), Play('sound', '9i/interface/alert.ogg')]
        add FileScreenshot(i, empty="system file thumb empty") at file_left_button_thumb
        text "[file_slot]" style "file_left_number_text"
        vbox style "file_left_info_vbox" style_prefix "file":
            if FileLoadable(i):
                $ file_name = FileSaveName(i)
                text "[file_name]"
                $ file_date, file_time = FileTime(i).split(", ")
                text "[file_date]"
                text "[file_time]"
            else:
                text _("Empty Slot.")

screen file_right_button(i):
    $ file_slot = FileSlotName(i, 8, auto="A", quick="Q")
    button action FileAction(i) style_prefix "file_right":
        key 'save_delete' action [FileDelete(i), Play('sound', '9i/interface/alert.ogg')]
        alternate [FileDelete(i), Play('sound', '9i/interface/alert.ogg')]
        add FileScreenshot(i, empty="system file thumb empty") at file_right_button_thumb
        text "[file_slot]" style "file_right_number_text"
        vbox style "file_right_info_vbox" style_prefix "file":
            if FileLoadable(i):
                $ file_name = FileSaveName(i)
                text "[file_name]"
                $ file_date, file_time = FileTime(i).split(", ")
                text "[file_date]"
                text "[file_time]"
            else:
                text _("Empty Slot.")

init:
    transform file_left_button_thumb:
        xpos scale(108)
        ypos int(scale(19.5))
        size (scale(252), scale(142))
    transform file_right_button_thumb:
        xpos int(scale(267.5))
        ypos int(scale(18.5))
        size (scale(252), scale(142))

    image system file thumb empty = Fixed(
        "9i/interface/saveload/thumb blank.jpg",
        Text(_("{#file}NO DATA"), xcenter=0.5, ycenter=0.5, style="file_thumb_text"),
        fit_first=True)

    style file_text is text:
        font "9i/fonts/FOT-SkipStd-B.otf"
        size scale(28)
        kerning scale(-1.0)
        color "#fff4d9"
        outlines [(0.0, "#341c0b", scale(-0.5), scale(-0.5))]
    style file_thumb_text is file_text:
        color "#948268"
        outlines []
    style file_left_button is default:
        xsize int(scale(626.5))
        ysize int(scale(182.5))
        background imagescale(1080)("9i/interface/saveload/file.png")
        hover_background imagescale(1080)("9i/interface/saveload/file hover.png")
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"
    style file_left_number_text is file_text:
        xanchor 1.0
        xpos scale(81)
        ycenter 0.5
    style file_left_info_vbox is vbox:
        xpos scale(390)
        ycenter 0.5
        spacing scale(6)
    style file_right_button is file_left_button:
        background imagescale(1080)(
            Transform("9i/interface/saveload/file.png", xzoom=-1))
        hover_background imagescale(1080)(
            Transform("9i/interface/saveload/file hover.png", xzoom=-1))
    style file_right_number_text is file_left_number_text:
        xpos scale(540)
        xanchor 0.0
    style file_right_info_vbox is vbox:
        xpos scale(48)
        ycenter 0.5
        spacing scale(6)

init python:
    renpy.start_predict(
        "9i/interface/saveload/load bg.png",
        "9i/interface/saveload/save bg.png")

screen load(standalone=False):
    tag menu
    modal True

    default play_action = [
        Play(channel="movie", file="9i/interface/saveload/load bg.mp4", loop=False),
        Play(channel="audio", file="9i/interface/flag drop 2.ogg")
    ]
    default stop_action = Stop(channel="movie")

    on "show" action play_action
    on "replace" action play_action
    on "replaced" action stop_action
    on "hide" action stop_action

    add "9i/interface/saveload/load bg.png" at imagescale(1080)
    add "movie"
    frame style_prefix "load_file_menu" at file_menu_inter:
        has fixed
        vbox:
            textbutton _("Auto") action FilePage("auto")
            for i in xrange(1, 8 + 1):
                textbutton "[i]" action FilePage(i)
        textbutton "Return" style "load_file_menu_return_button":


            action [stop_action, MenuReturn()]
            keysym "game_menu"
    label _("{#file}LOAD") style "caption_label" at caption_inter
    frame style_prefix "load_file_left" at file_buttons_left_inter:
        has vbox
        for i in xrange(1, 4 + 1):
            use file_left_button(i)
    frame style_prefix "load_file_right" at file_buttons_right_inter:
        has vbox
        for i in xrange(5, 8 + 1):
            use file_right_button(i)

screen save(standalone=False):
    tag menu
    modal True

    default play_action = [
        Play(channel="movie", file="9i/interface/saveload/save bg.mp4", loop=False),
        Play(channel="audio", file="9i/interface/flag_roll_down.ogg")
    ]
    default stop_action = Stop(channel="movie")

    on "show" action play_action
    on "replace" action play_action
    on "replaced" action stop_action
    on "hide" action stop_action

    add "9i/interface/saveload/save bg.png" at imagescale(1080)
    add "movie"
    frame style_prefix "save_file_menu" at file_menu_inter:
        has fixed
        vbox:
            textbutton _("Auto") action FilePage("auto")
            for i in xrange(1, 8 + 1):
                textbutton "[i]" action FilePage(i)
        textbutton "Return" style "save_file_menu_return_button":


            action [stop_action, MenuReturn()]
            keysym "game_menu"
    label _("{#file}SAVE") style "caption_label" at caption_inter
    frame style_prefix "save_file_left" at file_buttons_left_inter:
        has vbox
        for i in xrange(1, 4 + 1):
            use file_left_button(i)
    frame style_prefix "save_file_right" at file_buttons_right_inter:
        has vbox
        for i in xrange(5, 8 + 1):
            use file_right_button(i)


init:
    transform file_menu_inter:
        alpha 0
        0.3
        linear 0.2 alpha 1
    transform file_buttons_left_inter:
        subpixel True
        yanchor -1.0
        0.1
        power_in_time_warp_real 0.5 yanchor 0.0
    transform file_buttons_right_inter:
        subpixel True
        yanchor -1.0
        0.2
        power_in_time_warp_real 0.5 yanchor 0.0

    style file_menu_frame is default:
        xpos scale(59)
        ypos int(scale(-25))
        xsize scale(378)
        ysize scale(1158)
    style load_file_menu_frame is file_menu_frame
    style save_file_menu_frame is file_menu_frame
    style file_menu_vbox is vbox:
        xcenter 0.5
        ypos scale(183)
        spacing scale(-6)
    style file_menu_button is default:
        xsize scale(280)
        yminimum int(scale(62.5))
        activate_sound "9i/interface/click1.ogg"
    style load_file_menu_button is file_menu_button:
        hover_background imagescale(1080)(
            Image(
                "9i/interface/saveload/load menu button hover.png",
                xcenter=0.5,
                ycenter=0.5))
        selected_background imagescale(1080)(
            Image(
                "9i/interface/saveload/load menu button hover.png",
                xcenter=0.5,
                ycenter=0.5))
    style save_file_menu_button is file_menu_button:
        hover_background imagescale(1080)(
            Image(
                "9i/interface/saveload/save menu button hover.png",
                xcenter=0.5,
                ycenter=0.5))
        selected_background imagescale(1080)(
            Image(
                "9i/interface/saveload/save menu button hover.png",
                xcenter=0.5,
                ycenter=0.5))
    style file_menu_button_text is text:
        xcenter 0.5
        ycenter 0.5
        font "9i/fonts/FOT-SkipStd-B.otf"
        size scale(36)

        line_leading scale(9)
        line_spacing scale(-9)
        color "#fff"
        outlines [(scale(3.0), "#050b29", scale(0.0), scale(1.5))]
    style load_file_menu_button_text is file_menu_button_text:
        hover_color "#8fffe7"
    style save_file_menu_button_text is file_menu_button_text:
        hover_color "#ffe386"
    style file_menu_return_button is file_menu_button:
        xcenter 0.5
        ycenter scale(780)
    style load_file_menu_return_button is file_menu_return_button:
        properties style.load_file_menu_button.inspect()[0][1]
    style save_file_menu_return_button is file_menu_return_button:
        properties style.save_file_menu_button.inspect()[0][1]
    style file_menu_return_button_text is file_menu_button_text
    style load_file_menu_return_button_text is load_file_menu_button_text:
        properties style.file_menu_return_button_text.inspect()[0][1]
    style save_file_menu_return_button_text is save_file_menu_button_text:
        properties style.file_menu_return_button_text.inspect()[0][1]
    style file_left_frame is default:
        xsize scale(663)
        ysize scale(1081)
        background imagescale(1080)(Image(
            "9i/interface/saveload/pole left.png",
            xalign=1.0))
    style load_file_left_frame is file_left_frame:
        xpos scale(455)
        ypos scale(115)
    style save_file_left_frame is file_left_frame:
        xpos int(scale(456.5))
        ypos scale(7)
    style file_left_vbox is vbox:
        ypos scale(144)
        spacing scale(16)
    style file_right_frame is default:
        xsize scale(663)
        ysize scale(1081)
        background imagescale(1080)("9i/interface/saveload/pole right.png")
    style load_file_right_frame is file_right_frame:
        xpos int(scale(1155.5))
        ypos int(scale(20.5))
    style save_file_right_frame is file_right_frame:
        xpos int(scale(1155.5))
        ypos int(scale(128.5))
    style file_right_vbox is file_left_vbox:
        xpos scale(40)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
