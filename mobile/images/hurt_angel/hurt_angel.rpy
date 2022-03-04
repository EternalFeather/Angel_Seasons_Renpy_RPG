define set hurt_angel:
    path 'images/hurt_angel'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        xcenter 0.5
        ycenter 0.5
        zoom scale(0.59)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
