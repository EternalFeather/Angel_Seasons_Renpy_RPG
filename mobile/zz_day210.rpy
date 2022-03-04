
label inside_battle5(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "藤原瞳的拖延战术似乎逐渐奏效。"
    "面对她的攻势即便是有「满月」加持的铃音也没有占到丝毫便宜。"
    "此战为{color=#f00}尽力局{/color}，即使失败也不会迎来Bad End。"
    "为了避免不必要的损失建议{color=#f00}节省道具资源的消耗{/color}。"
    "总之还是那句话，祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label inside_battle6(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "随着水之濑凛的加入一边倒的局面被打破了。"
    "为了应对水之濑凛的居合道，藤原瞳启用了执事巫女才拥有的秘术结界{encyclopedia=rockwall}瓦轮刑部{/encyclopedia}。"
    "在结界的守护下藤原瞳以及见习巫女受到的{color=#f00}直接伤害将降低90%{/color}。"
    "在镇物「遗念镜」的祝福加持下，「雷亚」的普攻变更为「火」属性。"
    "「雷」与「火」发生的{color=#f66}超载反应{/color}能够暂时破除「瓦轮刑部」的效果，随着敌方角色的行动结界将逐渐恢复。"
    "另外拥有「植诚友加」的玩家也可以借助「雷」与「水」发生的{color=#99f}感电反应{/color}，利用间接伤害进行有效输出。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label day210:
    bookmark
    $ save_name = _("Day 210")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date208 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only laboratory inside2 xuejian
    with slowerdissolve
    play music second_104 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    play sound open_door4
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/白羽/711000010.ogg"
    stranger "哈喽哈喽圣护院~"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s4 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151000010.ogg"
    shy "切。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_h2
    show baiyu_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/圣护院/151000020.ogg"
    shy "辛苦了所长，恭候您多时了。"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711000020.ogg"
    baiyu "你刚刚咋舌了对吧？"
    play voice "voice/圣护院/151000030.ogg"
    shy "不愧是心理学的教授，这都被看穿了吗？"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711000030.ogg"
    baiyu "你还真是直言不讳啊......话说回来，你果然很讨厌我。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151000040.ogg"
    shy "只是不习惯而已，请别误会。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000040.ogg"
    baiyu "虽然不是时候，但是有件可能会让你听了更头疼的事情想和你谈，可以吗？"
    stop music fadeout 5.0
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151000050.ogg"
    shy "我就是为了这个才在这里等您的，要谈论的事情也大致已经猜到了。"
    play music second_122 fadein 3.0 if_changed
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151000060.ogg"
    shy "是“芬布尔之冬”计划的后续，以及最新的行星探测计划吧？"
    play voice "voice/圣护院/151000070.ogg"
    shy "新计划要让花山院加入的话，我也不得不同行。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711000050.ogg"
    baiyu "不只是同行而是被选作研究团队的一员，感到自豪吧~"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151000080.ogg"
    shy "要说的就这些了吗？"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711000060.ogg"
    baiyu "真是冷淡啊你......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151000090.ogg"
    shy "如果已经结束的话请容我先离开了。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711000070.ogg"
    baiyu "想早点回去是因为妹妹的事情？什么时候变得那么在乎家人了啊~"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151000100.ogg"
    shy "想隐瞒的事情一下子就会被戳破，这就是我不擅长和她相处的原因。（小声）"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show baiyu_yjf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.3
    play voice "voice/白羽/711000080.ogg"
    baiyu "不好意思，还有一件事。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151000110.ogg"
    shy "什么？"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711000090.ogg"
    baiyu "是关于{encyclopedia=klns}库洛诺斯{/encyclopedia}的事情。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151000120.ogg"
    shy "神野教授所属的部门吗？"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000100.ogg"
    baiyu "似乎库洛诺斯正在追击的一名祟已经潜入星天宫了。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151000130.ogg"
    shy "......祟？"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711000110.ogg"
    baiyu "这座城市里发生的事似乎也被神野教授注意到，于是乎我就被拜托前来调查了。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151000140.ogg"
    shy "......"
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711000130.ogg"
    baiyu "你觉得这样合理吗？"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151000160.ogg"
    shy "什么意思？"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000140.ogg"
    baiyu "比方说，在雪见市的{rb}灵继者{/rb}{rt}elfin{/rt}中其实就有来自库诺洛斯的卧底之类的。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151000180.ogg"
    shy "也就是说，所长对研究所麾下的{rb}灵继者{/rb}{rt}elfin{/rt}存有疑心？"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711000150.ogg"
    baiyu "就是这样的，那么你有什么人选吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151000190.ogg"
    shy "现在没有。"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711000160.ogg"
    baiyu "呼嗯~"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151000210.ogg"
    shy "如果存在的话就排除，我是这么认为的。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000180.ogg"
    baiyu "这所星天宫研究所集结人类的勇士，就是为了应对“芬布尔之冬”计划。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711000220.ogg"
    baiyu "“这些力量”对我们来说究竟是福是祸呢......真是有趣啊~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day210'
    $ seen_day210_balltower_event01 = False
    $ seen_day210_laboratory_event01 = False
    $ seen_day210_street_event01 = False

label day210.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day210':
        $ flcam.move(6100, -1800, 2800)
    elif _overworld_label == 'day210.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day210.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'])
    elif _overworld_label == 'day210.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        cloqks=("day210.balltower_event01", "not seen_day210_balltower_event01"),
        laboratory=("day210.laboratory_event01", "seen_day210_balltower_event01 and not seen_day210_laboratory_event01"),
        road2=("day210.street_event01", "seen_day210_laboratory_event01 and not seen_day210_street_event01"))
    $ window_animate_outro()
    if _return == 'day210.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day210.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day210.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day210.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    "与以往有些不同，今天从早晨就开始下起了雪。"
    "出门后眼前更是一片洁白的景象。"
    "冬雪，开始堆积了......"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    with dissolve
    play music second_140 fadein 3.0 if_changed
    play sound jiaobu
    pause 2.0 hard
    "漫无目的地走着，不知不觉就来到了钟楼广场。"
    "自从来到雪见市，总能梦见与希菲尔一起经历的往事。"
    "本来期待着这一次也能见到希菲尔，可没想到此刻出现在那里的却另有其人。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    stranger "......"
    me01 "我叫神野凉，那个......"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771000070.ogg"
    jsqd "我叫姬神，姬神千冬哟~"
    me01 "千冬？原来你就是希菲尔口中那位体弱......不对是最初的伙伴吗。"
    me01 "话说下着雪像这样一个人出来没问题吗？"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001830.ogg"
    jsqd "嗯，毕竟还有小希菲在我身边。"
    "话说回来千冬小姐和希菲尔长得不是一点点像。"
    "莫非是她的姐姐或者......母亲之类的？"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771001900.ogg"
    jsqd "你如果再这么自以为是地瞎猜，我就把你整个“叭咕”掉了哟~"
    me01 "为什么我的想法你听得到？！"
    me01 "再说了女孩子不要随便把“吃人”这样可怕的话挂在嘴边啊。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001860.ogg"
    jsqd "是吗......从很久以前开始就听说你们一起玩耍的事情了。"
    me01 "希菲尔经常和你说起我的事吗？"
    play voice "voice/千冬/771001830.ogg"
    jsqd "嗯，而且小希菲尔她......"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001870.ogg"
    jsqd "小希菲尔之所以会喜欢上这里，一定也是因为凉君的缘故吧。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001840.ogg"
    jsqd "因为是一个充满回忆的地方嘛。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771001810.ogg"
    jsqd "北欧神话......吗。"
    show jsqd_dsf_b1 b1 b1_ga3
    play voice "voice/千冬/771001820.ogg"
    jsqd "果然很难用几句话就说明白的。"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771001880.ogg"
    jsqd "这座钟楼广场，现在好像也在积雪的样子。"
    show jsqd_dsf_b1 b1 b1_ga3
    play voice "voice/千冬/771001890.ogg"
    jsqd "我也好想打雪仗、堆雪人啊。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001930.ogg"
    jsqd "如果向星神大人许愿的话就能实现吗，真是浪漫的设定呢~"
    me01 "愿望什么的暂且不说，有什么是我能帮得上千冬小姐的吗？"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771001950.ogg"
    jsqd "......感觉应该是没有。"
    play voice "voice/千冬/771001960.ogg"
    jsqd "硬要说的话我现在特别想吃雪。"
    me01 "别乱吃啊！"
    show jsqd_dsf_b1 b1 b1_ga3
    play voice "voice/千冬/771001970.ogg"
    jsqd "毕竟这是小希菲尔的特权呢~"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002140.ogg"
    jsqd "凉君，来玩游戏吧。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002150.ogg"
    jsqd "这样的话小希菲尔一定会出现的。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002160.ogg"
    jsqd "小希菲尔从以前开始就很希望像这样三个人一起玩耍。"
    show jsqd_dsf_b1 b1 b1_s3
    play voice "voice/千冬/771002170.ogg"
    jsqd "但是，凭我自己是无法帮她实现这个愿望的。"
    me01 "这不是你的错。"
    show jsqd_dsf_b1 b1 b1_n2
    play voice "voice/千冬/771002180.ogg"
    jsqd "但终归还是我的问题，如果我能再加把劲的话说不定，就不会让她感到寂寞了。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002190.ogg"
    jsqd "凉君，你不用顾虑我的。"
    me01 "那要玩什么呢？"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002200.ogg"
    jsqd "打雪仗~"
    "不知为何有种糟糕的既视感。"
    show jsqd_dsf_b1 b1 b1_h1:
        xpos 0.5 alpha 1.0 ypos 0.98
        parallel:
            linear 1.0 ypos 1.03
        parallel:
            linear 1.0 alpha 0.0
    play sound enjoy_snow1
    pause 0.5 hard
    hide jsqd_dsf_b1
    "千冬努力弯下腰想要拾起地上的积雪。"
    "我下意识地想要上前扶住她。"
    show jsqd_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 1.03
        parallel:
            linear 0.5 ypos 0.98
        parallel:
            linear 0.5 alpha 1.0
    pause 0.5 hard
    play voice "voice/千冬/771002210.ogg"
    jsqd "敢随便碰我的话，姐姐我可要生气了哟。"
    "虽然嘴上这样说，但千冬还是抓住了我的胳膊。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002220.ogg"
    jsqd "那么，请到对面去吧。"
    me01 "要丢雪球吗？"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002230.ogg"
    jsqd "嗯，凉君也可以对着我丢哟。丢中的话是有奖励的~"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771002240.ogg"
    jsqd "快点啦，不要傻站在那里。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002250.ogg"
    jsqd "这是姐姐的命令喔，弟弟君。"
    stop music fadeout 5.0
    hide jsqd_dsf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    hide snow_level1
    play music second_108 fadein 3.0 if_changed
    play sound enjoy_snow1
    scene set only jsqd_cg game1
    with slowdissolve
    pause 0.5 hard
    play voice "voice/千冬/771002260.ogg"
    jsqd "看招~"
    "千冬向我丢出了雪球。"
    "但因为力量不足，雪球飞出不远就开始下落了。"
    "以这样的轨迹是不可能打中我的......"
    show wflash onlayer texture
    play sound rune3
    with vpunch
    pause 0.1 hard
    scene set only jsqd_cg game2
    with dissolve
    me01 "？！"
    pause 0.1 hard
    play sound enjoy_snow1
    with vpunch
    scene set only jsqd_cg game3
    with dissolve
    me01 "咕哈。"
    "原本软绵绵的雪球，突然以难以置信的轨迹和速度命中了我的脸。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    show jsqd_dsf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/千冬/771002270.ogg"
    jsqd "抱、抱歉......很痛吗？"
    me01 "一、一点也不痛。"
    show jsqd_dsf_b1 b1 b1_ga3
    play voice "voice/千冬/771002280.ogg"
    jsqd "太好了~"
    me01 "刚刚那是......{rb}灵纹{/rb}{rt}rune{/rt}？"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002290.ogg"
    jsqd "嗯，虽然母亲说会对身体造成负担，让我别轻易使用。"
    me01 "千冬小姐也是{rb}灵继者{/rb}{rt}elfin{/rt}吗？"
    show jsqd_dsf_b1 b1 b1_ga1
    play voice "voice/千冬/771002300.ogg"
    jsqd "都说了再这么自以为是的话就打你喽~"
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_ga1:
        xpos 0.5 alpha 1.0 ypos 0.98
        parallel:
            linear 1.0 ypos 1.03
        parallel:
            linear 1.0 alpha 0.0
    play sound enjoy_snow1
    pause 0.5 hard
    hide jsqd_dsf_b1
    "说完，千冬又一次尝试俯身捡起地上的积雪。"
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 1.03
        parallel:
            linear 1.0 ypos 0.98
        parallel:
            linear 1.0 alpha 1.0
    pause 0.5 hard
    me01 "那个，请不要勉强。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002310.ogg"
    jsqd "不要紧，这次不会使用{rb}灵纹{/rb}{rt}rune{/rt}的。"
    me01 "我是担心你会从轮椅上摔下来。"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771002320.ogg"
    jsqd "再这样自以为是的话，我就把这雪吃下去！"
    me01 "别用这种奇怪的威胁方式啊......"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002330.ogg"
    jsqd "凉君也是，可以向我丢过来。"
    me01 "我才不要，弄疼你了怎么办。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002340.ogg"
    jsqd "那我就给你奖励~"
    me01 "对我来说，最好的奖励就是千冬小姐老老实实地待在那里。"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771002350.ogg"
    jsqd "如果还是一直这样自以为是，我这次就不是丢雪球而是把凉君你整个丢出去了哟。"
    me01 "听起来好可怕......"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002360.ogg"
    jsqd "我的目标是拥有能够把凉君抱起然后丢出去的力量。"
    me01 "我到底做错了什么？！" with vpunch
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002370.ogg"
    jsqd "拜托了，这也是复健的一环。"
    me01 "我知道了......"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only jsqd_cg game4
    with slowdissolve
    pause 0.5 hard
    play voice "voice/千冬/771002380.ogg"
    jsqd "看招~"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=0.5)
    with dissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_ga2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/千冬/771002390.ogg"
    jsqd "啊......"
    play sound jing01
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    "千冬因为用力过猛失去了平衡，连同轮椅一同向前倾倒。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play voice "voice/希菲尔/001004100.ogg"
    stranger "不行的......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian2
    with slowdissolve
    show snow_level1 onlayer fg
    $ flcam.move(-4500, 0, 900, duration=1.5)
    play music second_103 fadein 3.0 if_changed
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m2 at walkin_r(0.3)
    pause 0.5 hard
    play voice "voice/希菲尔/001004110.ogg"
    xfe "让凉君困扰可不行啊，千冬。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001004120.ogg"
    xfe "一直这样乱来的话，会让凉君担心的。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show jsqd_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771002400.ogg"
    jsqd "嗯......抱歉呢，小希菲尔。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002410.ogg"
    jsqd "我一直......很想见你。"
    $ flcam.move(-2500, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound touch
    play voice "voice/千冬/771002420.ogg"
    jsqd "小希菲尔，至今为止你都跑到哪里去了？"
    show ts_xfe_yjz_b1 b1 b1_s1
    show jsqd_dsf_b1 b1 b1_s3
    play voice "voice/千冬/771002440.ogg"
    jsqd "让你寂寞了，对不起......"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001004140.ogg"
    xfe "......"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002450.ogg"
    jsqd "但现在我的身体也已经恢复了。"
    play voice "voice/千冬/771002460.ogg"
    jsqd "不会再出现牺牲了。"
    play voice "voice/千冬/771002470.ogg"
    jsqd "已经......不会再让小希菲尔你寂寞了。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002480.ogg"
    jsqd "大家一起玩吧。"
    play voice "voice/希菲尔/001004150.ogg"
    xfe "......"
    play voice "voice/千冬/771002490.ogg"
    jsqd "凉君也是，三个人一起玩吧。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002500.ogg"
    jsqd "至今为止没能完成的心愿，三个人一起实现它吧。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002510.ogg"
    jsqd "怎么样，小希菲尔？"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001004160.ogg"
    xfe "......办不到。"
    pause 0.5 hard
    play sound xiaoshi_1
    show wflash onlayer texture
    hide ts_xfe_yjz_b1
    with slowdissolve
    pause 0.5 hard
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    show jsqd_dsf_b1 b1 b1_sp1
    play sound enjoy_snow1
    with vpunch
    "随着希菲尔的消失，我上前扶住了千冬。"
    play music second_129 fadein 3.0 if_changed
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg daze
    with slowdissolve
    pause 0.5 hard
    play voice "voice/希菲尔/001004170.ogg"
    xfe "已经没有办法像这样三人一起玩耍了。"
    play voice "voice/希菲尔/001004180.ogg"
    xfe "希菲尔我已经不再是懵懂无知的小孩子了。"
    pause 0.1 hard
    scene set only xfe_cg sad 
    with dissolve
    play voice "voice/希菲尔/001004200.ogg"
    xfe "{rb}灵纹{/rb}{rt}rune{/rt}会给人们带来伤害。"
    play voice "voice/希菲尔/001004210.ogg"
    xfe "所以，原本身体就很虚弱的千冬你才会陷入沉睡。"
    pause 0.1 hard
    scene set only xfe_cg daze
    with dissolve
    play voice "voice/希菲尔/001004220.ogg"
    xfe "这一切......都是希菲尔的错。"
    play voice "voice/希菲尔/001004230.ogg"
    xfe "希菲尔如果没有和千冬成为朋友的话，你就不会成为{rb}灵继者{/rb}{rt}elfin{/rt}了。"
    show jsqd_dsf_b1 b1 b1_s3 onlayer screens at side_left('jsqd', 0.18), basicfade
    play voice "voice/千冬/771002520.ogg"
    jsqd "小希菲尔......不是这样的。"
    show jsqd_dsf_b1 b1 b1_ga3
    play voice "voice/千冬/771002530.ogg"
    jsqd "我之所以会成为{rb}灵继者{/rb}{rt}elfin{/rt}，是我自己的愿望。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002570.ogg"
    jsqd "我一直都很感谢小希菲尔的。"
    hide jsqd_dsf_b1
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    with slowdissolve
    pause 0.5 hard
    play voice "voice/希菲尔/001004240.ogg"
    xfe "千冬也告诉了希菲尔我很多事情。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004250.ogg"
    xfe "讲了很多很多的故事给希菲尔听。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771002580.ogg"
    jsqd "我记得小希菲尔最喜欢的是北欧神话对吧。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002590.ogg"
    jsqd "妖精和人类和睦相处，温柔的故事。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004260.ogg"
    xfe "......"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771002600.ogg"
    jsqd "也许小希菲尔认为是因为自己的关系才让我变成了{rb}灵继者{/rb}{rt}elfin{/rt}。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002610.ogg"
    jsqd "但即便真是如此，我也很感谢你能让我成为{rb}灵继者{/rb}{rt}elfin{/rt}。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg angry
    with slowdissolve
    pause 0.5 hard
    play voice "voice/希菲尔/001004270.ogg"
    xfe "妖精和人类和睦相处。"
    play voice "voice/希菲尔/001004280.ogg"
    xfe "但最后还是会引发纷争。"
    play voice "voice/希菲尔/001004290.ogg"
    xfe "希菲尔我已经，不希望再有人受到伤害了。"
    play voice "voice/希菲尔/001004300.ogg"
    xfe "哪怕只是一点点，也想早点让这场纷争结束。"
    play voice "voice/希菲尔/001004310.ogg"
    xfe "即使只是像这样出现在你们面前，说不定又会让谁成为{rb}灵继者{/rb}{rt}elfin{/rt}。"
    pause 0.1 hard
    scene set only xfe_cg daze
    with dissolve
    play voice "voice/希菲尔/001004320.ogg"
    xfe "{rb}灵纹{/rb}{rt}rune{/rt}这种东西，就是这样传递下去的......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771002620.ogg"
    jsqd "小希菲尔，这些是从哪里听说的？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004330.ogg"
    xfe "......"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771002640.ogg"
    jsqd "母亲这样说了。{rb}灵纹{/rb}{rt}rune{/rt}是因为心灵相通才诞生的。"
    play voice "voice/千冬/771002650.ogg"
    jsqd "和某人的羁绊交织在一起的时候，就能够从那里获得力量。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771002660.ogg"
    jsqd "超心理学似乎这样认为，复数的意识交汇的话就会出现不可思议的次元显现。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001004340.ogg"
    xfe "这大概是没有错的，因为和希菲尔的关系变得要好了，才害得你们变成了{rb}灵继者{/rb}{rt}elfin{/rt}。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001004360.ogg"
    xfe "没有希菲尔的话，就不会把{rb}灵纹{/rb}{rt}rune{/rt}带来这颗星球了。"
    play voice "voice/希菲尔/001004370.ogg"
    xfe "就不会对凉君和千冬做些过分的事情了。"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771002700.ogg"
    jsqd "小希菲尔，我并没有......"
    me01 "千冬说的没错希菲尔，不是你想的那样。"
    me01 "我们其实......"
    hide jsqd_dsf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004390.ogg"
    xfe "拜拜，凉君。"
    show ts_xfe_yjz_b2 b2 b2_s3
    play voice "voice/希菲尔/001004400.ogg"
    xfe "希菲尔已经，不想再和任何人变得要好了。"
    play voice "voice/希菲尔/001004410.ogg"
    xfe "一人躲猫猫的话，一定更好......"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004420.ogg"
    xfe "所以，凉君你请再忍耐一下。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001004430.ogg"
    xfe "{rb}灵纹{/rb}{rt}rune{/rt}总有一天会融化消散的。"
    play voice "voice/希菲尔/001004440.ogg"
    xfe "只要春天来临的话，就会和这座城市的雪一起——"
    pause 1.0 hard
    hide snow_level1
    stop music fadeout 5.0
    scene white 
    with slowerdissolve
    pause 2.0 hard
    me01 "笨蛋！"
    me01 "不要说这些自以为是的话也没关系的。"
    me01 "不用一个人躲猫猫也没关系的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg touch3
    with slowdissolve
    pause 0.5 hard
    play music second_134 fadein 3.0 if_changed
    play voice "voice/希菲尔/001004450.ogg"
    xfe "......凉君？"
    me01 "如果你想要逃走的话，我就像现在这样抓住你。"
    me01 "如果你想要藏起来的话，不管多少次我都会找到你的。"
    play voice "voice/希菲尔/001004460.ogg"
    xfe "凉君......"
    play voice "voice/希菲尔/001004470.ogg"
    xfe "希菲尔不在的话，会觉得寂寞吗？"
    me01 "这是当然的吧。"
    pause 0.1 hard
    scene set only xfe_cg touch4
    with dissolve
    play voice "voice/希菲尔/001004480.ogg"
    xfe "但是希菲尔我......让凉君有了痛苦的回忆。"
    play voice "voice/希菲尔/001004490.ogg"
    xfe "这一切全都是{rb}灵纹{/rb}{rt}rune{/rt}的错。"
    play voice "voice/希菲尔/001004500.ogg"
    xfe "都是希菲尔的错。"
    me01 "听好了希菲尔，我一直很都很庆幸自己能够拥有这份力量。"
    me01 "也一直很感激能够有像希菲尔你这样的朋友来到我的身边。"
    me01 "我从来没有想过放弃这段羁绊。"
    me01 "也从来没有想过责怪希菲尔你。"
    pause 0.1 hard
    scene set only xfe_cg touch3
    with dissolve
    play voice "voice/希菲尔/001004510.ogg"
    xfe "新的太阳和......新的月亮。"
    play voice "voice/希菲尔/001004520.ogg"
    xfe "一直追赶着的天狗，完成了它的使命。"
    play voice "voice/希菲尔/001004530.ogg"
    xfe "神明崩坏，妖精毁灭，世界将再度被温柔的樱花所笼罩。"
    play voice "voice/希菲尔/001004540.ogg"
    xfe "然后最后的最后，属于人类的时代终将会到来......"
    play voice "voice/希菲尔/001004550.ogg"
    xfe "三年的寒冬过去后，就只剩下人类的繁荣。"
    play voice "voice/希菲尔/001004560.ogg"
    xfe "{rb}灵继者{/rb}{rt}elfin{/rt}褪去了{rb}灵纹{/rb}{rt}rune{/rt}，一切都将回归平静。"
    play voice "voice/希菲尔/001004570.ogg"
    xfe "希菲尔我，想要实现那个预言。"
    play voice "voice/希菲尔/001004580.ogg"
    xfe "为了不让梦里见到的景象变成现实。"
    pause 0.1 hard
    scene set only xfe_cg touch4
    with dissolve
    play voice "voice/希菲尔/001004590.ogg"
    xfe "就让希菲尔来做给你们看。"
    play voice "voice/希菲尔/001004600.ogg"
    xfe "就让我来拯救凉君还有千冬吧。"
    pause 0.1 hard
    scene set only xfe_cg touch2
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001004610.ogg"
    xfe "从千冬那里听到的北欧神话，我要和这最喜欢的故事里说的一样，守护你们的幸福——"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day210.balltower_event01'
    if not seen_day210_balltower_event01:
        $ seen_day210_balltower_event01 = True
    jump day210.map

label day210.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory day outside xuejian
    show snow_level1 onlayer fg
    play music second_114 fadein 3.0 if_changed
    with slowerdissolve
    pause 0.5 hard
    me01 "这里是......"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/白羽/711001510.ogg"
    baiyu "神野君，你果然来了。"
    "眼前的这位应该就是千冬口中的母亲——姬神白羽小姐了吧。"
    "只是没想到所谓的“医院”就是指星天宫研究所。"
    me01 "您一开始就知道我会来这里吗？"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711001520.ogg"
    baiyu "嗯，是千冬告诉我的。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711001530.ogg"
    baiyu "外面很冷先进来说吧，千冬也不要干等着了。"
    me01 "那个，我......"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711001540.ogg"
    baiyu "“我也一起进去真的好吗”你是不是打算这样问？"
    me01 "莫非看穿别人的想法是你们家族的特殊技能吗？！"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711001550.ogg"
    baiyu "我这个和{rb}灵纹{/rb}{rt}rune{/rt}可不一样。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711001560.ogg"
    baiyu "倒不如说我还想把千冬托付给你呢。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside1 xuejian
    with dissolve
    play ambience1 jiaobu2
    pause 2.0 hard
    stop ambience1 fadeout 3.0
    play sound open_door4
    pause 1.0 hard
    play music second_111 fadein 3.0 if_changed
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.3)
    pause 0.5 hard
    play voice "voice/千冬/771000820.ogg"
    jsqd "让你久等了，凉君。"
    me01 "不在床上躺着没问题吗？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show baiyu_yjf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/白羽/711001660.ogg"
    baiyu "为什么突然跑出去了，外面还下着雪。"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771000840.ogg"
    jsqd "还不都是因为母亲老不同意我出门，平时一直宅在这里的缘故。"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771000860.ogg"
    jsqd "那么接下来母亲就回自己的房间吧。"
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711001680.ogg"
    baiyu "欸？"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771000870.ogg"
    jsqd "跟过来可不行，我要和凉君两人独处。"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711001690.ogg"
    baiyu "那等下我送些茶水过去吧。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771000880.ogg"
    jsqd "不需要。这点小事我一个人就能搞定。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711001700.ogg"
    baiyu "那......"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771000890.ogg"
    jsqd "母亲你就一边凉快去，接下来是我和凉君的时间。"
    show baiyu_yjf_b1 b1 b1_s2
    play voice "voice/白羽/711001710.ogg"
    baiyu "......女儿也终于进入叛逆期了。"
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_s2 at walkout_r(0.5)
    play sound jiaobu2
    pause 1.0 hard
    "白羽小姐垂头丧气地离开了。"
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_s3
    play voice "voice/千冬/771000900.ogg"
    jsqd "抱歉呢凉君。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771000910.ogg"
    jsqd "因为母亲的缘故还特地让凉君你等这么久。"
    me01 "不必在意这些。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771000920.ogg"
    jsqd "真是温柔啊。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771000980.ogg"
    jsqd "也能理解为什么小希菲尔会喜欢上你了~"
    pause 1.0 hard
    play sound lunyi
    show jsqd_dsf_b1 b1 b1_n1 at walkout_l(0.3)
    pause 2.0 hard
    hide jsqd_dsf_b1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day210.laboratory_event02:
    $ flcam.move(0, 0, 0)
    play sound open_door4
    scene set only laboratory day bedroom xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771000990.ogg"
    jsqd "凉君，随便找个喜欢的地方坐就好了。"
    "说罢千冬就拿起了一旁的茶壶。"
    me01 "果然还是让我来吧？"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771001000.ogg"
    jsqd "凉君，你果然还是把我当成病人啊。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001010.ogg"
    jsqd "不用说些自以为是的话，交给姐姐我吧~"
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_h1 at walkout_l(0.5)
    pause 0.5 hard
    hide jsqd_dsf_b1
    "看到对方如此坚持，我也只能妥协了。"
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/千冬/771001020.ogg"
    jsqd "今天也很冷呢，给你热茶~"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001030.ogg"
    jsqd "需要姐姐我喂你喝吗？"
    play voice "voice/千冬/771001050.ogg"
    jsqd "我就抱着凉君然后喂你喝吧~"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771001060.ogg"
    jsqd "但是......以我的力气大概很难做到吧。"
    me01 "如果是我抱着千冬姐的话倒是很容易的。"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771001070.ogg"
    jsqd "想要代替我的轮椅吗？"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771001080.ogg"
    jsqd "做那种事的话，我可是要叫警察先生的。"
    me01 "果然这也是犯罪吗......"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771001090.ogg"
    jsqd "是啊，虽然姐姐我可以抱身为弟弟的凉君，但是反过来的话就不被允许。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001100.ogg"
    jsqd "如果说什么也要抱的话，就去找小希菲尔吧。"
    me01 "虽然刚刚的确这么做了......（小声）"
    show jsqd_dsf_b1 b1 b1_ga1
    play voice "voice/千冬/771001110.ogg"
    jsqd "真是犯罪呢......"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001120.ogg"
    jsqd "但如果是姐姐我允许的话，就不算犯罪了哟~"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771001130.ogg"
    jsqd "所以，如果凉君有了喜欢的人必须要告诉姐姐我。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001140.ogg"
    jsqd "姐姐我会决定是否同意的。"
    me01 "如果不同意呢？"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001150.ogg"
    jsqd "那姐姐我就一生一世照顾你啦~"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001190.ogg"
    jsqd "毕竟我的目标是拥有能够把凉君抱起来的力量。"
    me01 "唯独这点还是饶了我吧。"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771001200.ogg"
    jsqd "这个房间不冷吗？"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001210.ogg"
    jsqd "冷的话就和我说，虽然没办法抱起凉君，不过搂在怀里的程度还是可以做得到的。"
    show jsqd_dsf_b1 b1 b1_ga3
    play voice "voice/千冬/771001220.ogg"
    jsqd "现在的雪也开始堆积了，要是小希菲尔也能开心一些的话就更好了。"
    me01 "那么千冬小姐，能进入正题了吗？"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001230.ogg"
    jsqd "嗯，谢谢你陪我聊了这么多。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001250.ogg"
    jsqd "接下来还会去找小希菲尔吗？"
    "我点了点头。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771001260.ogg"
    jsqd "小希菲尔她呢......从我们第一次见面开始就一直和我在一起的。"
    play voice "voice/千冬/771001270.ogg"
    jsqd "无论何时都会陪在我的身边。"
    play voice "voice/千冬/771001280.ogg"
    jsqd "但是......在我沉睡之后，就不知道那孩子去了哪里。"
    show jsqd_dsf_b1 b1 b1_s3
    play voice "voice/千冬/771001290.ogg"
    jsqd "我还没有和任何人说过小希菲尔的事情，就连对母亲也未曾提起。"
    play voice "voice/千冬/771001300.ogg"
    jsqd "醒来的时候似乎还能隐约感觉到她的存在。"
    show jsqd_dsf_b1 b1 b1_n2
    play voice "voice/千冬/771001310.ogg"
    jsqd "但那之后却一次也没能见到她。虽然很期待她会再回来找我，但到刚才为止都未能如愿。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771001320.ogg"
    jsqd "我知道凭我自己是无法找到她的，虽然其中有着很复杂的原因。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001330.ogg"
    jsqd "但就在这个时候，你出现了。"
    play voice "voice/千冬/771001340.ogg"
    jsqd "除我之外又一个，能和小希菲尔成为朋友、与她一起玩耍的人。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001350.ogg"
    jsqd "被小希菲尔喜欢上的——我的弟弟。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001360.ogg"
    jsqd "你刚刚也说了会继续去找小希菲尔，所以我相信你们还能再见面的。"
    show jsqd_dsf_b1 b1 b1_n2
    play voice "voice/千冬/771001370.ogg"
    jsqd "拜托了凉君......如果决定留在希菲尔身边的话，请你连同我的那份一起带上。"
    show jsqd_dsf_b1 b1 b1_s3
    play voice "voice/千冬/771001380.ogg"
    jsqd "小希菲尔之所以不愿回到我身边一定是有她的理由。"
    play voice "voice/千冬/771001390.ogg"
    jsqd "她现在一定......是背负着什么。"
    me01 "希菲尔的事就交给我吧。"
    me01 "千冬姐还是以自己的身体为主。"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771001460.ogg"
    jsqd "凉君，稍微过来一下。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771001480.ogg"
    jsqd "......还够不着。"
    me01 "？"
    $ flcam.move(0, 0, 1100, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771001490.ogg"
    jsqd "凉君，在姐姐我的面前蹲下。"
    me01 "......"
    $ flcam.move(0, 0, 1100, duration=1.5)
    pause 0.5 hard
    play sound hite_light
    show jsqd_dsf_b1 b1 b1_a1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/千冬/771001500.ogg"
    jsqd "嘿！"
    "额头被敲了一下。"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771001510.ogg"
    jsqd "很、很痛吗？"
    me01 "不会。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001520.ogg"
    jsqd "太好了~"
    me01 "这是做什么？"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001530.ogg"
    jsqd "凉君，懂了吗？"
    play voice "voice/千冬/771001540.ogg"
    jsqd "请不要再说些自以为是的话了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play sound touch
    play music second_142 fadein 3.0 if_changed
    "千冬抱住了我。"
    show jsqd_dsf_b1 b1 b1_s1 onlayer screens at side_left('jsqd', 0.18), basicfade
    play voice "voice/千冬/771001550.ogg"
    jsqd "其实我原本是想让你来帮我实现所有的心愿。"
    play voice "voice/千冬/771001560.ogg"
    jsqd "我很不可靠，抱歉......"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001570.ogg"
    jsqd "谢谢你。"
    play voice "voice/千冬/771001580.ogg"
    jsqd "虽然姐姐我这么任性，你却也还是对我温柔以待。"
    hide jsqd_dsf_b1
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory day bedroom xuejian
    with dissolve
    pause 1.0 hard
    "千冬松开了手。"
    "环绕身体的温暖也随之褪去。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771001590.ogg"
    jsqd "这下明白了吗？"
    me01 "千冬姐的身上有很好闻的味道。"
    show jsqd_dsf_b1 b1 b1_ga2
    play voice "voice/千冬/771001600.ogg"
    jsqd "不、不是指这个啦！"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771001610.ogg"
    jsqd "凉君......你还是没明白呢。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771001620.ogg"
    jsqd "再继续这样的话，姐姐我就一个人去找小希菲尔了。"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771001630.ogg"
    jsqd "想让我放弃的话，就得乖乖听话知道吗？"
    me01 "立场突然变得很奇怪。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001640.ogg"
    jsqd "只是回到了姐弟的立场而已~"
    show jsqd_dsf_b1 b1 b1_n2
    play voice "voice/千冬/771001650.ogg"
    jsqd "小希菲尔很擅长躲猫猫，所以只凭凉君一个人的话大概也是很难找到她的。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771001660.ogg"
    jsqd "但是，我们两个人一起的话......一定能比任何人更快地找到她。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771001670.ogg"
    jsqd "这是姐姐的命令哟，弟弟君。"
    me01 "我知道了。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771001680.ogg"
    jsqd "嗯，谢谢你~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory day outside xuejian
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    me01 "......那是？"
    pause 1.0 hard
    play music second_133 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    me01 "好久不见，琉璃。"
    show liuli_dsf_b3 b3 b3_n1
    play voice "voice/琉璃/041402490.ogg"
    liuli "是的~"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041402500.ogg"
    liuli "上次见面也是在新城区对吧？"
    me01 "不介意的话能陪我一会儿吗？这次也想请你充当向导来着。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041402510.ogg"
    liuli "记得上次去了商店街和车站，也就是说接下来要去居民区方向吗？"
    me01 "关于这一点我倒是另有打算。"
    show liuli_dsf_b3 b3 b3_sp1 
    play voice "voice/琉璃/041402520.ogg"
    liuli "去哪里呢？"
    me01 "电波塔的展望台。"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041402530.ogg"
    liuli "......"
    me01 "虽然居民区的夜景也不错，但如果是展望台的话就能看清整座雪见市的全貌了。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041402680.ogg"
    liuli "那个......可以吗？"
    me01 "为什么这么问？"
    play voice "voice/琉璃/041402690.ogg"
    liuli "比起和我，不是应该和立花小姐一起去比较好吗？"
    me01 "倒不如说这样的安排刚好合适。"
    me01 "毕竟立花老师那边我已经打算和她一起去居民区了。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041402700.ogg"
    liuli "......我不会打扰到前辈办事吗？"
    me01 "本来也没有什么事情。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041402710.ogg"
    liuli "是、是这样啊......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day210.laboratory_event01'
    if not seen_day210_laboratory_event01:
        $ seen_day210_laboratory_event01 = True
    jump day210.map

label day210.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg city one
    play music second_133 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041400360.ogg"
    liuli "和之前一样，与前辈并排走的话果然还是这样子比较合适。"
    me01 "又在检查我的脉搏吗？"
    play voice "voice/琉璃/041400370.ogg"
    liuli "是的，因为前辈之前也说不太习惯人群。"
    pause 0.1 hard
    scene set only liuli_cg city two
    with dissolve
    play voice "voice/琉璃/041400380.ogg"
    liuli "为了能立刻诊断出前辈是否觉得难受，所以一定要挽着手才行。"
    "现在的我们在旁人眼里就是一对情侣吧......"
    pause 0.1 hard
    scene set only liuli_cg city three
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041400390.ogg"
    liuli "前辈的心跳好快。"
    pause 0.1 hard
    scene set only liuli_cg city four
    with dissolve
    play voice "voice/琉璃/041400400.ogg"
    liuli "累了吗？"
    me01 "虽然这里人很多，不过这种程度我还是能撑住的。"
    play voice "voice/琉璃/041400410.ogg"
    liuli "没有在勉强自己吗？"
    me01 "不必担心。"
    play voice "voice/琉璃/041400620.ogg"
    liuli "可是心率还在不断地加快。"
    me01 "可能是有些感冒了吧。"
    stop music fadeout 5.0
    pause 0.1 hard
    $ flcam.move(-3200, -2800, 800, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/琉璃/041400640.ogg"
    liuli "要是感冒就不好了，必须立刻进行治疗！"
    pause 1.0 hard
    play music second_106 fadein 3.0 if_changed
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    play sound jump_1
    scene set only liuli_cg street_sd one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041400650.ogg"
    liuli "{size=72}嘿！！！{/size}" with vpunch
    "琉璃将我举了起来。"
    "与她纤细的身材不符，她的力气却大得惊人。"
    me01 "等！？"
    pause 0.1 hard
    scene set only liuli_cg street_sd two
    with dissolve
    play voice "voice/琉璃/041400660.ogg"
    liuli "前辈，请忍耐一下。我现在马上就送你去医院。"
    me01 "等下等下，突然怎么了？"
    play voice "voice/琉璃/041400670.ogg"
    liuli "我把前辈举起来了。"
    me01 "你这是什么怪力啊！！！"
    pause 0.1 hard
    play sound yangmu
    scene set only liuli_cg street_sd three
    with dissolve
    "周围的人都直勾勾地看着我们。"
    "密集的视线使我的人群恐惧症加剧了。"
    pause 0.1 hard
    scene set only liuli_cg street_sd one
    with dissolve
    play voice "voice/琉璃/041400690.ogg"
    liuli "前辈请不要乱动。病人就要好好保持安静才行。"
    play voice "voice/琉璃/041400700.ogg"
    liuli "我能做的就只有尽快送前辈去医院了。"
    me01 "是我不好，感冒只是我骗你的而已，所以快放我下来吧。"
    pause 0.1 hard
    play sound ganga01
    scene set only liuli_cg street_sd four
    with dissolve
    play voice "voice/琉璃/041400720.ogg"
    liuli "是这样吗？可不能勉强自己哟。"
    me01 "完全没有，所以拜托了。"
    "难耐众目睽睽，我最后还是选择了投降。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only street day city3 xuejian
    with slowdissolve
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041400730.ogg"
    liuli "前辈......真的没问题吗？"
    me01 "托你的福这下彻底精神了。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041400740.ogg"
    liuli "前辈......请先不要动。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg city three
    play music second_133 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041400750.ogg"
    liuli "果然是这样，虽然看到前辈的脸那么红我就猜到了，心率又上升了好多。"
    play voice "voice/琉璃/041400760.ogg"
    liuli "体温也很高，必须好好躺在床上休养才行。"
    me01 "所以说我没有生病啦。"
    pause 0.1 hard
    scene set only liuli_cg city four
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041400770.ogg"
    liuli "啊咧？感觉街上的大家都在盯着我们看。"
    me01 "总之还是快点离开这里吧。"
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    with dissolve
    pause 1.0 hard
    "我们到达电波塔的时候已经是晚上了。"
    "在霓虹灯的照耀下整座高塔显得格外耀眼。"
    pause 1.0 hard
    scene set only store night tower xuejian
    $ flcam.moves([
        (0, 0, 0, 0, 0.0, 'linear'),
        (3200, 0, 900, 0, 1.5, 'ease_cubic'),
        (3200, -6000, 900, 0, 8.0, 'ease_cubic')
    ])
    with slowdissolve
    pause 8.0 hard
    "高耸的塔身在雪见市的黑夜中构筑起一道闪烁五彩斑斓的风景线。"
    "这是在樱华镇绝对没有办法欣赏到的景象。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only store night tower xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041400990.ogg"
    liuli "据说这座电波塔是雪见市最高的建筑。"
    show liuli_dsf_b3 b3 b3_h1
    play voice "voice/琉璃/041401020.ogg"
    liuli "和前辈一起度过的这段时光我一辈子都不会忘记。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    play voice "voice/琉璃/041401030.ogg"
    liuli "我希望这些都能永远成为我记忆里的一部分。"
    me01 "到塔顶看看吧，既然是一生中非常珍贵的回忆就应该让它足够完整才行。"
    me01 "不过在此之前先把这件衣服穿上吧，免得着凉了。"
    hide liuli_dsf_b3 with dissolve
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    "我将自己身上携带的校服递给了琉璃。"
    "原本计划是自己独自前往电波塔的，可既然有了琉璃的陪同自然是不能让对方受冻的。"
    "好在琉璃并没有太反对，而是接受了我的好意。"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black with dissolve
    pause 2.0 hard
    scene set only liuli_cg tower one
    play music second_111 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    "夜空中流淌着五光十色的星辰。"
    "站在电波塔顶的我们仿佛置身银河中一般。"
    "比起樱华镇的观景台还要更加地接近星空。"
    play voice "voice/琉璃/041402770.ogg"
    liuli "和前辈一起见证的......这座城市。"
    play voice "voice/琉璃/041402780.ogg"
    liuli "以及与前辈一起仰望的这片星空。"
    play voice "voice/琉璃/041402790.ogg"
    liuli "我绝不会忘记。"
    play voice "voice/琉璃/041402800.ogg"
    liuli "即使不知道属于我自己的时间还有多少。"
    pause 0.1 hard
    scene set only liuli_cg tower three
    with dissolve
    play voice "voice/琉璃/041402810.ogg"
    liuli "但是到最后一刻我也绝不会忘记。"
    pause 0.1 hard
    scene set only liuli_cg tower one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041402820.ogg"
    liuli "因为不想忘记......我像这样许过愿的。"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg center sp snow
    show sepiagrain onlayer fg
    with dissolve
    me01 "琉璃的家是在新城区那头吧？"
    pause 0.1 hard
    scene set only liuli_cg center normal snow
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/040102570.ogg"
    liuli "啊，是这样的。"
    me01 "我还没怎么去过那里，所以比较在意是什么样的地方。"
    play voice "voice/琉璃/040102580.ogg"
    liuli "如果神野前辈有兴趣的话，需要我带路吗？"
    me01 "可以吗？"
    play voice "voice/琉璃/040102670.ogg"
    liuli "是的，什么时间会比较好呢？"
    me01 "这个周末的话......可以吗？"
    pause 0.1 hard
    scene set only liuli_cg center happy snow
    with dissolve
    play voice "voice/琉璃/040102680.ogg"
    liuli "好的，我很乐意~"
    pause 1.0 hard
    hide sepiagrain
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg tower one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041404050.ogg"
    liuli "星空好耀眼......"
    play voice "voice/琉璃/041404060.ogg"
    liuli "特别是在冬天，星星比其他的季节更加的明亮。"
    pause 0.1 hard
    scene set only liuli_cg tower two
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041404070.ogg"
    liuli "即便城市灯火通明，星星也可以像现在这样清晰可见，不会被其他光芒所掩盖。"
    pause 0.1 hard
    scene set only liuli_cg tower three
    with dissolve
    play voice "voice/琉璃/041404090.ogg"
    liuli "所以......那一定是不会感到寂寞的地方吧。"
    pause 0.1 hard
    scene set only liuli_cg tower one
    with dissolve
    play voice "voice/琉璃/041404110.ogg"
    liuli "即使一个人独自踏上前往星之海洋的旅行也......"
    play voice "voice/琉璃/041404120.ogg"
    liuli "一定不会感到寂寞的吧。"
    play voice "voice/琉璃/041410620.ogg"
    liuli "那里一定......是与孤独无缘的地方。"
    pause 0.1 hard
    scene set only liuli_cg tower one
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041410640.ogg"
    liuli "我非常喜欢宇宙中的星辰。"
    play voice "voice/琉璃/041410650.ogg"
    liuli "与霓虹灯不同，间隔遥远的星星可能显得有些寂寞。"
    play voice "voice/琉璃/041410660.ogg"
    liuli "但是它们的光芒，却一直存在着。"
    play voice "voice/琉璃/041410670.ogg"
    liuli "我想那就是最接近永恒的存在吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day210.street_event01'
    if not seen_day210_street_event01:
        $ seen_day210_street_event01 = True
    jump day210.shenshe_event01

label day210.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only party front
    play music first_25 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/圣护院/100001.ogg"
    shy "万夜花小姐，你没在喝酒吗？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show wyh_wnf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/万夜花/140002.ogg"
    wyh "现在不是喝酒的时候吧，我察觉到了不祥的气息。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/100002.ogg"
    shy "就算再颓废好歹也是名神官呢。"
    show wyh_wnf_b1 b1 b1_h1
    play voice "voice/万夜花/140003.ogg"
    wyh "说的没错，所以就算你装傻也没用。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/100003.ogg"
    shy "我可没有装傻。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/100004.ogg"
    shy "对我来说，喝酒就是万夜花小姐工作的全部。"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/140004.ogg"
    wyh "话说你怎么气喘吁吁的。"
    show wyh_wnf_b1 b1 b1_sp1
    play voice "voice/万夜花/140005.ogg"
    wyh "发生什么事了？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/100006.ogg"
    shy "不必担心，我已经派人去确保铃音的安全了。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140006.ogg"
    wyh "果然和小铃有关啊......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/100007.ogg"
    shy "......"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/140007.ogg"
    wyh "对方也是星天宫的巫女吧？"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/100008.ogg"
    shy "嘛，是没错。"
    show wyh_wnf_b1 b1 b1_s3
    play voice "voice/万夜花/140008.ogg"
    wyh "记得之前也见过一次面的。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/100009.ogg"
    shy "是的，这已经不是第一次了，正如万夜花小姐想的那样。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/140011.ogg"
    wyh "谢谢你，暗中保护小铃。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/100012.ogg"
    shy "......"
    show wyh_wnf_b1 b1 b1_ga2
    play voice "voice/万夜花/140012.ogg"
    wyh "虽然作为感谢这些还远远不够，不过我还是希望你能收下我的好意。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/100013.ogg"
    shy "......这么温柔可不像万夜花小姐你。"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/140013.ogg"
    wyh "之前就想问了，我在你心中到底是怎样的啊？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/100014.ogg"
    shy "我的上司。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/100015.ogg"
    shy "而且还是史上最糟糕的......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day210.battle_lingyin_tyt:
    $ flcam.move(0, 0, 0)
    scene set only shenshe night xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    "此时的神社里。"
    show lingyin_wnf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/040161.ogg"
    lingyin "藤原瞳......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    play sound shoot2
    show yumi onlayer texture
    pause 2.0 hard
    play music second_126 fadein 3.0 if_changed
    scene set only sky night moon xuejian
    with slowdissolve
    pause 1.0 hard
    "一道光影划破天际。"
    pause 2.0 hard
    $ flcam.move(0, -300, 900)
    scene set only shenshe night xuejian
    show lingyin_wnf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/青木铃音/040162.ogg"
    lingyin "等你很久了。"
    hide lingyin_wnf_b1
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "从阴影中缓缓走出一个人影。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night moon xuejian
    with dissolve
    pause 1.0 hard
    "在月光下，两人展开了对峙——"
    pause 1.0 hard
    scene set only tyt_cg fight two
    with slowdissolve
    pause 1.0 hard
    play voice "voice/青木铃音/040163.ogg"
    lingyin "原来如此......"
    play voice "voice/青木铃音/040164.ogg"
    lingyin "刚才的光，是弓箭吗。"
    pause 0.1 hard
    play sound yumi
    scene set only tyt_cg fight one
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/藤原瞳/110023.ogg"
    tyt "我听说你负责送还{encyclopedia=xingshen}星神{/encyclopedia}的仪式失败了。"
    play voice "voice/藤原瞳/110024.ogg"
    tyt "而且我还听说，你自己本身也被{rb}灵纹{/rb}{rt}rune{/rt}的力量侵蚀了。"
    pause 0.1 hard
    scene set only tyt_cg fight two
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/040165.ogg"
    lingyin "谁知道呢......我只会执行我自己觉得有价值的任务。"
    pause 0.1 hard
    scene set only tyt_cg fight four
    with dissolve
    play voice "voice/青木铃音/040166.ogg"
    lingyin "明明是凡人的肉体，却拥有着无比坚强的意志并能将其转化成力量。"
    play voice "voice/青木铃音/040167.ogg"
    lingyin "拥有这种程度力量的人，在这片土地上就有四位。"
    pause 0.1 hard
    scene set only tyt_cg fight two
    with dissolve
    play voice "voice/藤原瞳/110025.ogg"
    tyt "水之濑凛、南星万夜花，还有两位是？"
    play voice "voice/青木铃音/040168.ogg"
    lingyin "姐姐和......神野同学。"
    play voice "voice/藤原瞳/110026.ogg"
    tyt "......"
    play voice "voice/青木铃音/040169.ogg"
    lingyin "那位名叫神野凉的人是我很重要的朋友，我想你应该也认识才对。"
    play voice "voice/青木铃音/040170.ogg"
    lingyin "至于姐姐那边的事你想必也早就有所耳闻了吧？"
    play voice "voice/藤原瞳/110028.ogg"
    tyt "据说你的姐姐以前也是星天宫的巫女，而且还参加过祭典的神乐。"
    play voice "voice/藤原瞳/110029.ogg"
    tyt "由于她的能力被总本社认可，才会让她继续接任首席巫女一职的。"
    pause 0.1 hard
    scene set only tyt_cg fight three
    with dissolve
    play voice "voice/藤原瞳/110030.ogg"
    tyt "不过既然已经失败了，那也就到此为止了。"
    play voice "voice/藤原瞳/110031.ogg"
    tyt "执行机构那边已经等得不耐烦了，水之濑那边暂且不说，这些都是队长的意思。"
    play voice "voice/藤原瞳/110032.ogg"
    tyt "我之所以会来就是证据。"
    stop music fadeout 5.0
    play voice "voice/青木铃音/040171.ogg"
    lingyin "话虽如此，你为何不继续刚才的攻击了？"
    play voice "voice/青木铃音/040172.ogg"
    lingyin "还是说除了送还，你还有别的什么目的？"
    play music second_144 fadein 3.0 if_changed
    play voice "voice/青木铃音/040173.ogg"
    lingyin "在我身上有你想要的什么。"
    play voice "voice/藤原瞳/110033.ogg"
    tyt "......"
    play voice "voice/青木铃音/040174.ogg"
    lingyin "没想到你会主动出现在我面前。"
    play voice "voice/青木铃音/040175.ogg"
    lingyin "看到我一个人站在这里，你难道就不觉得这是陷阱吗？"
    play voice "voice/藤原瞳/110035.ogg"
    tyt "我的使命是送还星神。"
    play voice "voice/藤原瞳/110036.ogg"
    tyt "镇压那扭曲人心的力量。"
    pause 0.1 hard
    scene set only tyt_cg fight five
    with dissolve
    play voice "voice/藤原瞳/110037.ogg"
    tyt "我之所以现身，除了讨伐你以外，还必须弄清和你一起的其他巫女情况。"
    play voice "voice/藤原瞳/110038.ogg"
    tyt "除此之外没有其他的理由。"
    pause 0.1 hard
    scene set only tyt_cg fight three
    with dissolve
    play voice "voice/青木铃音/040178.ogg"
    lingyin "那么......想必你也听说了水之濑前辈吧？"
    play voice "voice/藤原瞳/110039.ogg"
    tyt "如果她来了的话，我就不会出现在这里了。"
    play voice "voice/青木铃音/040179.ogg"
    lingyin "......"
    play voice "voice/藤原瞳/110040.ogg"
    tyt "水之濑并不在这里。"
    play voice "voice/藤原瞳/110041.ogg"
    tyt "你说这是陷阱，恐怕也是只是虚张声势罢了。"
    play voice "voice/青木铃音/040180.ogg"
    lingyin "看来你已经把周围的情况摸得一清二楚了啊。"
    play voice "voice/藤原瞳/110042.ogg"
    tyt "为什么你会一个人在这里等我？"
    play voice "voice/青木铃音/040181.ogg"
    lingyin "你觉得我会老实回答你吗？"
    play voice "voice/藤原瞳/110043.ogg"
    tyt "不说的话，就只剩下把你送还这一件事了。"
    play voice "voice/青木铃音/040182.ogg"
    lingyin "到目前为止还没把我送还，是因为你还没有十足的把握击败我吧。"
    play voice "voice/青木铃音/040183.ogg"
    lingyin "所以才会像现在这样拖延时间。"
    play voice "voice/藤原瞳/110044.ogg"
    tyt "......"
    play voice "voice/青木铃音/040184.ogg"
    lingyin "今晚已接近{encyclopedia=manyue}满月{/encyclopedia}，可不要觉得我会这么容易就被击败。"
    play voice "voice/藤原瞳/110045.ogg"
    tyt "......"
    play voice "voice/青木铃音/040185.ogg"
    lingyin "虽说不想上你拖延时间的当，不过我也告诉你我的目的吧。"
    play voice "voice/青木铃音/040186.ogg"
    lingyin "有件事我想托付给你......因为这点我才会来到这里。"
    pause 0.1 hard
    scene set only tyt_cg fight five
    with dissolve
    play voice "voice/青木铃音/040187.ogg"
    lingyin "希望你能告诉我。"
    play voice "voice/青木铃音/040188.ogg"
    lingyin "星天宫总本社那边，你是如何报告我们这里情况的？"
    play voice "voice/藤原瞳/110046.ogg"
    tyt "......"
    pause 0.1 hard
    scene set only tyt_cg fight three
    with dissolve
    play voice "voice/青木铃音/040189.ogg"
    lingyin "如果如实上报的话，就算不是你也会有新的巫女被派来。"
    play voice "voice/青木铃音/040190.ogg"
    lingyin "我们的处境也不会有任何变化。"
    play voice "voice/青木铃音/040191.ogg"
    lingyin "虽然有很多方法避免这一点，但是如果要想要和平地解决，手段就变得极为有限。"
    play voice "voice/青木铃音/040192.ogg"
    lingyin "而且其中靠我自己能够实现的可能性却只有一种。"
    play voice "voice/青木铃音/040193.ogg"
    lingyin "那就是托付给你。"
    play voice "voice/藤原瞳/110047.ogg"
    tyt "......"
    play voice "voice/青木铃音/040194.ogg"
    lingyin "我恳求你，藤原同学。"
    play voice "voice/青木铃音/040195.ogg"
    lingyin "我们并没有与总本社为敌的意思，唯独这一点能否请你转告给那边呢？"
    play voice "voice/青木铃音/040196.ogg"
    lingyin "我们会像至今为止一样继续为星天宫效力。守护星神大人的力量不被坏人利用，我们一族的子子孙孙也都会一直传承下去。"
    play voice "voice/青木铃音/040197.ogg"
    lingyin "若是这样你还要否定我的存在。"
    play voice "voice/青木铃音/040198.ogg"
    lingyin "我也可以随时献上我的生命。"
    play voice "voice/青木铃音/040199.ogg"
    lingyin "但相对的，请你们不要对青木家以及其他相关的人出手。"
    play voice "voice/青木铃音/040201.ogg"
    lingyin "这番话只有从你口中传达给总本社才有意义。"
    play voice "voice/青木铃音/040202.ogg"
    lingyin "现在的青木家，还有水之濑前辈都是总本社怀疑的对象。"
    play voice "voice/青木铃音/040203.ogg"
    lingyin "所以能够依靠的并不是站在我这边的人，而是同样站在总本社立场上的你。"
    play voice "voice/青木铃音/040204.ogg"
    lingyin "拜托了，能不能请你把我刚才说的话传达出去呢？"
    play voice "voice/青木铃音/040205.ogg"
    lingyin "简单来说，这是一场交易。"
    play voice "voice/青木铃音/040206.ogg"
    lingyin "用我的性命，来换取我“家人”的平安。"
    play voice "voice/藤原瞳/110051.ogg"
    tyt "这算不上交易。"
    play voice "voice/藤原瞳/110052.ogg"
    tyt "与你的“家人”无关，我本来就要取你的性命。"
    play voice "voice/青木铃音/040207.ogg"
    lingyin "如果你就这么动手的话，我想水之濑前辈也不会坐视不理的吧。"
    play voice "voice/藤原瞳/110053.ogg"
    tyt "......"
    play voice "voice/青木铃音/040208.ogg"
    lingyin "水之濑前辈绝不会眼睁睁地看着我死去。"
    play voice "voice/青木铃音/040209.ogg"
    lingyin "你会选择现在的现身，不就是因为你还在警惕着其他的巫女吗？"
    play voice "voice/青木铃音/040210.ogg"
    lingyin "无论如何，若日后被水之濑前辈碰见的话，她一定不会手下留情的。"
    play voice "voice/青木铃音/040211.ogg"
    lingyin "怎么样，作为确保你人身安全的条件，能请你接受我的条件吗？"
    play voice "voice/藤原瞳/110054.ogg"
    tyt "这就是你所谓的交易吗？"
    pause 0.1 hard
    scene set only tyt_cg fight five
    with dissolve
    play voice "voice/青木铃音/040212.ogg"
    lingyin "是的，这就是能带来双赢的交易。"
    play voice "voice/藤原瞳/110055.ogg"
    tyt "你的笑容看上去就像隐藏了什么卑鄙的目的一般。"
    play voice "voice/青木铃音/040213.ogg"
    lingyin "被这样评价好受打击......"
    play voice "voice/藤原瞳/110056.ogg"
    tyt "我没有打算和背叛星神之力的你做交易。"
    pause 0.1 hard
    scene set only tyt_cg fight three
    with dissolve
    play voice "voice/青木铃音/040214.ogg"
    lingyin "嘴上这么说，其实你自己也很憎恨星神之力对吧？"
    play voice "voice/藤原瞳/110057.ogg"
    tyt "......"
    play voice "voice/藤原瞳/110058.ogg"
    tyt "在你被送还之后，你的“家人”也不会因此憎恨星神之力吗？"
    play voice "voice/青木铃音/040217.ogg"
    lingyin "是的。"
    play voice "voice/藤原瞳/110059.ogg"
    tyt "你的“家人”不会因为你的死而憎恨总本社吗？"
    play voice "voice/青木铃音/040218.ogg"
    lingyin "我也曾伤害过他们......我想这一点他们也已经有所觉悟了吧。"
    play voice "voice/藤原瞳/110061.ogg"
    tyt "......"
    play voice "voice/青木铃音/040221.ogg"
    lingyin "怎么样，这下能相信我说的话了吗？"
    pause 0.1 hard
    scene set only tyt_cg fight two
    with dissolve
    play voice "voice/藤原瞳/110063.ogg"
    tyt "刚刚的那些都是你的真心？"
    play voice "voice/青木铃音/040223.ogg"
    lingyin "赌上我家族的名誉。"
    play voice "voice/藤原瞳/110064.ogg"
    tyt "真的？"
    play voice "voice/青木铃音/040224.ogg"
    lingyin "是的。"
    play voice "voice/藤原瞳/110066.ogg"
    tyt "你也知道的吧，那位叫雷亚的星神？"
    play voice "voice/青木铃音/040225.ogg"
    lingyin "......"
    play voice "voice/藤原瞳/110067.ogg"
    tyt "你知道的吧？"
    play voice "voice/青木铃音/040226.ogg"
    lingyin "不......我不知道。"
    play voice "voice/青木铃音/040227.ogg"
    lingyin "那恐怕是我们还没有掌握情报的某位星神吧。"
    play voice "voice/青木铃音/040228.ogg"
    lingyin "藤原同学，可以的话请将你知道的关于“雷亚”的情报告诉我。这样的话，我说不定也能......"
    play voice "voice/藤原瞳/110068.ogg"
    tyt "露出狐狸尾巴了呢。"
    play voice "voice/青木铃音/040229.ogg"
    lingyin "......"
    play voice "voice/藤原瞳/110069.ogg"
    tyt "不记得了吗，刚刚从你话中提到的那位名叫“神野凉”的人。"
    play voice "voice/藤原瞳/110070.ogg"
    tyt "那个人与名为“雷亚”的星神缔结了契约。"
    play voice "voice/藤原瞳/110071.ogg"
    tyt "既然是那个人的朋友，身为巫女的你不可能没有察觉。"
    play voice "voice/藤原瞳/110072.ogg"
    tyt "所以你一定是知道“雷亚”的。"
    play voice "voice/藤原瞳/110073.ogg"
    tyt "既然知道，却一直放任不管。"
    play voice "voice/藤原瞳/110074.ogg"
    tyt "你的话里充满了谎言。"
    pause 0.1 hard
    scene set only tyt_cg fight three
    with dissolve
    play voice "voice/藤原瞳/110075.ogg"
    tyt "面对这般花言巧语的你，我是绝不会听从你的条件的。"
    play voice "voice/青木铃音/040230.ogg"
    lingyin "......交易决裂了吗。"
    play voice "voice/藤原瞳/110076.ogg"
    tyt "愚蠢。"
    play voice "voice/藤原瞳/110077.ogg"
    tyt "打从一开始，我就没打算和你做任何交易。"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    stop music fadeout 5.0
    pause 2.0 hard
    
    $ flcam.move(0, 0, 0)
    scene set only fight_cg shenshe2
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        # 角色装备为随机史诗6件，等级6
        tyt_role_mirror.equip_experience = 99999999
        for cate in tyt_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
            sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
            sample_outfit = enemy_outfits[sample_index]
            sample_outfit.init_params()
            for xi in range(5):
                sample_outfit.level_up(tyt_role_mirror, 100)
            sample_outfit.enemy_equip_on(tyt_role_mirror)
        for xi in range(20):
            tyt_role_mirror.skill_levelup()

        ## 必输剧情
        # 我方角色替换为单人青木铃音，装备为随机普通6件，等级6
        lingyin_role_mirror.equip_experience = 99999999
        lingyin_role_mirror.stats_check(to_level=25, limit=True)
        for cate in lingyin_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
            sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
            sample_outfit = enemy_outfits[sample_index]
            sample_outfit.init_params()
            for xi in range(5):
                sample_outfit.level_up(lingyin_role_mirror, 100)
            sample_outfit.enemy_equip_on(lingyin_role_mirror)
        for xi in range(12):
            lingyin_role_mirror.skill_levelup()

        log_party = copy(local_config.party)
        lingyin_role_mirror.pose = "wnf"
        lingyin_role_mirror.xposition = 0.85
        local_config.party = [lingyin_role_mirror]

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=tyt_role_mirror, 
                boss_hp_plus=10000,
                side_enemy=[], 
                side_hp_plus=0,
                level=25,
                boss_first=True, 
                win_condition='must_lose', 
                stay_turn=0, 
                inside_label="inside_battle5", 
                mission_type="normal",
                treasures={
                    "eggs": (2, 0.6),
                    "soul_piece": (2, 0.3),
                    "soul_raise": (2, 0.3),
                    "rock_break_small": (3, 0.3),
                    "rock_break_large": (1, 0.3)
                })

    if _return == "win":
        python:
            lingyin_role_mirror.full_reset(heal_hp=True, ally_environment_effects=None, turn_end=True, level_reset=True)
            local_config.party = log_party
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day210.after_battle_lingyin_tyt

label day210.after_battle_lingyin_tyt:
    scene black
    with slowdissolve
    pause 1.0 hard
    play sound shoot2
    show wflash onlayer texture
    play music second_127 fadein 3.0 if_changed
    "顷刻间，藤原瞳的手中闪过一道光芒。"
    "而另一头铃音则以一个瞬身躲过了飞驰而过的攻击。"
    pause 1.0 hard
    scene set only tyt_cg fight one
    with dissolve
    play voice "voice/藤原瞳/110078.ogg"
    tyt "白费力气！"
    play sound yumi
    $ flcam.move(-1100, -1400, 450, duration=1.5, waper='ease_quad')
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowdissolve
    play sound shoot3
    show yumi_multi onlayer texture
    pause 1.0 hard
    scene set only sky night moon xuejian
    with slowdissolve
    pause 1.0 hard
    "没有给铃音任何喘息的机会，数支箭矢接踵而至。"
    "宛如怒涛般的连射。"
    "以藤原瞳为中心，数道光点不停地闪烁着。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    play sound yumi
    pause 1.0 hard
    scene set only tyt_cg fight three
    with slowdissolve
    pause 0.5 hard
    play voice "voice/青木铃音/040231.ogg"
    lingyin "这是......陨铁做成的箭矢。"
    play voice "voice/青木铃音/040232.ogg"
    lingyin "这些......全部都是！？"
    play voice "voice/藤原瞳/110090.ogg"
    tyt "陨铁并不是能够量产的矿石，我也只是在其中混杂了一些真货罢了。"
    play voice "voice/青木铃音/040233.ogg"
    lingyin "想利用电磁波的干扰吗。"
    "陨铁打造的箭矢散发着强烈的磁场。"
    "对同样是由陨铁打造的薙刀具有很强的引力作用。"
    "此刻铃音只感觉手中的薙刀犹如岩石般沉重。"
    "哪怕只是稍微挥舞都要花费相当大的力气。"
    play voice "voice/藤原瞳/110091.ogg"
    tyt "这个包围阵的磁场，覆盖着半径500米的范围。"
    play voice "voice/藤原瞳/110092.ogg"
    tyt "只要有那么大范围的话......"
    play sound yumi
    play voice "voice/藤原瞳/110093.ogg"
    tyt "就算是鬼神也无法跳脱！"
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900)
    scene set only shenshe night xuejian
    show tyt_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    with dissolve
    play voice "voice/藤原瞳/110094.ogg"
    tyt "虽说也费了一番周折。"
    play voice "voice/藤原瞳/110095.ogg"
    tyt "不过我已经不会再让你逃走了。"
    play voice "voice/藤原瞳/110096.ogg"
    tyt "所以......"
    stop music fadeout 5.0
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    play voice "voice/水之濑/100047.ogg"
    stranger "不过那也只是在一对一的前提下吧！"
    show tyt_wnf_b1 b1 b1_a2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/藤原瞳/110097.ogg"
    tyt "{size=72}！！！{/size}"
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.75 alpha 1
    pause 2.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    scene white 
    with dissolve
    pause 1.0 hard
    play music second_145 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only tyt_cg fight seven
    with slowerdissolve
    pause 0.5 hard
    play voice "voice/水之濑/100048.ogg"
    szl "拉开和我的距离吗，正确的判断。"
    "面对突然出现的水之濑凛，藤原瞳的脸上露出了前所未有的恐惧。"
    "巫女之间也有相性克制，擅长使用居合道进行中距离作战的水之濑在战斗中完美地克制了使用弓箭的藤原瞳。"
    show lingyin_wnf_b2 b2 b2_sp1 onlayer screens at side_right('lingyin'), basicfade
    play voice "voice/青木铃音/040235.ogg"
    lingyin "水之濑前辈......"
    hide lingyin_wnf_b2
    play voice "voice/水之濑/100049.ogg"
    szl "还没回总本社去吗，无论你怎么坚持结果都是一样的。"
    play voice "voice/藤原瞳/110098.ogg"
    tyt "......"
    play voice "voice/水之濑/100050.ogg"
    szl "你的目的也已经达到了吧，还是说你有什么无论如何也要找铃音的理由吗？"
    pause 0.1 hard
    scene set only tyt_cg fight six
    with dissolve
    play voice "voice/藤原瞳/110099.ogg"
    tyt "......"
    play voice "voice/水之濑/100051.ogg"
    szl "是对{encyclopedia=lingji}星神灵基{/encyclopedia}的仇视吗？"
    "藤原瞳屏住呼吸。"
    "紧握弓箭的手也开始颤抖起来。"
    play voice "voice/水之濑/100052.ogg"
    szl "灵力出众的你，从理论上来说使用弓箭也非常合适。"
    play voice "voice/水之濑/100053.ogg"
    szl "就算对方遮蔽气息，你也能凭直觉进行狙击。"
    play voice "voice/水之濑/100054.ogg"
    szl "不如说对于此刻神灵之力凭依的铃音来说更是如此。"
    play voice "voice/水之濑/100055.ogg"
    szl "但是想必你也已经知道，这些伎俩对我是不管用的。"
    play voice "voice/水之濑/100056.ogg"
    szl "对擅长远距离作战的你而言，擅长中距离战斗的我可以说是你的天敌。"
    pause 0.1 hard
    scene set only tyt_cg fight eight
    with dissolve
    play voice "voice/水之濑/100057.ogg"
    szl "更何况，你的身手比我想象的还要迟钝。"
    play voice "voice/藤原瞳/110100.ogg"
    tyt "......"
    pause 0.1 hard
    scene set only tyt_cg fight seven
    with dissolve
    play voice "voice/水之濑/100059.ogg"
    szl "所以你也应该明白的吧？这一切意味着什么。"
    play voice "voice/水之濑/100060.ogg"
    szl "伤害了铃音的你，总有一天会被我抓住。"
    play voice "voice/水之濑/100061.ogg"
    szl "不管是白天还是黑夜，不管你藏在哪里，慢吞吞的你一定会被我抓住。"
    play voice "voice/藤原瞳/110101.ogg"
    tyt "慢吞吞慢吞吞的，真是烦人！"
    pause 0.1 hard
    scene set only tyt_cg fight nine
    with dissolve
    play voice "voice/水之濑/100062.ogg"
    szl "终于生气了吗~"
    play voice "voice/藤原瞳/110102.ogg"
    tyt "......"
    play voice "voice/水之濑/100063.ogg"
    szl "不过也没什么好在意的，脚上功夫的差距只是锻炼的程度不同而已。"
    play voice "voice/水之濑/100065.ogg"
    szl "我承认你有才能，但是你应该也很清楚，凭现在的你还无法战胜我。"
    play voice "voice/水之濑/100066.ogg"
    szl "我说的没错吧，不成熟的可爱后辈。"
    play voice "voice/藤原瞳/110103.ogg"
    tyt "......"
    play voice "voice/水之濑/100067.ogg"
    szl "正值叛逆期的，爱逞强的大小姐。"
    play voice "voice/藤原瞳/110104.ogg"
    tyt "{size=72}！！！{/size}"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg shenshe2
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        ## 敌方初始化参数
        # Boss为藤原瞳，巫女个数2，所有敌方角色技能等级8，装备“稀有”随机等级5装备6件
        enemy_roles = [tyt_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
        for role in enemy_roles:
            role.equip_experience = 99999999
            for cate in role.outfits:
                enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                sample_outfit = enemy_outfits[sample_index]
                sample_outfit.init_params()
                for xi in range(4):
                    sample_outfit.level_up(role, 100)
                sample_outfit.enemy_equip_on(role)
            for xi in range(8):
                role.skill_levelup()

        # 水之濑凛加入我方战斗，且初始位置为3号位置；角色技能等级满级，水之濑装备为传说6件秋之韵-素律、雷伤套
        selected_equipments_szl = ["weapon_num11_04", 
                                   "armor_num11_04", 
                                   "necklace_num11_04", 
                                   "ring_num11_04",
                                   "magic_light_04",
                                   "stone_light_04"]
        szl_role_mirror.equip_experience = 99999999
        szl_role_mirror.stats_check(to_level=25, limit=True)
        for cate in szl_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments_szl and outfit.category == cate)]
            sample_outfit = enemy_outfits[0]
            sample_outfit.init_params()
            for xi in range(9):
                sample_outfit.level_up(szl_role_mirror, 100)
            sample_outfit.enemy_equip_on(szl_role_mirror)
        for xi in range(20):
            szl_role_mirror.skill_levelup()
        
        szl_role_mirror.pose = 'sf'
        lingyin_role.pose = "wnf"
        for role in copy(local_config.party)[:5]:
            if role.name == "雷亚":
                temp_selected_skills, temp_selected_skills_v2 = role.skills, role.skills_v2
                before_battle_general_attack = [s for s in temp_selected_skills if s.category == "General_attack"][0]
                before_battle_general_attack_v2 = [s for s in temp_selected_skills_v2 if s.category == "General_attack"][0]
                now_battle_general_attack = copy(getattr(store, "psychokinesis-fire"))
                for xi in range(before_battle_general_attack.level - 1):
                    now_battle_general_attack.level_change(now_battle_general_attack.level + 1)
                role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                role.base_skills = role.skills
                role.skills_v2 = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills_v2]
                role.base_skills_v2 = role.skills_v2
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

        local_config.party.insert(2, szl_role_mirror)

        # 初始化“瓦轮刑部”场地buff
        local_config.tutorial_step = "瓦轮刑部"

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=tyt_role_mirror, 
                boss_hp_plus=35000,
                side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                side_hp_plus=10000,
                level=25,
                boss_first=True, 
                win_condition='normal',
                stay_turn=0,
                inside_label="inside_battle6", 
                mission_type="normal", 
                treasures={
                    "eggs": (3, 0.6),
                    "mana_eggs": (1, 0.3),
                    "soul_piece": (5, 0.3),
                    "soul_raise": (5, 0.3),
                    "rock_break_small": (5, 0.3),
                    "rock_break_large": (3, 0.3)
                })

    if _return == "win":
        "战斗胜利！"
        python:
            szl_role_mirror.full_reset(heal_hp=True, ally_environment_effects=None, turn_end=True, level_reset=True)
            for role in copy(local_config.party):
                if role.name == "雷亚":
                    role.skills = [s if s.category != "General_attack" else before_battle_general_attack for s in role.skills]
                    role.base_skills = role.skills
                    role.skills_v2 = [s if s.category != "General_attack" else before_battle_general_attack_v2 for s in role.skills_v2]
                    role.base_skills_v2 = role.skills_v2
                if role.name == "青木铃音":
                    role.pose = "default"
                if role.objectname == "szl_role_mirror":
                    local_config.party.remove(role)

            if "tyt_role" not in local_config.role_pool:
                local_config.role_pool.add("tyt_role")

        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day210.after_battle_szl_tyt

