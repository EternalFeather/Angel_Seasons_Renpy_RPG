define set ritfrontyard:
    path 'images/ritfrontyard'
    python:
        layer_move('b1', 3000)
        layer_move('b2', 2745)
        layer_move('m1', 2550)
        layer_move('m2', 1849)
        layer_move('f1', 1620)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.61)
    piece mid onlayer m1:
        subpixel True
        xcenter 0.5
        ypos pscale(1290)
        yanchor 1.0
        zoom scale(1.37)
    piece frontl onlayer f2:
        subpixel True
        xpos 0.15
        xanchor 0.0
        ypos 0.85
        yanchor 1.0
        zoom scale(0.7)
    piece frontr onlayer f2:
        subpixel True
        xpos 0.85
        xanchor 1.0
        ypos 0.85
        yanchor 1.0
        zoom scale(0.7)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
