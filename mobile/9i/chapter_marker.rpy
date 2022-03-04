screen chapter_marker(index="", title=""):
    layer "texture"
    timer 4.0 action Hide("chapter_marker")
    vbox style_prefix "cm" at cm_interact:
        label "[index!t]" style "cm_index_label"
        label "[title!t]" style "cm_title_label"

transform cm_interact:
    on show:
        subpixel True alpha 0 yoffset scale(21)
        easein 0.5 alpha 1 yoffset scale(0)
    on hide:
        linear 2.0 alpha 0

style cm_vbox is vbox xpos 0.08 ypos 0.08
style cm_text is text:
    kerning scale(1.5) font "9i/fonts/浪漫雅圆.ttf"
    color "#000"
    outlines [
        (scale(9.0), "#ffffff01"),
        (scale(8.0), "#ffffff03"),
        (scale(7.0), "#ffffff07"),
        (scale(6.0), "#ffffff0f"),
        (scale(5.0), "#ffffff13"),
        (scale(4.0), "#ffffff17"),
        (scale(3.0), "#ffffff1f"),
        (scale(2.0), "#ffffff2b"),
        (scale(1.0), "#ffffff3f")
    ]
style cm_index_label is default
style cm_index_label_text is cm_text:
    italic True size scale(24)
style cm_title_label is default
style cm_title_label_text is cm_text:
    size scale(36)
    
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
