label day13:
    bookmark
    $ save_name = _("Day 13")
    pause 4.0 hard
    scene set only backend_yinghua winter
    with dissolve
    show backend_bg04 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date12 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only hospital day room yinghua
    with dissolve
    pause 1.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0141350.ogg"
    rxl "你好，梦同学~"
    play music first_06 fadein 3.0 if_changed
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    show xz_dzf_b1 b1 b1_ga3 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533950.ogg"
    lingyin "放学以后就来探望你了哟~"
    play voice "voice/翔子/0232640.ogg"
    xz "这么多人一起来真是抱歉。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_cg hsp normal
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0609640.ogg"
    yume "嗯。谢谢你们。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    $ flcam.move(-750, -1000, 300, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0609650.ogg"
    yume "欢迎大家~"
    "自从被禁止探望以后，梦默许了由伙伴们代替我来探望的提议。"
    "于是便有了今天的这一出。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0609660.ogg"
    yume "请转告凉君，我的身体状况跟平时一样。"
    play voice "voice/翔子/0609670.ogg"
    yume "让他不用太过担心了。"
    play voice "voice/翔子/0609690.ogg"
    yume "昨天的凉君还是那么地可爱温顺。"
    play voice "voice/翔子/0609700.ogg"
    yume "我是不会忘记的。嗯，绝对不会忘记的。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0609710.ogg"
    yume "所以今后也会好好地珍惜的，毕竟{rb}这{/rb}{rt}回忆{/rt}是我的宝物呢~"
    pause 1.0 hard
    scene set only hospital day room yinghua
    with dissolve
    pause 1.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0141380.ogg"
    rxl "越来越在意昨天到底发生了什么......"
    hide rxl_dzf_b3
    $ flcam.move(2250, -500, 1200, duration=1.5)
    pause 0.5 hard
    show yume_sy_b2 b2 b2_sp1 onlayer screens at side_right('yume', 0.90), basicfade
    play voice "voice/翔子/0609720.ogg"
    yume "凉君，还没有和大家说吗？"
    hide yume_sy_b2
    show yume_sy_b1 b1 b1_n1 onlayer screens at side_right('yume'), basicfade
    play voice "voice/翔子/0609730.ogg"
    yume "如果大家很在意的话就由我来替他说吧。凉君他呢，昨天在我的胸口哭得像个小孩子一样。"
    hide yume_sy_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0141390.ogg"
    rxl "胸口......"
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_ga2 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533980.ogg"
    lingyin "神野同学在学校外的行为还真是大胆啊。"
    hide rxl_dzf_b1
    show rxl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0141400.ogg"
    rxl "胸......我输了。"
    hide rxl_dzf_b3
    hide lingyin_dzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_a2 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0232700.ogg"
    xz "......笨蛋凉！"
    "在大家的欢声笑语中，女孩再一次体会到了原本早已告别了的学校生活。"
    "果然学校什么的，还是讨厌不起来啊。"
    "女孩这样想着。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only hospital night outside
    with dissolve
    pause 2.0 hard
    play music first_25 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0533860.ogg"
    lingyin "正门有上锁，恐怕是不能从那里潜入的。"
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0141230.ogg"
    rxl "后面有备用门吧？"
    show lingyin_dzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0533870.ogg"
    lingyin "是的。那或许是这个时间段唯一能进出医院的地方了。"
    hide lingyin_dzf_b2
    hide rxl_dzf_b2
    $ flcam.move(0, -500, 1100, duration=1.5)
    pause 0.5 hard
    "梦所在的西区大楼并没有在夜间开放。"
    "想要见到她的话就必须从中央大楼的后门进入。"
    "这些都是从铃音那里获取到的情报，多亏之前拜托过她们帮忙调查医院的一些事情。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0533880.ogg"
    lingyin "护士的巡逻时间，也从父亲那里打听到了~"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0141240.ogg"
    rxl "巡逻最松懈的时候，就是现在了吧。"
    hide lingyin_dzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0141250.ogg"
    rxl "从万夜花小姐那里借来了摩托车，之后就只剩把梦带出来了。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0141260.ogg"
    rxl "会来的，绝对。"
    show rxl_dzf_b1 b1 b1_s2
    play voice "voice/日向怜/0141270.ogg"
    rxl "因为我觉得，梦同学肯定也是想见小凉你的。"
    show rxl_dzf_b1 b1 b1_n3
    play voice "voice/日向怜/0141280.ogg"
    rxl "她一定也不想和小凉你分开的。"
    me01 "......谢谢你，日向同学。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 1.0 hard
    "啊啊，果然我还是不想就这么放弃。"
    "这七年间我一直在思考着、犹豫着。"
    "而就在今晚，我要做个了断。"
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900)
    scene set only hospital night outside
    show xz_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.3
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/0232550.ogg"
    xz "......真是让人看不下去，为什么最危险的工作要让我来做啊。"
    show xz_dzf_b2 b2 b2_s1
    play voice "voice/翔子/0232560.ogg"
    xz "我明明是最反对这个计划的。"
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0141290.ogg"
    rxl "毕竟之前还说了“没有常识”这样的话呢。"
    show xz_dzf_b2 b2 b2_a1
    play voice "voice/翔子/0232570.ogg"
    xz "说到底为什么是由我来做啊。"
    show lingyin_dzf_b2 b2 b2_ga3
    play voice "voice/青木铃音/0533900.ogg"
    lingyin "我们只不过是因才施用而已。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0141300.ogg"
    rxl "因为小翔你对医院的地形很熟悉嘛。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0232580.ogg"
    xz "如果是因为这一点的话让铃音去也是一样的吧。"
    show lingyin_dzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0533910.ogg"
    lingyin "毕竟要需要考虑到能够应付危急关头的优秀运动神经呢~"
    show xz_dzf_b1 b1 b1_ga1
    play voice "voice/翔子/0232590.ogg"
    xz "你难道是要我在护士阻拦的时候放倒她们吗，真是的......"
    hide lingyin_dzf_b2
    hide rxl_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "......翔子。"
    stop music fadeout 5.0
    show xz_dzf_b1 b1 b1_n2
    me01 "谢谢你，这次多亏了你计划才能顺利进行。"
    me01 "虽然这其中有着非常复杂的缘由，但总有一天我一定会向你解释清楚的。"
    "面对我的道谢，翔子无奈地耸了耸肩。"
    show xz_dzf_b1 b1 b1_n3
    play voice "voice/翔子/0232600.ogg"
    xz "人我帮你带过来了，你看。"
    hide xz_dzf_b1
    $ flcam.move(4500, -300, 900, duration=2.0)
    pause 1.0 hard
    show yume_sf_b1 b1 b1_n2 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/翔子/0607290.ogg"
    yume "......"
    play music first_42 fadein 3.0 if_changed
    $ flcam.move(4500, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607320.ogg"
    yume "凉君。"
    me01 "这么突然地把你带出来真是抱歉。"
    show yume_sf_b2 b2 b2_s2
    play voice "voice/翔子/0607370.ogg"
    yume "所以一路上我就在想会不会是为了一些奇怪的事情之类的。"
    show yume_sf_b2 b2 b2_n2
    play voice "voice/翔子/0607350.ogg"
    yume "因为这个时间穿睡衣出门会很冷，所以我就顺便换上便装了。"
    show yume_sf_b2 b2 b2_s2
    play voice "voice/翔子/0607330.ogg"
    yume "怎么样，这件衣服。"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607340.ogg"
    yume "不会觉得奇怪吧？"
    me01 "一点都不奇怪。"
    me01 "怎么看都是女孩子该有的装束。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_s4 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607390.ogg"
    yume "竟然把我当小孩子......"
    me01 "不是那样的。"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607400.ogg"
    yume "虽然你说得我很普通，但我还是很开心的。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607410.ogg"
    yume "所以你想把我怎么样？"
    me01 "我想带你去一个地方。"
    show yume_sf_b2 b2 b2_sp1
    play voice "voice/翔子/0607420.ogg"
    yume "去哪里？"
    me01 "暂时保密。"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607430.ogg"
    yume "如果被人发现的话，肯定会挨骂的哟。"
    me01 "那时候就由我来承担后果。"
    show yume_sf_b1 b1 b1_n1
    play voice "voice/翔子/0607440.ogg"
    yume "拜托你了呢~"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607450.ogg"
    yume "晚上溜出来什么的还是第一次，有点紧张啊。"
    show yume_sf_b2 b2 b2_h1
    play voice "voice/翔子/0607460.ogg"
    yume "特别是绕过站岗护士的时候，为了不被发现而大步向前冲的感觉真是太爽了~"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607470.ogg"
    yume "更何况即使事情败露了，还有凉君来替我挨骂。"
    show yume_sf_b1 b1 b1_h1
    play voice "voice/翔子/0607480.ogg"
    yume "到时候我就说是这个人把我劫走的，之类的~"
    me01 "你还真是一点情面都不给我留啊......"
    pause 1.0 hard
    hide yume_sf_b1
    play sound moto
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0141320.ogg"
    rxl "小凉，摩托的引擎已经发动了。"
    hide rxl_dzf_b1
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    show xz_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0533930.ogg"
    lingyin "给，头盔。"
    play voice "voice/翔子/0232620.ogg"
    xz "载人这点我先不追究了，不过记得要控制好速度。这本就是一辆破车来着。"
    hide lingyin_dzf_b2
    hide xz_dzf_b1
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show moto onlayer b2 at basicfade_c2u
    "之前帮万夜花小姐推车的时候怎么也不会想到。"
    "有朝一日会需要它的帮忙。"
    hide moto
    pause 1.0 hard
    $ flcam.move(3800, -200, 600, duration=1.5)
    pause 0.5 hard
    show yume_sf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.65
    "我带上头盔，接着把另一只递给了梦。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.65
    play voice "voice/翔子/0607490.ogg"
    yume "摩托......你会开吗？"
    me01 "嗯。"
    show yume_sf_b2 b2 b2_s4
    play voice "voice/翔子/0607500.ogg"
    yume "我还没有坐过。"
    play voice "voice/翔子/0607510.ogg"
    yume "......"
    me01 "车有点小，只能委屈你坐在后面的货架上了。但只要抓紧我的话就没问题的。"
    show yume_sf_b2 b2 b2_n2
    play voice "voice/翔子/0607520.ogg"
    yume "......明明我才是姐姐的说。"
    $ flcam.move(3800, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "还有这个。"
    "我把自己的外套也递给了她。"
    show yume_sf_b2 b2 b2_sp1
    play voice "voice/翔子/0607530.ogg"
    yume "这是......干什么？"
    me01 "路上会很冷的，穿上吧。"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_n2 onlayer m2:
        xpos 0.65
    play voice "voice/翔子/0607540.ogg"
    yume "不用了，凉君也会冷的吧。"
    me01 "我没事的。"
    show yume_sf_b1 b1 b1_a1
    play voice "voice/翔子/0607550.ogg"
    yume "不行。"
    me01 "听我的话，先穿上吧。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_a1 onlayer m2:
        xpos 0.65
    play voice "voice/翔子/0607560.ogg"
    yume "不行的啦，我才是姐姐的说！"
    me01 "我是男孩子所以不要紧，这次无论如何也不会妥协的。"
    show yume_sf_b2 b2 b2_s4
    play voice "voice/翔子/0607570.ogg"
    yume "......刚刚，胸口一紧。"
    show yume_sf_b2 b2 b2_s1
    play voice "voice/翔子/0607580.ogg"
    yume "不要以为这样子就赢了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 2.0 hard
    scene set only hospital night outside
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    show lingyin_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0232630.ogg"
    xz "回来的时候记得提前联系。我们会在附近的咖啡厅等你们的。"
    play voice "voice/青木铃音/0533940.ogg"
    lingyin "毕竟还得把梦同学带回病房呢。"
    play voice "voice/日向怜/0141330.ogg"
    rxl "路上小心。"
    pause 1.0 hard
    $ flcam.move(0, -200, 600)
    scene set only hospital night outside
    show yume_sf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    me01 "你怎么还没把外套穿上啊......"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607590.ogg"
    yume "我才不要输给凉君你呢。"
    me01 "这是什么奇怪的对抗心理啊？！"
    show yume_sf_b2 b2 b2_n1
    play voice "voice/翔子/0607600.ogg"
    yume "姐姐我来给你穿上哟~"
    "接着她把外套披在了我的身上。"
    "自己也顺势贴了上去。"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607610.ogg"
    yume "稍微有点挤啊。"
    me01 "马上就到了，在此之前就先忍耐一会儿吧。"
    show yume_sf_b1 b1 b1_s1
    play voice "voice/翔子/0607620.ogg"
    yume "好像真的会掉下去的样子。"
    me01 "放心好了，害怕的话就抱紧我。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607630.ogg"
    yume "......"
    me01 "怎么了？"
    show yume_sf_b2 b2 b2_s1
    play voice "voice/翔子/0607640.ogg"
    yume "这样一来不就得和凉君靠在一起了吗......"
    show yume_sf_b2 b2 b2_s2
    play voice "voice/翔子/0607650.ogg"
    yume "虽然并不是讨厌......的意思。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    "她慢慢地靠近了。"
    "背上传来了柔软的触感。"
    show yume_sf_b1 b1 b1_s2
    play voice "voice/翔子/0607660.ogg"
    yume "好像......还是会掉下去。"
    me01 "要出发了，抓稳了。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607670.ogg"
    yume "......就算你这么说。"
    "在车发动的那一刹那，由于后坐力的关系梦直接靠在了我的背上。"
    show yume_sf_b2 b2 b2_s2
    play voice "voice/翔子/0607680.ogg"
    yume "能抓的地方也只有这里了。"
    me01 "稍微暖和些了吗？"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607690.ogg"
    yume "嗯。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607730.ogg"
    yume "果然，是不需要外套的。"
    show yume_sf_b2 b2 b2_s4
    play voice "voice/翔子/0607740.ogg"
    yume "因为身子已经变得，非常温暖了......"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    play music first_29 fadein 3.0 if_changed
    scene set only street night yinghua
    with dissolve
    pause 2.0 hard
    scene set only starview night guardrail
    with right2left
    pause 2.0 hard
    "穿过街区和公路，我们来到了坡道尽头。"
    "我松开油门，把摩托车停了下来。"
    "引擎熄火后，周围立刻陷入了一片寂静之中。"
    me01 "到了，下来吧。"
    play voice "voice/翔子/0607750.ogg"
    yume "......"
    me01 "翔子？"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yume_sf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607760.ogg"
    yume "啊，什么？"
    me01 "身体不舒服吗？"
    show yume_sf_b1 b1 b1_s2
    play voice "voice/翔子/0607770.ogg"
    yume "不、不是的，因为我一直闭着眼的关系。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607780.ogg"
    yume "我们到了吗？"
    me01 "还有一点路程，不过摩托车只能骑到这里了。"
    show yume_sf_b2 b2 b2_s1
    play voice "voice/翔子/0607800.ogg"
    yume "......"
    "听了我的话她并没有松开手，而是不停地向四周环顾着。"
    me01 "那个......"
    show yume_sf_b2 b2 b2_n2
    play voice "voice/翔子/0607830.ogg"
    yume "......别以为这样就算赢了。"
    me01 "所以说从刚才开始到底在进行什么样的较量啊？！"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607850.ogg"
    yume "这里吗......嗯，我一开始就猜到了。"
    play voice "voice/翔子/0607860.ogg"
    yume "即使闭着眼睛，我也能感觉到是在朝着这里前进。"
    me01 "在铁丝网的后面，就是观景台了。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607870.ogg"
    yume "但是上面写着禁止进入，真的能进去吗？"
    me01 "嗯。得稍微绕下路。"
    "我向她伸出了手。"
    me01 "在到达之前都要跟紧我。"
    show yume_sf_b2 b2 b2_sp1 
    play voice "voice/翔子/0607880.ogg"
    yume "......要牵着手吗？"
    me01 "不行吗。"
    hide yume_sf_b2
    show yume_sf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607890.ogg"
    yume "......"
    show yume_sf_b1 b1 b1_n2
    play voice "voice/翔子/0607900.ogg"
    yume "只有这一次哟......"
    play voice "voice/翔子/0607910.ogg"
    yume "作为姐姐只能稍稍让步一次。"
    hide yume_sf_b1
    show yume_sf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607920.ogg"
    yume "带路的任务，就交给凉君你了。"
    pause 1.0 hard
    play ambience1 move_1
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 2.0 hard
    "一路上我都会用手挡开那些可能会伤到人的树枝，避免身后的翔子受伤。"
    "在黑暗中，我们牵着手朝着观景台的方向前进。"
    "是啊。"
    "就是这样的。"
    "冰冷潮湿的泥土散发着大自然的味道。"
    "就算过去了那么久，这里的一切还是没有改变。"
    "依然如回忆里那般亲切。"
    "时隔七年，我们又一次踏足了这里。"
    pause 2.0 hard
    stop music fadeout 5.0
    stop ambience1
    scene white
    with slowdissolve
    pause 2.0 hard
    $ set_replay_scene("label2_3")
    $ flcam.move(-3800, -200, 600)
    scene set only starview night starview
    with dissolve
    $ flcam.move(3800, -300, 900, duration=8.0, warper='ease_cubic')
    play music first_40 fadein 3.0 if_changed
    pause 5.0 hard
    play voice "voice/翔子/0607930.ogg"
    yume "没有改变......"
    play voice "voice/翔子/0607940.ogg"
    yume "没有改变啊，凉君。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_cg gjt surprise
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0607950.ogg"
    yume "夏日的星空也是，现在这片冬日的星空也是。"
    play voice "voice/翔子/0607960.ogg"
    yume "一点都没有改变，依旧那么美丽。"
    play voice "voice/翔子/0607970.ogg"
    yume "就像小时候一样，就像回忆中的一样。"
    play voice "voice/翔子/0607980.ogg"
    yume "明明我们都已经改变这么多了......"
    pause 0.1 hard
    scene set only xz_cg gjt normal
    with dissolve
    play voice "voice/翔子/0607990.ogg"
    yume "真是奇怪啊。"
    play voice "voice/翔子/0608000.ogg"
    yume "真是羡慕啊。"
    play voice "voice/翔子/0608010.ogg"
    yume "好羡慕樱华镇的星空啊。"
    pause 0.1 hard
    scene set only xz_cg gjt daze
    with dissolve
    $ flcam.move(750, -1500, 600, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0608020.ogg"
    yume "谢谢你，凉君。"
    play voice "voice/翔子/0608030.ogg"
    yume "我不会忘记今晚发生的一切。"
    play voice "voice/翔子/0608040.ogg"
    yume "绝对不会忘记。"
    play voice "voice/翔子/0608070.ogg"
    yume "所以，谢谢你。"
    play voice "voice/翔子/0608080.ogg"
    yume "谢谢你留给了我这样的回忆。"
    me01 "还没结束呢。"
    pause 0.1 hard
    scene set only xz_cg gjt surprise2
    with dissolve
    me01 "现在说谢谢的话还太早了。"
    me01 "我还没有教给你关于星星的知识呢。"
    me01 "我们都长大了。"
    me01 "比起回忆中的我们，现在更加接近这片星空了。"
    play voice "voice/翔子/0608090.ogg"
    yume "凉君......"
    me01 "所以，再稍微陪我一会儿。"
    me01 "听我讲完那关于七夕的故事吧——"
    pause 2.0 hard
    scene white
    with slowdissolve
    pause 2.0 hard
    "南天的猎户座，东天的双子座，以及头顶的御夫座都在闪耀着。"
    "随着天河的流动，织女星和牛郎星走下了舞台。"
    "一边期待着再会的时刻，一边履行着自己的天职。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    me01 "很久以前，在天河的河畔，天帝的女儿——被称为织女的美丽女子就住在那里。"
    me01 "织女遵守着天帝的指示，每天每天都很努力地织出一匹又一匹闪耀着五彩光辉的美丽织锦。"
    me01 "天帝虽然对织女的辛勤劳动感到很满意，但是考虑到这个年纪的她连恋爱的时间都没有实在觉得可怜。于是某天就让她与一名叫做牛郎的青年结婚了。"
    pause 1.0 hard
    scene set only xz_cg gjt daze
    with dissolve
    pause 2.0 hard
    play voice "voice/翔子/0608100.ogg"
    yume "可喜可贺可喜可贺。"
    me01 "......等等。"
    play voice "voice/翔子/0608110.ogg"
    yume "七夕的传说我还是知道的。"
    me01 "即使如此也还请听我把它说完，拜托了。"
    play voice "voice/翔子/0608130.ogg"
    yume "因为这是凉君的愿望？"
    me01 "嗯。"
    pause 0.1 hard
    scene set only xz_cg gjt daze
    with dissolve
    play voice "voice/翔子/0608180.ogg"
    yume "真是强硬啊，凉君~"
    pause 1.0 hard
    scene set only sky night yinghua
    with dissolve
    pause 2.0 hard
    me01 "织女和牛郎结婚以后，幸福地生活在一起。"
    me01 "但两人很快便沉浸在婚姻的幸福生活中，连本属于自己的天职也忘记了。"
    me01 "渐渐地天帝也开始恼火起来，最后将牛郎从织女的身边带走了。"
    me01 "并告诉他们只要好好地工作，就允许他们在每年的七夕见上一次面。"
    pause 1.0 hard
    scene set only xz_cg gjt daze
    with dissolve
    pause 2.0 hard
    play voice "voice/翔子/0608190.ogg"
    yume "可喜可贺可喜可贺。"
    me01 "......所以说等等啊。"
    pause 0.1 hard
    scene set only xz_cg gjt normal
    with dissolve
    play voice "voice/翔子/0608200.ogg"
    yume "每年能见一次面的话不是很好吗？"
    play voice "voice/翔子/0608210.ogg"
    yume "我明明都一直等了那么多年。"
    me01 "等谁？"
    play voice "voice/翔子/0608220.ogg"
    yume "不是凉君哟。嗯，不是凉君。"
    me01 "这一点还不肯承认吗。"
    play voice "voice/翔子/0608230.ogg"
    yume "不管问多少次我都会这么说的。直到凉君认输为止。"
    me01 "所以说这莫名的对抗心里到底是怎么回事啊。"
    pause 1.0 hard
    scene set only sky night yinghua
    with dissolve
    pause 2.0 hard
    me01 "和牛郎分隔两地的织女，为了一年一度的再会开始努力地织布。"
    me01 "另一边的牛郎也把与织女的约定藏在心里，每日辛勤劳作着。两人都在焦急地等待着重逢之日的到来。"
    me01 "不幸的是，在七夕那天却下起了倾盆大雨，织女因为天河洪水泛滥的缘故无法来到牛郎的身边。"
    me01 "两人隔河相望、痛心疾首。"
    show yume_sf_b1 b1 b1_n1 onlayer screens at side_right('yume'), basicfade
    play voice "voice/翔子/0608260.ogg"
    yume "就在这时，不忍心看着两人分开的喜鹊就来帮忙了吧。"
    hide yume_sf_b1
    me01 "没错。喜鹊们成群结队地飞了过来了。"
    me01 "它们张开翅膀彼此相连，架起了一座天桥，帮助织女到达了牛郎所在的彼岸。"
    show yume_sf_b1 b1 b1_h1 onlayer screens at side_right('yume'), basicfade
    play voice "voice/翔子/0608270.ogg"
    yume "这次终于可喜可贺可喜可贺了吧~"
    hide yume_sf_b1
    me01 "不对。"
    pause 1.0 hard
    scene set only xz_cg gjt surprise2
    with dissolve
    pause 2.0 hard
    play voice "voice/翔子/0608280.ogg"
    yume "......还没有结束吗？"
    me01 "嗯。"
    play voice "voice/翔子/0608290.ogg"
    yume "但是七夕传说......"
    me01 "还有后续的。"
    me01 "真正的七夕传说，还没有结束。"
    me01 "牛郎和织女，是有孩子的。"
    pause 1.0 hard
    scene set only sky night yinghua
    with dissolve
    pause 2.0 hard
    me01 "结为夫妻的两人，拥有了一男一女两个孩子。"
    me01 "但是由于天帝的命令，两人不得不继续分隔两岸。为此孩子们也必须接受离别的痛苦。"
    me01 "原本两个人的思念，此刻已然成为了四个人共同的思念。"
    me01 "七夕并不仅仅是织女和牛郎再会的约定之日。"
    me01 "更是家人团聚的日子。"
    me01 "是和自己重要之人一起，度过幸福生活的日子。"
    "在夏日夜空中的织女——天琴座的织女星，和其他两颗四等星形成了一个三角。"
    "那两颗四等星，在牛郎——天鹰座的牛郎星旁如同在陪伴着它似的散发着光芒。"
    "这就是七夕的孩子，织女和牛郎的子星与女儿星。"
    pause 1.0 hard
    $ flcam.move(750, -1500, 600)
    scene set only xz_cg gjt surprise2
    with dissolve
    pause 2.0 hard
    play voice "voice/翔子/0608320.ogg"
    yume "是这样啊......"
    pause 0.1 hard
    scene set only xz_cg gjt normal
    with dissolve
    play voice "voice/翔子/0608330.ogg"
    yume "织女星和牛郎星，是有孩子的啊。"
    play voice "voice/翔子/0608340.ogg"
    yume "是有，家人的啊。"
    play voice "voice/翔子/0608350.ogg"
    yume "结婚以后。"
    pause 0.1 hard
    scene set only xz_cg gjt daze
    with dissolve
    play voice "voice/翔子/0608360.ogg"
    yume "又有了新的家人了吗......"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0608380.ogg"
    yume "在凉君搬家的前一天，也就是七夕的时候。"
    play voice "voice/翔子/0608390.ogg"
    yume "我也想过和你的再会。就像织女和牛郎一样，原本是这么希望的。"
    play voice "voice/翔子/0608400.ogg"
    yume "然后和约定的一样，和凉君结婚。"
    play voice "voice/翔子/0608410.ogg"
    yume "就像凉君所说的七夕传说那样，成为一家人的。"
    play voice "voice/翔子/0608420.ogg"
    yume "虽然那时的我，的确是这么想的。"
    play voice "voice/翔子/0608430.ogg"
    yume "但是，那天我许下的愿望却并非如此。"
    play voice "voice/翔子/0608440.ogg"
    yume "如果我的身体能好起来的话，就和凉君结婚。"
    play voice "voice/翔子/0608450.ogg"
    yume "如若不然，那一切就是不可能发生的。"
    play voice "voice/翔子/0608460.ogg"
    yume "我希望凉君是能忘记我的。"
    play voice "voice/翔子/0608470.ogg"
    yume "忘记我，然后和其他人一起开始新的生活。"
    play voice "voice/翔子/0608490.ogg"
    yume "这样一来，凉君也一定能获得幸福的。"
    pause 0.1 hard
    scene set only xz_cg gjt daze
    with dissolve
    play voice "voice/翔子/0608500.ogg"
    yume "这才是我的愿望。"
    play voice "voice/翔子/0608510.ogg"
    yume "这才是我对着流星许下的，真正的愿望......"
    pause 0.1 hard
    scene set only xz_cg gjt normal
    with dissolve
    play voice "voice/翔子/0608520.ogg"
    yume "我并不是放弃治疗了。"
    play voice "voice/翔子/0608530.ogg"
    yume "为此我才去了城市里的大医院。"
    play voice "voice/翔子/0608540.ogg"
    yume "就像是追赶在凉君身后一般。"
    play voice "voice/翔子/0608560.ogg"
    yume "然而我却没有选择去见你。"
    play voice "voice/翔子/0608570.ogg"
    yume "因为我不知道我的病情还有没有希望。"
    play voice "voice/翔子/0608580.ogg"
    yume "直到现在依旧如此。"
    play voice "voice/翔子/0608590.ogg"
    yume "所以呢......"
    pause 1.0 hard
    scene set only xz_cg gjt cry1
    with dissolve
    play voice "voice/翔子/0608600.ogg"
    yume "也许很快就不在的我，是不能和凉君再会的。"
    play voice "voice/翔子/0608610.ogg"
    yume "你本来是必须要忘记我的。"
    me01 "不是的。"
    play voice "voice/翔子/0608620.ogg"
    yume "没有什么不对的......"
    play voice "voice/翔子/0608630.ogg"
    yume "凉君还不是优等生。"
    play voice "voice/翔子/0608640.ogg"
    yume "又在勉强自己了。"
    play voice "voice/翔子/0608660.ogg"
    yume "过去的我，一直想被你当成姐姐那样来看待。"
    play voice "voice/翔子/0608670.ogg"
    yume "希望你能够对我有所依赖。"
    play voice "voice/翔子/0608690.ogg"
    yume "那时候的任性。"
    play voice "voice/翔子/0608700.ogg"
    yume "固执地想成为大姐姐的我。"
    play voice "voice/翔子/0608710.ogg"
    yume "现在回想起来还真是小孩子气啊。"
    play voice "voice/翔子/0608720.ogg"
    yume "但是我还是很珍惜那份回忆的，所以才一直将她铭记到现在。"
    play voice "voice/翔子/0608730.ogg"
    yume "为了能够教给凉君关于星星的知识，我也努力学习了。"
    play voice "voice/翔子/0608750.ogg"
    yume "这样我就能成为真正的大姐姐了。"
    me01 "这些都没有关系的！"
    me01 "不管是谁依赖谁都没有关系的。"
    me01 "不管是朋友还是恋人，也都没有关系。"
    me01 "疾病什么的我也不在乎......"
    pause 0.1 hard
    scene set only xz_cg gjt cry2
    with dissolve
    play voice "voice/翔子/0608760.ogg"
    yume "......"
    me01 "我只是想待在你的身边。"
    me01 "只要这样就足够了。"
    play voice "voice/翔子/0608770.ogg"
    yume "明明不用逞强，也可以的。"
    me01 "你知道吗翔子，其实今天是我的生日。"
    me01 "现在的我比过去，在年纪上要更接近翔子你。"
    me01 "所以不是大姐姐也可以的。"
    me01 "对我撒娇，稍微依赖下我也是可以的。"
    play voice "voice/翔子/0608810.ogg"
    yume "凉君......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 2.0 hard
    play voice "voice/翔子/0608820.ogg"
    yume "你果然，还是没有变。"
    play voice "voice/翔子/0608830.ogg"
    yume "还不是优等生。"
    play voice "voice/翔子/0608840.ogg"
    yume "明明必须要改变的。在这星空下得我们明明，是必须要改变的。"
    play voice "voice/翔子/0608860.ogg"
    yume "但是也只有你。"
    play voice "voice/翔子/0608870.ogg"
    yume "像这样一次也没有想要尝试改变。"
    pause 1.0 hard
    scene set only xz_cg gjt normal
    with dissolve
    pause 2.0 hard
    play voice "voice/翔子/0617420.ogg"
    yume "但是对不起。"
    play voice "voice/翔子/0617430.ogg"
    yume "不管凉君说有多喜欢我。"
    play voice "voice/翔子/0617440.ogg"
    yume "我也是不会喜欢上凉君的。"
    pause 0.1 hard
    scene set only xz_cg gjt cry2
    with dissolve
    play voice "voice/翔子/0617450.ogg"
    yume "不会和你交往的。"
    play voice "voice/翔子/0617460.ogg"
    yume "我们不会成为恋人的。"
    "眼前的轮廓逐渐变得模糊。"
    "泪水早已经挂在眼眶上了。"
    play voice "voice/翔子/0617470.ogg"
    yume "因为我相信，凉君是能够变成优等生的。"
    pause 0.1 hard
    scene set only xz_cg gjt cry1
    with dissolve
    $ flcam.move(750, -1000, 300, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0617480.ogg"
    yume "我的使命已经结束了。"
    play voice "voice/翔子/0617490.ogg"
    yume "以后还请对我以外的人撒娇吧。"
    play voice "voice/翔子/0617500.ogg"
    yume "凉君的话一定可以的。"
    "就如同伸出手也触碰不到的星辰一般。"
    "我和翔子之间隔着无尽的天河。"
    "到头来还是没能抓住吗......"
    pause 0.1 hard
    scene set only xz_cg gjt cry2
    with dissolve
    play voice "voice/翔子/0617510.ogg"
    yume "我先回去了。"
    play voice "voice/翔子/0617520.ogg"
    yume "回医院去了。"
    play voice "voice/翔子/0617530.ogg"
    yume "不要追过来哦。"
    play voice "voice/翔子/0617540.ogg"
    yume "如果敢从后面来个公主抱的话，我就咬你哦。"
    play voice "voice/翔子/0617550.ogg"
    yume "一个人回去这种程度的事我还是能做到的。"
    pause 1.0 hard
    $ end_replay()
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    play sound move_1
    pause 1.0 hard
    "看着她远去的背影。"
    "那步伐虽然很慢，却很坚定。"
    "无法阻止。"
    "我只能在原地目送她。"
    "和七年前一样。"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    "虽然不希望就这么结束了。"
    "但如果这个结果是她所希望的。"
    "那也只能放弃了。"
    "无法到达的。"
    "如同没有交点的平行线。"
    "我们之间隔着天河的话，是注定无法到达对岸的。"
    "失恋就是最好的答案了吧。"
    "放手也是理所当然的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    $ flcam.move(0, -300, 900, duration=1.5)
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/天使雷亚/0027760.ogg"
    lst "凉君真是......笨笨的。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 3.0 hard

label day13.hospital_event02:
    $ flcam.move(0, 0, 0)
    scene set only hospital night room yinghua
    with dissolve
    pause 1.0 hard
    play music first_27 fadein 3.0 if_changed
    "女孩独自坐在病床上。"
    "像是在忍耐着什么。"
    "原本睡前的习惯，是去看一眼那片和黑夜融为一体的大海。"
    "但是现在却做不到，因为已经连站起来的力气都没有了。"
    "从观景台走回医院之后病情就开始恶化。"
    "因为没有听医生的话。"
    "这就是惩罚吧。"
    $ flcam.move(2250, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0617570.ogg"
    yume "不是凉君......的错。"
    "想要勉强维持意识都很困难。比起疼痛更加强烈的是睡意。"
    "不能就这样睡过去。"
    "害怕闭上眼睛就再也睁不开了。"
    "额头上开始冒冷汗。"
    "腿也在不停地颤抖。"
    play voice "voice/翔子/0617580.ogg"
    yume "啊哈哈......"
    play voice "voice/翔子/0617590.ogg"
    yume "真是丢人。"
    pause 1.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    play voice "voice/天使雷亚/0027770.ogg"
    stranger "很难过吗？"
    pause 1.0 hard
    $ flcam.move(4500, -300, 900)
    scene set only hospital night room yinghua
    show yume_sy_b2 b2 b2_s4 onlayer m2:
        xpos 0.7
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/0617600.ogg"
    yume "......"
    hide yume_sy_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1_d b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0027780.ogg"
    lst "很痛苦吗？"
    pause 0.5 hard
    show yume_sy_b2 b2 b2_s4 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0617610.ogg"
    yume "死神......小姐。"
    play voice "voice/翔子/0617620.ogg"
    yume "这次你是来割取我的性命了吗？"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0027790.ogg"
    lst "之前也说过的，我所能割取的只有噩梦而已。"
    play voice "voice/翔子/0617630.ogg"
    yume "......我的噩梦是什么？"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0027800.ogg"
    lst "对人来说，那是想要放弃却又舍不得。"
    play voice "voice/天使雷亚/0027810.ogg"
    lst "喜欢，却又让人心生厌恶的东西。"
    show ts_lst_ssz_b1_d b1 b1_s3
    play voice "voice/天使雷亚/0027820.ogg"
    lst "无法实现的......幻梦。"
    hide yume_sy_b2
    show yume_sy_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0617640.ogg"
    yume "听起来像是某个单相思的对象啊。"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0027830.ogg"
    lst "这么理解也没错。"
    hide yume_sy_b1
    show yume_sy_b2 b2 b2_s4 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0617650.ogg"
    yume "所以你是来割取的我噩梦吗？"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0027840.ogg"
    lst "不是，我并没有和谁约定过要割取你的噩梦。"
    show ts_lst_ssz_b2 b2 b2_s3
    play voice "voice/天使雷亚/0027850.ogg"
    lst "那天你许下的愿望是割取凉君的噩梦。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1_d b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0027860.ogg"
    lst "但是我讨厌你。"
    play voice "voice/天使雷亚/0027870.ogg"
    lst "讨厌那个让凉君难过的你。"
    hide yume_sy_b2
    show yume_sy_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0617660.ogg"
    yume "......是吗。"
    show yume_sy_b1 b1 b1_n1
    play voice "voice/翔子/0617670.ogg"
    yume "你也喜欢凉君呢。"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0027880.ogg"
    lst "才没有这种事。"
    hide yume_sy_b1
    show yume_sy_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0617680.ogg"
    yume "拜托你了，死神小姐。"
    play voice "voice/翔子/0617690.ogg"
    yume "请你成为凉君的力量吧。"
    show yume_sy_b2 b2 b2_s3
    play voice "voice/翔子/0617700.ogg"
    yume "因为我已经，无法继续成为凉君的依靠了。"
    play voice "voice/翔子/0617710.ogg"
    yume "现在的我只会成为他的累赘。"
    play voice "voice/翔子/0617720.ogg"
    yume "即使凉君想要依赖我，我也已经没有回应他的力量了。"
    play voice "voice/翔子/0617730.ogg"
    yume "所以，就由你来替我......"
    show ts_lst_ssz_b1_d b1 b1_s3
    play voice "voice/天使雷亚/0027890.ogg"
    lst "......笨笨的。"
    play voice "voice/天使雷亚/0027900.ogg"
    lst "想让凉君继续依赖的话，明明让自己变得足够坚强就可以了。"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0027910.ogg"
    lst "想让凉君向你撒娇的话，明明让自己变得更加成熟就可以了。"
    hide yume_sy_b2
    show yume_sy_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0617740.ogg"
    yume "......做不到的。"
    hide ts_lst_ssz_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yume_sy_b1 b1 b1_s3
    play voice "voice/翔子/0617750.ogg"
    yume "已经，没有时间了。"
    play voice "voice/翔子/0617760.ogg"
    yume "这样下去只会是半途而废的结局。"
    play voice "voice/翔子/0617770.ogg"
    yume "即使能撑到那时候，到最后希望还是会消失的，我还是会消失的。"
    play voice "voice/翔子/0617780.ogg"
    yume "那份所谓的希望就是这样脆弱的。"
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/天使雷亚/0027920.ogg"
    lst "......"
    hide yume_sy_b1
    show yume_sy_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0617810.ogg"
    yume "所以，拜托了......"
    show yume_sy_b2 b2 b2_n1
    play voice "voice/翔子/0617820.ogg"
    yume "正因为是同样喜欢凉君的你，我才能安心地托付。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1_d b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0027930.ogg"
    lst "你又在许愿了吗？"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0027940.ogg"
    lst "只是让凉君忘记你还不够吗。"
    play voice "voice/翔子/0617830.ogg"
    yume "嗯。"
    play voice "voice/翔子/0617840.ogg"
    yume "我是在许愿哟。"
    hide ts_lst_ssz_b1_d
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yume_sy_b1 b1 b1_n1
    play voice "voice/翔子/0617850.ogg"
    yume "不管过去还是现在，都没有变过。"
    show yume_sy_b1 b1 b1_h1
    play voice "voice/翔子/0617860.ogg"
    yume "这愿望无论何时，都是没有改变的。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with slowdissolve
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    play music first_36 fadein 3.0 if_changed
    scene set only xz_memory normal one
    with in2out_v2_slow
    pause 2.0 hard
    play voice "voice/翔子/0617880.ogg"
    tiny_xz "凉君，很快就要到明天了。"
    play voice "voice/翔子/0617890.ogg"
    tiny_xz "搬家就是在明天了吧。"
    me01 "是啊。"
    pause 0.1 hard
    scene set only xz_memory normal three
    with dissolve
    $ flcam.move(750, -1500, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0617900.ogg"
    tiny_xz "我会去送你的。"
    pause 0.1 hard
    scene set only xz_memory normal four
    with dissolve
    play voice "voice/翔子/0617920.ogg"
    tiny_xz "明天我会去车站送你的。"
    play voice "voice/翔子/0617930.ogg"
    tiny_xz "一定会去的！"
    me01 "在那之前......"
    pause 0.1 hard
    scene set only xz_memory normal three
    with dissolve
    play voice "voice/翔子/0617940.ogg"
    tiny_xz "什么？"
    me01 "你的联系方式，能告诉我吗？"
    play voice "voice/翔子/0617950.ogg"
    tiny_xz "......"
    me01 "这样一来就算我们分开了，也可以通过电话或者书信的方式交流了。"
    pause 0.1 hard
    scene set only xz_memory normal two
    with dissolve
    play voice "voice/翔子/0617970.ogg"
    tiny_xz "......对不起。"
    play voice "voice/翔子/0617980.ogg"
    tiny_xz "唯独这一点，是不行的。"
    me01 "为什么？"
    pause 0.1 hard
    scene set only xz_memory normal one
    with dissolve
    play voice "voice/翔子/0617990.ogg"
    tiny_xz "这其中的原因对于现在的凉君来说还太早了。"
    pause 0.1 hard
    scene set only xz_memory normal three
    with dissolve
    play voice "voice/翔子/0618010.ogg"
    tiny_xz "还不能告诉你的。"
    me01 "那什么时候才能告诉我呢？"
    play voice "voice/翔子/0618020.ogg"
    tiny_xz "等凉君你变成大人的时候。"
    play voice "voice/翔子/0618030.ogg"
    tiny_xz "成为大人，稍微成长一些的时候。"
    play voice "voice/翔子/0618040.ogg"
    tiny_xz "成为大人，变得坚强的时候。"
    pause 0.1 hard
    scene set only xz_memory normal four
    with dissolve
    play voice "voice/翔子/0618070.ogg"
    tiny_xz "等到我们彼此都变得坚强了之后，我就告诉你。"
    play voice "voice/翔子/0618110.ogg"
    pause 0.1 hard
    $ flcam.move(1500, -2000, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    tiny_xz "因为这是我的愿望。"
    play voice "voice/翔子/0618120.ogg"
    tiny_xz "是我与神明大人的约定。"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 3.0 hard
    $ flcam.move(750, -2000, 600)
    scene set only xz_cg kiss
    with in2out_v2_slow
    pause 2.0 hard
    play voice "voice/翔子/0618130.ogg"
    tiny_xz "是只能告诉牛郎和织女的秘密——"
    pause 1.0 hard
    scene white 
    with slowdissolve
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    $ suppress_overlay = True
    jump day14
