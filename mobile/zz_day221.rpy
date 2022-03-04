
label day221:
    bookmark
    $ save_name = _("Day 221")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date220 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian3
    play music second_164 fadein 3.0 if_changed
    with slowdissolve
    "天空的颜色有些不一样了。"
    "不只是天空，就连空气也变得格外清新。"
    "这里就是人工岛——库洛诺斯所属的宇宙研究中心。"
    pause 1.0 hard
    scene set only rocket_center day outside klns
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    me01 "终于到了。"
    play voice "voice/植澄友加/021218010.ogg"
    yj "嗯。"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021218020.ogg"
    yj "然、然后该怎么办？"
    me01 "当然是马上开始我们的“约会”啦。"
    show yj_dsf_b2 b2 b2_s3
    play voice "voice/植澄友加/021218130.ogg"
    yj "......"
    stop music fadeout 5.0
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021218140.ogg"
    yj "凉君，我......"
    pause 1.0 hard
    $ set_replay_scene("label10_1")
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian3
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/151201770.ogg"
    stranger "......友加？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only rocket_center day outside klns
    play music second_131 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dsf_b2 b2 b2_s3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021218150.ogg"
    yj "......"
    hide yj_dsf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    me01 "在工作的时候过来打扰真是很抱歉。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151201780.ogg"
    shy "......"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show yj_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151201790.ogg"
    shy "你......"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151201800.ogg"
    shy "还是跟过来了吗？"
    show yj_dsf_b2 b2 b2_s2
    play voice "voice/植澄友加/021218160.ogg"
    yj "......"
    show yj_dsf_b2 b2 b2_s1
    play voice "voice/植澄友加/021218170.ogg"
    yj "姐姐。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151201810.ogg"
    shy "不对......应该不是这样的。"
    "我冲友加点了点头。"
    $ flcam.move(2250, -350, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b2
    show yj_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021218190.ogg"
    yj "是我自己决定追过来的！"
    hide yj_dsf_b3
    show yj_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021218210.ogg"
    yj "我只是想和姐姐见面，想和你说说话才来的。"
    stop music fadeout 5.0
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021218220.ogg"
    yj "姐姐......"
    pause 1.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    play sound touch
    pause 5.0 hard
    $ flcam.move(0, 0, 0)
    play music second_157 fadein 3.0 if_changed
    scene set only yj_cg rocket one
    with slowdissolve
    pause 1.0 hard
    "友加用尽全力扑向了她。"
    "此时的圣护院主任脸上满是无法掩饰的惊讶。"
    play voice "voice/植澄友加/021218230.ogg"
    yj "有个问题我可以问吗？"
    play voice "voice/圣护院/151201850.ogg"
    shy "......是什么？"
    play voice "voice/植澄友加/021218240.ogg"
    yj "姐姐你为什么，会选择走上宇宙研发这条路的呢？"
    pause 0.1 hard
    scene set only yj_cg rocket two
    with dissolve
    play voice "voice/植澄友加/021218250.ogg"
    yj "像这样由我来发问还是第一次呢~"
    play voice "voice/植澄友加/021218260.ogg"
    yj "请告诉我姐姐。"
    play voice "voice/圣护院/151201870.ogg"
    shy "......"
    play voice "voice/圣护院/151201880.ogg"
    shy "以前......也有过两人一起参观火箭发射的场景。"
    pause 0.1 hard
    scene set only yj_cg rocket three
    with dissolve
    play voice "voice/圣护院/151201890.ogg"
    shy "友加你当时一直闹腾个不停。"
    play voice "voice/圣护院/151201900.ogg"
    shy "眼里闪闪发光地望着那飞向远方的火箭。"
    play voice "voice/圣护院/151201910.ogg"
    shy "握着我的手，笑着说“好厉害啊、好厉害啊”。"
    pause 0.1 hard
    scene set only yj_cg rocket two
    with dissolve
    play voice "voice/圣护院/151201920.ogg"
    shy "那对我而言，是最美丽的风景。"
    pause 0.1 hard
    scene set only yj_cg rocket four
    with dissolve
    play voice "voice/植澄友加/021218290.ogg"
    yj "......"
    play voice "voice/植澄友加/021218300.ogg"
    yj "果然姐姐你是为了我才......"
    play voice "voice/植澄友加/021218310.ogg"
    yj "原来姐姐你一直......都还是那个姐姐。"
    play voice "voice/植澄友加/021218320.ogg"
    yj "那......为什么之后就开始不回家了呢？"
    play voice "voice/圣护院/151201940.ogg"
    shy "那是因为你也成为{rb}灵继者{/rb}{rt}elfin{/rt}了。"
    pause 0.1 hard
    scene set only yj_cg rocket five
    with dissolve
    play voice "voice/圣护院/151201950.ogg"
    shy "现在你的{rb}灵纹{/rb}{rt}rune{/rt}也稳定下来了，我也理所当然地失去了关心你的动机。"
    pause 0.1 hard
    scene set only yj_cg rocket three
    with dissolve
    play voice "voice/植澄友加/021218330.ogg"
    yj "......动机？"
    play voice "voice/圣护院/151201960.ogg"
    shy "是的。"
    play voice "voice/植澄友加/021218340.ogg"
    yj "那让我留在雪见市也是？"
    pause 0.1 hard
    scene set only yj_cg rocket two
    with dissolve
    play voice "voice/圣护院/151201970.ogg"
    shy "如此依赖神野君的你，我可不能因为自己的缘故就把你强行拉过来。"
    play voice "voice/圣护院/151201980.ogg"
    shy "更何况我已经没有，再让你继续跟着我的理由了。"
    play voice "voice/植澄友加/021218350.ogg"
    yj "因为我不再是组织所需要的{rb}灵继者{/rb}{rt}elfin{/rt}了？"
    pause 0.1 hard
    scene set only yj_cg rocket three
    with dissolve
    play voice "voice/圣护院/151201990.ogg"
    shy "是的。"
    play voice "voice/植澄友加/021218360.ogg"
    yj "就算是作为能做饭的妹妹而待在一起也不行吗？"
    play voice "voice/圣护院/151202000.ogg"
    shy "那不能成为理由，更不能当成动机。"
    play voice "voice/植澄友加/021218370.ogg"
    yj "......托辞也好、理由也好、借口也罢我都不在乎。"
    pause 0.1 hard
    scene set only yj_cg rocket six
    with dissolve
    play voice "voice/圣护院/151202010.ogg"
    shy "可是我在乎所谓的理由啊。"
    play voice "voice/圣护院/151202020.ogg"
    shy "友加，你一定也有相同的体验吧？"
    play voice "voice/圣护院/151202030.ogg"
    shy "这一点我希望你能理解。"
    play voice "voice/圣护院/151202040.ogg"
    shy "因为我也是一样的。"
    pause 0.1 hard
    scene set only yj_cg rocket seven
    with dissolve
    play voice "voice/植澄友加/021218410.ogg"
    yj "毕竟我们是姐妹嘛。"
    play voice "voice/圣护院/151202050.ogg"
    shy "是啊。"
    play voice "voice/圣护院/151202060.ogg"
    shy "不管发生什么事情。"
    play voice "voice/圣护院/151202070.ogg"
    shy "只有这点......绝对不会改变。"
    pause 0.1 hard
    scene set only yj_cg rocket six
    with dissolve
    play voice "voice/植澄友加/021218430.ogg"
    yj "姐姐你真是个大笨蛋！"
    play voice "voice/圣护院/151202080.ogg"
    shy "被你这么数落也是第一次啊。"
    play voice "voice/植澄友加/021218440.ogg"
    yj "谁让你总是寡言少语、自作主张。"
    play voice "voice/植澄友加/021218450.ogg"
    yj "明明一直为我着想却不告诉我，也不问我的看法。"
    play voice "voice/圣护院/151202090.ogg"
    shy "......这份自觉我还是有的。"
    play voice "voice/植澄友加/021218460.ogg"
    yj "我也是个大笨蛋，从以前开始就一直被蒙在鼓里。"
    pause 0.1 hard
    scene set only yj_cg rocket eight
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/151202100.ogg"
    shy "友、友加？"
    pause 0.1 hard
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/植澄友加/021218480.ogg"
    yj "根本不需要什么动机啊姐姐。"
    play voice "voice/植澄友加/021218490.ogg"
    yj "只要坦诚地告诉我就可以了。"
    play voice "voice/植澄友加/021218500.ogg"
    yj "只要能像现在这样和你说说话就足够了。"
    play voice "voice/植澄友加/021218510.ogg"
    yj "明明......就是这么简单的事情啊。"
    play voice "voice/圣护院/151202120.ogg"
    shy "虽然我知道你想表达什么。"
    play voice "voice/圣护院/151202130.ogg"
    shy "但这对我来说......还是有点难为情。"
    play voice "voice/植澄友加/021218540.ogg"
    yj "那姐姐你现在打算怎么办？"
    play voice "voice/圣护院/151202140.ogg"
    shy "虽然我也不想看到你哭。"
    play voice "voice/圣护院/151202150.ogg"
    shy "但是在神野君面前的话，我......"
    play voice "voice/植澄友加/021218550.ogg"
    yj "大胆地做自己想做的事情啊。真是的，姐姐也是、我也是！"
    play voice "voice/植澄友加/021218560.ogg"
    yj "因为我们从一开始，就一直是很在乎对方的。"
    play voice "voice/圣护院/151202160.ogg"
    shy "......"
    play voice "voice/圣护院/151202170.ogg"
    shy "啊......是啊~"
    pause 0.1 hard
    play sound touch
    scene set only yj_cg rocket nine
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/151202180.ogg"
    shy "就像你说的那样。"
    pause 0.1 hard
    scene set only yj_cg rocket ten
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021218590.ogg"
    yj "一直以来谢谢你了......姐姐。"
    play voice "voice/植澄友加/021218600.ogg"
    yj "你会继续像这样等着我吗？"
    pause 0.1 hard
    scene set only yj_cg rocket four
    with dissolve
    play voice "voice/植澄友加/021218610.ogg"
    yj "虽然现在还做不到，但我一定会追上姐姐你的。"
    play voice "voice/植澄友加/021218620.ogg"
    yj "因为我也想像姐姐一样，在通往宇宙的道路上继续前进。"
    play voice "voice/圣护院/151202200.ogg"
    shy "不是说动机什么的都不重要了吗？"
    play voice "voice/植澄友加/021218630.ogg"
    yj "不是的，我只是单纯地想要那么做。"
    play voice "voice/植澄友加/021218640.ogg"
    yj "就像我当初追随姐姐你去雪见市的时候一样。"
    play voice "voice/圣护院/151202210.ogg"
    shy "......是吗。"
    pause 0.1 hard
    scene set only yj_cg rocket eleven
    with dissolve
    play voice "voice/植澄友加/021218650.ogg"
    yj "更何况，我们是姐妹嘛~"
    play voice "voice/圣护院/151202220.ogg"
    shy "是啊。"
    pause 0.1 hard
    scene set only yj_cg rocket nine
    with dissolve
    play voice "voice/圣护院/151202230.ogg"
    shy "所以，就像学习草船的制作方法时一样。"
    pause 0.1 hard
    scene set only yj_cg rocket ten
    with dissolve
    play voice "voice/植澄友加/021218660.ogg"
    yj "嗯，我也要向姐姐你学习。"
    play voice "voice/圣护院/151202240.ogg"
    shy "相对的我也要更加努力才行。"
    play voice "voice/植澄友加/021218670.ogg"
    yj "今后可要好好吃饭哟。"
    play voice "voice/圣护院/151202250.ogg"
    shy "......这点我会妥善处理的。不对，我会努力妥善处理的。"
    pause 0.1 hard
    scene set only yj_cg rocket nine
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021218680.ogg"
    yj "真是的~"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    "一切都没有任何的改变，今后也不会有所改变。"
    "两姐妹的羁绊永远永远都会延续下去的——"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only rocket_center day outside klns
    $ flcam.move(4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151202260.ogg"
    shy "不过话说回来......你还真是个厉害的男人呢。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151202270.ogg"
    shy "我的妹妹，完全变得坚强起来了。"
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/151202280.ogg"
    shy "因为喜欢上你的缘故。"
    me01 "啊不那个，我们只是......"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show yj_dsf_b2 b2 b2_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021218690.ogg"
    yj "姐、姐姐！"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151202290.ogg"
    shy "怎么......事到如今还会害羞吗？"
    show yj_dsf_b2 b2 b2_s2
    play voice "voice/植澄友加/021218700.ogg"
    yj "因为被姐姐这样说还是第一次嘛~"
    show shy_yjf_b1 b1 b1_ga2
    play voice "voice/圣护院/151202310.ogg"
    shy "脸都红到耳根了啊。"
    show yj_dsf_b2 b2 b2_ga2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021218710.ogg"
    yj "毕竟我可是立刻就会火热起来的女人呢~"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151202320.ogg"
    shy "怎么看都不像嘛。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151202330.ogg"
    shy "神野君......你是怎么想的？"
    me01 "友加她本来就很坚强，满脑子都是身为姐姐的您。"
    me01 "但是她和您一样都不擅长表达自己的想法。"
    me01 "也正因为这一点，才会让人忍不住想要帮助她的吧。"
    $ flcam.move(2250, -350, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b2
    show yj_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021218720.ogg"
    yj "凉君......"
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/151202340.ogg"
    shy "是吗~"
    hide yj_dsf_b3
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151202370.ogg"
    shy "虽然我一直觉得{rb}灵纹{/rb}{rt}rune{/rt}是人类最终进化的可能性。"
    play voice "voice/圣护院/151202380.ogg"
    shy "但也许名为“感情”的力量也是一样的不可或缺。"
    $ flcam.move(4500, -300, 1000, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/151202390.ogg"
    shy "那一定会成为有朝一日，能够开拓宇宙、引领人们朝着未来前进最强大的力量——"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ end_replay()

label day221.rocket_event01:
    $ flcam.move(0, 0, 0)
    scene set only rocket_center day inside klns
    with slowdissolve
    pause 1.0 hard
    me01 "这里就是星天宫宇宙研究中心的基地吗？"
    "眼前一副忙碌的景象着实把我震撼到了。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    play voice "voice/琉璃/041413380.ogg"
    stranger "我听说有客人想要见我于是就过来看看。"
    play music second_151 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_yzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041413390.ogg"
    liuli "骗人......"
    hide liuli_yzf_b1
    show liuli_yzf_b3 b3 b3_c1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041413400.ogg"
    liuli "前辈。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide liuli_yzf_b3 with None
    pause 0.1 hard
    show liuli_yzf_b2 b2 b2_c1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041413410.ogg"
    liuli "神野......前辈！"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg rocket two
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041413420.ogg"
    liuli "前辈、神野前辈！"
    play voice "voice/琉璃/041413430.ogg"
    liuli "为什么你会在这里？"
    me01 "因为一些原因就来看看，没能提前告诉你真是抱歉。"
    play voice "voice/琉璃/041413440.ogg"
    liuli "不会的......能够见到前辈我已经很满足了。"
    play voice "voice/琉璃/041413450.ogg"
    liuli "我一直以为......再见面应该会是很久很久以后的事情了。"
    me01 "学校那边我已经拜托翔子帮我请了假。"
    me01 "至于{rb}灵继者{/rb}{rt}elfin{/rt}的调查工作我也拜托了立花老师和水之濑同学。"
    me01 "托大家的福我也终于能够够追上琉璃你了。"
    me01 "今后也多多关照。"
    pause 0.1 hard
    scene set only liuli_cg rocket four
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041413530.ogg"
    liuli "小女子不才，今后也请多多指教~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day221.rocket_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian3
    play music second_114 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "虽说是得到了圣护院主任的许可留在了宇宙研究中心。"
    "但是我所能做的也就是陪在琉璃身边看着她接受各种严格的专业训练。"
    "就在吃完午饭不久后，正式的训练马上就开始了。"
    "不过话虽如此，下午的内容基本上都是讲习。"
    pause 1.0 hard
    scene set only rocket_center day inside klns
    $ flcam.move(4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151406070.ogg"
    shy "来了啊，还挺准时的。"
    me01 "训练的内容也是由圣护院小姐亲自负责吗？"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151406080.ogg"
    shy "基本上是吧。不过虽然暂时是这样安排的，但也并非一直都是如此。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dsf_b3 b3 b3_h1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/041415190.ogg"
    liuli "训练内容的安排我也已经拿到手了，像早上那样的自由项目比较多。"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151406090.ogg"
    shy "时间宝贵，你们赶紧就座吧。"
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only rocket_center classes one
    play music second_115 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/圣护院/151406100.ogg"
    shy "神野君还是第一次听这个内容吧，我就从最基本的开始。首先是这个计划的概要。"
    play voice "voice/圣护院/151406110.ogg"
    shy "花山院就当是复习来听吧。"
    pause 0.1 hard
    scene set only rocket_center classes two
    with dissolve
    play voice "voice/圣护院/151406120.ogg"
    shy "这个计划的目的是完成载人火星探测，包含从火星的气候和科学观测得到样本，并对其进行采集等等。"
    me01 "探测火星，有什么意义吗？"
    play voice "voice/圣护院/151406130.ogg"
    shy "当然了，比如说可能会证明火星上有水之类的。"
    me01 "证明之后要做什么？"
    play voice "voice/圣护院/151406140.ogg"
    shy "那么也就说明了微生物存在的可能性极高。"
    me01 "然后呢？"
    play voice "voice/圣护院/151406150.ogg"
    shy "火星上是否有生命这样的疑问就能够得到解决了。"
    play voice "voice/圣护院/151406160.ogg"
    shy "过去，其他国家也成功将无人探测器送上火星。"
    play voice "voice/圣护院/151406170.ogg"
    shy "那时虽然确认了地表有类似河川的结构，但别说是液态水，就连冰都没有发现。"
    play voice "voice/圣护院/151406180.ogg"
    shy "所以我们不光是要收集行星表面的物质，更是提出了开采地下物质的挑战。"
    play voice "voice/圣护院/151406190.ogg"
    shy "我们希望通过花山院的力量来完成。"
    play voice "voice/琉璃/041415200.ogg"
    liuli "真、真是责任重大......"
    play voice "voice/圣护院/151406200.ogg"
    shy "为了不重蹈覆辙，所以这一次是由星天宫总本社研究机构主导项目。"
    me01 "之前不是由他们主导的吗？"
    play voice "voice/圣护院/151406210.ogg"
    shy "是啊，之前是和欧洲联邦一起进行的，因为也有这一些与星天宫关系密切的机构。"
    play voice "voice/琉璃/041415210.ogg"
    liuli "欧盟宇宙研究机构——ESA之中，也有以北欧诸国为中心的研究小组。"
    me01 "可是电视上说的是小行星探测......"
    pause 0.1 hard
    scene set only rocket_center classes one
    with dissolve
    play voice "voice/圣护院/151406220.ogg"
    shy "虽说是这样，但把它理解成此次计划的“热身”也不足为奇了。"
    play voice "voice/圣护院/151406320.ogg"
    shy "如果成功的话，说不定就能揭开外星生命的谜团了。"
    pause 0.1 hard
    scene set only rocket_center classes two
    with dissolve
    play voice "voice/圣护院/151406330.ogg"
    shy "这不光是对人类，对{rb}灵继者{/rb}{rt}elfin{/rt}来说也具有重要的意义的。"
    stop music fadeout 5.0
    ".........."
    "......"
    "..."
    pause 1.0 hard
    scene set only rocket_center classes three
    with dissolve
    play music second_104 fadein 3.0 if_changed
    "讲习大概过了两个小时左右，期间圣护院小姐完全没有停下来的意思。"
    "糟糕，好想睡......"
    "早上陪友加折腾了一番，现在的睡意完全挡不住啊。"
    pause 0.1 hard
    scene set only rocket_center classes four
    with dissolve
    play voice "voice/圣护院/151406340.ogg"
    shy "神野君，你在认真听吗？"
    me01 "......在听着呢。"
    play voice "voice/圣护院/151406350.ogg"
    shy "注意力不够集中啊，你这样的状态要是去参加任务的话可是会很麻烦的。"
    play voice "voice/圣护院/151406360.ogg"
    shy "宇航员自然不用说，对其他工作人员来说集中注意力也是很重要的。"
    play voice "voice/圣护院/151406380.ogg"
    shy "对于宇宙航行任务更是如此，你要是明白的话就好好地振作起来。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian3
    with slowdissolve
    pause 1.0 hard
    "好不容易熬过了讲习课程，紧接着的迎接我们的是实战训练。"
    "本来被睡意困扰的我，刚走进训练室那股睡意就被冲散了。"
    pause 1.0 hard
    scene set only rocket_center train one
    play music second_106 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041415250.ogg"
    liuli "眼、眼睛在不停地旋转！"
    "琉璃被安排坐在了离心机上。"
    "就以那样的姿势，开始咕噜咕噜地旋转。"
    "这样的训练是为了保持宇航员的身体平衡。"
    me01 "这是为了能够锻炼耐力和适应性的训练吗？"
    play voice "voice/圣护院/151406500.ogg"
    shy "不仅如此，还必须一边应对不断增加的重力，一边完成规定好的动作。"
    play voice "voice/圣护院/151406510.ogg"
    shy "因为宇航员很多时候要忍受数倍于地球重力进行作业。"
    pause 0.1 hard
    scene set only rocket_center train two
    with dissolve
    play voice "voice/圣护院/151406520.ogg"
    shy "所以花山院，赶快按照顺序按下座位上的按钮。"
    pause 0.1 hard
    scene set only rocket_center train three
    with dissolve
    play voice "voice/琉璃/041415260.ogg"
    liuli "好、好的......"
    "琉璃抬起手，努力地想要按下座位上的按钮，但是因为离心力的关系似乎不是很顺利的样子。"
    pause 0.1 hard
    scene set only rocket_center train four
    with dissolve
    play voice "voice/圣护院/151406530.ogg"
    shy "......看来还需要加强肌肉训练。"
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 1.0 hard
    "于是在健身室内，以肌肉训练为主的新一轮训练又开始了。"
    pause 1.0 hard
    scene set only rocket_center train five
    with dissolve
    show wflash onlayer texture
    with vpunch
    play voice "voice/琉璃/041415270.ogg"
    liuli "坚、坚持不住了......"
    "在一旁的我，也试着举了下相同的杠铃。"
    "与琉璃不同的是，我还算比较轻松就举了起来。"
    pause 0.1 hard
    play sound yangmu
    scene set only rocket_center train six
    with dissolve
    play voice "voice/琉璃/041415280.ogg"
    liuli "哇......前辈很轻松就举起来了，果然很厉害。"
    play voice "voice/圣护院/151406540.ogg"
    shy "在适应性测试的时候就察觉了，神野君你除了注意力以外其他方面都很优秀啊。"
    play voice "voice/琉璃/041415290.ogg"
    liuli "前辈第一次做离心机的时候，也是很轻松就成功了。相反我就被转晕了好几次。"
    play voice "voice/圣护院/151406570.ogg"
    shy "那么花山院，你也赶快把杠铃举起来！"
    pause 0.1 hard
    scene set only rocket_center train seven
    with dissolve
    show wflash onlayer texture
    with vpunch
    play voice "voice/琉璃/041415300.ogg"
    liuli "从刚才开始我就一直在尝试了，但还是举不起来！"
    play voice "voice/圣护院/151406580.ogg"
    shy "用毅力给我举起来。"
    play voice "voice/琉璃/041415310.ogg"
    liuli "干劲也好毅力也好都举不起来......"
    pause 0.1 hard
    play sound rune2
    show wflash onlayer texture
    scene set only rocket_center train eight
    with dissolve
    play voice "voice/琉璃/041415320.ogg"
    liuli "这样的话......不行吗？"
    play voice "voice/圣护院/151406590.ogg"
    shy "不行。"
    me01 "{rb}灵纹{/rb}{rt}rune{/rt}的使用是禁止的吗？"
    pause 0.1 hard
    scene set only rocket_center train nine
    with dissolve
    play voice "voice/圣护院/151406600.ogg"
    shy "都说了是肌肉训练吧，虽说是{rb}灵继者{/rb}{rt}elfin{/rt}，但也不能放松基础的体能训练。"
    play voice "voice/圣护院/151406610.ogg"
    shy "一味地依赖{rb}灵纹{/rb}{rt}rune{/rt}的话，长时间的任务就会很麻烦了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only rocket_center train ten
    play music second_140 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "宇宙飞行的模拟近乎完美。"
    "因为是假想的飞行过程，所以在这里{rb}灵纹{/rb}{rt}rune{/rt}的使用被允许了。"
    "和肌肉训练不同，需要用到许多讲习时学到的知识。"
    "之后就是琉璃一个人的舞台了。"
    "坐在驾驶舱里的她，在一大堆的计算机面前忙碌着。"
    "凭借{rb}思维透视{/rb}{rt}telepathy{/rt}和{rb}接触感应{/rb}{rt}psychometry{/rt}，琉璃能够快速地检查所有的仪器的工作状况。"
    "即使在真空环境中，也能够使用{rb}念动力场{/rb}{rt}psychokinesis{/rt}顺利行动。"
    "所以说，唯一的挑战就是体力了，毕竟无论是谁也无法长时间地使用{rb}灵纹{/rb}{rt}rune{/rt}。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day221.rocket_event03:
    $ flcam.move(0, 0, 0)
    scene set only rocket_center night outside klns
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/神野大和/171400010.ogg"
    dh "嚯......凉吗？"
    "在和琉璃回宿舍的途中，我遇到了许久未见的那个身影。"
    play music second_104 fadein 3.0 if_changed
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171400020.ogg"
    dh "为什么你会在这里？"
    me01 "这是我的台词吧。"
    me01 "突然叫住我们就只是为了说这个吗？"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/171400030.ogg"
    dh "我只是稍微问候一下而已。"
    me01 "一如既往地招人厌。"
    show dh_zf_b1 b1 b1_a1
    play voice "voice/神野大和/171400040.ogg"
    dh "关于雪见市的异常气候，和你期望的一样我也正在密切关注着。"
    me01 "谁也没有对你抱有期望吧。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171400050.ogg"
    dh "这种恶心的社交辞令就免了吧。"
    "这家伙......"
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    show liuli_dsf_b2 b2 b2_s3
    play voice "voice/琉璃/041414070.ogg"
    liuli "我从藤原瞳同学那里也听说了，在神社发生的那些事件，还是偶尔会再发生的。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show dh_zf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/神野大和/171400060.ogg"
    dh "其实当初组织也考虑过要派人过去的。"
    me01 "派人？"
    hide liuli_dsf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171400080.ogg"
    dh "毕竟星天宫现在似乎正在以那座城市为舞台，策划着什么事情的样子。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171400090.ogg"
    dh "虽然并不清楚这和行星探测是否有关。"
    me01 "你到底想说什么？"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/171400100.ogg"
    dh "就当是我的胡说八道就好。"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/171400170.ogg"
    dh "你能够站在这里，虽然也有植澄主任的帮助，但更多的是因为我的推荐。"
    me01 "那我还真得谢谢你啊。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/171400180.ogg"
    dh "叫我爸比也没问题的哟~"
    me01 "去死好了。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171400200.ogg"
    dh "所以你旁边这个女孩是谁？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b3 b3 b3_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041414080.ogg"
    liuli "我是这次的集训生花山院琉璃，请多指教~"
    show dh_zf_b1 b1 b1_sp1
    play voice "voice/神野大和/171400210.ogg"
    dh "啊~你就是这次的宇航员。"
    me01 "你不是说自己是负责人之一吗，怎么连这个都不知道？"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171400220.ogg"
    dh "这也是我们第一次见面，我所属的部门和宇航员没有直接关联。"
    me01 "你这也太散漫了吧......"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171400260.ogg"
    dh "花山院君，在这里相遇也是一种缘分，我可以问一个问题吗？"
    show liuli_dsf_b3 b3 b3_n1
    play voice "voice/琉璃/041414100.ogg"
    liuli "好的，是什么问题呢？"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171400270.ogg"
    dh "告诉我你的胸围是多少！"
    show liuli_dsf_b3 b3 b3_ga3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041414110.ogg"
    liuli "......哈？"
    show dh_zf_b1 b1 b1_n3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/神野大和/171400280.ogg"
    dh "让本大爷见识一下你的胸部吧！"
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show liuli_dsf_b3 b3 b3_ga1 at flu_down(0.15, 20, 2):
        xpos 0.5
    play voice "voice/琉璃/041414120.ogg"
    liuli "{size=72}呀啊！！{/size}"
    hide liuli_dsf_b3
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    me01 "你这个性骚扰大叔，小心我用{rb}灵纹{/rb}{rt}rune{/rt}把你扔出去。"
    show dh_zf_b1 b1 b1_s2
    play voice "voice/神野大和/171400290.ogg"
    dh "我只是想知道她的身高而已。"
    me01 "我刚刚明明听到了胸部之类的。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171400300.ogg"
    dh "这是研究者的本能。"
    me01 "给我向所有的研究者们道歉！"
    show dh_zf_b1 b1 b1_ga2
    play voice "voice/神野大和/171400310.ogg"
    dh "在宇航员的适应性要求上，身体的尺寸是相当重要的。"
    me01 "别胡说八道了，接受检查的时候我也没听说过。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171400320.ogg"
    dh "你说到底也只是后援的吧，和她不同所以不需要实际乘坐探测器。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/171400340.ogg"
    dh "比如说宇航员的体重增加一千克，那么许多轻量化的作业就会变得更加严格。燃料的负担也会滚雪球式地增加。"
    show dh_zf_b1 b1 b1_ga2
    play voice "voice/神野大和/171400350.ogg"
    dh "体格小的话，作为宇航员来说是有好处的。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/171400360.ogg"
    dh "也就是说，用我的肉眼亲自确认她的胸部是属于正常的工作范畴！"
    me01 "再胡说八道的话小心我报警了。"
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041414130.ogg"
    liuli "受益匪浅啊，原来对宇航员来说胸部大小也是非常重要的！"
    me01 "那个......琉璃你不用听他胡扯也没关系的。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show dh_zf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/神野大和/171400370.ogg"
    dh "不过说白了这些也都是技术班的事情，与我无关。"
    me01 "果然只是单纯的性骚扰吗！"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/171400380.ogg"
    dh "不过看样子她胸部的尺寸刚刚好。"
    me01 "行了你快滚吧！"
    hide liuli_dsf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_a2
    play voice "voice/神野大和/171400390.ogg"
    dh "花山院本人都没说什么，你为什么那么激动？"
    me01 "琉璃是我的朋友，我不允许你这样欺负她。"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/171400400.ogg"
    dh "嚯~朋友吗。"
    "也许在他的眼中我一直都是一个人。"
    "也难怪他会如此惊讶。"
    show dh_zf_b1 b1 b1_ga2
    play voice "voice/神野大和/171400420.ogg"
    dh "小心点啊，如果因为你的关系让她的胸成长的话，你会被技术班的那群人追杀的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day221.rocket_event04:
    $ flcam.move(0, 0, 0)
    scene set only rocket_center room1
    play music second_111 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041414200.ogg"
    liuli "前辈，请用~"
    hide liuli_dsf_b1
    $ flcam.move(0, -100, 400, duration=1.5, warper='ease_cubic')
    pause 1.0 hard
    show bottle onlayer b2_c2u:
        xpos 0.0
    "回到房间里，琉璃就拿出了饮料招待我。"
    hide bottle
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_n4 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041414210.ogg"
    liuli "一直以来我都是一个人住在这里，现在和前辈面对面坐着总觉得有点奇怪。"
    me01 "这座宿舍楼里，还住着其他人吗？"
    show liuli_dsf_b3 b3 b3_n1
    play voice "voice/琉璃/041414220.ogg"
    liuli "是的，项目的其他工作人员们也都住在这里。"
    me01 "原来如此。"
    pause 0.5 hard
    hide liuli_dsf_b3
    $ flcam.move(0, -100, 400, duration=1.5)
    play ambience1 phone1 fadein 3.0
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041414800.ogg"
    liuli "前、前辈，有电话。"
    me01 "究竟是谁这么不识趣......"
    stop music fadeout 5.0
    stop ambience1 fadeout 1.0
    hide liuli_dsf_b1
    pause 2.0 hard
    $ flcam.move(3800, -400, 800, duration=1.5)
    pause 1.0 hard
    play music second_108 fadein 3.0 if_changed
    investigation call block tyt_wnf_b1 b1 b1_h1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    nvl clear
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131402160.ogg"
    c.tyt_wnf_b1 "你好，我就是那个不识趣的女人~"
    c.me01 "你怎么会知道我的号码？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131402170.ogg"
    c.tyt_wnf_b1 "是立花小姐告诉我的。"
    c.me01 "你们的关系什么时候变得这么要好了？"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131402180.ogg"
    c.tyt_wnf_b1 "因为工作关系~"
    c.me01 "是之前在神社的时候？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131402190.ogg"
    c.tyt_wnf_b1 "有点不一样，准确来说是组织的工作。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131402200.ogg"
    c.tyt_wnf_b1 "星天宫的高层传来指示，要我们协助守护这座城市。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131402230.ogg"
    c.tyt_wnf_b1 "正因如此，虽说是很让人困扰的请求，但前辈不在时的人员空缺就交给我好了~"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131402240.ogg"
    c.tyt_wnf_b1 "灵纹什么的我虽然不太懂，但是我的灵能力还是可以的。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131402250.ogg"
    c.tyt_wnf_b1 "更重要的是，伏笔的交代也算是告一段落了。"
    c.me01 "你这家伙不会是剧情遗留下来的bug吧......"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131402260.ogg"
    c.tyt_wnf_b1 "真是肤浅呢......嗯，好肤浅。"
    c.me01 "整个角色都崩坏了啊你。"
    play voice "voice/藤原瞳/131402270.ogg"
    c.tyt_wnf_b1 "立花小姐就在我旁边，现在我就把电话交给她。"
    hide tyt_wnf_b1
    investigation call block lhx_dsf_b2 b2 b2_n1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/031402310.ogg"
    c.lhx_dsf_b2 "所以电话这头现在换成我了~"
    show lhx_dsf_b2 b2 b2_h2
    play voice "voice/立花希/031402320.ogg"
    c.lhx_dsf_b2 "至此，近况报告完毕。"
    c.me01 "以后汇报这种任务请自己好好完成啊。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031402330.ogg"
    c.lhx_dsf_b2 "看来研究所那边也向星天宫本部求援了，感觉是把这里的工作全部丢给了别人的样子。"
    c.me01 "所以你才会和藤原瞳一起行动吗？"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031402350.ogg"
    c.lhx_dsf_b2 "我也不是很清楚，藤原同学说她也还有很多不知道的东西。"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/031402360.ogg"
    c.lhx_dsf_b2 "虽然星天宫这个机构很可疑，但是实力确实还不赖。"
    play voice "voice/立花希/031402370.ogg"
    c.lhx_dsf_b2 "刚才也和我一起阻止了灵继者的暴走。"
    c.me01 "总之有你在我就放心了。"
    show lhx_dsf_b2 b2 b2_sp1
    play voice "voice/立花希/031402390.ogg"
    c.lhx_dsf_b2 "你那边怎么样了？八成是在跟璃之助卿卿我我吧？"
    c.me01 "你这脑子装的都是什么啊......"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031402400.ogg"
    c.lhx_dsf_b2 "想到之后的日子，一定爽得偷笑着了吧。"
    c.me01 "别开玩叫了。（咬舌）"
    c.me01 "不管怎么说我多少还是会想念你们大家的。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031402410.ogg"
    c.lhx_dsf_b2 "你是指青木同学还有爱衣吧？"
    c.me01 "不只是她们，立花老师你也是一样的。"
    stop music fadeout 5.0
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031402420.ogg"
    c.lhx_dsf_b2 "......"
    c.me01 "是被我感动到说不出话来了吗？"
    show lhx_dsf_b2 b2 b2_a1
    play voice "voice/立花希/031402430.ogg"
    c.lhx_dsf_b2 "不对，这是花心！"
    play music second_104 fadein 3.0 if_changed
    c.me01 "你说啥？"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031402440.ogg"
    c.lhx_dsf_b2 "毕竟凉君你一直是把我当成备胎来看待的。"
    c.me01 "所以说不要随便脑补一些奇怪的剧情啊！"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031402450.ogg"
    c.lhx_dsf_b2 "到底怎么回事呢，凉君竟然和我建立起了这样龌龊的关系。"
    show lhx_dsf_b2 b2 b2_h3
    play voice "voice/立花希/031402460.ogg"
    c.lhx_dsf_b2 "还请不要对我做下流的事情......"
    c.me01 "你放心好了，我是不会做的。"
    show lhx_dsf_b2 b2 b2_a1
    play voice "voice/立花希/031402470.ogg"
    c.lhx_dsf_b2 "为什么不做啊！"
    c.me01 "完全不知道你为什么生气。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031402480.ogg"
    c.lhx_dsf_b2 "凉君什么的变成花花公子就好了~"
    show lhx_dsf_b2 b2 b2_h1
    play voice "voice/立花希/031402490.ogg"
    c.lhx_dsf_b2 "晚上打太长时间的电话不太好，那先就这样吧。"
    investigation call end
    play sound phone2
    pause 0.5 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041414830.ogg"
    liuli "打电话来的是藤原同学和立花小姐对吧？"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041414850.ogg"
    liuli "虽然只听到了“花心”、“备胎”和“龌龊的关系”这些内容而已......"
    "竟然只听到了最危险的东西？！"
    show liuli_dsf_b2 b2 b2_ga4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041414860.ogg"
    liuli "前、前辈和立花小姐原来......是这种关系吗？"
    me01 "不是的，你误会了。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041414870.ogg"
    liuli "是那样龌龊的关系吗。"
    me01 "都说是误会了啦！"
    show liuli_dsf_b3 b3 b3_n4
    play voice "voice/琉璃/041414890.ogg"
    liuli "果然还是由我来当备胎才是合理的。"
    me01 "所以说听我解释啊！" with vpunch
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day222
