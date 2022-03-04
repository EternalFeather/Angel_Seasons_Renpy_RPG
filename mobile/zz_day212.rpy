label day212:
    bookmark
    $ save_name = _("Day 212")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date210 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    show snow_level1 onlayer fg
    with slowerdissolve
    pause 1.0 hard
    "今天是圣诞节。"
    "翔子最终还是同意在家里举办圣诞派对的建议。"
    "天空仍下着小雪。"
    "看来今年会是一个“白色”的圣诞节。"
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    hide snow_level1
    pause 5.0 hard
    play music second_139 fadein 3.0 if_changed
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only party xz_home one
    with slowdissolve
    pause 1.0 hard
    "热闹的氛围充斥着整个房间。"
    "翔子把料理一个接一个地端出来。"
    "无论是幼儿园的小朋友，还是学生会的成员大家都到齐了。"
    pause 1.0 hard
    scene set only home day living_room xuejian
    $ flcam.move(-4500, 300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    play sound appear
    show qianbo_dsf_b1 b1 b1_n4 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/211100010.ogg"
    qb "凉君男，就让你来作我的对手吧。"
    me01 "看在今天是特殊日子的份上，就勉为其难地答应你。"
    show qianbo_dsf_b1 b1 b1_h1
    play voice "voice/千波/211100020.ogg"
    qb "毕竟是圣诞节嘛~"
    me01 "没错。"
    show qianbo_dsf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211100030.ogg"
    qb "毕竟是谈情说爱的圣诞节嘛~"
    me01 "干嘛特地强调这个！？"
    show qianbo_dsf_b1 b1 b1_n4
    play voice "voice/千波/211100040.ogg"
    qb "所以对我的命令要绝对服从呢~"
    me01 "才不要！"
    "这家伙脑海里的恋人就是这样肤浅的关系吗。"
    $ flcam.move(0, 300, 600, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    show ycxt_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111100320.ogg"
    aiyi "小桃不和你的哥哥一起过节吗？"
    play voice "voice/小桃/221100010.ogg"
    ycxt "大哥哥说了派对结束就陪我去逛街~"
    play voice "voice/小桃/221100020.ogg"
    ycxt "而且今天晚上也会一直在一起。"
    me01 "那样的话真是太好了。"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    hide qianbo_dsf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 2.0 hard
    scene set only party xz_home one
    with slowdissolve
    pause 1.0 hard
    me01 "话说回来翔子，这个寿司真好吃。"
    play voice "voice/翔子/011100600.ogg"
    xz "是这样吗......这是最后的料理了。"
    me01 "这些全部都是翔子你准备的吗？"
    play voice "voice/翔子/011100610.ogg"
    xz "不是的，再怎么说这个蛋糕还是买来的。"
    me01 "即便如此也辛苦你了，终于知道为什么爱衣比起“姐姐”那更喜欢这里了。"
    me01 "毕竟......"
    pause 0.1 hard
    scene set only party xz_home two
    with dissolve
    rxl "......"
    "突然感受到来自日向怜充满抗议的目光。"
    "于是我把剩下的话咽了下去。"
    play voice "voice/翔子/011100620.ogg"
    xz "没这回事，毕竟我并不讨厌做菜，当然也不仅限于料理。"
    play voice "voice/翔子/011100630.ogg"
    xz "我并没有把“做家务”当成自己的负担。"
    play voice "voice/翔子/011100640.ogg"
    xz "所以神野君现在的任务不是来帮我，而是好好地陪着爱衣她们哟~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home day living_room xuejian
    $ flcam.move(-4500, 300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show qianbo_dsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100050.ogg"
    qb "凉君男最应该服侍的果然是我吧~"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111100330.ogg"
    aiyi "服侍是什么？"
    $ flcam.move(0, 300, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221100030.ogg"
    ycxt "奶奶说这是一种爱的表现。"
    show qianbo_dsf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211100060.ogg"
    qb "是能加深关系的行为。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111100340.ogg"
    aiyi "也就是结婚吧。"
    play sound jump_1
    hide qianbo_dsf_b1 with None
    pause 0.1 hard
    show qianbo_dsf_b2 b2 b2_ga1 onlayer m2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211100070.ogg"
    qb "谁、谁也没有说想和凉君男结婚什么的！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only party xz_home one
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/011100650.ogg"
    xz "神野君要是真的和谁结婚了的话，肯定会对另一方唯命是从吧。我觉得你就是这种类型。"
    pause 1.0 hard
    scene set only home day living_room xuejian
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    with dissolve
    play voice "voice/小桃/221100040.ogg"
    ycxt "啊......"
    with vpunch
    hide ycxt_dzf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    show drink onlayer texture_c2u
    pause 0.5 hard
    "小桃一个不留神将装满饮料的杯子打翻了。"
    "果汁洒了出来，在桌上蔓延开来。"
    hide drink
    pause 1.0 hard
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/小桃/221100050.ogg"
    ycxt "......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show xz_dzf_b1 b1 b1_sp2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/翔子/011100660.ogg"
    xz "小桃，衣服有没有弄湿吧？"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221100060.ogg"
    ycxt "唔、嗯，没弄湿......"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100670.ogg"
    xz "布偶也没事吗？"
    show ycxt_dzf_b1 b1 b1_s4 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/221100070.ogg"
    ycxt "嗯，对不起......"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100680.ogg"
    xz "不，没关系的~"
    hide xz_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show qianbo_dsf_b1 b1 b1_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211100080.ogg"
    qb "啊......"
    with vpunch
    hide qianbo_dsf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    show food onlayer texture_c2u
    pause 0.5 hard
    "这次是千波把蛋糕上的草莓弄到了地上。"
    "翔子见状仍是一边擦洗着地面的同时一边安慰着千波。"
    hide food
    pause 1.0 hard
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100090.ogg"
    qb "我的草莓......"
    me01 "比起这个赶紧道歉。"
    play sound jump_1
    hide qianbo_dsf_b2 with None
    pause 0.1 hard
    show qianbo_dsf_b1 b1 b1_a2 onlayer m2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211100100.ogg"
    qb "还轮不到凉君男来说我！"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100690.ogg"
    xz "千波不用道歉的，我去给你再拿块新的蛋糕吧~"
    hide qianbo_dsf_b1
    show qianbo_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100110.ogg"
    qb "我、我是不会道谢的。"
    me01 "这点小事就不用谢我了。"
    hide qianbo_dsf_b2 with None
    pause 0.1 hard
    show qianbo_dsf_b1 b1 b1_a2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211100120.ogg"
    qb "凉君男什么都没干吧？！"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/011100700.ogg"
    xz "大家的衣服都没有弄脏真是太好了。"
    show qianbo_dsf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.3
    stop music fadeout 5.0
    play voice "voice/千波/211100130.ogg"
    qb "用餐中保持衣服整洁可是淑女的必修课。"
    hide qianbo_dsf_b1
    hide xz_dzf_b2
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play music second_108 fadein 3.0 if_changed
    play voice "voice/小桃/221100080.ogg"
    ycxt "奶奶说过的，爱衣的大姐姐是容易被激发出母性本能的类型。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100720.ogg"
    xz "这个一般......是男性才会用的词吧。"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221100090.ogg"
    ycxt "啊咧？"
    $ flcam.move(2250, 300, 750, duration=1.5)
    hide xz_dzf_b2
    pause 0.5 hard
    show qianbo_dsf_b2 b2 b2_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/千波/211100150.ogg"
    qb "诱发母性本能后就会变得容易妥协吗？"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221100100.ogg"
    ycxt "啊，没准是这样的。"
    $ flcam.move(0, 300, 600, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111100370.ogg"
    aiyi "怎么回事？"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221100110.ogg"
    ycxt "我也不是很明白......"
    hide qianbo_dsf_b2 with None
    pause 0.1 hard
    show qianbo_dsf_b1 b1 b1_h2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/千波/211100160.ogg"
    qb "指的肯定是被玩弄就会妥协的胸部啦~"
    hide aiyi_dzf_b1
    hide qianbo_dsf_b1
    hide ycxt_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_a1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/011100730.ogg"
    xz "才不是这样的！"
    $ flcam.move(2250, -200, 600, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111100380.ogg"
    aiyi "大哥哥你知道吗？"
    me01 "大概是指你翔子姐姐很擅长照顾人的意思吧。"
    me01 "所以说如果翔子要是喜欢上谁的话，那对方肯定是会给别人添麻烦的类型。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100740.ogg"
    xz "能别一脸正经地瞎分析吗......"
    $ flcam.move(0, 0, 750, duration=1.5)
    show qianbo_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100170.ogg"
    qb "也就是说，爱衣的大姐姐因为母性泛滥的缘故所以喜欢废柴男喽？"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100750.ogg"
    xz "别给我套上奇怪的形象......"
    hide qianbo_dsf_b2
    show qianbo_dsf_b1 b1 b1_n4 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100180.ogg"
    qb "毕竟爱衣的大姐姐很会照顾人嘛~"
    hide xz_dzf_b2
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dsf_b1 b1 b1_ga2
    play voice "voice/千波/211100190.ogg"
    qb "相比之下，凉君男就是完全派不上用场的废柴男。"
    me01 "我废柴吃你家大米了吗！"
    play sound jump_1
    show qianbo_dsf_b1 b1 b1_h2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211100200.ogg"
    qb "毕竟要对我的命令绝对服从~"
    me01 "敲脑袋的话我会服从的。"
    hide qianbo_dsf_b1 with None
    pause 0.1 hard
    show qianbo_dsf_b2 b2 b2_s1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211100210.ogg"
    qb "最近......经常被飞机场老师敲脑袋。"
    me01 "话说你姐姐不也是很会照顾人的类型吗？"
    hide qianbo_dsf_b2
    show qianbo_dsf_b1 b1 b1_h2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100220.ogg"
    qb "那是当然的~"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100770.ogg"
    xz "是啊，泽村同学可是担任学生会长的大人物嘛。"
    show qianbo_dsf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211100250.ogg"
    qb "嗯，所以身为妹妹的我也是最厉害的！"
    me01 "只有添麻烦这一点我承认你是最厉害的。"
    hide xz_dzf_b2
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show qianbo_dsf_b1 b1 b1_a2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211100260.ogg"
    qb "{size=72}哈啊！！！{/size}"
    pause 1.0 hard
    play sound appear
    show qianbo_dsf_b1 b1 b1_a2:
        alpha 1.0 xpos 0.3
        parallel:
            linear 0.5 xpos 0.5
        parallel:
            linear 0.5 alpha 0.0
    pause 0.5 hard
    hide qianbo_dsf_b1
    play sound hite_heavy
    with vpunch
    me01 "{size=72}噗哈！{/size}"
    pause 1.0 hard
    me01 "别用头撞我啊！"
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dsf_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/千波/211100270.ogg"
    qb "无论是美貌还是智慧都是我最强。"
    $ flcam.move(2250, 300, 750, duration=1.5)
    play sound yangmu
    show ycxt_dzf_b1 b1 b1_h2 onlayer m2:
        xpos 0.7
    show yangmu onlayer m2:
        xalign 0.73 yalign 0.52
    play voice "voice/小桃/221100120.ogg"
    ycxt "千波好帅~"
    hide yangmu
    hide ycxt_dzf_b1
    hide qianbo_dsf_b1
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.3
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111100400.ogg"
    aiyi "大、大哥哥，你没事吧？"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/011100790.ogg"
    xz "神野君你深得千波的欢心呢。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111100420.ogg"
    aiyi "没有那回事，最喜欢大哥哥的肯定是大姐姐呀~"
    hide xz_dzf_b2 with None
    pause 0.1 hard
    show xz_dzf_b1 b1 b1_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/011100810.ogg"
    xz "为、为什么是这样的啊？！"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/111100430.ogg"
    aiyi "啊......但是，大姐姐喜欢的是废柴男。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100820.ogg"
    xz "这一点本身也是错误的......"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111100440.ogg"
    aiyi "大哥哥不是废柴男......怎么办呢？"
    hide xz_dzf_b2
    show qianbo_dsf_b2 b2 b2_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/千波/211100280.ogg"
    qb "让凉君男变成废柴不就好了吗？"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111100450.ogg"
    aiyi "大哥哥和爱衣我们不一样，完全不需要别人操心。"
    hide qianbo_dsf_b2
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100830.ogg"
    xz "才没有呢，爱衣反而成熟得多。"
    hide aiyi_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100840.ogg"
    xz "神野君可是连自己的衣服都没办法好好整理的。"
    me01 "我不是有好好地放到衣柜里吗？"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100850.ogg"
    xz "叠得乱七八糟的都起皱了，这样一点意义都没有吧。"
    play voice "voice/翔子/011100860.ogg"
    xz "所以每次我都要帮你重新叠一遍。"
    "完全没有注意到......"
    me01 "那个，帮我整理衣服什么的多谢了。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100870.ogg"
    xz "嘛，都是些小事不用客气的。"
    show xz_dzf_b3 b3 b3_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/011100880.ogg"
    xz "内、内裤什么的我没看到。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221100130.ogg"
    ycxt "盯......"
    hide xz_dzf_b3
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100890.ogg"
    xz "小桃，怎么了吗？"
    play voice "voice/小桃/221100140.ogg"
    ycxt "好像爸爸妈妈一样。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100900.ogg"
    xz "欸？"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221100150.ogg"
    ycxt "感觉大哥哥和大姐姐，就像夫妇一样在对话。"
    play sound jump_1
    show xz_dzf_b1 b1 b1_ga2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/翔子/011100900.ogg"
    xz "{size=72}诶！？{/size}"
    $ flcam.move(0, 0, 600, duration=1.5)
    show qianbo_dsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211100290.ogg"
    qb "与其说是夫妻，不如说是纯情的情侣。"
    hide xz_dzf_b1 with None
    pause 0.1 hard
    show xz_dzf_b2 b2 b2_a2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/翔子/011100910.ogg"
    xz "才不是啦！"
    show qianbo_dsf_b1 b1 b1_sp2
    play voice "voice/千波/211100300.ogg"
    qb "但是还带着项链，就是脖子上那个。"
    "千波指着翔子胸口的吊坠。"
    show ycxt_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/221100160.ogg"
    ycxt "奶奶说，有定情信物的不是恋人就是夫妻。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011100920.ogg"
    xz "这个又不是定情信物。（小声）"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221100170.ogg"
    ycxt "爱衣也结婚了吗？"
    show qianbo_dsf_b1 b1 b1_sp1
    play voice "voice/千波/211100320.ogg"
    qb "和凉君男？"
    hide xz_dzf_b3 with None
    pause 0.1 hard
    show xz_dzf_b2 b2 b2_a2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/011100940.ogg"
    xz "我决不允许！"
    play sound jump_1
    show qianbo_dsf_b1 b1 b1_sp2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211100330.ogg"
    qb "难道说难道说，是和我？！"
    me01 "这一点我也绝不允许的所以请你放心。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day212.yjroom_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    play music second_124 fadein 3.0 if_changed
    with slowdissolve
    pause 2.0 hard
    scene set only home night kitchen xuejian
    with dissolve
    pause 1.0 hard
    me01 "......"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011200260.ogg"
    xz "那个......发生什么事了吗？"
    me01 "怎么没有看到友加。"
    me01 "那家伙可是第一个吵着要来办派对来着。"
    show xz_dzf_b2 b2 b2_s1
    play voice "voice/翔子/011200280.ogg"
    xz "刚才也接到友加打来的电话，那时候我也听到了圣护院小姐的声音。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/011200290.ogg"
    xz "是发生什么了吧......"
    me01 "......"
    me01 "抱歉翔子，我出去一趟。"
    show xz_dzf_b2 b2 b2_n1
    play voice "voice/翔子/011200350.ogg"
    xz "这里的事就交给我，你放心去吧~"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/011200360.ogg"
    xz "如果真的是姐姐回来的话，那是最好的。"
    me01 "无论如何现在去确认一下就知道了。"
    me01 "我会赶在下一场派对开始之前回来的。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011200410.ogg"
    xz "嗯，路上小心~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day212'
    $ seen_day212_yjroom_event02 = False
    $ seen_day212_home_event01 = False

label day212.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day212':
        show set maps winter evening
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day212.yjroom_event02':
        show set maps winter night
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['road2'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        road2=("day212.yjroom_event02", "not seen_day212_yjroom_event02"),
        road1=("day212.home_event01", "not seen_day212_home_event01 and seen_day212_yjroom_event02"))
    $ window_animate_outro()
    if _return == 'day212.yjroom_event02':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day212.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
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

label day212.yjroom_event02:   
    $ flcam.move(0, 0, 0)
    play sound open_door6
    scene set only home night yj_room xuejian
    play music second_140 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    me01 "我进来了，友加。"
    pause 1.0 hard
    scene set only yj_cg home1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021201450.ogg"
    yj "......"
    "刚来到友加公寓门前就看到大门敞开着。"
    "桌上摆着准备好的料理。"
    "沙发上却只有友加独自一个人。"
    "双手抱腿蜷缩着。"
    "似乎正在烦恼着什么，她丝毫没有察觉到我的到来。"
    "或者说已经注意到了，只是没有回应而已。"
    "比想象中要消沉。"
    me01 "那个......"
    play voice "voice/植澄友加/021201460.ogg"
    yj "对不起，难得你来看我。"
    play voice "voice/植澄友加/021201470.ogg"
    yj "总觉得比想象中的还要难受。"
    play voice "voice/植澄友加/021201480.ogg"
    yj "又让凉君，看到我这样子......"
    me01 "别这么说，总之现在我来了。"
    play voice "voice/植澄友加/021201490.ogg"
    yj "果然凉君就是凉君。"
    play voice "voice/植澄友加/021201500.ogg"
    yj "就算只是一会儿也好，可以陪我说说话吗？"
    me01 "如果这样能让你好受些的话。"
    pause 0.1 hard
    scene set only yj_cg home2
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021201520.ogg"
    yj "......"
    play voice "voice/植澄友加/021201530.ogg"
    yj "如果是以前的话。"
    play voice "voice/植澄友加/021201540.ogg"
    yj "不对，具体来说也是最近才察觉到的。"
    play voice "voice/植澄友加/021201550.ogg"
    yj "虽然知道姐姐很忙，没有时间来看我。"
    play voice "voice/植澄友加/021201560.ogg"
    yj "虽然我也清楚会发生这样的事情，但是......"
    play voice "voice/植澄友加/021201570.ogg"
    yj "我也依然像过去那样准备了。"
    play voice "voice/植澄友加/021201580.ogg"
    yj "烧好饭菜，也挂好了装饰。"
    play voice "voice/植澄友加/021201590.ogg"
    yj "我在想或许今年，就能两人一起庆祝圣诞了吧......"
    "友加苦笑着摸了摸头上的圣诞帽。"
    "这个具有欢乐喜庆象征的装饰物，此时却显得有些寂寞。"
    pause 0.1 hard
    scene set only yj_cg home1
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021201600.ogg"
    yj "但是姐姐她......还是没能回来。"
    play voice "voice/植澄友加/021201610.ogg"
    yj "我总是不自觉地去想，会不会又变成这样的结果。"
    play voice "voice/植澄友加/021201620.ogg"
    yj "虽然不愿去思考......但是冥冥之中还是会在意起来。"
    play voice "voice/植澄友加/021201630.ogg"
    yj "对我来说，姐姐就是这样的。"
    "我拿起桌上的电话递了过去。"
    me01 "试着再和她说说吧。"
    me01 "也许此时的她正在赶回来的路上。"
    me01 "亦或者只是想给你一个惊喜所以躲了起来。"
    me01 "我想她一定也......"
    play voice "voice/植澄友加/021201640.ogg"
    yj "嗯，也许是这样没错。"
    play voice "voice/植澄友加/021201650.ogg"
    yj "可是，我还是会害怕。"
    me01 "不是说好了要在翔子家开派对的吗？"
    me01 "不是说好了要一起带给大家欢笑的吗？"
    me01 "如果连你自己都失去了欢笑那该怎么办啊？"
    me01 "呐，友加......"
    play voice "voice/植澄友加/021201660.ogg"
    yj "......"
    me01 "你也稍微反抗一下啊。"
    pause 0.1 hard
    scene set only yj_cg home2
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "我拨通了手中的电话。"
    play sound phone1
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home night yj_room xuejian alpha
    with dissolve
    pause 1.0 hard
    $ flcam.move(3800, -400, 800, duration=1.5)
    pause 1.0 hard
    investigation call block shy_yjf_b1 b1 b1_sp1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    nvl clear
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151200280.ogg"
    c.shy_yjf_b1 "怎么了？"
    hide shy_yjf_b1
    investigation call block yj_dsf_b1 b1 b1_s2 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/021201680.ogg"
    c.yj_dsf_b1 "啊，姐姐......"
    hide yj_dsf_b1
    investigation call block shy_yjf_b1 b1 b1_s1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151200290.ogg"
    c.shy_yjf_b1 "抱歉，说简洁点吧，我现在脱不开身。"
    hide shy_yjf_b1
    investigation call block yj_dsf_b1 b1 b1_s3 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show yj_dsf_b1 b1 b1_s3
    play voice "voice/植澄友加/021201690.ogg"
    c.yj_dsf_b1 "......果然很忙吗？"
    hide yj_dsf_b1
    investigation call block shy_yjf_b1 b1 b1_s3 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151200300.ogg"
    c.shy_yjf_b1 "嗯。"
    hide shy_yjf_b1
    investigation call block yj_dsf_b1 b1 b1_s1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/021201700.ogg"
    c.yj_dsf_b1 "......"
    hide yj_dsf_b1
    investigation call block shy_yjf_b1 b1 b1_n1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151200310.ogg"
    c.shy_yjf_b1 "你打电话来是因为灵纹出现什么异常了吗？"
    hide shy_yjf_b1
    investigation call block yj_dsf_b1 b1 b1_s2 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/021201710.ogg"
    c.yj_dsf_b1 "啊，不是......不是这个原因。"
    hide yj_dsf_b1
    investigation call block shy_yjf_b1 b1 b1_s4 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151200320.ogg"
    c.shy_yjf_b1 "这样的话就好......另外我今天回不去了，抱歉。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151200330.ogg"
    c.shy_yjf_b1 "以上。"
    hide shy_yjf_b1
    investigation call block yj_dsf_b1 b1 b1_s3 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show yj_dsf_b1 b1 b1_s3
    play voice "voice/植澄友加/021201720.ogg"
    c.yj_dsf_b1 "......"
    investigation call end
    play sound phone2
    pause 0.5 hard
    me01 "果然，还是不行吗......"
    "虽然知道圣护院小姐没有恶意，但是这么直白的拒绝还是让人火大。"
    "被事业吞噬了的工作狂真是难搞。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg home1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021201730.ogg"
    yj "......她刚刚说今天不回来了。"
    me01 "对不起......做了多余的事。"
    play voice "voice/植澄友加/021201740.ogg"
    yj "不是凉君的错，会是这样的结果我也早就猜到了的。"
    play voice "voice/植澄友加/021201750.ogg"
    yj "果然对于姐姐来说，我也只是单纯的研究对象而已。"
    play voice "voice/植澄友加/021201760.ogg"
    yj "所以之前才会说要回家的。"
    play voice "voice/植澄友加/021201770.ogg"
    yj "如果{rb}灵纹{/rb}{rt}rune{/rt}保持稳定的话就没有必要回来了吧。"
    play voice "voice/植澄友加/021201790.ogg"
    yj "但是啊......凉君。"
    pause 0.1 hard
    scene set only yj_cg home2
    with dissolve
    play voice "voice/植澄友加/021201800.ogg"
    yj "相比之下凉君却来了，这一点是我没有想过的。"
    play voice "voice/植澄友加/021201810.ogg"
    yj "凉君会劝我打电话什么的，我也从来没有想过。"
    pause 0.1 hard
    scene set only yj_cg home1
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021201820.ogg"
    yj "呐凉君......可以拜托你一件事吗？"
    play voice "voice/植澄友加/021201830.ogg"
    yj "虽然我总是拜托你，总是被你帮助。"
    play voice "voice/植澄友加/021201840.ogg"
    yj "可是、可是......我还是希望能继续拜托你，可以吗？"
    me01 "放马过来吧。"
    pause 0.1 hard
    scene set only yj_cg home3
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021201850.ogg"
    yj "我希望你能继续教我{rb}灵纹{/rb}{rt}rune{/rt}。"
    play voice "voice/植澄友加/021201860.ogg"
    yj "教我更多，为了有朝一日能够熟练地使用这股力量。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    "对于“家庭”这种东西，在我的记忆中早已模糊淡化了。"
    "但是此刻我却能够明白友加的心情。"
    "就是这份执着，让眼前的这个女孩越发耀眼的吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play music second_111 fadein 3.0 if_changed
    scene set only yj_cg home3
    with dissolve
    me01 "我知道了。"
    me01 "虽然不知道自己能够做到什么程度。"
    me01 "但是我一定会把我知道的全部教给你的。"
    pause 0.1 hard
    scene set only yj_cg home4
    with dissolve
    me01 "虽然不是第一次说了。"
    me01 "但是......请多指教~"
    play voice "voice/植澄友加/021201870.ogg"
    yj "......"
    me01 "友加？"
    play voice "voice/植澄友加/021201880.ogg"
    yj "啊、没什么......"
    pause 0.1 hard
    scene set only yj_cg home5
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021201890.ogg"
    yj "谢谢~"
    play voice "voice/植澄友加/021201900.ogg"
    yj "对我来说这就是你给我的圣诞礼物。"
    play voice "voice/植澄友加/021201910.ogg"
    yj "对不起......凉君。还有谢谢你~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day212.laboratory_event01:
    $ flcam.move(0, 0, 0)
    play sound phone2
    play music second_122 fadein 3.0 if_changed
    scene set only laboratory inside2 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    show shy_yjf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151200340.ogg"
    shy "......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041200160.ogg"
    liuli "是友加前辈......对吧？"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041200170.ogg"
    liuli "圣护院小姐您工作的时候很少接电话的......"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151200350.ogg"
    shy "啊，是友加。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041200180.ogg"
    liuli "那个......不回去真的可以吗？"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151200360.ogg"
    shy "今天没这个打算，最近这段时间的工作累积了很多。"
    show liuli_dsf_b3 b3 b3_s2
    play voice "voice/琉璃/041200190.ogg"
    liuli "但是，今天是圣诞节......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151200370.ogg"
    shy "这个不能作为理由。"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041200200.ogg"
    liuli "真的是这样吗？"
    show liuli_dsf_b1 b1 b1_s2
    play voice "voice/琉璃/041200210.ogg"
    liuli "今天是很重要的节日，是必须和重要的人一起度过的。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151200380.ogg"
    shy "我也听说过。但是，我就是我。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151200390.ogg"
    shy "所以......这个无法成为理由。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041200220.ogg"
    liuli "......"
    hide liuli_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151200400.ogg"
    shy "而且，现在友加身边似乎有比我更适合的人选。"
    play voice "voice/圣护院/151200410.ogg"
    shy "比起我能够更加坦率真诚地对待，毫无保留的人在。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151200420.ogg"
    shy "既然是这样就好。"
    play voice "voice/圣护院/151200430.ogg"
    shy "无论发生什么，我......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041200230.ogg"
    liuli "圣护院小姐？"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151200440.ogg"
    shy "啊抱歉，继续吧。"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151200450.ogg"
    shy "看样子那边的情况也开始恶化了。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/041200240.ogg"
    liuli "是的......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day212_yjroom_event02:
        $ seen_day212_yjroom_event02 = True
    $ _overworld_label = "day212.yjroom_event02"
    jump day212.map

label day212.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only home night outside xuejian
    with dissolve
    play sound open_door4
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    scene set only home night living_room xuejian
    $ flcam.move(0, 300, 900, duration=1.5)
    with dissolve
    play music second_106 fadein 3.0 if_changed
    pause 0.5 hard
    play sound appear
    show qianbo_dsf_b1 b1 b1_n4 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/千波/211500010.ogg"
    qb "凉君男，再干一杯！"
    me01 "你要干多少杯才满足啊？"
    $ flcam.move(2250, 300, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221500010.ogg"
    ycxt "千波在之前干杯的时候大哥哥你们还没有回来，所以才很在意。"
    play sound jump_1
    hide qianbo_dsf_b1 with None
    pause 0.1 hard
    show qianbo_dsf_b2 b2 b2_ga1 onlayer m2 at flu_up(0.15, 20):
        xpos 0.5
    play voice "voice/千波/211500020.ogg"
    qb "人、人家才不是想要把他的那一份补回来呢！"
    show rxl_dzf_b1 b1 b1_h2 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121500360.ogg"
    rxl "不过，如果准备很多杯子的话，不就可以一直干杯了吗？"
    hide rxl_dzf_b1
    $ flcam.move(0, 300, 600, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    show qianbo_dsf_b2 b2 b2_n4
    play voice "voice/千波/211500030.ogg"
    qb "就是这样的！爱衣，快去准备！"
    play voice "voice/爱衣/111500090.ogg"
    aiyi "干杯的时候，是要一口气喝完吗？"
    show rxl_dzf_b1 b1 b1_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121500370.ogg"
    rxl "凉君和千波他们是要比试谁喝得更快吧。"
    hide rxl_dzf_b1
    play sound jing01
    hide qianbo_dsf_b2 with None
    pause 0.1 hard
    show qianbo_dsf_b1 b1 b1_a2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/千波/211500040.ogg"
    qb "我是绝对不会输给凉君男的！"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221500020.ogg"
    ycxt "小桃也加入可以吗？"
    me01 "奇怪的比赛交给我就行了。"
    me01 "而且小桃你刚刚也已经喝太多果汁了。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111500100.ogg"
    aiyi "那我就让大姐姐准备大哥哥和千波用的杯子。"
    me01 "不用麻烦翔子了，我用这一个杯子就行了。"
    show qianbo_dsf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/千波/211500050.ogg"
    qb "也就是说我已经赢过凉君男了。"
    play sound yangmu
    show ycxt_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.7
    show yangmu onlayer m2:
        xalign 0.72 yalign 0.52
    play voice "voice/小桃/221500030.ogg"
    ycxt "千波好帅~"
    show aiyi_dzf_b1 b1 b1_ga2
    play voice "voice/爱衣/111500110.ogg"
    aiyi "大哥哥的话，真可惜啊。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111500120.ogg"
    aiyi "千波，一起去吃东西吧，大哥哥和植澄姐姐带了一些点心回来。"
    show qianbo_dsf_b1 b1 b1_n4
    play voice "voice/千波/211500010.ogg"
    qb "凉君男，下次再一起干杯了！"
    hide yangmu
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221500040.ogg"
    ycxt "啊，小桃也......"
    hide ycxt_dzf_b1
    hide qianbo_dsf_b1
    hide aiyi_dzf_b1
    stop music fadeout 5.0
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    me01 "呼......"
    "陪小孩子玩真是累人。"
    play music second_112 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/立花希/031500060.ogg"
    lhx "看起来很累的样子啊。"
    me01 "老实说，我开始打心底里佩服立花老师你了。"
    show lhx_dsf_b2 b2 b2_ga3
    play voice "voice/立花希/031500070.ogg"
    lhx "刚回来就加入畅饮聚会，还要迎合她们会累是当然的吧。"
    me01 "虽然我并不是讨厌这样。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031500080.ogg"
    lhx "也许在适当的时间，离场休息下会更好。"
    me01 "不愧是老师，很擅长处理这样的场面嘛。"
    me01 "那么接下来打算做什么呢？"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031500090.ogg"
    lhx "我去帮青木同学的忙了。"
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_n1 at walkout_r(0.3)
    pause 0.5 hard
    hide lhx_dsf_b1
    me01 "那么，我也趁现在稍微休息一下。"
    "虽然是这么想的......"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500600.ogg"
    szl "......"
    stop music fadeout 5.0
    "正想离开的我正好撞见了独自在角落里站着的水之濑。"
    "刚刚一直被孩子们围着，完全没有发现她的存在。"
    "由于之前的“较量”现在我们之间的气氛还比较尴尬。"
    "这个时候要是有人能来引导一下话题的话......"
    play music second_108 fadein 3.0 if_changed
    $ flcam.move(2250, 0, 750, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_sp1
    show qianbo_dsf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/千波/211500070.ogg"
    qb "吧唧吧唧......这是战利品哟，也分给你吧~"
    "千波把手里的蛋糕递给了水之濑。"
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/小桃/221500050.ogg"
    ycxt "那个，这个也......"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_n4 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500610.ogg"
    szl "谢、谢谢......"
    show ycxt_dzf_b1 b1 b1_s4 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/小桃/221500060.ogg"
    ycxt "......"
    hide ycxt_dzf_b1
    $ flcam.move(2250, 0, 750, duration=1.5)
    pause 0.5 hard
    show qianbo_dsf_b2 b2 b2_ga2
    play voice "voice/千波/211500080.ogg"
    qb "盯~"
    hide szl_dsf_b3
    show szl_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500620.ogg"
    szl "你不和朋友一起过去吗？"
    show qianbo_dsf_b2 b2 b2_n2
    play voice "voice/千波/211500090.ogg"
    qb "小凛你......"
    show szl_dsf_b1 b1 b1_s1
    play voice "voice/水之濑/051500630.ogg"
    szl "我说你啊，直呼名字什么的......倒也无所谓了，再怎么挑小孩子的毛病也是没有用的。"
    show qianbo_dsf_b2 b2 b2_n3
    play voice "voice/千波/211500100.ogg"
    qb "话说回来到目前为止我都没有和小凛你好好说过话。"
    show szl_dsf_b1 b1 b1_n2
    play voice "voice/水之濑/051500640.ogg"
    szl "毕竟你一个劲缠着神野君嘛。"
    hide qianbo_dsf_b2 with None
    pause 0.1 hard
    show qianbo_dsf_b1 b1 b1_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/211500110.ogg"
    qb "最后是我的胜利呢~"
    show qianbo_dsf_b1 b1 b1_h2
    play voice "voice/千波/211500120.ogg"
    qb "总有一天我也能胜过小凛你的。"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500650.ogg"
    szl "你指什么？论干杯的话，我是不会输的。"
    "就算对方是小孩子，水之濑的好胜心也丝毫不会受影响。"
    play sound jing01
    show qianbo_dsf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/211500130.ogg"
    qb "总有一天我会拥有比你和爱衣的姐姐还要大的胸部。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500660.ogg"
    szl "......真是个早熟的孩子。"
    show qianbo_dsf_b1 b1 b1_h2
    play voice "voice/千波/211500140.ogg"
    qb "我经常被这样说。"
    show szl_dsf_b1 b1 b1_s1
    play voice "voice/水之濑/051500670.ogg"
    szl "我又没夸你......"
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500680.ogg"
    szl "总之，就算变大了也没有什么好的，说实话反而很碍事。"
    "认真起来的水之濑，意外地很古板。"
    "换做是我的话直接无视就行了。"
    play sound jump_1
    show qianbo_dsf_b1 b1 b1_a3 at flu_up(0.15, 20):
        xpos 0.7
    play voice "voice/千波/211500150.ogg"
    qb "就算你这样牵制将来的对手也是没有用的！"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500690.ogg"
    szl "的确。"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dsf_b1 b1 b1_n4
    play voice "voice/千波/211500160.ogg"
    qb "小凛你和凉君男是什么关系？"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/051500700.ogg"
    szl "只是单纯的同级生而已。"
    show qianbo_dsf_b1 b1 b1_n1
    play voice "voice/千波/211500170.ogg"
    qb "你和爱衣的大姐姐，是欧派联盟什么的吧？"
    show szl_dsf_b2 b2 b2_a3
    play voice "voice/水之濑/051500710.ogg"
    szl "哪有那种联盟啊......"
    play sound jump_1
    show qianbo_dsf_b1 b1 b1_h2 at flu_up(0.15, 20):
        xpos 0.7
    play voice "voice/千波/211500180.ogg"
    qb "我也要加入！"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500720.ogg"
    szl "我和青木同学只是学生会的同级生罢了！"
    hide qianbo_dsf_b1
    show qianbo_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/千波/211500190.ogg"
    qb "也就是说，你们两个都是我姐姐的手下喽？"
    show szl_dsf_b3 b3 b3_s2
    play voice "voice/水之濑/051500750.ogg"
    szl "你真的和柚子完全不像啊。"
    play sound jing01
    show qianbo_dsf_b2 b2 b2_a2 at flu_up(0.15, 20):
        xpos 0.7
    play voice "voice/千波/211500220.ogg"
    qb "{size=72}喂！{/size}"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500760.ogg"
    szl "为什么要突然对我大叫啊？"
    hide qianbo_dsf_b2
    show qianbo_dsf_b1 b1 b1_a3 onlayer m2:
        xpos 0.7
    play voice "voice/千波/211500230.ogg"
    qb "明明只是姐姐的部下，不要那么嚣张！"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/051500790.ogg"
    szl "也是呢......"
    show qianbo_dsf_b1 b1 b1_ga2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/211500250.ogg"
    qb "盯~"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051500800.ogg"
    szl "这次又怎么了？"
    show qianbo_dsf_b1 b1 b1_h2
    play voice "voice/千波/211500260.ogg"
    qb "除了胸部以外，全部都是我姐姐的胜利喔！"
    show szl_dsf_b2 b2 b2_a1
    play voice "voice/水之濑/051500810.ogg"
    szl "姑且还有身高和成绩也赢了。"
    show qianbo_dsf_b1 b1 b1_n2
    play voice "voice/千波/211500280.ogg"
    qb "小凛你来这种地方参加派对真的可以吗？"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500820.ogg"
    szl "反正我很闲。"
    show qianbo_dsf_b1 b1 b1_sp2
    play voice "voice/千波/211500320.ogg"
    qb "啊！爱衣，要切蛋糕了吗？我也要吃！"
    stop music fadeout 5.0
    pause 0.5 hard
    show qianbo_dsf_b1 b1 b1_sp2 at walkout_r(0.7)
    pause 0.5 hard
    hide qianbo_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 1.0 hard
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500860.ogg"
    szl "突然过来搭话，然后又擅自结束。"
    show szl_dsf_b3 b3 b3_s1
    play voice "voice/水之濑/051500870.ogg"
    szl "嘛，反正得救了......"
    me01 "辛苦了。"
    play music second_112 fadein 3.0 if_changed
    show szl_dsf_b3 b3 b3_ga1
    play voice "voice/水之濑/051500880.ogg"
    szl "看到的话倒是来帮个忙啊。"
    me01 "千波好像也很想和水之濑同学说话。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500890.ogg"
    szl "还以为会说个没完，结果突然就结束了。"
    me01 "千波就是这样的孩子，不要太在意了。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500900.ogg"
    szl "不过老实说，若不是这样的话我还真的不知道要怎么办才好。"
    me01 "不是能好好地对话了吗？"
    show szl_dsf_b1 b1 b1_s1
    play voice "voice/水之濑/051500910.ogg"
    szl "光是跟上她话题我就已经尽全力了，而且有时候连她说些什么都没有明白。"
    me01 "啊，深有同感。"
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500940.ogg"
    szl "小孩子......还真是厉害啊。"
    me01 "嘛，总会习惯的。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051500950.ogg"
    szl "也就是说你已经习惯了？"
    me01 "当然不是！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day212_home_event01:
        $ seen_day212_home_event01 = True
    $ _overworld_label = "seen_day212_home_event01"
    $ seen_kitchen_room = False
    jump day212.myroom_event01

label day212.myroom_event01:
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    pause 1.0 hard
    scene set only home night my_room xuejian
    show xz_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dzf_b3 onlayer m2:
            hide screen investigation_popup
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            move _("厨房") jump day212.kitchenroom_event01
            screen_direction left
            sleep jump day212.sleep

label day212.kitchenroom_event01:
    if not seen_kitchen_room:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ seen_kitchen_room = True
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night kitchen xuejian
        play music second_112 fadein 3.0 if_changed
        $ flcam.move(-4500, 300, 900, duration=1.5)
        with dissolve
        show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        play voice "voice/爱衣/111100490.ogg"
        aiyi "大姐姐，爱衣也来帮忙吧~"
        $ flcam.move(-2250, 0, 750, duration=1.5)
        show xz_dzf_b2 b2 b2_h1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011100950.ogg"
        xz "嗯，谢谢~"
        hide aiyi_dzf_b1
        $ flcam.move(0, -300, 900, duration=1.5)
        pause 0.5 hard
        me01 "那我也......"
        show xz_dzf_b2 b2 b2_n1
        play voice "voice/翔子/011100960.ogg"
        xz "神野君的话不用了。"
        me01 "......为什么啊？"
        show xz_dzf_b2 b2 b2_s1
        play voice "voice/翔子/011100970.ogg"
        xz "料理的话暂且不提，洗碗之类的活神野君没干过吧。要是把碗打碎了就更麻烦了。"
        "对我完全没有信心啊......"
        $ flcam.move(-2250, 0, 750, duration=1.5)
        show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
            xpos 0.3
        play voice "voice/爱衣/111100500.ogg"
        aiyi "大哥哥，你待在客厅就好了。"
        me01 "颜面扫地啊。"
        show xz_dzf_b2 b2 b2_n1
        play voice "voice/翔子/011100980.ogg"
        xz "都说了别在意嘛。"
        "当初同意我留下来的条件之一是能够帮她们分担一些。"
        "可是没想到顺理成章地住下来之后，我却什么忙也帮不上。"
        hide aiyi_dzf_b1
        $ flcam.move(0, -300, 900, duration=1.5)
        pause 0.5 hard
        show xz_dzf_b2 b2 b2_s2
        play voice "voice/翔子/011100990.ogg"
        xz "如果神野君实在想帮忙的话，就做点其他的吧。"
        me01 "比如？"
        "似乎是察觉到了我的失落感，翔子开口道。"
        play voice "voice/翔子/011101000.ogg"
        xz "可以的话帮忙擦下桌子吧。"
        me01 "之前就一直想问，翔子你其实挺会看气氛的吧？"
        hide xz_dzf_b2
        show xz_dzf_b1 b1 b1_s2 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/011101010.ogg"
        xz "偶尔也有这种情况吧。有什么问题吗？"
        me01 "没什么，放心交给我吧~"
        show xz_dzf_b1 b1 b1_ga3
        play voice "voice/翔子/011101020.ogg"
        xz "一个人能做好吧？"
        me01 "这点事情还是可以的，别把我当小孩子啊。"
        show xz_dzf_b1 b1 b1_h1
        play voice "voice/翔子/011101030.ogg"
        xz "开个玩笑啦~"
        stop music fadeout 5.0
        pause 1.0 hard
        scene black
        with slowerdissolve
        pause 1.0 hard
        scene set only home night kitchen xuejian
        show xz_dzf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        $ flcam.move(0, -400, 600)
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
    else:
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night kitchen xuejian
        show xz_dzf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        $ flcam.move(0, -400, 600)
        $ flcam.move(0, -100, 400, duration=3.0)
        with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dzf_b3 onlayer m1:
            camera_pos (scale(2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction right
            move _("卧室") jump day212.myroom_event01

label day212.sleep:
    menu:
        "早点休息":
            if not seen_kitchen_room:
                window mode thought
                me01 "睡觉之前还是先去看看翔子的情况吧。"
                $ flcam.move(0, -100, 400, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            show xz_dzf_b3 b3 b3_h1
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
    jump day213
