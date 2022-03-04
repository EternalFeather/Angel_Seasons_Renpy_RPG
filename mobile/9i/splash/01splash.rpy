image disclaimer:
    "9i/splash/disclaimer.png"
    imagescale(1080)
    alpha 0
    linear 1.0 alpha 1
    1.
    linear 1.0 alpha 0

image disclaimer_2:
    "9i/splash/disclaimer_2.png"
    alpha 0
    linear 1.0 alpha 1
    1.
    linear 1.0 alpha 0

image click_continue:
    xcenter 0.5
    yalign 0.95
    linear 0.1 alpha 0.0
    "9i/splash/click_continue.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

label splashscreen:
    scene black
    with Pause(1.0)

    show disclaimer
    with Pause(3.0)

    show disclaimer_2
    with Pause(3.0)

    $ mouse_visible = False

    scene black
    $ renpy.music.play("9i/splash/sp_logo_reveal.mp3", synchro_start='movie')
    show movie onlayer master
    play movie "9i/splash/sp_logo_reveal.mp4"
    pause 12.5 hard

    scene black
    $ mouse_visible = True
    stop music fadeout 1.0
    stop movie
    hide movie
    pause 1.0 hard
    
    python:
        fake_updater.update()

    jump prologue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
