
label day220:
    bookmark
    $ save_name = _("Day 220")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date219 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    "今天是与琉璃一行人道别的日子。"
    "从早上开始天就一直下着雪。"
    play voice "voice/希菲尔/001500010.ogg"
    stranger "凉君......"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 2.0 hard
    scene set only bridge snow day xuejian
    show snow_level1 onlayer fg
    play music second_103 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    me01 "......"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001500030.ogg"
    xfe "也想听凉君说这句话。"
    me01 "希菲尔......"
    show ts_xfe_yjz_b3 b3 b3_h1 at flu_down(0.35, 20):
        xpos 0.5
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    "我摸了摸希菲尔德头。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001500040.ogg"
    xfe "凉君你在烦恼什么吗？"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001500050.ogg"
    xfe "在见到希菲尔之前一直都是一副不好的表情。"
    play voice "voice/希菲尔/001500060.ogg"
    xfe "一直是在思考着什么样子。"
    me01 "果然还是被你发现了。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001500070.ogg"
    xfe "凉君为什么会烦恼呢？"
    play voice "voice/希菲尔/001500080.ogg"
    xfe "又在思考些什么呢？"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001500090.ogg"
    xfe "说实话希菲尔也不知道。"
    me01 "就算是希菲尔也没办法吗？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001500110.ogg"
    xfe "就算是希菲尔也是一样的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001500130.ogg"
    xfe "所以呢，希菲尔也会像这样一直看着凉君你的。"
    me01 "......如果能够轻易地理解对方的想法该有多好啊。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001500150.ogg"
    xfe "那，我们是一样的呢~"
    me01 "希菲尔也是这么想的吗？"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001500160.ogg"
    xfe "不过不用担心的。"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/001500170.ogg"
    xfe "凉君你只是......在害怕而已。"
    play voice "voice/希菲尔/001500180.ogg"
    xfe "害怕着、犹豫着应该怎么做。"
    stop music fadeout 5.0
    pause 0.5 hard
    hide snow_level1
    play sound xiaoshi_1
    scene white
    with slowerdissolve
    pause 1.0 hard

label day220.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "随着希菲尔身影的消失，原本持续的雪也停止了。"
    pause 1.0 hard
    scene set only bridge snow day xuejian
    play music second_140 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031401280.ogg"
    lhx "你终于来了吗。"
    show lhx_dsf_b2 b2 b2_a1
    play voice "voice/立花希/031401290.ogg"
    lhx "怎么这么慢啊，你要是再不来我就要打电话了。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031401300.ogg"
    lhx "接下来还要去送行的吧，再不快点的话就赶不上电车了。"
    me01 "立花老师你一直在这里等我吗？"
    show lhx_dsf_b3 b3 b3_sp2
    play voice "voice/立花希/031401310.ogg"
    lhx "有什么问题吗？"
    me01 "完全没有。"
    me01 "看来就算是立花老师也很重视琉璃这个朋友的。"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031401320.ogg"
    lhx "我们也不算什么很要好的朋友......"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031401330.ogg"
    lhx "我才不是为了给璃之助送行才来的呢，这么难为情的事我才不做。"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031401340.ogg"
    lhx "我只是碰巧有事而已。"
    me01 "你指的“有事”不就是送行吗？"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031401350.ogg"
    lhx "我不是来找璃之助的，而是凉君你。"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031401360.ogg"
    lhx "你真的觉得这样子就可以了吗？"
    me01 "你指什么？"
    show lhx_dsf_b1 b1 b1_a1
    play voice "voice/立花希/031401370.ogg"
    lhx "当然是指璃之助的事情啊！"
    me01 "琉璃她是因为有重要的任务才选择离开雪见市的，为此我没有阻止她的权利。"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031401380.ogg"
    lhx "权利什么的都无所谓，我只想听听凉君你是怎么想的。"
    me01 "为什么立花老师你对此这么关心啊？"
    show lhx_dsf_b3 b3 b3_ga2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031401390.ogg"
    lhx "......凉君你怎么样都和我没有关系。"
    me01 "等一切都结束了我会告诉你的。"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031401400.ogg"
    lhx "......"
    hide lhx_dsf_b1 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_a1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031401410.ogg"
    lhx "凉君什么的，和璃之助怎么样都无所谓了。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031401420.ogg"
    lhx "逛街什么的都和她一起去就好了！"
    me01 "你是在闹别扭吗？"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031401430.ogg"
    lhx "去死好了。"
    me01 "虽然不知道你为什么不开心，但是琉璃走后和我逛街不就只剩立花老师你了吗？"
    show lhx_dsf_b2 b2 b2_a1
    play voice "voice/立花希/031401440.ogg"
    lhx "我只是备胎而已吗。"
    me01 "我不是这个意思。"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031401450.ogg"
    lhx "反正凉君你就是个萝莉控。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031401460.ogg"
    lhx "成熟的我已经脱离这个范围了。"
    me01 "不如说你才是最适合“萝莉”这个词的人。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031401470.ogg"
    lhx "竟然是这么一回事！"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031401480.ogg"
    lhx "请不要用下流的眼神看我。"
    me01 "完全搞不懂你在说什么。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_a1
    play voice "voice/立花希/031401490.ogg"
    lhx "我说的是凉君你真的觉得这样就可以了吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031401500.ogg"
    lhx "你应该也清楚才对。"
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031401510.ogg"
    lhx "不只有和璃之助道别这一条路。"
    show lhx_dsf_b1 b1 b1_a1
    play voice "voice/立花希/031401520.ogg"
    lhx "应该还有其他的选择......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "也许正如立花老师所说的，只要我坚持的话......琉璃说不定就能留下来了。"
    "但是我不能因为自己的私心就去干涉琉璃的生活。"
    "在我的眼中，她一直都是无时无刻不为别人着想的。"
    "所以这次......我也相信她的决定。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day220'
    $ seen_day220_street_event01 = False
    $ seen_day220_school_event01 = False
    $ seen_day220_yjroom_event01 = False
    $ seen_day220_bridge_event02 = False

