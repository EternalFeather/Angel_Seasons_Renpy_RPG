
label day223:
    bookmark
    $ save_name = _("Day 223")
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play sound "sound/system/second_menu.wav"
    scene black with Dissolve(8.0)
    pause 4.0 hard

    $ renpy.block_rollback()
    $ _rollback = True

    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date222 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    with slowdissolve
    play music second_114 fadein 3.0 if_changed
    pause 2.0 hard
    scene set only home day neighbor xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031313990.ogg"
    lhx "来了吗？"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314000.ogg"
    lhx "时间正好。"
    me01 "勉强算是赶上了。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314010.ogg"
    lhx "为什么你要这么准时啊？"
    me01 "还是一如既往地搞不懂你生气的理由。"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031314020.ogg"
    lhx "......我又没在生气。"
    me01 "莫非你等很久了？"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314030.ogg"
    lhx "我也是刚刚才出来而已。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show rxl_dsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121303130.ogg"
    rxl "此乃谎言。"
    show rxl_dsf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121303140.ogg"
    rxl "立花她从一大早就在这里等凉君你了~"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314040.ogg"
    lhx "......我只是因为天气好出来晒晒太阳而已。"
    show rxl_dsf_b1 b1 b1_ga1
    play voice "voice/日向怜/121303150.ogg"
    rxl "明明之前那么怕冷的。"
    me01 "让你久等的话我道歉。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314050.ogg"
    lhx "凉君你也是按时来的，所以没有必要道歉。"
    show rxl_dsf_b1 b1 b1_sp1
    play voice "voice/日向怜/121303160.ogg"
    rxl "听说你们俩等下是要去约会？"
    show lhx_dsf_b3 b3 b3_ga2
    play voice "voice/立花希/031314060.ogg"
    lhx "......才不是，只是要去商店街逛逛而已。"
    show rxl_dsf_b1 b1 b1_n4
    play voice "voice/日向怜/121303170.ogg"
    rxl "如果是这样的话带上我一起也可以吧？"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314070.ogg"
    lhx "难得的休息日日向你也有自己的安排吧，还请以你那边为重。"
    show rxl_dsf_b1 b1 b1_h3 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/日向怜/121303180.ogg"
    rxl "我没什么特别的安排，所以就和你们一起行动好了~"
    hide rxl_dsf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_a1
    play voice "voice/立花希/031314080.ogg"
    lhx "......"
    me01 "就算你这样看着我也......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show rxl_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    me01 "既然日向同学也说了我们接下来要去约会，就请你还是别跟来了吧。"
    show rxl_dsf_b1 b1 b1_h1
    play voice "voice/日向怜/121303190.ogg"
    rxl "果然是这样的嘛~"
    hide lhx_dsf_b1 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_a1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031314090.ogg"
    lhx "才、才不是这样的，只是凉君他擅自决定的而已。"
    show rxl_dsf_b1 b1 b1_h3
    play voice "voice/日向怜/121303200.ogg"
    rxl "那带我一起去也可以吧？"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031314100.ogg"
    lhx "凉君不是说了叫你不要跟来的吗？"
    show rxl_dsf_b1 b1 b1_ga1
    play voice "voice/日向怜/121303210.ogg"
    rxl "不跟去的理由是？"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031314110.ogg"
    lhx "是因为凉君他讨厌日向。"
    hide rxl_dsf_b1 with None
    pause 0.1 hard
    show rxl_dsf_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121303220.ogg"
    rxl "我倒是挺喜欢凉君的哟~"
    show lhx_dsf_b3 b3 b3_ga1
    play voice "voice/立花希/031314120.ogg"
    lhx "你花心吗？"
    me01 "才不是！"
    hide rxl_dsf_b2
    play sound yangmu
    show rxl_dsf_b1 b1 b1_h3 onlayer m2:
        xpos 0.7
    show yangmu onlayer m2:
        xalign 0.7 yalign 0.42
    play voice "voice/日向怜/121303230.ogg"
    rxl "当然我也很喜欢立花你哟~"
    me01 "你也花心吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314130.ogg"
    lhx "这绝不可能。"
    hide yangmu
    show rxl_dsf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121303240.ogg"
    rxl "请不要为了我争执~"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314140.ogg"
    lhx "何等烦人的家伙，真想把她丢到宇宙的尽头去。"
    me01 "差不多也该出发了，日向同学可别擅自跟来啊。"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121303270.ogg"
    rxl "我们的友情也就只有这种程度吗......"
    show lhx_dsf_b3 b3 b3_ga1
    play voice "voice/立花希/031314170.ogg"
    lhx "就是这样呢~"
    hide rxl_dsf_b2
    show rxl_dsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121303280.ogg"
    rxl "这是好的意思吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314180.ogg"
    lhx "都这时候了还说什么傻话呢。"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_h2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121303290.ogg"
    rxl "祝你们二位玩的开心~"
    me01 "话说你可不要躲起来偷窥才是。"    
    show rxl_dsf_b2 b2 b2_ga1 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121303300.ogg"
    rxl "我怎么可能做那种不解风情的事情嘛~"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031314200.ogg"
    lhx "......要是不会就好。"
    show rxl_dsf_b2 b2 b2_n1
    play voice "voice/日向怜/121303310.ogg"
    rxl "毕竟凉君也习惯应付立花了，我也没什么需要担心的了。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031314210.ogg"
    lhx "本来就没有让日向你担心的必要。"
    hide rxl_dsf_b2
    show rxl_dsf_b1 b1 b1_h3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121303320.ogg"
    rxl "第一次约会要加油哟~"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314220.ogg"
    lhx "都说了不是约会，怎么可能做那种事，我们只是单纯的逛街而已！"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121303330.ogg"
    rxl "是是是，路上小心~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day223'
    $ seen_day223_street_event01 = False
    $ seen_day223_balltower_event01 = False

