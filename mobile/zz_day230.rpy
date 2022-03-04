
label inside_battle16(enemy_list):
    $ config.skipping = None
    pause 0.5 hard
    "这次我一定要靠自己的力量守护我所在乎的人。"
    "弗兰小姐曾经给予我的第二次希望——时空之境。"
    "虽然还不能完全掌握，但至少已经可以靠自己的意志强行进入了。"
    "那么剩下的，就是全力打败眼前的自己然后找到你。"
    "在「遗念镜」的作用下我方角色的{color=#f00}最大生命值{/color}和{color=#f00}防御力{/color}得到提升。"
    "等着我吧......希菲尔！"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label winter_final_battle_step0:
    $ config.skipping = None
    pause 0.5 hard
    "可恶，终归是半吊子的实力强行进入的时空之境。"
    "结界的扭曲程度比我想象的还要强大。"
    window mode thought
    me01 "不稳定的结界会对会{color=#f00}提升对方角色的属性{/color}，尽可能地稳定住局面。"
    window mode thought
    me01 "同时想办法利用协战和元素反应制造致胜的机会。"
    "为了希菲尔可绝不能在这里倒下。"
    return

label winter_final_battle_step1:
    $ local_config.in_battle = False
    $ config.skipping = None
    stop music fadeout 5.0
    $ renpy.hide_screen("battle_ui", layer="fg")
    scene onlayer fg
    scene black
    with slowdissolve
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    pause 1.0 hard
    play voice "voice/希菲尔/001011080.ogg"
    xfe "......这个声音是？"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg xuejian yume2
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    me01 "醒了吗希菲尔？"
    play music second_134 fadein 3.0 if_changed
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg tree noleaf one
    with dissolve
    play voice "voice/希菲尔/001011090.ogg"
    xfe "......凉君。"
    me01 "早安。"
    play voice "voice/希菲尔/001011100.ogg"
    xfe "早安。"
    play voice "voice/希菲尔/001011110.ogg"
    xfe "为什么......你会在这里？"
    me01 "因为一切都还没有结束。"
    me01 "堆雪人也好，日常巡回也罢，这个冬天所留下的足迹还远远不够。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf six
    with dissolve
    play voice "voice/希菲尔/001011120.ogg"
    xfe "我的......魔法。"
    me01 "解开了，多亏了那歌声的帮助。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf one
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011130.ogg"
    xfe "千冬的？"
    me01 "不仅如此，我想是大家的力量也说不定。"
    play voice "voice/希菲尔/001011140.ogg"
    xfe "凉君的......也是？"
    me01 "那是当然的。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf five
    with dissolve
    play voice "voice/希菲尔/001011150.ogg"
    xfe "......"
    me01 "怎么觉得你一脸地嫌弃啊。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf three
    with dissolve
    play voice "voice/希菲尔/001011160.ogg"
    xfe "完全没有的事......希菲尔能和凉君与千冬变得要好的话我也会很开心。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf six
    with dissolve
    play voice "voice/希菲尔/001011210.ogg"
    xfe "希菲尔的选择......从一开始就是错误的，这样一来春天就不会降临了。"
    me01 "这种事怎么样都无所谓。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf one
    with dissolve
    play voice "voice/希菲尔/001011220.ogg"
    xfe "凉君你不希望春天降临吗？"
    me01 "如果那是以希菲尔的生命为代价的话，那我宁可它永远也不要降临。"
    me01 "没有希菲尔的话，无论是哪个季节都是没有意义的。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf four
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011230.ogg"
    xfe "听说能量这种东西，是有限的。"
    play voice "voice/希菲尔/001011240.ogg"
    xfe "就连光也无法一直存在，终有一天会消失殆尽。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf two
    with dissolve
    play voice "voice/希菲尔/001011250.ogg"
    xfe "雪人也是一样的。"
    play voice "voice/希菲尔/001011260.ogg"
    xfe "希菲尔也是......一样的。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf three
    with dissolve
    play voice "voice/希菲尔/001011270.ogg"
    xfe "所以......这样就够了。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf two
    with dissolve
    play voice "voice/希菲尔/001011280.ogg"
    xfe "凉君已经没有什么值得让你留恋的了。"
    play voice "voice/希菲尔/001011290.ogg"
    xfe "希菲尔也一点都没有觉得后悔。"
    pause 1.0 hard
    $ flcam.move(0, -1539, 0)
    scene set only memory_cg xuejian yume2
    with dissolve
    pause 1.0 hard
    "无论是不会堆积的白雪、还是堆积在人们心中的白雪。"
    "这些雪花都很温柔，却又很寂寞。"
    "所以才会靠近人心。"
    "所以才会在带来寒意之前就选择消融。"
    "在温柔与寂寞中徘徊的......崭新的生命。"
    "{rb}灵纹{/rb}{rt}rune{/rt}之所以会诞生，难道不正是迷途的孩子们相遇最好的证明吗？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg tree noleaf four
    with dissolve
    play voice "voice/希菲尔/001011300.ogg"
    xfe "{rb}灵纹{/rb}{rt}rune{/rt}会给人带来不幸。"
    play voice "voice/希菲尔/001011310.ogg"
    xfe "对希菲尔而言完全没有影响的异常气候......也会给大家带来麻烦。"
    play voice "voice/希菲尔/001011320.ogg"
    xfe "所以，妖精与人类是没办法和睦相处的。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf six
    with dissolve
    play voice "voice/希菲尔/001011330.ogg"
    xfe "明明在千冬沉睡之时就已经下定决心了的。"
    pause 0.1 hard
    scene set only xfe_cg tree noleaf seven
    with dissolve
    play voice "voice/希菲尔/001011340.ogg"
    xfe "但是无论如何都会犹豫。"
    play voice "voice/希菲尔/001011350.ogg"
    xfe "因为想要朋友而犹豫。"
    play voice "voice/希菲尔/001011360.ogg"
    xfe "因为不想要孤身一人，而是希望有人一起玩耍才会犹豫。"
    play voice "voice/希菲尔/001011370.ogg"
    xfe "明明知道这么做的话，大家会困扰的。"
    play voice "voice/希菲尔/001011380.ogg"
    xfe "可怕的梦里也是如此。"
    play voice "voice/希菲尔/001011390.ogg"
    xfe "另一个希菲尔——用“我”称呼自己的希菲尔也说过的。"
    play voice "voice/希菲尔/001011400.ogg"
    xfe "想要交朋友。"
    play voice "voice/希菲尔/001011410.ogg"
    xfe "想要更多的伙伴。"
    play voice "voice/希菲尔/001011420.ogg"
    xfe "那句话虽然很悲伤却很温暖。明明是第一次听到却很熟悉，明明会感到害怕......却忍不住想要再听一次。"
    play voice "voice/希菲尔/001011430.ogg"
    xfe "希菲尔我......讨厌孤单一人。"
    play voice "voice/希菲尔/001011440.ogg"
    xfe "但是，大家一定也是同样的。"
    play voice "voice/希菲尔/001011450.ogg"
    xfe "如果因为希菲尔的错，让大家变得孤身一人的话。"
    play voice "voice/希菲尔/001011460.ogg"
    xfe "让凉君......变得孤身一人的话。"
    play voice "voice/希菲尔/001011470.ogg"
    xfe "那样的话......更加地讨厌。"
    pause 0.1 hard
    $ flcam.move(-1100, -1400, 450, duration=3.0, warper='ease_quad')
    play voice "voice/希菲尔/001011480.ogg"
    xfe "已经不要......再发生那样的事了。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play sound touch
    me01 "傻瓜。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg end touch two
    with dissolve
    me01 "不是那样的希菲尔，是你搞错了。"
    play voice "voice/希菲尔/001011490.ogg"
    xfe "没有搞错。"
    play voice "voice/希菲尔/001011500.ogg"
    xfe "希菲尔我一直看着大家，所以不会弄错的。"
    me01 "希菲尔所看到的只是表象而已。"
    me01 "大家内心真实的想法，希菲尔还没有看到吧。"
    me01 "就连我的想法，都被忽略了。"
    play voice "voice/希菲尔/001011510.ogg"
    xfe "......"
    me01 "大家都是从心底里，深爱着{rb}灵纹{/rb}{rt}rune{/rt}的。"
    me01 "深爱着这份被给予的羁绊的。"
    me01 "虽然无法保证获得{rb}灵纹{/rb}{rt}rune{/rt}的大家都能够幸福。"
    me01 "但是我可以保证，{rb}灵纹{/rb}{rt}rune{/rt}绝不是只会给大家带来不幸的东西。"
    pause 0.1 hard
    scene set only xfe_cg end touch one
    with dissolve
    play voice "voice/希菲尔/001011520.ogg"
    xfe "果然，希菲尔没有弄错......"
    play voice "voice/希菲尔/001011530.ogg"
    xfe "就算凉君再怎么说喜欢，其他的人也是不一样的。"
    play voice "voice/希菲尔/001011540.ogg"
    xfe "对大家而言，{rb}灵纹{/rb}{rt}rune{/rt}只会带来困扰而已。"
    play voice "voice/希菲尔/001011550.ogg"
    xfe "大家......都是讨厌希菲尔的。"
    me01 "没有那回事。"
    play voice "voice/希菲尔/001011560.ogg"
    xfe "就是这样的！"
    play voice "voice/希菲尔/001011570.ogg"
    xfe "因为现在，在雪见市集中了许许多多的{rb}灵继者{/rb}{rt}elfin{/rt}。"
    play voice "voice/希菲尔/001011580.ogg"
    xfe "那就是答案。"
    play voice "voice/希菲尔/001011590.ogg"
    xfe "大家......都是不需要{rb}灵纹{/rb}{rt}rune{/rt}的。"
    play voice "voice/希菲尔/001011600.ogg"
    xfe "被人擅自强加在自己身上的东西，换做是谁都想要早点丢弃掉的。"
    pause 0.1 hard
    scene set only xfe_cg end touch two
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011610.ogg"
    xfe "大家是无法与希菲尔成为朋友的！"
    stop music fadeout 5.0
    $ local_config.in_battle = True
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    pause 2.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    scene set only fight_cg rune1
    with dissolve
    pause 0.5 hard
    play music battle1 fadein 3.0 if_changed
    window mode thought
    me01 "在希菲尔的灵压下角色的普攻、元素战技、被动技能和元素爆发{color=#f00}失效{/color}。"
    return

