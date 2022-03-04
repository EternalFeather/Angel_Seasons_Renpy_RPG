label day211:
    bookmark
    $ save_name = _("Day 211")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date209 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    with slowerdissolve
    show snow_level1 onlayer fg
    play music second_114 fadein 3.0 if_changed
    pause 2.0 hard
    hide snow_level1
    scene set only school day room xuejian
    $ flcam.move(2250, -350, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    show yj_dzf_b2 b2 b2_s1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010106420.ogg"
    xz "挂科了......所以要补习吧。"
    show yj_dzf_b2 b2 b2_s2
    play voice "voice/植澄友加/020108680.ogg"
    yj "嗯......老师说下周也得来学校。"
    hide xz_dzf_b2
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yczs_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180102060.ogg"
    yczs "明明是难得的寒假，请节哀。"
    hide yj_dzf_b2 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_ga3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020108690.ogg"
    yj "也不是这样的，反正还有社团活动来学校这一点也不会变的。"
    show yj_dzf_b3 b3 b3_n1
    play voice "voice/植澄友加/020108700.ogg"
    yj "补习也只有早上而已，下午之后就能参加社团活动了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "虽然假期暂时没有什么特别的安排。"
    "但是圣诞和初诣还是值得期待的。"
    pause 1.0 hard
    hide snow_level1
    scene set only school day room xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    with dissolve
    show yj_dzf_b2 b2 b2_h4 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020108710.ogg"
    yj "比起补习，圣诞节怎么打算？难得的机会大家找个地方聚一聚吗？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yczs_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180102070.ogg"
    yczs "我的话......"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180102060.ogg"
    yczs "难得的圣诞时间我要陪小桃一起。"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_ga3 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020108720.ogg"
    yj "开始变得像个好哥哥了嘛~"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180102090.ogg"
    yczs "你有意见吗......那我差不多也要回去了。"
    pause 0.5 hard
    play sound jiaobu2
    show yczs_dzf_b1 b1 b1_ga1 at walkout_l(0.3)
    pause 1.0 hard
    hide yczs_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_ga1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020108730.ogg"
    yj "啊，逃跑了。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010106440.ogg"
    xz "圣诞节友加不和姐姐一起过吗？"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_ga3 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020108740.ogg"
    yj "完全没有，姐姐说她那天有工作。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010106450.ogg"
    xz "......这样啊。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020108750.ogg"
    yj "翔子你要和凉君一起过？"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_ga3 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010106460.ogg"
    xz "为什么要和神野君啊......一般是和爱衣一起啦。"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_h1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020108760.ogg"
    yj "那就在翔子家集合吧，大家一起开圣诞party了~"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010106470.ogg"
    xz "能不要擅自决定吗......"
    hide xz_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    show yj_dzf_b3 b3 b3_n1
    play voice "voice/植澄友加/020108770.ogg"
    yj "凉君，这样可以吗？"
    me01 "听起来不错，爱衣也会很开心的。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010106480.ogg"
    xz "神野君也不要擅自决定好吗......"
    show yj_dzf_b3 b3 b3_n3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020108780.ogg"
    yj "翔子，不行吗~"
    show xz_dzf_b1 b1 b1_ga3
    play voice "voice/翔子/010106490.ogg"
    xz "稍微等等吧，具体怎么安排之后会再联系你。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_ga4 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020108790.ogg"
    yj "也是呢，毕竟翔子的父母可能也会回来吧？"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010106500.ogg"
    xz "唯独这点我觉得不会，我指的安排是想确认一下爱衣那边的情况而已。"
    me01 "毕竟怜同学才是爱衣的亲姐姐吗......"
    show yj_dzf_b2 b2 b2_h1
    play voice "voice/植澄友加/020108880.ogg"
    yj "凉君也是，要好好地把圣诞节空出来哟~"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/010106550.ogg"
    xz "虽然计划还没定下来。"
    me01 "我知道了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day211.school_event01:
    play sound open_door5
    $ flcam.move(0, 0, 0)
    scene set only school day corridor xuejian
    with slowdissolve
    pause 1.0 hard
    play music second_118 fadein 3.0
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    me01 "翔子你现在要去学生会对吧？"
    play voice "voice/翔子/010106560.ogg"
    xz "嗯，得去结算一下今年的工作，神野君你呢？"
    me01 "我的话应该是去接爱衣放学吧。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010106570.ogg"
    xz "那就拜托你了~"
    show xz_dzf_b3 b3 b3_n1
    play voice "voice/翔子/010106580.ogg"
    xz "圣诞节......要是大家都能开心的话就好了。"
    hide xz_dzf_b3 with None
    pause 0.1 hard
    show xz_dzf_b2 b2 b2_sp2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/翔子/010106590.ogg"
    xz "当然我指的不是两人独处那方面！"
    "感觉像在看独角戏一样。"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010106600.ogg"
    xz "都怪友加刚才说了奇怪的话......"
    me01 "奇怪的话是指什么？"
    show xz_dzf_b2 b2 b2_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010106610.ogg"
    xz "我才不知道。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010106620.ogg"
    xz "神野君你最想和谁一起过圣诞节？"
    me01 "这个嘛......"
    show xz_dzf_b2 b2 b2_sp1
    play voice "voice/翔子/010106630.ogg"
    xz "就没有特别想和谁一起过吗？"
    me01 "能和翔子你们一起过度过我就很满足了。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010106640.ogg"
    xz "真的吗？"
    "当然要是雷亚和希菲尔也能出现的话就更好了。"
    "也许聚会的确是一个不错的选择。"
    "虽然也想和翔子单独待一会儿。"
    "真是艰难的抉择。"
    me01 "翔子你最想和谁一起过呢？"
    hide xz_dzf_b3 with None
    pause 0.1 hard
    show xz_dzf_b1 b1 b1_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010106650.ogg"
    xz "现、现在不是讨论我的时候吧。"
    me01 "意思是不能说？"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010106660.ogg"
    xz "意思是和神野君没有关系。"
    me01 "这种双标的态度可不行啊。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.48
    xz "......"
    me01 "抱歉是我错了，还请别用这种眼神看我......"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010106670.ogg"
    xz "我差不多要去学生会了。"
    me01 "那晚点见吧。"
    show xz_dzf_b2 b2 b2_n1
    play voice "voice/翔子/010106680.ogg"
    xz "嗯，晚点见~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day211.school_event02:
    $ flcam.move(0, 0, 0)
    scene set only school day room2 xuejian
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show qbj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/千波姐/160102200.ogg"
    qbj "哈啊......"
    play music second_119 fadein 3.0 if_changed
    $ flcam.move(2250, -350, 750, duration=1.5)
    show szl_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/050103090.ogg"
    szl "怎么了愁眉苦脸的，这学期的工作不是已经结束了吗？"
    show qbj_dzf_b1 b1 b1_ga1
    play voice "voice/千波姐/160102210.ogg"
    qbj "怎么可能结束，我倒是觉得会这样一直持续下去。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/050103100.ogg"
    szl "你也真是劳苦命啊......"
    hide szl_dzf_b3
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/010106690.ogg"
    xz "不过那样反而更有紧张感，某种程度也上比较好吧。"
    hide xz_dzf_b2
    $ flcam.move(2250, -350, 750, duration=1.5)
    show rxl_dzf_b2 b2 b2_h3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102760.ogg"
    rxl "嘛，还请注意不要劳累过度倒下了。"
    show qbj_dzf_b1 b1 b1_ga2
    play voice "voice/千波姐/160102220.ogg"
    qbj "倒也不至于会到累倒的程度......"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102770.ogg"
    rxl "果然是关于丰胸的烦恼吗？"
    show qbj_dzf_b1 b1 b1_sp1
    play voice "voice/千波姐/160102230.ogg"
    qbj "欸？"
    show rxl_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.7
    play sound yangmu
    show yangmu onlayer m2:
        xalign 0.70 yalign 0.45
    play voice "voice/日向怜/120102780.ogg"
    rxl "这样的话由我来帮你揉揉吧~"
    play sound jump_1
    show qbj_dzf_b1 b1 b1_sp2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/千波姐/160102240.ogg"
    qbj "{size=72}呀！{/size}"
    $ flcam.move(1500, -150, 450, duration=1.5)
    hide yangmu
    pause 0.5 hard
    show qbj_dzf_b1 b1 b1_sp2:
        xpos 0.5
        linear 0.5 xpos 0.4
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_a1 onlayer m1:
        xpos 0.6
    show rxl_dzf_b1 b1 b1_h3:
        xpos 0.7
        linear 0.5 xpos 0.8
    play voice "voice/水之濑/050103110.ogg"
    szl "{size=72}住手！{/size}"
    play sound hite_light
    show wflash onlayer texture
    with vpunch
    hide yangmu
    show rxl_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.8
    play voice "voice/日向怜/120102790.ogg"
    rxl "好痛！"
    hide qbj_dzf_b1
    $ flcam.move(5000, -350, 750, duration=1.5)
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_a1 onlayer m1:
        xpos 0.6
    play voice "voice/水之濑/050103120.ogg"
    szl "你已经可以滚了。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.8
    play voice "voice/日向怜/120102800.ogg"
    rxl "好过分啊......我明明只是想帮会长放松一下而已。"
    hide rxl_dzf_b2
    hide szl_dzf_b3
    $ flcam.move(-5000, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.2
    show qbj_dzf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.4
    play voice "voice/翔子/010106700.ogg"
    xz "这是今年最后的工作了吧？"
    play voice "voice/千波姐/160102250.ogg"
    qbj "嗯，就是开个总结会而已，鼓励来年继续加油的。"
    show qbj_dzf_b1 b1 b1_h1
    play voice "voice/千波姐/160102260.ogg"
    qbj "新的学期还请各位多多关照~"
    show qbj_dzf_b1 b1 b1_n1
    play voice "voice/千波姐/160102270.ogg"
    qbj "也没打算花太长时间，赶快结束去吃饭吧。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.2
    play voice "voice/翔子/010106710.ogg"
    xz "我去泡个茶吧~"
    hide xz_dzf_b1
    hide qbj_dzf_b1
    $ flcam.move(5000, -350, 750, duration=1.5)
    show szl_dzf_b3 b3 b3_n1 onlayer m1:
        xpos 0.6
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.8
    play voice "voice/水之濑/050103170.ogg"
    szl "太好了，柚子又能好好振作起来了。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.8
    play voice "voice/日向怜/120102810.ogg"
    rxl "说的也是呢，毕竟还在发育中很快就会变大的。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.6
    play voice "voice/水之濑/050103180.ogg"
    szl "你的脑子里果然全是胸啊......"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.8
    play voice "voice/日向怜/120102820.ogg"
    rxl "我的意思是指“作为会长的责任感成长”了的说。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/050103190.ogg"
    szl "......"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.8
    play voice "voice/日向怜/120102830.ogg"
    rxl "小凛你真是好色啊~"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_a1 onlayer m1:
        xpos 0.6
    play voice "voice/水之濑/050103200.ogg"
    szl "都是你带来的负面影响好吗！"
    show rxl_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.8
    play voice "voice/日向怜/120102840.ogg"
    rxl "我会继续这样影响你的~"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s1 onlayer m1:
        xpos 0.6
    play voice "voice/水之濑/050103210.ogg"
    szl "你可能是想这样和我搞好关系......但是很遗憾，我可不是和谁都会亲近的野猫。"
    show szl_dzf_b2 b2 b2_n2
    play voice "voice/水之濑/050103220.ogg"
    szl "对你们是自然，就算是对饲主说不定也会露出獠牙的。"
    show rxl_dzf_b1 b1 b1_sp1
    play voice "voice/日向怜/120102850.ogg"
    rxl "也就是说，小凛你是被谁“饲养”着吧？"
    show szl_dzf_b2 b2 b2_s4
    play voice "voice/水之濑/050103230.ogg"
    szl "那只是比喻而已。"
    show rxl_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.8
    play voice "voice/日向怜/120102860.ogg"
    rxl "对我来说，比起露出獠牙还是更希望你能脱掉衣服啊~"
    hide szl_dzf_b2
    show szl_dzf_b1 b1 b1_s1 onlayer m1:
        xpos 0.6
    play voice "voice/水之濑/050103240.ogg"
    szl "......再也不想和你正经说话了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 3.0 hard

label day211.school_event03:
    $ flcam.move(0, 0, 0)
    scene set only school day center room xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    me01 "喂！"
    play music second_108 fadein 3.0 if_changed
    show tyt_wnf_b1 b1 b1_s1 onlayer screens at side_left('tyt'), basicfade
    play voice "voice/藤原瞳/131401330.ogg"
    tyt "呼——"
    hide tyt_wnf_b1
    me01 "想活命的话，就赶快给我起来！"
    show tyt_wnf_b1 b1 b1_n2 onlayer screens at side_left('tyt'), basicfade
    play voice "voice/藤原瞳/131401340.ogg"
    tyt "我是醒着的，只是有点想冬眠而已。"
    hide tyt_wnf_b1
    me01 "如果是这样的话就赶快回教室去。"
    play sound touch
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5 ypos 1.03 alpha 0.0
        parallel:
            linear 1.0 ypos 0.98
        parallel:
            linear 1.0 alpha 1.0
    pause 1.5 hard
    play voice "voice/藤原瞳/131401350.ogg"
    tyt "今天前辈也是笨笨的呢。"
    me01 "总觉得你这个角色设定有太多重复，有点多余啊！"
    me01 "还有你来这里干什么，琉璃可不在这里。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131401360.ogg"
    tyt "正因为如此我才来的。"
    play voice "voice/藤原瞳/131401370.ogg"
    tyt "一想到花山院最喜欢这里，就自然而然地来了。"
    me01 "你这个理由很牵强啊......"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131401380.ogg"
    tyt "前辈不是也一样的吗？"
    hide tyt_wnf_b1
    $ flcam.move(4500, 4000, 1500, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    "藤原瞳刚才睡觉的地方，是琉璃平时最常坐的长椅。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    me01 "不过你是怎么不留下脚印就来到这里的啊？"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131401390.ogg"
    tyt "这是我的灵能力。"
    me01 "你还真是个......厉害的巫女啊。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131401410.ogg"
    tyt "就是这样~"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131401420.ogg"
    tyt "哼哼~"
    me01 "这欠揍的笑声是闹哪样啊？！"
    play voice "voice/藤原瞳/131401430.ogg"
    tyt "你上当了~"
    me01 "能弄哭你吗。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131401440.ogg"
    tyt "我今天是穿着雪橇来上学的，所以才没有留下脚印啊。"
    me01 "你又整这么花哨的上学方式，巫女服还不是你的极限吗！"
    play voice "voice/藤原瞳/131401450.ogg"
    tyt "我住的神社离学校很远，所以比起穿长靴走过来，还是滑雪更轻松些。"
    me01 "不坐电车吗？"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131401470.ogg"
    tyt "这个不太方便，发车数量又少要是没赶上要等好久。"
    me01 "按照班车的时间来安排不就好了吗。"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131401480.ogg"
    tyt "我的灵能力无法完成这个任务，前辈果然还是太肤浅了。"
    me01 "是你自己没有时间观念而已吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    play music second_140 fadein 3.0 if_changed
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131401490.ogg"
    tyt "前辈是如何看待花山院的呢？"
    "话题一转，藤原瞳把脸瞥向了无人的长椅说道。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131401510.ogg"
    tyt "我不怎么明白这些东西。"
    play voice "voice/藤原瞳/131401540.ogg"
    tyt "所以很难和别人保持亲近。"
    me01 "硬要说的话就是一见如故的感觉吧？"
    me01 "虽然只是朋友，但是见不到面的时候还是会感到寂寞的。"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/131401610.ogg"
    tyt "这样的话，为了消除前辈的寂寞感，要不要参观下神社的陨石？"
    me01 "陨石？"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131401620.ogg"
    tyt "就是在星天宫神社祭坛被供奉的神石。"
    "虽然雷亚曾说过自己凭依的陨石是坐落在樱华镇附近的可能性最大。"
    "但雪见市距离樱华镇也只不过数十公里的距离而已。"
    "为了保险起见还是有必要确认一下。"
    "毕竟不久前雷亚也在这里现身了。"
    "那种强烈的感觉是不会骗人的。"
    me01 "可是为什么突然邀请我看陨石？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131401630.ogg"
    tyt "请把它当成花山院来让自己好受一点吧。"
    me01 "白痴吗你。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131401640.ogg"
    tyt "要去吗？"
    me01 "当然要......请务必带我见识一下！"
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school snow day outside xuejian2
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/藤原瞳/131401660.ogg"
    tyt "眨眼间就已经是这个时候了，难道是时空在我眨眼的瞬间发生扭曲了吗？"
    me01 "只是因为你一直在睡觉的缘故吧。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131401670.ogg"
    tyt "我现在总算明白花山院不在时那种对时间流逝感到淡然的感觉。"
    me01 "......别突然正经起来啊。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131401680.ogg"
    tyt "就算花山院不在身边，也请别把我当做慰藉的替代品。"
    me01 "我觉得这是不可能发生的事情。"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131401690.ogg"
    tyt "好冷......好困。"
    me01 "你这家伙还真是让人捉摸不透。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131401700.ogg"
    tyt "今天从早上开始就一直在下雪。"
    me01 "再不出发的话积雪可是要没过膝盖了。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131401650.ogg"
    tyt "那我们出发吧~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day211'
    $ seen_day211_shenshe_event01 = False
    $ seen_day211_school_event04 = False
    $ seen_day211_laboratory_event01 = False
    $ seen_day211_bridge_event01 = False
    $ seen_day211_kindergarden_event02 = False

label day211.map:
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
    if _overworld_label == 'day211':
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day211.shenshe_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    elif _overworld_label == 'day211.school_event04':
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day211.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'])
    elif _overworld_label == 'day211.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        shenshe=("day211.shenshe_event01", "not seen_day211_shenshe_event01"),
        school=("day211.school_event04", "not seen_day211_school_event04 and seen_day211_shenshe_event01"),
        laboratory=("day211.laboratory_event01", "not seen_day211_laboratory_event01 and seen_day211_school_event04"),
        bridge=("day211.bridge_event01", "not seen_day211_bridge_event01 and seen_day211_laboratory_event01"),
        kindergarden=("day211.kindergarden_event02", "not seen_day211_kindergarden_event02 and seen_day211_bridge_event01"))
    $ window_animate_outro()
    if _return == 'day211.shenshe_event01':
        $ flcam.move(*overworld.camera_positions['shenshe'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day211.school_event04':
        $ flcam.move(*overworld.camera_positions['school'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day211.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day211.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day211.kindergarden_event02':
        $ flcam.move(*overworld.camera_positions['kindergarden'], duration=3.0, warper='easeout_cubic')
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

label day211.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only shenshe day xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    "白天的神社显得格外冷清。"
    "由于平时有巫女负责扫雪的缘故，这里并没有太多的积雪。"
    pause 1.0 hard
    scene set only shenshe day inside xuejian
    play music second_120 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/藤原瞳/131401760.ogg"
    tyt "按照前辈的要求，我已经换上了干净的衣服。"
    me01 "我可不记得提出过这样的要求。"
    me01 "行了，快点给我看看吧。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131401820.ogg"
    tyt "我的裸体吗？"
    me01 "才不是！"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131401830.ogg"
    tyt "我这身衣服下可什么都没穿。"
    play voice "voice/藤原瞳/131401840.ogg"
    tyt "但是很可惜，我不是可以攻略的角色。"
    me01 "那你到底是什么？"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131401850.ogg"
    tyt "重要的伏笔角色。"
    me01 "不要剧透啊！"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131401860.ogg"
    tyt "脱下这层布料的话，我就是全裸了。"
    me01 "你不冷吗？"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131401870.ogg"
    tyt "你是打算来温暖我吗？"
    me01 "我回去了......"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131401880.ogg"
    tyt "这就是神社供奉的陨石。"
    me01 "还真是变脸如翻书一样快。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only shenshe stone
    with slowdissolve
    pause 1.0 hard
    "神社正殿的祭台被独特的光芒包裹着，闪闪发光的陨石就陈列在上面。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only shenshe day inside xuejian
    show snow_level1 onlayer fg
    show tyt_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/藤原瞳/131401910.ogg"
    tyt "所谓的陨石，是经历了很长时间才降落到地球上的星之碎片。"
    play voice "voice/藤原瞳/131401920.ogg"
    tyt "所以这其中一定蕴含着神秘的力量，就如同比电磁波之类的。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131401930.ogg"
    tyt "虽然这些是星天宫科研小组调查的结果，但是我觉得应该错不了。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131401940.ogg"
    tyt "然后，能够承载这股力量的道具则被称为{encyclopedia=caiwu}{rb}祭器{/rb}{rt}採物{/rt}{/encyclopedia}。"
    play voice "voice/藤原瞳/131401950.ogg"
    tyt "我们在神乐时会使用的薙刀也是其中之一。"
    me01 "原来如此。"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/131402060.ogg"
    tyt "稍微对前辈有些帮助了吗？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131402070.ogg"
    tyt "陨石之中也许蕴藏着不可思议的力量。"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131402140.ogg"
    tyt "我希望前辈能够利用这股力量帮助花山院。"
    play voice "voice/藤原瞳/131402150.ogg"
    tyt "因为身为星天宫巫女的我，是没有办法插手其中的......"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day211.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school snow day outside xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    play music second_108 fadein 3.0 if_changed
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_h4 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001001200.ogg"
    xfe "叭咕叭咕~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031000330.ogg"
    lhx "......雪很好吃吗？"
    hide ts_xfe_yjz_b3 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/希菲尔/001001210.ogg"
    xfe "就像在舌头上弹奏出的旋律谱写成了绝妙的乐章的感觉哟~"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031000340.ogg"
    lhx "我只觉得那只是杀戮兵器而已。"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h4 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/希菲尔/001001220.ogg"
    xfe "叭咕叭咕~"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031000350.ogg"
    lhx "你来这里有什么事吗？找人的话现在还不到放学的时间。"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/001001230.ogg"
    xfe "生理是什么呢？"
    show lhx_dzf_b2 b2 b2_s2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/031000360.ogg"
    lhx "为什么突然问这种事情啊......"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001001240.ogg"
    xfe "刚才，那边的小朋友们在说这个。"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031000370.ogg"
    lhx "多半又是千波吧......"
    stop music fadeout 5.0
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031000380.ogg"
    lhx "话说回来，你来这里不会只是为了和我说这个的吧？"
    play music second_103 fadein 3.0
    hide ts_xfe_yjz_b2 
    show ts_xfe_yjz_b3 b3 b3_n2 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001001250.ogg"
    xfe "我想想请你帮个忙。"
    show lhx_dzf_b3 b3 b3_sp2
    play voice "voice/立花希/031000390.ogg"
    lhx "......"
    hide lhx_dzf_b3
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001001260.ogg"
    xfe "请你帮助凉君和他的家人。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001001280.ogg"
    xfe "拜托你。"
    pause 0.5 hard
    show wflash onlayer texture
    play sound xiaoshi_1
    show ts_xfe_yjz_b1 b1 b1_s1:
        xpos 0.7 alpha 1.0
        linear 0.8 alpha 0.0
    stop music fadeout 5.0
    pause 3.0 hard
    hide ts_xfe_yjz_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b3 b3 b3_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031000400.ogg"
    lhx "真是耐人寻味的内容......"
    pause 0.5 hard
    play music second_123 fadein 3.0 if_changed
    play sound rune1
    show wflash onlayer texture
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b3 with None
    pause 0.1 hard
    show lhx_dzf_b2 b2 b2_s3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031000410.ogg"
    lhx "......"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day211_shenshe_event01:
        $ seen_day211_shenshe_event01 = True
    $ _overworld_label = 'day211.shenshe_event01'
    jump day211.map

label day211.school_event04:
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    play ambience1 rain fadein 3.0
    with slowdissolve
    pause 1.0 hard
    "从神社回来的路上开始下起雨。"
    "因为习惯了不会堆积的雪所以并没有带伞的习惯。"
    "本想等雨小一些再去接爱衣的，但过了许久雨也没有减弱的趋势。"
    "这样下去可不是办法。"
    "总之先联系下翔子吧，在她结束学生会的工作之前就先在学校等着吧。"
    pause 1.0 hard
    scene set only school night outside xuejian2
    with dissolve
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    play voice "voice/植澄友加/021204640.ogg"
    stranger "凉君~"
    play sound jiaobu4
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play music second_111 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg rain one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021204650.ogg"
    yj "刚好我包里有一把折叠伞。"
    me01 "社团活动那边结束了吗？"
    play voice "voice/植澄友加/021204660.ogg"
    yj "啊嗯。因为是这种天气，所以今天取消了。" 
    play voice "voice/植澄友加/021204670.ogg"
    yj "下雨的话也是没办法的事嘛。"
    me01 "不过托你的福我也得救了。"
    play voice "voice/植澄友加/021204680.ogg"
    yj "嗯、嗯。"
    me01 "不过......"
    pause 0.1 hard
    scene set only yj_cg rain two
    with dissolve
    play voice "voice/植澄友加/021204690.ogg"
    yj "欸？"
    me01 "不会觉得有些挨得太近了吗？"
    "虽然有了之前和琉璃接触的经验，但是面对突如其来的状况还是令我心跳加速。"
    "毕竟我不太擅长应付这样的情况。"
    play voice "voice/植澄友加/021204700.ogg"
    yj "因、因为伞很小所以没办法啊。"
    "友加嘴上这么说着，身体却越靠越近。"
    play voice "voice/植澄友加/021204710.ogg"
    yj "如、如果不这样的话就会淋湿了。"
    me01 "我淋湿的话倒是无所谓。"
    pause 0.1 hard
    scene set only yj_cg rain one
    with dissolve
    play voice "voice/植澄友加/021204720.ogg"
    yj "不可以啦，你好好进来啊凉君。"
    "手臂被稍微拉了过去，两个人再一次紧密地靠在了一起。"
    pause 0.1 hard
    scene set only yj_cg rain two
    with dissolve
    play voice "voice/植澄友加/021204730.ogg"
    yj "凉君......脸很红啊。"
    play voice "voice/植澄友加/021204740.ogg"
    yj "觉得困扰吗？"
    me01 "没、没有。"
    pause 0.1 hard
    scene set only yj_cg rain one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021204750.ogg"
    yj "是吗~"
    pause 0.1 hard
    scene set only yj_cg rain three
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021204760.ogg"
    yj "太好了。"
    play voice "voice/植澄友加/021204770.ogg"
    yj "诶嘿~"
    play voice "voice/植澄友加/021204780.ogg"
    yj "这样就帮上凉君的忙了。"
    me01 "为什么这么想要帮我的忙呢？"
    play voice "voice/植澄友加/021204790.ogg"
    yj "那个，怎么说呢......"
    play voice "voice/植澄友加/021204800.ogg"
    yj "凉君也帮助了我不是吗。"
    me01 "意思就是说像回礼一样？"
    play voice "voice/植澄友加/021204810.ogg"
    yj "虽然是这样，但也不全是。"
    play voice "voice/植澄友加/021204820.ogg"
    yj "总觉得没法好好表达出来，啊哈哈~"
    me01 "我之前也说过的，不必放在心上。"
    pause 0.1 hard
    scene set only yj_cg rain one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021204830.ogg"
    yj "“别放在心上”什么的是不可能的。"
    me01 "......"
    play voice "voice/植澄友加/021204840.ogg"
    yj "因为已经在意起来了。对我来说，这可是非常非常重要的事。"
    pause 0.5 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge day under xuejian alpha
    show sepiagrain onlayer texture
    with slowdissolve
    pause 1.0 hard
    "那天在河滩上帮助友加控制住暴走的灵纹时。"
    "我的确是能感觉到自己是不想失去她的。"
    pause 1.0 hard
    scene set only yj_cg rain one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021204850.ogg"
    yj "凉君......也会把我放在心上的吧。（小声）"
    me01 "这种事还需要再问吗。"
    pause 0.1 hard
    scene set only yj_cg rain four
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021204860.ogg"
    yj "嗯~"
    pause 0.1 hard
    scene set only yj_cg rain three
    with dissolve
    play voice "voice/植澄友加/021204870.ogg"
    yj "那个，虽然有点突然......"
    me01 "现在要去你姐姐那里吧？"
    me01 "正好离幼儿园放学还有些时间，我就陪你一起去吧。"
    pause 0.1 hard
    scene set only yj_cg rain four
    with dissolve
    play voice "voice/植澄友加/021204910.ogg"
    yj "......谢谢你，凉君。"
    stop music fadeout 5.0
    stop ambience1
    pause 1.0 hard 
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day211_school_event04:
        $ seen_day211_school_event04 = True
    $ _overworld_label = 'day211.school_event04'
    jump day211.map

label day211.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    play music second_112 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/圣护院/150101370.ogg"
    shy "怎么......又来了吗？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b2 b2 b2_ga4 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/植澄友加/020109640.ogg"
    yj "抱歉姐姐，在你工作的时候过来打扰。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101380.ogg"
    shy "嘛，在休息时间陪你们一下倒也无所谓。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101390.ogg"
    shy "今天有什么事？"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020109650.ogg"
    yj "姐姐你有好好吃饭吗？"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150101400.ogg"
    shy "最近不是一直都和你一起吃的吗？"
    play voice "voice/植澄友加/020109660.ogg"
    yj "虽然早饭和晚饭是这样没错，那午饭又怎么样呢？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101410.ogg"
    shy "虽然没有记忆，不过应该是吃过了。"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_a2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020109670.ogg"
    yj "这绝对是没吃的吧。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/150101420.ogg"
    shy "身体都还能动，没问题的吧。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020109680.ogg"
    yj "真是的......要好好吃饭啊。不然的话我可要叫花山院教训你了哟。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101430.ogg"
    shy "我会努力处理好的。"
    hide yj_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "看来现在的工作依旧很忙的样子。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150101440.ogg"
    shy "你找我也有事吗？"
    me01 "只是想稍微问点事情。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b2 b2 b2_h4 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020109690.ogg"
    yj "这边的才是正题~"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101450.ogg"
    shy "我想也是，毕竟如果只是关心我的话没必要让他也跟着来。"
    me01 "我也很担心圣护院小姐的身体啊。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150101460.ogg"
    shy "比起我更希望你留意的是友加，至少帮我监督她在学校不要胡乱地使用{rb}灵纹{/rb}{rt}rune{/rt}。"
    show yj_dzf_b2 b2 b2_ga1
    play voice "voice/植澄友加/020109700.ogg"
    yj "......信用度为零啊。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101470.ogg"
    shy "所以，你想问的是什么？"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020109710.ogg"
    yj "希望你能告诉我们关于{rb}灵继者{/rb}{rt}elfin{/rt}的事。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150101480.ogg"
    shy "为什么要问这些？"
    show yj_dzf_b3 b3 b3_ga3
    play voice "voice/植澄友加/020109720.ogg"
    yj "毕竟我也变成了{rb}灵继者{/rb}{rt}elfin{/rt}，所以有些在意。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101490.ogg"
    shy "我觉得最低限度必要的事情都已经告诉你了。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020109730.ogg"
    yj "在那之上的事我也想知道。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101500.ogg"
    shy "......"
    me01 "因为是机密所以不能说吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101510.ogg"
    shy "这倒也不是。"
    hide yj_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150101520.ogg"
    shy "因为关于{rb}灵继者{/rb}{rt}elfin{/rt}的事，和研究所本来的研究是放在不同定位上的。"
    play voice "voice/圣护院/150101530.ogg"
    shy "所以没有什么好隐瞒的。"
    play voice "voice/圣护院/150101540.ogg"
    shy "{rb}灵继者{/rb}{rt}elfin{/rt}在记载中是“恶作剧的妖精”的意思。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101550.ogg"
    shy "虽然不知道最开始是谁提起的这个名字。"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/150101560.ogg"
    shy "不过我觉得这样的表达很准确。"
    pause 1.0 hard
    play sound touch
    $ flcam.move(0, 0, 0)
    scene set only shy_cg one
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/150101570.ogg"
    shy "虽然神野君你可能也知道，这个世界上除了你们之外还存在着其他觉醒了{rb}灵纹{/rb}{rt}rune{/rt}的人。"
    play voice "voice/圣护院/150101580.ogg"
    shy "简单来说你们就是超能力者。研究者们把这类人统称为{rb}灵继者{/rb}{rt}elfin{/rt}。"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/150101590.ogg"
    shy "那种力量不仅可以用于生物学的研究上，还能运用在军事和生产业上这一点不难想象的。"
    play voice "voice/圣护院/150101600.ogg"
    shy "但是{rb}灵继者{/rb}{rt}elfin{/rt}这种存在比起一般人来说却是压倒性的少。"
    pause 0.1 hard
    scene set only shy_cg four
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/150101610.ogg"
    shy "所以一部分国家或是民间机构努力想获得更多的{rb}灵继者{/rb}{rt}elfin{/rt}。"
    play voice "voice/圣护院/150101620.ogg"
    shy "没有将{rb}灵继者{/rb}{rt}elfin{/rt}的存在公之于众也并不是为了防止社会混乱，而是方便其中的一部分人独占利益。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only laboratory inside2 xuejian
    show shy_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/圣护院/150101630.ogg"
    shy "差不多就是这样，明白了吗？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020109740.ogg"
    yj "啊咧，这就结束了？"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101640.ogg"
    shy "结束了。"
    hide yj_dzf_b2 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_a1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020109750.ogg"
    yj "姆......"
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/150101650.ogg"
    shy "乖啦乖啦~"
    show yj_dzf_b3 b3 b3_s1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020109760.ogg"
    yj "别摸我的头。"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/150101660.ogg"
    shy "我差不多要回去工作了，今天也是打算早点回去的。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020109770.ogg"
    yj "姐姐，晚饭想吃什么？"
    play voice "voice/圣护院/150101670.ogg"
    shy "什么都行，只要是你做的。"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020109780.ogg"
    yj "我做的饭好吃吗？比起以前拿手了很多哟~"
    show shy_yjf_b1 b1 b1_ga2
    play voice "voice/圣护院/150101680.ogg"
    shy "不是那样的，我的意思是只要是能吃的东西我就没问题。"
    show yj_dzf_b3 b3 b3_a1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020109790.ogg"
    yj "姆......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day211_laboratory_event01:
        $ seen_day211_laboratory_event01 = True
    $ _overworld_label = 'day211.laboratory_event01'
    jump day211.map

label day211.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only bridge evening xuejian
    play music second_103 fadein 3.0 if_changed
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    me01 "最近雪下得越来越频繁了......"
    pause 1.0 hard
    scene set only sky evening xuejian
    with dissolve
    pause 1.0 hard
    "降驻于雪见市的，温柔的雪。"
    "这样的雪，将雪见市变成了常冬的城市。"
    "到了来年——从春天不再到访的时候开始已经是第三年的冬天了。"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 1.0 hard
    "没有人知道，春天什么时候会来临。"
    pause 2.0 hard
    scene set only bridge evening xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    play voice "voice/希菲尔/000100250.ogg"
    stranger "凉君。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg bridge normal
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/000100260.ogg"
    xfe "再一下子，今年也要结束了。"
    pause 0.1 hard
    scene set only xfe_cg bridge daze
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/000100270.ogg"
    xfe "时光的流逝是很快的。"
    play voice "voice/希菲尔/000100280.ogg"
    xfe "如果是快乐的时光的话，就更加如此......"
    pause 0.1 hard
    scene set only xfe_cg bridge normal
    with dissolve
    play voice "voice/希菲尔/000100290.ogg"
    xfe "凉君......怎么样了？"
    play voice "voice/希菲尔/000100300.ogg"
    xfe "回顾今年看看。"
    me01 "这还真是一言难尽啊。"
    me01 "光是熟悉眼前的新环境就让我觉得有些应付不过来了。"
    play voice "voice/希菲尔/000100310.ogg"
    xfe "但是多亏了这样，才和凉君再会了。"
    me01 "我也很高兴能和希菲尔再次见面。"
    play voice "voice/希菲尔/000100320.ogg"
    xfe "凉君，提前祝你新年快乐。"
    pause 0.1 hard
    scene set only xfe_cg bridge happy
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/000100330.ogg"
    xfe "明年也是，请多指教~"
    pause 1.0 hard
    scene white
    with slowerdissolve
    play sound xiaoshi_1
    pause 1.0 hard
    "留下最后一句话，希菲尔的身影消失了。"
    "我的身边此刻就只剩下洁白的结晶缓缓飘落。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge evening xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    me01 "本来还想......再多说说话的。"
    "突然就回去了，都没来得及说出口。"
    "明明......想要道歉的。"
    me01 "下次见面的时候再一起玩吧。"
    me01 "就像以前那样。"
    "也许，和以前稍微有些不同了——"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 0.5 hard
    nvl clear
    nvl_narrator "不只是两个人一起玩耍，而是把希菲尔介绍给大家。"
    nvl_narrator "现在的我已经不是孤单一人了。"
    nvl_narrator "不仅如此。"
    nvl_narrator "连家人也有了。"
    nvl_narrator "我也已经......改变了。"
    nvl_narrator  "对于现在这样的我，希菲尔又是怎么看的呢？"
    nvl clear
    pause 1.0 hard
    scene set only sky evening xuejian2
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    nvl clear
    pcenter "雪花纷然飘落。"
    nvl clear
    pcenter "顺着这条悠长的雪道，绵延向前——"
    nvl clear
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day211_bridge_event01:
        $ seen_day211_bridge_event01 = True
    $ _overworld_label = 'day211.bridge_event01'
    jump day211.map

label day211.kindergarden_event02:
    $ flcam.move(0, 0, 0)
    scene set only school evening outside xuejian
    play music second_118 fadein 3.0 if_changed
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/爱衣/111200550.ogg"
    aiyi "大哥哥~"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/爱衣/111200560.ogg"
    aiyi "嘿嘿~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/千川老师/141200050.ogg"
    qcls "一直以来辛苦你了。"
    me01 "老师也辛苦了。"
    stop music fadeout 5.0
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b1 b1 b1_h4 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/211200100.ogg"
    qb "毕竟凉君男是我们的仆人嘛！"
    play music second_104 fadein 3.0 if_changed
    me01 "看到你我突然觉得一直以来确实挺辛苦的。"
    hide qcls_zf_b1
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound jing01
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211200110.ogg"
    qb "你什么意思啊！"
    me01 "你也想体会当仆人的滋味吗？"
    show qianbo_dzf_b1 b1 b1_h3
    play voice "voice/千波/211200120.ogg"
    qb "凉君男你想将我这样朝气蓬勃的女子当做奴隶对吧？"
    me01 "现在我只看到一颗圆滚滚的橡子而已。"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/小桃/221200050.ogg"
    ycxt "小桃我们已经，成为凉君的奴隶了吗？"
    $ flcam.move(-500, 300, 600, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111200570.ogg"
    aiyi "如果对方是大哥哥的话，无论对爱衣做什么都没关系的哟~"
    pause 0.5 hard
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    hide qianbo_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/千川老师/141200060.ogg"
    qcls "神、神野......君？"
    play sound jing02
    with vpunch
    me01 "{size=72}我什么都没干！{/size}"
    pause 0.5 hard
    hide qcls_zf_b1
    $ flcam.move(-500, 300, 600, duration=1.5)
    show qianbo_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.3
    show ycxt_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/千波/211200130.ogg"
    qb "凭凉君男的本事最多也只能是玩玩的程度而已。"
    me01 "只是玩的话我可以奉陪。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/爱衣/111200580.ogg"
    aiyi "哇！"
    stop music fadeout 5.0
    hide qianbo_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play music second_118 fadein 3.0 if_changed
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111200590.ogg"
    aiyi "那么在大姐姐来之前大家就一起玩吧？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 2.0 hard
    scene set only school evening outside xuejian
    with slowdissolve
    pause 0.5 hard
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031201660.ogg"
    lhx "......"
    me01 "你也在啊立花老师？"
    show lhx_dzf_b2 b2 b2_h3
    play voice "voice/立花希/031201670.ogg"
    lhx "当然了，现在还是工作时间。况且我扮演的是一个认真温柔的老师。"
    me01 "除此之外还要扮演飞机场吧。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031201680.ogg"
    lhx "就算凉君有多喜欢小朋友，也请不要把目标转到我身上来。"
    me01 "你对我好像有很深的误会......"
    show lhx_dzf_b3 b3 b3_s1
    play voice "voice/立花希/031201700.ogg"
    lhx "我一直都对凉君有最正确的认识。"
    me01 "我觉得你的这份自信才是最棘手的。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b3
    show lhx_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031201710.ogg"
    lhx "而且......可能并不是只有我自己这么想。（小声）"
    me01 "你说什么？"
    show lhx_dzf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/立花希/031201720.ogg"
    lhx "没什么！"
    hide lhx_dzf_b1
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031201730.ogg"
    lhx "凉君快进去吧，孩子们还在等你呢。"
    me01 "那么回头见。"
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowdissolve
    pause 1.0 hard
    play sound open_door5
    pause 2.0 hard
    $ flcam.move(-4500, 0, 900)
    scene set only school evening outside xuejian
    show snow_level1 onlayer fg
    show lhx_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031201740.ogg"
    lhx "......"
    play voice "voice/立花希/031201750.ogg"
    lhx "就是因为太了解你的想法，所以才会困扰的。"
    show lhx_dzf_b1 b1 b1_s1
    play voice "voice/立花希/031201760.ogg"
    lhx "这样一来我也只能......被迫接受了不是吗。"
    play voice "voice/立花希/031201770.ogg"
    lhx "本想尽我所能地完成使命。"
    play voice "voice/立花希/031201780.ogg"
    lhx "结局会像日向说的那样吗，有点在意啊......"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ seen_living_room = False
    jump day211.myroom_event01

label day211.myroom_event01:
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    pause 1.0 hard
    scene set only home night my_room xuejian
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
            move _("客厅") jump day211.livingroom_event01
            screen_direction left
            sleep jump day211.sleep

label day211.livingroom_event01:
    if not seen_living_room:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ seen_living_room = True
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        with slowdissolve
        pause 1.0 hard
        play music second_102 fadein 3.0 if_changed
        show wflash onlayer texture
        pause 0.5 hard
        $ flcam.move(0, -300, 900, duration=1.5)
        pause 0.5 hard
        show xz_dsf_b3 b3 b3_s2 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011100030.ogg"
        xz "不会堆积的雪......吗。"
        "翔子胸口的吊坠闪烁着微弱的光芒。"
        "仿佛在预示着什么的到来一般。"
        show xz_dsf_b3 b3 b3_s1
        play voice "voice/翔子/011100090.ogg"
        xz "从早上开始我都在想什么啊......"
        hide xz_dsf_b3
        $ flcam.move(0, 0, 0, duration=1.5)
        pause 0.5 hard
        play sound touch
        "翔子把胸前的吊坠摘了下来。"
        "朝着灯光的方向举起。"
        "吊坠表面反射着光芒。"
        "仿佛夜空中的星辰般闪耀夺目。"
        pause 1.0 hard
        scene set only items necklace
        with slowdissolve
        pause 1.0 hard
        "虽然凉君已经把另一个我——“梦”的事情告诉了自己。"
        "并且还特地让我用“神野君”的称呼来区分彼此。"
        "但尽管如此我还是很在意她们之间究竟发生了什么。"
        "脑海里只有隐约的记忆残片，仿佛是被塞进了许多不属于自己、却又感同身受的梦境一般。"
        "唯一清晰记得的，是和雷亚的约定。"
        "这串项链是她赐予我的第二次生命。"
        "也是目前能够证明她存在的唯一的信物。"
        "虽然只是过去了一年的时间，但是却仿佛要跨越整个次元的距离般漫长。"
        "虽然对凉君的到来感到意外和惊喜，但是同样地也多了一份不知所措。"
        "因为自己的关系才害得雷亚陷入沉睡。"
        "虽然知道不是永久的分别，但却总是忍不住地牵挂。"
        "我们究竟......何时才能重逢呢？"
        stop music fadeout 5.0
        pause 1.0 hard
        scene black
        with slowerdissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        show xz_dsf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        $ flcam.move(0, -400, 600)
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
    else:
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
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
            camera_pos (scale(3097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction right
            move _("卧室") jump day211.myroom_event01

label day211.sleep:
    menu:
        "早点休息":
            if not seen_living_room:
                window mode thought
                me01 "睡觉之前还是先去看看翔子的情况吧。"
                $ flcam.move(0, -100, 400, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            show xz_dsf_b3 b3 b3_h1
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
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump day212
