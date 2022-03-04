label prologue:

    $ style.default.font = "9i/fonts/浪漫雅圆.ttf"
    $ style.default.language = "eastasian"

    $ renpy.pause(2.0, hard=True)

# 第一次进入游戏
if persistent.now_story is None or persistent.now_story == "序章":
    $ persistent.now_story = "序章"
    $ persistent.stories = set()
    jump prologue_main
elif persistent.break_title:
    return

menu:
    
    "我想要重新寻觅新的轮回。(新手推荐：帮助构建世界观)":

        menu:

            "轮回过后一切记忆都清除哦 QAQ（攻略痕迹清空，慎重！）":

                $ persistent._clear(progress=True)
                $ persistent.now_story = None
                $ persistent.stories = set()
                $ persistent.encyclopedia_article_unlocks = set()
                $ persistent.encyclopedia_section_unlocks = set()
                jump splashscreen

            "我氪金了，我是带着记忆闯荡的龙傲天（保留攻略痕迹从头来过）":

                jump prologue_main

    "我想要重温旧的记忆。（回归者 or 老玩家）":

        return

label prologue_main:
    bookmark
    $ save_name = _("Prologue")
    $ mouse_visible = False
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = True
    $ _skipping = renpy.seen_audio("video/prologue01.mp4")
    scene black
    pause 3.0 hard
    $ renpy.music.play(audio.prologue01, synchro_start='movie', loop=False)
    show movie onlayer master
    play movie "video/prologue01.mp4"
    play ambience2 "video/prologue01.mp3"
    
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.25)
        ease_cubic 4.5 yzoom scale(1.0)
    $ flcam.move(0, 0, 0)

    pause 44.5 hard
    stop ambience2 fadeout 1.0
    $ mouse_visible = True
    $ suppress_overlay = False
    $ _skipping = True
    
    stop music fadeout 1.0
    play ambience1 ocean_ambience fadein 1.0
    play ambience2 ["<silence 1.0>", ship_engine_ambience] fadein 1.0
    scene black
    stop movie

    show set 00prologue-cut01
    show 00prologue-cut01-imza:
        "images/prologue/cut01/imza pulse.png" with slowerdissolve
        3.0
        "images/prologue/cut01/imza.png" with slowerdissolve
        4.0
        repeat
    show cinemascope onlayer texture
    $ flcam.move(-3400, -2300, 900)
    
    show black onlayer texture
    show movie onlayer texture
    play movie "video/prologue02.mp4" noloop
    $ renpy.music.play("video/prologue02.mp3", synchro_start='movie', loop=False)
    queue movie "video/a loop.mp4" loop
    pause 3.5 hard
    window mode cinema
    stop music fadeout 1.0
    show screen investigation_popup(investigation.preg1)
    "神秘人·A" "{rb}发射{/rb}{rt}Flash Shoot{/rt}！"
    hide screen investigation_popup
    play movie "video/prologue03.mp4" noloop
    $ renpy.music.play("video/prologue03.mp3", synchro_start='movie', loop=False)
    pause 2.5 hard
    stop movie
    hide movie
    stop music fadeout 1.0
    pause 2.0 hard
    hide black onlayer texture
    $ flcam.move(0, scale(-1200), 0, duration=0.75, warper='easein_cubic')
    window mode cinema
    "幸存船员" "这是...什么！？"
    scene black
    show set 00prologue-cut02
    show kail 00prologue-cut02 b1 f10 onlayer m1
    show cinemascope onlayer texture
    $ flcam.move(250, -4077, 100)
    $ flcam.move(160, -4077, 100, duration=0.75)
    window mode cinema
    "幸存船员" "这么远的距离..."
    window mode cinema
    "幸存船员" "轻易地\n就贯穿了身体！？"
    $ renpy.music.play(audio.prologue03_blank, fadeout=1.0, synchro_start='movie')
    $ renpy.music.play(audio.prologue03, fadein=1.0, channel='sound', synchro_start='movie')
    scene black
    show set 00prologue-cut03
    show sm 00prologue-cut03 b1 f0 onlayer m1
    show sf 00prologue-cut03 b1 f0 onlayer m2
    show cinemascope onlayer texture
    show black onlayer texture
    show movie onlayer texture
    play movie "video/prologue04.mp4" noloop
    $ renpy.music.play("video/prologue04.mp3", synchro_start='movie', loop=False)
    pause 2.0 hard
    window mode cinema
    "幸存船员" "这样下去要被干掉了！" nointeract
    pause 3.125 hard 
    pause 5.333 hard 
    window mode cinema
    "幸存船员" "啊啊啊啊啊！" nointeract
    pause 1.334 hard 
    $ renpy.music.set_volume(0, channel='ambience1')
    $ renpy.music.set_volume(0, channel='ambience2')
    pause 7.958 hard 
    $ renpy.music.set_volume(1, delay=1.0, channel='ambience1')
    $ renpy.music.set_volume(1, delay=1.0, channel='ambience2')
    pause 9.242 hard 
    stop movie
    hide movie
    stop music fadeout 1.0
    hide black onlayer texture
    $ flcam.move(14538, -2266, 100)
    $ flcam.move(7038, -2366, 300, duration=1.0)
    window mode cinema
    show sf 00prologue-cut03 b1 f1 s
    "神秘人·A" "什、什么人！？"
    show sf 00prologue-cut03 b1 f0 s
    $ flcam.move(-666, -4766, 600, duration=1.5)
    window mode cinema
    show sm 00prologue-cut03 b1 f2
    "神秘人·B" "那是！"
    window mode cinema
    show screen investigation_popup(investigation.preg2)
    "神秘人·B" "{encyclopedia=elfin}{rb}灵继者{/rb}{rt}elfin{/rt}{/encyclopedia}！！"
    pause 0.5 hard
    hide screen investigation_popup
    scene black
    show set 00prolgue-cut05 b
    show cinemascope onlayer texture
    $ flcam.move(-3600, -2700, 1600)
    $ renpy.transition(dissolve)
    $ flcam.move(8000, -2640, 1600, duration=2.5, warper='ease_cubic')
    pause 2.0 hard
    show set 00prologue-cut04
    show sc 00prologue-cut04 b1 f2 s onlayer b2
    show sb 00prologue-cut04 b1 f0 s onlayer m1
    show sa 00prologue-cut04 b1 f0 s onlayer m2
    show cinemascope onlayer texture
    $ flcam.move(0, 0, 0)
    with dissolve
    window mode cinema
    "神秘人·C" "！！！！！"
    $ flcam.move(3993, -566, 600, duration=1.5)
    window mode cinema
    show sb 00prologue-cut04 b1 f1 s
    "神秘人·D" "第一次看到真正的灵继者，那刚刚他用的就是{encyclopedia=rune}{rb}灵纹{/rb}{rt}rune{/rt}{/encyclopedia}吗..."
    show sb 00prologue-cut04 b1 f0 s
    $ flcam.move(3593, -866, 1400, duration=1.5)
    window mode cinema
    "神秘人首领" "..."
    $ flcam.move(-3200, 1200, 600, duration=1.0)
    window mode cinema
    show sa 00prologue-cut04 b1 f1 s
    "神秘人·C" "难以置信。"
    window mode cinema
    "神秘人·C" "使用仪器增幅的全力一击竟被徒手化解，这就是实力上的差距吗。"
    window mode cinema
    "神秘人·C" "这可怎么办啊，如此一来我们的任务就要失败了！"
    show sa 00prologue-cut04 b1 f0 s
    pause 0.5 hard
    scene black
    show set 00prologue-cut03
    show sm 00prologue-cut03 b1 f0 s onlayer m1
    show sf 00prologue-cut03 b1 f0 s onlayer m2
    show cinemascope onlayer texture
    $ flcam.move(-606, -5366, 600)
    $ flcam.move(-666, -5366, 600, duration=0.5)
    window mode cinema
    show sm 00prologue-cut03 b1 f1 s
    "神秘人·B" "可、可恶。"
    window mode cinema
    "神秘人·B" "要撤退吗？"
    show sm 00prologue-cut03 b1 f0 s
    $ flcam.move(7038, -2366, 300, duration=1.0)
    window mode cinema
    show sf 00prologue-cut03 b1 f1 s
    "神秘人·A" "可这样一来我们日后的行踪不就暴露了吗。"
    window mode cinema
    show sf 00prologue-cut03 b1 f2 s
    "神秘人·A" "事到如今，无论如何也要在这里解决掉他们！"
    show sf 00prologue-cut03 b1 f0 s
    $ flcam.move(-666, -5366, 600, duration=1.0)
    window mode cinema
    show sm 00prologue-cut03 b1 f1 s
    "神秘人·B" "可是你也看到了，刚刚的攻击..."
    window mode cinema
    show sm 00prologue-cut03 b1 f2 s
    "神秘人·B" "我们根本不是他的对手！"
    show sm 00prologue-cut03 b1 f0
    $ flcam.move(7038, -2366, 300, duration=1.0)
    window mode cinema
    show sf 00prologue-cut03 b1 f2 s
    "神秘人·A" "那就只好采取最终手段了！"
    window mode cinema
    "神秘人·A" "即使是同归于尽..."
    window mode cinema
    "神秘人·A" "也绝不能辜负那位大人！"
    show sf 00prologue-cut03 b1 f0 s
    scene black
    show set 00prologue-cut04
    show sc 00prologue-cut04 b1 f2 s onlayer b2
    show sb 00prologue-cut04 b1 f0 s onlayer m1
    show sa 00prologue-cut04 b2 f0 s onlayer m2
    show cinemascope onlayer texture
    $ flcam.move(0, 0, 0)
    window mode cinema
    show sa 00prologue-cut04 b2 f1 s
    "神秘人·C" "同归于尽...你是说！"
    show sa 00prologue-cut04 b2 f0 s
    $ flcam.move(3993, -566, 600, duration=1.5)
    window mode cinema
    show sb 00prologue-cut04 b1 f1 s
    "神秘人·D" "眼下也只有这个办法了。"
    window mode cinema
    "神秘人·D" "能够对{rb}灵继者{/rb}{rt}elfin{/rt}造成伤害的，也就只有“那个”了！"
    show sb 00prologue-cut04 b1 f0 s
    $ flcam.move(-4718, 588, 600, duration=1.5)
    window mode cinema
    show sa 00prologue-cut04 b2 f1 s
    "神秘人·C" "看来...今天要交代在这里了吗。"
    show sa 00prologue-cut04 b2 f0 s
    window mode cinema
    show sb 00prologue-cut04 b1 f1 s
    "神秘人·C" "不过能够亲手消灭{rb}灵继者{/rb}{rt}elfin{/rt}也算值了！"
    show sb 00prologue-cut04 b1 f0 s
    $ flcam.move(3562, -1233, 1600, duration=1.5)
    window mode cinema
    show sc 00prologue-cut04 b1 f3 s
    "神秘人首领" "哈哈哈哈，那位大人一定会为我们感到骄傲的！"
    scene black
    show set 00prologue-cut06 bb
    show 00prologue-cut06-bg:
        ypos 1.27
    hide 00prologue-cut06-kail
    show eiyus 00prologue-cut07 b1 f0 onlayer m1:
        xpos 0.38
        ypos 1.02
    show kail 00prologue-cut08 b1a fa1 fc0 s1 onlayer m2:
        xpos 0.81
        ypos 1.52
        rotate 12
    show cinemascope onlayer texture
    $ flcam.layer_move('m1', 2200)
    $ flcam.layer_move('m2', 2200)
    $ flcam.move(0, 0, 0)
    window mode cinema
    show eiyus 00prologue-cut07 b1 f1
    "灵继者" "认识这些家伙吗？"
    show eiyus 00prologue-cut07 b1 f0
    window mode cinema
    show kail 00prologue-cut08 b1a fa3 fc2 s1
    "幸存船员" "完、完全不认识。"
    show kail 00prologue-cut08 b1a fa3 fc00 s1
    window mode cinema
    show eiyus 00prologue-cut07 b1 f1
    "灵继者" "看来这艘船上有他们想要找的东西。"
    show eiyus 00prologue-cut07 b1 f0
    window mode cinema
    show kail 00prologue-cut08 b2a fa1 fblank s1
    "幸存船员" "这种事我才不知道，我只想活下去而已！"
    window mode cinema
    "幸存船员" "没有任何的交涉就直接发起攻击，害得那么多无辜的人丧命！"
    show kail 00prologue-cut08 b1a fa1 fc0 s1
    window mode cinema
    show eiyus 00prologue-cut07 b1 f1
    "灵继者" "在这些家伙眼中没有人是“无辜”的。"
    show eiyus 00prologue-cut07 b1 f0
    window mode cinema
    show kail 00prologue-cut08 b1a fa2 fc2 s1
    "幸存船员" "那...就一定要置我们于死地吗？"
    window mode cinema
    show eiyus 00prologue-cut07 b1 f1
    "灵继者" "他们都是一群渴望战争的{encyclopedia=yjt}祟{/encyclopedia}，是没有感情的杀戮者。"
    show eiyus 00prologue-cut07 b1 f0
    window mode cinema
    show kail 00prologue-cut08 b1a fa1 fc2 s2
    "幸存船员" "祟？战乱？你在说些什么啊..."
    show kail 00prologue-cut08 b1a fa1 fc0 s2
    window mode cinema
    show eiyus 00prologue-cut07 b2 fa1 fc11
    "灵继者" "赶紧逃命去吧年轻人。"
    window mode cinema
    "灵继者" "另外也是为了你着想，还请千万不要向其他人说起今天发生的事情。"
    show eiyus 00prologue-cut07 b2 fa2 fc10
    window mode cinema
    show kail 00prologue-cut08 b1a fa3 fc2 s2
    "幸存船员" "我、我知道了！"
    pause 0.5 hard
    scene black
    show set 00prologue-cut03
    show sm 00prologue-cut03 b1 f0 onlayer m1
    show sf 00prologue-cut03 b1 f0 onlayer m2
    show cinemascope onlayer texture
    $ flcam.move(0, scale(-3400), 0)
    window mode cinema
    show sm 00prologue-cut03 b1 f2
    "神秘人·A" "想跑？！恐怕你们是没有这个机会了！"
    window mode cinema
    show sm 00prologue-cut03 b1 f1
    "神秘人·A" "就是现在，解除能量限制！"
    window mode cinema
    show sf 00prologue-cut03 b1 f2
    "神秘人·B" "检测到异常的能量波动，马上就要控制不住了！"
    window mode cinema
    show sf 00prologue-cut03 b1 f1
    "神秘人·A" "让那些自命不凡的灵继者们见识一下我们的厉害！"
    window mode cinema
    show sf 00prologue-cut03 b1 f2
    "神秘人·B" "发射！"
    window mode cinema
    show sm 00prologue-cut03 b1 f2
    "神秘人·A" "发射！"
    $ flcam.move(4500, -3400, 0, duration=1.0, warper='easeout')
    pause 0.3 hard
    scene black
    show set 00prologue-cut04
    show sc 00prologue-cut04 b1 f2 s onlayer b2
    show sb 00prologue-cut04 b1 f0 s onlayer m1
    show sa 00prologue-cut04 b1 f0 s onlayer m2
    show cinemascope onlayer texture
    $ flcam.move(scale(-3000), 0, 300)
    $ flcam.move(0, 0, 300, duration=1.0, warper='easein_cubic')
    with dissolve
    pause 0.2 hard
    window mode cinema
    show sc 00prologue-cut04 b1 f3 s
    "神秘人首领" "哈哈哈哈！"
    $ flcam.move(3568, -911, 1400, duration=1.0)
    window mode cinema
    show sc 00prologue-cut04 b1 f4 s
    "神秘人首领" "All High！{encyclopedia=mel}Koliya{/encyclopedia}！"
    $ flcam.move(0, 0, 0, duration=1.0)
    window mode cinema
    show sa 00prologue-cut04 b1 f1 s
    "一同" "All High！Koliya！！！"
    pause 0.5 hard
    stop music fadeout 2.0
    stop ambience1 fadeout 1.0
    stop ambience2 fadeout 1.0
    scene black
    with slowerdissolve
    pause 2.0 hard
    scene movie onlayer texture at basicfade
    play movie "video/prologue05.mp4"
    $ renpy.music.play("video/prologue05.mp3", synchro_start='movie', loop=False)
    $ flcam.move(0, 0, 0)
    pause 14.0 hard
    scene black
    stop movie
    hide movie
    stop music fadeout 1.0
    pause 6.0 hard
    play ambience1 ocean_waves_ambience fadein 3.0
    scene black
    $ flcam.move(-2000, -13200, 200, duration=0.0, warper='linear'),
    pause 6.0 hard
    show set 00prologue-cut09
    show cinemascope onlayer texture
    $ flcam.move(-1000, 2000, 300, duration=9.0, warper='ease')
    $ renpy.transition(slowerdissolve)
    pause 11.0 hard
    stop ambience1 fadeout 1.0
    scene black
    with slowerdissolve
    pause 3.0 hard

