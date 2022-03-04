define set anthor_screen:
    path 'images/anthor'
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
