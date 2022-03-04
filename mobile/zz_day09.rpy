label day09:
    bookmark
    $ save_name = _("Day 09")
    pause 4.0 hard
    scene set only backend_yinghua autumn
    with dissolve
    show backend_bg03 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date08 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    $ suppress_overlay = False
    scene set only hospital day outside
    with dissolve
    pause 2.0 hard
    "人生中第一次翘课，仅仅只是为了能和“她”有更多聊天的机会。"
    pause 1.0 hard
    scene set only hospital day passwalk
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "说实话我还是很紧张。"
    "犹豫了好一会儿才下定决心。"
    play sound knock_door
    pause 0.5 hard
    scene black
    with dissolve
    pause 1.0 hard
    play sound open_door3
    $ flcam.move(0, 0, 0)
    scene set only hospital day room yinghua
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0602030.ogg"
    xz "啊，凉君~"
    pause 1.0 hard
    scene set only xz_cg hsp normal
    with dissolve
    play music first_42 fadein 3.0 if_changed
    play voice "voice/翔子/0602040.ogg"
    xz "又来探病了吗？"
    me01 "打扰了。"
    play voice "voice/翔子/0602050.ogg"
    xz "不会，我一直都很闲的。除了看海以外就无事可做了。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0602060.ogg"
    xz "所以你能来我很开心。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602080.ogg"
    xz "其实我也猜到了你今天会来。"
    me01 "是这样吗？"
    play voice "voice/翔子/0602090.ogg"
    xz "嗯，是的。"
    me01 "为什么？"
    play voice "voice/翔子/0602100.ogg"
    xz "因为昨天的你，总感觉有话没说完。"
    play voice "voice/翔子/0602110.ogg"
    xz "但又不知道该怎么说出口，所以才匆匆离开的吧。"
    play voice "voice/翔子/0602120.ogg"
    xz "所以你今天是来反击的吗？"
    me01 "反击......怎么感觉像是在和什么战斗一样。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0602130.ogg"
    xz "凉君你是对我有所顾虑吧？"
    me01 "就这么明显吗？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602140.ogg"
    xz "感觉就是这样的~"
    me01 "为什么？"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0602150.ogg"
    xz "因为凉君，在回答问题之前总会停顿一下，感觉好像在犹豫什么该说什么不该说似的。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602160.ogg"
    xz "所以你不是来反击的吗？"
    me01 "关于我的事情，你真的......什么都不记得了吗？"
    play voice "voice/翔子/0602170.ogg"
    xz "不记得了哟。嗯，不记得了。"
    me01 "是“不记得”而不是“不认识”对吧？"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0602180.ogg"
    xz "啊，说错了。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602190.ogg"
    xz "我们没有见过面哟。嗯，没有见过面。"
    me01 "突然觉得很可疑啊。"
    play voice "voice/翔子/0602200.ogg"
    xz "不可疑哟。嗯，不可疑。"
    me01 "其实是在我回去之后想起来了吧？"
    play voice "voice/翔子/0602210.ogg"
    xz "没有那种事哟。嗯，没有那种事。"
    me01 "果然很可疑。"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0602220.ogg"
    xz "你连姐姐的话都不相信了吗？"
    me01 "为什么你知道自己是姐姐？"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0602230.ogg"
    xz "......诶？"
    me01 "不管是昨天还是今天，我都没有告诉你我的年龄吧？"
    scene set only xz_cg hsp sad
    play voice "voice/翔子/0602240.ogg"
    xz "不是那样的。"
    play voice "voice/翔子/0602250.ogg"
    xz "我从昨天接待你的那名护士那里问了关于你的事情。所以才知道你是樱华中学二年级的学生。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602260.ogg"
    xz "所以我就是你姐姐。明白了吗？"
    play voice "voice/翔子/0602270.ogg"
    xz "我和你，是昨天第一次见面的。姐姐说的话你都不听了吗？"
    me01 "我不听我不听。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0602280.ogg"
    xz "为什么这么固执啊......"
    me01 "你是今年七月才搬到这里的吧？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602290.ogg"
    xz "是啊。"
    me01 "七夕那天，我们见过面的吧？"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0602300.ogg"
    xz "......"
    me01 "你不记得了吗？"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0602320.ogg"
    xz "嗯。"
    me01 "真的？"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0602330.ogg"
    xz "真的不记得了。"
    play voice "voice/翔子/0602340.ogg"
    xz "姐姐说的话都不听了吗？"
    me01 "不听。"
    play voice "voice/翔子/0602350.ogg"
    xz "以前你明明是很听话的说。（小声）"
    me01 "以前？你刚刚说了以前吧？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602360.ogg"
    xz "没有说哟。嗯，没有说。"
    me01 "你现在是在住院中吧？"
    play voice "voice/翔子/0602370.ogg"
    xz "是啊。看现在的情况不就知道了吗。"
    me01 "但还是能到外面去的吧？"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0602380.ogg"
    xz "现在的话出不去了。"
    me01 "抱歉。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602390.ogg"
    xz "真是的，不是你想的那样。"
    play voice "voice/翔子/0602400.ogg"
    xz "你理解错了啦。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0602410.ogg"
    xz "并不是因为病情恶化才出不去的，而是因为我擅自跑出去惹医生们生气的关系。"
    play voice "voice/翔子/0602420.ogg"
    xz "所以只是被盯上了而已。医生们虽然平时一副老好人的样子，但是生气起来很可怕的。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602430.ogg"
    xz "所以凉君你没必要自责，知道了吗？"
    me01 "真的吗？"
    play voice "voice/翔子/0602440.ogg"
    xz "真的。"
    me01 "为什么跑出去呢？"
    play voice "voice/翔子/0602460.ogg"
    xz "因为想稍微去小镇上转转。"
    me01 "是因为很久没回来了吧？"
    play voice "voice/翔子/0602470.ogg"
    xz "嗯，那个坡道果然还是和以前一样一点都没变......"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0602480.ogg"
    xz "啊、不对，我也是第一次去过那里。"
    me01 "穿着睡衣去的？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602490.ogg"
    xz "我这种状况穿着便服在医院里走反而会很显眼。所以必须在不被人发现的情况下才能出去。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0602500.ogg"
    xz "也不是这样的，换做是谁也不会随便穿着睡衣到处跑吧。"
    me01 "出去的时候也见过我的吧？"
    play voice "voice/翔子/0602510.ogg"
    xz "没有见过哟。嗯，没有见过。"
    me01 "知道银河吗？"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0602520.ogg"
    xz "怎么了突然问这个？"
    me01 "不知道吗？"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0602530.ogg"
    xz "当然知道，这可是常识呢。"
    me01 "银河，用英文说就是Milky Way。"
    play voice "voice/翔子/0602540.ogg"
    xz "这个我也知道。"
    me01 "你不觉得那看起来就像牛奶吗？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602550.ogg"
    xz "牛奶......总觉得像个小孩子一样~"
    me01 "是吗？"
    play voice "voice/翔子/0602560.ogg"
    xz "嗯，会把银河说成食物什么的。"
    me01 "最喜欢的食物是什么？"
    play voice "voice/翔子/0602570.ogg"
    xz "我的话，应该是炸面包吧。"
    me01 "你不觉得银河看起来像炸面包吗？"
    play voice "voice/翔子/0602580.ogg"
    xz "我......"
    stop music fadeout 5.0
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 2.5 alpha 1
    pause 3.0 hard
    scene set only xz_memory piecezero yinghua
    with in2out_v2_slow
    pause 1.0 hard
    play music first_27 fadein 3.0 if_changed
    play voice "voice/翔子/0602590.ogg"
    tiny_xz "凉君想要哪颗星星呢？"
    me01 "那颗就不错，又大又亮的那颗。"
    play voice "voice/翔子/0602600.ogg"
    tiny_xz "我倒觉得那个又白又长的就不错~"
    me01 "为什么？"
    play voice "voice/翔子/0602610.ogg"
    tiny_xz "因为不觉得那个很像炸面包吗？"
    pause 1.0 hard
    scene set only xz_cg hsp angry
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0602620.ogg"
    xz "......凉君。"
    "她鼓起了脸。"
    play voice "voice/翔子/0602630.ogg"
    xz "凉君什么时候变成这么卑鄙的孩子了，姐姐我很吃惊啊。"
    me01 "为什么这么说？"
    play voice "voice/翔子/0602640.ogg"
    xz "因为像诱导审问一样。"
    me01 "才不是那样的。"
    play voice "voice/翔子/0602650.ogg"
    xz "那你打算干什么？"
    me01 "这只是为了建立起友我们友好关系的第一步。想要彻底了解对方首先要从对方感兴趣的地方入手。"
    play voice "voice/翔子/0602660.ogg"
    xz "那为什么要说银河啊。"
    me01 "因为我很喜欢，樱华镇的星空。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0602670.ogg"
    xz "......"
    me01 "那片和你一起仰望过的、独一无二的星空。"
    play voice "voice/翔子/0602680.ogg"
    xz "......"
    play voice "voice/翔子/0602690.ogg"
    xz "这也是诱导审问？"
    me01 "这是我真实的想法。"  
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602700.ogg"
    xz "你说过你也是刚从都市那边搬过来的对吧？"
    me01 "嗯。"
    play voice "voice/翔子/0602710.ogg"
    xz "在那之前，我和你见过面了吗？"
    me01 "嗯。"
    play voice "voice/翔子/0602720.ogg"
    xz "一起玩耍了吗？"
    me01 "嗯。"
    "翔子的嘴角微微上扬，像是在笑。但却给人一种悲伤的感觉。"
    play voice "voice/翔子/0602730.ogg"
    xz "银河呢，是由两千亿颗星星汇聚而成的。"
    play voice "voice/翔子/0602740.ogg"
    xz "我们居住的地球，是以太阳为首的多颗星星组成的星云中的一员。"
    play voice "voice/翔子/0602750.ogg"
    xz "从地面仰望银河时的模样，就像是天河一般。"
    play voice "voice/翔子/0602760.ogg"
    xz "人类之所以能够知道这些，是因为发现了从银河那里传来的、肉眼无法捕捉到的光。"
    play voice "voice/翔子/0602770.ogg"
    xz "不可思议的电磁波。"
    play voice "voice/翔子/0602780.ogg"
    xz "而研究这种电磁波的学问，就叫电波天文学。你知道吗，凉君？"
    "我摇了摇头。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0602790.ogg"
    xz "太好了~"
    "她做出了胜利的手势。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    $ flcam.move(-1500, -2000, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0602800.ogg"
    xz "我呢，以前认识一个男孩。"
    play voice "voice/翔子/0602810.ogg"
    xz "为了不输给他我拼命地学习。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0602820.ogg"
    xz "那男孩虽然比我小，但却比我更了解星星。"
    play voice "voice/翔子/0602830.ogg"
    xz "不只是星星。对很多事情他都很了解。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602840.ogg"
    xz "所以我能教给他的，就只有{rb}Kiss{/rb}{rt}泛指恋爱{/rt}而已。"
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 2.5 alpha 1
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_cg kiss
    with in2out_v2_slow
    pause 1.0 hard
    play voice "voice/翔子/0602850.ogg"
    tiny_xz "还......不可以睁开眼睛哟。"
    play voice "voice/翔子/0602860.ogg"
    tiny_xz "睁开的话，就绝交。"
    pause 1.0 hard
    $ flcam.move(-1500, -2000, 600)
    scene set only xz_cg hsp normal
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0602870.ogg"
    xz "我觉得不甘心，于是就拼命地学习。"
    play voice "voice/翔子/0602880.ogg"
    xz "为了有一天能教那个男孩更多他所不知道的、关于星星的知识，我也稍微努力了一下。"
    me01 "也就是说。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0602890.ogg"
    xz "不是你哟。嗯，不是你。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0602900.ogg"
    xz "因为我记忆中的男孩和你不同，是既温柔又可爱的。"
    play voice "voice/翔子/0602910.ogg"
    xz "不像现在的你，坏心眼欺负人。"
    play voice "voice/翔子/0602920.ogg"
    xz "所以再会的kiss，我是绝对不会给你的~"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black
    with dissolve

