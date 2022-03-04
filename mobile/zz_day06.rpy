label day06:
    bookmark
    $ save_name = _("Day 06")
    pause 4.0 hard
    scene set only backend_yinghua summer
    with dissolve
    show backend_bg02 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date05 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    $ suppress_overlay = False
    scene set only sky day yinghua
    with dissolve
    pause 2.0 hard
    play sound fengling
    scene set only store day coffee_room yinghua
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xsf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504350.ogg"
    lingyin "你好，神野同学。"
    play music first_05 fadein 3.0 if_changed
    me01 "你好铃音同学，就你一个人吗？"
    show lingyin_xsf_b2 b2 b2_s1
    play voice "voice/青木铃音/0504360.ogg"
    lingyin "是的。虽然邀请了姐姐，但是立刻就被拒绝了。"
    me01 "毕竟那家伙连暑假也如此地忙碌。"
    hide lingyin_xsf_b2
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    "我和铃音找了个位子坐下。"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xsf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/日向怜/0113940.ogg"
    rxl "小铃，好久不见~"
    pause 0.5 hard
    show lingyin_xsf_b2 b2 b2_ga2 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0504370.ogg"
    lingyin "也只有两天不见而已。"
    hide rxl_xsf_b1
    show rxl_xsf_b2 b2 b2_h2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0113950.ogg"
    rxl "要点些什么吗？"
    show lingyin_xsf_b2 b2 b2_n1
    play voice "voice/青木铃音/0504380.ogg"
    lingyin "那就平时的菜单就可以了。"
    show rxl_xsf_b2 b2 b2_h1
    play voice "voice/日向怜/0113960.ogg"
    rxl "洛天山的十字架套餐对吧，我知道了~"
    pause 0.5 hard
    play sound move_2
    show rxl_xsf_b2 b2 b2_h1 onlayer m2 at walkout_r(0.7)
    pause 2.0 hard
    hide rxl_xsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xsf_b2 b2 b2_h1
    play voice "voice/青木铃音/0504390.ogg"
    lingyin "事实上，我有在偷偷收集十字架哟~"
    me01 "是指食物的附赠品吧，喜欢收集这些铃音同学不愧是女孩子呢。"
    show lingyin_xsf_b2 b2 b2_ga1
    play voice "voice/青木铃音/0504400.ogg"
    lingyin "我可以理解为这是对女性的蔑视吗？"
    me01 "抱歉，我没有那个意思。"
    show lingyin_xsf_b2 b2 b2_h1
    play voice "voice/青木铃音/0504410.ogg"
    lingyin "我知道的，神野同学才不是那样子的人。"
    "与喜欢逞强的姐姐翔子不同，铃音给人的感觉更像是成熟稳重的大家闺秀。"
    hide lingyin_xsf_b2
    show lingyin_xsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0504420.ogg"
    lingyin "不坐下来吗？今天我找神野同学是有事商量的。"
    me01 "那就恭敬不如从命了。"
    hide lingyin_xsf_b1
    show lingyin_xsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0504430.ogg"
    lingyin "神野同学，这周末有什么预定吗？"
    me01 "暂时没有什么特别的。打工也只有在工作日的时候进行。"
    show lingyin_xsf_b2 b2 b2_h1
    play voice "voice/青木铃音/0504440.ogg"
    lingyin "那么一起去海水浴怎么样？"
    show lingyin_xsf_b2 b2 b2_n1
    play voice "voice/青木铃音/0504450.ogg"
    lingyin "母亲大人她呢，说是假期的时候也想见见诗乃阿姨的儿子。"
    me01 "确实有一段时间没有去打扰了。"
    me01 "话说回来家母莫非也是很久以前就认识我母亲了吗？"
    hide lingyin_xsf_b2
    show lingyin_xsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0504460.ogg"
    lingyin "是的。所以听说你回来的消息之后，也是第一时间提议可以在暑假的时候一起到樱华镇的海滩上放松一下。"
    "虽然小时候因为翔子的关系没少受到青木家的照顾。"
    "可没想到这座小镇上的大家都有着那么多的故事。"
    me01 "我明白了，我会考虑一下的。"
    hide lingyin_xsf_b1
    show lingyin_xsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0504470.ogg"
    lingyin "星期六和星期天，如果能确认是哪一天的话就帮大忙了。"
    me01 "具体时间就由铃音同学这边决定吧。"
    show lingyin_xsf_b2 b2 b2_h1
    play voice "voice/青木铃音/0504480.ogg"
    lingyin "太感谢了~"
    me01 "对了，铃音同学的父母也是一直以来都住在这座小镇上吗？"
    show lingyin_xsf_b2 b2 b2_n1
    play voice "voice/青木铃音/0504490.ogg"
    lingyin "是的。不过这次父亲因为医院那边的工作所以没有办法参加。"
    me01 "令尊是医生吗？"
    hide lingyin_xsf_b2
    show lingyin_xsf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0504500.ogg"
    lingyin "是的。很稀奇是吧，明明母亲之前是个神官呢。"
    me01 "我到是觉得这样的组合也不错呢。"
    show lingyin_xsf_b1 b1 b1_h1
    play voice "voice/青木铃音/0504510.ogg"
    lingyin "真是男孩子的想法呢~"
    me01 "这可以理解成是对男性的蔑视吗？"
    show lingyin_xsf_b1 b1 b1_s1
    play voice "voice/青木铃音/0504520.ogg"
    lingyin "原来在神野同学眼中我竟然是这样的，真是受打击。"
    me01 "真是输给你了。"
    me01 "对了，翔子那边需要通知她吗？"
    hide lingyin_xsf_b1
    show lingyin_xsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0504530.ogg"
    lingyin "要的，就拜托你了~"
    "当然对我而言还有一个需要邀请的对象。"
    pause 0.5 hard
    show rxl_xsf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.7)
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0113970.ogg"
    rxl "让您久等了，这是洛天山的十字架~"
    show lingyin_xsf_b2 b2 b2_n1
    play voice "voice/青木铃音/0504540.ogg"
    lingyin "日向同学，我有话想对你说，现在方便吗？"
    stop music fadeout 5.0
    hide rxl_xsf_b1
    show rxl_xsf_b2 b2 b2_h2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0113980.ogg"
    rxl "嗯，我正好也休息一下。"
    pause 0.5 hard
    show rxl_xsf_b2 b2 b2_h2 at flu_down(0.25, 20):
        xpos 0.7
    "说着日向怜就坐到了铃音的旁边。"
    pause 0.5 hard
    play voice "voice/青木铃音/0504550.ogg"
    lingyin "日向同学，这周末有什么预定吗？"
    show rxl_xsf_b2 b2 b2_s1
    play voice "voice/日向怜/0113990.ogg"
    rxl "我的话要在店里帮忙吧，从白天到晚上。"
    show lingyin_xsf_b2 b2 b2_h1
    play voice "voice/青木铃音/0504560.ogg"
    lingyin "那么，我就传达一下母亲大人的指示吧。"
    "铃音同学清了清喉咙。"
    show lingyin_xsf_b2 b2 b2_n2
    play voice "voice/青木铃音/0504580.ogg"
    lingyin "星期六或星期天，随便空一天出来。她是这样说的。"
    show rxl_xsf_b2 b2 b2_sp1
    play voice "voice/日向怜/0114010.ogg"
    rxl "周末的话......"
    hide rxl_xsf_b2
    show rxl_xsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0114020.ogg"
    rxl "是有什么事吗？"
    play music first_06 fadein 3.0 if_changed
    show lingyin_xsf_b2 b2 b2_h1
    play voice "voice/青木铃音/0504590.ogg"
    lingyin "是的。想邀请你们去海水浴，我同样也邀请了神野同学。"
    show rxl_xsf_b1 b1 b1_h1
    play voice "voice/日向怜/0114030.ogg"
    rxl "哇，真的吗，我去我去！"
    "刚刚还说要从早忙到晚的。"
    show lingyin_xsf_b2 b2 b2_n1
    play voice "voice/青木铃音/0504600.ogg"
    lingyin "不仅是日向同学。母亲她也邀请了你的父亲。"
    show rxl_xsf_b1 b1 b1_ga1
    play voice "voice/日向怜/0114040.ogg"
    rxl "为什么连老爸他也。"
    show lingyin_xsf_b2 b2 b2_s1
    play voice "voice/青木铃音/0504610.ogg"
    lingyin "因为是母上大人的决定。"
    show lingyin_xsf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0504620.ogg"
    lingyin "关于这其中的理由，先不说神野同学，估计就连日向同学你也不知道的样子。"
    hide rxl_xsf_b1
    show rxl_xsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0114060.ogg"
    rxl "什么理由？"
    hide lingyin_xsf_b2
    show lingyin_xsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0504630.ogg"
    lingyin "其实呢，日向同学的父亲——宗一郎先生，和母上大人还有诗乃阿姨都是曾经天文部的部友呢~"
    show lingyin_xsf_b1 b1 b1_n1
    play voice "voice/青木铃音/0504640.ogg"
    lingyin "所以这次的邀请，同时也是天文部的OB会。我们这些小孩子只是附属品一样的存在。"
    me01 "这个......怎么说呢。"
    show rxl_xsf_b2 b2 b2_ga1
    play voice "voice/日向怜/0114070.ogg"
    rxl "世界还真小呢。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black 
    with dissolve
    pause 2.0 hard

