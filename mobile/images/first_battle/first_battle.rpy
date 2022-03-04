define set first_battle_cg:
    path 'images/first_battle'
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
    piece queen onlayer b1 optional:
        subpixel True
        pos (-100, 0)
        zoom scale(0.58)
    piece bush onlayer b1 optional:
        subpixel True
        pos (-1100, -450)
        zoom scale(1.28)
    piece role2 onlayer b1 optional:
        subpixel True
        pos (-675, 250)
        zoom scale(0.68)
    piece rain onlayer b1 optional:
        subpixel True
        pos (550, 350)
        zoom scale(0.68)
    piece role3 onlayer b1 optional:
        subpixel True
        pos (1860, -300)
        zoom scale(0.68)
    piece partner onlayer b1 optional:
        subpixel True
        pos (-1227, -1001)
        zoom scale(1.01)


define set first_battle_cg_normal:
    path 'images/first_battle'
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
