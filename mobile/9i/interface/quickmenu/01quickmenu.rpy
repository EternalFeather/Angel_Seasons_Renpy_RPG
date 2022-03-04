
# screen quick_menu():
#     zorder +1

#     default state = "idle"
#     default tooltip = Tooltip(None)

#     on "update" action [
#         SetScreenVariable("state", "idle"),
#         ResetTooltip(tooltip)
#     ]

#     key "focus_up" action NullAction()
#     key "focus_down" action NullAction()
#     key "focus_left" action NullAction()
#     key "focus_right" action NullAction()

#     frame style_prefix "qm" at qm_sh, get_qm_tf(state, default=qm_default, idle=qm_idle, hover=qm_hover):
#         has hbox
#         button:
#             has fixed fit_first True
#             button at invisible:
#                 add "system qm blue prefs"
#             button at get_qm_tf(state, idle=qm_gear_idle, hover=qm_gear_hover):
#                 size_group None
#                 add "system qm blue prefs"
#                 action [
#                     ShowMenu("preferences", standalone=True),
#                     SetField(tooltip, 'value', tooltip.default)
#                 ]
#                 hovered tooltip.Action(_("{#qm}Settings"))
#         button:
#             add "system qm blue auto"
#             action Preference("auto-forward", "toggle")
#             hovered tooltip.Action(_("{#qm}Auto Forward"))
#         button:
#             add "system qm blue skip"
#             action Skip()
#             hovered tooltip.Action(_("{#qm}Skip"))
#         button:
#             add "system qm blue encyclopedia"
#             action [
#                 ShowMenu("encyclopedia", standalone=True),
#                 SetField(tooltip, 'value', tooltip.default)
#             ]
#             hovered tooltip.Action(_("{#qm}Encyclopedia"))
#         button:
#             add "system qm blue save"
#             action [
#                 ShowMenu("save", standalone=True),
#                 SetField(tooltip, 'value', tooltip.default)
#             ]
#             hovered tooltip.Action(_("{#qm}Save"))
#         button:
#             add "system qm blue load"
#             action [
#                 ShowMenu("load", standalone=True),
#                 SetField(tooltip, 'value', tooltip.default)
#             ]
#             hovered tooltip.Action(_("{#qm}Load"))

#     if tooltip.value:
#         transform at qm_sh:
#             label "[tooltip.value!t]" style "qm_label"
#     mousearea style "qm_mousearea":
#         hovered SetScreenVariable("state", "hover")
#         unhovered SetScreenVariable("state", "idle")


screen quick_menu():
    default hover_action = Show(
        "_quick_menu",
        bar_trans=qm_bar_in,
        caption_trans=qm_caption_out,
        panel_trans=qm_panel_in)
    default unhover_action = Show(
        "_quick_menu",
        bar_trans=qm_bar_out,
        caption_trans=qm_caption_in,
        panel_trans=qm_panel_out)
    default hover_action0 = Show(
        "_quick_menu",
        bar_trans=qm_bar_in0,
        caption_trans=qm_caption_out0,
        panel_trans=qm_panel_in0)
    default unhover_action0 = Show(
        "_quick_menu",
        bar_trans=qm_bar_out0,
        caption_trans=qm_caption_in0,
        panel_trans=qm_panel_out0)
    
    on "show" action hover_action
    # on "show" action If(
    #     in_quick_menu_area(),
    #     true=hover_action0,
    #     false=unhover_action0)
    # on "replace" action If(
    #     in_quick_menu_area(),
    #     true=hover_action0,
    #     false=unhover_action0)
    # on "update" action If(
    #     in_quick_menu_area(),
    #     true=hover_action0,
    #     false=unhover_action0)

    on "hide" action Hide("_quick_menu")

    # mousearea:
    #     area (scale(0), scale(1080 - 105), scale(1920), scale(105))
    #     hovered hover_action
    #     unhovered unhover_action


screen _quick_menu(bar_trans, caption_trans, panel_trans):
    style_prefix "qm"

    label _("{#qm}MENU") id "qm_caption":
        at caption_trans
    frame:
        xcenter 0.5
        yalign 1.0
        ymargin scale(5)

        has hbox:
            spacing scale(24)
        
        if not persistent.in_battle:
            add At("9i/interface/quickmenu/qm bar.png", imagescale(4320)) at bar_trans(1):
                xalign 1.0
                ycenter 0.5

        hbox id "qm_hbox":
            at panel_trans
            xcenter 0.5
            ycenter 0.5
            spacing scale(44)
            
            if not persistent.in_battle:
                textbutton _("{#qm}Auto"):
                    action Preference("auto-forward", "toggle")
                textbutton _("{#qm}Auto-Skip"):
                    action Skip()
                textbutton _("{#qm}QSave"):
                    action QuickSave()
                textbutton _("{#qm}QLoad"):
                    action QuickLoad()
                textbutton _("{#qm}Encyclopedia"):
                    action ShowMenu("encyclopedia", standalone=True)
                textbutton _("{#qm}Settings"):
                    action ShowMenu("preferences", standalone=True)
                textbutton _("{#qm}Title"):
                    if not persistent._in_replay:
                        action [MainMenu(confirm=True)]
                    else:
                        action Show("navigation")
            textbutton _("{#qm}Menu"):
                if not persistent.in_battle:
                    action Show("navigation")
                else:
                    action [Play("battle_music", "Open_Menu"), Return("cancel")]
        
        if not persistent.in_battle:
            add At("9i/interface/quickmenu/qm bar.png", imagescale(4320)) at bar_trans(-1):
                xalign 0.0
                ycenter 0.5
                xzoom -1


