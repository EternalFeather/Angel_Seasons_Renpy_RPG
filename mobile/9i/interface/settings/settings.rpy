screen preferences(standalone=False):
    tag menu
    modal True

    default focused_item = None
    default prev_focused_item = None
    default focus_ypos = {
        item: (
            (style.settings_vbox.ypos
                + idx * (style.settings_vbox.spacing + scale(46)))
            if item != 'return'
            else style.settings_return_button.ypos)
        for idx, item in enumerate(
            [
                'display',
                'skip',
                'after choices',
                'text speed',
                'auto-forward time',
                'music volume',
                'sound volume',
                'update',
                'return'
            ])
    }

    use aerolinguistics()
    add "9i/interface/settings/bg.jpg" at imagescale(1080), settings_bg_inter
    if focused_item:
        add Solid("#fff", xsize=scale(10), ysize=scale(46)):
            if prev_focused_item:
                at settings_cursor_move(ypos=focus_ypos[focused_item])
            else:
                at settings_cursor_show(ypos=focus_ypos[focused_item])
    vbox style_prefix "settings":

        button style "default" hovered SettingsFocusItem("display"):
            at settings_controls_inter(idx=0)
            action NullAction()
            sensitive (not renpy.mobile)
            has hbox
            if focused_item == "display":
                style_prefix "settings_focus"

            if not renpy.mobile:
                label _("{#settings}Display")
                hbox style "settings_checkbox_hbox":
                    textbutton _("{#settings}Window") style_suffix "checkbox":
                        action Preference("display", "window")
                        hovered SettingsFocusItem("display")
                        selected (not _preferences.fullscreen)
                    textbutton _("{#settings}Fullscreen") style_suffix "checkbox":
                        action Preference("display", "fullscreen")
                        hovered SettingsFocusItem("display")
            else:
                label ""
        # button style "default" hovered SettingsFocusItem("language"):
        #     at settings_controls_inter(idx=1)
        #     action NullAction()
        #     has hbox
            # if focused_item == "language":
            #     style_prefix "settings_focus"
            # if renpy.has_screen("aerowheel"):
            #     $ language = aero.get_name(_preferences.language) or '日本語'
            #     label _("{#settings}Language")
            #     frame style "settings_checkbox_frame":
            #         has fixed fit_first "vertical"
            #         textbutton "[language]" style_suffix "checkbox":
            #             action Show("aerowheel")
            #             hovered SettingsFocusItem("language")
            #             selected True
            # else:
            #     textbutton ""
        button style "default" hovered SettingsFocusItem("skip"):
            at settings_controls_inter(idx=2)
            action NullAction()
            has hbox
            if focused_item == "skip":
                style_prefix "settings_focus"
            label _("{#settings}Message Skip")
            frame style "settings_checkbox_frame":
                has fixed fit_first True
                hbox style "settings_checkbox_hbox":
                    textbutton _("{#settings}Read") style_suffix "checkbox":
                        action Preference("skip", "seen")
                        hovered SettingsFocusItem("skip")
                        size_group "settings_checkboxes"
                    textbutton _("{#settings}All") style_suffix "checkbox":
                        action Preference("skip", "all")
                        hovered SettingsFocusItem("skip")
                        size_group "settings_checkboxes"
        button style "default" hovered SettingsFocusItem("after choices"):
            at settings_controls_inter(idx=3)
            action NullAction()
            has hbox
            if focused_item == "after choices":
                style_prefix "settings_focus"
            label _("{#settings}After Choices")
            frame style "settings_checkbox_frame":
                has fixed fit_first True
                hbox style "settings_checkbox_hbox":
                    textbutton _("{#settings}Keep Skipping") style_suffix "checkbox":
                        action Preference("after choices", "skip")
                        hovered SettingsFocusItem("after choices")
                        size_group "settings_checkboxes"
                    textbutton _("{#settings}Stop Skipping") style_suffix "checkbox":
                        action Preference("after choices", "stop")
                        hovered SettingsFocusItem("after choices")
                        size_group "settings_checkboxes"
        button style "default" hovered SettingsFocusItem("text speed"):
            at settings_controls_inter(idx=4)
            action NullAction()
            has hbox
            if focused_item == "text speed":
                style_prefix "settings_focus"
            label _("{#settings}Text Speed")
            bar value Preference("text speed"):
                hovered SettingsFocusItem("text speed")
        button style "default" hovered SettingsFocusItem("auto-forward time"):
            at settings_controls_inter(idx=5)
            action NullAction()
            has hbox
            if focused_item == "auto-forward time":
                style_prefix "settings_focus"
            label _("{#settings}Auto Message Speed")
            bar value Preference("auto-forward time"):
                hovered SettingsFocusItem("auto-forward time")
        button style "default" hovered SettingsFocusItem("music volume"):
            at settings_controls_inter(idx=6)
            action NullAction()
            has hbox
            if focused_item == "music volume":
                style_prefix "settings_focus"
            label _("{#settings}Music Volume")
            bar value Preference("music volume"):
                hovered SettingsFocusItem("music volume")
        button style "default" hovered SettingsFocusItem("sound volume"):
            at settings_controls_inter(idx=7)
            action NullAction()
            has hbox
            if focused_item == "sound volume":
                style_prefix "settings_focus"
            label _("{#settings}Effects Volume")
            bar value Preference("sound volume"):
                hovered SettingsFocusItem("sound volume")


    textbutton "Return" style "settings_return_button":
        action MenuReturn()
        hovered SettingsFocusItem("return")
        unhovered SettingsFocusItem(None)

    key "game_menu" action [MenuReturn(), Play('sound', '9i/interface/click1.ogg')]
    label _("{#settings}SETTINGS") style "caption_label" at caption_inter

