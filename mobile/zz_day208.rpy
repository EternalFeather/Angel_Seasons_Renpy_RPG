label day208:
    bookmark
    $ save_name = _("Day 208")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    pause 2.0 hard
    show backend_date207 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    with slowdissolve
    play music second_114 fadein 3.0 if_changed
    pause 2.0 hard
    scene set only home day living_room xuejian
    with dissolve
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111500350.ogg"
    aiyi "呐大哥哥~"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111500360.ogg"
    aiyi "今天休息对吧？"
    me01 "是啊。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111500370.ogg"
    aiyi "大哥哥就算休息也要出门吗？"
    me01 "总觉得需要出去放松一下心情。"
    me01 "爱衣今天也要去幼儿园吧，抱歉这次不能陪你一起了。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    "我摸了摸她的头。"
    show aiyi_dzf_b1 b1 b1_ga2
    play voice "voice/爱衣/111500380.ogg"
    aiyi "没关系的，毕竟大哥哥也已经{rb}道过歉{/rb}{rt}摸头{/rt}了。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111500390.ogg"
    aiyi "晚上要早点回来哟~"
    me01 "我知道了。"
    "作为回报刚才的关心，我又一次抚摸了爱衣的头。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/爱衣/111500400.ogg"
    aiyi "诶嘿嘿~"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111500410.ogg"
    aiyi "大哥哥打算去做什么呢？"
    me01 "暂时没有什么安排，总之先去街上看看吧。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111500420.ogg"
    aiyi "也就是说......约会吗？"
    me01 "一人的话算不上约会吧。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111500430.ogg"
    aiyi "男孩子和女孩子一起出门的话，就是约会了。"
    me01 "要这么说的话，平日里我和爱衣也经常一起约会的。"
    show aiyi_dzf_b1 b1 b1_s2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/爱衣/111500440.ogg"
    aiyi "啊......真的耶。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111500450.ogg"
    aiyi "爱衣我，以前都没有约过会。"
    me01 "和我是第一次吗？"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111500460.ogg"
    aiyi "嗯，大哥哥收下了爱衣的第一次呢~"
    stop music fadeout 5.0
    pause 0.5 hard
    hide aiyi_dzf_b1
    play music second_104 fadein 3.0 if_changed
    $ flcam.move(3200, -1800, 1400, duration=1.5)
    pause 1.5 hard
    play sound bottle_drop
    with vpunch 
    pause 1.0 hard
    "从厨房里传来了盘子打翻的声音。"
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "刚才那番话对你翔子姐姐的精神卫生来说可能不太友好，所以我们还是跳过吧。"
    play voice "voice/爱衣/111500470.ogg"
    aiyi "精神卫生......是什么？"
    me01 "简单来说就是我可能会被误会的。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111500480.ogg"
    aiyi "那就不说了。"
    me01 "得救了。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111500490.ogg"
    aiyi "但是，大姐姐的第一次也是给的大哥哥呀~"
    pause 0.5 hard
    hide aiyi_dzf_b1
    $ flcam.move(3200, -1800, 1400, duration=1.5)
    pause 1.5 hard
    play sound bottle_drop
    with vpunch
    pause 1.0 hard
    "动静比刚才更大了！"
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "我还是去看看翔子的情况吧。"
    show aiyi_dzf_b1 b1 b1_sp1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/爱衣/111500500.ogg"
    aiyi "那爱衣也......"
    me01 "不用了，爱衣就在这里等着吧。如果盘子摔碎了的话是很危险的。"
    pause 1.0 hard
    scene black 
    with right2left_02
    play sound open_door4
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home night kitchen xuejian
    with right2left_02
    pause 0.5 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b1 b1 b1_sp2 onlayer m2 at walkin_l(0.7)
    pause 0.5 hard
    play voice "voice/翔子/011500920.ogg"
    xz "没、没打碎，一切安全的说。"
    "虽然翔子勉强接住了快要落地的盘子，但是动作幅度之大却有点像是杂技演员一般。"
    show xz_dsf_b1 b1 b1_s2
    play voice "voice/翔子/011500930.ogg"
    xz "我的第一次才没有给过神野君你！"
    stop music fadeout 5.0
    me01 "小孩子的话别当真啊......"
    play music second_112 fadein 3.0 if_changed
    hide xz_dsf_b1
    show xz_dsf_b2 b2 b2_ga2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011500940.ogg"
    xz "但是，为爱衣担心这一点还是要谢谢你。"
    me01 "这都是我应该做的。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011500950.ogg"
    xz "虽然这回盘子没有打碎，但是如果真的出现意外的话，就像神野君说的那样很危险的。"
    show xz_dsf_b3 b3 b3_h1
    play voice "voice/翔子/011500960.ogg"
    xz "还想着提醒你们注意的，可是被神野君抢先了。"
    me01 "别这么说，我也很担心翔子你会不会因此生我的气。"
    $ flcam.move(4500, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011500970.ogg"
    xz "......真是的。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011500980.ogg"
    xz "好了，结束了~"
    show xz_dsf_b3 b3 b3_sp1
    play voice "voice/翔子/011500990.ogg"
    xz "所以神野君你今天要出门吗？"
    me01 "是啊。"
    show xz_dsf_b3 b3 b3_s4
    play voice "voice/翔子/011501000.ogg"
    xz "是这样啊......"
    me01 "有什么需要我帮忙的吗？"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_ga2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011501010.ogg"
    xz "没有，这些小事就不麻烦你了。"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_s2
    play voice "voice/翔子/011501060.ogg"
    xz "呐，神野君......"
    show xz_dsf_b2 b2 b2_ga2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/翔子/011501090.ogg"
    xz "上周末你也出门了对吧？"
    me01 "是这样没错。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011501100.ogg"
    xz "那个，对方......是同一个人？"
    me01 "不是，这次是我自己想出去而已。"
    show xz_dsf_b3 b3 b3_s1
    play voice "voice/翔子/011501110.ogg"
    xz "这样啊......"
    me01 "有什么问题吗？"
    show xz_dsf_b3 b3 b3_n1 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/翔子/011501240.ogg"
    xz "没什么......路上小心~"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011501250.ogg"
    xz "虽然我只能目送你，但是......"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011501260.ogg"
    xz "无论什么时候我都会在这里等你回来的~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day208'
    $ seen_day208_balltower_event01 = False
    $ seen_day208_bridge_event01 = False
    $ seen_day208_home_event01 = False
    $ seen_day208_street_event01 = False
    $ seen_day208_laboratory_event01 = False

label day208.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day208':
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day208.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day208.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'])
    elif _overworld_label == 'day208.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day208.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'])
    elif _overworld_label == 'day208.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    if _overworld_label == 'day208':
        window mode map
        me01 "先去哪里好呢......" nointeract
    else:
        window mode map
        me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        cloqks=("day208.balltower_event01", "(not seen_day208_balltower_event01 and not seen_day208_bridge_event01) or (seen_day208_home_event01 and seen_day208_street_event01 and seen_day208_laboratory_event01)"),
        bridge=("day208.bridge_event01", "not seen_day208_bridge_event01"),
        road1=("day208.home_event01", "seen_day208_bridge_event01 and not seen_day208_home_event01"),
        road2=("day208.street_event01", "seen_day208_bridge_event01 and not seen_day208_street_event01"),
        laboratory=("day208.laboratory_event01", "seen_day208_street_event01 and seen_day208_home_event01 and not seen_day208_laboratory_event01"))
    $ window_animate_outro()
    if _return == 'day208.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day208.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day208.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day208.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day208.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day208.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian
    play music second_103 fadein 3.0 if_changed
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    show ts_xfe_yjz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    me01 "找到你了，希菲尔。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200460.ogg"
    xfe "嗯~"
    me01 "在看钟楼吗？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200470.ogg"
    xfe "嗯。"
    $ flcam.moves([
        (0,      0,   900, 0, 0.0, 'linear'),
        (0,      0,   900, 0, 0.5, 'linear'),
        (0, -2800, 1100, 0, 5.0, 'ease_cubic')
    ])
    with dissolve
    pause 0.5 hard
    "希菲尔抬头望向身后的钟楼。"
    "眼神中充满了羡慕。"
    $ flcam.move(0, 0, 900, duration=2.0, warper='ease_cubic')
    pause 2.0 hard
    me01 "为什么喜欢钟楼呢？"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/000200490.ogg"
    xfe "在约定好的时间，钟声总会如期而至。"
    play voice "voice/希菲尔/000200500.ogg"
    xfe "从很久很久以前开始，就一直如此......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day big
    with dissolve
    pause 1.0 hard
    "钟声每隔一段时间就会响起，听附近的人说已经有上百年的历史了。"
    "就算是这样，但对于刚搬来不久的我也没什么实感。"
    "就连当初来到这里的时候也是，并没有给我留下什么深刻的印象。"
    "要说留下来的也姑且只有与希菲尔一起在这里玩耍的回忆而已。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play sound enjoy_snow1
    play voice "voice/希菲尔/000200510.ogg"
    xfe "凉君，一起玩吧~"
    me01 "玩什么？"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/000200520.ogg"
    xfe "那个呢，来丢雪球吧。"
    pause 0.5 hard
    $ flcam.move(0, 0, 750, duration=1.5)
    show ts_xfe_yjz_b2 b2 b2_h1:
        xpos 0.5 alpha 1.0 ypos 1.02
        parallel:
            linear 1.0 ypos 1.05
        parallel:
            linear 1.0 alpha 0.0
    play sound enjoy_snow2
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    "希菲尔用小手抓起地上薄薄的积雪。"
    $ flcam.move(0, 0, 900, duration=1.5)
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 1.02
        parallel:
            linear 1.0 ypos 1.0
        parallel:
            linear 1.0 alpha 1.0
    pause 0.5 hard
    play voice "voice/希菲尔/000200530.ogg"
    xfe "这个广场有的时候会有小孩子来玩，看起来很有趣的。"
    me01 "你说的是打雪仗吧？"
    play sound yangmu
    show ts_xfe_yjz_b3 b3 b3_h5 at flu_down(0.15, 20):
        xpos 0.5
    show yangmu onlayer m2:
        xalign 0.49 yalign 0.47 zoom 0.85
    play voice "voice/希菲尔/000200540.ogg"
    xfe "原来是叫这个名字呀~"
    "希菲尔两眼放光地看着我。"
    hide yangmu
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200550.ogg"
    xfe "像这样把雪弄得圆圆的对吧？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200560.ogg"
    xfe "像这个样子吧？"
    stop music fadeout 5.0
    me01 "最后只需要把雪球丢出去就......"
    play music second_104 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_h4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200570.ogg"
    xfe "叭咕叭咕~"
    me01 "为什么要吃掉啊？！" with vpunch
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200580.ogg"
    xfe "不能吃吗？"
    me01 "一般来说是要丢出去的。"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200590.ogg"
    xfe "丢到希菲尔的嘴巴里了哟~"
    me01 "这样就不是打雪仗了。"
    show ts_xfe_yjz_b3 b3 b3_h4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200600.ogg"
    xfe "叭咕叭咕~"
    me01 "还是不要吃太多比较好......"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200610.ogg"
    xfe "是这样吗？"
    me01 "而且看起来也不怎么好吃。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200620.ogg"
    xfe "没有那回事，很好吃的哟~"
    me01 "就算是这样也请不要再吃了。"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/000200630.ogg"
    xfe "是这样吗？"
    me01 "吃坏肚子就不好了。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200650.ogg"
    xfe "希菲尔的肚子，不想要吃坏掉......"
    me01 "那就到此为止了。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200660.ogg"
    xfe "这样啊......"
    show ts_xfe_yjz_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200670.ogg"
    xfe "叭咕叭咕~"
    "无精打采的同时还在咀嚼着口中残留的积雪。"
    play sound jing01
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_ga4 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    show han onlayer m2:
        xalign 0.49 yalign 0.42 zoom 0.85
    play voice "voice/希菲尔/000200680.ogg"
    xfe "不、不是这样的，希菲尔吃掉的不是雪而是{rb}比菲德氏菌{/rb}{rt}肠道益生菌{/rt}。"
    me01 "雪里面才没有那种东西。"
    hide han
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200690.ogg"
    xfe "这样啊......"
    "更加地失落了。"
    me01 "不过做成刨冰的话，应该就可以吃了。"
    show ts_xfe_yjz_b2 b2 b2_sp3
    play voice "voice/希菲尔/000200700.ogg"
    xfe "刨冰？"
    me01 "就是用冰做的点心。"
    play sound yangmu
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h5 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    show yangmu onlayer m2:
        xalign 0.49 yalign 0.47 zoom 0.85
    play voice "voice/希菲尔/000200710.ogg"
    xfe "好像很好吃。"
    me01 "希菲尔不知道刨冰吗？明明连比菲德氏菌都知道......"
    hide yangmu
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200720.ogg"
    xfe "那个叫做刨冰的东西，在千冬讲给希菲尔的书里面没有出现过。"
    "到底是什么样的书里才会出现比菲德氏菌啊！？"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/000200730.ogg"
    xfe "那个刨冰，要怎么样才能吃到呢？"
    me01 "等到夏天就可以买到了。"
    show ts_xfe_yjz_b2 b2 b2_s3
    play voice "voice/希菲尔/000200740.ogg"
    xfe "夏天......"
    me01 "再怎么说这个季节也是吃不到的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200750.ogg"
    xfe "......"
    me01 "抱歉啊。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/000200760.ogg"
    xfe "没关系的......总有一天也想吃吃看~"
    me01 "那还要打雪仗吗？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200770.ogg"
    xfe "已经在打了哟。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    play sound enjoy_snow1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg play one
    with slowdissolve
    pause 1.0 hard
    "我随手做了个雪球，朝希菲尔的方向丢去。"
    play music second_108 fadein 3.0 if_changed
    pause 0.1 hard
    play sound jump_1
    scene set only xfe_cg play two
    with dissolve
    play voice "voice/希菲尔/000200780.ogg"
    xfe "跳~"
    pause 0.1 hard
    with vpunch
    scene set only xfe_cg play three
    with dissolve
    play voice "voice/希菲尔/000200790.ogg"
    xfe "{size=72}叭咕！{/size}"
    pause 0.1 hard
    scene set only xfe_cg play four
    with dissolve
    play voice "voice/希菲尔/000200800.ogg"
    xfe "嚼、嚼......吞下。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian alpha
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    me01 "希菲尔......你刚刚都做了什么？"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200810.ogg"
    xfe "打雪仗很好吃呢~"
    me01 "不是说了不能吃吗？"
    play sound jump_1
    show ts_xfe_yjz_b3 b3 b3_ga4 at flu_down(0.15, 20):
        xpos 0.5
    show han onlayer m2:
        xalign 0.49 yalign 0.42 zoom 0.85
    play voice "voice/希菲尔/000200820.ogg"
    xfe "不、不是这样的，希菲尔只是吃掉了{rb}乳酸菌{/rb}{rt}另一种益生菌{/rt}而已。"
    me01 "所以说雪里才没有那种东西！"
    hide han
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200830.ogg"
    xfe "打雪仗......好难的说。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200840.ogg"
    xfe "再试一次吧~"
    me01 "这次可不能再把雪吃掉了。"
    pause 0.5 hard
    play sound enjoy_snow1
    me01 "嘿~"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.5 alpha 1.0 ypos 1.0
        1.0
        parallel:
            linear 0.15 ypos 1.02
            linear 0.5 ypos 0.96
        parallel:
            0.15
            linear 0.5 alpha 0.0
    pause 1.15 hard
    play voice "voice/希菲尔/000200850.ogg"
    xfe "我跳~"
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    pause 1.0 hard
    hide snow_level1
    play sound jump_1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg play five
    with slowdissolve
    pause 0.5 hard
    play sound ganga02
    scene set only xfe_cg play six
    with dissolve
    pause 2.0 hard
    scene set only balltower snow day xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp2 onlayer m2 at flu_down(0.15, 20, 2):
        xpos 0.5
    show han onlayer m2:
        xalign 0.49 yalign 0.42 zoom 0.85
    play voice "voice/希菲尔/000200860.ogg"
    xfe "呜啊~希菲尔的鼻子！"
    hide han
    show ts_xfe_yjz_b2 b2 b2_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200870.ogg"
    xfe "打雪仗......好痛的说。"
    me01 "抱歉，似乎是我教学的方式不对。"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/000200880.ogg"
    xfe "没关系的，这下总算知道该怎么玩了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200890.ogg"
    xfe "只要像刚刚那样，使劲用雪砸凉君就可以了吧？"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg play seven
    with slowdissolve
    play music second_106 fadein 3.0 if_changed
    pause 0.5 hard
    me01 "......诶？"
    play voice "voice/希菲尔/000200900.ogg"
    xfe "要向凉君砸过去了哟~"
    me01 "等、等一下！？"
    pause 0.1 hard
    scene set only xfe_cg play eight
    with dissolve
    play sound shoot1
    play voice "voice/希菲尔/000200910.ogg"
    xfe "去吧~"
    play sound enjoy_snow1
    me01 "{size=72}呀啊！！！{/size}" with vpunch
    pause 0.1 hard
    show wflash onlayer texture
    with vpunch
    scene set only xfe_cg play nine
    with dissolve
    me01 "希菲尔......"
    play voice "voice/希菲尔/000200920.ogg"
    xfe "什么？"
    pause 0.1 hard
    play sound ganga01
    scene set only xfe_cg play ten
    with dissolve
    me01 "还是不要打雪仗了吧......"
    play voice "voice/希菲尔/000200930.ogg"
    xfe "是这样吗？"
    me01 "我的身体好像承受不住这个游戏。"
    pause 0.1 hard
    scene set only xfe_cg play eleven
    with dissolve
    play voice "voice/希菲尔/000200940.ogg"
    xfe "希菲尔刚才，鼻子也很痛的说~"
    play voice "voice/希菲尔/000200950.ogg"
    xfe "打雪仗，就是这般无情的游戏。"
    me01 "无情的只有希菲尔而已吧......"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    me01 "没想到居然会在打雪仗的时候被打成雪人。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200960.ogg"
    xfe "雪人？"
    me01 "就是用雪堆成人的模样。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    pause 1.0 hard
    play sound enjoy_snow2
    "为了满足希菲尔的好奇心，我们开始了比较“和平”的游戏——堆雪人。"
    "干净的雪很容易就吸附在了一起，原本只有薄薄的一层积雪，也慢慢地累积成大雪球。"
    pause 1.0 hard
    scene set only balltower snow day xuejian alpha
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200970.ogg"
    xfe "哇，好大~"
    me01 "再用树枝随便做个表情就完成......"
    play music second_108 fadein 3.0 if_changed
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h4 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200980.ogg"
    xfe "叭咕叭咕~"
    me01 "为什么又开始吃雪了？！"
    with vpunch
    show ts_xfe_yjz_b3 b3 b3_h4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200990.ogg"
    xfe "叭咕叭咕~"
    me01 "所以说不要吃啊！"
    show ts_xfe_yjz_b3 b3 b3_h1
    play voice "voice/希菲尔/000201000.ogg"
    xfe "为了不让雪人先生生病，希菲尔要帮他把不好的细菌全都吃掉~"
    me01 "不管怎么样，希菲尔你别生病就行了。"
    show ts_xfe_yjz_b3 b3 b3_n1
    play voice "voice/希菲尔/000201010.ogg"
    xfe "这样就完成了？"
    me01 "算是吧......"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only items snowman
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/000201020.ogg"
    xfe "头部缺了一块，好像月亮一样~"
    me01 "这都是希菲尔你的杰作。"
    pause 1.0 ahrd
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian alpha
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/希菲尔/000201030.ogg"
    xfe "堆雪人真是一项好吃的游戏啊~"
    stop music fadeout 5.0
    "真是不可思议，只要和这个女孩在一起甚至连寒冷的感觉都不复存在了。"
    "即便是过去的我想必也一定体会到了这一点吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day big
    with slowdissolve
    play music second_117 fadein 3.0 if_changed
    play ambience1 zhong_rill
    pause 0.5 hard
    "钟声响起，欢乐的时光结束了。"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/希菲尔/000201040.ogg"
    xfe "凉君，再见了~"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201050.ogg"
    xfe "以后再两个人一起玩吧~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    "说完，希菲尔的身影消失了。"
    "与她一同消失的还有这场漫天的飘雪。"
    pause 2.0 hard
    if not seen_day208_balltower_event01:
        $ seen_day208_balltower_event01 = True
    $ _overworld_label = 'day208.balltower_event01'

    if seen_day208_balltower_event01 and seen_day208_home_event01 and seen_day208_street_event01 and seen_day208_laboratory_event01:
        jump day208.end_part
    jump day208.map

