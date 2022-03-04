
image bg shufang = im.Scale("9i/interface/room/images/bg/书房.jpg", 2048, 1152)
image bg waimian2 = im.Scale("9i/interface/room/images/bg/外面2.jpg", 2048, 1152)
image QBbg = "9i/interface/room/images/QBbg.png"

image selectpublicity:
    xalign 0.5
    yalign 0.06
    linear 0.1 alpha 0.0
    "9i/interface/room/images/宣传方案.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

image up:
    linear 0.1 alpha 0.0
    "9i/interface/room/images/up.png"
    linear 1.0 alpha 1.0
    linear 0.75 alpha 1.0
    linear 0.5 alpha 0.0
    repeat

image down:
    linear 0.1 alpha 0.0
    "9i/interface/room/images/down.png"
    linear 1.0 alpha 1.0
    linear 0.75 alpha 1.0
    linear 0.5 alpha 0.0
    repeat

transform customzoom6:
    zoom 0.34
transform customzoom6_1:
    zoom 0.32
transform customzoom8:
    zoom 0.86
transform customzoom:
    zoom 0.66
transform customzoom2:
    zoom 0.47

transform sideways3:
    rotate 3

init -2 style mioutline:
    outlines [(2, "#fbe9d6")]
    
init -2 style blackoutline:
    outlines [(3, "#2D2724")]

style tilistyle:
    outlines [(2, "#fbe9d6")]

style zhibanstyle:
    size 25
    color "FEB434"
    outlines [(3, "#503327")]

style mrrw_text:
    font "9i/fonts/yangrendong.ttf"
    size 30
    color "#391C16"

define -2 gui.vslider_borders = Borders(0, 0, 0, 0)
