label day05:
    bookmark
    $ save_name = _("Day 05")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_yinghua summer
    with dissolve
    show backend_bg02 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date04 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only school day road yinghua
    with dissolve
    pause 3.0 hard
    scene set only school day room2 yinghua
    with dissolve
    pause 3.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/0111580.ogg"
    rxl "早上好小凉，今天这么早啊。"
    me01 "还好吧。"
    "自从得知上次我和苍衣莲差点迟到的消息之后，翔子每天早上都会来监督我起床。"
    me01 "日向同学今天来得也好早啊。"
    show rxl_xzf_b1 b1 b1_s1
    play voice "voice/日向怜/0111590.ogg"
    rxl "没办法啊，昨晚被吓了一跳所以完全睡不着嘛。"
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.3)
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0503560.ogg"
    lingyin "发生什么事了？"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111600.ogg"
    rxl "嗯，人凭空消失了。"
    play music first_17 fadein 3.0 if_changed
    hide lingyin_xzf_b1
    show yczs_xzf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.7)
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1601250.ogg"
    yczs "那是啥！"
    show rxl_xzf_b2 b2 b2_s1
    play voice "voice/日向怜/0111610.ogg"
    rxl "女孩子从眼前凭空消失了。就像这样，嘶~地，融化在了空气中。"
    show rxl_xzf_b2 b2 b2_s2
    play voice "voice/日向怜/0111620.ogg"
    rxl "就因为这个，我昨晚完全无法静下心来学习啊。"
    hide yczs_xzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_n2
    play voice "voice/日向怜/0111630.ogg"
    rxl "我如果考试挂科的话，就是小凉你的错哟。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111640.ogg"
    rxl "要负起责任哦~"
    me01 "别说的那么开心啊喂！"
    "就因为我解锁了死神的话题所以就要负责吗。"
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0503570.ogg"
    lingyin "虽然我不是很明白......但日向同学昨天是遇到透明人了吗？"
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1601260.ogg"
    yczs "透明的话照相机也拍不到啊，真无聊。"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111650.ogg"
    rxl "不是的，小凉你说过那就是死神对吧？"
    hide lingyin_xzf_b1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/1601270.ogg"
    yczs "你说死神，就是樱华校都市传中的那位吧？"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111670.ogg"
    rxl "她拿着这么大一把镰刀，绝对错不了。"
    play voice "voice/一诚总司/1601280.ogg"
    yczs "莫非你们两位都见到那位死神了吗？"
    me01 "算是吧。"
    show yczs_xzf_b1 b1 b1_a1
    play voice "voice/一诚总司/1601290.ogg"
    yczs "在哪里见到的？"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111680.ogg"
    rxl "观景台啊，就是禁止进入的那里。"
    show yczs_xzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/1601300.ogg"
    yczs "你们擅自进去了吗？"
    show rxl_xzf_b2 b2 b2_s2
    play voice "voice/日向怜/0111690.ogg"
    rxl "别跟其他人说哦~"
    me01 "虽说我是在那里遇到雷亚的。"
    me01 "可没想到日向同学你也会一个人去那种地方。"
    hide rxl_xzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1601310.ogg"
    yczs "死神的名字是雷亚......嗯。"
    hide yczs_xzf_b1
    $ flcam.move(-2250, 350, 750, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    show lingyin_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0503580.ogg"
    lingyin "神野同学和日向同学，你们真的都看到了吗？"
    hide rxl_xzf_b2
    show rxl_xzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111710.ogg"
    rxl "是啊，虽然没有说上话。"
    me01 "毕竟那里的星空对于天协成员来说具有极强的诱惑力。"
    hide rxl_xzf_b3
    hide lingyin_xzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/1601320.ogg"
    yczs "死神对星星感兴趣......嗯。"
    "找到了，那个添油加醋的罪魁祸首！"
    hide yczs_xzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0503590.ogg"
    lingyin "是在梦里见到的......这样的说法行不通吗？"
    me01 "原本我也是这么认为的，所以才会去调查关于幻觉的资料。"
    me01 "不过既然连日向同学也看见了的话，那么是幻觉的概率就很低了吧。"
    show lingyin_xzf_b1 b1 b1_n2
    play voice "voice/青木铃音/0503600.ogg"
    lingyin "大家都看到了同一个梦境，这种可能性也是有的。"
    hide lingyin_xzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/1601340.ogg"
    yczs "如果你们说的都是事实，我也会去观景台撒网的。作为超自然研究协会的成员可不能放过这一次机会~"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show rxl_xzf_b2 b2 b2_a2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111730.ogg"
    rxl "诶......"
    show yczs_xzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/1601350.ogg"
    yczs "为什么你一副很反感的样子啊！"
    show rxl_xzf_b2 b2 b2_a1
    play voice "voice/日向怜/0111740.ogg"
    rxl "因为难得一个浪漫的地方，你却说要去撒网，还有超自然什么的......"
    show yczs_xzf_b1 b1 b1_h1
    play voice "voice/一诚总司/1601360.ogg"
    yczs "也就是说日向亲你其实是想和神野两人单独行动对吧~"
    hide rxl_xzf_b2 with None
    pause 0.1 hard
    show rxl_xzf_b1 b1 b1_sp2 onlayer m2 at flu_down(0.05, 20):
        xpos 0.5
    show tanhao onlayer m2:
        xalign 0.4 yalign 0.25 alpha 1.0
        parallel:
            linear 0.8 xalign 0.35 yalign 0.22
        parallel:
            linear 0.8 alpha 0.0
        parallel:
            linear 0.8 zoom 1.15
    play voice "voice/日向怜/0111750.ogg"
    rxl "不、不是这样的！"
    hide yczs_xzf_b1
    show lingyin_xzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0503610.ogg"
    lingyin "你们今晚也打算去观景台吗？"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111760.ogg"
    rxl "啊、嗯，当然。"
    me01 "铃音同学如果感兴趣的话要不要一起？"
    "铃音摇了摇头。"
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0503620.ogg"
    lingyin "因为是禁止进入的，不会是很危险的地方吧？"
    show rxl_xzf_b2 b2 b2_n2
    play voice "voice/日向怜/0111770.ogg"
    rxl "没有那种事，落脚的地方也很开阔。"
    hide lingyin_xzf_b2
    show lingyin_xzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0503630.ogg"
    lingyin "日向同学，现在还是以学习为主吧？这周可是要考试的。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111780.ogg"
    rxl "考试是从上午一直持续到傍晚，之后的时间就可以去观星了，这样的安排万事ok~"
    show lingyin_xzf_b1 b1 b1_n2
    play voice "voice/青木铃音/0503640.ogg"
    lingyin "傍晚过后不是还要为天协招募新成员吗？"
    show rxl_xzf_b1 b1 b1_sp2
    play voice "voice/日向怜/0111790.ogg"
    rxl "啊对耶！"
    me01 "身为部长的你自己忘了可怎么行啊。"
    hide lingyin_xzf_b1
    show yczs_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1601370.ogg"
    yczs "总之你们还是老老实实地复习备考吧。死神那边就由我去打个招呼~"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111800.ogg"
    rxl "谁也没说不去吧，而且学习的话在休息日的时候就有好好做过了！"
    "刚刚不是才说没精力学习的吗。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111810.ogg"
    rxl "小凉是站在我这边的对吧？"
    me01 "如果你不至于挂科的话我倒是无所谓。"
    hide yczs_xzf_b1
    hide rxl_xzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0503650.ogg"
    lingyin "......只有我一个人反对的话也没有什么意义呢。"
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0111820.ogg"
    rxl "小铃要不要和我们一起？"
    hide lingyin_xzf_b2
    show lingyin_xzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0503660.ogg"
    lingyin "对不起，这个恐怕有点困难。"
    show rxl_xzf_b2 b2 b2_s2
    play voice "voice/日向怜/0111830.ogg"
    rxl "毕竟还要学习嘛，那就等考试结束后吧？"
    show lingyin_xzf_b1 b1 b1_s1
    play voice "voice/青木铃音/0503670.ogg"
    lingyin "这个恐怕还也是有点困难。"
    me01 "是家人规定了不允许去那种地方吗？"
    show rxl_xzf_b2 b2 b2_sp1
    play voice "voice/日向怜/0111840.ogg"
    rxl "诶，为什么？"
    "铃音没有正面回答，只是露着一副很为难的表情。"
    hide rxl_xzf_b2
    show rxl_xzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111850.ogg"
    rxl "果然是因为观景台很危险吗？"
    show lingyin_xzf_b1 b1 b1_n2
    play voice "voice/青木铃音/0503680.ogg"
    lingyin "因为我和姐姐是站在这一边的。"
    me01 "你姐姐？也就是说你姐姐会反对吗？"
    show lingyin_xzf_b1 b1 b1_s1
    play voice "voice/青木铃音/0503690.ogg"
    lingyin "差不多是这样的。"
    show rxl_xzf_b3 b3 b3_s2
    play voice "voice/日向怜/0111860.ogg"
    rxl "可是小铃也是天协的一员啊......"
    show lingyin_xzf_b1 b1 b1_s2
    play voice "voice/青木铃音/0503700.ogg"
    lingyin "抱歉。"
    me01 "没事的，也并非只有观景台那里才适合进行天体观测，铃音同学不要太在意。"
    hide lingyin_xzf_b1
    hide rxl_xzf_b3
    $ flcam.move(0, 0, 0, duration=1.5)
    stop music fadeout 5.0
    play sound rill
    pause 2.0 hard
    "响铃了。"
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    show lingyin_xzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    show yczs_xzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/1601380.ogg"
    yczs "不管是天体还是超自然，现在还是以考试为主吗。"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0503710.ogg"
    lingyin "祝大家好运。"
    hide rxl_xzf_b3
    show rxl_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0111880.ogg"
    rxl "考试结束之后一起吃午饭吧~"
    hide lingyin_xzf_b1
    hide rxl_xzf_b1
    hide yczs_xzf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard

label day05.wyh_event01:
    $ flcam.move(0, 0, 0)
    scene set only street day yinghua
    with dissolve
    pause 1.0 hard
    "果然除了我别人也能看到雷亚的存在。"
    "可是为什么她没有对其他人提出割取噩梦的要求呢？"
    "换句话说，如果第一个闯入观景台禁区的不是我而是其他人。"
    "那么接下来发生的事情还会是现在这样的结果吗？"
    "总而言之，更多的细节还需要当面向雷亚问清楚才行。"
    "话说回来，自从我回来之后，除了在学校和偶尔早上会来叫我起床以外，似乎都没怎么见到过翔子了。"
    "她到底在忙些什么呢。"
    pause 0.5 hard
    $ flcam.move(1100, 0, 600, duration=1.5)
    pause 0.5 hard
    me01 "......那是？"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_s1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/万夜花/1300010.ogg"
    stranger "真是的......我已经受够这个破烂了。"
    "炎炎烈日下，有个人汗流浃背地围在一辆摩托车前。"
    play voice "voice/万夜花/1300020.ogg"
    stranger "附近也没有可以修理的地方，真是伤脑筋了。"
    $ flcam.move(0, 0, 0, duration=1.5)
    hide wyh_xsf_b1
    pause 0.5 hard
    "虽然不知道其中的缘由，不过看她的焦急的样子似乎是遇上麻烦了。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "那个，有什么可以帮忙吗？"
    play music first_14 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300030.ogg"
    stranger "真是得救了，能请你在后面帮我推一下吗？"
    "依照她的指示，我将手搭在后座上使劲向前推。"
    "座位底下似乎放了什么东西，比想象中的还要重。"
    show wyh_xsf_b1 b1 b1_ga2
    play voice "voice/万夜花/1300040.ogg"
    stranger "刚刚在商店街买完东西回来，如果很重的话还真是不好意思。"
    me01 "不，我觉得遇到困难的时候就应该互相帮助。"
    show wyh_xsf_b1 b1 b1_h2
    play voice "voice/万夜花/1300050.ogg"
    stranger "啊哈哈，真是个好孩子呢。看上去很陌生，你也住在这座小镇上吗？"
    me01 "我是前些日子刚搬到这里来的。"
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300060.ogg"
    stranger "原来如此。"
    me01 "我叫神野凉，请多多关照。"
    show wyh_xsf_b1 b1 b1_sp1
    play voice "voice/万夜花/1300070.ogg"
    stranger "真懂礼貌，和我年轻的时候完全不同。"
    me01 "您看上去也很年轻啊。"
    show wyh_xsf_b1 b1 b1_h2
    play voice "voice/万夜花/1300080.ogg"
    stranger "真会说话。但是从你这样年纪的孩子口中听到这样的社交辞令还真是令我有点不爽呢。"
    me01 "我并不是那个意思。"
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300090.ogg"
    stranger "啊哈哈，别装大人了。小鬼就应该有小鬼的样子。"
    play voice "voice/万夜花/1300100.ogg"
    stranger "这座小镇感觉如何？搬过来还习惯吗？"
    me01 "并没有什么奇怪的地方，毕竟我以前也曾在这里待过一段时间。"
    show wyh_xsf_b1 b1 b1_sp1
    play voice "voice/万夜花/1300110.ogg"
    stranger "搬出去又回来了吗......还真少见。"
    show wyh_xsf_b1 b1 b1_s1
    play voice "voice/万夜花/1300120.ogg"
    stranger "搬走的人对于这里落后的条件发些牢骚也实属正常，但是会选择搬回来的你想必不是出于这样的想法吧？"
    me01 "怎么说呢，倒不如说我有不得不回来的理由。"
    show wyh_xsf_b1 b1 b1_n2
    play voice "voice/万夜花/1300130.ogg"
    stranger "你看起来很喜欢这座小镇嘛。"
    me01 "某种意义上来说是的吧。"
    show wyh_xsf_b1 b1 b1_h2
    play voice "voice/万夜花/1300140.ogg"
    stranger "真是坦率的回答。有像你这样的孩子在，这座小镇或许也不至于就此荒废下去。"
    me01 "话说回来，您这是要去哪里呢？"
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300150.ogg"
    stranger "虽然很不好意思，但是希望你能帮我推到家为止。"
    me01 "您家在什么地方？"
    play voice "voice/万夜花/1300160.ogg"
    stranger "隔壁的镇上。"
    show wyh_xsf_b1 b1 b1_h2
    play voice "voice/万夜花/1300170.ogg"
    stranger "看在你比我年轻的份上，就拜托你了~"
    "总感觉被压榨了。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with dissolve
    pause 2.0 hard

label day05.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua
    with dissolve
    pause 2.0 hard
    "经历了一番周折，到达目的地的时候时间已经过去快要三个小时了。"
    "且不说摩托车的重量，就算徒步在这高温的天气下也会消耗不少体力。"
    play voice "voice/万夜花/1300180.ogg"
    stranger "我先把车停到车库里，你稍等一下。还要向你道谢呢~"
    play ambience1 zhiliao fadein 5.0
    pause 1.0 hard
    scene set only shenshe day yinghua
    with dissolve
    pause 1.0 hard
    "对于她家居然是神社这一点我是万万没有想到的。"
    "鸟居上写着“星天宫”的字样。"
    "星天宫？这不就是在观景台立下禁止进入标识的政府机构吗。"
    "话说......"
    me01 "还真热啊。"
    "为了寻找阴凉的地方避暑，我也是在神社四周闲逛了起来。"
    "周围被密集的植被覆盖着，蝉鸣声顿时让燥热的气氛越发浓烈。"
    $ flcam.move(0, -100, 400, duration=1.5)
    "刚走上台阶，不远处的身影就引起了我的注意。"
    "似乎是这里的巫女。"
    "她正在用勺子舀着水泼向四周的台阶。"
    "为了给参拜的游客降温用的吧？"
    pause 1.0 hard
    play music first_15 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only xz_cg surprise
    with right2left
    pause 1.0 hard
    play voice "voice/翔子/0202910.ogg"
    xz "为......"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    play voice "voice/翔子/0202920.ogg"
    xz "......为什么凉、神野君会在这里啊？"
    "和私下相处的时候不同，此时的翔子称呼我“神野君”。"
    "是因为身为巫女的基本礼仪吗？"
    me01 "我是来参拜的。"
    play voice "voice/翔子/0202930.ogg"
    xz "认真的？"
    me01 "骗你的。"
    play voice "voice/翔子/0202940.ogg"
    xz "我想也是，谁会选择在这种大热天来参拜啊。"
    play voice "voice/翔子/0202950.ogg"
    xz "夏日祭也还早着呢。"
    play sound sashui
    pause 1.0
    "洒水的巫女，感觉就像是夏日里一道靓丽的风景线。"
    me01 "我就想怎么这么久都没见到翔子你，没想到你原来是这里的巫女啊。"
    pause 0.1 hard
    scene set only xz_cg normal
    with dissolve
    play voice "voice/翔子/0202960.ogg"
    xz "只是家里恰巧有亲戚在神社工作罢了。所以才要帮忙做这么多麻烦的工作。"
    me01 "翔子你不仅是学生会，就连神社的工作也参与了。"
    me01 "话说巫女可不是什么人都能当的吧？"
    play voice "voice/翔子/0202970.ogg"
    xz "别把这和女仆之类的联想起来。"
    me01 "哪里的话，再说了职业是不分贵贱的。"
    pause 0.1 hard
    scene set only xz_cg angry
    with dissolve
    $ flcam.move(4100, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0202980.ogg"
    xz "烦死了。"
    play sound sashui
    with vpunch
    pause 1.0 hard
    me01 "我说，水似乎洒到我脚上了啊！"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0202990.ogg"
    xz "还不是因为你站在我旁边的关系吗，另外从刚才我就在问了，为什么你会在这里啊？"
    me01 "我也是来帮忙推车的，虽然工作已经结束了。"
    pause 0.1 hard
    scene set only xz_cg normal
    with dissolve
    play voice "voice/翔子/0203010.ogg"
    xz "那台摩托年代久远，我想差不也多快要报废了。"
    play voice "voice/翔子/0203030.ogg"
    xz "作为回礼，你就来替我来洒水好了~"
    me01 "需要我帮忙的话就直说嘛。"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    play voice "voice/翔子/0203040.ogg"
    xz "啊，真的可以吗？"
    me01 "这水要洒到什么程度？"
    pause 0.1 hard
    scene set only xz_cg happy
    with dissolve
    play voice "voice/翔子/0203050.ogg"
    xz "神社内所有的台阶都要洒遍。"
    me01 "接下来，差不多我也该回去了。"
    play voice "voice/翔子/0203060.ogg"
    xz "骗你的啦。这里的台阶附近就可以，拜托了~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only shenshe day yinghua
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "等等，你把勺子给我了你自己干什么啊？"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_wnf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/翔子/0203070.ogg"
    xz "你不是说要帮忙吗？"
    me01 "别全部推给我，你自己也做一部分啦。"
    hide xz_wnf_b1
    show xz_wnf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0203080.ogg"
    xz "并没有全部推给你。只是水快不够用了，我准备去提点备用而已。"
    me01 "提水这样的体力活还是让我来吧？"
    show xz_wnf_b3 b3 b3_h1
    play voice "voice/翔子/0203090.ogg"
    xz "那就交给你了~"
    me01 "地点呢？"
    hide xz_wnf_b3
    show xz_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0203100.ogg"
    xz "鸟居附近就有清水。"
    me01 "那里的水不是用来干这个的吧？"
    hide xz_wnf_b1
    show xz_wnf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0203110.ogg"
    xz "附近的自来水也是可以的。"
    me01 "了解。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_cg happy
    with dissolve
    "翔子把已经快要见底的水桶交给我，自己又开始了洒水的工作。"
    play voice "voice/翔子/0203130.ogg"
    xz "不如你也来这里打工怎么样？只在我轮班的时候来帮忙就可以了。"
    me01 "总觉得会有很多的剥削所以还请容我拒绝。"
    play voice "voice/翔子/0203140.ogg"
    xz "只需要负责洒水和扫地就可以了。"
    me01 "是为了祭典举办而做的准备工作吗？"
    pause 0.1 hard
    scene set only xz_cg normal
    with dissolve
    play voice "voice/翔子/0203150.ogg"
    xz "是啊。"
    me01 "那销售方面的工作应该会很有趣吧。"
    play voice "voice/翔子/0203160.ogg"
    xz "那些可不归这里管，是社区委员会的事情。"
    me01 "那祭典的时候翔子你的工作究竟是什么？"
    pause 0.1 hard
    scene set only xz_cg shame
    with dissolve
    play voice "voice/翔子/0203170.ogg"
    xz "......"
    "翔子没有回答，只是红着脸低下头。"
    pause 0.1 hard
    scene set only xz_cg angry
    with dissolve
    $ flcam.move(4100, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    with vpunch
    play sound sashui
    pause 1.0 hard
    me01 "什么情况啊？"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    play voice "voice/翔子/0203180.ogg"
    xz "好了啦，快点去提水了！"
    me01 "真是搞不懂你啊。"
    play voice "voice/翔子/0203190.ogg"
    xz "......哼！"
    me01 "在我提水回来之前，赶紧把剩下的地方打扫干净吧。"
    play voice "voice/翔子/0203200.ogg"
    xz "那是当然。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0203210.ogg"
    xz "啊啊，真想快点回家避暑啊~"
    "真是个爱发牢骚的巫女。"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard
    stop ambience1
    scene set only shenshe day yinghua inside
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/万夜花/1300190.ogg"
    wyh "真不好意思，居然还帮了{rb}小翔{/rb}{rt}昵称{/rt}的忙。"
    "听翔子说摩托车的主人就是这里的大神官，南星万夜花小姐。"
    "虽然对神官什么的并不是很了解，不过据说大神官在世界范围内也是颇具影响力的职位，真看不出这座小镇也能容得下这样的大人物啊。"
    show wyh_xsf_b1 b1 b1_h2
    play voice "voice/万夜花/1300200.ogg"
    wyh "很热吧，我去准备麦茶。"
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_h2 onlayer m2 at walkout_r(0.5)
    pause 2.0 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_xsf_b1 b1 b1_n2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/翔子/0203220.ogg"
    xz "你还没有回去吗？"
    play music first_13 fadein 3.0 if_changed
    me01 "似乎被留下来喝茶了。"
    show xz_xsf_b1 b1 b1_s1
    play voice "voice/翔子/0203230.ogg"
    xz "毕竟说过要回礼嘛。"
    "此时的翔子换上了便服，看来今天的任务是结束了。"
    show xz_xsf_b1 b1 b1_n1
    play voice "voice/翔子/0203240.ogg"
    xz "既然屋里的空调那么舒服，我也在这乘凉好了。"
    me01 "翔子你经常来这里帮忙吗？"
    show xz_xsf_b1 b1 b1_sp1
    play voice "voice/翔子/0203250.ogg"
    xz "是啊，不是和你说过我要坐电车出门吗？"
    me01 "这离学校也不远，像万夜花小姐一样骑摩托去不就行了？"
    show xz_xsf_b1 b1 b1_n1
    play voice "voice/翔子/0203270.ogg"
    xz "樱华校是禁止骑摩托车或者自行车上学的。考虑到山路的危险程度这也是很合情合理的。"
    hide xz_xsf_b1
    show xz_xsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0203280.ogg"
    xz "要是校门口能有巴士站台就好了呢。"
    me01 "就算有巴士，会来这里的除了樱华校的学生就没有其他人了吧？"
    show xz_xsf_b3 b3 b3_s1
    play voice "voice/翔子/0203290.ogg"
    xz "毕竟观景台也被禁止进入了嘛。"
    show xz_xsf_b3 b3 b3_s2
    play voice "voice/翔子/0203300.ogg"
    xz "天气凉爽的时候也就罢了，在这种大热天还要爬那个坡道就有点......"
    me01 "我理解你的心情，不过现在就开始感叹返校时的凄惨体验也是有些煞风景了。"
    me01 "话说回来，开学的时候学生会也会召开例行会议吗？"
    show xz_xsf_b3 b3 b3_n2
    play voice "voice/翔子/0203310.ogg"
    xz "......怎么了，突然问这个？"
    me01 "是或不是，到底是哪一个啊。"
    hide xz_xsf_b3
    show xz_xsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0203320.ogg"
    xz "非要选择的话应该是会的......我说，怎么有一种不好的预感。"
    me01 "不愧是翔子，反应真快。"
    show xz_xsf_b1 b1 b1_ga1
    play voice "voice/翔子/0203330.ogg"
    xz "多谢夸奖，但还是驳回。"
    show xz_xsf_b1 b1 b1_s1
    play voice "voice/翔子/0203340.ogg"
    xz "反正一定是和天协有关的吧？"
    me01 "您说的一点也没错。"
    me01 "其实我们想要屋顶的使用许可。"
    play voice "voice/翔子/0203370.ogg"
    xz "到了第二学期自然就会给你们了，虽然会加上一些限制的说。"
    me01 "第二学期就太迟了。能不能在暑假也......"
    show xz_xsf_b1 b1 b1_ga1
    play voice "voice/翔子/0203380.ogg"
    xz "别开玩笑了。"
    me01 "我是认真的。"
    show xz_xsf_b1 b1 b1_s1
    play voice "voice/翔子/0203390.ogg"
    xz "暑假的时候就算是学生会也要休息的吧。"
    show xz_xsf_b1 b1 b1_n2
    play voice "voice/翔子/0203400.ogg"
    xz "天协也要在社团会议决策后才会被批准成为正式的社团，那个社团会议要在第二学期才会召开，明白了吗？"
    me01 "只要临时的使用权限就可以了。"
    hide xz_xsf_b1
    show xz_xsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0203410.ogg"
    xz "这种例外是不被允许的。"
    me01 "那非社团成员参加社团活动也不被允许吗？"
    show xz_xsf_b3 b3 b3_a1
    play voice "voice/翔子/0203420.ogg"
    xz "你以为这些都是谁定的规矩啊？"
    me01 "是你们学生会吧。"
    me01 "就帮个忙破个例呗？"
    show xz_xsf_b3 b3 b3_s1
    play voice "voice/翔子/0203430.ogg"
    xz "不觉得很厚脸皮吗。"
    me01 "这个人情我一定会还的。"
    hide xz_xsf_b3
    show xz_xsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0203440.ogg"
    xz "那神社洒水和打扫的工作今后就交给你了~"
    me01 "洒水已经做完了，还剩下打扫没错吧？"
    show xz_xsf_b1 b1 b1_h1
    play voice "voice/翔子/0203450.ogg"
    xz "整个暑假的活都交给你了~"
    me01 "暴君啊！"
    hide xz_xsf_b1
    show xz_xsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0203460.ogg"
    xz "或者说......加入学生会。"
    me01 "我知道了。"
    show xz_xsf_b2 b2 b2_sp1
    "听了我的回答，翔子表现的十分惊讶。"
    hide xz_xsf_b2
    show xz_xsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0203470.ogg"
    xz "等等，那么爽快就答应了，之前为什么那么抗拒啊？"
    me01 "老实说，我觉得自己并不适合学生会，所以如果不是因为有求于你我是无论如何也不会加入的。"
    show xz_xsf_b1 b1 b1_s1
    play voice "voice/翔子/0203480.ogg"
    xz "......天协就那么重要吗？"
    me01 "是啊。"
    show xz_xsf_b1 b1 b1_n2
    play voice "voice/翔子/0203481.ogg"
    xz "连第二学期都等不到？"
    me01 "等不到。"
    play voice "voice/翔子/0203490.ogg"
    xz "为什么？"
    me01 "理由虽然也不是什么大不了的东西，但是我不想说。"
    hide xz_xsf_b1
    show xz_xsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0203500.ogg"
    xz "快·告·诉·我！"
    hide xz_xsf_b2
    show xz_xsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/0203510.ogg"
    xz "如果是不可告人的理由，我就更不可能同意了。"
    me01 "所以说不是你想的那样。"
    show xz_xsf_b1 b1 b1_n2
    play voice "voice/翔子/0203520.ogg"
    xz "那就是可以说的吧？"
    stop music fadeout 5.0
    pause 0.5 hard
    show lingyin_xsf_b1 b1 b1_n2 onlayer m2 at walkin_r(0.5)
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504250.ogg"
    lingyin "姐姐，刨根问底是恶趣味哦~"
    show xz_xsf_b1 b1 b1_s1
    play voice "voice/翔子/0203530.ogg"
    xz "......帮手在这个的时机登场了吗。"
    play music first_09 fadein 3.0 if_changed
    hide lingyin_xsf_b1
    show lingyin_xsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0504260.ogg"
    lingyin "神野同学你好。"
    me01 "铃音同学，见到你真高兴。"
    "虽然之前听到“青木”这个姓氏的时候就有这种感觉了，但没想到她们竟然真的是姐妹。"
    "小的时候也完全没有听翔子提到过。"
    show lingyin_xsf_b2 b2 b2_ga3
    play voice "voice/青木铃音/0504270.ogg"
    lingyin "果然不能把姐姐置之不理呢。"
    show xz_xsf_b1 b1 b1_n2
    play voice "voice/翔子/0203540.ogg"
    xz "虽然不知道你误会了些什么，但并不是我把他带来的。"
    pause 0.5 hard
    hide lingyin_xsf_b2
    hide xz_xsf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/万夜花/1300210.ogg"
    wyh "哦呀，大家都到齐了啊。"
    show wyh_xsf_b1 b1 b1_s2
    play voice "voice/万夜花/1300220.ogg"
    wyh "话说回来，加上{rb}小铃{/rb}{rt}昵称{/rt}的话我那份就没有了。"
    pause 0.5 hard
    show lingyin_xsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504280.ogg"
    lingyin "我的那份我自己去拿好了。"
    hide lingyin_xsf_b2
    hide wyh_xsf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    "铃音走进了厨房。"
    stop music fadeout 5.0
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/万夜花/1300230.ogg"
    wyh "你们说的话我都听到了。还真是令人怀念的话题啊。"
    pause 0.5 hard
    show xz_xsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0203550.ogg"
    xz "......怀念？"
    show wyh_xsf_b1 b1 b1_sp1
    play voice "voice/万夜花/1300240.ogg"
    wyh "啊啊。还没对小翔说过呢。"
    "万夜花小姐喝了一口麦茶。"
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300250.ogg"
    wyh "我以前也是樱华校的学生哟。那时候还加入了天文部。"
    play music first_14 fadein 3.0 if_changed
    show xz_xsf_b1 b1 b1_sp2
    play voice "voice/翔子/0203560.ogg"
    xz "这、这样吗？"
    show wyh_xsf_b1 b1 b1_s1
    play voice "voice/万夜花/1300260.ogg"
    wyh "嗯，我们家的神社祭祀的是天津瓮星，作为继承者的我对天体观测有兴趣也没什么值得大惊小怪的吧？"
    show wyh_xsf_b1 b1 b1_sp1
    play voice "voice/万夜花/1300280.ogg"
    wyh "你是叫神野凉对吧。如今的天文部变成天协了吗？"
    me01 "啊，是的。因为成员人数不够的关系所以从社团被降级成了同好会。"
    pause 0.5 hard
    show lingyin_xsf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.3)
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504290.ogg"
    lingyin "但是，马上就能再一次被认可成为社团了哟~"
    show lingyin_xsf_b1 b1 b1_h1
    play voice "voice/青木铃音/0504300.ogg"
    lingyin "多亏了神野同学的加入。"
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300290.ogg"
    wyh "你们两个都加入了天协啊。怎么样，社团活动开心吗？"
    show lingyin_xsf_b1 b1 b1_n1
    play voice "voice/青木铃音/0504310.ogg"
    lingyin "迄今为止已经很开心了，但从今往后会变得更开心的。"
    me01 "真正的活动才刚刚开始。"
    show wyh_xsf_b1 b1 b1_h1
    play voice "voice/万夜花/1300300.ogg"
    wyh "讴歌青春的感觉呢~"
    show xz_xsf_b1 b1 b1_s1
    play voice "voice/翔子/0203580.ogg"
    xz "......"
    show wyh_xsf_b1 b1 b1_ga1
    play voice "voice/万夜花/1300310.ogg"
    wyh "别摆出这么一副臭脸了，你也加入不就好了？"
    hide xz_xsf_b1
    show xz_xsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0203590.ogg"
    xz "别开玩笑了。光是巫女的工作已经够麻烦的了。"
    "说完翔子站起身准备离开。"
    show lingyin_xsf_b1 b1 b1_sp1
    play voice "voice/青木铃音/0504320.ogg"
    lingyin "姐姐，要回家了吗？"
    show xz_xsf_b3 b3 b3_s1
    play voice "voice/翔子/0203600.ogg"
    xz "嗯。还有作业要做呢。"
    hide lingyin_xsf_b1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1300320.ogg"
    wyh "大白天的不用那么着急去写作业吧？"
    hide xz_xsf_b3
    show xz_xsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0203610.ogg"
    xz "我只是有计划地进行而已。"
    show wyh_xsf_b1 b1 b1_s1
    play voice "voice/万夜花/1300330.ogg"
    wyh "学习这种东西到了社会上就什么忙都帮不上的。"
    show wyh_xsf_b1 b1 b1_ga1
    play voice "voice/万夜花/1300340.ogg"
    wyh "你好歹也是这座神社的候补继承人之一。"
    show xz_xsf_b1 b1 b1_s2
    play voice "voice/翔子/0203630.ogg"
    xz "并没有打算继承。"
    show wyh_xsf_b1 b1 b1_s1
    play voice "voice/万夜花/1300350.ogg"
    wyh "真是难相处啊。"
    show xz_xsf_b1 b1 b1_a1
    play voice "voice/翔子/0203640.ogg"
    xz "虽然是首席巫女但是也没有必要奉陪到这个地步。"
    show wyh_xsf_b1 b1 b1_ga1
    play voice "voice/万夜花/1300360.ogg"
    wyh "不是指这个，我是指服务客人这一点。"
    show wyh_xsf_b1 b1 b1_h1
    play voice "voice/万夜花/1300370.ogg"
    wyh "神野君，想不想看看小翔的高清无码照？"
    hide xz_xsf_b1 with None
    pause 0.1 hard
    show xz_xsf_b2 b2 b2_ga1 onlayer m2 at flu_up(0.05, 20):
        xpos 0.5
    show tanhao at tanhao_x05 onlayer m2
    play voice "voice/翔子/0203660.ogg"
    xz "那是什么东西啊？！"
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300380.ogg"
    wyh "以前你家人寄来的照片而已啦。"
    show xz_xsf_b2 b2 b2_a1
    play voice "voice/翔子/0203670.ogg"
    xz "为什么要把那种东西拿出来啊！"
    show wyh_xsf_b1 b1 b1_ga2
    play voice "voice/万夜花/1300390.ogg"
    wyh "因为在讨论关于小翔人生的话题嘛~"
    show xz_xsf_b2 b2 b2_a2
    play voice "voice/翔子/0203680.ogg"
    xz "所以说这些和我没有关系吧？"
    hide wyh_xsf_b1
    show lingyin_xsf_b2 b2 b2_h3 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504330.ogg"
    lingyin "神野同学，这是姐姐去年夏日祭时候的照片。"
    hide xz_xsf_b2
    show xz_xsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    with vpunch 
    play voice "voice/翔子/0203690.ogg"
    xz "住手！"
    "我还没来得及看就被一把夺了过去。"
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1300400.ogg"
    wyh "那只能用小翔净身时候的照片来将就一下了。"
    show lingyin_xsf_b2 b2 b2_h1
    play voice "voice/青木铃音/0504340.ogg"
    lingyin "神野同学想听姐姐几岁时候的故事呢？"
    show xz_xsf_b1 b1 b1_s1
    play voice "voice/翔子/0203700.ogg"
    xz "......总而言之就是我没有办法走出这个房间的意思呢。"
    "真是一家人的感觉啊。"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    play music first_07 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only shenshe evening yinghua
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_xsf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/万夜花/1300410.ogg"
    wyh "神野君，你认识诗乃吗？"
    me01 "......"
    "这是一个许久不曾听到的名字了，没想到眼前的这位神官小姐竟然能够说出母亲的名讳。"
    "虽然母亲生前也是一名巫女，不过没想到她与星天宫也有渊源。"
    me01 "万夜花小姐认识我母亲吗？"
    show wyh_xsf_b1 b1 b1_sp1
    play voice "voice/万夜花/1300420.ogg"
    wyh "果然啊。"
    show wyh_xsf_b1 b1 b1_s1
    play voice "voice/万夜花/1300430.ogg"
    wyh "也没有听说诗乃结婚的消息，听到你的身世时我也是吓了一跳呢。"
    me01 "母亲原来也是星天宫的巫女吗？"
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300440.ogg"
    wyh "是啊。你还不知道啊。"
    "母亲在我出生不久后便去世了，还有太多的话来不及对她说。"
    me01 "那您和母亲是同学吗？"
    show wyh_xsf_b1 b1 b1_s1
    play voice "voice/万夜花/1300450.ogg"
    wyh "不是哦。诗乃比我小两岁，所以无论是年级还是班级都是不一样的。"
    show wyh_xsf_b1 b1 b1_n1
    play voice "voice/万夜花/1300460.ogg"
    wyh "但是在天文部的时候是一起的呢。"
    "原来樱华中学的天文部也是母亲生前重要的东西。"
    "既然如此，作为承载母亲回忆的一份重要寄托，就更不能让它在这里就解散。"
    "是时候进行下一步行动了......"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black 
    with dissolve
    pause 2.0 hard

label day05.starview_event01:
    play sound move_1
    $ flcam.move(0, 0, 0)
    scene set only starview night road
    with dissolve
    pause 2.0 hard
    scene set only starview night starview
    with dissolve
    pause 2.0 hard
    play music first_18 fadein 3.0 if_changed
    scene set only lisite_cg normal
    with in2out_v2_slow
    pause 2.0 hard
    play voice "voice/天使雷亚/0004500.ogg"
    lst "中午好。"
    me01 "中午好。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0004510.ogg"
    lst "我可以捅你吗？" 
    me01 "不是你先说中午好的吗。"
    play voice "voice/天使雷亚/0004520.ogg"
    lst "今晚的你也是笨笨的呢。"
    "这台词我已经听腻了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004530.ogg"
    lst "......那个。"
    "雷亚看了看四周。"
    show ts_lst_ssz_b1 b1 b1_a1
    play voice "voice/天使雷亚/0004540.ogg"
    lst "之前你说的那些人呢？"
    "之前似乎确实邀请过她一起参加天体观测来着。"
    me01 "今天她们大概不会来了。"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004550.ogg"
    lst "那，望远镜呢？"
    me01 "也没有带来。"
    hide ts_lst_ssz_b3
    show ts_lst_ssz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004560.ogg"
    lst "......"
    "雷亚一脸不快地扭过头去。"
    me01 "你想看星星吗？"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/0004570.ogg"
    lst "也不是。"
    me01 "抱歉。"
    show ts_lst_ssz_b2 b2 b2_a1
    play voice "voice/天使雷亚/0004580.ogg"
    lst "我都说了不是的。"
    me01 "作为补偿我带来了这个。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    stop music fadeout 5.0
    show ts_lst_ssz_b2 b2 b2_sp1
    show shenqingshu onlayer m2 at shenqingshu:
        xpos 0.55
    "我递给她一张纸条。"
    pause 1.0 hard
    hide shenqingshu
    show ts_lst_ssz_b2 b2 b2_n2
    play voice "voice/天使雷亚/0004590.ogg"
    lst "这是什么？"
    play music first_13 fadein 3.0 if_changed
    me01 "天协的入部申请书。"
    show ts_lst_ssz_b2 b2 b2_sp1
    play voice "voice/天使雷亚/0004600.ogg"
    lst "天协？"
    me01 "天体观测爱好者协会，简称天协。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004610.ogg"
    lst "天体观测......"
    me01 "是的，只要加入这个同好会的话，就能随心所欲地使用望远镜了。"
    me01 "怎么样雷亚，想不想和我们一起让思绪乘着星星驰骋在这广阔的宇宙中呢？"
    show ts_lst_ssz_b1 b1 b1_a2
    play voice "voice/天使雷亚/0004620.ogg"
    lst "不想。"
    "被拒绝了。"
    me01 "为什么啊？！"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0004630.ogg"
    lst "就算你问为什么。"
    me01 "刚刚不是还在为我没有带望远镜来而失望的吗。"
    show ts_lst_ssz_b1 b1 b1_a2
    play voice "voice/天使雷亚/0004640.ogg"
    lst "死神才不会去用望远镜呢。"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0004650.ogg"
    lst "说错了。死神才不会让思绪乘着星星驰骋在广阔的宇宙中呢。"
    me01 "可是看星星，不觉得是件很开心的事吗？"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0004660.ogg"
    lst "很普通。"
    me01 "雷亚。能不能在这里签个名？"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004670.ogg"
    lst "不要。"
    me01 "只要写下名字就好了。真的只要这样就行了。之后的事情全部交给我来处理，这样我们大家都会很开心的。"
    show ts_lst_ssz_b2 b2 b2_n2
    play voice "voice/天使雷亚/0004680.ogg"
    lst "因为很麻烦所以不要。"
    me01 "拜托了，能不能为了我加入天协呢？"
    show ts_lst_ssz_b2 b2 b2_a1
    play voice "voice/天使雷亚/0004690.ogg"
    lst "不要。"
    "可恶，这个别扭鬼。"
    "今晚的计划刚开始就遇到瓶颈了。"
    show ts_lst_ssz_b2 b2 b2_n2
    play voice "voice/天使雷亚/0004700.ogg"
    lst "而且为什么我非要加入那个叫天协的不可啊？"
    me01 "因为我想要让你加入。"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0004710.ogg"
    lst "今晚的你也是笨笨的呢。"
    show ts_lst_ssz_b2 b2 b2_ga1
    play voice "voice/天使雷亚/0004720.ogg"
    lst "我就是问你想让我加入的理由。"
    me01 "因为我想和雷亚一起看星星。"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/0004730.ogg"
    lst "看星星的话，每天在这里进行不就行了吗。即使不加入天协不也是可以的吗？"
    me01 "就算是这样也拜托了。"
    show ts_lst_ssz_b2 b2 b2_a1
    play voice "voice/天使雷亚/0004740.ogg"
    lst "都说了不要。"
    me01 "即便是不在观景台的时候，我也想和雷亚在一起啊。"
    show ts_lst_ssz_b2 b2 b2_sp1
    play voice "voice/天使雷亚/0004750.ogg"
    lst "......"
    me01 "和你在一起的时间我希望越长越好。"
    show ts_lst_ssz_b2 b2 b2_s2
    play voice "voice/天使雷亚/0004760.ogg"
    lst "......"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004770.ogg"
    lst "刚刚......胸口一紧。"
    me01 "所以你同意了？"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004780.ogg"
    lst "我觉得那是想要捅你的躁动。"
    me01 "如果我能空手夺下镰刀的话你就会加入天协吗？"
    show ts_lst_ssz_b2 b2 b2_a1
    play voice "voice/天使雷亚/0004790.ogg"
    lst "我知道了。那我出招了。"
    me01 "对不起，我是开玩笑的。"
    me01 "其实啊雷亚，想让你加入天协我也是有其他考虑的。"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0004800.ogg"
    lst "从刚开始我就一直在问这个的。"
    me01 "要知道，天协是樱华校的同好会。"
    show ts_lst_ssz_b2 b2 b2_sp1
    play voice "voice/天使雷亚/0004810.ogg"
    lst "是坡下的那所学校吧？"
    me01 "你知道啊。"
    show ts_lst_ssz_b2 b2 b2_n2
    play voice "voice/天使雷亚/0004820.ogg"
    lst "因为很近。"
    me01 "那所樱华校的天协，现在正在为无法晋升成社团而面临废部的重大危机。"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0004830.ogg"
    lst "呼嗯~"
    me01 "所以为了让它晋升成功，还需要雷亚加入成为部员。"
    play voice "voice/天使雷亚/0004840.ogg"
    lst "呼嗯~"
    me01 "就是这样，如果雷亚同意的话天协就有救了。"
    play voice "voice/天使雷亚/0004850.ogg"
    lst "呼嗯~"
    me01 "所以拜托了，就当是帮我一回吧。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004860.ogg"
    lst "不要。"
    "这个混账！"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0004870.ogg"
    lst "直接废部不就好了吗。"
    me01 "就是因为不愿意看到这种事情发生才拜托你的！"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0004880.ogg"
    lst "所有的生命总有一天都会归于死亡。有形的事物总有一天都会归于腐朽。我想你所说的天协也是一样的。"
    me01 "这种诗一样的大道理怎么样都无所谓了！"
    show ts_lst_ssz_b2 b2 b2_a1
    play voice "voice/天使雷亚/0004890.ogg"
    lst "你这话让我很不爽。"
    me01 "这里有笔，剩下的只要雷亚签名就可以了。只要在这个入部申请书上签名的话一切都会圆满了。"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0004900.ogg"
    lst "这才是怎么样都无所谓的事情！"
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_s1 at flu_down(0.25, 20):
        xpos 0.5
    show shenqingshu onlayer m2 at basicfade_u2c:
        xpos 0.55
    with vpunch
    hide shenqingshu
    play sound throw
    pause 2.0 hard
    "雷亚随手就把入部申请书给扔了。"
    stop music fadeout 2.0
    show jingya onlayer texture
    play sound jingya
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    with vpunch
    me01 "{size=72}s h i ~ ~ ~ ~ ~ t ！ ！ ！{/size}"
    show ts_lst_ssz_b2 b2 b2_sp3 onlayer m2 at flu_down(0.1, 20):
        xpos 0.5
    play voice "voice/天使雷亚/0004910.ogg"
    lst "{size=72}呀啊啊啊啊啊啊啊！{/size}"
    pause 1.0 hard
    play sound hide_sound
    show ts_lst_ssz_b2 b2 b2_sp3 onlayer m2 at walkout_l(0.5)
    pause 1.5 hard
    "面对我突然的吼叫，雷亚像是受到惊吓的小动物一般躲进了后面的树丛中。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night road
    with right2left
    pause 2.0 hard
    me01 "喂雷亚，我不会再这样了所以快点出来吧。"
    "片刻的沉默过后，雷亚畏畏缩缩地从树林里探出头。"
    play music first_17 fadein 3.0 if_changed
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b3 b3 b3_s2 onlayer screens at side_right('ts_lst', 0.91), basicfade
    play voice "voice/天使雷亚/0004920.ogg"
    lst "......不、不会咬我吗？"
    me01 "当然不会了。"
    show ts_lst_ssz_b3 b3 b3_a1 onlayer screens at side_right('ts_lst', 0.91), basicfade
    play voice "voice/天使雷亚/0004930.ogg"
    lst "如、如果再犯的话，就捅你哦。"
    hide ts_lst_ssz_b3
    "看着女孩惊魂未定的模样，刚才那一下恐怕吓得不轻啊。"
    show ts_lst_ssz_b3 b3 b3_ga1 onlayer screens at side_right('ts_lst', 0.91), basicfade
    play voice "voice/天使雷亚/0004940.ogg"
    lst "如、如果再犯的话，下次就叫你变态狗......"
    show ts_lst_ssz_b3 b3 b3_s2 onlayer screens at side_right('ts_lst', 0.91), basicfade
    play voice "voice/天使雷亚/0004950.ogg"
    lst "知、知道了吗......？"
    hide ts_lst_ssz_b3
    me01 "我知道了。"
    pause 1.0 hard
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_s2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    me01 "所以，感觉怎么样？"
    show ts_lst_ssz_b2 b2 b2_sp1
    play voice "voice/天使雷亚/0004960.ogg"
    lst "......什么怎么样？"
    me01 "感受到我的热情了吗？"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0004970.ogg"
    lst "变态的热情我倒是感受到了。"
    me01 "能不能考虑加入天协呢？"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/0004980.ogg"
    lst "越来越不想加入了。"
    me01 "雷亚你到底想要我怎么做才能答应我呢？"
    show ts_lst_ssz_b2 b2 b2_ga1
    play voice "voice/天使雷亚/0004990.ogg"
    lst "这个说法好像很微妙。"
    me01 "那我换个说法，要用什么手段才能让你加入天协呢？"
    stop music fadeout 5.0
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0005000.ogg"
    lst "话说回来，我又不是樱华校的学生，能加入天协吗？"
    me01 "关于这点我自有办法。"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0005010.ogg"
    lst "不惜做到这一步也想让我加入吗？"
    me01 "是的。"
    play voice "voice/天使雷亚/0005020.ogg"
    lst "就这么不想让天协消失吗？"
    me01 "除此之外还有另一个目的。"
    show ts_lst_ssz_b2 b2 b2_sp1
    play voice "voice/天使雷亚/0005030.ogg"
    lst "是什么？"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    play music first_30 fadein 3.0 if_changed
    me01 "我说过的吧，我想要和雷亚在一起的时间更长一些。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1_d b1 b1_s3 onlayer m2:
        xpos 0.5
    me01 "即使雷亚你不加入，我也不能让天协就这样毁灭。"
    me01 "我一定会让天协继续存在下去的。"
    me01 "但如果有一天，天协真的成为了正式的社团，那么在学校的屋顶上也可以名正言顺地进行天体观测了。"
    me01 "如此一来我到这里来的时间也会变少。雷亚你也知道的吧，这座观景台是禁止外人进入的。"
    me01 "社团活动自然也是不允许在这里举办。"
    me01 "这样的话我和雷亚见面的时间就会越来越少了。"
    play voice "voice/天使雷亚/0005040.ogg"
    lst "......"
    me01 "我喜欢樱华镇的星空，所以才会选择加入天协。"
    me01 "但如果雷亚你不在那里的话，我会觉得寂寞的。"
    me01 "所以，就当是为了我能不能请你再考虑一下呢？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 2.0 hard
    "雷亚没有回答。"
    "像是在烦恼应该如何回复我的话。"
    "我捡起了被扔在地上的入部申请书，再次交给了雷亚。"
    pause 2.0 hard
    scene set only starview night road
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    me01 "抱歉，好像是我在强迫你一样。"
    "雷亚叹了口气。"
    show ts_lst_ssz_b1 b1 b1_n1
    play voice "voice/天使雷亚/0005050.ogg"
    lst "真是的。明明说讨厌把心意强加给别人的。"
    me01 "不用马上做决定，先考虑一下吧。"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0005060.ogg"
    lst "也许到最后我也不会签的。"
    me01 "嗯。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0005070.ogg"
    lst "即使这样也不要恨我哦。"
    me01 "嗯。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0005080.ogg"
    lst "......"
    hide ts_lst_ssz_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    "雷亚转过身，似乎是准备离开了。"
    "在临走之际，她回头看向了我。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0005090.ogg"
    lst "再见了，变态君。"
    show ts_lst_ssz_b1 b1 b1_n1 onlayer m2 at basicfade_f2b:
        xpos 0.5
    play sound xiaoshi_1
    hide ts_lst_ssz_b1
    pause 2.0 hard
    stop music fadeout 5.0
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    $ suppress_overlay = True
    jump day06