label day09.starview_event01:
    play ambience1 zhiliao fadein 3.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night road
    with dissolve
    pause 2.0 hard
    scene set only starview night starview
    with dissolve
    pause 2.0 hard
    stop ambience1
    scene set only lisite_cg normal
    with dissolve
    pause 1.0 hard
    play music first_42 fadein 3.0 if_changed
    play voice "voice/天使雷亚/0016530.ogg"
    lst "今天你也去见你的“梦中情人”了吗？"
    me01 "只是去探望而已，你这种说法有些微妙啊。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0016540.ogg"
    lst "探望？"
    me01 "是的，她住在海边的医院。"
    play voice "voice/天使雷亚/0016550.ogg"
    lst "......"
    me01 "雷亚知道什么是住院吗？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0016560.ogg"
    lst "别把我当笨蛋，住院就是住在医院里吧？"
    me01 "是啊，为了接受治疗。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0016570.ogg"
    lst "那孩子身体不好吗？"
    me01 "好像是的。"
    play voice "voice/天使雷亚/0016580.ogg"
    lst "你也不知道吗？"
    me01 "嗯。"
    play voice "voice/天使雷亚/0016590.ogg"
    lst "没有问她吗？"
    me01 "嗯。"
    play voice "voice/天使雷亚/0016600.ogg"
    lst "你不想知道吗？"
    me01 "说实话，我想知道。"
    play voice "voice/天使雷亚/0016610.ogg"
    lst "那直接问她不就好了吗？"
    me01 "在犹豫该不该问的时候就是不该问。之前雷亚不是这么说的吗？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0016620.ogg"
    lst "当确信该问的时候，对方自然就会说了？"
    me01 "是啊。"
    play voice "voice/天使雷亚/0016630.ogg"
    lst "那是什么时候？"
    me01 "不知道。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0016640.ogg"
    lst "净是些不知道的事情。"
    pause 1.0 hard
    scene set only starview night starview
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    me01 "雷亚。"
    $ flcam.move(0, -200, 600, duration=1.5)
    play sound hide_sound
    hide ts_lst_ssz_b2 with None
    pause 0.1 hard
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2 at flu_down(0.15, 30):
        xpos 0.5
    play voice "voice/天使雷亚/0016650.ogg"
    lst "！"
    "我刚向她靠近，雷亚也顺势后退了几步。"
    me01 "我什么都不会做的。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0016660.ogg"
    lst "那、那就好！"
    me01 "雷亚你知道银河吗？"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016670.ogg"
    lst "知道啊。在夜空中不就可以看到吗？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    me01 "那雷亚你觉得，银河像什么？"
    pause 1.0 hard
    stop music fadeout 5.0
    $ flcam.move(0, -200, 600)
    scene set only starview night starview
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/天使雷亚/0016680.ogg"
    lst "银河，就是天上的河流吧。"
    me01 "那你觉得它的本体是什么？"
    show ts_lst_ssz_b2 b2 b2_sp1
    play voice "voice/天使雷亚/0016690.ogg"
    lst "本体？"
    me01 "嗯，银河的本体。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016700.ogg"
    lst "把牛郎星和织女星分开的，境界线？"
    me01 "真是小孩子的回答啊~"
    play sound punch
    show wflash onlayer f1
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2_d b2 b2_a1 onlayer m2:
        xpos 0.5
    with vpunch
    "{size=72}咚！！！{/size}"
    pause 0.5 hard
    me01 "好痛。"
    show ts_lst_ssz_b2_d b2 b2_h1
    play music first_13 fadein 3.0 if_changed
    play voice "voice/天使雷亚/0016720.ogg"
    lst "好久没这样做了，但还是觉得不错。"
    me01 "明明昨天也打过的吧？"
    show ts_lst_ssz_b2_d b2 b2_sp1
    play voice "voice/天使雷亚/0016740.ogg"
    lst "还有其他的答案吗？"
    me01 "大人会做出更科学的解释。"
    show ts_lst_ssz_b2_d b2 b2_a1
    play voice "voice/天使雷亚/0016750.ogg"
    lst "我比凉君更像大人~"
    me01 "哪里像了？"
    play sound punch
    show wflash onlayer f1
    show ts_lst_ssz_b2_d b2 b2_ga1
    with vpunch
    "{size=72}咚！！！{/size}"
    pause 0.5 hard
    me01 "好痛。"
    show ts_lst_ssz_b2_d b2 b2_a1
    play voice "voice/天使雷亚/0016770.ogg"
    lst "我是大人哟。"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016780.ogg"
    lst "我是个成熟的死神~"
    me01 "死神才不会变得成熟呢。"
    show ts_lst_ssz_b3 b3 b3_ga1
    play voice "voice/天使雷亚/0016790.ogg"
    lst "......被模仿了。"
    me01 "所谓的天河呢，形容的是从地面观测银河时所呈现出来的样子。"
    show ts_lst_ssz_b3 b3 b3_s1
    play voice "voice/天使雷亚/0016800.ogg"
    lst "呼嗯~"
    me01 "我们之所以能够知道这些，是因为发现了从银河那里传来的、肉眼无法捕捉到的光。"
    hide ts_lst_ssz_b3
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016810.ogg"
    lst "真是无聊的回答呢。"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/0016820.ogg"
    lst "去注意那些肉眼看不到的东西也没有什么意义吧。"
    show ts_lst_ssz_b2 b2 b2_s1
    play voice "voice/天使雷亚/0016830.ogg"
    lst "人们明明就连能看见的东西，都不会用心去看的......"
    me01 "我能看见雷亚你。"
    show ts_lst_ssz_b2 b2 b2_n1
    play voice "voice/天使雷亚/0016850.ogg"
    lst "那是当然的。"
    me01 "所以请不要突然消失啊。"
    stop music fadeout 5.0
    show ts_lst_ssz_b2 b2 b2_s3
    play voice "voice/天使雷亚/0016860.ogg"
    lst "......"
    me01 "我们约好了。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016870.ogg"
    lst "不要。"
    "雷亚将头转向一旁。"
    $ flcam.move(0, -350, 1000, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0016880.ogg"
    lst "我不会再和谁做约定了。"
    show ts_lst_ssz_b1 b1 b1_s3
    play voice "voice/天使雷亚/0016890.ogg"
    lst "因为我已经有过约定了，再追加的话会很辛苦的。"
    play voice "voice/天使雷亚/0016900.ogg"
    lst "再追加的话......我会承受不了的。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    $ suppress_overlay = True
    jump day10