label day223.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day223':
        $ flcam.move(*overworld.camera_positions['road2'])
    elif _overworld_label == 'day223.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        road2=("day223.street_event01", "not seen_day223_street_event01"),
        cloqks=("day223.balltower_event01", "seen_day223_street_event01 and not seen_day223_balltower_event01"))
    $ window_animate_outro()
    if _return == 'day223.street_event01' and _overworld_label == 'day223':
        with Pause(1.0)
        scene black with dissolve
    elif _return == 'day223.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day223.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street day road1 xuejian
    play music second_112 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    play sound jiaobu2
    show lhx_dsf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031314230.ogg"
    lhx "凉君，想好去哪里了吗？"
    me01 "是啊，不过在那之前......"
    show lhx_dsf_b2 b2 b2_sp1
    play voice "voice/立花希/031314240.ogg"
    lhx "还有什么事吗？"
    me01 "上次没能做成的事，现在可以吗？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_h3
    play voice "voice/立花希/031314250.ogg"
    lhx "......你指的是什么？"
    me01 "虽然上次被千川老师打断了，不过总归是我赢了。"
    me01 "所以那个......要试着牵手看看吗？"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031314260.ogg"
    lhx "多少钱？"
    me01 "还要付钱的？"
    show lhx_dsf_b2 b2 b2_h2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031314270.ogg"
    lhx "这是一个高贵女人应该有的自尊心~"
    me01 "不过仔细想想牵着你的手，我的确可能会被误认为是想要赎金而诱拐小孩子的嫌疑犯。"
    hide lhx_dsf_b2 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_a1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/031314280.ogg"
    lhx "你这是什么说法啊，我想发飙了。"
    me01 "那我来喽~"
    show lhx_dsf_b3 b3 b3_ga2
    play voice "voice/立花希/031314290.ogg"
    lhx "等、等一下。"
    me01 "又怎么了？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314300.ogg"
    lhx "我、我要先有个心理准备。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314310.ogg"
    lhx "说到底......牵手这件事本身到底有什么意义。我倒觉得只会妨碍走路而已。"
    me01 "你不会是想反悔吧？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    show lhx_dsf_b1 b1 b1_s2 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031314320.ogg"
    lhx "今天天气不错~"
    hide lhx_dsf_b1
    me01 "别一边转移话题一边往后退了，快回来。"
    pause 1.0 hard
    scene set only street day road1 xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314330.ogg"
    lhx "这是何等屈辱的手势，我都想咬那只手了。"
    me01 "想咬也无所谓，只要你肯过来就行了。"
    show lhx_dsf_b1 b1 b1_s3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031314340.ogg"
    lhx "你是打算在我靠近的瞬间袭击我吧。" 
    me01 "只是单纯的牵个手而已。"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314350.ogg"
    lhx "你再用“快过来~快过来~”的手势招呼的话我就先走了。"
    me01 "放心吧，摸头也可以的。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031314360.ogg"
    lhx "我可不是会因为那种诱惑就轻易上钩的女人。"
    "嘴上这么说着，却还是靠了过来。"
    show lhx_dsf_b2 b2 b2_s2 at flu_down(0.35, 20):
        xpos 0.5
    me01 "乖乖乖。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314370.ogg"
    lhx "......脚竟然擅自移动了，这是什么诅咒吗。"
    me01 "那接下来我要牵手了。"
    show lhx_dsf_b3 b3 b3_a1
    play voice "voice/立花希/031314380.ogg"
    lhx "为什么就这么想牵手啊？！"
    me01 "因为是我赢了。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031314390.ogg"
    lhx "不能理解，请给出能让我信服的理由。"
    me01 "因为立花老师也是对我而言非常重要的人。"
    me01 "作为想要更了解你的方式之一这样的理由不行吗？"
    show lhx_dsf_b2 b2 b2_h3
    play voice "voice/立花希/031314400.ogg"
    lhx "......"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031314410.ogg"
    lhx "凉君你......想要更了解我吗？"
    me01 "是啊。"
    show lhx_dsf_b2 b2 b2_h3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031314420.ogg"
    lhx "也就是说你想做下流的事情吧？"
    me01 "如果你指的是牵手的话那么我的回答是“yes”。"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031314430.ogg"
    lhx "负心汉......"
    me01 "为什么会是这样的结论啊？"
    show lhx_dsf_b2 b2 b2_h3
    play voice "voice/立花希/031314440.ogg"
    lhx "让人害羞的台词已经足够了。"
    me01 "同感，那我真的来喽~"
    $ flcam.move(0, 0, 1100, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show lhx_dsf_b2 b2 b2_ga2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/031314450.ogg"
    lhx "等、等一下......"
    me01 "多说无益！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg street1
    play music second_142 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031314470.ogg"
    lhx "......"
    "剧烈的颤抖从手掌传来。"
    "手的温度有点低，是因为在门口等我的时候冻的吧。"
    "何等纤细的手臂，感觉就如同牵着爱衣一般。"
    me01 "为什么你会紧张到这种程度？"
    play voice "voice/立花希/031314480.ogg"
    lhx "才、才没有紧张。"
    me01 "跟其他事情比起来，果然牵手算是最简单的吧？"
    pause 0.1 hard
    scene set only lhx_cg street2
    with dissolve
    play voice "voice/立花希/031314500.ogg"
    lhx "不、不是的......"
    me01 "是这样吗？"
    pause 0.1 hard
    scene set only lhx_cg street1
    with dissolve
    play voice "voice/立花希/031314530.ogg"
    lhx "是的。"
    me01 "抱歉，是我想得太简单了。"
    play voice "voice/立花希/031314540.ogg"
    lhx "我之前也总是奇怪地闹别扭，现在算是就扯平了。"
    play voice "voice/立花希/031314560.ogg"
    lhx "我其实并不讨厌这样。"
    play voice "voice/立花希/031314570.ogg"
    lhx "只是害怕而已......"
    play voice "voice/立花希/031314580.ogg"
    lhx "害怕这样牵着凉君的手，{rb}接触感应{/rb}{rt}psychometry{/rt}说不定就会擅自发动了。"
    play voice "voice/立花希/031314590.ogg"
    lhx "紧张起来感情就会变得混乱，说不定还会暴走。"
    play voice "voice/立花希/031314600.ogg"
    lhx "还说不定会知道凉君的真实想法。"
    play voice "voice/立花希/031314610.ogg"
    lhx "虽然没办法清晰地看到内心，但还是能隐约感觉到......"
    pause 0.1 hard
    scene set only lhx_cg street2
    with dissolve
    play voice "voice/立花希/031314620.ogg"
    lhx "说不定就是因为我太胆小的关系。"
    play voice "voice/立花希/031314630.ogg"
    lhx "所以才会担心如果凉君讨厌我的话该怎么办这类的。"
    play voice "voice/立花希/031314640.ogg"
    lhx "要是看上我这近乎完美的身材想要对我做下流的事情该怎么办之类的......"
    me01 "煽情的时候不要搞笑啊喂！"
    pause 0.1 hard
    scene set only lhx_cg street1
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031314650.ogg"
    lhx "我、我是认真的！"
    play voice "voice/立花希/031314660.ogg"
    lhx "总之每次和凉君接触的时候，我总有一种你会离我而去的感觉，所以才会很害怕牵手。"
    me01 "那现在已经没问题了吗？"
    play voice "voice/立花希/031314670.ogg"
    lhx "......"
    me01 "告诉我你现在的想法。"
    pause 0.1 hard
    scene set only lhx_cg street3
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "立花希加大了握手的力度。"
    play voice "voice/立花希/031314680.ogg"
    lhx "这就是回答~"
    "本来冰冷的手不知不觉也暖和了起来。"
    me01 "现在想想，能够和立花老师战斗真是太好了。"
    play voice "voice/立花希/031314690.ogg"
    lhx "只是没想到你会以获得对方的身体为目标。"
    me01 "硬要这么说的话也没错。"
    pause 0.1 hard
    scene set only lhx_cg street1
    with dissolve
    play voice "voice/立花希/031314700.ogg"
    lhx "终于暴露出本性来了？！"
    me01 "我是指能够更了解立花老师你这件事。"
    me01 "毕竟光靠牵手就能够知道立花老师你在想什么，也可以算是以“身体”为目标了吧。"
    play voice "voice/立花希/031314710.ogg"
    lhx "......"
    me01 "相对的，立花老师又是怎么看我的呢？"
    play voice "voice/立花希/031314720.ogg"
    lhx "我是怎么看待凉君这一点，之前就已经说过了。"
    me01 "再说一遍吧，我都说出来了。"
    pause 0.1 hard
    scene set only lhx_cg street2
    with dissolve
    play voice "voice/立花希/031314730.ogg"
    lhx "......不要，我的话才没那么不值钱。"
    me01 "因为是高贵的女人？"
    play voice "voice/立花希/031314740.ogg"
    lhx "是的。"
    pause 0.1 hard
    scene set only lhx_cg street3
    with dissolve
    play voice "voice/立花希/031314750.ogg"
    lhx "而且我的想法什么的，就按凉君脑中的妄想来补充就好了。"
    me01 "顺带一提，我的想法可不是你用{rb}灵纹{/rb}{rt}rune{/rt}给我看到的那样。"
    play voice "voice/立花希/031314760.ogg"
    lhx "我输给凉君的时候就已经成为你的所有物了......随便处置就好了。"
    me01 "说好的高贵呢？"
    play voice "voice/立花希/031314770.ogg"
    lhx "我的“男朋友”是个怂货呢~"
    pause 0.1 hard
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/立花希/031314780.ogg"
    lhx "没问题的，请拿出点自信来。"
    play voice "voice/立花希/031314790.ogg"
    lhx "按凉君自己的想法去做，对我来说也是不会有问题的。"
    play voice "voice/立花希/031314800.ogg"
    lhx "就算世人不看好凉君，作为搭档的我也会接受你的。"
    play voice "voice/立花希/031314810.ogg"
    lhx "现在的我们已经是这种关系了~"
    pause 0.1 hard
    scene set only lhx_cg street2
    with dissolve
    play voice "voice/立花希/031314830.ogg"
    lhx "难得的约会，如果凉君不开心的话我也不会开心的。"
    me01 "立花老师......"
    play voice "voice/立花希/031314840.ogg"
    lhx "我究竟是多么能干的女人啊，说不定凉君和我在一起是在拖后腿呢~"
    me01 "我也是这么认为的。"
    pause 0.1 hard
    scene set only lhx_cg street1
    with dissolve
    play voice "voice/立花希/031314850.ogg"
    lhx "请不要这么认真地回答我的玩笑。"
    "我们就这样走在四下无人的街道上。"
    "也许正是因为这样的契机让我明白。"
    "那份从很久以前就萌芽了的感情。"
    "在遇到雷亚和希菲尔之前，除了翔子我几乎没有再与任何人有过交流了。"
    "也许我们的命运正是因为有了这样的羁绊才会交织在一起的。"
    "而得到了家人和朋友的我此时早已记不清。"
    "究竟是从什么时候开始，又是由谁带走了我的寂寞呢？"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day road1 xuejian
    with slowdissolve
    pause 1.0 hard
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('chapter seven'), _("梦的尽头没有你"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 1.0 hard
    play sound rune1
    play music second_126 fadein 3.0 if_changed
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303960.ogg"
    lhx "......"
    me01 "立花老师？"
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031303970.ogg"
    lhx "很遗憾我们又有工作了。"
    me01 "{rb}灵纹{/rb}{rt}rune{/rt}的暴走？"
    show lhx_dsf_b1 b1 b1_a1
    play voice "voice/立花希/031303980.ogg"
    lhx "是的。我感知到了异常的{rb}灵纹{/rb}{rt}rune{/rt}波动。"
    me01 "虽然很抱歉，但是“约会”的事情可能要暂时放一放了。"
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031304000.ogg"
    lhx "我知道的。已经确定了地点，我们快点过去吧。"
    me01 "不愧是立花老师~"
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard
    if not seen_day223_street_event01:
        $ seen_day223_street_event01 = True
    $ _overworld_label = 'day223.street_event01'
    jump day223.map

label day223.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian2
    play ambience1 strong_wind fadein 3.0
    show snow_level2 onlayer fg
    play music second_126 fadein 3.0 if_changed
    with slowdissolve
    pause 2.0 hard
    scene set only balltower snow day big2
    with dissolve
    pause 1.0 hard
    me01 "明明一路上都没有下雪的，为什么偏偏这里的雪下得这么大啊？！"
    "周围的气流很乱，被一股暴风雪包围着。"
    "虽然跟小桃暴走时产生的风暴相比算是温和了不少，但还是对行动有所影响。"
    me01 "那孩子就是主犯吗？"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031304030.ogg"
    lhx "那孩子是......"
    me01 "你认识她吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031304040.ogg"
    lhx "是的。她是幼儿园的孩子。"
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_n2 at walkout_r(0.5)
    pause 0.5 hard
    hide lhx_dsf_b2
    "立花老师缓缓地靠了上去。"
    "明明那么怕冷的她，此时却孤身一人走进了那吹雪之中。"
    me01 "别一个人进去，很危险的。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with dissolve
    pause 1.0 hard
    "我一边用{rb}念动力场{/rb}{rt}psychokinesis{/rt}制造风壁阻隔风暴，一边也跟了上去。"
    scene set only balltower snow day xuejian2 alpha
    play music second_111 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031304050.ogg"
    lhx "发生什么事了？一个人来这种地方。爸爸和妈妈去哪里了？"
    $ flcam.move(2250, -300, 1100, duration=1.5)
    pause 0.5 hard
    show girl01 onlayer m2:
        xpos 0.65 ypos 0.25 alpha 0.0 zoom 0.5
        parallel:
            linear 1.0 xpos 0.55
        parallel:
            linear 1.0 alpha 1.0
    pause 1.5 hard
    "立花希一边摸着她的头一边询问着事情的经过。"
    "随着对话的进行，周围的风暴也渐渐平息了下来。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031304060.ogg"
    lhx "是吗......在去买东西的途中走散了吗。"
    show lhx_dsf_b3 b3 b3_n1
    play voice "voice/立花希/031304070.ogg"
    lhx "我想你的爸爸妈妈应该在就电车站附近，之前去神社的时候顺便了解过了，要去商店街的话一定会经过那里不会错的。"
    play voice "voice/立花希/031304080.ogg"
    lhx "他们现在一定也在担心你，让我们带你过去吧。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031304090.ogg"
    lhx "所以不用再难过了。"
    stop ambience1 fadeout 3.0
    show lhx_dsf_b2 b2 b2_h1
    play voice "voice/立花希/031304100.ogg"
    lhx "已经可以安心了~"
    pause 1.0 hard
    hide snow_level2
    scene white
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "雪花依旧飘舞着，但是却没有了风。"
    "很幸运，暴走只是暂时的，现在已经完全感觉不到灵力波动了。"
    "没有出现伤者真是太好了。"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031304110.ogg"
    lhx "凉君，我去帮这孩子找她的家人。"
    me01 "不，这件事交给我好了。"
    me01 "立花老师就留在这里，说不定对方也会找过来。"
    pause 0.5 hard
    hide lhx_dsf_b2
    play sound jiaobu2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    "说完，我拉着孩子的手离开了钟楼广场。"
    stop music fadeout 5.0
    pause 2.0 hard

label day223.balltower_event02:
    play music second_125 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    show lhx_dsf_b1 b1 b1_s3
    play voice "voice/立花希/031319240.ogg"
    lhx "为什么我还是磨磨蹭蹭的呢......"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    $ flcam.move(0, 0, 0)
    scene set only items key
    with slowdissolve
    pause 1.0 hard
    "这段回忆无论是对“她”还是凉君来说，都是很重要的吧。"
    "通过{rb}接触感应{/rb}{rt}psychometry{/rt}也早已无数次地窥见了凉君内心的伤痛。"
    "明明想过要帮助他的，明明是必须要告诉他真相的，明明......一直都是这样决定好了的。"
    "但是，为什么到了现在反而越发害怕起来了呢？"
    "潘多拉的魔盒。"
    "一面是希望，另一面则是与之对等绝望。"
    "解开温柔魔法的咒语，同时也是葬送幸福的利刃。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    show lhx_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/立花希/031319260.ogg"
    lhx "我到底在做什么，这样只会给他添麻烦而已。"
    pause 0.5 hard
    play sound rune1
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031319270.ogg"
    lhx "......"
    play voice "voice/立花希/031319280.ogg"
    lhx "这是？"
    stop music fadeout 5.0
    show lhx_dsf_b1 b1 b1_h1
    play voice "voice/立花希/031319290.ogg"
    lhx "是这样啊......"
    show lhx_dsf_b1 b1 b1_n1
    play voice "voice/立花希/031319300.ogg"
    lhx "你所说的“一直看着我们”果然是真的啊~"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    play music second_134 fadein 3.0 if_changed
    scene set only xfe_cg normal
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001301440.ogg"
    xfe "嗯，今后我也会继续看着你们。"
    play voice "voice/希菲尔/001301450.ogg"
    xfe "希菲尔我想要守望你们的幸福。"
    play voice "voice/希菲尔/001301460.ogg"
    xfe "所以像这样在你面前出现也是最后一次了。"
    play voice "voice/希菲尔/001301470.ogg"
    xfe "在最后无论如何我都想要说出来。"
    pause 0.1 hard
    scene set only xfe_cg normal
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001301480.ogg"
    xfe "谢谢你~"
    play voice "voice/希菲尔/001301490.ogg"
    xfe "正因为有你，凉君变得更坚强了。"
    play voice "voice/希菲尔/001301500.ogg"
    xfe "又能够继续向前迈进了。"
    play voice "voice/希菲尔/001301510.ogg"
    xfe "学会了什么是家人。"
    play voice "voice/希菲尔/001301520.ogg"
    xfe "也学会了什么是爱情。"
    play voice "voice/希菲尔/001301530.ogg"
    xfe "就这样找到了新的伙伴。"
    play voice "voice/希菲尔/001301540.ogg"
    xfe "雪的足迹会一直延续下去。"
    play voice "voice/希菲尔/001301550.ogg"
    xfe "已经......不会再迷路了。"
    play voice "voice/希菲尔/001301560.ogg"
    xfe "已经不会再寂寞了。"
    play voice "voice/希菲尔/001301570.ogg"
    xfe "所以，谢谢你。"
    pause 0.1 hard
    scene set only xfe_cg happy
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001301580.ogg"
    xfe "能够喜欢上凉君，谢谢你~"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/立花希/031319320.ogg"
    lhx "你大概是误会了吧。"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031319330.ogg"
    lhx "如果说有人帮凉君从寂寞中走出来的话，那个人一定不是我。"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031319340.ogg"
    lhx "是因为有你在的关系才......"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031319350.ogg"
    lhx "是因为你成为了凉君最初的伙伴。"
    play voice "voice/立花希/031319360.ogg"
    lhx "给予了他最初的羁绊。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031319370.ogg"
    lhx "正是因为有你的存在，凉君他才能遇见我。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031319380.ogg"
    lhx "也正是因为这样，凉君才能在重返雪见市之后变得坚强起来的。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301590.ogg"
    xfe "不是的。"
    show ts_xfe_yjz_b1 b1 b1_n2
    play voice "voice/希菲尔/001301600.ogg"
    xfe "果然，不该是这样的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301610.ogg"
    xfe "你可以更加自信的。"
    hide lhx_dsf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301620.ogg"
    xfe "因为你追上凉君了。"
    play voice "voice/希菲尔/001301630.ogg"
    xfe "因为你喜欢上凉君了。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001301640.ogg"
    xfe "所以凉君才会没有被过去所牵绊。"
    play voice "voice/希菲尔/001301650.ogg"
    xfe "才会不再依赖那已经消融淡化的雪之足迹。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001301660.ogg"
    xfe "才不需要再继续追赶希菲尔的背影了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031319390.ogg"
    lhx "......"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301670.ogg"
    xfe "因为凉君的身边，随时随地都有你们在帮助他。"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001301680.ogg"
    xfe "凉君他也终于注意到了，那近在咫尺的、重要的存在。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031319400.ogg"
    lhx "......"
    hide lhx_dsf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301690.ogg"
    xfe "所以凉君，才变得坚强了。"
    $ flcam.move(4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_h1
    play voice "voice/希菲尔/001301700.ogg"
    xfe "这样的凉君，也一定会让你变得坚强的。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with dissolve
    pause 1.0 hard
    "希菲尔的身影消失的那一刻，雪也跟着停止了。"
    "最后一片雪花飞舞着，与蓝天融为了一体。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian2
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/立花希/031319410.ogg"
    lhx "是啊......我也是知道的。"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031319420.ogg"
    lhx "我也因为凉君而变得坚强了。"
    play voice "voice/立花希/031319430.ogg"
    lhx "摆脱了软弱的自己，一定能够有所成长。"
    show lhx_dsf_b2 b2 b2_s1
    play voice "voice/立花希/031319440.ogg"
    lhx "所以我才会来到这里。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031319450.ogg"
    lhx "谢谢你，希菲尔。"
    show lhx_dsf_b1 b1 b1_h1
    play voice "voice/立花希/031319460.ogg"
    lhx "在最后你还是帮了我一把。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day223.balltower_event03:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    play music second_131 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    me01 "雪......停了。"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    with dissolve
    play sound jiaobu
    "回到了钟楼广场的我没有发现立花老师的身影。"
    "但是雪地上却留下了一行清晰的足迹。"
    "简单易懂的提示。"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    "我顺着足迹蔓延的方向追了上去。"
    pause 1.0 hard
    "......为什么呢？"
    "此刻脑海里浮现出了熟悉的画面。"
    pause 1.0 hard
    scene set only lhx_cg memory
    with slowdissolve
    pause 1.0 hard
    "那是过去我和希菲尔一起玩耍的地方。"
    "而就在这座钟楼广场的某个角落里。"
    "总有一个身影悄悄地注视着我们。"
    "默默地......投来羡慕的目光。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.25
        linear 0.75 alpha 1
    pause 5.0 hard
    $ flcam.move(0, 0, 0)
    play music second_130 fadein 3.0 if_changed
    scene set only lhx_cg final one
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031319470.ogg"
    lhx "凉君......"
    play voice "voice/立花希/031319490.ogg"
    lhx "就算我不再要求，你也会主动来到我的身边了。"
    play voice "voice/立花希/031319500.ogg"
    lhx "就算我不再追赶，你也会回过头来看着我了。"
    play voice "voice/立花希/031319510.ogg"
    lhx "是啊......"
    play voice "voice/立花希/031319520.ogg"
    lhx "也许正因如此我才会迷茫。"
    play voice "voice/立花希/031319530.ogg"
    lhx "因为我和凉君的羁绊更加清晰了。"
    play voice "voice/立花希/031319540.ogg"
    lhx "正因如此我才花了更长的时间下定决心的。"
    pause 0.1 hard
    scene set only lhx_cg final three
    with dissolve
    play voice "voice/立花希/031319550.ogg"
    lhx "但是现在，有人在背后支持着我。"
    play voice "voice/立花希/031319560.ogg"
    lhx "她把凉君托付给我了。"
    play voice "voice/立花希/031319570.ogg"
    lhx "在这里逃避了的话，我就不配做女人了。"
    play voice "voice/立花希/031319580.ogg"
    lhx "我也想和凉君一样选择继续前进。"
    play voice "voice/立花希/031319590.ogg"
    lhx "如果可以的话，我希望能带着笑容启程。"
    play voice "voice/立花希/031319600.ogg"
    lhx "能抬头挺胸地，把这件事情解决。"
    pause 0.1 hard
    scene set only lhx_cg final five
    with dissolve
    play voice "voice/立花希/031319610.ogg"
    lhx "为此，我必须把我对凉君隐瞒的秘密说出来。"
    "此时的我才注意到，立花希的手中捧着一个盒子。"
    "那是一个看起来经历了许多个年头的、陈旧的木盒。"
    play voice "voice/立花希/031319640.ogg"
    lhx "就在刚才“她”托付给了我。"
    play voice "voice/立花希/031319650.ogg"
    lhx "所谓“{encyclopedia=panduola}潘多拉的魔盒{/encyclopedia}”，说的就是这个了吧。"
    play voice "voice/立花希/031319660.ogg"
    lhx "但我相信里面装着的就是凉君一直想要找的东西。"
    me01 "原来如此。"
    pause 0.1 hard
    scene set only lhx_cg final six
    with dissolve
    play voice "voice/立花希/031319690.ogg"
    lhx "......你不惊讶吗？"
    me01 "比起惊讶，我更好奇为什么立花老师会知道我一直在找“某样东西”。"
    me01 "雷亚凭依的陨石......难不成就在这个盒子里吗？"
    pause 0.1 hard
    scene set only lhx_cg final three
    with dissolve
    play voice "voice/立花希/031319710.ogg"
    lhx "我说的话是真是假，只要打开盒子就知道了。"
    me01 "那如果我拒绝作出选择呢？"
    pause 0.1 hard
    scene set only lhx_cg final one
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031319720.ogg"
    lhx "无论多少次我都会说的。"
    play voice "voice/立花希/031319730.ogg"
    lhx "直到凉君同意我的要求为止。"
    play voice "voice/立花希/031319740.ogg"
    lhx "就像那个时候一样——"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg memory
    show sepiagrain onlayer texture
    with dissolve
    play voice "voice/立花希/031319750.ogg"
    lhx "就像是和凉君告别的那天一样。"
    play voice "voice/立花希/031319760.ogg"
    lhx "明明知道那可能是我最后的机会了。"
    play voice "voice/立花希/031319770.ogg"
    lhx "可就算是这样我还是没能说出口。"
    play voice "voice/立花希/031319780.ogg"
    lhx "只是在暗中看着你们，却没有站出来。"
    pause 1.0 hard
    scene set only lhx_cg final one
    with dissolve
    play voice "voice/立花希/031319790.ogg"
    lhx "因为没有勇气站出来。"
    play voice "voice/立花希/031319800.ogg"
    lhx "不管怎么努力，始终无法克服恐惧。"
    play voice "voice/立花希/031319820.ogg"
    lhx "别说被接受了，说不定还会因此失去成为朋友的机会。"
    play voice "voice/立花希/031319830.ogg"
    lhx "你说不定会因此而讨厌我。"
    play voice "voice/立花希/031319840.ogg"
    lhx "就算我相信凉君你不会那么做，但还是不自觉地这样想了。"
    play voice "voice/立花希/031319850.ogg"
    lhx "就这样......直到再次见面的时候我还是这样想的。"
    pause 0.1 hard
    scene set only lhx_cg final three
    with dissolve
    play voice "voice/立花希/031319860.ogg"
    lhx "我就是这样的软弱。"
    play voice "voice/立花希/031319880.ogg"
    lhx "孤独会将人击垮。"
    play voice "voice/立花希/031319890.ogg"
    lhx "唯一能够依靠的也只有与某人一起度过的回忆而已。"
    pause 0.1 hard
    scene set only lhx_cg final one
    with dissolve
    play voice "voice/立花希/031319910.ogg"
    lhx "仅仅只是这么相信着，我就觉得自己不再是孤单一人了。"
    play voice "voice/立花希/031319920.ogg"
    lhx "即使就这样去了另一个世界，我也能够感到满足了。"
    play voice "voice/立花希/031319930.ogg"
    lhx "当我见到凉君你的第一眼开始......这个念头就在我的脑海中诞生了。"
    play voice "voice/立花希/031319950.ogg"
    lhx "我们羁绊的来源就封存在这个盒子里。"
    play voice "voice/立花希/031319960.ogg"
    lhx "钥匙也被我当成护身符随身带着。"
    pause 0.1 hard
    scene set only lhx_cg final three
    with dissolve
    play voice "voice/立花希/031319970.ogg"
    lhx "我认为只要一直这样下去就好了。"
    play voice "voice/立花希/031319980.ogg"
    lhx "但是......"
    pause 0.1 hard
    scene set only lhx_cg final five
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031319990.ogg"
    lhx "再次遇到你之后我的想法改变了。"
    play voice "voice/立花希/031320010.ogg"
    lhx "同时我的心愿也在那一刻实现了。"
    play voice "voice/立花希/031320030.ogg"
    lhx "所以这一次轮到你了。"
    play voice "voice/立花希/031320040.ogg"
    lhx "今后的路，就由你来选择。"
    play voice "voice/立花希/031320050.ogg"
    lhx "是不是要打开这个盒子，就由你来决定。"
    play voice "voice/立花希/031320060.ogg"
    lhx "潘多拉的魔盒也许真的只装着绝望。"
    play voice "voice/立花希/031320070.ogg"
    lhx "或许根本......就没有希望也说不定。"
    pause 0.1 hard
    scene set only lhx_cg final three
    with dissolve
    play voice "voice/立花希/031320080.ogg"
    lhx "如果选择放弃的话，我们还能像之前一样回归正常的生活。"
    play voice "voice/立花希/031320100.ogg"
    lhx "就算这样也不会被任何人指责。"
    pause 0.1 hard
    scene set only lhx_cg final one
    with dissolve
    play voice "voice/立花希/031320120.ogg"
    lhx "而如果选择打开盒子的话，就必然会产生更多的迷茫。"
    play voice "voice/立花希/031320130.ogg"
    lhx "你说不定会因此而后悔。"
    play voice "voice/立花希/031320140.ogg"
    lhx "也许不仅找不回的失去的羁绊，甚至就连我们现在的羁绊也会因此而失去。"
    pause 0.1 hard
    scene set only lhx_cg final five
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031320150.ogg"
    lhx "凉君......请选择吧。"
    play voice "voice/立花希/031320160.ogg"
    lhx "是否要打开潘多拉的魔盒，就由你来决定。"
    "如果我猜得没错的话，里面放着的应该就是雷亚凭依的陨石。"
    "虽说不上原因，但是见到立花老师的第一眼我就在她的身上看到了雷亚的影子。"
    "无论是发色、眼睛、就连怕生的性格也简直一模一样。"
    "而此刻的我更加确信了这一点。"
    "无论等待着我的是什么，我都必须去尝试。"
    "尝试解开这一切谜团。"
    "所以......"
    me01 "把钥匙给我吧。"
    pause 0.1 hard
    scene set only lhx_cg final six
    with dissolve
    play voice "voice/立花希/031320170.ogg"
    lhx "......"
    pause 0.1 hard
    scene set only lhx_cg final one
    with dissolve
    play voice "voice/立花希/031320180.ogg"
    lhx "你一定......会后悔的。"
    me01 "也许就像你说的那样，我一定会后悔。"
    me01 "但是啊立花老师。"
    me01 "比起自己做了错误的决定而后悔，我更讨厌的是自己能做决定却放弃了。"
    me01 "过去的我就是这样，看着自己重要的人离我而去却什么事都没有做。"
    pause 0.1 hard
    scene set only lhx_cg final three
    with dissolve
    play voice "voice/立花希/031320190.ogg"
    lhx "......"
    me01 "也许即使我什么都不做也不会有人会因此责备我。"
    me01 "也许即使我尽力去做了最终却还是失败了。"
    me01 "也许到头来我还是什么都改变不了。"
    me01 "但是啊，我已经不想再停滞不前了。"
    me01 "过去有人曾对我说过，如果连自己都不相信，那么就连站在起跑线上的资格都没有了。"
    me01 "就算会失去更多的东西。"
    me01 "那么下次一起夺回来就好了。"
    me01 "不管多少次我都会奉陪到底的，因为人的就是这样充满勇气的生物。"
    me01 "所以，请把钥匙给我。"
    me01 "请允许我相信，这二分之一的希望吧。"
    play voice "voice/立花希/031320200.ogg"
    lhx "好的......"
    pause 0.1 hard
    scene set only lhx_cg final one
    with dissolve
    play voice "voice/立花希/031320210.ogg"
    lhx "后悔的话，我可不管你。"
    pause 1.0 hard
    scene white
    with slowdissolve
    pause 1.0 hard
    "我打开了盒子。"
    "里面什么都没有。"
    "那一刻我才真正明白。"
    "所谓的希望和绝望，并不是真实存在的东西。"
    "回忆并不是能够被“封印”在某处的东西，它一直都在那里，只是缺乏一个理由。"
    "一个让当事人接受它的理由而已。"
    "而这个理由，也许只是一个选择那么简单。"
    stop music fadeout 5.0
    me01 "谢谢你。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg final seven
    play music second_157 fadein 3.0 if_changed
    with dissolve
    play voice "voice/立花希/031320280.ogg"
    lhx "......欸？"
    me01 "以前的我们果然，也在这里见过面的吧？"
    me01 "那个总是躲在暗处看着我们的女孩。"
    me01 "虽然不是所有的事情都记得，但我多多少少还是注意到了。"
    me01 "过去的立花老师你还真是非常地怕生啊。"
    me01 "别说后悔了，现在的我反而开心得不得了。"
    me01 "即使是那样独来独往、性格怪癖的我，也有像立花老师这样的人在默默地关注着我。"
    me01 "我在想我果然是很幸运的。"
    play voice "voice/立花希/031320290.ogg"
    lhx "......"
    pause 0.1 hard
    scene set only lhx_cg final eight
    with dissolve
    play voice "voice/立花希/031320300.ogg"
    lhx "凉君你真是个笨蛋。"
    play voice "voice/立花希/031320310.ogg"
    lhx "无药可救的......超级大笨蛋。"
    play voice "voice/立花希/031320320.ogg"
    lhx "你到底要温柔到什么程度才肯罢休呢。"
    me01 "我不知道接下来的路会如何。"
    me01 "也不知道我今天的选择是否正确。"
    me01 "但我一定会更加坚定地朝着那个方向迈进。"
    me01 "能够认识立花老师你，我真的很开心。"
    me01 "那时的你也好，现在的你也罢。"
    me01 "无论哪一个都是我生命中不可替代的存在。"
    me01 "是无法被磨灭的伙伴！"
    play voice "voice/立花希/031320350.ogg"
    lhx "......"
    pause 0.1 hard
    scene set only lhx_cg final nine
    with dissolve
    play voice "voice/立花希/031320360.ogg"
    lhx "呜......"
    me01 "毕竟这就是我们的羁绊嘛。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene white 
    with slowerdissolve
    pause 2.0 hard
    scene set only lhx_cg final twelve
    with dissolve
    play voice "voice/天使雷亚/0090001.ogg"
    lhx "就像在做梦一样。"
    play voice "voice/天使雷亚/0090014.ogg"
    lhx "仿佛就要放开与那个人的回忆。"
    play voice "voice/天使雷亚/0090015.ogg"
    lhx "我这个个体，曾经就是这样的。"
    play voice "voice/天使雷亚/0090018.ogg"
    lhx "我依然在这里。"
    play voice "voice/天使雷亚/0090019.ogg"
    lhx "依然可以维持。"
    play voice "voice/天使雷亚/0090020.ogg"
    lhx "被守护着。"
    play voice "voice/天使雷亚/0090021.ogg"
    lhx "到底还能守护多久呢？"
    play voice "voice/天使雷亚/0090022.ogg"
    lhx "能存在于百年之后吗，还是说只能维持几年，亦或者连几天都承受不了呢？"
    play voice "voice/天使雷亚/0090023.ogg"
    lhx "还是此刻早已经是极限了呢......"
    pause 0.1 hard
    scene set only lhx_cg final ten
    with dissolve
    play voice "voice/天使雷亚/0090024.ogg"
    lhx "即使如此，我依然有着想要守护的未来。"
    play voice "voice/天使雷亚/0090025.ogg"
    lhx "我相信着。"
    play voice "voice/天使雷亚/0090026.ogg"
    lhx "并不是祈祷或者愿望。"
    play voice "voice/天使雷亚/0090027.ogg"
    lhx "我可以确信。"
    play voice "voice/天使雷亚/0090028.ogg"
    lhx "因为许下了约定。"
    play voice "voice/天使雷亚/0090029.ogg"
    lhx "因为得到了约定的光。"
    play voice "voice/天使雷亚/0090030.ogg"
    lhx "因为那是在温暖的沉睡之中，依然能够感觉到的，温柔的光。"
    pause 0.1 hard
    scene set only lhx_cg final eleven
    with dissolve
    play voice "voice/天使雷亚/0090031.ogg"
    lhx "所以......"
    play voice "voice/天使雷亚/0090032.ogg"
    lhx "只要朝着那道光的方向看去的话。"
    pause 0.1 hard
    scene set only lhx_cg final twelve
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 2.0 hard
    play voice "voice/天使雷亚/0090033.ogg"
    lhx "在那里，回忆一定也在延续着——"
    stop music fadeout 3.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day223.memory_event01:
    $ set_replay_scene("label15_3")
    $ flcam.move(0, 0, 0)
    scene set only school day corridor xuejian
    play music second_151 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    "空荡荡的教室，少了往日的喧闹声。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_zf_b3 b3 b3_s3 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031324510.ogg"
    lhx "......怎么样？"
    me01 "嗯，很合身。"
    hide lhx_zf_b3
    show lhx_zf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031324520.ogg"
    lhx "反正你肯定觉得胸部那边空荡荡的。"
    me01 "之前就脑补过这样的场景。"
    hide lhx_zf_b1
    show lhx_zf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031324530.ogg"
    lhx "......我也是。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_zf_b2 b2 b2_h1
    play voice "voice/立花希/031324540.ogg"
    lhx "但我还是更为自己在幼儿园的工作感到骄傲。"
    me01 "我知道的，毕竟立花老师比起幼儿园的小朋友更像是老师嘛。"
    hide lhx_zf_b2
    show lhx_zf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031324550.ogg"
    lhx "接下来要去哪里呢？"
    me01 "立花老师有想去的地方吗？"
    show lhx_zf_b3 b3 b3_n1
    play voice "voice/立花希/031324560.ogg"
    lhx "我的话嘛......有很多。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_zf_b3
    show lhx_zf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031324570.ogg"
    lhx "但是最想去的果然还是凉君所在的教室。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    scene set only school day room xuejian nobody
    play music second_152 fadein 3.0 if_changed
    play sound open_door5
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show lhx_zf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031324600.ogg"
    lhx "这里就是凉君的教室吗？"
    me01 "是啊，虽然平淡无奇，但还是充满了美好的回忆。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_zf_b2 b2 b2_h1
    play voice "voice/立花希/031324610.ogg"
    lhx "凉君的座位是哪个？"
    me01 "最后一排靠窗户的位置。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with dissolve
    pause 1.0 hard
    "立花希轻轻抚摸着课桌。"
    "就好像是在和这个教室告别一样。"
    "我也跟着坐到了旁边的位置上。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    scene set only lhx_cg school one
    with dissolve
    pause 1.0 hard
    "立花希就座之后，挺直了背向黑板的方向望去。"
    "就这样默默地注视着前方。"
    "保持了很长的一段时间。"
    "那是一段静谧的时光。"
    "没有言语。"
    "取而代之的是思索。"
    "一定是想起了过去上学时的事了吧。"
    "如果没有发生那么多事情，而是作为两个毫不相干的普通人各自生活的话......"
    "我一定会后悔错过了这样的光景。"
    pause 0.1 hard
    scene set only lhx_cg school two
    with dissolve
    play voice "voice/立花希/031324620.ogg"
    lhx "凉君。"
    play voice "voice/立花希/031324630.ogg"
    lhx "怎么了，在那里发呆？"
    play voice "voice/立花希/031324640.ogg"
    lhx "上课太不专心。"
    play voice "voice/立花希/031324650.ogg"
    lhx "难道说是忘记带教科书了吗？"
    pause 0.1 hard
    scene set only lhx_cg school three
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031324660.ogg"
    lhx "真拿你没办法，我的借给你吧~"
    "立花希把桌子靠了过来。"
    "我们的距离被拉近了。"
    pause 0.1 hard
    scene set only lhx_cg school two
    with dissolve
    play voice "voice/立花希/031324670.ogg"
    lhx "这样的校园生活，说不定会挺开心啊~"
    me01 "下次再一起来吧？"
    pause 0.1 hard
    scene set only lhx_cg school four
    with dissolve
    play voice "voice/立花希/031324680.ogg"
    lhx "......欸？"
    me01 "不是在这个妄想的世界里，而是在我们的真实世界。"
    me01 "我会给你介绍我最好朋友们。"
    me01 "顺便也让大家认识一下立花老师你。"
    me01 "就这样大家一起上学吧！"
    play voice "voice/立花希/031324690.ogg"
    lhx "......"
    me01 "那样的话，说不定就能产生出新的羁绊也说不定。"
    me01 "那样说不定......"
    me01 "不对，是一定能够再见面的！"
    pause 0.1 hard
    scene set only lhx_cg school two
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031324700.ogg"
    lhx "请不要说些自以为是的话。"
    play voice "voice/立花希/031324720.ogg"
    lhx "听好了，我喜欢的不是校园生活，而是凉君你啊~"
    me01 "今后的路......不会觉得寂寞吗？"
    pause 0.1 hard
    scene set only lhx_cg school three
    with dissolve
    play voice "voice/立花希/031324730.ogg"
    lhx "没问题的~"
    pause 0.1 hard
    scene set only lhx_cg school two
    with dissolve
    play voice "voice/立花希/031324740.ogg"
    lhx "之前不是也说过的吗，我这是毕业了嘛。"
    me01 "这样真的可以吗？"
    play voice "voice/立花希/031324750.ogg"
    lhx "是的，虽然肉眼看不见，但我们的思念却始终是一体的。"
    me01 "既然这样，今后也请多多关照了，立花老师。"
    pause 0.1 hard
    scene set only lhx_cg school four
    with dissolve
    me01 "无论在哪里，一起走下去吧！"
    me01 "如果立花老师忘了我的话，我一定会很伤心的。"
    pause 0.1 hard
    scene set only lhx_cg school three
    with dissolve
    play voice "voice/立花希/031324770.ogg"
    lhx "你这是在吃醋吗？"
    me01 "某种意义上是吧。"
    play voice "voice/立花希/031324780.ogg"
    lhx "我也曾因为希菲尔和凉君的关系吃过醋，这下算是扯平了。"
    me01 "那么你意下如何呢？"
    pause 0.1 hard
    scene set only lhx_cg school two
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031324790.ogg"
    lhx "是啊，在我们彼此找到新的羁绊之前。"
    play voice "voice/立花希/031324800.ogg"
    lhx "要毕业的不只是我一人。"
    play voice "voice/立花希/031324810.ogg"
    lhx "{rb}灵纹{/rb}{rt}rune{/rt}一定......也是一样的。"
    play voice "voice/立花希/031324820.ogg"
    lhx "我从凉君那里得到了名为羁绊的{rb}灵纹{/rb}{rt}rune{/rt}。"
    play voice "voice/立花希/031324830.ogg"
    lhx "通过和凉君的接触明白了彼此的想法。"
    play voice "voice/立花希/031324840.ogg"
    lhx "这是饯别礼。"
    play voice "voice/立花希/031324850.ogg"
    lhx "心与心的交汇。"
    play voice "voice/立花希/031324860.ogg"
    lhx "心与心之间通过{rb}灵纹{/rb}{rt}rune{/rt}传递着感情。"
    pause 0.1 hard
    scene set only lhx_cg school three
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031324870.ogg"
    lhx "名为恋爱的光。"
    play voice "voice/立花希/031324880.ogg"
    lhx "那一定就是被称作“家人”的{rb}灵纹{/rb}{rt}rune{/rt}——"
    pause 2.0 hard
    scene white 
    with slowerdissolve
    stop music fadeout 5.0
    pause 1.0 hard
    $ end_replay()
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    python:
        local_config.masters = ["xfe_role"]
        for role in local_config.party:
            if role.name == "立花希" or role.name == "雷亚":
                local_config.party.remove(role)
                local_config.release.append(role)

        for role in local_config.backup:
            if role.name == "立花希" or role.name == "雷亚":
                local_config.backup.remove(role)
                if role not in local_config.release:
                    local_config.release.append(role)

        local_config.role_pool.remove("lst_role")
        local_config.role_pool.remove("lhx_role")

    $ suppress_overlay = True

    jump day224
