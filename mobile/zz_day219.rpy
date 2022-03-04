
label inside_battle14(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "花山院琉璃属于输出型角色，在战斗过程中需注意控制我方角色的{color=#f00}血量{/color}。"
    "当花山院琉璃的生命值每损失上限的30%将进入「超燃凝聚态」。期间获得一层基于其攻击力数值的{color=#f30}火元素{/color}护盾并锁定行动条。"
    "若我方无法在{color=#f00}5个回合内{/color}破除护盾，则场上全体友方将受到生命上限60%的{color=#f30}火元素{/color}间接伤害（承受伤害的角色生命值不低于1），同时恢复花山院琉璃10%生命上限的生命值。"
    "在河滩附近作战使得所有角色的{color=#19f}水元素伤害{/color}提升40%。"
    "{color=#f00}降低其攻击力{/color}以及使用{color=#19f}水元素{/color}攻击是比较好的应对手段。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label day219:
    bookmark
    $ save_name = _("Day 219")
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
    show backend_date218 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only school snow day outside xuejian2
    show snow_level1 onlayer fg
    play music second_142 fadein 3.0 if_changed
    with slowdissolve
    pause 2.0 hard
    scene set only school snow day center room xuejian
    with dissolve
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/041100560.ogg"
    liuli "......神野前辈。"
    me01 "琉璃你今天也一个人吃饭吗？"
    show liuli_dzf_b1 b1 b1_s2
    play voice "voice/琉璃/041100590.ogg"
    liuli "是、是这样的。"
    play voice "voice/琉璃/041100600.ogg"
    liuli "虽然这种天气在这里吃饭有点困难，但我想说不定......"
    hide liuli_dzf_b1
    show liuli_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041100610.ogg"
    liuli "还能再见到神野前辈的话......就太好了。"
    me01 "我也觉得说不定来这里就能和琉璃一起吃饭了。"
    me01 "那么话不多说，我们开始吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with dissolve
    pause 1.0 hard
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('chapter six'), _("若你困于星辰之间"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard
    "雪花纷然飘落。"
    "空气中弥漫着令人窒息的寒冷与寂寞。"
    "此刻的雪见市迎来了新一年的冬天——"

    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day219'
    $ seen_day219_school_event01 = False
    $ seen_day219_laboratory_event01 = False
    $ seen_day219_balltower_event01 = False
    $ seen_day219_home_event01 = False
    $ seen_day219_laboratory_event02 = False

label day219.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day219':
        show set maps winter day
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day219.school_event01':
        show set maps winter day
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day219.laboratory_event01':
        show set maps winter day
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['laboratory'])
    elif _overworld_label == 'day219.balltower_event02':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day219.home_event01':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day219.laboratory_event02':
        show set maps winter evening
        $ flcam.move(*overworld.camera_positions['laboratory'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        school=("day219.school_event01", "not seen_day219_school_event01"),
        cloqks=("day219.balltower_event01", "seen_day219_school_event01 and seen_day219_laboratory_event01 and not seen_day219_balltower_event01"),
        road1=("day219.home_event01", "seen_day219_balltower_event01 and not seen_day219_home_event01"),
        laboratory=("day219.laboratory_event02", "(not seen_day219_laboratory_event01) or (seen_day219_home_event01 and not seen_day219_laboratory_event02)"),
        bridge=("day219.bridge_event01", "seen_day219_laboratory_event02"))
    $ window_animate_outro()
    if _return == 'day219.school_event01' and _overworld_label == 'day219':
        with Pause(1.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day219.school_event01' and _overworld_label != 'day219':
        $ flcam.move(*overworld.camera_positions['school'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day219.laboratory_event02' and (_overworld_label == 'day219' or _overworld_label == 'day219.school_event01'):
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
        $ _window_animation = None
        stop music fadeout 3.0
        pause 3.0 hard
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        jump expression 'day219.laboratory_event01'
    elif _return == 'day219.laboratory_event02' and _overworld_label == 'day219.home_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day219.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day219.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day219.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
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

label day219.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day corridor xuejian
    play music second_102 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dzf_b3 b3 b3_s3 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011500790.ogg"
    xz "......"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021500920.ogg"
    yj "翔子？"
    hide xz_dzf_b3
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011500800.ogg"
    xz "太突然了吧，这件事。"
    play voice "voice/翔子/011500810.ogg"
    xz "转学什么的......"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/021500930.ogg"
    yj "抱歉......我也是突然从姐姐那里了解到的。"
    show yj_dzf_b1 b1 b1_s2
    play voice "voice/植澄友加/021500940.ogg"
    yj "说是要去岛上的宇宙研究中心。"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/021500950.ogg"
    yj "还被问了“友加，你打算怎么办”之类的。"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/011500820.ogg"
    xz "所以你马上就答应下来了吗？"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021500960.ogg"
    yj "这也是没有办法的事，毕竟姐姐她没我在的话不知道会怎么样嘛。"
    hide xz_dzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021500970.ogg"
    yj "虽然听了这个消息的时候我也吓了一跳、也很生气。"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_ga4 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021500980.ogg"
    yj "但一想到要让姐姐一个人生活的话，就会变成连饭也不按时吃的状态了。"
    show yj_dzf_b2 b2 b2_s2
    play voice "voice/植澄友加/021500990.ogg"
    yj "想到这里就会很担心......如果分开的话可能就会更加担心了。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_h2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021501000.ogg"
    yj "所以，我才决定要和姐姐一起离开雪见市的。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011500830.ogg"
    xz "......"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021501010.ogg"
    yj "但是翔子，你不用担心。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    show yj_dzf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021501020.ogg"
    yj "有机会的话我还是会回来雪见市的。"
    show yj_dzf_b2 b2 b2_n1
    play voice "voice/植澄友加/021501040.ogg"
    yj "所以一定不会寂寞的。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_h2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021501050.ogg"
    yj "这不是离别。"
    hide xz_dzf_b3
    show xz_dzf_b1 b1 b1_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011500850.ogg"
    xz "是吗。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day219_school_event01:
        $ seen_day219_school_event01 = True
    $ _overworld_label = 'day219.school_event01'
    jump day219.map

label day219.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    play music second_125 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show liuli_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041404670.ogg"
    liuli "我们真的就要......加入新的计划团队了？"
    show liuli_dzf_b1 b1 b1_s3
    play voice "voice/琉璃/041404720.ogg"
    liuli "我很快就要离开这座城市了吗？"
    show liuli_dzf_b1 b1 b1_s1
    play voice "voice/琉璃/041404650.ogg"
    liuli "......"
    show liuli_dzf_b1 b1 b1_c1
    play voice "voice/琉璃/041404780.ogg"
    liuli "我不要。"
    play voice "voice/琉璃/041404790.ogg"
    liuli "我果然还不想离开这座城市。"
    play voice "voice/琉璃/041404800.ogg"
    liuli "不想和藤原同学分开。"
    play voice "voice/琉璃/041404810.ogg"
    liuli "不想从神野前辈的身边离开。"
    show liuli_dzf_b1 b1 b1_s3
    play voice "voice/琉璃/041404840.ogg"
    liuli "虽然我明白......这些说到底也只是我的任性罢了。"
    show liuli_dzf_b1 b1 b1_c1
    play voice "voice/琉璃/041404850.ogg"
    liuli "但是......只要再一下子就好了。"
    play voice "voice/琉璃/041404870.ogg"
    liuli "让我在神野前辈的身边再多待一阵子。"
    play voice "voice/琉璃/041404900.ogg"
    liuli "再多创造一点回忆。"
    show liuli_dzf_b1 b1 b1_s1
    play voice "voice/琉璃/041404910.ogg"
    liuli "这样的话......即使我踏上了宇宙。"
    show liuli_dzf_b1 b1 b1_s3
    play voice "voice/琉璃/041404920.ogg"
    liuli "即使在那孤独的宇宙中，我也能够忍耐。"
    play voice "voice/琉璃/041404940.ogg"
    liuli "即使孤独一人，我也能坦然接受了。"
    stop music fadeout 5.0
    show liuli_dzf_b1 b1 b1_c1
    play voice "voice/琉璃/041404950.ogg"
    liuli "所以......"
    pause 1.0 hard
    play sound rune1
    show wflash onlayer texture
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    play music second_123 fadein 3.0 if_changed
    scene white
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    show liuli_dzf_b1 b1 b1_n3 onlayer screens at side_left('liuli'), basicfade
    play voice "voice/琉璃/041405020.ogg"
    liuli "为了人类的未来必须离开雪见市。"
    play voice "voice/琉璃/041405030.ogg"
    liuli "舍弃朋友。"
    play voice "voice/琉璃/041405040.ogg"
    liuli "放弃......神野凉。"
    hide liuli_dzf_b1
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard
    scene set only laboratory inside1 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151401080.ogg"
    shy "呐......花山院。"
    play voice "voice/圣护院/151401090.ogg"
    shy "当初的你不也是为了忘记一切才决定加入星天宫的吗？"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151401100.ogg"
    shy "所以打从一开始你就已经做出选择了吧。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151401120.ogg"
    shy "就算真的迎来了春天，{rb}灵继者{/rb}{rt}elfin{/rt}的命运也无法改变。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_c1
    play voice "voice/圣护院/151401130.ogg"
    shy "因为至少现在她们无论如何，也无法再次成为人类的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day219_laboratory_event01:
        $ seen_day219_laboratory_event01 = True
    $ _overworld_label = 'day219.laboratory_event01'
    jump day219.map

label day219.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 2.0 hard
    play sound jiaobu
    scene set only balltower snow day xuejian
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "说起来也有一段时间没见到希菲尔了。"
    "现在才注意到，每次都是她突然出现在我的身边。"
    "像这样主动找她的次数也算是非常少的。"
    "如果希菲尔和雷亚是相同的存在，那么她想要“收割”的噩梦又会是什么呢？"
    "又为什么要在这座城市降下温柔的雪呢？"
    "为什么明明笑着的她看起来......却是那么的悲伤呢？"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    me01 "找到你了，希菲尔。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg normal
    play music second_103 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001400160.ogg"
    xfe "被找到了~"
    me01 "在玩躲猫猫吗？"
    play voice "voice/希菲尔/001400170.ogg"
    xfe "是啊。"
    me01 "我总有种只要来这里就一定能见到希菲尔的感觉。"
    pause 0.1 hard
    scene set only xfe_cg happy
    with dissolve
    play voice "voice/希菲尔/001400190.ogg"
    xfe "希菲尔无论何时也都想和凉君一起玩的。"
    me01 "这次是称呼自己为“希菲尔”了吗？"
    pause 0.1 hard
    scene set only xfe_cg normal
    with dissolve
    play voice "voice/希菲尔/001400200.ogg"
    xfe "凉君你对叫作“希菲尔”的希菲尔，和叫作“我”的希菲尔，更喜欢哪一个？"
    me01 "有什么区别吗？"
    play voice "voice/希菲尔/001400210.ogg"
    xfe "叫“希菲尔”的时候是什么感觉？"
    me01 "很可爱的感觉？"
    pause 0.1 hard
    scene set only xfe_cg happy
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001400220.ogg"
    xfe "很像“雪”一般的感觉？"
    me01 "差不多就是这样的。"
    pause 0.1 hard
    scene set only xfe_cg normal
    with dissolve
    play voice "voice/希菲尔/001400230.ogg"
    xfe "那叫“我”的时候又是什么感觉？"
    me01 "也是很有希菲尔风格的感觉。"
    pause 0.1 hard
    scene set only xfe_cg daze
    with dissolve
    play voice "voice/希菲尔/001400240.ogg"
    xfe "但是......“希菲尔”和“我”是不一样的。"
    me01 "这是怎么回事？"
    me01 "这两个称呼所指的不都是希菲尔你本人吗？"
    play voice "voice/希菲尔/001400250.ogg"
    xfe "虽然是这样，但也不只是这样的。"
    pause 0.1 hard
    scene set only xfe_cg angry
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001400270.ogg"
    xfe "凉君你觉得自己......没有改变吗？"
    play voice "voice/希菲尔/001400280.ogg"
    xfe "这次也是......又要选择放弃吗？"
    play voice "voice/希菲尔/001400290.ogg"
    xfe "像这样轻易地......接受与某人的离别吗？"
    play voice "voice/希菲尔/001400300.ogg"
    xfe "就像当初和希菲尔分别的时候一样......"
    me01 "我当然也不想分开的。"
    me01 "毕竟希菲尔对我来说也是非常重要的伙伴。"
    pause 0.1 hard
    scene set only xfe_cg normal
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001400340.ogg"
    xfe "但是......不只是这样的。"
    play voice "voice/希菲尔/001400350.ogg"
    xfe "现在值得凉君在意的人，不只是希菲尔。"
    play voice "voice/希菲尔/001400360.ogg"
    xfe "已经......不再只有希菲尔一个了。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/001400370.ogg"
    xfe "在凉君的身边有家人。"
    play voice "voice/希菲尔/001400380.ogg"
    xfe "有朋友在。"
    play voice "voice/希菲尔/001400390.ogg"
    xfe "也许还有恋人在。"
    pause 1.0 hard
    scene set only xfe_cg daze
    with dissolve
    play voice "voice/希菲尔/001400400.ogg"
    xfe "虽然希菲尔我还不懂得爱情。"
    play voice "voice/希菲尔/001400410.ogg"
    xfe "但是家人和朋友的话，还是能够明白的。"
    pause 0.1 hard
    scene set only xfe_cg normal
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001400420.ogg"
    xfe "所谓的家人，就算离得再远也还是家人。"
    play voice "voice/希菲尔/001400430.ogg"
    xfe "凉君的家人，是不会阻止凉君继续前进的。"
    play voice "voice/希菲尔/001400440.ogg"
    xfe "凉君的家人，是会默默地在背后推凉君一把的。"
    play voice "voice/希菲尔/001400450.ogg"
    xfe "希菲尔也是......一样的。"
    play voice "voice/希菲尔/001400460.ogg"
    xfe "对希菲尔而言，凉君是非常非常重要的人。"
    play voice "voice/希菲尔/001400470.ogg"
    xfe "对希菲尔来说的凉君一直都没有改变。"
    play voice "voice/希菲尔/001400480.ogg"
    xfe "想要一起玩耍的回忆也都没有改变。"
    play voice "voice/希菲尔/001400490.ogg"
    xfe "一直都不希望它......有所改变。"
    play voice "voice/希菲尔/001400510.ogg"
    xfe "一直希望两人的足迹能够这样永远地延续下去。"
    play voice "voice/希菲尔/001400520.ogg"
    xfe "但是同时，希菲尔也明白了......改变是必须的。"
    pause 0.1 hard
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/001400570.ogg"
    xfe "因为对现在的凉君而言，即使真的迎来了春天，也一定不会再孤单了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    play sound xiaoshi_1
    with slowerdissolve
    pause 2.0 hard

label day219.balltower_event02:
    $ flcam.move(0, 0, 0)
    play ambience1 zhong_rill fadein 3.0
    scene set only balltower day big
    with slowdissolve
    pause 3.0 hard
    "随着钟声的响起，希菲尔的身影消失了。"
    "伴随着一起消失的还有这场雪。"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_n4 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/琉璃/041405050.ogg"
    liuli "神野前辈。"
    play music second_124 fadein 3.0 if_changed
    play voice "voice/琉璃/041405060.ogg"
    liuli "有件事今天必须告诉你，所以我才会来这里。"
    "有些不对劲。"
    "乍一看没什么，但是总觉得哪里怪怪的。"
    "和刚刚在学校见到的琉璃有些不同。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_n3 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041405070.ogg"
    liuli "再过不久我就要离开雪见市了，学校的生活也会随之结束。"
    play voice "voice/琉璃/041405080.ogg"
    liuli "今后已经没有办法......再和前辈见面了。"
    me01 "我们之前不是说好不讲这些寂寞的话吗？"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n4 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041405090.ogg"
    liuli "我要说的就是这些。"
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_n4 at walkout_r(0.3)
    pause 0.5 hard
    hide liuli_dsf_b2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "等等，琉璃......"
    play sound touch
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    "我追了上去。"
    "从背后抓住了她的肩膀。"
    $ flcam.move(4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    play voice "voice/琉璃/041405100.ogg"
    liuli "请不要碰我。"
    stop music fadeout 5.0
    pause 0.5 hard
    play sound rune1
    show wflash onlayer texture
    with vpunch
    pause 0.5 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, -100, 400)
    scene set only balltower snow day xuejian2
    with right2left
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    with vpunch
    pause 0.5 hard
    play music second_123 fadein 3.0 if_changed
    "刚刚的......是什么？"
    "一股无形的冲击突然将我的身体弹开了。"
    "不同于我的{rb}念动立场{/rb}{rt}psychokinesis{/rt}，完全没有感受到念波的存在。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    me01 "刚刚那个......是琉璃你做的吗？"
    "与迄今为止处理过的{rb}灵继者{/rb}{rt}elfin{/rt}暴走不同。"
    "刚刚的冲击很明显是被恰到好处地操控着，没有多余的波及。"
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n3:
        0.75
        easein 1.25 alpha 0.0
    pause 4.0 hard
    hide liuli_dsf_b1
    "就在我企图弄清楚一切的时候，琉璃的身影消失了。"
    "与雷亚还有希菲尔消失的时候一样。"
    "不对，琉璃的确是实实在在的普通人。"
    "至少这一点我可以确信。"
    "不同于希菲尔和雷亚，单从可以上学以及能够自由地出现在大众视线中这一点来看，很明显琉璃没有被特定的羁绊所束缚。"
    "从她刚刚的反应来看，一定是发生了什么事情。"
    "简直就像——"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge day xuejian
    show sepiagrain onlayer texture
    $ flcam.move(2250, 0, 750, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show szl_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    show liuli_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051100250.ogg"
    szl "没时间了，你快去点去研究所吧。"
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
    szl "即便是百般祈求，也终究是无法成为人类。"
    hide szl_dzf_b3
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b1 b1 b1_s1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    pause 0.5 hard
    $ flcam.move(2250, -200, 600, duration=1.5)
    show szl_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
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
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian2
    with dissolve
    pause 1.0 hard
    "虽然没有明白当时水之濑口中那段话的意思。"
    "但是从刚刚琉璃的反应来看和那次简直一模一样。"
    "也就是说星天宫那边也对琉璃做了什么手脚。"
    "看来也只能去问当事人才能了解真相了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day219_balltower_event01:
        $ seen_day219_balltower_event01 = True
    $ _overworld_label = 'day219.balltower_event02'
    jump day219.map

label day219.home_event01:
    default seen_day219_call = False
    $ flcam.move(0, 0, 0)
    scene set only home day passwalk xuejian
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
            move _("外出") jump day219.moveout_event01
            screen_direction left
        call yj_dsf_b1 jump day219.call_yj:
            sensitive (not seen_day219_call)

label day219.call_yj:
    $ seen_day219_call = True
    hide xz_dsf_b3
    $ flcam.move(3800, -400, 800, duration=1.5)
    pause 1.0 hard
    show callflash onlayer texture
    pause 3.0 hard
    hide callflash
    investigation call block yj_dsf_b1 b1 b1_n1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction rights
    nvl clear
    play music second_102 fadein 3.0 if_changed
    show yj_dsf_b1 b1 b1_n1
    play voice "voice/植澄友加/021400010.ogg"
    c.yj_dsf_b1 "好久不见了凉君。"
    c.me01 "抱歉，突然打电话给你。"
    c.me01 "有件事情无论如何都想请你帮个忙。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/021400020.ogg"
    c.yj_dsf_b1 "毕竟凉君你的声音听起来好像很着急的样子。"
    c.me01 "因为是很重要的事情。"
    show yj_dsf_b1 b1 b1_h1
    play voice "voice/植澄友加/021400040.ogg"
    c.yj_dsf_b1 "难不成是你迫不及待想见我了吗~"
    c.me01 "很遗憾，并不是这样的。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/021400050.ogg"
    c.yj_dsf_b1 "真过分啊，这种时候就算不是也应该承认的吧......"
    c.me01 "抱歉。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/021400060.ogg"
    c.yj_dsf_b1 "不、不需要道歉啦，凉君你有点奇怪啊。"
    c.me01 "其实是研究所那边有些事情让我很在意。"
    c.me01 "所以......"
    show yj_dsf_b1 b1 b1_h1
    play voice "voice/植澄友加/021400100.ogg"
    c.yj_dsf_b1 "那走吧，一起去把姐姐干掉~"
    c.me01 "谢谢你友加。"
    investigation call end
    stop music fadeout 5.0
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -100, 400, duration=3.0)
    pause 0.5 hard
    jump investigate

label day219.moveout_event01:
    if not seen_day219_call:
        window mode thought
        me01 "在出发之前先通知友加吧。"
        $ flcam.move(0, -100, 400, duration=3.0)
        pause 0.5 hard
        jump investigate
    stop music fadeout 5.0
    pause 1.0 hard
    hide xz_dsf_b3
    $ flcam.move(0, -100, 400, duration=1.5)
    scene black
    with slowdissolve
    pause 2.0 hard
    if not seen_day219_home_event01:
        $ seen_day219_home_event01 = True
    $ _overworld_label = 'day219.home_event01'
    jump day219.map

label day219.laboratory_event02:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside1 xuejian
    play music second_102 fadein 3.0 if_changed
    $ flcam.move(2250, -350, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.5
    show szl_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400400.ogg"
    szl "......"
    play voice "voice/千川老师/141400390.ogg"
    qcls "神野同学和主任的......"
    $ flcam.move(0, -200, 600, duration=1.5)
    show yj_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400150.ogg"
    yj "......为什么你们也在这里？"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051400410.ogg"
    szl "这是我们的台词吧。"
    hide qcls_zf_b1
    hide yj_dsf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_n4
    play voice "voice/水之濑/051400420.ogg"
    szl "神野君你找主任有什么事吗？"
    me01 "是关于琉璃的事情。"
    show szl_dsf_b2 b2 b2_sp1
    play voice "voice/水之濑/051400430.ogg"
    szl "花山院......说起来今天确实没见到她，出什么事了？"
    me01 "刚刚我们在钟楼广场见面了。"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400440.ogg"
    szl "......你们的关系已经到这一步了吗。"
    me01 "不是你想的那样。"
    me01 "我想说的是今天琉璃的状况很奇怪。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show qcls_zf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.5
    show yj_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400160.ogg"
    yj "那个......花山院今天的状态是？"
    me01 "非常的冷淡，就好像是机器一般。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400450.ogg"
    szl "......"
    me01 "我在想如果是你们的话应该知道些什么。"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/051400460.ogg"
    szl "我先回去了。"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051400470.ogg"
    szl "是我没兴趣的话题......连打发时间都算不上。"
    pause 0.5 hard
    play sound jiaobu2
    show szl_dsf_b2 b2 b2_s1 at walkout_r(0.7)
    pause 1.0 hard
    hide szl_dsf_b2
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141400400.ogg"
    qcls "......植澄同学。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141400410.ogg"
    qcls "今后你也许会从你姐姐那里了解到一些事情，但无论如何还请你不要因此责怪她。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/021400170.ogg"
    yj "哈......"
    pause 0.5 hard
    play sound jiaobu2
    show qcls_zf_b1 b1 b1_s2 at walkout_r(0.5)
    pause 1.0 hard
    hide qcls_zf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "她们会这样选择离开，十有八九是知道其中的原因了。"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_ga3 onlayer m2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/植澄友加/021400320.ogg"
    yj "凉君你在这里等一下，我马上就去通知姐姐。"
    pause 0.5 hard
    play sound jiaobu4
    show yj_dsf_b2 b2 b2_ga3 at walkout_r(0.3)
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard

label day219.laboratory_event03:
    $ flcam.move(0, 0, 0)
    play sound open_door4
    scene set only laboratory inside2 xuejian
    with dissolve
    pause 0.5 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_ga1 onlayer m1:
        xpos 0.5
    play voice "voice/圣护院/151401640.ogg"
    shy "今天客人还真多啊。虽然水之濑和千川是我叫来的就是了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400330.ogg"
    yj "姐姐，你们刚才说了些什么吗？"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151401650.ogg"
    shy "都是工作上的事情，和你没关系。"
    hide yj_dsf_b1 with None
    pause 0.1 hard
    show yj_dsf_b3 b3 b3_ga1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021400340.ogg"
    yj "......"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151401660.ogg"
    shy "反正你来无非就是看我有没有按时吃饭的吧？"
    hide yj_dsf_b3
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400350.ogg"
    yj "虽说是这样没错......那姐姐你午饭有好好吃吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401670.ogg"
    shy "你还真是为了这个特地跑一趟啊。"
    show yj_dsf_b1 b1 b1_s3
    play voice "voice/植澄友加/021400360.ogg"
    yj "当然这点也想问清楚的......"
    hide yj_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151401680.ogg"
    shy "神野君。"
    play voice "voice/圣护院/151401690.ogg"
    shy "有事的是你吧？友加只是你为了防止我拒见才叫来的不是吗。"
    me01 "不愧是您。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401700.ogg"
    shy "从时机考虑也只能是这样的结论了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play sound touch
    scene set only shy_cg one
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/151401710.ogg"
    shy "神野君......你很幸运啊。"
    me01 "此话怎讲？"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/151401720.ogg"
    shy "我指的是认识友加这件事，多亏了她你才能像现在这样和我面对面说话。"
    play voice "voice/圣护院/151401730.ogg"
    shy "缘分是很不可思议的东西，总让人觉得仿佛有命运的存在一般。"
    pause 0.1 hard
    scene set only shy_cg three
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/151401740.ogg"
    shy "你能与友加相识真是太好了。"
    play voice "voice/圣护院/151401750.ogg"
    shy "我能与你相识，也算是幸运的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400370.ogg"
    yj "为什么姐姐也是？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_n2 onlayer m1:
        xpos 0.5
    play voice "voice/圣护院/151401760.ogg"
    shy "因为我对{rb}灵继者{/rb}{rt}elfin{/rt}是怀有敬意的。"
    hide yj_dsf_b3
    show yj_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400380.ogg"
    yj "是这样啊，那对我也是喽~"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151401770.ogg"
    shy "只有你是个例外，你是我的妹妹。这点是无论如何都不会改变的。"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400390.ogg"
    yj "我是该高兴还是别的......好微妙啊。"
    hide yj_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151401790.ogg"
    shy "神野君，稍微给我一点时间，我有话想先对友加说。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151401800.ogg"
    shy "之所以会这样安排，是因为你想问的事情也很难简单地解释清楚。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400410.ogg"
    yj "什么事情？"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151401820.ogg"
    shy "神野君，这样可以吗？"
    hide yj_dsf_b2 with None
    pause 0.1 hard
    show yj_dsf_b3 b3 b3_ga1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021400420.ogg"
    yj "被无视了......"
    me01 "只要能解答我的问题，等多久我都愿意。"
    hide yj_dsf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151401840.ogg"
    shy "这点不用担心，你想问的是花山院的事情吧？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401850.ogg"
    shy "花山院想必也已经正式向你道别了吧。"
    play voice "voice/圣护院/151401860.ogg"
    shy "在此之前，我正好也和她见过面。"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151401870.ogg"
    shy "所以你今天来的时候，我大概也能够察觉到你的来意。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151401880.ogg"
    shy "看来花山院她对你的执念还是很深的。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151401890.ogg"
    shy "相对的，你对她的影响也是如此。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400430.ogg"
    yj "那、那个，花山院的事情是？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401900.ogg"
    shy "友加......包括这个原因在内，我有话想跟你说。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151401910.ogg"
    shy "其实我原本是打算回家后再慢慢跟你说的。"
    play voice "voice/圣护院/151401920.ogg"
    shy "不对......也许只是因为我一直没有找到合适的时机也说不定。"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400440.ogg"
    yj "是很难开口的事情吗？"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151401930.ogg"
    shy "是啊，这样犹豫一点都不像我的风格。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with slowdissolve
    pause 1.0 hard
    "之后我们从圣护院小姐的口中得知了星天宫即将开展的行星探测计划。"
    "为了计划的顺利进行，她和琉璃必须前往人工岛——库洛诺斯的研究基地。"
    "而此刻离出发也只剩不到一周的时间了。"
    pause 1.0 hard
    scene set only laboratory inside2 xuejian
    $ flcam.move(-2250, -350, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    show shy_yjf_b1 b1 b1_s1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/021400450.ogg"
    yj "姐姐马上也要换工作了吗？"
    show shy_yjf_b1 b1 b1_n3
    play voice "voice/圣护院/151401950.ogg"
    shy "是的。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/021400470.ogg"
    yj "我也马上就要转学了。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401970.ogg"
    shy "......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151401980.ogg"
    shy "由你自己决定，要跟着我还是留在这里。"
    play voice "voice/圣护院/151401990.ogg"
    shy "没必要马上做决定，虽然没有太多的时间但让你考虑的话还是绰绰有余的。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/021400500.ogg"
    yj "姐姐你......希望我怎么做？"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151402000.ogg"
    shy "我不是说了由你自己决定吗。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151402010.ogg"
    shy "你的未来应该由你自己把握，我没有插嘴的余地。"
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/021400510.ogg"
    yj "......"
    play voice "voice/植澄友加/021400520.ogg"
    yj "姐姐想要对我说的就是这件事吗？"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151402020.ogg"
    shy "是啊，之后就是神野君的事情了。"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400530.ogg"
    yj "那我先回去了......"
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400540.ogg"
    yj "对不起凉君，临阵脱逃了。"
    me01 "没事的，需要我送你吗？"
    show yj_dsf_b1 b1 b1_n2
    play voice "voice/植澄友加/021400550.ogg"
    yj "凉君不是还要和姐姐讨论花山院的事情吗？"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400560.ogg"
    yj "这才是最重要的，我就不打扰了。"
    me01 "对我来说友加的事情也同样很重要。"
    hide yj_dsf_b2
    show yj_dsf_b3 b3 b3_n3 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400570.ogg"
    yj "因为我们是朋友吧，但是花山院不一样吧。"
    me01 "琉璃也是我的朋友，所以你们是一样的。"
    show yj_dsf_b3 b3 b3_ga1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021400580.ogg"
    yj "凉君你真是一个天然的负心汉。"
    hide yj_dsf_b3
    show yj_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021400590.ogg"
    yj "我想一个人考虑一下，虽然不擅长但总觉得必须尝试一下。"
    show yj_dsf_b2 b2 b2_s2
    play voice "voice/植澄友加/021400600.ogg"
    yj "所以，回去的话我一个人就行了。"
    me01 "抱歉友加......没能帮上忙。"
    show yj_dsf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/021400610.ogg"
    yj "没有的事，光是你说要送我回去这一点我就已经很开心了。"
    pause 0.5 hard
    play sound close_door4
    show yj_dsf_b2 b2 b2_h1 at walkout_l(0.3)
    pause 0.5 hard
    hide yj_dsf_b2
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151402040.ogg"
    shy "那么我们继续刚才的话题吧。我这里也没那么闲的，负心汉君。"
    me01 "......怎么连主任你也这样说？！"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151402050.ogg"
    shy "是啊，毕竟友加回去之后绝对会大哭一场的吧。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151402060.ogg"
    shy "然后我回去或许也会被她大骂一顿。"
    me01 "为什么不告诉她您的真实想法呢？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151402070.ogg"
    shy "那是因为最后做决定的是还是她自己。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151402080.ogg"
    shy "是要离开雪见市还是留下来，我不打算剥夺她选择的权利。"
    me01 "既然这样的话琉璃也有选择去留的权利吧？"
    show shy_yjf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/圣护院/151402090.ogg"
    shy "......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play sound touch
    scene set only shy_cg two
    with slowdissolve
    pause 1.0 hard
    play voice "voice/圣护院/151402100.ogg"
    shy "没有。"
    stop music fadeout 5.0
    play voice "voice/圣护院/151402110.ogg"
    shy "花山院的情况不一样，对于我们所进行的下一项计划而言她的存在是不可或缺的。"
    play voice "voice/圣护院/151402120.ogg"
    shy "这不是以一个人的意志就能改变的东西。"
    play voice "voice/圣护院/151402130.ogg"
    shy "行星探测......就是这么庞大的计划。"
    play music second_125 fadein 3.0 if_changed
    "行星探测......"
    "这种只在电视上看过的东西，没想到会与自己身边的人有关系。"
    "我现在才开始体会到当初{rb}梦{/rb}{rt}量子态翔子{/rt}对我提到的宇宙探测。"
    "从她对我说明的那些内容可以看出。"
    "这些确实对于人类而言具有非常神圣的意义。"
    pause 0.1 hard
    scene set only shy_cg four
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/151402140.ogg"
    shy "我一开始就说过，你跟友加相识是幸运的事情。"
    play voice "voice/圣护院/151402150.ogg"
    shy "但是，你和花山院的相识又是怎样的呢？"
    play voice "voice/圣护院/151402160.ogg"
    shy "是幸运呢，还是不幸呢？"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/151402170.ogg"
    shy "就现在情况来看，也许是不幸吧。"
    me01 "我不认为光凭相遇的时机能够决定两个人的命运。"
    me01 "更何况我和琉璃的相遇更像是某种机缘的安排。"
    me01 "我们有着共同的命运，我们......都曾是离群的孩子。"
    me01 "请告诉我，琉璃她什么时候会离开这座城市？"
    pause 0.1 hard
    scene set only shy_cg five
    with dissolve
    play voice "voice/圣护院/151402180.ogg"
    shy "这个月就会出发吧。"
    me01 "宇宙中心的具体位置呢？"
    pause 0.1 hard
    scene set only shy_cg four
    with dissolve
    play voice "voice/圣护院/151402190.ogg"
    shy "虽然住所和联系方式我可以告诉你，但是知道这些的你又能做什么？"
    me01 "我会抽空去看她。就算离开了雪见市，我们也一定还能再见面的。"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/151402200.ogg"
    shy "这点应该是不可能的。"
    pause 0.1 hard
    scene set only shy_cg four
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/151402210.ogg"
    shy "也正因如此花山院才会狠心与你“告别”。"
    play voice "voice/圣护院/151402220.ogg"
    shy "因为她也清楚你们之间，已经再无相见的可能了。"
    play voice "voice/圣护院/151402230.ogg"
    shy "即使运气好能够见到，那大概也得等上四五年的时间吧。"
    me01 "怎么会这样......"
    play voice "voice/圣护院/151402240.ogg"
    shy "我说过的吧，花山院的情况是不一样的，这不是转学而是退学。"
    play voice "voice/圣护院/151402250.ogg"
    shy "她已经不能再继续过正常人的生活，项目试验的阶段也已经通过了。"
    play voice "voice/圣护院/151402260.ogg"
    shy "花山院今后会作为载人行星探测的对象而拼尽全力，已经不可能会有时间跟你见面了。"
    me01 "载人......行星探测？"
    me01 "琉璃她......会前往宇宙吗？"
    play voice "voice/圣护院/151402270.ogg"
    shy "......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151402280.ogg"
    shy "真是的......"
    play voice "voice/圣护院/151402290.ogg"
    shy "要是你能简单地放弃我也能轻松些，都说了我可没那么闲。"
    me01 "虽然很抱歉，但是......"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151402300.ogg"
    shy "但是你并不打算就这么放弃对吧？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151402310.ogg"
    shy "我希望你能理解我的立场，这里已经不能再给你透露更多的信息了。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151402380.ogg"
    shy "你此刻无法接受的心情我也不是不能理解。"
    me01 "琉璃也是这么选择的吗？"
    me01 "即使表面上接受了，但其实她的内心是否真的认同这项任务呢？"
    me01 "就在刚刚琉璃不惜使用{rb}灵纹{/rb}{rt}rune{/rt}也想要与我诀别。"
    me01 "明明之前她答应过我的，答应我绝对不再说那些会让人寂寞的话。"
    me01 "但是现在......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151402410.ogg"
    shy "花山院她对你采取了这样的行动吗？"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151402460.ogg"
    shy "正如你想的那样，她应该也是想要彻底斩断对你的留恋吧。"
    play voice "voice/圣护院/151402470.ogg"
    shy "为了说服自己离开这座城市。"
    play voice "voice/圣护院/151402480.ogg"
    shy "那个所谓的“留恋”一定就和你有关吧。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151402540.ogg"
    shy "至今为止，花山院的所有行动都会向我汇报。"
    play voice "voice/圣护院/151402550.ogg"
    shy "但是你刚刚说的事情我却完全不知情。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151402560.ogg"
    shy "今天一整天她也没有向我汇报具体的去向。"
    play voice "voice/圣护院/151402570.ogg"
    shy "与你有关的事她都对我隐瞒了，至今为止这样的事情应该已经发生过很多次了。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151402580.ogg"
    shy "就像思春期少女一般的行为，犹豫着袒护自己喜欢的人。"
    stop music fadeout 5.0
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151402590.ogg"
    shy "也许你的存在对她来说，就是如此的重要。"
    pause 1.0 hard
    play music second_138 fadein 3.0 if_changed
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "呐，琉璃......"
    "曾经的我也轻易地接受了与某人离别的命运。"
    "但是后来我才发现，如果当初能够勇敢些。"
    "哪怕只是稍微挣扎片刻，也许就能够守住那份珍贵的美好了。"
    "命运从我这里夺走的东西，我不希望在你那里也被夺走。"
    "所以这次。"
    "就让我来帮你。"
    "就让我......来帮你回忆起那些想说，却又没机会说出的话吧。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only laboratory inside2 xuejian
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    with dissolve
    me01 "我还有最后一个问题，可以吗？"
    play voice "voice/圣护院/151403660.ogg"
    shy "是什么？"
    me01 "为什么星天宫这么执着于利用{rb}灵继者{/rb}{rt}elfin{/rt}进行宇宙开发呢？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151403670.ogg"
    shy "是气象研究经验的缘故吧。姑且不论本部那边，这座研究所从事的项目至今为止一直没有什么重大的进展。"
    me01 "所以想要借助{rb}灵继者{/rb}{rt}elfin{/rt}来突破瓶颈吗？"
    play voice "voice/圣护院/151403690.ogg"
    shy "最终能做到什么程度，说实话连我们自己也无法估量。"
    me01 "这是什么意思？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151403700.ogg"
    shy "忘了刚才的话吧，我也不能透露更多了。"
    me01 "虽然很感谢您能抽空解答我的问题，但是琉璃那边我也不打算让步。"
    me01 "既然圣护院小姐也说了让友加自己决定去留。"
    me01 "那么相对的我也会让琉璃她自己决定今后的人生。"
    me01 "这才是身为朋友的我应该做的。"
    me01 "也是我唯一......能为她做的事了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day219_laboratory_event02:
        $ seen_day219_laboratory_event02 = True
    $ _overworld_label = 'day219.laboratory_event02'
    jump day219.map

label day219.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only bridge evening under xuejian alpha
    play music second_129 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041406680.ogg"
    liuli "马上就要入夜了......"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041406690.ogg"
    liuli "从我离开研究所开始，也已经过了很长的时间。"
    show liuli_dsf_b1 b1 b1_s3
    play voice "voice/琉璃/041406700.ogg"
    liuli "前辈现在在做什么呢......虽然中午的时候才见面的。"
    play voice "voice/琉璃/041406720.ogg"
    liuli "大概是去研究所了吧......"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041406730.ogg"
    liuli "圣护院小姐会告诉他吗，前辈他已经知道真相了吗。"
    show liuli_dsf_b1 b1 b1_s3
    play voice "voice/琉璃/041406740.ogg"
    liuli "......我的身份。"
    show liuli_dsf_b1 b1 b1_c1
    play voice "voice/琉璃/041406800.ogg"
    liuli "明明不希望这样的。"
    play voice "voice/琉璃/041406850.ogg"
    liuli "明明不应该是这样的，前辈......"
    play voice "voice/琉璃/041406860.ogg"
    liuli "这一切都是你的错。"
    show liuli_dsf_b1 b1 b1_s3
    play voice "voice/琉璃/041406870.ogg"
    liuli "是你让我产生动摇。"
    play voice "voice/琉璃/041406880.ogg"
    liuli "过去也好现在也罢，一直一直......在动摇着我。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041406890.ogg"
    liuli "是你让我渐渐开始回想起来。"
    show liuli_dsf_b1 b1 b1_s3
    play voice "voice/琉璃/041406900.ogg"
    liuli "那本该已经抛弃了的......感情。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041406910.ogg"
    liuli "本已经不再需要的那颗心。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg center normal
    show sepiagrain onlayer fg
    with dissolve
    "我也想一直这样，和前辈坐在中庭的长椅上喝着自己最喜欢的饮料。"
    "向前辈介绍雪见市的天气变化。"
    pause 0.1 hard
    scene set only liuli_cg center happy
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "那时候的我也许不曾怀疑过。"
    "甚至是如此地坚信着。"
    "这一切的可能性......"
    pause 1.0 hard
    hide sepiagrain
    scene white 
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg city two
    show sepiagrain onlayer fg
    with dissolve
    "就算不在学校里，我们也会手挽着手一起去逛商店街。"
    "那时候的我一定是发自内心地快乐着吧。"
    pause 1.0 hard
    hide sepiagrain
    scene white
    with slowerdissolve
    pause 2.0 hard
    scene set only liuli_cg tower one
    show sepiagrain onlayer fg
    with dissolve
    play voice "voice/琉璃/041406920.ogg"
    liuli "前辈......"
    play voice "voice/琉璃/041406930.ogg"
    liuli "和你一起在这座电波塔上仰望星空时的我，是怎样一副表情的呢？"
    play voice "voice/琉璃/041406940.ogg"
    liuli "是像人类一样充满热情的吗？"
    play voice "voice/琉璃/041406950.ogg"
    liuli "还是说......是像机器一样冷漠的呢？"
    play voice "voice/琉璃/041406960.ogg"
    liuli "再过不了多久，我就会向着你最爱的那片星之海洋独自踏上旅途。"
    pause 0.1 hard
    scene set only liuli_cg tower three
    with dissolve
    play voice "voice/琉璃/041406970.ogg"
    liuli "虽然从地面上能看到的星光都很明亮，但实际上它们的距离却是相当的遥远。"
    play voice "voice/琉璃/041406980.ogg"
    liuli "星星与星星之间，弥漫着能让人窒息的广阔黑暗。"
    pause 0.1 hard
    scene set only liuli_cg tower one
    with dissolve
    play voice "voice/琉璃/041406990.ogg"
    liuli "星星......是孤独的。"
    play voice "voice/琉璃/041407000.ogg"
    liuli "所以宇宙也一定是非常黑暗且寒冷的。"
    play voice "voice/琉璃/041407010.ogg"
    liuli "独自旅行的我不得不忍受好几年这样的孤独。"
    pause 0.1 hard
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/琉璃/041407020.ogg"
    liuli "所以我是不需要感情的。"
    play voice "voice/琉璃/041407030.ogg"
    liuli "会在孤独中感到寂寞的心......是不需要的。"
    play voice "voice/琉璃/041407040.ogg"
    liuli "这样一定......才是正确的。"
    play voice "voice/琉璃/041407050.ogg"
    liuli "对我来说也好，对星天宫的大家来说也好。"
    pause 1.0 hard
    hide sepiagrain
    $ flcam.move(0, 0, 900)
    scene set only bridge evening under xuejian alpha
    show snow_level1 onlayer fg
    show liuli_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407070.ogg"
    liuli "前辈、神野前辈。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041407090.ogg"
    liuli "不能动摇......我必须接受这一切。"
    play voice "voice/琉璃/041407100.ogg"
    liuli "所以我希望你也是如此。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with dissolve
    pause 1.0 hard
    show liuli_dsf_b1 b1 b1_s3 onlayer screens at side_left('liuli'), basicfade
    play voice "voice/琉璃/041407110.ogg"
    liuli "希望你也能像这片天空尽头的宇宙那般，冷漠、无情地目送我离去。"
    hide liuli_dsf_b1
    "泪水从琉璃的眼角滑落。"
    "白色的结晶纷然飘下。"
    "此刻那温柔而又寂寞的雪，再一次降临了这座城市——"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve

label day219.battle_liuli:
    pause 2.0 hard
    "命运是什么？"
    "在它面前人真的......无力反抗吗？"
    "如果生下来注定是以悲剧收场，那我们还会像这样努力地改变自己吗？"
    "照这样来看，人无法窥探命运这件事是上天给予我们的一种仁慈吗？"
    "就因为看不到未来，我们才会天真地想要为美好而努力。"
    "如果当初那位——企图以全世界为敌的天使大人能够知道自己发动战争的后果，她还会选择这么做吗？"
    "如果当时星天宫的成立不是巧合，而是早已注定了的，还会有那么多无辜的{rb}灵继者{/rb}{rt}elfin{/rt}遭受苦难吗。"
    "如果我与雷亚、梦以及希菲尔的相遇是一开始就注定了的，我还会那样地珍惜彼此的羁绊吗？"
    "难道我们真的只要顺从命运的安排就可以了吗。"
    "是啊，经历了那么多，我的答案始终只有一个。"
    "那就是......"
    pause 1.0 hard
    scene set only bridge evening under xuejian
    show snow_level1 onlayer fg
    play music second_138 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    me01 "{size=72}我拒绝！{/size}"
    show liuli_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407120.ogg"
    liuli "前辈？"
    show liuli_dsf_b1 b1 b1_s2
    play voice "voice/琉璃/041407130.ogg"
    liuli "为什么......你会在这里？"
    me01 "琉璃，不管你是不是为了人类的未来，我都不会接受现在这样的离别。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041407140.ogg"
    liuli "......"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407150.ogg"
    liuli "我就猜到说不定会是这样的。"
    $ flcam.move(0, 0, 1000, duration=1.5, warper='ease_cubic')
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_s3
    play voice "voice/琉璃/041407160.ogg"
    liuli "说实话前辈会不会来我自己也没有把握。"
    play voice "voice/琉璃/041407170.ogg"
    liuli "毕竟我无法使用{rb}预知未来{/rb}{rt}precognition{/rt}。"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407180.ogg"
    liuli "只是我想如果没来的话也好。"
    show liuli_dsf_b2 b2 b2_s3
    play voice "voice/琉璃/041407190.ogg"
    liuli "那就恰恰说明前辈并没有把与我的分别当作是值得惋惜的事情。"
    show liuli_dsf_b2 b2 b2_s1
    play voice "voice/琉璃/041407200.ogg"
    liuli "那样的话，我也能做好觉悟了。"
    play voice "voice/琉璃/041407210.ogg"
    liuli "冰冷地、如同机器一般地接受和前辈离别的事实。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407220.ogg"
    liuli "而相对的如果前辈真的来了，我也不得不做好觉悟。"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407230.ogg"
    liuli "我不得不对前辈做些更过分的事情！"
    show liuli_dsf_b2 b2 b2_s3
    play voice "voice/琉璃/041407270.ogg"
    liuli "这样前辈就会愿意从我身边离开。"
    play voice "voice/琉璃/041407290.ogg"
    liuli "我必须要扼杀掉多余的感情。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_c1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407310.ogg"
    liuli "不然的话即使飞向了宇宙，我也一定会因此而无法让计划得以成功。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg fight angry1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407390.ogg"
    liuli "前辈你......做好觉悟了吗？"
    me01 "如果没有觉悟我也不会出现在这里。"
    pause 0.1 hard
    scene set only liuli_cg fight daze1
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407400.ogg"
    liuli "那么为了跨越这道障碍，我现在必须要打倒你。"
    me01 "除此之外已经没有办法阻止你了对吧？"
    pause 0.1 hard
    scene set only liuli_cg fight angry1
    with dissolve
    play voice "voice/琉璃/041407410.ogg"
    liuli "是的，只是言语的话只会让我越来越迷茫。"
    play voice "voice/琉璃/041407420.ogg"
    liuli "我想换作是前辈肯定也不会接受这样的离别方式。"
    me01 "的确如此。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only bridge evening under xuejian
    show snow_level1 onlayer fg
    show liuli_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407450.ogg"
    liuli "就在刚才这座河滩已经被我施加了{rb}视线诱导{/rb}{rt}misdirection{/rt}。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_s3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407460.ogg"
    liuli "前辈没有注意到也是情有可原，因为这是连我自己都很难感知到的{rb}灵纹{/rb}{rt}rune{/rt}。"
    me01 "这么厉害的吗？"
    show liuli_dsf_b3 b3 b3_n2
    play voice "voice/琉璃/041407530.ogg"
    liuli "是的，这可是综合了{rb}念动立场{/rb}{rt}psychokinesis{/rt}和{rb}思维透视{/rb}{rt}telepathy{/rt}，能够操控对方视觉的结界型{rb}灵纹{/rb}{rt}rune{/rt}。"
    play voice "voice/琉璃/041407550.ogg"
    liuli "正因如此对一般人能够很好地发挥作用。"
    me01 "即使不确定我是否会来，却也做了这么多的准备吗？"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041407570.ogg"
    liuli "是的，除此之外我还用{rb}远隔透视{/rb}{rt}clairvoyance{/rt}能力确认过周围的情况。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    play voice "voice/琉璃/041407620.ogg"
    liuli "现在的我眼中，就只有前辈一个人。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg fight sad1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407630.ogg"
    liuli "我已经无法思考除你以外的事情了。"
    play voice "voice/琉璃/041407640.ogg"
    liuli "让我变成这样的是你。"
    play voice "voice/琉璃/041407650.ogg"
    liuli "我不会说让你负责之类的话，毕竟这都是我自身软弱而造成的后果。"
    pause 0.1 hard
    scene set only liuli_cg fight daze1
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407660.ogg"
    liuli "但若前辈能稍微顺从一下我的任性，我会很开心的。"
    play voice "voice/琉璃/041407670.ogg"
    liuli "我希望前辈能堂堂正正地与我较量。"
    play voice "voice/琉璃/041407680.ogg"
    liuli "不要逃避。"
    play voice "voice/琉璃/041407690.ogg"
    liuli "也不要移开视线。"
    pause 0.1 hard
    scene set only liuli_cg fight cry1
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407700.ogg"
    liuli "希望你能好好看着身为人类的我。"
    play voice "voice/琉璃/041407710.ogg"
    liuli "在这之后如果前辈能顺利讨厌我的话。"
    play voice "voice/琉璃/041407720.ogg"
    liuli "若是能被你发自内心地讨厌的话......我就没有遗憾了。"
    play voice "voice/琉璃/041407730.ogg"
    liuli "就能舍弃所有......离开雪见市了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001400070.ogg"
    xfe "凉君......"
    pause 1.0 hard
    scene set only bridge evening xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001400080.ogg"
    xfe "还有......抛弃真心不断勉强着的她。"
    show ts_xfe_yjz_b1 b1 b1_s3
    play voice "voice/希菲尔/001400090.ogg"
    xfe "今天又争执起来了。"
    play voice "voice/希菲尔/001400100.ogg"
    xfe "在迎来春天之前，冲突还是会持续下去的......"
    $ flcam.move(0, 0, 1000, duration=1.5, warper='ease_cubic')
    pause 0.5 hard
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001400110.ogg"
    xfe "不、不是这样的。"
    show ts_xfe_yjz_b2 b2 b2_s3
    play voice "voice/希菲尔/001400120.ogg"
    xfe "人一定是为了迎来春天才选择战斗的——"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001400130.ogg"
    xfe "也正因如此，才会有冬天的不是吗......"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory6
    play music second_128 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001400140.ogg"
    xfe "温柔的雪堆积在人们心上。"
    pause 0.1 hard
    scene set only xfe_cg memory7
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001400150.ogg"
    xfe "然后总有一天......会融化、消失不见。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "天使开始歌唱。"
    "此刻的这座城市，降下了温柔的雪——"
    pause 2.0 hard
    $ flcam.move(0, 0, 900)
    scene set only bridge fight under xuejian
    show snow_level1 onlayer fg
    show liuli_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    with slowdissolve
    pause 0.5 hard
    play voice "voice/琉璃/041407740.ogg"
    liuli "前辈......这次就请你认真地作我的对手。"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    me01 "如你所愿，我会尽全力阻止你的。"
    me01 "只是有件事情你可能误会了。"
    me01 "胜负这种东西可不是为了结束，而是为了开始才存在的东西！"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 1.0 hard
    play sound rune2
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg bridge3
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        ## 初始化参数
        # Boss为花山院琉璃，装备为随机传说6件，等级10，技能满级
        liuli_role_mirror.equip_experience = 99999999
        for cate in lhx_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if ("_04" in outfit.objectname and outfit.category == cate)]
            sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
            sample_outfit = enemy_outfits[sample_index]
            sample_outfit.init_params()
            for xi in range(9):
                sample_outfit.level_up(liuli_role_mirror, 100)
            sample_outfit.enemy_equip_on(liuli_role_mirror)
        for xi in range(20):
            liuli_role_mirror.skill_levelup()

        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

        local_config.tutorial_step = "liuli_day219"

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=liuli_role_mirror, 
                boss_hp_plus=80000,
                side_enemy=[], 
                side_hp_plus=0,
                level=35,
                boss_first=True, 
                win_condition='normal', 
                stay_turn=0, 
                inside_label="inside_battle14", 
                mission_type="normal", 
                treasures={
                    "eggs": (3, 0.6),
                    "mana_eggs": (2, 0.3),
                    "soul_piece": (10, 0.3),
                    "soul_raise": (10, 0.3),
                    "fire_break_small": (8, 0.3),
                    "fire_break_large": (5, 0.3)
                })

    if _return == "win":
        "战斗胜利！"
        python:
            if "liuli_role" not in local_config.role_pool:
                local_config.role_pool.add("liuli_role")
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day219.after_battle_liuli

label day219.after_battle_liuli:
    $ flcam.move(1100, 0, 450)
    scene set only myself_cg four
    play music second_128 fadein 3.0 if_changed
    with dissolve
    show wflash onlayer texture
    with vpunch
    pause 1.0 hard
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "我发动了{rb}念动立场{/rb}{rt}psychokinesis{/rt}，狂风卷起积雪形成了风壁。"
    "琉璃能够使用{rb}空间跳跃{/rb}{rt}teleport{/rt}，因此我才决定采取这样的行动。"
    "要是像与立花希的战斗中那样，从死角被发动攻击就麻烦了。"
    "可是被动防御终归不是长久之计，得想办法进攻才行。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level2 onlayer fg
    with dissolve
    pause 1.0 hard
    "制胜点有两个。"
    "如果是{rb}念动立场{/rb}{rt}psychokinesis{/rt}的正面交锋，毫无疑问是我占优势。"
    "但是不同于水之濑的自尊心，琉璃那种扬长避短的作战风格这点应该很难奏效。"
    "既然如此，那就只能采取另一种办法了。"
    "但是这个办法弄不好会伤害到琉璃。"
    "这也是我最担心的事情。"
    pause 1.0 hard
    hide snow_level2
    scene set only liuli_cg fight angry1
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407770.ogg"
    liuli "用风压制造的屏障吗？"
    play voice "voice/琉璃/041407780.ogg"
    liuli "这样的话的确想用{rb}空间跳跃{/rb}{rt}teleport{/rt}来接近确实很困难。"
    pause 0.1 hard
    scene set only liuli_cg fight daze1
    with dissolve
    play voice "voice/琉璃/041407800.ogg"
    liuli "但是，对我而言这可不能说是个好办法。"
    pause 0.1 hard
    play sound rune3
    scene set only liuli_cg fight angry3
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407810.ogg"
    liuli "还以为前辈也是知道的，真是遗憾~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene white 
    with slowerdissolve
    play ambience1 rell_fire fadein 3.0
    show fight_rune2 onlayer texture
    with in2out_02
    pause 1.0 hard
    "琉璃张开手掌，转眼之间烈焰升腾而起。"
    me01 "{rb}冥火{/rb}{rt}pyrokinesis{/rt}！？"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    scene set only liuli_cg fight angry2
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407840.ogg"
    liuli "话虽如此，火焰也只是虚招罢了。"
    play voice "voice/琉璃/041407860.ogg"
    liuli "我的目的是为了提升空气的温度。"
    pause 0.1 hard
    scene set only liuli_cg fight daze2
    with dissolve
    play voice "voice/琉璃/041407870.ogg"
    liuli "这样一来你制造的风墙也会瓦解。"
    play voice "voice/琉璃/041407880.ogg"
    liuli "{rb}冥火{/rb}{rt}pyrokinesis{/rt}并非只是杀伤型的{rb}灵纹{/rb}{rt}rune{/rt}。"
    pause 0.1 hard
    scene set only liuli_cg fight angry3
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407890.ogg"
    liuli "如果是拥有高水准的话，就连对方的体温都可以随意操纵。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene white 
    with slowerdissolve
    show fight_rune2 onlayer texture
    with in2out_02
    pause 1.0 hard
    "热浪渐渐袭来，萦绕在周身的吹雪也逐渐减弱了势头。"
    "大致的原理就和上次营救小桃时消除风暴一样。"
    pause 1.0 hard
    play sound rune2
    scene set only myself_cg five
    show fight_rune2 onlayer texture
    with slowdissolve
    pause 1.0 hard
    me01 "即使如此，只要源源不断制造风暴就可以了吧！"
    "意料之外地进入到了第一个制胜点的节奏中来。"
    "那么接下来就是灵力之间的对决了。"
    "最终将以一方率先支撑不住而告终。"
    pause 1.0 hard
    scene set only liuli_cg fight sad2
    show fight_rune2 onlayer texture
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041407900.ogg"
    liuli "前辈你这么做，就已经是在逃避了吧。"
    play voice "voice/琉璃/041407910.ogg"
    liuli "果然从一开始你就没打算和我认真地交手。"
    pause 1.0 hard
    scene set only myself_cg four
    show fight_rune2 onlayer texture
    with dissolve
    pause 1.0 hard
    me01 "......什、什么？"
    "此刻的我发现了异样。"
    "不管怎么发动{rb}念动立场{/rb}{rt}psychokinesis{/rt}，都无法改变周围空气的流动。"
    me01 "你做了什么？"
    pause 1.0 hard
    scene set only liuli_cg fight daze2
    with dissolve
    play voice "voice/琉璃/041407930.ogg"
    liuli "风是随着气压差而产生的。"
    play voice "voice/琉璃/041407940.ogg"
    liuli "而气压差却是由温度决定。"
    pause 0.1 hard
    scene set only liuli_cg fight angry2
    with dissolve
    play voice "voice/琉璃/041407950.ogg"
    liuli "前辈利用{rb}念动立场{/rb}{rt}psychokinesis{/rt}产生的动能来操纵空气的流动。"
    play voice "voice/琉璃/041407970.ogg"
    liuli "如果利用温度的变化为气压加入些许干扰的话，便可以轻松打破空气的流动规律。"
    play voice "voice/琉璃/041407980.ogg"
    liuli "而能够做到这一点的，就是刚刚的{rb}冥火{/rb}{rt}pyrokinesis{/rt}和{rb}接触感应{/rb}{rt}psychometry{/rt}。"
    "利用{rb}接触感应{/rb}{rt}psychometry{/rt}将空气作为{rb}冥火{/rb}{rt}pyrokinesis{/rt}作用的媒介。"
    "在我毫无察觉的情况下改变了周围空气的流向。"
    "如此庞大的计算和工程竟然一下子就完成了。"
    pause 0.1 hard
    scene set only liuli_cg fight daze2
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041408020.ogg"
    liuli "即使前辈不是通过风，而是利用水或者沙土等其他媒介来制作屏障也是没有用的。"
    play voice "voice/琉璃/041408030.ogg"
    liuli "只要跳脱不出物质层面的范畴，就很难抵抗温度的变化。"
    pause 0.1 hard
    scene set only liuli_cg fight angry2
    with dissolve
    play voice "voice/琉璃/041408040.ogg"
    liuli "而且在我所有的{rb}灵纹{/rb}{rt}rune{/rt}中，{rb}冥火{/rb}{rt}pyrokinesis{/rt}是我最擅长的。"
    play voice "voice/琉璃/041408050.ogg"
    liuli "无论是强度还是控制力都要远超前辈的{rb}念动立场{/rb}{rt}psychokinesis{/rt}。"
    pause 0.1 hard
    scene set only liuli_cg fight angry3
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041408060.ogg"
    liuli "要说{rb}灵纹{/rb}{rt}rune{/rt}这种东西，最重要的还是相性匹配原理。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    show liuli_dsf_b1 b1 b1_s3 onlayer screens at side_left('liuli'), basicfade
    play voice "voice/琉璃/041408080.ogg"
    liuli "前辈明明说过自己已经做好了觉悟。"
    play voice "voice/琉璃/041408090.ogg"
    liuli "可我更多地却只是看到了你的犹豫不决。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041408100.ogg"
    liuli "所以才会像现在这样......做出了错误的判断不是吗？"
    hide liuli_dsf_b1
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play sound touch
    "背部突然传来一阵温柔的触感。"
    play music second_130 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg fight end1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041408110.ogg"
    liuli "现在不是前辈应该感到惊讶的时候。"
    play voice "voice/琉璃/041408120.ogg"
    liuli "就不该把视线从我身上移开的。"
    play voice "voice/琉璃/041408130.ogg"
    liuli "不应该继续待在这里，而是在知道自己无法制造风墙的时候就逃走的......"
    play voice "voice/琉璃/041408140.ogg"
    liuli "所以才会被我用{rb}空间跳跃{/rb}{rt}teleport{/rt}绕到了背后。"
    play voice "voice/琉璃/041408150.ogg"
    liuli "现在只要稍微一下子，我就能打倒前辈了。"
    "雪已经停了。"
    "仿佛在暗示着这场胜负的落幕。"
    "是我......输了。"
    me01 "没想到会是这样的结果。"
    play voice "voice/琉璃/041408160.ogg"
    liuli "都是因为前辈疏忽大意了。"
    me01 "琉璃你从一开始就没觉得会输给我吧。"
    me01 "与其说是因为相性问题，不如说我的败北是一开始就注定的了。"
    me01 "真是讨厌啊。"
    me01 "没想到身为前辈的我会如此地狼狈。"
    play voice "voice/琉璃/041408180.ogg"
    liuli "......那前辈你，有稍微对我感到失望了吗？"
    play voice "voice/琉璃/041408190.ogg"
    liuli "正如我所说，我已经把前辈打得落花流水了。"
    play voice "voice/琉璃/041408200.ogg"
    liuli "我想自己已经是一个非常讨人厌的孩子了。"
    play voice "voice/琉璃/041408210.ogg"
    liuli "所以......只要一句话就够了。"
    play voice "voice/琉璃/041408220.ogg"
    liuli "能对我说一次“我讨厌你”吗？"
    "琉璃与我战斗的理由仅仅是为了这个。"
    "为了斩断对我的执念才做了这样拐弯抹角的事情。"
    "为了解开自己内心的迷茫才选择兵戎相见的。"
    "但是啊琉璃......"
    "如果连你自己也会为此而烦恼，那不就恰恰说明了有“心”吗？"
    "正因为有着身为人类的心，我们才会不由自主地心生好恶。"
    "Indestructibility。"
    "“Indestructibility”——意思是无法磨灭的事物。"
    "身为“自己”的这个个体，是任何人都无法否定的存在。无论是从物理还是哲学上，乃至鬼神都无法做到。"
    "你一直想要抛弃的这颗心，也许就是这样无法被轻易抹去的东西吧......"
    play voice "voice/琉璃/041408230.ogg"
    liuli "只要对我说，你讨厌我的话......"
    play voice "voice/琉璃/041408240.ogg"
    liuli "只要这样......我就会放弃了。"
    me01 "抱歉琉璃，唯独这一点是我无法妥协的。"
    pause 0.1 hard
    scene set only liuli_cg fight end2
    $ flcam.move(0, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    me01 "就算这一次是我输了，我也不会承认的。"
    me01 "无论多少次我都会再向你挑战。"
    me01 "直到打败你为止。"
    me01 "这是我从一开始就决定好的。"
    me01 "我所说的觉悟，指的就是这个。"
    play voice "voice/琉璃/041408280.ogg"
    liuli "为、为什么......"
    pause 0.1 hard
    scene set only liuli_cg fight end1
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041408290.ogg"
    liuli "为什么要说这样欺负人的话。"
    me01 "我只是说了真心话而已。"
    play voice "voice/琉璃/041408340.ogg"
    liuli "过去的“我”并不是真正意义上的我。"
    play voice "voice/琉璃/041408350.ogg"
    liuli "现在的“我”才是真真正正的我！"
    play voice "voice/琉璃/041408360.ogg"
    liuli "放弃身为“人类”的身份，抛弃所有的一切......"
    play voice "voice/琉璃/041408380.ogg"
    liuli "所以......前辈是个大骗子。"
    play voice "voice/琉璃/041408390.ogg"
    liuli "前辈只是......喜欢上那个虚假的“我”而已。"
    me01 "对我来说，过去也好现在也罢，在我眼里的花山院琉璃永远只有一个！"
    pause 0.1 hard
    scene set only liuli_cg fight end3
    with dissolve
    play voice "voice/琉璃/041408400.ogg"
    liuli "不是的。"
    play voice "voice/琉璃/041408410.ogg"
    liuli "喜欢上你的“我”不过只是个孩子！"
    play voice "voice/琉璃/041408420.ogg"
    liuli "还没有做好觉悟......对任何事情都一无所知的孩子而已。"
    play voice "voice/琉璃/041408430.ogg"
    liuli "所以才会喜欢上你。"
    play voice "voice/琉璃/041408440.ogg"
    liuli "正是因为没有接受过别人的我，才会轻易地喜欢上温柔的前辈。"
    play voice "voice/琉璃/041408490.ogg"
    liuli "过去的我对自己使用了{rb}催眠{/rb}{rt}hypno{/rt}，施加了这样的暗示。"
    play voice "voice/琉璃/041408500.ogg"
    liuli "舍弃所有感情，抛弃身为人类的内心。"
    play voice "voice/琉璃/041408530.ogg"
    liuli "尤其是，在和前辈在一起的时候更加如此。"
    play voice "voice/琉璃/041408540.ogg"
    liuli "即使前辈不在身边，只要一想到你我就会变成自己讨厌的样子。"
    play voice "voice/琉璃/041408550.ogg"
    liuli "变得动摇，也许会因此导致{rb}灵纹{/rb}{rt}rune{/rt}的暴走也说不定。"
    play voice "voice/琉璃/041408560.ogg"
    liuli "如果因为这样让星天宫的项目失败了......我就无法为人类做出贡献了。"
    play voice "voice/琉璃/041408570.ogg"
    liuli "所以我将{rb}催眠{/rb}{rt}hypno{/rt}的暗语告诉了圣护院小姐。"
    play voice "voice/琉璃/041408580.ogg"
    liuli "这也是为了防止我一错再错。"
    play voice "voice/琉璃/041408640.ogg"
    liuli "明明现在就只剩下学长而已了，明明就只剩下在雪见市留下的回忆而已了！"
    play voice "voice/琉璃/041408660.ogg"
    liuli "明明一直......是这么打算的！"
    pause 0.1 hard
    scene set only liuli_cg fight end4
    $ flcam.move(0, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041408670.ogg"
    liuli "但我却犹豫了！"
    play voice "voice/琉璃/041408680.ogg"
    liuli "这份感情在阻挠着我。"
    play voice "voice/琉璃/041408690.ogg"
    liuli "明明应该舍弃，却又不想舍弃。"
    play voice "voice/琉璃/041408700.ogg"
    liuli "明明应该丢掉，却又不舍不得丢掉。"
    play voice "voice/琉璃/041408710.ogg"
    liuli "在这雪见市留下的那些回忆......没有一个是我能够狠心丢弃的。"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041408760.ogg"
    liuli "一直以来我都认为，只要被你讨厌的话就能做到了！"
    play voice "voice/琉璃/041408770.ogg"
    liuli "无论何时我都这样让自己保持清醒。"
    play voice "voice/琉璃/041408780.ogg"
    liuli "逃避着软弱的自己。"
    play voice "voice/琉璃/041408790.ogg"
    liuli "逃避着那颗尽是迷惘的内心。"
    play voice "voice/琉璃/041408800.ogg"
    liuli "无论何时我都希望保持机械般的自己。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day city3 xuejian
    show sepiagrain onlayer texture
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve    
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104070.ogg"
    liuli "因为这里的雪和其他地方不一样的关系，才吸引了这样密集的人群也说不定。"
    show liuli_dsf_b2 b2 b2_sp1
    me01 "呐琉璃，我以前也来过这里，不过和现在比起来差别有点大。"
    me01 "关于我的过去，你想听吗？"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104080.ogg"
    liuli "是的，比起历史的客观事实，我更想听的是关于这里居民的故事。"
    play voice "voice/琉璃/040104090.ogg"
    liuli "我想知道这里的居民过去在这里经历的事情，对这座城市抱着什么样特殊的感情。"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg fight end3
    with dissolve
    pause 1.0 hard
    me01 "琉璃你真的......"
    me01 "希望自己变成那样冰冷无情的机器吗？"
    play voice "voice/琉璃/041408850.ogg"
    liuli "这个问题我已经说过很多次了。"
    me01 "那为什么又会对人类的感情感到迷茫呢？"
    me01 "又为什么要来到学校，为什么要认识藤原瞳呢？"
    me01 "为什么明明曾经放弃一切的你，会渴望为了人类的未来而努力呢。"
    me01 "我并没有打算阻止琉璃你离开雪见市。"
    me01 "也不会阻止你前往宇宙执行任务。"
    me01 "如果那是你的梦想，我又怎么可能阻止。"
    me01 "可是啊，如果不能笑着目送你离开。"
    me01 "我是绝对不会罢休的！"
    play voice "voice/琉璃/041408900.ogg"
    liuli "前辈......真是残忍。"
    pause 0.1 hard
    scene set only liuli_cg fight end4
    $ flcam.move(0, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041408930.ogg"
    liuli "你是要让我用愉快的心情，面对与你离别吗？"
    play voice "voice/琉璃/041408950.ogg"
    liuli "我说不定......会哭的。"
    pause 0.1 hard
    scene set only liuli_cg fight end5
    with dissolve
    play voice "voice/琉璃/041408970.ogg"
    liuli "想到自己见不到前辈了，就会无法集中精力去工作的。"
    me01 "这才是我们真正需要一起克服的困难不是吗？"
    play voice "voice/琉璃/041408980.ogg"
    liuli "......"
    me01 "让我讨厌你或者抹去记忆什么的，这些都只是逃避的方式罢了。"
    me01 "明明让我不要逃避，可是到头来真正逃避的不正是琉璃你自己吗？"
    pause 0.1 hard
    scene set only liuli_cg fight end4
    with dissolve
    play voice "voice/琉璃/041408990.ogg"
    liuli "前辈你果然......很残忍！"
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    "制胜点有两个。"
    "第一个我已经失败了。"
    "所以剩下的——就只有一个办法。"
    pause 1.0 hard
    $ flcam.move(0, -1400, 450)
    scene set only liuli_cg fight end3
    with dissolve
    pause 1.0 hard
    me01 "琉璃你很想被我讨厌吗？"
    play voice "voice/琉璃/041409090.ogg"
    liuli "是的。"
    me01 "但同样你也是喜欢我的吧？"
    play voice "voice/琉璃/041409100.ogg"
    liuli "是的。"
    pause 0.1 hard
    scene set only liuli_cg fight end5
    $ flcam.move(0, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041409110.ogg"
    liuli "我喜欢前辈！"
    pause 0.1 hard
    scene set only liuli_cg fight end4
    with dissolve
    play voice "voice/琉璃/041409120.ogg"
    liuli "当自己注意到的时候，已经无药可救地喜欢上你了！"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "谢谢你琉璃。"
    "也正因如此，我才能够赢得这最后的胜利——"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg fight end6
    with in2out_02_l
    pause 1.0 hard
    play voice "voice/琉璃/041409130.ogg"
    liuli "......"
    "我在转身的一瞬间亲吻了她的嘴唇。"
    show wflash onlayer texture
    "与此同时这也是我发动{rb}催眠{/rb}{rt}hypno{/rt}的条件。"
    python:
        local_config.player.skills += [tyt_breakout]
    pause 0.1 hard
    scene set only liuli_cg fight end6_2
    with dissolve
    "琉璃一动不动。"
    "完全没有反抗。"
    "从正面接受了它。"
    pause 0.1 hard
    scene set only liuli_cg fight end7
    $ flcam.move(0, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "没有逃避这份感情。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge evening xuejian
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(5200, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2 at walkin_l(0.7)
    pause 0.5 hard
    play voice "voice/立花希/031401140.ogg"
    lhx "急着赶过来结果目击到了不得了的场景。"
    play music second_111 fadein 3.0 if_changed
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031401150.ogg"
    lhx "这里似乎是被人用了{rb}视线诱导{/rb}{rt}misdirection{/rt}，出奇的安静。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031401160.ogg"
    lhx "不管怎么说凉君和{rb}璃之助{/rb}{rt}昵称{/rt}似乎已经分出胜负了，我又白跑了一趟。"
    show lhx_dsf_b2 b2 b2_s3
    play voice "voice/立花希/031401170.ogg"
    lhx "......"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031401190.ogg"
    lhx "不要误会......我不开心的理由从一开始就不存在的。"
    hide lhx_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_n2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/水之濑/051400480.ogg"
    szl "既然如此就不要围观了，快点闪人吧。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141400420.ogg"
    qcls "感觉到了强大的{rb}灵纹{/rb}{rt}rune{/rt}所以赶来看看。"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/051400490.ogg"
    szl "虽然跟工作没关系，也不是什么异常的{rb}灵纹{/rb}{rt}rune{/rt}。"
    hide szl_dsf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141400430.ogg"
    qcls "但是花山院小姐的{rb}灵纹{/rb}{rt}rune{/rt}是高输出类型的，所以为了不对城市造成危害我们还是会时刻注意的。"
    show qcls_zf_b1 b1 b1_n2
    play voice "voice/千川老师/141400440.ogg"
    qcls "如果有什么万一我也会使用{rb}虚无{/rb}{rt}psi-missing{/rt}的。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show szl_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051400500.ogg"
    szl "虽然我从最开始就觉得没这个必要，又不是花山院自己想要伤害别人。"
    show szl_dsf_b3 b3 b3_s3
    play voice "voice/水之濑/051400510.ogg"
    szl "倒不如说那孩子就是善良的集合体。"
    hide qcls_zf_b1
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031401200.ogg"
    lhx "即使如此你还是赶过来了，因为是同伴的缘故吗？"
    show szl_dsf_b3 b3 b3_s1
    play voice "voice/水之濑/051400520.ogg"
    szl "只是普通的同僚而已......"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051400570.ogg"
    szl "现在的花山院看不出有任何扼杀感情的迹象，和以前她完全一样了。"
    play voice "voice/水之濑/051400580.ogg"
    szl "所以，这不就又回到原点了吗？"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051400590.ogg"
    szl "今后也没有必要再依靠{rb}催眠{/rb}{rt}hypno{/rt}去约束自己了吧。"
    $ flcam.move(0, 0, 600, duration=1.5)
    show qcls_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141400480.ogg"
    qcls "不再舍弃自己的内心，而是坚定地按照自己的意志迈向崭新的人生。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051400600.ogg"
    szl "反正花山院马上就要离开这座城市了，以后也没有机会再见面了吧。"
    show szl_dsf_b1 b1 b1_n2
    play voice "voice/水之濑/051400610.ogg"
    szl "就算是和神野凉也不得不告别了。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141400490.ogg"
    qcls "虽然离别总是让人悲伤的，但这也是没有办法的事情。"
    show lhx_dsf_b2 b2 b2_s1
    play voice "voice/立花希/031401240.ogg"
    lhx "这可说不定。"
    show lhx_dsf_b2 b2 b2_n2
    play voice "voice/立花希/031401250.ogg"
    lhx "我不认为分别是唯一的结果。"
    hide qcls_zf_b1
    hide szl_dsf_b1
    $ flcam.move(5200, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031401260.ogg"
    lhx "一定还有别的路可选。"
    show lhx_dsf_b1 b1 b1_n2
    play voice "voice/立花希/031401270.ogg"
    lhx "一条让凉君和璃之助都能够幸福的路。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    play music second_131 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    "乌云散去后，天空又恢复了平静。"
    "琉璃安静地躺在我的怀里。"
    "她埋着头，仿佛是在极力隐藏自己那早已布满泪水的脸颊。"
    pause 1.0 hard
    scene set only bridge evening under xuejian alpha
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409140.ogg"
    liuli "原本我是应该拒绝的。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409150.ogg"
    liuli "不应该接受前辈的。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041409160.ogg"
    liuli "但是到头来还是失败了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409180.ogg"
    liuli "我原本已经决定了要将自己的一生奉献给星天宫的宇宙开发事业。"
    play voice "voice/琉璃/041409190.ogg"
    liuli "为了人类......也是为了{rb}灵继者{/rb}{rt}elfin{/rt}们。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409200.ogg"
    liuli "如果我足够努力的话，也许就能解释{rb}灵继者{/rb}{rt}elfin{/rt}诞生的原因了。"
    play voice "voice/琉璃/041409210.ogg"
    liuli "说不定就能解开{rb}灵纹{/rb}{rt}rune{/rt}的秘密了。"
    play voice "voice/琉璃/041409220.ogg"
    liuli "这次的计划也是为了这个。"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409230.ogg"
    liuli "为什么我们会和普通人不一样？"
    play voice "voice/琉璃/041409240.ogg"
    liuli "为什么只有我们变成了{rb}灵继者{/rb}{rt}elfin{/rt}？"
    show liuli_dsf_b1 b1 b1_s3
    play voice "voice/琉璃/041409250.ogg"
    liuli "我们诞生的理由......如果能够知道的话，就不会再有人为此而苦恼了。"
    play voice "voice/琉璃/041409260.ogg"
    liuli "也不会再有{rb}灵纹{/rb}{rt}rune{/rt}的暴走了。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409270.ogg"
    liuli "到时候也许我就能，接受身为{rb}灵继者{/rb}{rt}elfin{/rt}的自己了......"
    pause 1.0 hard
    scene white
    with slowerdissolve
    stop music fadeout 5.0
    pause 1.0 hard
    "就像星天宫的大家渴望琉璃的帮助一样。"
    "琉璃她自己也渴望过别人的帮助吗？"
    "渴望过有人来拯救身为{rb}灵继者{/rb}{rt}elfin{/rt}的自己吗？"
    "对于普通人怀有的憧憬。"
    "渴望平凡的心。"
    "不是作为{rb}灵继者{/rb}{rt}elfin{/rt}，而是作为一名普通人而被大家所接受、被大家所需要——"
    "在那希望的背后，是一束光。"
    "耀眼、纯净的光。"
    "温柔得......让人无法移开视线。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge evening under xuejian alpha
    play music second_134 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409640.ogg"
    liuli "我很感激星天宫的大家。"
    play voice "voice/琉璃/041409650.ogg"
    liuli "多亏了圣护院小姐她们，让即使是离开家生活的我也没有因此而感到寂寞。"
    show liuli_dsf_b1 b1 b1_n1
    play voice "voice/琉璃/041409660.ogg"
    liuli "就算那只是为了利用身为{rb}灵继者{/rb}{rt}elfin{/rt}的我也好，至少不再是孤单一人。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409670.ogg"
    liuli "也许就是因为这样。"
    show liuli_dsf_b3 b3 b3_s4
    play voice "voice/琉璃/041409690.ogg"
    liuli "明明想要否定自己的内心，可到头来即便是脱胎换骨也还是无法完全抛弃身为人的感情。"
    play voice "voice/琉璃/041409700.ogg"
    liuli "我想如果自己没有被星天宫收留而是孤单一个人的话，可能就会变得如同机器一般的冰冷吧......"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041409710.ogg"
    liuli "甚至会因此拒绝与人接触。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_s3
    play voice "voice/琉璃/041409720.ogg"
    liuli "但是我果然......还是喜欢人类的。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041409740.ogg"
    liuli "我也曾烦恼为什么自己会变成{rb}灵继者{/rb}{rt}elfin{/rt}。"
    show liuli_dsf_b1 b1 b1_s3
    play voice "voice/琉璃/041409750.ogg"
    liuli "如果不是这样的话，就不会伤害到家人和身边的人了。"
    play voice "voice/琉璃/041409760.ogg"
    liuli "也不会伤害到前辈了。"
    show liuli_dsf_b1 b1 b1_c1
    play voice "voice/琉璃/041409780.ogg"
    liuli "所以一直认为，就算被前辈讨厌了也是没有办法的事情。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    play sound touch
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg fight end6
    with dissolve
    pause 1.0 hard
    me01 "你还不明白吗？"
    me01 "是{rb}灵继者{/rb}{rt}elfin{/rt}也好普通人也罢，无论琉璃你变成什么样子。"
    me01 "我、藤原瞳、还有星天宫的大家都会一直喜欢着你的。"
    play voice "voice/琉璃/041409800.ogg"
    liuli "前、辈......"
    pause 0.1 hard
    scene set only liuli_cg fight end7
    $ flcam.move(0, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041409810.ogg"
    liuli "也许......这是第一次。"
    play voice "voice/琉璃/041409820.ogg"
    liuli "肯定了身为{rb}灵继者{/rb}{rt}elfin{/rt}的我。"
    play voice "voice/琉璃/041409850.ogg"
    liuli "我不想就这样和前辈告别。"
    play voice "voice/琉璃/041409860.ogg"
    liuli "不想就这样分开......想要继续待在你的身边。"
    play voice "voice/琉璃/041409870.ogg"
    liuli "一直都是这样想的。"
    pause 0.1 hard
    scene set only liuli_cg fight end8
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041409880.ogg"
    liuli "也许抱着这样的心情去执行任务会很辛苦。"
    play voice "voice/琉璃/041409890.ogg"
    liuli "但我一定会克服给你看的！"
    play voice "voice/琉璃/041409900.ogg"
    liuli "我想现在的自己，已经从前辈那里得到了勇气。"
    pause 0.1 hard
    scene set only liuli_cg fight end7
    $ flcam.move(0, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041409950.ogg"
    liuli "我会和这份感情一起，出色地完成任务。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 3.0 hard

label day219.laboratory_event04:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    play music second_140 fadein 3.0 if_changed
    play sound open_door4
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/白羽/711400010.ogg"
    baiyu "哈喽哈喽，圣护院~"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151404000.ogg"
    shy "......今天真是贵客盈门啊，您竟然也来了。"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711400020.ogg"
    baiyu "累死了，给我来杯咖啡吧~"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151404010.ogg"
    shy "这里不是咖啡店，要是想喝就自己随便找个自动贩卖机买吧。"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711400030.ogg"
    baiyu "难得我特地来一次，你却依旧那么冷淡啊。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404020.ogg"
    shy "您的劳苦我表示理解，事故的后续工作也辛苦了~"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711400040.ogg"
    baiyu "从你的话里只能听到挖苦呢。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404030.ogg"
    shy "性格如此，我并不打算更正。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151404040.ogg"
    shy "......话说回来，您来的还真是早，手头应该还有各种收尾工作吧？"
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711400050.ogg"
    baiyu "全都交给部下了，这次失败的责任应该由谁承担之类的争论我已经厌倦了。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711400060.ogg"
    baiyu "然后我就立刻离开了本部赶来雪见市了。"
    show by smile01 with dissolve
    play voice "voice/白羽/711400070.ogg"
    baiyu "而且在这里准备交接的工作也更有意义，我想你那边也准备得差不多了吧？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151404050.ogg"
    shy "就如我刚才所说今天是贵客盈门，所以我现在才要开始呢。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711400080.ogg"
    baiyu "是吗，那么花山院那边呢？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404060.ogg"
    shy "她现在正在外出中。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711400090.ogg"
    baiyu "组织决定这个月就要把你们两人都派到总部去，到时候就拜托你了。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151404070.ogg"
    shy "我明白。交接工作是自然，关于载人探测器方面我也正打算抓紧时间。"
    play voice "voice/圣护院/151404080.ogg"
    shy "毕竟我是负责花山院这边的工作。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711400100.ogg"
    baiyu "圣护院亲果然很可靠呢~"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404090.ogg"
    shy "......请不要用这种让人误会的称呼。"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711400110.ogg"
    baiyu "不只是花山院的事情，将你选为研究所的主任还真是选对人了。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404100.ogg"
    shy "......"
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711400120.ogg"
    baiyu "还有什么担心的事吗？"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151404160.ogg"
    shy "为什么这么问？"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711400130.ogg"
    baiyu "因为有这种直觉。"
    play voice "voice/圣护院/151404170.ogg"
    shy "......"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711400140.ogg"
    baiyu "虽然你面无表情，但是动作之间却能透露出来。"
    play voice "voice/白羽/711400150.ogg"
    baiyu "人将要撒谎的时候，体温会变化，而容易暴露的部位就是手心。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711400160.ogg"
    baiyu "你从刚才开始就时不时地用手指敲打胳膊。"
    play voice "voice/白羽/711400170.ogg"
    baiyu "这也是常用来调节体温的行为哟~"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711400180.ogg"
    baiyu "无论哪个都是生理上的反射，所以就算想要隐藏也是白费力气的，尤其是在我面前。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711400190.ogg"
    baiyu "因为人无法对自己撒谎嘛。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404180.ogg"
    shy "......真是败给你了，不愧是心理学教授。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711400200.ogg"
    baiyu "虽然我的专业不是心理学，而是“超”心理学才对。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151404190.ogg"
    shy "我所担心的是花山院的事情。"
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711400210.ogg"
    baiyu "不是已经既定了吗？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404200.ogg"
    shy "就在她来到这里之后心里又产生了新的迷茫。最糟糕的情况也许会拒绝参加行星探测的任务。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711400220.ogg"
    baiyu "......"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404210.ogg"
    shy "一副意味深长的样子......是不相信我的话吗，还是说这些也早已经预料到了？（小声）"
    play voice "voice/圣护院/151404220.ogg"
    shy "就在刚刚也是轻易地就看破了我的烦恼。仿佛自己的心被窥探了一般，有种不舒服的感觉。（小声）"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404230.ogg"
    shy "我是怎么也没办法和她好好相处......（小声）"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show baiyu_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/白羽/711400230.ogg"
    baiyu "你并没有担心花山院会做出那样的举动，我能感到你对此很从容啊。"
    play voice "voice/圣护院/151404240.ogg"
    shy "......"
    play voice "voice/白羽/711400240.ogg"
    baiyu "花山院性格认真，又活泼得让人想要紧紧搂住，最重要的是她觉得自己欠了星天宫的恩情。"
    play voice "voice/白羽/711400250.ogg"
    baiyu "也正因为这样她是绝对不会做出抛下任务这种没有责任心的举动的。"
    play voice "voice/白羽/711400260.ogg"
    baiyu "即使如此花山院还是会犹豫不定的话，归根结底应该是对“家人”有所顾虑吧？"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711400270.ogg"
    baiyu "看来是无法简单就排除的障碍呢。被称之为“不悦情动反射”的东西。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151404250.ogg"
    shy "......那是什么？"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711400280.ogg"
    baiyu "人在遭遇不幸的时候，就会本能地想要保护自己。这种反应是由“不悦情动反射”而产生的。"
    play voice "voice/白羽/711400290.ogg"
    baiyu "因此，这种反抗的心理和条件反射差不多，就连本人也无法控制。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711400300.ogg"
    baiyu "身为局外人的我们就算担心，也不会有所改变，只能让她自己去克服了。"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404270.ogg"
    shy "真的......是这样吗？（小声）"
    play voice "voice/圣护院/151404280.ogg"
    shy "难道不是因为本人束手无策了，才更需要别人的帮助吗？（小声）"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151404300.ogg"
    shy "从这层意义上来说的话，我对他也是抱有期待的。（小声）"
    play voice "voice/圣护院/151404310.ogg"
    shy "不过归根结底也只是为了让载人探测能够圆满完成而已。（小声）"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show baiyu_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/白羽/711400310.ogg"
    baiyu "圣护院，关于载人探测的项目还请你尽情展现你的才能。"
    play voice "voice/白羽/711400320.ogg"
    baiyu "也期待着你将“芬布尔之冬”计划的后续报告给我。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404320.ogg"
    shy "......我听说这个计划就是人类的勇士被召集的一个前奏。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711400330.ogg"
    baiyu "是啊。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404330.ogg"
    shy "而这些所谓的人类的勇士，就是{rb}灵继者{/rb}{rt}elfin{/rt}。"
    play voice "voice/圣护院/151404340.ogg"
    shy "能够为人类的未来做出贡献，拥有优秀素质的个体。"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151404350.ogg"
    shy "所以星天宫才会一直希望得到新的{rb}灵继者{/rb}{rt}elfin{/rt}。（小声）"
    play voice "voice/圣护院/151404370.ogg"
    shy "一旦感知到暴走的{rb}灵纹{/rb}{rt}rune{/rt}，就会通知手下直接赶往现场。（小声）"
    play voice "voice/圣护院/151404380.ogg"
    shy "如果这些不是暂时性的状况，而是{rb}灵继者{/rb}{rt}elfin{/rt}觉醒征兆的话，就将其劝诱加入星天宫。（小声）"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151404390.ogg"
    shy "友加也有可能成为其中之一。（小声）"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151404400.ogg"
    shy "一切都是为了开展载人行星探测计划。"
    play voice "voice/圣护院/151404410.ogg"
    shy "为了使辽阔的宇宙不再是属于神明，而是成为人类的所有物。"
    play voice "voice/圣护院/151404420.ogg"
    shy "我们在这片土地上所做的一切，也正是因为有了这个使命吧。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show baiyu_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/白羽/711400340.ogg"
    baiyu "是呢，因为雪见市是一片很容易诞生{rb}灵继者{/rb}{rt}elfin{/rt}的土地。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711400360.ogg"
    baiyu "竟然还派生出了行星气象学。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711400370.ogg"
    baiyu "如果能够查明真相，我们就离{rb}灵继者{/rb}{rt}elfin{/rt}诞生秘密更进一步了呢。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711400380.ogg"
    baiyu "呐......你刚刚说的这些果然是因为还有别的担心的事情吧？"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711400390.ogg"
    baiyu "你真正牵挂的不是花山院，而是把矛头指向了我。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404450.ogg"
    shy "......"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711400400.ogg"
    baiyu "如果想以研究者的身份取得成功的话，就必须要舍弃迷茫。不然只会让自己一直痛苦下去而已。"
    play voice "voice/白羽/711400410.ogg"
    baiyu "就这一点，希望你和花山院都是如此。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404460.ogg"
    shy "我会铭记在心的。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711400420.ogg"
    baiyu "那么，我差不多要去见“那孩子”了~"
    pause 1.0 hard
    play sound close_door4
    show baiyu_yjf_b1 b1 b1_h1 at walkout_l(0.3)
    pause 3.0 hard
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151404470.ogg"
    shy "......心情愉快地离开了。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151404480.ogg"
    shy "就那么想和“她”再见一面吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404490.ogg"
    shy "将人类勇士——{rb}灵继者{/rb}{rt}elfin{/rt}召集到一起的关键所在，大天使瓦尔基里。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404510.ogg"
    shy "到头来我还是没能查明她的身份......"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151404520.ogg"
    shy "芬布尔之冬。"
    play voice "voice/圣护院/151404540.ogg"
    shy "{rb}灵继者{/rb}{rt}elfin{/rt}难道真的只是人类通向未来的棋子吗？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404550.ogg"
    shy "我倒是觉得这样的设定是不公平的。"
    play voice "voice/圣护院/151404560.ogg"
    shy "{rb}灵继者{/rb}{rt}elfin{/rt}不应该是高人一等的存在吗？"
    play voice "voice/圣护院/151404570.ogg"
    shy "低等的人类才应该是被当做棋子的吧？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404580.ogg"
    shy "如果大家都无法放下成见，也许这样的日子终将会到来吧。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151404590.ogg"
    shy "明明所长您也是对此才心怀忧虑的吧......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day219.laboratory_event05:
    $ flcam.move(0, 0, 0)
    scene set only laboratory evening outside xuejian
    play music second_163 fadein 3.0 if_changed
    with slowdissolve
    pause 2.0 hard
    scene set only laboratory inside2 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151404650.ogg"
    shy "......今天一天我什么工作都没完成。"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151404660.ogg"
    shy "但所有发生的这些都远比交接工作来得重要。我抽出时间也是算是值得了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041409960.ogg"
    liuli "是的~"
    play voice "voice/琉璃/041409970.ogg"
    liuli "我决定了，要与您一起前往宇宙研究中心。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n5 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041409980.ogg"
    liuli "虽然本来就是这个打算，但是现在的决心比起以前更加坚定了。"
    show shy_yjf_b1 b1 b1_ga2
    play voice "voice/圣护院/151404680.ogg"
    shy "是因为神野凉吗？"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041409990.ogg"
    liuli "是的，因为前辈的支持我终于能够斩断迷茫了。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404690.ogg"
    shy "这么说来我也不得不感谢他呢。"
    hide liuli_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "道谢什么的就不需要了，相对的我有个请求。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151404700.ogg"
    shy "是什么？"
    me01 "今后能让我和琉璃保持联系吗？"
    me01 "虽说是道别，但请允许我们用电话交流。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151404710.ogg"
    shy "什么啊，这不还没斩断留恋吗......"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041410000.ogg"
    liuli "圣护院小姐......我会忙到连接电话的时间都没有吗？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404720.ogg"
    shy "这倒不会。"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151404730.ogg"
    shy "虽说多少会有几个重要的任务，但是也没有完全霸占你的自由时间，如果是在那范围之外的话就随意了。"
    show liuli_dsf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/琉璃/041410010.ogg"
    liuli "谢、谢谢您~"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404740.ogg"
    shy "但是这并不代表你们有很多闲暇时光，这点也希望你们明白。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n4 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041410020.ogg"
    liuli "在空出的时间里返回雪见市......也很困难的吗？"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151404750.ogg"
    shy "是啊，挤不出那么多时间吧。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151404770.ogg"
    shy "虽然会很煎熬，但是希望你们能理解这一点。"
    show liuli_dsf_b3 b3 b3_n2
    play voice "voice/琉璃/041410030.ogg"
    liuli "好吧......我明白了。"
    hide shy_yjf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041410040.ogg"
    liuli "我想要报答星天宫大家的恩情。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041410050.ogg"
    liuli "多亏了圣护院小姐和万夜花小姐，我才能学到{rb}灵纹{/rb}{rt}rune{/rt}的使用方法。"
    show liuli_dsf_b2 b2 b2_n2
    play voice "voice/琉璃/041410060.ogg"
    liuli "为了不伤害他人，掌握避免暴走的方法。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041410080.ogg"
    liuli "然后才能和前辈相遇。"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041410090.ogg"
    liuli "就连现在的我能够放弃依赖{rb}催眠{/rb}{rt}hypno{/rt}，也是多亏了圣护院小姐的教导。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151404780.ogg"
    shy "这些都是拜你自己的努力所赐，赞美的话应该对你自己说才最为妥当。"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151404830.ogg"
    shy "接下来将会有更加严格的训练等待着你，为了克服难关也只能这样继续前进了。"
    show liuli_dsf_b1 b1 b1_n2
    play voice "voice/琉璃/041410140.ogg"
    liuli "是的~"
    hide shy_yjf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041410150.ogg"
    liuli "现在的我并不觉得自己很渺小。"
    show liuli_dsf_b2 b2 b2_n1
    play voice "voice/琉璃/041410170.ogg"
    liuli "况且我并不是一人。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151404870.ogg"
    shy "那么，我要说的就只有一件事了。"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151404880.ogg"
    shy "期待你能够引导这个行星探测计划走向成功。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151404890.ogg"
    shy "你是我们唯一的依靠，所以拜托了。"
    show liuli_dsf_b2 b2 b2_h1
    play voice "voice/琉璃/041410210.ogg"
    liuli "好的，请放心交给我吧！"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151404970.ogg"
    shy "神野君也请你节制一点，不要做出让花山院苦恼的举动。"
    me01 "您指的举动是什么啊......"
    show liuli_dsf_b2 b2 b2_n3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/琉璃/041410260.ogg"
    liuli "也就是说又可以和前辈约会了~"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151404990.ogg"
    shy "就是要你注意，别让花山院变成这样。"
    me01 "这个恕我也没办法保证。"
    show shy_yjf_b1 b1 b1_a1
    play voice "voice/圣护院/151405000.ogg"
    shy "如果对计划造成影响的话，我们星天宫会全力铲除你的。"
    me01 "突然感觉责任重大！"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151405010.ogg"
    shy "完全感受不到你的觉悟啊......"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day220
