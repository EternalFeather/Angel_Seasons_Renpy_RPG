
init:
    $ style.default.font = u"浪漫雅圆.ttf"
    $ style.default.language = "eastasian"
init python:
    config.debug_sound = True


label start:
    
    $ _game_menu_screen = "navigation"
    stop music fadeout 4.0
    $ _window_subtitle = " - Spring"
    play sound "se_sys/start1.wav"
    $ persistent.fanwai = False
    $ persistent.gamecomplete = False
    $ persistent.clear_game = False
    $ persistent.gallery_unlocked = False
    $ persistent.encyclopedia1 = True
    scene black with Dissolve(8.0)
    $ renpy.pause(3.0)
    
    window show
    pcenter3 "那一夜，我与她定下了约定......"
    nvl clear
    pcenter3 "尽管如今这份回忆已经如同间隔着一层层污迹斑驳的玻璃一样模糊不清。"
    nvl clear
    pcenter3 "但在这数年里，这份记忆仍然存在于我的内心未曾被抹去。"
    nvl clear
    pcenter3 "因为她，我才有勇气面对未来的一切。"
    nvl clear
    pcenter3 "因为她，我才会摆脱碌碌无为的人生。"
    nvl clear
    pcenter3 "也正是因为她......"
    nvl clear
    pcenter3 "我才真正懂得了什么是珍惜。"
    nvl clear
    pcenter3 "天使在带给人们幸福的同时，自己却承受着痛苦。"
    nvl clear
    pcenter3 "当十年之后的我们回想起这一切......"
    nvl clear
    pcenter3 "心里总会忍不住去问。"
    nvl clear
    pcenter3 "如今的你是否依然能像当初那般笑容洋溢......"
    pause 2.0
    nvl clear
    window hide

    scene bg xuzhang01 at Pan((0, 2480), (0, 0), 50.0, time_warp=cgease, subpixel=True) with slowerdissolve
    play music "bgm/01.ogg" fadeout 3.0 fadein 3.0
    window show
    narrator "    多年来，我一直期待着实现约定的那一天。{p}\n\n    期待着收获存在约定之地的果实，然后前往约定的另一端。{p}\n\n    也只有这样，我才能牢牢地把羁绊握我在手中。"
    nvl clear
    narrator "    如果那时的天真，是能够把\"接吻\"误解为吻在额头上的程度。{p}\n\n    那么此刻的心情是否就不会那么沉重了呢？"
    nvl clear
    narrator "    所以数年之后当我再次回到这个熟悉的地方。{p}\n\n    与\"她\"再会，我多么希望能够是一个感人的重逢。{p}\n\n    我甚至为此准备好了眼药水，如果在\"她\"面前我真的哭了的话。{p}\n\n    就能一边冷静地说着「这只是眼药水的效果喔」一边宣泄心中沉积多年的感伤情绪。"
    nvl clear
    window hide
    $ renpy.pause(2.0, hard=True)
    scene bg xuzhang02 with dissolve:
        size (1280, 720)
        easein 20 crop (0, 0, 1280, 720)
    window show    
    narrator "    不过我虽然知道她的名字，但是却没有相应的联络方式。{p}\n\n    也许我只能够独自在街上徘徊着，一边想着这个坡道怎么还那么长之类的话题，在脑海里与过去模模糊糊的记忆进行对比。{p}\n\n    一边想象着她长大后的样子，哪怕只是身高也好......"
    nvl clear
    narrator "    但是，我比谁都清楚，她不会再回到我身边了......{p}\n\n    她是个善良诚实的孩子，正因为如此，离别时的一句「谢谢」在我看来也是一个足够刺穿心扉的词。{p}\n\n    现在想想的话，如果一切能够重来的话，说不定就能找到让大家都幸福的结局也说不定呢。"
    nvl clear
    narrator "    不过......{p}\n\n    一切都不同了呢......那时一起仰望的星空，神社前的那棵樱花树。{p}\n\n    在我离开的这几年里，已经淡去了原来的面貌......{p}\n\n    走在夜幕的街道上，熟悉的只剩下那偶尔过往车辆的嘈杂，以及路灯下渐渐拉长的身影。"
    nvl clear
    narrator "    和她在一起的时光仿佛都是一场梦，然而此刻的我多么希望那就是一场梦。{p}\n\n    因为只有这样......{p}"
    nvl clear
    pcenter "也许只要睡着了，就能够见面了吧......"
    scene black with slowerdissolve
    with Pause(0.7)
    stop music fadeout 2.0
    nvl clear
    with slowerdissolve
    window hide
    $ renpy.pause(2.0, hard=True)
    jump xuzhang



