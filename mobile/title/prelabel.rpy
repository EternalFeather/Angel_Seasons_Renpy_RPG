
label prelabel:
    $ mouse_visible = False
    $ suppress_overlay = True
    $ _skipping = renpy.seen_audio("video/second_ed.mp4")
    $ config.skipping = None

    # $ renpy.audio.audio.set_force_stop("music", True)
    stop music fadeout 4.0
    scene black 
    with Dissolve(8.0)
    pause 3.0 hard

    show movie onlayer master
    play movie "video/second_ed.mp4" noloop
    $ renpy.music.play("video/second_ed.mp3", synchro_start='movie', loop=False)
    pause 292.0 hard
    stop movie
    hide movie
    stop music fadeout 1.0

    if renpy.loadable('title/credits.txt'):
        pause 0.5 hard
        show screen tlthanks
        pause 3.0
        hide screen tlthanks
        pause 1.0
        python hide:
            language_sections = parse_monologue('title/credits.txt')
            for section in language_sections:
                language_id = section.options
                image_path = 'title/tlcredits/' + language_id + '.png'
                team_members = [line[1][0] for line in section.lines]
                
                renpy.show_screen(
                    'tlcredits',
                    image_path=image_path,
                    text_body=team_members)
                renpy.transition(slowdissolve)
                renpy.pause(5.0)
                renpy.hide_screen('tlcredits')
                renpy.transition(slowdissolve)
                renpy.pause(1.5)

    # $ renpy.audio.audio.set_force_stop("music", False)

    # $ _skipping = renpy.seen_audio("video/third_op.mp4")
    # stop music fadeout 4.0
    # scene black 
    # with Dissolve(2.0)
    # pause 1.0 hard

    # show movie onlayer master
    # play movie "video/third_op.mp4" noloop
    # $ renpy.music.play("video/third_op.mp3", synchro_start='movie', loop=False)
    # show screen recap
    # pause 143.0 hard
    # stop movie
    # stop music fadeout 1.0

    $ _skipping = True
    $ mouse_visible = True
    $ suppress_overlay = False
    hide screen recap
    hide movie


screen tlcredits(image_path, text_body):
    add image_path at imagescale(1105) xalign 1.0 ycenter 0.5
    vbox style "tlcredits_vbox":
        for line in text_body:
            text "[line]" style "tlcredits_body_text"


screen tlthanks():
    text "Our thanks to the communities for bringing this game so many resources all over the world." at tlcredits_inter style "tlcredits_thanks_text"


screen recap():
    style_prefix "recap"
    transform at recap_block_show(start=135.375, end=140.5):
        text _("四季轮转，希望不灭\n新的冒险也即将展开——") style "recap_block_text"
    transform at recap_subtitle_show(start=140.694, end=142.584):
        text _("让我们一起祈祷最终的胜利吧。") style "recap_subtitle_text"


init:
    transform tlcredits_inter:
        on show:
            alpha 0
            linear 1.0 alpha 1
        on replace:
            alpha 0
            linear 1.0 alpha 1
        on replaced:
            linear 1.0 alpha 0
        on hide:
            linear 1.0 alpha 0
    style tlcredits_vbox is vbox xpos 0.25 spacing scale(8) ycenter 0.5
    style tlcredits_thanks_text is text:
        xmaximum scale(960) xcenter 0.5 text_align 0.5 ycenter 0.5
        font "9i/fonts/FOT-ModeMinBStd-B.otf"
        size scale(24)
        line_spacing scale(9)
        color "#fff"
    style tlcredits_body_text is text:
        xcenter 0.5 text_align 0.5
        font "9i/fonts/FOT-ModeMinBStd-B.otf"
        size scale(30)
        color "#fff"

    transform recap_subtitle_show(start, end):
        alpha 0
        start
        alpha 1
        (end - start)
        alpha 0
    transform recap_block_show(start, end):
        alpha 0
        start
        linear 0.5 alpha 1
        (end - start - 1.0)
        linear 0.5 alpha 0
    style recap_subtitle_text is text:
        xcenter 0.5
        ycenter 0.85
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(28)
    translate None style recap_subtitle_text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(28)
    style recap_block_text is text:
        xcenter 0.6
        ycenter 0.5
        xmaximum scale(810)
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(27)
        color "#fff"
        outlines [
            (absolute(scale(1.5)), "#0008"),
            (absolute(scale(3.0)), "#0004"),
            (absolute(scale(4.5)), "#0002"),
            (absolute(scale(6.0)), "#0001")
        ]
        text_align 0.5
        line_leading scale(0)
        line_spacing scale(0)
        line_overlap_split scale(0)
    translate None style recap_block_text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(27)
        line_leading scale(6)
        line_spacing scale(6)
        line_overlap_split scale(0)