label day210.after_battle_szl_tyt:
    scene black
    with slowdissolve
    pause 1.0 hard
    play sound yumi
    scene set only tyt_cg fight one
    play music second_145 fadein 3.0 if_changed
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    scene black 
    with slowdissolve
    play sound shoot2
    show yumi onlayer texture
    pause 0.5 hard
    "箭矢不断从藤原瞳手中射出。"
    "比之前的速度还要快，看得出之前的射击是有所保留的。"
    "面对自己没有把握战胜的敌人，藤原瞳选择使出自己的全部实力。"
    "可即便如此......"
    pause 1.0 hard
    $ flcam.move(2200, -2800, 800)
    scene set only tyt_cg fight nine
    with slowdissolve
    pause 0.5 hard
    play voice "voice/水之濑/100068.ogg"
    szl "{size=72}太慢了！{/size}"
    pause 0.2 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    scene white 
    with dissolve
    pause 1.0 hard
    "这全力的一击竟被水之濑轻而易举就斩断了。"
    "顾不上多想，藤原瞳转身就朝不远处的丛林方向逃去。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only shenshe night xuejian
    with dissolve
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_wnf_b1 b1 b1_a2 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/040236.ogg"
    lingyin "瞳小姐！"
    play voice "voice/青木铃音/040237.ogg"
    lingyin "难道你就不想和我们一起守护人类的未来吗？"
    $ flcam.move(0, 0, 600, duration=1.5)
    show tyt_wnf_b1 b1 b1_s3 onlayer m2 at walkin_r(0.3)
    pause 0.5 hard
    "听到铃音的呼喊，藤原瞳停下了脚步。"
    play voice "voice/藤原瞳/110105.ogg"
    tyt "我已经......连去守护的资格没有了。（小声）"
    hide lingyin_wnf_b1
    show lingyin_wnf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/040238.ogg"
    lingyin "这是什么意思？"
    show tyt_wnf_b1 b1 b1_s1
    tyt "......"
    pause 1.0 hard
    play sound jiaobu2
    show tyt_wnf_b1 b1 b1_s1 at walkout_l(0.3)
    pause 1.0 hard
    $ flcam.move(4500, -300, 900, duratino=1.5)
    show lingyin_wnf_b2 b2 b2_a1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/青木铃音/040239.ogg"
    lingyin "瞳小姐！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    play voice "voice/天使莲/170082.ogg"
    stranger "路过打个酱油~"
    show tyt_wnf_b1 b1 b1_a2 onlayer screens at side_left('tyt'), basicfade
    play voice "voice/藤原瞳/110161.ogg"
    tyt "{size=72}什？！{/size}"
    hide tyt_wnf_b1
    pause 0.5 hard
    play sound hite_knife
    show bslash1 onlayer texture
    with vpunch
    pause 1.0 hard
    "一道明亮的光影划过了藤原瞳的胸口。"
    "此刻她的身体正向前扑倒。"
    "紧束的头发也因刚刚的一击撒乱开来。"
    pause 0.5 hard
    scene white 
    with slowerdissolve
    play music first_31 fadein 3.0 if_changed
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only kls_cg happy
    with slowdissolve
    pause 0.5 hard
    play voice "voice/天使莲/170083.ogg"
    ts_lian "掉以轻心可不行。"
    pause 1.0 hard
    scene set only tyt_cg end three
    with slowdissolve
    pause 0.5 hard
    play voice "voice/藤原瞳/110162.ogg"
    tyt "......骗、骗人。"
    play voice "voice/藤原瞳/110163.ogg"
    tyt "又一位......星神。"
    pause 0.5 hard
    scene set only kls_cg normal
    with dissolve
    pause 0.5 hard
    play voice "voice/天使莲/170084.ogg"
    ts_lian "这孩子......好像晕过去了。"
    pause 1.0 hard
    scene set only tyt_cg end one
    with dissolve
    play voice "voice/藤原瞳/110164.ogg"
    tyt "哥哥......"
    "藤原瞳的嘴角微微动了下。"
    "此时从她的眼角渗出了晶莹的泪水。"
    pause 0.1 hard
    scene set only tyt_cg end two
    with dissolve
    play voice "voice/藤原瞳/110165.ogg"
    tyt "不要走......哥哥。"
    play voice "voice/藤原瞳/110166.ogg"
    tyt "这里......是哪里？"
    play voice "voice/藤原瞳/110167.ogg"
    tyt "好黑啊......好可怕。"
    play voice "voice/藤原瞳/110168.ogg"
    tyt "你在哪里......哥哥。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 3.0 hard

