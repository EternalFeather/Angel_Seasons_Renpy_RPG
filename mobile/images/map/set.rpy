define set maps:
    path 'images/map'
    python:
        layer_move('b1', 2880)
        layer_move('b2', 840)
        layer_move('m1', 875)
        layer_move('m2', 990)
        layer_move('f1', 1270)
        layer_move('f2', 1440)
    piece bg onlayer b1:
        subpixel True
        xcenter 0.5
        ypos -0.3
        zoom scale(1.04)
    piece cloud4 onlayer b2:
        subpixel True
        ypos 0.4
        zoom scale(0.8)
        alpha 0.5
        block:
            subpixel True
            xpos 0.16
            linear 48.4211 xpos -0.76
            5.0
            xpos 0.76
            linear 31.5789 xpos 0.16
            repeat
    piece cloud2 onlayer m1:
        subpixel True
        ypos 0.24
        zoom scale(0.3)
        alpha 0.5
        block:
            subpixel True
            xpos 0.52
            linear 40.0 xpos 0.04
            15.0
            xpos 0.76
            linear 20.0 xpos 0.52
            repeat
    piece cloud3 onlayer m2:
        subpixel True
        ypos 0.32
        zoom scale(0.45)
        alpha 0.5
        block:
            subpixel True
            xpos -0.09
            2.5
            xpos 0.72
            linear 30.0 xpos -0.09
            repeat
    piece cloud1 onlayer f1:
        subpixel True
        ypos 0.0
        zoom scale(0.6)
        block:
            subpixel True
            xpos 0.54
            linear 40.0 xpos -0.68
            10.0
            xpos 0.84
            linear 15.0 xpos 0.54
            repeat
    piece cloud5 onlayer f2:
        subpixel True
        xpos 0.1
        ypos 0.1
        zoom scale(0.3)
        alpha 0.5
        xtile 4
        block:
            subpixel True
            xanchor 0.0
            linear 270.0 xanchor 1.0
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
