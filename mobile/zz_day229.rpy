
label day229:
    bookmark
    $ save_name = _("Day 229")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date228 onlayer m1 at backend_date2
    pause 5.0 hard
    $ suppress_overlay = False
    scene black
    with dissolve
    pause 3.0 hard
    "又和希菲尔在梦中相遇了。"
    "最近一直重复着这样的梦。"
    pause 1.0 hard
    scene set only home day my_room xuejian
    play music second_124 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    me01 "......希菲尔？"
    "醒来之后，怀里的温度消失了。"
    "环视四周都找不到希菲尔的身影。"
    window mode through
    "「希菲尔」离开队伍。"
    pause 1.0 hard
    scene set only sky day xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "现在是二月中旬。"
    "只剩下不到一个月的时间春天就会到来。"
    "如果正如梦里希菲尔所说的那样。"
    "为了躲避冰雪消融的春天，希菲尔她也不得不躲起来。"
    "不管怎么样，先试着找到她吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 1.0 hard
    $ _overworld_label = 'day229'
    $ seen_day229_balltower_event01 = False
    $ seen_day229_home_event01 = False

label day229.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    show snow_level1 onlayer fg
    if _overworld_label == 'day229':
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day229.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    if _overworld_label == 'day229':
        window mode map
        me01 "想想希菲尔最有可能去的地方是哪里吧......" nointeract
    else:
        window mode map
        me01 "赶紧带着希菲尔回家......" nointeract
    call screen rughzenhaide(
        cloqks=("day229.balltower_event01", "not seen_day229_balltower_event01"),
        road1=("day229.home_event01", "seen_day229_balltower_event01 and not seen_day229_home_event01"))
    $ window_animate_outro()
    if _return == 'day229.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day229.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day229.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    play music second_103 fadein 3.0 if_changed
    with dissolve
    pause 2.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory6
    with slowdissolve
    pause 1.0 hard
    "不出我所料，在钟楼下方坐着的正是那个熟悉的身影。"
    "就像要将自己的歌声献给钟楼一般，此时的她正抬头哼着歌。"
    "曾经希菲尔说过。"
    "她很羡慕这能够记录时间轨迹的钟楼。"
    "不变且永恒。"
    "这也许就是她所憧憬的理由吧。"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer texture
    with dissolve
    pause 1.0 hard
    me01 "找到你了，希菲尔。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    "听到我的话，希菲尔并没有像上次那样朝我跑来。"
    "而是缓缓地转过身。"
    "那动作明显比以往还要疲惫许多。"
    pause 1.0 hard
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001009910.ogg"
    xfe "嗯......被找到了~"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_ga3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    "说完她依旧起身打算朝我的方向走来。"
    "可是......"
    pause 0.5 hard
    play sound enjoy_snow1
    show ts_xfe_yjz_b2 b2 b2_sp2:
        xpos 0.5 ypos 1.0 alpha 1.0
        parallel:
            linear 0.5 ypos 1.05
        parallel:
            linear 0.5 alpha 0.0
    with vpunch
    pause 0.75 hard
    "噗嗤。"
    "又一次在途中摔倒了。"
    me01 "......没事吧？"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day big2
    show snow_level1 onlayer texture
    with dissolve
    pause 1.0 hard
    "这一次希菲尔并没有靠自己的力量重新站起来。"
    "莫非她的身体状况已经恶化到连站起身的力气都没有了吗。"
    "想到这里我连忙跑到了希菲尔的跟前将她抱了起来。"
    play sound touch
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play music second_129 fadein 3.0 if_changed
    scene set only xfe_cg touch4
    with dissolve
    "滚烫的温度透过希菲尔的身体传了过来。"
    "她一直都是......这样勉强自己的吗？"
    play voice "voice/希菲尔/001009920.ogg"
    xfe "哈啊、哈......"
    "就连呼吸都带着热气。"
    "脸颊也赤红一片。"
    "这种症状对我而言并不陌生。"
    "就像是过去“梦”住院的时候也能偶尔从她身上察觉到这样微妙的温度。"
    "为什么？"
    "这是什么的前兆吗？"
    "希菲尔的身上将要发生的到底是什么。"
    "{rb}灵纹{/rb}{rt}rune{/rt}的暴走吗？"
    "还是说......"
    pause 0.1 hard
    scene set only xfe_cg touch6
    with dissolve
    play voice "voice/希菲尔/001009930.ogg"
    xfe "凉君，露出那样的表情是发生什么事了吗？"
    play voice "voice/希菲尔/001009940.ogg"
    xfe "发生了什么......痛苦的事吗？"
    me01 "这应该是我要说的话才对。"
    me01 "希菲尔你一直对我隐瞒着什么。"
    me01 "那个可怕的噩梦究竟是怎么回事？"
    me01 "为什么现在的你，已经到了连站起来的力气也没有了？"
    pause 0.1 hard
    scene set only xfe_cg touch7
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001009950.ogg"
    xfe "希菲尔我不要紧的......只是身子有些暖呼呼的，快要融化的感觉。"
    play voice "voice/希菲尔/001009960.ogg"
    xfe "不过多亏了凉君，我也渐渐开始喜欢上这种暖呼呼的感觉了。"
    me01 "这一切都是因为我才造成的吗？"
    me01 "是因为我强行让希菲尔陪在我的身边才害得你变成现在这样的吗？"
    play voice "voice/希菲尔/001009970.ogg"
    xfe "不是的。"
    play voice "voice/希菲尔/001009980.ogg"
    xfe "希菲尔会变成这样，是从一开始就注定了的。"
    play voice "voice/希菲尔/001010000.ogg"
    xfe "所以......请不要露出那样的表情。"
    play voice "voice/希菲尔/001010010.ogg"
    xfe "凉君痛苦的话，希菲尔也会痛苦的。"
    play voice "voice/希菲尔/001010020.ogg"
    xfe "凉君能保持笑容的话，希菲尔也能保持笑容了。"
    play voice "voice/希菲尔/001010030.ogg"
    xfe "只要看着这样的凉君，希菲尔就觉得一切都会没事的。"
    play voice "voice/希菲尔/001010040.ogg"
    xfe "只要有凉君在身边陪着的话，就更是如此了。"
    play voice "voice/希菲尔/001010050.ogg"
    xfe "所以......拜托了。"
    pause 0.1 hard
    scene set only xfe_cg touch2
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010060.ogg"
    xfe "请让希菲尔一直看着凉君微笑时的样子。"
    play voice "voice/希菲尔/001010070.ogg"
    xfe "也希望凉君见到希菲尔的时候，我也能一直是微笑着的样子。"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black
    with dissolve
    pause 1.0 hard
    if not seen_day229_balltower_event01:
        $ seen_day229_balltower_event01 = True
    $ _overworld_label = 'day229.balltower_event01'
    jump day229.map

