label day04:
    bookmark
    $ save_name = _("Day 04")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_yinghua spring
    with dissolve
    show backend_bg01 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date03 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    $ flcam.move(0, 0, 0)
    play sound rill
    scene set only school day road yinghua
    with dissolve
    pause 3.0 hard
    scene set only school day library yinghua
    with dissolve
    pause 3.0 hard
    play music first_05 fadein 3.0 if_changed
    $ flcam.move(0, -100, 400, duration=1.5)
    "放学后的图书馆几乎成为了我每日打卡的必经场所。"
    "为了彻底调查雷亚的身世，我几乎翻阅了这里所有关于观景台信息的书籍。"
    "可能是见我每天都往图书馆跑的缘故，学生会的那帮家伙更加频繁地派人来劝诱我了。"
    "虽然每次都以天协的名义搪塞过去，但再这么下去总归不是办法。"
    me01 "今天一定要查清楚是怎么回事。"
    "先前因为得到了铃音同学的帮助，我才能顺利地找到想要找的资料。"
    "可是今天......"
    $ flcam.move(-3800, -600, 900, duration=1.5)
    pause 2.0 hard
    $ flcam.move(3800, -600, 900, duration=1.5)
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 2.0 hard
    with vpunch
    "为什么偏偏这个时候谁都不在啊？！"
    me01 "要是有个人能帮忙的话就好了。"
    play voice "voice/日向怜/0106290.ogg"
    stranger "......虽然是没问题，遇到什么麻烦了吗？"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    me01 "日向同学，你在的话早一点出现啊，吓了我一跳。"
    play voice "voice/日向怜/0106300.ogg"
    rxl "你在调查什么？"
    me01 "是关于死神美少女的生活习性......之类的。"
    show rxl_xzf_b1 b1 b1_ga1
    me01 "我、我是认真的，请不要用那样的眼神看我。"
    pause 0.5 hard
    hide rxl_xzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/青木铃音/0502560.ogg"
    lingyin "啊，神野同学，还有日向同学也在~"
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0106310.ogg"
    rxl "小铃，辛苦了~"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0502590.ogg"
    lingyin "天协那边的活动怎么样了？"
    show rxl_xzf_b2 b2 b2_a1
    play voice "voice/日向怜/0106320.ogg"
    rxl "呜——"
    show lingyin_xzf_b1 b1 b1_ga1
    play voice "voice/青木铃音/0502580.ogg"
    lingyin "真是容易理解的回答呢，谢谢了。"
    show rxl_xzf_b2 b2 b2_n1
    play voice "voice/日向怜/0106330.ogg"
    rxl "比起这个，小凉他好像需要你的帮助。"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0502600.ogg"
    lingyin "神野同学，这次也是来调查东西吗？"
    me01 "是的。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106340.ogg"
    rxl "你说也是......小凉你对死神很感兴趣吗？"
    stop ambience1 fadeout 5.0
    stop music fadeout 5.0
    show lingyin_xzf_b1 b1 b1_sp1
    play voice "voice/青木铃音/0502610.ogg"
    lingyin "......死神？"
    me01 "只是我的个人兴趣罢了。"
    "想要解释清楚这一切似乎有些麻烦。"
    play music first_17 fadein 3.0 if_changed
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0502620.ogg"
    lingyin "在新生里面也有很多呢，喜欢死神的人。"
    show rxl_xzf_b1 b1 b1_s1
    play voice "voice/日向怜/0106350.ogg"
    rxl "入学的时候大家也都听说了。不过那些都只是都市传说罢了。"
    show lingyin_xzf_b2 b2 b2_n2
    play voice "voice/青木铃音/0502630.ogg"
    lingyin "我也很在意是谁流传下来的说法。"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106360.ogg"
    rxl "也不知道是从什么时候就开始了。"
    play voice "voice/青木铃音/0502640.ogg"
    lingyin "一诚同学去年调查过了吧，结果却是什么收获都没有。"
    show rxl_xzf_b2 b2 b2_ga1
    play voice "voice/日向怜/0106370.ogg"
    rxl "一诚君也是个三分钟热度的人呢，作为超自然现象爱好者而言。"
    hide lingyin_xzf_b2
    show lingyin_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0502650.ogg"
    lingyin "正因为是超自然现象爱好者才更容易流传这些传说的吧？比起天文学，关于超自然现象的文献比较容易引起关注。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106380.ogg"
    rxl "小凉，虽然不知道你想了解的是关于哪个传闻中提到的死神，但就算调查了也不会有什么太大帮助的。"
    me01 "请稍等一下。"
    hide rxl_xzf_b1
    hide lingyin_xzf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    me01 "大家都知道雷亚的事情吗？"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106390.ogg"
    rxl "雷亚？"
    $ flcam.move(0, -350, 750, duration=1.5)
    show lingyin_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    play voice "voice/青木铃音/0502660.ogg"
    lingyin "是谁的名字吗？"
    me01 "是死神的名字。"
    show rxl_xzf_b1 b1 b1_s1
    play voice "voice/日向怜/0106400.ogg"
    rxl "死神也有名字吗？"
    show lingyin_xzf_b1 b1 b1_s1
    play voice "voice/青木铃音/0502670.ogg"
    lingyin "死神就是死神吧。"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106410.ogg"
    rxl "是谁添油加醋的结果吗？"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0502680.ogg"
    lingyin "这样的说法有很多，既然是都市传说，就得让它成为能够与时俱进的东西才行，就像一般的传统文化那样。"
    show rxl_xzf_b2 b2 b2_ga1
    play voice "voice/日向怜/0106420.ogg"
    rxl "不可以哟小凉，随便添油加醋什么的。"
    me01 "等等，都市传说？你们究竟在说什么？"
    show rxl_xzf_b2 b2 b2_n1
    play voice "voice/日向怜/0106430.ogg"
    rxl "是关于死神的传闻哟。我想大致内容应该就是能够把遇见的情侣拆散之类的。"
    show lingyin_xzf_b1 b1 b1_h1
    play voice "voice/青木铃音/0502690.ogg"
    lingyin "所以那位死神在学生口中就被称作“恋爱死神”了。"
    show rxl_xzf_b2 b2 b2_ga1
    play voice "voice/日向怜/0106440.ogg"
    rxl "就是让情侣之间的恋爱走向死亡的意思吧？"
    "这所学校居然还有这样的传闻吗。"
    me01 "但是，为什么在班里却从来没有听大家提起过死神的事情呢？"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0502700.ogg"
    lingyin "对都市传说感兴趣的多半是一年级的学生，升上二年级以后一般就不会在意了吧。"
    show rxl_xzf_b2 b2 b2_sp1
    play voice "voice/日向怜/0106450.ogg"
    rxl "话说小凉你，一定也是从哪里听说了才会感兴趣的吧？可是你看起来似乎并不知道这些。"
    me01 "虽然是这样，但也不完全是。"
    show lingyin_xzf_b1 b1 b1_sp1
    play voice "voice/青木铃音/0502710.ogg"
    lingyin "神野同学不就是想调查关于死神的都市传说吗？"
    me01 "我觉得这其中大概是有些误会。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106460.ogg"
    rxl "为什么是大概啊？"
    "连我自己都被搞糊涂了。"
    me01 "那个，关于死神的传闻，能详细和我说明一下吗？"
    show rxl_xzf_b1 b1 b1_s1
    play voice "voice/日向怜/0106470.ogg"
    rxl "就算要我详细说明，传闻的版本实在太多了，我也不知该从何说起。"
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0502720.ogg"
    lingyin "虽然传闻有很多种，但相同的部分大致就是日向同学刚刚说的那些哟。"
    me01 "是指拆散情侣之类的吗？"
    play voice "voice/青木铃音/0502730.ogg"
    lingyin "是的。"
    me01 "那关于死神的相貌之类的呢？"
    show rxl_xzf_b1 b1 b1_sp1 
    play voice "voice/日向怜/0106480.ogg"
    rxl "因为是死神所以会拿着镰刀吧？"
    show lingyin_xzf_b2 b2 b2_n2
    play voice "voice/青木铃音/0502740.ogg"
    lingyin "不仅是相貌，就连年龄和性别也千差万别。"
    me01 "出现地点呢？"
    show rxl_xzf_b1 b1 b1_n1
    play voice "voice/日向怜/0106490.ogg"
    rxl "既然是樱华校的都市传说，那就是在学校里吧？"
    show lingyin_xzf_b2 b2 b2_ga2
    play voice "voice/青木铃音/0502750.ogg"
    lingyin "一般来说的话是这样的。"
    me01 "有没有听说过在观景台出没的死神呢？"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106500.ogg"
    rxl "小铃，你听说过吗？"
    show lingyin_xzf_b2 b2 b2_n2
    play voice "voice/青木铃音/0502760.ogg"
    lingyin "不好说，这种传闻说不定也是存在的吧。"
    stop music fadeout 5.0
    "也就是说并不能确定大家口中的传闻说的就是雷亚。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with dissolve
    play music first_25 fadein 3.0 if_changed
    pause 1.0 hard
    "不过对于传闻这种东西我是不打算全盘接受的。"
    "可让我在意的地方还是有的，如果她们口中的那位死神真是雷亚的话，那她也会拆散我与某人的恋爱吗？"
    pause 1.0 hard
    scene set only school day library yinghua
    with right2left
    pause 1.0 hard
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    show rxl_xzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106510.ogg"
    rxl "小凉进入思考模式了。"
    play voice "voice/青木铃音/0502770.ogg"
    lingyin "之前也有过这样的情况吗？"
    me01 "这件事就先暂且放一边吧。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106530.ogg"
    rxl "欢迎回来，小凉~"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0502780.ogg"
    lingyin "神野同学，这次来图书馆也是要找什么书的吧？"
    me01 "是啊，正在为没人帮忙而发愁呢。"
    hide rxl_xzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_h1
    play voice "voice/青木铃音/0502800.ogg"
    lingyin "是什么样的书呢？"
    me01 "是关于幻觉的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua
    with dissolve
    pause 1.0 hard
    "当人们声称自己看到了幽灵或外星人这种超自然的存在，首先想到的都是幻觉。"
    "也许是自己太累了吧？诸如此类的想法算是再正常不过的了。"
    "如果我所经历的一切都不是幻觉，那相对的我也有理由相信那些传闻所言非虚。"
    "毕竟雷亚当时也说了，她是割取噩梦的死神，所谓的噩梦至今为止我都没能彻底搞明白是怎么回事。"
    "但如果结合传闻来看的话，这一切又似乎说得通了。"
    pause 1.0 hard
    scene set only school day library yinghua
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show namelist2 onlayer b2 at basicfade_c2u
    "人在什么样的场合下才会产生幻觉——主要原因有药物、压力、酒精、心理疾病、因为发热、重度失血或头部受到猛烈击打而产生的脑损伤等。"
    "乍看之下无论是何种原因都有着共通点。"
    "它们都是由多巴胺和内咖肽分泌过多所导致的。"
    "这样一来人就会陷入某种与睡眠类似的精神状态。"
    "也正因如此，此刻的想法、过去的回忆什么的都会以幻觉的形式刺激大脑皮层的中枢神经。"
    "如果雷亚是幻觉的话，那我每晚的行为不就像是梦游一样了吗。"
    "难道是我始终忘不掉那段在观景台的经历，才会强迫性地把自己内心深处的那个“她”幻想成雷亚不成。"
    "也就是说雷亚是我创造出来的死神？"
    stop music fadeout 5.0
    hide namelist2
    pause 2.0 hard
    with vpunch
    me01 "这种电影里才有的情节怎么可能发生在我身上啊！"
    pause 1.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106540.ogg"
    rxl "小凉，明白什么了吗？"
    play music first_07 fadein 3.0 if_changed
    me01 "虽然不是很清楚，但似乎领悟了一些并不愉快的东西。"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106550.ogg"
    rxl "不愉快的东西是什么样的？"
    me01 "这个暂时还没办法得到答案。"
    play voice "voice/日向怜/0106560.ogg"
    rxl "想要什么样的答案？"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106570.ogg"
    rxl "小凉，你为什么会想要调查关于幻觉的事情呢？"
    me01 "我有权保持沉默吗？"
    show rxl_xzf_b1 b1 b1_a1
    play voice "voice/日向怜/0106580.ogg"
    rxl "没有，毕竟人家等了你那么久。"
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0502810.ogg"
    lingyin "日向同学，神野同学他非常地困扰呢。"
    show rxl_xzf_b1 b1 b1_c1
    show han onlayer m2:
        xalign 0.72 yalign 0.37
    play voice "voice/日向怜/0106590.ogg"
    rxl "但我真的很在意嘛~"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0502820.ogg"
    lingyin "在图书馆里还请保持安静。"
    hide han
    show rxl_xzf_b1 b1 b1_s1
    play voice "voice/日向怜/0106600.ogg"
    rxl "......对不起。"
    hide rxl_xzf_b1
    hide lingyin_xzf_b1
    pause 0.5 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "今天谢谢你们了，铃音同学、日向同学。"
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0502830.ogg"
    lingyin "不用客气，能帮上忙真是太好了~"
    me01 "那我也差不多要走了。"
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0106610.ogg"
    rxl "这么说来，不赶快回去的话......"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0502840.ogg"
    lingyin "图书馆也快要关门了，今天就在这里解散吧。"
    hide lingyin_xzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0106620.ogg"
    rxl "小凉，要一起回去吗？"
    me01 "抱歉，我还有一个必须要去的地方。"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.7
    "看着日向怜一脸犬化的表情，我也只能双手合十地向她道歉。"
    "关于我遇到雷亚的事还是暂时向她们保密比较好。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with dissolve
    pause 2.0 hard