label day220.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day220':
        $ flcam.move(*overworld.camera_positions['bridge'])
    elif _overworld_label == 'day220.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'])
    elif _overworld_label == 'day220.school_event01':
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day220.yjroom_event01':
        $ flcam.move(*overworld.camera_positions['rocket'])
    elif _overworld_label == 'day220.bridge_event02':
        $ flcam.move(*overworld.camera_positions['bridge'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    if _overworld_label == 'day220':
        window mode map
        me01 "先去和琉璃她们道别吧......" nointeract
    else:
        window mode map
        me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        road2=("day220.street_event01", "not seen_day220_street_event01"),
        school=("day220.school_event01", "seen_day220_street_event01 and not seen_day220_school_event01"),
        rocket=("day220.yjroom_event01", "seen_day220_street_event01 and not seen_day220_yjroom_event01"),
        bridge=("day220.bridge_event02", "seen_day220_yjroom_event01 and not seen_day220_bridge_event02"))
    $ window_animate_outro()
    if _return == 'day220.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day220.school_event01':
        $ flcam.move(*overworld.camera_positions['school'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day220.yjroom_event01':
        $ flcam.move(*overworld.camera_positions['rocket'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day220.bridge_event02':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day220.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street snow day city1 xuejian
    play music second_111 fadein 3.0 if_changed
    with dissolve
    "车站前聚集了很多人。"
    "除了几个熟悉的身影外，还有许多不认识的同学。"
    "大家也是来为友加和琉璃送行的。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.3
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021400840.ogg"
    yj "翔子，下次见面的时候就是春天了吧。"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011400360.ogg"
    xz "春天友加就会回来了吗？"
    show yj_dsf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021400850.ogg"
    yj "只要心里想着，一定很快就可以见面了~"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011400370.ogg"
    xz "友加这次要去的地方很远吧？"
    show yj_dsf_b2 b2 b2_a2
    play voice "voice/植澄友加/021400860.ogg"
    yj "想我的话就打个电话、或者偶尔写写信也不错，还挺新鲜的。"
    show xz_dsf_b3 b3 b3_h1
    play voice "voice/翔子/011400380.ogg"
    xz "友加你还是那么乐观啊，让我都觉得自己有些担心过头了。"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_h2 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/021400870.ogg"
    yj "因为这不是什么悲伤的离别。一定很快就能再见到翔子还有大家了。"
    show yj_dsf_b1 b1 b1_h1
    play voice "voice/植澄友加/021400880.ogg"
    yj "而且......"
    hide xz_dsf_b3
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_h1 onlayer m1:
        xpos 0.3
    "友加向远处匆匆赶来的我和立花希挥了挥手。"
    show yj_dsf_b2 b2 b2_s1
    yj "......"
    show yj_dsf_b2 b2 b2_c1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021400900.ogg"
    yj "明明不该伤感的，却还是忍不住哭了。"
    stop music fadeout 5.0
    pause 0.5 hard
    hide yj_dsf_b2
    $ flcam.move(2250, 0, 750, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    show shy_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041412960.ogg"
    liuli "啊，是前辈~"
    pause 0.5 hard
    play sound jiaobu2
    show liuli_dsf_b3 b3 b3_n1 at walkout_l(0.5)
    pause 0.5 hard
    hide liuli_dsf_b3
    hide shy_yjf_b1
    play music second_157 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_h1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/041412970.ogg"
    liuli "前辈你是来给我们送行的吗？"
    me01 "那是当然的。"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041412980.ogg"
    liuli "刚才藤原瞳同学也来了。稍微说了一些话她就回去了。"
    show liuli_dsf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041412990.ogg"
    liuli "她临走之前说了“我是个会解读气氛的女人”之类的话。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041413000.ogg"
    liuli "而且不光是藤原瞳同学，其他的同学也来了。"
    show liuli_dsf_b3 b3 b3_n1
    play voice "voice/琉璃/041413010.ogg"
    liuli "明明我以前和班里的大家都不怎么熟悉，完全没有想到他们也会来。"
    me01 "虽然已经说了很多次了，但是我还是想要再说一次。"
    me01 "这不是最后的离别。"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041413030.ogg"
    liuli "是的，这不是最后的离别~"
    play voice "voice/琉璃/041413040.ogg"
    liuli "我一定会回到你身边。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041413050.ogg"
    liuli "虽然不知道要过多久，但是一定会再见的......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_h1
    play voice "voice/琉璃/041413060.ogg"
    liuli "即使之后只有我一个人，也一定也会好好地完成任务给你看。"
    play voice "voice/琉璃/041413070.ogg"
    liuli "我从前辈那里得到了很多美好的回忆。"
    play voice "voice/琉璃/041413090.ogg"
    liuli "如此看来我离成熟的女性又更进一步了！"
    pause 0.5 hard
    hide liuli_dsf_b3
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151405020.ogg"
    shy "我把花山院交给你说不定是个错误的决定。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041413100.ogg"
    liuli "圣护院小姐，多亏了前辈我才下定了决心，这绝对不是什么错误的决定。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151405030.ogg"
    shy "真是这样吗？"
    show liuli_dsf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041413110.ogg"
    liuli "绝对绝对~是大成功的说！"
    show shy_yjf_b1 b1 b1_a1
    play voice "voice/圣护院/151405060.ogg"
    shy "神野君，万一出了什么事对计划造成影响星天宫将会全力以赴铲除你，这点你没忘记吧？"
    me01 "是的......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151405070.ogg"
    shy "花山院也是，暴走要适可而止。"
    show liuli_dsf_b2 b2 b2_ga4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041413180.ogg"
    liuli "这、这才不是暴走！"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151405080.ogg"
    shy "差不多到时间了，我们走吧。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041413190.ogg"
    liuli "啊，好的。"
    hide shy_yjf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n1
    play voice "voice/琉璃/041413200.ogg"
    liuli "前辈......那么我走了。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041413210.ogg"
    liuli "到了之后我会给你打电话的。"
    me01 "想我的话随时都可以联系我。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151405090.ogg"
    shy "......真是的。"
    show liuli_dsf_b2 b2 b2_h1
    play voice "voice/琉璃/041413320.ogg"
    liuli "前辈，谢谢你能来送行。"
    play voice "voice/琉璃/041413330.ogg"
    liuli "我们出发了~"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    play ambience1 train fadein 3.0
    "随着列车的轰鸣声，我送走了与我朝夕相伴的伙伴们。"
    "与儿时在车站饯别翔子的场景不同，此刻的我们并没有对流星许下心愿。"
    "并不是没有愿望，而是我们知道这个愿望将由我们亲手实现。"
    "与此同时，这份重逢的约定也乘着这飞舞的白雪，飘向远方......"
    stop ambience1 fadeout 3.0
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day220_street_event01:
        $ seen_day220_street_event01 = True
    $ _overworld_label = 'day220.street_event01'
    jump day220.map

label day220.school_event01:
    if not seen_day220_yjroom_event01:
        nvl clear
        pcenter "几天后......"
        pause 1.0 hard
        nvl clear
        with dissolve
    $ flcam.move(0, 0, 0)
    scene set only school snow day center room xuejian
    show snow_level1 onlayer texture
    with slowdissolve
    pause 1.0 hard
    me01 "没想到只是几天不见就开始想念了。"
    me01 "没有琉璃的中庭长椅，还真是除了凄凉什么都不剩了。"
    play voice "voice/藤原瞳/131400860.ogg"
    stranger "顺带一提我也在~"
    play music second_119 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    me01 "你还真是阴魂不散啊。"
    show tyt_wnf_b1 b1 b1_n1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131400870.ogg"
    tyt "吡~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    play sound fly1
    show alu_ct_b2 b2 b2_1 onlayer m2 at fly(0.5):
        xpos 0.7
    play voice "voice/藤原瞳/131400880.ogg"
    tyt "阿露也在。"
    me01 "不要把它带来学校啊！"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131400890.ogg"
    tyt "如果是这样的话那我也会和阿露一起消失的，毕竟我是个会解读气氛的女人。"
    me01 "我真实越来越搞不懂你了......"
    hide alu_ct_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131400900.ogg"
    tyt "欸~"
    me01 "别用那种无辜的眼神看我。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131400920.ogg"
    tyt "相比之下花山院她一下课就会立刻来这里。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131400930.ogg"
    tyt "就这么想见到前辈你吗。"
    me01 "毕竟我们约好了一起吃午饭。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131400970.ogg"
    tyt "就当是这样吧。"
    me01 "为什么我非得和你这家伙说这些往事不可啊？"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131400980.ogg"
    tyt "噗哈~"
    me01 "我可以发火了吗？！"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131400990.ogg"
    tyt "阿露。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    pause 0.5 hard
    play sound fly1
    show alu_ct_b7 b7 b7_1 onlayer m2 at fly(0.5):
        xpos 0.7
    me01 "你要干嘛？"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131401000.ogg"
    tyt "防卫手段。"
    me01 "区区一只仿制天鹅能阻止得了我？"
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/131401010.ogg"
    tyt "看来你是想被阿露的火焰烤焦脑袋。"
    me01 "做得到的话那放马过来吧！"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    hide alu_ct_b7
    show alu_ct_b10 b10 b10_2 onlayer m2 at fly(0.5):
        xpos 0.7
    play voice "voice/藤原瞳/131401020.ogg"
    tyt "好冷、好困......"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131401030.ogg"
    tyt "阿露。"
    play sound fly1
    hide alu_ct_b10
    show alu_ct_b2 b2 b2_1 onlayer m2 at fly_away(0.5):
        xpos 0.7
    pause 0.5 hard
    hide alu_ct_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "不是要打架吗？"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131401040.ogg"
    tyt "我可是比前辈稳重得多了。"
    me01 "你是来搞笑的吗？"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131401050.ogg"
    tyt "前辈好肤浅~"
    me01 "......"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131401060.ogg"
    tyt "吾非肤浅之辈~"
    me01 "已经懒得吐槽你了。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131401120.ogg"
    tyt "无论是什么我都能看穿，毕竟我也是个重要的伏笔角色。"
    me01 "所以说这就是你的{rb}灵纹{/rb}{rt}rune{/rt}吗？"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131401130.ogg"
    tyt "你中二病犯了吗？"
    me01 "......"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131401140.ogg"
    tyt "中二病只有在国中二年级之前才可以被原谅。"
    me01 "在激怒我这方面你果然是天才啊！"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131401180.ogg"
    tyt "明明之前还和花山院在桥下战斗过的。"
    me01 "这你也知道了？"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.15, 20, 2):
        xpos 0.5
    play voice "voice/藤原瞳/131401190.ogg"
    tyt "收集情报对我来说是小菜一碟......咯咯咯咯~"
    me01 "所以说你到底是谁？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131401270.ogg"
    tyt "无论是人类、动物、花草甚至是机械，寄宿在其中的灵魂皆为平等，这是神明大人给予的教诲。"
    play voice "voice/藤原瞳/131401280.ogg"
    tyt "所以在我眼中的花山院无论如何都是不会改变的。"
    play voice "voice/藤原瞳/131401290.ogg"
    tyt "即使分开了也一样。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131401300.ogg"
    tyt "我希望自己无论何时都是花山院最好的朋友。"
    me01 "你拿错剧本了吧喂！"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131401310.ogg"
    tyt "而在我眼中的前辈永远是一个中二少年。"
    me01 "果然我还是不擅长应付你这样的家伙......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day220_school_event01:
        $ seen_day220_school_event01 = True
    $ _overworld_label = 'day220.school_event01'
    if seen_day220_bridge_event02:
        jump day222
    jump day220.map

label day220.yjroom_event01:
    if not seen_day220_school_event01:
        nvl clear
        pcenter "几天后......"
        pause 1.0 hard
        nvl clear
        with dissolve
    $ flcam.move(0, 0, 0)
    scene set only home night yj_room xuejian
    with slowdissolve
    pause 1.0 hard
    play sound open_door6
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021215210.ogg"
    yj "......啊咧？"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021215220.ogg"
    yj "姐姐？"
    play music second_124 fadein 3.0 if_changed
    $ flcam.move(2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/圣护院/151201610.ogg"
    shy "是我......我回来了。"
    play voice "voice/植澄友加/021215230.ogg"
    yj "......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151201630.ogg"
    shy "这么说来，我还是第一次对你说“我回来了”这样的话吧？"
    play voice "voice/圣护院/151201640.ogg"
    shy "友加你会被吓一跳也是情理之中的事。"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021215240.ogg"
    yj "啊不、不是那样的。"
    show shy_yjf_b1 b1 b1_s1
    shy "......"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021215250.ogg"
    yj "姐姐？"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151201660.ogg"
    shy "......我就直接告诉你吧。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151201670.ogg"
    shy "之后我可能暂时回不来了。"
    show yj_dsf_b1 b1 b1_sp1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021215260.ogg"
    yj "......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151201680.ogg"
    shy "我必须暂时住在研究中心那里。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151201690.ogg"
    shy "虽然很抱歉如此地突然，但今晚我就必须收拾行李，明天出发。"
    play voice "voice/圣护院/151201700.ogg"
    shy "至于你......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151201710.ogg"
    shy "就暂时继续留在这里生活吧。"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021215280.ogg"
    yj "......"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151201720.ogg"
    shy "没必要勉强自己跟过来的。"
    show yj_dsf_b2 b2 b2_s1
    play voice "voice/植澄友加/021215290.ogg"
    yj "......"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151201730.ogg"
    shy "我没有理由再一次把你也带走。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151201740.ogg"
    shy "我要说的就是这些......"
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1 at walkout_r(0.7)
    pause 0.5 hard
    hide shy_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b2 b2 b2_c1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021215310.ogg"
    yj "等等啊姐姐......等等！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day220_yjroom_event01:
        $ seen_day220_yjroom_event01 = True
    $ _overworld_label = 'day220.yjroom_event01'
    jump day220.map

label day220.bridge_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    play music second_131 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    "天空充满了阴霾。"
    "从午后开始就一直是这个状态了。"
    pause 1.0 hard
    scene set only bridge evening under xuejian2
    with dissolve
    pause 2.0 hard
    scene set only yj_cg under normal
    with slowdissolve
    pause 1.0 hard
    me01 "友加？"
    me01 "你怎么一个人回来了？"
    me01 "发生什么事了吗？"
    pause 0.1 hard
    scene set only yj_cg under sad
    with dissolve
    play voice "voice/植澄友加/021215320.ogg"
    yj "......"
    pause 0.1 hard
    scene set only yj_cg under normal2
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021215340.ogg"
    yj "“我没有理由再一次把你也带走”。"
    pause 0.1 hard
    scene set only yj_cg under sad2
    with dissolve
    play voice "voice/植澄友加/021215350.ogg"
    yj "姐姐她是这么说的。"
    pause 0.1 hard
    scene set only yj_cg under normal2
    with dissolve
    play voice "voice/植澄友加/021215360.ogg"
    yj "姐姐她。"
    play voice "voice/植澄友加/021215370.ogg"
    yj "刚踏上宇宙研发道路的时候，我是真的很替她高兴的。"
    play voice "voice/植澄友加/021215380.ogg"
    yj "但是渐渐地......姐姐她变了。工作成了她唯一的在乎的东西。"
    play voice "voice/植澄友加/021215390.ogg"
    yj "自从来到雪见市之后，她就开始不停地埋头于气象工作的研究当中。"
    pause 0.1 hard
    scene set only yj_cg under sad2
    with dissolve
    play voice "voice/植澄友加/021215420.ogg"
    yj "而现在姐姐她又一次回到宇宙研发中心。"
    play voice "voice/植澄友加/021215440.ogg"
    yj "可这一次......她却选择把我也抛下。"
    pause 0.1 hard
    scene set only yj_cg under normal
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "友加说着，再一次将手里的草船放入河中。"
    "任凭它飘向远方。"
    pause 0.1 hard
    scene set only yj_cg under sad3
    with dissolve
    play voice "voice/植澄友加/021215450.ogg"
    yj "是因为对她来说身为{rb}灵继者{/rb}{rt}elfin{/rt}的我已经没用了，所以才不带我一起的吗？"
    play voice "voice/植澄友加/021215460.ogg"
    yj "果然，如果不是{rb}灵继者{/rb}{rt}elfin{/rt}的我就没有价值了吗。"
    me01 "不是这样的。"
    me01 "圣护院小姐也一定有她的苦衷。"
    play voice "voice/植澄友加/021215470.ogg"
    yj "嗯，我也希望自己能够这样想。"
    play voice "voice/植澄友加/021215480.ogg"
    yj "明明凉君都那么努力地帮助我了。"
    play voice "voice/植澄友加/021215490.ogg"
    yj "但是，姐姐她却......"
    pause 0.1 hard
    scene set only yj_cg under normal3
    with dissolve
    play voice "voice/植澄友加/021215500.ogg"
    yj "我已经......搞不懂该怎么办了。"
    play voice "voice/植澄友加/021215510.ogg"
    yj "搞不懂姐姐到底在想些什么。"
    pause 0.1 hard
    scene set only yj_cg under sad3
    with dissolve
    play voice "voice/植澄友加/021215520.ogg"
    yj "搞不懂我是否应该继续追随她的身影了。"
    play voice "voice/植澄友加/021215530.ogg"
    yj "已经......什么都搞不懂了。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 1.0 hard
    scene set only laboratory inside2 xuejian
    show sepiagrain onlayer texture
    play music second_138 fadein 3.0 if_changed
    $ flcam.move(-2250, -350, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.3
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020105690.ogg"
    yj "就是无论我变成什么样子都无所谓的意思吧？"
    play voice "voice/植澄友加/020105700.ogg"
    yj "就算我现在觉醒成了{rb}灵继者{/rb}{rt}elfin{/rt}也是一样的吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100960.ogg"
    shy "啊......什么都不会改变。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100970.ogg"
    shy "无论多少次我都会这么说的，因为你是就我的独一无二的妹妹。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene white 
    with slowerdissolve
    pause 2.0 hard
    "那个时候我觉得，圣护院小姐说的这句话是出于对妹妹的关心，与{rb}灵继者{/rb}{rt}elfin{/rt}的身份无关。"
    "直到现在我也如此坚信着。"
    "所以这次也一定也是这样的。"
    "“无论多少次我都会这么说的，因为你是就我的独一无二的妹妹”。"
    "这句话中一定隐含着什么更重要的东西。"
    pause 1.0 hard
    scene set only yj_cg under normal
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021217430.ogg"
    yj "姐姐曾对我说过，我们是一样的。"
    pause 0.1 hard
    scene set only yj_cg under smile
    with dissolve
    play voice "voice/植澄友加/021217440.ogg"
    yj "但是好奇怪，明明不可能是那样的。"
    play voice "voice/植澄友加/021217450.ogg"
    yj "因为我总是笨手笨脚的，头脑也不聪明。"
    pause 0.1 hard
    scene set only yj_cg under happy
    with dissolve
    play voice "voice/植澄友加/021217460.ogg"
    yj "甚至到了需要补考的那种程度。"
    pause 0.1 hard
    scene set only yj_cg under smile
    with dissolve
    play voice "voice/植澄友加/021217470.ogg"
    yj "相比之下我的姐姐她，从以前开始就很优秀。"
    play voice "voice/植澄友加/021217480.ogg"
    yj "无论什么事都能做得很好，头脑也很优秀......对作为妹妹的我而言，姐姐她一直都是我的骄傲。"
    pause 0.1 hard
    scene set only yj_cg under normal
    with dissolve
    play voice "voice/植澄友加/021217490.ogg"
    yj "而相对的......也让我感到了同等程度的自卑。"
    pause 0.1 hard
    scene set only yj_cg under sad
    with dissolve
    play voice "voice/植澄友加/021217500.ogg"
    yj "我开始思考，为什么自己不能像姐姐一样？"
    play voice "voice/植澄友加/021217510.ogg"
    yj "我之所以会喜欢上跑步，一定也是因为这方面的缘故。"
    pause 0.1 hard
    scene set only yj_cg under normal
    with dissolve
    play voice "voice/植澄友加/021217520.ogg"
    yj "因为在奔跑的过程中，我就可以什么忘掉那些烦恼。"
    play voice "voice/植澄友加/021217530.ogg"
    yj "那些和姐姐有关的烦恼都可以抛之脑后了。"
    pause 0.1 hard
    scene set only yj_cg under normal3
    $ flcam.move(-1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021217540.ogg"
    yj "但是......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge evening under xuejian2
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_tcf_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021217560.ogg"
    yj "草船的制作方法，就是我从姐姐那里学的。"
    show yj_tcf_b1 b1 b1_s1
    play voice "voice/植澄友加/021217570.ogg"
    yj "虽然都是孩童时期的事情了。"
    show yj_tcf_b1 b1 b1_n1
    play voice "voice/植澄友加/021217580.ogg"
    yj "那时的姐姐还不像现在这样，还是可以一直陪在我的身边。"
    me01 "果然是这样。"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021217590.ogg"
    yj "果然？"
    me01 "就在刚才友加你制作草船的时候我就在想了。"
    me01 "一定有什么是你和你姐姐最为珍贵的回忆。"
    me01 "对她来说一定也是一样的。"
    show yj_tcf_b2 b2 b2_ga3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021217600.ogg"
    yj "啊哈哈，也许是这样没错。一旦动起手制作草船就会不自觉地想起来当时的场景。"
    show yj_tcf_b2 b2 b2_s2
    play voice "voice/植澄友加/021217610.ogg"
    yj "因为我头脑不好，总是记不住制作方法。"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021217620.ogg"
    yj "即使好不容易记住了，也会因为笨手笨脚的缘故总是做不好。"
    me01 "但是不管怎么样，圣护院小姐她都会一直教你的对吧？"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show yj_tcf_b1 b1 b1_n1
    play voice "voice/植澄友加/021217630.ogg"
    yj "嗯。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg under smile2
    with dissolve
    play voice "voice/植澄友加/021217640.ogg"
    yj "那时的我们，关系真的很要好。"
    play voice "voice/植澄友加/021217650.ogg"
    yj "我也总是跟在姐姐的身后。"
    play voice "voice/植澄友加/021217660.ogg"
    yj "姐姐也很照顾我。"
    pause 0.1 hard
    scene set only yj_cg under happy2
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021217670.ogg"
    yj "真的，一直一直......在一起的。"
    me01 "莫非友加你所说的故乡，就是现在的星天宫宇宙研究中心吗？"
    play voice "voice/植澄友加/021217720.ogg"
    yj "嗯，是同样坐落在宇宙研究中心的小岛上的城市。"
    hide yj_tcf_b1
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg memory
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021217730.ogg"
    yj "所以火箭撕裂湛蓝的天空飞向远方的场景......我一直都记得。"
    play voice "voice/植澄友加/021217740.ogg"
    yj "和姐姐一起仰望的那边蓝天，一直以来也都历历在目。"
    play voice "voice/植澄友加/021217750.ogg"
    yj "以前我总是央求着她，就说“去看吧去看吧”这样的。"
    play voice "voice/植澄友加/021217760.ogg"
    yj "而姐姐也总是同意陪我同行。"
    play voice "voice/植澄友加/021217770.ogg"
    yj "比起火箭，她的眼里更多的是对火箭痴狂的我。"
    play voice "voice/植澄友加/021217780.ogg"
    yj "就这样陪着我，和我一起感叹着那句“好厉害”。"
    pause 0.1 hard
    $ flcam.move(-2200, -1400, 800, duration=3.0, warper='ease_quad')
    play voice "voice/植澄友加/021217790.ogg"
    yj "姐姐她总是问我，“友加你喜欢火箭吗”。"
    play voice "voice/植澄友加/021217800.ogg"
    yj "虽然我不太懂复杂的事情。"
    play voice "voice/植澄友加/021217810.ogg"
    yj "但只要想着那火箭能够飞向天空的彼端。"
    play voice "voice/植澄友加/021217820.ogg"
    yj "想着将来有一天，能够去往别的星星之上时。"
    play voice "voice/植澄友加/021217830.ogg"
    yj "就觉得那是非常、非常棒的事情。"
    play voice "voice/植澄友加/021217840.ogg"
    yj "宇宙也好、火箭也是......我都最喜欢了。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/植澄友加/021217850.ogg"
    yj "和姐姐一起仰望火箭的那些瞬间......我都最喜欢了。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only bridge evening under xuejian2
    show yj_tcf_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/植澄友加/021217860.ogg"
    yj "所以当我得知姐姐踏上了宇宙研发的道路时，我真的很开心。"
    show yj_tcf_b1 b1 b1_s1
    play voice "voice/植澄友加/021217870.ogg"
    yj "但是一提到工作，姐姐就变了。"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021217880.ogg"
    yj "把姐姐变成这样的......宇宙研发计划，也不再让我感兴趣了。"
    play voice "voice/植澄友加/021217890.ogg"
    yj "姐姐她也一定，不记得曾经的那种感觉了。"
    play voice "voice/植澄友加/021217900.ogg"
    yj "我们已经无法......再回到过去了。"
    show yj_tcf_b2 b2 b2_ga3 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/021217910.ogg"
    yj "对不起呢，说了奇怪的话~"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021217920.ogg"
    yj "......"
    me01 "我们出发吧！"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show yj_tcf_b1 b1 b1_sp1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021217930.ogg"
    yj "欸？！"
    "我拉起了友加的手。"
    play voice "voice/植澄友加/021217940.ogg"
    yj "凉、凉君？"
    me01 "谢谢你告诉了我这么重要的事情。"
    me01 "那么现在可以陪我去个地方吗？"
    show yj_tcf_b1 b1 b1_s2
    play voice "voice/植澄友加/021217950.ogg"
    yj "约、约会？"
    me01 "是啊。"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021217960.ogg"
    yj "可、可是我......"
    me01 "讨厌和我约会吗？"
    show yj_tcf_b2 b2 b2_s2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021217990.ogg"
    yj "不、不是这样的......"
    me01 "把你想要对姐姐说的话全都说出来吧。"
    me01 "不然的话对方是永远也不会明白的。"
    me01 "毕竟和友加不同，你的姐姐她......"
    me01 "在这方面就是个不折不扣的大笨蛋啊！"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day220_bridge_event02:
        $ seen_day220_bridge_event02 = True
    $ _overworld_label = 'day220.bridge_event02'
    if seen_day220_school_event01:
        jump day221
    jump day220.map
    