label day229.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only home snow day outside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111001280.ogg"
    aiyi "小希菲尔她......身体不舒服吗？"
    play music second_140 fadein 3.0 if_changed
    $ flcam.move(2250, 0, 750, duration=1.5)
    show xz_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011001530.ogg"
    xz "好像是这样的......不过，有神野君陪着的话就不要紧的。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111001290.ogg"
    aiyi "爱衣也想为小希菲尔做点什么。"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011001540.ogg"
    xz "那样的话就和往常一样去上幼儿园吧。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111001300.ogg"
    aiyi "不是留下来帮忙吗？"
    show xz_dsf_b2 b2 b2_s2
    play voice "voice/翔子/011001550.ogg"
    xz "嗯，如果不只是神野君就连我们也一起来帮忙的话，反而会让希菲尔在意的。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011001560.ogg"
    xz "通过这几个月与希菲尔的相处我也明白了这一点。"
    hide aiyi_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_s1
    play voice "voice/翔子/011001570.ogg"
    xz "希菲尔她希望大家都能像往常一样生活。"
    play voice "voice/翔子/011001580.ogg"
    xz "喜欢看着大家平凡的每一天。"
    show xz_dsf_b3 b3 b3_n1
    play voice "voice/翔子/011001590.ogg"
    xz "所以希菲尔她才一直小心翼翼地不让自己闯入我们的生活中来。"
    play voice "voice/翔子/011001600.ogg"
    xz "不希望把{rb}灵纹{/rb}{rt}rune{/rt}带进谁的生活，我觉得说的就是这样的状态吧。"
    play voice "voice/翔子/011001610.ogg"
    xz "喜欢钟楼的初衷......我想也是出自这种心情吧。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    show xz_dsf_b3 b3 b3_h1
    play voice "voice/翔子/011001620.ogg"
    xz "所以我们大家为了希菲尔也要好好地过好每一天才行呢~"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111001310.ogg"
    aiyi "那小希菲尔她，是不是希望爱衣和大家把{rb}灵纹{/rb}{rt}rune{/rt}都抛弃掉呢？"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011001630.ogg"
    xz "虽然我也不太清楚，不过如果是希望大家能够过平凡的生活的话，的确可能是这样没错。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111001320.ogg"
    aiyi "大姐姐的话，如果春天降临的话会怎么办呢？"
    play voice "voice/爱衣/111001330.ogg"
    aiyi "会为了回归平凡的生活，而把{rb}灵纹{/rb}{rt}rune{/rt}抛弃掉吗？"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111001340.ogg"
    aiyi "还是说......是因为讨厌作为{rb}灵继者{/rb}{rt}elfin{/rt}的关系，才想要抛弃掉{rb}灵纹{/rb}{rt}rune{/rt}的呢？"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011001640.ogg"
    xz "爱衣，我的话两种都不是。"
    show xz_dsf_b3 b3 b3_h1
    play voice "voice/翔子/011001650.ogg"
    xz "好不容易才获得的{rb}灵纹{/rb}{rt}rune{/rt}，怎么可能说抛弃就抛弃掉呢。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111001350.ogg"
    aiyi "那样的话......"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011001660.ogg"
    xz "爱衣也一样的吧，正因为是自己的{rb}灵纹{/rb}{rt}rune{/rt}，所以不管是痛苦的回忆还是别的什么，都会尝试用自己的方式去面对。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011001670.ogg"
    xz "这就是平凡的生活——我们的日常所的蕴含的意义吧。"
    pause 1.0 hard
    hide snow_level1

