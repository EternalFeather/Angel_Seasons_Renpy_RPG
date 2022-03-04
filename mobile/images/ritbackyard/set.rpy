define set ritbackyard:
    path 'images/ritbackyard'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2025)
        layer_move('m1', 2025)
        layer_move('m2', 1849)
        layer_move('f1', 1620)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.18)
    piece mid onlayer b2:
        subpixel True
        xcenter 0.5
        ypos 1.05
        yanchor 1.0
        zoom scale(1.08)
    piece headband onlayer b2 optional:
        subpixel True
        xcenter pscale(1150)
        ycenter pscale(380)
        zoom scale(1.08)
    piece fieldc onlayer m1:
        subpixel True
        xcenter pscale(1656)
        ypos scale(997)
        yanchor 1.0
        zoom scale(1.08)
    piece fieldl onlayer m1:
        subpixel True
        xcenter pscale(1656)
        ypos scale(997)
        yanchor 1.0
        zoom scale(1.08)
    piece fieldr onlayer m1:
        subpixel True
        xcenter scale(1656)
        ypos pscale(997)
        yanchor 1.0
        zoom scale(1.08)
    piece frontl onlayer f2:
        subpixel True
        xcenter -0.025
        xanchor 0.0
        ypos 0.85
        yanchor 1.0
        zoom scale(0.7)
    piece frontc onlayer f2:
        subpixel True
        xcenter 0.5
        ypos 0.85
        yanchor 1.0
        zoom scale(0.7)
    piece frontr onlayer f2:
        subpixel True
        xpos 1.025
        xanchor 1.0
        ypos 0.85
        yanchor 1.0
        zoom scale(0.7)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
