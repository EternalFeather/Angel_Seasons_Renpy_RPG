screen encyclopedia(article=None, section=None, standalone=False):
    tag menu
    modal True

    default open_article = article
    default open_section = section

    default play_action = [
        Play(channel="movie", file="9i/interface/encyclopedia/bg.mp4", loop=False),
        Play(channel="audio", file="9i/interface/flag_roll_down.ogg")
    ]
    default stop_action = Stop(channel="movie")
    on "show" action play_action
    on "replace" action play_action
    on "replaced" action stop_action
    on "hide" action stop_action

    python:
        root_sections = [
            node
            for node in encyclopedia.sections["root"].nodes
            if isinstance(node, encyclopedia.Section)
        ]

    use aerolinguistics()
    add "9i/interface/encyclopedia/bg.png" at imagescale(1080)
    # add "movie"
    frame style_prefix "ency_menu" at ency_menu_inter:
        has fixed
        vbox:
            for node in encyclopedia.sections["root"].nodes:
                textbutton "[node.title]":
                    if isinstance(node, encyclopedia.Section):
                        action encyclopedia.ShowSection(node.id)
                    else:
                        action encyclopedia.ShowArticle(node.id)
        textbutton "Return" style "ency_menu_return_button":
            action MenuReturn()
            keysym "game_menu"

    key "game_menu" action [MenuReturn(), Play('sound', '9i/interface/click1.ogg')]

    use encyclopedia_section(section=open_section)
    use encyclopedia_article(article=open_article, section=open_section)
    label _("{#ency}INTRODUCTION") style "caption_label" at caption_inter
init:
    transform ency_menu_inter:
        alpha 0
        0.3
        linear 0.2 alpha 1
    transform ency_mask_show:
        alpha 0
        0.4
        linear 0.2 alpha 1

    style ency_menu_frame is default:
        xpos int(scale(20.5))
        ypos scale(-14)
        xsize scale(378)
        ysize scale(1159.5)

    style ency_menu_vbox is vbox:
        xcenter 0.5
        ypos scale(216)
        spacing scale(-6)
    style ency_menu_button is default:
        xsize scale(280)
        yminimum int(scale(62.5))
        hover_background Frame("9i/interface/encyclopedia/menu button hover.png")
        selected_background Frame("9i/interface/encyclopedia/menu button hover.png")
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"
    style ency_menu_button_text is text:
        xcenter 0.5
        ycenter 0.5
        text_align 0.5
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(33)

        line_leading scale(9)
        line_spacing scale(-9)
        color "#fff"
        hover_color "#96f4ff"
        outlines [(scale(3.0), "#050b29", scale(0.0), scale(1.5))]
    style ency_menu_return_button is ency_menu_button:
        xcenter 0.5
        ycenter scale(780)
    style ency_menu_return_button_text is ency_menu_button_text


screen encyclopedia_section(section):
    python:
        section_instance = encyclopedia.sections.get(section)
        articles = (
            [
                node
                for node in section_instance.nodes
                if isinstance(node, encyclopedia.Article)
            ]
            if section is not None
            else [])

    frame style_prefix "ency_section_border" at ency_mask_show:
        has fixed
        add LiveTile(
            imagescale(1080)("9i/interface/encyclopedia/section lines.png")):
            ypos scale(42)
        viewport id "ency_section_viewport" mousewheel True style_prefix "ency_section":
            vbox:
                if section_instance is not None:
                    for article in articles:
                        if article.visible and article.unlocked:
                            textbutton "[article.title]":
                                action encyclopedia.ShowArticle(article.id)
                        elif article.visible:
                            textbutton _("{#ency}???")
    if len(articles) > 15:
        vbar value YScrollValue("ency_section_viewport") style "ency_section_vscrollbar"

init:
    style ency_section_border_frame is default:
        xpos scale(348)
        ypos int(scale(88.5))
        xsize int(scale(649.5))
        ysize scale(896)
    style ency_section_border_fixed is fixed:
        xpos int(scale(56.5))
        ypos scale(117)
        xsize scale(410)
        ysize int(scale(693.5))
    style ency_section_vbox is vbox:
        xpos scale(22)
        spacing scale(10)
    style ency_section_button is default:
        xsize scale(375)
        ysize int(scale(36.5))
        hover_background imagescale(1080)(
            "9i/interface/encyclopedia/section button hover.png")
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click2.ogg"
    style ency_section_button_text is text:
        ycenter 0.5
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(25)

        line_leading scale(9)
        line_spacing scale(-9)
        color "#341c0b"
    style ency_section_vscrollbar is default:
        xpos scale(783)
        ypos scale(335)
        xsize scale(24)
        ysize scale(546)
        bar_invert True
        bar_vertical True
        base_bar Frame(
            imagescale(1080)("9i/interface/vscrollbar base.png"),
            top=scale(12))
        thumb imagescale(1080)("9i/interface/vscrollbar thumb.png")
        thumb_offset scale(66)
        top_gutter scale(66)
        bottom_gutter scale(66)
        unscrollable "hide"


