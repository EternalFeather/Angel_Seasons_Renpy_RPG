define set backend_yinghua:
    path 'images/场景转换'
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
        zoom scale(1.38)
    piece mask_up onlayer b2:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.18)
    piece mask_down onlayer b2:
        subpixel True
        xcenter 0.5
        ycenter 0.5
        zoom scale(1.18)

define set backend_xuejian:
    path 'images/场景转换'
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
        zoom scale(1.38)

image backend_date01 = "images/场景转换/date/date one.png"
image backend_date02 = "images/场景转换/date/date two.png"
image backend_date03 = "images/场景转换/date/date three.png"
image backend_date04 = "images/场景转换/date/date four.png"
image backend_date05 = "images/场景转换/date/date five.png"
image backend_date06 = "images/场景转换/date/date five_after.png"
image backend_date07 = "images/场景转换/date/date six.png"
image backend_date08 = "images/场景转换/date/date seven.png"
image backend_date09 = "images/场景转换/date/date eight.png"
image backend_date10 = "images/场景转换/date/date nine_front.png"
image backend_date11 = "images/场景转换/date/date nine.png"
image backend_date12 = "images/场景转换/date/date ten.png"
image backend_date13 = "images/场景转换/date/date eleven.png"
image backend_date14 = "images/场景转换/date/date twelve.png"
image backend_date15 = "images/场景转换/date/date end.png"

image backend_date201 = "images/场景转换/date2/day01.png"
image backend_date202 = "images/场景转换/date2/day02.png"
image backend_date203 = "images/场景转换/date2/day03.png"
image backend_date204 = "images/场景转换/date2/day04.png"
image backend_date205 = "images/场景转换/date2/day05.png"
image backend_date206 = "images/场景转换/date2/day06.png"
image backend_date207 = "images/场景转换/date2/day07.png"
image backend_date208 = "images/场景转换/date2/day08.png"
image backend_date209 = "images/场景转换/date2/day09.png"
image backend_date210 = "images/场景转换/date2/day10.png"
image backend_date211 = "images/场景转换/date2/day11.png"
image backend_date212 = "images/场景转换/date2/day12.png"
image backend_date213 = "images/场景转换/date2/day13.png"
image backend_date214 = "images/场景转换/date2/day14.png"
image backend_date215 = "images/场景转换/date2/day15.png"
image backend_date216 = "images/场景转换/date2/day16.png"
image backend_date217 = "images/场景转换/date2/day17.png"
image backend_date218 = "images/场景转换/date2/day18.png"
image backend_date219 = "images/场景转换/date2/day19.png"
image backend_date220 = "images/场景转换/date2/day20.png"
image backend_date221 = "images/场景转换/date2/day21.png"
image backend_date222 = "images/场景转换/date2/day22.png"
image backend_date223 = "images/场景转换/date2/day23.png"
image backend_date224 = "images/场景转换/date2/day24.png"
image backend_date225 = "images/场景转换/date2/day25.png"
image backend_date226 = "images/场景转换/date2/day26.png"
image backend_date227 = "images/场景转换/date2/day27.png"
image backend_date228 = "images/场景转换/date2/day28.png"
image backend_date229 = "images/场景转换/date2/day29.png"

image backend_bg01 = "images/场景转换/bg spring.jpg"
image backend_bg02 = "images/场景转换/bg summer.jpg"
image backend_bg03 = "images/场景转换/bg autumn.jpg"
image backend_bg04 = "images/场景转换/bg winter.jpg"

transform backend_date:
    alpha 0.0 xalign 0.5 yalign 0.9
    easein 3.0 alpha 1.0 yalign 0.85

transform backend_date2:
    alpha 0.0 xalign 0.5 yalign 0.65
    easein 3.0 alpha 1.0 yalign 0.5

transform backend_bg:
    zoom 1.38
    xcenter 0.5
    ycenter 0.5
    easein 5.0 zoom 1.18
