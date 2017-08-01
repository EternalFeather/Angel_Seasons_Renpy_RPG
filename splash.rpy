

init -3 python:
    if persistent.prologue_shown is None:
        persistent.prologue_shown = False

init:

    define slowdissolve = Dissolve(1.0)

    image splash1 = "ui/bg_001.png"
    image splash2 = "ui/bg_002.png"
    image splash3 = "ui/a_top_s1.bmp"
    image bg prologue = "ui/bg_prologue.png"
    image bg black = "#000000"

label splashscreen:

    scene black
    with Pause(1.0)

    show splash1 with slowdissolve
    with Pause(3.5)
    hide splash1 with slowdissolve
    $ renpy.pause(0.5, hard=True)
    show splash3 with slowdissolve
    with Pause(3.5)
    hide splash3 with slowdissolve
    $ renpy.pause(0.5, hard=True)
    show splash2 with slowdissolve
    with Pause(3.5)
    $ renpy.pause(0.5, hard=True)
    hide splash2 with slowdissolve
    pause 1



    # call movie6 from _call_movie6
    # show bg black with Dissolve(2.0)
    # with Pause(0.5)


    call movie5 from _call_movie5
    show bg black with Dissolve(2.0)
    with Pause(0.5)


    call movie1 from _call_movie1
    scene bg black



    return