label day208.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only bridge day under xuejian
    with dissolve
    play music second_133 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_tcf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021201920.ogg"
    yj "啊，凉君~"
    me01 "这么冷的天你怎么还在这里？"
    show yj_tcf_b2 b2 b2_h1
    play voice "voice/植澄友加/021201930.ogg"
    yj "补习一结束我就迫不及待地赶过来了嘛~"
    me01 "一结束就......"
    hide yj_tcf_b2 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021201940.ogg"
    yj "因为因为，人家想快点开始嘛~"
    $ flcam.move(0, -300, 1000, duration=1.5)
    hide yj_tcf_b3
    show yj_tcf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021201950.ogg"
    yj "那么凉君，今天也拜托你了~"
    show yj_tcf_b1 b1 b1_h1
    play voice "voice/植澄友加/021201960.ogg"
    yj "我会尽全力的，凉君也要好好教我哟。"
    me01 "那么废话不多说，直接开始吧。"
    hide yj_tcf_b1 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/021201970.ogg"
    yj "嗯！"
    show yj_tcf_b3 b3 b3_n1
    play voice "voice/植澄友加/021201980.ogg"
    yj "首先是练习对{rb}念动立场{/rb}{rt}psychokinesis{/rt}的控制对吧？"
    me01 "鉴于你之前的暴走关系，想必灵力也消耗了相当大的一部分。"
    me01 "所以就从对灵力要求较为宽松的控制训练开始吧。"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021201990.ogg"
    yj "毕竟我还没办法像凉君那样完美地控制{rb}灵纹{/rb}{rt}rune{/rt}。"
    me01 "只要掌握诀窍就简单多了，在习惯之前就辛苦一下吧。"
    hide yj_tcf_b2 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_h2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021202000.ogg"
    yj "嘿嘿......凉君你为我想得好周到。"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021202010.ogg"
    yj "那个那个，我其实也有思考过。"
    me01 "思考什么？"
    show yj_tcf_b2 b2 b2_h1
    play voice "voice/植澄友加/021202020.ogg"
    yj "也许可行的改良方案。"
    me01 "嚯~"
    show yj_tcf_b2 b2 b2_n1
    play voice "voice/植澄友加/021202030.ogg"
    yj "可以让我试试吗？"
    hide yj_tcf_b2
    show yj_tcf_b3 b3 b3_h2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021202040.ogg"
    yj "凉君你会好好看着我的吧？"
    me01 "那就争取让我对你刮目相看吧。"
    hide yj_tcf_b3
    show yj_tcf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021202050.ogg"
    yj "嗯！那个啊，我觉得问题是出在“帅气程度”上。"
    stop music fadeout 5.0
    me01 "......帅气？"
    "气氛突然变得诡异了起来。"
    play music second_108 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg train1
    with slowdissolve
    play voice "voice/植澄友加/021202060.ogg"
    yj "一般都是像这样，用手心朝向前方对吧？"
    play voice "voice/植澄友加/021202070.ogg"
    yj "但是，如果像这样摆出帅气姿势的话......我觉得可以做得更好。"
    pause 0.1 hard
    scene set only yj_cg train2
    with dissolve
    play voice "voice/植澄友加/021202090.ogg"
    yj "我在想这个可能就是诀窍吧。"
    me01 "不......那只是下意识的动作，根本不是重点。"
    "话说回来，我一直都在做着这样奇怪的动作吗？"
    "看来以后有必要注意一下了......"
    play voice "voice/植澄友加/021202110.ogg"
    yj "既然这样，那我也和凉君一样好了。"
    play voice "voice/植澄友加/021202120.ogg"
    yj "因为我和凉君一样，是擅长使用{rb}念动立场{/rb}{rt}psychokinesis{/rt}的{rb}灵继者{/rb}{rt}elfin{/rt}。"
    play voice "voice/植澄友加/021202130.ogg"
    yj "总之，我现在要像凉君那样行动了。"
    pause 0.1 hard
    scene set only yj_cg train3
    with dissolve
    play voice "voice/植澄友加/021202140.ogg"
    yj "像凉君一样，帅气地、帅气地......呀啊啊啊啊啊！"
    pause 0.1 hard
    scene set only yj_cg train4
    with dissolve
    play sound rune2
    with vpunch
    me01 "等等，这个力道有点......"
    pause 0.1 hard
    play sound water
    scene set only yj_cg train5
    with dissolve
    play voice "voice/植澄友加/021202150.ogg"
    yj "{size=72}呀啊！？{/size}"
    pause 0.1 hard
    scene set only yj_cg train6
    with dissolve
    play sound ganga03
    with vpunch
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    play sound touch
    pause 0.5 hard
    me01 "你没事吧？"
    me01 "听好了友加，控制{rb}灵纹{/rb}{rt}rune{/rt}的关键不是靠蛮力，而是要集中注意力。"
    me01 "像你现在这样......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only yj_cg bridge1
    $ flcam.move(-1100, -1400, 450, duration=3.0, warper='ease_cubic')
    play music second_111 fadein 3.0 if_changed
    with slowdissolve
    pause 3.0 hard
    play voice "voice/植澄友加/020104540.ogg"
    yj "......凉君？"
    me01 "......"
    pause 0.1 hard
    scene set only yj_cg bridge3
    with dissolve
    play voice "voice/植澄友加/020104590.ogg"
    yj "凉君你的脸很红啊，难道是因为刚才的练习害你受伤了？"
    me01 "先别在意我这边了，你现在的问题似乎比较严重......"
    play voice "voice/植澄友加/020104550.ogg"
    yj "我的话没问题的，活力满满的呢。"
    play voice "voice/植澄友加/020104570.ogg"
    yj "只是全身都湿透了而已。"
    me01 "......"
    pause 0.1 hard
    scene set only yj_cg bridge1
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/020104600.ogg"
    yj "凉君？"
    me01 "......"
    play voice "voice/植澄友加/020104610.ogg"
    yj "你为什么不看我这边？"
    me01 "这种事别让我说出来啊！"
    play voice "voice/植澄友加/020104620.ogg"
    yj "......欸？"
    pause 0.1 hard
    scene set only yj_cg bridge5
    with dissolve
    play voice "voice/植澄友加/020104630.ogg"
    yj "......"
    pause 0.1 hard
    scene set only yj_cg bridge6
    with dissolve
    play voice "voice/植澄友加/020104640.ogg"
    yj "看、看到了？"
    me01 "没看到。"
    play voice "voice/植澄友加/020104650.ogg"
    yj "看、看到了吧？！"
    me01 "都说了没有看到！"
    play voice "voice/植澄友加/020104660.ogg"
    yj "你、你要负责啊~"
    pause 0.1 hard
    scene set only yj_cg bridge2
    with dissolve
    play voice "voice/植澄友加/020104670.ogg"
    yj "......又失败了啊。"
    me01 "比起这个你不会冷吗？"
    play voice "voice/植澄友加/020104680.ogg"
    yj "......没问题的，我可是立刻就会火热起来的女人呢。"
    pause 0.1 hard
    scene set only yj_cg bridge7
    with dissolve
    play voice "voice/植澄友加/020104720.ogg"
    yj "......谢谢你。"
    me01 "比起这个还是先把衣服换了吧。"
    me01 "好在训练穿的是体操服，有带替换的衣服吧？"
    pause 0.1 hard
    scene set only yj_cg bridge4
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/020104740.ogg"
    yj "嗯......有的。"
    pause 0.1 hard
    scene set only yj_cg bridge7
    with dissolve
    play voice "voice/植澄友加/020104760.ogg"
    yj "刚才真是吓了一跳......好大一个浪突然就拍了过来。"
    play voice "voice/植澄友加/020104770.ogg"
    yj "这就是所谓的异常气候吧？"
    me01 "我想应该还算不上。"
    pause 0.1 hard
    scene set only yj_cg bridge6
    with dissolve
    play voice "voice/植澄友加/020104780.ogg"
    yj "凉君，关于异常气候你知道什么吗？"
    me01 "为什么突然问这个？"
    pause 0.1 hard
    scene set only yj_cg bridge2
    with dissolve
    play voice "voice/植澄友加/020104790.ogg"
    yj "之前去姐姐那里的时候，就隐约这样想了。"
    me01 "比起这个......先换衣服吧。"
    me01 "刚刚好像有人从桥上经过。"
    pause 0.1 hard
    scene set only yj_cg bridge5
    with dissolve
    play voice "voice/植澄友加/020104920.ogg"
    yj "欸？！"
    me01 "手......你的手！"
    pause 0.1 hard
    scene set only yj_cg bridge6
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/020104930.ogg"
    yj "看、看见了？"
    me01 "......没看见。"
    play voice "voice/植澄友加/020104940.ogg"
    yj "看、看见了吧！"
    me01 "都说了没看见！"
    play voice "voice/植澄友加/020104950.ogg"
    yj "你、你可要负起责任啊~"
    "搞了半天又绕回来了。"
    pause 0.1 hard
    scene set only yj_cg bridge7
    with dissolve
    play voice "voice/植澄友加/020104990.ogg"
    yj "我有带毛巾，也借给你吧。"
    pause 0.1 hard
    scene set only yj_cg bridge4
    with dissolve
    play voice "voice/植澄友加/020105000.ogg"
    yj "能麻烦你帮我把下风吗？"
    me01 "我知道了，你快去吧。"
    pause 0.1 hard
    scene set only yj_cg bridge7
    with dissolve
    play voice "voice/植澄友加/020105010.ogg"
    yj "可不能像刚才那样偷看了哟。"
    me01 "知道了......不对，我一次也没有偷看好吧！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with slowdissolve
    play sound jiaobu4
    pause 2.0 hard
    scene set only bridge day under xuejian
    $ flcam.move(0, -100, 400, duration=1.5)
    with dissolve
    pause 1.0 hard
    "不一会儿的功夫，友加就换好衣服回来了。"
    "同时还向我递出了毛巾。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020105020.ogg"
    yj "等等......不好好把身子擦干的话会感冒的。"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b2 b2 b2_s2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    "友加接过毛巾小心地帮我擦拭了脸和肩膀。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020105030.ogg"
    yj "只用毛巾的话，果然还是不行的。"
    show yj_dzf_b1 b1 b1_a1
    play voice "voice/植澄友加/020105040.ogg"
    yj "回去要记得好好洗个澡喔~"
    me01 "你是我母上大人吗......"
    "不得不说，友加在照顾人这点上一点也不输给翔子。"
    "这也是托她那位姐姐的福吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day208_bridge_event01:
        $ seen_day208_bridge_event01 = True
    $ _overworld_label = 'day208.bridge_event01'
    jump day208.map