label day06.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only shenshe day yinghua
    with slowdissolve
    pause 2.0 hard
    "告别了铃音一行人，我依照与翔子的约定来到了神社帮忙。"
    play music first_15 fadein 3.0 if_changed
    scene set only xz_cg normal
    with dissolve
    play voice "voice/翔子/0205810.ogg"
    xz "真慢啊，笨蛋凉。"
    me01 "之前明明用的还是巫女的礼节，现在怎么直接加上绰号了啊。"
    play voice "voice/翔子/0205820.ogg"
    xz "只怪你迟到了。"
    me01 "这不是准时到了吗？"
    play voice "voice/翔子/0205830.ogg"
    xz "迟到了三十秒。"
    me01 "真是严格啊你。"
    play voice "voice/翔子/0205840.ogg"
    xz "而且不是说了凡事都要提前十分钟行动吗，我都已经开始洒水了。"
    me01 "神社里似乎也来了参拜客，开始热闹起来了啊。"
    play voice "voice/翔子/0205850.ogg"
    xz "是啊，上午和社区委员会、自愿者们都做了祭典筹建工作的交接。"
    me01 "现在呢？"
    play voice "voice/翔子/0205860.ogg"
    xz "这时间是一天中最热的时候所以暂时休息，大概等到傍晚的时候就又会开始了吧。"
    me01 "然而我们却是在这最热的时候工作吗。"
    pause 0.1 hard
    scene set only xz_cg happy
    with dissolve
    play voice "voice/翔子/0205870.ogg"
    xz "毕竟洒水的目的就是为了能让参拜的人能觉得凉快些。"
    me01 "说的也是，那我先去打桶水来吧。"
    play voice "voice/翔子/0205880.ogg"
    xz "拜托你了~"
    "我一边盛着水，一边看向正在洒水的翔子。"
    "水花溅起的涟漪打在石板地上闪闪发光。"
    "身着巫女装的翔子此刻也宛如雕像美人一般夺目。"
    pause 0.1 hard
    scene set only xz_cg normal
    with dissolve
    $ flcam.move(3500, -1800, 600, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0205890.ogg"
    xz "......怎么了，一直盯着我看。"
    me01 "可惜，如果性格再收敛一些的话就完美了。"
    pause 0.1 hard
    scene set only xz_cg angry
    with dissolve
    play voice "voice/翔子/0205900.ogg"
    xz "你在说什么啊？"
    me01 "我是说翔子你还真是个大美人啊。"
    pause 0.1 hard
    scene set only xz_cg shame
    with dissolve
    play voice "voice/翔子/0205910.ogg"
    xz "......"
    me01 "其实也挺受欢迎的吧，在学校？"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    play voice "voice/翔子/0205920.ogg"
    xz "怎、怎么了啊，突然间。"
    me01 "在我遇见的人里面，翔子你就算被认为是第一美女也不为过了。"
    play voice "voice/翔子/0205930.ogg"
    xz "......你是认真的吗？"
    me01 "虽然说这话多少有些害羞，但是这时候我还是觉得应该把真实的想法说出来比较好。"
    play voice "voice/翔子/0205940.ogg"
    xz "......"
    me01 "有被表白过吗？"
    pause 0.1 hard
    scene set only xz_cg angry
    with dissolve
    play voice "voice/翔子/0205950.ogg"
    xz "和、和你没关系吧？"
    me01 "男朋友......应该没有吧。不然也不会让我来帮忙了。"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    play voice "voice/翔子/0205960.ogg"
    xz "真、真烦人啊。"
    me01 "为什么不交个男朋友？"
    play voice "voice/翔子/0205970.ogg"
    xz "都、都说了和你没关系吧。"
    me01 "因为是巫女的关系？"
    play voice "voice/翔子/0205980.ogg"
    xz "那是什么时代的巫女啊。虽然在原则上是要未婚的。"
    play voice "voice/翔子/0205990.ogg"
    xz "如果是那些有神职资格的巫女，对于恋爱问题或许还会犹豫一下，但我们终归只是业余的神社而已，没有那么多规矩。"
    me01 "那究竟是为什么？"
    pause 0.1 hard
    scene set only xz_cg angry
    with dissolve
    $ flcam.move(4100, -2800, 900, duration=1.5, warper='ease_quad')
    play voice "voice/翔子/0206000.ogg"
    xz "......"
    play sound sashui
    with vpunch
    pause 1.0 hard
    me01 "别一言不发就朝我泼水啊喂！"
    play voice "voice/翔子/0206010.ogg"
    xz "再追问的话小心我踹你哦。这是第四个要求，违反的话借用屋顶的事情就取消。"
    "之前明明约好了的三个要求，怎么无端又追加一个？！"
    me01 "对我你还真是毫不留情啊。"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    $ flcam.move(3500, -1800, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0206020.ogg"
    xz "你以为是谁的错啊。"
    play voice "voice/翔子/0206030.ogg"
    xz "再说，神野同学你似乎搞错一件事了吧。"
    me01 "搞错什么了？"
    pause 0.1 hard
    scene set only xz_cg normal
    with dissolve
    play voice "voice/翔子/0206040.ogg"
    xz "我可不是什么第一美人，这不还有我的双胞胎妹妹铃音吗。"
    me01 "意思是长得一模一样所以最多算是并列第一？"
    me01 "不过铃音同学不如说是可爱更确切一点吧？"
    play voice "voice/翔子/0206050.ogg"
    xz "你问我我也不知道啊。"
    me01 "毕竟和铃音同学不同，翔子你的性格怎么想也算不上可爱吧。"
    pause 0.1 hard
    scene set only xz_cg angry
    with dissolve
    $ flcam.move(4100, -2800, 900, duration=1.5,  warper='ease_quad')
    pause 1.0 hard
    play sound punch
    with vpunch
    "{size=72}咚嗙！！{/size}"
    me01 "结果还是被踹了！"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    play voice "voice/翔子/0206060.ogg"
    xz "......哼！"
    pause 0.1 hard
    scene set only xz_cg normal
    with dissolve
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0206070.ogg"
    xz "别老说些废话了，给我好好干活。"
    me01 "话说你把唯一的勺子占用了，我这边可就没事情做了。"
    play voice "voice/翔子/0206100.ogg"
    xz "为什么是让我来洒水啊。"
    me01 "是你自己选的吧。"
    play voice "voice/翔子/0206110.ogg"
    xz "你就没有主动替我分担的慈爱精神吗？"
    me01 "那换我来吧？"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    play voice "voice/翔子/0206120.ogg"
    xz "都快结束了，算了吧。"
    me01 "到底是想让我怎样啊......"
    pause 0.1 hard
    scene set only xz_cg normal
    with dissolve
    play voice "voice/翔子/0206130.ogg"
    xz "至少帮我扇扇风吧。"
    me01 "我又没有扇子。"
    play voice "voice/翔子/0206140.ogg"
    xz "我说，好热啊~"
    me01 "对苍天抱怨去吧。"
    play voice "voice/翔子/0206150.ogg"
    xz "那个蝉鸣好烦的说~"
    me01 "去跟蝉商量下。"
    play voice "voice/翔子/0206160.ogg"
    xz "去屋里把扇子和麦茶帮我拿来吧。"
    me01 "别把我当跑腿的使唤啊！"
    play voice "voice/翔子/0206170.ogg"
    xz "这是第五个要求。"
    "简直是暴君啊......"
    pause 0.1 hard
    scene set only xz_cg daze
    with dissolve
    play voice "voice/翔子/0206180.ogg"
    xz "啊，好想快点凉快起来啊~"
    "真是个无可救药的巫女。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with dissolve
    pause 3.0 hard

label day06.starview_event01:
    play music first_07 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 2.0 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0006510.ogg"
    lst "海水浴？"
    me01 "是啊。这周末大家都会去的。"
    me01 "雷亚也一起来如何？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0006520.ogg"
    lst "不要。"
    me01 "别马上拒绝啊，不稍微考虑一下吗？"
    play voice "voice/天使雷亚/0006530.ogg"
    lst "......"
    me01 "雷亚你见过大海吗？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0006540.ogg"
    lst "从这里不就能看到吗，虽然很暗。"
    me01 "有亲自去过那里吗？"
    play voice "voice/天使雷亚/0006550.ogg"
    lst "这倒没有。"
    me01 "我保证你看了一定会很兴奋的。另外偷偷告诉你，海水可是咸的哟。"
    play voice "voice/天使雷亚/0006560.ogg"
    lst "这种程度的知识我还是知道的。"
    me01 "大家都会去的。"
    play voice "voice/天使雷亚/0006570.ogg"
    lst "呼嗯~"
    me01 "雷亚也会去的吧？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    $ flcam.move(1500, -1800, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0006580.ogg"
    lst "不要擅自决定。"
    me01 "明天她们就要去选泳衣了，雷亚也一起去如何？"
    play voice "voice/天使雷亚/0006590.ogg"
    lst "不要。"
    me01 "雷亚的泳装，我很期待。"
    pause 0.1 hard
    scene set only lisite_cg shy
    with dissolve
    play voice "voice/天使雷亚/0006600.ogg"
    lst "......变态。"
    me01 "放心好了，对方是小孩子的话我是不会有奇怪想法的。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0006610.ogg"
    lst "能捅你吗？"
    me01 "莫非雷亚你......希望我动歪脑筋吗？"
    pause 0.1 hard
    scene set only lisite_cg shy
    with dissolve
    play voice "voice/天使雷亚/0006620.ogg"
    lst "才、才没有那种事！"
    me01 "没想到雷亚还是个成熟的小孩子呢~"
    $ flcam.move(2000, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0006630.ogg"
    lst "吵死了你这个变态！"
    pause 0.1 hard
    stop music fadeout 5.0
    scene black
    with dissolve
    pause 1.0 hard
    play sound hite_1
    show hite_1 onlayer m2
    pause 2.0 hard
    $ flcam.move(0, -100, 400)
    scene set only starview night starview
    with dissolve
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    with vpunch
    me01 "我闪！"
    "我一个后撤步躲过了飞袭而来的镰刀。"
    play music first_13 fadein 3.0 if_changed
    me01 "太天真了，你那些招式都已经被我看穿了！"
    $ flcam.move(-1800, -300, 600, duration=2.0)
    pause 2.0 hard
    $ flcam.move(1800, -300, 600, duration=2.0)
    pause 2.0 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.5 hard
    "啊咧......人呢？"
    "因为打不着所以赌气回去了？"
    $ flcam.move(0, -100, 400, duration=1.5)
    play sound punch
    show wflash onlayer f1
    with vpunch
    "{size=72}彭！！！{/size}"
    pause 1.0 hard
    me01 "好痛！"
    "感受到了来自头顶的冲击。"
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1_d b1 b1_n1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/天使雷亚/0006640.ogg"
    lst "今晚的你也是笨笨的呢。"
    "我转过身，雷亚就站在离我不远的位置。"
    me01 "刚刚是怎么回事？"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0006650.ogg"
    lst "从你身后用刀柄揍了你。"
    me01 "不是指那个，你还会瞬间移动吗？"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_n2 onlayer m2:
        xpos 0.3
    play voice "voice/天使雷亚/0006660.ogg"
    lst "不是啊，只是消失了再显现而已。"
    me01 "这种程度也能做得到吗？"
    show ts_lst_ssz_b2_d b2 b2_s1
    play voice "voice/天使雷亚/0006670.ogg"
    lst "因为今晚的星光不是很稳定。"
    me01 "我一直很在意。一旦星光消失了，雷亚就会跟着不见吗？"
    show ts_lst_ssz_b2_d b2 b2_n2
    play voice "voice/天使雷亚/0006680.ogg"
    lst "嗯。"
    me01 "这是什么原理？"
    show ts_lst_ssz_b2_d b2 b2_s1
    play voice "voice/天使雷亚/0006690.ogg"
    lst "那种东西我才不知道。"
    me01 "明明不知道原理但却能做到？"
    show ts_lst_ssz_b2_d b2 b2_n1
    play voice "voice/天使雷亚/0006700.ogg"
    lst "不都是这样的吗？你也不知道自己为什么用两只脚走路吧？"
    "的确是这样。"
    me01 "那雷亚你会游泳吗？"
    show ts_lst_ssz_b2_d b2 b2_s2
    play voice "voice/天使雷亚/0006710.ogg"
    lst "那种事我才不知道。"
    me01 "连瞬间移动这种技能都能掌握，雷亚你肯定能做到的。"
    show ts_lst_ssz_b2_d b2 b2_sp1
    play voice "voice/天使雷亚/0006720.ogg"
    lst "是这样吗？"
    me01 "是啊，就算不行我也会教你的。"
    hide ts_lst_ssz_b2_d 
    show ts_lst_ssz_b1_d b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/天使雷亚/0006730.ogg"
    lst "......"
    me01 "海水浴，再稍微考虑一下吧？"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0006740.ogg"
    lst "......真拿你没办法，我会考虑一下的。"
    pause 2.0 hard
    stop music fadeout 5.0
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    $ suppress_overlay = True
    jump day07
