label day12:
    bookmark
    $ save_name = _("Day 12")
    pause 4.0 hard
    scene set only backend_yinghua winter
    with dissolve
    show backend_bg04 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date11 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    play ambience1 niaoming
    $ suppress_overlay = False
    scene set only hospital day outside
    with dissolve
    play music first_26 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(-2250, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_sp1 onlayer m2 at walkin_l(0.4)
    pause 0.5 hard
    play voice "voice/翔子/0232210.ogg"
    xz "这是第几次到医院来了？"
    $ flcam.move(0, -350, 750, duration=1.5)
    show lingyin_dsf_b2 b2 b2_n2 onlayer m2 at walkin_r(0.6)
    pause 0.5 hard
    play voice "voice/青木铃音/0533470.ogg"
    lingyin "为神野同学的事情而来的话应该算是第一次吧？"
    pause 1.0 hard
    hide xz_dsf_b2
    hide lingyin_dsf_b2
    $ flcam.move(-1000, -1500, 1100, duration=1.5)
    pause 0.5 hard
    "由于青木家父在这所医院工作的缘故，即使没有什么事情两人也会经常前来探望。"
    "然而此行的目的除了探望还有更重要的事情。"
    "之前答应过了帮助调查七月份入院病人的资料，两位“学生会优等生”也势必会言出必行。"
    "医院的布局分为两部分。"
    "主要的就诊都在中央大楼进行，急诊或者住院手续也是在这里。"
    "而接下来要去的西区大楼，则是为一些长期住院的患者准备的。"
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.4
    show lingyin_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.6
    play voice "voice/青木铃音/0533480.ogg"
    lingyin "已经提前跟对方打过招呼了，我们走吧。"
    hide xz_dsf_b2
    show xz_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.4
    play voice "voice/翔子/0232240.ogg"
    xz "探病的时候记得保持安静。"
    pause 1.0 hard
    scene black
    with dissolve
    stop ambience1 fadeout 2.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only hospital day passwalk
    with dissolve
    pause 2.0 hard
    $ flcam.move(-2250, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_n2 onlayer m2 at walkin_r(0.4)
    pause 0.5 hard
    play voice "voice/翔子/0232250.ogg"
    xz "在这里住院的患者并不是很多，所以父亲好像已经记住了所有患者的名字。"
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    show lingyin_dsf_b2 b2 b2_n2 onlayer m2 at walkin_r(0.6)
    pause 0.5 hard
    play voice "voice/青木铃音/0533500.ogg"
    lingyin "患者基本上都是上了年纪的，即使年轻的也已经是三十多岁的样子了。"
    hide xz_dsf_b3
    show xz_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.4
    play voice "voice/翔子/0232290.ogg"
    xz "详细的我也没有多问，范围好像都是七月的时候从别的医院搬过来的吧？"
    hide lingyin_dsf_b2
    show lingyin_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.6
    play voice "voice/青木铃音/0533510.ogg"
    lingyin "毕竟这些信息是不会轻易泄露给无关人员的，如果是家人的话就另当别论了。"
    show xz_dsf_b1 b1 b1_n2
    play voice "voice/翔子/0232310.ogg"
    xz "即使问了父亲他也不肯回答呢。"
    show xz_dsf_b1 b1 b1_s1
    play voice "voice/翔子/0232300.ogg"
    xz "......真是难办了啊。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard

label day12.hospital_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua
    with dissolve
    pause 2.0 hard
    play music first_41 fadein 3.0 if_changed
    scene set only xz_cg hsp normal
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0605220.ogg"
    yume "我不在的时候，有乖乖地待着吗？有好好地坐在椅子上吗？"
    me01 "我是小孩子吗......"
    "刚刚接受过治疗的翔子一回到病房就和我聊起了天。"
    play voice "voice/翔子/0605230.ogg"
    yume "所以到底怎样的呢？"
    me01 "我有老实待着啦。"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0605240.ogg"
    yume "真的吗？"
    me01 "为什么要怀疑啊。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0605250.ogg"
    yume "因为如果床底下被人搜过的话还是会觉得讨厌啊。"
    me01 "藏着什么东西吗？"
    play voice "voice/翔子/0605260.ogg"
    yume "嗯。"
    me01 "藏着什么东西？"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0605270.ogg"
    yume "工口书籍~"
    me01 "......抱歉，刚说了啥？"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0605280.ogg"
    yume "这种话就不要让女孩子说出来啊，真是的。"
    me01 "你是认真的？"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0605290.ogg"
    yume "当然是骗你的呀~"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0605300.ogg"
    yume "凉君，今天是你第几次来探病了？"
    me01 "已经一个月了，所以差不多来了三十次吧。"
    play voice "voice/翔子/0605310.ogg"
    yume "每天都来啊？"
    me01 "嗯。"
    play voice "voice/翔子/0605320.ogg"
    yume "不觉得麻烦吗？"
    me01 "完全不会。"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0605330.ogg"
    yume "真的吗？"
    me01 "嗯。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0605340.ogg"
    yume "感觉你来的次数已经超过妖精先生了。"
    me01 "那位家庭教师来的频率大概是怎样的？"
    play voice "voice/翔子/0605350.ogg"
    yume "三天来一次左右？"
    me01 "可我们甚至连一次面也没有见到。"
    play voice "voice/翔子/0605360.ogg"
    yume "他每次都是在凉君回去以后才来的。"
    me01 "现在在学些什么呢？"
    play voice "voice/翔子/0605370.ogg"
    yume "关于宇宙的知识。"
    me01 "......一直都是跟天文有关的内容吗？"
    play voice "voice/翔子/0605380.ogg"
    yume "嗯，妖精先生以前好像是天文部的。这似乎是他最得意的科目哟。"
    me01 "翔子的梦想是成为天文学家吗？"
    play voice "voice/翔子/0605390.ogg"
    yume "虽然我没有想过，但如果能当的话也不错呢~"
    me01 "可如果要成为科学家的话，除了天文学以外的内容也要学习才行。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0605400.ogg"
    yume "天文学家什么的不当也罢。"
    me01 "放弃得这么干脆吗。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0605410.ogg"
    yume "我从妖精先生那里听说了。凉君你知道吗？"
    $ flcam.move(-750, -1000, 300, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0605420.ogg"
    yume "天文学家和宇宙物理学家，都在尝试着用一个数学公式来证明宇宙的奥秘。"
    play voice "voice/翔子/0605430.ogg"
    yume "但即使找到了公式，随着宇宙探索的进展马上就会产生新的分歧。所以他们每天都在研究。"
    play voice "voice/翔子/0605440.ogg"
    yume "宇宙，真的是非常广阔呢~"
    play voice "voice/翔子/0605460.ogg"
    yume "银河里的两千亿颗恒星中的一个，就是我们的太阳。"
    play voice "voice/翔子/0605470.ogg"
    yume "而环绕在太阳周围的行星之一，就是我们的地球了。"
    play voice "voice/翔子/0605480.ogg"
    yume "然后，住在地球上的我和凉君，也只不过是六十亿人中的两位而已。"
    play voice "voice/翔子/0605490.ogg"
    yume "我们是那么的渺小。"
    play voice "voice/翔子/0605500.ogg"
    yume "但是我们却依然想要探索宇宙。"
    play voice "voice/翔子/0605510.ogg"
    yume "虽然这好像有点不知天高地厚一样......"
    play voice "voice/翔子/0605520.ogg"
    yume "但是，我们其实和住在宇宙中是一样的。"
    play voice "voice/翔子/0605530.ogg"
    yume "所以了解一下自己的家是什么样的，也不是什么坏事吧？"
    me01 "但我觉得在了解宇宙之前，先了解地球本身可能比较好一点。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0605540.ogg"
    yume "是吗？"
    me01 "如果说宇宙是家的话，地球就是房间了吧。我们现在可是连房间是什么样子的都没有完全搞清楚。"
    me01 "构成地球内部的环境的成分仍然还有很多值得学习的东西，书上是这么说的。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0605560.ogg"
    yume "......"
    "对方似乎有点不高兴了。"
    play voice "voice/翔子/0605570.ogg"
    yume "......被凉君教育了。"
    me01 "这在以前不是常有的事情吗？"
    play voice "voice/翔子/0605580.ogg"
    yume "所以我才讨厌嘛。"
    me01 "那你是承认我们以前在一起学习过了吗？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0605590.ogg"
    yume "不承认哟。嗯，不承认。"
    me01 "明明都已经找到你说话的破绽了。"
    play voice "voice/翔子/0605600.ogg"
    yume "没有找到哟。嗯，没有找到。"
    me01 "我一定不会再忘记你了。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0605610.ogg"
    yume "......"
    $ flcam.move(-1500, -2000, 600, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    me01 "因为我对你......"
    play voice "voice/翔子/0605620.ogg"
    yume "对我......什么？"
    stop music fadeout 5.0
    me01 "......"
    play voice "voice/翔子/0605630.ogg"
    yume "话刚说到一半啊？"
    me01 "......"
    play voice "voice/翔子/0605640.ogg"
    yume "是很难说出口吗？"
    me01 "稍微需要一点勇气......"
    "对我来说，这是比解开宇宙的秘密更难做到的事情。"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0605650.ogg"
    yume "凉君。"
    play voice "voice/翔子/0605660.ogg"
    yume "如果你说了奇怪的话，我就禁止你来探望哟。"
    "我知道的，明明是知道的。"
    "但是......"
    me01 "即使你赶我走也没关系，但是我想说的是......"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play music first_29 fadein 3.0 if_changed
    play voice "voice/翔子/0605760.ogg"
    yume "吓、吓了我一跳啊，真是的。"
    "翔子打断了我的话。"
    play voice "voice/翔子/0605770.ogg"
    yume "血压，都上升了啊。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0605780.ogg"
    yume "身体也非常的热。"
    play voice "voice/翔子/0605790.ogg"
    yume "现在如果再去检查的话，绝对会变成谢绝会面的状态呢。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    $ flcam.move(-750, -1000, 300, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    me01 "我想说......"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0605800.ogg"
    yume "凉君。"
    play sound hite_3
    with vpunch
    pause 1.0 hard
    "翔子突然敲了一下我的额头。"
    play voice "voice/翔子/0605810.ogg"
    yume "虽然不知道这是什么恶作剧，但是请不要再做第二次了。"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0605830.ogg"
    yume "刚才的事我就当没发生过，知道了吗？"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0605840.ogg"
    yume "回答呢？"
    me01 "......"
    play voice "voice/翔子/0605850.ogg"
    yume "姐姐说的话你都不听了吗？"
    me01 "......"
    play voice "voice/翔子/0605860.ogg"
    yume "如果再顶嘴的话就禁止你来探病哟。"
    me01 "......我知道了。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0605870.ogg"
    yume "很好~"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0605890.ogg"
    yume "那么，现在继续畅谈天文知识吧。"
    me01 "那个......"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0605900.ogg"
    yume "什么？"
    me01 "偶尔也说点别的话题怎么样？"
    play voice "voice/翔子/0605910.ogg"
    yume "别的话题是？"
    me01 "总是讲天文知识的话就算是我也会觉得厌倦的。"
    me01 "有其他的话题吗？"
    play voice "voice/翔子/0605930.ogg"
    yume "没有呢。"
    me01 "没有吗......"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0605940.ogg"
    yume "没有。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0605950.ogg"
    yume "凉君你有吗？"
    me01 "恋爱......之类的？"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0605960.ogg"
    yume "......你不是凉君！"
    play voice "voice/翔子/0605970.ogg"
    yume "我所认识的凉君是不可能会说到恋爱话题的。"
    me01 "为什么啊？"
    play voice "voice/翔子/0605980.ogg"
    yume "因为凉君你对恋爱很生疏吧？"
    me01 "别随便下结论啊。"
    play voice "voice/翔子/0605990.ogg"
    yume "不是吗？"
    me01 "虽然以前是这样没错。"
    play voice "voice/翔子/0606000.ogg"
    yume "现在不是了吗？"
    me01 "现在也许也还是那样的。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0606010.ogg"
    yume "那就“嘿”地把恋爱的话题扔到垃圾桶去吧~"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606020.ogg"
    yume "这样一来，剩下的就只有天文知识了嘛。"
    me01 "翔子的初恋是谁呢？"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0606030.ogg"
    yume "扔进垃圾桶，{rb}嘿{/rb}{rt}扔垃圾的声音{/rt}。"
    me01 "你喜欢什么样的男孩子？"
    play voice "voice/翔子/0606040.ogg"
    yume "嘿！"
    me01 "有和谁交往过吗？"
    play voice "voice/翔子/0606050.ogg"
    yume "嘿！"
    me01 "现在还是单身吗？"
    play voice "voice/翔子/0606060.ogg"
    yume "嘿！"
    "全都被扔掉了。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0606070.ogg"
    yume "果然除了天文知识就想不到其他话题了啊。"
    me01 "......等等。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606080.ogg"
    yume "凉君，你觉得幸福是什么？"
    me01 "......真是突然啊。"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0606090.ogg"
    yume "不是凉君你说要说点别的话题的吗。所以到底是什么？"
    me01 "幸福也是因人而异的，我觉得没有统一的答案。"
    play voice "voice/翔子/0606100.ogg"
    yume "才不是那样的，是有答案的哟~"
    me01 "是什么？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606110.ogg"
    yume "幸福呢，就是强迫固执的一方直到他认输为止。"
    me01 "......什、什么？"
    play voice "voice/翔子/0606120.ogg"
    yume "固执的，对象，直到明白为止，一直强迫他。（注释：四个短语的日文发音第一个音连起来就是日语的“幸福”）"
    me01 "原来是字谜啊。"
    play voice "voice/翔子/0606130.ogg"
    yume "凉君，那你觉得普通是什么？"
    me01 "钓鲫鱼的秃头？"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0606140.ogg"
    yume "那是什么鬼故事啊......"
    me01 "鲫鱼，钓，秃头。（注释：三个短语的日文发音第一个音连起来就是日语的“普通”）"
    play voice "voice/翔子/0606150.ogg"
    yume "认真地去解释那么无聊的玩笑是很冷啦。"
    me01 "......那答案是？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606160.ogg"
    yume "就是平凡地度过每一天啊。"
    play voice "voice/翔子/0606170.ogg"
    yume "将“普通”的汉字分解开的话就是这样了（平常の日々を送る）。"
    "果然还是文字游戏啊！"
    play voice "voice/翔子/0606180.ogg"
    yume "所以，我呢......"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0606190.ogg"
    yume "也会一直强迫着凉君，直到你肯过上平凡的生活为止。"
    me01 "......"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606200.ogg"
    yume "懂了吗？"
    me01 "不懂。"
    play voice "voice/翔子/0606210.ogg"
    yume "是吗。果然对凉君而言有点太难了吗？"
    stop music fadeout 5.0
    me01 "那对翔子你而言，到底什么才算是幸福呢？"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play music first_23 fadein 3.0 if_changed
    "翔子她一直都在医院里。"
    "那一定是段很漫长的时光。"
    "在病房里甚至没见过她穿过其他的衣服。"
    "她肯定也一直都没有买过新衣服。"
    "没有化过妆。"
    "指甲也一直很短。"
    "头发也只是稍微修剪了一下。"
    "所以，这一切的东西，作为平常人的生活，翔子都是没有的。"
    "同龄的女孩子们所拥有的普通的东西，她却没有。"
    "被疾病夺走了。"
    "翔子她所期待的，我的普通。"
    "而就是那种普通，她自己并没有。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0606220.ogg"
    yume "我的幸福，吗......"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606230.ogg"
    yume "一下子想不出来啊。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    me01 "小时候的约定，还记得吗？"
    me01 "如果再会的话，我们就结婚。这个约定，你还记得吗？"
    me01 "一直以来我的心意都没有改变。"
    me01 "即使过去了这么长的时间也依旧如此。"
    me01 "我喜欢你，翔子。"
    me01 "和我，交往吧。"
    me01 "成为我的恋人吧。"
    play voice "voice/翔子/0606240.ogg"
    yume "......"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0606250.ogg"
    yume "不行，的啊。"
    play voice "voice/翔子/0606260.ogg"
    yume "我，是不能和凉君交往......"
    play voice "voice/翔子/0606270.ogg"
    yume "我是无法成为凉君恋人的。"
    play voice "voice/翔子/0606280.ogg"
    yume "因为凉君，还只是小孩子。"
    play voice "voice/翔子/0606290.ogg"
    yume "这样的恋情，只是小孩子的幻想而已。"
    play voice "voice/翔子/0606300.ogg"
    yume "是过去的你所做的梦而已。"
    play voice "voice/翔子/0606310.ogg"
    yume "是一场噩梦。"
    play voice "voice/翔子/0606320.ogg"
    yume "是已经褪色了的，回忆......"
    me01 "才没有褪色！"
    me01 "这也不是幻想。"
    me01 "不是小孩子的玩笑。"
    me01 "我已经不是小孩子了。"
    me01 "我已经成长了。"
    play voice "voice/翔子/0606330.ogg"
    yume "......不是的。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606340.ogg"
    yume "你没有成长。嗯，没有成长。"
    play voice "voice/翔子/0606350.ogg"
    yume "凉君跟以前一样，一点都没有变。"
    play voice "voice/翔子/0606360.ogg"
    yume "还是没能成为优等生。"
    play voice "voice/翔子/0606370.ogg"
    yume "虽然很可惜。连我都觉得你只差一点点了。"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0606380.ogg"
    yume "但是，你却向我告白了。"
    play voice "voice/翔子/0606390.ogg"
    yume "说明你完全不行的。"
    play voice "voice/翔子/0606400.ogg"
    yume "不及格哟。"
    me01 "......也就是说，我被甩了吗？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606410.ogg"
    yume "是啊。"
    play voice "voice/翔子/0606420.ogg"
    yume "你是我的朋友。很重要的朋友。"
    play voice "voice/翔子/0606430.ogg"
    yume "虽然现在才说很抱歉，但你的确是我第一个朋友。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0606440.ogg"
    yume "正因为你是我的朋友。"
    play voice "voice/翔子/0606450.ogg"
    yume "我才会这么想的。"
    scene set only xz_cg hsp daze
    play voice "voice/翔子/0606460.ogg"
    yume "但是，如果你不是这么认为的话。"
    play voice "voice/翔子/0606470.ogg"
    yume "那我就只能禁止你来探病了。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    $ flcam.move(-1500, -2000, 600, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0606480.ogg"
    yume "因为你期望和我有朋友以外的关系。"
    play voice "voice/翔子/0606490.ogg"
    yume "因为你期望和我有恋人的关系。"
    play voice "voice/翔子/0606500.ogg"
    yume "所以以后，也请不要再来这里了。"
    me01 "不是这样的，其实我......"
    play voice "voice/翔子/0606510.ogg"
    yume "拜托了。"
    me01 "......"
    pause 1.0 hard
    scene black
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only hospital day room yinghua alpha
    with dissolve
    pause 1.0 hard
    "没想到鼓起勇气的举动竟然会迎来这样的结局。"
    pause 0.5 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    "在走出病房前我还是停下了脚步。"
    me01 "......我的朋友们。"
    me01 "多亏了她们，我才能这么快融入这里的生活。"
    me01 "我以后不会再来了。"
    me01 "但是如果、我是说如果。"
    me01 "她们能代替我来探望你的话......"
    play voice "voice/翔子/0606520.ogg"
    yume "嗯，可以哟~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_cg hsp sad
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0606540.ogg"
    yume "回到樱华镇后，我一个人独处的时间太长了。"
    play voice "voice/翔子/0606550.ogg"
    yume "那真是非常无聊、同时也是非常痛苦的时光。"
    play voice "voice/翔子/0606560.ogg"
    yume "为此我非常地不安。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0606570.ogg"
    yume "但是多亏了凉君你，那样的感觉已经消失不见了。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0606580.ogg"
    yume "因为凉君的陪伴鼓励了我。"
    play voice "voice/翔子/0606590.ogg"
    yume "最后还要介绍朋友给我。"
    play voice "voice/翔子/0606600.ogg"
    yume "所以，谢谢你。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    $ flcam.move(-1500, -2000, 600, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0606610.ogg"
    yume "你果然，是我最好的朋友~"
    pause 2.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only hospital day outside
    with dissolve
    pause 1.0 hard
    "是啊，不是恋人而是朋友。"
    "我本应对此感到满足了才对。"
    pause 1.0 hard
    scene set only sky day yinghua
    with dissolve
    pause 1.0 hard
    "第一次在黄昏前结束探望，也是最后一次。"
    "这也许就是初恋吧。如果不是的话，那我这样的人一定是无法得到爱的。"
    "长年守望着的恋爱崩塌了。"
    "就在今天，我失恋了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 3.0 hard

label day12.shenshe_event01:
    scene set only shenshe night yinghua
    with dissolve
    pause 2.0 hard
    scene set only party front
    with dissolve
    pause 2.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_h2 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/万夜花/1305250.ogg"
    wyh "呀嚯，等你好久了~"
    play music first_17 fadein 3.0 if_changed
    pause 0.5 hard
    show dh_zf_b1 b1 b1_ga2 onlayer m2 at walkin_l(0.5)
    $ flcam.move(2250, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801590.ogg"
    stranger "......你穿成这样还用这种语气真的合适吗？"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/1305260.ogg"
    wyh "因为听你说是有关星天宫的话题，所以虽然觉得麻烦但是还是换上了正装。明明我晚上还喝了酒的。"
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/1801600.ogg"
    stranger "这么急着通知你真是抱歉。"
    hide wyh_wnf_b1
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/1703670.ogg"
    ts_lian "......"
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305270.ogg"
    wyh "好久不见了呢，莲。你和神野老师都还好吗？"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/1703680.ogg"
    ts_lian "托你的福......虽然充当保护者的角色也是很累的。"
    hide wyh_wnf_b1
    pause 0.5 hard
    show dh_zf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801610.ogg"
    dh "谁是谁的保护者啊？"
    play voice "voice/天使莲/1703690.ogg"
    ts_lian "当然我是大和君的保护者。"
    hide dh_zf_b1
    hide ts_lian_ssz_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.7
    play voice "voice/万夜花/1305280.ogg"
    wyh "啊哈哈，看到你们还是老样子我就放心了。"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    show dh_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801620.ogg"
    dh "不到夜晚莲就无法发挥她原本的力量，所以没办法轻易地与你见面。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1305290.ogg"
    wyh "话说我也有点想见见总一郎和诗乃了呢~"
    show dh_zf_b1 b1 b1_s1
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/1703700.ogg"
    ts_lian "是吗，总一郎君的话倒先不说......"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305300.ogg"
    wyh "诗乃还是没有找到吗......"
    play voice "voice/天使莲/1703710.ogg"
    ts_lian "......"
    show dh_zf_b1 b1 b1_s2
    play voice "voice/神野大和/1801630.ogg"
    dh "都说了让大家不要在意。"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/1305310.ogg"
    wyh "老师你就算这样说也没用的，因为最在意的本来就是你自己啊。"
    stop music fadeout 5.0
    hide wyh_wnf_b1
    hide ts_lian_ssz_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1801650.ogg"
    dh "闲话就到此为止吧，接下来还要说正事了。"
    pause 0.5 hard
    play music first_26 fadein 3.0 if_changed
    show wyh_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305330.ogg"
    wyh "跟星天宫有关的话题，也就是说和莲有关吧？"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/1801660.ogg"
    dh "也可以这么说。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305340.ogg"
    wyh "我可没有想过把莲出卖给星天宫。从一开始这点就从来没有改变过。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/1305350.ogg"
    wyh "当时我虽然是星天宫的巫女但却更喜欢天文部，即使现在成了神官，我也依然把社团的大家当成朋友。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1305360.ogg"
    wyh "老师和莲当然也包括在其中哟~"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1801670.ogg"
    dh "我知道。实际上，至今为止我都没有见过巫女来讨伐莲。"
    show wyh_wnf_b1 b1 b1_sp1
    play voice "voice/万夜花/1305370.ogg"
    wyh "......至今为止？"
    play voice "voice/神野大和/1801680.ogg"
    dh "啊，至今为止。"
    hide wyh_wnf_b1
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/1703730.ogg"
    ts_lian "准确来说，她们现在的目标并不是我......因为她们瞄准的是观景台。"
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305380.ogg"
    wyh "这么说你也遇到过星天宫的巫女了？"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801690.ogg"
    dh "好像是莲在观景台附近发现的。"
    hide dh_zf_b1
    hide wyh_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/1703740.ogg"
    ts_lian "那个时候多亏了我一边隐藏气息一边发出脚步声，把她们都吓跑了。"
    hide ts_lian_ssz_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/万夜花/1305390.ogg"
    wyh "星天宫的主业，讨伐不从之神——祟，终归是不太想被人目击的工作。所以莲的判断是正确的。"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.45
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801700.ogg"
    dh "听当时的情况，那个巫女的目标似乎是观景台的死神。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305400.ogg"
    wyh "观景台的死神我听水之濑报告过。那个指的就是莲吧？"
    play voice "voice/万夜花/1305410.ogg"
    wyh "我没有向星天宫报告任何有关莲的事情。以前没有，现在也没有这个打算。"
    play voice "voice/万夜花/1305420.ogg"
    wyh "所以这件事我自然也是装作不知道的。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/1801710.ogg"
    dh "等等，我想你是误会了些什么。"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/1305430.ogg"
    wyh "什么意思？"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/1801720.ogg"
    dh "观景台的死神不是莲，是一位名叫“雷亚”的少女。"
    show wyh_wnf_b1 b1 b1_sp1
    play voice "voice/万夜花/1305440.ogg"
    wyh "......那是谁？"
    hide dh_zf_b1
    hide wyh_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/1703760.ogg"
    ts_lian "我自己也去了一次，是一个非常让人火大的小孩子......"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_ga3 onlayer m2:
        xpos 0.25
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801730.ogg"
    dh "把她当作是莲的同类会比较合适。"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/1703770.ogg"
    ts_lian "虽然我不是外星人，不过可以这么认为。"
    hide dh_zf_b1
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305450.ogg"
    wyh "观景台的死神名叫雷亚，她的真实身份其实是星之使。你是这么认为的吗？"
    play voice "voice/天使莲/1703780.ogg"
    ts_lian "我和大和君是这样觉得的。"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/1305460.ogg"
    wyh "怎么这样啊，这样一来这座樱华镇不就聚集了三位天使了吗......"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801750.ogg"
    dh "说不定这片土地上还有我们尚未发现的陨石。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/1305480.ogg"
    wyh "我到底当了一个什么地区的神官啊......"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/1801760.ogg"
    dh "对于这点我深表同情。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/1703790.ogg"
    ts_lian "对那个将善良的我们当成邪祟处理的星天宫也没什么值得同情的。"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/1305490.ogg"
    wyh "你们来找我不会就是为了说些讽刺的话吧......"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1801770.ogg"
    dh "我只是来打听关于讨伐观景台死神的巫女而已。"
    play voice "voice/神野大和/1801780.ogg"
    dh "毕竟这说不定也会牵连到莲。"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/1703800.ogg"
    ts_lian "我即使不用大和君来保护也没问题的。"
    hide wyh_wnf_b1
    $ flcam.move(-3200, -200, 600, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/1801790.ogg"
    dh "别这么说嘛~"
    show ts_lian_ssz_b1 b1 b1_ga2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/天使莲/1703810.ogg"
    ts_lian "啊，不要摸我的头......"
    hide ts_lian_ssz_b1
    hide dh_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/万夜花/1305500.ogg"
    wyh "本以为观景台的死神指的就是莲。听到水之濑的报告之后我就让她放着不管了。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305510.ogg"
    wyh "所以关于你说的那位巫女我也不清楚。"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801800.ogg"
    dh "但不管怎么样对方都是星天宫的巫女没错吧？"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/1305520.ogg"
    wyh "恐怕跟水之濑一样是{encyclopedia=zbs}总本社{/encyclopedia}的成员。也有可能是水之濑背着我向总本社报告了观景台死神的情报。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305530.ogg"
    wyh "亦或者这位巫女，是因为其他什么目的才被派来的。"
    hide wyh_wnf_b1
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/1703820.ogg"
    ts_lian "除了讨伐我和观景台的死神之外，还有什么其他可能的原因吗？"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    show wyh_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305540.ogg"
    wyh "还有一个。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1801810.ogg"
    dh "是什么？"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305550.ogg"
    wyh "我们社的小铃。"
    show dh_zf_b1 b1 b1_sp1
    play voice "voice/神野大和/1801820.ogg"
    dh "......"
    hide dh_zf_b1
    hide ts_lian_ssz_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/1305560.ogg"
    wyh "小铃对星天宫而言也一直是个大问题。借助吞噬天使之力的{encyclopedia=lingji}灵基{/encyclopedia}成为刑部巫女，这样的先例之前也都没有发生过。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305570.ogg"
    wyh "到目前为止星天宫还是决定静观其变，甚至将小铃交给我处理。"
    play voice "voice/万夜花/1305580.ogg"
    wyh "表面上是为了帮我镇压凭依在小铃身上的天使，星天宫才将水之濑派来的，但私底下她们想要肃清的态度还是没有改变。倒不如说反而更加明确了。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/1305590.ogg"
    wyh "但是到了今天这个地步我们也早就改变主意了。他们会采取这样的行动也是可以理解的。"
    show wyh_wnf_b1 b1 b1_a1
    play voice "voice/万夜花/1305600.ogg"
    wyh "毕竟水之濑主动选择放弃了这份委托。"
    play voice "voice/万夜花/1305610.ogg"
    wyh "因为她无法对小铃下手。"
    hide wyh_wnf_b1 
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/神野大和/1801830.ogg"
    dh "......确实，从理论上都说得通了。"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/天使莲/1703830.ogg"
    ts_lian "如果是身为总本社的巫女也无法送还不从之神的话，将其视为威胁也不是没有道理。"
    hide ts_lian_ssz_b1
    hide dh_zf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/万夜花/1305620.ogg"
    wyh "也许是误以为小铃是用武力才导致现在这种局面的。但事实明明是恰恰相反的，他们这群人还真是木头脑袋啊。"
    show wyh_wnf_b1 b1 b1_a1
    play voice "voice/万夜花/1305630.ogg"
    wyh "而且也不通知我就送巫女过来，想必是不想多费口舌了。"
    show dh_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801840.ogg"
    dh "{rb}诹访{/rb}{rt}水之濑的代号{/rt}她的态度虽然很高傲，但她其实也是我很看重的学生。她现在怎么样了？"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/1305640.ogg"
    wyh "虽然她说要向星天宫谢罪，但我还是把她留了下来。毕竟如果就这样回去的话很可能再也回不来了。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305650.ogg"
    wyh "如果对方的目标真是小铃的话，那我今后也一直把她留在身边算了。本来我也想要一个保镖的。"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/1801850.ogg"
    dh "虽然这件事情上我本不该插嘴，但如果需要我帮忙的话尽管开口。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1305660.ogg"
    wyh "真打起来的话比起老师，莲反而更有用吧......"
    hide wyh_wnf_b1
    hide dh_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/1703840.ogg"
    ts_lian "如果你希望的话，我现在就去用镰刀狠狠地教训那个邪恶的巫女。"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801860.ogg"
    dh "到那时你可是真成大家眼里的不从之神了啊。"
    show ts_lian_ssz_b1 b1 b1_ga1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/天使莲/1703850.ogg"
    ts_lian "那就用刀柄狠狠地敲她脑袋。"
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305670.ogg"
    wyh "啊哈哈，到那时就拜托你了~"
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/1801870.ogg"
    dh "可以的话希望可以不用动手就让那位巫女回去啊。"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/1305680.ogg"
    wyh "派遣来的巫女是谁都还不知道呢，现在也无法下结论。"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/1703860.ogg"
    ts_lian "以上，我们要说的事情就是这些。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1801880.ogg"
    dh "总之就是不要掉以轻心。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305690.ogg"
    wyh "毕竟是我自己惹的麻烦，所以我会尽量不给你们添麻烦的。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/1801890.ogg"
    dh "虽然不能说让你放手去干，但要是能帮上忙的话我们都会尽力的。怎么说你也是我可爱的学生啊。"
    show wyh_wnf_b1 b1 b1_ga2
    play voice "voice/万夜花/1305700.ogg"
    wyh "都这个岁数了还被那么称呼真有点不是滋味呢......"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/1801900.ogg"
    dh "晚上来打扰真是抱歉，万夜花。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1305710.ogg"
    wyh "这就回去了？起码陪我喝两杯啊。"
    hide dh_zf_b1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/1703870.ogg"
    ts_lian "我不擅长喝酒......"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/1305720.ogg"
    wyh "明明也算是个神明，真是不争气啊。"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/1703880.ogg"
    ts_lian "真是失礼，让人火大。"
    show wyh_wnf_b1 b1 b1_ga2
    play voice "voice/万夜花/1305730.ogg"
    wyh "啊哈哈，虽然已经相识这么久了，但还是觉得你的存在真是不可思议啊。"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801910.ogg"
    dh "对于星天宫的神官来说，这种说法还真是奇怪。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1305740.ogg"
    wyh "我本来就是现实主义者嘛，小铃和小翔也是。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/1801920.ogg"
    dh "即使讨厌星天宫，却也还是想让她们来继承神社吗。"
    show wyh_wnf_b1 b1 b1_h1
    play voice "voice/万夜花/1305750.ogg"
    wyh "因为我也很喜欢这样的不可思议大冒险啊~"
    show dh_zf_b1 b1 b1_ga2
    play voice "voice/神野大和/1801930.ogg"
    dh "别玩火上身了，小心哪天会遭报应的。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305760.ogg"
    wyh "话说莲的身世还是没有办法知道吗？"
    hide dh_zf_b1
    hide wyh_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/1703900.ogg"
    ts_lian "就像你们人类无法完全明白自己生命的起源一样，我的情况也是这么回事。"
    hide ts_lian_ssz_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/万夜花/1305770.ogg"
    wyh "老师你对于莲了解多少？"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1801940.ogg"
    dh "这个嘛。你也知道我们人类之所以能看见东西是需要借助光的吧？"
    show wyh_wnf_b1 b1 b1_s1
    play voice "voice/万夜花/1305780.ogg"
    wyh "那肯定的，黑漆漆的话什么都看不见了。"
    show wyh_wnf_b1 b1 b1_n2
    play voice "voice/万夜花/1305790.ogg"
    wyh "而星天宫也同样是借助了採物的光，才能窥见天使的存在。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1801950.ogg"
    dh "那你知道人类是利用电磁波才能观察到黑暗的宇宙吗？这是关乎电波天文学和重力天文学的领域。"
    show wyh_wnf_b1 b1 b1_ga1
    play voice "voice/万夜花/1305800.ogg"
    wyh "那种东西我才不知道呢......"
    hide wyh_wnf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/1801960.ogg"
    dh "我们想要看见什么、察觉什么，是需要依赖以光为媒介的电磁波。"
    play voice "voice/神野大和/1801970.ogg"
    dh "但现在的天文观测，还无法使用电磁波的全域波长。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1801980.ogg"
    dh "理由很简单，即使想用也用不了。"
    play voice "voice/神野大和/1801990.ogg"
    dh "我们还不知道电磁波的全貌，因为剩下的部分还在研究当中。"
    play voice "voice/神野大和/1802000.ogg"
    dh "所以宇宙现在还有很多尚未解开的谜团。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/1802010.ogg"
    dh "我想莲就是其中之一。之所以有的人看得见而有些人看不见，就是这么回事。"
    play voice "voice/神野大和/1802020.ogg"
    dh "就像是科学是有极限的一样，我们的视觉亦是如此。"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/1802030.ogg"
    dh "因为对宇宙的观测有着局限，所以我们所能观测到的莲也是“有限的”。"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/1802040.ogg"
    dh "而想要真正观测到莲的本质，单纯依靠三次元的情报是远远不够的。"
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305810.ogg"
    wyh "等等......请再说得通俗易懂些。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1802050.ogg"
    dh "听好了，简单来说莲是属于比我们更高维度的存在。"
    hide wyh_wnf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/1802060.ogg"
    dh "目前对于次元的解释是多样的，但简而言之就是{rb}物理量的坐标{/rb}{rt}测度{/rt}。次元的差别体现就是坐标轴的差异。"
    play voice "voice/神野大和/1802080.ogg"
    dh "莲和我们不同，不会被三次元的物理法则所束缚。"
    show dh_zf_b1 b1 b1_n3
    play voice "voice/神野大和/1802090.ogg"
    dh "虽然低次元的存在目前是无法干涉高次元的，但相反高次元的存在却可以干涉到低次元。（注释：低维存在相当于高维空间中的低维流型，就像平面中的点一样难以被察觉）"
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305820.ogg"
    wyh "......果然还是不明白，这是什么工程科学啊。"
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/1802120.ogg"
    dh "是普通的现代物理学范畴。"
    show wyh_wnf_b1 b1 b1_a1
    play voice "voice/万夜花/1305830.ogg"
    wyh "就因为这样我才讨厌你们学者啊。"
    show dh_zf_b1 b1 b1_ga3
    play voice "voice/神野大和/1802140.ogg"
    dh "你还是跟以前一样的不讲情面啊，不管是动手还是动嘴。"
    hide dh_zf_b1 
    hide wyh_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/1703910.ogg"
    ts_lian "虽然我不是很清楚大和君说的电磁波，但是在宇宙中的确充满着很多的能量体。"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/1703920.ogg"
    ts_lian "大和君身上携带着的陨石碎片，应该也充斥着那股能量。"
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/神野大和/1802150.ogg"
    dh "没错。念波和可视光线、红外线、紫外线、X射线、γ射线这样的电磁波是一样的。"
    play voice "voice/神野大和/1802160.ogg"
    dh "在宇宙中，包括这些在内的高能量射线都在不停地照射着周围的天体。"
    play voice "voice/神野大和/1802170.ogg"
    dh "在那之中，就有我们所不知道的光。"
    show dh_zf_b1 b1 b1_n2
    play voice "voice/神野大和/1802180.ogg"
    dh "如果那些在宇宙中旅行了很长时间的陨石，孕育着新的光而降临到地球上来的话。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only items necklace
    with in2out_v2_slow
    pause 2.0 hard
    show dh_zf_b1 b1 b1_n1 onlayer screens at side_right('dh', 0.90), basicfade
    play voice "voice/神野大和/1802190.ogg"
    dh "我们就能依靠这个察觉到莲的存在。"
    play voice "voice/神野大和/1802200.ogg"
    dh "因为都受到陨石所携带的宇宙射线影响。所以我们能够看见一般情况下看不见的存在。"
    show dh_zf_b1 b1 b1_s1
    play voice "voice/神野大和/1802210.ogg"
    dh "寄宿在这颗陨石上的光，借由这份羁绊便能够呈现在我们眼前了。"
    hide dh_zf_b1
    pause 1.0 hard
    scene set only party front
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/神野大和/1802220.ogg"
    dh "这就是主张用科学而不是超自然现象去解释的，我的看法。"
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305850.ogg"
    wyh "简直就像是天象仪一样呢。"
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/1802230.ogg"
    dh "本来这些陨石就是星星的投影机。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1305860.ogg"
    wyh "但是不仅能看见还能过触摸，莲果然是不可思议的存在。"
    $ flcam.move(0, 250, 650, duration=1.5)
    show ts_lian_ssz_b1 b1 b1_ga2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    pause 0.5 hard
    play voice "voice/天使莲/1703930.ogg"
    ts_lian "啊，不要摸我的头......"
    play voice "voice/万夜花/1305870.ogg"
    wyh "不仅是我们能触摸到，莲也能触摸到我们。"
    show dh_zf_b1 b1 b1_n1
    play voice "voice/神野大和/1802240.ogg"
    dh "这是因为未知的光并不局限于我们的视线。其他的感观，甚至对于万物而言都有所影响。"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/1305880.ogg"
    wyh "虽然站在星天宫干部的立场上，我有着将莲视为邪祟镇压的责任。"
    show wyh_wnf_b1 b1 b1_h1
    play voice "voice/万夜花/1305890.ogg"
    wyh "但无论如何你们也都是我作为天文部成员最重要的伙伴啊。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1305900.ogg"
    wyh "无论你是多么难以理解、多么不可思议的存在，但你都是我的朋友。"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/1703940.ogg"
    ts_lian "......"
    hide wyh_wnf_b1
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show dh_zf_b1 b1 b1_h1
    play voice "voice/神野大和/1802250.ogg"
    dh "这份害羞感觉不错呢~"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/1703950.ogg"
    ts_lian "才、才没有害羞......"
    pause 0.5 hard
    show wyh_wnf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/万夜花/1305910.ogg"
    wyh "啊哈哈，好久没尝试过了，干脆大家一起去天体观测吧？"
    show wyh_wnf_b1 b1 b1_s2
    play voice "voice/万夜花/1305920.ogg"
    wyh "虽然想要召集当时的天文部全员似乎是非常困难的。"
    show wyh_wnf_b1 b1 b1_n1
    play voice "voice/万夜花/1305940.ogg"
    wyh "但即使看不见对方，我相信他们也一定还在某个地方。"
    show wyh_wnf_b1 b1 b1_h1
    play voice "voice/万夜花/1305950.ogg"
    wyh "也在和我们一起，仰望着樱华镇的星空吧——"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 3.0 hard

label day12.starview_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 2.0 hard
    play music first_27 fadein 3.0 if_changed
    "吃过晚饭后，我和往常一样朝着观景台的方向走去。"
    "一路上我反复思考着过去的{rb}我{/rb}{rt}boku{/rt}。"
    "翔子是我第一个朋友，无论是对于现在的我还是小时候的神野凉而言都一样。"
    "初夏的夜晚，我都会和翔子一起在观景台玩耍。"
    "可是跟翔子的第一次见面，却是要追溯到更早以前。"
    pause 1.0 hard
    scene set only starview night road
    with dissolve
    pause 1.0 hard
    "那次邂逅，是在一个樱花盛开的春天。"
    "那时的我——"
    pause 1.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 4.0 hard
    "交朋友并不是一件重要的事项。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day past yinghua
    with dissolve
    pause 1.0 hard
    "这就是国小时的我。"
    "每天放学后的第一件事就是直接回家。"
    "对于同学们的邀请我一向都是拒绝的。"
    "比起这些，我有更重要的事情要做。"
    "因为比起朋友，家人在我的心中更加重要。"
    "由于父母工作的关系，我频繁地搬家。"
    "也因此我的身边没有朋友。"
    "我唯一的目标就是尽我一切努力去减轻父母的负担。"
    "因为我知道想要撑起一个三口之家是多么地不容易。"
    "所以我想至少要帮忙做点家务。"
    "这样的话，母亲也会很高兴的。"
    "除此之外我也会努力完成自己的学业。"
    "每一次考试拿到满分的话，母亲也会很高兴。"
    "这些全都是好事。"
    "所以我从来没有想过要去改变什么。"
    "我觉得这样的生活已经足够幸福了。"
    "与“她”的邂逅，就是在这样不断循环着的日子里。"
    "那一天，我跟往常一样踏上了回家的路。"
    stop music fadeout 5.0
    $ flcam.move(0, -300, 900, duration=8.0, warper='ease_cubic')
    pause 4.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        1.0
        linear 1.25 alpha 1
    pause 3.0 hard
    play music first_36 fadein 3.0 if_changed
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_memory normal one
    with slowerdissolve
    pause 3.0 hard
    "一位女孩站在校门口。"
    "目不转睛地盯着校舍的方向发呆。"
    "周围没有一个人。"
    "一般这个时候同学们都会选择留在教室里和朋友们一起嬉戏玩耍。"
    "所以此刻在这里的，只有我和她。"
    "以及那些在风中轻舞飘散的花瓣。"
    play voice "voice/翔子/0606620.ogg"
    tiny_xz "这就是、分别。"
    play voice "voice/翔子/0606630.ogg"
    tiny_xz "和学校的、分别......"
    "她向前张开手臂。"
    "就像是想要悉数接住那些落下的花瓣一般。"
    pause 0.1 hard
    scene set only xz_memory normal two
    with dissolve
    play voice "voice/翔子/0606640.ogg"
    tiny_xz "我想再最后来道一次别。"
    pause 0.1 hard
    scene set only xz_memory normal one
    with dissolve
    $ flcam.move(750, -1500, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0606650.ogg"
    tiny_xz "你喜欢学校吗？"
    me01 "不太喜欢。"
    play voice "voice/翔子/0606660.ogg"
    tiny_xz "那你讨厌学校吗？"
    me01 "也不讨厌。"
    play voice "voice/翔子/0606670.ogg"
    tiny_xz "是吗......"
    play voice "voice/翔子/0606680.ogg"
    tiny_xz "你对学校漠不关心啊。"
    "漠不关心，这对小孩子来说是很难的成语，她好像也是思索了片刻之后才想出起来的。"
    "就像是在假装大人一样。"
    "为什么我会停下脚步呢？"
    "为什么我会和不认识的人说话呢？"
    play voice "voice/翔子/0606690.ogg"
    tiny_xz "你是这里的学生对吧？"
    me01 "嗯。"
    play voice "voice/翔子/0606700.ogg"
    tiny_xz "几年级？"
    me01 "四年级。"
    "为什么我会回答她呢？"
    "大概是因为在漫天飞舞的樱花之中，女孩的身影显得十分美丽吧。"
    "也许是因为我被迷住了，所以才迟迟没有离开吧。"
    play voice "voice/翔子/0606710.ogg"
    tiny_xz "你的名字是？"
    me01 "这和你没关系吧。"
    play voice "voice/翔子/0606730.ogg"
    tiny_xz "你的名字，叫什么呢？"
    me01 "都说了跟你没关系。"
    play voice "voice/翔子/0606740.ogg"
    tiny_xz "你喜欢樱花吗？"
    me01 "你问这个做什么？"
    play voice "voice/翔子/0606750.ogg"
    tiny_xz "你觉得我妨碍到你了吗？"
    me01 "这都无所谓的吧。"
    play voice "voice/翔子/0606760.ogg"
    tiny_xz "是吗......"
    play voice "voice/翔子/0606770.ogg"
    tiny_xz "你对我也是漠不关心呢。"
    "我觉得不是的。"
    "如果是漠不关心的话，我早就已经离开了。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0606780.ogg"
    tiny_xz "这里的樱花真多啊。花瓣就像是雪一样飘落、堆积起来。"
    play voice "voice/翔子/0606800.ogg"
    tiny_xz "多到让人觉得忧伤。"
    play voice "voice/翔子/0606810.ogg"
    tiny_xz "也许你可能觉得，不管是樱花、还是现在的我，都只会让人觉得忧伤而已吧。"
    me01 "你喜欢樱花吗？"
    play voice "voice/翔子/0606820.ogg"
    tiny_xz "喜欢。"
    play voice "voice/翔子/0606830.ogg"
    tiny_xz "初开的樱花，我很喜欢。"
    play voice "voice/翔子/0606840.ogg"
    tiny_xz "但是凋零的樱花，我却不喜欢......"
    "樱花在开花后的一周之内就会达到顶盛，之后等待着它的只有凋零。"
    "这就是，{rb}春之花{/rb}{rt}S p r i n g  E p h e m e r a l{/rt}。（注释：春季短生植物）"
    "春天里短暂的生命。"
    pause 0.1 hard
    scene set only xz_memory normal two
    with dissolve
    play voice "voice/翔子/0606850.ogg"
    tiny_xz "短暂的生命，我不喜欢。"
    play voice "voice/翔子/0606860.ogg"
    tiny_xz "短暂的美好，我不明白。"
    me01 "我也......不喜欢。"
    me01 "我也觉得，初开时的樱花更好。"
    me01 "一直都盛开着就更好了。"
    me01 "毕竟要打扫飘落的樱花是件很麻烦的事。"
    play voice "voice/翔子/0606870.ogg"
    tiny_xz "......"
    pause 0.1 hard
    scene set only xz_memory normal three
    with dissolve
    $ flcam.move(750, -1500, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0606880.ogg"
    tiny_xz "嗯。"
    "她冲我笑了笑。"
    "那笑容宛如这盛开着的樱花那般美丽。"
    play voice "voice/翔子/0606890.ogg"
    tiny_xz "是呢。就是这样的。"
    play voice "voice/翔子/0606900.ogg"
    tiny_xz "但是呢，就算春之花凋零了。"
    pause 0.1 hard
    scene set only xz_memory normal four
    with dissolve
    $ flcam.move(1500, -2000, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0606910.ogg"
    tiny_xz "到了夏天的时候，{rb}夏之花{/rb}{rt}S u m m e r  E p h e m e r a l{/rt}就会盛开了哟~"
    play voice "voice/翔子/0606920.ogg"
    tiny_xz "就如同是结束了，却又没有结束。就像是改变了，却又没有改变一样。"
    play voice "voice/翔子/0606930.ogg"
    tiny_xz "有些东西无论何时都不会改变，都会永远地存在下去。"
    play voice "voice/翔子/0606940.ogg"
    tiny_xz "而我们，也都身在其中。"
    pause 0.1 hard
    scene set only xz_memory normal three
    with dissolve
    play voice "voice/翔子/0606950.ogg"
    tiny_xz "如果能告诉我名字的话，我会很开心的。"
    me01 "神野凉。"
    play voice "voice/翔子/0606960.ogg"
    tiny_xz "谢谢你，凉君。"
    play voice "voice/翔子/0606970.ogg"
    tiny_xz "能够遇到你，我很高兴。"
    play voice "voice/翔子/0606980.ogg"
    tiny_xz "如果还能再见面的话，我会更高兴的。"
    play voice "voice/翔子/0606990.ogg"
    tiny_xz "想要和我玩的话，随时都可以跟我说哟。"
    play voice "voice/翔子/0607000.ogg"
    tiny_xz "因为，我喜欢和你在一起。"
    play voice "voice/翔子/0607010.ogg"
    tiny_xz "这一定是永远也不会改变的东西。"
    pause 0.1 hard
    scene set only xz_memory normal four
    with dissolve
    play voice "voice/翔子/0607020.ogg"
    tiny_xz "因为，我喜欢你~"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day past yinghua
    with dissolve
    pause 1.0 hard
    "说完，她离开了。"
    "并没有告诉我她的年龄和名字。"
    "所以我没有办法自己去找她。"
    "如果她不来找我的话，我们就不会再见面了。"
    pause 1.0 hard
    scene white
    with dissolve
    pause 1.0 hard
    "在那之后，每次一个人回家的途中，我都会注意着四周。"
    "注意着那个女孩的身影。"
    "是不是又会再一次沐浴在某处的落樱之中。"
    "然而尽管我百般等待，她却始终没有再来找我。"
    "几次偶然在街上遇到的时候，我也总会犹豫要不要上前搭话。"
    "而每次她都会主动地接近我。"
    "摆出一副姐姐的样子，邀请我和她一起玩。"
    "最开始的时候我是拒绝的，就如同对待其他同学们的做法一样，以一副冷漠的态度回应。"
    "但每次分开之后，我又会期待着与她的相遇。"
    "因为我不知道该说什么才好。"
    "因为我不知道该用什么样的方式和她相处。"
    "就这样重复着见面与分别。"
    "但是同时我们之间的对话也渐渐多了起来。"
    "我的态度也渐渐缓和了。"
    "偶尔也会接受她的邀请。"
    "就这样持续了一段时间后，某一天的晚上，她把我叫到了观景台。"
    "在我的额头上吻了一下。"
    "从那以后每当放学我都会到观景台去。"
    "甚至有时也有过不回家直接过去的情况。"
    "而她也总是会在那里等我。"
    "太阳下山之前，我们总会在一起玩耍。"
    pause 1.0 hard
    scene set only xz_cg kiss 
    with in2out_v2_slow
    pause 3.0 hard
    "是的。"
    "所以过去的{rb}我{/rb}{rt}boku{/rt}喜欢上了她。"
    "不知从何时起，我在她的面前变得温顺了。"
    "不知从何时起，我在她的面前露出了只会对家人展露的一面。"
    "和她的邂逅。"
    "被她东拉西扯的日子。"
    "这段时光的终点，是因为我的搬家。"
    "从那以后，我不再摆出冷漠的态度，变得能和别人正常交流了。"
    "不再拒绝别人的邀请了。"
    "偶尔也会和朋友们一起，甚至主动邀请大家一起玩了。"
    "虽然并没有放弃家务和功课。"
    "但是除了家人之外，我也找到了其他活着的意义了。"
    "变得能够喜欢上家人以外的人了。"
    "多亏了她，我的世界变得更广阔了。"
    "是她教会了我仰望宇宙的方法。"
    pause 1.0 hard
    scene white
    with dissolve
    pause 2.0 hard
    "和她一起仰望过的、樱华镇的星空，今晚也依旧闪耀着那永恒不变的光辉——"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/0018340.ogg"
    lst "今晚也来看星星了吗。"
    pause 1.0 hard
    scene set only lisite_cg normal
    with slowdissolve
    pause 2.0 hard
    play music first_31 fadein 3.0 if_changed
    me01 "还在想今晚能不能见到你呢。"
    play voice "voice/天使雷亚/0018350.ogg"
    lst "......是吗。"
    me01 "怎么了，无精打采的？"
    pause 0.1 hard
    scene set only lisite_cg shy
    with dissolve
    play voice "voice/天使雷亚/0018360.ogg"
    lst "没什么......"
    me01 "有什么心事吗？"
    play voice "voice/天使雷亚/0018370.ogg"
    lst "没什么。"
    me01 "是吗。"
    play voice "voice/天使雷亚/0018380.ogg"
    lst "嗯。"
    "我走到雷亚的身边，俯身靠在栏杆上。"
    "静静地看着眼前交织的星光。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0018390.ogg"
    lst "怎么了？"
    me01 "你指什么？"
    play voice "voice/天使雷亚/0018400.ogg"
    lst "今晚的你也是废废的呢。"
    me01 "哪里废了啊。"
    play voice "voice/天使雷亚/0018410.ogg"
    lst "因为你总是一副废废的而且笨笨的表情。"
    me01 "我有露出那么不堪的表情吗......"
    play voice "voice/天使雷亚/0018420.ogg"
    lst "嗯。"
    me01 "雷亚你觉得人是孤独的吗？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0018430.ogg"
    lst "......诶？"
    me01 "不只是人。雷亚你是死神吧。"
    me01 "你觉得死神也是孤独的吗？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0018440.ogg"
    lst "死神才不会孤独呢。"
    me01 "是吗。毕竟在那之前还有过和谁的约定吗。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0018450.ogg"
    lst "嗯。"
    "眼前的光辉，星星和月亮，以及城镇上的灯火。"
    "那些熙攘的光，虽然看起来是相依相融，但是其实却相隔遥远。"
    "光芒之间，隔着广阔、黑暗宇宙空间。"
    play voice "voice/天使雷亚/0018460.ogg"
    lst "人......是孤独的吗？"
    me01 "虽然看起来很近，实际上却相隔很远。但尽管如此人也并不是孤独的。"
    play voice "voice/天使雷亚/0018470.ogg"
    lst "什么意思？"
    me01 "就好比即使我和“她”曾经分开了，但还是能再见面的。"
    play voice "voice/天使雷亚/0018480.ogg"
    lst "你是来秀恩爱吗......"
    me01 "是啊，本来应该是个浪漫的爱情故事呢。"
    me01 "但如果加入了失恋这个结局，也实在是很遗憾啊。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0018490.ogg"
    lst "......"
    me01 "我喜欢翔子。她是我第一个朋友，我很感谢她让我的世界变得广阔了。"
    me01 "所以我向她告白了。但结果却被甩了。"
    me01 "虽然被甩了应该是很痛苦的。"
    me01 "但即使不能成为恋人，我还是很开心能和她再会。"
    me01 "她也说我是她最好的朋友，这点我非常开心。"
    me01 "明明应该是，很开心的事情......"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only starview night starview
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    me01 "呐，雷亚。"
    me01 "这到底是什么？"
    me01 "不是爱情吗？"
    me01 "还是说，这是别的什么......"
    show ts_lst_ssz_b2 b2 b2_s3
    play voice "voice/天使雷亚/0018500.ogg"
    lst "我不知道。"
    me01 "说了奇怪的话，抱歉。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0018510.ogg"
    lst "嗯。"
    show ts_lst_ssz_b1 b1 b1_n2
    play voice "voice/天使雷亚/0018520.ogg"
    lst "但是，梦甩了你这件事，我也能理解。"
    show ts_lst_ssz_b1 b1 b1_s3
    play voice "voice/天使雷亚/0018530.ogg"
    lst "因为我，和她也有过约定。"
    play voice "voice/天使雷亚/0018540.ogg"
    lst "她希望你能够忘记她。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0018550.ogg"
    lst "所以我才一直在这里等你。"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0018560.ogg"
    lst "一直一直，都在观景台等着你。"
    show ts_lst_ssz_b2 b2 b2_s3
    play voice "voice/天使雷亚/0018570.ogg"
    lst "虽然不能确信凉君的噩梦是否就是与她有关。"
    play voice "voice/天使雷亚/0018580.ogg"
    lst "甚至事后凉君你会不会忘记有关她的哪些事情，我也无从知晓。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0018590.ogg"
    lst "但是我能做到的，就只有割取你的噩梦而已。"
    show ts_lst_ssz_b1 b1 b1_n2
    play voice "voice/天使雷亚/0018600.ogg"
    lst "所以我，才会用镰刀刺向你的。"
    me01 "......原来是这样啊。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0018610.ogg"
    lst "嗯。"
    me01 "雷亚你早已经和翔子见过面了吗。"
    me01 "明明许下了再会的约定。"
    me01 "但是翔子她，其实是不希望再会的啊。"
    me01 "原来......是这样吗。"
    me01 "原来我从一开始就被甩了的。"
    "我守护了七年的这份思念，在七年前就已经崩塌了。"
    "翔子会禁止我去探病就是因为这样，会装作忘记我的事情也是这样的。"
    "这么想的话，一切都可以得到解释了。"
    show ts_lst_ssz_b1 b1 b1_s3
    play voice "voice/天使雷亚/0018630.ogg"
    lst "要不要再一次割去噩梦呢？"
    play voice "voice/天使雷亚/0018640.ogg"
    lst "要不要我帮你带走你这份感情呢？"
    play voice "voice/天使雷亚/0018650.ogg"
    lst "要不要让我帮你消去......这份痛苦呢？"
    me01 "不......"
    show ts_lst_ssz_b1 b1 b1_n2
    play voice "voice/天使雷亚/0018660.ogg"
    lst "这样可以吗？"
    me01 "嗯。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0018670.ogg"
    lst "为什么？"
    me01 "不为什么。"
    show ts_lst_ssz_b1 b1 b1_s3
    play voice "voice/天使雷亚/0018680.ogg"
    lst "可你明明这么痛苦。"
    me01 "即使这样。"
    play voice "voice/天使雷亚/0018690.ogg"
    lst "你明明这么悲伤的......"
    me01 "虽然很悲伤，但是我并不想这样就丢掉一切。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0018700.ogg"
    lst "我不明白。"
    me01 "我自己也不是很明白。"
    show ts_lst_ssz_b1 b1 b1_s3
    play voice "voice/天使雷亚/0018710.ogg"
    lst "那......到底要怎么做才好呢？"
    play voice "voice/天使雷亚/0018720.ogg"
    lst "我到底该怎么做，才能帮助凉君呢......"
    me01 "你愿意帮助我吗？"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0018730.ogg"
    lst "也不是。"
    me01 "你愿意安慰我吗？"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0018740.ogg"
    lst "......也不是。"
    me01 "可以摸你的头吗？"
    show ts_lst_ssz_b2 b2 b2_a1
    play voice "voice/天使雷亚/0018750.ogg"
    lst "为什么会变成这样啊。"
    me01 "我只是觉得摸了雷亚的头说不定就会变得有精神的。"
    show ts_lst_ssz_b2 b2 b2_ga1
    play voice "voice/天使雷亚/0018760.ogg"
    lst "......那是什么原理？"
    me01 "就是这样的。"
    show ts_lst_ssz_b2 b2 b2_s3
    play voice "voice/天使雷亚/0018770.ogg"
    lst "真的吗？"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0018780.ogg"
    lst "真的，会有精神吗？"
    me01 "嗯。"
    show ts_lst_ssz_b1 b1 b1_s1
    play voice "voice/天使雷亚/0018790.ogg"
    lst "凉君，会变回平时的样子吗？"
    me01 "嗯。"
    play voice "voice/天使雷亚/0018800.ogg"
    lst "......"
    $ flcam.move(0, -350, 1000, duration=1.5)
    pause 0.5 hard
    stop music fadeout 5.0
    show ts_lst_ssz_b1 b1 b1_s3
    play voice "voice/天使雷亚/0018810.ogg"
    lst "那么......可以的。"
    play voice "voice/天使雷亚/0018820.ogg"
    lst "可以摸。"
    play voice "voice/天使雷亚/0018830.ogg"
    lst "可以，让你摸我的头。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg head shy
    with in2out_v2_slow
    play music first_29 fadein 3.0 if_changed
    pause 2.0 hard
    "我轻轻地抚摸着雷亚的头。"
    "已经记不清是第几次了。但雷亚还是没有习惯，看起来十分地紧张和抗拒。"
    pause 0.1 hard
    scene set only lisite_cg head sad
    with dissolve
    play voice "voice/天使雷亚/0018840.ogg"
    lst "有精神了吗？"
    me01 "嗯。"
    play voice "voice/天使雷亚/0018850.ogg"
    lst "变回平时的凉君了吗？"
    me01 "嗯。"
    play voice "voice/天使雷亚/0018860.ogg"
    lst "那......"
    me01 "这次可以抱你吗？"
    play voice "voice/天使雷亚/0018870.ogg"
    lst "......"
    play voice "voice/天使雷亚/0018880.ogg"
    lst "为什么？"
    me01 "因为这样我一定会更有精神的。"
    play voice "voice/天使雷亚/0018890.ogg"
    lst "不......"
    me01 "不行吗？"
    play voice "voice/天使雷亚/0018900.ogg"
    lst "嗯。"
    me01 "可是我真的很想抱你。"
    play voice "voice/天使雷亚/0018910.ogg"
    lst "绝对不要！"
    play voice "voice/天使雷亚/0018920.ogg"
    lst "因为，比起被摸头，这么做会让我的心情变得奇怪的。"
    play voice "voice/天使雷亚/0018940.ogg"
    lst "所以不要。"
    me01 "那真是遗憾。"
    play voice "voice/天使雷亚/0018950.ogg"
    lst "凉君也是，经历过的话就会明白的。"
    me01 "是什么样的心情？"
    play voice "voice/天使雷亚/0018960.ogg"
    lst "很奇怪的心情。"
    me01 "如果是我不知道的心情的话，我也想经历一次。"
    play voice "voice/天使雷亚/0018970.ogg"
    lst "那样的话......"
    "雷亚好像想到了什么。"
    $ flcam.move(1500, -1000, 300, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0018980.ogg"
    lst "如果心情变得奇怪的话......凉君就不会痛苦了吗？"
    play voice "voice/天使雷亚/0018990.ogg"
    lst "就像我这样，如果心情变得奇怪了的话，就不会感到悲伤了吗？"
    me01 "不试试看的话我也不知道。"
    play voice "voice/天使雷亚/0019000.ogg"
    lst "因为凉君你总是笨笨的。"
    play voice "voice/天使雷亚/0019010.ogg"
    lst "这样的凉君让我也开始变得笨笨的了......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 1.0 hard
    "雷亚站到了栏杆上。"
    "她那幼小的身体，朝着我的方向倾斜着。"
    pause 1.0 hard
    scene white
    with slowdissolve
    pause 2.0 hard
    play voice "voice/天使雷亚/0019020.ogg"
    lst "死神本来，是不会做这种事的——"
    pause 1.0 hard
    scene set only lisite_cg kiss
    with cent2side
    pause 2.0 hard
    "她吻了我的额头。"
    "就像七年前道别的时候一样。"
    "嘴唇那温柔的触感。"
    "一瞬间，将我的回忆唤醒了。"
    "但是，和那时不同。"
    "现在的我已经成长了。"
    "现在的我已经不再是小孩子了。"
    "已经经历过失去的我，已经不再是对恋爱生疏的小孩子了。"
    "就像眼前的雷亚与“她”不同一样。"
    "现在的{rb}我{/rb}{rt}ore{/rt}和过去的{rb}我{/rb}{rt}boku{/rt}也已然不同了。"
    $ flcam.move(1000, -1500, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "回忆依旧是回忆，仍是我最为珍贵的东西。"
    "但是时候也差不多，该继续向前迈进了。"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 3.0 hard
    stop music fadeout 5.0
    scene black
    with slowdissolve
    pause 3.0 hard

label day12.hospital_event02:
    $ flcam.move(0, 0, 0)
    scene set only hospital night room yinghua
    with slowdissolve
    pause 1.0 hard
    "病房里的电源被切断了。医院已经到了熄灯的时间。"
    "女孩坐在床上眺望着窗外。"
    play music first_27 fadein 3.0 if_changed
    pause 1.0 hard
    scene set only beach night yinghua2
    with dissolve
    pause 1.0 hard
    "夜色中的大海。"
    "潮起潮落的海浪声。"
    "就像闪烁的星光一般重复着。"
    pause 1.0 hard
    scene set only hospital night room yinghua
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yume_sy_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0607030.ogg"
    yume "那么......就这样晚安吧。"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    "因为害怕闭上眼睛，所以在自然入睡之前她都会一直盯着天花板看。"
    "星光从窗户照射进屋内。"
    "四周都被染上了同样的颜色。"
    "为这早已厌倦了的房间填上了几分色彩。"
    "也因为这样，回忆也渐渐清晰了起来——"
    pause 1.0 hard
    scene white
    with dissolve
    pause 2.0 hard
    "在即将升入高年级的那个春天，女孩就再也没有去过学校。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day past yinghua
    with in2out_v2_slow
    pause 2.0 hard
    "虽然在此之前也经常缺席过，但那对于女孩而言却是家常便饭。"
    "因为身体的缘故，从小体弱多病的她和班上的同学一起上课的时间是很少的，所以想要融入这个环境也非常困难。"
    "退学对她而言也只是时间问题。"
    "即使这样，女孩还是坚持要去学校。"
    "因为她喜欢学校。"
    "喜欢食堂的炸面包。"
    "虽然上学对她而言会对身体造成负担，但只要和大家待在一起就会觉得有意义。"
    "女孩不想退学。"
    "不想因为自己虚弱的身体而变得和别人不一样，她不想孤独一人。"
    "不想放弃这普通的生活，因为对他而言恰恰这份普通才是最美好的。"
    "明明只要能普通地学习、普通地玩耍，就已经很满足了。"
    "但是，偶尔身体缺恙的时候还是只能留在家里让奶奶代为照顾。"
    "没关系，学习的话有身为家庭教师的奶奶在就可以了。"
    "那一天，女孩最后一次去了学校。"
    pause 1.0 hard
    scene set only xz_memory normal one
    with dissolve
    pause 1.0 hard
    "在那时遇见的男孩，就是他。"
    "他说他叫“神野凉”。因为年纪比自己小的缘故，女孩就称他为凉君。"
    "他是个不喜欢笑，态度有些冷漠，和别人保持着距离的孤僻少年。"
    "和女孩不同的是。"
    "他并不讨厌孤独，甚至自己选择了孤身一人。"
    play voice "voice/翔子/0607040.ogg"
    tiny_xz "你喜欢樱花吗？"
    me01 "你问这个做什么？"
    play voice "voice/翔子/0607050.ogg"
    tiny_xz "你觉得我妨碍到你了吗？"
    me01 "这都无所谓的吧。"
    play voice "voice/翔子/0607060.ogg"
    tiny_xz "是吗......"
    play voice "voice/翔子/0607070.ogg"
    tiny_xz "你对我也是漠不关心呢。"
    "对什么事都漠不关心的他。"
    "却让女孩也是很羡慕。"
    "如果能像他一样的话，就不会变成这样了吧。"
    "如果能够对一切漠不关心——如果能让自己对学校的事情漠不关心的话，就不会有现在这样寂寞的心情了吧。"
    "所以......"
    "让我变得讨厌学校就好了。"
    "痛苦也是，悲伤也是，后悔也是，已经不想再体会这些了。"
    "而相对的，就让他变得对学校感兴趣吧。"
    "就让他来实现，我无法达成的愿望吧——"
    pause 0.1 hard
    scene set only xz_memory normal three
    with dissolve
    $ flcam.move(750, -1500, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0607080.ogg"
    tiny_xz "谢谢你，凉君。"
    play voice "voice/翔子/0607090.ogg"
    tiny_xz "能够遇到你，我很高兴。"
    play voice "voice/翔子/0607100.ogg"
    tiny_xz "如果还能再见面的话，我会更高兴的。"
    play voice "voice/翔子/0607110.ogg"
    tiny_xz "想要和我玩的话，随时都可以跟我说哟。"
    play voice "voice/翔子/0607120.ogg"
    tiny_xz "因为，我喜欢和你在一起。"
    "他也能为了我发自内心地欢笑吗？"
    "他也能为了我从此摆脱孤独吗？"
    "他也能为了我继续留在这里吗？"
    "他也能代替我守护我所爱的一切吗......"
    play voice "voice/翔子/0607130.ogg"
    tiny_xz "这一定是永远也不会改变的东西。"
    pause 0.1 hard
    scene set only xz_memory normal four
    with dissolve
    play voice "voice/翔子/0607140.ogg"
    tiny_xz "因为，我喜欢你~"
    pause 1.0 hard
    scene white
    with dissolve
    pause 2.0 hard
    "在那之后，女孩并没有老老实实地在家养病，而是经常瞒着家人跑出来。"
    "女孩走到街上，寻找着少年的身影。"
    "找到他并不难，甚至比想象中的要容易得多。"
    "也许是因为对方也在寻找自己的缘故。"
    "只要算好放学的时间在校门口附近等着的话，就经常能够遇到。"
    "但是即使遇见了，他也从不主动来找自己搭话。"
    "即使如此，女孩还是会选择和他一起玩耍。"
    "对任何事情都漠不关心的他，女孩相信自己会是特别的。"
    pause 1.0 hard
    scene set only xz_cg kiss
    with dissolve
    pause 1.0 hard  
    "就这样，两人的距离逐渐拉近。"
    "之后女孩第一次带少年去了观景台。"
    "在那里，女孩吻了他的额头。"
    "因为觉得害羞，所以丢下他一个人回去了。"
    "回家的时候还发烧了，在床上睡了好长一段时间。"
    "在那之后，观景台就成了彼此约定见面的场所。"
    "女孩没有告诉他关于自己的秘密。因为她希望对方能把自己当成普通的女孩子一样看待。"
    "因为两人已经是朋友了。"
    "因为朋友就是能够一起度过平凡的每一天的关系——"
    pause 1.0 hard
    scene white 
    with dissolve
    pause 2.0 hard
    "而那份普通却以他的搬家结束了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua
    with dissolve
    pause 1.0 hard
    "在那之后女孩的身体情况恶化了。"
    "到头来还是没有办法摆脱寂寞。"
    "其实自己早就明白的。"
    "也正因为如此女孩才没有将联系方式告诉给少年。"
    "因为她自己也无法保证是否还能够再见面。"
    "即使对方要求了，却也回绝了。"
    pause 1.0 hard
    scene set only sky evening yinghua
    with dissolve
    pause 1.0 hard
    "从那以后的每一天，女孩虽然生活在病痛的折磨中，却没有流过泪。"
    "因为眼泪已经在离别的那一刻为少年流干了。"
    "那么至少，在离开前留下自己最后的心愿吧。"
    pause 1.0 hard
    scene set only sky night yinghua2
    with dissolve
    pause 1.0 hard
    "再会的话，就等到自己的身体痊愈了。"
    "等到自己变回普通人的时候。"
    "这是女孩的第一个愿望。"
    "如若不然。"
    "就让他忘记这一切吧。"
    "忘记那份曾经一起嬉戏打闹的时光。"
    "回到真正属于他的、平凡的生活中去吧。"
    "这是女孩的第二个愿望。"
    pause 1.0 hard
    scene white
    with slowdissolve
    pause 2.0 hard
    "如果就这么去了另一个世界的话。"
    "女孩希望是在这片曾经和少年一起度过美好时光的土地上。"
    "明明曾经是为了不再寂寞，所以才结识了少年的。"
    "但是造化弄人，到头来还是要一个人孤独地离开。"
    "这到底是什么呢？"
    "明明想要待在谁的身边，却不得不选择离开。"
    pause 1.0 hard
    scene set only beach night yinghua2
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0607150.ogg"
    yume "所以，我才禁止你来探病了。"
    play voice "voice/翔子/0607160.ogg"
    yume "因为我不想让你困扰。"
    play voice "voice/翔子/0607170.ogg"
    yume "如果结局是注定了的话，我倒是希望能走得更干脆一点啊。"
    play voice "voice/翔子/0607180.ogg"
    yume "干脆得，让我没有时间去后悔......"
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 900)
    scene set only hospital night room yinghua
    show ts_lst_ssz_b1_d b1 b1_n2 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/天使雷亚/0020550.ogg"
    lst "那么，要不要试试看呢？"
    play voice "voice/翔子/0607190.ogg"
    yume "......"
    play music first_28 fadein 3.0 if_changed
    play voice "voice/天使雷亚/0020560.ogg"
    lst "要干脆得，让你没有时间去后悔地替你割去吗？"
    pause 0.5 hard
    show yume_sy_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0607200.ogg"
    yume "......谁、谁？"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0020570.ogg"
    lst "雷亚。这还是第一次告诉你我的名字。"
    hide yume_sy_b1
    show yume_sy_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607210.ogg"
    yume "......诶？"
    show ts_lst_ssz_b2 b2 b2_n1
    play voice "voice/天使雷亚/0020580.ogg"
    lst "虽然并不是第一次见面了，但是以这副姿态出现在你面前却还是第一次。"
    play voice "voice/翔子/0607220.ogg"
    yume "诶，什么？"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1_d b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0020590.ogg"
    lst "你不明白的话也好。"
    hide yume_sy_b2
    show yume_sy_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607230.ogg"
    yume "难道你是......死神吗？"
    show ts_lst_ssz_b1 b1 b1_n2
    play voice "voice/天使雷亚/0020600.ogg"
    lst "是的，我是死神。"
    show yume_sy_b1 b1 b1_n2
    play voice "voice/翔子/0607240.ogg"
    yume "你是来......割取我的生命吗？"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0020610.ogg"
    lst "我是割取噩梦的死神。所以，只要你的噩梦不是生命本身就不会被割去。"
    play voice "voice/天使雷亚/0020620.ogg"
    lst "但是，也许还有试一试的价值。"
    show yume_sy_b1 b1 b1_sp1
    play voice "voice/翔子/0607250.ogg"
    yume "......要试吗？"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1_d b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0020630.ogg"
    lst "你再这样下去的话，凉君会生气的。"
    hide yume_sy_b1
    show yume_sy_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607260.ogg"
    yume "......你是凉君的朋友吗？"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0020640.ogg"
    lst "比起这个。"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0020650.ogg"
    lst "本来如果你睡着的话，我是打算叫醒你的。但你醒着的话就没问题了。"
    show yume_sy_b2 b2 b2_n2
    play voice "voice/翔子/0607270.ogg"
    yume "那个......你是？"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/0020660.ogg"
    lst "因为这里离观景台太远了，所以不能待太久。"
    show ts_lst_ssz_b2 b2 b2_n2
    play voice "voice/天使雷亚/0020670.ogg"
    lst "所以，我只说一遍。"
    hide yume_sy_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1_d b1 b1_n2 onlayer m2:
        xpos 0.5
        0.15
        easein 1.25 alpha 0.8
        0.15
        easein 1.25 alpha 0.4
        repeat
    play voice "voice/天使雷亚/0020680.ogg"
    lst "如果让凉君伤心的话，我会毫不犹豫地将镰刀挥向你的。"
    pause 0.5 hard
    play sound xiaoshi_1
    show ts_lst_ssz_b1_d b1 b1_n2:
        xpos 0.5
        0.75
        easein 1.25 alpha 0.0
    pause 4.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yume_sy_b2 b2 b2_s3 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/0607280.ogg"
    yume "这到底是怎么回事......"
    "出现也是，消失也是。"
    "都是在自己毫无察觉的情况下发生的。"
    "简直就像是......"
    "家庭教师的妖精先生一样。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    $ suppress_overlay = True
    jump day13
