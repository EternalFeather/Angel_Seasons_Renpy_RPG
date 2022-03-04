label day205:
    bookmark
    $ save_name = _("Day 205")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    pause 2.0 hard
    show backend_date204 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    play music second_114 fadein 3.0 if_changed
    scene set only school day room xuejian
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_tcf_b2 b2 b2_h1 onlayer m1 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/植澄友加/020101890.ogg"
    yj "早上好二位~"
    me01 "噢，早上好。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/翔子/010103330.ogg"
    xz "早上好。"
    hide yj_tcf_b2
    show yj_tcf_b3 b3 b3_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020101900.ogg"
    yj "翔子你今天又和凉君一起上学了啊。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010103340.ogg"
    xz "碰巧而已......"
    me01 "比起这个，为什么是体操服？"
    hide xz_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    show yj_tcf_b3 b3 b3_h1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/植澄友加/020101910.ogg"
    yj "当然是因为刚晨练完嘛~"
    show yj_tcf_b3 b3 b3_ga1
    play voice "voice/植澄友加/020101920.ogg"
    yj "虽然就我一个人......"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010103350.ogg"
    xz "快要考试了，是不是该放下社团活动努力学习一下了？"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_a1 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020101930.ogg"
    yj "我有在好好学习啊，虽然是体育方面。"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/010103360.ogg"
    xz "友加的话实技没问题的吧。不如多学习一下保健体育如何？"
    show yj_tcf_b2 b2 b2_h3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020101940.ogg"
    yj "真是好色啊~~~"
    show xz_dzf_b2 b2 b2_a1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010103370.ogg"
    xz "不是指那些啦！"
    hide xz_dzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    me01 "对了友加，我有些事情想问你。"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_n2 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020101950.ogg"
    yj "刚好我也有事想要问凉君你。"
    me01 "如果你是指昨天的事情可以去问一诚同学。"
    hide yj_tcf_b1 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_h1 onlayer m1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/植澄友加/020101960.ogg"
    yj "昨天已经给一诚君打过电话了。能平安找到小桃真是太好了~"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010103380.ogg"
    xz "神野君想要问的事情是？"
    me01 "其实我也只是想要确认下你们对昨天的事情了解多少。"
    "{rb}灵纹{/rb}{rt}rune{/rt}的事还是越少人知道越好。"
    "毕竟和警察解释起来可是相当的麻烦啊......"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020101990.ogg"
    yj "听一诚君说当时神社的情况真的很糟？"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010103390.ogg"
    xz "神社发生什么了吗？"
    show yj_tcf_b2 b2 b2_n1
    play voice "voice/植澄友加/020102000.ogg"
    yj "据说好像是建筑倒塌了，虽然具体的情况一诚君好像也不知道的样子。"
    me01 "是这样啊，那太可惜了......"
    "看大家的反应，应该是勉强隐瞒过去了。"
    hide xz_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_n2 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020102030.ogg"
    yj "凉君......你知道些什么？"
    me01 "为什么这样问？"
    hide yj_tcf_b1
    show yj_tcf_b3 b3 b3_n2 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020102040.ogg"
    yj "因为凉君似乎比一诚君还要早到神社的样子。"
    me01 "当时的情况非常混乱，我也完全搞不懂。"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020102050.ogg"
    yj "哼嗯~"
    me01 "......"
    me01 "..."
    me01 "比、比起这个，早上新闻不是有相关的报道吗？"
    hide yj_tcf_b2
    show yj_tcf_b3 b3 b3_a1 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020102060.ogg"
    yj "不仅是神社的事故，城市各处好像都在发生不明原因的事故。"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_s1 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020102070.ogg"
    yj "比如突然刮起狂风，房子突然燃烧起来，突然打雷，河水水位突然升高之类的。"
    me01 "竟然有这种事......"
    hide yj_tcf_b2
    show yj_tcf_b3 b3 b3_n2 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020102080.ogg"
    yj "还有人突然消失了的传闻哟，虽然后来被找到了。"
    hide yj_tcf_b3
    show yj_tcf_b1 b1 b1_s1 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020102090.ogg"
    yj "所以当时听说小桃不见了，我就更担心了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010103440.ogg"
    xz "友加对这些事情似乎很清楚嘛。"
    hide yj_tcf_b1 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_ga4 onlayer m1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020102120.ogg"
    yj "都是从姐姐那里听来的，虽然有些时候是我缠着她强行问到的。"
    show xz_dzf_b2 b2 b2_n1
    play voice "voice/翔子/010103450.ogg"
    xz "你姐姐是在新城区工作吧？"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_n3 onlayer m1:
        xpos 0.3
    play voice "voice/植澄友加/020102130.ogg"
    yj "是啊，是在一个叫“星天宫研究所”的地方。"
    "星天宫......{w=0.5}{nw}"
    extend "研究所？！"
    me01 "新城区的研究所不是研究行星探测的吗？"
    show yj_tcf_b2 b2 b2_sp1
    play voice "voice/植澄友加/020102140.ogg"
    yj "欸？行星？"
    hide yj_tcf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    show xz_dzf_b2 b2 b2_s1
    play voice "voice/翔子/010103460.ogg"
    xz "果然是这样啊，神野君对宇宙开发之类的还是的很在意嘛......（小声）"
    hide xz_dzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    play sound open_door5
    pause 2.0 hard
    show yczs_dzf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.7)
    pause 0.5 hard
    play voice "voice/一诚总司/180101680.ogg"
    yczs "哟，大家早啊~"
    $ flcam.move(2250, -200, 600, duration=1.5)
    show yj_tcf_b2 b2 b2_n3 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020102290.ogg"
    yj "一诚君，早上好。"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/180101690.ogg"
    yczs "为什么你又穿着体操服？"
    hide yj_tcf_b2
    show yj_tcf_b3 b3 b3_h1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020102300.ogg"
    yj "当然是因为晨练呀！"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180101700.ogg"
    yczs "还是那么精神。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/010103530.ogg"
    xz "一诚君你今天看起来很有精神。"
    show yczs_dzf_b1 b1 b1_n1
    play voice "voice/一诚总司/180101710.ogg"
    yczs "没有那种事。"
    me01 "果然是因为和小桃的关系变好了吧。"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180101720.ogg"
    yczs "嘛，算是吧~"
    show yczs_dzf_b1 b1 b1_n1
    play voice "voice/一诚总司/180101730.ogg"
    yczs "送妹妹上学还是第一次。"
    play voice "voice/一诚总司/180101740.ogg"
    yczs "放学后去接她也是。"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020102310.ogg"
    yj "放学后？一诚君，社团活动怎么办？"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180101750.ogg"
    yczs "今天开始暂停了吧。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/010103540.ogg"
    xz "直到考试完毕为止。"
    hide yj_tcf_b2 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3 b3_ga2 onlayer m1 at flu_down(0.15, 20):
        xpos 0.48
    show han onlayer m2:
        xpos 0.405 ypos 0.29
    play voice "voice/植澄友加/020102320.ogg"
    yj "{size=72}没听说过啊！{/size}"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/010103550.ogg"
    xz "之前也说过的吧。"
    hide han
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_h3 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020102330.ogg"
    yj "凉君，看来只剩下你和我一起挥洒青春的汗水了呢。"
    me01 "抱歉，我要去接爱衣，你一个人加油吧，奋~斗~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard

