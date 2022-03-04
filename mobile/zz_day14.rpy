label day14:
    bookmark
    $ save_name = _("Day 14")
    pause 4.0 hard
    scene set only backend_yinghua winter
    with dissolve
    show backend_bg04 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date13 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only hospital day outside
    with dissolve
    pause 1.0 hard
    "刚一放学我就朝着医院的方向奔去。"
    play music first_23 fadein 3.0 if_changed
    "接到了医院护士的通知。"
    "虽然不知道发生了什么，但没有多想我就出发了。"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    scene set only hospital day passwalk
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show nurse_dzf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/护士/2200100.ogg"
    nurse "你就是神野凉吧？"
    show nurse_dzf_b1 b1 b1_s1
    play voice "voice/护士/2200110.ogg"
    nurse "抱歉突然把你叫过来。"
    me01 "翔子那边的情况怎么样了？"
    show nurse_dzf_b1 b1 b1_n2
    play voice "voice/护士/2200140.ogg"
    nurse "现在除了家人以外谁都不允许来探望了。"
    me01 "病情......又恶化了吗？"
    show nurse_dzf_b1 b1 b1_n2
    play voice "voice/护士/2200160.ogg"
    nurse "是的。从昨晚开始。"
    "昨晚，果然是因为和我去观景台所以才......"
    me01 "那、那我明天再来。之后也是，我可以再等等......"
    play voice "voice/护士/2200170.ogg"
    nurse "明天也不能来探望的。"
    me01 "抱歉让您为难了。"
    play voice "voice/护士/2200190.ogg"
    nurse "要道歉的不是你而是我们。"
    show nurse_dzf_b1 b1 b1_s1
    play voice "voice/护士/2200200.ogg"
    nurse "因为我们的无能，真是对不起。"
    show nurse_dzf_b1 b1 b1_n1
    play voice "voice/护士/2200210.ogg"
    nurse "还有，一直以来谢谢你能来探望梦。"
    "第一次从护士的口中听到“梦”这个名字。"
    "我明明只对班上的同学们提到过的而已。"
    "这其中究竟发什么什么。"
    "不禁让我有种不好的预感。"
    "想要开口询问缘由，却又不自觉地犹豫着该不该说。"
    play voice "voice/护士/2200220.ogg"
    nurse "我每次去看护的时候，她都会提到你。和刚转院过来的时候相比，现在看她笑得更频繁了。"
    stop music fadeout 5.0
    $ flcam.move(500, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/护士/2200250.ogg"
    nurse "另外我想把这个交给你，所以让你来了。"
    show letter onlayer m2 at item_7to6:
        xpos 0.6
    "她将手中握着的信封递给了我。"
    "棱角粘贴得很完美，似乎是精心准备的。"
    hide letter
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show nurse_dzf_b1 b1 b1_n1
    play voice "voice/护士/2200270.ogg"
    nurse "那我先回去工作了。"
    pause 0.5 hard
    show nurse_dzf_b1 b1 b1_n1 onlayer m2 at walkout_l(0.5)
    play sound move_2
    pause 2.0 hard
    scene white 
    with slowerdissolve
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only items letter
    with in2out_v2_slow
    pause 2.0 hard
    play voice "voice/翔子/0609930.ogg"
    yume "致凉君——"
    play music first_27 fadein 3.0 if_changed
    play voice "voice/翔子/0609940.ogg"
    yume "这封信，是凉君在观景台向我告白的那天晚上写的。"
    play voice "voice/翔子/0609960.ogg"
    yume "其实直到现在，我的情绪也依旧没有平复。"
    play voice "voice/翔子/0609970.ogg"
    yume "因为太兴奋了，所以今晚或许也睡不着了。"
    play voice "voice/翔子/0609980.ogg"
    yume "所以借着这个机会就想试着写信看看，于是我就写下了这些。"
    play voice "voice/翔子/0609990.ogg"
    yume "因为病房已经熄灯了，所以我只能依靠星光来书写。果然还是有些困难的。"
    play voice "voice/翔子/0610000.ogg"
    yume "首先，祝你生日快乐。"
    play voice "voice/翔子/0610010.ogg"
    yume "因为那时没有说，所以现在一起祝贺你。"
    play voice "voice/翔子/0610020.ogg"
    yume "虽然也想过准备些礼物的，但因为我无法独自外出所以还是有点困难。"
    play voice "voice/翔子/0610030.ogg"
    yume "抱歉了。"
    play voice "voice/翔子/0610040.ogg"
    yume "所以这封信就当是礼物的替代。"
    play voice "voice/翔子/0610050.ogg"
    yume "我有话想对你说。"
    play voice "voice/翔子/0610060.ogg"
    yume "我大概马上就会陷入沉睡了。"
    play voice "voice/翔子/0610070.ogg"
    yume "虽然不知道什么时候，但一定是在不久的将来，所以我想趁现在把所有想对你说的话都写下来。"
    play voice "voice/翔子/0610080.ogg"
    yume "这封信，我打算拜托别人在我离开之后转交给你。"
    play voice "voice/翔子/0610090.ogg"
    yume "所以在你读这封信的时候，我大概已经不在了。"
    play voice "voice/翔子/0610100.ogg"
    yume "也许不会再醒过来了。"
    play voice "voice/翔子/0610110.ogg"
    yume "所以我希望你以后不要再来探望我了。"
    play voice "voice/翔子/0610130.ogg"
    yume "再一次，禁止你的探病。"
    play voice "voice/翔子/0610140.ogg"
    yume "这就是我最后的要求。"
    play voice "voice/翔子/0610150.ogg"
    yume "并不是因为我讨厌凉君才这么决定的。"
    play voice "voice/翔子/0610160.ogg"
    yume "因为如果我就这样沉睡下去的话，就真的很难再见面了。"
    play voice "voice/翔子/0610171.ogg"
    yume "因为星星的光一直在影响着我。"
    play voice "voice/翔子/0610180.ogg"
    yume "听说这种症状是和电磁波有关的，虽然轻微的话也只是引起头痛这样的程度而已。"
    play voice "voice/翔子/0610190.ogg"
    yume "但我的情况似乎更加严重。"
    play voice "voice/翔子/0610200.ogg"
    yume "我的病情是会危及生命的。"
    play voice "voice/翔子/0610210.ogg"
    yume "SAR值什么的{encyclopedia=hotspot}Hot Spot{/encyclopedia}现象什么的，即使我听了也无法理解。"
    play voice "voice/翔子/0610220.ogg"
    yume "我从出生的那一刻起，就已经患上了这种疾病。"
    play voice "voice/翔子/0610230.ogg"
    yume "虽然也有想过如果病因是星光的话，只要避开那些带有特殊电波的光芒就可以了。"
    play voice "voice/翔子/0610240.ogg"
    yume "但即使不在晚上、即使躲在建筑物里，那股力量仍然可以到达。"
    play voice "voice/翔子/0610250.ogg"
    yume "星星的光，比起任何机器产生的光要强烈许多。"
    play voice "voice/翔子/0610260.ogg"
    yume "所以我这个病，是治不好的。"
    play voice "voice/翔子/0610270.ogg"
    yume "即使医生们努力地想办法，天文学家们也在拼命地研究。"
    play voice "voice/翔子/0610280.ogg"
    yume "可是面对像我这样的患者，仍然无计可施。"
    play voice "voice/翔子/0610290.ogg"
    yume "所以凉君。"
    play voice "voice/翔子/0610300.ogg"
    yume "在你读完这封信之后，请不要再来找我了。"
    play voice "voice/翔子/0610310.ogg"
    yume "不要再来探望我了。"
    play voice "voice/翔子/0610320.ogg"
    yume "因为我累了。"
    play voice "voice/翔子/0610330.ogg"
    yume "不会再醒来了。"
    play voice "voice/翔子/0610340.ogg"
    yume "无法再陪在你身边了。"
    play voice "voice/翔子/0610350.ogg"
    yume "我的生命已经结束了。"
    play voice "voice/翔子/0610360.ogg"
    yume "对不起。"
    play voice "voice/翔子/0610370.ogg"
    yume "明明说了可以依赖我的，对不起。"
    play voice "voice/翔子/0610380.ogg"
    yume "明明说了可以对我撒娇的，对不起。"
    play voice "voice/翔子/0610390.ogg"
    yume "不能陪在你身边，对不起。"
    play voice "voice/翔子/0610400.ogg"
    yume "但是请你不要因此而讨厌星星。"
    play voice "voice/翔子/0610420.ogg"
    yume "我们约好了。"
    play voice "voice/翔子/0610430.ogg"
    yume "这是我和你许下的，最后的约定。"
    play voice "voice/翔子/0610440.ogg"
    yume "在最后我想对你说。"
    play voice "voice/翔子/0610450.ogg"
    yume "即使如此我依然最喜欢星星了。"
    play voice "voice/翔子/0610460.ogg"
    yume "和你一起仰望的，樱华镇的星空我最喜欢了——"
    pause 2.0 hard
    stop music fadeout 5.0
    scene white
    with slowerdissolve
    pause 3.0 hard
    play music first_36 fadein 3.0 if_changed
    "我发了疯似的朝病房的方向跑去。"
    "然而门口早已挂上了“谢绝会面”的牌子。"
    pause 1.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    "悲伤已经完全压倒了理性。"
    "不断磨损的精神正在剥夺着我的思考。"
    "脑海深处，有一块冰冷、黑暗的区域正在扩散。"
    "那是我将至今为止试图将所有悲伤隐藏起来的地方。"
    pause 1.0 hard
    scene set only hospital night outside
    with dissolve
    pause 1.0 hard
    "搬家的时候也是。"
    "母亲去世的时候也是。"
    "现在梦的离去也依然如此。"
    "一切都是那么突然。"
    "如同噩梦般地向我袭来。"
    "毫无预测的可能。"
    "只能被命运玩弄。"
    "被玩弄着，被痛苦、悔恨以及无尽的悲伤所吞噬。"
    "紧接着某天，再次回到那毫无期待的日常中去。"
    "安静地等待灵魂的死亡。"
    "最后连仅剩的希望也消失殆尽。"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    "真的，就这样结束了吗......"
    "从唐突造访的偶遇，再到如今的不辞而别。"
    "我真的，谁也拯救不了吗。"
    "因为害怕打破日常秩序而默许了两个翔子的存在。"
    "因为害怕被禁止探病而一直没有问出口住院的缘由。"
    "因为害怕完全失去而接受了表白的失败。"
    "我从未想过去争取些什么。"
    "为什么到现在我还是什么都没有做成呢。"
    "为什么我没能像翔子、没能像梦那样为别人而着想呢。"
    "我果然和过去一样，只会选择逃避。"
    pause 1.0 hard
    scene set only sky night yinghua2
    with dissolve
    pause 2.0 hard
    "梦最后也说了，即使如此她也依然喜欢星空。"
    "即使因为星星的关系而死去，即使因为星星的关系而饱受病痛的折磨。"
    "即使从我身边把她带走。"
    "也要让我喜欢上这样的星空吗......"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    me01 "真是残酷啊。"
    pause 1.0 hard

label day14.starview_event01:
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    with dissolve
    pause 2.0 hard
    play voice "voice/天使雷亚/0021730.ogg"
    lst "凉君......"
    pause 1.0 hard
    scene set only lisite_cg surprise
    with dissolve
    pause 2.0 hard
    play voice "voice/天使雷亚/0021740.ogg"
    lst "怎么了，凉君？"
    play voice "voice/天使雷亚/0021750.ogg"
    lst "一直呆呆地看着星空。"
    me01 "因为我在看星星啊。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0021760.ogg"
    lst "不是的。"
    play voice "voice/天使雷亚/0021770.ogg"
    lst "凉君，没有在看星星。"
    play voice "voice/天使雷亚/0021780.ogg"
    lst "在看着星星以外的，别的东西。"
    me01 "那到底是什么呢？"
    pause 0.1 hard
    scene set only lisite_cg shy
    with dissolve
    $ flcam.move(1500, -1800, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0021790.ogg"
    lst "发问的明明是我。"
    me01 "也许吧。"
    play voice "voice/天使雷亚/0021800.ogg"
    lst "......"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only starview night starview
    show ts_lst_ssz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/天使雷亚/0021810.ogg"
    lst "凉君变得没有精神了。"
    me01 "是吗。"
    show ts_lst_ssz_b2 b2 b2_s3
    play voice "voice/天使雷亚/0021820.ogg"
    lst "要怎么做，凉君才会有精神呢？"
    me01 "......"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0021830.ogg"
    lst "凉君......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg head sad
    with dissolve
    pause 2.0 hard
    play voice "voice/天使雷亚/0021870.ogg"
    lst "不、不是这样的。"
    play voice "voice/天使雷亚/0021880.ogg"
    lst "不是要，被摸头......"
    me01 "谢谢你。"
    me01 "让你担心了。"
    play voice "voice/天使雷亚/0021890.ogg"
    lst "......"
    play voice "voice/天使雷亚/0021900.ogg"
    lst "这种感觉好奇怪。"
    play voice "voice/天使雷亚/0021910.ogg"
    lst "明明我是想为凉君做点什么的。"
    me01 "我没事的。"
    me01 "我真的......没事的。"
    "在雷亚的身上我总能够看到梦的身影。"
    "回忆一次又一次地重复着。"
    "那股沉睡在我脑海深处的，冰冷黑暗的感情堆积起来。"
    "这份感情不允许我哭。"
    "但却折磨着我。"
    "不用一个人承受，两个人背负也是可以的。"
    "虽然经常被翔子教训了。"
    "天真的我以为这样就可以改变了。"
    "明明就快要相信了的。"
    "明明就快要渡过天河了。"
    "可你却不在我身边。"
    pause 2.0 hard
    stop music fadeout 5.0
    scene black
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    $ suppress_overlay = True
    jump day15
