
label day222:
    bookmark
    $ save_name = _("Day 222")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date221 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian3
    play music second_133 fadein 3.0 if_changed
    with slowdissolve
    "一觉醒来神清气爽。"
    "打开窗户，迎面就是一阵微风吹到脸上。"
    "人工岛上的气温恰到好处，看天气似乎很适合出行。"
    "碰巧今天没有训练，于是我打算和琉璃一起出去放松一下。"
    "毕竟这几天除了训练之外几乎没有其他的活动了。"
    pause 1.0 hard
    scene set only rocket_center room1
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/041416460.ogg"
    liuli "因为是和平时一样的时间起床，所以还是绰绰有余的~"
    me01 "难得的休息日，不好好放松一下可不行。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041416480.ogg"
    liuli "前辈的语气越来越像圣护院小姐了。"
    me01 "是这样吗？"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041416490.ogg"
    liuli "那么前辈首先想要去哪里呢？"
    me01 "比起我琉璃有想去的地方吗？"
    hide liuli_dsf_b3 with None
    pause 0.1 hard
    show liuli_dsf_b2 b2 b2_h1 onlayer m2 at flu_down(0.2, 20):
        xpos 0.5
    play voice "voice/琉璃/041416610.ogg"
    liuli "我的话是摩天轮吧~"
    me01 "游乐园吗？"
    show liuli_dsf_b2 b2 b2_n1
    play voice "voice/琉璃/041416620.ogg"
    liuli "不是的，就在岛上的瞭望台附近。"
    show liuli_dsf_b2 b2 b2_h1
    play voice "voice/琉璃/041416630.ogg"
    liuli "虽然从这里也可以眺望整座岛的美景，但如果是从摩天轮的话我想应该可以看得更清楚。"
    me01 "也就是说琉璃你想坐那个摩天轮吗？"
    show liuli_dsf_b2 b2 b2_ga3
    play voice "voice/琉璃/041416640.ogg"
    liuli "是的......但一个人的话有总觉得有点难为情。"
    me01 "那就一起去吧。"
    show liuli_dsf_b2 b2 b2_h1 at flu_down(0.2, 20):
        xpos 0.5
    play voice "voice/琉璃/041416650.ogg"
    liuli "嗯~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    play music second_151 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg motian1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041416660.ogg"
    liuli "哇~"
    "身处瞭望台的摩天轮上。"
    "慢慢地、旋转着。"
    "仿佛天地都融为了一体。"
    "又仿佛置身于混沌的宇宙中一般。"
    "琉璃紧将身子贴在巨大的玻璃窗上放声欢呼着。"
    "在窗户的另一头，是望不到尽头的海天。"
    "无论是翡翠的海水，还是雪白的山峰都能尽收眼底。"
    "就连平日里都能看见的火箭发射台。"
    "此刻都觉着是绝佳的美景。"
    pause 0.1 hard
    scene set only liuli_cg motian2
    with dissolve
    play voice "voice/琉璃/041416670.ogg"
    liuli "那是总面积970万平方米，本土最大的发射基地！"
    play voice "voice/琉璃/041416680.ogg"
    liuli "不仅仅是大而已，那面向海岸线的构造，还被称为世界第一美丽的发射基地呢~"
    pause 0.1 hard
    scene set only liuli_cg motian3
    with dissolve
    play voice "voice/琉璃/041416690.ogg"
    liuli "搭载火星探测机的火箭。"
    play voice "voice/琉璃/041416700.ogg"
    liuli "再过不久我就要乘着它，开始宇宙之旅。"
    play voice "voice/琉璃/041416710.ogg"
    liuli "也许等待着我的将是非常黑暗的宇宙空间......普通人难以忍受的严酷环境。"
    pause 0.1 hard
    scene set only liuli_cg motian2
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041416720.ogg"
    liuli "但只要想到还有前辈在我身边的话。"
    play voice "voice/琉璃/041416730.ogg"
    liuli "有前辈在支持着我的话。"
    play voice "voice/琉璃/041416740.ogg"
    liuli "我就能继续前进。"
    play voice "voice/琉璃/041416760.ogg"
    liuli "就能回应大家的期待了。"
    pause 0.1 hard
    scene set only liuli_cg motian1
    with dissolve
    play voice "voice/琉璃/041416770.ogg"
    liuli "我的、我们的{rb}灵纹{/rb}{rt}rune{/rt}为人类做出贡献的时刻终于要到来了。"
    play voice "voice/琉璃/041416780.ogg"
    liuli "没有比这更令人兴奋的事情了。"
    play voice "voice/琉璃/041416790.ogg"
    liuli "我也终于体会到作为一名{rb}灵继者{/rb}{rt}elfin{/rt}真是太好了。"
    pause 0.1 hard
    scene set only liuli_cg motian2
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    me01 "为了人类、为了谁之类的暂且不说，比起这些......"
    me01 "我更希望琉璃你能够优先考虑自己。"
    me01 "要以宇宙为目标的话，我希望你能优先以自己的目标而启程。"
    me01 "为了能够实现自己的梦想，为了能够尽快平安地回来。"
    "是啊，荣誉什么的都不是最重要的。"
    "只要你能够平安回来，对我来说就已经是最大的光荣了。"
    pause 0.1 hard
    scene set only liuli_cg motian3
    with dissolve
    play voice "voice/琉璃/041416800.ogg"
    liuli "前辈......"
    pause 0.1 hard
    scene set only liuli_cg motian2
    with dissolve
    play voice "voice/琉璃/041416810.ogg"
    liuli "没问题的，我不是说过的吗？"
    play voice "voice/琉璃/041416820.ogg"
    liuli "这个计划成功的话，我就能真正作为一名{rb}灵继者{/rb}{rt}elfin{/rt}被大家认可了。"
    pause 0.1 hard
    scene set only liuli_cg motian4
    with dissolve
    play voice "voice/琉璃/041416830.ogg"
    liuli "所以，这也是为了我自己。"
    play voice "voice/琉璃/041416840.ogg"
    liuli "为了认可身为{rb}灵继者{/rb}{rt}elfin{/rt}的自己，我才会选择走向宇宙的。"
    pause 0.1 hard
    scene set only liuli_cg motian2
    with dissolve
    play voice "voice/琉璃/041416860.ogg"
    liuli "前辈你又是怎么想的呢？"
    play voice "voice/琉璃/041416870.ogg"
    liuli "前辈也是为了自己才选择加入计划的吗？"
    me01 "......我当然也是为了全人类。"
    "不是的。"
    "我之所以在这里的原因并不是为了自己。"
    "友加也好，琉璃也罢，一切的一切我都只是想要留住身边的人而已。"
    "说到底我也只是为了满足自己对朋友的依赖心罢了。"
    "然而，琉璃比我要无私得多，心里想的永远都是组织、是人类的未来。"
    "相比之下这样的我......简直太过渺小了。"
    pause 0.1 hard
    scene set only liuli_cg motian4
    with dissolve
    play voice "voice/琉璃/041416880.ogg"
    liuli "太好了~"
    play voice "voice/琉璃/041416920.ogg"
    liuli "我真是个非常幸运的人。"
    play voice "voice/琉璃/041416930.ogg"
    liuli "能和前辈一起见证宇宙奥秘的我，一定是被上天眷恋的。"
    pause 0.1 hard
    scene set only liuli_cg motian1
    with dissolve
    play voice "voice/琉璃/041416940.ogg"
    liuli "已经......没有什么需要担心的了。"
    play voice "voice/琉璃/041417010.ogg"
    liuli "只要我有名为{rb}灵纹{/rb}{rt}rune{/rt}的羁绊维系着我们，我就能克服内心的恐惧了。"
    pause 0.1 hard
    scene set only liuli_cg motian4
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041417020.ogg"
    liuli "计划失败的概率从此刻起，已经是零了~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard

label day222.rocket_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian3
    with slowdissolve
    pause 1.0 hard
    "几周后......"
    pause 1.0 hard
    scene set only rocket_center day outside klns
    with dissolve
    play ambience1 space_ship fadein 3.0
    play music second_151 fadein 3.0 if_changed
    me01 "高度、速度良好，动力正常。"
    me01 "就这样进入最后的姿势调整。"
    me01 "琉璃，现在那边的状况如何？"
    me01 "这里是控制室，请回答。"
    stop ambience1 fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    scene set only space ship1
    with slowdissolve
    pause 1.0 hard
    me01 "这个任务完成之后，和我一起回雪见市吧？"
    pause 1.0 hard
    scene set only liuli_cg space1
    with dissolve
    play voice "voice/琉璃/041419660.ogg"
    liuli "哇啊啊啊！"
    play voice "voice/琉璃/041419670.ogg"
    liuli "请不要突然说这么让人害羞的话......在听的可不止我们两个。"
    play voice "voice/琉璃/041419680.ogg"
    liuli "而且总觉得立了一个奇怪的flag好不吉利的说......"
    me01 "比起那个请一定要好好检查安全状况。"
    play voice "voice/琉璃/041419700.ogg"
    liuli "被敷衍过去了......"
    pause 0.1 hard
    scene set only liuli_cg space2
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041419710.ogg"
    liuli "是的，现在指示灯全部显示绿色。"
    play voice "voice/琉璃/041419720.ogg"
    liuli "接下来将进入姿势调整阶段，向左侧低速回旋。"
    me01 "回转速率OK，进入预定轨道。"
    me01 "记得别太依赖{rb}灵纹{/rb}{rt}rune{/rt}。"
    play voice "voice/琉璃/041419730.ogg"
    liuli "虽然自动恒温系统不知什么原因而存在一些偏差，但是通过手动调节的话应该是没有问题。"
    me01 "引擎方面似乎也检测到了故障，这部分也是通过{rb}灵纹{/rb}{rt}rune{/rt}修复的吗......负担这么多真的没问题吗？"
    play voice "voice/琉璃/041419740.ogg"
    liuli "请不要这么说，宇宙探测中不出现意外情况的例子至今还是很少的。"
    play voice "voice/琉璃/041419750.ogg"
    liuli "正因如此才需要{rb}灵继者{/rb}{rt}elfin{/rt}飞行员不是吗？"
    play voice "voice/琉璃/041419760.ogg"
    liuli "而且，到现在为止都还算顺利。"
    pause 0.1 hard
    scene set only liuli_cg space3
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041419770.ogg"
    liuli "......"
    me01 "琉璃？"
    play voice "voice/琉璃/041419780.ogg"
    liuli "是的......我在听。"
    me01 "刚刚也是，你的回答延迟了一下......发生什么事情了？"
    play voice "voice/琉璃/041419790.ogg"
    liuli "抱歉，我只是开小差了而已。"
    me01 "是身体出现异常了吗？"
    pause 0.1 hard
    scene set only liuli_cg space2
    with dissolve
    play voice "voice/琉璃/041419800.ogg"
    liuli "全是绿灯的说，计量器没有这样显示吗？"
    me01 "状态显示良好，可是总觉的怪怪的......"
    pause 0.1 hard
    scene set only liuli_cg space3
    with dissolve
    play voice "voice/琉璃/041419810.ogg"
    liuli "稍微......能够从窗外看见地球了。"
    pause 0.1 hard
    scene set only liuli_cg space2
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    play voice "voice/琉璃/041419820.ogg"
    liuli "那颗美丽的......蓝色星球。"
    play voice "voice/琉璃/041419830.ogg"
    liuli "据说火星上的蓝色夕阳也很美丽。"
    play voice "voice/琉璃/041419840.ogg"
    liuli "但是果然地球才是最美的。"
    play voice "voice/琉璃/041419850.ogg"
    liuli "有你在的这颗星球，是如此的美丽。"
    play voice "voice/琉璃/041419860.ogg"
    liuli "一定可以的......"
    play voice "voice/琉璃/041419870.ogg"
    liuli "到最后我一定可以实现曾经许下的诺言。"
    pause 0.1 hard
    scene set only liuli_cg space4
    with dissolve
    play voice "voice/琉璃/041419880.ogg"
    liuli "活着回到你的身边。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    scene set only space mars
    with slowdissolve
    pause 2.0 hard
    "引擎的故障，程序的错误，飞船的损坏。"
    "至今为止在演习中遇到的各种各样的困难都被我们克服了。"
    "所以这一次也一定......"
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    scene set only space ship1
    with dissolve
    pause 1.0 hard
    "接下来要面临的考验是突破大气层。"
    "只要完成这个，琉璃就能顺利飞向火星了。"
    pause 1.0 hard
    scene set only liuli_cg space2
    with slowdissolve
    pause 1.0 hard
    me01 "琉璃，之后的联络工作就交给圣护院小姐了。"
    me01 "需要我再给你复习一下逆喷射减速吗？"
    play voice "voice/琉璃/041419910.ogg"
    liuli "没问题的，我已经做过无数次的练习了。"
    pause 0.1 hard
    scene set only liuli_cg space3
    with dissolve
    play voice "voice/琉璃/041419920.ogg"
    liuli "比起这个，如果这次是最后的联络的话，就请让我说点别的吧。"
    me01 "别的是指？"
    pause 0.1 hard
    scene set only liuli_cg space2
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041419930.ogg"
    liuli "前辈，我喜欢你~"
    play voice "voice/琉璃/041419950.ogg"
    liuli "前辈是我最棒的搭档。"
    play voice "voice/琉璃/041419970.ogg"
    liuli "有你在的话，我就没有什么好怕的，总感觉什么都能做到了。"
    pause 0.1 hard
    scene set only liuli_cg space4
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041419980.ogg"
    liuli "不管是什么样的障碍都可以跨越。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian3
    with dissolve
    pause 1.0 hard
    "随着通话的结束，我的任务也完成了。"
    "离开了控制室，我朝着瞭望台跑去。"
    "在那里可以清晰地看见飞船划过大气层的景象。"
    "这也是我能用肉眼看着琉璃的，最后的瞬间。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    play ambience1 space_ship fadein 3.0
    scene set only sky day xuejian4
    with dissolve
    pause 1.0 hard
    "飞跃大气层的火箭在天空中划出一条赤红色的轨迹。"
    "就如同流星般闪亮而耀眼。"
    stop music fadeout 5.0
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    play music second_129 fadein 3.0 if_changed
    scene set only space star_sky
    with slowdissolve
    pause 1.0 hard
    "站在瞭望台上的我。"
    "就仿佛置身在了星星的海洋中一般。"
    "头顶就是广阔无垠的宇宙。"
    pause 1.0 hard
    scene set only myself_cg space one
    with slowdissolve
    pause 1.0 hard
    me01 "快回来吧，琉璃。"
    me01 "直到那一天到来为止，我都会像这样出现在这里等着你的。"
    "尽管这里没有通讯设备，但是我依然可以使用{rb}思维透视{/rb}{rt}telepathy{/rt}联系琉璃。"
    "这是我在研究中心的训练中觉醒的新{rb}灵纹{/rb}{rt}rune{/rt}。"
    python:
        local_config.player.skills += [yj_breakout]
    me01 "......果然没办法吗？"
    "一点回应也没有。"
    "对于以超音速飞行的飞船来说，与大气层摩擦产生的温度成为了隔绝念波的障碍。"
    "以我这不成熟的{rb}思维透视{/rb}{rt}telepathy{/rt}是很难突破障碍的。"
    pause 1.0 hard
    play sound rune3
    scene set only space ship2
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041419990.ogg"
    liuli "......前辈？"
    play voice "voice/琉璃/041420000.ogg"
    liuli "听得见吗......前辈？"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "此刻脑海里传来琉璃的呼唤。"
    "在这个距离、这样的条件下依旧能够使用{rb}思维透视{/rb}{rt}telepathy{/rt}，不愧是琉璃。"
    pause 1.0 hard
    scene set only liuli_cg space2
    with dissolve
    pause 1.0 hard
    me01 "琉璃？"
    play voice "voice/琉璃/041420010.ogg"
    liuli "是的......太好了，传达到了~"
    play voice "voice/琉璃/041420020.ogg"
    liuli "刚刚，感受到了前辈的念波......所以我想说不定是前辈也在尝试联络我。"
    pause 0.1 hard
    scene set only liuli_cg space3
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041420040.ogg"
    liuli "接下来就要突破大气层了。"
    pause 0.1 hard
    scene set only liuli_cg space2
    with dissolve
    play voice "voice/琉璃/041420060.ogg"
    liuli "虽然不确定能否传达到......但还是试着这么做了。"
    play voice "voice/琉璃/041420070.ogg"
    liuli "这应该就叫做“奇迹”吧。"
    me01 "这不是奇迹，是因为我和琉璃的羁绊已经跨越这遥远的距离了。"
    play voice "voice/琉璃/041420080.ogg"
    liuli "前辈还有什么事想要对我说的吗？"
    me01 "在等你回来的时候，我也会在这个瞭望台等着你的。"
    me01 "绝对会比任何人都要早，在这里等着你的！"
    pause 0.1 hard
    scene set only liuli_cg space4
    with dissolve
    play voice "voice/琉璃/041420090.ogg"
    liuli "那样还真是令人期待啊~"
    pause 0.1 hard
    scene set only liuli_cg space2
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041420110.ogg"
    liuli "我这里一切正常，之后只要再稍微忍耐一下就可以执行逆喷射了。"
    pause 0.1 hard
    scene set only liuli_cg space3
    with dissolve
    play voice "voice/琉璃/041420130.ogg"
    liuli "所以已经......没有什么需要担心的了。"
    pause 0.1 hard
    scene set only liuli_cg space2
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041420140.ogg"
    liuli "前辈？"
    me01 "抱歉，我这里收到了圣护院小姐的联络。"
    play voice "voice/琉璃/041420150.ogg"
    liuli "我知道了，那么前辈我们就此别过吧。"
    pause 0.1 hard
    scene set only liuli_cg space4
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    play voice "voice/琉璃/041420160.ogg"
    liuli "下一次我们，就在地面上见~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only space star_sky
    with slowdissolve
    stop music fadeout 5.0
    pause 1.0 hard
    "随着琉璃最后的话语传入我的耳中，念波中断了。"
    "飞船的光芒也消失在了空中。"
    pause 1.0 hard
    play sound warning
    show wflash_red onlayer texture
    pause 4.0 hard
    "指挥室突然传来了刺耳的警报声。"
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 2.0 hard