label day229.myroom_event01:
    default seen_day229_memory_event01 = False
    default seen_day229_kitchen_event01 = False
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    pause 1.0 hard
    scene set only home day my_room xuejian
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dsf_b3 onlayer m2:
            hide screen investigation_popup
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            move _("外出") jump day229.kitchen_event01
            screen_direction left
            sleep jump day229.sleep

label day229.sleep:
    default seen_day229_sleep = False
    if not seen_day229_sleep:
        $ seen_day229_sleep = True
        stop music fadeout 5.0
        scene white 
        with slowerdissolve
        pause 1.0 hard
        jump day229.memory_event01
    elif not seen_day229_kitchen_event01:
        window mode thought
        me01 "先去看看有没有什么能够带给希菲尔的吧。"
        $ flcam.move(0, -100, 400, duration=3.0)
        pause 0.5 hard
        jump investigate
    else:
        jump day229.myroom_event02

label day229.memory_event01:
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    $ flcam.move(0, 0, 0)
    "雪花漫天飞舞。"
    "不会堆积的、温柔的雪，此刻却停留在了人们的心上。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory four
    play music second_131 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    me01 "希菲尔，你累了吗？"
    play voice "voice/希菲尔/001010080.ogg"
    xfe "嗯。"
    me01 "要休息一下吗？"
    play voice "voice/希菲尔/001010090.ogg"
    xfe "嗯。"
    pause 0.1 hard
    scene set only xfe_cg memory one
    with dissolve
    play voice "voice/希菲尔/001010100.ogg"
    xfe "对不起，凉君......"
    me01 "不要道歉。"
    play voice "voice/希菲尔/001010110.ogg"
    xfe "确实是这样的......比起道歉，感谢的话比较好呢。"
    pause 0.1 hard
    scene set only xfe_cg memory two
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010120.ogg"
    xfe "谢谢你，凉君......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg yuki ground
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "我在四周寻找着能够休息的地方。"
    "在雪原的尽头，有一棵高大挺拔的树。"
    "那是至今为止漫长的旅途中，除了我们以外唯一的生命了。"
    me01 "再坚持一下就好。"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowdissolve
    pause 1.0 hard
    play sound touch
    "我抱起了希菲尔，径直朝着大树的方向前进。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg touch4
    with slowdissolve
    pause 1.0 hard 
    "比之前还要滚烫的身体。"
    "稀薄的存在感。"
    pause 0.1 hard
    $ flcam.move(-1100, -1400, 450, duration=3.0, warper='ease_quad')
    "我一边遏制住自己内心的焦虑感，一边加快了步伐。"
    "此时漫天飘落的白雪也成为了前进路上的障碍。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white with slowerdissolve
    pause 2.0 hard
    "不知过了多久，我们终于抵达了雪原的尽头。"
    play music second_134 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg xuejian yume
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    "我将希菲尔安置在树下。"
    "自己则坐在了她的身边。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg tree one
    with slowdissolve
    me01 "希菲尔......这里的话可以吗？"
    play voice "voice/希菲尔/001010130.ogg"
    xfe "嗯。"
    me01 "好些了吗？"
    play voice "voice/希菲尔/001010140.ogg"
    xfe "嗯。"
    me01 "肚子会饿吗？"
    play voice "voice/希菲尔/001010150.ogg"
    xfe "嗯。"
    me01 "还有什么......是我能为你做的吗？"
    pause 0.1 hard
    scene set only xfe_cg tree four
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010170.ogg"
    xfe "对不起，凉君。"
    pause 0.1 hard
    scene set only xfe_cg tree two
    with dissolve
    play voice "voice/希菲尔/001010180.ogg"
    xfe "谢谢你，凉君......"
    play voice "voice/希菲尔/001010190.ogg"
    xfe "能陪着希菲尔......一起走到现在。"
    me01 "拜托了希菲尔，请不要再说这样寂寞的话。"
    me01 "不会就这么结束的。"
    me01 "未来的路，我们还要一起走下去的。"
    play voice "voice/希菲尔/001010200.ogg"
    xfe "......"
    "到底要怎么做，才能让希菲尔恢复元气呢？"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(2250, 300, 750)
    scene set only home night kitchen xuejian
    show sepiagrain onlayer texture
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    with dissolve
    play voice "voice/爱衣/111001120.ogg"
    aiyi "没能做成刨冰，抱歉。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001006110.ogg"
    xfe "没关系的，那个就当作是期待留到下次再吃吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg tree one
    with dissolve
    pause 1.0 hard
    me01 "希菲尔，你在这里等我一下。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day229_memory_event01:
        $ seen_day229_memory_event01 = True
    jump day229.myroom_event01