screen encyclopedia_article(article, section):
    python:
        article_instance = encyclopedia.articles.get(article)

    frame style_prefix "ency_article" at ency_mask_show:
        vbox:
            if article_instance is not None:
                label article_instance.title style "ency_article_title_label" at invisible
                label article_instance.subtitle style "ency_article_subtitle_label" at invisible
                viewport id "ency_article_viewport" mousewheel True:
                    has frame style_prefix "ency_article_contents"
                    vbox:
                        if len(article_instance.images) >= 1:
                            # side "c l r" style_prefix "ency_article_image":
                            frame style_prefix "ency_article_image":
                                has fixed
                                add article_instance.images
                        
                        if section != "cat3":
                            frame style_prefix "ency_article_text":
                                text "[article_instance.text]"
                        else:
                            frame style_prefix "ency_article_text2":
                                text "[article_instance.text]"
        add "9i/interface/encyclopedia/article mask.png" at imagescale(1080)
        vbox:
            if article_instance is not None:
                label "[article_instance.title]" style "ency_article_title_label"
                label "[article_instance.subtitle]" style "ency_article_subtitle_label"
    if article_instance is not None:
        vbar value YScrollValue("ency_article_viewport") style "ency_article_vscrollbar"


init:
    style ency_article_frame is default:
        xpos scale(812)
        ypos scale(142)
        xsize int(scale(1099.5))
        ysize int(scale(812.5))
    style ency_article_vbox is vbox:
        xpos scale(88)
        ypos int(scale(85.5))
        xsize int(scale(885.5))
        ymaximum scale(659)
        spacing scale(0)

    style ency_article_title_label is default
    style ency_article_title_label_text is text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(48)
        color "#331b0b"
        outlines [(0.0, "#c79757", scale(1.5), scale(1.5))]

    style ency_article_subtitle_label is default
    style ency_article_subtitle_label_text is text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(24)
        color "#c68f54"

    style ency_article_contents_frame is default:
        top_padding scale(15)
        bottom_padding scale(15)

    # style ency_article_image_side is side:
    #     xcenter 0.5
    style ency_article_image_frame is default:
        xcenter 0.5
        xsize scale(546)
        ysize int(scale(334.5))
        background imagescale(1080)(
            "9i/interface/encyclopedia/article image frame.png")

    style ency_article_image_fixed is fixed:
        xcenter 0.5
        ycenter 0.5
        fit_first True

    style ency_article_text_frame is default:
        xfill True
        yminimum scale(493)
        ypadding scale(6)
        background LiveTile(
            Fixed(
                imagescale(1080)(
                    Image(
                        "9i/interface/encyclopedia/article line 1.png",
                        ypos=absolute(scale(55.5)))),
                imagescale(1080)(
                    Image(
                        "9i/interface/encyclopedia/article line 2.png",
                        ypos=absolute(scale(55.5 * 2)))),
                imagescale(1080)(
                    Image(
                        "9i/interface/encyclopedia/article line 3.png",
                        ypos=absolute(scale(55.5 * 3)))),
                xsize=scale(786),
                ysize=int(scale(165))))
    
    style ency_article_text_text is text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(30)
        color "#341c0b"
        line_leading scale(12)
        line_spacing scale(12)

    style ency_article_text2_frame:
        xfill True
        yminimum scale(493)
        ypadding scale(6)
        background None

    style ency_article_text2_text is text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(30)
        color "#341c0b"
        line_leading scale(12)
        line_spacing scale(12)
        
    style ency_article_vscrollbar is default:
        xpos scale(1803)
        ypos scale(335)
        xsize scale(24)
        ysize scale(546)
        bar_invert True
        bar_vertical True
        base_bar Frame(
            imagescale(1080)("9i/interface/vscrollbar base.png"),
            top=scale(12))
        thumb imagescale(1080)("9i/interface/vscrollbar thumb.png")
        thumb_offset scale(66)
        top_gutter scale(66)
        bottom_gutter scale(66)
        unscrollable "hide"


init -999:
    define encyclopedia.hyperlink_color = "#f39700"


screen encyclopedia_popup(article):
    $ article_instance = encyclopedia.articles[article]
    default mouse_pos = renpy.get_mouse_pos()
    default align = (
        mouse_pos[0] * 1.0 / config.screen_width,
        mouse_pos[1] * 1.0 / config.screen_height
    )

    key "mousedown_1" action [
        encyclopedia.ShowArticle(article),
        Hide("encyclopedia_popup")
        ]

    frame style_prefix "ency_quick" align align at ency_quick_inter:
        has fixed at ency_quick_inner_inter
        text article_instance.title style_suffix "heading_text"
        text article_instance.short_text

init:
    transform ency_quick_inter:
        subpixel True
        transform_anchor True
        zoom 0.5
        on show:
            alpha 0
            0.2
            parallel:
                linear 0.15 alpha 1
            parallel:
                power_in_time_warp_real 0.15 zoom 1.0
        on hide:
            alpha 1
            linear 0.2 alpha 0
    transform ency_quick_inner_inter:
        on show:
            alpha 0
            0.3
            linear 0.1 alpha 1
        on replace:
            alpha 0
            0.3
            linear 0.1 alpha 1
    style ency_quick_frame is default:
        xsize int(scale(844.5))
        ysize scale(252)
        background imagescale(1080)("9i/interface/encyclopedia/quick frame.png")
    style ency_quick_vbox is vbox:
        spacing scale(9)
    style ency_quick_text is text:
        xpos scale(60)
        ypos scale(90)
        xmaximum scale(724)
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(26)
        line_leading scale(6)
        line_spacing scale(6)
        outlines [(scale(1.5), "#37231b")]
    style ency_quick_heading_text is ency_quick_text:
        xcenter 0.5
        ycenter scale(63)
        font "9i/fonts/浪漫雅圆.ttf"
        color "#e1cc8b"
        outlines [(scale(1.5), "#0e0501")]
translate None style ency_quick_text:
    kerning scale(-2.0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
