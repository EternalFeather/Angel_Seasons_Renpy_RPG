define set fight_cg:
    path 'images/战斗背景'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer bg:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.18)

image fight_rune2 = "images/战斗背景/bg rune2.png"
image fight_rune3 = "images/战斗背景/bg rune3.png"
