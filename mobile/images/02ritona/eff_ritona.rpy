define set 02ritona:
    path 'images/02ritona'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer m1:
        xcenter 0.5
        yalign 1.0
        zoom scale(0.5)
    piece front onlayer f1:
        pos (0.93, 0.85)
        anchor (1.0, 1.0)
        zoom scale(0.40)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
