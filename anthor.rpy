
label anthor:
    
    stop music fadeout 4.0
    play sound "se_sys/fanstart.wav" 
    scene black with Dissolve(8.0)
    $ renpy.pause(3.0, hard=True)

    play music "bgm/gal.ogg" fadeout 2.0 fadein 2.0
    scene bg sel with slowerdissolve 
    show screen start

    $ ui.interact()
    # jump second01