label day04.starview_event01:
    play ambience1 zhiliao
    scene set only starview evening guardrail
    with slowdissolve
    play music first_22 fadein 3.0 if_changed
    pause 3.0 hard
    $ flcam.move(0, 3500, 1500, duration=2.5)
    pause 2.5 hard
    play voice "voice/圣护院/1000010.ogg"
    stranger "这些脚印果然是别人留下的吧。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 1.0 hard
    show shy_yjf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/圣护院/1000020.ogg"
    stranger "好事之徒吗？"
    "再怎么说普通的游客也不可能不顾上面的警示标语擅自闯入，更何况根据脚印的新旧判断，此人还不止一次出入这里。"
    "到底是出于什么目的才会不顾阻拦地前往观景台呢？"
    $ flcam.move(0, -450, 1000, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000030.ogg"
    stranger "虽然不知道有什么企图，但请不要给我添麻烦。"
    "女子盯着护栏上醒目的“禁止进入”字样，意味深长地叹了口气。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/1000040.ogg"
    stranger "在到达终点之前还需要搬开一些绊脚石吗。"
    "如果那个人的目的仅仅是观光倒也是无所谓，但如果......"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000050.ogg"
    stranger "到底是如何呢。"
    hide shy_yjf_b1
    $ flcam.move(3500, -200, 600, duration=1.5)
    play sound move_1
    pause 2.0 hard
    "就在这时，身后传来了脚步声。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/1000060.ogg"
    stranger "......又来了吗？"
    show shy_yjf_b1 b1 b1_s1
    stop music fadeout 5.0
    "她有些无奈地撩了下那头靓丽的长发。"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview evening road
    with dissolve
    pause 2.0 hard
    scene set only starview evening guardrail
    with right2left
    pause 0.5 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/1000070.ogg"
    stranger "......"
    play music first_17 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_a1
    play voice "voice/圣护院/1000080.ogg"
    stranger "再往前就是禁区了，观光的话还是请回吧。"
    me01 "抱歉，我是不久前才搬到小镇上来的，我的名字叫神野凉。"
    "虽然猜到对方是来阻止我进入观景台的，但是必要的社交辞令自然是不能少。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000090.ogg"
    stranger "这么说，你果然不知道这座观景台已经不向外人开放了啊？"
    me01 "不，你身后牌匾上写的东西我还是知道的。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/1000100.ogg"
    stranger "那你为什么还要来？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000110.ogg"
    stranger "你应该已经不是第一次来这里了吧？"
    me01 "因为有很重要的事情。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/1000120.ogg"
    stranger "什么事？"
    me01 "从刚才就想问了，这个标识是你立在这里的吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000130.ogg"
    stranger "那倒不是。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/1000140.ogg"
    stranger "我只是发现最近似乎有人擅自闯入观景台，所以有些在意罢了。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/1000150.ogg"
    stranger "言归正传，你到底是来观景台做什么的？"
    me01 "既然不是你修建的围栏，也不是你立下“禁止进入”的标识，那我来这里的目的也没有义务向你汇报吧。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000160.ogg"
    stranger "作为同是这座小镇上的居民，我还是有义务提醒你一下的。"
    me01 "仅仅只是建议吗？"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/1000170.ogg"
    stranger "嘛，差不多是这样。"
    me01 "虽然很感谢你善意的提醒，但还是请你放我过去吧。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000180.ogg"
    stranger "可以的话我倒是更希望看到你尽快离开。"
    me01 "......"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/1000190.ogg"
    stranger "无论如何也要过去吗？"
    me01 "是的。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/1000200.ogg"
    stranger "是非常重要的事？"
    me01 "是的。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/1000210.ogg"
    stranger "什么样的事？"
    me01 "......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/1000220.ogg"
    stranger "不能说吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000230.ogg"
    stranger "不能说也就代表着是什么亏心的事吧？"
    me01 "不是的。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/1000240.ogg"
    stranger "那就回答我。"
    me01 "如果你的目的仅仅是让我离开，大可直接向这里的政府机构投诉，而不是自己在这里向我说教的吧？"
    me01 "既然知道我不止一次来这里也就是说，你对这一带应该也是颇为熟悉了，难道只是碰巧路过而已？"
    me01 "我想你来这里应该也是出于你的某种私人目的而已，既然如此我们各取所需，井水不犯河水岂不更好？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000250.ogg"
    stranger "说来惭愧，的确如你所言。"
    me01 "那就先告辞了。"
    hide shy_yjf_b1
    $ flcam.move(3500, -200, 600, duration=1.5)
    pause 1.0 hard
    "我正打算绕开她进入观景台。"
    "虽说有一定的把握，但刚刚那段话也只是出于试探的目的才说的。"
    "没想到竟然被我言中了，真是幸运啊。"
    "明明没有做亏心事，但此刻心里却有种莫名的罪恶感。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/1000260.ogg"
    stranger "能再问你一个问题吗？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/1000270.ogg"
    stranger "你今后也会一直来这座观景台吗？"
    me01 "是这么打算的。"
    "至少在搞清楚雷亚的秘密之前。"
    "我不会放弃的。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/1000280.ogg"
    stranger "这样啊......"
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1 onlayer m2 at walkout_l(0.5)
    play sound move_1
    pause 2.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 3.0 hard

label day04.starview_event02:
    $ flcam.move(-2800, -200, 600)
    scene set only starview night starview
    with dissolve
    $ flcam.move(2800, -200, 600, duration=5.0, warper='ease_cubic')
    pause 6.0 hard
    "登上观景台的时候夜幕也随之降临。"
    "虽说是黑夜但在星光的点缀下这里也显得格外迷人。"
    "今晚的夜空也溢满了星光。"
    pause 1.0 hard
    play music first_18 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg normal
    with in2out_v2_slow
    pause 2.0 hard
    play voice "voice/天使雷亚/0003170.ogg"
    lst "晚上好。"
    me01 "中午好。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0003190.ogg"
    lst "我能回去吗？"
    me01 "开玩笑的啦，惹你不开心的话我道歉。"
    play voice "voice/天使雷亚/0003200.ogg"
    lst "虽然不是这样，不过我确实想回去了。"
    pause 0.1 hard
    scene set only lisite_cg shy
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0003210.ogg"
    lst "......因为今天感觉胸口闷闷的。"
    me01 "感冒了吗？"
    play voice "voice/天使雷亚/0003220.ogg"
    lst "死神才不会感冒呢。"
    me01 "那发生了什么事了？"
    play voice "voice/天使雷亚/0003230.ogg"
    lst "想捅你的感觉实在快要抑制不住了。"
    me01 "是杀人的冲动啊！"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0003240.ogg"
    lst "回去之前能让我捅一下吗？"
    me01 "当然不行。"
    play voice "voice/天使雷亚/0003250.ogg"
    lst "不会痛的。"
    me01 "即使是这样也不行。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0003260.ogg"
    lst "明明是你自己不好。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0003270.ogg"
    lst "因为你还要继续做噩梦。"
    play voice "voice/天使雷亚/0003280.ogg"
    lst "因为你一直不愿意放弃。"
    me01 "之前就一直想说。"
    play voice "voice/天使雷亚/0003290.ogg"
    lst "......"
    me01 "如果因为无法割取噩梦而让身为死神的雷亚你感到难堪的话，我也想尽可能为你做些什么。"
    me01 "毕竟对我而言，雷亚你也算是我的伙伴了。"
    play voice "voice/天使雷亚/0003300.ogg"
    lst "......"
    me01 "但是啊，回忆这种东西并不是只属于我一个人的东西。"
    me01 "那是记录了我一路走来所有开心与不开心的见证，是所有对我而言重要之人与我共同创造的东西。"
    me01 "所以，如果雷亚你所谓的噩梦指的就是我的回忆本身，唯独这一点我无法退让。"
    me01 "即使是雷亚你的要求，我也不会答应的。"
    play voice "voice/天使雷亚/0003310.ogg"
    lst "......"
    me01 "抱歉。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0003330.ogg"
    lst "人家才不会在意呢。"
    me01 "真的抱歉。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0003340.ogg"
    lst "我说了没什么的。"
    me01 "你能理解真是太好了。"
    play voice "voice/天使雷亚/0003350.ogg"
    lst "反正不管怎么样我都会从你背后狠狠捅下去的。"
    "完全没有明白？！"
    me01 "你的脸有点红啊。"
    me01 "莫非真是身体不舒服？"
    play voice "voice/天使雷亚/0003360.ogg"
    lst "才不是。就因为你完全不肯妥协所以我才会这般苦恼的。"
    me01 "需要我安慰你吗？"
    play voice "voice/天使雷亚/0003370.ogg"
    lst "吵死了你这个变态！"
    play voice "voice/天使雷亚/0003380.ogg"
    lst "本以为今天的你会有所不同的，不过现在又变得废废的了。"
    me01 "如果不从我这里割取噩梦，雷亚的使命就完不成是吗？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0003390.ogg"
    lst "嗯。"
    me01 "但要是我永远都不肯放弃的话，雷亚你打算怎么办？"
    me01 "没有我的同意，雷亚你就无法割取我的噩梦吧？"
    play voice "voice/天使雷亚/0003400.ogg"
    lst "并非如此，不过如果你能主动选择放弃的话我会更开心的。"
    me01 "雷亚你就这么讨厌我的过去吗？"
    play voice "voice/天使雷亚/0003410.ogg"
    lst "嗯。"
    me01 "为什么？"
    play voice "voice/天使雷亚/0003420.ogg"
    lst "不为什么。"
    me01 "你这工作还真是辛苦啊。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0003430.ogg"
    lst "你以为是谁的错啊。"
    me01 "果然是我的问题吗？"
    play voice "voice/天使雷亚/0003440.ogg"
    lst "嗯。"
    me01 "那还真是遗憾啊，死神小姐。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0003450.ogg"
    lst "我绝对会捅你的，变态君。"
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    with dissolve
    pause 1.0 hard
    me01 "对了雷亚。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    with vpunch
    play voice "voice/天使雷亚/0003460.ogg"
    lst "！"
    pause 0.5 hard
    play sound hide_sound
    $ flcam.move(0, -200, 600, duration=1.5)
    hide ts_lst_ssz_b2 with None
    pause 0.1 hard
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play music first_08 fadein 3.0 if_changed
    me01 "这次没有什么实验，放心好了。"
    play voice "voice/天使雷亚/0003470.ogg"
    lst "那、那样的话就好。"
    me01 "我呢，有些事情想要和雷亚你说。"
    show ts_lst_ssz_b1 b1 b1_a2
    play voice "voice/天使雷亚/0003480.ogg"
    lst "什么事？"
    me01 "在说之前可不可以拜托你不要这么防备我啊。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0003490.ogg"
    lst "我才没有防备你。"
    me01 "好了别生气。"
    show ts_lst_ssz_b1 b1 b1_a1
    play voice "voice/天使雷亚/0003500.ogg"
    lst "才没有生气！"
    me01 "哈哈哈。"
    play sound liandao
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2_d b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0003510.ogg"
    lst "为什么要在这里发笑啊！"
    me01 "抱歉抱歉，还请你先把镰刀放下来。"
    show ts_lst_ssz_b2_d b2 b2_ga1
    play voice "voice/天使雷亚/0003520.ogg"
    lst "有种被戏耍了的感觉。"
    me01 "没那回事，我只是觉得雷亚你有的时候就像小孩子一样。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2_d b2 b2_a1
    play voice "voice/天使雷亚/0003530.ogg"
    lst "果然是在戏弄我！"
    me01 "不是你想的那样，我只是稍微有些安心了。"
    "看着眼前率直的女孩，感觉那些传闻的影响顿时不复存在了。"
    me01 "另外我是真的有事想和你说。"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_a2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0003540.ogg"
    lst "什么事，快说！"
    me01 "雷亚你喜欢星星吗？"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0003550.ogg"
    lst "说不定吧。"
    me01 "那要不要和我一起参加天体观测呢？"
    show ts_lst_ssz_b1_d b1 b1_a2
    play voice "voice/天使雷亚/0003560.ogg"
    lst "不要。"
    me01 "别那么快就拒绝嘛。"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0003570.ogg"
    lst "我在这个世界上最最讨厌的事情之一就是和别人亲近了，所以不要。"
    "说起来这家伙的确有一大堆讨厌的事情。"
    me01 "那这么说吧，雷亚你要不要自己来和我一起参加天体观测呢？"
    show ts_lst_ssz_b2 b2 b2_ga1
    play voice "voice/天使雷亚/0003580.ogg"
    lst "你说的话还真是晦涩难懂呢。"
    me01 "比起一个人在这里看星星，不如和我们一起吧？"
    me01 "用望远镜的话，就能看到更加广阔的宇宙了。"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0003590.ogg"
    lst "不要。"
    me01 "为什么啊？"
    show ts_lst_ssz_b2 b2 b2_a1
    play voice "voice/天使雷亚/0003600.ogg"
    lst "我在这个世界上最最讨厌的事情之一就是和变态玩了，所以不要。"
    "变态......是指我吗？"
    me01 "雷亚有用过望远镜吗？"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/0003610.ogg"
    lst "这倒没有。"
    me01 "不想试试看吗？"
    play voice "voice/天使雷亚/0003620.ogg"
    lst "我不知道。"
    "这个别扭鬼。"
    show ts_lst_ssz_b2 b2 b2_n1
    play voice "voice/天使雷亚/0003630.ogg"
    lst "但是，星星什么的就算不用望远镜也可以看得见吧。"
    me01 "有了望远镜就能看到更多更远的星星了呀。"
    "雷亚一边听我说着，一边抬头看着夜空。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 2.0 hard
    play voice "voice/天使雷亚/0003640.ogg"
    lst "在那之后......会怎么样？"
    me01 "那种感觉我也说不明白。"
    play voice "voice/天使雷亚/0003650.ogg"
    lst "即使不明白也想看吗？"
    me01 "不如说正是因为这样所以才想看。"
    me01 "那里一定是像是万花筒一样绚丽的世界吧。"
    stop music fadeout 5.0
    pause 2.0 hard
    scene set only starview night starview
    with dissolve
    pause 1.0 hard
    play music first_30 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0003660.ogg"
    lst "你见过万花筒吗？"
    me01 "无论是谁小的时都玩过吧。"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0003670.ogg"
    lst "......"
    me01 "莫非雷亚你没看过？"
    play voice "voice/天使雷亚/0003680.ogg"
    lst "不行吗。"
    me01 "也没什么不行的，只是觉得太可惜了。"
    show ts_lst_ssz_b2 b2 b2_sp1
    play voice "voice/天使雷亚/0003690.ogg"
    lst "就真的那么好看吗？"
    me01 "你等等。"
    "我从包里拿出了从部门那里借来的迷你星象仪递给了她。"
    me01 "要试试吗？"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0003700.ogg"
    lst "我也能在这里进行天体观测吗？"
    me01 "当然没问题。"
    show ts_lst_ssz_b3 b3 b3_s1
    play voice "voice/天使雷亚/0003710.ogg"
    lst "我也会觉得美丽吗？"
    me01 "啊，一定会的。"
    me01 "喜欢星星的雷亚你，一定也会爱上这片星空的。"
    show ts_lst_ssz_b3 b3 b3_s1 at flu_down(0.25, 20):
        xpos 0.5
    "犹豫片刻后雷亚点了点头。"
    show ts_lst_ssz_b3 b3 b3_n1
    play voice "voice/天使雷亚/0003720.ogg"
    lst "如果不好看的话就捅你哦。"
    me01 "到时候我会负责的。"
    hide ts_lst_ssz_b3
    show ts_lst_ssz_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0003730.ogg"
    lst "其实......你是有什么阴谋吧？"
    me01 "怎么可能有。"
    play sound liandao
    $ flcam.move(0, -200, 600, duration=1.5)
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1_d b1 b1_a2 onlayer m2:
        xpos 0.5
    me01 "这次又是为什么拿起镰刀啊！？"
    play voice "voice/天使雷亚/0003740.ogg"
    lst "表情装过头了。"
    "觉得这样表情很帅的只有我自己吗？！"
    me01 "比起这个雷亚，能告诉我你的全名吗？"
    show ts_lst_ssz_b1_d b1 b1_sp1
    "女孩露出了惊讶的表情。"
    $ flcam.move(0, 0, 900, duration=1.5)
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0003750.ogg"
    lst "......为什么？"
    me01 "有点想知道。"
    me01 "我想和雷亚成为关系更好的朋友。"
    show ts_lst_ssz_b2_d b2 b2_a1
    play voice "voice/天使雷亚/0003760.ogg"
    lst "不要。"
    me01 "告诉别人自己的全名也是最最讨厌的事情之一吗？"
    show ts_lst_ssz_b2_d b2 b2_s4
    play voice "voice/天使雷亚/0003770.ogg"
    lst "那倒不是。"
    me01 "那告诉我也没关系吧？"
    show ts_lst_ssz_b2_d b2 b2_n2
    play voice "voice/天使雷亚/0003780.ogg"
    lst "死神才没有全名呢。"
    me01 "雷亚不就是你的名字吗？"
    show ts_lst_ssz_b2_d b2 b2_s3
    play voice "voice/天使雷亚/0003790.ogg"
    lst "虽然是这样没错。"
    me01 "那姓氏呢？"
    show ts_lst_ssz_b2_d b2 b2_n2
    play voice "voice/天使雷亚/0003800.ogg"
    lst "死神才没有姓氏呢。"
    me01 "不想现在告诉我也没关系，等你想说的时候再告诉我就行了。"
    show ts_lst_ssz_b2_d b2 b2_s4
    play voice "voice/天使雷亚/0003810.ogg"
    lst "都说没有了。"
    me01 "也就是说还不是时候？"
    show ts_lst_ssz_b2_d b2 b2_a1
    play voice "voice/天使雷亚/0003820.ogg"
    lst "今天的你也是笨笨的啊。"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0003830.ogg"
    lst "是时候回去了！"
    me01 "那我们说定了。"
    show ts_lst_ssz_b1 b1 b1_a2
    play voice "voice/天使雷亚/0003840.ogg"
    lst "我明明说了不会告诉你的。"
    me01 "我是说天体观测的事情。"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0004170.ogg"
    lst "......"
    me01 "等你想看星星的时候记得告诉我。"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0004160.ogg"
    lst "不要。"
    me01 "意思是现在就想看？"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0004170.ogg"
    lst "......"
    me01 "雷亚你总是嘴上说着不要，但是每天还是会在这里等我。"
    me01 "昨天也是，今天也是，一直一直都会在这里等我。"
    play voice "voice/天使雷亚/0004180.ogg"
    lst "......"
    me01 "你其实也很想跟我一起玩的吧？"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0004190.ogg"
    lst "才不是......"
    me01 "也是啊。"
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 1.0 hard
    "我向后退了几步。"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004200.ogg"
    lst "诶？"
    me01 "换作是我的话，也会拒绝的。"
    me01 "毕竟在这个世界上我最最讨厌的事情之一就是把自己的想法强加给别人了。"
    me01 "所以如果我是雷亚你的话也一定会做出相同的决定。"
    me01 "所以啊......"
    "我挠了挠头。"
    me01 "如果有一天你想要参加天体观测的话，记得随时告诉我。"
    me01 "想要和我玩耍的话，也都可以跟我说。"
    me01 "以后有什么困难需要我帮忙的，也尽管开口。"
    me01 "因为，我喜欢和雷亚你在一起。"
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.75 alpha 1
    pause 3.5 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_memory piecethree yinghua
    with dissolve
    pause 2.0 hard
    play voice "voice/翔子/0601350.ogg"
    tiny_xz "想要找我玩的时候就说出来。"
    play voice "voice/翔子/0601360.ogg"
    tiny_xz "因为，我喜欢和你在一起。"
    pause 2.0 hard
    scene set only starview night starview
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004210.ogg"
    lst "......刚才。"
    play voice "voice/天使雷亚/0004220.ogg"
    lst "刚才，胸口一紧。"
    me01 "胸口痛吗？"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0004230.ogg"
    lst "嗯。"
    me01 "没问题吗？"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0004240.ogg"
    lst "肯定是你的错。"
    me01 "我看未必吧。"
    show ts_lst_ssz_b1 b1 b1_sp1
    play voice "voice/天使雷亚/0004250.ogg"
    lst "为什么这么说？"
    me01 "因为在我的印象中，过去也曾有过同样的对话。"
    me01 "雷亚你能够看到我的过去对吧？"
    me01 "所以你一定也会，喜欢上我的过去的。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0003860.ogg"
    lst "我考虑考虑......"
    pause 1.0 hard
    show ts_lst_ssz_b1 b1 b1_s1 at walkout_l(0.5)
    play sound xiaoshi_1
    pause 3.0 hard
    "说完，雷亚的身影消失了。"
    $ flcam.move(0, 0, 0, duration=1.5)
    "果然是个奇怪的女孩子啊。"
    "也许同样奇怪的还有我自己。"
    "明明知道自己的过去是那样的不堪，但是仅仅为了那片刻的美好，就死活不肯放弃。"
    "就如同无论如何也无法说服自己放弃曾经的约定一般。"
    "明明此刻自己应该......有了更加需要珍惜的东西才对。"
    pause 2.0 hard
    stop ambience1
    stop music fadeout 5.0
    scene black with slowerdissolve
    $ suppress_overlay = True
    jump day05
