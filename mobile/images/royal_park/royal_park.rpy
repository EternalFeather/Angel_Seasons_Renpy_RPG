define set royal_park:
    path 'images/royal_park'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.18)
    piece mid onlayer b2:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.18)
    piece front onlayer m1:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