screen actual_quick_menu:
    timer 0.1 action Hide("actual_quick_menu")

init python:
    def in_quick_menu_area():
        x, y = renpy.get_mouse_pos()
        return y >= scale(1080 - 105)

init:
    transform qm_bar_in(s):
        alpha 0.5

        easein 0.2 xoffset scale(0)
    transform qm_bar_in0(s):
        alpha 0.5
        xoffset scale(0)
    transform qm_bar_out(s):
        alpha 0.5

        easein 0.2 xoffset scale(style.qm_bar.xoffset * s)
    transform qm_bar_out0(s):
        alpha 0.5
        xoffset scale(style.qm_bar.xoffset * s)
    transform qm_caption_in:
        linear 0.2 alpha 0.5
    transform qm_caption_in0:
        alpha 0.5
    transform qm_caption_out:
        linear 0.1 alpha 0.0
    transform qm_caption_out0:
        alpha 0.0
    transform qm_panel_in:

        easein 0.2 yoffset scale(0)
    transform qm_panel_in0:
        yoffset scale(0)
    transform qm_panel_out:

        easeout 0.2 yoffset scale(74)
    transform qm_panel_out0:
        yoffset scale(74)

    style qm_text is text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(24)
        color "#8b8a86"
    translate None style qm_text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(24)

    style qm_bar is default xoffset scale(630)
    translate None style qm_bar xoffset scale(630)
    style qm_frame is default:
        xcenter 0.5
        yalign 1.0
        ymargin scale(5)
    style qm_hbox is hbox:
        ysize scale(45)
    style qm_label is default:
        xcenter 0.5
        ycenter scale(1054)
    style qm_label_text is qm_text
    style qm_button is default:
        ycenter 0.5
        xmargin scale(-6)
        ymargin scale(-6)
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"
    style qm_button_text is qm_text:
        insensitive_color "#595956"
        outlines [(scale(6.0), "#0000")]
        hover_outlines [
            (scale(6.0), "#00baff02"),
            (scale(5.0), "#00baff05"),
            (scale(4.0), "#00baff0a"),
            (scale(3.0), "#00baff15"),
            (scale(2.0), "#00baff1c"),
            (scale(1.0), "#00baff23")
        ]
        hover_color "#fff"
        selected_outlines [
            (scale(6.0), "#00baff01"),
            (scale(5.0), "#00baff03"),
            (scale(4.0), "#00baff06"),
            (scale(3.0), "#00baff11"),
            (scale(2.0), "#00baff08"),
            (scale(1.0), "#00baff1f")
        ]
        selected_color "#c5c4c2"
        selected_hover_outlines [
            (scale(6.0), "#00baff02"),
            (scale(5.0), "#00baff05"),
            (scale(4.0), "#00baff0a"),
            (scale(3.0), "#00baff15"),
            (scale(2.0), "#00baff1c"),
            (scale(1.0), "#00baff23")
        ]
        selected_hover_color "#fff"


# init python:
#     @renpy.pure
#     class ResetTooltip(renpy.ui.Action):
#         def __init__(self, tooltip):
#             self.tooltip = tooltip
        
#         def __call__(self):
#             self.tooltip.value = self.tooltip.default

#     @renpy.pure
#     def get_qm_tf(state, default=None, **tfs):
#         return tfs.get(state, default)
# init:
#     transform qm_default:
#         xanchor scale(154)
#     transform qm_idle:
#         subpixel True
#         easein_cubic 0.5 qm_default
#     transform qm_hover:
#         subpixel True
#         easein_cubic 0.5 xanchor int(scale(423.5))

#     transform qm_sh:
#         on show:
#             qm_show
#         on hide:
#             qm_hide
#     transform qm_show:
#         xanchor 0.0
#         easein_cubic 0.5 qm_default
#     transform qm_hide:
#         linear 0.3 alpha 0.0

#     transform qm_gear_idle:
#         subpixel True
#         rotate 0.0
#         linear 8.0 rotate 360.0
#         repeat
#     transform qm_gear_hover:
#         subpixel True
#         easein 0.75 rotate 0.0

#     define qm_dissolve = Dissolve(0.1, alpha=True)

