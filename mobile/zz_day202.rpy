label day202:
    bookmark
    $ save_name = _("Day 202")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    pause 2.0 hard
    show backend_date201 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black 
    with dissolve
    $ flcam.move(0, 0, 0)
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    with cent2side
    pause 1.0 hard
    "早晨清新的空气扑面而来。"
    "明明应该是寒冷的季节，却怎么也感觉不到一丝凉意。"
    "甚至还能察觉到一股温暖包裹全身。"
    "托它的福，我又差点睡过去。"
    "但是现在必须起床了。"
    "毕竟今天是上学的第一天，我可不想就这样迟到。"
    play music second_114 fadein 3.0 if_changed
    play sound touch
    pause 1.0 hard
    scene set only aiyi_cg one
    with slowdissolve
    pause 1.0 hard
    "我翻了个身，发现爱衣就睡在我的身旁。"
    "应该是昨晚擅自跑过来的。"
    "睡迷糊了就钻到我的被窝里来了吗。"
    play voice "voice/爱衣/110100010.ogg"
    aiyi "......"
    pause 0.1 hard
    $ flcam.move(-1400, -750, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/爱衣/110100010.ogg"
    aiyi "呜嗯......"
    "要是被发现了可解释不清。"
    "总之还是赶紧脱身为妙。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.5 hard
    play sound open_door6
    pause 1.0 hard
    show xz_dzf_b2 b2 b2_n1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/010100010.ogg"
    xz "神野君，起床了吗？"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_n1 onlayer screens at side_right('xz'), basicfade
    stop music fadeout 5.0
    play voice "voice/翔子/010100020.ogg"
    xz "我刚才找不到爱衣，你有没有......"
    hide xz_dzf_b1
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home day my_room xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b3 b3 b3_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/翔子/010100030.ogg"
    xz "......"
    show xz_dzf_b3 b3 b3_s3
    play voice "voice/翔子/010100040.ogg"
    xz "神野君你......"
    play music second_104 fadein 3.0 if_changed
    hide xz_dzf_b3
    show xz_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010100050.ogg"
    xz "诱拐犯。"
    me01 "果然解释不清啊！" with vpunch
    hide xz_dzf_b1
    show xz_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010100060.ogg"
    xz "早上发现爱衣不在房间里，刚想怎么到处都找不到，结果竟然是被你带到这里来了。"
    me01 "误会啊翔子，我醒来的时候已经是这样了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only aiyi_cg three
    with dissolve
    pause 0.5 hard
    play voice "voice/爱衣/110100030.ogg"
    aiyi "......嗯？"
    stop music fadeout 5.0
    pause 1.0 hard
    play sound touch
    scene set only home day my_room xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_sy_b1 b1 b1_n3 onlayer m2:
        xpos 0.3 alpha 0.0 ypos 1.04
        parallel:
            linear 1.0 ypos 1.0
        parallel:
            linear 1.0 alpha 1.0
    pause 0.5 hard
    play voice "voice/爱衣/110100040.ogg"
    aiyi "......大姐姐？"
    pause 0.5 hard
    show xz_dzf_b3 b3 b3_n1 onlayer m1:
        xpos 0.5
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/010100070.ogg"
    xz "爱衣，该起床了。"
    show aiyi_sy_b1 b1 b1_s3
    play voice "voice/爱衣/110100060.ogg"
    aiyi "稍微睡过头了。"
    play voice "voice/翔子/010100100.ogg"
    xz "一个人洗脸没问题吗？"
    show aiyi_sy_b1 b1 b1_h1
    play voice "voice/爱衣/110100080.ogg"
    aiyi "没问题的，爱衣已经是大人了嘛~"
    show xz_dzf_b3 b3 b3_h1
    play voice "voice/翔子/010100090.ogg"
    xz "早饭马上就好。"
    pause 1.0 hard
    show xz_dzf_b3 b3 b3_h1 at walkout_r(0.5)
    pause 0.5 hard
    hide xz_dzf_b3
    pause 2.0 hard
    "翔子没有理会我，径直走出了房间。"
    "看来是相当生气啊......"
    pause 0.5 hard
    play music second_115 fadein 3.0 if_changed
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_sy_b1 b1 b1_n1
    play voice "voice/爱衣/110100090.ogg"
    aiyi "大哥哥也一起呢~"
    me01 "是啊，毕竟接下来还得去学校。"
    show aiyi_sy_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/爱衣/110100100.ogg"
    aiyi "我来告诉你卫生间的位置哦，这边这边~"
    pause 0.5 hard
    show aiyi_sy_b1 b1 b1_h1 at walkout_l(0.3)
    pause 0.5 hard
    play sound close_door3
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard

label day202.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "今天没有下雪，天空相对晴朗了许多。"
    "但因为是冬天的缘故，依旧是那么的寒冷。"
    pause 1.0 hard
    scene set only home night kitchen xuejian
    with slowdissolve
    "餐桌上摆满了饭菜，都是翔子一个人准备的。"
    pause 0.5 hard
    show breakfast onlayer texture at basicfade_c2u
    pause 1.0 hard
    "看起来非常的丰盛。"
    "食物的精致程度着实把我惊艳到了。"
    hide breakfast
    pause 1.0 hard
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/爱衣/110100110.ogg"
    aiyi "我开动了~"
    show xz_dzf_b3 b3 b3_n1 onlayer m1 at walkin_r(0.5)
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    "吃饭的过程中翔子还不时地为爱衣擦去脸颊上的饭粒。"
    "这种感觉真的就像是一家人一样。"
    hide aiyi_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b3 b3 b3_sp1
    me01 "抱歉，让你多准备了我的份。"
    hide xz_dzf_b3
    show xz_dzf_b1 b1 b1_s2 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010100120.ogg"
    xz "多做一份也没什么辛苦的。"
    me01 "我会付钱的。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010100130.ogg"
    xz "不需要了，钱的话还是足够富余的。"
    pause 0.5 hard
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 1.0 hard
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010100150.ogg"
    xz "关于让神野君住在我家的事情......"
    me01 "和家人那边联系了吗？"
    show xz_dzf_b3 b3 b3_n2
    play voice "voice/翔子/010100160.ogg"
    xz "虽然从早上开始打了好几个电话，但是完全打不通。"
    me01 "是家母那边吗？"
    play voice "voice/翔子/010100170.ogg"
    xz "不对，是爸爸的手机。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with dissolve
    pause 1.0 hard
    "如果是翔子的父母的话应该会站在我这边的吧。"
    "毕竟之前留给他们的印象还算不错。"
    "不过虽是这样说，生活费还是需要支付的。"
    pause 1.0 hard
    scene set only home day passwalk xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dzf_b3 b3 b3_n1 onlayer m1:
        xpos 0.5
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    play voice "voice/爱衣/110100130.ogg"
    aiyi "我出门了~"
    show xz_dzf_b3 b3 b3_h1
    play voice "voice/翔子/010100180.ogg"
    xz "我出门了~"
    pause 1.0 hard
    stop music fadeout 5.0
    play sound close_door3
    scene black
    with right2left_02
    pause 1.0 hard
    play music second_114 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only home day outside xuejian
    with right2left_02
    play ambience1 niaoming fadein 3.0
    pause 1.0 hard
    "今早依旧是不需要带伞出门。"
    "听说父亲现在工作的地方坐落于雪见市北部的人工岛屿上。"
    "相比之下那里的气候应该会更加宜人一些吧。"
    pause 2.0 hard

label day202.street_event01:
    scene set only street day road1 xuejian
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b3 b3 b3_s4 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/翔子/010100210.ogg"
    xz "我今早洗过了......"
    hide xz_dzf_b3
    show xz_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010100220.ogg"
    xz "男孩子的内裤什么的......还是第一次洗。"
    me01 "以后我自己洗就行了。"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/010100230.ogg"
    xz "只是还没有习惯而已，这倒不是问题。"
    "出门之前，我注意到洗好的衣服已经放进烘干机里了。"
    "考虑到还要照顾爱衣和做饭，翔子的自由时间感觉已经被压缩得非常有限了。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_n1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010100240.ogg"
    xz "做饭和洗衣服的事情都不要在意了，毕竟神野君你也不会一直住在我家里的吧？"
    me01 "确实是这样没错。"
    "关于借宿的期限还没有具体讨论过。"
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2 at walkin_l(0.3)
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/爱衣/110100180.ogg"
    aiyi "大哥哥......要搬出去了吗？"
    me01 "放心好了，都还没决定的。"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/110100190.ogg"
    aiyi "爱衣，希望大哥哥能一直留在这里。"
    show xz_dzf_b1 b1 b1_sp1 
    play voice "voice/翔子/010100260.ogg"
    xz "爱衣......"
    me01 "至少今天我还在这里，所以放学以后还会去接爱衣你的。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/爱衣/110100200.ogg"
    aiyi "哇！"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_a2 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010100270.ogg"
    xz "别擅自决定......"
    hide aiyi_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "翔子你已经够辛苦的了，就让我替你分担一些吧。"
    play voice "voice/翔子/010100280.ogg"
    xz "这些还不至于让我觉得辛苦。"
    me01 "如果我的决定让你为难的话，就当我没有说过吧。"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010100290.ogg"
    xz "也不是为难......而且爱衣也很开心的样子。"
    hide xz_dzf_b2
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    play voice "voice/爱衣/110100210.ogg"
    aiyi "大哥哥，要来跟爱衣一起玩吗？"
    me01 "在幼儿园？"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/110100220.ogg"
    aiyi "嗯，千波和小桃也在的哟~"
    "且不说小桃，跟千波玩相当累人啊。"
    me01 "放学后的话自然没问题，只是玩玩的话。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110100230.ogg"
    aiyi "那大哥哥你就正式加入“幼儿社”了呢~"
    me01 "幼儿社？"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110100240.ogg"
    aiyi "小桃说过，放学后做的事情就叫做社团活动。"
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.5
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/010100300.ogg"
    xz "虽然小桃懂得也挺多，但还是别记住那些奇怪的部分比较好。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110100250.ogg"
    aiyi "在大哥哥来之前，我会在幼儿园等着你的。"
    me01 "我知道了，不过约好别再擅自跑出去了。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/爱衣/110100260.ogg"
    aiyi "嗯！"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010100310.ogg"
    xz "哈啊......"
    pause 1.0 hard
    scene black
    with slowdissolve
    stop ambience1 fadeout 5.0
    pause 2.0 hard

label day202.kindergarten_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_h3 onlayer m1 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千川老师/140100010.ogg"
    qcls "早上好，青木同学。"
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.5)
    show xz_dzf_b2 b2 b2_h2 onlayer m1 at walkin_r(0.7)
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/010100360.ogg"
    xz "早上好。"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/140100020.ogg"
    qcls "爱衣也是，早上好。"
    play voice "voice/爱衣/110100270.ogg"
    aiyi "嗯，老师早上好。"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/140100030.ogg"
    qcls "然后神野同学也，昨天的事情真是谢谢你了。"
    "对方似乎已经知道了我的名字了，可是是什么时候......"
    hide xz_dzf_b2
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/爱衣/110100280.ogg"
    aiyi "大哥哥已经是爱衣的好朋友了。"
    play voice "voice/千川老师/140100050.ogg"
    show qcls_zf_b1 b1 b1_h1
    qcls "嗯，是这样呢。"
    play voice "voice/爱衣/110100290.ogg"
    aiyi "不只是朋友，还是爱衣的大哥哥哟~"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/140100060.ogg"
    qcls "和神野同学的关系真好呢~"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110100300.ogg"
    aiyi "嗯，不只是爱衣，大哥哥和大姐姐的关系也很要好哟~"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/爱衣/110100310.ogg"
    aiyi "还有呢还有呢，大哥哥和大姐姐住在一起了。"
    show qcls_zf_b1 b1 b1_sp1
    play voice "voice/千川老师/140100070.ogg"
    qcls "是这样吗？"
    hide qcls_zf_b1
    $ flcam.move(2250, 0, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_sp2 onlayer m1:
        xpos 0.7
    play voice "voice/翔子/010100370.ogg"
    xz "不是这样的！"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110100320.ogg"
    aiyi "大姐姐......不对吗？"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010100380.ogg"
    xz "也不是不对，或者说还不清楚......"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110100330.ogg"
    aiyi "还是要把大哥哥赶出去吗？"
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp2 onlayer m1:
        xpos 0.3
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_s1
    play voice "voice/翔子/010100390.ogg"
    xz "比、比起这个爱衣，还是快点跟老师进去比较好。千川老师，之后就拜托了~"
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_s1:
        linear 0.8 xpos 0.45
    pause 0.2 hard
    show aiyi_dzf_b1 b1 b1_sp1:
        linear 0.6 xpos 0.35 alpha 1.0
    pause 2.0 hard
    play sound jiaobu3
    show xz_dzf_b2 b2 b2_s1 at walkout_r(0.45)
    pause 0.5 hard
    hide xz_dzf_b2
    "翔子把爱衣交给千川老师后就自顾自地逃跑了。"
    $ flcam.move(-4100, 0, 750, duration=1.5)
    pause 1.0 hard
    me01 "那么我也该走了。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110100340.ogg"
    aiyi "大哥哥再见啦~"
    pause 1.0 hard
    scene black
    with slowdissolve
    stop music fadeout 5.0
    pause 2.0 hard

label day202.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    me01 "我叫神野凉，今后就要跟大家一起学习了，请多指教。"
    pause 1.0 hard
    scene set only school day room xuejian
    with dissolve
    pause 1.0 hard
    "就这样，我又一次开始了全新的校园生活。"
    "多亏了在樱华校的经历，这次的介绍环节进行得还算顺利。"
    "顺利地结束了早会时间。"
    "借着这短暂的休息，邻座的同学们也开始聚集起来。"
    play music second_119 fadein 3.0 if_changed
    show xz_dzf_b3 b3 b3_s2 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/010100530.ogg"
    xz "想不到竟然会转到我的班级里来......而且还是旁边的座位。"
    hide xz_dzf_b3
    me01 "这大概就是缘分吧。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    show yj_dzf_b2 b2 b2_h4 onlayer m1 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/植澄友加/020100010.ogg"
    stranger "虽然不知道在同一个班级是不是偶然，但是我觉得坐在翔子的旁边是理所当然的结果哟~"
    "坐在翔子前排的女同学突然加入了我们的话题。"
    pause 0.5 hard
    show xz_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/010100550.ogg"
    xz "友加......为什么？"
    show yj_dzf_b2 b2 b2_ga4
    play voice "voice/植澄友加/020100030.ogg"
    yj "难道不是因为老师觉得翔子你能够介绍学校的各种事情给他，所以才这样安排的吗？"
    hide xz_dzf_b3
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010100560.ogg"
    xz "要是这样的话，擅长跟人交流的友加应该更适合吧。"
    "这位女孩身材比较娇小，加上双马尾显得十分可爱。"
    hide xz_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b2 b2 b2_h1
    play voice "voice/植澄友加/020100040.ogg"
    yj "我的名字叫植澄友加，请多指教~"
    me01 "请多关照，那个......植澄同学。"
    show yj_dzf_b2 b2 b2_n1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100050.ogg"
    yj "叫我友加吧，称呼的话用名字就好。"
    play voice "voice/植澄友加/020100060.ogg"
    yj "是翔子的朋友也就是我的朋友了。"
    pause 0.5 hard
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010100570.ogg"
    xz "我其实，也并不算是神野君的朋友。"
    hide yj_dzf_b2
    hide xz_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    show yczs_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180100010.ogg"
    yczs "但是你们两位，不是互相认识的吗？"
    show yczs_dzf_b1 b1 b1_h2
    play voice "voice/一诚总司/180100020.ogg"
    yczs "我叫一城总司，请多指教~"
    me01 "请多指教......才怪啊！"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180100030.ogg"
    yczs "两位说起话来很亲密呢~"
    pause 0.5 hard
    $ flcam.move(0, -200, 600, duration=1.5)
    show yj_dzf_b3 b3 b3_h1 onlayer m1:
        xpos 0.5
    show xz_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010100580.ogg"
    xz "才、才没有亲密什么的......"
    me01 "嘛，昨天才{rb}偶然{/rb}{rt}重音{/rt}认识而已。"
    play voice "voice/植澄友加/020100070.ogg"
    yj "那个，凉君你。"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/180100040.ogg"
    yczs "凉君？一上来就直呼其名！？"
    show yj_dzf_b3 b3 b3_n3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100080.ogg"
    yj "听到你叫“凉君”就习惯性地就变成这样了。"
    hide yczs_dzf_b1
    $ flcam.move(2250, -350, 750, duration=1.5)
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010100590.ogg"
    xz "我倒是觉得一见面就喊对方名字这一点很有可疑啊。"
    show yj_dzf_b3 b3 b3_h1
    play voice "voice/植澄友加/020100090.ogg"
    yj "因为我也让他用名字来叫我了，这样不是显得更友好吗？"
    me01 "我倒是觉得无所谓。"
    hide xz_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dzf_b3
    show yj_dzf_b1 b1 b1_s2 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100100.ogg"
    yj "对了凉君你刚才的自我介绍说了吧，之前也来过这座城市对吧？"
    me01 "都是小时候的事情了。"
    play voice "voice/植澄友加/020100110.ogg"
    yj "那么，是在那之后才认识翔子的吗？"
    me01 "和翔子认识是在那之前了吧。"
    hide yj_dzf_b1
    show yj_dzf_b3 b3 b3_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020100120.ogg"
    yj "不是再会吗？"
    me01 "为什么你会这么想？"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_h1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020100130.ogg"
    yj "我在想两人是不是青梅竹马，所以迫不及待想见对方才特地搬过来之类的。"
    play voice "voice/植澄友加/020100140.ogg"
    yj "毕竟要说是偶然的话也实在是在太牵强了。"
    me01 "咳咳咳，是你多虑了。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.7
    pause 0.5 hard
    play voice "voice/翔子/010100600.ogg"
    xz "我也不记得自己小时候认识神野君的。（小声）"
    pause 0.5 hard
    hide xz_dzf_b2
    hide yj_dzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    show yczs_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    play voice "voice/一诚总司/180100050.ogg"
    yczs "但是既然来过这里，应该有一两个在这座城市生活的熟人吧？"
    me01 "该怎么说呢。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b2 b2 b2_s2 onlayer m1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100150.ogg"
    yj "刚刚提到的“来过”是到什么时候为止呢？"
    me01 "到国中毕业为止。"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180100060.ogg"
    yczs "那应该能久违地遇到那个时候的同级生吧？"
    me01 "我想这是很困难的事情，毕竟当时的我并没有很正式地上过学。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020100160.ogg"
    yj "欸？"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/180100070.ogg"
    yczs "怎么回事？"
    me01 "......"
    "这该怎么回答呢......"
    "因为自己小时候太过孤僻以至于一直没有朋友什么的，果然还是说不出口啊。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010100610.ogg"
    xz "各位，提问就到此为止了，没看到神野君正在困扰着的吗？"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180100080.ogg"
    yczs "就是那个吧，转校生的宿命什么的。"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/010100620.ogg"
    xz "不管怎么说，马上就要上课了。"
    hide xz_dzf_b2
    hide yczs_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_n1 onlayer m1:
        xpos 0.5
    pause 0.5 hard 
    play voice "voice/植澄友加/020100170.ogg"
    yj "那么凉君，下一个休息时间再来继续我们的话题吧~"
    me01 "我倒是觉得我回答不出你感兴趣的东西。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b2 b2 b2_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100180.ogg"
    yj "不管怎么说，在满足我的好奇心之前都会让你奉陪的哟~"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black 
    with slowdissolve
    pause 2.0 hard

label day202.kindergarten_event02:
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian
    with dissolve
    play music second_112 fadein 3.0
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    show lhx_dsf_b2 b2 b2_n1 onlayer m1 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/030100010.ogg"
    stranger "初次见面，我叫立花希，请多指教~"
    $ flcam.move(2250, -150, 750, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_h1 onlayer m1 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/千川老师/140100080.ogg"
    qcls "你好，这边也请多多关照，立花希老师~"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga2 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/030100020.ogg"
    lhx "请不要叫我老师，我只是单纯来帮忙的而已。"
    show lhx_dsf_b3 b3 b3_n1
    play voice "voice/立花希/030100030.ogg"
    lhx "虽然可能做不到照顾小孩的程度，但是杂活我还是能做的，还请多多指教。"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/140100090.ogg"
    qcls "可以的话我倒是希望你能够成为正式的老师在这里工作。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m1:
        xpos 0.5
    play voice "voice/立花希/030100040.ogg"
    lhx "这个一时半会儿我还无法做决定。"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/030100050.ogg"
    lhx "我只是听说了幼儿园的人手不够，所以来帮个忙。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/140100100.ogg"
    qcls "之后也打算离开雪见市吗？"
    play voice "voice/千川老师/140100110.ogg"
    qcls "毕竟立花小姐还十分年轻呢，看起来应该还是学生的年纪。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s1 onlayer m1:
        xpos 0.5
    play voice "voice/立花希/030100070.ogg"
    lhx "因为有各种各样的原因，不继续问下去的话就帮大忙了......"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/140100120.ogg"
    qcls "抱歉，真是失礼。"
    show lhx_dsf_b1 b1 b1_n1
    play voice "voice/立花希/030100080.ogg"
    lhx "不会，我只是担心您会觉得很不可思议。"
    pause 0.5 hard
    hide lhx_dsf_b1
    hide qcls_zf_b1
    $ flcam.move(3800, 300, 900, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n4 onlayer m1:
        xpos 0.65
    play voice "voice/小桃/220100010.ogg"
    ycxt "盯......"
    pause 0.5 hard
    $ flcam.move(2250, 150, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.5
    pause 0.5 hard
    play voice "voice/立花希/030100090.ogg"
    lhx "不知不觉被小孩子盯着看了。"
    pause 0.5 hard
    $ flcam.move(2800, 0, 600, duration=1.5)
    show qcls_zf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.75
    pause 0.5 hard
    play voice "voice/千川老师/140100130.ogg"
    qcls "小桃？"
    pause 0.5 hard
    play sound jump_1
    show ycxt_dzf_b1 b1 b1_s4:
        linear 0.5 xpos 0.7
    play voice "voice/小桃/220100020.ogg"
    ycxt "......"
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_sp1
    play voice "voice/立花希/030100100.ogg"
    lhx "躲到千川老师身后藏起来了。"
    hide lhx_dsf_b2
    hide qcls_zf_b1
    hide ycxt_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110100350.ogg"
    aiyi "啊小桃，原来你在这里啊。"
    $ flcam.move(2800, 0, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n2 onlayer m1:
        xpos 0.7
    show qcls_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.75
    play voice "voice/小桃/220100030.ogg"
    ycxt "盯......"
    $ flcam.move(1100, 0, 600, duration=1.5)
    show lhx_dsf_b2 b2 b2_s2 onlayer m1:
        xpos 0.35
    play voice "voice/立花希/030100110.ogg"
    lhx "被不明所以地盯上了。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110100360.ogg"
    aiyi "那个千川老师，这孩子是？"
    show qcls_zf_b1 b1 b1_h3
    play voice "voice/千川老师/140100140.ogg"
    qcls "是立花小姐哟~"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m1:
        xpos 0.35
    play voice "voice/立花希/030100120.ogg"
    lhx "居然把身为大人的我称作“这孩子”，真是好胆量啊。"
    hide qcls_zf_b1
    hide ycxt_dzf_b1
    $ flcam.move(-1800, 150, 750, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.5
    pause 0.5 hard
    play voice "voice/爱衣/110100370.ogg"
    aiyi "初次见面立花，从今天起就正式加入幼儿园了呢~"
    show lhx_dsf_b3 b3 b3_n3
    play voice "voice/立花希/030100130.ogg"
    lhx "我不是小孩子。刚才也是，不管我个子有多矮这也太过分了吧。"
    hide lhx_dsf_b3
    hide aiyi_dzf_b1
    $ flcam.move(6500, -300, 900, duration=1.5)
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.75
    play voice "voice/千川老师/140100150.ogg"
    qcls "立花小姐是大家的老师哟~"
    $ flcam.move(2800, -150, 750, duration=1.5)
    show lhx_dsf_b3 b3 b3_s2 onlayer m1:
        xpos 0.5
    pause 0.5 hard
    play voice "voice/立花希/030100140.ogg"
    lhx "也没有打算当老师的。（小声）"
    show ycxt_dzf_b1 b1 b1_n2 onlayer m1:
        xpos 0.7
    play voice "voice/小桃/220100040.ogg"
    ycxt "盯......"
    show lhx_dsf_b3 b3 b3_n4
    play voice "voice/立花希/030100150.ogg"
    lhx "要盯着我看到什么时候啊？"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/140100160.ogg"
    qcls "小桃别藏了，你的问候呢？"
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n1 at walkout_r(0.75)
    pause 0.5 hard
    hide qcls_zf_b1
    $ flcam.move(2250, 150, 750, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/220100050.ogg"
    ycxt "你、你好......"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.5
    play voice "voice/立花希/030100160.ogg"
    lhx "嗯，你好~"
    show ycxt_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/小桃/220100060.ogg"
    ycxt "呜......"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/030100170.ogg"
    lhx "竟然哭了。"
    pause 0.5 hard
    stop music fadeout 5.0
    hide lhx_dsf_b2
    hide ycxt_dzf_b1
    $ flcam.move(-8500, 300, 900, duration=1.5)
    play sound appear
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at walkin_l(0.15)
    pause 0.5 hard
    play music second_106 fadein 3.0 if_changed
    play voice "voice/千波/210100010.ogg"
    qb "喂！那边的小屁孩！！！"
    pause 0.5 hard
    $ flcam.move(-6200, 150, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.35
    play voice "voice/立花希/030100180.ogg"
    lhx "你指的是谁啊？"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 30):
        xpos 0.15
    play voice "voice/千波/210100020.ogg"
    qb "当然是你了！！！"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_s1 onlayer m1:
        xpos 0.35
    play voice "voice/立花希/030100190.ogg"
    lhx "被一个小屁孩唤作“小屁孩”，没有比这更大的羞辱了。"
    show qianbo_dzf_b1 b1 b1_a3
    play voice "voice/千波/210100030.ogg"
    qb "别欺负小桃和爱衣啊！！！"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/030100200.ogg"
    lhx "谁也没有欺负她们。"
    $ flcam.move(-3800, 0, 600, duration=1.5)
    show qcls_zf_b1 b1 b1_a1 onlayer m2:
        xpos 0.55
    play voice "voice/千川老师/140100170.ogg"
    qcls "不行啊千波。不加上“老师”是不对的。"
    show lhx_dsf_b3 b3 b3_ga2
    play voice "voice/立花希/030100210.ogg"
    lhx "都说了我没有当老师的打算。"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/140100180.ogg"
    qcls "或者就叫立花酱吧~"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s2 onlayer m1:
        xpos 0.35
    play voice "voice/立花希/030100220.ogg"
    lhx "也请别把我当成小孩子。"
    hide qcls_zf_b1
    $ flcam.move(-6200, 150, 750, duration=1.5)
    show qianbo_dzf_b1 b1 b1_n2
    pause 0.5 hard
    play voice "voice/千波/210100040.ogg"
    qb "也就是说这家伙是披着小孩子外衣的狼是吧。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n2 onlayer m1:
        xpos 0.35
    play voice "voice/立花希/030100230.ogg"
    lhx "虽然觉得难以置信，不过你莫非是把我当成男孩子了？我毫无疑问是个成熟的女性。"
    show qianbo_dzf_b1 b1 b1_sp2
    play voice "voice/千波/210100050.ogg"
    qb "明明是个飞机场？"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/030100240.ogg"
    lhx "受到如此过分的羞辱，我实在是忍不住想去做点什么。"
    show qianbo_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.15
    play voice "voice/千波/210100060.ogg"
    qb "要以成熟的女性自称的话，至少要有我这样的身材啊~"
    show lhx_dsf_b3 b3 b3_n2
    play voice "voice/立花希/030100250.ogg"
    lhx "不管你怎么卖弄身姿，但在我眼中确实只看到了一个小不点而已。"
    show qianbo_dzf_b1 b1 b1_h2
    play voice "voice/千波/210100070.ogg"
    qb "小屁孩根本不懂我的魅力啊。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.35
    play voice "voice/立花希/030100260.ogg"
    lhx "看来这家伙已经被我认定是敌人了。"
    hide lhx_dsf_b2
    hide qianbo_dzf_b1
    $ flcam.move(5800, 0, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s2 onlayer m1:
        xpos 0.7
    show qcls_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.75
    pause 0.5 hard
    play voice "voice/小桃/220100070.ogg"
    ycxt "吵、吵架是不对的......"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/140100190.ogg"
    qcls "大家要好好相处哦，立花小姐是你们的新伙伴。"
    $ flcam.move(2000, 0, 600, duration=1.5)
    show lhx_dsf_b3 b3 b3_a1 onlayer m1:
        xpos 0.4
    play voice "voice/立花希/030100270.ogg"
    lhx "怎么连老师都加入她们了，别把我当成幼儿园的小朋友。"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/140100210.ogg"
    qcls "大家，差不多该回里屋去了。"
    $ flcam.move(1800, 0, 500, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    pause 0.5 hard
    play voice "voice/爱衣/110100430.ogg"
    aiyi "立花酱，我们走吧~"
    show lhx_dsf_b3 b3 b3_ga2
    play voice "voice/立花希/030100410.ogg"
    lhx "呀，请别拽我的手......"
    $ flcam.move(0, 0, 400, duration=1.5)
    show qianbo_dzf_b1 b1 b1_h4 onlayer m2:
        xpos 0.25
    play voice "voice/千波/210100130.ogg"
    qb "真拿你没办法，也给你介绍介绍其他人认识吧。"
    show ycxt_dzf_b1 b1 b1_h1:
        linear 0.5 xpos 0.63
    pause 0.5 hard
    play voice "voice/小桃/220100100.ogg"
    ycxt "小桃的新朋友~"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/030100420.ogg"
    lhx "我又不是幼儿园的小朋友。照样子下去真的能顺利相处吗......"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/140100230.ogg"
    qcls "似乎已经顺利成为大家的新伙伴，真是帮大忙了~"
    show lhx_dsf_b3 b3 b3_ga2 at flu_down(0.35, 20):
        xpos 0.4
    play voice "voice/立花希/030100430.ogg"
    lhx "我可不打算做小孩子的伙伴！"
    pause 2.0 hard
    stop music fadeout 5.0
    scene black
    with slowdissolve
    pause 2.0 hard

label day202.school_event02:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian2
    with dissolve
    pause 2.0 hard
    scene set only school day room xuejian
    with dissolve
    pause 1.0 hard
    play music second_116 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.3)
    pause 0.5 hard
    play voice "voice/一诚总司/180100140.ogg"
    yczs "那么去食堂吧。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show yj_dzf_b2 b2 b2_h4 onlayer m1:
        xpos 0.5
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/植澄友加/020100250.ogg"
    yj "之后的事情就边吃边说吧。"
    me01 "你们都是去食堂吃饭的吗？"
    play voice "voice/植澄友加/020100290.ogg"
    yj "是啊，在那里可以买餐券。"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180100160.ogg"
    yczs "菜单不是很丰富，可别太期待哦。"
    hide yj_dzf_b2 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_h1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100300.ogg"
    yj "凉君还没去过吧，我来给你带路~"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    play sound open_door5
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day corridor xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020100260.ogg"
    yj "凉君有带便当盒吗？"
    me01 "不，我什么都没有准备。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/植澄友加/020100270.ogg"
    yj "翔子有时候也会自己带便当的吧？"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010100660.ogg"
    xz "嗯，只在晚饭有剩余的时候才会考虑，所以今天是去食堂的。"
    hide yj_dzf_b3
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010100670.ogg"
    xz "如果不嫌弃的话，我倒是可以连神野君的那份一起准备。"
    me01 "不用在意我，去食堂吃饭也是校园生活的一部分。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.7
    stop music fadeout 5.0
    play voice "voice/翔子/010100680.ogg"
    xz "那有需要的时候我就一起准备吧，反正多一个人的量也不会觉得累。"
    pause 1.0 hard
    $ flcam.move(2250, -200, 600, duration=1.5)
    show yj_dzf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.5
    play music second_108 fadein 3.0 if_changed
    play voice "voice/植澄友加/020100280.ogg"
    yj "那个......为什么翔子会帮凉君做便当？"
    hide xz_dzf_b3 with None
    pause 0.1 hard
    show xz_dzf_b2 b2 b2_ga1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/翔子/010100690.ogg"
    xz "不、不是的，说错了。我怎么可能会给他做便当嘛。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show yczs_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    play voice "voice/一诚总司/180100150.ogg"
    yczs "两人的关系真是越来越令人在意了啊~"
    "这个看热闹不嫌事大家伙！"
    "说起来他才是这一切的罪魁祸首。"
    show xz_dzf_b2 b2 b2_s1
    play voice "voice/翔子/010100700.ogg"
    xz "只是昨天偶然遇见而已。"
    "翔子把头撇向了一边。"
    "不知是什么原因，再见面之后翔子似乎对我们的关系似乎表现得非常敏感。"
    hide yczs_dzf_b1
    hide yj_dzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/010100710.ogg"
    xz "而且，还不知道神野君明天是不是还住在这里......（小声）"
    pause 0.5 hard
    $ flcam.move(2250, -350, 750, duration=1.5)
    show yczs_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    pause 0.5 hard
    play voice "voice/一诚总司/1600060.ogg"
    yczs "有什么八卦吗？"
    pause 0.5 hard
    stop music fadeout 5.0
    hide yczs_dzf_b1
    hide xz_dzf_b2
    $ flcam.move(0, 0, 0, duration=1.5)
    play voice "voice/青木铃音/0500360.ogg"
    stranger "一诚同学，我觉得刨根问底是恶趣味哟。如果想要更加了解对方的话，就等到关系更进一步的时候再说吧。"
    play music second_119 fadein 5.0
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0500370.ogg"
    lingyin "又见面了呢，转校生同学，之后也请多多指教~"
    me01 "好久不见了铃音同学，真是让人怀念的开场方式啊。"
    hide lingyin_dzf_b2
    show lingyin_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0500400.ogg"
    lingyin "不可以去掉“同学”吗？"
    me01 "......这一点还是饶了我吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard

label day202.school_event03:
    $ flcam.move(0, 0, 0)
    scene set only school day restaurant xuejian
    with dissolve
    pause 1.0 hard
    play music second_115 fadein 3.0 if_changed
    "食堂里挤满了学生，此刻正是人潮最集中的时候。"
    me01 "平时都是这么多人吗？"
    $ flcam.move(0, -300, 900, duration=1.5)
    show yj_dzf_b2 b2 b2_h4 onlayer m1 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/植澄友加/020100340.ogg"
    yj "毕竟空间有限，午饭时间基本都是这样的。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yczs_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180100200.ogg"
    yczs "不喜欢拥挤的话，就只好去其他地方吃了。"
    me01 "其他地方是指？"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_n1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100350.ogg"
    yj "可以去便利店买面包哟~"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180100210.ogg"
    yczs "或者也可以在中庭或者天台吃。"
    hide yczs_dzf_b1
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    pause 0.5 hard
    play voice "voice/翔子/010100760.ogg"
    xz "这个季节在外面吃的话会着凉的吧。"
    show yj_dzf_b3 b3 b3_ga3
    play voice "voice/植澄友加/020100360.ogg"
    yj "毕竟是冬天嘛，虽然今天没有下雪。"
    play voice "voice/翔子/010100770.ogg"
    xz "就算是这样应该也不会有人刻意选择在寒风中进食的吧。"
    me01 "换句话说到了外面就不会拥挤了吧？"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020100370.ogg"
    yj "凉君不喜欢人多的地方？"
    me01 "算是吧。"
    show xz_dzf_b2 b2 b2_s1
    play voice "voice/翔子/010100780.ogg"
    xz "话虽如此，但比起寒冷还是忍耐下拥挤更加轻松吧？"
    $ flcam.move(0, -200, 600, duration=1.5)
    show yczs_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180100220.ogg"
    yczs "站在这里会妨碍其他人的，快去买餐券吧。"
    show yj_dzf_b2 b2 b2_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100380.ogg"
    yj "磨磨蹭蹭的话座位也会被占光了。"
    hide yczs_dzf_b1
    hide yj_dzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_h2
    play voice "voice/翔子/010100790.ogg"
    xz "神野君，开销方面没问题吧？"
    me01 "是的，借住期间的费用我也会好好支付的。"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/010100800.ogg"
    xz "不用了~毕竟爸爸给的生活费也都有剩余。"
    stop music fadeout 5.0
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010100810.ogg"
    xz "而且，也还没决定要一直住在一起吧？"
    pause 0.5 hard
    $ flcam.move(2250, -350, 750, duration=1.5)
    show yj_dzf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.5
    pause 0.5 hard
    play music second_104 fadein 3.0 if_changed
    play voice "voice/植澄友加/020100390.ogg"
    yj "......凉君和翔子住在一起吗？"
    play sound jump_1
    show xz_dzf_b2 b2 b2_sp2 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/翔子/010100820.ogg"
    xz "怎、怎么可能有这种事。"
    pause 1.0 hard
    show xz_dzf_b2 b2 b2_sp2 at walkout_r(0.7)
    pause 0.5 hard
    "顶着友加怀疑的目光，翔子慌忙地躲进人群之中。"
    "这家伙还真是容易说漏嘴啊......"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yczs_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    play voice "voice/一诚总司/180100230.ogg"
    yczs "神野你啊，现在住在哪里呀~"
    show yj_dzf_b2 b2 b2_sp1
    play voice "voice/植澄友加/020100400.ogg"
    yj "翔子家里？"
    hide yj_dzf_b2
    hide yczs_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    hide xz_dzf_b2
    show xz_dzf_b2 b2 b2_a1 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/010100830.ogg"
    xz "别说多余的话啊！"
    hide xz_dzf_b2
    "隔了老远都能读懂翔子眼神中传递的信息。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve

label day202.centergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day center room xuejian
    play music second_102 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "吃完午饭，我独自一人来到了中庭。"
    "果然和友加说的一样，这里几乎看不到人影。"
    "和传统的校园构造类似，中庭的设计没有太大的新奇之处。"
    pause 0.5 hard
    $ flcam.move(0, 0, 1000, duration=1.5)
    show liuli_dzf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    stranger "......"
    "就在我转身准备离开的时候，一个娇小的身影引起了我的注意。"
    "看上去似乎是比我的年纪还要小一些的女孩子。"
    pause 0.5 hard
    play sound rune1
    show wflash onlayer texture
    with vpunch
    pause 1.0 hard
    "......刚才那种感觉是什么？"
    pause 0.5 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dzf_b1
    show liuli_dzf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100010.ogg"
    stranger "......"
    show liuli_dzf_b2 b2 b2_ga3 at flu_down(0.35, 20):
        xpos 0.5
    "女孩没有说话，只是向我鞠了个躬。"
    "给人一种彬彬有礼的感觉。"
    pause 1.0 hard
    play sound jiaobu3
    show liuli_dzf_b2 b2 b2_ga3 at walkout_r(0.5)
    pause 1.0 hard
    "没有太多交流，女孩从长椅上站起来，转身离开了。"
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 2.0 hard

label day202.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "放学的时候，天下起了小雪。"
    "翔子那边因为学生会的工作脱不开身，于是让我一个人先去接爱衣回家。"
    "距离幼儿园放学的时间还有些许盈余，所以我特地放慢了脚步，想趁此机会欣赏一下沿途的风景。"
    pause 1.0 hard
    scene set only bridge day xuejian
    with dissolve
    pause 1.0 hard
    "此刻不管怎么下，雪一直都没有办法堆积起来。"
    "翔子说过这是温柔的雪，同时也是悲伤的雪。"
    "如果是印象中的话，这个时节明明是会堆积起更厚的雪才对。"
    "想要在雪地上行走的话，长靴是必要的装备。"
    "就算在樱华镇，爬上屋顶清理积雪、在大街上扫除多余的积雪之类的也是例行的工作。"
    "然而此刻显然已经看不到这样的景象了。"
    "也许对于这里的居民来说反倒是轻松了不少。"
    "而对于我而言，更多的则是某种怀念和感伤。"
    stop music fadeout 5.0
    pause 1.0 hard
    play voice "voice/希菲尔/000100010.ogg"
    stranger "凉君......"
    pause 0.5 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play music second_103 fadein 3.0 if_changed
    scene set only xfe_cg bridge normal
    with slowdissolve
    pause 0.5 hard
    "希菲尔再次出现了。"
    "一样的问候，一样的表情，一样的时机，就好像早就安排好了一般。"
    "她的身影并不是很显眼，更像是与周围的雪融为了一体的感觉。"
    play voice "voice/希菲尔/000100020.ogg"
    xfe "现在还是早点回去比较好。"
    play voice "voice/希菲尔/000100040.ogg"
    xfe "你的家人，也在等着你。"
    me01 "希菲尔才是，这个时候不回去没问题吗？"
    pause 0.1 hard
    scene set only xfe_cg bridge happy
    with dissolve
    play voice "voice/希菲尔/000100050.ogg"
    xfe "我也正准备回去哟~"
    "{rb}我{/rb}{rt}Watashi{/rt}？"
    "也许是因为一直以来希菲尔说的话都比较晦涩难懂。"
    "看似不经意的措辞改变也引起了我的注意。"
    me01 "不用“希菲尔”自称了吗？"
    pause 0.1 hard
    scene set only xfe_cg bridge normal
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/希菲尔/000100060.ogg"
    xfe "我也改变了~"
    play voice "voice/希菲尔/000100070.ogg"
    xfe "即使看起来没有改变，但也有已经改变了的东西。"
    play voice "voice/希菲尔/000100080.ogg"
    xfe "因为时间从来不等人的。"
    play voice "voice/希菲尔/000100090.ogg"
    xfe "而我们，也只能继续向前迈进了......"
    pause 1.0 hard
    scene white
    with slowdissolve
    pause 2.0 hard
    "说完，希菲尔的身影消失了。"
    "与她一同消失的，还有这场温柔的雪。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day202.kindergarten_event03:
    $ flcam.move(0, 0, 0)
    scene set only school evening outside xuejian
    with dissolve
    pause 1.0 hard
    me01 "那个......"
    pause 0.5 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    show lhx_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030100450.ogg"
    lhx "是来接人的吧，我在想也差不多到放学的时间了。"
    me01 "我还什么都没说呢。"
    show lhx_dzf_b3 b3 b3_n1
    play voice "voice/立花希/030100460.ogg"
    lhx "因为爱衣说“凉君”会来接她。"
    me01 "初次见面，能和爱衣成为朋友真是太好了。"
    play music second_108 fadein 3.0 if_changed
    show lhx_dzf_b3 b3 b3_s1
    play voice "voice/立花希/030100520.ogg"
    lhx "虽然从年龄上看没什么问题，但是不知为何，我总是被当成是这里的学生看待。"
    me01 "......欸，你是老师吗？！"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030100510.ogg"
    lhx "很奇怪吗？"
    me01 "失、失礼了。"
    me01 "不过话说回来，比起年龄你的外表才是问题的关键吧。"
    show lhx_dzf_b2 b2 b2_h3
    play voice "voice/立花希/030100530.ogg"
    lhx "是的，毕竟我的外表怎么看都是非常成熟的大人呢~"
    play voice "voice/立花希/030100540.ogg"
    lhx "而且不仅是外表看起来成熟，精神上也是如此，所以一定是被大家当成是成熟的大姐姐了吧~"
    me01 "不，那个......"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/030100550.ogg"
    lhx "所以做老师的话一定更应景吧。"
    me01 "虽然很遗憾，不过肯定还是幼儿园的小朋友这个设定更加的适合你。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030100560.ogg"
    lhx "我好像出现幻听了，如果不是幻听的话我可能已经发飙了。"
    show lhx_dzf_b3 b3 b3_s1
    play voice "voice/立花希/030100570.ogg"
    lhx "不过退一步来说我还不是老师，只是单纯来帮忙的而已。"
    "原来之前千川老师说的就是这孩子吗。"
    me01 "让我猜猜看，立花老师的工作不是管理小朋友，而是陪他们一起玩吧？"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030100580.ogg"
    lhx "没有一起玩的打算，硬要说的话我其实不擅长应付小孩子。"
    pause 0.5 hard
    $ flcam.move(2250, 150, 750, duration=1.5)
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_sp2 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/千波/210100140.ogg"
    qb "飞机场老师，你在外面做什么呢？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030100590.ogg"
    lhx "今天的幻听还真多啊。"
    hide lhx_dzf_b3
    $ flcam.move(4500, 300, 900, duration=1.5)
    show qianbo_dzf_b1 b1 b1_sp2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/210100150.ogg"
    qb "啊，昨天的凉君男。"
    me01 "你说的没错，今天似乎很容易出现幻听。"
    stop music fadeout 5.0
    pause 0.5 hard
    $ flcam.move(2250, 250, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110100440.ogg"
    aiyi "大哥哥，你放学了吗？"
    me01 "是啊，翔子姐姐让我来接你了。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110100450.ogg"
    aiyi "那在大姐姐回来之前，来和我们一起玩吧~"
    pause 1.0 hard
    scene black
    $ flcam.move(0, 0, 0)
    with right2left_02
    pause 1.0 hard
    scene set only school evening inside xuejian
    with right2left_02
    pause 2.0 hard
    play music second_115
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030100600.ogg"
    lhx "我先去千川老师那里了。"
    me01 "还有别的工作吗？"
    show lhx_dzf_b2 b2 b2_ga2
    play voice "voice/立花希/030100610.ogg"
    lhx "在幼儿园的小朋友全部回家之前都不算结束。"
    me01 "看来当幼儿园的老师也挺不容易的。"
    show lhx_dzf_b2 b2 b2_h3
    play voice "voice/立花希/030100640.ogg"
    lhx "那是自然，回头见~"
    pause 0.5 hard
    play sound jiaobu2
    show lhx_dzf_b2 b2 b2_h3 at walkout_r(0.5)
    pause 2.0 hard
    $ flcam.move(3800, 250, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s3 onlayer m1:
        xpos 0.6
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/110100460.ogg"
    aiyi "大哥哥，小桃她有话要说。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110100470.ogg"
    aiyi "来吧小桃。"
    show ycxt_dzf_b1 b1 b1_s2 at flu_down(0.15, 20):
        xpos 0.6
    play voice "voice/小桃/220100110.ogg"
    ycxt "呜，嗯......"
    "原本躲在爱衣身后的小桃畏畏缩缩地走了出来。"
    pause 0.5 hard
    hide aiyi_dzf_b1
    show ycxt_dzf_b1 b1 b1_s2:
        xpos 0.6
        linear 0.5 xpos 0.5
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/小桃/220100120.ogg"
    ycxt "那、那个......昨天的事，谢谢你。"
    show ycxt_dzf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.5
    pause 0.5 hard
    play sound jump_1
    show ycxt_dzf_b1 b1 b1_s1:
        xpos 0.5
        linear 0.5 xpos 0.6
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(3800, 250, 750, duration=1.5)
    pause 0.5 hard
    "说完就立刻躲回了爱衣身后。"
    "看起来是真的很怕生。"
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_h2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/210100160.ogg"
    qb "还没到需要鞠躬道谢的程度嘛。"
    me01 "你这家伙还真是让人喜欢不起来。"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a3 at flu_up(0.15, 30):
        xpos 0.3
    play voice "voice/千波/210100170.ogg"
    qb "人家才不会向你鞠躬的呢！"
    me01 "果然是个傲娇吗。"
    $ flcam.move(-2250, 250, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/小桃/220100130.ogg"
    ycxt "那、那个......"
    hide qianbo_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/220100140.ogg"
    ycxt "凉君和爱衣住在一起了吗？"
    me01 "算是吧。"
    "对小孩子应该没什么好隐瞒的吧。"
    $ flcam.move(2250, 250, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/110100480.ogg"
    aiyi "不只是这样哦，翔子姐姐也住在一起的。"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/220100150.ogg"
    ycxt "是这样吗？"
    stop music fadeout 5.0
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/220100160.ogg"
    ycxt "凉君你......结婚了吗？"
    play music second_106 fadein 3.0 if_changed
    me01 "什么？"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110100490.ogg"
    aiyi "大哥哥你结婚了？"
    "结婚......和谁？"
    show ycxt_dzf_b1 b1 b1_s1
    play voice "voice/小桃/220100170.ogg"
    ycxt "我在想是不是因为结婚了所以才会住在一起的。"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at flu_up(0.15, 30):
        xpos 0.3
    play voice "voice/千波/210100180.ogg"
    qb "{size=72}喂！！！{/size}"
    me01 "干嘛突然大喊大叫的啊。"
    show qianbo_dzf_b1 b1 b1_a1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/210100190.ogg"
    qb "爱衣和这个男人结婚什么的，怎么可能相信！"
    me01 "这句话应该由我来说吧！编故事的话拜托对象至少是个成熟的大姐姐啊。"
    pause 0.5 hard
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/110100500.ogg"
    aiyi "对啊，凉君是爱衣的大哥哥嘛。"
    play voice "voice/小桃/220100180.ogg"
    ycxt "那凉君和爱衣的姐姐结婚了吗？"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 30):
        xpos 0.3
    play voice "voice/千波/210100200.ogg"
    qb "{size=72}怎么可能相信！！！{/size}"
    me01 "结婚这个前提本身就是错误的！"
    hide qianbo_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/220100190.ogg"
    ycxt "那......是情人吗？"
    me01 "你说情人，没想到竟然还知道这个词......"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/220100200.ogg"
    ycxt "我听奶奶说的，没有结婚的话住在一起的都是情人。"
    me01 "虽然大多数情况是这样没错，但我只是一个食客罢了。"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/220100210.ogg"
    ycxt "食客？"
    me01 "就是虽然住在一起，但还是外人的意思。"
    $ flcam.move(2250, 250, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/110100510.ogg"
    aiyi "才不是外人呢。大哥哥是爱衣的大哥哥！"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110100520.ogg"
    aiyi "而且将来的事还不一定呢~"
    play voice "voice/小桃/220100220.ogg"
    ycxt "将来要结婚吗？"
    hide aiyi_dzf_b1 
    hide ycxt_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    show qianbo_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/210100210.ogg"
    qb "和爱衣？"
    me01 "怎么可能！"
    play voice "voice/千波/210100220.ogg"
    qb "和爱衣的姐姐吗？"
    me01 "......"
    "本能地犹豫了一下。"
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/210100230.ogg"
    qb "难道说难道说，是和我？"
    me01 "唯独这一点还是饶了我吧。"
    show qianbo_dzf_b1 b1 b1_h3
    play voice "voice/千波/210100240.ogg"
    qb "我虽然还是个小孩子，但请别把我当成傻瓜好吗。"
    me01 "知道了知道了，别再卖弄你那毫无价值的姿色了。"
    show qianbo_dzf_b1 b1 b1_ga1
    play voice "voice/千波/210100250.ogg"
    qb "不是以身体为目的的话，那就是财产了。"
    me01 "你把我当成什么人了！"
    show qianbo_dzf_b1 b1 b1_a1
    play voice "voice/千波/210100260.ogg"
    qb "与其牺牲自己的朋友，不如就由我来代替她吧！"
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    $ flcam.move(-2250, 250, 750, duration=1.5)
    pause 0.5 hard
    play sound yangmu
    show yangmu onlayer m2:
        xalign 0.49 yalign 0.53 zoom 0.7
    play voice "voice/小桃/220100230.ogg"
    ycxt "千波好帅~"
    "陪这群孩子玩真是累人啊......"
    show qianbo_dzf_b1 b1 b1_ga2
    play voice "voice/千波/210100270.ogg"
    qb "哄骗爱衣，让爱衣的大姐姐养着你，最后再将她们抛弃是吧。"
    me01 "你的思考方式有问题啊。"
    $ flcam.move(0, 200, 600, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/110100530.ogg"
    aiyi "千波，大哥哥才不会做这么过分的事呢。"
    show qianbo_dzf_b1 b1 b1_a3
    play voice "voice/千波/210100280.ogg"
    qb "不能被骗了，比起爱情男人更重视金钱的！"
    hide yangmu
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    hide qianbo_dzf_b1
    show qianbo_dzf_b2 b2 b2_sp1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    me01 "好乖好乖。"
    play sound jump_1
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at flu_up(0.15, 30):
        xpos 0.3
    play voice "voice/千波/210100290.ogg"
    qb "别摸我的头啊！！！"
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/220100240.ogg"
    ycxt "我从奶奶那里听说过，这个叫“美人局”。（注释：丈夫让妻子去勾引其他男人，从而获取金钱的手段。）" 
    me01 "所以说都是误会......"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black 
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 2.0 hard
    scene set only sky night xuejian
    with dissolve
    pause 2.0 hard

label day202.myroom_event01:
    scene set only home night my_room xuejian
    with dissolve
    pause 1.0 hard
    "晚饭过后简单地洗漱了一番，我便回到了自己的房间。"
    "折腾了一天也是够累的，尤其是“幼儿社”的活动可谓是空前地消耗体力。"
    "想到这里一阵困意开始席卷全身......"
    pause 1.0 hard
    scene black
    with side2cent_slow 
    pause 3.0 hard

label day202.memory_event08:
    nvl clear
    pcenter "    雪——"
    pause 0.5 hard
    nvl clear
    pcenter "    雪花纷然飘落。"
    pause 0.5 hard
    nvl clear
    with dissolve
    play music second_117 fadein 3.0 if_changed
    "桥上的身影。"
    "我想要见她。"
    "尽管印象中她的身影早已模糊。"
    "但是还是想要见到她。"
    "说起理由的话......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory6
    with dissolve
    pause 0.5 hard
    "大概是觉得她的身影看起来有些寂寞吧。"
    "过去的我们，究竟是什么样的关系呢？"
    "脑海里，回忆正在渐渐苏醒——"
    pause 1.0 hard
    scene white
    with slowdissolve
    pause 2.0 hard
    scene set only balltower snow day xuejian alpha
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "那一天我偶然路过了这座钟楼，四周没有行人的身影显得格外地安静。"
    "我毫无目的地走着，足迹铺满了整片雪地。"
    pause 1.0 hard
    scene set only balltower snow day big
    with dissolve
    pause 1.0 hard
    "好冷。"
    "手脚都冻僵了。"
    "空虚的感觉涌上心头。"
    "回去吧......"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/000200050.ogg"
    xfe "又被找到了~"
    pause 2.0 hard
    play music second_103 fadein 3.0 if_changed
    scene set only xfe_cg normal
    with slowdissolve
    pause 1.0 hard
    "仿佛听见了我的想法一般。"
    "她的身影出现在了漫天飞舞的白雪之中。"
    play voice "voice/希菲尔/000200060.ogg"
    xfe "为什么呢......感觉总能被你找到。"
    "她笑了。"
    "我决定鼓起勇气也对她说点什么。"
    "可是这种时候应该说些什么呢？"
    "这对当时的我而言可谓是人生中最大的难题吧。"
    me01 "你在这里做什么？"
    pause 0.1 hard
    scene set only xfe_cg happy
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.5 hard
    play voice "voice/希菲尔/000200070.ogg"
    xfe "躲猫猫哟~"
    me01 "躲猫猫？"
    me01 "在这大雪中吗？"
    pause 0.1 hard
    scene set only xfe_cg normal
    with dissolve
    play voice "voice/希菲尔/000200080.ogg"
    xfe "你是第二个哟~"
    me01 "第二个？"
    play voice "voice/希菲尔/000200090.ogg"
    xfe "嗯，能发现希菲尔的人。"
    play voice "voice/希菲尔/000200100.ogg"
    xfe "希菲尔我呢，很擅长躲猫猫的。"
    me01 "“希菲尔”说的你自己吗？"
    play voice "voice/希菲尔/000200110.ogg"
    xfe "是啊，“希菲尔”就是希菲尔。"
    me01 "虽然不是很清楚，但那是你的名字吧？"
    pause 0.1 hard
    scene set only xfe_cg happy
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/000200120.ogg"
    xfe "是的哟~"
    "名叫“希菲尔”的女孩子开心地点了点头。"
    "看着她的笑容，想必她一定很喜欢这个的名字吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian alpha
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200130.ogg"
    xfe "你也有名字吗？"
    me01 "那是当然。"
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/000200140.ogg"
    xfe "叫什么呢？"
    me01 "神野凉。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200150.ogg"
    xfe "哈鲁咔咪君？"
    me01 "才不是那种奇怪的名字呢，神·野·凉。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200160.ogg"
    xfe "哈鲁咔......凉君？"
    me01 "请不要再“哈鲁哈鲁”地叫我了。"
    hide ts_xfe_yjz_b3 with None
    pause 0.1 hard
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200170.ogg"
    xfe "那就凉君~"
    me01 "这样倒是没问题。"
    "听起来有点像小名。"
    "除了母亲和翔子以外，还是第一次有人这么叫我。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200180.ogg"
    xfe "凉君。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200190.ogg"
    xfe "凉君凉君~"
    "为什么明明只是一个名字，她却能笑得那么开心呢？"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200200.ogg"
    xfe "希菲尔现在最喜欢“神野凉”这个名字了哟~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    $ flcam.move(0, 0, 400, duration=30.0, warper='ease_quad')
    pause 1.0 hard
    nvl clear
    nvl_narrator "就这样，我们成为了能够直呼对方名字的好朋友。"
    nvl_narrator "尽管内心深处仍然会感到不安。"
    nvl_narrator "但我也如获至宝一般地默许了这样的关系。"
    nvl_narrator "也许就如同我对她来说是特别的一样，希菲尔对于那时的我而言也是特别的存在。"
    nvl_narrator "即便只是刚认识不久，我也如此坚信着。"
    nvl_narrator "对于孤独的我而言，在这座陌生的城市里终于有了一个能够让我敞开心扉的“朋友”。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowdissolve
    pause 2.0 hard
    "隔日——"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    play music second_117 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200210.ogg"
    xfe "我来找你玩了哟，凉君~"
    "这一次我刚到钟楼广场，希菲尔就向我跑了过来。"
    "在那之后经常能够在这里看到她的身影。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200220.ogg"
    xfe "“可以来玩”千冬这样对我说了，所以我就来了。"
    me01 "千冬？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200230.ogg"
    xfe "她是第一个发现希菲尔的人哟~"
    show ts_xfe_yjz_b3 b3 b3_n1
    play voice "voice/希菲尔/000200240.ogg"
    xfe "所以希菲尔也最喜欢千冬了~"
    show ts_xfe_yjz_b3 b3 b3_h1
    play voice "voice/希菲尔/000200250.ogg"
    xfe "凉君也能找到希菲尔，所以也最喜欢凉君你了~"
    "也就是说所有能“找到”她的人都是她的朋友吗？"
    "好奇怪的理由。"
    "我被称作“第二”的原因就是这个吧。"
    me01 "不过，希菲尔你为什么要玩躲猫猫呢？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200260.ogg"
    xfe "希菲尔我......其实是不能被大家找到的哟。"
    me01 "怎么回事？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200270.ogg"
    xfe "因为如果希菲尔的存在被大家发现的话，千冬会很困扰的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200280.ogg"
    xfe "所以昨天被凉君找到的时候，本来以为千冬会生气的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200290.ogg"
    xfe "但是呢，千冬却说“没关系”，所以希菲尔就继续来找凉君了。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200300.ogg"
    xfe "凉君，来和希菲尔一起玩吧~"
    "她握住了我的手。"
    "从手心传来了温和且柔软的触感。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200320.ogg"
    xfe "那走吧~"
    me01 "要去哪里呢？"
    show ts_xfe_yjz_b3 b3 b3_h1
    play voice "voice/希菲尔/000200330.ogg"
    xfe "去哪里都可以哟~在春天来临之前去哪里都可以的。"
    me01 "那个......"
    show ts_xfe_yjz_b3 b3 b3_n2
    play voice "voice/希菲尔/000200340.ogg"
    xfe "不行？"
    me01 "稍等我一下。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    pause 1.0 hard
    "从来没有想过除了翔子以外，还有第二个能够一起玩耍的伙伴。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian alpha
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    "那么至少这一次。"
    "就这一次就好。"
    me01 "我去拿点东西，然后我们就出发吧。"
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowdissolve
    pause 1.0 hard
    nvl clear
    pcenter "　　――是啊{p}　　　　　　如果是和她一起的话......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street snow day road1 xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "我们一起牵着手走在绵长的雪道上。"
    "享受彼此并肩前行的过程，谁也没有去思考目的地在哪。"
    "因为比起结果，过程更加吸引我。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2:
        xpos 0.5
    me01 "我说希菲尔。"
    show ts_xfe_yjz_b2 b2 b2_sp3
    play voice "voice/希菲尔/000200350.ogg"
    xfe "什么？"
    me01 "我们就这样一直走下去吗？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200360.ogg"
    xfe "是啊~"
    me01 "你不会冷吗？"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/000200370.ogg"
    xfe "希菲尔看起来很冷吗？"
    me01 "我只是问一下。"
    "希菲尔的穿着看起来很单薄，光是看着她就连我都不自觉地打起寒战来。"
    me01 "而且也没有撑伞。"
    me01 "这样的话积雪落在身上有点碍事。"
    hide ts_xfe_yjz_b3 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200380.ogg"
    xfe "撑伞？"
    me01 "还有手套。"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200390.ogg"
    xfe "手套？"
    me01 "长靴也......"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000200400.ogg"
    xfe "长靴？"
    me01 "希菲尔你没见过这些东西吗？"
    "与希菲尔不同，此刻的我身上被厚重的衣物包裹着。"
    show ts_xfe_yjz_b3 b3 b3_s3
    play voice "voice/希菲尔/000200410.ogg"
    xfe "凉君很冷吗？"
    me01 "毕竟是冬天嘛。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000200420.ogg"
    xfe "是希菲尔的错吗？"
    me01 "怎、怎么了突然......"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/000200430.ogg"
    xfe "要怎么样才能让凉君不觉得冷呢？"
    me01 "我这里有伞，希菲尔你......要一起进来吗？"
    "原本只是想要确认女孩是不是会冷，却反过来被对方担心了。"
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/000200440.ogg"
    xfe "这个是......情人伞？"
    me01 "为什么撑伞都不知道的你却会知道“情人伞”啊......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/000200450.ogg"
    xfe "因为在千冬给希菲尔讲的故事里有出现过哟~"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 2.0 hard
    "希菲尔一边说着，一边开心地朝我靠了过来。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory2
    with dissolve
    pause 1.0 hard
    "我们就这样一起撑着伞。"
    "继续向前走着。"
    "不知不觉中，身后的两行足迹在空旷的雪道上蔓延开来——"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day203
