
init:
    image bg table = "9i/interface/battle/system/d_icon0.png"

init -3 python:
    theme.roundrect(
        widget = "#ffc4e464",
        widget_hover = "#ffc4e484",
        widget_text = "#ffffffcc",
        widget_selected = "#ffffffff",
        disabled = "#22222288",
        disabled_text = "#594f4f",
        label = "#ffffffdd",
        mm_root = "main_menu",
        rounded_window = False,
        text_size = 32)

    # Activity Button
    style.activity = Style(style.default)
    style.activity.activate_sound = "9i/interface/click2.ogg"
    style.activity.xpadding = 60
    style.activity.ypadding = 20
    style.activity_text.font = "9i/fonts/浪漫雅圆.ttf"
    style.activity_text.size = 22
    style.activity_text.kerning = -0.5
    style.activity_text.outlines = [ (absolute(1), "#ffffff55", absolute(0), absolute(0)) ]
    style.activity.outlines = [ (absolute(1), "#ffffff55", absolute(0), absolute(0)) ]
    style.activity.insensitive_background = Frame("9i/interface/battle/system/textbtn.png", 50, 20, tile=False)
    style.activity.idle_background = Frame(im.MatrixColor("9i/interface/battle/system/textbtn.png", im.matrix.tint(1, 0.8, 0.9)), 20, 20, tile=False)
    style.activity.hover_background = Frame(im.MatrixColor("9i/interface/battle/system/textbtn.png", im.matrix.tint(1, 0, 0.5)), 20, 20, tile=False)

    renpy.register_style_preference("button", "off", style.button, "hover_sound", None)
    renpy.register_style_preference("button", "off", style.slider, "hover_sound", None)
    renpy.register_style_preference("button", "on", style.scrollbar, "hover_sound", None)
    renpy.register_style_preference("button", "on", style.vscrollbar, "hover_sound", None)

    renpy.register_style_preference("button", "on", style.button, "hover_sound", "Hover_Button")
    renpy.register_style_preference("button", "on", style.slider, "hover_sound", "Hover_Button")
    renpy.register_style_preference("button", "on", style.scrollbar, "hover_sound", "Hover_Button")
    renpy.register_style_preference("button", "on", style.vscrollbar, "hover_sound", "Hover_Button")

    font_text = "9i/fonts/浪漫雅圆.ttf"
    font_label = "9i/fonts/浪漫雅圆.ttf"
    font_name = "9i/fonts/浪漫雅圆.ttf"
    font_button = "9i/fonts/浪漫雅圆.ttf"

style frame_title:
    font "9i/fonts/浪漫雅圆.ttf"
    xalign 0.5
    size 66
    kerning -0.5
    outlines [ (absolute(1), "#ffffff55", absolute(0), absolute(0)) ]
    text_align 0.5

style button:
    insensitive_background None
    idle_background None
    selected_background None
    hover_background gui_shine(Frame("9i/interface/battle/system/button_shine_small.png", 18, 9))
    selected_hover_background gui_shine(Frame("9i/interface/battle/system/button_shine_small.png", 18, 9))

    xpadding 6
    ypadding 3
    xmargin 0
    ymargin 0

style slider:
    left_bar Frame("9i/interface/battle/system/slider_idle.png", 18, 9)
    hover_left_bar Frame("9i/interface/battle/system/slider_hover.png", 18, 9)
    selected_hover_left_bar Frame("9i/interface/battle/system/slider_selected.png", 18, 9)
    right_bar Frame("9i/interface/battle/system/slider_disabled.png", 18, 9)
    thumb None
    left_gutter 18
    right_gutter 0
    ysize 21

style scrollbar:
    left_bar None
    right_bar None
    unscrollable "hide"
    ysize 15

style say_dialogue3:
    size 33
    color "#3d220c"
    outlines []

style say_dialogue2:
    font "9i/fonts/浪漫雅圆.ttf"
    size 33
    color "#3d220c"
    outlines []

style effect_text:
    size 75
    font font_name
    outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
style finish_text is effect_text:
    size 120
    color "#f00"
    outlines [(0, "#0006", 6, 6), (4, "#000c"), (3, "000")]
style ability_text is effect_text:
    size 60
    color "#ff6"
style damage_text is effect_text

style label_text:
    color "#fff2de"
    font font_label
    bold False
    size 33
style large_label is label
style large_label_text is label_text:
    font font_button
    size 75

style nav_menu_frame is frame:
    background Frame("9i/interface/battle/system/frame.png", 18, 18)
style nav_menu_button:
    xfill True
    xalign 0.1

style item_frame is frame:
    background Frame("9i/interface/battle/system/frame.png", 18, 18)
style item_button take button:
    xfill True
    xalign 0.5
style item_button_text take button_text