label day210.shenshe_event02:
    $ flcam.move(0, 0, 0)
    scene set only party front
    $ flcam.move(0, -200, 600, duration=1.5)
    with slowdissolve
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    show wyh_wnf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play music second_125 fadein 3.0 if_changed
    pause 1.0 hard
    play voice "voice/神野大和/180002.ogg"
    dh "我之前就有种不好的预感。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140049.ogg"
    wyh "嘛......也只有在发生坏事的时候才能和“老师”你见面。"
    hide wyh_wnf_b1
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/170001.ogg"
    ts_lian "其他的巫女还会出现吗？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show wyh_wnf_b1 b1 b1_s2 onlayer m1:
        xpos 0.7
    play voice "voice/万夜花/140050.ogg"
    wyh "谁知道呢，说不定这件事已经引起总本社的注意了，毕竟对方之前也在追查水之濑的下落。"
    show wyh_wnf_b1 b1 b1_s3
    play voice "voice/万夜花/140051.ogg"
    wyh "比起这个莲，你自己也要小心才行。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/170002.ogg"
    ts_lian "嗯......"
    play voice "voice/万夜花/140052.ogg"
    wyh "向你们报告这件事，也是为了提醒你。"
    hide ts_lian_ssz_b1
    hide wyh_wnf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n3 onlayer m1:
        xpos 0.3
    play voice "voice/神野大和/180003.ogg"
    dh "在关心莲和雷亚之前，你那边怎么样了？"
    $ flcam.move(0, -200, 600, duration=1.5)
    show wyh_wnf_b1 b1 b1_n1 onlayer m1:
        xpos 0.7
    play voice "voice/万夜花/140054.ogg"
    wyh "小铃身边有我和水之濑跟着，莲只要跟着老师的话应该也没有什么问题吧。"
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/180004.ogg"
    dh "感谢你多余的忠告。"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/140055.ogg"
    wyh "雷亚那边有神野凉在，这一点自然也是没问题的。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140056.ogg"
    wyh "原本这场骚乱的罪魁祸首就是星天宫与天使之间的积怨，要是把你们也卷进来的话......"
    hide dh_zf_b1
    hide wyh_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    show ts_lian_ssz_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/170003.ogg"
    ts_lian "我觉得大和君想说的应该不是这些。"
    stop music fadeout 5.0
    $ flcam.move(2250, 0, 750, duration=1.5)
    show wyh_wnf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.7
    pause 0.5 hard
    play voice "voice/万夜花/140057.ogg"
    wyh "那是什么？"
    play music first_30 fadein 3.0 if_changed
    hide ts_lian_ssz_b1
    hide wyh_wnf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    show dh_zf_b1 b1 b1_n1 onlayer m1:
        xpos 0.3
    play voice "voice/神野大和/180005.ogg"
    dh "我问的“你那边怎么样”，是指你真的还要继续肩负星天宫神官这一职吗？"
    $ flcam.move(0, -200, 600, duration=1.5)
    show wyh_wnf_b1 b1 b1_s1 onlayer m1:
        xpos 0.7
    play voice "voice/万夜花/140058.ogg"
    wyh "......"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/180006.ogg"
    dh "就算一两次顺利地隐瞒过去，也不表示事情会因此而结束不是吗？"
    play voice "voice/神野大和/180007.ogg"
    dh "对方回到星天宫之后，还是会派第二、第三位巫女来吧？"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/140059.ogg"
    wyh "也许就正如你说的那样吧。"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/180008.ogg"
    dh "你也犯不着那么老实地去硬撑。"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/万夜花/140060.ogg"
    wyh "老师你的话会怎么做？"
    play voice "voice/万夜花/140061.ogg"
    wyh "要我带上家人一起，离开雪见市比较好吗？"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/180009.ogg"
    dh "......"
    show wyh_wnf_b1 b1 b1_ga2
    play voice "voice/万夜花/140062.ogg"
    wyh "其实，我相公也说了同样的话。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140063.ogg"
    wyh "相公也是第一次对星天宫的做法提出意见。"
    play voice "voice/万夜花/140064.ogg"
    wyh "可见这次的事情，让他多么担心。"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/140066.ogg"
    wyh "毕竟会提出搬家也是为了儿女着想。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/180010.ogg"
    dh "不只是这样而已，他也在为你着想。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140067.ogg"
    wyh "......"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/180011.ogg"
    dh "不仅仅是你的孩子们，你自己的处境也很危险。"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/140068.ogg"
    wyh "也是呢......考虑到这边战力的话，面对总本社的众人还是太过弱小了。"
    hide wyh_wnf_b1
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/170004.ogg"
    ts_lian "即使如此，你还是会犹豫要不要离开吗？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show wyh_wnf_b1 b1 b1_s2 onlayer m1:
        xpos 0.7
    play voice "voice/万夜花/140069.ogg"
    wyh "那是当然的，如果我们就这样离开了雪见市，每年的夏日祭典怎么办啊？"
    hide wyh_wnf_b1 
    hide ts_lian_ssz_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    show dh_zf_b1 b1 b1_a1 onlayer m1:
        xpos 0.3
    play voice "voice/神野大和/180012.ogg"
    dh "比起担心这个，先考虑自己吧。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show wyh_wnf_b1 b1 b1_s1 onlayer m1:
        xpos 0.7
    play voice "voice/万夜花/140070.ogg"
    wyh "我这不是失业了嘛。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/180013.ogg"
    dh "那样的话来我这里帮忙如何？"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/140071.ogg"
    wyh "我的相公不也会受到牵连了吗？"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/180015.ogg"
    dh "原来如此。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/180016.ogg"
    dh "你也不希望离开雪见市。"
    play voice "voice/神野大和/180017.ogg"
    dh "那么地......喜欢这座城市啊。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140073.ogg"
    wyh "......"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/180018.ogg"
    dh "你的相公、孩子们一定也是一样的。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/180019.ogg"
    dh "大家都是因为喜欢着这里，才会感到迷茫的吧。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day210.shenshe_event03:
    $ flcam.move(0, 0, 0)
    scene set only shenshe night xuejian
    with dissolve
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_ga3 onlayer m1:
        xpos 0.5
    play voice "voice/神野大和/180020.ogg"
    dh "我说莲......"
    play voice "voice/神野大和/180021.ogg"
    dh "你觉得万夜花她是在任性吗？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.7
    play voice "voice/天使莲/170005.ogg"
    ts_lian "......"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/180022.ogg"
    dh "比起使命，家人的安危还是更加重要的吧？"
    play voice "voice/神野大和/180023.ogg"
    dh "就算不惜让家人冒着危险......"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/170006.ogg"
    ts_lian "我也不是很明白。"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170007.ogg"
    ts_lian "不过......她是个废柴人类。"
    show ts_lian_ssz_b1 b1 b1_h1
    play voice "voice/天使莲/170008.ogg"
    ts_lian "所以我最喜欢她了~"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/180024.ogg"
    dh "是吗。"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170009.ogg"
    ts_lian "是的，就像喜欢大和君一样。"
    play voice "voice/神野大和/180025.ogg"
    dh "你的最喜欢，还真是让人搞不懂。"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/170010.ogg"
    ts_lian "后悔了吗？"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/170011.ogg"
    ts_lian "大和君如果当初没有把我唤醒的话，就不会被卷入这样的麻烦里了。"
    play voice "voice/天使莲/170012.ogg"
    ts_lian "就能作为一名普通的教授......自然地生活下去了。"
    play voice "voice/天使莲/170013.ogg"
    ts_lian "也就不用失去{encyclopedia=kasumi}霞{/encyclopedia}了......"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/180026.ogg"
    dh "打住了。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/180027.ogg"
    dh "就算重来一遍，我和霞都依旧会选择那么做的。"
    play voice "voice/天使莲/170014.ogg"
    ts_lian "大和君你......其实也不想和她分开的。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/180028.ogg"
    dh "已经，足够了......"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/180029.ogg"
    dh "我并没有后悔，相反我还得感谢你。"
    play voice "voice/神野大和/180030.ogg"
    dh "那时候的我们对着流星许愿了。"
    play voice "voice/神野大和/180031.ogg"
    dh "而你也回应了我们的愿望，降临到我们身边。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/170015.ogg"
    ts_lian "正确的来说，因为大和君无论如何都没有办法独立生活，所以我才勉为其难陪在你身边的。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/180032.ogg"
    dh "现在也是你让我有了新的羁绊。"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170016.ogg"
    ts_lian "我们要永远在一起......"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/180033.ogg"
    dh "是啊。"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/170017.ogg"
    ts_lian "一直在一起......也可以吗？"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/180034.ogg"
    dh "这么问可不符合你的性格啊，废柴宇宙人。"
    show ts_lian_ssz_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/天使莲/170018.ogg"
    ts_lian "才不是这样，真叫人火大！"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/180035.ogg"
    dh "正是这样的你，我才更加喜欢。"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/170019.ogg"
    ts_lian "......"
    play voice "voice/神野大和/180036.ogg"
    dh "铃音的身边有万夜花作为家人陪着。"
    play voice "voice/神野大和/180037.ogg"
    dh "雷亚身边有凉陪着。"
    play voice "voice/神野大和/180038.ogg"
    dh "而你身边，有我在......"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/180039.ogg"
    dh "所以，就由我来守护你吧。"
    play voice "voice/天使莲/170020.ogg"
    ts_lian "......"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/180040.ogg"
    dh "我会先从不拖你后腿的程度开始努力的。"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170021.ogg"
    ts_lian "大和君什么都不用做。"
    hide dh_zf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    show ts_lian_ssz_b1 b1 b1_h1
    play voice "voice/天使莲/170022.ogg"
    ts_lian "只要一直陪在我的身边......就足够了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day210.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only home day my_room xuejian alpha
    $ flcam.move(0, -100, 400, duration=1.5)
    with slowdissolve
    pause 1.0 hard
    play voice "voice/青木铃音/040321.ogg"
    stranger "好像醒过来了。"
    play voice "voice/翔子/030218.ogg"
    stranger "感觉怎么样？藤原同学？"
    play music first_26 fadein 3.0 if_changed
    $ flcam.move(2250, -350, 750, duration=1.5)
    show lingyin_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    show xz_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    pause 0.5 hard
    play voice "voice/翔子/030219.ogg"
    xz "难道是肚子饿了吗？"
    show lingyin_dsf_b2 b2 b2_h1
    play voice "voice/青木铃音/040322.ogg"
    lingyin "我去拿点什么吃的来吧。"
    play voice "voice/藤原瞳/110169.ogg"
    tyt "......"
    hide xz_dsf_b1
    hide lingyin_dsf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/藤原瞳/110170.ogg"
    tyt "这里是？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b1 b1 b1_h1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030222.ogg"
    xz "这是我家，藤原同学去学校的时候也会从这里经过的吧？"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/110171.ogg"
    tyt "......"
    $ flcam.move(0, -200, 600, duration=1.5)
    show lingyin_dsf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.7
    play voice "voice/青木铃音/040323.ogg"
    lingyin "是不是应该联系她的家人更好呢？"
    hide xz_dsf_b1
    show xz_dsf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030223.ogg"
    xz "在那之前我还想和藤原瞳小姐谈谈，我有话想问你。"
    show tyt_wnf_b1 b1 b1_n2
    tyt "......"
    hide lingyin_dsf_b2
    $ flcam.move(-2250, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/030224.ogg"
    xz "藤原同学，你是不是......经常在外面露宿？"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_h1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030225.ogg"
    xz "身上非常的脏。"
    stop music fadeout 5.0
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/110172.ogg"
    tyt "......欸？"
    play music first_13 fadein 3.0 if_changed
    hide xz_dsf_b3
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lingyin_dsf_b2 b2 b2_h1 onlayer m1:
        xpos 0.7
    play voice "voice/青木铃音/040324.ogg"
    lingyin "在藤原同学睡着的时候，我和姐姐帮你擦过身子了。"
    play voice "voice/青木铃音/040325.ogg"
    lingyin "把你整个脱光了一次~"
    play voice "voice/藤原瞳/110173.ogg"
    tyt "......"
    hide lingyin_dsf_b2
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030226.ogg"
    xz "话说藤原同学你怎么没穿内衣。"
    play voice "voice/藤原瞳/110174.ogg"
    tyt "......"
    hide xz_dsf_b1
    show xz_dsf_b3 b3 b3_s4 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030227.ogg"
    xz "不仅仅是上面，就连下面也是......让我有点吃惊啊。"
    hide xz_dsf_b3
    hide tyt_wnf_b1
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show tyt sd1 onlayer b2_c2u:
        xpos 0.175
        zoom 1.3
    pause 1.0 hard
    play voice "voice/青木铃音/040326.ogg"
    lingyin "真空的巫女小姐呢~"
    play voice "voice/翔子/030228.ogg"
    xz "......你稍微闭嘴啦。"
    hide tyt sd1
    pause 1.5 hard
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.3
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/030229.ogg"
    xz "藤原同学，不管是不是因为穿和服的缘故，不过你在发育途中还是穿上比较好。"
    play voice "voice/藤原瞳/110175.ogg"
    tyt "Ho......Ho......"
    show xz_dsf_b2 b2 b2_sp1
    play voice "voice/翔子/030230.ogg"
    xz "Ho？"
    $ flcam.move(0, -200, 600, duration=1.5)
    show lingyin_dsf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.7
    play voice "voice/青木铃音/040327.ogg"
    lingyin "{rb}煎饼{/rb}{rt}Hot Cake{/rt}吗？"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/110176.ogg"
    tyt "请、请别管我......"
    hide xz_dsf_b2
    show xz_dsf_b1 b1 b1_h1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030231.ogg"
    xz "什么嘛，不也是能有这种可爱的表情吗~"
    show lingyin_dsf_b2 b2 b2_h1
    play voice "voice/青木铃音/040328.ogg"
    lingyin "总觉得让人松了口气呢。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/110177.ogg"
    tyt "因、因为暖气......太热了的关系。"
    play voice "voice/青木铃音/040329.ogg"
    lingyin "浴室的话你也可以用~"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/110178.ogg"
    tyt "我、我去澡堂洗......"
    hide xz_dsf_b1
    show xz_dsf_b3 b3 b3_s1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030232.ogg"
    xz "就算是这样，继续睡在外面的话就没有意义了。"
    play voice "voice/翔子/030233.ogg"
    xz "而且......雪见市的冬天很冷的。"
    show lingyin_dsf_b2 b2 b2_n1
    play voice "voice/青木铃音/040330.ogg"
    lingyin "这个季节还在外面露宿，和自杀没什么差别。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/110179.ogg"
    tyt "没什么......习惯了以后根本没什么大不了的。"
    hide xz_dsf_b3
    show xz_dsf_b1 b1 b1_a1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030234.ogg"
    xz "就是因为你这么想，才会晕过去不是吗？"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/110180.ogg"
    tyt "......"
    hide xz_dsf_b1
    show xz_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030235.ogg"
    xz "藤原同学，能再问你一个问题吗？不过如果你想要先洗澡的话也没关系。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/110181.ogg"
    tyt "没、没人说要去洗......"
    show lingyin_dsf_b2 b2 b2_h1
    play voice "voice/青木铃音/040331.ogg"
    lingyin "还是说想要吃点什么？藤原同学果然还想要吃煎饼的吧？"
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/110182.ogg"
    tyt "我、我可没说......"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030236.ogg"
    xz "藤原同学，不用勉强自己也没关系的。不然会像水之濑前辈那样被排挤的。"
    show lingyin_dsf_b2 b2 b2_ga3
    play voice "voice/青木铃音/040332.ogg"
    lingyin "要是被本人听到的话可真的会生气了呢。"
    hide lingyin_dsf_b2
    hide xz_dsf_b3
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/110183.ogg"
    tyt "总、总之，我没什么可以跟你们说的......"
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/110184.ogg"
    tyt "我是你们的敌人，能像这样轻松地对话也就只有现在了。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/110185.ogg"
    tyt "没能彻底击败我算是你们的失策，只要我恢复了元气，立刻就能把你们......"
    hide tyt_wnf_b1
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show tyt sd1 onlayer b2_c2u:
        xpos 0.175
        zoom 1.3
    pause 1.0 hard
    play voice "voice/青木铃音/040333.ogg"
    lingyin "就凭你的真空穿搭吗？"
    play voice "voice/藤原瞳/110186.ogg"
    tyt "和、和这个没关系吧。"
    pause 0.1 hard
    show tyt sd2
    play voice "voice/藤原瞳/110187.ogg"
    tyt "冷静下来......深呼吸。"
    play voice "voice/翔子/030237.ogg"
    xz "这孩子，好可爱。"
    pause 0.1 hard
    show tyt sd3
    play voice "voice/藤原瞳/110188.ogg"
    tyt "快变回来......平时的我。"
    pause 0.1 hard
    hide tyt sd3
    pause 1.5 hard
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    show xz_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030238.ogg"
    xz "不如说，这才是真正的你不是吗？"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/110189.ogg"
    tyt "欸？"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030239.ogg"
    xz "我听说你好像隐瞒了自己的过去。可这也只是你不想去面对的借口对吧？"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/110190.ogg"
    tyt "......"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_s2 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030241.ogg"
    xz "如果真是那样的话，自己真正想要的真相......不更应该去寻找吗？"
    show tyt_wnf_b1 b1 b1_sp1
    "面对翔子的话，藤原瞳瞪大了眼睛看着她。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/030242.ogg"
    xz "稍等一下，我去拿吃的给你。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show lingyin_dsf_b2 b2 b2_h1 onlayer m1:
        xpos 0.7
    play voice "voice/青木铃音/040334.ogg"
    lingyin "我去烤煎饼~"
    hide xz_dsf_b3
    hide lingyin_dsf_b2
    pause 0.5 hard
    play sound open_door4
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    "两人离开后，藤原瞳依旧无法从刚才的氛围中走出来。"
    "同样没有走出来的不只她一个......"
    pause 0.5 hard
    show szl_dsf_b3 b3 b3_ga1 onlayer screens at side_right('szl'), basicfade
    play voice "voice/水之濑/100169.ogg"
    szl "我才没有被排挤......"
    hide szl_dsf_b3
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day210.laboratory_event03:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    play music first_25 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with slowerdissolve
    pause 1.0 hard
    show wyh_wnf_b1 b1 b1_n2 onlayer m2 at walkin_r(0.3)
    pause 0.5 hard
    play voice "voice/万夜花/140074.ogg"
    wyh "这么晚了真是不好意思，资料我送来了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/100185.ogg"
    shy "是从总本社总那里得到的吗？"
    show wyh_wnf_b1 b1 b1_ga2
    play voice "voice/万夜花/140075.ogg"
    wyh "嗯，那边也有和我一起的神官，是我拜托他们帮忙调查的。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/100186.ogg"
    shy "我还在想最近都没看到万夜花小姐，原来有在好好工作啊。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140076.ogg"
    wyh "找不到我也是没办法的事情，大神官怎么能随便抛头露面呢。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/100187.ogg"
    shy "......我可不记得大神官有这么厉害。"
    show wyh_wnf_b1 b1 b1_h1
    play voice "voice/万夜花/140077.ogg"
    wyh "就算是你说的这样，只要时不时看看自己，检讨检讨就发现身边的大家都很优秀。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/100188.ogg"
    shy "也就是说拥有优秀的部下真是幸运的意思吗。"
    play voice "voice/万夜花/140078.ogg"
    wyh "不是部下，是家人哟~"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/100189.ogg"
    shy "......"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/140079.ogg"
    wyh "看来是没有异议了啊。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/100190.ogg"
    shy "......比起这个，从那份资料里知道些什么了？"
    show wyh_wnf_b1 b1 b1_s3
    play voice "voice/万夜花/140080.ogg"
    wyh "关于“她”为什么会成为星天宫的巫女。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/100191.ogg"
    shy "......"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/140081.ogg"
    wyh "藤原祖先是关西某神社的神主。"
    play voice "voice/万夜花/140082.ogg"
    wyh "好像是御灵法术的使用者，一种类似星天宫灵纹的能力。"
    play voice "voice/万夜花/140083.ogg"
    wyh "似乎当时与星天宫的关系很差，不过那都是上层之间的事情，和我们没有什么关系就是了。"
    play voice "voice/万夜花/140084.ogg"
    wyh "但是，似乎跟不久前解散并移居到樱华镇的青木家族有一些渊源。"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/140088.ogg"
    wyh "自从他们知道了小翔还有小铃身上发生的降灵事件之后，就不断派人来神社寻找她们的下落。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140089.ogg"
    wyh "星天宫内部也不是团结一致的，大家都是各有所图。"
    play voice "voice/万夜花/140090.ogg"
    wyh "不过那个时候也算是平安度过了，组织也最终决定暂时交给我来处理。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140091.ogg"
    wyh "所以，我在想这次的事件应该是源于这个。"
    play voice "voice/万夜花/140092.ogg"
    wyh "从藤原瞳和总本社行动的时间来看，也讲得通。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/100192.ogg"
    shy "......"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/140096.ogg"
    wyh "总本社各派系都希望得到天使的力量，以此来争夺大神主的统治地位。"
    play voice "voice/万夜花/140097.ogg"
    wyh "所以，也会有像这样不择手段的事情发生。"
    play voice "voice/万夜花/140098.ogg"
    wyh "就连抹杀小铃也是......"
    show shy_yjf_b1 b1 b1_a1
    play voice "voice/圣护院/100196.ogg"
    shy "真是令人作呕。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/140100.ogg"
    wyh "再回到藤原瞳的问题上来，如果刚才为止的信息的都是正确的，这次灵力暴走的起因应该就是在七年前。"
    play voice "voice/万夜花/140101.ogg"
    wyh "那个时候的藤原瞳还是一个年幼的孩子，估计也没有办法反抗自己的命运吧。"
    play voice "voice/圣护院/100198.ogg"
    show shy_yjf_b1 b1 b1_s1
    shy "总本社居然会做到这个地步......老实说真是令人难以置信。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140102.ogg"
    wyh "到底是哪一派干的，只要调查一下藤原瞳所属的神官就知道了。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/140103.ogg"
    wyh "而且这次派遣藤原瞳来，恐怕也是上层借着她的家人作为威胁的吧。"
    play voice "voice/万夜花/140104.ogg"
    wyh "星天宫的巫女都是秘密行动的，组织会极力避免和一般人的直接接触。"
    play voice "voice/万夜花/140105.ogg"
    wyh "而且，藤原瞳自己也没有过去的记忆，也就是说现在的她想反抗也没有办法了。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/100199.ogg"
    shy "但是，要是能让藤原瞳的记忆恢复的话......"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140106.ogg"
    wyh "是啊。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/140107.ogg"
    wyh "被莲割去的藤原瞳的噩梦，恐怕不是她自己真实的记忆。"
    play voice "voice/万夜花/140108.ogg"
    wyh "此刻的她正被别人强加着记忆。"
    play voice "voice/万夜花/140109.ogg"
    wyh "失去和家人的羁绊，才是她真正的噩梦吧。"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/140110.ogg"
    wyh "所以，被割去噩梦的她才会渐渐回想起一些事情。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/100200.ogg"
    shy "......"
    show wyh_wnf_b1 b1 b1_sp1
    play voice "voice/万夜花/140111.ogg"
    wyh "你要去哪里？我还没说完呢。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/140112.ogg"
    wyh "关于今后要怎么办......"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/100201.ogg"
    shy "已经够了，我要出去吹吹风。"
    play voice "voice/圣护院/100202.ogg"
    shy "那么告辞了。"
    show shy_yjf_b1 b1 b1_s1 at walkout_r(0.5)
    pause 0.5 hard
    play sound close_door4
    pause 2.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140113.ogg"
    wyh "......"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/140114.ogg"
    wyh "也是呢......对不起诗乃。"
    play voice "voice/万夜花/140115.ogg"
    wyh "你和我们不一样，不是分社出身。"
    show wyh_wnf_b1 b1 b1_s3
    play voice "voice/万夜花/140116.ogg"
    wyh "身为总本社嫡传巫女的你。"
    play voice "voice/万夜花/140117.ogg"
    wyh "应该也曾经历过这样可笑的仪式吧。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/140118.ogg"
    wyh "说不定你也因此......而失去过什么重要的东西吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day211
