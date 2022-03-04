
label inside_battle11(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "在立花希的「妄想颠覆」结界中，其{color=#f00}受到的伤害最高不超过1点{/color}，但反弹伤害照常计算，需多加注意。"
    "利用千川老师的元素爆发「虚无」能够开启封印结界抵消「妄想颠覆」的效果。"
    "同时「虚无」结界提供的「积重鬼怨」效果还能大幅{color=#f00}降低敌方角色属性{/color}和{color=#f00}提升我方角色技能伤害{/color}。"
    "在封印结界中的立花希将{color=#f00}失去{/color}「被动技能」和「装备4件套效果」。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label inside_battle12(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "有了千川老师的祝福加持，水之濑凛的实力进一步提升了。"
    "此刻的目标只有一个，那就是{color=#f00}尽一切所能拖延时间{/color}，寻找突破口。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label inside_battle13(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "在立花希的「妄想颠覆」结界中周围的水汽迅速凝结成小型风暴遮蔽视线，致使水之濑凛{color=#3ff}冰元素伤害抗性{/color}大幅下降，且每个回合开始时有20%固定概率眩晕1回合。"
    "但是她的实力依然不可小觑。在千川老师的帮助下，水之濑凛在回合开始时将获得自身攻击比例120%的固定数值{color=#f0f}雷元素护盾{/color}，持续1回合。"
    "在护盾加持下的水之濑凛对雷元素伤害减免75%，尽量避免同属性攻击。利用{color=#3ff}冰元素{/color}攻击能够最有效破除「雷」属性{encyclopedia=shield_buff}护盾{/encyclopedia}。"
    "{color=#f00}优先解决{/color}千川老师也能快速打开局面。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label day217:
    bookmark
    $ save_name = _("Day 217")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date216 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    play ambience1 niaoming fadein 3.0
    scene set only home day outside xuejian
    with slowdissolve
    pause 2.0 hard
    stop ambience1 fadeout 3.0
    scene set only home day living_room xuejian
    play music second_114 fadein 3.0 if_changed
    $ flcam.move(0, -100, 400, duration=1.5)
    with dissolve
    pause 1.0 hard
    "一大早电视里就播放着新闻。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home television
    with dissolve
    pause 1.0 hard
    "内容是关于火星探测卫星的报道。"
    "最近的事故一个接一个发生，似乎不是很顺利的样子。"
    play sound open_door6
    pause 1.0 hard
    scene set only home day living_room xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/翔子/011104950.ogg"
    xz "神野君，早餐做好了。"
    me01 "一直以来真是辛苦你了。"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/011104960.ogg"
    xz "都这时候你还在说什么呢。"
    me01 "只是单纯地想说声“谢谢”而已。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_h1
    play voice "voice/翔子/011104980.ogg"
    xz "比起这个......给，今天的便当。"
    me01 "喔~3Q。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011104990.ogg"
    xz "都说不用客气了......你该不会又要说想帮忙做家务来补偿之类的话吧？"
    me01 "那个的话我放弃了，果然还是只会碍手碍脚。"
    show xz_dzf_b3 b3 b3_n1
    play voice "voice/翔子/011105000.ogg"
    xz "知道的话神野君做好自己的“工作”就行了。"
    me01 "我的工作是指接送爱衣？"
    hide xz_dzf_b3
    show xz_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105010.ogg"
    xz "是的。"
    me01 "要是这样能稍微减轻翔子你的负担的话。"
    show xz_dzf_b1 b1 b1_ga3
    play voice "voice/翔子/011105020.ogg"
    xz "我并没觉得这是负担。"
    me01 "不过最近因为一些事情也都是让翔子你替我去接送，总感觉自己真的太不靠谱了。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105030.ogg"
    xz "没有的事。"
    show xz_dzf_b2 b2 b2_h1
    play voice "voice/翔子/011105040.ogg"
    xz "神野君确实也帮了不少忙。"
    play voice "voice/翔子/011105050.ogg"
    xz "我没能让爱衣得到的快乐，神野君替我做到了。"
    show xz_dzf_b2 b2 b2_h2
    play voice "voice/翔子/011105070.ogg"
    xz "所以神野君你的任务就是守护爱衣笑容。"
    "幼儿园社的事情......看来已经不生气了。"
    show xz_dzf_b2 b2 b2_n1
    play voice "voice/翔子/011105080.ogg"
    xz "知道了吗？"
    me01 "包在我身上。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105090.ogg"
    xz "那就快点来吃饭吧~"
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_h1 at walkout_r(0.5)
    pause 0.5 hard
    hide xz_dzf_b1
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "守护爱衣的笑容......吗。"
    "但是不只是这样的吧。"
    "我也想......守护翔子你的笑容。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home television
    with dissolve
    pause 1.0 hard
    "就在这时翔子的目光被电视机屏幕上的新闻给吸引了。"
    "虽然依旧是在播报火星探测的事情。"
    pause 1.0 hard
    scene set only home day living_room xuejian
    $ flcam.move(5200, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.7
    me01 "很在意吗？"
    show xz_dzf_b3 b3 b3_h1
    play voice "voice/翔子/011105110.ogg"
    xz "没什么......"
    stop music fadeout 5.0
    pause 1.0 hard
    play sound close_door3
    show xz_dzf_b3 b3 b3_h1 at walkout_r(0.7)
    pause 0.5 hard
    hide xz_dzf_b3
    scene black
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home night kitchen xuejian
    $ flcam.move(-4500, 300, 900, duration=1.5)
    play music second_102 fadein 3.0 if_changed
    with dissolve
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111102280.ogg"
    aiyi "那个......大哥哥、大姐姐。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102290.ogg"
    aiyi "我有种不好的预感......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105120.ogg"
    xz "今天也会下雨吗？"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/111102300.ogg"
    aiyi "不是这样的。"
    show aiyi_dzf_b1 b1 b1_s3
    play voice "voice/爱衣/111102310.ogg"
    aiyi "是一些......更严重的事情。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105130.ogg"
    xz "比天气还严重吗？"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111102320.ogg"
    aiyi "我也不清楚......"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105140.ogg"
    xz "是吗......不过爱衣也不用太在意。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102330.ogg"
    aiyi "是这样吗？"
    show xz_dzf_b2 b2 b2_sp1 
    play voice "voice/翔子/011105150.ogg"
    xz "毕竟也不知道会发生什么吧？"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/111102340.ogg"
    aiyi "嗯，虽然是这样没错。"
    me01 "不过一直以来爱衣的直觉都很准，所以这其中一定有什么更深的意义存在。"
    hide aiyi_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/011105160.ogg"
    xz "神野君你也没必要太在意。"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/011105180.ogg"
    xz "毕竟和天气不同，如果是与我们的主观意识有关的事也只能是毫无头绪的猜测而已。"
    "的确，如果只是因为预感会出事而过度采取行动的话。"
    "往往会因为“过激反应”而最终陷入悲剧的深渊。"
    "预言什么的就是这样的东西......"
    hide xz_dzf_b2
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    me01 "爱衣现在是什么感觉？"
    show aiyi_dzf_b1 b1 b1_s3
    play voice "voice/爱衣/111102350.ogg"
    aiyi "不知道......只觉得是种不好的感觉。"
    me01 "最近才开始的吗？"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111102370.ogg"
    aiyi "嗯。"
    me01 "那有发生过什么不好事吗？"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/111102380.ogg"
    aiyi "我也不清楚......"
    "也就是说危机还未解除的意思吗。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105200.ogg"
    xz "刚才也说了，不一定就会发生在我们身边。"
    me01 "话虽如此还是有必要确认一下的。"
    hide xz_dzf_b2
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1
    me01 "爱衣你知道之前发生在神社的异常气候吗？"
    play voice "voice/爱衣/111102420.ogg"
    aiyi "......是小桃迷路的那次对吧？"
    me01 "那个时候是不是也有这种不好的预感？"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111102430.ogg"
    aiyi "......当时就觉得胸口乱糟糟的。"
    "果然如此，都说小孩子的直觉非常的灵验。"
    "如果这一切不是巧合的话。"
    "接下来说不定又会有{rb}灵纹{/rb}{rt}rune{/rt}的暴走发生。"
    "看来有必要提前做好准备才行。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105210.ogg"
    xz "好了，这个话题就到此为止，不快点吃饭的话上学要迟到了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day217'
    $ seen_day217_kindergarden_event01 = False
    $ seen_day217_school_event01 = False
    $ seen_day217_bridge_event01 = False
    $ seen_day217_laboratory_event02 = False

label day217.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day217':
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day217.kindergarden_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    elif _overworld_label == 'day217.school_event01':
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day217.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'])
    elif _overworld_label == 'day217.laboratory_event02':
        $ flcam.move(*overworld.camera_positions['laboratory'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        kindergarden=("day217.kindergarden_event01", "not seen_day217_kindergarden_event01"),
        school=("day217.school_event01", "not seen_day217_school_event01 and seen_day217_kindergarden_event01"),
        bridge=("day217.bridge_event01", "not seen_day217_bridge_event01 and seen_day217_school_event01"),
        laboratory=("day217.laboratory_event02", "not seen_day217_laboratory_event02 and seen_day217_bridge_event01"))
    $ window_animate_outro()
    if _return == 'day217.kindergarden_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day217.school_event01':
        $ flcam.move(*overworld.camera_positions['school'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day217.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day217.laboratory_event02':
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

label day217.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian
    play music second_108 fadein 3.0 if_changed
    with slowdissolve
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n5 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100110.ogg"
    lhx "困~"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    me01 "喂！"
    play sound hite_light
    show wflash onlayer texture
    with vpunch
    show lhx_dzf_b2 b2 b2_n5 at flu_down(0.15, 20):
        xpos 0.5
    pause 0.5 hard
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100120.ogg"
    lhx "感觉额头好像挨了一记手刀的感觉。"
    me01 "我确实这么做了。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b3 b3 b3_s1
    play voice "voice/立花希/031100130.ogg"
    lhx "早上好，今早也好冷啊。"
    show lhx_dzf_b3 b3 b3_s2
    play voice "voice/立花希/031100140.ogg"
    lhx "这样的日子就应该躲在被炉里才是正确的。"
    me01 "就因为你老这么想早上才会这般慵懒的。"
    show lhx_dzf_b3 b3 b3_n6
    play voice "voice/立花希/031100150.ogg"
    lhx "困~"
    me01 "别睡过去啊！"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    play sound hite_light
    show wflash onlayer texture
    with vpunch
    show lhx_dzf_b3 b3 b3_n6 at flu_down(0.15, 20):
        xpos 0.5
    me01 "我劈！"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_n4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100160.ogg"
    lhx "早上好，今早也好冷啊。"
    me01 "你是复读机吗！"
    hide lhx_dzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千川老师/141100010.ogg"
    qcls "大家早上好~"
    $ flcam.move(0, 0, 600, duration=1.5)
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    show xz_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011104640.ogg"
    xz "早上好~"
    play voice "voice/爱衣/111101860.ogg"
    aiyi "老师，今天也请多关照~"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/141100020.ogg"
    qcls "我才是，请多关照呢~"
    show xz_dzf_b2 b2 b2_n1
    play voice "voice/翔子/011104650.ogg"
    xz "老师，接下来就拜托您了。"
    play voice "voice/千川老师/141100040.ogg"
    qcls "好的，上学一路顺风。"
    hide qcls_zf_b1
    hide aiyi_dzf_b1
    hide xz_dzf_b2
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031100180.ogg"
    lhx "虽然很困，但也请注意不要懈怠。"
    me01 "这话先对你自己说去吧。"
    hide lhx_dzf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011104660.ogg"
    xz "神野君，我们走吧。"
    pause 0.5 hard
    play sound jiaobu2
    show xz_dzf_b2 b2 b2_n1 at walkout_l(0.5)
    pause 0.5 hard
    hide xz_dzf_b2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day217.kindergarden_event02:
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian2
    $ flcam.move(4500, 0, 900, duration=1.5)
    play music second_112 fadein 3.0 if_changed
    with slowdissolve
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221100290.ogg"
    ycxt "......爱衣你怎么了？"
    $ flcam.move(2250, 300, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111102440.ogg"
    aiyi "欸？"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221100300.ogg"
    ycxt "总觉得你有些消沉所以试着叫你一下。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102450.ogg"
    aiyi "是这样吗？"
    $ flcam.move(0, 200, 600, duration=1.5)
    show qianbo_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100500.ogg"
    qb "是啊，看你今天没什么精神。"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221100310.ogg"
    ycxt "发生什么事了吗？"
    show qianbo_dzf_b1 b1 b1_sp2
    play voice "voice/千波/211100510.ogg"
    qb "难道是把重要的东西弄丢了吗？"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111102470.ogg"
    aiyi "不是的......没有丢东西，只是有种不好的预感。"
    show qianbo_dzf_b1 b1 b1_sp1
    play voice "voice/千波/211100520.ogg"
    qb "今天也会下雨吗？"
    play voice "voice/小桃/221100320.ogg"
    ycxt "上次有这样预感的时候结果就下雨了。"
    show qianbo_dzf_b1 b1 b1_h4
    play voice "voice/千波/211100530.ogg"
    qb "而且那次带伞来的也只有爱衣而已。"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221100330.ogg"
    ycxt "爱衣的天气预报真的很准呢~"
    show qianbo_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211100540.ogg"
    qb "那一次是大人带着伞来接我们，所以才没有淋湿。"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221100340.ogg"
    ycxt "但是爱衣你今天也没有带伞来。"
    hide qianbo_dzf_b1
    show qianbo_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100550.ogg"
    qb "爱衣说的不好的预感不是指天气吗？"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/111102490.ogg"
    aiyi "我也不知道......也可能只是错觉而已。"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221100350.ogg"
    ycxt "爱衣......你的脸色好差啊。"
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100560.ogg"
    qb "果然是因为身体不舒服吧？比如感冒什么的。"
    play voice "voice/小桃/221100360.ogg"
    ycxt "最近也特别冷的说......"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102500.ogg"
    aiyi "......"
    show qianbo_dzf_b1 b1 b1_a1
    play voice "voice/千波/211100570.ogg"
    qb "果然爱衣有点不对劲，还是去保健室休息一下吧？"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221100370.ogg"
    ycxt "要我叫老师来吗？"
    show aiyi_dzf_b1 b1 b1_sp2
    play voice "voice/爱衣/111102510.ogg"
    aiyi "......不用了，我没关系的。"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    hide qianbo_dzf_b1 with None
    pause 0.1 hard
    show qianbo_dzf_b2 b2 b2_a3 onlayer m2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211100580.ogg"
    qb "勉强的话反而会恶化的，我现在就去叫老师来！"
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b2 b2 b2_a3 at walkout_l(0.3)
    pause 1.0 hard
    hide qianbo_dzf_b2
    $ flcam.move(2250, 300, 750, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    show ycxt_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111102520.ogg"
    aiyi "啊......走掉了。"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221100380.ogg"
    ycxt "千波她就是这么担心爱衣的。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102530.ogg"
    aiyi "抱歉......"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221100390.ogg"
    ycxt "为、为什么要道歉？"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111102540.ogg"
    aiyi "明明只是感觉而已，却把事情闹大了。"
    play voice "voice/小桃/221100400.ogg"
    ycxt "不是感冒吗？"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102550.ogg"
    aiyi "我也不知道。"
    show ycxt_dzf_b1 b1 b1_s2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/221100410.ogg"
    ycxt "不是爱衣的错，毕竟爱衣的预感一直很准的。"
    show ycxt_dzf_b1 b1 b1_s4
    play voice "voice/小桃/221100420.ogg"
    ycxt "所以应该担心的是接下来会不会发生不好的事情。"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111102560.ogg"
    aiyi "是这样吗？"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221100430.ogg"
    ycxt "应该就是这样......大概。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/111102570.ogg"
    aiyi "如果真的发生什么不好的事情，就必须想点办法才行。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102580.ogg"
    aiyi "阻止不好的事情发生才对吧。"
    show ycxt_dzf_b1 b1 b1_s3
    play voice "voice/小桃/221100440.ogg"
    ycxt "或许......是这样没错。"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b1 b1 b1_h2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/千波/211100590.ogg"
    qb "我把老师叫来了~"
    hide qianbo_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千川老师/141100090.ogg"
    qcls "爱衣，听说你身体不舒服？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111102590.ogg"
    aiyi "啊，那个......"
    hide qcls_zf_b1
    $ flcam.move(2250, 300, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221100450.ogg"
    ycxt "爱衣，还是去保健室休息一下比较好。"
    play voice "voice/小桃/221100460.ogg"
    ycxt "不好的预感也不要太在意了。"
    hide aiyi_dzf_b1
    pause 0.5 hard
    show qianbo_dzf_b2 b2 b2_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/千波/211100600.ogg"
    qb "你们在说什么？"
    show ycxt_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/221100470.ogg"
    ycxt "大人的话题哟~"
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/千波/211100610.ogg"
    qb "我不在也能讨论这样的话题，小桃你也成长了啊。"
    hide ycxt_dzf_b1
    hide qianbo_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100100.ogg"
    qcls "啊啦啊啦，明明三人之中千波才是最不成熟的那一个。"
    hide qcls_zf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at flu_up(0.15, 20):
        xpos 0.5
    pause 0.5 hard
    play voice "voice/千波/211100620.ogg"
    qb "这句话我可不能装作没听见啊！"
    pause 0.5 hard
    play sound hide_sound
    show qianbo_dzf_b1 b1 b1_a2 at walkout_l(0.5)
    pause 1.0 hard
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221100480.ogg"
    ycxt "虽、虽然不知道怎么回事，但就这么跑掉了......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_h3 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141100110.ogg"
    qcls "千波一直都很有精神呢~"
    hide ycxt_dzf_b1
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111102600.ogg"
    aiyi "......"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141100120.ogg"
    qcls "爱衣也想变成像千波那样有精神的话，不好好休息可不行。"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111102610.ogg"
    aiyi "嗯。"
    show qcls_zf_b1 b1 b1_h3
    play voice "voice/千川老师/141100130.ogg"
    qcls "外面很冷的，赶紧回屋里吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    play sound open_door5
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian
    $ flcam.move(4500, 300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111102620.ogg"
    aiyi "老师......不是要去保健室吗？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141100140.ogg"
    qcls "在那之前我有话想对爱衣说。"
    play voice "voice/爱衣/111102630.ogg"
    aiyi "是什么？"
    play music second_123 fadein 3.0 if_changed
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100150.ogg"
    qcls "爱衣的身体不舒服是因为有不好的预感吗？"
    show aiyi_dzf_b1 b1 b1_s3 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/爱衣/111102640.ogg"
    aiyi "那、那个......大概是的。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141100160.ogg"
    qcls "是什么样的感觉能说说看吗？"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102650.ogg"
    aiyi "对不起......爱衣我自己也不是很清楚。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100170.ogg"
    qcls "是吗......果然。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111102660.ogg"
    aiyi "欸？"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100180.ogg"
    qcls "据说{rb}预知未来{/rb}{rt}precognition{/rt}所能描述的也只有一些{encyclopedia=bansheng}伴生现象{/encyclopedia}而已。"
    play voice "voice/爱衣/111102670.ogg"
    aiyi "pre......什么？"
    show qcls_zf_b1 b1 b1_h3
    play voice "voice/千川老师/141100190.ogg"
    qcls "爱衣不知道也没关系的。"
    hide aiyi_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100200.ogg"
    qcls "但我们却必须要知道。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100210.ogg"
    qcls "如果圣护院主任没有骗我，也就是说星天宫那里已经开始有所行动了......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111102680.ogg"
    aiyi "老、老师？"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141100220.ogg"
    qcls "所以爱衣，接下来希望你能陪我去个地方。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day217.battle_lhx_qcls:
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian2
    with slowdissolve
    pause 2.0 hard
    show wflash onlayer texture
    play sound rune1
    play music second_137 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100490.ogg"
    lhx "......"
    "突然胸口一紧。"
    "通过{rb}接触感应{/rb}{rt}psychometry{/rt}察觉到了空气中稀薄的灵力。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    show lhx_dzf_b1 b1 b1_s2 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031100500.ogg"
    lhx "刚刚的是......"
    hide lhx_dzf_b1
    pause 1.0 hard
    scene set only school day inside xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100510.ogg"
    lhx "是错觉......吗？"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play sound open_door5
    scene set only school day inside xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 2.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    "教室里除了玩耍嬉戏的小孩子以外没有任何异常。"
    "要说唯一和往常不同的就是一直围着凉君的“热闹三人组”现在只剩下两位。"
    "爱衣不见了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with right2left_02
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian
    with right2left_02
    pause 1.0 hard
    play music second_146 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千川老师/141100240.ogg"
    qcls "......立花老师。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dzf_b3 b3 b3_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100580.ogg"
    lhx "为什么会带着爱衣在这里？"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141100250.ogg"
    qcls "爱衣说她身体不舒服好像是发烧了。所以我接下来打算带她去医院。"
    play voice "voice/千川老师/141100280.ogg"
    qcls "幼儿园人手本来就不够......当然有立花老师在的话我也多少有些放心了。"
    show lhx_dzf_b3 b3 b3_ga1
    play voice "voice/立花希/031100590.ogg"
    lhx "爱衣身体不舒服的话，联络青木翔子才是正确的选择吧？"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100290.ogg"
    qcls "虽然是这样没错，但我觉得让她太过担心也不太好。况且青木同学现在应该还在学校。"
    show lhx_dzf_b3 b3 b3_n2
    play voice "voice/立花希/031100600.ogg"
    lhx "也就是说这件事目前还没有人知道吗？"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100300.ogg"
    qcls "是这样的。"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141100310.ogg"
    qcls "爱衣的事情就交给我吧，立花老师也快点回到工作中......"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100610.ogg"
    lhx "你打算把爱衣带去哪里？"
    show qcls_zf_b1 b1 b1_sp2
    play voice "voice/千川老师/141100320.ogg"
    qcls "所以说是去医院......"
    show lhx_dzf_b2 b2 b2_s1
    play voice "voice/立花希/031100620.ogg"
    lhx "真的是去医院吗？"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100330.ogg"
    qcls "......"
    hide qcls_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100630.ogg"
    lhx "就在刚才，我在幼儿园里察觉到了{rb}灵纹{/rb}{rt}rune{/rb}的存在，一开始还以为是场误会。"
    play voice "voice/立花希/031100640.ogg"
    lhx "然后就撞见了你，而你却很不自然地想要把我支开。"
    show lhx_dzf_b3 b3 b3_ga1
    play voice "voice/立花希/031100650.ogg"
    lhx "也不说一声就想要把爱衣带到走。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100340.ogg"
    qcls "......"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100660.ogg"
    lhx "我再问一次......你接下来要去的地方真的是医院吗？"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100350.ogg"
    qcls "是的。"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031100670.ogg"
    lhx "你真是不擅长说谎啊。"
    show qcls_zf_b1 b1 b1_sp1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千川老师/141100370.ogg"
    qcls "......"
    show lhx_dzf_b2 b2 b2_ga1
    play voice "voice/立花希/031100680.ogg"
    lhx "听到我口中的{rb}灵纹{/rb}{rt}rune{/rb}一词还能若无其事地对话。"
    show lhx_dzf_b2 b2 b2_s1
    play voice "voice/立花希/031100690.ogg"
    lhx "也就是说你是知道{rb}灵纹{/rb}{rt}rune{/rt}的存在，既然如此也只有你也是{rb}灵继者{/rb}{rt}elfin{/rt}这一种可能了。"
    show lhx_dzf_b2 b2 b2_a1
    play voice "voice/立花希/031100700.ogg"
    lhx "难道不是你在这所幼儿园里使用{rb}灵纹{/rb}{rt}rune{/rt}的吗？"
    show qcls_zf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千川老师/141100360.ogg"
    qcls "......"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031100710.ogg"
    lhx "奇怪的是从你的身上我察觉不到灵力的存在。不止是现在，一直以来都是如此。"
    show lhx_dzf_b2 b2 b2_n2
    play voice "voice/立花希/031100730.ogg"
    lhx "排除一切可能因素，再离谱的也只能是真相了。"
    hide qcls_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b2
    show lhx_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100780.ogg"
    lhx "{rb}虚无{/rb}{rt}psi-missing{/rt}——能消除{rb}灵纹{/rb}{rt}rune{/rt}的{rb}灵纹{/rb}{rt}rune{/rt}。"
    hide lhx_dzf_b1
    show lhx_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100790.ogg"
    lhx "虽然是一种用来化解对方招式的{rb}灵纹{/rb}{rt}rune{/rt}，但你却用它来伪装自己。"
    play voice "voice/立花希/031100800.ogg"
    lhx "为了平时不让人察觉自己是{rb}灵继者{/rb}{rt}elfin{/rt}吗。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100810.ogg"
    lhx "为了隐藏你的真实身份。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100400.ogg"
    qcls "为何还是......被你发现了。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100410.ogg"
    qcls "没错......正如你所说的那样，我也是一名{rb}灵继者{/rb}{rt}elfin{/rt}。"
    show lhx_dzf_b2 b2 b2_ga1
    play voice "voice/立花希/031100840.ogg"
    lhx "不打算再继续隐瞒了吗？"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141100420.ogg"
    qcls "就算想隐瞒，我也不认为你会善罢甘休。"
    show lhx_dzf_b2 b2 b2_h3
    play voice "voice/立花希/031100850.ogg"
    lhx "明智的判断。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141100430.ogg"
    qcls "回到最初的问题，为什么你会知道我是{rb}灵继者{/rb}{rt}elfin{/rt}呢？"
    play voice "voice/千川老师/141100440.ogg"
    qcls "不会仅仅是因为套出了我的话吧？"
    show lhx_dzf_b3 b3 b3_n2
    play voice "voice/立花希/031100720.ogg"
    lhx "即使对于不是{rb}灵继者{/rb}{rt}elfin{/rt}的人，我也能通过接触获取对方的情报。"
    show lhx_dzf_b3 b3 b3_n4
    play voice "voice/立花希/031100890.ogg"
    lhx "但是你太过“干净”了。"
    show lhx_dzf_b3 b3 b3_s2
    play voice "voice/立花希/031100900.ogg"
    lhx "就连我的{rb}接触感应{/rb}{rt}psychometry{/rt}也没有办法窥探你的内心。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100470.ogg"
    qcls "......"
    hide qcls_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100910.ogg"
    lhx "你用{rb}虚无{/rb}{rt}psi-missing{/rt}隐藏自己{rb}灵纹{/rb}{rt}rune{/rt}的同时。"
    play voice "voice/立花希/031100920.ogg"
    lhx "也暴露了自己是{rb}灵继者{/rb}{rt}elfin{/rt}的事实。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100480.ogg"
    qcls "的确，我一开始是不打算使用的。"
    hide lhx_dzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141100490.ogg"
    qcls "但自从上一次我知道了你是{rb}接触感应{/rb}{rt}psychometry{/rt}的使用者。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100500.ogg"
    qcls "因为担心暴露身份我才会出此下策。"
    show qcls_zf_b1 b1 b1_n2
    play voice "voice/千川老师/141100510.ogg"
    qcls "明明这么努力地避免接触到身为{rb}灵继者{/rb}{rt}elfin{/rt}的你，可是到头来还是暴露了。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031100990.ogg"
    lhx "你的{rb}虚无{/rb}{rt}psi-missing{/rt}真的十分方便。不仅能消除能力，连“存在”本身也能抹去。"
    play voice "voice/立花希/031101000.ogg"
    lhx "某种意义上可以说和我的{rb}接触感应{/rb}{rt}psychometry{/rt}正好相反。"
    play voice "voice/千川老师/141100540.ogg"
    qcls "......"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031101020.ogg"
    lhx "你这样做的理由究竟是什么？"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141100550.ogg"
    qcls "也没有什么特别的理由。"
    show lhx_dzf_b2 b2 b2_ga1
    play voice "voice/立花希/031101040.ogg"
    lhx "真的吗？"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141100570.ogg"
    qcls "是真的。"
    show lhx_dzf_b2 b2 b2_a1
    play voice "voice/立花希/031101050.ogg"
    lhx "不惜隐瞒真实身份，难道不是因为背后组织的利害关系吗？"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141100580.ogg"
    qcls "......立花老师果然机智过人。"
    show qcls_zf_b1 b1 b1_h3
    play voice "voice/千川老师/141100590.ogg"
    qcls "但这个世界不是只靠理论运作的，作为人生的前辈我想如此告诫你。"
    show lhx_dzf_b2 b2 b2_a1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031101120.ogg"
    lhx "你对爱衣做了什么？"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100610.ogg"
    qcls "......"
    show lhx_dzf_b2 b2 b2_ga1
    play voice "voice/立花希/031101130.ogg"
    lhx "果然不肯说吗。"
    play voice "voice/千川老师/141100620.ogg"
    qcls "不是的。"
    stop music fadeout 5.0
    hide lhx_dzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_s3
    play voice "voice/千川老师/141100630.ogg"
    qcls "因为你马上就会知道了。"
    $ flcam.move(-4500, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide qcls_zf_b1
    play sound rune1
    show qcls_zf_b2_rune b2 b2 b2_s3 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100640.ogg"
    qcls "愿天主赐予福祸。"
    show qcls_zf_b2_rune b2 b2 b2_s3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千川老师/141100650.ogg"
    qcls "随汝身承神明之庇护。"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    pause 1.0 hard
    play sound rune2
    scene white 
    with in2out_02_l
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg kindergarden2
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        ## 初始化参数
        # Boss为立花希，装备为随机普通6件，等级5，技能满级
        lhx_role_mirror.equip_experience = 99999999
        for cate in lhx_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
            sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
            sample_outfit = enemy_outfits[sample_index]
            sample_outfit.init_params()
            for xi in range(4):
                sample_outfit.level_up(lhx_role_mirror, 100)
            sample_outfit.enemy_equip_on(lhx_role_mirror)
        for xi in range(20):
            lhx_role_mirror.skill_levelup()

        # 我方为千川老师，装备为随机传说6件，等级10，技能满级
        qcls_role_mirror.equip_experience = 99999999
        qcls_role_mirror.stats_check(to_level=30, limit=True)
        for cate in qcls_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if ("_04" in outfit.objectname and outfit.category == cate)]
            sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
            sample_outfit = enemy_outfits[sample_index]
            sample_outfit.init_params()
            for xi in range(9):
                sample_outfit.level_up(qcls_role_mirror, 100)
            sample_outfit.enemy_equip_on(qcls_role_mirror)
        for xi in range(20):
            qcls_role_mirror.skill_levelup()

        log_party = copy(local_config.party)
        local_config.party = [qcls_role_mirror]

        # 初始化结界“妄想颠覆”，只有在面具存在的时候才能造成伤害，否则为1
        local_config.tutorial_step = "虚无封印"

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=lhx_role_mirror, 
                boss_hp_plus=8000,
                side_enemy=[], 
                side_hp_plus=0,
                level=30,
                boss_first=True, 
                win_condition='normal',
                stay_turn=0,
                inside_label="inside_battle11", 
                mission_type="normal", 
                treasures={
                    "eggs": (2, 0.6),
                    "soul_piece": (2, 0.3),
                    "soul_raise": (2, 0.3),
                    "wind_break_small": (3, 0.3),
                    "wind_break_large": (1, 0.3)
                })

    if _return == "win":
        "战斗胜利！"
        python:
            qcls_role_mirror.full_reset(heal_hp=True, ally_environment_effects=None, turn_end=True, level_reset=True)
            local_config.party = log_party
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day217.after_battle_lhx_qcls

label day217.after_battle_lhx_qcls:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian
    play music second_126 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dzf_b1 b1 b1_rs1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031101140.ogg"
    lhx "......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100660.ogg"
    qcls "就算你想拉开距离也已经晚了。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100680.ogg"
    qcls "只注意到我是{rb}虚无{/rb}{rt}psi-missing{/rt}的使用者是你太大意了。"
    pause 1.0 hard
    play sound rune3
    scene white 
    with right2left_02
    pause 1.0 hard
    "立花希的视线开始扭曲，对方的声音也渐渐变得模糊起来。"
    "一股强烈的睡意袭来。"
    pause 0.5 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian
    with right2left_02
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n4 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100690.ogg"
    qcls "居然没有马上昏过去真叫人吃惊......立花老师果然是一名优秀的{rb}灵继者{/rb}{rt}elfin{/rt}。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    show lhx_dzf_b1 b1 b1_rs1 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031101150.ogg"
    lhx "抱歉......凉君。"
    play voice "voice/立花希/031101160.ogg"
    lhx "还是没能保护好你的家人。"
    hide lhx_dzf_b1
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day217_kindergarden_event01:
        $ seen_day217_kindergarden_event01 = True
    $ _overworld_label = 'day217.kindergarden_event01'
    jump day217.map

label day217.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian3
    with slowdissolve
    pause 1.0 hard
    play sound rune1
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "这是......"
    play music second_122 fadein 3.0 if_changed
    "断断续续的念波回荡在空气中。"
    "这么快就来了吗。"
    "爱衣早上说的“不好的预感”指的应该就是这个吧。"
    play sound open_door5
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian2
    with dissolve
    pause 1.0 hard
    play sound jiaobu3
    pause 1.0 hard
    play voice "voice/琉璃/041100140.ogg"
    stranger "啊咧......前辈？"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/041100150.ogg"
    liuli "果然是神野前辈，有急事吗？"
    me01 "抱歉琉璃，我现在有很重要的事情要处理。"
    show liuli_dzf_b2 b2 b2_s2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041100170.ogg"
    liuli "抱歉打扰到你......不过既然会在这里想必也是早退了吧。"
    play voice "voice/琉璃/041100180.ogg"
    liuli "和我一样的。"
    "琉璃也......难道说。"
    me01 "琉璃你现在要去的地方莫非是星天宫研究所？"
    hide liuli_dzf_b2
    show liuli_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041100210.ogg"
    liuli "是这样的......前辈居然会知道。"
    show liuli_dzf_b1 b1 b1_s2
    play voice "voice/琉璃/041100220.ogg"
    liuli "就在刚才圣护院小姐突然联络我，要我尽快赶回研究所。"
    play voice "voice/琉璃/041100230.ogg"
    liuli "好像说是有什么重要的工作。"
    me01 "没有告诉你具体的工作内容吗？"
    show liuli_dzf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041100240.ogg"
    liuli "是的......"
    "如果这一次的行动也和星天宫有关的话，那么一定有人被安排在爱衣的身边。"
    "可是幼儿园除了一群小孩子就只剩下老师了。"
    "千波虽然很可疑，但是同样是小孩子的她应该掀不起什么风浪才对。"
    "立花老师也不太可能会做什么对爱衣不理的事情。"
    "难道说......"
    me01 "还有一个问题。"
    show liuli_dzf_b1 b1 b1_sp1
    play voice "voice/琉璃/041100250.ogg"
    liuli "好、好的，是什么呢？"
    me01 "琉璃你认识千川老师吗？"
    show liuli_dzf_b1 b1 b1_n1
    play voice "voice/琉璃/041100260.ogg"
    liuli "是的，就是在幼儿园工作的那位吧？"
    me01 "你有在研究所见到过她吗？"
    show liuli_dzf_b1 b1 b1_h1
    play voice "voice/琉璃/041100270.ogg"
    liuli "是有几次，她好像也是圣护院小姐的朋友所以偶尔会来拜访。"
    "最不愿意相信的事情发生了。"
    "如果这次的对手是那位温柔的老师的话。"
    "我还能下得去手吗......"
    hide liuli_dzf_b1
    show liuli_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041100280.ogg"
    liuli "那个......有什么问题吗？"
    me01 "没什么，正好我也要去研究所，不如一起吧？"
    me01 "这次还得麻烦你带路了。"
    show liuli_dzf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041100310.ogg"
    liuli "请交给我吧~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day217.school_event02:
    $ flcam.move(0, 0, 0)
    scene set only school day corridor xuejian
    play music second_102 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show yj_dzf_b2 b2 b2_s2 onlayer m1 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/植澄友加/021101450.ogg"
    yj "呐......听说凉君他早退了？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_s1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/翔子/011105560.ogg"
    xz "好像是这样的。"
    show yj_dzf_b2 b2 b2_sp1
    play voice "voice/植澄友加/021101460.ogg"
    yj "理由是？"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/011105570.ogg"
    xz "说是身体不舒服。"
    show yj_dzf_b2 b2 b2_ga1
    play voice "voice/植澄友加/021101470.ogg"
    yj "是因为感冒？"
    show xz_dzf_b2 b2 b2_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/011105580.ogg"
    xz "不......大概是装病吧。"
    show yj_dzf_b2 b2 b2_s2
    play voice "voice/植澄友加/021101480.ogg"
    yj "装病......为什么？"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/011105590.ogg"
    xz "理由我也不知道。"
    show yj_dzf_b2 b2 b2_ga1
    play voice "voice/植澄友加/021101490.ogg"
    yj "不会是单纯的不想上课吧......"
    show xz_dzf_b2 b2 b2_n1
    play voice "voice/翔子/011105600.ogg"
    xz "我想不是的，从至今为止神野君的表现来看他对学习还是很用心的。"
    show yj_dzf_b2 b2 b2_ga4 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021101500.ogg"
    yj "我大部分时间都在睡觉，完全没注意到凉君的学习状态。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105610.ogg"
    xz "......"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/021101510.ogg"
    yj "......翔子？"
    hide yj_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b3 b3 b3_s2
    play voice "voice/翔子/011105620.ogg"
    xz "神野君突然早退，是和爱衣说的“不好的预感”有关吧。（小声）"
    play voice "voice/翔子/011105630.ogg"
    xz "还是我想多了吗。（小声）"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b1 b1 b1_s2 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/021101520.ogg"
    yj "凉君搞不好是去工作了。（小声）"
    hide xz_dzf_b3
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105640.ogg"
    xz "工作？"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_ga3 onlayer m1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021101530.ogg"
    yj "没、没什么......"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105650.ogg"
    xz "友加你果然有什么事情瞒着我吧？"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_s2 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/021101540.ogg"
    yj "不要问我......还是让凉君告诉你比较好。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105660.ogg"
    xz "......"
    show yj_dzf_b2 b2 b2_n3 at flu_down(0.35, 20):
        xpos 0.3
    show yj smile02 with dissolve
    play voice "voice/植澄友加/021101570.ogg"
    yj "不用担心的~"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011105810.ogg"
    xz "......"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b2 b2 b2_n1
    play voice "voice/植澄友加/021101580.ogg"
    yj "即使现在凉君有事瞒着你，总有一天他也会告诉翔子你的。"
    play voice "voice/植澄友加/021101590.ogg"
    yj "就算不由我来说......对吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day217_school_event01:
        $ seen_day217_school_event01 = True
    $ _overworld_label = 'day217.school_event01'
    jump day217.map

label day217.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    play music second_126 fadein 3.0 if_changed
    with dissolve
    pause 2.0 hard
    scene set only bridge day xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100010.ogg"
    szl "果然来了吗。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041100320.ogg"
    liuli "水之濑前辈......"
    me01 "你们果然也认识吗？"
    hide szl_dzf_b3
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dzf_b3
    show liuli_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041100330.ogg"
    liuli "是、是的，不过平时没怎么说过话。"
    me01 "所以她会出现在这里也是因为你刚刚说的“工作”？"
    show liuli_dzf_b1 b1 b1_s1
    play voice "voice/琉璃/041100340.ogg"
    liuli "这、这个......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100020.ogg"
    szl "花山院......不要说些多余的话。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100030.ogg"
    szl "比起这个你赶紧过去吧，主任还在等着你。"
    hide liuli_dzf_b1 with None
    pause 0.1 hard
    show liuli_dzf_b3 b3 b3_s5 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/琉璃/041100350.ogg"
    liuli "好、好的，但是......"
    hide liuli_dzf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "水之濑同学才是，不上课在这里做什么？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100040.ogg"
    szl "和你有什么关系吗？"
    me01 "现在这个时间你不是应该在学校的吗？"
    show szl_dzf_b3 b3 b3_s1
    play voice "voice/水之濑/051100050.ogg"
    szl "也许是这样吧。"
    me01 "可这和你实际做的可不一样。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100060.ogg"
    szl "我只是奉命在这里等花山院而已，反倒是你怎么也一起来了？"
    me01 "就像你刚刚说的，和你有什么关系吗。"
    show szl_dzf_b2 b2 b2_s4
    play voice "voice/水之濑/051100070.ogg"
    szl "不打算回答我的问题是吧？"
    me01 "你的工作就是在这里拦住碍事的人？"
    me01 "就像上次那样。"
    show szl_dzf_b2 b2 b2_s3
    play voice "voice/水之濑/051100080.ogg"
    szl "......"
    me01 "星天宫果然很可疑。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/051100090.ogg"
    szl "我没有回答你的义务。"
    me01 "你们打算把爱衣怎么样？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100100.ogg"
    szl "原来如此。"
    show szl_dzf_b3 b3 b3_n2
    play voice "voice/水之濑/051100110.ogg"
    szl "这次又被你抢先了，不过我们也早就料到会有这个结果。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100120.ogg"
    szl "看来是千川老师那边大意了啊。"
    me01 "大意的是你吧。"
    show szl_dzf_b2 b2 b2_sp1
    play voice "voice/水之濑/051100130.ogg"
    szl "......"
    me01 "到目前为止我所能确定的也只有“你是星天宫的一份子”这项事实而已。"
    me01 "因为在意先前爱衣提到过的“预感”我才故意拿她来套话的。"
    me01 "只是没想到你承认得那么干脆。"
    show szl_dzf_b2 b2 b2_ga2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051100140.ogg"
    szl "......"
    me01 "所以你到底想怎么样？"
    show szl_dzf_b2 b2 b2_n2
    play voice "voice/水之濑/051100150.ogg"
    szl "虽然对于你的提问我没有回答的义务，但是这次还是告诉你好了。"
    show szl_dzf_b2 b2 b2_n1
    play voice "voice/水之濑/051100160.ogg"
    szl "反正这也是为了争取时间而采取的手段罢了。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100170.ogg"
    szl "正如你所说我出现在这里的理由是为了排除碍事之人。"
    show szl_dzf_b3 b3 b3_s1
    play voice "voice/水之濑/051100180.ogg"
    szl "主任那边接到了千川小姐的电话，说这此的行动被立花希发现了。"
    show szl_dzf_b3 b3 b3_a1
    play voice "voice/水之濑/051100190.ogg"
    szl "考虑到她会通过{rb}思维透视{/rb}{rt}telepathy{/rt}联系你的可能性很高。"
    show szl_dzf_b3 b3 b3_s2
    play voice "voice/水之濑/051100200.ogg"
    szl "只是没想到先被你用日向爱衣作为诱饵套出了情报......这一点确实是我的失策。"
    show szl_dzf_b3 b3 b3_n3
    play voice "voice/水之濑/051100210.ogg"
    szl "不管怎么说，我现在有确保花山院安全抵达研究所的任务在身。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dzf_b3 b3 b3_s5 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041100360.ogg"
    liuli "那、那个......从刚才开始你们在说什么？"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100220.ogg"
    szl "不用在意，比起这个快点去研究所吧，这是命令吧？"
    hide liuli_dzf_b3
    show liuli_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041100370.ogg"
    liuli "话是这么说没错......"
    show szl_dzf_b2 b2 b2_ga1
    play voice "voice/水之濑/051100230.ogg"
    szl "你好像从刚才开始就很在意这家伙，不会是想带他一起去吧？"
    hide liuli_dzf_b1
    show liuli_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041100380.ogg"
    liuli "就是这样打算的。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/051100240.ogg"
    szl "......你的缺点就是太老好人了，到底是为了什么才加入星天宫的啊。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100250.ogg"
    szl "没时间了，你快去研究所。"
    play voice "voice/水之濑/051100260.ogg"
    szl "这个命令是绝对的。"
    show szl_dzf_b3 b3 b3_n2
    play voice "voice/水之濑/051100270.ogg"
    szl "所以......听好了。"
    hide liuli_dzf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b3 b3 b3_n3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051100280.ogg"
    szl "即使春天来临，{rb}天使{/rb}{rt}elf{/rt}的愿望也不会实现。"
    play voice "voice/水之濑/051100290.ogg"
    szl "即便是百般祈求，也终究是无法成为人类的。"
    pause 0.5 hard
    hide szl_dzf_b3
    $ flcam.move(0, -100, 400, duration=1.5, warper='ease_cubic')
    pause 1.0 hard
    play sound bottle_drop2
    show bottle onlayer b2_c2u:
        xpos 0.0
    with vpunch
    "琉璃手上拿着的饮料瓶应声落地。"
    hide bottle
    pause 0.5 hard
    inventory add bottle
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "看着这样反常的举动。"
    "一种不好的预感涌上心头。"
    pause 1.0 hard
    scene set only bridge day xuejian
    $ flcam.move(2250, 0, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    show liuli_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051100300.ogg"
    szl "我再说一次。"
    play voice "voice/水之濑/051100310.ogg"
    szl "主任在等你，快去研究所吧。"
    hide szl_dzf_b2
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_n4
    play voice "voice/琉璃/041100390.ogg"
    liuli "我知道了。"
    "声音没有起伏，就像是毫无感情的机器一般。"
    "这样的琉璃和我先前认识的简直判若两人。"
    pause 0.5 hard
    play sound jiaobu2
    show liuli_dzf_b2 b2 b2_n4 at walkout_r(0.7)
    pause 1.0 hard
    hide liuli_dzf_b2
    me01 "琉璃！" with vpunch
    "不管我怎么呼唤，琉璃始终没有停下脚步。"
    "我只能眼睁睁地看着她越走越远。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    me01 "刚才那是......什么？"
    play voice "voice/水之濑/051100330.ogg"
    szl "这些话的含义我自己也不是很清楚。"
    me01 "既然这样就不要拦着我。"
    hide szl_dzf_b2
    $ flcam.move(7500, -500, 1500, duration=1.5)
    pause 2.0 hard
    "就在我刚迈出脚的一瞬间。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_n3 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/水之濑/051100340.ogg"
    szl "且慢！"
    me01 "快让开！"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100350.ogg"
    szl "这我可办不到，不是说过了吗，我的任务是排除碍事之人。"
    me01 "你们带走爱衣到底是为了什么？"
    show szl_dzf_b3 b3 b3_n3
    play voice "voice/水之濑/051100370.ogg"
    szl "明知道我不会回答你可还是问了，不过这对我来说也是有好处的。"
    me01 "因为能争取时间？"
    show szl_dzf_b3 b3 b3_n2
    play voice "voice/水之濑/051100380.ogg"
    szl "你也不喜欢毫无意义的战斗吧？"
    me01 "......无论如何也不肯放我过去吗？"
    show szl_dzf_b3 b3 b3_n1
    play voice "voice/水之濑/051100390.ogg"
    szl "等一切结束了自然会让你过去的。"
    me01 "那个时候爱衣她会怎样？"
    show szl_dzf_b3 b3 b3_s1
    play voice "voice/水之濑/051100400.ogg"
    szl "不知道，也和我没关系......"
    me01 "那就只好得罪了！"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100410.ogg"
    szl "都说了这里是禁止通行的。"
    me01 "那就只好强行突破了。"
    show szl_dzf_b2 b2 b2_n1
    play voice "voice/水之濑/051100420.ogg"
    szl "嘿~想用武力吗？"
    me01 "虽然并非我的本意，但眼下也只有这一种办法了。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_a1
    play voice "voice/水之濑/051100430.ogg"
    szl "既然这样的话我就奉陪到底吧，毕竟上次的胜负还没有分出来呢。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    play sound rune2
    scene set only myself_cg one
    with slowdissolve
    play music second_149 fadein 3.0 if_changed
    play ambience1 strong_wind fadein 3.0
    pause 1.0 hard
    "我发动{rb}念动立场{/rb}{rt}psychokinesis{/rb}在周围席卷起一阵狂风。"
    "打算在水之濑召唤太刀之前借助风暴的掩护快速撤离。"
    "上次的手段已经行不通了，简单的障眼法又会被她轻易地识破。"
    "从上一次的交战过后我就意识到了，想要战胜水之濑不出其不意是无法做到的。"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    scene set only bridge day xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_b3 b3 b3_a2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100440.ogg"
    szl "{rb}幻境化物{/rb}{rt}apports{/rt}！"
    play sound rune3
    scene white 
    with right2left_02
    pause 1.0 hard
    "几乎就在我抬手的一瞬间，身子忽然被一阵强大的力道掀翻在地。"
    "紧接而来的强烈疼痛让我几乎无法动弹。"
    "这是什么......就像被千钧巨石压在身上一般。"
    "上次那个果然是她手下留情了吗？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge day under xuejian
    with right2left_02
    pause 1.0 hard
    play sound hite_heavy
    with vpunch
    me01 "......呃哈！"
    "我抬头一看，自己已然身处桥下的河滩上。"
    "这次的{rb}幻境化物{/rb}{rt}apports{/rt}移动的目标竟然是我吗......"
    "可恶啊，刚才那一摔差点就让我失去知觉了。"
    me01 "对待同级生你就不能温柔一些吗！"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_knife_b2_rune b2 b2 b2_ga1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/水之濑/051100450.ogg"
    szl "我就猜到会是这样，嘴上说着武力解决，心里却只想着逃跑。"
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100460.ogg"
    szl "别太让我失望啊。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show szl_dzf_knife_b3_rune b3 b3 b3_n1
    play voice "voice/水之濑/051100470.ogg"
    szl "我可是期待着你陪我打发时间呢。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/水之濑/051100480.ogg"
    szl "别再只想着逃了。"
    play voice "voice/水之濑/051100490.ogg"
    szl "我的{rb}幻镜化物{/rb}{rt}apports{/rt}可以隔空操控物体。"
    play voice "voice/水之濑/051100500.ogg"
    szl "所以包括你的身体在内，将你拉回来这种事也是很容易就能办到的。"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051100510.ogg"
    szl "......连打发时间都谈不上啊~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day217.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory day outside xuejian
    with slowdissolve
    pause 2.0 hard
    scene set only laboratory inside3 xuejian
    with dissolve
    pause 1.0 hard
    play music second_123 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/圣护院/151100210.ogg"
    shy "好了，接下来只要等花山院过来就可以了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_n4 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100720.ogg"
    qcls "是的，我这边也准备就绪了。"
    hide shy_yjf_b1
    hide qcls_zf_b1
    $ flcam.move(0, 0, 0, duration=1.5, warper='easeout_quint')
    pause 1.0 hard
    "在两人面前的是一座拥有高精密仪器的实验台。"
    "此时熟睡中的爱衣正躺在上面。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151100230.ogg"
    shy "花山院马上就到，我已经让水之濑去接她了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100740.ogg"
    qcls "是吗......是为了防止出现意外才这么安排的对吧？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151100240.ogg"
    shy "没错，毕竟上头要求我们的计划万无一失。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100250.ogg"
    shy "所以这也是提高成功率的手段。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100750.ogg"
    qcls "......"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151100270.ogg"
    shy "这次的行动虽然手段强硬了点，但是还算顺利。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151100280.ogg"
    shy "主要是因为有你和水之濑两人在，我为有你们这样优秀的部下而感到庆幸。"
    show qcls_zf_b1 b1 b1_sp2
    play voice "voice/千川老师/141100750.ogg"
    qcls "......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100290.ogg"
    shy "剩下的就只有等花山院的到达之后才能进行了。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100760.ogg"
    qcls "到那个时候......我也必须解除{rb}虚无{/rb}{rt}psi-missing{/rt}对吧。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100300.ogg"
    shy "没错，不然不只是你自己，就连日向爱衣也无法发动{rb}灵纹{/rb}{rt}rune{/rt}。"
    hide qcls_zf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/圣护院/151100330.ogg"
    shy "{rb}预知未来{/rb}{rt}precognition{/rt}在一般情况下，单独使用的意义不大。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100340.ogg"
    shy "就像是魔术师的障眼法一样，净是一些不明所以的暗示。"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151100350.ogg"
    shy "但如果是和{rb}接触感应{/rb}{rt}psychometry{/rt}一起使用的话，那内容就会有所示意。"
    play voice "voice/圣护院/151100360.ogg"
    shy "想要跨越量子的谜团找到真实时间线下的线索也不是不可能。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100770.ogg"
    qcls "叫花山院过来的目的就是这个吧？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151100370.ogg"
    shy "是啊，毕竟花山院的{rb}接触感应{/rb}{rt}psychometry{/rt}是解析的关键。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151100380.ogg"
    shy "所以我本来是打算让花山院和水之濑一起请假的。"
    play voice "voice/圣护院/151100390.ogg"
    shy "这样的话就不用让她一个人特地赶过来了。"
    show qcls_zf_b1 b1 b1_sp2
    play voice "voice/千川老师/141100780.ogg"
    qcls "可是没有这样做是因为花山院自己坚持要去上学吗？"
    show shy_yjf_b1 b1 b1_ga2
    play voice "voice/圣护院/151100400.ogg"
    shy "嘛就是这样，毕竟花山院自己也还没完全适应研究所的行动方式。"
    play voice "voice/圣护院/151100410.ogg"
    shy "我这边也不好太多干涉她的决定。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141100790.ogg"
    qcls "那么水之濑那边呢？"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151100420.ogg"
    shy "原本打算要是你失败的话，就让水之濑去帮忙的。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100800.ogg"
    qcls "......我就这么不可靠吗？"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151100430.ogg"
    shy "我最放不下心的就是你那过于善良的性格。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100810.ogg"
    qcls "......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100440.ogg"
    shy "不管怎么说，等花山院到了之后我们得迅速把事情完成才行。"
    play voice "voice/圣护院/151100450.ogg"
    shy "要知道解除了{rb}虚无{/rb}{rt}psi-missing{/rt}就相当于暴露了自己。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100820.ogg"
    qcls "到时候立花老师也会赶来的吧。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100460.ogg"
    shy "不过并不会造成多大的影响，即使有碍事之人水之濑那边也会帮忙排除的。"
    play voice "voice/圣护院/151100470.ogg"
    shy "能从她的居合道下逃走的人是不存在的。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151100480.ogg"
    shy "就算实在不小心让碍事之人闯进来了，有你的保护也是无须担心的。"
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/151100490.ogg"
    shy "果然有两个优秀部下的我真是幸运啊。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141100830.ogg"
    qcls "这是......真心话吗？"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151100500.ogg"
    shy "当然。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100840.ogg"
    qcls "主任你的话有时候听起来带些讽刺的味道。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151100510.ogg"
    shy "那只是因为你没有直率地接受而已......果然还是无法让自己喜欢上{rb}灵纹{/rb}{rt}rune{/rt}吗？"
    play voice "voice/千川老师/141100850.ogg"
    qcls "......"
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/151100520.ogg"
    shy "我对你们的称赞无论何时都是发自内心的。"
    play voice "voice/圣护院/151100530.ogg"
    shy "毕竟再怎么说，我对{rb}灵继者{/rb}{rt}elfin{/rt}本身是抱有敬意的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day217.battle_szl_qcls_first:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001100010.ogg"
    xfe "凉君......"
    pause 1.0 hard
    scene set only bridge day xuejian alpha
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100020.ogg"
    xfe "还有......总是勉强着自己的她。"
    play voice "voice/希菲尔/001100030.ogg"
    xfe "她也和凉君一样，是我的伙伴。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001100050.ogg"
    xfe "朋友之间兵刃相向。"
    play voice "voice/希菲尔/001100060.ogg"
    xfe "即使不是真的憎恨对方，但也会引发纷争......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100070.ogg"
    xfe "这一定就是——芬布尔之冬。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play music second_128 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory4
    with slowdissolve
    pause 1.0 hard
    "天使开始歌唱。"
    pause 0.1 hard
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "此刻的这座城市，降下了温柔的雪——"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show szl_dzf_knife_b2_rune b2 b2 b2_n5 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100520.ogg"
    szl "神野君，我姑且先确认一下。"
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100530.ogg"
    szl "还有让你归降的可能性吗？"
    me01 "这一点你自己心里很清楚吧。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dzf_knife_b3_rune
    show szl_dzf_knife_b2_rune b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100540.ogg"
    szl "也许吧，所以我才说是“姑且确认一下”。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf3
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051100550.ogg"
    szl "没有什么能从我的刀下逃跑。"
    play voice "voice/水之濑/051100560.ogg"
    szl "就连你的生命我也能轻易地斩断。"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051100570.ogg"
    szl "即使这样你也不肯放弃吗？"
    me01 "很不巧，固执一直是我最大的缺点。"
    play voice "voice/水之濑/051100580.ogg"
    szl "对你来说，日向爱衣就真的有这么重要吗？"
    me01 "这个问题的答案就让你用败北来体会吧。"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    with dissolve
    play voice "voice/水之濑/051100590.ogg"
    szl "办得到的话就试试看。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0)
    play sound rune2
    scene set only myself_cg three
    with dissolve
    pause 0.5 hard
    me01 "看招！"
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051100600.ogg"
    szl "要我说几次你才会明白？"
    pause 0.1 hard
    scene set only szl_cg fight dzf3
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051100610.ogg"
    szl "没有我的刀斩不断的东西！"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    pause 0.1 hard
    play sound rune2
    pause 1.0 hard
    stop music fadeout 3.0
    scene black
    with slowdissolve
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg bridge3
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        ## 敌方初始化参数
        # Boss为水之濑、千川老师，所有敌方角色技能等级满级，分别装备“传说”秋之韵-素律、雷伤套；天之印-碧落、雷伤套，等级10
        szl_role_mirror.equip_experience = 99999999
        selected_equipments = ["weapon_num11_04", 
                               "armor_num11_04", 
                               "necklace_num11_04", 
                               "ring_num11_04",
                               "magic_light_04",
                               "stone_light_04"]
        for cate in szl_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments and outfit.category == cate)]
            sample_outfit = enemy_outfits[0]
            sample_outfit.init_params()
            for xi in range(9):
                sample_outfit.level_up(szl_role_mirror, 100)
            sample_outfit.enemy_equip_on(szl_role_mirror)
        for xi in range(20):
            szl_role_mirror.skill_levelup()

        qcls_role_mirror.equip_experience = 99999999
        selected_equipments = ["weapon_num1_04", 
                               "armor_num1_04", 
                               "necklace_num1_04", 
                               "ring_num1_04",
                               "magic_light_04",
                               "stone_light_04"]
        for cate in qcls_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments and outfit.category == cate)]
            sample_outfit = enemy_outfits[0]
            sample_outfit.init_params()
            for xi in range(9):
                sample_outfit.level_up(qcls_role_mirror, 100)
            sample_outfit.enemy_equip_on(qcls_role_mirror)
        for xi in range(20):
            qcls_role_mirror.skill_levelup()

        ## 必输剧情-生存战
        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

        local_config.tutorial_step = "生存战"
        
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=szl_role_mirror, 
                boss_hp_plus=999999,
                side_enemy=[], 
                side_hp_plus=0,
                level=32,
                boss_first=True, 
                win_condition='stay', 
                stay_turn=10, 
                inside_label="inside_battle12", 
                mission_type="normal", 
                treasures={
                    "eggs": (3, 0.6),
                    "soul_piece": (5, 0.3),
                    "soul_raise": (5, 0.3),
                    "light_break_small": (5, 0.3),
                    "light_break_large": (3, 0.3)
                })

    if _return == "win":
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day217.after_battle_szl_qcls_first

label day217.after_battle_szl_qcls_first:
    $ flcam.move(0, 0, 0)
    scene set only myself_cg one
    play music second_128 fadein 3.0 if_changed
    with dissolve
    me01 "可恶......"
    "虽然很不甘心，但是我们的实力确实差距太过悬殊了。"
    "无论我怎么发起攻击，水之濑都能轻松化解。"
    "不仅如此，在水之濑的身上还能感觉到一丝来自千川老师的气息。"
    "一定是通过某种暗示事先将她的{rb}灵纹{/rb}{rt}rune{/rt}附着在对方身上。"
    "原本就无比棘手的对手现在更加无懈可击了。"
    show szl_dzf_knife_b3_rune b3 b3 b3_a2 onlayer screens at side_left('szl', 0.15), basicfade
    play voice "voice/水之濑/051100620.ogg"
    szl "没用的！"
    hide szl_dzf_knife_b3_rune
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    me01 "还没完呢！"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051100630.ogg"
    szl "都说了没用的。"
    play sound hite_knife3
    show knife2 onlayer texture
    pause 0.5 hard
    "连续的攻击将我的体力逼至极限。"
    "再这样下去不用水之濑出手我自己就趴下了。"
    "但是......"
    pause 0.1 hard
    play sound rune2
    scene set only myself_cg three
    with dissolve
    me01 "不到最后一刻是无法知道结果的！"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051100640.ogg"
    szl "原来如此。"
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    play sound rune2
    scene set only myself_cg two
    with dissolve
    me01 "难道你不是这么认为的吗？"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051100650.ogg"
    szl "还真是辛苦你了~"
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    play sound rune2
    scene set only sky day xuejian
    show snow_level2 onlayer fg
    with dissolve
    play ambience1 strong_wind
    pause 1.0 hard
    "我尝试复现和立花希交战时使用过的技巧。"
    "利用{rb}念动立场{/rb}{rt}psychokinesis{/rb}制造吹雪企图混淆水之濑的视线。"
    "然后在对方警惕我会从哪个方向攻过来的时候，利用{rb}灵纹{/rb}{rt}rune{/rt}强化自身逃离战场。"
    "即使对方反应过来，那时想要再将我拉回也已经为时已......"
    pause 1.0 hard
    hide snow_level2
    scene set only szl_cg fight dzf3
    with right2left_02
    pause 1.0 hard
    play voice "voice/水之濑/051100660.ogg"
    szl "{rb}幻镜化物{/rb}{rt}apports{/rt}！"
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    with right2left_02
    play sound hite_heavy
    with vpunch
    me01 "什！"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_knife_b2_rune b2 b2 b2_ga1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/水之濑/051100680.ogg"
    szl "不错啊，这次不是背而是脚先着地了。"
    "精心准备的吹雪仅在一瞬间就被斩击瓦解了。"
    "这家伙的刀究竟是什么构造啊？！"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051100690.ogg"
    szl "我说过没用的，谁也无法从我的{rb}幻镜化物{/rb}{rt}apports{/rt}中逃脱。"
    play voice "voice/水之濑/051100700.ogg"
    szl "不管你是强行突破还是迂回。"
    play voice "voice/水之濑/051100710.ogg"
    szl "这一点我也说过很多次了吧。"
    me01 "我说水之濑同学。"
    pause 0.1 hard
    scene set only szl_cg fight dzf4
    with dissolve
    play voice "voice/水之濑/051100740.ogg"
    szl "什么事？"
    me01 "如果你的{rb}灵纹{/rb}{rt}rune{/rt}真如你所说的一样方便，就完全不需要在这里守着我了吧？"
    me01 "特地早我一步来到这条必经之路等候，千方百计也想要把我困在这里。"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051100750.ogg"
    szl "......"
    me01 "想必这并不是你的本意吧。"
    pause 0.1 hard
    scene set only szl_cg fight dzf3
    with dissolve
    play voice "voice/水之濑/051100760.ogg"
    szl "即使我现在将你传送走，也无法保证你不会通过其他途径前往研究所。"
    play voice "voice/水之濑/051100770.ogg"
    szl "我只是担心这种情况发生而已。"
    me01 "不是不想，而是你做不到吧。"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051100780.ogg"
    szl "......"
    me01 "之前就在想，并不是{rb}幻镜化物{/rb}{rt}apports{/rt}本身是多么厉害的{rb}灵纹{/rb}{rt}rune{/rt}。"
    me01 "而是像这样的{rb}灵纹{/rb}{rt}rune{/rt}到了水之濑你的手上才变得如此棘手。"
    play voice "voice/水之濑/051100800.ogg"
    szl "......所以你想说什么？"
    me01 "如果我没猜错的话，{rb}幻镜化物{/rb}{rt}apports{/rt}并不是能够随意操控物体的{rb}灵纹{/rb}{rt}rune{/rt}。"
    me01 "先前说什么能轻易把我拉回来也是你的障眼法而已。"
    pause 0.1 hard
    scene set only szl_cg fight dzf3
    with dissolve
    play voice "voice/水之濑/051100810.ogg"
    szl "......我还以为你要说什么。"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051100820.ogg"
    szl "现在的你还站在我眼前，还有什么比这个更具有说服力的吗？"
    play voice "voice/水之濑/051100830.ogg"
    szl "更何况你已经两次被我丢在这河滩上了。"
    me01 "你说的没错。"
    me01 "但是能做到这一切的不是{rb}幻镜化物{/rb}{rt}apports{/rt}本身，而是你手中的那把太刀。"
    pause 0.1 hard
    scene set only szl_cg fight dzf4
    with dissolve
    play voice "voice/水之濑/051100840.ogg"
    szl "......"
    me01 "换句话说，不是你将我送回这里的，而是你手中的刀将我拉回来的。"
    me01 "{rb}幻镜化物{/rb}{rt}apports{/rt}的作用就像磁铁的引力一样。"
    me01 "实现物体之间的相互引、斥。"
    me01 "水之濑之所以能将太刀召唤到你的手中，是因为刀的质量远小于你本身。所以才能在几乎不被牵引的状态下握住太刀。"
    me01 "很可惜，与我相比不管是水之濑同学还是你手中的太刀都无法在保持自身不动的状态下将我牵引。"
    me01 "相反要是轻易发动的话还会反过来被我所牵制。"
    me01 "至于你能像刚才那样将我拉回来，恐怕就是身为居合道剑士的水之濑同学你自己的本事了吧。"
    play voice "voice/水之濑/051100850.ogg"
    szl "......"
    me01 "与空气相比，太刀的质量则要大得多。"
    me01 "通过高速的斩击便可以轻松地将太刀周围的空气吸附在刀身上，从而以你周身为中心制造出短暂的真空领域。"
    me01 "而我就是被这样的气压差给拉回来的。"
    me01 "我说的没错吧？"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/水之濑/051100870.ogg"
    szl "没想到神野君你还挺聪明的嘛~"
    me01 "别看我这样，从刚才开始我的视线可是一刻也没离开过水之濑同学你。"
    pause 0.1 hard
    scene set only szl_cg fight dzf3
    with dissolve
    play voice "voice/水之濑/051100890.ogg"
    szl "就算你能明白{rb}幻镜化物{/rb}{rt}apports{/rt}的原理，也是没有胜算的。"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    with dissolve
    play voice "voice/水之濑/051100900.ogg"
    szl "现状丝毫不会有所改变。"
    "的确，就算明白了敌人的招式原理，想要打破这悬殊的实力差距还是有些困难。"
    stop music fadeout 5.0
    pause 1.0 hard

label day217.battle_szl_qcls_second:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    show snow_level1 onlayer fg
    with dissolve
    play sound rune3
    pause 3.0 hard
    play voice "voice/立花希/031101200.ogg"
    stranger "凉君——"
    play music second_145 fadein 3.0 if_changed
    show lhx_dsf_b3_rune b3 b3 b3_n2 onlayer screens at side_left('lhx', xzoom=1), basicfade
    play voice "voice/立花希/031101210.ogg"
    lhx "抱歉，让你久等了~"
    hide lhx_dsf_b3_rune
    "是立花老师。"
    "曾经最棘手的对手，此刻已然成为了最可靠的同伴。"
    "这也许就是命运的安排吧。"
    pause 1.0 hard
    $ flcam.move(0, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 5.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only fight_cg rune1
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show lhx_dsf_b3_rune b3 b3 b3_n1 onlayer m2:
        xpos 0.5 alpha 0.5
    me01 "你的身体没问题吗？"
    play voice "voice/立花希/031101230.ogg"
    lhx "这一点无需担心，比起这个还请先说明一下现在的情况。"
    me01 "爱衣正被千川老师带往研究所，而我在赶往的途中被水之濑凛给拦住了。"
    show lhx_dsf_b3_rune b3 b3 b3_s2
    play voice "voice/立花希/031101240.ogg"
    lhx "原来如此。"
    me01 "光靠我自己是无法战胜水之濑的，立花老师有什么办法吗？"
    show lhx_dsf_b3_rune b3 b3 b3_s1
    play voice "voice/立花希/031101250.ogg"
    lhx "能破解水之濑凛{rb}灵纹{/rb}{rt}rune{/rt}的方法吗......"
    hide lhx_dsf_b3_rune
    show lhx_dsf_b2_rune b2 b2 b2_s4 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101260.ogg"
    lhx "我现在脑袋还昏沉沉的，所以请别抱太大的期待。"
    me01 "就算这样还是拜托了。"
    show lhx_dsf_b2_rune b2 b2 b2_sp1
    play voice "voice/立花希/031101270.ogg"
    lhx "你们现在在什么地方？"
    me01 "新旧城区交界处的大桥下。"
    show lhx_dsf_b2_rune b2 b2 b2_s2
    play voice "voice/立花希/031101280.ogg"
    lhx "我刚才试图通过{rb}远隔透视{/rb}{rt}clairvoyance{/rt}观察战局，但却无法锁定水之濑凛的位置。"
    show lhx_dsf_b2_rune b2 b2 b2_s1
    play voice "voice/立花希/031101290.ogg"
    lhx "要使用{rb}思维透视{/rb}{rt}telepathy{/rt}的话，现在的距离也已经超出极限了。"
    me01 "也就是说立花老师你现在是在很远的地方和我对话吗？"
    show lhx_dsf_b2_rune b2 b2 b2_n2
    play voice "voice/立花希/031101300.ogg"
    lhx "是的，我在幼儿园的保健室，需要我立刻赶过去吗？"
    me01 "不必勉强，立花老师只需要作为我的军师支援我就行了。"
    me01 "战斗的事情我会想办法解决的。"
    show lhx_dsf_b2_rune b2 b2 b2_s3
    play voice "voice/立花希/031101310.ogg"
    lhx "抱歉了。"
    show lhx_dsf_b2_rune b2 b2 b2_a1
    play voice "voice/立花希/031101320.ogg"
    lhx "既然爱衣是被带往研究所，那水之濑的出现就意味着她是负责断后的吧？"
    me01 "是啊，这一点水之濑本人也承认了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_knife_b3_rune b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100920.ogg"
    szl "怎么突然安静了下来，难不成你是在和谁商量对策吗？"
    "对方似乎还没有发现立花老师。"
    "也就是说是只有我才能听到的声音。"
    hide szl_dzf_knife_b3_rune
    show szl_dzf_knife_b2_rune b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100930.ogg"
    szl "能察觉到念波的存在，是{rb}思维透视{/rb}{rt}telepathy{/rt}和{rb}远隔透视{/rb}{rt}clairvoyance{/rt}吧？"
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100960.ogg"
    szl "不过我是不会妨碍你们的。"
    show szl_dzf_knife_b3_rune b3 b3 b3_a1
    play voice "voice/水之濑/051100970.ogg"
    szl "不管你们怎么打算也只是浪费时间而已。"
    me01 "你这flag立得倒是挺到位的......"
    me01 "不过我还是接受你的好意了。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only fight_cg rune1
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_sp1 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101340.ogg"
    lhx "凉君，用你的{rb}念动立场{/rb}{rt}psychokinesis{/rt}强行突破也不行吗？"
    me01 "虽然尝试过几次，但总是能被对方的{rb}幻镜化物{/rb}{rt}apports{/rt}拉回原地。"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_n3 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101360.ogg"
    lhx "也就是说需要应付的{rb}灵纹{/rb}{rt}rune{/rt}只有一种，还真是谢天谢地。"
    me01 "作为挨打一方的我来说简直糟糕透了！"
    show lhx_dsf_b3_rune b3 b3 b3_n2
    play voice "voice/立花希/031101370.ogg"
    lhx "我认为水之濑凛的{rb}幻镜化物{/rb}{rt}apports{/rt}是受到某种限制的。"
    me01 "啊，这一点我也看出来了。"
    show lhx_dsf_b3_rune b3 b3 b3_s1
    play voice "voice/立花希/031101380.ogg"
    lhx "制造真空然后利用气压把人拉回原地吗。"
    me01 "能读取思维真是方便啊......"
    show lhx_dsf_b3_rune b3 b3 b3_n2
    play voice "voice/立花希/031101390.ogg"
    lhx "如果不是逃跑，而是反过来用你的{rb}念动立场{/rb}{rt}psychokinesis{/rt}发动攻击呢？"
    me01 "同样行不通，她的太刀能够轻易斩断我的念波。"
    show lhx_dsf_b3_rune b3 b3 b3_s2
    play voice "voice/立花希/031101400.ogg"
    lhx "也就是说，任何接触到太刀的物质或者能量都会被她的{rb}幻镜化物{/rb}{rt}apports{/rt}瞬间瓦解的意思吗......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf1
    show sepiagrain onlayer texture
    with slowdissolve
    pause 1.0 hard
    show lhx_dsf_b1_rune b1 b1 b1_a1 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031101420.ogg"
    lhx "从你脑海中她的架势来看，对方是个很擅长居合道的人。"
    play voice "voice/立花希/031101430.ogg"
    lhx "能够以高速斩击将眼前的物体一分为二。而且不仅是表面看上去那么简单，就连无实体的物质也能够斩断吗......"
    hide lhx_dsf_b1_rune
    pause 1.0 hard
    scene set only fight_cg rune1
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_n2 onlayer m2:
        xpos 0.5 alpha 0.5
    me01 "别光顾着夸赞对方了，有没有什么办法能够对付她的吗？"
    play voice "voice/立花希/031101440.ogg"
    lhx "如果是这样的话对策自然也变得简单多了，换句话说只要从她那里把刀抢过来就行了。"
    me01 "这个对我来说有点困难啊......"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_n2 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101460.ogg"
    lhx "话虽如此我并不是让你冒然接近对方，说不定真的会受伤也说不定。"
    me01 "那样的斩击会死人的吧喂！"
    show lhx_dsf_b3_rune b3 b3 b3_n4
    play voice "voice/立花希/031101470.ogg"
    lhx "考虑到对方连空气都能斩断，凉君的身体肯定会毫无疑问地被一分为二吧。"
    me01 "别说的事不关己啊。"
    hide lhx_dsf_b3_rune
    show lhx_dsf_b2_rune b2 b2 b2_s4 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101490.ogg"
    lhx "虽然我也可以使用念波干扰对方......但是考虑到居合斩的速度，我不认为这一招能够奏效。"
    me01 "念波......干扰？"
    me01 "就是这个！"
    show lhx_dsf_b2_rune b2 b2 b2_s3
    play voice "voice/立花希/031101510.ogg"
    lhx "我就知道凉君会这么想。"
    me01 "那么就开始吧。"
    me01 "让她尝尝我们的厉害。"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_n2 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101520.ogg"
    lhx "请等一下，还有一点是我担心的。"
    me01 "什么？"
    show lhx_dsf_b3_rune b3 b3 b3_a1
    play voice "voice/立花希/031101530.ogg"
    lhx "即使能够顺利从她手里抢到太刀，说不定对方还是能够通过{rb}灵纹{/rb}{rt}rune{/rt}召唤回去。"
    show lhx_dsf_b3_rune b3 b3 b3_s2
    play voice "voice/立花希/031101570.ogg"
    lhx "毕竟现在面对的是极其危险的......且尤为罕见的{rb}灵纹{/rb}{rt}rune{/rt}。"
    me01 "这一点不用担心，我自有我的打算。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show szl_dzf_knife_b2_rune b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051100980.ogg"
    szl "还在讨论中吗，我都犯困了。"
    me01 "已经结束了，这场战斗。"
    show szl_dzf_knife_b2_rune b2 b2 b2_s1
    play voice "voice/水之濑/051100990.ogg"
    szl "是吗......"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf2
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051101000.ogg"
    szl "那么接下来希望如你所说，能让我看到一些有趣的东西。"
    show lhx_dsf_b1_rune b1 b1 b1_n2 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031101580.ogg"
    lhx "千万别勉强，还不到需要赌上性命的时候。"
    show lhx_dsf_b1_rune b1 b1 b1_a1
    play voice "voice/立花希/031101590.ogg"
    lhx "虽然爱衣的事情也很重要，但是还请优先考虑自己的安危。"
    hide lhx_dsf_b1_rune
    me01 "多谢关心！"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    stop ambience1 fadeout 3.0
    stop music fadeout 5.0
    pause 0.1 hard
    hide snow_level1
    scene white
    with slowerdissolve
    play sound rune2
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg bridge3
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        ## 敌方初始化参数
        # Boss为水之濑凛、千川老师，巫女个数4，所有敌方角色技能等级满级，巫女装备稀有随机等级8装备6件；水之濑装备为史诗6件秋之韵-素律、雷伤套；千川老师装备为史诗6件天之印-碧落、雷伤套
        selected_equipments_szl = ["weapon_num11_03", 
                                   "armor_num11_03", 
                                   "necklace_num11_03", 
                                   "ring_num11_03",
                                   "magic_light_03",
                                   "stone_light_03"]
        selected_equipments_qcls = ["weapon_num1_03", 
                                    "armor_num1_03", 
                                    "necklace_num1_03", 
                                    "ring_num1_03",
                                    "magic_light_03",
                                    "stone_light_03"]
        enemy_roles = [szl_role_mirror, qcls_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3]
        for role in enemy_roles:
            role.equip_experience = 99999999
            for cate in role.outfits:
                if role.name == "水之濑凛":
                    enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments_szl and outfit.category == cate)]
                    sample_outfit = enemy_outfits[0]
                elif role.name == "千川老师":
                    enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments_qcls and outfit.category == cate)]
                    sample_outfit = enemy_outfits[0]
                else:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                sample_outfit.init_params()
                for xi in range(7):
                    sample_outfit.level_up(role, 100)
                sample_outfit.enemy_equip_on(role)

            for xi in range(20):
                role.skill_levelup()

        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

        local_config.tutorial_step = "shield_buff_217"

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=szl_role_mirror, 
                boss_hp_plus=30000,
                side_enemy=[qcls_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3], 
                side_hp_plus=10000,
                level=30,
                boss_first=True,
                win_condition='normal',
                stay_turn=0,
                inside_label="inside_battle13", 
                mission_type="normal", 
                treasures={
                    "eggs": (5, 0.6),
                    "mana_eggs": (2, 0.3),
                    "soul_piece": (8, 0.3),
                    "soul_raise": (8, 0.3),
                    "light_break_small": (7, 0.3),
                    "light_break_large": (4, 0.3)
                })

    if _return == "win":
        "战斗胜利！"
        python:
            if "qcls_role" not in local_config.role_pool:
                local_config.role_pool.add("qcls_role")
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day217.after_battle_szl_qcls_second

label day217.after_battle_szl_qcls_second:
    $ flcam.move(0, 0, 0)
    scene black
    with dissolve
    pause 1.0 hard
    scene set only myself_cg one
    play music second_145 fadein 3.0 if_changed
    with dissolve
    "我发动{rb}念动立场{/rb}{rt}psychokinesis{/rt}卷起尘土遮盖视线。"
    "沙石夹杂着积雪铺天盖地地蔓延开来。"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051101010.ogg"
    szl "这就是你的对策吗？反正也不会有什么帮助的。"
    pause 0.1 hard
    scene set only myself_cg two
    with dissolve
    me01 "好戏还在后头呢。"
    play sound rune2
    play ambience1 strong_wind fadein 3.0
    $ flcam.move(1100, -300, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "我加大了灵力的强度，风暴越来越猛烈。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf4
    with dissolve
    play voice "voice/水之濑/051101020.ogg"
    szl "障眼法？还真是喜欢耍些小聪明......"
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 2.0 hard
    "风暴覆盖了战场，我们彼此的身影也从对方的视线中消失了。"
    "接下来就是最关键的时刻。"
    "必须在对方斩断风暴之前尽可能地接近她。"
    "有了立花老师的帮助我能够很方便地掌握对方现在的方位。"
    "我有预感这次一定会成功，以我对水之濑凛的了解。"
    "在她的眼里，此刻的我是绝对不会堂堂正正地从正面发动进攻的。"
    pause 1.0 hard
    scene set only szl_cg fight dzf3
    with dissolve
    play voice "voice/水之濑/051101030.ogg"
    szl "白费力气，反正你一定又打算趁机逃跑吧。"
    play voice "voice/水之濑/051101040.ogg"
    szl "是时候放弃这种想法了！"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051101050.ogg"
    szl "我的刀不只是光......就连黑暗也能斩断！"
    stop ambience1 fadeout 5.0
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    "一道明亮的斩击划破天际。"
    "就像是水面驶过船只溅起的波纹一般，空间被硬生生地划开了一道口子。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    play sound water1
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky fight xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    play ambience1 water2 fadein 3.0
    pause 1.0 hard
    "随着斩击的落下，洪水般的巨浪席卷而来。"
    "来不及闪避的水之濑浑身上下都被淋湿了。"
    "这也是我的计划之一。"
    "无论多么精湛的剑技，也无法悉数斩尽像水这样流体物质。"
    "面对无比柔弱的水，即便是拥有高超剑技的水之濑也将束手无策。"
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowdissolve
    pause 1.0 hard
    scene set only bridge fight under xuejian
    show snow_level1
    show screen investigation_popup(investigation.hint_szl)
    show szl_dzf_knife_b2_rune b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu szl_dzf_knife_b2_rune onlayer m2:
            camera_pos (scale(2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction right

label day217.examine_bottle:
    hide screen investigation_popup
    window mode thought
    me01 "琉璃临走前留下来的饮料瓶。"
    window mode thought
    me01 "里面还有残余的饮料。"
    window mode thought
    me01 "总觉得还有什么利用价值......"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    jump investigate

label day217.use_bottle:
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    hide screen investigation_popup
    stop ambience1 fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 5.0 hard
    hide snow_level1
    with slowdissolve
    pause 1.0 hard
    "几乎就在水花击中水之濑的那一刻，我飞身上前夺过了她手中的太刀。"
    pause 0.5 hard
    play sound rune1
    scene set only fight_cg rune1
    play music second_127 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1_rune b1 b1 b1_a2 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101670.ogg"
    lhx "凉君，快退后！"
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf3
    with dissolve
    "水之濑闭着眼睛。"
    "听不到她的呼吸声，就这样站在原地一动不动。"
    "不知何时我手中的太刀已经又回到了她的手中。"
    show lhx_dsf_b1_rune b1 b1 b1_s2 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031101690.ogg"
    lhx "凉君，快用{rb}念动立场{/rb}{rt}psychokinesis{/rt}，不要大意！"
    hide lhx_dsf_b1_rune
    pause 0.1 hard
    play sound rune2
    scene set only myself_cg one
    with dissolve
    "顾不上多想，我按立花老师的指示发动了{rb}灵纹{/rb}{rt}rune{/rt}。"
    pause 0.5 hard
    play sound hite_knife3
    show knife2 onlayer texture
    pause 0.5 hard
    with vpunch
    "飞来的斩击被{rb}念动立场{/rb}{rt}psychokinesis{/rt}产生的屏障挡住了。"
    me01 "好险，差一点就完蛋了。"
    pause 1.0 hard
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "站稳之后，我的视线再一次锁定在水之濑身上。"
    "此时的她正捂着手腕。"
    "不知道是因为生气还是寒冷的缘故，她的身子抖得厉害。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_knife_b2_rune b2 b2 b2_a2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101060.ogg"
    szl "......真亏你能干出这种事来！"
    me01 "刚刚的攻击，水之濑同学你没有受伤吧？"
    show szl_dzf_knife_b2_rune b2 b2 b2_s4
    play voice "voice/水之濑/051101110.ogg"
    szl "这点小伤不算什么。"
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101120.ogg"
    szl "比起这个，刚刚的水让我全身都湿透了。"
    me01 "......抱歉。"
    hide szl_dzf_knife_b3_rune
    show szl_dzf_knife_b2_rune b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101130.ogg"
    szl "你该不会是特地为了关心我，才选择继续站在那里的吧？"
    me01 "只要水之濑你不肯放弃，就算我想逃也是逃不掉的吧。"
    me01 "现在的情况不如赶紧去换件衣服然后包扎一下伤口如何？"
    show szl_dzf_knife_b2_rune b2 b2 b2_s1
    play voice "voice/水之濑/051101140.ogg"
    szl "......也是呢。"
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101150.ogg"
    szl "不过这得等到工作结束了以后。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show jingya onlayer texture:
        xpos 0.0
    show szl_dzf_knife_b3_rune b3 b3 b3_a2
    play voice "voice/水之濑/051101160.ogg"
    szl "{rb}幻镜化物{/rb}{rt}apports{/rt}！"
    play sound rune3
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play voice "voice/水之濑/051101170.ogg"
    szl "神野君，就算你夺走了我的太刀也没用。"
    pause 0.5 hard
    play music second_161 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051101180.ogg"
    szl "到头来你还是无法逃出我的手掌心。"
    play voice "voice/水之濑/051101190.ogg"
    szl "如果你逃跑的话，我就斩断空气把你拉回来。"
    pause 1.0 hard
    scene set only fight_cg rune1
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_n2 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101760.ogg"
    lhx "水之濑凛的{rb}幻镜化物{/rb}{rt}apports{/rt}只有对那把刀才可以无视相互作用的原理进行召唤。"
    play voice "voice/立花希/031101770.ogg"
    lhx "而除此之外的其他物体却都只是透过太刀本身来接触，总算找到{rb}灵纹{/rb}{rt}rune{/rt}的源头了。"
    me01 "也就是说，对于无法挥舞太刀的水之濑而言，{rb}幻镜化物{/rb}{rt}apports{/rt}也就成了摆设而已。"
    me01 "到时候想要牵制我也是不可能的了。"
    play sound rune2
    $ flcam.move(2250, 0, 750, duration=1.5)
    show szl_dzf_knife_b1_rune b1 b1 b1_a1 onlayer m2:
        xpos 0.7 alpha 0.5
    play voice "voice/水之濑/051101210.ogg"
    szl "原来你就是那位优秀的参谋啊......不过即使被你们发现了真相也不过只是回到了原点。"
    show lhx_dsf_b2_rune b2 b2 b2_a1
    play voice "voice/立花希/031101790.ogg"
    lhx "凉君，她的手腕受伤了，这样的话挥刀是会受到影响的。"
    play voice "voice/立花希/031101800.ogg"
    lhx "现在的话就可以顺利逃跑也说不定。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf2
    with dissolve
    play voice "voice/水之濑/051101230.ogg"
    szl "你这么认为的话大可以试试看！"
    pause 0.1 hard
    scene set only szl_cg fight dzf4
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051101240.ogg"
    szl "！？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_knife_b3 b3 b3 b3_ga3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051101250.ogg"
    szl "这是......什么啊？！"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show szl_dzf_knife_b3 b3 b3_s2
    play voice "voice/水之濑/051101260.ogg"
    szl "怎么觉得刀身黏糊糊的。"
    me01 "不应该是滑溜溜的吗？"
    show szl_dzf_knife_b3 b3 b3_ga1
    play voice "voice/水之濑/051101270.ogg"
    szl "......你对我的刀做了什么？"
    me01 "这个嘛，我试着浇上了这个。"
    hide szl_dzf_knife_b3
    $ flcam.move(0, -100, 400, duration=1.5, warper='ease_cubic')
    pause 1.0 hard
    show bottle onlayer b2_c2u:
        xpos 0.0
    "我拿出了装着饮料的罐子。"
    hide bottle
    pause 0.5 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_knife_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101280.ogg"
    szl "那是花山院的丢掉的......"
    me01 "是啊，似乎是今年的最新款。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only fight_cg rune1
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_n1 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031101830.ogg"
    lhx "虽然不清楚璃之助的果汁是什么成分。"
    play voice "voice/立花希/031101820.ogg"
    lhx "但是饮料一般都是滑溜溜的呢~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show szl_dzf_knife_b1 b1 b1_s2 onlayer m2:
        xpos 0.7 alpha 0.5
    play voice "voice/水之濑/051101290.ogg"
    szl "与其说是滑，不如说更加地粘稠......"
    show lhx_dsf_b2_rune b2 b2 b2_n3
    play voice "voice/立花希/031101840.ogg"
    lhx "不管怎么样，现在的你就更加无法自由挥刀了。"
    show lhx_dsf_b2_rune b2 b2 b2_h2
    play voice "voice/立花希/031101850.ogg"
    lhx "这样一来凉君就可以悠哉地去研究所了~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_knife_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101300.ogg"
    szl "归根到底......你还是打算逃跑吗？"
    show szl_dzf_knife_b2 b2 b2_n3
    play voice "voice/水之濑/051101310.ogg"
    szl "从我这里夺走太刀也是为了这个。"
    show szl_dzf_knife_b2 b2 b2_a2
    play voice "voice/水之濑/051101320.ogg"
    szl "真是接二连三地惹我生气......"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051101330.ogg"
    szl "事后清洗起来很麻烦的，你要怎么赔我啊！"
    me01 "还不肯放弃吗？"
    play voice "voice/水之濑/051101340.ogg"
    szl "谁知道呢，你要试试看吗？"
    play voice "voice/水之濑/051101350.ogg"
    szl "是你逃跑的速度——{rb}念动立场{/rb}{rt}psychokinesis{/rt}快，还是我的{rb}幻镜化物{/rb}{rt}apports{/rt}快，要试试看吗？"
    play voice "voice/水之濑/051101360.ogg"
    szl "要是我失败的话，你就能顺利逃跑。"
    play voice "voice/水之濑/051101370.ogg"
    szl "但如果你失败了，就不要再妄想离开这里了。"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    with dissolve
    play voice "voice/水之濑/051101380.ogg"
    szl "反正你是认为我不会直接对你挥刀才没把我放在眼里吧。"
    play voice "voice/水之濑/051101390.ogg"
    szl "虽然确实是这样没错。"
    pause 0.1 hard
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/水之濑/051101400.ogg"
    szl "但用刀背把你打晕的程度对我来说还是轻而易举的！"
    me01 "别说些可怕的话啊。"
    me01 "即使是刀背也很疼的。"
    "已经不知道是第几次，我再次发动了{rb}念动立场{/rb}{rt}psychokinesis{/rt}。"
    pause 0.1 hard
    play sound rune3
    scene set only myself_cg three
    $ flcam.move(-1100, -1400, 450, duration=1.5)
    pause 1.0 hard
    with dissolve
    show wflash onlayer texture
    me01 "这是最后的一击！"
    scene white 
    with in2out_02_l
    pause 1.0 hard
    show szl_dzf_knife_b3_rune b3 b3 b3_n3 onlayer screens at side_left('szl', 0.15), basicfade
    play voice "voice/水之濑/051101420.ogg"
    szl "原来如此，这次的攻击不是利用沙石，而是只有吹雪吗。"
    show szl_dzf_knife_b3_rune b3 b3 b3_ga1
    play voice "voice/水之濑/051101430.ogg"
    szl "本来就够冷了，真是讨厌啊。"
    play voice "voice/水之濑/051101440.ogg"
    szl "要是这样感冒的话，再怎么说我也会恨你的！"
    hide szl_dzf_knife_b3_rune
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf3
    with dissolve
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    "斩击在空中划过一道明亮的轨迹。"
    "即使负伤加上刀身被我做了手脚，斩击的威力却丝毫没有减弱。"
    pause 1.0 hard
    scene white
    with slowdissolve
    pause 1.0 hard
    "可恶......还是没有办法吗。"
    "就算有立花老师的帮忙，结果还是一样的吗？"
    "屏障再一次被斩击轻松切断了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_knife_b1_rune b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101450.ogg"
    szl "骗人的吧......"
    play music second_154 fadein 3.0 if_changed
    hide szl_dzf_knife_b1_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101460.ogg"
    szl "为、为什么？！"
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    "水之濑发现了异样。"
    "明明一击便能够斩断空间的太刀。"
    "此时无论如何也无法劈开眼前的吹雪。"
    show szl_dzf_knife_b3_rune b3 b3 b3_a2 at flu_down(0.35, 20):
        xpos 0.5
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    play sound hite_knife3
    show knife2 onlayer texture
    pause 0.5 hard
    play sound hite_knife3
    show knife3 onlayer texture
    pause 0.5 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene white
    with slowdissolve
    pause 1.0 hard
    show szl_dzf_knife_b3_rune b3 b3 b3_sp1 onlayer screens at side_left('szl', 0.15), basicfade
    play voice "voice/水之濑/051101470.ogg"
    szl "这雪......难道是？"
    play voice "voice/水之濑/051101480.ogg"
    szl "它的真面目究竟——"
    hide szl_dzf_knife_b3_rune
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    scene set only bridge day under xuejian
    with slowdissolve
    pause 1.0 hard
    "片刻的平静之后，周围的一切仿佛都都恢复了正常。"
    "灵力的屏障解除了，从刚才为止一直持续的飘雪也停止了。"
    "仿佛一切都没有发生过一样。"
    play sound touch
    $ flcam.move(0, 500, 1100, duration=1.5, warper='ease_cubic')
    play music second_124 fadein 3.0 if_changed
    pause 1.0 hard
    me01 "水之濑同学？"
    "水之濑瘫软在地。"
    "我上前扶住了她。"
    "也许是疲劳过度昏过去了。"
    me01 "刚才到底......发生了什么？"
    "本以为会是以我的失败告终的。"
    "可没想到水之濑自己先倒下了。"
    me01 "要是感冒的话，之后随你怎么责怪我都行。"
    me01 "但是现在抱歉了......"
    "我将外套披在了水之濑的身上，然后拨通了翔子的电话。"
    "安排好水之濑的善后工作，我动身朝研究所的方向赶去。"
    pause 1.0 hard
    scene set only bridge day xuejian
    with dissolve
    pause 1.0 hard
    play sound rune3
    scene set only fight_cg rune1
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_s4 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031102210.ogg"
    lhx "凉君......能问你个问题吗？"
    me01 "什么？"
    show lhx_dsf_b2_rune b2 b2 b2_s2
    play voice "voice/立花希/031102220.ogg"
    lhx "凉君你最后是用了什么方法才......"
    play voice "voice/立花希/031102230.ogg"
    lhx "是用{rb}念动立场{/rb}{rt}psychokinesis{/rt}打败了水之濑，还是说......"
    me01 "怎么样都无所谓了吧，事情都已经结束了。"
    show lhx_dsf_b2_rune b2 b2 b2_s3
    play voice "voice/立花希/031102240.ogg"
    lhx "......"
    me01 "立花老师，你没事吧？"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_n2 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031102250.ogg"
    lhx "那还用说吗，我现在就去和你汇合。"
    me01 "真的没问题吗？"
    show lhx_dsf_b3_rune b3 b3 b3_h1
    play voice "voice/立花希/031102260.ogg"
    lhx "别小看我了，{rb}催眠{/rb}{rt}hypno{/rt}的效果早就消失了。"
    show lhx_dsf_b3_rune b3 b3 b3_n1
    play voice "voice/立花希/031102270.ogg"
    lhx "而且我说过，无论何时我都会追上凉君你的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day217_bridge_event01:
        $ seen_day217_bridge_event01 = True
    $ _overworld_label = 'day217.bridge_event01'
    jump day217.map

label day217.laboratory_event02:
    $ flcam.move(0, 0, 0)
    scene set only laboratory day outside xuejian
    with slowdissolve
    pause 2.0 hard
    scene set only laboratory inside3 xuejian alpha
    with dissolve
    play music second_123 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_n4 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/041100400.ogg"
    liuli "我来了，圣护院主任。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151100540.ogg"
    shy "来了吗，真慢啊。"
    play voice "voice/琉璃/041100410.ogg"
    liuli "非常抱歉。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100550.ogg"
    shy "水之濑怎么没来？"
    hide liuli_dzf_b2
    show liuli_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041100420.ogg"
    liuli "在和神野凉接触之后我就不知道了。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151100560.ogg"
    shy "是吗，果然被他察觉到了吗......"
    hide liuli_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151100590.ogg"
    shy "虽然之前就料到了身为爱衣家人的他一定会冒着风险来研究所询问真相。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141100860.ogg"
    qcls "......"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100600.ogg"
    shy "神野凉与大和教授都开始调查{rb}灵纹{/rb}{rt}rune{/rt}的事情了，虽然其中的理由各不相同。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151100610.ogg"
    shy "这座城市的异常气候，大和教授那边也是知道的，可以说是有其父必有其子吧......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100620.ogg"
    shy "看来他似乎也并不想让自己的家人牵扯上{rb}灵纹{/rb}{rt}rune{/rt}这种东西。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141100870.ogg"
    qcls "......"
    hide qcls_zf_b1
    $ flcam.move(2250, 0, 900, duration=1.5)
    show liuli_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151100650.ogg"
    shy "赶紧推进计划吧。花山院，情况怎么样了？"
    play voice "voice/琉璃/041100430.ogg"
    liuli "没有问题，一切指令都顺利执行。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100660.ogg"
    shy "那么解析工作就交给你了，对象就是实验台上的她——日向爱衣所掌握的{rb}预知未来{/rb}{rt}precognition{/rt}。"
    hide liuli_dzf_b1
    show liuli_dzf_b2 b2 b2_n4 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041100440.ogg"
    liuli "我知道了。"
    hide liuli_dzf_b2
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100880.ogg"
    qcls "花山院同学......怎么感觉给人的感觉和平时不一样了？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151100670.ogg"
    shy "应该是是水之濑激活了“限制”吧......没时间了，之后再和你解释吧。"
    show qcls_zf_b1 b1 b1_n4
    play voice "voice/千川老师/141100890.ogg"
    qcls "那我现在就解除{rb}虚无{/rb}{rt}psi-missing{/rt}。"
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide qcls_zf_b1
    play sound rune3
    show qcls_zf_b1_rune b1 b1 b1_s3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    pause 3.0 hard
    show qcls_zf_b1_rune b1 b1 b1_h3
    play voice "voice/千川老师/141100900.ogg"
    qcls "爱衣......醒醒，爱衣~"
    show aiyi_dzf_b1 b1 b1_n2 onlayer screens at side_left('aiyi'), basicfade
    play voice "voice/爱衣/111102690.ogg"
    aiyi "嗯、嗯......"
    hide aiyi_dzf_b1
    $ flcam.move(-2250, 0, 750, duration=1.5)
    play sound touch
    show aiyi_dzf_b1 b1 b1_s4 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 1.04
        parallel:
            linear 1.0 ypos 1.0
        parallel:
            linear 1.0 alpha 1.0
    pause 0.5 hard
    hide qcls_zf_b1_rune
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141100910.ogg"
    qcls "下午好爱衣。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111102700.ogg"
    aiyi "......千川老师？"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141100920.ogg"
    qcls "抱歉，占用你的休息时间。"
    play voice "voice/爱衣/111102710.ogg"
    aiyi "休息？"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141100930.ogg"
    qcls "是啊，爱衣你在去医院的途中睡着了。"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s3
    play voice "voice/爱衣/111102720.ogg"
    aiyi "这里是......医院？"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141100940.ogg"
    qcls "是啊。"
    play voice "voice/千川老师/141100950.ogg"
    qcls "检查已经结束了，只是疲劳过度而已没什么大问题。"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141100960.ogg"
    qcls "好好休息的话就没事了。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102730.ogg"
    aiyi "原来如此......抱歉老师，给您添麻烦了。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141100970.ogg"
    qcls "完全没有，不用在意的。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111102740.ogg"
    aiyi "老师，接下来要回幼儿园吗？"
    show qcls_zf_b1 b1 b1_h3
    play voice "voice/千川老师/141100980.ogg"
    qcls "今天就先回家休息吧，等下我会联系青木同学的。"
    hide qcls_zf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111102750.ogg"
    aiyi "让大姐姐她担心了吗？"
    hide aiyi_dzf_b1
    $ flcam.move(2800, 0, 750, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1 onlayer m1:
        xpos 0.6
    show liuli_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.8
    pause 1.0 hard
    $ flcam.move(2250, 0, 600, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer f2:
        xpos 0.5
    play voice "voice/爱衣/111102760.ogg"
    aiyi "......后面的那些人是？"
    hide shy_yjf_b1
    hide liuli_dzf_b1
    $ flcam.move(-2250, 0, 400, duration=1.5)
    show qcls_zf_b1 b1 b1_h2 onlayer f1:
        xpos 0.3
    play voice "voice/千川老师/141100990.ogg"
    qcls "她是这里的医生哟~"
    play voice "voice/爱衣/111102770.ogg"
    aiyi "......是这样吗？"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141101000.ogg"
    qcls "比起这个爱衣，我们有一个请求。"
    play voice "voice/爱衣/111102780.ogg"
    aiyi "什么？"
    show qcls_zf_b1 b1 b1_n2
    play voice "voice/千川老师/141101010.ogg"
    qcls "能不能帮我们预知一下呢？"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111102790.ogg"
    aiyi "？"
    hide aiyi_dzf_b1
    hide qcls_zf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    play sound rune3
    show qcls_zf_b1_rune b1 b1 b1_s3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千川老师/141101020.ogg"
    qcls "愿神之加护赐予汝身——"
    pause 1.0 hard
    play sound rune1
    scene white 
    with dissolve
    pause 2.0 hard
    show qcls_zf_b1_rune b1 b1 b1_n2 onlayer screens at side_left('qcls', 0.08), basicfade
    play voice "voice/千川老师/141101030.ogg"
    qcls "请为我们星天宫研究项目的未来进行预测。"
    stop music fadeout 5.0
    play voice "voice/千川老师/141101040.ogg"
    qcls "用你的{rb}预知未来{/rb}{rt}precognition{/rt}。"
    hide qcls_zf_b1_rune
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside3 xuejian alpha
    $ flcam.move(-4500, 300, 900, duration=1.5)
    play music second_146 fadein 3.0 if_changed
    with dissolve
    pause 0.5 hard
    show aiyi_dzf_b1_rune b1 b1 b1_rs2 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111102800.ogg"
    aiyi "......"
    hide aiyi_dzf_b1_rune
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1_rune b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151100680.ogg"
    shy "成功了吗？"
    play voice "voice/千川老师/141101050.ogg"
    qcls "应该是的。"
    hide shy_yjf_b1
    hide qcls_zf_b1_rune
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1_rune b1 b1 b1_rs2 onlayer m2:
        xpos 0.3
    "此时爱衣的周身充斥着强大的灵力。"
    "瞳孔的颜色也发生了变化。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qcls_zf_b1_rune b1 b1 b1_h3 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141101060.ogg"
    qcls "拜托了爱衣，解答完我们的问题就可以送你回家了哟~"
    play voice "voice/千川老师/141101070.ogg"
    qcls "能帮我们预知一下未来计划的结果吗？"
    show aiyi_dzf_b1_rune b1 b1 b1_s2
    play voice "voice/爱衣/111102810.ogg"
    aiyi "......"
    hide qcls_zf_b1_rune
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1_rune b1 b1 b1_rs2
    play voice "voice/爱衣/111102820.ogg"
    aiyi "芬布尔之冬......"
    hide aiyi_dzf_b1_rune
    $ flcam.move(2250, 0, 750, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    show liuli_dzf_b1 b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151100690.ogg"
    shy "花山院！"
    play voice "voice/琉璃/041100450.ogg"
    liuli "我知道了。"
    hide shy_yjf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dzf_b1
    play sound rune3
    show wflash onlayer texture
    show liuli_dzf_b1_rune b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041100460.ogg"
    liuli "现在开始使用{rb}接触感应{/rb}{rt}psychometry{/rt}对预言进行解析。"
    hide liuli_dzf_b1_rune
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1_rune b1 b1 b1_rs2 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111102830.ogg"
    aiyi "芬布尔之冬——"
    play voice "voice/爱衣/111102840.ogg"
    aiyi "持续三年的寒冬。"
    $ flcam.move(-4500, 300, 1000, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1_rune b1 b1 b1_s2
    play voice "voice/爱衣/111102850.ogg"
    aiyi "悲伤的冬季过后，将是永恒的沉寂。"
    show aiyi_dzf_b1_rune b1 b1 b1_rs2
    play voice "voice/爱衣/111102870.ogg"
    aiyi "但是这片天空中的月亮却并未消逝。"
    play voice "voice/爱衣/111102880.ogg"
    aiyi "天狗并没有选择啃食月亮。"
    play voice "voice/爱衣/111102890.ogg"
    aiyi "天狗选择了离开。"
    play voice "voice/爱衣/111102900.ogg"
    aiyi "在月亮消逝之前，先迷路了......"
    show aiyi_dzf_b1_rune b1 b1 b1_s2
    play voice "voice/爱衣/111102910.ogg"
    aiyi "......"
    play sound touch
    show aiyi_dzf_b1_rune b1 b1 b1_s2:
        xpos 0.3 alpha 1.0 ypos 1.0
        parallel:
            linear 0.75 ypos 1.04
        parallel:
            linear 0.75 alpha 0.0
    pause 1.0 hard
    hide aiyi_dzf_b1_rune
    with vpunch
    "话音刚落爱衣又一次陷入了沉睡。"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151100700.ogg"
    shy "这就结束了吗？"
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141101080.ogg"
    qcls "似乎是这样的。"
    $ flcam.move(0, 0, 600, duration=1.5)
    show liuli_dzf_b2 b2 b2_n4 onlayer m2:
        xpos 0.3
    play voice "voice/圣护院/151100710.ogg"
    shy "花山院，结果如何？"
    play voice "voice/琉璃/041100470.ogg"
    liuli "解析完毕，现在开始报告。"
    hide shy_yjf_b1
    hide qcls_zf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/琉璃/041100480.ogg"
    liuli "如果用月亮比喻行星，而天狗暗指探测器的话。"
    play voice "voice/琉璃/041100490.ogg"
    liuli "这与星天宫宇宙航天中心正在进行的行星探测计划的相关性很高。"
    play voice "voice/琉璃/041100500.ogg"
    liuli "“天狗并没有啃食月亮”，就意味着探测器无法抵达行星。"
    play voice "voice/琉璃/041100510.ogg"
    liuli "“天狗选择了离开”，就是说探测器最终只能返航。"
    play voice "voice/琉璃/041100520.ogg"
    liuli "而“在月亮消逝之前先迷路了”则是......"
    hide liuli_dzf_b2
    show liuli_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041100530.ogg"
    liuli "意味着控制室将会丢失探测器的信号，而后者将独自游荡在宇宙之中。"
    hide liuli_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151100720.ogg"
    shy "......是吗。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100730.ogg"
    shy "花山院，其他的可能性如何？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dzf_b2 b2 b2_n4 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041100540.ogg"
    liuli "解析只进行到这里，我的灵力回路并没有找到其他符合的可能性。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100740.ogg"
    shy "我知道了，辛苦你了。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100890.ogg"
    shy "那么花山院，你先到别的房间去吧。"
    hide liuli_dzf_b2
    show liuli_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041100550.ogg"
    liuli "明白了。"
    pause 0.5 hard
    play sound jiaobu2
    show liuli_dzf_b1 b1 b1_n3 at walkout_l(0.5)
    pause 0.5 hard
    play sound close_door4
    pause 3.0 hard
    $ flcam.move(2250, -350, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_sp2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/千川老师/141101150.ogg"
    qcls "发生什么事了吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100900.ogg"
    shy "花山院在这里的话，辩解起来会很麻烦。"
    show qcls_zf_b1 b1 b1_sp1
    play voice "voice/千川老师/141101160.ogg"
    qcls "欸？"
    play voice "voice/圣护院/151100910.ogg"
    shy "预言的解析到此为止，虽然还不完整但也算有了应对的手段，就先这样吧。"
    show qcls_zf_b1 b1 b1_sp2
    play voice "voice/千川老师/141101170.ogg"
    qcls "这究竟是......"
    play ambience1 jiaobu3 fadein 3.0
    $ flcam.move(2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151100920.ogg"
    shy "想必你也听到了吧，走廊传来的脚步声。看样子是朝着这个房间来的。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100930.ogg"
    shy "保护公主的骑士登场了。" 
    stop music fadeout 5.0
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day217.laboratory_event03:
    play sound close_door2
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside3 xuejian
    play music second_125 fadein 3.0 if_changed
    with right2left_02
    pause 1.0 hard
    me01 "爱衣！"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141101180.ogg"
    qcls "神野同学......你是来接爱衣的吗？"
    me01 "是啊，不过这里可不是幼儿园。"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141101190.ogg"
    qcls "即便是这样你还是来了，看来你真的是非常地喜欢爱衣。"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/141101200.ogg"
    qcls "相对的爱衣也非常喜欢神野同学，真是两情相悦呢~"
    me01 "抱歉我现在可没心情开玩笑。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141101210.ogg"
    qcls "是啊，这次的事件给你添麻烦了，真的非常抱歉。"
    me01 "之后我会好好听您解释的，在此之前能把爱衣还给我了吗？"
    play voice "voice/千川老师/141101220.ogg"
    qcls "这个......"
    hide qcls_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151100940.ogg"
    shy "真是吓了我一跳。"
    show shy_yjf_b1 b1 b1_n3
    play voice "voice/圣护院/151100950.ogg"
    shy "你的脚步声没有丝毫的犹豫，径直朝着这里而来。"
    play voice "voice/圣护院/151100960.ogg"
    shy "“日向爱衣就在研究所”这一点从水之濑那里得知也不难理解。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100970.ogg"
    shy "但是我们并没有告诉她这次计划的详情，所以她应该也不知道日向爱衣究竟会被带到哪个房间。"
    show shy_yjf_b1 b1 b1_n3
    play voice "voice/圣护院/151100980.ogg"
    shy "但是你对此似乎却很了解，可以告诉我原因吗？"
    me01 "非要说的话这并不是我的本事。"
    hide shy_yjf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_s1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/立花希/031102280.ogg"
    lhx "嘛，其实答案很简单~"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/031102290.ogg"
    lhx "只是我的{rb}接触感应{/rb}{rt}psychometry{/rt}碰巧捕捉到了爱衣的情报而已。"
    me01 "虽然不知道为何千川老师会突然解除{rb}灵纹{/rb}{rt}rune{/rt}，但多亏了那一瞬间我们才能找到这里。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141101230.ogg"
    qcls "......立花老师你也来了吗？"
    show lhx_dsf_b2 b2 b2_h2
    play voice "voice/立花希/031102320.ogg"
    lhx "别看我这样，我好歹也是幼儿园的一份子，保护学生是我分内的工作。"
    show lhx_dsf_b2 b2 b2_n2
    play voice "voice/立花希/031102330.ogg"
    lhx "千川老师难道不是这样想的吗？"
    show qcls_zf_b1 b1 b1_s2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/千川老师/141101240.ogg"
    qcls "......"
    me01 "那么差不多也该把爱衣还回来了吧？"
    hide lhx_dsf_b2
    hide qcls_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151101090.ogg"
    shy "啊，随你们高兴了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031102400.ogg"
    lhx "这么轻易就交出来了吗......"
    hide lhx_dsf_b3
    hide shy_yjf_b1
    $ flcam.move(-2800, 0, 1100, duration=1.5, warper='ease_cubic')
    pause 1.0 hard
    play sound touch
    pause 2.0 hard
    "我抱起了熟睡中的爱衣。"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151101100.ogg"
    shy "话说回来，水之濑那边怎么样了？"
    me01 "她的话我已经通知翔子去接应了。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151101110.ogg"
    shy "没想到水之濑竟然会败给你，真是难以置信......"
    me01 "圣护院小姐到底是为了什么才要绑架爱衣？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151101140.ogg"
    shy "你的说法很牵强啊，我们只不过是单纯地检查了一下日向爱衣的“病情”而已。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151101150.ogg"
    shy "看这房间就知道了，这座研究所的医疗设备是最齐全的。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151101190.ogg"
    shy "要知道她现在是{rb}灵继者{/rb}{rt}elfin{/rt}，不能排除会暴走的可能性。"
    play voice "voice/圣护院/151101200.ogg"
    shy "{rb}灵纹{/rb}{rt}rune{/rt}对小孩子的身体有很大的负担，这一点你们应该也是清楚的吧。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151101210.ogg"
    shy "所以我们也只是单纯地想要帮助日向爱衣而已。"
    me01 "总觉得很可疑啊......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151101220.ogg"
    shy "没什么可疑的，我们星天宫研究所的目的是研究异常气候。"
    play voice "voice/圣护院/151101230.ogg"
    shy "进一步而言也可以说是对{rb}灵继者{/rb}{rt}elfin{/rt}的研究。"
    play voice "voice/圣护院/151101240.ogg"
    shy "而且这并非是伤害{rb}灵继者{/rb}{rt}elfin{/rt}的意思，而是谋求合作。"
    show shy_yjf_b1 b1 b1_ga2
    play voice "voice/圣护院/151101250.ogg"
    shy "你也看到了吧？我对妹妹友加的情况也是这样处理的。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031102420.ogg"
    lhx "凉君，她是不是在说谎用我的{rb}接触感应{/rb}{rt}psychometry{/rt}探知一下就知道了。"
    hide lhx_dsf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151101260.ogg"
    shy "千川。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141101290.ogg"
    qcls "是......"
    hide qcls_zf_b1 with None
    pause 0.1 hard
    play sound rune3
    show qcls_zf_b1_rune b1 b1 b1_s3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    "千川老师发动了{rb}虚无{/rb}{rt}psi-missing{/rt}。"
    "整座研究所建筑都笼罩在了{rb}灵纹{/rb}{rt}rune{/rt}的覆盖范围内。"
    hide qcls_zf_b1_rune
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/151101270.ogg"
    shy "辛苦了~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031102450.ogg"
    lhx "什么叫辛苦了啊，你这样不就等于承认自己在说谎了吗？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151101280.ogg"
    shy "我只是有义务保护这座研究所的机密而已。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151101300.ogg"
    shy "更何况你们的擅自闯入本来就是非法入侵的行为。"
    me01 "算了立花老师，姑且就先相信她们说的话好了。"
    hide lhx_dsf_b3
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151101320.ogg"
    shy "明白的话就请回吧，我们也不是一直这么闲的。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151101330.ogg"
    shy "因为接下来会变得很忙了......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day217.birdge_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with slowdissolve
    pause 1.0 hard
    show szl_dzf_b3 b3 b3_s1 onlayer screens at side_left('szl', 0.15), basicfade
    play voice "voice/水之濑/051101490.ogg"
    szl "......"
    hide szl_dzf_b3
    pause 1.0 hard
    scene set only bridge day under xuejian alpha 
    $ flcam.move(4500, -300, 900, duration=1.5)
    play music second_118 fadein 3.0 if_changed
    with dissolve
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100660.ogg"
    rxl "醒了吗？"
    $ flcam.move(2250, -350, 750, duration=1.5)
    play sound touch
    show szl_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 0.992
        parallel:
            linear 1.0 ypos 0.942
        parallel:
            linear 1.0 alpha 1.0
    pause 0.5 hard
    play voice "voice/水之濑/051101500.ogg"
    szl "......日向同学？"
    play voice "voice/日向怜/121100670.ogg"
    rxl "已经可以站起来了吗？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101510.ogg"
    szl "......我没事，只是有点冷而已。"
    show rxl_dzf_b1 b1 b1_h3
    play voice "voice/日向怜/121100680.ogg"
    rxl "那要我帮你暖和一下吗？"
    show szl_dzf_b3 b3 b3_ga1
    play voice "voice/水之濑/051101520.ogg"
    szl "你要是敢靠近我的话就把你一刀两段。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100690.ogg"
    rxl "还是一如既往的冷淡呢~"
    $ flcam.move(2250, -350, 900, duration=1.5)
    pause 0.5 hard
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101530.ogg"
    szl "比起这个，为什么你会在这里？"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100700.ogg"
    rxl "当然是因为担心小凛你啊~"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/051101540.ogg"
    szl "怕是又想拿我寻开心吧。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100710.ogg"
    rxl "别明知故问啊。"
    show rxl_dzf_b2 b2 b2_n2
    play voice "voice/日向怜/121100790.ogg"
    rxl "小凛你，是不是有什么事瞒着我？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101610.ogg"
    szl "......没有什么特别的。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100800.ogg"
    rxl "不想说的话......那也没事。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101620.ogg"
    szl "你还真是怠惰呢。"
    show rxl_dzf_b1 b1 b1_h1
    play voice "voice/日向怜/121100830.ogg"
    rxl "反正有什么事情的话交给凉君就行了，我只对你比较感兴趣。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101640.ogg"
    szl "都说了再靠近的话我就把你一刀两断。"
    show rxl_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121100840.ogg"
    rxl "八十八吗......"
    play sound jing04
    show szl_dzf_b3 b3 b3_ga4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051101650.ogg"
    szl "{size=72}！！！{/size}"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100850.ogg"
    rxl "别紧张，之前就说了我是没办法透视的啦~"
    hide szl_dzf_b3
    show szl_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101660.ogg"
    szl "......的确如此。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100860.ogg"
    rxl "不过内衣倒是湿透了呢~"
    hide szl_dzf_b1 with None
    pause 0.1 hard
    show szl_dzf_b3 b3 b3_ga3 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/水之濑/051101670.ogg"
    szl "{size=72}！！！{/size}"
    play voice "voice/日向怜/121100870.ogg"
    rxl "小凛对生理方面的事情真是单纯啊~"
    hide szl_dzf_b3
    play sound hite_knife2
    show szl_dzf_knife_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101680.ogg"
    szl "你是想成为刀上的铁锈吗？"
    show rxl_dzf_b1 b1 b1_ga2
    play voice "voice/日向怜/121100880.ogg"
    rxl "别突然摆起架势啊......而且你那刀从哪里来的啊？"
    stop music fadeout 5.0
    hide szl_dzf_knife_b3
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101690.ogg"
    szl "怎么样都无所谓吧......"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100900.ogg"
    rxl "小凛，这里刚刚发生了什么？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101700.ogg"
    szl "......"
    show rxl_dzf_b2 b2 b2_n2
    play voice "voice/日向怜/121100910.ogg"
    rxl "我接到消息说你突然晕倒了。"
    play music second_122 fadein 3.0 if_changed
    show szl_dzf_b3 b3 b3_s1
    play voice "voice/水之濑/051101710.ogg"
    szl "我也不是很清楚。"
    hide szl_dzf_b3
    show szl_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101720.ogg"
    szl "总感觉自己好像看到了什么不得了的东西......"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100920.ogg"
    rxl "是因为惊吓过度所以忘记了？"
    show szl_dzf_b1 b1 b1_s1
    play voice "voice/水之濑/051101730.ogg"
    szl "不如说是一种不明所以的感觉。"
    show rxl_dzf_b1 b1 b1_ga1
    play voice "voice/日向怜/121100930.ogg"
    rxl "......什么意思？"
    show szl_dzf_b1 b1 b1_s1
    play voice "voice/水之濑/051101760.ogg"
    szl "就是经历了却没有办法解释的意思。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100940.ogg"
    rxl "......"
    hide szl_dzf_b1
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101770.ogg"
    szl "这座雪见市降下的温柔的雪——它的真面目或许就是这样的存在吧。"
    show rxl_dzf_b2 b2 b2_ga1
    play voice "voice/日向怜/121100950.ogg"
    rxl "怎么好像连我也开始听不懂了。"
    stop music fadeout 5.0
    hide szl_dzf_b2
    show szl_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101790.ogg"
    szl "那我走了。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121100960.ogg"
    rxl "去哪里？"
    play music second_118 fadein 3.0
    show szl_dzf_b1 b1 b1_s2
    play voice "voice/水之濑/051101800.ogg"
    szl "回家，再不换一套衣服的话......"
    pause 0.5 hard
    show szl_dzf_b1 b1 b1_s2 at walkout_l(0.5)
    pause 1.5 hard
    hide szl_zdf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_dzf_b1 with None
    pause 0.1 hard
    show rxl_dzf_b2 b2 b2_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/日向怜/121100970.ogg"
    rxl "我明白了~"
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_h1 at walkout_l(0.7)
    pause 0.5 hard
    hide rxl_dzf_b2
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    show rxl_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101810.ogg"
    szl "......为什么你要跟过来啊？"
    hide rxl_dzf_b2 with None
    pause 0.1 hard
    show rxl_dzf_b1 b1 b1_h3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121100980.ogg"
    rxl "小凛你手腕受伤了，所以让我来帮你换衣服吧~"
    show szl_dzf_b3 b3 b3_a1
    play voice "voice/水之濑/051101820.ogg"
    szl "你敢过来的话我就把你碎尸万段！"
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    play sound jiaobu2
    $ flcam.move(0, 0, 0)
    scene set only bridge day xuejian alpha
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_s3 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/水之濑/051101840.ogg"
    szl "......失败什么的还是第一次。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121101010.ogg"
    rxl "欸？"
    show szl_dzf_b2 b2 b2_s4
    play voice "voice/水之濑/051101850.ogg"
    szl "我是说神野君的事啦，在决胜负的时候输掉这还是第一次。"
    show rxl_dzf_b1 b1 b1_h1
    play voice "voice/日向怜/121101020.ogg"
    rxl "没关系的，我也会帮你的嘛~"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/051101860.ogg"
    szl "也许吧。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051101870.ogg"
    szl "嘛，反正我也没有自尊心这种东西，随便怎么样都行。"
    $ flcam.move(2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_sp1
    play voice "voice/日向怜/121101030.ogg"
    rxl "我倒是觉得小凛你一副非常在意的样子啊......"
    show szl_dzf_b3 b3 b3_ga1
    play voice "voice/水之濑/051101910.ogg"
    szl "丑话说在前面，就算你成为我的同伴我也没有和你好好相处的打算。"
    show rxl_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121101080.ogg"
    rxl "这才是野生的小凛啊~"
    show szl_dzf_b3 b3 b3_ga3
    play voice "voice/水之濑/051101920.ogg"
    szl "......别给我追加绰号啊。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day217.laboratory_event04:
    $ flcam.move(0, 0, 0)
    scene set only laboratory evening outside xuejian
    play music second_102 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141101300.ogg"
    qcls "神野同学、立花老师......抱歉能请你们等一下吗？"
    play voice "voice/千川老师/141101310.ogg"
    qcls "这次的事情我真的非常抱歉。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141101320.ogg"
    qcls "真不知道应该如何向你们解释才好......"
    me01 "事情都已经过去了，我也知道老师您其实并没有恶意。"
    me01 "我从藤原同学那里也了解到一些星天宫的事情，想必圣护院主任那边也一定有她自己的苦衷。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031102460.ogg"
    lhx "说到底主谋还是植澄圣护院，要道歉也应该是她来才对。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141101330.ogg"
    qcls "圣护院主任的发言是有一些欠妥的地方......让你们的误会了。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141101340.ogg"
    qcls "其实她只是热衷于工作而已。"
    me01 "这点我们自然明白，您不必太在意。"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031102470.ogg"
    lhx "千川老师也是星天宫的人对吧？"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141101350.ogg"
    qcls "是的......或者应该说是助手吧。"
    me01 "圣护院小姐的？"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141101360.ogg"
    qcls "嗯。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031102480.ogg"
    lhx "不过无论如何，本职还是幼儿园的老师这一点是不会变的对吧？"
    show qcls_zf_b1 b1 b1_n4
    play voice "voice/千川老师/141101370.ogg"
    qcls "那是当然的，我很喜欢幼儿园的工作。"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141101380.ogg"
    qcls "我最喜欢在那里上学的孩子们了~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ seen_living_room = False

label day217.myroom_event01:
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    pause 1.0 hard
    scene set only home night my_room xuejian
    show xz_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dzf_b3 onlayer m2:
            hide screen investigation_popup
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            move _("客厅") jump day217.livingroom_event01
            screen_direction left
            sleep jump day217.sleep

label day217.livingroom_event01:
    if not seen_living_room:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        play music second_111 fadein 3.0 if_changed
        $ flcam.move(0, -300, 900, duration=1.5)
        with dissolve
        pause 0.5 hard
        show xz_dzf_b2 b2 b2_sp1 onlayer m2 at walkin_r(0.5)
        pause 0.5 hard
        play voice "voice/翔子/011105820.ogg"
        xz "刚刚千川老师打电话来......说是爱衣那边也早退了？"
        me01 "是啊，还是放心不下吗？"
        hide xz_dzf_b2
        show xz_dzf_b1 b1 b1_s2 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011105830.ogg"
        xz "是啊......话说回来神野君你现在没问题了吗？不是说身体不舒服吗？"
        me01 "已经没事了。"
        $ flcam.move(0, -300, 1000, duration=1.5)
        pause 0.5 hard
        hide xz_dzf_b1
        show xz_dzf_b2 b2 b2_n1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011105840.ogg"
        xz "是吗......那太好了。"
        me01 "抱歉，让你担心了。"
        show xz_dzf_b2 b2 b2_s1
        play voice "voice/翔子/011105850.ogg"
        xz "担心到时没有，反正你是在装病吧。"
        me01 "有那么明显吗？"
        show xz_dzf_b2 b2 b2_s1 at flu_down(0.35, 20):
            xpos 0.5
        play voice "voice/翔子/011105860.ogg"
        xz "很明显，现在也是。"
        me01 "......突然觉得有点累，我还是稍微躺一会儿吧。"
        hide xz_dzf_b2
        show xz_dzf_b1 b1 b1_ga1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011105870.ogg"
        xz "不用假装也没事的，就算这样我也不会阻止你的。"
        show xz_dzf_b1 b1 b1_sp1
        play voice "voice/翔子/011105880.ogg"
        xz "爱衣在房间里？"
        me01 "是啊，我让她先睡下了。"
        hide xz_dzf_b1
        play sound open_door6
        $ flcam.move(-4500, 300, 900, duration=1.5)
        pause 0.5 hard
        show aiyi_sy_b1 b1 b1_n3 onlayer m2 at walkin_l(0.3)
        pause 0.5 hard
        play voice "voice/爱衣/111102920.ogg"
        aiyi "大哥哥？"
        show aiyi_sy_b1 b1 b1_sp1
        play voice "voice/爱衣/111102930.ogg"
        aiyi "......大姐姐也在，已经放学了吗？"
        $ flcam.move(-2250, 0, 750, duration=1.5)
        show xz_dzf_b1 b1 b1_sp2 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011105900.ogg"
        xz "比起这个爱衣......不去休息没关系吗？"
        hide xz_dzf_b1
        show xz_dzf_b2 b2 b2_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011105910.ogg"
        xz "身体怎么样？有哪里不舒服吗？"
        show aiyi_sy_b1 b1 b1_s2
        play voice "voice/爱衣/111102940.ogg"
        aiyi "睡太久了，感觉脑袋晕晕的。"
        play voice "voice/翔子/011105920.ogg"
        xz "其他的呢？"
        show aiyi_sy_b1 b1 b1_ga2
        play voice "voice/爱衣/111102950.ogg"
        aiyi "其他的没什么问题哟。"
        show xz_dzf_b2 b2 b2_s2
        play voice "voice/翔子/011105930.ogg"
        xz "我从千川老师那里听说你身体不舒服。"
        show aiyi_sy_b1 b1 b1_h1
        play voice "voice/爱衣/111102960.ogg"
        aiyi "请医生给我看过了，所以已经没事了。"
        show xz_dzf_b2 b2 b2_sp1
        play voice "voice/翔子/011105940.ogg"
        xz "你去医院了吗？"
        show aiyi_sy_b1 b1 b1_n1
        play voice "voice/爱衣/111102970.ogg"
        aiyi "嗯，千川老师带我去的。"
        show xz_dzf_b2 b2 b2_n1
        play voice "voice/翔子/011105950.ogg"
        xz "是吗......之后得向她道谢才行，钱也得还给她。"
        "我想这钱千川老师是绝对不会收的吧，不仅如此还会反过来道歉。"
        "似乎已经可以看到翔子茫然的表情了......"
        hide xz_dzf_b2
        show xz_dzf_b1 b1 b1_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011105960.ogg"
        xz "医生说了什么吗？"
        show aiyi_sy_b1 b1 b1_s2
        play voice "voice/爱衣/111102980.ogg"
        aiyi "那个......记不太清了，只是听千川老师说好好休息的话就没问题了。"
        show aiyi_sy_b1 b1 b1_h1
        play voice "voice/爱衣/111102990.ogg"
        aiyi "爱衣我已经充分休息过了，所以已经没事了~"
        show xz_dzf_b1 b1 b1_h1
        play voice "voice/翔子/011105970.ogg"
        xz "是吗......太好了。"
        hide xz_dzf_b1
        show xz_dzf_b3 b3 b3_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011105990.ogg"
        xz "爱衣，饭还吃得下吗？"
        show aiyi_sy_b1 b1 b1_n1
        play voice "voice/爱衣/111103040.ogg"
        aiyi "嗯，稍微有点肚子饿了。"
        hide xz_dzf_b3
        show xz_dzf_b2 b2 b2_h2 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011106020.ogg"
        xz "神野君呢？"
        me01 "那我也不客气了。"
        show aiyi_sy_b1 b1 b1_h1
        play voice "voice/爱衣/111103090.ogg"
        aiyi "爱衣我也来帮忙~"
        show xz_dzf_b2 b2 b2_ga1
        play voice "voice/翔子/011106250.ogg"
        xz "不用了，病人要好好休息才行。"
        me01 "作为补偿，就由我这个装病的来帮忙好了。"
        show xz_dzf_b2 b2 b2_h2
        play voice "voice/翔子/011106260.ogg"
        xz "那就拜托你了~"
        show aiyi_sy_b1 b1 b1_sp1
        play voice "voice/爱衣/111103100.ogg"
        aiyi "大哥哥不算病人吗？"
        show xz_dzf_b2 b2 b2_ga1
        play voice "voice/翔子/011106270.ogg"
        xz "毕竟只是装病而已嘛。"
        me01 "你还真是揪着不放啊。"
        $ flcam.move(-2250, 0, 900, duration=1.5)
        pause 0.5 hard
        show aiyi_sy_b1 b1 b1_n1
        play voice "voice/爱衣/111103110.ogg"
        aiyi "大姐姐你最近经常让大哥哥帮忙了呢。"
        show xz_dzf_b2 b2 b2_s2
        play voice "voice/翔子/011106280.ogg"
        xz "是这样吗？"
        show aiyi_sy_b1 b1 b1_h1
        play voice "voice/爱衣/111103120.ogg"
        aiyi "嗯，好像新婚夫妇一样~"
        show xz_dzf_b2 b2 b2_a2 at flu_down(0.35, 20):
            xpos 0.5
        play voice "voice/翔子/011106290.ogg"
        xz "才不是！"
        show aiyi_sy_b1 b1 b1_n1
        play voice "voice/爱衣/111103130.ogg"
        aiyi "那让爱衣也来帮忙行吗？"
        show xz_dzf_b2 b2 b2_s1
        play voice "voice/翔子/011106300.ogg"
        xz "不行......今天就老实地休息吧。"
        show aiyi_sy_b1 b1 b1_s2
        play voice "voice/爱衣/111103140.ogg"
        aiyi "爱衣我明明已经恢复精神了。"
        show xz_dzf_b2 b2 b2_n1
        play voice "voice/翔子/011106310.ogg"
        xz "不用勉强的，有神野君帮忙就足够了。"
        show aiyi_sy_b1 b1 b1_h1
        play voice "voice/爱衣/111103150.ogg"
        aiyi "因为要结婚了？"
        hide xz_dzf_b2
        show xz_dzf_b1 b1 b1_ga2 onlayer m2 at flu_down(0.15, 20):
            xpos 0.5
        play voice "voice/翔子/011106320.ogg"
        xz "才不是！"
        stop music fadeout 5.0
        pause 1.0 hard
        $ seen_living_room = True
    $ flcam.move(0, 0, 0)
    scene black 
    with dissolve
    pause 1.0 hard
    scene set only home night living_room xuejian
    show xz_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dzf_b3 onlayer m2:
            camera_pos (scale(2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction right
            move _("卧室") jump day217.myroom_event01

label day217.sleep:
    menu:
        "早点休息":
            if not seen_living_room:
                window mode thought
                me01 "睡觉之前还是先去看看翔子她们的情况吧。"
                $ flcam.move(0, -100, 400, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            show xz_dzf_b3 b3 b3_h1
            play voice "voice/翔子/010001080.ogg"
            xz "晚安~"
        "{#cancel}再等等":
            xz "还有什么事情要考虑吗......"
            $ flcam.move(0, -100, 400, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    jump day217.ritroom

label day217.ritroom:
    default seen_day217_ritroom = False
    play music ritroom_day fadein 3.0 if_changed
    play ambience1 ritroom_fireplace fadein 3.0 if_changed

    if not seen_day217_ritroom:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        scene set ritfrontyard autumn night:
            mid autumn night
            frontl autumn night
            frontr autumn night
        $ flcam.move(0, 0, 400)
        $ flcam.move(0, 0, 0, duration=1.5)
        with dissolve
        pause 3.0 hard

        scene set ritroom night:
            eggs
            eggscover
            windchime
            midl
            midc
            midr
            midt
            front1
            front2
            front3
            front6
            front4
            front5
        $ flcam.move(-14575, 0, 0)
        $ flcam.move(14575, 0, 0, duration=3.0, warper='ease_cubic')
        with dissolve
        pause 3.5 hard
        $ flcam.move(-5400, -100, 400, duration=1.5)
        pause 0.25 hard
        show ritona b3 fb5 fa1 fc12 s onlayer m2:
            xpos 0.5
        show ritona b1 fb1 fa0 fc11 s
        ritona "鉴于你目前的实力已经有所提升，接下来将会给你安排更加具有挑战性的试炼。"
        me01 "......"
        show ritona b3 fb5 fa1 fc02
        ritona "话说这种时候不应该兴奋起来吗。"
        me01 "我说啊，真正能让我兴奋起来的应该是躺着就能拿奖励的情况吧。"
        show ritona b1 fb5 fa2 fc01
        ritona "......"
        show ritona b1 fb4 fa2 fc12 s
        ritona "愚、愚蠢之徒！看你这散漫的样子，恐怕都没有好好体会剧情吧？！"
        me01 "冷静！冷静啊芙兰小姐！"
        show ritona b1 fb2 fa5 fc12
        ritona "哈、哈......（喘气声）"
        show ritona b1 fb2 fa5 fc12
        ritona "算了，反正我就是个没有配音的角色怎么样也不会有人在乎的。"
        me01 "那个......"
        ritona "再说了这些枯燥的副本也不是我想让你体验的，只是怕你在今后的战斗中吃亏而已......"
        me01 "芙兰小姐？！"
        show ritona b1 fb5 fa2 fc01
        ritona "欸？！"
        me01 "抱歉，刚刚只是一时失言还请你别往心里去。"
        show ritona b1 fb4 fa2 fc12 s
        ritona "......我、我才不会在意呢。"
        show ritona b1 fb4 fa3 fc01
        ritona "比起这个还是快点去尝试新的试炼吧。"
        show ritona b3 fb1 fa5 fc02 s
        ritona "顺带一提随着难度的提升试炼的奖励也会更加丰富，能够减少刷图的次数。"
        show ritona b1 fb4 fa3 fc01
        ritona "当然这些无关紧要的小事你肯定也......"
        me01 "就是这个！" with vpunch
        show ritona b1 fb5 fa2 fc15
        ritona "呜哇啊啊啊！"
        ritona "突然怎么了吓我一跳。"
        me01 "不如说这才是能让我兴奋起来的事情。"
        me01 "芙兰小姐你还真是不懂男孩子的心思啊。"
        show ritona b1 fb2 fa5 fc12
        ritona "要、要你管......"
        show ritona b1 fb4 fa2 fc12 s
        ritona "等等，你说谁不懂男孩子的心思啊！" with vpunch
        $ flcam.stop()
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
        $ seen_day217_ritroom = True
       
        python:
            local_config.total_tutorial_flags += [
                "attack_battle_hard",
                "speed_battle_hard",
                "protect_battle_hard",
                "fire_battle_hard",
                "light_battle_hard", 
                "water_battle_hard", 
                "ice_battle_hard", 
                "rock_battle_hard", 
                "wind_battle_hard"
            ]
    else:
        pause 0.5 hard
        scene black with dissolve
        pause 3.0 hard
        scene set ritroom night:
            eggs
            eggscover
            windchime
            midl
            midc
            midr
            midt
            front1
            front2
            front3
            front6
            front4
            front5
        show ritona b3 fb1 fa0 fc02 onlayer m2:
            xpos 0.5
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-14575.0), scale(-0.0), 0.0) to (scale(+14575.0), scale(+0.0), 1350.0)
        menu ritona onlayer m2:
            camera_pos (scale(-4140), scale(-510), 800)
            screen_pos (0.5, 1.0)
            screen_direction left
            sleep jump day217.sleep_memory
            shop jump day217.shop
            member jump day217.stats
            teleport jump day217.teleport
            callback jump day217.callback
            roleroom jump day217.roleroom


label day217.callback:
    default seen_day217_callback = False
    hide screen investigation_popup
    scene black
    pause 1.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg msk
    with slowdissolve
    pause 0.5 hard
    
    python:
        can_get_roles_1 = "、".join(["「{}」".format(getattr(store, obj).name) for obj in list(local_config.role_pool)[:6]])
        can_get_roles_2 = "、".join(["「{}」".format(getattr(store, obj).name) for obj in list(local_config.role_pool)[6:]])
        outfits_level1 = [outfit for outfit in outfit_list if "_01" in outfit.objectname]
        outfits_level2 = [outfit for outfit in outfit_list if "_02" in outfit.objectname]
        outfits_level3 = [outfit for outfit in outfit_list if "_03" in outfit.objectname]
        outfits_level4 = [outfit for outfit in outfit_list if "_04" in outfit.objectname]

        equip_is_full = local_config.player.is_equipments_full(recall=1)
        equip_is_full_10 = local_config.player.is_equipments_full(recall=10)

    if not seen_day217_callback:
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
        show ritona b9 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)
        window mode thought
        ritona "当前可抽取的角色包括[can_get_roles_1]"
        window mode thought
        ritona "[can_get_roles_2]"
        show ritona b3
        pause 0.15 hard
        show ritona b3 at walkout_r(0.75)
        pause 0.5 hard
        hide ritona b3
        $ flcam.move(0, 0, 0, duration=1.5)
        pause 0.5 hard

        show white onlayer texture:
            additive 1
            alpha 0
            1.75
            linear 0.25 alpha 1
        pause 5.0 hard

        $ seen_day217_callback = True
    
    stop music fadeout 2.0
    pause 1.0 hard
    $ mouse_visible = False
    $ _skipping = renpy.seen_audio("video/second_op.mp4")
    $ config.skipping = None
    scene black
    show movie onlayer master
    play movie "video/second_op.mp4" loop
    play music "video/second_op.mp3" loop
    pause 5.0 hard
    $ _window_animation = 'in'
    $ mouse_visible = True
    
    while True:
        $ detect_drop = False
        $ drag_name = ""

        menu:
            "召唤":
                if equip_is_full:
                    window mode thgouth
                    me01 "装备栏已接近上限，优先清理一下无用道具防止装备无法获取的情况出现。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day206.ritroom
                elif local_config.player.currency >= 160:
                    $ local_config.player.currency -= 160
                    
                    while not detect_drop:
                        call screen send_detective_screen

                    show pooler_move:
                        xalign 0.5
                        yalign 0.35

                    # call screen input_sentence
                    # $ sentence = _return.strip()

                    pause 0.5 hard
                    show wflash onlayer m2
                    play sound chain_voice
                    show chain1 with vpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain2 with hpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain3 with vpunch
                    pause 0.25 hard
                    show wflash onlayer m2
                    play ambience1 pent_charge fadein 1.0
                    show cut_pentblack:
                        xalign 0.5 yalign 0.5
                        zoom 0
                        rotate 0
                        parallel:
                            ease 0.3 zoom 1.0
                        parallel:
                            linear 4.0 rotate 360
                            repeat
                    pause 2.0 hard
                    show white onlayer screens
                    with slowdissolve
                    pause 2.0 hard
                    hide chain1
                    hide chain2
                    hide chain3
                    hide cut_pentblack
                    hide white
                    stop ambience1 fadeout 2.0

                    python:
                        sp_ratio = renpy.random.random()
                        # 角色
                        if sp_ratio <= persistent.ratio_table["role"]:
                            chosen_member_idx = renpy.random.randint(0, len(local_config.role_pool) - 1)
                            chosen_member_objectname = list(local_config.role_pool)[chosen_member_idx]
                            chosen_member = getattr(store, chosen_member_objectname)
                            chosen_name = chosen_member.name

                            renpy.pause(1.0, hard=True)
                            renpy.show("black", layer="f2")
                            renpy.transition(dissolve)
                            renpy.pause(1.0, hard=True)
                            renpy.hide("black", layer="f2")
                            renpy.show("sp_ani_role", layer="screens")
                            renpy.music.play("video/ms2_portal.mp3", synchro_start='movie', channel='sound', loop=False)
                            renpy.pause(0.4)
                            renpy.hide("sp_ani_role", layer="screens")
                            renpy.show("black", layer="f2")
                            renpy.transition(dissolve)
                            renpy.pause(3.0, hard=True)
                            renpy.hide("black", layer="f2")

                            renpy.show(chosen_member.objectname, at_list=[show_player(0.5)], layer="m2")
                            renpy.pause(1.0, hard=True)

                            renpy.say(chosen_name, "我的名字是「[chosen_name]」")
                            renpy.say(chosen_name, "以后请多多指教~")

                            # 已拥有角色：技能等级加1
                            if chosen_name in [obj.name for obj in (local_config.party + local_config.backup)]:
                                for role in local_config.party + local_config.backup:
                                    if role.name == chosen_name:
                                        if any(s.level < 5 for s in role.skills):
                                            selectup_skill = role.skill_levelup()
                                            renpy.say(chosen_name, "技能「[selectup_skill.name]」强化至Lv.[selectup_skill.level]")
                                        else:
                                            local_config.player.currency += 1500
                                        break
                            # 未拥有角色：加入后补队伍
                            elif chosen_name in [getattr(store, obj).name for obj in local_config.role_pool]:
                                local_config.backup.append(chosen_member)
                                renpy.say(chosen_name, "「[chosen_name]」加入队伍")
                            else:
                                local_config.player.currency += 1500

                            renpy.hide(chosen_member.objectname, layer="m2")
                            renpy.pause(0.75, hard=True)
                        # # 道具
                        # elif sp_ratio <= persistent.ratio_table["items"]:
                        #     chosen_item_idx = renpy.random.randint(0, len(local_config.shop_list) - 1)
                        #     chosen_item_objectname = local_config.shop_list[chosen_item_idx]
                        #     chosen_item = getattr(store, chosen_item_objectname)
                        #     chosen_item.get(who=local_config.player)
                        #     chosen_name = chosen_item.name

                        #     if chosen_item.image not in [None, ""]:
                        #         if chosen_item.image == "item01":
                        #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.7, xalign=0.5, yalign=0.5)], layer="m2")
                        #         else:
                        #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.3, xalign=0.5, yalign=0.5)], layer="m2")
                        #         renpy.pause(1.0, hard=True)

                        #     renpy.say(chosen_name, "获得物品「[chosen_name]」")

                        #     renpy.hide(chosen_item.image, layer="m2")
                        #     renpy.pause(0.75, hard=True)
                        # 装备
                        else:
                            if renpy.random.random() <= 0.25:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level1) - 1)
                                chosen_equip = outfits_level1[chosen_equip_idx]
                            elif renpy.random.random() <= 0.5:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level2) - 1)
                                chosen_equip = outfits_level2[chosen_equip_idx]
                            elif renpy.random.random() <= 0.75:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level3) - 1)
                                chosen_equip = outfits_level3[chosen_equip_idx]
                            else:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level4) - 1)
                                chosen_equip = outfits_level4[chosen_equip_idx]
                            
                            chosen_equip_objectname = chosen_equip.objectname
                            chosen_equip.get(who=local_config.player)
                            chosen_name = chosen_equip.name
                            
                            renpy.show(chosen_equip_objectname, at_list=[Transform(zoom=1.0, xalign=0.5, yalign=0.5)], layer="m2")
                            renpy.pause(1.0, hard=True)

                            equip_level = ""
                            if "_01" in chosen_equip_objectname:
                                equip_level = "普通"
                            elif "_02" in chosen_equip_objectname:
                                equip_level = "稀有"
                            elif "_03" in chosen_equip_objectname:
                                equip_level = "史诗"
                            else:
                                equip_level = "传说"
                            renpy.say(me01, "获得「[equip_level]」[chosen_equip.category]「[chosen_name]」")

                            renpy.hide(chosen_equip_objectname, layer="m2")
                            renpy.pause(0.75, hard=True)

                    hide pooler_move
                else:
                    window mode thought
                    me01 "魔法币不足500是无法进入异空间的，无论在哪个世界穷是永远的痛！"
                    me01 "快去「异界」获取更多魔法币吧。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day217.ritroom
            "十连召唤":
                if equip_is_full_10:
                    window mode thgouth
                    me01 "装备栏已接近上限，优先清理一下无用道具防止装备无法获取的情况出现。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day206.ritroom
                elif local_config.player.currency >= 1500:
                    $ local_config.player.currency -= 1500

                    while not detect_drop:
                        call screen send_detective_screen

                    show pooler_move:
                        xalign 0.5
                        yalign 0.35

                    # call screen input_sentence
                    # $ sentence = _return.strip()

                    pause 0.5 hard
                    show wflash onlayer m2
                    play sound chain_voice
                    show chain1 with vpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain2 with hpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain3 with vpunch
                    pause 0.25 hard
                    show wflash onlayer m2
                    play ambience1 pent_charge fadein 1.0
                    show cut_pentblack:
                        xalign 0.5 yalign 0.5
                        zoom 0
                        rotate 0
                        parallel:
                            ease 0.3 zoom 1.0
                        parallel:
                            linear 4.0 rotate 360
                            repeat
                    pause 2.0 hard
                    show white onlayer screens
                    with slowdissolve
                    pause 2.0 hard
                    hide chain1
                    hide chain2
                    hide chain3
                    hide cut_pentblack
                    hide white
                    stop ambience1 fadeout 2.0
                    
                    python:
                        for i in xrange(10):
                            sp_ratio = renpy.random.random()
                            # 角色
                            if sp_ratio <= persistent.ratio_table["role"]:
                                chosen_member_idx = renpy.random.randint(0, len(local_config.role_pool) - 1)
                                chosen_member_objectname = list(local_config.role_pool)[chosen_member_idx]
                                chosen_member = getattr(store, chosen_member_objectname)
                                chosen_name = chosen_member.name

                                renpy.pause(1.0, hard=True)
                                renpy.show("black", layer="f2")
                                renpy.transition(dissolve)
                                renpy.pause(1.0, hard=True)
                                renpy.hide("black", layer="f2")
                                renpy.show("sp_ani_role", layer="screens")
                                renpy.music.play("video/ms2_portal.mp3", synchro_start='movie', channel='sound', loop=False)
                                renpy.pause(0.4)
                                renpy.hide("sp_ani_role", layer="screens")
                                renpy.show("black", layer="f2")
                                renpy.transition(dissolve)
                                renpy.pause(3.0, hard=True)
                                renpy.hide("black", layer="f2")

                                renpy.show(chosen_member.objectname, at_list=[show_player(0.5)], layer="m2")
                                renpy.pause(1.0, hard=True)

                                renpy.say(chosen_name, "我的名字是「[chosen_name]」{w=1.0}{nw}")
                                renpy.say(chosen_name, "以后请多多指教~{w=1.0}{nw}")

                                # 已拥有角色：技能等级加1
                                if chosen_name in [obj.name for obj in (local_config.party + local_config.backup)]:
                                    for role in local_config.party + local_config.backup:
                                        if role.name == chosen_name:
                                            if any(s.level < 5 for s in role.skills):
                                                selectup_skill = role.skill_levelup()
                                                renpy.say(chosen_name, "技能「[selectup_skill.name]」强化至Lv.[selectup_skill.level]")
                                            else:
                                                local_config.player.currency += 1500
                                            break
                                # 未拥有角色：加入后补队伍
                                elif chosen_name in [getattr(store, obj).name for obj in local_config.role_pool]:
                                    local_config.backup.append(chosen_member)
                                    renpy.say(chosen_name, "「[chosen_name]」加入队伍{w=1.0}{nw}")
                                else:
                                    local_config.player.currency += 1500

                                renpy.hide(chosen_member.objectname, layer="m2")
                                renpy.pause(0.75, hard=True)
                            # 道具
                            # elif sp_ratio <= persistent.ratio_table["items"]:
                            #     chosen_item_idx = renpy.random.randint(0, len(local_config.shop_list) - 1)
                            #     chosen_item_objectname = local_config.shop_list[chosen_item_idx]
                            #     chosen_item = getattr(store, chosen_item_objectname)
                            #     chosen_item.get(who=local_config.player)
                            #     chosen_name = chosen_item.name

                            #     if chosen_item.image not in [None, ""]:
                            #         if chosen_item.image == "item01":
                            #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.7, xalign=0.5, yalign=0.5)], layer="m2")
                            #         else:
                            #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.3, xalign=0.5, yalign=0.5)], layer="m2")
                            #         renpy.pause(1.0, hard=True)

                            #     renpy.say(chosen_name, "获得物品「[chosen_name]」{w=1.0}{nw}")

                            #     renpy.hide(chosen_item.image, layer="m2")
                            #     renpy.pause(0.75, hard=True)
                            # 装备
                            else:
                                if renpy.random.random() <= 0.25:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level1) - 1)
                                    chosen_equip = outfits_level1[chosen_equip_idx]
                                elif renpy.random.random() <= 0.5:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level2) - 1)
                                    chosen_equip = outfits_level2[chosen_equip_idx]
                                elif renpy.random.random() <= 0.75:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level3) - 1)
                                    chosen_equip = outfits_level3[chosen_equip_idx]
                                else:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level4) - 1)
                                    chosen_equip = outfits_level4[chosen_equip_idx]
                                
                                chosen_equip_objectname = chosen_equip.objectname
                                chosen_equip.get(who=local_config.player)
                                chosen_name = chosen_equip.name
                                
                                renpy.show(chosen_equip_objectname, at_list=[Transform(zoom=1.0, xalign=0.5, yalign=0.5)], layer="m2")
                                renpy.pause(1.0, hard=True)
                                
                                equip_level = ""
                                if "_01" in chosen_equip_objectname:
                                    equip_level = "普通"
                                elif "_02" in chosen_equip_objectname:
                                    equip_level = "稀有"
                                elif "_03" in chosen_equip_objectname:
                                    equip_level = "史诗"
                                else:
                                    equip_level = "传说"
                                renpy.say(chosen_name, "获得「[equip_level]」[chosen_equip.category]「[chosen_name]」{w=1.0}{nw}")

                                renpy.hide(chosen_equip_objectname, layer="m2")
                                renpy.pause(0.75, hard=True)

                    hide pooler_move
                else:
                    window mode thought
                    me01 "魔法币不足4500是无法进入多重异空间的，无论在哪个世界穷是永远的痛！"
                    me01 "快去「异界」获取更多魔法币吧。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day217.ritroom
            "下次一定":
                window mode thgouth
                me01 "相遇即是缘，请好好珍惜这份来之不易的羁绊。"
                pause 0.5 hard
                $ window_animate_outro()
                stop movie
                hide movie
                stop music fadeout 1.0
                $ _skipping = True
                jump day217.ritroom