label day222.rocket_event02:
    play music second_138 fadein 3.0 if_changed
    play voice "voice/圣护院/151407130.ogg"
    shy "......飞船的引擎快撑不住了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only rocket_center day inside klns
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151407140.ogg"
    shy "能走到这一步，都是因为花山院用{rb}灵纹{/rb}{rt}rune{/rt}勉强支撑的缘故，但现在的状况动力已经无法继续维持下去了。"
    play voice "voice/圣护院/151407150.ogg"
    shy "这可能意味着花山院她的{rb}灵纹{/rb}{rt}rune{/rt}也已经中断了。"
    play voice "voice/圣护院/151407160.ogg"
    shy "不对......恐怕是已经到了想使也使不出来的地步了吧。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151407170.ogg"
    shy "没有来自花山院的求救信号......说不定连意识都丧失了。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151407180.ogg"
    shy "恐怕是因为长时间过度使用{rb}灵纹{/rb}{rt}rune{/rt}。"
    play voice "voice/圣护院/151407190.ogg"
    shy "比起之后漫长的宇宙旅行，现在的花山院已经达到极限了！"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    "这是怎么回事？"
    "明明刚刚还在用念波联系我的琉璃。"
    "此刻却已经到了近乎丧失意识的地步了？"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only rocket_center day inside klns
    show shy_yjf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/圣护院/151407200.ogg"
    shy "飞船角度显示器的报告数值存在异常，已经无法维持控制了。现在飞船完全就是被地球的重力支配着。"
    play voice "voice/圣护院/151407210.ogg"
    shy "从轨道上大幅偏离，虽然现在全体工作人员正在努力尝试重新调整折返路线。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151407220.ogg"
    shy "但是在无法得知飞船具体位置的情况下，无论如何都是没有办法。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151407230.ogg"
    shy "已经......没有时间了。"
    play voice "voice/圣护院/151407240.ogg"
    shy "以现在的状态强行突破大气层的话。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151407280.ogg"
    shy "再这样下去的话花山院她......"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "不知从什么时候开始，我就已经无法听清圣护院小姐的话了。"
    "脑海里一片空白。"
    "在最后为了人类的未来、为了自己热爱的工作。"
    "琉璃即使牺牲生命也选择奋不顾身。"
    "但即便是能够顺利地回来，即便是这项研究最终能够拯救万千的{rb}灵继者{/rb}{rt}elfin{/rt}。"
    "但是此刻又该由谁来拯救为这一切拼尽全力的琉璃呢？"
    "如果守护的前提是失去，那守护本身又有什么意义呢......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only myself_cg space two
    with slowdissolve
    pause 1.0 hard
    me01 "经历了那么多苦难好不容易走到了这一步。"
    me01 "最后却是这样的结局。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play voice "voice/琉璃/041420170.ogg"
    liuli "前、辈......"
    play voice "voice/琉璃/041420180.ogg"
    liuli "我的声音......"
    play voice "voice/琉璃/041420190.ogg"
    liuli "还听得到吗？"
    pause 1.0 hard
    play music second_134 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg space22
    with dissolve
    pause 1.0 hard
    me01 "琉璃！"
    play voice "voice/琉璃/041420200.ogg"
    liuli "......前辈。"
    play voice "voice/琉璃/041420210.ogg"
    liuli "太好了。我的声音传达到了......"
    play voice "voice/琉璃/041420220.ogg"
    liuli "意识已经......断断续续了。"
    play voice "voice/琉璃/041420230.ogg"
    liuli "因为过度使用{rb}灵纹{/rb}{rt}rune{/rt}的缘故。"
    play voice "voice/琉璃/041420240.ogg"
    liuli "明明健康管理也是重要的环节，但是我却搞砸了......"
    pause 0.1 hard
    scene set only liuli_cg space23
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041420260.ogg"
    liuli "是我对仪器做了手脚。"
    play voice "voice/琉璃/041420270.ogg"
    liuli "利用{rb}思维透视{/rb}{rt}telepathy{/rt}让它们一直显示正常的数值。"
    me01 "都是我的错，要是我能早一些察觉到异样的话。"
    me01 "我只是不希望让你这么久以来的努力白费，我只是想要说服自己相信你而已。"
    me01 "但是......"
    pause 0.1 hard
    scene set only liuli_cg space22
    with dissolve
    play voice "voice/琉璃/041420290.ogg"
    liuli "是的......前辈一直都是正确的。"
    play voice "voice/琉璃/041420300.ogg"
    liuli "没有任何的错。"
    play voice "voice/琉璃/041420310.ogg"
    liuli "所以我也没有为此而感到不安。"
    play voice "voice/琉璃/041420320.ogg"
    liuli "现在也是，没有一丝的不安。"
    play voice "voice/琉璃/041420330.ogg"
    liuli "所以前辈是不需要自责的。"
    me01 "为什么即使是现在，你还能够笑得出来呢？"
    me01 "为什么就不肯放弃，那份温柔呢？"
    pause 0.1 hard
    scene set only liuli_cg space23
    with dissolve
    play voice "voice/琉璃/041420340.ogg"
    liuli "为什么......吗。"
    play voice "voice/琉璃/041420350.ogg"
    liuli "那一定是不想让前辈失望吧。"
    me01 "笨蛋，我不是说了只考虑自己的事情就好了吗！"
    pause 0.1 hard
    scene set only liuli_cg space22
    with dissolve
    play voice "voice/琉璃/041420380.ogg"
    liuli "也许是这样没错。"
    play voice "voice/琉璃/041420390.ogg"
    liuli "但这就是我的生活方式。"
    me01 "等你回来我再好好地骂你一顿。"
    me01 "这次我不会再手下留情了。"
    me01 "一定要让你彻底改掉这样的毛病。"
    me01 "人类的未来什么的，星天宫什么的都无所谓。"
    me01 "我要让你从今往后只为了自己而活！"
    play voice "voice/琉璃/041420400.ogg"
    liuli "好的。"
    me01 "我们......说好了，绝对、绝对要遵守承诺。"
    play voice "voice/琉璃/041420410.ogg"
    liuli "好的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only space ship3
    with dissolve
    pause 1.0 hard
    "飞船失去动力的同时也开始回落。"
    "在快要脱离地心引力的那一刻坠落了下来。"
    "缓缓略过大气层，摩擦产生的火花点亮了星空。"
    "所有的仪器都失去了功效，这样下去根本没有办法知道飞船的具体位置。"
    "最糟糕的是，现在的飞船能否顺利穿越大气层都还是个未知数。"
    pause 1.0 hard
    scene set only myself_cg space two
    with dissolve
    pause 1.0 hard
    "我仰头凝视着头顶的星空。"
    "耳边传来的是早已乱成一团的控制室发来的一条又一条的警报。"
    "然而内容是什么我早已无心去听了。"
    "琉璃已经用她仅存的力气告诉了我所发生的一切。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "冷静点......"
    "一定还有什么办法。"
    pause 1.0 hard
    scene set only liuli_cg space22
    with dissolve
    me01 "琉璃，紧急逃生舱启动了吗？"
    play voice "voice/琉璃/041420460.ogg"
    liuli "抱歉......已经错过了最佳的启动时机。"
    play voice "voice/琉璃/041420470.ogg"
    liuli "周围在剧烈地震动......好像已经开始发生爆炸了。"
    me01 "阀门呢，阀门还能操作吗？"
    play voice "voice/琉璃/041420480.ogg"
    liuli "无法打开。"
    me01 "降落伞呢？"
    play voice "voice/琉璃/041420490.ogg"
    liuli "也没有办法分离。"
    me01 "还有什么可以使用的仪器吗？"
    play voice "voice/琉璃/041420500.ogg"
    liuli "因为刚刚爆炸的关系，已经全都失灵了。"
    me01 "那......{rb}灵纹{/rb}{rt}rune{/rt}呢？"
    play voice "voice/琉璃/041420510.ogg"
    liuli "现在的这个{rb}思维透视{/rb}{rt}telepathy{/rt}已经是我最后的极限了。"
    "已经......没有办法了吗？"
    pause 0.1 hard
    scene set only liuli_cg space23
    with dissolve
    play voice "voice/琉璃/041420520.ogg"
    liuli "飞船尾部的爆炸从刚才开始就一直在持续着。"
    play voice "voice/琉璃/041420530.ogg"
    liuli "舱内的压力也不断地变大......现在就连维持意识也已经非常辛苦了。"
    pause 0.1 hard
    scene set only liuli_cg space24
    with dissolve
    play voice "voice/琉璃/041420540.ogg"
    liuli "但是呢......外面的火焰，就像是烟花一样......非常地美丽。"
    play voice "voice/琉璃/041420550.ogg"
    liuli "啊哈哈~"
    pause 0.1 hard
    scene set only liuli_cg space22
    with dissolve
    play voice "voice/琉璃/041420560.ogg"
    liuli "前辈......"
    play voice "voice/琉璃/041420570.ogg"
    liuli "我的声音......还能传达吗？"
    me01 "啊啊，我听得很清楚。"
    play voice "voice/琉璃/041420580.ogg"
    liuli "太好了~"
    me01 "琉璃，尝试把剩下的灵力全部集中在{rb}念动立场{/rb}{rt}psychokinesis{/rt}上。"
    me01 "这样说不定可以保护自己不受压力的影响。"
    play voice "voice/琉璃/041420590.ogg"
    liuli "前、辈......"
    play voice "voice/琉璃/041420600.ogg"
    liuli "对不起，你的声音已经......无法听清了。"
    play voice "voice/琉璃/041420610.ogg"
    liuli "快要被爆炸声所掩盖了。"
    play voice "voice/琉璃/041420620.ogg"
    liuli "意识也......已经开始断断续续的了。"
    play voice "voice/琉璃/041420630.ogg"
    liuli "非常、感谢......"
    play voice "voice/琉璃/041420640.ogg"
    liuli "托前辈的福，我才能努力到这一步。"
    play voice "voice/琉璃/041420650.ogg"
    liuli "依赖某人到这个地步，我想在我的生命中还是第一次。"
    play voice "voice/琉璃/041420660.ogg"
    liuli "前辈的教诲，无论何时都是正确的。"
    play voice "voice/琉璃/041420670.ogg"
    liuli "就算发生意外也能冷静地应对。"
    play voice "voice/琉璃/041420680.ogg"
    liuli "就算在我暴走的时候，也能立刻让我平息下来。"
    play voice "voice/琉璃/041420690.ogg"
    liuli "带给我希望......"
    play voice "voice/琉璃/041420700.ogg"
    liuli "前辈......你一直都说了。"
    play voice "voice/琉璃/041420710.ogg"
    liuli "“其他的怎么样都好，交给我就行了，所以放心好了”之类的。"
    play voice "voice/琉璃/041420720.ogg"
    liuli "让我只考虑自己的安全。"
    play voice "voice/琉璃/041420730.ogg"
    liuli "但是......现在这种情况也是没有办法的吧。"
    play voice "voice/琉璃/041420750.ogg"
    liuli "这个世界的......未来。"
    play voice "voice/琉璃/041420760.ogg"
    liuli "即使我不在了，还是会有人将它传递下去。"
    play voice "voice/琉璃/041420770.ogg"
    liuli "为了人类未来的载人航天计划。"
    play voice "voice/琉璃/041420780.ogg"
    liuli "为了{rb}灵继者{/rb}{rt}elfin{/rt}的未来而开展的火星探测计划。"
    play voice "voice/琉璃/041420790.ogg"
    liuli "我都做出贡献了吗？"
    play voice "voice/琉璃/041420800.ogg"
    liuli "有帮到了大家了吗？"
    play voice "voice/琉璃/041420810.ogg"
    liuli "一直以来只会添麻烦的我，也做到了吗？"
    play voice "voice/琉璃/041420820.ogg"
    liuli "你会为我感到骄傲吗？"
    play voice "voice/琉璃/041420830.ogg"
    liuli "会因此表扬我吗？"
    play voice "voice/琉璃/041420840.ogg"
    liuli "呐......前辈。"
    play voice "voice/琉璃/041420850.ogg"
    liuli "前辈......"
    pause 0.1 hard
    scene set only liuli_cg space25
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041420860.ogg"
    liuli "不要！"
    play voice "voice/琉璃/041420870.ogg"
    liuli "都是骗人的！"
    play voice "voice/琉璃/041420880.ogg"
    liuli "就算不表扬我也好！"
    play voice "voice/琉璃/041420890.ogg"
    liuli "好想见你，我真的......好想见你！"
    play voice "voice/琉璃/041420900.ogg"
    liuli "只要这样就好！"
    play voice "voice/琉璃/041420910.ogg"
    liuli "明明只要这样就好了！"
    play voice "voice/琉璃/041420920.ogg"
    liuli "在这孤独的宇宙中，只有前辈的声音是我的唯一依靠。"
    play voice "voice/琉璃/041420930.ogg"
    liuli "因为有你的鼓励，我才没有放弃希望。"
    play voice "voice/琉璃/041420940.ogg"
    liuli "人类的未来什么的怎么样都无所谓！"
    play voice "voice/琉璃/041420950.ogg"
    liuli "{rb}灵继者{/rb}{rt}elfin{/rt}的未来什么的我才不在乎！"
    play voice "voice/琉璃/041420960.ogg"
    liuli "我心里想的就只有前辈而已！"
    play voice "voice/琉璃/041420970.ogg"
    liuli "就和前辈说的一样。"
    play voice "voice/琉璃/041420980.ogg"
    liuli "我只要考虑自己的事情就好。"
    play voice "voice/琉璃/041420990.ogg"
    liuli "只要考虑自己的幸福就好了！"
    play voice "voice/琉璃/041421000.ogg"
    liuli "好想见前辈......好想见你啊！"
    play voice "voice/琉璃/041421010.ogg"
    liuli "我已经受够离别了！"
    play voice "voice/琉璃/041421020.ogg"
    liuli "才不想去什么宇宙！"
    play voice "voice/琉璃/041421030.ogg"
    liuli "其实我哪里都不想去的！"
    play voice "voice/琉璃/041421040.ogg"
    liuli "只想一直待在你的身边。"
    pause 0.1 hard
    scene set only liuli_cg space26
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041421060.ogg"
    liuli "我想要继续，和前辈一起活下去啊！"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    "天空中划过了一道流星——"
    "已经分辨不清那是真的流星还是飞船遗落的碎片了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only space star_sky2
    with slowdissolve
    pause 1.0 hard
    "琉璃乘坐的宇宙飞船，正在大气层中燃烧着。"
    "那燃烧生命的火光将周围的一切照耀得灿灿生辉。"
    "不知不觉，那道光芒已经变得四分五裂了。"
    "残留的光迹，就像是燃烧殆尽的烟花。"
    "盛开在这冬日的夜空中。"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    "流星划过的瞬间。"
    "念波另一头的声音也消失了。"
    "也许是随着飞船一起化为宇宙中的星辰了。"
    "即使一次又一次地面对失去亲人、失去朋友的痛苦。"
    "到最后我还是无能为力。"
    "我还是......拯救不了琉璃。"
    pause 1.0 hard
    scene set only myself_cg space two
    with dissolve
    pause 1.0 hard
    "我不管世人会怎么看。"
    "也从没考虑过对人类能够有什么贡献。"
    "就连创造让{rb}灵继者{/rb}{rt}elfin{/rt}能够被社会接受那样伟大的事情，我也从没放在眼里。"
    "只要琉璃能够平安地回来。"
    "只要能够看到她的笑容。"
    "明明只要这样......就足够了。"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only rocket_center day inside klns
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151407200.ogg"
    shy "从飞船最后传回来的坐标来看，应该是失去了动力正在被地球的重力操控着。"
    play voice "voice/圣护院/151407210.ogg"
    shy "从轨道的偏离测算来看，即便是重新计算落点也很难完成。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151407220.ogg"
    shy "在无法得知飞船具体位置的情况下，无论什么样的计算都要花上一番功夫。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151407230.ogg"
    shy "但是已经没有时间了。"
    play voice "voice/圣护院/151407240.ogg"
    shy "以这样的状态是很难突破大气层的。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151407250.ogg"
    shy "再过不了多久就要到达临界状态了。"
    play voice "voice/圣护院/151407260.ogg"
    shy "不依靠花山院的{rb}灵纹{/rb}{rt}rune{/rt}就什么也做不到了。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151407280.ogg"
    shy "再这样下去的话，飞船和花山院都会......"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151407350.ogg"
    shy "抱歉。"
    play voice "voice/圣护院/151407360.ogg"
    shy "我们所有的工作人员都已经束手无策了。"
    play voice "voice/圣护院/151407370.ogg"
    shy "现在只能依靠你了......"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_c1
    play voice "voice/圣护院/151407380.ogg"
    shy "拜托了......"
    play voice "voice/圣护院/151407390.ogg"
    shy "样本什么的以后再说。"
    play voice "voice/圣护院/151407400.ogg"
    shy "我只传达最优先事项。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    nvl clear
    play voice "voice/圣护院/151407410.ogg"
    pcenter "  请救救花山院吧——"
    pause 2.0 hard