label winter_final_battle_step2:
    $ local_config.in_battle = False
    $ config.skipping = None
    stop music fadeout 5.0
    $ renpy.hide_screen("battle_ui", layer="fg")
    scene onlayer fg
    scene black
    with dissolve
    pause 1.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    $ flcam.move(0, -1539, 0)
    scene set only memory_cg xuejian yume2
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    me01 "不是的希菲尔。"
    me01 "你仔细听，这歌声究竟意味着什么。"
    me01 "你还没明白吗。"
    pause 1.0 hard
    hide snow_level1
    play music second_156 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg end touch five
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011620.ogg"
    xfe "......欸？"
    me01 "不只是千冬姐，还有大家的声音全部都在其中。"
    me01 "这是雪见市的{rb}灵继者{/rb}{rt}elfin{/rt}们送给你的礼物。"
    me01 "这才是大家内心深处最真实的想法啊——"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 3.0 hard
    scene set only balltower night xuejian
    show snow_rev onlayer fg
    $ flcam.move(2250, 0, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111001500.ogg"
    aiyi "小希菲尔，快点回来吧~"
    show xz_dsf_b3 b3 b3_h1
    play voice "voice/翔子/011002010.ogg"
    xz "我们会做好晚饭等着你的。"
    pause 1.0 hard
    hide snow_rev
    scene white 
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower night xuejian
    show snow_rev onlayer fg
    $ flcam.move(800, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    show lhx_dsf_b3 b3 b3_s1 onlayer m1:
        xpos 0.61 ypos 0.95 zoom 0.95 alpha 0.5
    play voice "voice/立花希/031004180.ogg"
    lhx "虽然我很不习惯寒冷，一心想要早点回到被炉里。"
    show lhx_dsf_b3 b3 b3_n1
    play voice "voice/立花希/031004190.ogg"
    lhx "但是托你的福，多少有些爱上冬天了。"
    show ts_lst_ssz_b2 b2 b2_h1
    show lhx_dsf_b3 b3 b3_h1
    play voice "voice/立花希/031004200.ogg"
    lhx "这都是你的功劳，我比以前更喜欢雪了。"
    show lhx_dsf_b3 b3 b3_n1
    play voice "voice/立花希/031004210.ogg"
    lhx "原本讨厌的东西，也开始变得喜欢了~"
    show lhx_dsf_b3 b3 b3_h1
    play voice "voice/立花希/031004220.ogg"
    lhx "我也已经......不再只会依靠我最喜欢的{rb}灵纹{/rb}{rt}rune{/rt}而已了。"
    play voice "voice/立花希/031004230.ogg"
    lhx "已经不再只是单纯地依赖你了。"
    $ flcam.move(800, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_n1
    show lhx_dsf_b3 b3 b3_n1
    play voice "voice/立花希/031004240.ogg"
    lhx "所以这次，就让我来报答你吧~"
    pause 1.0 hard
    hide snow_rev
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower night xuejian
    show snow_rev onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dsf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021001320.ogg"
    yj "在这片星空的尽头，是花山院曾经到达过的地方吧？"
    show yj_dsf_b2 b2 b2_h1
    play voice "voice/植澄友加/021001330.ogg"
    yj "那时候的姐姐也很努力地帮助她了。"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021001340.ogg"
    yj "多亏了你我也想起来了。"
    show yj_dsf_b1 b1 b1_h2
    play voice "voice/植澄友加/021001350.ogg"
    yj "那份喜欢宇宙、以及喜欢星空的初心。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021001360.ogg"
    yj "从姐姐那里传承下来的......这份感情。"
    pause 1.0 hard
    hide snow_rev
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower night xuejian
    show snow_rev onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051002980.ogg"
    szl "神野君，还有一起的妖精小姐。"
    play voice "voice/水之濑/051002990.ogg"
    szl "请不要轻易地，就决定我们的想法。"
    show szl_dsf_b2 b2 b2_n1
    play voice "voice/水之濑/051003000.ogg"
    szl "我们所选择的道路不是为了别人，而是追随着自己的本心。"
    play voice "voice/水之濑/051003010.ogg"
    szl "从今往后，我也会用自己的力量开辟一条新的道路给你们看。"
    show szl_dsf_b2 b2 b2_h1
    play voice "voice/水之濑/051003020.ogg"
    szl "虽然凭一己之力踏上这条路是必要的。但是如果需要帮助的话，也希望我能够在你们的身边。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051003030.ogg"
    szl "我从你们身上学到的，就是这样的东西。"
    pause 1.0 hard
    hide snow_rev
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower night xuejian
    show snow_rev onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show qcls_zf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141000580.ogg"
    qcls "我喜欢幼儿园，也最喜欢来上课的小朋友们了。"
    play voice "voice/千川老师/141000590.ogg"
    qcls "我会如此地喜欢小孩子，也许是因为自己小时候总是因为一些小事而忧心忡忡吧。"
    play voice "voice/千川老师/141000600.ogg"
    qcls "所以刚开始面对{rb}灵纹{/rb}{rt}rune{/rt}的时候也是，总是在担忧着。"
    play voice "voice/千川老师/141000610.ogg"
    qcls "正因为是这样的我，才喜欢上了小孩子们天真纯洁的笑容。"
    play voice "voice/千川老师/141000620.ogg"
    qcls "我也一直从孩子们的身上获得了勇气。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide qcls_zf_b2
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141000630.ogg"
    qcls "但是现在，我也不仅仅是从孩子们身上获得勇气而已，我觉得自己也可以守护他们了。"
    pause 1.0 hard
    hide snow_rev
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower night xuejian
    show snow_rev onlayer fg
    $ flcam.move(2250, 0, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    show alu_ct_b2 b2 b2_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.7
    play voice "voice/藤原瞳/131001600.ogg"
    tyt "如此一来这座城市就不会有暴走出现，再次恢复和平了。"
    show alu_ct_b2 b2 b2_2 at fly(0.5):
        xpos 0.7
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎~（就是这样~）"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131001620.ogg"
    tyt "虽然这个冬天或许是非常艰苦且严峻的季节。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131001630.ogg"
    tyt "或许也发生过许多悲伤的事情。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131001640.ogg"
    tyt "但是能和阿露说上话，我真的很开心。"
    show alu_ct_b2 b2 b2_1 at fly(0.5):
        xpos 0.7
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎~（本小姐也是~）"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131001650.ogg"
    tyt "这个冬天，我很中意~"
    show alu_ct_b2 b2 b2_2 at fly(0.5):
        xpos 0.7
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎~（本小姐也最喜欢了~）"
    pause 1.0 hard
    hide snow_rev
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian4
    show snow_rev onlayer fg
    with slowdissolve
    pause 1.0 hard
    "雪花缓缓飘向空中。"
    "堆积在人们心中的雪，此刻随着大家的歌声一起被送还天空。"
    "妖精降下的希望。"
    "承载着所有人的感谢一起。"
    "此刻正划过宇宙的尽头，飘向另一颗星球——"
    pause 1.0 hard
    hide snow_rev
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only jsqd_cg end one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/千冬/771004990.ogg"
    jsqd "这些光芒，是小希菲尔思念的碎片。"
    play voice "voice/千冬/771005000.ogg"
    jsqd "我们大家每个人，都保留着小希菲尔你的愿望。"
    play voice "voice/千冬/771005010.ogg"
    jsqd "不知从何时开始，{rb}灵纹{/rb}{rt}rune{/rt}就变得不稳定了，是你在向我们诉说着什么吧。"
    play voice "voice/千冬/771005020.ogg"
    jsqd "说一个人很寂寞。"
    play voice "voice/千冬/771005030.ogg"
    jsqd "实际上......不想要消失。"
    play voice "voice/千冬/771005040.ogg"
    jsqd "不想要死去。"
    play voice "voice/千冬/771005050.ogg"
    jsqd "没错，是你向我们大家求救了吧。"
    play voice "voice/千冬/771005060.ogg"
    jsqd "小希菲尔你真的很坚强。"
    play voice "voice/千冬/771005070.ogg"
    jsqd "努力克制自己的感情，为了不让我们担心。"
    play voice "voice/千冬/771005080.ogg"
    jsqd "在我们的面前一次也没有露出悲伤的表情，无论何时都保持着笑容。"
    play voice "voice/千冬/771005090.ogg"
    jsqd "但是已经足够了。"
    play voice "voice/千冬/771005100.ogg"
    jsqd "向我们求救也可以的。"
    play voice "voice/千冬/771005110.ogg"
    jsqd "我们不是因为讨厌{rb}灵纹{/rb}{rt}rune{/rt}才将其归还的。"
    play voice "voice/千冬/771005120.ogg"
    jsqd "而是想要让小希菲尔你能够明白我们的想法才归还的。"
    pause 0.1 hard
    scene set only jsqd_cg end two
    $ flcam.move(1100, -750, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千冬/771005130.ogg"
    jsqd "就让我们的思念，乘着这些雪花的光芒一起——"
    pause 1.0 hard
    $ local_config.in_battle = True
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    scene white 
    with slowerdissolve
    pause 2.0 hard
    scene set only fight_cg rune1
    with dissolve
    pause 0.5 hard
    window mode thought
    me01 "大家的声音通过「遗念镜」传达了过来。"
    window mode thought
    me01 "在大家的帮助下结界的污秽消失了，我方全体{color=#f00}恢复状态{/color}并{color=#f00}获得增益{/color}。"
    window mode thought
    me01 "大家的愿望唤醒了沉睡的灵纹，所有角色的普攻、元素战技、被动技能和元素爆发{color=#f00}恢复{/color}。"
    return

label day230:
    bookmark
    $ save_name = _("Day 230")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date229 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    play music second_129 fadein 3.0 if_changed
    with slowdissolve
    pause 2.0 hard
    scene set only home day my_room xuejian
    with dissolve
    pause 1.0 hard
    "春天降临了。"
    "希菲尔还是没有恢复以往的活力。"
    "不如说反而变得越来越虚弱了。"
    "现在的我们只有在梦里面才能见面。"
    pause 1.0 hard
    scene set only xfe_cg sleep
    with slowdissolve
    pause 1.0 hard
    "此时的她几乎一整天的时间都在沉睡。"
    "就算是同为天使的雷亚也不知道原因。"
    pause 0.1 hard
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    "希菲尔她已经无法继续在人们的视线中出现了。"
    "已经......很难在这颗星球上生存下去了。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg tree one
    with slowdissolve
    pause 1.0 hard
    me01 "希菲尔，你看我给你带来了什么。"
    me01 "这是大家为你做的。"
    pause 1.0 hard
    scene set only items ice rabbit
    with dissolve
    pause 1.0 hard
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer screens at side_left('xfe', 0.06), basicfade
    play voice "voice/希菲尔/001010260.ogg"
    xfe "......阿露？"
    hide ts_xfe_yjz_b1
    me01 "不对，这才是真的雪兔。"
    pause 1.0 hard
    scene set only xfe_cg tree three
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010270.ogg"
    xfe "这孩子......长的好像阿露~"
    me01 "希菲尔，还有什么想做的事吗？"
    pause 0.1 hard
    scene set only xfe_cg tree two
    with dissolve
    play voice "voice/希菲尔/001010290.ogg"
    xfe "雪人......"
    play voice "voice/希菲尔/001010300.ogg"
    xfe "还想......再做看看。"
    play voice "voice/希菲尔/001010310.ogg"
    xfe "就像以前一样。"
    pause 0.1 hard
    scene set only xfe_cg tree three
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010320.ogg"
    xfe "看到雪兔之后，就更加这样觉得了。"
    me01 "是这样吗......"
    play voice "voice/希菲尔/001010330.ogg"
    xfe "嗯。"
    me01 "等希菲尔恢复精神以后，我们就一起来做吧。"
    me01 "恢复了精神后，我们再一起玩吧。"
    pause 0.1 hard
    scene set only xfe_cg tree four
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010340.ogg"
    xfe "......"
    me01 "希菲尔......"
    me01 "还能听得到我的声音吗？"
    me01 "你还能像以前一样，对我说声“被找到了”吗。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "树叶再次发出了声响。"
    "仿佛一曲别离的恋歌。"
    "可此时的希菲尔已经没有力气再唱歌了。"
    "那么这又是谁的歌声呢？"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    "洁白的视线中，温柔的雪花悄然降临——"
    pause 0.5 hard
    play music second_147 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory5
    with slowdissolve
    pause 1.0 hard
    me01 "......你是？"
    "眼前的女孩虽然长得和希菲尔一模一样。"
    "但是我可以确信她并不是希菲尔本人。"
    "从她的身上，我能够感受到什么不一样的东西。"
    "那是经历过漫长时光的、复杂的情感。"
    "孤独、绝望、悲伤却又充满了温暖的、奇妙的感觉。"
    play voice "voice/诗乃/701000320.ogg"
    stranger "所以我希望至少要将希望托付出去。"
    play voice "voice/诗乃/701000330.ogg"
    stranger "想要留下吾曾经作为生命活着的证据。"
    play voice "voice/诗乃/701000340.ogg"
    stranger "即便已是油尽灯枯的、这残存的生命。"
    play voice "voice/诗乃/701000350.ogg"
    stranger "也并非只有死寂。"
    play voice "voice/诗乃/701000360.ogg"
    stranger "吾等都是为了活着而在反抗命运之人——"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "这片雪原的主人——这里的第三个、不对，确切来讲应该是这里的第一个生命。"
    "与希菲尔签订契约的，最初的那个人，此刻所凭依的就是眼前这颗树吗。"
    "陪伴着希菲尔度过无数个日月的——最初的“家庭教师”。"
    pause 1.0 hard
    play voice "voice/诗乃/701000370.ogg"
    stranger "最初与吾相遇的就是这位女孩。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory5
    with dissolve
    pause 1.0 hard
    play voice "voice/诗乃/701000390.ogg"
    "诗乃" "少女渴望着能交到朋友。"
    play voice "voice/诗乃/701000400.ogg"
    "诗乃" "而吾也希望能有人继承吾之意志。"
    play voice "voice/诗乃/701000410.ogg"
    "诗乃" "毕竟换作是谁都不想孤身一人。"
    play voice "voice/诗乃/701000420.ogg"
    "诗乃" "希望有朝一日能被别人找到。"
    play voice "voice/诗乃/701000430.ogg"
    "诗乃" "这样想着，吾认为眼前的少女就是能够继承吾之意志、替吾完成使命的最佳人选。"
    play voice "voice/诗乃/701000440.ogg"
    "诗乃" "从这颗星球，到那颗星球。"
    play voice "voice/诗乃/701000450.ogg"
    "诗乃" "新生的——纯白生命。"
    play voice "voice/诗乃/701000460.ogg"
    "诗乃" "是吾等愿望所化作的光——就如同吾的孩子一般。"
    play voice "voice/诗乃/701000470.ogg"
    "诗乃" "吾将那孩子取名为“希菲尔”。"
    play voice "voice/诗乃/701000480.ogg"
    "诗乃" "那是一个与孤独无缘的名字，吾原本希望这能够让她摆脱孤独的束缚，但却始终未能如愿。"
    play voice "voice/诗乃/701000490.ogg"
    "诗乃" "但她却成功遇见了。"
    play voice "voice/诗乃/701000510.ogg"
    "诗乃" "能够和她并肩前行的生命。"
    play voice "voice/诗乃/701000520.ogg"
    "诗乃" "正因为有了最初的相遇，才能唤来春天。正因为有了羁绊才能成为家人。"
    play voice "voice/诗乃/701000530.ogg"
    "诗乃" "正因为心意相通，崭新的生命才得以降生。"
    play voice "voice/诗乃/701000540.ogg"
    "诗乃" "吾将自己的生命托付给了她。"
    play voice "voice/诗乃/701000550.ogg"
    "诗乃" "吾本是希望这孩子能过上幸福快乐的生活。"
    play voice "voice/诗乃/701000560.ogg"
    "诗乃" "但奈何无论吾如何劝说，她仍然做出了自己的选择。"
    play voice "voice/诗乃/701000570.ogg"
    "诗乃" "而结果就是，由吾等所创下的罪孽，将由这孩子独自承担。"
    play voice "voice/诗乃/701000580.ogg"
    "诗乃" "这孩子非常的温柔。"
    play voice "voice/诗乃/701000600.ogg"
    "诗乃" "或许也有汝的影响也说不定。"
    play voice "voice/诗乃/701000610.ogg"
    "诗乃" "但吾相信这孩子最终一定能收获幸福的。"
    play voice "voice/诗乃/701000620.ogg"
    "诗乃" "若是吾的孩子们能得以幸福，吾亦能得偿所愿了吧。"
    pause 1.0 hard
    scene set only xfe_cg memory11
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/诗乃/701000630.ogg"
    "诗乃" "感谢汝，赠予吾最美好的东西。"
    play voice "voice/诗乃/701000640.ogg"
    "诗乃" "若是可以的话，希望汝也能够实现这孩子的心愿。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg xuejian yume2
    show snow_level1 onlayer texture
    $ flcam.moves([
        (0,      0,   0, 0, 0.0, 'linear'),
        (0,      0,   0, 0, 0.5, 'linear'),
        (0, -9750, 0, 0, 10.0, 'ease_cubic')
    ])
    with dissolve
    "再次抬起头，树上的叶子已经凋零。" 
    "仿佛达成心愿一般缓缓飘落。"
    "而就在此刻我注意到，同样消失了的还有一旁的希菲尔。"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 2.0 hard

label day230.map_event01:
    $ flcam.move(0, 0, 0)
    play sound open_door4
    scene set only home snow day outside xuejian
    with dissolve
    pause 2.0 hard
    play ambience1 jiaobu3
    scene set only street snow day road1 xuejian
    with right2left_02
    pause 1.0 hard
    "不在街上......"
    pause 1.0 hard
    scene set only bridge snow day xuejian
    with right2left_02
    pause 1.0 hard
    "也不在桥上......"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    with right2left_02
    pause 1.0 hard
    "钟楼广场也没有......"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "不好的预感一点点地侵蚀着我的内心。"
    "仿佛就快要夺走了我的思考。"
    "为什么......命运总是不肯放过我呢？"
    "只要是我身边的人，哪怕只要得到一丝的幸福都不可以吗？"
    "究竟为什么......要一次又一次地夺走对我而言重要之人呢？"
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 1.0 hard
    "梦也好、雷亚也好、立花老师也罢，我究竟......还要经历多少才行。"
    "或许到头来什么都不懂的人是我。"
    "只有我自己沉醉在自以为是的美好中。"
    "以为能和大家在一起就是给她们幸福了。"
    "可是就像芙兰小姐说的那样，我始终只是个半调子的废柴{rb}灵继者{/rb}{rt}elfin{/rt}。"
    "凭我自己根本无法拯救大家。"
    "和我在一起也只有不幸而已。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    $ _overworld_label = 'day230'
    $ seen_day230_laboratory_event01 = False
    $ seen_day230_street_event01 = False
    $ seen_day230_home_event01 = False
    $ seen_day230_balltower_event01 = False

label day230.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day230':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day230.laboratory_event01':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['laboratory'])
    elif _overworld_label == 'day230.street_event01':
        show set maps winter night
        $ flcam.move(*overworld.camera_positions['laboratory'])
    elif _overworld_label == 'day230.home_event01':
        show set maps winter night
        $ flcam.move(*overworld.camera_positions['road1'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        laboratory=("day230.laboratory_event01", "not seen_day230_laboratory_event01"),
        road2=("day230.street_event01", "seen_day230_laboratory_event01 and not seen_day230_street_event01"),
        road1=("day230.home_event01", "seen_day230_street_event01 and not seen_day230_home_event01"),
        cloqks=("day230.balltower_event01", "seen_day230_home_event01 and not seen_day230_balltower_event01"))
    $ window_animate_outro()
    if _return == 'day230.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day230.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day230.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day230.balltower_event01':
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

label day230.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory day outside xuejian
    with slowdissolve
    pause 1.0 hard
    "只剩下这里了吗。"
    "说实话真的不想进去啊。"
    "对于现在的局面我又有什么脸面去面对千冬姐呢......"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    play sound open_door4
    $ flcam.move(0, 0, 0)
    scene set only laboratory day bedroom xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/千冬/771004010.ogg"
    jsqd "小希菲尔......不见了？"
    play voice "voice/千冬/771004020.ogg"
    jsqd "小希菲尔已经恢复到能够外出的程度了吗？"
    me01 "不，此时的她或许已经无法再出现在我们面前了。"
    me01 "抱歉，都是我的错。"
    play voice "voice/千冬/771004030.ogg"
    jsqd "钟楼广场呢？"
    me01 "能找的地方我都找过了，现在只有依靠千冬姐的力量了。"
    me01 "如果你是第一个“找到”希菲尔的人，那么一定可以办到的对吗？"
    me01 "我已经......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "{size=+25}不想再失去她了！{/size}"
    play music second_134 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only laboratory day bedroom xuejian
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/千冬/771004040.ogg"
    jsqd "小希菲尔还没有消失的，姐姐我可以向你保证。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004050.ogg"
    jsqd "虽然我与小希菲尔的共感已经中断了。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771004060.ogg"
    jsqd "也正因为意识到了这一点，我才决定让小希菲尔留在凉君身边的。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771004070.ogg"
    jsqd "但是现在的我还是能感觉到小希菲尔的存在。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004080.ogg"
    jsqd "只有迷路的人才能够找到小希菲尔，这点凉君也是知道的吧？"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771004090.ogg"
    jsqd "有思考过其中的缘由吗？"
    play voice "voice/千冬/771004100.ogg"
    jsqd "我认为这大概就是因为小希菲尔她自己也是位迷路的孩子。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771004110.ogg"
    jsqd "只有那些同样能够体会小希菲尔内心孤独的人，才能感知到她的存在。"
    show jsqd_dsf_b1 b1 b1_s3
    play voice "voice/千冬/771004120.ogg"
    jsqd "所以小希菲尔她无时无刻不在纠结着。"
    play voice "voice/千冬/771004130.ogg"
    jsqd "无时无刻......不在烦恼着。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004140.ogg"
    jsqd "小希菲尔一定是为了不让{rb}灵纹{/rb}{rt}rune{/rt}再次进入我们的生活，所以才会选择躲起来的。"
    play voice "voice/千冬/771004150.ogg"
    jsqd "而这一定......就是小希菲尔迷惘的真正原因。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n2
    play voice "voice/千冬/771004170.ogg"
    jsqd "现在的我们还没有办法帮助小希菲尔。"
    play voice "voice/千冬/771004180.ogg"
    jsqd "因为我们还没有找到那孩子真正的迷茫所在。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004190.ogg"
    jsqd "凉君你现在之所以没办法找到小希菲尔，也许就是因为还没有办法理解那孩子的想法。"
    play voice "voice/千冬/771004200.ogg"
    jsqd "没办法继续一起前进的原因，大概就是这么回事吧......"
    me01 "就连千冬姐也不知道吗？"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004220.ogg"
    jsqd "原因的话我也不知道。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771004230.ogg"
    jsqd "虽然小希菲尔以前就不适应炎热的天气，但也不至于会发烧的。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg daze
    show sepiagrain onlayer fg
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010350.ogg"
    xfe "多亏了千冬，希菲尔才能在外自由地行动。"
    play voice "voice/希菲尔/001010360.ogg"
    xfe "也多亏了凉君，希菲尔才明白了与别人一起玩耍是多么开心的一件事。"
    pause 0.1 hard
    scene set only xfe_cg normal
    with dissolve
    play voice "voice/希菲尔/001010370.ogg"
    xfe "所以这一次......轮到希菲尔了。"
    play voice "voice/希菲尔/001010380.ogg"
    xfe "轮到希菲尔来帮助你们了。"
    pause 1.0 hard
    hide sepiagrain
    scene set only laboratory day bedroom xuejian
    with dissolve
    pause 1.0 hard
    "希菲尔说过要帮助我们。"
    "这究竟是怎么一回事呢？"
    "希菲尔所说的噩梦又是什么？"
    "芬布尔之冬......星天宫究竟又隐瞒着什么秘密？"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "千冬姐，能告诉我你和希菲尔相遇时的场景吗。"
    me01 "之前的你......想必也有所隐瞒吧？"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004360.ogg"
    jsqd "我并不是故意隐瞒的，只是一直都在烦恼应该怎么说比较好。"
    show jsqd_dsf_b1 b1 b1_n2
    play voice "voice/千冬/771004370.ogg"
    jsqd "要是太随意说出来的话，会让凉君感到难堪的。"
    play voice "voice/千冬/771004380.ogg"
    jsqd "就像过去我让小希菲尔背负的罪孽一样。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771004340.ogg"
    jsqd "也许凉君也早就注意到了，小希菲尔的变化。"
    play voice "voice/千冬/771004350.ogg"
    jsqd "说自己不再是懵懂无知的小孩子，大概也是因为这个。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004410.ogg"
    jsqd "你觉得为什么，我会从沉睡中苏醒呢？"
    play voice "voice/千冬/771004420.ogg"
    jsqd "又为什么，我还能继续存在于这个世界上呢。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/千冬/771004430.ogg"
    jsqd "我会把一切都告诉你。"
    play voice "voice/千冬/771004440.ogg"
    jsqd "因为我相信你。"
    play voice "voice/千冬/771004450.ogg"
    jsqd "相信小希菲尔。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg yuki ground
    show sepiagrain onlayer fg
    show snow_level1 onlayer fg
    with slowdissolve
    play voice "voice/千冬/771004460.ogg"
    jsqd "那一天，在母亲研究陨石碎片的时候，我偶然在一个宛若梦境一般的世界里遇到了小希菲尔。"
    play voice "voice/千冬/771004470.ogg"
    jsqd "那是一片纯白的雪原。"
    pause 1.0 hard
    scene black
    with dissolve
    pause 1.0 hard
    play voice "voice/千冬/771004480.ogg"
    jsqd "但是天空却仿佛在燃烧。"
    play voice "voice/千冬/771004490.ogg"
    jsqd "看起来就像是末日一般的景象。"
    pause 1.0 hard
    scene set only memory_cg sky ground
    with dissolve
    pause 1.0 hard
    play voice "voice/千冬/771004500.ogg"
    jsqd "当时我觉得这副景象是那么的梦幻、美丽、却又悲伤。"
    play voice "voice/千冬/771004510.ogg"
    jsqd "遇到那孩子时也是，带着孤独和寂寞。"
    play voice "voice/千冬/771004520.ogg"
    jsqd "那是和我的内心一样的光景。"
    play voice "voice/千冬/771004530.ogg"
    jsqd "所以我想要与她成为朋友，她那渴望得到爱的心情和当时的我是一样的。"
    play voice "voice/千冬/771004540.ogg"
    jsqd "所以我与那孩子共感了。"
    play voice "voice/千冬/771004550.ogg"
    jsqd "我想那时的她也看到了我的内心。"
    play voice "voice/千冬/771004560.ogg"
    jsqd "那个时候的小希菲尔，似乎和现在的她并非同一个人。"
    play voice "voice/千冬/771004570.ogg"
    jsqd "虽然外表是一样，但是却不是小希菲尔。"
    play voice "voice/千冬/771004580.ogg"
    jsqd "那时的她这样对我说了——"
    play voice "voice/千冬/771004590.ogg"
    jsqd "作为赋予新生命的代价，想要借用我的身体。"
    play voice "voice/千冬/771004600.ogg"
    jsqd "作为实现我渴望朋友的愿望的代价，想要借用我的生命。"
    pause 1.0 hard
    hide snow_level1
    hide sepiagrain
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/千冬/771004610.ogg"
    jsqd "当时的我毫不犹豫地接受了那个提议。"
    play voice "voice/千冬/771004620.ogg"
    jsqd "我也作为研究所的第一位{rb}灵继者{/rb}{rt}elfin{/rt}——{rb}妖精{/rb}{rt}elf{/rt}而诞生了。"
    play voice "voice/千冬/771004630.ogg"
    jsqd "虽然无法理解，但是我却接受了。"
    play voice "voice/千冬/771004640.ogg"
    jsqd "月亮和天狗相遇的时候，会如何呢？"
    play voice "voice/千冬/771004650.ogg"
    jsqd "寂寞的天狗因为吞噬了同样寂寞的月亮而获得了圆满。"
    play voice "voice/千冬/771004660.ogg"
    jsqd "那个新的生命，就如同吃掉了月亮的天狗，借由共享我的生命让她的存在得以延续下去。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only laboratory day bedroom xuejian
    show jsqd_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/千冬/771004670.ogg"
    jsqd "从梦境中醒来的时候，我的怀里抱着一个女孩。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771004680.ogg"
    jsqd "她就宛若新生的婴儿一般，纯白无瑕。"
    play voice "voice/千冬/771004690.ogg"
    jsqd "我的愿望实现了。"
    play voice "voice/千冬/771004700.ogg"
    jsqd "得到了小希菲尔这个朋友的我非常开心。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771004710.ogg"
    jsqd "但是作为代价，我的生命也逐渐被一步步地侵蚀殆尽。"
    play voice "voice/千冬/771004720.ogg"
    jsqd "小希菲尔在外面玩耍的时候，我的体力就会更加地衰弱，以至于最后陷入了沉睡......"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771004730.ogg"
    jsqd "这些就是我所知道的一切了。"
    me01 "所以，千冬姐之所以会沉睡，原因就是希菲尔吗？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_ga3
    play voice "voice/千冬/771004740.ogg"
    jsqd "不要说一些自以为是的话。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771004750.ogg"
    jsqd "这都是我自己的选择......更何况我现在不是也变得精神起来了吗？"
    "因为希菲尔的存在，才将{rb}灵纹{/rb}{rt}rune{/rt}带给了人类。"
    "不只是千冬姐姐。"
    "所有的雪见市的{rb}灵继者{/rb}{rt}elfin{/rt}也是一样的。"
    "“芬布尔之冬”中所描述的——妖精会毁灭，而人类会生存下来难道就是这个意思吗？"
    play voice "voice/千冬/771004770.ogg"
    jsqd "现在就算小希菲尔在外面玩耍，我也不会觉得难受了。"
    play voice "voice/千冬/771004780.ogg"
    jsqd "刚开始我也以为是自己的身体好转了，所以没有太在意凉君刚才说的那番话。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771004790.ogg"
    jsqd "但如果不是那样的话......"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower night xuejian
    show sepiagrain onlayer fg
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001010390.ogg"
    xfe "希菲尔我还不想放弃。"
    play voice "voice/希菲尔/001010400.ogg"
    xfe "妖精与人类，是能够和睦相处的。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001010410.ogg"
    xfe "能不能再一次......相信它呢。"
    pause 2.0 hard
    hide sepiagrain
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "因为想要朋友而遇见希菲尔的千冬姐。"
    "陷入沉睡的{rb}灵继者{/rb}{rt}elfin{/rt}。"
    "迷路的孩子。"
    "不会堆积的、温柔的雪......"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    stop music fadeout 5.0    
    pause 1.0 hard
    "希菲尔究竟是什么样的存在？"
    "她所害怕的梦境又是什么？"
    "为什么只有迷路的孩子才能找到她？"
    "为什么立花老师会希望我能喜欢上{rb}灵纹{/rb}{rt}rune{/rt}呢？"
    pause 1.0 hard
    play music second_130 fadein 3.0 if_changed
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow evening xuejian
    show sepiagrain onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001003370.ogg"
    xfe "住在这座城市的{rb}灵继者{/rb}{rt}elfin{/rt}们，希菲尔一直都在关注着的~"
    pause 1.0 hard
    hide sepiagrain
    scene white 
    with slowdissolve
    pause 1.0 hard
    "为什么我没有早一点注意到呢？"
    "或许正是因为这样。"
    "因为距离太近了的关系才没有察觉到。"
    "才会忽略最应该看到的东西......"
    "芬布尔之冬，世界的尽头。"
    "漫长的寒冬对于喜欢冬天的希菲尔而言并不意味着毁灭。"
    "那么春天降临之时，真正会消失的东西又是什么......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory day bedroom xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    me01 "骗人......的吧。"
    play sound touch
    me01 "为什么到现在才明白！" with vpunch
    me01 "那家伙明明，早就已经用{rb}共感{/rb}{rt}empathy{/rt}告诉我真相了。"
    me01 "明明已经......向我求救了的。"
    me01 "为什么啊！我这个大笨蛋！"
    show jsqd_dsf_b1 b1 b1_n2
    play voice "voice/千冬/771004800.ogg"
    jsqd "凉君，再去一次钟楼广场吧。"
    show jsqd_dsf_b1 b1 b1_a1
    play voice "voice/千冬/771004810.ogg"
    jsqd "绝对要把小希菲尔找出来。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_c3
    play voice "voice/千冬/771004820.ogg"
    jsqd "不把那孩子好好骂一顿的话......我是不会罢休的。"
    play voice "voice/千冬/771004830.ogg"
    jsqd "正因为是最好的朋友......我才会这么想的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day230_laboratory_event01:
        $ seen_day230_laboratory_event01 = True
    $ _overworld_label = 'day230.laboratory_event01'
    jump day230.map

label day230.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street snow day city1 xuejian
    play music second_164 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/other/601000010.ogg"
    stranger "这就是雪见市吗？"
    "刚走下列车的男子——北条昂说道。"
    pause 1.0 hard
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    play voice "voice/other/601000020.ogg"
    "北条昂" "虽然雪好像停了，但就和传闻说的一样一片白色的景象。"
    play voice "voice/other/611000010.ogg"
    "纯" "此处即为吾等的新战场了~"
    "长的像座敷童子的孩子——纯喊出了与可爱的外表大相径庭的话。"
    play voice "voice/other/621000010.ogg"
    "库鲁玛" "这里......是战场吗？"
    "翻着麻花绳的女孩——库鲁玛战战兢兢地说道。"
    play voice "voice/other/631000010.ogg"
    "美凤" "这种程度的{rb}灵纹{/rb}{rt}rune{/rt}插曲......虽然是带有点斗争的味道，但还是希望不要真的打起来啊。"
    "用扇子遮住嘴的大小姐——美凤皱着眉头说道。"
    play voice "voice/other/641000010.ogg"
    "米丽德怀特" "你们几个别捣乱了，等着局长的命令吧。"
    "戴着眼罩的女子——米丽德怀特严肃地说道。"
    play voice "voice/other/611000020.ogg"
    "纯" "吾知道了，总之先打雪仗吧~"
    play voice "voice/other/601000030.ogg"
    "北条昂" "这种程度的战场，还真是可爱啊。"
    play voice "voice/other/611000030.ogg"
    "纯" "让你尝尝吾的镭射光线~"
    play voice "voice/other/631000020.ogg"
    "美凤" "请别朝我这里丢，会弄湿的。"
    play voice "voice/other/621000020.ogg"
    "库鲁玛" "不、不乖乖听话的话......会惹眼罩酱生气的。"
    play voice "voice/other/641000020.ogg"
    "米丽德怀特" "为了不变成那样，局长请下达命令吧。"
    pause 1.0 hard
    scene set only street snow day city1 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001210.ogg"
    dh "......"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show rxl_dsf_b1 b1 b1_sp2 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/日向怜/121003500.ogg"
    rxl "呜哇......真的到齐了。"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    show rxxf happy02 with dissolve
    play voice "voice/日向怜/121003510.ogg"
    rxl "大家为了阻止{rb}灵继者{/rb}{rt}elfin{/rt}暴走，一直都在各地奔走。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show lingyin_dsf_b1 b1 b1_s1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/青木铃音/031003390.ogg"
    lingyin "可以的话真希望这种见面是最后一次了......（小声）"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    play voice "voice/other/611000040.ogg"
    "纯" "好久不见了~铃音、日向~"
    play voice "voice/other/621000030.ogg"
    "库鲁玛" "有、有精神......比什么都重要。"
    play voice "voice/other/601000040.ogg"
    "北条昂" "我们听说这里需要援手，就快马加鞭地赶来了。"
    play voice "voice/other/651000010.ogg"
    "露露" "哔喽哔喽~"
    "嘴里叼着口哨的无口少女——露露，从开始到现在一直不停地吹着。"
    play voice "voice/other/631000030.ogg"
    "美凤" "突然被叫到这种偏僻的地区，对我来说可是很困扰的。"
    play voice "voice/other/611000050.ogg"
    "纯" "嘛请安心吧，有吾在足以以一敌百。"
    play voice "voice/other/621000040.ogg"
    "库鲁玛" "反、反对用那么粗鲁的方式......"
    play voice "voice/other/641000030.ogg"
    "米丽德怀特" "你们几个别擅自开口了，会让话题没有进展的，别打乱队形立正等候局长的命令。"
    pause 1.0 hard
    scene set only street snow day city1 xuejian
    $ flcam.move(4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show rxl_dsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003530.ogg"
    rxl "那么局长，差不多也该告诉我们是什么事了吧？"
    hide rxl_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001220.ogg"
    dh "的确，虽然这也只是我个人的猜想而已。"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/171001230.ogg"
    dh "因为这个让你们跟着我折腾，说实话我还是抱有歉意的。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show rxl_dsf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003540.ogg"
    rxl "虽然很想承认但是完全看不出来啊......"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171001250.ogg"
    dh "也是，所以我每月一次会让值得信赖的{rb}灵继者{/rb}{rt}elfin{/rt}前来调查这座城市。"
    show rxl_dsf_b1 b1 b1_sp1
    play voice "voice/日向怜/121003550.ogg"
    rxl "局长你为什么会选择花山院呢？虽说她的确是一名优秀的{rb}灵继者{/rb}{rt}elfin{/rt}。"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/171001270.ogg"
    dh "当然也有考虑过交给你们，但是又担心你们会因为私情而意气用事。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171001290.ogg"
    dh "毕竟我可是下达了对神野凉行动加倍留意的命令，只要对方稍微有点奇怪的举动，就要不择手段地将他制服。"
    show rxl_dsf_b1 b1 b1_s2
    play voice "voice/日向怜/121003560.ogg"
    rxl "确实比起我们，让组织其他没接触过当事人的{rb}灵继者{/rb}{rt}elfin{/rt}来的话，会比较稳妥一些。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    play voice "voice/other/601000050.ogg"
    "北条昂" "毕竟到时不管他变得怎么样，我也不会放在心上的。"
    play voice "voice/other/641000040.ogg"
    "米丽德怀特" "我的话当然也不会犹豫，是命令的话就应该果断地执行。"
    play voice "voice/other/611000060.ogg"
    "纯" "这可是大好的机会，不听话的家伙就应该惩罚惩罚。"
    play voice "voice/other/631000040.ogg"
    "美凤" "虽然我不喜欢折腾，但是这点程度的对手也未免有点不够看呢。"
    play voice "voice/other/621000050.ogg"
    "库鲁玛" "大、大家都赞成的话，我也......"
    play voice "voice/other/651000020.ogg"
    "露露" "哔喽哔喽~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street snow day city1 xuejian
    $ flcam.move(4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show rxl_dsf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003570.ogg"
    rxl "啊行了行了，也就是说在场的各位都是傲娇就对了。"
    hide rxl_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001300.ogg"
    dh "就是因为担心会这样，我才交给其他{rb}灵继者{/rb}{rt}elfin{/rt}处理的。"
    show dh_zf_b1 b1 b1_s2
    play voice "voice/神野大和/171001320.ogg"
    dh "拜他所赐，我才能再一次找到她......（小声）"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001330.ogg"
    dh "即便知道等待我们的将会是毁灭......（小声）"
    stop music fadeout 5.0
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/171001340.ogg"
    dh "我之所以能够自由调度同样隶属于研究所的花山院，是因为我从上级那里得到指示。考虑到利害关系，即使不愿意我也只能照办了。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show rxl_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003580.ogg"
    rxl "毁灭？什么毁灭？"
    play music second_123 fadein 3.0 if_changed
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171001350.ogg"
    dh "就是你们——{rb}灵继者{/rb}{rt}elfin{/rt}。"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003590.ogg"
    rxl "......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    play voice "voice/other/601000060.ogg"
    "北条昂" "......"
    play voice "voice/other/641000050.ogg"
    "米丽德怀特" "......"
    play voice "voice/other/611000070.ogg"
    "纯" "......"
    play voice "voice/other/631000050.ogg"
    "美凤" "......"
    play voice "voice/other/621000060.ogg"
    "库鲁玛" "......"
    play voice "voice/other/651000030.ogg"
    "露露" "哔喽哔喽~"
    pause 1.0 hard
    scene set only street snow day city1 xuejian
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lingyin_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/031003500.ogg"
    lingyin "局长......能更具体地说一下吗？"
    hide lingyin_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001360.ogg"
    dh "我从爱衣的预言里了解到，雪见市所降下的雪来源于北欧神话。"
    play voice "voice/神野大和/171001370.ogg"
    dh "这样一来的话，对此类异常气候所带来的后果我也相应的有几种猜测。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001380.ogg"
    dh "而其中最坏的情况，就是{rb}灵继者{/rb}{rt}elfin{/rt}的毁灭。"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/171001390.ogg"
    dh "我指的是丧失生命的，死亡......"
    play voice "voice/神野大和/171001410.ogg"
    dh "根据神话传闻，在持续了三年之久的寒冬过后，天狗和月亮相遇的那一刻就会引发{rb}诸神黄昏{/rb}{rt}Ragnarok{/rt}。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001420.ogg"
    dh "而最后就是春天降临，存活下来的就只剩下人类。"
    play voice "voice/神野大和/171001430.ogg"
    dh "换句话说，就是{rb}灵继者{/rb}{rt}elfin{/rt}接连地死去。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171001440.ogg"
    dh "{rb}灵纹{/rb}{rt}rune{/rt}本身就会对身体产生很大的负担，在活体实验中也证实了这一点。"
    play voice "voice/神野大和/171001450.ogg"
    dh "就如同过去的{rb}妖精{/rb}{rt}elf{/rt}一般，我们无法确定新的{rb}灵继者{/rb}{rt}elfin{/rt}们会不会再次变成那样。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001460.ogg"
    dh "而作为最佳舞台的雪见市，被称为导火索的邂逅也在悄悄发生着。"
    play voice "voice/神野大和/171001470.ogg"
    dh "如果神野凉和{rb}妖精{/rb}{rt}elf{/rt}的相遇，召唤了“春天”的话......"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/171001480.ogg"
    dh "我就不得不倾尽我手头上所有的力量来阻止它。"
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171001490.ogg"
    dh "这次召集你们过来，就是为了攻占星天宫研究就所，揪出背后那个令人不爽的所长。"
    play voice "voice/神野大和/171001500.ogg"
    dh "发现{rb}妖精{/rb}{rt}elf{/rt}的话同样要确保能够抓住她。"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/171001510.ogg"
    dh "之所以没有通知神野凉，就是为了不让他来妨碍我们。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001520.ogg"
    dh "这次的事件很明显也是白羽教授策划的，因为她的女儿陷入沉睡的关系，使得她对{rb}灵纹{/rb}{rt}rune{/rt}十分憎恨。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171001530.ogg"
    dh "表面上是在保护{rb}灵继者{/rb}{rt}elfin{/rt}，而实际上却是想要将其毁灭吧。"
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171001540.ogg"
    dh "虽然我之前也曾被她玩弄于股掌之间，但是现在不一样了。绝对不会让她逃跑了，就算哭着求我也不会饶恕她。"
    stop music fadeout 5.0
    show jingya onlayer texture
    show dh_zf_b1 b1 b1_a2
    play voice "voice/神野大和/171001550.ogg"
    dh "听好了大家，去将那家伙的首级带来见我吧！！！"
    pause 1.0 hard
    hide jingya
    $ flcam.move(0, 0, 0)
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    play music second_108 fadein 3.0 if_changed
    play voice "voice/other/631000060.ogg"
    "美凤" "局长，请不要那么大火气，啪嗒啪嗒。"
    show dh_zf_b1 b1 b1_ga2 onlayer screens at side_left('dh'), basicfade
    play voice "voice/神野大和/171001560.ogg"
    dh "......别在那扇扇子了，反而让人更加火大了。"
    hide dh_zf_b1
    play voice "voice/other/601000070.ogg"
    "北条昂" "先不论局长的妄想是否属实，那个研究所的确有调查的价值呢。"
    play voice "voice/other/641000060.ogg"
    "米丽德怀特" "比起调查，在没有线索的情况下也只能强行突破了吧。"
    play voice "voice/other/611000080.ogg"
    "纯" "吾等毁灭之事，可不能当做没听见啊。"
    play voice "voice/other/631000070.ogg"
    "美凤" "真是的，真麻烦。"
    play voice "voice/other/651000040.ogg"
    "露露" "哔喽哔喽~"
    show dh_zf_b1 b1 b1_a2 onlayer screens at side_left('dh'), basicfade
    play voice "voice/神野大和/171001570.ogg"
    dh "整顿完毕了，就让我们出发吧！"
    hide dh_zf_b1
    play voice "voice/other/631000080.ogg"
    "美凤" "火气上头的话血压会升高的哟，啪嗒啪嗒。"
    play voice "voice/other/621000070.ogg"
    "库鲁玛" "啊，天空树，完成了......（注释：东京天空树，正式译名为晴空塔，在这里是库鲁玛手中的麻花绳）"
    play voice "voice/other/611000090.ogg"
    "纯" "明明平常都只会做出怪异的翻花绳，真是稀奇啊。"
    play voice "voice/other/601000080.ogg"
    "北条昂" "这或许是什么事情要发生的前兆。"
    play voice "voice/other/641000070.ogg"
    "米丽德怀特" "我们讨论的时候有人接近了，这脚步声是......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only street snow day city1 xuejian
    $ flcam.move(4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show rxl_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003600.ogg"
    rxl "如果这能让局长稍微冷静下来就好了。"
    pause 1.0 hard
    scene black 
    with slowdissolve
    play sound jiaobu3
    pause 2.0 hard

label day230.street_event02:
    play music second_138 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    "星天宫所属机构——库洛诺斯的{rb}灵继者{/rb}{rt}elfin{/rt}们全都聚集在了这里。"
    "包括日向同学和铃音同学在内一共有八人。"
    "而带领他们的就是我的父亲神野大和。"
    pause 1.0 hard
    scene set only street snow day city1 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001580.ogg"
    dh "为什么你会在这里？"
    me01 "是你让我来这里的，为了阻止你。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001590.ogg"
    dh "我可不记得有下达过这种命令。"
    me01 "你说过的，{rb}灵继者{/rb}{rt}elfin{/rt}的工作就是阻止{rb}灵纹{/rb}{rt}rune{/rt}暴走保护人类。"
    show dh_zf_b1 b1 b1_ga1
    play voice "voice/神野大和/171001600.ogg"
    dh "你是觉得我也是{rb}灵继者{/rb}{rt}elfin{/rt}吗？"
    me01 "就算你不是{rb}灵继者{/rb}{rt}elfin{/rt}，但你也还是暴走了吧？"
    me01 "仅凭自己所谓的猜测就一意孤行。"
    me01 "你想连希菲尔、连同“母亲”的努力也一起摧毁吗！"
    play voice "voice/神野大和/171001610.ogg"
    dh "你又能明白什么？不对......应该说你究竟知道了什么？"
    me01 "啊，会告诉你的。"
    me01 "我会把我知道的一切全部都告诉你！"
    me01 "就是因为这样我才来到这里的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "我把从千冬姐那里得到的情报全部说了出来。"
    "持续了三年寒冬的雪见市，以及那温柔的雪的真面目。"
    "希菲尔模仿了她最喜欢的北欧神话，在这座城市降下了雪。"
    "春天降临以后，{rb}灵继者{/rb}{rt}elfin{/rt}所面临的不是死亡和毁灭，而是蜕变。"
    "变回普通的人类。"
    "温柔的雪会带走{rb}灵纹{/rb}{rt}rune{/rt}和这个寒冬所有的记忆，随着春天的到来一起消失。"
    "因为她喜欢看到大家都过上平凡的生活。"
    "看起来是改变了，但却又没有改变。"
    "那份渴望一起玩耍却又不得不选择孤独的心......"
    "一直都没有改变。"
    pause 1.0 hard
    scene set only street snow day city1 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show dh_zf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001620.ogg"
    dh "这种荒谬的说法，你认为我会相信吗？"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171001710.ogg"
    dh "那位名叫希菲尔的少女，真的没有对你隐瞒什么吗？"
    play voice "voice/神野大和/171001720.ogg"
    dh "难道不是因为你的一厢情愿而被利用了而已吗？"
    me01 "这话我可不能装作没听到！"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001730.ogg"
    dh "更何况对{rb}灵纹{/rb}{rt}rune{/rt}调查了那么久的我，怎么可能轻易被你这般说法说服。"
    me01 "单纯是因为我比你更优秀吧。"
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/171001740.ogg"
    dh "我不要，才不会承认这种事。"
    me01 "你是小孩子吗？！" with vpunch
    pause 1.0 hard
    hide dh_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/白羽/711002330.ogg"
    baiyu "神野教授，就算不能理解也请坦率一点，你也一定从{rb}共感{/rb}{rt}empathy{/rt}中察觉到了什么吧。"
    play voice "voice/白羽/711002340.ogg"
    baiyu "希菲尔她一定是大自然派来帮助我们的使者。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show dh_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001750.ogg"
    dh "......没想到连你也来了。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711002350.ogg"
    baiyu "被女儿拜托了来帮助神野凉。所以我才会来说服你这个独断专行的专家啊。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711002360.ogg"
    baiyu "对这座城市的气候研究至今的我，应该可以给出你想要的科学解释的。"
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171001760.ogg"
    dh "飞莹扑火就是指这种情况吧。"
    stop music fadeout 5.0
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711002370.ogg"
    baiyu "夏天还早吧~（注释：飞莹指的是萤火虫，也被称为“夏虫”）"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show jingya onlayer texture
    play sound jing01
    show dh_zf_b1 b1 b1_a2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/神野大和/171001770.ogg"
    dh "诸位，给我把这家伙拿下！！！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street klns party
    play music second_108 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    play voice "voice/other/631000090.ogg"
    "美凤" "啪嗒啪嗒。"
    show dh_zf_b1 b1 b1_ga3 onlayer screens at side_left('dh'), basicfade
    play voice "voice/神野大和/171001780.ogg"
    dh "真是烦人！"
    hide dh_zf_b1
    play voice "voice/other/601000090.ogg"
    "北条昂" "原来如此，果然又是局长过早下的结论了吗。"
    play voice "voice/other/631000100.ogg"
    "美凤" "我早就觉得是这样了。"
    play voice "voice/other/641000080.ogg"
    "米丽德怀特" "从以前开始，只要和心爱的儿子有关的事情就会不断地犯错。如果是那个以外的命令我就会严肃执行了。"
    play voice "voice/other/611000100.ogg"
    "纯" "吾等白跑一趟啦，回去可以吗？"
    play voice "voice/other/621000080.ogg"
    "库鲁玛" "我、我觉得......机会难得所以想观光一下。"
    play voice "voice/other/651000050.ogg"
    "露露" "哔喽哔喽~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street snow day city1 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show dh_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001790.ogg"
    dh "你们几个，知道自己在说什么吗......"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show rxl_dsf_b1 b1 b1_h3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003610.ogg"
    rxl "这也是大家敬爱你的表现嘛~"
    stop music fadeout 3.0
    pause 2.0 hard

label day230.laboratory_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    play music second_163 fadein 3.0 if_changed
    with dissolve
    pause 2.0 hard
    scene set only laboratory day outside xuejian
    with dissolve
    pause 2.0 hard
    "在白羽小姐的带领下，我们一同回到了星天宫研究所。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    play sound open_door4
    pause 1.0 hard
    scene set only laboratory inside2 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show dh_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001800.ogg"
    dh "这份报告是？"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show baiyu_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/白羽/711002380.ogg"
    baiyu "是对雪见市气候持续研究的成果。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711002390.ogg"
    baiyu "用一句话概括就是，雪见市降下的雪是以{rb}共感{/rb}{rt}empathy{/rt}为灵体所创造出来的东西。"
    hide dh_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711002400.ogg"
    baiyu "{rb}灵纹{/rb}{rt}rune{/rt}本身就被认为是其他星球上的自然衍生物。"
    play voice "voice/白羽/711002410.ogg"
    baiyu "所以由{rb}灵继者{/rb}{rt}elfin{/rt}操控的话，也能达到与异常气候相同的效果。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711002420.ogg"
    baiyu "也就是说{rb}灵纹{/rb}{rt}rune{/rt}不只是生物为了能适应宇宙环境而产生的变异。"
    play voice "voice/白羽/711002430.ogg"
    baiyu "从长远的角度来看，这也是一种自适应环境的创造机制——{rb}量化改造{/rb}{rt}terraforming{/rt}吧。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711002470.ogg"
    baiyu "为的是在结束了地球的旅行之后，能够踏上新的旅程。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show dh_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001810.ogg"
    dh "......"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/白羽/711002480.ogg"
    baiyu "综上所述，为了帮助我们人类，某位大人将这份力量赐给了我们。"
    play voice "voice/白羽/711002490.ogg"
    baiyu "如果说{rb}灵纹{/rb}{rt}rune{/rt}是自然之力的话，那我们所谓的某位大人就是指这颗星球本身吧。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001820.ogg"
    dh "......"
    hide dh_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711002500.ogg"
    baiyu "欧洲那边也有心理学者提出了这样的假设。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711002510.ogg"
    baiyu "人类独有的两大{rb}灵纹{/rb}{rt}rune{/rt}，就是感情和理性系统。"
    play voice "voice/白羽/711002520.ogg"
    baiyu "这么想的话，由{rb}共感{/rb}{rt}empathy{/rt}而引发的异常气候——雪见市降下的雪可谓是集两者之大成了吧。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show dh_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001830.ogg"
    dh "......讲到这里就行了。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001840.ogg"
    dh "星天宫研究所将{rb}灵纹{/rb}{rt}rune{/rt}用于宇宙开发是人尽皆知的事实。"
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171001850.ogg"
    dh "更何况我从你的汇报中听出了许多掺杂了心理学和超心理学的理论，但是到头来你想说的到底是什么？"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711002540.ogg"
    baiyu "到目前为止都是我作为研究者的见解。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711002550.ogg"
    baiyu "而我真正想要传达的，是作为母亲的请求。"
    hide dh_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_s2
    play voice "voice/白羽/711002560.ogg"
    baiyu "就像你说的那样，{rb}灵纹{/rb}{rt}rune{/rt}会对身体带来极大的负担。"
    play voice "voice/白羽/711002570.ogg"
    baiyu "即使未来某天，又会再次出现像我女儿那样的{rb}灵继者{/rb}{rt}elfin{/rt}也不足为奇。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711002580.ogg"
    baiyu "这么思考的话，对现在的我们而言{rb}灵纹{/rb}{rt}rune{/rt}仍然是过于强大的存在。"
    play voice "voice/白羽/711002590.ogg"
    baiyu "虽然想像库洛诺斯那样，让{rb}灵继者{/rb}{rt}elfin{/rt}接受正规的训练，或许就能驾驭{rb}灵纹{/rb}{rt}rune{/rt}。"
    show baiyu_yjf_b1 b1 b1_s2
    play voice "voice/白羽/711002600.ogg"
    baiyu "但是也有像我女儿一样，无法正常行动的人，无论何时都有可能被夺去生命......"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711002610.ogg"
    baiyu "所以为了找到能够让{rb}灵继者{/rb}{rt}elfin{/rt}正常生活的方法，我需要你的帮助。"
    play voice "voice/白羽/711002620.ogg"
    baiyu "至少也能够帮助那些被迫成为{rb}灵继者{/rb}{rt}elfin{/rt}的人。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711002630.ogg"
    baiyu "虽然我无法保证经过了三年的寒冬，{rb}灵纹{/rb}{rt}rune{/rt}会真的消失。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711002640.ogg"
    baiyu "不如说我更想打破这种局面。所以我也想邀请你也加入到我的研究中来。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711002650.ogg"
    baiyu "不只是雪见市的气候研究，我在研究所得到的成果都会统统告诉你。"
    play voice "voice/白羽/711002660.ogg"
    baiyu "包括现在正在进行的宇宙行星探测也同样一并奉上。"
    show baiyu_yjf_b1 b1 b1_s3
    play voice "voice/白羽/711002670.ogg"
    baiyu "这样一来，你那原本处于瓶颈的活体研究项目说不定就能有所突破了。"
    show baiyu_yjf_b1 b1 b1_s2
    play voice "voice/白羽/711002680.ogg"
    baiyu "所以拜托了，如果三年的寒冬过去{rb}灵纹{/rb}{rt}rune{/rt}依旧无法被救赎的话......"
    $ flcam.move(4500, -300, 1000, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711002690.ogg"
    baiyu "我希望能由你来拯救{rb}灵继者{/rb}{rt}elfin{/rt}们。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show dh_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001860.ogg"
    dh "......"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711002700.ogg"
    baiyu "你所提出的{rb}黄昏症候群{/rb}{rt}twilight syndrome{/rt}理论，请好好地完成它呀。"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/171001870.ogg"
    dh "......我这是怎么了，本来应该是来讨伐你们的。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001880.ogg"
    dh "我又一次白费力气了吗？"
    me01 "而且还是最差劲的一次。"
    show dh_zf_b1 b1 b1_s2
    play voice "voice/神野大和/171001890.ogg"
    dh "你的意思是我错了吗？"
    me01 "就是那样的。"
    show dh_zf_b1 b1 b1_ga2
    play voice "voice/神野大和/171001900.ogg"
    dh "我不要，我才是正确的。"
    me01 "到底是有多孩子气啊你！"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001910.ogg"
    dh "本来即使没有人拜托我，拯救{rb}灵继者{/rb}{rt}elfin{/rt}也一直是我亲力亲为的事情。"
    show dh_zf_b1 b1 b1_c1
    play voice "voice/神野大和/171001920.ogg"
    dh "要拯救剩下的孩子们，我和诗乃是这么约好了的......（小声）"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    play sound open_door4
    pause 1.0 hard

label day230.laboratory_event03:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside1 xuejian
    play music second_151 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    play voice "voice/other/601000100.ogg"
    "北条昂" "哦呀，终于出来了。"
    pause 1.0 hard
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    play voice "voice/other/631000110.ogg"
    "美凤" "都等到不耐烦了。"
    play voice "voice/other/611000110.ogg"
    "纯" "顺带一提，吾等聚集在这里并非是想要偷听。"
    play voice "voice/other/641000090.ogg"
    "米丽德怀特" "就算想用{rb}灵纹{/rb}{rt}rune{/rt}调查研究所内部，也会因为这里的特殊钢材被干扰。"
    play voice "voice/other/621000090.ogg"
    "库鲁玛" "而且也、也被......隔音了。"
    play voice "voice/other/651000060.ogg"
    "露露" "哔喽哔喽~"
    pause 1.0 hard
    scene set only laboratory inside1 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171001940.ogg"
    dh "这些事情等等再说，在此之前我要对你们下达新的命令。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    play voice "voice/other/611000120.ogg"
    "纯" "是观光对吧~"
    play voice "voice/other/621000100.ogg"
    "库鲁玛" "太、太好了......"
    show dh_zf_b1 b1 b1_ga3 onlayer screens at side_left('dh'), basicfade
    play voice "voice/神野大和/171001950.ogg"
    dh "嘛，空闲的时候让你们放松一下也是可以的。"
    hide dh_zf_b1
    play voice "voice/other/601000110.ogg"
    "北条昂" "不会说接下来就给你们放假这样的话吧。"
    play voice "voice/other/641000100.ogg"
    "米丽德怀特" "我们可都是因为任务的关系才来到雪见市的。"
    play voice "voice/other/631000120.ogg"
    "美凤" "工作结束后真想早点回到本部。这座城市真是冷得要命啊。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only laboratory inside1 xuejian
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/神野大和/171001960.ogg"
    dh "那样想的话，可能要继续忍耐了。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171001970.ogg"
    dh "我们不回本部了，不对说错了......"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171001980.ogg"
    dh "从今天开始，库洛诺斯决定在雪见市建立新的本部，你们全员今后就给我全力保护这座城市。"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/171001990.ogg"
    dh "至少等到春天降临为止。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street klns party
    with dissolve
    pause 1.0 hard
    play voice "voice/other/601000120.ogg"
    "北条昂" "......"
    play voice "voice/other/641000110.ogg"
    "米丽德怀特" "......"
    play voice "voice/other/611000130.ogg"
    "纯" "......"
    play voice "voice/other/631000130.ogg"
    "美凤" "......"
    play voice "voice/other/621000110.ogg"
    "库鲁玛" "......"
    play voice "voice/other/651000070.ogg"
    "露露" "哔喽哔喽~"
    pause 1.0 hard
    scene set only laboratory inside1 xuejian
    with dissolve
    pause 1.0 hard
    me01 "就是这样，今后也请各位多多指教。"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003640.ogg"
    rxl "其他各地也还有许多暴走事件需要处理的吧？"
    hide rxl_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171002000.ogg"
    dh "当然如果在雪见市以外的地区发生事故的话也不得不出动。"
    play voice "voice/神野大和/171002010.ogg"
    dh "但是，那些会尽可能地交给其他星天宫的分部去做。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171002020.ogg"
    dh "应该说这才是星天宫该有的样子。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show rxl_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003650.ogg"
    rxl "神社那边的几位也是吗？"
    me01 "是啊，运气好的话藤原瞳和万夜花小姐也会帮助我们的。"
    hide rxl_dsf_b1
    hide dh_zf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/白羽/711002710.ogg"
    baiyu "神野教授。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711002730.ogg"
    baiyu "要在雪见市建立本部的话，需要相当宽敞的地方吧，你打算怎么做？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show dh_zf_b1 b1 b1_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171002050.ogg"
    dh "这个嘛......"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/白羽/711002740.ogg"
    baiyu "不介意的话就使用这座研究所吧。"
    show dh_zf_b1 b1 b1_sp1
    play voice "voice/神野大和/171002060.ogg"
    dh "......可以吗？"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711002750.ogg"
    baiyu "正好研究员们都离开了，不妨碍我女儿复健的话就没有问题。"
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/171002070.ogg"
    dh "我是不会道谢的。"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711002760.ogg"
    baiyu "我才不需要那种东西呢，呜哇好恶心。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171002080.ogg"
    dh "没想到居然会有这一天，是第一次大概也是最后一次吧。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711002770.ogg"
    baiyu "这是我的台词吧，再合作什么的还是饶了我吧。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show rxl_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121003660.ogg"
    rxl "虽然由我来说好像不太合适，不过二位的关系还真是好呢~"
    hide rxl_dsf_b2
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171002090.ogg"
    dh "你眼睛怎么长的，这当然都是{rb}犬猿之交{/rb}{rt}势不两立{/rt}啊。"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711002780.ogg"
    baiyu "这男的，从我们同僚时期开始就很碍眼呢，总是抢夺我的研究成果。"
    show dh_zf_b1 b1 b1_a2
    play voice "voice/神野大和/171002100.ogg"
    dh "别扭曲事实了，明明是我先做出的来成果，你只是过来掺一脚罢了。"
    show baiyu_yjf_b1 b1 b1_a1
    play voice "voice/白羽/711002790.ogg"
    baiyu "才不是呢，那是我先发现的......"
    "不得不说，两位的关系确实很好。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    play sound open_door4
    pause 1.0 hard

label day230.laboratory_event04:
    $ flcam.move(0, 0, 0)
    scene set only laboratory day bedroom xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771002800.ogg"
    jsqd "凉君辛苦你了，谈话结束了吗？"
    me01 "是啊，托千冬姐的福一切都进行得很顺利。"
    show jsqd_dsf_b1 b1 b1_ga3
    play voice "voice/千冬/771002810.ogg"
    jsqd "我也只是拜托母亲帮一下凉君的忙而已。"
    me01 "但是因此我也终于明白了。"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771002820.ogg"
    jsqd "明白什么了？"
    me01 "月亮和天狗相遇的秘密，有预言说这将会成为一切导火索。"
    me01 "我想现在的情况大概就是这样的吧。"
    me01 "所谓的毁灭，就是如同月亮的盈亏。"
    me01 "我们大家能够像这样在这雪见市的冬天相遇，也是多亏了希菲尔吧。"
    me01 "天狗因为寂寞而追随月亮，同样的，月亮也因为寂寞接受了天狗。"
    me01 "彼此倚靠，才成就了今天的大家。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002830.ogg"
    jsqd "嗯，如果真是那样的话就太好了呢~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    if not seen_day230_street_event01:
        $ seen_day230_street_event01 = True
    $ _overworld_label = 'day230.street_event01'
    jump day230.map

label day230.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    play music first_40 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    "和星天宫的大家一起寻找着希菲尔的踪迹。"
    "然而即便是这样到了晚上仍旧一无所获。"
    "其实我都明白的。"
    "就像寻找雷亚的时候一样。"
    "如果不是迷路的孩子，是没有办法在这片雪地上留下足迹的。"
    "如果不是拥有羁绊的两人，是没有办法并肩前行的。"
    "但是现在，我连希菲尔的存在都感受不到了。"
    "已经，再也到达不了那片雪原了。"
    "已经，再也见不到希菲尔的身影了。"
    "只要想到这里，我的内心就宛如针扎一般难受。"
    pause 1.0 hard
    scene set only home night outside xuejian
    with slowdissolve
    pause 2.0 hard
    $ set_replay_scene("label21_1")
    scene set only xz_cg end two
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0607930.ogg"
    xz "没有改变。"
    play voice "voice/翔子/0607940.ogg"
    xz "都没有改变啊，凉君~"
    me01 "翔子......"
    play voice "voice/翔子/0607950.ogg"
    xz "夏天的星空也是、这个冬天的星空也是。"
    play voice "voice/翔子/0607960.ogg"
    xz "一点都没有改变，还是如此的美丽。"
    play voice "voice/翔子/0607970.ogg"
    xz "就像小时候一样，就像回忆中的一样......"
    play voice "voice/翔子/0607980.ogg"
    xz "我们明明都已经改变了这么多。"
    play voice "voice/翔子/0607990.ogg"
    xz "真是奇怪啊~"
    play voice "voice/翔子/0608000.ogg"
    xz "真是令人羡慕啊。"
    me01 "对不起翔子，到头来我还是一点办法都没有。"
    me01 "凭我自己是没有办法拯救希菲尔的。"
    me01 "为了拯救翔子你，雷亚选择了牺牲自己。"
    me01 "为了让我和雷亚重逢，立花老师也选择了离开。"
    me01 "而现在，为了让大家更好地活下去，希菲尔也不得不离开我们。"
    me01 "到底是为什么呢......"
    me01 "为什么我身边的人就必须遭受这样的经历才行呢？"
    me01 "为什么到头来，我只能给她们带来不幸呢？"
    me01 "明明我也想，为大家的幸福而努力一次。"
    me01 "明明我也想，成为一次被大家需要的、可靠的伙伴。"
    me01 "可是，为什么......"
    me01 "我究竟要怎么做才好。"
    me01 "翔子，现在的我一定让你失望了吧。"
    me01 "我果然还是无法像你所说的那样，成为优等生。"
    pause 0.1 hard
    scene set only xz_cg end one
    with dissolve
    play voice "voice/翔子/0608810.ogg"
    xz "凉君......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    with dissolve
    pause 1.0 hard
    $ renpy.pause(1.0, hard=True)
    play voice "voice/翔子/0608820.ogg"
    xz "你果然还是没有改变。"
    play voice "voice/翔子/0608840.ogg"
    xz "明明必须要改变的。在这片不变的星空下，我们明明......是必须要改变的。"
    play voice "voice/翔子/0608850.ogg"
    xz "正是因为仰望星空的我们改变了，才让这片永恒不变的宇宙看起来更加精彩不是吗？"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    play music first_36 fadein 3.0 if_changed
    pause 3.0 hard
    scene set only xz_cg yume xuejian one
    with slowdissolve
    pause 1.0 hard
    "抬头的一瞬间，眼前出现的竟然是梦的身影。"
    "刚刚翔子称呼我的时候叫的也是“凉君”。"
    play voice "voice/翔子/0608910.ogg"
    xz "凉君没有改变。"
    play voice "voice/翔子/0608930.ogg"
    xz "所以从一开始你就搞错了的。"
    play voice "voice/翔子/0608940.ogg"
    xz "因为搞错了，所以才会像现在这样一次又一次地擦肩而过。"
    play voice "voice/翔子/0608950.ogg"
    xz "一直在勉强的不是我......而是凉君你啊。"
    play voice "voice/翔子/0608960.ogg"
    xz "从以前开始......到现在也是。"
    play voice "voice/翔子/0608970.ogg"
    xz "虽然我或许也在逞强，但是凉君比起我来更加的严重。"
    play voice "voice/翔子/0609000.ogg"
    xz "我是知道的。"
    play voice "voice/翔子/0609020.ogg"
    xz "凉君很努力了。"
    play voice "voice/翔子/0609030.ogg"
    xz "所有的事情都自己一个人努力着。"
    play voice "voice/翔子/0609040.ogg"
    xz "不希望依靠谁。"
    play voice "voice/翔子/0609050.ogg"
    xz "也不想向谁求助。"
    play voice "voice/翔子/0609060.ogg"
    xz "明明稍微依靠一下也是可以的。"
    play voice "voice/翔子/0609070.ogg"
    xz "明明依赖别人......也是可以的。"
    play voice "voice/翔子/0609110.ogg"
    xz "所以呢......"
    pause 0.1 hard
    scene set only xz_cg yume xuejian two
    with dissolve
    play voice "voice/翔子/0609120.ogg"
    xz "稍微依靠一下我也是没有问题的。"
    play voice "voice/翔子/0609130.ogg"
    xz "你也说过的吧。"
    play voice "voice/翔子/0609190.ogg"
    xz "痛苦的时候，说出来就好了。"
    play voice "voice/翔子/0609200.ogg"
    xz "想要撒娇的时候，尽情撒娇就好了。"
    play voice "voice/翔子/0609210.ogg"
    xz "因为这才是家人。"
    play voice "voice/翔子/0609220.ogg"
    xz "才是朋友。"
    pause 0.1 hard
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0609230.ogg"
    xz "这才是......陪伴的意义啊——"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "仿佛有什么东西落下来了。"
    "从璀璨的星空落下的——纯白的碎片。"
    "一片片飘落在我的脸上，然后被泪水融化。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_cg yume xuejian four
    with dissolve
    play voice "voice/翔子/0609540.ogg"
    xz "你很努力了，凉君。"
    play voice "voice/翔子/0609550.ogg"
    xz "很了不起呢，凉君。"
    play voice "voice/翔子/0609560.ogg"
    xz "很痛苦吧，凉君......"
    play voice "voice/翔子/0609570.ogg"
    xz "现在就算哭出来也是没有关系的。"
    play voice "voice/翔子/0609580.ogg"
    xz "不用忍耐也是没有关系的。"
    pause 0.1 hard
    scene set only xz_cg yume xuejian three
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0609590.ogg"
    xz "因为我允许了~"
    me01 "谢谢你，翔子。"
    me01 "谢谢你，梦。"
    me01 "一直以来我都忍耐着不让别人看到我难过时的样子。"
    me01 "但这也许也只是我在害怕而已。"
    me01 "一直以来即便是有人在彼岸呼唤，我也只是等在原地而已。"
    me01 "鹊桥明明已经构建起来了。"
    me01 "而我，却一直没能渡过天河——"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ end_replay()

label day230.laboratory_event05:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    play music second_138 fadein 3.0 if_changed
    $ flcam.move(4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/白羽/711003050.ogg"
    baiyu "这样的条件似乎能行。"
    play voice "voice/白羽/711003060.ogg"
    baiyu "我们接下来要重现那片梦幻的世界。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show dh_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171002200.ogg"
    dh "这样一来，那些被迫成为{rb}灵继者{/rb}{rt}elfin{/rt}的大家，也终于能踏上自己希望的道路了吧。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711003070.ogg"
    baiyu "是啊，自己选择的道路果然还是要靠自己的双脚走完才是完美的吧。"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711003080.ogg"
    baiyu "然后这对于我们而言亦是如此。"
    hide dh_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711003090.ogg"
    baiyu "神野教授，丑话说在前面我所能做的也只有到这里为止了。"
    play voice "voice/白羽/711003100.ogg"
    baiyu "今后的事情，就拜托给你了。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711003110.ogg"
    baiyu "我们的努力能否顺利实现，关系到那些散落在世界各地的，正在迎接春天的{rb}灵继者{/rb}{rt}elfin{/rt}们。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711003120.ogg"
    baiyu "所以就请你好好地帮助他们吧。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show dh_zf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/171002210.ogg"
    dh "别说的事不关己似的，难不成你忘了自己还有宇宙开发任务在身吗？"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711003130.ogg"
    baiyu "也是啊。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711003140.ogg"
    baiyu "如果迎来春天的话，研究所拥有的{rb}灵继者{/rb}{rt}elfin{/rt}也就只剩下花山院一人了。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711003150.ogg"
    baiyu "将所有重担压在一名{rb}灵继者{/rb}{rt}elfin{/rt}宇航员的身上，这次计划未免也太过沉重了吧。"
    show baiyu_yjf_b1 b1 b1_s2
    play voice "voice/白羽/711003160.ogg"
    baiyu "搞不好的话，花山院也会变得像我的女儿一样......"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171002230.ogg"
    dh "......"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711003180.ogg"
    baiyu "所以你也知道的吧？如果真的变成那样的话，我的才能就没有用武之地了。"
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171002240.ogg"
    dh "别开玩笑了！"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_a2
    play voice "voice/神野大和/171002250.ogg"
    dh "现在的宇宙中心，大家都在拼命想要完成火星探测任务，别一个人自顾自地地说什么结束。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171002260.ogg"
    dh "观测至今，让那些资料发挥作用吧。为了将来有一天会降临的......崭新的时代。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show baiyu_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/白羽/711003190.ogg"
    baiyu "......"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171002270.ogg"
    dh "说到底，要我一个人拯救{rb}灵继者{/rb}{rt}elfin{/rt}还是太抬举我了。现在我深刻感受到了这一点。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171002280.ogg"
    dh "所以你也过来帮助我吧。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711003200.ogg"
    baiyu "......没想到居然会被你邀请啊。"
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171002290.ogg"
    dh "这不是邀请，是命令！"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711003210.ogg"
    baiyu "......你这毫无意义的自尊，还真是一点都没变啊~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    with dissolve
    pause 1.0 hard
    show baiyu_yjf_b1 b1 b1_n2 onlayer screens at side_left('baiyu'), basicfade
    play voice "voice/白羽/711003220.ogg"
    baiyu "雪......停止了。"
    show dh_zf_b1 b1 b1_s1 onlayer screens at side_right('dh'), basicfade
    play voice "voice/神野大和/171002300.ogg"
    dh "舞台准备好了吗？"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711003230.ogg"
    baiyu "接下来我们只能等待了。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711003240.ogg"
    baiyu "等待迎来春天，迎来崭新的时代——"
    hide dh_zf_b1
    hide baiyu_yjf_b1
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard

label day230.laboratory_event06:
    $ flcam.move(0, 0, 0)
    scene set only laboratory night outside xuejian2
    $ flcam.move(4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/天使莲/1705140.ogg"
    ts_lian "这是......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show dh_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/1802530.ogg"
    dh "怎么了？"
    play voice "voice/天使莲/1705150.ogg"
    ts_lian "刚才，我感受到了强烈的光。"
    hide dh_zf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/1705160.ogg"
    ts_lian "非常的......温暖。"
    show ts_lian_ssz_b1 b1 b1_h1
    play voice "voice/天使莲/1705170.ogg"
    ts_lian "简直就像......家人一样的感觉。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show dh_zf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/1802540.ogg"
    dh "......"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/1705180.ogg"
    ts_lian "明明关于家人的感觉，我早就已经记不清了。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/1802550.ogg"
    dh "我就是你的家人。"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/1705190.ogg"
    ts_lian "反正你也只是安慰我的而已......"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/1802560.ogg"
    dh "不是发过誓要永远在一起的吗？"
    show ts_lian_ssz_b1 b1 b1_ga2 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/天使莲/1705200.ogg"
    ts_lian "啊，摸人家头的大和君......最讨厌了。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/1705210.ogg"
    ts_lian "再说大和君你自己不也是有家人的吗？"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/1802570.ogg"
    dh "也许是吧。"
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/1802580.ogg"
    dh "“霞”也好，孩子们也罢，我一直都没有尽力去为他们做些什么。"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/1705220.ogg"
    ts_lian "就算是这样，不还是有我替你守护着他们的吗？"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/1802590.ogg"
    dh "是啊。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/1802600.ogg"
    dh "所以你也是，我的家人啊。"
    show ts_lian_ssz_b1 b1 b1_sp1
    play voice "voice/天使莲/1705240.ogg"
    ts_lian "......"
    show dh_zf_b1 b1 b1_sp1
    play voice "voice/神野大和/1802610.ogg"
    dh "这次又怎么了？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    with dissolve
    pause 2.0 hard
    show liuxing onlayer m2:
        xpos 0.45 ypos 0.3
    pause 1.0 hard
    play voice "voice/天使莲/1705250.ogg"
    ts_lian "流星。"
    play voice "voice/神野大和/1802620.ogg"
    dh "在哪里？"
    play voice "voice/天使莲/1705260.ogg"
    ts_lian "消失了......"
    play voice "voice/神野大和/1802630.ogg"
    dh "是吗。"
    pause 1.0 hard
    $ flcam.move(4500, 0, 900)
    scene set only laboratory night outside xuejian2
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.7
    with dissolve
    play voice "voice/天使莲/1705280.ogg"
    ts_lian "忘记许愿了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show dh_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/神野大和/1802640.ogg"
    dh "想许什么愿望？"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/1705290.ogg"
    ts_lian "秘密~"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/1802650.ogg"
    dh "是吗。"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/1705300.ogg"
    ts_lian "没有许愿果然......还是很遗憾啊。"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/1802660.ogg"
    dh "还能看到的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    with dissolve
    pause 1.0 hard
    show dh_zf_b1 b1 b1_n1 onlayer screens at side_left('dh'), basicfade
    play voice "voice/神野大和/1802670.ogg"
    dh "流星，一定还会再次划过这片天空的。"
    hide dh_zf_b1
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day230_home_event01:
        $ seen_day230_home_event01 = True
    $ _overworld_label = 'day230.home_event01'
    jump day230.map

label day230.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory night bedroom xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771004840.ogg"
    jsqd "小希菲尔......你一定也是为了这一刻才选择躲起来的吧。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004850.ogg"
    jsqd "唯独只有今天，希望自己一定能被凉君找到。"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    nvl clear
    pcenter "暮空开始发生变化——"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    $ set_replay_scene("label19_1")
    play music second_155 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(0, -3500, 600)
    scene set only balltower snow night xuejian end xuejian
    with slowdissolve
    pause 1.0 hard
    "月虹高挂。"
    "发出绚烂的光芒。"
    "如同彩虹一般在银河之中架起了一座闪光的桥。"
    "如同幻境一般，即便是在宇宙观测中心的数据库中也没有见过。"
    "月亮与太阳交织而成的——魔幻的天空。"
    "魔幻的世界。"
    "我在这光芒的指引下，向着钟楼广场进发——"
    play ambience1 zhong_rill fadein 3.0
    pause 1.0 hard
    me01 "找到你了，希菲尔。"
    pause 1.0 hard
    $ flcam.move(0, 9750, 900, duration=8.0, warper='ease_cubic')
    with dissolve
    pause 8.5 hard
    stop ambience1 fadeout 5.0
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5 yalign 4.45
    play voice "voice/希菲尔/001010440.ogg"
    xfe "嗯，被找到了~"
    me01 "不休息没关系吗？"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001010450.ogg"
    xfe "嗯，现在的话......没关系。"
    hide ts_xfe_yjz_b1 
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2:
        xpos 0.5 yalign 4.85
    play voice "voice/希菲尔/001010460.ogg"
    xfe "毕竟为了这一刻，希菲尔才拼命休息到现在的哟~"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001010470.ogg"
    xfe "因为还想再和凉君一起玩......所以才一直睡到现在的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5 yalign 4.45
    play voice "voice/希菲尔/001010480.ogg"
    xfe "对不起，让你担心了。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001010490.ogg"
    xfe "凉君，之前的约定还记得吗？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.5 yalign 4.85
    play voice "voice/希菲尔/001010500.ogg"
    xfe "希菲尔我变得有精神了，所以一起来玩吧。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5 yalign 4.85
    play voice "voice/希菲尔/001010510.ogg"
    xfe "一起来做雪人吧~"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg end two
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010520.ogg"
    xfe "以前也有像这样子，做过雪人吧？"
    me01 "好不容易做好的头还被希菲尔吃掉了。"
    play voice "voice/希菲尔/001010530.ogg"
    xfe "已经不会再做那种事了。"
    pause 0.1 hard
    scene set only xfe_cg end one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010540.ogg"
    xfe "希菲尔我已经不再是懵懂无知的小孩子了。"
    play voice "voice/希菲尔/001010550.ogg"
    xfe "和刚与凉君相遇时的我不一样了~"
    pause 0.1 hard
    scene set only xfe_cg end two
    with dissolve
    play voice "voice/希菲尔/001010560.ogg"
    xfe "就像凉君成长了一样，我也跟着成长了。"
    play voice "voice/希菲尔/001010570.ogg"
    xfe "原本不想改变的——和凉君的关系，也渐渐开始改变了。"
    play voice "voice/希菲尔/001010580.ogg"
    xfe "从朋友，变成恋人......"
    pause 0.1 hard
    scene set only xfe_cg end one
    with dissolve
    play voice "voice/希菲尔/001010590.ogg"
    xfe "所以，我才知道自己是不得不和凉君分开的。"
    pause 0.1 hard
    scene set only xfe_cg end two
    with dissolve
    play voice "voice/希菲尔/001010600.ogg"
    xfe "我仰望钟楼的理由也改变了。"
    play voice "voice/希菲尔/001010610.ogg"
    xfe "和凉君相遇之前的我，想着如果这个冬天能像这座钟楼一样，无论何时都能永远这样延续下去就好了。"
    play voice "voice/希菲尔/001010630.ogg"
    xfe "和凉君相遇后的我，果然也还是希望这个冬天能够继续下去。"
    play voice "voice/希菲尔/001010640.ogg"
    xfe "因为春天降临的话，就必须和凉君分开了。"
    play voice "voice/希菲尔/001010650.ogg"
    xfe "然后......现在的我，却希望春天能早点到来。"
    pause 0.1 hard
    scene set only xfe_cg end one
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010660.ogg"
    xfe "祈祷着大家的生活，能够随着春天的降临，像这座钟楼一样永远永远地持续下去。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow night end xuejian
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010670.ogg"
    xfe "永恒不变的东西，可能根本就不存在于这个世界上。不过......"
    play voice "voice/希菲尔/001010680.ogg"
    xfe "不想改变的东西果然还是存在的。"
    pause 1.0 hard
    scene set only xfe_cg end one
    with dissolve
    play voice "voice/希菲尔/001010690.ogg"
    xfe "为了守护那些不想改变的东西，我才必须和凉君告别的。"
    pause 0.1 hard
    scene set only xfe_cg end two
    with dissolve
    play voice "voice/希菲尔/001010700.ogg"
    xfe "悲伤的冬天已经结束了。"
    play voice "voice/希菲尔/001010710.ogg"
    xfe "温柔的春天马上就会降临。"
    play voice "voice/希菲尔/001010720.ogg"
    xfe "千冬告诉我的——温柔故事的完美结局。"
    play voice "voice/希菲尔/001010730.ogg"
    xfe "神明崩坏，妖精毁灭。但是人类却能够好好地存活下来。"
    play voice "voice/希菲尔/001010740.ogg"
    xfe "没有了争执，和平就会到来。"
    play voice "voice/希菲尔/001010750.ogg"
    xfe "没有了{rb}灵纹{/rb}{rt}rune{/rt}，大家脸上的笑容就会再一次绽放了吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow night end xuejian
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010760.ogg"
    xfe "{rb}灵纹{/rb}{rt}rune{/rt}之所以会在这颗星球上传播开来，也许是因为我降生的缘故。"
    play voice "voice/希菲尔/001010770.ogg"
    xfe "比起让人们变得幸福，{rb}灵纹{/rb}{rt}rune{/rt}更多地只会给人们带来不幸。"
    play voice "voice/希菲尔/001010780.ogg"
    xfe "凉君也是、千冬也是。"
    play voice "voice/希菲尔/001010790.ogg"
    xfe "其他的人也是，大家大家，都因为这不可思议的光而变得不幸了......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg end two
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010800.ogg"
    xfe "妖精和人类和睦地生活在一起。"
    play voice "voice/希菲尔/001010810.ogg"
    xfe "但是那样的情况不会长久。总有一天会迎来毁灭。"
    play voice "voice/希菲尔/001010820.ogg"
    xfe "纷争四起，终有一方会消失不见。"
    play voice "voice/希菲尔/001010830.ogg"
    xfe "因为，妖精和人类是不一样的。"
    play voice "voice/希菲尔/001010840.ogg"
    xfe "降生的星球是不一样的。"
    pause 0.1 hard
    scene set only xfe_cg end one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010850.ogg"
    xfe "对于这颗星球来说，合适的生命是必须的。"
    play voice "voice/希菲尔/001010860.ogg"
    xfe "我也是这么认为的。"
    play voice "voice/希菲尔/001010870.ogg"
    xfe "对我来说，这颗星球......很温暖。"
    play voice "voice/希菲尔/001010880.ogg"
    xfe "春天非常的......温暖。"
    play voice "voice/希菲尔/001010890.ogg"
    xfe "温暖到让我很难独自生存下去。"
    play voice "voice/希菲尔/001010900.ogg"
    xfe "习惯了温暖之后，如果不待在谁身边的话，就会冷到难以忍受的程度。"
    pause 0.1 hard
    scene set only xfe_cg end two
    with dissolve
    play voice "voice/希菲尔/001010910.ogg"
    xfe "所以......"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    nvl clear
    play voice "voice/希菲尔/001010920.ogg"
    pcenter "已经要和凉君......告别了。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg end two
    with dissolve
    play voice "voice/希菲尔/001010930.ogg"
    xfe "这次是真的......告别。"
    me01 "等等啊希菲尔。"
    me01 "告别什么的，不是说好不再说这么寂寞的话吗。"
    play voice "voice/希菲尔/001010940.ogg"
    xfe "凉君，请不要露出那样的表情。"
    play voice "voice/希菲尔/001010950.ogg"
    xfe "悲伤的寒冬已经结束了。"
    play voice "voice/希菲尔/001010960.ogg"
    xfe "再过不久这座城市，就会被樱花所覆盖。"
    pause 0.1 hard
    scene set only xfe_cg end one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010970.ogg"
    xfe "就会被笑容所填满。"
    pause 0.1 hard
    play sound xiaoshi_1
    scene set only xfe_cg end three
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001010980.ogg"
    xfe "拜拜凉君~"
    play voice "voice/希菲尔/001010990.ogg"
    xfe "对不起......凉君。"
    play voice "voice/希菲尔/001011000.ogg"
    xfe "没能两个人......一起走下去。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    "为什么呢......明明应该是开心的重逢才对。"
    "明明一直相信只要是两个人的话，就一定能克服困难的。"
    "明明一直这样相信着的......"
    pause 2.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower night xuejian
    show sepiagrain onlayer texture
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5 
    play voice "voice/希菲尔/001011010.ogg"
    xfe "希菲尔我还不想放弃。"
    play voice "voice/希菲尔/001011020.ogg"
    xfe "妖精与人类，是能够和睦相处的。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001011030.ogg"
    xfe "能不能再一次......相信它呢。"
    pause 2.0 hard
    hide sepiagrain
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg end three
    with dissolve
    play voice "voice/希菲尔/001011040.ogg"
    xfe "雪人......还没有完成呢。"
    play voice "voice/希菲尔/001011050.ogg"
    xfe "但是......就算真的完成了，春天降临的时候也会融化掉的。"
    play voice "voice/希菲尔/001011060.ogg"
    xfe "所以......这样就好。"
    pause 0.1 hard
    scene set only xfe_cg end four
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011070.ogg"
    xfe "这样......就好了——"
    pause 3.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ end_replay()
    "没有来得及伸出手。"
    "融化的积雪顺势掉落在了地上，仿佛一切都是一场梦。"
    "感觉不到温度。"
    "感觉不到呼吸。"
    "更感觉不到她的存在。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian end
    with dissolve
    pause 1.0 hard
    "温柔的魔法，解开了。"
    "而就在那一刻。"
    "三年未曾到访的春天降临在了这座城市。"
    pause 2.0 hard
    stop music fadeout 5.0
    scene black 
    with slowerdissolve
    pause 3.0 hard

label day230.laboratory_event07:
    $ flcam.move(0, 0, 0)
    scene set only laboratory night bedroom xuejian
    play music second_130 fadein 3.0
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771004860.ogg"
    jsqd "小希菲尔......成功解开魔法的不只有凉君而已。"
    show jsqd_dsf_b1 b1 b1_s3
    play voice "voice/千冬/771004870.ogg"
    jsqd "我也是一样的。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004880.ogg"
    jsqd "所以我无论如何......也无法认同这样的结局。"
    show jsqd_dsf_b1 b1 b1_s3
    play voice "voice/千冬/771004930.ogg"
    jsqd "明明我们大家都在尽力阻止小希菲尔你的。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771004940.ogg"
    jsqd "小希菲尔你知道吗？"
    play voice "voice/千冬/771004950.ogg"
    jsqd "雪花的结晶，是没有完全一样的。"
    play voice "voice/千冬/771004960.ogg"
    jsqd "小希菲尔的替代品，上哪里都是没有办法找到的。"
    show jsqd_dsf_b1 b1 b1_s1
    play voice "voice/千冬/771004970.ogg"
    jsqd "虽然小希菲尔你希望我们大家都能过上正常的生活。"
    play voice "voice/千冬/771004980.ogg"
    jsqd "但是无论怎么结交新的朋友，在那里没有小希菲尔的话......是不行的。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    nvl clear
    pcenter "姬神千冬开始轻声地哼起了歌谣。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    pcenter "虽然是第一次，但是却并不陌生。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    pcenter "那是在梦里希菲尔时常会哼起的歌谣——"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    stop music fadeout 5.0
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    pause 2.0 hard

label day230.battle_xfe:    
    $ flcam.move(0, 0, 0)
    scene set only fight_cg rune1
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    python:
        # 战斗boss为希菲尔，其他角色为镜像角色（除了雷亚），所有敌方等级、装备均与队伍中保持相同
        side_enemy_roles = []
        for ori_role in local_config.party + local_config.release:
            if ori_role.name != "希菲尔":
                role = getattr(store, ori_role.objectname + "_mirror")
                # 装备继承
                for cate, outfit in ori_role.outfits.items():
                    if outfit is not None:
                        outfit.enemy_equip_on(role)
                # 技能等级继承
                for skill in ori_role.skills:
                    new_skill = [s for s in role.skills if s.category == skill.category][0]
                    new_skill.level_change(skill.level)
                if len(ori_role.skills_v2) > 0:
                    for skill_v2 in ori_role.skills_v2:
                        new_skill = [s for s in role.skills_v2 if s.category == skill_v2.category][0]
                        new_skill.level_change(skill_v2.level)
                # 等级继承
                role.stats_check(ori_role.level)
                side_enemy_roles.append(role)
            else:
                # role = xfe_role_mirror
                # # 装备继承
                # for cate, outfit in ori_role.outfits.items():
                #     if outfit is not None:
                #         outfit.enemy_equip_on(role)
                # # 技能等级继承
                # for skill in ori_role.skills:
                #     new_skill = [s for s in role.skills if s.category == skill.category][0]
                #     new_skill.level_change(skill.level)
                # if len(ori_role.skills_v2) > 0:
                #     for skill_v2 in ori_role.skills_v2:
                #         new_skill = [s for s in role.skills_v2 if s.category == skill_v2.category][0]
                #         new_skill.level_change(skill_v2.level)
                #     # 等级继承
                # role.stats_check(ori_role.level)

                # xfe_role_mirror.battle_params_match(ori_role)

                xfe_role_mirror.equip_experience = 99999999
                xfe_role_mirror.stats_check(40)
                selected_equipments = ["weapon_num10_04", 
                                       "armor_num10_04", 
                                       "necklace_num10_04", 
                                       "ring_num10_04",
                                       "magic_fire_04",
                                       "stone_fire_04"]
                for cate in xfe_role_mirror.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments and outfit.category == cate)]
                    sample_outfit = enemy_outfits[0]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(xfe_role_mirror, 100)
                    sample_outfit.enemy_equip_on(xfe_role_mirror)
                for xi in range(20):
                    xfe_role_mirror.skill_levelup()

        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

    pause 0.25
    call battle(boss=xfe_role_mirror,
                boss_hp_plus=30000,
                side_enemy=side_enemy_roles, 
                side_hp_plus=15000,
                level=-1,
                boss_first=False, 
                win_condition='winter_special', 
                stay_turn=0,
                inside_label="inside_battle16", 
                mission_type="normal", 
                treasures={
                    "angel_tears": (1, 1.0)
                })

    if _return == "win":
        python:
            for role in local_config.release:
                if role.name == "希菲尔":
                    role.mp = role.max_mp
                    role.hp = role.max_hp + role.extend_max_hp
                    local_config.backup.append(role)
                    local_config.release.remove(role)
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day230.after_battle_xfe

label day230.after_battle_xfe:
    $ flcam.move(0, 0, 0)
    scene black
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011640.ogg"
    xfe "呜......呜呜......呜呜......"
    pause 1.0 hard
    play music second_157 fadein 3.0 if_changed
    scene set only xfe_cg end touch four
    with slowdissolve
    play voice "voice/希菲尔/001011650.ogg"
    xfe "......呜啊啊啊啊啊啊！"
    me01 "希菲尔......这下你总算明白了吧。"
    me01 "从一开始大家就没有讨厌过你。"
    me01 "没有讨厌过{rb}灵纹{/rb}{rt}rune{/rt}。"
    me01 "大家都因为这个冬天而收获了属于自己的幸福。"
    me01 "所以......"
    me01 "希菲尔也是，不需要再继续忍耐了。"
    me01 "不需要再一个人独自承受了。"
    me01 "不需要再一个人躲起来了。"
    me01 "试着把自己内心最真实的想法说出来吧。"
    me01 "我们大家，一定都会理解你的。"
    pause 0.1 hard
    scene set only xfe_cg end touch three
    $ flcam.move(1100, -750, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011660.ogg"
    xfe "......凉君。"
    play voice "voice/希菲尔/001011670.ogg"
    xfe "......想要留在身边。"
    play voice "voice/希菲尔/001011680.ogg"
    xfe "......想要一直在一起。"
    play voice "voice/希菲尔/001011690.ogg"
    xfe "......救救我。"
    pause 0.1 hard
    scene set only xfe_cg end touch four
    $ flcam.move(1100, -1400, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011700.ogg"
    xfe "......快救救我啊，凉君！"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    nvl clear
    pcenter "我说过的。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    pcenter "无论发生什么我都会救你的。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 3.0 hard
    $ set_replay_scene("label19_3")
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg end kiss one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/999997001.ogg"
    xfe "我是这么想的。"
    pause 0.1 hard
    scene set only xfe_cg end kiss two
    with dissolve
    play voice "voice/希菲尔/999997002.ogg"
    xfe "和他一起结下羁绊的话，虽然让我的生命得以延续下去，但他的生命也必然会在中途凋零。"
    play voice "voice/希菲尔/999997003.ogg"
    xfe "虽然不知会在何时发生，但却是必定会迎来的结果。"
    play voice "voice/希菲尔/999997004.ogg"
    xfe "尽管如此，我还是接受了。"
    play voice "voice/希菲尔/999997005.ogg"
    xfe "无法反抗他的意志。"
    play voice "voice/希菲尔/999997006.ogg"
    xfe "被大家的想法给影响了。"
    play voice "voice/希菲尔/999997007.ogg"
    xfe "无法抗拒自己想要被拯救的冲动。"
    pause 0.1 hard
    scene set only xfe_cg end kiss one
    $ flcam.move(0, -750, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/999997008.ogg"
    xfe "谢谢你......凉君。"
    play voice "voice/希菲尔/999997009.ogg"
    xfe "既然你赌上性命也要救我的话。"
    play voice "voice/希菲尔/999997010.ogg"
    xfe "我也会赌上性命保护你的。"
    play voice "voice/希菲尔/999997011.ogg"
    xfe "不会让你死掉。"
    pause 0.1 hard
    scene set only xfe_cg end kiss two
    $ flcam.move(0, -1400, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/999997012.ogg"
    xfe "两个人一起活下去吧。"
    play voice "voice/希菲尔/999997013.ogg"
    xfe "一起期待着那样的未来吧——"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    nvl clear
    play voice "voice/希菲尔/999997014.ogg"
    pcenter "妖精与人类和睦相处的那一天。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/希菲尔/999997015.ogg"
    pcenter "　　曾经无数次放弃的那条路\n　　　　　　让我们再一次朝它迈进吧。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory2
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/999997016.ogg"
    xfe "然后在这条雪道上，延续我们的足迹。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ end_replay()
    pause 3.0 hard
    play music second_158 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    scene end_graph2 at Pan((0, 0), (0, 3783), 250.0, time_warp=cgease, subpixel=True)
    show snow_level1 onlayer fg
    with slowerdissolve
    pause 5.0 hard
    show logo_second onlayer f2 at end_words
    pause 30.0 hard
    show end2_1 onlayer f2 at end_words with slowerdissolve
    show end_pic2_1 onlayer m2 at end_lpic with slowerdissolve
    pause 20.0 hard
    show end2_2 onlayer f2 at end_words with slowerdissolve
    show end_pic2_2 onlayer m2 at end_rpic with slowerdissolve
    pause 6.0 hard
    show end2_3 onlayer f2 at end_words with slowerdissolve
    pause 8.0 hard
    show end2_4 onlayer f2 at end_words with slowerdissolve
    pause 8.0 hard
    show end2_5 onlayer f2 at end_words with slowerdissolve
    show end_pic2_3 onlayer m2 at end_lpic with slowerdissolve
    pause 5.0 hard
    show end2_6 onlayer f2 at end_words with slowerdissolve
    pause 8.0 hard
    show end2_7 onlayer f2 at end_words with slowerdissolve
    show end_pic2_4 onlayer m2 at end_lpic with slowerdissolve
    pause 20.0 hard
    show end2_8 onlayer f2 at end_words with slowerdissolve
    show end_pic2_5 onlayer m2 at end_rpic with slowerdissolve
    pause 20.0 hard
    show end2_9 onlayer f2 at end_words with slowerdissolve
    show end_pic2_6 onlayer m2 at end_lpic with slowerdissolve
    pause 20.0 hard
    show end2_10 onlayer f2 at end_words with slowerdissolve
    show end_pic2_7 onlayer m2 at end_rpic with slowerdissolve
    pause 35.0 hard
    hide snow_level1
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 5.0 hard
    jump day231