init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    @renpy.pure
    class SettingsFocusItem(renpy.ui.Action):
        def __init__(self, name):
            self.name = name
        
        def __call__(self):
            scope = renpy.current_screen().scope
            if scope['focused_item'] == self.name: return
            
            scope['prev_focused_item'] = scope['focused_item']
            scope['focused_item'] = self.name

            renpy.play('9i/interface/click2.ogg')
            
            renpy.restart_interaction()

init:
    transform settings_bg_inter:
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
    transform settings_flourish_inter:
        xalign 1.0
        on show:
            alpha 0
            xpos 1.05
            parallel:
                linear 0.3 alpha 1
            parallel:
                subpixel True
                easein_cubic 0.5 xpos 1.0
        on replace:
            alpha 0
            xpos 1.05
            parallel:
                linear 0.3 alpha 1
            parallel:
                subpixel True
                easein_cubic 0.5 xpos 1.0
    transform settings_controls_inter(idx):
        alpha 0
        xoffset scale(-30)
        yoffset scale(-45)
        zoom 1.05
        (0.2 + 0.03 * idx)
        parallel:
            linear 0.1 alpha 1
        parallel:
            subpixel True
            easein_cubic 0.2 xoffset scale(0) yoffset scale(0) zoom 1.0
    transform settings_cursor_show(ypos):
        xpos style.settings_vbox.xpos
        ypos ypos
        alpha 0
        linear 0.1 alpha 1
    transform settings_cursor_move(ypos):
        subpixel True
        xpos style.settings_vbox.xpos
        parallel:
            easeout_quad 0.1 ypos ypos
        parallel:
            easein_quad 0.05 alpha 0.25
            easeout_cubic 0.05 alpha 1
    style settings_text is text:
        font "9i/fonts/FOT-ChiaroStd-B.otf"
        size scale(42)
        outlines [(1.0, "#0009", scale(1.0), scale(1.0))]
    style settings_vbox is vbox:
        xpos int(scale(149.5))
        ypos scale(213)
        spacing scale(23)
    style settings_button is default:
        yminimum scale(46)
        left_padding scale(19)
        # hover_background Solid("#fff")
        hover_background imagescale(1080)(
            Image(
                "9i/interface/settings/button hover.png",
                xcenter=0.5,
                ycenter=0.6))
    style settings_button_text is settings_text:
        ycenter 0.5
        color "#fff"
        hover_color "#000"
        outlines [(1.5, "#000", scale(1.0), scale(1.0))]
    style settings_return_button is settings_button:
        xpos style.settings_vbox.xpos
        ypos scale(932)
        right_padding scale(56)
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"
    style settings_return_button_text is settings_button_text:
        color "#ffffff"
        # hover_color "#000"
        outlines [(1.5, "#000", scale(0.0), scale(0.0))]
    style settings_checkbox_frame is default:
        size_group "settings_buttons"
    style settings_checkbox_hbox is hbox:
        spacing scale(30)
    style settings_fixed is fixed:
        xcenter 0.5
        ycenter 0.5
    style settings_focus_fixed is settings_fixed
    style settings_label is settings_button:
        xminimum scale(678)
        hover_background None
    style settings_label_text is settings_button_text
    style settings_focus_label is settings_label
    style settings_focus_label_text is settings_label_text:
        color "#fff"
        outlines [(0.0, "#050b29", scale(1.5), scale(1.5))]
    style settings_checkbox is default:
        xminimum int(scale(221.5))
        ysize scale(46)
        selected_background imagescale(1080)(
            Image(
                "9i/interface/settings/button selected.png",
                xcenter=0.5,
                ycenter=0.6))
        activate_sound "9i/interface/click3.ogg"
    style settings_checkbox_text is settings_label_text:
        xcenter 0.5
        ycenter 0.6
        outlines [(scale(1.5), "#000")]
        selected_color style.settings_focus_label.color
    style settings_focus_checkbox is settings_checkbox:
        hover_background imagescale(1080)(
            Image(
                "9i/interface/settings/button hover.png",
                xcenter=0.5,
                ycenter=0.6))
    style settings_focus_checkbox_text is settings_checkbox_text:
        color style.settings_focus_label_text.color
        selected_idle_outlines [
            (scale(5.0), "#0000"),
            (0.0, "#050b29", scale(1.5), scale(1.5))
        ]
        hover_outlines [
            (scale(5.0), "#c4a14e0f"),
            (scale(4.0), "#c4a14e17"),
            (scale(3.0), "#c4a14e1f"),
            (scale(2.0), "#c4a14e27"),
            (scale(1.0), "#c4a14e33"),
            (scale(0.5), "#c4a14e3f"),
            (0.0, "#564c34", scale(1.5), scale(1.5))
        ]
    style settings_slider is default:
        ycenter 0.5
        xsize scale(494)
        ysize scale(46)
        bar_resizing True
        left_bar Frame(
            imagescale(1080)("9i/interface/settings/bar left.png"),
            left=scale(6),
            right=scale(12))
        right_bar Frame(
            imagescale(1080)("9i/interface/settings/bar right.png"),
            right=scale(6))
        thumb imagescale(1080)("9i/interface/settings/bar thumb.png")
        thumb_offset scale(23)
        hover_sound "9i/interface/click2.ogg"
    style settings_focus_slider is settings_slider:
        left_bar Frame(
            imagescale(1080)("9i/interface/settings/bar left hover.png"),
            left=scale(6),
            right=scale(12))
        right_bar Frame(
            imagescale(1080)("9i/interface/settings/bar right hover.png"),
            right=scale(6))
        thumb imagescale(1080)("9i/interface/settings/bar thumb hover.png")
        hover_sound None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
