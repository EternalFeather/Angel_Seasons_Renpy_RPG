define set ritroom:
    path 'images/ritroom'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2050)
        layer_move('m1', 2000)
        layer_move('m2', 1800)
        layer_move('f1', 1575)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.20)
    piece windchime onlayer b1:
        subpixel True
        xcenter 0.1
        ycenter 0.38
        zoom scale(1.20)
    piece midl onlayer b2:
        subpixel True
        xcenter -0.28
        ycenter 0.8
        zoom scale(0.99)
    piece midc onlayer m1:
        subpixel True
        xcenter 0.3
        ycenter 0.79
        zoom scale(1.10)
    piece midr onlayer b2:
        subpixel True
        xcenter 1.02
        ycenter 0.85
        zoom scale(0.54)
    piece midt onlayer f2:
        subpixel True
        xcenter 0.5
        ycenter 0.33
        zoom scale(0.70)
    piece eggs onlayer m1 optional:
        subpixel True
        xcenter 0.29
        ypos 0.78
        yanchor 1.0
    piece eggscover onlayer m1 optional:
        subpixel True
        xcenter 0.29
        ypos 0.78
        yanchor 1.0
    piece front1 onlayer f1:
        subpixel True
        xcenter -0.45
        ycenter 0.48
        zoom scale(0.90)
    piece front2 onlayer f1:
        subpixel True
        xcenter -0.21
        ycenter 0.79
        zoom scale(0.97)
    piece front3 onlayer f1:
        subpixel True
        xcenter 0.61
        ycenter 0.44
        zoom scale(0.97)
    piece front6 onlayer f1:
        subpixel True
        xcenter 0.73
        ycenter 0.18
        zoom scale(0.80)
    piece front4 onlayer f1:
        subpixel True
        xcenter 1.12
        ycenter 0.84
        zoom scale(0.97)
    piece front5 onlayer f1:
        subpixel True
        xcenter 1.43
        ycenter 0.48
        zoom scale(0.90)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