label day222.rocket_event03:
    $ flcam.move(0, 0, 0)
    scene set only myself_cg space three
    with dissolve
    play music second_165 fadein 3.0 if_changed
    pause 1.0 hard
    "一定会救她的！"
    "不会让她死的！"
    "我们会再重逢的。"
    "会一起活下去的。"
    "就算全世界都放弃了，就算你自己也早已不抱任何希望了。"
    "即使是这样我也依然会救你的。"
    "无论如何都会救你的。"
    "因为我有预感，虽然说不上原因但是我能够确信。"
    "{rb}灵纹{/rb}{rt}rune{/rt}就是为了这一刻才存在的——"
    pause 1.0 hard
    play sound rune2
    play ambience1 space_ship fadein 3.0
    show wflash onlayer texture
    pause 0.5 hard
    scene set only space star_sky3
    show fight_rune3 onlayer texture
    with slowdissolve
    pause 1.0 hard
    "琉璃留下的生命之光。"
    "只要向着那道光芒前进的话......"
    "在让人窒息的训练后，我的{rb}念动立场{/rb}{rt}psychokinesis{/rt}也得到了质的提升，利用它能够轻易地突破重力的限制。"
    "乘着上升气流，我的身体不断加速。"
    "从地面上升至10km的高空——我穿越了对流层。"
    "继续上升50km——来到了平流层。"
    pause 1.0 hard
    scene set only space star_sky4
    show fight_rune3 onlayer texture
    with slowdissolve
    pause 1.0 hard
    "虽然到达这种高度的时候大气密度会很低。"
    "但即便如此以这样的速度还是会与稀薄的空气摩擦产生热量。"
    "就如同气动加热的原理一般。"
    "飞船周围空气受剧烈压缩而出现的高温。"
    me01 "头发烧了算什么！"
    me01 "给我继续冲啊！"
    "我用{rb}念动立场{/rb}{rt}psychokinesis{/rt}制造出气流壁，违反{encyclopedia=rlxdr}热力学第二定律{/encyclopedia}来重组因高温而散乱的分子。"
    "通过抑制分子运动降低热量，顺便也将烦人的紫外线也一起屏蔽了。"
    "一口气让周围的温度降了下来。"
    "头痛剧烈，体内的血红蛋白在向我提出警告。"
    me01 "果然隔绝了空气也就意味着无法呼吸了吗......"
    "继续上升80km——突破中间层，好不容易到达了热层之中，我开始寻找琉璃的踪迹。"
    "但是，发信器早已停止了工作。"
    "太阳射线中的高能量子剧烈碰撞，造成的磁暴干扰了念波。"
    "{rb}思维透视{/rb}{rt}telepathy{/rt}也无法使用。"
    me01 "可恶，都给我安分点啊！"
    "我凝聚残存的灵力，开启{rb}微量化改造{/rb}{rt}terraforming{/rt}尽可能地排除周围磁场的干扰。"
    "尝试再次呼唤琉璃，但是还是没有回应。"
    "虽然可以感受到念波，但此时的她却收不到。"
    "是因为失去意识了吗？"
    "还是说......"
    me01 "拜托了......一定要给我撑住啊！"
    stop ambience1 fadeout 5.0
    "我放弃了所有仪器，开始用肉眼捕捉方位。"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only space earth
    $ flcam.move(0, 1400, 800, duration=15.0, warper='ease_quad')
    with slowdissolve
    "应该是在这附近的。"
    "然而，即使无法使用{rb}远隔透视{/rb}{rt}clarivoyance{/rt}的我，如果能够合理利用{rb}接触感应{/rb}{rt}psychometry{/rt}的话也是能够做到一样的效果。"
    "就像立花老师说的那样。"
    "利用仅存的稀薄的空气感知周围的环境。"
    "调整光的折射角度，将视野放大到极致。"
    "在讲座上被圣护院小姐强行灌输进去的知识，现在一口气全部浮现了出来。"
    "那是拯救琉璃的力量。"
    "那是大家的力量。"
    me01 "伙伴们都在等待着你回来。"
    me01 "快回应我吧！"
    "顺着念波飘散的方向，我追了上去。"
    "流星再一次划过了我视野的那一刹那。"
    "在那里，我捕捉到了光——"
    "没能穿过大气层的密封舱似乎正在溶解。"
    "是吗......"
    "琉璃她也......"
    "还没有放弃吗......"
    "有好好地用{rb}念动立场{/rb}{rt}psychokinesis{/rt}保护着驾驶舱。"
    "谢谢你......"
    "我追赶着飞船碎片的轨迹。"
    "视线里不断重复着的光与暗。"
    "生命的光芒仍在闪烁着。"
    "那是琉璃的{rb}灵纹{/rb}{rt}rune{/rt}。"
    "由{rb}冥火{/rb}{rt}pyrokinesis{/rt}包裹而成的光球，仿佛在发送着“SOS”的信号一样。"
    pause 1.0 hard
    $ set_replay_scene("label13_4")
    scene black 
    with slowerdissolve
    pause 2.0 hard
    me01 "找到你了，琉璃。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041421070.ogg"
    liuli "前、辈......"
    play voice "voice/琉璃/041421080.ogg"
    liuli "前辈的......味道。"
    play voice "voice/琉璃/041421090.ogg"
    liuli "坚实有力的手腕。"
    play voice "voice/琉璃/041421100.ogg"
    liuli "让人安心的胸膛。"
    play voice "voice/琉璃/041421110.ogg"
    liuli "全部都是......我所期望见到的。"
    play voice "voice/琉璃/041421120.ogg"
    liuli "都是我梦寐以求的东西。"
    play voice "voice/琉璃/041421130.ogg"
    liuli "这是......梦吗？"
    me01 "这不是梦。"
    me01 "这是我们一起抓住的现实。"
    me01 "欢迎回来，琉璃——"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg space31
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/041421140.ogg"
    liuli "......骗人。"
    play voice "voice/琉璃/041421150.ogg"
    liuli "前辈。"
    play voice "voice/琉璃/041421160.ogg"
    liuli "终于......能够见面了。"
    play voice "voice/琉璃/041421170.ogg"
    liuli "感觉好漫长。"
    play voice "voice/琉璃/041421180.ogg"
    liuli "我已经记不清自己曾经多少次想要放弃了。"
    play voice "voice/琉璃/041421190.ogg"
    liuli "已经数不清自己绝望了多少次。"
    pause 0.1 hard
    scene set only liuli_cg space32
    with dissolve
    play voice "voice/琉璃/041421200.ogg"
    liuli "前辈......你是在生气吗？"
    me01 "那是当然的。"
    play voice "voice/琉璃/041421210.ogg"
    liuli "对不起，我对前辈说了谎。"
    me01 "不是因为这个。"
    me01 "我是为自己的无能而生气。"
    me01 "为自己没能在你最需要的时候陪在你身边而感到气愤。"
    me01 "为这个不公平的世界而气愤。"
    play voice "voice/琉璃/041421220.ogg"
    liuli "你这是要征服世界吗？"
    me01 "如果琉璃希望的话，这么做也不错。"
    me01 "将只会利用{rb}灵继者{/rb}{rt}elfin{/rt}的世界，用我这双手彻底改变它。"
    play voice "voice/琉璃/041421230.ogg"
    liuli "不行哟，前辈。"
    play voice "voice/琉璃/041421240.ogg"
    liuli "这样做的话星天宫的大家，还有雪见市的大家都会有麻烦的。"
    me01 "那就让圣护院小姐帮忙，她应该会有办法的。"
    pause 0.1 hard
    scene set only liuli_cg space33
    $ flcam.move(1100, 1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041421270.ogg"
    liuli "不行哟......我讨厌那样的前辈。"
    me01 "是这样吗？"
    play voice "voice/琉璃/041421280.ogg"
    liuli "是的。"
    me01 "回去吧，一起回到大家的身边。"
    play voice "voice/琉璃/041421310.ogg"
    liuli "好的~"
    play voice "voice/琉璃/041421320.ogg"
    liuli "不是宿舍，而是回到我们普通的生活中去。"
    play voice "voice/琉璃/041421330.ogg"
    liuli "回到家人身边，和前辈一起好好地活下去。"
    play voice "voice/琉璃/041421340.ogg"
    liuli "我想要继续留在前辈的身边。"
    play voice "voice/琉璃/041421350.ogg"
    liuli "如果前辈又像刚才那样暴走的话，就由我来阻止你。"
    play voice "voice/琉璃/041421360.ogg"
    liuli "我会在你的耳边说“乖啊乖啊”~"
    me01 "到时候就拜托你了。"
    pause 0.1 hard
    scene set only liuli_cg space31
    with dissolve
    play voice "voice/琉璃/041421370.ogg"
    liuli "......前辈你看。"
    pause 0.1 hard
    scene set only liuli_cg space34
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041421380.ogg"
    liuli "星空......真是美丽~"
    "我们穿过大气层。"
    "正在不停地朝着地面飞去。"
    "在那里有着令人安心的灯火指引着我们方向。"
    "我想那一定是比宇宙更加令人向往的地方。"
    pause 0.1 hard
    scene set only liuli_cg space33
    $ flcam.move(1100, 1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/041421390.ogg"
    liuli "我的愿望只有一个。"
    play voice "voice/琉璃/041421400.ogg"
    liuli "只要能和你一起活下去。"
    play voice "voice/琉璃/041421410.ogg"
    liuli "回到故乡好好地生活下去。"
    play voice "voice/琉璃/041421430.ogg"
    liuli "从一开始，就只有这一个而已。"
    pause 0.1 hard
    scene set only liuli_cg space34
    $ flcam.move(2200, 1400, 800, duration=4.0, warper='ease_quad')
    with dissolve
    play voice "voice/琉璃/041421440.ogg"
    liuli "这就是我向流星许愿的——崭新的未来。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    stop music fadeout 5.0
    pause 1.0 hard
    $ end_replay()
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 1.0 hard

    $ persistent.lingyin = True
    $ persistent.szl_ling = True
    $ persistent.youjia = True
    $ persistent.lihuaxi = True
    $ persistent.liuli = True
    $ persistent.lisite = True 
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    
    jump second_menu