style vscrollbar:
    top_bar None
    bottom_bar None
    thumb Frame("9i/interface/battle/system/vscrollbar_thumb_idle.png", 18, 9)
    hover_thumb Frame("9i/interface/battle/system/vscrollbar_thumb_hover.png", 18, 9)
    selected_hover_thumb Frame("9i/interface/battle/system/vscrollbar_thumb_selected.png", 18, 9)
    unscrollable "hide"
    xsize 15
style alt_vscrollbar:
    top_bar None
    bottom_bar None
    thumb Frame("9i/interface/battle/system/scroll_thumb.png", 18, 9)
    hover_thumb Frame("9i/interface/battle/system/scroll_thumb.png", 18, 9)
    selected_hover_thumb Frame("9i/interface/battle/system/scroll_thumb.png", 18, 9)
    unscrollable "hide"
    xsize 18
    xoffset 4
    top_gutter 12
    bottom_gutter 12

style skill_text is effect_text:
    size 105
    color "#77f"
    font "9i/fonts/浪漫雅圆.ttf"
    outlines [(0, "#0009", 4, 4), (2, "#000d"), (1, "#000")]
    text_align 0.5
    xmaximum 585

style small_button take button:
    insensitive_background Frame("9i/interface/battle/system/button_disabled.png", 18, 18)
    idle_background Frame("9i/interface/battle/system/button_idle.png", 18,18)
    selected_background Frame("9i/interface/battle/system/button_selected.png", 18,18)
    hover_background Fixed(Frame("9i/interface/battle/system/button_selected.png", 18,18),
        gui_shine(Frame("9i/interface/battle/system/button_hover.png", 18,18)))
    selected_hover_background Fixed(Frame("9i/interface/battle/system/button_selected.png", 18,18),
        gui_shine(Frame("9i/interface/battle/system/button_hover.png", 18,18)))
    xminimum 114
    xpadding 6
    ypadding 4
style small_button_text take button:
    size 24
style large_button take small_button:
    xmargin 1
    ymargin 1
    xfill True
style large_button_text take button
style slot_button2 is small_button:
    xpadding 15
    ypadding 15
style orientation_button is small_button:
    background None
    hover_background gui_shine("#ff8")
    xpadding 15
    ypadding 1
    xsize 112
    ysize 112
    activate_sound None

style face_button is button:
    hover_background gui_shine("#ff69")
    selected_hover_background gui_shine("#ff69")

style attributes_button:
    ypadding 0
    hover_background gui_shine("#ee56")
    selected_hover_background gui_shine("#ee56")

style skill_button take large_button:
    xsize 285

style say_label2:
    size 36
    bold False
    font font_name
    outlines [(1, "#0009", 1, 1), (1, "#000d")]

style bFont:
    font font_name
    size 36

style default:
    font font_text
    outlines [(1, "#341f1b", 1, 1)]
    color "#fff2de"
    size 30

style say_thought:
    size 33

style text:
    size 28

style centered_text:
    size 150
    font font_button
    outlines [(1, "#0009", 1, 1), (1, "#000d")]

style window:
    background Frame("9i/interface/battle/system/textbox2.png", 18, 18)
    left_padding 27
    right_padding 18
    ypadding 27
    xsize 975
    ysize 270
    align (0.5, 0.95)

style gm_root:
    background "#000c"

style mm_root:
    background "#000c"

style frame:
    background Frame("9i/interface/battle/system/frame.png", 18, 18)
    xpadding 9
    ypadding 9
style pref_frame is frame:
    background Frame("9i/interface/battle/system/frame.png", 18, 18)
style small_frame is frame

style label:
    bottom_margin 4

style button_text:
    color "#fff2de"
    insensitive_color "#666"

    selected_color "#ff6"
    hover_color "#ffa"
    selected_hover_color "#ff6"
    font font_button
    size 28

style slot_button_text2 is default

style orientation_button_text is default:
    size 54
    xalign 0.5

style mm_button:
    xalign 0.5
    xpadding 90
    hover_background Fixed(im.Flip("9i/interface/battle/system/mm_frame_side.png", horizontal=True, align=(0.0, 0.5), xoffset=60),
        Image("9i/interface/battle/system/mm_frame_center.png", align=(0.5, 0.6)), Image("9i/interface/battle/system/mm_frame_side.png", align=(1.0, 0.5), xoffset=-60))

style mm_button_text:
    font "9i/fonts/浪漫雅圆.ttf"
    size 36
    color "#ffe2c3"
    insensitive_color "#777"
    hover_color "#fff1e1"
    outlines [(4, "#36365b99", -3, 2), (3, "#36365b", -3, 2), (1, "#36365b99")]

style teleporter_button:
    xoffset 6
    yoffset 6
    xysize (240, 135)
    hover_background gui_shine("#ff69")
    activate_sound None

style bar:
    left_bar Frame("9i/interface/battle/system/bar_red.png", 18, 6)
    right_bar None
    left_gutter 0
    right_gutter 18
    thumb None
    ysize 24