label day217.shop:
    hide investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day city3 xuejian
    with slowdissolve
    pause 1.0 hard
    show ritona b3 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)

    python:
        config.skipping = None
        renpy.block_rollback()
        _rollback = True

        local_config.current_message = ""
        local_config.current_mode = "buy"
        renpy.retain_after_load()
        _rollback = False

    if _return != False:
        call screen shop
    pause 0.5 hard
    jump day217.ritroom


label day217.stats:
    hide screen investigation_popup
    
    python:
        for role in local_config.party:
            role.hp = role.max_hp + role.extend_max_hp
            role.mp = role.max_mp
    $ local_config.current_mode == "Consumables"
    $ local_config.current_actor = local_config.party[0]

    call screen stats
    jump investigate


label day217.roleroom:
    hide screen investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)

    python:
        local_config.start_init(local_config.player, local_config.party)
        local_config.next_story = "day217.ritroom"
    
    call info


label day217.teleport:
    hide screen investigation_popup

    python:
        current_message = ""
        
    call screen teleporter("217")
    jump investigate


label day217.sleep_memory:
    menu:
        "结束梦境":
            python:
                ms_average_level = 0
                breakout_flag = []
                outfits_levels = []
                for par_name in local_config.masters:
                    for role in local_config.party:
                        if role.objectname == par_name:
                            ms_average_level += role.level
                            if role.level < 40 and role.level % 5 == 0 and (not role.break_through):
                                breakout_flag.append(False)
                            else:
                                breakout_flag.append(True)
                            for categ, outfit in role.outfits.items():
                                if outfit is not None:
                                    outfits_levels.append(outfit.level)
                                else:
                                    outfits_levels.append(0)
                ms_average_level /= len(local_config.masters)

            if (ms_average_level < 35) or (not all(breakout_flag)) or any([l < 10 for l in outfits_levels]):
                window mode thought
                me01 "下一次的敌人可能会比较棘手，还是去「异界」和「养成屋」多准备一下吧。"
                window mode thought
                me01 "确保队伍的平均等级在{color=#ff0000}35级突破{/color}以上、且装备等级均在10级以上比较稳妥。"
                menu:
                    "继续前进（不推荐）":
                        pass
                    "再准备准备":
                        $ camera_move(-5400, 100, 200, duration=3.0)
                        pause 0.5 hard
                        jump investigate
            $ flcam.move(-5400, -100, 400, duration=1.5)
            pause 0.5 hard
            show ritona b1 fb4 fa3 fc01
            ritona "我们还会再见的，神野凉......"
        "{#cancel}再等等":
            ritona "还有什么事情要考虑的吗？"
            $ camera_move(-5400, 100, 200, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard

    $ renpy.block_rollback()
    $ _rollback = True

    jump day218
