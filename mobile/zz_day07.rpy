label day07:
    bookmark
    $ save_name = _("Day 07")
    pause 4.0 hard
    scene set only backend_yinghua summer
    with dissolve
    show backend_bg02 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date06 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    $ suppress_overlay = False
    scene set only sky day yinghua2
    with dissolve
    pause 2.0 hard
    "随着大暑节气的到来，气温也越发地炎热了。"
    pause 1.0 hard
    scene set only beach day yinghua
    with dissolve
    pause 2.0 hard
    show rxl_sz_b1 b1 b1_h1 onlayer screens at side_left('rx_lian'), basicfade
    play voice "voice/日向怜/0114110.ogg"
    rxl "小凉，久等了~"
    hide rxl_sz_b1
    play music first_10 fadein 3.0 if_changed
    $ flcam.move(-7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_sz_b2 b2 b2_h3 onlayer m2 at walkin_l(0.2)
    pause 0.5 hard
    play voice "voice/日向怜/0114120.ogg"
    rxl "抱歉了，让你一个人帮忙看行李。"
    me01 "这种事情本来就是交给男生做的，不必在意。"
    hide rxl_sz_b2
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    "放眼望去，海滩上到处都是前来游玩的客人。"
    "旅店的天台上，万夜花小姐以及各位长辈们正一边聊天一边品尝着手中的美酒。"
    $ flcam.move(-7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_sz_b2 b2 b2_s2 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114130.ogg"
    rxl "父亲他们说今天不游泳了。都不知道他们到底来干什么了。"
    me01 "毕竟大人之间有很多话要说吧，海水浴只是聚会见面的托词罢了。"
    show rxl_sz_b2 b2 b2_ga1
    play voice "voice/日向怜/0114140.ogg"
    rxl "真是这样的话，这片蔚蓝的大海可就要哭泣了~"
    "樱华镇所靠的海岸绵延数百公里，一直延伸到岛屿另一头的{encyclopedia=xuejian}雪见市{/encyclopedia}。"
    me01 "其他人呢？"
    hide rxl_sz_b2
    show rxl_sz_b1 b1 b1_n3 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114150.ogg"
    rxl "小铃她们还在换衣服。学生会的前辈们、一诚君，还有小苍衣她们应该马上就到了吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 2.0 hard
    "没想到能够邀请到这么多的人，青木家母真是不可小瞧啊，虽然平时看起来冒冒失失的。"
    "我环顾了四周，并没有发现雷亚的身影。"
    "现在离天黑还有很长的时间。"
    "况且以那家伙怕生的性格来看，即使来了也不会那么轻易被我找到吧。"
    "虽说有把集合地点告诉她，可毕竟对方只是说了考虑一下。"
    "话说回来，还真一次也没有在白天见过那家伙。"
    "该说不愧是死神吗......"
    pause 1.0 hard
    $ flcam.move(0, -350, 750)
    scene set only beach day yinghua
    with dissolve
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_n1 onlayer m2 at walkin_l(0.4)
    show xz_sz_b1 b1 b1_s1 onlayer m2 at walkin_r(0.6)
    pause 0.5 hard
    play voice "voice/青木铃音/0504720.ogg"
    lingyin "大家，久等了~"
    play voice "voice/翔子/0203710.ogg"
    xz "今天也很热呢......真想一整天都待在有空调的屋子里。"
    pause 0.5 hard
    show rxl_sz_b2 b2 b2_h3 onlayer m2:
        xpos 0.2
    $ flcam.move(-2250, -200, 600, duration=1.5)
    pause 0.5 hard
    "被众人五彩缤纷的泳装包围着的我，顿时失去了思考能力。"
    show rxl_sz_b2 b2 b2_a1
    play voice "voice/日向怜/0114220.ogg"
    rxl "小凉，鼻血。"
    hide rxl_sz_b2
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_h3
    play voice "voice/青木铃音/0504730.ogg"
    lingyin "能在这么近的距离看到姐姐的泳装，真是荣幸之至~"
    show xz_sz_b1 b1 b1_sp2
    play voice "voice/翔子/0203720.ogg"
    xz "就算是开玩笑也不要说这种容易让人误会的话啊！" 
    hide lingyin_sz_b2
    hide xz_sz_b1
    $ flcam.move(-7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_sz_b2 b2 b2_s1 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114230.ogg"
    rxl "......虽然知道输了，但还是好不甘心。"
    "拜托你不要再托着胸了。"
    hide rxl_sz_b2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "无视了日向怜的抱怨，一旁的翔子在我身旁的阴凉处坐了下来。"
    me01 "很怕热吗？"
    show xz_sz_b3 b3 b3_n2 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0203740.ogg"
    xz "我讨厌太热或者太冷的环境，所以快点帮我拿点饮料过来吧。"
    hide xz_sz_b3
    "真是个任性的小公主啊。"
    show lingyin_sz_b1 b1 b1_h1 onlayer screens at side_left('lingyin', 0.05), basicfade
    play voice "voice/青木铃音/0504740.ogg"
    lingyin "姐姐，你这个姿势看起来就像是想让神野同学帮你涂防晒霜哟~"
    hide lingyin_sz_b1
    show rxl_sz_b1 b1 b1_a1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/0114240.ogg"
    rxl "小凉，可不能做那种不知廉耻的事情啦！"
    hide rxl_sz_b1
    show xz_sz_b1 b1 b1_a1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0203750.ogg"
    xz "就算日向同学你不说，我也不会让他涂的。"
    hide rxl_sz_b1
    hide xz_sz_b1
    me01 "我也不想涂啊。"
    show xz_sz_b3 b3 b3_a1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0203760.ogg"
    xz "为什么啊笨蛋凉！"
    hide xz_sz_b3
    me01 "不知道你在生什么气。"
    show xz_sz_b3 b3 b3_s1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0203770.ogg"
    xz "哼！"
    hide xz_sz_b3
    show lingyin_sz_b2 b2 b2_n1 onlayer screens at side_left('lingyin'), basicfade
    play voice "voice/青木铃音/0504750.ogg"
    lingyin "这应该就是所谓女人的自尊心吧？"
    hide lingyin_sz_b2
    show xz_sz_b1 b1 b1_a1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0203780.ogg"
    xz "不要详细说明了，小心我修理你哦。"
    hide xz_sz_b1
    show lingyin_sz_b2 b2 b2_h3 onlayer screens at side_left('lingyin'), basicfade
    play voice "voice/青木铃音/0504760.ogg"
    lingyin "是，好兴奋~"
    hide lingyin_sz_b2
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_n1 onlayer m2 at walkin_r(0.8)
    pause 0.5 hard
    play voice "voice/一诚总司/1601820.ogg"
    yczs "哦，大家都到了啊，很热闹嘛。"
    hide yczs_sz_b1
    $ flcam.move(-7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_sz_b1 b1 b1_h1 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114360.ogg"
    rxl "那么那么，天协的海水浴现在开~始~"
    pause 0.5 hard
    show rxl_sz_b1 b1 b1_h1 onlayer m2 at walkout_r(0.2)
    pause 1.5 hard
    hide rxl_sz_b1
    "伴随着激昂的宣言，日向怜第一个冲向了大海。"
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b1 b1 b1_n2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0203860.ogg"
    xz "话说我可不是天协的部员。"
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.8
    $ flcam.move(5000, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1601830.ogg"
    yczs "我也不是。"
    hide yczs_sz_b1
    hide xz_sz_b1
    $ flcam.move(-7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114370.ogg"
    rxl "喂，为什么没人跟过来啊？！"
    me01 "下水前还是做一下准备运动比较好。"
    hide rxl_sz_b2
    show rxl_sz_b1 b1 b1_ga1 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114380.ogg"
    rxl "诶......"
    me01 "这是基本常识吧。"
    hide rxl_sz_b1
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0203870.ogg"
    xz "真是小孩子呢，真是的。"
    pause 0.5 hard
    show lingyin_sz_b1 b1 b1_n1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504820.ogg"
    lingyin "我们要做什么呢？"
    hide xz_sz_b1
    hide lingyin_sz_b1
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_h1 onlayer m2:
        xpos 0.8
    play voice "voice/一诚总司/1601840.ogg"
    yczs "去搭讪吗？"
    me01 "请恕我拒绝。"
    show yczs_sz_b1 b1 b1_n1
    play voice "voice/一诚总司/1601850.ogg"
    yczs "泡妞呢？"
    me01 "这两者没区别吧。"
    hide yczs_sz_b1
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    show xz_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.6
    show lingyin_sz_b2 b2 b2_n1 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0504830.ogg"
    lingyin "我带了沙滩排球过来哟~"
    show xz_sz_b1 b1 b1_sp1
    play voice "voice/翔子/0203880.ogg"
    xz "那不是用来代替枕头用的吗？"
    show lingyin_sz_b2 b2 b2_h1
    play voice "voice/青木铃音/0504840.ogg"
    lingyin "虽然是这样，但机会难得嘛。"
    show xz_sz_b1 b1 b1_s2
    play voice "voice/翔子/0203890.ogg"
    xz "我就在一旁喝果汁就好。"
    me01 "会这么说莫非翔子你并不擅长运动吗？"
    hide xz_sz_b1
    show xz_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0203900.ogg"
    xz "......真是失礼啊，别看我这样，我可是文武双全的。"
    show lingyin_sz_b2 b2 b2_n1
    play voice "voice/青木铃音/0504850.ogg"
    lingyin "要是全部人都到海里去的话，小苍衣她们来了的话就没有人接应了呢，不如大家一起来玩沙滩排球吧？"
    me01 "正好也能顺便作为入水前的准备运动，我赞成。"
    show xz_sz_b2 b2 b2_s1
    play voice "voice/翔子/0203910.ogg"
    xz "真是不太想暴露在烈日下呢。"
    show lingyin_sz_b2 b2 b2_h1
    play voice "voice/青木铃音/0504860.ogg"
    lingyin "排球的赛制采用对战的形式吧。这样一来大家就都会有动力了。"
    hide lingyin_sz_b2
    hide xz_sz_b2
    $ flcam.move(8100, -500, 900, duration=1.5)
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_n1 onlayer m2:
        xpos 0.85
    me01 "一诚同学，玩吗？"
    show yczs_sz_b1 b1 b1_h1
    play voice "voice/一诚总司/1601860.ogg"
    yczs "本来想去做些观察的，真拿你们没办法啊~"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 2.0 hard
    play music first_04 fadein 3.0 if_changed
    scene set only beach day beachball1
    with dissolve
    pause 2.0 hard
    play voice "voice/青木铃音/0504870.ogg"
    lingyin "因为正好有四个人，采用分组的方式比较好。"
    me01 "那谁和谁一组呢？"
    play voice "voice/翔子/0203920.ogg"
    xz "就这个组合不就行了？"
    play voice "voice/一诚总司/1601870.ogg"
    yczs "这样一来，我们这边不是比较有利吗？"
    me01 "考虑到男女体力差异的话的确是这样没错。"
    play voice "voice/翔子/0203930.ogg"
    xz "虽然神野君的实力如何我不太清楚，但是一诚君的运动能力只算一般，没有问题的。"
    play voice "voice/一诚总司/1601880.ogg"
    yczs "你竟然对我这么了解吗，明明只算是认识而已吧。"
    play voice "voice/翔子/0203940.ogg"
    xz "谁让我是学生会成员呢。"
    play voice "voice/一诚总司/1601890.ogg"
    yczs "那我能称呼你“小翔”吗？"
    scene set only beach day beachball2
    play voice "voice/翔子/0203950.ogg"
    xz "只有这个绝对不行！"
    play voice "voice/青木铃音/0504880.ogg"
    lingyin "比赛还没开始呢，先冷静下来小翔姐姐~"
    play voice "voice/翔子/0203960.ogg"
    xz "你可从来没有这样称呼过我的！"
    me01 "翔子，再这样争辩下去的话还没开打你的体力可就要耗尽了。"
    play voice "voice/翔子/0203970.ogg"
    xz "哼，沙滩排球比起体力，更重要的是灵敏度和反射神经。"
    play voice "voice/青木铃音/0504890.ogg"
    lingyin "简单来说就是腕力不是重点吧？"
    me01 "毕竟不是专业的比赛，就算扣球也不会有太快的速度。"
    play voice "voice/青木铃音/0504900.ogg"
    lingyin "靠你了，姐姐。"
    play voice "voice/翔子/0203980.ogg"
    xz "嘛，适当地努力一下吧。"
    play voice "voice/青木铃音/0504910.ogg"
    lingyin "输了的话，作为惩罚要被对方涂防晒霜哟~"
    play voice "voice/翔子/0203990.ogg"
    xz "刚才没有听说过啊！"
    play voice "voice/一诚总司/1601900.ogg"
    yczs "神野，目标是铃音。从她们刚才的对话来看，在运动方面她远不如姐姐。"
    me01 "眼神变了啊喂，为了胜利全力以赴的你比这夏日的阳光更加的耀眼啊！"
    play voice "voice/青木铃音/0504920.ogg"
    lingyin "规则是先拿三分的队伍获胜。那么，我开球了~"
    play voice "voice/翔子/0204000.ogg"
    xz "等、等等，我可不承认什么惩罚游戏！"
    play voice "voice/青木铃音/0504930.ogg"
    lingyin "赢了就行啦，姐姐。"
    play voice "voice/翔子/0204010.ogg"
    xz "就算赢了也没有什么好处不是吗！"
    play voice "voice/青木铃音/0504940.ogg"
    lingyin "可以尽情抚摸年轻男性的肉体哦~"
    play voice "voice/翔子/0204020.ogg"
    xz "我可没有那种兴趣！"
    me01 "怎么了翔子，刚才的自信哪去了？"
    play voice "voice/翔子/0204030.ogg"
    xz "......看来你是想被尽情地蹂躏了。"
    scene set only beach day beachball3
    play voice "voice/青木铃音/0504950.ogg"
    lingyin "姐姐，我们一起退治那些变态吧。"
    play voice "voice/翔子/0204040.ogg"
    xz "是呢，在他们扰乱风纪之前。"
    play voice "voice/一诚总司/1601910.ogg"
    yczs "这样一来大家就都有斗志了吗，不愧是铃音同学。"
    me01 "只有我一个人被当成反派吗。"
    play voice "voice/一诚总司/1601920.ogg"
    yczs "赢了的话我会把涂抹防晒霜的机会先让给你的放心好啦。"
    me01 "不要加深误会啊！"
    play voice "voice/一诚总司/1601930.ogg"
    yczs "青木姐妹那娇羞的姿势我会完整地记录下来的，卖出去的钱我们对半分吧。"
    $ flcam.move(2250, -1100, 400, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0204050.ogg"
    xz "绝~对不要输给这两个变态！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "随着铃音将球抛出，比赛也正式开始了。"
    pause 1.0 hard
    scene set only beach day yinghua
    with dissolve
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_n1 onlayer m2:
        xpos 0.8
    play voice "voice/一诚总司/1601940.ogg"
    yczs "我们也要认真上了！"
    show yczs_sz_b1 b1 b1_h1
    play voice "voice/一诚总司/1601950.ogg"
    yczs "神野，我负责接球，托球的部分就拜托了！"
    me01 "噢！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "我托起一诚的接发球，球笔直地飞向网前。"
    show yczs_sz_b1 b1 b1_a1 onlayer screens:
        subpixel True
        xpos 0.87
        xzoom -1
        ypos side_actor_ypos.get('yczs', 0.5)
        yanchor 0.0
        zoom 1.8
    play voice "voice/一诚总司/1601960.ogg"
    yczs "不要怨我哦，觉悟吧！"
    hide yczs_sz_b1
    pause 0.5 hard
    play sound punch_2
    show wflash onlayer f1
    with vpunch
    pause 0.5 hard
    "一诚的扣杀直直地朝着铃音的方向飞去。"
    pause 1.0 hard
    scene set only beach day yinghua
    with dissolve
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204060.ogg"
    xz "想法太明显了！"
    pause 0.5 hard
    show xz_sz_b2 b2 b2_a2 at flu_up(0.15, 20):
        xpos 0.6
    show wflash onlayer f1
    pause 0.5 hard
    "翔子一个飞身截住了飞向铃音的球。"
    hide xz_sz_b2
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    show xz_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.6
    show lingyin_sz_b2 b2 b2_h3 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0504960.ogg"
    lingyin "干得真漂亮，姐姐。"
    hide xz_sz_b2
    show xz_sz_b1 b1 b1_a1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204070.ogg"
    xz "好了，快点把球托起来！"
    hide lingyin_sz_b2
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show jingya onlayer texture:
        xpos 0.0
    hide xz_sz_b1
    show xz_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.6
    pause 0.3 hard
    show xz_sz_b2 b2 b2_a2 at flu_up(0.15, 30):
        xpos 0.6
    play voice "voice/翔子/0204080.ogg"
    xz "看招！"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "翔子高高地跳起，上身大幅度向后仰。"
    "像是为了卯足劲才摆出这副姿势，不过那突出的身材在这个时候倒成了累赘。"
    "可恶，虽然很不甘心但真的很壮观，从任何意义上来说。"
    show xz_sz_b1 b1 b1_a1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0204090.ogg"
    xz "{size=72}呀啊！{/size}"
    hide xz_sz_b1
    stop music fadeout 5.0
    pause 0.5 hard
    play sound camera
    show wflash onlayer f1
    "咔嚓——"
    pause 1.0 hard
    scene set only beach day yinghua
    with dissolve
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    play music first_12 fadein 3.0 if_changed
    pause 0.3 hard
    show xz_sz_b1 b1 b1_ga2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.6
    play voice "voice/翔子/0204100.ogg"
    xz "{size=72}你在拍什么啊！{/size}"
    "挥空了。"
    pause 0.5 hard
    show lingyin_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504970.ogg"
    lingyin "啊啊，被对方得了一分。"
    hide xz_sz_b1
    show xz_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204110.ogg"
    xz "用照相机的闪光灯照我，也太卑鄙了吧！"
    hide xz_sz_b2
    hide lingyin_sz_b1
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_h1 onlayer m2:
        xpos 0.8
    play voice "voice/一诚总司/1601970.ogg"
    yczs "作战成功，青木姐姐的照片到手了神野~"
    me01 "不要在这个时候把话题丢过来啊！"
    show yczs_sz_b1 b1 b1_n1
    play voice "voice/一诚总司/1601980.ogg"
    yczs "好的，接下来也要继续以沙滩排球的名义努力“观察”才行！"
    $ flcam.move(5500, -200, 600, duration=1.5)
    pause 0.5 hard
    show camera_item onlayer m2 at basicfade_u2c:
        xpos 0.9
    show xz_sz_b3 b3 b3_a2 onlayer m1:
        xpos 0.5
        xzoom -1
        0.1
        easein 0.25 xoffset scale(+260)
    with vpunch
    play sound punch
    hide camera_item
    pause 0.5 hard
    play sound broken
    pause 2.0 hard
    hide xz_sz_b3
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    play sound bgsound1
    with vpunch
    show yczs_sz_b1 b1 b1_sp2
    play voice "voice/一诚总司/1601990.ogg"
    yczs "{size=72}搭档啊啊啊啊啊啊啊啊！！{/size}"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only beach day beachball2
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/0204120.ogg"
    xz "......这样相机应该就不能用了。别想着能活着回去，笨蛋凉。"
    me01 "你误会了翔子，刚刚那个不是我的计划！"
    play voice "voice/翔子/0204130.ogg"
    xz "铃音，发球！"
    pause 0.5 hard
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "话音未落，排球已经从铃音手中飞出。"
    pause 0.5 hard
    scene set only beach day yinghua
    with dissolve
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_s2 onlayer m2:
        xpos 0.8
    me01 "一诚，球来了！"
    play voice "voice/一诚总司/1602000.ogg"
    yczs "我一生都不会忘记你的，搭档......"
    me01 "现在不是给相机追悼的时候吧！"
    "既然一诚已经派不上用场了，那就只能一击把球打回去了。"
    hide yczs_sz_b1
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b1 b1 b1_a1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204140.ogg"
    xz "敌人只有一个了，现在就是机会！"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "铃音把回击的球高高托起，翔子盯着球的位置纵身跃起。"
    show xz_sz_b1 b1 b1_h1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0204150.ogg"
    xz "这样就同分了！"
    hide xz_sz_b1
    "看来是瞄准了一诚的空档，被击中的球径直向我的身后飞去。"
    pause 0.5 hard
    scene set only beach day yinghua
    with dissolve
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b2 b2 b2_h1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204160.ogg"
    xz "{size=72}拿下了！{/size}"
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_h1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504980.ogg"
    lingyin "赢了的话，就由我来代替男生们让姐姐涂防晒霜吧~"
    show xz_sz_b2 b2 b2_ga1 at flu_down(0.25, 20):
        xpos 0.6
    play voice "voice/翔子/0204170.ogg"
    xz "你用那样的手势说些什么呢！"
    "由于铃音的突然搭话，翔子击出的球向着我的方向飞来。"
    me01 "好机会！"
    hide lingyin_sz_b2
    show lingyin_sz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0504990.ogg"
    lingyin "啊啊，又被得了一分。"
    hide xz_sz_b2
    show xz_sz_b1 b1 b1_a1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204180.ogg"
    xz "都是你害的吧！"
    show lingyin_sz_b1 b1 b1_s1
    play voice "voice/青木铃音/0505000.ogg"
    lingyin "真是打击。"
    play voice "voice/翔子/0204190.ogg"
    xz "回去后要好好修理你！"
    hide lingyin_sz_b1
    show lingyin_sz_b2 b2 b2_h3 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0505010.ogg"
    lingyin "是，好兴奋~"
    "顺带一提，这一记扣杀借着反弹的力向着一诚的方向弹射而出。"
    "完美地砸在了破碎的相机上。"
    hide lingyin_sz_b2
    hide xz_sz_b1
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_sp2 onlayer m2:
        xpos 0.8
    play voice "voice/一诚总司/1602010.ogg"
    yczs "{size=72}搭档啊啊啊啊啊啊啊啊！！{/size}"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only beach day beachball3
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/0204200.ogg"
    xz "唔，这样一来对方不就拿到了赛点了吗。"
    play voice "voice/青木铃音/0505020.ogg"
    lingyin "但是姐姐，一诚同学失去战斗能力的现在，敌人只剩下神野同学一个人了。"
    play voice "voice/翔子/0204210.ogg"
    xz "我怎么觉得背后也有一个敌人......"
    play voice "voice/青木铃音/0505030.ogg"
    lingyin "姐姐的背后灵现在正处于反抗期呢~"
    play voice "voice/翔子/0204220.ogg"
    xz "我是在说你啦！"
    pause 0.5 hard
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "铃音发出的球再次朝着一诚的方向飞去。"
    "由于他仍旧处于挂机的状态，我也只好普通地把球顶了回去。"
    pause 0.5 hard
    scene set only beach day yinghua
    with dissolve
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b1 b1 b1_a1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204230.ogg"
    xz "铃音，接球！"
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_a1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0505040.ogg"
    lingyin "好的姐姐，托球就拜托了！"
    hide lingyin_sz_b2
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show jingya onlayer texture:
        xpos 0.0
    hide xz_sz_b1
    show xz_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204240.ogg"
    xz "接招吧神野君！"
    show xz_sz_b2 b2 b2_a2 at flu_up(0.15, 30):
        xpos 0.6
    hide jingya
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_sp2 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0505050.ogg"
    lingyin "姐姐，我要扣杀的球怎么自己飞过去了？"
    hide xz_sz_b2
    show xz_sz_b1 b1 b1_ga3 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204250.ogg"
    xz "你和我比起来就是个运动白痴，给你球的话自然是有概率会挥空的。"
    show lingyin_sz_b2 b2 b2_s1
    play voice "voice/青木铃音/0505060.ogg"
    lingyin "打击......"
    "真是不懂两人的关系是好还是坏。"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "总算是接起了翔子抛来的球，我把球高高地托起。"
    pause 0.5 hard
    scene set only beach day yinghua
    with dissolve
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b1 b1 b1_a1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204260.ogg"
    xz "铃音，接球！"
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_s1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0505070.ogg"
    lingyin "哼~"
    show xz_sz_b1 b1 b1_sp2 at flu_down(0.15, 20):
        xpos 0.6
    play voice "voice/翔子/0204270.ogg"
    xz "别闹别扭了，快把球接起来，拜托了。"
    hide lingyin_sz_b2
    show lingyin_sz_b1 b1 b1_n2 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0505080.ogg"
    lingyin "赢了的话，能让我给你涂防晒霜吗？"
    hide xz_sz_b1
    show xz_sz_b2 b2 b2_ga1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.6
    play voice "voice/翔子/0204280.ogg"
    xz "防晒霜还是什么都给你涂啦，快点快点，球快要落地了！"
    hide xz_sz_b2
    $ flcam.move(-2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show jingya onlayer texture:
        xpos 0.0
    hide lingyin_sz_b1
    show lingyin_sz_b2 b2 b2_a1 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0505090.ogg"
    lingyin "神野同学，觉悟吧！"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "铃音眼中突然燃起了火焰，在球几乎落地的瞬间将它托了起来。"
    show xz_sz_b1 b1 b1_a1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0204290.ogg"
    xz "就这样先得一分！"
    hide xz_sz_b1
    play sound punch_2
    show wflash onlayer f1
    pause 1.0 hard
    me01 "没那么容易！"
    "好在和我预想的一样，扣杀后的球飞向了毫无还手之力的一诚，勉强算是被我救了回来。"
    pause 0.5 hard
    $ flcam.move(2500, -300, 900, duration=1.5)
    scene set only beach day yinghua
    show xz_sz_b1 b1 b1_a1 onlayer m2:
        xpos 0.6
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/0204300.ogg"
    xz "铃音，再接一次球！"    
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_s1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0505100.ogg"
    lingyin "哼~"
    hide xz_sz_b1
    show xz_sz_b2 b2 b2_ga1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.6
    play voice "voice/翔子/0204310.ogg"
    xz "这次又是为什么闹别扭啊！"
    hide lingyin_sz_b2
    show lingyin_sz_b1 b1 b1_n2 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0505110.ogg"
    lingyin "那、那个......我有重要的事情要说。虽然觉得可能有点不体面，但是能听我说完吗？"
    hide xz_sz_b2
    show xz_sz_b1 b1 b1_sp2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204320.ogg"
    xz "在这种分秒必争的时候，你到底想怎么样啊？"
    show lingyin_sz_b1 b1 b1_s2
    play voice "voice/青木铃音/0505120.ogg"
    lingyin "可以的话，我在涂防晒霜的时候，姐姐能把泳装脱下来的话我会很开心的~"
    show xz_sz_b1 b1 b1_a1
    play voice "voice/翔子/0204330.ogg"
    xz "这种事怎么可能照做啊！"
    show lingyin_sz_b1 b1 b1_s1
    play voice "voice/青木铃音/0505130.ogg"
    lingyin "打击......"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "铃音那毫无干劲的拖球直接让球越过了网飞到了我的上方。"
    me01 "{size=72}机会！{/size}"
    pause 0.5 hard
    $ flcam.move(0, -200, 600)
    scene set only beach day yinghua
    show xz_sz_b1 b1 b1_a1 onlayer m2:
        xpos 0.6
    show lingyin_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.4
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/0204340.ogg"
    xz "铃音，你给我记住！"
    hide lingyin_sz_b1 
    hide xz_sz_b1
    $ flcam.move(4500, -100, 400, duration=1.5)
    pause 0.5 hard
    "从球的轨迹来看正好会在扣杀的绝佳位置落下。"
    me01 "这样一来就赢了！"
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204350.ogg"
    xz "没那么容易！"
    show xz_sz_b2 b2 b2_a2 at flu_up(0.15, 30):
        xpos 0.6
    show wflash onlayer f1
    "不愧是翔子，不仅预判到了我会狙击铃音，而且还一份飞身轻松化解了我的扣杀。"
    pause 0.5 hard
    show lingyin_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0204360.ogg"
    xz "铃音，把球托起来！"
    show lingyin_sz_b1 b1 b1_s3
    play voice "voice/青木铃音/0505140.ogg"
    lingyin "姐姐不肯脱泳装......"
    hide xz_sz_b2
    show xz_sz_b1 b1 b1_sp2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204370.ogg"
    xz "我、我知道了啦，在没人的地方我会脱下来三秒钟的！"
    hide xz_sz_b1
    $ flcam.move(-2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show jingya onlayer texture:
        xpos 0.0
    hide lingyin_sz_b1
    show lingyin_sz_b2 b2 b2_a1 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0505150.ogg"
    lingyin "为了这三秒钟，我就算是刀山火海也能跳进去！"
    "铃音的眼中再次燃起了斗志的火焰。"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua2
    with dissolve
    pause 1.0 hard
    "既然机会球不再来的话，光凭我一人已经没办法再打出完美的扣杀了。"
    "我可不想在这眼看就要赢下来的情况被慢慢反超啊，就没有什么办法了吗？"
    "就在我踌躇不定的时候，我与铃音的眼神交汇了。"
    pause 0.5 hard
    $ flcam.move(-2250, -300, 900)
    scene set only beach day yinghua
    show lingyin_sz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.4
    with dissolve
    me01 "（我可以把涂防晒霜的机会让给你，让我赢吧。这样一来无论多久你都可以尽情地抚摸翔子的肌肤了！）"
    show lingyin_sz_b2 b2 b2_h1
    play voice "voice/青木铃音/0505160.ogg"
    lingyin "在扣球之前悄悄地把姐姐的比基尼解开就行了是吧，我知道了神野同学！"
    "传达的意思差别太大了！"
    hide lingyin_sz_b2
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b2 b2 b2_a1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204380.ogg"
    xz "笨蛋凉！"
    me01 "不不，这和我想传达的意思可不一样！"
    show xz_sz_b2 b2 b2_a2
    play voice "voice/翔子/0204390.ogg"
    xz "那不就说明你有其他的目的了吗。"
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    show lingyin_sz_b1 b1 b1_h1 onlayer m1:
        xpos 0.4
        xzoom -1
        0.1
        easein 0.3 xpos 0.45
    play voice "voice/青木铃音/0505170.ogg"
    lingyin "趁现在......"
    $ flcam.move(1300, -350, 750, duration=1.5)
    pause 0.5 hard
    hide xz_sz_b2 with None
    pause 0.1 hard
    show xz_sz_b1 b1 b1_sp2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.6
    play voice "voice/翔子/0204400.ogg"
    xz "啊啊啊，不要真的照做啊！"
    hide lingyin_sz_b1
    show lingyin_sz_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0505180.ogg"
    lingyin "姐姐，这样下去的话球就要落地了！"
    show xz_sz_b1 b1 b1_a1
    play voice "voice/翔子/0204410.ogg"
    xz "你以为是谁的错啊。"
    "翔子没有了扣杀的余力，只好把球高高地托起。"
    me01 "好机会！"
    hide lingyin_sz_b2
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0204420.ogg"
    xz "！"
    "明明是抓住了空档的扣杀，却还是被翔子救了回来。"
    pause 0.5 hard
    show lingyin_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0204430.ogg"
    xz "铃音，托球拜托了！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only beach huachi1
    with dissolve
    pause 0.5 hard
    play voice "voice/青木铃音/0505190.ogg"
    lingyin "啊姐姐，连续的飞身救球搞得全身那珍珠般的肌肤都脏了~"
    play voice "voice/翔子/0204440.ogg"
    xz "你干嘛突然靠到人家身上来啊？！"
    play voice "voice/青木铃音/0505200.ogg"
    lingyin "浑身是泥的姐姐也是如此地让人垂涎欲滴。"
    play voice "voice/翔子/0204450.ogg"
    xz "行了别闹了，快点把球救起来！"
    scene set only beach huachi2
    play voice "voice/青木铃音/0505210.ogg"
    lingyin "大概是被高温所影响，我有些控制不住自己了~"
    scene set only beach huachi3
    $ flcam.move(1250, -1100, 400, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0204460.ogg"
    xz "呀啊，别脱我泳衣啊，不行，不要碰，哈啊啊，那里不行~"
    pause 0.5 hard
    stop music fadeout 5.0
    scene set only beach day yinghua
    with dissolve
    pause 1.0 hard
    $ flcam.move(-2500, -300, 900, duration=1.5)
    pause 0.5 hard
    play music first_13 fadein 3.0 if_changed
    show lingyin_sz_b2 b2 b2_s1 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0505220.ogg"
    lingyin "啊啊，最后还是被对方先拿了三分。"
    pause 0.5 hard
    show xz_sz_b1 b1 b1_a1 onlayer m2:
        xpos 0.6
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0204470.ogg"
    xz "铃、铃音，你到底想怎么样！"
    hide lingyin_sz_b2
    show lingyin_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0505230.ogg"
    lingyin "祥瑞御免恶灵退散。"
    hide xz_sz_b1
    show xz_sz_b2 b2 b2_a2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204480.ogg"
    xz "给我好好解释清楚！"
    show lingyin_sz_b1 b1 b1_s2
    play voice "voice/青木铃音/0505240.ogg"
    lingyin "神野同学威胁我......要是不让他赢的话就把防晒霜涂遍我的全身。"
    hide lingyin_sz_b1
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_sz_b2 b2 b2_a1
    play voice "voice/翔子/0204490.ogg"
    xz "笨蛋凉！"
    me01 "拜托你不要相信这种敷衍的谎话啊，我是被冤枉的！"
    hide xz_sz_b2
    show xz_sz_b3 b3 b3_a1 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0204500.ogg"
    xz "威胁可是犯规的行为，所以这次的惩罚无效，明白了吗？"
    hide xz_sz_b3
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_sz_b1 b1 b1_s1 onlayer m2:
        xpos 0.8
    play voice "voice/一诚总司/1602020.ogg"
    yczs "搭档......你要安心成佛啊。"
    hide yczs_sz_b1
    $ flcam.move(-2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_h1 onlayer m2:
        xpos 0.4
    play voice "voice/青木铃音/0505250.ogg"
    lingyin "海水浴真是有意思呢~"
    "结果只有铃音一人成为了“赢家”。"
    hide lingyin_sz_b2
    $ flcam.move(-7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_sz_b2 b2 b2_h2 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114410.ogg"
    rxl "小凉，小铃~大家也快来游泳啊。"
    pause 0.5 hard
    show lingyin_sz_b2 b2 b2_h1 onlayer m2:
        xpos 0.4
    show xz_sz_b3 b3 b3_s1 onlayer m2:
        xpos 0.6
    $ flcam.move(-2250, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0505460.ogg"
    lingyin "日向同学回来了啊。"
    hide rxl_sz_b2
    show rxl_sz_b1 b1 b1_ga1 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114420.ogg"
    rxl "啊咧，怎么小凉好像有点消沉的样子。还有那边的前辈们和一诚君也是。"
    play voice "voice/翔子/0205080.ogg"
    xz "真是的，最近的男孩子真是丢脸呢。"
    show lingyin_sz_b2 b2 b2_n1
    play voice "voice/青木铃音/0505470.ogg"
    lingyin "从姐姐嘴里说出来真是没有说服力呢。"
    hide rxl_sz_b1
    hide lingyin_sz_b2
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    "翔子起身从遮阳伞的阴影中走了出来。"
    show lingyin_sz_b1 b1 b1_n1 onlayer m2:
        xpos 0.4
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0505480.ogg"
    lingyin "姐姐，我也一起去游泳。"
    hide xz_sz_b3
    show xz_sz_b1 b1 b1_n2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/0205110.ogg"
    xz "......要是在海里做些奇怪的事我可不会轻易饶恕你的。"
    show lingyin_sz_b1 b1 b1_h1
    play voice "voice/青木铃音/0505490.ogg"
    lingyin "是，好兴奋~"
    hide lingyin_sz_b1
    hide xz_sz_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    $ flcam.move(-7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_sz_b1 b1 b1_n3 onlayer m2:
        xpos 0.2
    play voice "voice/日向怜/0114440.ogg"
    rxl "小凉也来吧~"
    me01 "日向同学不休息下没问题吗？"
    show rxl_sz_b1 b1 b1_h1
    play voice "voice/日向怜/0114450.ogg"
    rxl "没问题的，我还能一直游到晚上的。"
    me01 "真有精神啊。"
    show rxl_sz_b1 b1 b1_n3
    play voice "voice/日向怜/0114460.ogg"
    rxl "小凉也打起精神来吧~"
    "于是乎我也被精力充沛的日向怜拉着一起向大海的方向走去。"
    "只留下消沉的一诚继续蹲在原地。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard

label day07.beach_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky evening yinghua2
    with dissolve
    play music first_07 fadein 3.0 if_changed
    pause 2.0 hard
    scene set only beach evening yinghua
    with right2left
    pause 2.0 hard
    "傍晚时分，海滩上的游客也开始陆续离开了。"
    $ flcam.move(2250, -100, 400, duration=1.5)
    pause 0.5 hard
    stop music fadeout 5.0
    "黄昏的余晖中，我遇见今夜的第一颗星辰——"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0006750.ogg"
    lst "这就是，大海......"
    play voice "voice/天使雷亚/0006760.ogg"
    lst "樱华镇的海。"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0006770.ogg"
    lst "不是漆黑一片的海，还是第一次看到。"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening yinghua2
    with dissolve
    pause 2.0 hard
    play music first_33 fadein 3.0 if_changed
    pause 1.0 hard
    scene set only lisite_cg sea1
    with cent2side
    pause 2.0 hard
    "在海天都被夜色笼罩的当下，也只有地平线的地方还残存着些许淡淡的光芒。"
    "那是将世界一分为二的光。"
    "境界的彼方。"
    "虽然天地已经被同一种颜色所覆盖，但只要有看着它就仿佛在证明有另一个世界的存在。"
    play voice "voice/天使雷亚/0006780.ogg"
    lst "这就是......"
    "或许这片光景也正象征着我和雷亚的关系。那份本不该相交，却又彼此纠缠的牵绊。"
    play voice "voice/天使雷亚/0006790.ogg"
    lst "这就是夜空出现之前，世界的景色。"
    me01 "雷亚。"
    pause 0.1 hard
    scene set only lisite_cg sea2
    with dissolve
    play voice "voice/天使雷亚/0006800.ogg"
    lst "什么事？"
    me01 "你觉得从这里到水平线的距离有多远？"
    pause 0.1 hard
    scene set only lisite_cg sea1
    with dissolve
    play voice "voice/天使雷亚/0006810.ogg"
    lst "非常非常地远吧？"
    me01 "具体有多远？"
    play voice "voice/天使雷亚/0006820.ogg"
    lst "......一百公里左右？"
    me01 "不，是五公里。"
    me01 "根据勾股定理和圆周率就可以推算出来。"
    play voice "voice/天使雷亚/0006830.ogg"
    lst "书呆子。"
    "水平线与我们意外的近。"
    "但虽是如此的靠近。"
    me01 "明明只有五公里，我们却永远也无法触及那道光。"
    "越美好的事物，就越是无法留住。"
    "在离开的这些日子里。"
    "我也渐渐开始怀念起那段美好却又无法挽留的时光。"
    "欲求而不达，这或许就是最开始人们定义美好的标准吧。"
    pause 0.1 hard
    scene set only lisite_cg sea2
    with dissolve
    $ flcam.move(1800, -1100, 400, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0006840.ogg"
    lst "为什么突然在那边傻笑啊？"
    me01 "总觉得有点可惜呢。"
    play voice "voice/天使雷亚/0006850.ogg"
    lst "可惜什么？"
    me01 "城市那头并没有海，所以也没有办法像这样和大家一起来到海边。"
    me01 "虽说是有游泳池，但那狭窄的空间难免也会让人感到些许寂寞。"
    me01 "但这里不一样。"
    me01 "这里对我来说是特别的。"
    me01 "说实话，能和雷亚你一起欣赏这样的美景，也是我一生中最重要的回忆之一了。"
    play voice "voice/天使雷亚/0006860.ogg"
    lst "......"
    pause 0.1 hard
    scene set only lisite_cg sea1
    with dissolve
    "雷亚正打算说些什么，就在这时身后传来了大家的声音。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    show rxl_sz_b1 b1 b1_n3 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/0114810.ogg"
    rxl "哇，这是什么，这样的景色从来没有见到过~"
    hide rxl_sz_b1
    show xz_sz_b1 b1 b1_n3 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0205120.ogg"
    xz "日落西山，这也是我平生第一次看到吧。"
    hide xz_sz_b1
    show lingyin_sz_b2 b2 b2_n1 onlayer screens at side_left('lingyin'), basicfade
    play voice "voice/青木铃音/0505500.ogg"
    lingyin "世上真有这样的景色呢~"
    hide lingyin_sz_b2
    show yczs_sz_b1 b1 b1_n1 onlayer screens:
        subpixel True
        xpos 0.87
        xzoom -1
        ypos side_actor_ypos.get('yczs', 0.5)
        yanchor 0.0
        zoom 1.82
    play voice "voice/一诚总司/1602050.ogg"
    yczs "如果照相机还在就好了。"
    hide yczs_sz_b1
    hide lingyin_sz_b2
    $ flcam.move(1800, -1100, 400, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "余晖渐渐消散。"
    "境界残存的光芒溶解在了夜空之中。"
    "无论如何感到惋惜，但还是清楚的。"
    "那束美丽的光从来不会为了谁而多停留片刻。"
    pause 0.5 hard
    scene black
    with slowerdissolve
    stop music fadeout 5.0
    pause 3.0 hard

label day07.party_event01:
    $ flcam.move(0, 0, 0)
    scene set only party yinghua
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    "事后才知道，原来铃音母亲安排的不只有海水浴而已。"
    "这一切也是为了今晚庆典做出的准备。"
    "热闹的神社内人山人海。"
    "男女老少们穿着浴衣行走在石板街上，周围更是遍布了各种商铺。"
    "在场的大多数面孔都是早上海滩上的游客，这里不得不佩服万夜花小姐的营销手段。"
    "作为夏日祭庆典的压轴，听说还会举办神事。"
    $ flcam.move(-2500, -300, 900, duration=1.5)
    pause 0.5 hard
    play music first_16 fadein 3.0 if_changed
    show rxl_xsf_b2 b2 b2_h3 onlayer m2 at walkin_l(0.4)
    pause 0.5 hard
    play voice "voice/日向怜/0115730.ogg"
    rxl "今天是八月七日，也是樱华镇夏日祭最热闹的一天~"
    hide rxl_xsf_b2
    show rxl_xsf_b1 b1 b1_n3 onlayer m2:
        xpos 0.4
    play voice "voice/日向怜/0115740.ogg"
    rxl "这节日本来也叫七夕节。毕竟按照旧历算，七夕也是在这一天附近。"
    show rxl_xsf_b1 b1 b1_h1
    play voice "voice/日向怜/0115750.ogg"
    rxl "而且，牛郎星和织女星最闪耀的时候也是在七夕。所以等庆典结束了我们就去看星星吧~"
    me01 "神事的内容也和七夕有关吗？"
    hide rxl_xsf_b1
    show rxl_xsf_b2 b2 b2_h3 onlayer m2:
        xpos 0.4
    play voice "voice/日向怜/0115770.ogg"
    rxl "嗯。听说是在神社里面的神殿举行，到时候会有很多人，是十分难得的场面。"
    me01 "话说怎么不见铃音同学，既然是主办方的“亲信”，可以让她们帮个忙绕开人群吧？"
    show rxl_xsf_b2 b2 b2_s2
    play voice "voice/日向怜/0115780.ogg"
    rxl "小铃可是很忙的，所以也不好强人所难。至于小翔那边就算拜托她，多半也会被拒绝的。"
    me01 "话说回来之前我问过翔子，她似乎不太喜欢别人提到在庆典上的工作。"
    show rxl_xsf_b2 b2 b2_ga1
    play voice "voice/日向怜/0115790.ogg"
    rxl "啊哈哈，大概是是因为难为情吧~"
    me01 "难为情？"
    show rxl_xsf_b2 b2 b2_n1
    play voice "voice/日向怜/0115800.ogg"
    rxl "之前的主角一直都是万夜花小姐，但是自从去年邀请樱华校来承办，主角就变成小翔了。"
    pause 0.5 hard
    show yczs_xsf_b1 b1 b1_s1 onlayer m2 at walkin_r(0.6)
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1603470.ogg"
    yczs "如果青木长女搞砸的话，明年或许就会轮到铃音同学了。"
    me01 "身为主角具体要做些什么呢？"
    hide rxl_xsf_b2 
    show rxl_xsf_b1 b1 b1_n3 onlayer m2:
        xpos 0.4
    play voice "voice/日向怜/0115810.ogg"
    rxl "别急，很快就开始了。既然来了就去看看吧。"
    me01 "日向同学不一起去吗？"
    hide rxl_xsf_b1
    show rxl_xsf_b2 b2 b2_h2 onlayer m2:
        xpos 0.4
    play voice "voice/日向怜/0115820.ogg"
    rxl "人太多了，以我的身高不太方便。小凉的话就算从后排也能看到的吧？"
    me01 "一诚同学呢？"
    show yczs_xsf_b1 b1 b1_ga1
    play voice "voice/一诚总司/1603480.ogg"
    yczs "虽然是想，但祭典也差不多要结束了吧。"
    hide rxl_xsf_b2
    hide yczs_xsf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_wnf_b2 b2 b2_h1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/青木铃音/0506110.ogg"
    lingyin "正好大家也到齐了。"
    show lingyin_wnf_b2 b2 b2_n1
    play voice "voice/青木铃音/0506120.ogg"
    lingyin "今年也有很多的人参加呢。"
    me01 "也难怪你们一直都很忙的样子。"
    show lingyin_wnf_b2 b2 b2_ga3
    play voice "voice/青木铃音/0506130.ogg"
    lingyin "我的话还算轻松的了，只需要接几个电话就行。"
    show lingyin_wnf_b2 b2 b2_n1
    play voice "voice/青木铃音/0506140.ogg"
    lingyin "辛苦的是接受电话委托那边，到处奔波的妈妈和姐姐。"
    pause 0.5 hard
    show yczs_xsf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1603490.ogg"
    yczs "相比之下，万夜花阿姨刚刚似乎还在大厅里喝酒来着。"
    "明明是神官，却一点也不靠谱的样子。"
    hide lingyin_wnf_b2
    show lingyin_wnf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0506150.ogg"
    lingyin "我就想她迟迟不来，肯定又是在偷懒了。"
    hide yczs_xsf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "翔子那边还在工作吗？"
    show lingyin_wnf_b1 b1 b1_n1
    play voice "voice/青木铃音/0506160.ogg"
    lingyin "是的，正在为神事做准备。"
    "到头来，今年也没能和翔子一起逛夜市。"
    "有点失落。"
    hide lingyin_wnf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/0115940.ogg"
    rxl "我拿到了三个奖品~"
    pause 0.5 hard
    show yczs_xsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    show lingyin_wnf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0506170.ogg"
    lingyin "那么大家，正好手里也没什么事了，可以跟我过来一下吗？"
    hide rxl_xsf_b1
    show rxl_xsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/0115950.ogg"
    rxl "要去哪里？"
    hide lingyin_wnf_b2
    show lingyin_wnf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0506190.ogg"
    lingyin "神殿。"
    hide rxl_xsf_b2
    hide yczs_xsf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide lingyin_wnf_b1
    show lingyin_wnf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0506200.ogg"
    lingyin "虽然离神事开始还有些时间，但我想早点把大家带过去。"
    show lingyin_wnf_b2 b2 b2_h1
    stop music fadeout 5.0
    play voice "voice/青木铃音/0506210.ogg"
    lingyin "已经订好了特等席~"
    hide lingyin_wnf_b2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    play music first_47 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only party xiangzi
    with slowdissolve
    pause 1.0 hard
    "庄严的太鼓、澄澈的铮鸣和清脆的笛声相辅相成。所有的声音都交织在了一起。"
    "在这舞台——神乐殿的正中央，呈现在众人面前的是翔子的身影。"
    "随着旋律，在这幻彩的空间中舞动着。"
    $ flcam.move(1500, -1800, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "此时她身着的并非是之前的巫女服，而是更加艳丽的羽衣。"
    "一边挥舞着薙刀，一边将神乐献给神明。"
    play voice "voice/万夜花/1300470.ogg"
    stranger "对小翔来说虽然还只是第二次，不过却已经是有模有样了。"
    "身后飘来一阵酒气。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only party front
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/万夜花/1300480.ogg"
    wyh "如何，对樱华镇的祭典有什么感想？"
    me01 "应该说很有其独到之处吧。"
    show wyh_wnf_b1 b1 b1_h1
    play voice "voice/万夜花/1300490.ogg"
    wyh "啊哈哈，独到之处说到底这也只是盂兰节的一部分而已。七夕本来也有祭拜祖先的仪式。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1300500.ogg"
    wyh "这巫女神乐也是一样的，被选出来的巫女需要一边做裁缝一边等待神明的认可。"
    me01 "与其说是做裁缝，不如说更像是舞剑。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1300510.ogg"
    wyh "是啊，不过裁缝本身就是织女坊布用的{encyclopedia=caiwu}採物{/encyclopedia}，只是在星天宫被换成了薙刀而已。"
    me01 "採物？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only party xiangzi
    with dissolve
    pause 1.0 hard
    show wyh_wnf_b1 b1 b1_n1 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300520.ogg"
    wyh "所谓神乐，就是用身体来表现灵魂的一种祈祷。而最终会被神明的力量依附的咒具就是採物。"
    play voice "voice/万夜花/1300530.ogg"
    wyh "小翔她现在正在用这採物将神明的灵魂纳入自己的身体，然后祈福、送还。"
    play voice "voice/万夜花/1300540.ogg"
    wyh "这也被称为镇魂或者送魂，母亲同样是巫女的你应该也有所耳闻吧。"
    play voice "voice/万夜花/1300550.ogg"
    wyh "以前还有过把竹笺顺着河水顺流而下的祈愿仪式，那孩子的舞蹈总会让我想起当年的场景啊。"
    show wyh_wnf_b1 b1 b1_ga2
    play voice "voice/万夜花/1300560.ogg"
    wyh "嘛，虽然在我看来，冲击......或者说攻击力还不够。"
    hide wyh_wnf_b1
    me01 "别破坏气氛啊！"
    show wyh_wnf_b1 b1 b1_n1 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300570.ogg"
    wyh "採物除了刚才说到的裁缝和薙刀外，还有各种各样的类型。它们各自都有自己的用途。"
    play voice "voice/万夜花/1300580.ogg"
    wyh "在日本，铃铛和扇子为邀请神灵，竹笺和布帛则是为了祈祷进化和再生。"
    show wyh_wnf_b1 b1 b1_h1 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300590.ogg"
    wyh "而欧洲的剑、中国的弓弩和日本的薙刀等则象征武力，起到驱邪避恶的作用。"
    hide wyh_wnf_b1
    me01 "所以才说是攻击力吗？"
    show wyh_wnf_b1 b1 b1_s1 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300600.ogg"
    wyh "请你别破坏气氛啊。"
    hide wyh_wnf_b1
    me01 "唯独不想被您这么说！"
    show wyh_wnf_b1 b1 b1_n1 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300610.ogg"
    wyh "使用武器的舞蹈，祖型是修习道术，据说是为了消灭鬼而存在的。"
    play voice "voice/万夜花/1300620.ogg"
    wyh "事实上不只是驱鬼，还有将“祟”送还{rb}原处{/rb}{rt}冥界{/rt}的意思。"
    play voice "voice/万夜花/1300630.ogg"
    wyh "在那里的是什么，你知道吗？"
    hide wyh_wnf_b1
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only party stone
    with dissolve
    pause 1.0 hard
    $ flcam.move(500, -800, 400, duration=1.5)
    pause 0.5 hard
    "那被摆放在祭坛上方的东西，一眼看去像是块石头。"
    me01 "这就是目前神体的凭依吗？"
    show wyh_wnf_b1 b1 b1_h1 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300640.ogg"
    wyh "没错，它的本质是什么知道吗？"
    hide wyh_wnf_b1
    me01 "水晶？"
    show wyh_wnf_b1 b1 b1_ga2 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300650.ogg"
    wyh "差一点，虽然在矿石这一点上说对了。"
    hide wyh_wnf_b1
    "虽然外表粗糙，但是却能够反射灯光，通体还散发着微弱的淡紫色光芒。"
    show wyh_wnf_b1 b1 b1_n1 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300660.ogg"
    wyh "我们将那视为天津瓮星的凭依祭祀在这神社之中。"
    play voice "voice/万夜花/1300670.ogg"
    wyh "星天宫奉命镇守于此，并依照旧历在七夕时节开展神事。"
    hide wyh_wnf_b1
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only party xiangzi
    with dissolve
    pause 1.0 hard
    show wyh_wnf_b1 b1 b1_h1 onlayer screens at side_left('wyh', 0.09), basicfade
    play voice "voice/万夜花/1300680.ogg"
    wyh "那孩子虽然有时挺倔强，但却并非无所畏惧。只要是缺点她都会靠自己的努力来弥补。"
    play voice "voice/万夜花/1300690.ogg"
    wyh "不愧是我们神社的新舞姬，真不知道是受哪个优秀家伙的影响呢~"
    hide wyh_wnf_b1
    "的确，比起印象中，眼前的翔子给我的感觉更加成熟了。"
    "如今的她已然是能够独当一面，在我未曾踏足的地方开辟出属于自己的辉煌荣耀了。"
    "也许此刻的她比我更加配得上“优等生”这个称号吧。"
    pause 2.0 hard
    stop music fadeout 5.0
    scene black
    with dissolve
    pause 3.0 hard

label day07.starview_event01:
    play ambience1 zhiliao fadein 3.0
    $ flcam.move(0, 0, 0)
    scene set only starview night road
    with slowerdissolve
    pause 1.0 hard
    "庆典结束后，我依旧还是来到了观景台。"
    "话说祭典上完全没有看到雷亚的身影。"
    "不过这么热闹的地方那家伙一定会避而远之的吧。"
    pause 1.0 hard
    play voice "voice/翔子/010503.ogg"
    stranger "凉君？"
    play music first_42 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_xsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    me01 "翔子？"
    hide xz_xsf_b3
    show xz_xsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010504.ogg"
    xz "果然在这里。"
    "也许是私底下相处的关系，此时的翔子称呼我为“凉君”。"
    "虽说见面之后这样的称谓也不是第一次听到，但比起儿时也的确少了许多。"
    "这也总让我觉得有些许违和感。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_xsf_b3 b3 b3_s4 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    me01 "庆典那边的工作都结束了吗？"
    play voice "voice/翔子/010505.ogg"
    xz "嗯。"
    show xz_xsf_b3 b3 b3_s2
    play voice "voice/翔子/010506.ogg"
    xz "今天真是抱歉。明明是庆典的最后一天，我却因为自己的事情耽误了。"
    me01 "别放在心上，虽然没能一起逛灯会总归还是有些遗憾的。"
    me01 "但能在那么近的距离欣赏到翔子你的神乐也算值得了。"
    me01 "不过话说回来，现在不休息没问题吗？"
    hide xz_xsf_b3
    show xz_xsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010507.ogg"
    xz "嗯，现在已经没事了。多亏了这片星空吧~"
    hide xz_xsf_b2
    show xz_xsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010508.ogg"
    xz "只要看着星星的光辉，我就会变得有精神。"
    me01 "呐，翔子......"
    show xz_xsf_b3 b3 b3_sp1
    "我向她诉说了与雷亚的相遇。"
    "以及她口中的“噩梦”。"
    me01 "要是我今后也会一直来这里，你......"
    me01 "会阻止我吗？"
    show xz_xsf_b3 b3 b3_n1
    play voice "voice/翔子/010514.ogg"
    xz "不会的。"
    hide xz_xsf_b3
    show xz_xsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010515.ogg"
    xz "因为，是我也会选择继续来这里的。"
    play voice "voice/翔子/010516.ogg"
    xz "我不想就这么放弃。"
    show xz_xsf_b2 b2 b2_n2
    play voice "voice/翔子/010518.ogg"
    xz "我也想让凉君知道，在你身后还有我在支持着你的。"
    play voice "voice/翔子/010519.ogg"
    xz "我不想成为你的负担。"
    show xz_xsf_b2 b2 b2_n1
    play voice "voice/翔子/010520.ogg"
    xz "所以，把你的背后交给我就行了。"
    play voice "voice/翔子/010521.ogg"
    xz "凉君你，只要一直向前看就好了......"
    stop ambience1
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 1.75 alpha 1
    pause 3.0 hard
    show sepiagrain onlayer texture
    nvl clear
    pcenter "  ——是从那时候开始的吧。"
    nvl clear
    pcenter "  在这座观景台我发现了人生中最宝贵的东西。"
    nvl clear
    pcenter "  那是我成为“优等生”所不可或缺的东西。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only starview night starview
    show xz_xsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    me01 "天气开始变凉了，翔子你还是先回去吧。"
    me01 "我还得去见雷亚一面，有一些事情必须问清楚。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    hide xz_xsf_b3
    $ flcam.move(-4500, -200, 600, duration=1.5)
    pause 0.5 hard
    "我将外套脱下披在翔子的肩上，然后转身向观景台深处走去。"
    "目送我远去后，翔子静静地望着这片星空伫立了许久。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 1.0 hard
    show xz_xsf_b1 b1 b1_s2 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/010510.ogg"
    xz "夏日的星空还真是安静，这也许是在观景台上最能感受祥和氛围的季节了吧。"
    show xz_xsf_b1 b1 b1_s3
    play voice "voice/翔子/010512.ogg"
    xz "所以如果再也不能来这里的话，是不是就会觉得寂寞了呢？"
    play voice "voice/翔子/010513.ogg"
    xz "雷亚她......"
    hide xz_xsf_b1
    pause 2.0 hard
    stop music fadeout 5.0
    scene black 
    with slowdissolve
    pause 3.0 hard

label day07.starview_event02:
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg normal
    play music first_27 fadein 3.0 if_changed
    with dissolve
    play voice "voice/天使雷亚/0001570.ogg"
    lst "这就是......七夕的星空吗？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0001580.ogg"
    lst "总觉得星星多到让人害怕。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001590.ogg"
    lst "再美丽的东西看多了也会变得怪诞起来。"
    me01 "这种表达倒是有些破坏现在的气氛啊。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    $ flcam.move(1500, -1800, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0001600.ogg"
    lst "织女星和牛郎星，能认出来吗？"
    me01 "那条像云彩一样的光带就是银河。在银河上下围绕着的就是织女星和牛郎星。"
    play voice "voice/天使雷亚/0001610.ogg"
    lst "上面的那个是？"
    me01 "织女星。"
    play voice "voice/天使雷亚/0001620.ogg"
    lst "下面那个是牛郎星？"
    me01 "是的。"
    pause 0.1 hard
    scene set only lisite_cg happy
    with dissolve
    play voice "voice/天使雷亚/0001630.ogg"
    lst "答得不错~"
    play voice "voice/天使雷亚/0001640.ogg"
    lst "那么牛郎星他......"
    pause 0.1 hard
    scene set only lisite_cg smile
    with dissolve
    play voice "voice/天使雷亚/0001650.ogg"
    lst "牛郎星他，一定会对织女星唯命是从吧。"
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 1.75 alpha 1
    pause 3.0 hard
    scene set only xz_memory piecefour yinghua
    with dissolve
    play voice "voice/翔子/0601240.ogg"
    tiny_xz "那我们约好了。"
    play voice "voice/翔子/0601250.ogg"
    tiny_xz "我们一定要再次相见。"
    play voice "voice/翔子/0601260.ogg"
    tiny_xz "一定要在这座观景台再次相见。"
    play voice "voice/翔子/0601270.ogg"
    tiny_xz "就像牛郎和织女那样，即使暂时分开了到最后也一定要再次相遇！"
    play voice "voice/翔子/0601290.ogg"
    tiny_xz "然后结婚，对我唯命是从！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0001660.ogg"
    lst "怎么了，一直在傻笑？"
    me01 "没什么。"
    "这孩子总能在不经意间勾起我的回忆。"
    me01 "雷亚你知道七夕的传说吗？"
    "雷亚没有回答。"
    "只是默默地摇了摇头。"
    me01 "我来告诉你吧？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0001670.ogg"
    lst "说不说都无所谓。"
    me01 "不要那么抗拒嘛。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0001680.ogg"
    lst "到头来只是你自己想说而已嘛。"
    pause 1.0 hard
    scene set only sky night yinghua2
    with dissolve
    pause 1.0 hard
    me01 "很久很久以前，在银河边上住着一位美丽的女子，她叫织女，是天帝的女儿。"
    me01 "谨记天帝的嘱咐，织女日复一日地织布，创造出了许多美丽的布帛。"
    me01 "天帝对织女的工作表示赞许，可又觉得到了合适的年龄没有恋爱的女儿有些可怜。于是某一天他让织女和一个放牛的青年结婚了。"
    me01 "在那之后，织女和那位放牛的青年就生活在了一起。"
    pause 1.0 hard
    scene set only lisite_cg happy
    with dissolve
    play voice "voice/天使雷亚/0001690.ogg"
    lst "可喜可贺可喜可贺~"
    me01 "后面还有呢。"
    play voice "voice/天使雷亚/0001700.ogg"
    lst "牛郎星还没出场吗？"
    me01 "刚刚说到放牛的青年就是牛郎。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0001710.ogg"
    lst "这样啊......"
    pause 0.5 hard
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    me01 "织女和牛郎结婚以后，过着幸福美满的生活。"
    me01 "但是织女她也因此疏忽了织布的天职。"
    me01 "虽然天帝看在他们新婚的面子上再三容忍，但最终还是生气了。"
    me01 "织女被带回了银河。"
    me01 "从此天帝让她再此专心织布。"
    me01 "并告诉她如果她认真工作，就允许每年的七夕那天和牛郎见面。"
    pause 0.5 hard
    scene set only lisite_cg happy
    with dissolve
    play voice "voice/天使雷亚/0001720.ogg"
    lst "可喜可贺可喜可贺~"
    me01 "就这么结束的话怎么能算是可喜可贺啊。"
    play voice "voice/天使雷亚/0001730.ogg"
    lst "每年能见一次不就行了吗？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001740.ogg"
    lst "我都不知道已经等了几年了......"
    me01 "等谁？"
    play voice "voice/天使雷亚/0001750.ogg"
    lst "等你。"
    me01 "为什么？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0001760.ogg"
    lst "不知道。"
    "我摸了摸后脑勺。"
    me01 "那我继续了。"
    pause 0.1 hard
    scene set only lisite_cg happy
    with dissolve
    play voice "voice/天使雷亚/0001770.ogg"
    lst "嗯。"
    pause 0.5 hard
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    me01 "和牛郎分开的织女为了能和心爱的人见面努力地织布。"
    me01 "他们两人都在焦急地等待着七夕的到来。"
    me01 "然而不幸的是，七夕当天银河却突发洪水，织女和牛郎只能隔岸相望。"
    pause 0.5 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 1.75 alpha 1
    pause 3.0 hard
    "自从和翔子分开以后，我一直将“与她的重逢”作为自己前进的动力。"
    "喜欢上星星也是从那时候开始的。"
    pause 0.5 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001780.ogg"
    lst "下雨的话，织女和牛郎就不能见面了。"
    me01 "总会有办法的。"
    me01 "不忍心目睹两人伤心的喜鹊们飞了过来。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0001790.ogg"
    lst "喜鹊？"
    me01 "是一种雀形目鸦科的鸟类。"
    play voice "voice/天使雷亚/0001800.ogg"
    lst "听起来像是种很小的鸟。"
    me01 "正因如此一般都是成群结队活动的。"
    me01 "它们张开翅膀彼此相连，在银河上架起了一座桥。于是织女终于来到了牛郎的身边。"
    play voice "voice/天使雷亚/0001810.ogg"
    lst "可喜可贺可喜可贺？"
    me01 "可喜可贺可喜可贺~"
    me01 "怎么样，有趣吗？"
    pause 0.1 hard
    scene set only lisite_cg normal 
    with dissolve
    play voice "voice/天使雷亚/0001820.ogg"
    lst "很普通。"
    me01 "虽然不是第一次问你了，雷亚也喜欢星星对吧？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0001830.ogg"
    lst "为什么问这个？"
    me01 "因为你只会在看得见星星的夜晚才来这里。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001840.ogg"
    lst "......"
    me01 "你之前说过在这里等我，究竟是为了什么？"
    "雷亚没有回答，只是目不转睛地看着我。"
    $ flcam.move(1500, -1800, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0001850.ogg"
    lst "愿你的喜鹊......"
    play voice "voice/天使雷亚/0001860.ogg"
    lst "总有一天也会出现在你的面前。"
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    with dissolve
    pause 1.0 hard
    "雷亚缓缓走到我的跟前。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/天使雷亚/0001870.ogg"
    lst "稍微闭一下眼睛。"
    me01 "为什么？"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0001880.ogg"
    lst "不为什么。"
    me01 "总觉得有点可怕啊。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0001890.ogg"
    lst "不可怕的。"
    me01 "真可疑。"
    show ts_lst_ssz_b1 b1 b1_a1
    play voice "voice/天使雷亚/0001900.ogg"
    lst "快一点，你连姐姐的话都不听了吗！"
    me01 "我、我知道了。"
    pause 0.5 hard
    play music first_22 fadein 3.0 if_changed
    scene black
    with side2cent
    pause 1.0 hard
    play voice "voice/天使雷亚/0001910.ogg"
    lst "还不可以睁开眼睛哦。"
    play voice "voice/天使雷亚/0001920.ogg"
    lst "睁开的话，就绝交......"
    "究竟是为什么呢。"
    "眼前的光景再次与记忆重合了。"
    "虽然我基本上能够确信雷亚和观景台的“她”并不是同一个人。"
    "因为真正的翔子我已经见过面了的。"
    "但是啊。"
    "即便是这样没错，我还是把她当成了对我而言最重要的伙伴之一。"
    "对于雷亚是不是“她”这一点，对我早已经不是那么重要了。"
    stop music fadeout 5.0
    $ set_replay_scene("label4_1")
    play voice "voice/天使雷亚/0001930.ogg"
    lst "谢谢你，凉君——"
    pause 1.0 hard
    play sound hite_1
    show hite_1 onlayer m2
    pause 2.0 hard
    "随之而来的是一种不可思议的感觉。"
    "从胸口传来像是亲吻在额头一般温柔的触感。"
    "我缓缓睁开了眼睛。"
    "即使没有她的允许，我还是充满好奇地睁眼了。"
    pause 1.0 hard
    scene white
    with in2out_v2_slow
    pause 2.0 hard
    play music first_28 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg cut1
    with slowerdissolve
    pause 2.0 hard    
    play voice "voice/天使雷亚/0001940.ogg"
    lst "可以的话，我本不想在你记起噩梦的时候做这种事的。"
    play voice "voice/天使雷亚/0001960.ogg"
    lst "可你的噩梦却一直在膨胀。"
    $ flcam.move(-2800, 1500, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "我低下头。"
    "雷亚手中那把巨大的镰刀，此刻正嵌在我的胸膛之中。"
    "已经没有闲暇去思考什么罪恶感了，留给我的只有纯粹的惊愕与恐惧。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "虽然我想要发出声音，但此刻我的舌头和喉咙都麻痹了。"
    "连疼痛也感觉不到。"
    play voice "voice/天使雷亚/0001970.ogg"
    lst "这样一来，你的噩梦就被割去了。"
    pause 1.0 hard
    scene set only xz_memory piecefour yinghua
    with dissolve
    "我想起来了，闭眼时感受到的那种温暖的感觉，就跟回忆中的场景十分类似。"
    "明明应该为分别而悲伤我，却因为没有来得及理解其中的感情而体会不到丝毫的痛苦。"
    "就和当年在这里与“她”许下再会的约定时一样。"
    "那是只属于我和***的约定。"
    me01 "......诶？"
    pause 0.5 hard
    scene set only lisite_cg cut1
    with dissolve
    "此刻我察觉到了异样。"
    "就像是第一次走进百货大楼迷路的孩子一样，眼前不知何时变成了陌生的街道，心里充满了迷惘和恐惧的感觉。"
    "刚刚在我身上发生了什么？"
    "虽然在脑海里拼命地想要抓住些什么，但却无法真正意识到那东西的存在。"
    pause 0.1 hard
    scene set only lisite_cg cut2
    with dissolve
    $ flcam.move(-1400, -1500, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0001980.ogg"
    lst "不是已经说过很多次了吗。"
    "惊愕的我此时才注意到从雷亚脸颊上滑落的泪珠。"
    "明明现在被刺的人是我，可是为什么哭泣的却是对方呢？"
    play voice "voice/天使雷亚/0001990.ogg"
    lst "我说过的，我是收割噩梦的死神。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_memory piecefour yinghua
    with dissolve
    pause 0.5 hard
    "随着她那比夜空中的星辰还要闪耀的泪水滴落之际，我脑海里拼命想要抓住的东西消失了。"
    pause 1.0 hard
    scene set only xz_memory piecethree yinghua
    with slowdissolve
    pause 0.5 hard
    play voice "voice/天使雷亚/0002000.ogg"
    lst "因为这个我才一直在这里等你。"
    pause 1.0 hard
    scene set only xz_memory pieceone yinghua
    with slowdissolve
    pause 0.5 hard
    "完全，消失了——"
    pause 1.0 hard
    scene set only xz_memory piecezero yinghua
    with slowdissolve
    pause 0.5 hard
    "那明明是非常重要的东西。"
    "对我而言***明明是非常重要的人。"
    "这样一来就不能和***再会了。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(-1400, -1500, 600)
    scene set only lisite_cg cut2
    with dissolve
    pause 0.5 hard
    me01 "怎么会这样......"
    play music first_24 fadein 3.0 if_changed
    pause 0.1 hard
    scene set only lisite_cg cut3
    with dissolve
    $ flcam.move(-2800, -3000, 900, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0002010.ogg"
    lst "呜......"
    "我是喜欢***的。"
    "***是我第一个朋友。"
    "即便是和***分开了，我也没有忘记。"
    "为了***去学习关于她最喜欢的、星空的知识。"
    "为了在和***见面的时候能够亲口讲给她听。"
    "为了和***永远在一起的。"
    play voice "voice/天使雷亚/0002020.ogg"
    lst "快停下......请不要再想起来了。"
    play voice "voice/天使雷亚/0002030.ogg"
    lst "会痛苦的，快停下！"
    "明白了。"
    "我忘记了。"
    "我把和***一起的回忆弄丢了。"
    "明明刚刚还记得的。"
    "这样就真的无法再见了。"
    "遗失了最重要的东西——与***的约定，就再也无法与她相遇了。"
    me01 "求求你了......"
    "不要这样。"
    "我和她的约定。"
    "为了实现它我不是能忘记的。"
    me01 "还给我。"
    "那无论何时，都被我当做天职来擦拭的、最重要的回忆。"
    me01 "求求你，快还给我啊！"
    me01 "关于那个女孩的记忆，还给我啊！"
    play voice "voice/天使雷亚/0002040.ogg"
    lst "不要......"
    pause 0.1 hard
    scene set only lisite_cg cut2
    with dissolve
    play voice "voice/天使雷亚/0002050.ogg"
    lst "因为，我是死神......"
    play voice "voice/天使雷亚/0002060.ogg"
    lst "我是割取噩梦的死神......"
    me01 "你想说这一切就是我的噩梦吗？"
    play voice "voice/天使雷亚/0002070.ogg"
    lst "是这样的。"
    play voice "voice/天使雷亚/0002080.ogg"
    lst "因为你刚才忘记了，所以就是这样没错的。"
    scene set only lisite_cg cut4
    play voice "voice/天使雷亚/0002090.ogg"
    lst "太好了呢......"
    "即使早已满是泪水，但雷亚还是笑了。"
    play voice "voice/天使雷亚/0002100.ogg"
    lst "这样，就再也不会为噩梦而烦恼了。"
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 2.5 alpha 1
    pause 3.0 hard
    scene set only sky night yinghua3
    $ flcam.move(0, 8500, 400)
    $ flcam.move(0, 0, 400, duration=30.0, warper='ease_quad')
    with dissolve
    pause 0.5 hard
    nvl clear
    pcenter "  蔓延到天空尽头的七夕之星。"
    nvl clear
    pcenter "  被多得可怕的光芒萦绕着，织女和牛郎隔岸相望。"
    nvl clear
    play voice "voice/天使雷亚/0002110.ogg"
    pcenter "  真的，太好了~"
    nvl clear
    play voice "voice/天使雷亚/0002120.ogg"
    pcenter "  凉君。"
    nvl clear
    pcenter "  在撕心裂肺的哭泣声中。"
    nvl clear
    pcenter "  天空中的两颗星，消失在了浩瀚的天际——"
    nvl clear
    pause 3.0 hard
    stop music fadeout 5.0
    $ flcam.move(0, 0, 0)
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ end_replay()
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day08
