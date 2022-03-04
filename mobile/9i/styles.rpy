
init 1:
    style default:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(18)
        color "#fff"
        outlines [(scale(1.0), "#000")]
        language "unicode"
        slow_cps_multiplier 1.0

    translate None style default:
        language "japanese-strict"
        slow_cps_multiplier 0.4

init -998:
    style _default font "9i/fonts/浪漫雅圆.ttf"

    style text is default:
        size scale(15)
        outlines []

    style window is default:
        xpadding scale(15)
        ypadding scale(9)
        background BasicFrame("#1f1f1f", "#7f7f7f", "#000")
    style frame is default:
        xpadding scale(15)
        ypadding scale(9)
        background BasicFrame("#1f1f1f", "#7f7f7f", "#000")

    style label is default
    style label_text is text

    style button is default:
        xpadding scale(24)
        ypadding scale(6)
        background Solid("#0000005f")
        hover_background Solid("#5f5f5f")
        selected_idle_background Solid("#1d484d")
        selected_hover_background Solid("#3a9099")
    style button_text is text:
        xcenter 0.5
        ycenter 0.5
        insensitive_color "#7f7f7f"
        hover_color "#9cdce3"
        outlines [(scale(1.0), "#2f2f2f")]

    style checkbox_text is button_text
    style checkbox is default:
        xfill False
        left_padding scale(21)
        foreground Text(
            "□",
            style="checkbox_text",
            align=(0.0, 0.5))
        selected_foreground Text(
            "▣",
            style="checkbox_text",
            align=(0.0, 0.5))

    style hyperlink is text:
        color "#9cdce3"
        hover_underline True

    style bar is default:
        left_bar Solid("#1d484d")
        hover_left_bar Solid("#9cdce3")
        right_bar Solid("#2f2f2f")
        hover_right_bar Solid("#3f3f3f")
        thumb_offset scale(10)
        left_gutter scale(5)
        right_gutter scale(5)
        ymaximum scale(12)
    style vbar is default:
        top_bar Solid("#1d484d")
        hover_top_bar Solid("#9cdce3")
        bottom_bar Solid("#2f2f2f")
        hover_bottom_bar Solid("#3f3f3f")
        thumb_offset scale(10)
        left_gutter scale(5)
        right_gutter scale(5)
        xmaximum scale(12)
        bar_vertical True

    style scrollbar is default:
        base_bar Solid("#2f2f2f")
        hover_base_bar Solid("#3f3f3f")
        thumb Solid("#1d484d")
        hover_thumb Solid("#9cdce3")
        thumb_offset scale(10)
        left_gutter scale(5)
        right_gutter scale(5)
        unscrollable "hide"
        ymaximum scale(12)
    style vscrollbar is default:
        base_bar Solid("#2f2f2f")
        hover_base_bar Solid("#3f3f3f")
        thumb Solid("#1d484d")
        hover_thumb Solid("#9cdce3")
        thumb_offset scale(10)
        top_gutter scale(5)
        bottom_gutter scale(5)
        unscrollable "hide"
        xmaximum scale(12)
        bar_vertical True
        bar_invert True

init python:
    renpy.config.font_replacement_map[('9i/fonts/浪漫雅圆.ttf', True, False)] = ('9i/fonts/浪漫雅圆.ttf', False, False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