#     image system qm blue prefs:
#         xcenter 0.5
#         ycenter 0.5
#         "9i/interface/quickmenu/blue prefs.png"
#         imagescale(1080)
#         on idle:
#             "9i/interface/quickmenu/blue prefs.png" with qm_dissolve
#         on hover:
#             "9i/interface/quickmenu/blue prefs hover.png" with qm_dissolve
#     image system qm blue auto:
#         xcenter 0.5
#         ycenter 0.5
#         imagescale(1080)
#         "9i/interface/quickmenu/blue auto.png"
#         on idle:
#             "9i/interface/quickmenu/blue auto.png" with qm_dissolve
#         on hover:
#             "9i/interface/quickmenu/blue auto hover.png" with qm_dissolve
#     image system qm blue skip:
#         xcenter 0.5
#         ycenter 0.5
#         imagescale(1080)
#         "9i/interface/quickmenu/blue skip.png"
#         on idle:
#             "9i/interface/quickmenu/blue skip.png" with qm_dissolve
#         on hover:
#             "9i/interface/quickmenu/blue skip hover.png" with qm_dissolve
#     image system qm blue encyclopedia:
#         xcenter 0.5
#         ycenter 0.5
#         imagescale(1080)
#         "9i/interface/quickmenu/blue ency.png"
#         on idle:
#             "9i/interface/quickmenu/blue ency.png" with qm_dissolve
#         on hover:
#             "9i/interface/quickmenu/blue ency hover.png" with qm_dissolve
#     image system qm blue save:
#         xcenter 0.5
#         ycenter 0.5
#         imagescale(1080)
#         "9i/interface/quickmenu/blue save.png"
#         on idle:
#             "9i/interface/quickmenu/blue save.png" with qm_dissolve
#         on hover:
#             "9i/interface/quickmenu/blue save hover.png" with qm_dissolve
#     image system qm blue load:
#         xcenter 0.5
#         ycenter 0.5
#         imagescale(1080)
#         "9i/interface/quickmenu/blue load.png"
#         on idle:
#             "9i/interface/quickmenu/blue load.png" with qm_dissolve
#         on hover:
#             "9i/interface/quickmenu/blue load hover.png" with qm_dissolve
#     image system qm blue aero:
#         xcenter 0.5
#         ycenter 0.5
#         imagescale(2160)
#         "9i/interface/quickmenu/blue aero.png"
#         on idle:
#             "9i/interface/quickmenu/blue aero.png" with qm_dissolve
#         on hover:
#             "9i/interface/quickmenu/blue aero hover.png" with qm_dissolve

#     style qm_text is text:
#         font "9i/fonts/浪漫雅圆.ttf"
#         size scale(32)
#         color "#dff0f9"
#         outlines [
#             (scale(1.0), "#000"),
#             (scale(1.0), "#000", scale(1.5), scale(1.5))
#         ]
#     style qm_mousearea is default:
#         xalign 1.0
#         yalign 1.0
#         xsize 0.2
#         ysize 0.2
#     style qm_frame is default:
#         xalign 1.0
#         ycenter 0.96
#         xsize int(scale(423.5))
#         ysize scale(53)
#         right_padding scale(9)
#         background imagescale(1080)("9i/interface/quickmenu/blue frame.png")
#     style qm_hbox is hbox:
#         xalign 1.0
#         ycenter 0.5
#     style qm_label is qm_frame:
#         ycenter 0.90
#         right_padding scale(15)
#     style qm_label_text is qm_text:
#         xalign 1.0
#         ycenter 0.5
#     style qm_button is default:
#         xcenter 0.5
#         ycenter 0.5
#         size_group "qm"
#         activate_sound "9i/interface/click1.ogg"
#         hover_sound "9i/interface/click2.ogg"
        
# translate None strings:
#     old "{#qm}Settings"
#     new "设定"

#     old "{#qm}Auto Forward"
#     new "自动阅读"

#     old "{#qm}Skip"
#     new "跳过"

#     old "{#qm}Encyclopedia"
#     new "图鉴"

#     old "{#qm}Save"
#     new "保存"

#     old "{#qm}Load"
#     new "载入"


translate None strings:
    old "{#qm}MENU"
    new "功能菜单"

    old "{#qm}Auto"
    new "自动阅读"

    old "{#qm}Auto-Skip"
    new "跳过"

    old "{#qm}QSave"
    new "快速保存"

    old "{#qm}QLoad"
    new "快速加载"

    old "{#qm}Encyclopedia"
    new "图鉴"

    old "{#qm}Settings"
    new "设置"

    old "{#qm}Title"
    new "返回主界面"

    old "{#qm}Menu"
    new "菜单"


init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def qm_on_interact():
        """Per-interact callback. Shows or hides the quick menu.
        """
        if suppress_overlay and not persistent.in_battle:
            renpy.hide_screen('quick_menu')
        else:
            renpy.show_screen('quick_menu')

    renpy.config.start_interact_callbacks.append(qm_on_interact)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
