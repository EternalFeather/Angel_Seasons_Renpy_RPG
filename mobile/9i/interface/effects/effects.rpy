init python:
    def callflash_play(tf, st, at):
        renpy.play('9i/interface/call.ogg', channel='audio')

image callflash:
    function callflash_play
    Solid("#fff")
    alpha 0.5
    linear 0.325 alpha 0.1
    alpha 0.3
    linear 0.675 alpha 0.0

image cinemascope = Fixed(
    Solid("#000", xsize=scale(1920), ysize=int(scale(131.5))),
    Solid("#000", xsize=scale(1920), ysize=int(scale(131.5)), yalign=1.0),
    xcenter=0.5,
    ycenter=0.5)

image dreamglass1 = Movie(channel="movie", play="9i/interface/dream_glass1.mp4")
image dreamglass2 = Movie(channel="movie", play="9i/interface/dream_glass2.mp4")

init -1:
    transform mobpos(x, y, zoom):
        xpos absolute((x - 25) * 0.5 * zoom - 1920 * (zoom * 0.5 - 0.5))
        ypos absolute((y - 25) * 0.5 * zoom - 1080 * (zoom * 0.5 - 0.5))
        zoom zoom

image hintarrow:
    "itemsign.png"
    subpixel True
    zoom scale(0.375)
    xanchor 0.5
    yanchor 1.0
    parallel:
        yanchor 1.5
        easeout_quad 0.5 yanchor 1.0
        easein_quad 0.5 yanchor 1.5
        repeat
    # parallel:
    #     6.0
    #     linear 1.5 alpha 0

image hintarrow2:
    "itemsign.png"
    subpixel True
    zoom scale(0.375)
    xanchor 0.5
    yanchor 1.0
    yzoom -1
    parallel:
        yanchor 1.0
        easeout_quad 0.5 yanchor 1.5
        easein_quad 0.5 yanchor 1.0
        repeat
    # parallel:
    #     6.0
    #     linear 1.5 alpha 0

image sepiagrain:
    size (renpy.config.screen_width, renpy.config.screen_height)
    additive 0.75
    block:
        "9i/interface/effects/sepiagrain0.png"
        0.1
        "9i/interface/effects/sepiagrain1.png"
        0.1
        "9i/interface/effects/sepiagrain2.png"
        0.1
        "9i/interface/effects/sepiagrain3.png"
        0.1
        "9i/interface/effects/sepiagrain4.png"
        0.1
        repeat

image wflash:
    Solid("#fff")
    alpha 0.5
    linear 0.25 alpha 0.0

image white = Solid("#fff")


init python:
    renpy.music.register_channel(
        name='ambience1',
        mixer='sfx',
        loop=True,
        stop_on_mute=False,
        tight=True)
    renpy.music.register_channel(
        name='ambience2',
        mixer='sfx',
        loop=True,
        stop_on_mute=False,
        tight=True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
