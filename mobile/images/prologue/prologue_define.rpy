define set 00prologue-cut01:
    path 'images/prologue/cut01'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        xcenter 0.5
        ypos 1.1
        yanchor 1.0
        zoom scale(0.59)
    piece kail onlayer m1:
        xcenter scale(510)
        yalign 1.0
        zoom scale(0.52)
    piece imza onlayer f1:
        xcenter scale(1065)
        yalign 1.0
        zoom scale(0.52)

define set 00prologue-cut02:
    path 'images/prologue/cut02'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        xcenter 0.5
        ypos 1.1
        yanchor 1.0
        zoom scale(0.59)
        
define composite kail 00prologue-cut02:
    path "images/prologue/cut02/kail"
    transform:
        xcenter 0.45
        yalign 1.0
        zoom scale(0.59)
    position body
    position face:
        pos (381, 264)


define set 00prologue-cut03:
    path 'images/prologue/cut03'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        xcenter 0.5
        ypos 1.1
        yanchor 1.0
        zoom scale(1.0)

define composite sf 00prologue-cut03:
    path "images/prologue/cut03/sf"
    transform:
        xcenter 0.8
        ypos scale(1089)
        yanchor 1.0
        zoom scale(0.52)
    position body
    position etc:
        pos (923, 504)
    position face:
        pos (923, 504)

define composite sm 00prologue-cut03:
    path "images/prologue/cut03/sm"
    transform:
        xcenter 0.5
        yalign 1.0
        zoom scale(0.52)
    position body
    position face:
        pos (2965, 649)
    position etc:
        pos (2965, 649)


define set 00prologue-cut04:
    path 'images/prologue/cut04'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        xcenter 0.5
        ypos 1.1
        yanchor 1.0
        zoom scale(0.59)

define composite sa 00prologue-cut04:
    path "images/prologue/cut04/sa"
    transform:
        xcenter 0.33
        ypos 1.1
        yanchor 1.0
        xzoom -1
        zoom scale(0.5)
    position body
    position face:
        pos (912, 824)
    position etc:
        pos (810, 676)

define composite sb 00prologue-cut04:
    path "images/prologue/cut04/sb"
    transform:
        xcenter 0.8
        ypos 1.1
        yanchor 1.0
        xzoom -1
        zoom scale(0.5)
    position body
    position face:
        pos (1004, 430)
    position etc:
        pos (972, 390)

define composite sc 00prologue-cut04:
    path "images/prologue/cut04/sc"
    transform:
        xcenter 0.63
        ypos 1.1
        yanchor 1.0
        xzoom -1
        zoom scale(0.5)
    position body
    position face:
        pos (303, 236)
    position etc:
        pos (366, 220)


define set 00prologue-cut05:
    path 'images/prologue/cut05'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        xcenter 0.5
        ypos 1.2
        yanchor 1.0
        zoom scale(0.59)
    piece rain onlayer b2 optional:
        xcenter 0.5
        ypos 1.2
        yanchor 1.0
        zoom scale(0.59)


define set 00prologue-cut06:
    path 'images/prologue/cut06'
    python:
        layer_move('b1', 1849)
        layer_move('b2', 1849)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece sky onlayer b1:
        xcenter 0.5
        ypos 0.88
        yanchor 1.0
        zoom scale(0.59)
    piece bg onlayer b2:
        xcenter 0.5
        ypos 1.1
        yanchor 1.0
        zoom scale(0.59)
    piece kail onlayer m1:
        pos (scale(149), scale(825))
        yanchor 1.0
        zoom scale(0.59)
    piece rain onlayer m2 optional:
        xcenter 0.5
        ypos 1.1
        yanchor 1.0
        zoom scale(0.59)


define set 00prologue-cut07:
    path 'images/prologue/cut07'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1680)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        xcenter 0.5
        ypos 1.1
        yanchor 1.0
        zoom scale(0.59)

define composite eiyus 00prologue-cut07 b1:
    path "images/prologue/cut07/eiyus b1"
    transform:
        xcenter 0.5
        yalign 1.0
        zoom scale(0.5)
    position body

define composite eiyus 00prologue-cut07:
    path "images/prologue/cut07/eiyus b2"
    transform:
        xcenter 0.5
        yalign 1.0
        zoom scale(0.5)
    position body
    position fa:
        pos (90, 374)
    position fc:
        pos (138, 974)


define composite kail 00prologue-cut08:
    path "images/prologue/cut08/kail"
    transform:
        xcenter 0.5
        yalign 1.0
        zoom scale(0.5)
    position body
    position fa:
        pos (270, 618)
    position fc:
        pos (438, 1155)
    position etc:
        pos (717, 813)


define set 00prologue-cut09:
    path 'images/prologue/cut09'
    python:
        layer_move('b1', 2200)
        layer_move('b2', 2200)
        layer_move('m1', 1849)
        layer_move('m2', 1849)
        layer_move('f1', 1280)
        layer_move('f2', 1280)
    piece bg onlayer b1:
        xcenter 0.5
        ypos 1.1
        yanchor 1.0
        zoom scale(0.59)