label prologue_main.monologue:
    bookmark
    $ save_name = _("Prologue")
    play music black_box_prologue fadein 5.0
    scene set only Europe_city winter night
    show sepiagrain onlayer texture
    $ flcam.move(-1200, 0, 200)
    $ flcam.move(1200, 0, 200, duration=12.0, warper='ease_quad')
    with slowdissolve
    pause 0.5 hard
    nvl clear
    nvl_narrator "　发生在北欧某海域的船只袭击事件迅速引起了异能者协会的重视。\n"
    nvl_narrator "　面对突如其来的袭击，此时工会的众人都无法再置身事外。"
    nvl_narrator "　欧洲联邦最具影响力的灵继者也在袭击过后失去了踪迹。"
    nvl_narrator "　现场没有留下任何炮弹的金属痕迹，一切的矛头全都指向了灵继者。面对能够将一艘货轮瞬间粉碎的力量，工会也是不得已向全世界的灵继者们发起了求助。\n"
    nvl_narrator "　希望能够借助他们的力量帮忙找到幕后黑手。"
    scene set only jungle_room spring night
    show sepiagrain onlayer texture
    $ flcam.move(-5550, -750, 1700)
    $ flcam.move(0, 0, 0, duration=12.0, warper='ease_quad')
    $ renpy.transition(slowdissolve, layer='b1')
    $ renpy.transition(slowdissolve, layer='m1')
    nvl_narrator "{w=1.0}　北美、日本、中华联邦、埃及联邦等几个世界知名组织机构也纷纷响应。"
    nvl_narrator "　在这前所未有的惨烈代价面前，在场所有人都表达了自己的悲愤\n然而真正愿意为此付诸行动的势力却是少之又少。"
    nvl clear
    nvl_narrator "　离开宿主超过一定的时间，契约另一方的生命体——天使的存在也会逐渐消亡。"
    nvl_narrator "　由于缺乏相应的线索，目前能够获取的情报也只有对现场残留痕迹的勘察、分析报告而已。"
    nvl_narrator "　残骸表面燃烧着的淡紫色火焰，犹如来自地狱的邪魅踏足后留下的焦土一般。"
    nvl_narrator "　仿佛还能从中听到受害者们撕心裂肺的哀嚎与悲鸣。"
    scene set only hurt_angel
    show sepiagrain onlayer texture
    $ flcam.move(0, 0, 0)
    $ flcam.move(0, 0, 300, duration=12.0, warper='easeout_quad')
    $ renpy.transition(slowdissolve, layer='b1')
    $ renpy.transition(slowdissolve, layer='m1')
    $ renpy.transition(slowdissolve, layer='f2')
    nvl clear
    nvl_narrator "{w=1.0}　灵继者和天使之间存在着“共感”。"
    nvl_narrator "　因此有的人提出从身为天使一方的{encyclopedia=fl}弗兰{/encyclopedia}意识中提取出情报。"
    nvl_narrator "　然而所有的尝试都以失败告终。"
    nvl_narrator "　不仅如此，这一举动也近乎耗尽了少女体内残存的最后一丝力量。"
    scene set only royal_park night
    show sepiagrain onlayer texture
    $ flcam.move(2775, 0, 300)
    $ flcam.move(-1950, 0, 0, duration=12.0, warper='ease_quad')
    $ renpy.transition(slowdissolve, layer='b1')
    $ renpy.transition(slowdissolve, layer='b2')
    $ renpy.transition(slowdissolve, layer='m1')
    nvl clear
    nvl_narrator "{w=1.0}　与此同时，世界各地也陆续传来了灵继者被袭的消息。"
    nvl_narrator "　由于手法过于类似而让人不由得相信这些袭击是来自同一帮人所为。"
    nvl_narrator "　终于，所有的人都坐不住了。"
    nvl_narrator "　一场战争已然打响。"
    nvl clear
    nvl_narrator "　面对未知的强敌，世界各地的灵继者们第一次团结在了一起。"
    nvl_narrator "　无论发色、血统、年龄、出身、信仰，所有人全都聚集一堂，共同讨伐这个所谓的幕后组织。"
    nvl_narrator "　经过缜密的部署作战，以及有越来越多的“祟”被击败，那名“幕后黑手”的身份也逐渐浮出了水面。\n"
    nvl_narrator "  然而令大家都没有想到的是，对方的真实身份竟然是一位没有契约者的天使。"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard

    $ _skipping = renpy.seen_audio("video/prologue06.mp4")
    show movie onlayer texture
    play movie "video/prologue06.mp4" loop
    pause 1.0 hard
    nvl clear
    $ _window_animation = 'in'
    nvl_narrator "  在她压倒性的实力面前，联军节节败退，损失惨重。"
    nvl_narrator "  战火席卷了欧洲、美洲、亚洲等绝大部分城市和岛屿，灵力碰撞所产生的灵能脉冲划破天际，日夜不休。\n"
    nvl_narrator "  在联盟军万众一心的攻势之下，终于迎来了第一封捷报，暴走的天使被镇压了。"
    nvl_narrator "　也许是战争的影响过于惨痛，即便是迎来了胜利凯旋归来的众人脸上依然没有一丝笑容。"
    pause 1.0 hard
    $ window_animate_outro()
    scene black
    stop movie
    hide movie
    pause 0.5 hard
    $ _skipping = True
    
    scene set only kingroom
    show sepiagrain onlayer texture
    $ flcam.move(-100, -2250, 600)
    $ flcam.move(300, 800, 200, duration=12.0, warper='ease_quad')
    nvl clear
    nvl_narrator "{w=1.0}　至此事件得到了平息。"
    nvl_narrator "　但是其留下的阴影却始终无法磨灭。"
    nvl_narrator "　就在此时，几乎所有的灵继者们做了一个共同的决定。"
    nvl_narrator "　那就是成立一个统一的管理和执行部门，专门对抗这类突发事件。"
    nvl clear
    nvl_narrator "  来自世界各地的灵继者们签署了一份协议。"
    nvl_narrator "　一个由灵继者组成的联盟就此诞生。\n"
    nvl_narrator "　囊括了巫女、阴阳师、武士、忍者、牧师、骑士、神官等一系列体质于一身。"
    nvl_narrator "　分治于世界各地的每一个角落。"
    nvl_narrator "　在保障灵继者人身安全的同时，也负责调查和镇压那些企图伤害他人、滥用灵纹的不法分子。"
    stop music fadeout 3.0
    nvl clear
    pcenter "――――名为希望、守护世间羁绊的{encyclopedia=xtg}星天宫{/encyclopedia}就此成立。"
    pause 1.0 hard

    $ mouse_visible = False
    $ suppress_overlay = True
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 2.0
    $ _skipping = renpy.seen_audio("video/start_info.mp4")
    $ config.skipping = None
    scene black
    show movie onlayer texture
    play movie "video/start_info.mp4" noloop
    $ renpy.music.play("video/start_info.mp3", synchro_start='movie', loop=False)
    pause 5.845 hard
    pause 1.0 hard
    nvl clear
    $ _window_animation = 'in'
    pcenter "就和当初设想的一样，星天宫的势力不断壮大。" nointeract
    pause 4.396 hard
    $ window_animate_outro()
    pause 5.897 hard
    nvl clear
    $ _window_animation = 'in'
    pcenter "毕竟换作是谁也不愿再看到，那些重要的人从眼前消失了。" nointeract
    pause 4.878 hard
    nvl clear
    $ _window_animation = 'continue'
    pcenter "这份逝去羁绊的痛苦，除了拥有共感的天使以外\n又有谁能够真正体会呢..." nointeract
    pause 4.0 hard
    $ window_animate_outro()
    pause 68.184 hard
    stop movie
    hide movie
    stop music fadeout 1.0
    $ _skipping = True
    $ mouse_visible = True
    $ suppress_overlay = False
    pause 3.0
    
    $ persistent.stories.add("序章")
    if "夏之章" not in persistent.stories:
        $ persistent.now_story = "夏之章"
    
    return