label day208.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only home day outside xuejian
    play music second_107 fadein 3.0 if_changed
    with dissolve
    pause 2.0 hard
    play sound open_door4
    scene set only home day passwalk xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105120.ogg"
    yj "......这样啊，果然凉君是住在翔子家的。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show xz_dsf_b1 b1 b1_sp2 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010104870.ogg"
    xz "比起这个友加，发生什么事了？你和神野君都湿透了。"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_ga3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020105130.ogg"
    yj "嗯，稍微出了点小问题......"
    hide xz_dsf_b1
    show xz_dsf_b2 b2 b2_a1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010104880.ogg"
    xz "发生了什么？"
    show yj_dzf_b3 b3 b3_h1
    play voice "voice/植澄友加/020105140.ogg"
    yj "这是只属于我和凉君的秘密哟~"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010104890.ogg"
    xz "......"
    me01 "等等友加......这么说容易被误会。"
    me01 "还是快点解释清楚比较好。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105150.ogg"
    yj "翔子你也有和凉君两个人的秘密对吧？"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010104900.ogg"
    xz "才没有呢......那种东西。"
    hide yj_dzf_b2 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_h1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020105160.ogg"
    yj "比如和凉君同居之类的~"
    show xz_dsf_b2 b2 b2_a1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/翔子/010104910.ogg"
    xz "才不是同居！"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105170.ogg"
    yj "呐翔子......我觉得能坦率地说出心里的想法才是最重要的。"
    play voice "voice/植澄友加/020105190.ogg"
    yj "不是需要处处留意的关系。"
    play voice "voice/植澄友加/020105200.ogg"
    yj "就算过去留有秘密，也能像现在这样轻松地交谈的关系才是最好的。"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105210.ogg"
    yj "我在想这样是不是......才称得上是朋友呢。"
    hide xz_dsf_b2
    show xz_dsf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010104920.ogg"
    xz "友加......"
    $ flcam.move(-2250, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105220.ogg"
    yj "所以呢......从今往后也请多多关照~"
    show xz_dsf_b1 b1 b1_h1
    play voice "voice/翔子/010104930.ogg"
    xz "嗯~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day208_home_event01:
        $ seen_day208_home_event01 = True
    $ _overworld_label = 'day208.home_event01'

    if seen_day208_balltower_event01 and seen_day208_home_event01 and seen_day208_street_event01 and seen_day208_laboratory_event01:
        jump day208.end_part
    jump day208.map

label day208.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street day road1 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dzf_b2 b2 b2_s1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020105230.ogg"
    yj "{size=72}呀！{/size}" with vpunch
    play music second_133 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg street1
    with slowdissolve
    pause 1.0 hard
    "走着走着，友加突然用手按住了裙子。"
    "我被她这突如其来的反应吓了一跳。"
    pause 0.1 hard
    scene set only yj_cg street2
    with dissolve
    play voice "voice/植澄友加/020105240.ogg"
    yj "好、好险......"
    me01 "怎么了？"
    pause 0.1 hard
    scene set only yj_cg street3
    with dissolve
    play voice "voice/植澄友加/020105250.ogg"
    yj "裙子差点被风吹起来了。"
    play voice "voice/植澄友加/020105260.ogg"
    yj "果然，冷静不下来啊。"
    play voice "voice/植澄友加/020105270.ogg"
    yj "感觉凉飕飕的......"
    pause 0.1 hard
    play sound jing01
    scene set only yj_cg street4
    with dissolve
    me01 "凉飕飕的？"
    me01 "......难道。"
    play voice "voice/植澄友加/020105280.ogg"
    yj "里面不穿的话果然还是太......"
    me01 "里面没穿吗？"
    play voice "voice/植澄友加/020105290.ogg"
    yj "呜......嗯，毕竟里面也湿了。"
    play voice "voice/植澄友加/020105300.ogg"
    yj "又没带替换的内衣，所以就......"
    me01 "那现在是......"
    pause 0.1 hard
    play sound ganga01
    scene set only yj_cg street5
    with dissolve
    play voice "voice/植澄友加/020105310.ogg"
    yj "......真空。"
    me01 "......"
    play voice "voice/植澄友加/020105320.ogg"
    yj "呜嗯......啊哈哈~"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only street day road1 xuejian
    show yj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/020105330.ogg"
    yj "一直盯着人家看......可不行啊。"
    me01 "比、比起这个，我们还是先去一趟商店街吧。"
    show yj_dzf_b1 b1 b1_sp1
    play voice "voice/植澄友加/020105340.ogg"
    yj "不是要送我回家吗？"
    me01 "在那之前得先买点东西。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020105350.ogg"
    yj "......买内衣吗？"
    me01 "别说出来啊！"
    show yj_dzf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020105360.ogg"
    yj "没问题的啦......谢谢你。"
    me01 "这种事早点说的话就能让翔子帮忙想办法了。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020105300.ogg"
    yj "果然......还是不太好意思开口。"
    me01 "因为我也在场的关系？"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b2 b2 b2_a1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020105380.ogg"
    yj "没有那回事，凉君你还是以处理你自己的事情为优先就可以了。"
    me01 "果然还是叫出租车吧？"
    show yj_dzf_b2 b2 b2_h4
    play voice "voice/植澄友加/020105400.ogg"
    yj "不用到那种程度也没问题的。"
    me01 "不过坐姿也要注意。"
    me01 "对了，如果是我现在回去拿的话应该来得及。"
    me01 "不过让你一个人在这里也不是办法......"
    show yj_dzf_b2 b2 b2_ga4
    play voice "voice/植澄友加/020105410.ogg"
    yj "真是的，我都说没问题的。"
    me01 "这种事情才不是那么简单的！"
    hide yj_dzf_b2 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_n3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020105420.ogg"
    yj "凉君真是好色啊~"
    me01 "连本人都毫不在意反而更显得我紧张过头了。"
    show yj_dzf_b3 b3 b3_ga3
    play voice "voice/植澄友加/020105430.ogg"
    yj "呃嗯......啊哈哈~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day208_street_event01:
        $ seen_day208_street_event01 = True
    $ _overworld_label = 'day208.street_event01'

    if seen_day208_balltower_event01 and seen_day208_home_event01 and seen_day208_street_event01 and seen_day208_laboratory_event01:
        jump day208.end_part
    jump day208.map

label day208.laboratory_event01:
    $ flcam.move(0, 0, 0)
    play sound close_door4
    scene set only laboratory inside2 xuejian
    play music second_102 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h1 onlayer m1:
         xpos 0.5
    play voice "voice/圣护院/150100660.ogg"
    shy "来了啊友加。"
    "一进研究所的大门，圣护院小姐就迎了出来。"
    "这次似乎没有之前那么繁忙了。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100670.ogg"
    shy "果然你也一起来了吗......虽然早就知道会这样了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b2 b2 b2_sp1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/植澄友加/020105480.ogg"
    yj "诶，我有说过凉君会一起来吗？"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/150100680.ogg"
    shy "那倒没有，是来自其他地方的情报。"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105490.ogg"
    yj "其他地方？"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100690.ogg"
    shy "比起这个友加，我有话要跟你说。"
    show yj_dzf_b3 b3 b3_n3
    play voice "voice/植澄友加/020105500.ogg"
    yj "啊嗯......所以才叫我来的吧。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105510.ogg"
    yj "......要说的事情是什么？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play sound touch
    scene set only shy_cg two
    with slowdissolve
    play voice "voice/圣护院/150100700.ogg"
    shy "......之前不知怎么就被花山院说教了。"
    play voice "voice/圣护院/150100710.ogg"
    shy "被自己的下属说教什么的还是第一次。"
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900)
    scene set only laboratory inside2 xuejian
    show yj_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    with dissolve
    play voice "voice/植澄友加/020105520.ogg"
    yj "......姐姐要说的事就是指这个吗？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/150100750.ogg"
    shy "......"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/020105530.ogg"
    yj "我不觉得姐姐是那种被人说教就会简单听进去的类型。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100750.ogg"
    shy "......"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/020105550.ogg"
    yj "我还以为要说的事情一定是关于{rb}灵纹{/rb}{rt}rune{/rt}或者异常气候的呢。"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_ga4 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105570.ogg"
    yj "不过姐姐刚才也说了有其他地方的情报所以想必也已经比我更清楚了吧。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150100760.ogg"
    shy "洞察力不错。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105590.ogg"
    yj "......虽然不知道姐姐你是怎么看待我的。"
    show yj_dzf_b1 b1 b1_s2
    play voice "voice/植澄友加/020105580.ogg"
    yj "但再怎么说我也算是姐姐你的妹妹。"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/150100770.ogg"
    shy "你是我妹妹这一点，无论如何都是不会改变的。"
    hide yj_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150100780.ogg"
    shy "就算你不再是{rb}灵继者{/rb}{rt}elfin{/rt}了，也是一样的。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100790.ogg"
    shy "我收到了下属的汇报，说你作为{rb}灵继者{/rb}{rt}elfin{/rt}觉醒了。"
    play voice "voice/圣护院/150100800.ogg"
    shy "所以友加，这段时间星天宫也需要派人继续观察你的一举一动。"
    play voice "voice/植澄友加/020105600.ogg"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    yj "......什么意思？"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150100810.ogg"
    shy "你也知道这里是研究异常气候的地方。"
    play voice "voice/圣护院/150100820.ogg"
    shy "如果这一切和{rb}灵继者{/rb}{rt}elfin{/rt}有关系的话，我们当然会将其作为研究的对象。"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/020105610.ogg"
    yj "......"
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/150100830.ogg"
    shy "你不需要担心，你要做的就是照常地生活、上学就行了。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100840.ogg"
    shy "但是，如果发生什么变化的话，希望你能够立刻与我联系。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100850.ogg"
    shy "还有这件事尽量不要外传，会引起混乱的......"
    hide yj_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150100860.ogg"
    shy "神野凉君，也希望你充分理解我们的苦衷。"
    play voice "voice/圣护院/150100870.ogg"
    shy "现在你被允许到这里来，是因为你目睹了友加的觉醒。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/150100880.ogg"
    shy "虽然不会强行封你的口，但是希望你不要声张可以吗？"
    "我点了点头。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150100890.ogg"
    shy "那么，我要说的就是这些了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105620.ogg"
    yj "......"
    play voice "voice/圣护院/150100900.ogg"
    shy "友加，今天就好好休息，等你冷静下来了我们再好好谈谈。"
    show yj_dzf_b1 b1 b1_s2
    play voice "voice/植澄友加/020105630.ogg"
    yj "......呐，姐姐。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100910.ogg"
    shy "怎么了？"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b1 b1 b1_s3
    play voice "voice/植澄友加/020105640.ogg"
    yj "在姐姐的眼里......我究竟是什么？"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150100920.ogg"
    shy "你是我的妹妹。"
    show yj_dzf_b1 b1 b1_a1
    play voice "voice/植澄友加/020105650.ogg"
    yj "......那是什么意思？"
    play voice "voice/圣护院/150100930.ogg"
    shy "字面上的意思。"
    play voice "voice/圣护院/150100940.ogg"
    shy "你是我的妹妹，除此之外没有别的。"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/020105660.ogg"
    yj "......意思是“好用”的妹妹吧？"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100950.ogg"
    shy "友加？"
    show yj_dzf_b1 b1 b1_s3
    play voice "voice/植澄友加/020105670.ogg"
    yj "先是作为能够料理家务的妹妹，然后是作为实验对象的妹妹没错吧？"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/020105680.ogg"
    yj "姐姐你说我是你的妹妹。"
    show yj_dzf_b1 b1 b1_a1
    play voice "voice/植澄友加/020105690.ogg"
    yj "就是无论我变成什么样子都无所谓的意思吗？"
    play voice "voice/植澄友加/020105700.ogg"
    yj "就算我现在觉醒成了{rb}灵继者{/rb}{rt}elfin{/rt}也是一样的吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100960.ogg"
    shy "啊......什么都不会改变。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100970.ogg"
    shy "无论多少次我都会这么说的，因为你是就我的独一无二的妹妹。"
    stop music fadeout 5.0
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/150100980.ogg"
    shy "那么，话也说完了......一起回去吧？"
    play music second_111 fadein 3.0 if_changed
    show yj_dzf_b1 b1 b1_sp1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020105710.ogg"
    yj "诶？"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101000.ogg"
    shy "一起回家，还是说你现在有其他事情？"
    show yj_dzf_b1 b1 b1_s2
    play voice "voice/植澄友加/020105720.ogg"
    yj "......不是。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150101010.ogg"
    shy "还有其他问题吗？"
    play voice "voice/植澄友加/020105730.ogg"
    yj "凉君说他会送我回去。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101020.ogg"
    shy "如果你觉得比起和我一起更想和他回去的话，我倒也无所谓。"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105740.ogg"
    yj "我不是这个意思......"
    show yj_dzf_b2 b2 b2_s2
    play voice "voice/植澄友加/020105750.ogg"
    yj "只是姐姐突然说要和我一起回去什么的，打从一开始就没有想过......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101030.ogg"
    shy "刚才我不是也说了需要有人观察你的身体状况吗？因为这个的缘故我现在必须待在你身边才行。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105760.ogg"
    yj "这也是......工作吗？"
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/150101040.ogg"
    shy "是的。"
    play voice "voice/植澄友加/020105770.ogg"
    yj "......是这样啊。"
    "友加露出了欣慰的笑容。"
    "那是久违的愉悦的表情。"
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/020105780.ogg"
    yj "姐姐果然还是那么我行我素。"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105790.ogg"
    yj "但是为什么呢......"
    play voice "voice/植澄友加/020105800.ogg"
    yj "现在姐姐的话仍然回荡在我的脑海里。"
    show yj_dzf_b2 b2 b2_c1
    play voice "voice/植澄友加/020105810.ogg"
    yj "我想我现在大概是......很开心吧。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/150101050.ogg"
    shy "真是傻瓜。"
    play voice "voice/圣护院/150101060.ogg"
    shy "你自己不是也都没变吗，不管什么都还是一样。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101070.ogg"
    shy "已经没有什么需要担心的了。"
    hide yj_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150101080.ogg"
    shy "那么神野君，你打算怎么办？"
    me01 "友加的事就拜托您了。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101090.ogg"
    shy "是吗......毕竟你也有其他事情要忙。"
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    show yj_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020105830.ogg"
    yj "凉君......今天真的谢谢你了。"
    me01 "道谢的话已经够多了，总之我们学校见吧。"
    hide yj_dzf_b3 with None
    pause 0.1 hard
    show yj_dzf_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020105840.ogg"
    yj "嗯，我们学校见~"
    hide yj_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    show shy_yjf_b1 b1 b1_n3 onlayer m1:
        xpos 0.5
    play voice "voice/圣护院/150101100.ogg"
    shy "神野君，最后能再拜托你一件事吗？"
    me01 "什么事？"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101110.ogg"
    shy "我认为友加的{rb}灵纹{/rb}{rt}rune{/rt}虽然已经度过了暴走的危险期，但是暂时还会有一段时间保持着不稳定的状态。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/150101120.ogg"
    shy "所以作为友加姐姐的我想拜托你。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101130.ogg"
    shy "如果友加出了什么事的话，希望你能尽力帮助她。当然是在朋友的范围内就行，拜托你了。"
    me01 "为什么是我？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101140.ogg"
    shy "因为你似乎和{rb}灵纹{/rb}{rt}rune{/rt}本身的相性很好。"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/150101150.ogg"
    shy "你也是......一位新生的{rb}灵继者{/rb}{rt}elfin{/rt}吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    if not seen_day208_laboratory_event01:
        $ seen_day208_laboratory_event01 = True
    $ _overworld_label = 'day208.laboratory_event01'

    if seen_day208_balltower_event01 and seen_day208_home_event01 and seen_day208_street_event01 and seen_day208_laboratory_event01:
        jump day208.end_part
    jump day208.map

label day208.end_part:
    $ persistent.lingyin = True
    $ persistent.szl_ling = True
    $ persistent.youjia = True
    $ renpy.block_rollback()
    $ _rollback = False
    jump second_menu