label day205.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day center room xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    me01 "下雪了吗......"
    "就在我和往常一样来到中庭的时候，琉璃已经坐在那里了。"
    play music second_133 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040102290.ogg"
    liuli "神野前辈，等你很久了。今天的长椅也暖好了。"
    me01 "啊，谢谢你。"
    show liuli_dzf_b3 b3 b3_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/琉璃/040102300.ogg"
    liuli "是！今天很冷呢~"
    hide liuli_dzf_b3
    $ flcam.move(4500, 1500, 1100, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s1 onlayer screens at side_left('tyt'), basicfade
    play voice "voice/藤原瞳/130100930.ogg"
    tyt "因为太冷了所以只能冬眠了......呼~"
    hide tyt_wnf_b1
    "藤原瞳此时已经横躺在琉璃暖过的长椅上。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040102310.ogg"
    liuli "神野前辈也请入坐吧。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg center normal snow
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/040102320.ogg"
    liuli "那个......神野前辈。"
    play voice "voice/琉璃/040102330.ogg"
    liuli "我有事想要问你。"
    me01 "是关于小桃的伤势问题吧？"
    pause 0.1 hard
    scene set only liuli_cg center normal2 snow
    with dissolve
    play voice "voice/琉璃/040102340.ogg"
    liuli "啊不是......虽然那个也很在意。"
    play voice "voice/琉璃/040102360.ogg"
    liuli "小桃没受伤真是太好了，但总感觉发生了很多不可思议的事。"
    pause 0.1 hard
    scene set only liuli_cg center sad snow
    with dissolve
    play voice "voice/琉璃/040102390.ogg"
    liuli "藤原同学似乎也没怎么在意昨天的事情。甚至是一副基本忘掉的感觉。"
    me01 "那家伙说不定只是真的忘记了而已。"
    pause 0.1 hard
    scene set only liuli_cg center normal2 snow
    with dissolve
    play voice "voice/琉璃/040102410.ogg"
    liuli "神野前辈你知道些什么吗？"
    "得想办法先瞒过去。"
    "记得刚才友加是这么说的......"
    me01 "我觉得应该是异常气象导致的吧。"
    me01 "你看最近不是也常报道类似的事件吗。"
    pause 0.1 hard
    scene set only liuli_cg center sp snow
    with dissolve
    play voice "voice/琉璃/040102430.ogg"
    liuli "是这样吗？"
    me01 "就是这样的。"
    play voice "voice/琉璃/040102440.ogg"
    liuli "好厉害......这样一来谜团就解开了。"
    me01 "那太好了。"
    pause 0.1 hard
    scene set only liuli_cg center normal2 snow
    with dissolve
    play voice "voice/琉璃/040102460.ogg"
    liuli "总感觉在这之前神野前辈就已经预料到了一般。"
    me01 "是你多虑了吧。"
    play voice "voice/琉璃/040102470.ogg"
    liuli "即使如此，那场风暴依然有很多无法解释的地方。"
    me01 "所以说那个是异常气象......"
    play voice "voice/琉璃/040102480.ogg"
    liuli "以那样的时间、那样的温度条件，怎么想都无法形成风暴。"
    play voice "voice/琉璃/040102490.ogg"
    liuli "也就是说，仅考虑自然因素会发生风暴的概率几乎为零。"
    play voice "voice/琉璃/040102500.ogg"
    liuli "所以只能认为是其他原因导致的了。"
    me01 "呐琉璃，比起这个......"
    pause 0.1 hard
    scene set only liuli_cg center sp snow
    with dissolve
    play voice "voice/琉璃/040102510.ogg"
    liuli "什么事？"
    me01 "神社那边情况怎么样？果然很糟糕吗？"
    pause 0.1 hard
    scene set only liuli_cg center normal snow
    with dissolve
    play voice "voice/琉璃/040102520.ogg"
    liuli "是的，藤原同学说今天已经开始修复了。"
    play voice "voice/琉璃/040102530.ogg"
    liuli "幸好没有伤到人，建筑的话只要重新加固一下就没事了。"
    play voice "voice/琉璃/040102540.ogg"
    liuli "这样的话似乎也能赶上初诣了。"
    me01 "太好了，真是松了口气。"
    pause 0.1 hard
    scene set only liuli_cg center normal2 snow
    with dissolve
    play voice "voice/琉璃/040102550.ogg"
    liuli "那么接着刚才的话题......"
    me01 "呐琉璃，我还有件事想问你。"
    pause 0.1 hard
    scene set only liuli_cg center sp snow
    with dissolve
    play voice "voice/琉璃/040102560.ogg"
    liuli "什么事？"
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
    me01 "太好了。"
    pause 0.1 hard
    scene set only liuli_cg center sp snow
    with dissolve
    play voice "voice/琉璃/040102700.ogg"
    liuli "啊但是，现在不是临近考试的时间吗？不准备的话没问题吗？"
    me01 "考试是下周来着，应该来得及。"
    play voice "voice/琉璃/040102710.ogg"
    liuli "是的，从下周开始持续一周。"
    me01 "如果你觉得没问题的话，导游的任务可以拜托你吗？"
    play voice "voice/琉璃/040102770.ogg"
    liuli "那么，就让我带你参观研究所还有新城区商店街那边吧。"
    me01 "帮大忙了~"
    pause 0.1 hard
    scene set only liuli_cg center normal2 snow
    with dissolve
    play voice "voice/琉璃/040102780.ogg"
    liuli "那么关于风暴的事情......"
    me01 "琉璃，我喜欢你。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only school day center room xuejian alpha
    with dissolve
    show snow_level1 onlayer fg
    show liuli_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040102790.ogg"
    liuli "......你刚才说了啥？"
    me01 "琉璃，我喜欢你，做我的女朋友吧！"
    play sound jump_1
    show liuli_dzf_b3 b3 b3_ga1 at flu_up(0.15, 30):
        xpos 0.5
    show yun onlayer m2:
        xalign 0.495 yalign 0.35 zoom 0.75
    show yun1 onlayer m2:
        xalign 0.5 yalign 0.28 zoom 0.75
    play voice "voice/琉璃/040102800.ogg"
    liuli "{size=72}哈哇！？{/size}"
    me01 "你没事吧。"
    hide yun
    hide yun1
    show liuli_dzf_b3 b3 b3_s5
    play voice "voice/琉璃/040102810.ogg"
    liuli "前、前辈才是没问题吧？！"
    me01 "我只是开个玩笑，没想到你的反应会这么激动。"
    hide liuli_dzf_b3
    show liuli_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040102820.ogg"
    liuli "不是激动，是被吓到了......害得我连想说什么都忘了。"
    "好样的，成功摆脱话题。"
    hide liuli_dzf_b1
    show liuli_dzf_b3 b3 b3_s5 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040102830.ogg"
    liuli "啊，我想起来了，神野前辈是个花花公子。"
    me01 "才不是呢！"
    show liuli_dzf_b3 b3 b3_s1
    play voice "voice/琉璃/040102850.ogg"
    liuli "啊，这次真的想起来了，好像是风暴......"
    me01 "不对哦，是带我逛商店街的话题。"
    hide liuli_dzf_b3
    show liuli_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040102860.ogg"
    liuli "是这样吗？"
    me01 "是的。"
    me01 "那么周末在大桥上集合可以吗？"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg center normal snow
    with dissolve
    play voice "voice/琉璃/040102870.ogg"
    liuli "啊，好的~"
    me01 "到时候就是我们两人的约会时间了。"
    pause 0.1 hard
    scene set only liuli_cg center shy snow
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/040102880.ogg"
    liuli "啊是的，请多指教！"
    play voice "voice/琉璃/040102900.ogg"
    liuli "我还是第一次在休息日的时候和朋友出去玩。"
    "琉璃看起来挺高兴的样子。"
    "不管怎么说总算是摆脱那个话题了。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard

label day205.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 2.0 hard
    play music second_118 fadein 3.0 if_changed
    scene set only school evening inside xuejian
    with dissolve
    pause 1.0 hard
    me01 "久等了爱衣，我们来接你了。"
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/210100730.ogg"
    qb "才不需要大人的接送，毕竟我们都是大人了嘛。"
    me01 "你可是最不让人省心的那个。"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s2 onlayer m1:
        xpos 0.5
    play voice "voice/小桃/220101620.ogg"
    ycxt "那个，凉君......"
    hide qianbo_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s4
    play voice "voice/小桃/220101630.ogg"
    ycxt "昨天没能好好谢谢你。"
    show ycxt_dzf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/小桃/220101640.ogg"
    ycxt "能来救我，非常感谢！"
    play voice "voice/小桃/220101650.ogg"
    ycxt "帮我找回布偶，非常感谢！"
    "原本总是躲在千川老师背后的那个身影现在也能鼓起勇气来到我面前了。"
    "这是何等让人高兴的事情。"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show qianbo_dzf_b1 b1 b1_h4 onlayer m2:
        xpos 0.3
    play voice "voice/千波/210100740.ogg"
    qb "还没到需要鞠躬道谢的程度啦~"
    me01 "都说了这话不应该由你来说。"
    hide qianbo_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/180101760.ogg"
    yczs "哦，这不是神野和青木同学吗？"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010103580.ogg"
    xz "来接小桃吗？"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180101770.ogg"
    yczs "是这样的。"
    me01 "毕竟早上也是这么说的。"
    play voice "voice/一诚总司/180101780.ogg"
    yczs "嘛，约好了没有社团活动的时候就由我来接送。"
    hide xz_dzf_b2
    hide yczs_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s4 onlayer m2:
        xpos 0.3
    play voice "voice/小桃/220101660.ogg"
    ycxt "哥哥，听说你还有考试......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show yczs_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/一诚总司/180101790.ogg"
    yczs "总是坐着学习也会累的。"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/180101800.ogg"
    yczs "所以休息的时候就过来接你吧。"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/220101680.ogg"
    ycxt "嗯！"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/小桃/220101690.ogg"
    ycxt "好开心~"
    show yczs_dzf_b1 b1 b1_n1
    play voice "voice/一诚总司/180101820.ogg"
    yczs "那么小桃我们回家吧。"
    show ycxt_dzf_b1 b1 b1_h1 at flu_down(0.25, 20):
        xpos 0.3
    play voice "voice/小桃/220101700.ogg"
    ycxt "嗯！"
    hide yczs_dzf_b1
    $ flcam.move(-2250, 300, 750, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110101830.ogg"
    aiyi "拜拜，小桃~"
    $ flcam.move(0, -200, 600, duration=1.5)
    show qianbo_dzf_b1 b1 b1_a3 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210100750.ogg"
    qb "人家就算一个人也能回去的......"
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_sp1 at flu_down(0.35, 20):
        xpos 0.7
    me01 "好乖好乖。"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 30):
        xpos 0.7
    play voice "voice/千波/210000130.ogg"
    qb "别摸我的头啊！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 2.0 hard
    scene set only school evening outside xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    me01 "昨天有好好休息吗？"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/030104580.ogg"
    lhx "本来是想要休息来着，但是为了阻止日向用额头来量体温搞得更累了。"
    me01 "那周末也请好好休息吧。"
    play voice "voice/立花希/030104590.ogg"
    lhx "虽然是想这样的，不过在此之前要一起去熟悉一下新城区吗？"
    me01 "等你恢复精神了再说吧。"
    hide lhx_dzf_b2 with None
    pause 0.1 hard
    show lhx_dzf_b3 b3 b3_n3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/030104600.ogg"
    lhx "那凉君你这周末的打算是什么？"
    show lhx_dzf_b3 b3 b3_s1
    play voice "voice/立花希/030104610.ogg"
    lhx "还想说没有预定的话，就一起去新城区逛逛的。"
    me01 "比起这个我倒是觉得休息才是首要任务。"
    show lhx_dzf_b3 b3 b3_n3
    play voice "voice/立花希/030104620.ogg"
    lhx "今天也只是普通的幼儿园日常工作而已。"
    me01 "工作的疲劳不也会积累起来吗？休息日就和日向两个人好好放松一下吧。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104630.ogg"
    lhx "就是因为和日向一起才放松不了的。"
    me01 "去新城区的事之后还有机会的。"
    show lhx_dzf_b2 b2 b2_s2
    play voice "voice/立花希/030104640.ogg"
    lhx "我知道了......"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/030104650.ogg"
    lhx "这样一来下一次见面就是下周的事情了。"
    me01 "是啊。"
    show lhx_dzf_b2 b2 b2_ga1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/030104660.ogg"
    lhx "在那之前我的贞操如果被日向夺走的话，就是凉君你的责任。"
    me01 "......这种事谁管你啊！"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104670.ogg"
    lhx "可要好好地负起责任。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day205.memory_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    play music second_134 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "究竟是从何时起的呢......"
    "我又开始接受别人走进我的世界了。"
    "明明这样说不定又会失去重要的东西。"
    "但却还是接受了。"
    "脑海里有过类似的经历。"
    "这就是......所谓的救赎吗？"
    "那么又是谁将这一切来之不易的美好带到我的身边的呢？"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    "说不定因为过去我眼中的她......"
    pause 1.0 hard
    scene set only xfe_cg memory1
    with dissolve
    play voice "voice/希菲尔/000100170.ogg"
    xfe "我来玩了哟，凉君。"
    play voice "voice/希菲尔/000100180.ogg"
    xfe "今天要去哪里呢？"
    play voice "voice/希菲尔/000100190.ogg"
    xfe "要让这足迹延续到哪里呢？"
    pause 0.5 hard
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/000100200.ogg"
    xfe "无论去哪里都可以哟~"
    play voice "voice/希菲尔/000100210.ogg"
    xfe "因为这足迹是两人一起走过的证明。"
    play voice "voice/希菲尔/000100220.ogg"
    xfe "即使途中混入了其他人的足迹......就算在那之后完全融化消失了。"
    play voice "voice/希菲尔/000100230.ogg"
    xfe "希菲尔我......都会记得的。"
    pause 0.1 hard
    scene set only xfe_cg memory2
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/000100240.ogg"
    xfe "和凉君一起经历的事情，永远永远都会记得的哟——"
    pause 1.0 hard
    scene white
    with slowerdissolve
    stop music fadeout 5.0
    pause 2.0 hard
    scene black 
    with slowerdissolve
    
    $ persistent.lingyin = True
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    jump second_menu