label day229.kitchen_event01:
    if not seen_day229_memory_event01:
        window mode thought
        me01 "这个时候还是不要随便跑出去比较好......"
        $ flcam.move(0, -100, 400, duration=3.0)
        pause 0.5 hard
        jump investigate
    if not seen_day229_kitchen_event01:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ seen_day229_kitchen_event01 = True
        scene black
        with slowdissolve
        pause 2.0 hard
        play sound close_door2
        $ flcam.move(0, 0, 0)
        scene set only home snow day outside xuejian
        with dissolve
        "我冲出了家门，目标是商店街。"
        "即使没有卖刨冰，但如果有制作刨冰的材料的话......"
        pause 1.0 hard
        scene black
        with slowerdissolve
        pause 2.0 hard
        $ flcam.move(0, 0, 0)
        scene set only sky day xuejian2
        with dissolve
        pause 1.0 hard
        "找遍商店街的每一个角落，终于买来了碎冰机和蜂蜜。"
        pause 1.0 hard
        scene set only home night kitchen xuejian
        $ flcam.move(0, -300, 900, duration=1.5)
        with dissolve
        pause 0.5 hard
        show xz_dsf_b1 b1 b1_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011001690.ogg"
        xz "神野君？"
        hide xz_dsf_b1
        show xz_dsf_b2 b2 b2_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011001700.ogg"
        xz "就觉得听到什么声音......你在这里做什么呢？"
        me01 "不好意思，打扰到你了。"
        hide xz_dsf_b2
        show xz_dsf_b1 b1 b1_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011001710.ogg"
        xz "这个倒没什么......这是刨冰？"
        me01 "是啊。"
        $ flcam.move(0, -300, 1000, duration=1.5)
        pause 0.5 hard
        show xz_dsf_b1 b1 b1_ga2
        play voice "voice/翔子/011001720.ogg"
        xz "为希菲尔做的吧？"
        me01 "是啊。"
        show xz_dsf_b1 b1 b1_h2
        play voice "voice/翔子/011001730.ogg"
        xz "用碗装可以吗？"
        me01 "翔子......"
        show xz_dsf_b1 b1 b1_h1
        play voice "voice/翔子/011001740.ogg"
        xz "我也来帮忙吧~"
        pause 0.5 hard
        show xz_dsf_b1 b1 b1_h1 at walkout_r(0.5)
        pause 0.5 hard
        hide xz_dsf_b1
        "翔子熟练地从碗柜里拿出了餐具。"
        pause 1.0 hard
        $ flcam.move(0, 0, 0)
        scene set only items ice1
        with slowdissolve
        pause 1.0 hard
        "在我和翔子的共同努力下，刨冰终于完成了。"
        pause 1.0 hard
        scene set only home night kitchen xuejian
        $ flcam.move(0, -300, 900, duration=1.5)
        with dissolve
        pause 0.5 hard
        show xz_dsf_b2 b2 b2_n1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011001750.ogg"
        xz "快点把这个拿给希菲尔吧，剩下的我会收拾的。"
        me01 "谢谢你翔子。"
        hide xz_dsf_b2
        show xz_dsf_b3 b3 b3_n1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011001760.ogg"
        xz "不用在意的，我也是、爱衣也是，大家都很担心希菲尔。"
        me01 "但如果因为自己的关系让大家担心的话，感觉希菲尔会更难过的。"
        show xz_dsf_b3 b3 b3_s1
        play voice "voice/翔子/011001790.ogg"
        xz "......神野君你这个大木头。（小声）"
        me01 "？"
        show xz_dsf_b3 b3 b3_s4
        play voice "voice/翔子/011001800.ogg"
        xz "我的{rb}共感{/rb}{rt}empathy{/rt}必须要和对方心意相通才能使用的。"
        show xz_dsf_b3 b3 b3_n1
        play voice "voice/翔子/011001880.ogg"
        xz "我想希菲尔也是一样的。"
        me01 "也就是说希菲尔她......"
        me01 "其实已经接受了大家的帮助吗？"
        me01 "她其实，也是希望自己能够被大家“找到”的。"
        $ flcam.move(0, -300, 1000, duration=1.5)
        pause 0.5 hard
        play voice "voice/翔子/011001890.ogg"
        xz "拜托你了，还需要刨冰的话我和爱衣也会帮忙准备的。"
        stop music fadeout 5.0
        pause 1.0 hard
        scene black 
        with slowerdissolve
        pause 1.0 hard
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night kitchen xuejian
        show xz_dsf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        $ flcam.move(0, -400, 600)
        $ flcam.move(0, -100, 400, duration=3.0)
        with dissolve
    else:
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night kitchen xuejian
        show xz_dsf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        $ flcam.move(0, -400, 600)
        $ flcam.move(0, -100, 400, duration=3.0)
        with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dsf_b3 onlayer m1:
            camera_pos (scale(2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction right
            move _("卧室") jump day229.myroom_event01

label day229.myroom_event02:
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    hide xz_dsf_b3
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    "刚刚翔子所说的{rb}共感{/rb}{rt}empathy{/rt}究竟是不是真的呢？"
    "难道希菲尔不是因为“不能”被大家找到，而是单纯的“不想”被大家找到吗？"
    "比起一个人玩耍，两个人的话会更开心......"
    "明明之前她一直是这么说的，可为什么又要一个人躲起来呢？"
    "芬布尔之冬、寂寞的雪原、追逐月亮的天狗、春天的降临......"
    "还有太多的谜题没有解开。"
    "不过现在的当务之急果然还是尽快让希菲尔恢复精神才是。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with side2cent_slow
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg xuejian yume
    play music second_131 fadein 3.0 if_changed
    show snow_level1 onlayer fg
    with cent2side
    pause 1.0 hard
    me01 "希菲尔，我拿刨冰来了。"
    "我用汤匙喂了希菲尔一口。"
    pause 1.0 hard
    hide snow_level1
    scene set only xfe_cg tree two
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010220.ogg"
    xfe "冰冰凉凉的，很好吃~"
    me01 "有稍微恢复一些了吗？"
    pause 0.1 hard
    scene set only xfe_cg tree three
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010230.ogg"
    xfe "嗯，肚子好饱。"
    play voice "voice/希菲尔/001010240.ogg"
    xfe "多亏了凉君，我也变得有精神了。"
    pause 0.1 hard
    scene set only xfe_cg tree one
    with dissolve
    play voice "voice/希菲尔/001010250.ogg"
    xfe "吃饱了的话......就变得想睡觉了。"
    pause 0.1 hard
    scene set only xfe_cg tree four
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "希菲尔闭上了双眼。"
    "还没有来得及问候一声就......再一次闭上了眼睛。"
    "安静地睡着了。"
    "因为太过平静的缘故，让我有种她再也不会醒来的错觉。"
    "想要呼唤她的名字。"
    "但又怕打扰到熟睡中的她。"
    "没错。"
    "这只是暂时的休息。"
    "足迹不会在这里中断。"
    "我们一定......还能继续向前迈进的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg xuejian yume
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "树叶发出“沙沙”的声音。"
    "没有感觉到风，却不停地摇曳着。"
    "那个声音好熟悉，仿佛是有谁在述说些什么一般。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    scene set only home day my_room xuejian
    with cent2side
    pause 1.0 hard
    "从梦中醒来后，我手中的刨冰早已融化。"
    pause 1.0 hard
    scene set only items ice2
    with dissolve
    pause 1.0 hard
    "再带更多过去吧。"
    "直到希菲尔恢复精神为止，不管多少次......"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day230
