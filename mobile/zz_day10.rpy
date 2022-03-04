label day10:
    bookmark
    $ save_name = _("Day 10")
    pause 4.0 hard
    scene set only backend_yinghua autumn
    with dissolve
    show backend_bg03 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date09 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    $ suppress_overlay = False
    scene set only school day road yinghua
    with dissolve
    pause 2.0 hard
    scene set only school day room2 yinghua
    with dissolve
    pause 1.0 hard
    play music first_05 fadein 3.0 if_changed
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/一诚总司/1606280.ogg"
    yczs "也就是说，你已经找到寻觅已久的初恋对象了？"
    me01 "虽然其中还有一些无法解释的东西，不过差不多是这样的。"
    me01 "名字的话......叫{encyclopedia=yume}梦{/encyclopedia}。"
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0140780.ogg"
    rxl "成功再会了啊~"
    play voice "voice/青木铃音/0533680.ogg"
    lingyin "我们的帮忙也算有价值了。"
    show yczs_dzf_b1 b1 b1_n1
    play voice "voice/一诚总司/1606290.ogg"
    yczs "虽然我什么都没做，但是这样不是也很好吗。"
    hide rxl_dzf_b1
    hide lingyin_dzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_s2
    play voice "voice/一诚总司/1606300.ogg"
    yczs "神野都完成了自己的再会了。我也必须加油才行啊。（小声）"
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0140790.ogg"
    rxl "一诚君身边也有分隔两地的幼女吗？"
    show yczs_dzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1606310.ogg"
    yczs "虽然是幼女，但是别把我和神野混为一谈。"
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533690.ogg"
    lingyin "是以前一起玩的女孩子吗？"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/1606320.ogg"
    yczs "虽然也可以这么说，但是和神野不同并不是初恋的对象。"
    me01 "为什么要拿我作比较啊。"
    hide lingyin_dzf_b2
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_sp1
    play voice "voice/日向怜/0140800.ogg"
    rxl "一诚君也在找人吗？"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/1606330.ogg"
    yczs "算是吧。"
    show rxl_dzf_b2 b2 b2_n1 
    play voice "voice/日向怜/0140810.ogg"
    rxl "是什么样的女孩子呢？"
    show yczs_dzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1606340.ogg"
    yczs "......比起我，日向亲不是更应该在意梦的事情吗？"
    stop music fadeout 5.0
    hide rxl_dzf_b2
    show rxl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140820.ogg"
    rxl "我才没有！"
    show yczs_dzf_b1 b1 b1_a1
    play voice "voice/一诚总司/1606350.ogg"
    yczs "不用勉强，真不像你啊。"
    show rxl_dzf_b3 b3 b3_n2
    play voice "voice/日向怜/0140830.ogg"
    rxl "你才是，多管闲事的一点也不像一诚君！"
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533700.ogg"
    lingyin "一诚同学也是，如果需要的话我们也会帮忙一起找的哟~"
    show yczs_dzf_b1 b1 b1_n1
    play voice "voice/一诚总司/1606360.ogg"
    yczs "不、我这边已经有人帮忙了。"
    hide lingyin_dzf_b2
    hide rxl_dzf_b3
    hide yczs_dzf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    "一诚总司站了起来。"
    "就像是在说着“不要再问了”似的走出了教室。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140840.ogg"
    rxl "......还是不要再追问下去比较好。"
    pause 0.5 hard
    play music first_04 fadein 3.0 if_changed
    show lingyin_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533710.ogg"
    lingyin "神野同学，今天也要去探病吗？"
    me01 "嗯。放学后就去。"
    hide lingyin_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_dzf_b3
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140850.ogg"
    rxl "那么小凉，给~"
    $ flcam.move(1500, -200, 600, duration=1.5)
    show rxl_dzf_b2 b2 b2_n1 at flu_down(0.15, 30):
        xpos 0.5
    show lihe onlayer m2 at item_7to6:
        xpos 0.6
    pause 1.0 hard
    "日向怜从书包里拿出了一个包裹。"
    play voice "voice/日向怜/0140860.ogg"
    rxl "慰问品。和梦一起吃吧。"
    me01 "真的可以吗？"
    show rxl_dzf_b2 b2 b2_h1
    play voice "voice/日向怜/0140870.ogg"
    rxl "嗯，当然了~"
    hide lihe
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140880.ogg"
    rxl "梦是小凉的朋友的话，也是我们的朋友嘛~"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black
    with dissolve
    pause 2.0 hard

label day10.hospital_event01:
    $ flcam.move(0, 0, 0)
    scene set only hospital day outside
    with dissolve
    pause 3.0 hard
    scene set only hospital day room yinghua
    with dissolve
    pause 3.0 hard
    play music first_42 fadein 3.0 if_changed
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "不睡觉没关系吗？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_cg hsp normal
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0602930.ogg"
    yume "嗯。因为我现在很精神啊。"
    me01 "如果真如你所说就不至于待在医院里了。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0602940.ogg"
    yume "也是呢~"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0602950.ogg"
    yume "大家都太认真了。本来也没有那么严重的。"
    play voice "voice/翔子/0602960.ogg"
    yume "真想快点从软禁状态解放出来啊。凉君也帮我去求求医生吧？"
    me01 "等你恢复到不用住院的程度再说吧。"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0602970.ogg"
    yume "......明明我是真的很精神啊。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0602990.ogg"
    yume "你又来探望了呢。"
    me01 "我来的话会有什么困扰吗？"
    play voice "voice/翔子/0603000.ogg"
    yume "不太好哟。嗯，不太好。"
    me01 "如果你讨厌的话我就不来了。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0603010.ogg"
    yume "开玩笑的啦。嗯，开玩笑的。"
    play voice "voice/翔子/0603020.ogg"
    yume "你不要那么消沉嘛。"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0603040.ogg"
    yume "年轻的住院患者很少见吧？"
    play voice "voice/翔子/0603050.ogg"
    yume "除我以外的患者，大多都是老爷爷或者老奶奶。你也知道的吧？"
    me01 "嗯，从我朋友那里听说了。"
    play voice "voice/翔子/0603060.ogg"
    yume "是青木医生的女儿？"
    me01 "你认识她们？"
    "一般来说处于不同时空的“自己”能够察觉的另一方的存在吗......"
    "这一切果然很奇怪。"
    play voice "voice/翔子/0603070.ogg"
    yume "我呢，到中央大楼去的时候，爷爷奶奶们总是会来和我搭话。大家都很喜欢聊天呢~"
    play voice "voice/翔子/0603080.ogg"
    yume "这个我倒不是很讨厌。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603090.ogg"
    yume "但是，和凉君聊天我觉得更开心。"
    play voice "voice/翔子/0603100.ogg"
    yume "也就是说，我是希望凉君你来探病的哟~"
    me01 "真的吗？"
    play voice "voice/翔子/0603110.ogg"
    yume "真的。"
    me01 "你想起以前的事情了？"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0603120.ogg"
    yume "这个和那个是两回事。凉君你有时候真是坏心眼呢。"
    me01 "诱导审问的事情真的抱歉。"
    play voice "voice/翔子/0603130.ogg"
    yume "你真的觉得抱歉吗？"
    me01 "嗯，作为道歉我带了礼物来。"
    "我从包里拿出了日向怜给我的礼盒。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0603140.ogg"
    yume "给我的？"
    me01 "嗯。大家说了，给“梦”的。"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0603150.ogg"
    yume "竟然随便给我起绰号。"
    me01 "以前是叫你姐姐的吧？"
    play voice "voice/翔子/0603160.ogg"
    yume "是啊，是以前的话肯定也会叫“梦”姐姐......"
    me01 "你刚刚你说了“以前”吧？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603170.ogg"
    yume "没那回事哟。嗯，没那回事。"
    pause 0.1 hard
    scene set only xz_cg hsp angry
    with dissolve
    play voice "voice/翔子/0603180.ogg"
    yume "话说回来，诱导审问......"
    me01 "刚才的不算。"
    play voice "voice/翔子/0603190.ogg"
    yume "真的吗？"
    me01 "这些是一位名叫日向怜的同班同学让我拿给你的。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603200.ogg"
    yume "是朋友做的啊~"
    me01 "嗯。"
    play voice "voice/翔子/0603210.ogg"
    yume "对方是女孩子吧？"
    me01 "嗯。"
    play voice "voice/翔子/0603220.ogg"
    yume "凉君，变成优等生了呢。"
    play voice "voice/翔子/0603230.ogg"
    yume "凉君你如果你想吃的话就吃吧。"
    me01 "那你呢？"
    play voice "voice/翔子/0603240.ogg"
    yume "我现在肚子还不饿。"
    me01 "那就待会儿再吃吧。"
    "我把包裹放在了桌上。"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0603250.ogg"
    yume "不用在意我你就吃吧。"
    me01 "可是这是特地留给翔子你的啊。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603260.ogg"
    yume "但是你女朋友做的吧？"
    me01 "不，日向同学只是我的朋友而已。"
    play voice "voice/翔子/0603270.ogg"
    yume "明明不用掩饰也可以的......"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0603280.ogg"
    yume "凉君果然还不是优等生啊。看来和我想的还有些差距。"
    me01 "如果不是优等生的话会怎么样？"
    play voice "voice/翔子/0603290.ogg"
    yume "那凉君就不可以来探望我了。"
    me01 "为什么？"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603300.ogg"
    yume "凉君，你不打算交女朋友吗？"
    play voice "voice/翔子/0603310.ogg"
    yume "没有喜欢的女孩子吗？"
    me01 "如果我说有呢？"
    play voice "voice/翔子/0603320.ogg"
    yume "那凉君就可以继续来探望我了~"
    me01 "我有一个问题。"
    play voice "voice/翔子/0603330.ogg"
    yume "请吧，我允许了。"
    me01 "如果、我是说如果，我喜欢的女孩子是翔子你的话？"
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    $ flcam.move(-1500, -2000, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0603340.ogg"
    yume "......那样的话，会是件很遗憾的事情。"
    me01 "有多遗憾？"
    play voice "voice/翔子/0603350.ogg"
    yume "对凉君来说就像是人生中第一次不及格那么严重的程度。"
    me01 "但是，我已经有过不及格的体验了。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0603360.ogg"
    yume "诶？真的吗？"
    me01 "嗯。"
    play voice "voice/翔子/0603370.ogg"
    yume "凉君，以前明明对学习很在行啊。"
    me01 "因为现在的我已经成长了。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603380.ogg"
    yume "已经不再是书呆子了吗？"
    me01 "嗯。"
    play voice "voice/翔子/0603390.ogg"
    yume "夏夜的女王是什么？"
    me01 "七夕的织女星。"
    play voice "voice/翔子/0603400.ogg"
    yume "你这不是完全没有变嘛~"
    me01 "虽然不算是诱导审问，但是翔子你好像对我的过去很了解啊。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0603170.ogg"
    yume "没那回事哟。嗯，没那回事。"
    me01 "要说对七夕的了解我觉得自己还是比较在行的。"
    play voice "voice/翔子/0603410.ogg"
    yume "为什么？"
    me01 "因为你的缘故。"
    play voice "voice/翔子/0603420.ogg"
    yume "别把错误推给别人啊。"
    me01 "不是的，刚刚那是在夸你吧。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603430.ogg"
    yume "据说织女星呢，一直都在慢慢地移动着，在一万两千年后会取代现在北极星的位置。"
    play voice "voice/翔子/0603440.ogg"
    yume "虽然我觉得成为群星的中心是一件很棒的事情。"
    play voice "voice/翔子/0603450.ogg"
    yume "但那样的话和牛郎星的距离就更远了，要见面的话就会更困难了。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0603460.ogg"
    yume "对织女星唯命是从的牛郎星，最后也许就会选择放弃了吧。"
    "她这么说着，有些寂寞地笑了起来。"
    me01 "对于星星，你似乎已经比我更加了解了。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603470.ogg"
    yume "即使是住在医院里，我也是在学习的。但是比起学校这里学习的也只是很小的一部分。"
    play voice "voice/翔子/0603490.ogg"
    yume "但是呢，即使不去上学也没有关系的。因为我有两位家庭教师~"
    me01 "家庭教师？"
    play voice "voice/翔子/0603500.ogg"
    yume "嗯。我说想要了解有关星星的知识，所以他们两位就负责教我了。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    me01 "你的家庭教师，是什么样的人呢？"
    play voice "voice/翔子/0603510.ogg"
    yume "其中一个是我的祖母。她是一个非常注重礼节而且博学的人，平时我都会叫她奶奶。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0603520.ogg"
    yume "虽然今年春天的时候她已经去世了。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603530.ogg"
    yume "所以呢，浪漫的星座神话是奶奶教给我的。"
    play voice "voice/翔子/0603540.ogg"
    yume "而更加科学的知识，是妖精先生教给我的。"
    me01 "妖精先生？"
    play voice "voice/翔子/0603570.ogg"
    yume "我和妖精先生是在樱华镇认识的，现在也会经常到病房来。他教给我的是和奶奶完全不同的内容。"
    me01 "也就是说我不是唯一一个来探望你的吗？"
    play voice "voice/翔子/0603580.ogg"
    yume "妖精先生并不是来探望的，毕竟是家庭教师嘛。"
    me01 "就是那位妖精先生交给你关于星星的天文知识？"
    play voice "voice/翔子/0603590.ogg"
    yume "嗯。"
    me01 "我也想见一次啊。"
    play voice "voice/翔子/0603600.ogg"
    yume "妖精先生只有被选中的人才能遇见，所以可能会很困难。"
    stop music fadeout 5.0
    me01 "那......"
    "我犹豫了片刻。"
    me01 "我可以再来吗？"
    play music first_29 fadein 3.0 if_changed
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0603610.ogg"
    yume "嗯，可以哟~"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603620.ogg"
    yume "因为我相信凉君是可以成为优等生的。"
    me01 "明天也是、后天也是，每一天都可以来吗？"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0603630.ogg"
    yume "毕竟我现在是被禁足了的。所以随时都可以哟~"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0603640.ogg"
    yume "啊、但是，出去检查的时候可能不在。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0603650.ogg"
    yume "那个时候就在这里等我就可以了，不会花很长时间的。"
    me01 "我知道了。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0603660.ogg"
    yume "嗯，跟以前一样温顺真是不错~"
    me01 "你肯定是想起来什么了吧？"
    play voice "voice/翔子/0603670.ogg"
    yume "没有想起来哟。嗯，没有想起来~"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard

label day10.starview_event01:
    scene set only starview night starview
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "呐，雷亚。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg surprise
    with in2out_v2_slow
    pause 2.0 hard
    play music first_42 fadein 3.0 if_changed
    play voice "voice/天使雷亚/0016910.ogg"
    lst "什么？"
    me01 "雷亚你几岁了？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0016920.ogg"
    lst "死神才没有年龄呢。"
    me01 "你就告诉我吧。"
    play voice "voice/天使雷亚/0016930.ogg"
    lst "我不是说过没有年龄了吗。"
    me01 "我无论如何都想要知道。"
    play voice "voice/天使雷亚/0016940.ogg"
    lst "都说了没有......"
    me01 "那雷亚你是从什么时候起开始来观景台的呢？"
    play voice "voice/天使雷亚/0016950.ogg"
    lst "很久以前。"
    me01 "何年何月？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0016960.ogg"
    lst "那种事情我不记得了。"
    me01 "这只是个假设，如果我和雷亚开始交往的话......"
    scene set only lisite_cg angry
    $ flcam.move(2200, -2800, 900, duration=0.5, warper='ease_quad')
    play sound punch
    show wflash onlayer f1
    with vpunch
    stop music fadeout 5.0
    "{size=72}咚！！{/size}"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    with right2left
    pause 1.0 hard
    play music first_13 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1_d b1 b1_a2 onlayer m2:
        xpos 0.5
    me01 "你干什么啊！"
    show ts_lst_ssz_b1_d b1 b1_s2
    play voice "voice/天使雷亚/0016970.ogg"
    lst "因为你说了奇怪的东西。"
    me01 "我说了是假设吧？"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0016980.ogg"
    lst "但是......总觉得就是想敲你。"
    show ts_lst_ssz_b1_d b1 b1_s3
    play voice "voice/天使雷亚/0016990.ogg"
    lst "这种感觉到底是什么？"
    me01 "是恋爱吧。"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0017000.ogg"
    lst "我觉得是杀人的冲动。"
    me01 "我开玩笑的，别把镰刀举起来啊！"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0017010.ogg"
    lst "今晚的你也是笨笨的呢。"
    me01 "那么，回到刚才那个假设上来。"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0017020.ogg"
    lst "还要继续啊......"
    me01 "你觉得假如我和雷亚开始交往了的话，我是不是就变成萝莉控了？"
    show ts_lst_ssz_b2_d b2 b2_s1
    play voice "voice/天使雷亚/0017030.ogg"
    lst "不会的。"
    show ts_lst_ssz_b2_d b2 b2_n2
    play voice "voice/天使雷亚/0017040.ogg"
    lst "如果和凉君交往的话，我就变成正太控了。"
    show ts_lst_ssz_b2_d b2 b2_n1
    play voice "voice/天使雷亚/0017050.ogg"
    lst "因为我比凉君要成熟得多~"
    me01 "世人的观点怎么看都是和你相反的吧。"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0017060.ogg"
    lst "因为人的眼睛能看到的是有限的，所以也是没有办法。大家都无法捕捉到事物的本质呢。"
    me01 "那雷亚的本质是？"
    show ts_lst_ssz_b1_d b1 b1_h1
    play voice "voice/天使雷亚/0017070.ogg"
    lst "成熟的大姐姐。"
    me01 "{size=72}噗哈哈哈哈！{/size}"
    $ flcam.move(0, -350, 1000, duration=1.5)
    play sound punch
    show wflash onlayer f1
    show ts_lst_ssz_b1_d b1 b1_a2
    with vpunch
    "{size=72}咚！！！{/size}"
    pause 0.5 hard
    me01 "好痛！"
    stop music fadeout 5.0
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0017080.ogg"
    lst "然后，凉君是个一点都不可爱的小屁孩。"
    me01 "随你怎么说好了。"
    show ts_lst_ssz_b2_d b2 b2_n2
    play voice "voice/天使雷亚/0017090.ogg"
    lst "这是事实。"
    me01 "雷亚能够捕捉到人的本质吗？"
    play music first_27 fadein 3.0 if_changed
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0017100.ogg"
    lst "因为我是死神。"
    me01 "死神的眼睛还真是好用啊。"
    show ts_lst_ssz_b1_d b1 b1_n1
    play voice "voice/天使雷亚/0017110.ogg"
    lst "我觉得至少比凉君的好用。"
    me01 "能看到寿命吗？"
    show ts_lst_ssz_b1_d b1 b1_s2
    play voice "voice/天使雷亚/0017120.ogg"
    lst "那种东西看不见的。因为我是割取噩梦的死神。"
    me01 "也就是说能看见噩梦？"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0017130.ogg"
    lst "看不见。"
    me01 "那不是一点用都没有吗！"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0017140.ogg"
    lst "虽然看不见噩梦，但是还是能找到目标。"
    me01 "你自己没有噩梦吗？"
    show ts_lst_ssz_b2_d b2 b2_sp1
    play voice "voice/天使雷亚/0017150.ogg"
    lst "诶？"
    me01 "雷亚你自己，不会像我们一样做梦吗？"
    show ts_lst_ssz_b2_d b2 b2_s4
    play voice "voice/天使雷亚/0017160.ogg"
    lst "不知道。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    show ts_lst_ssz_b2 b2 b2_n2 onlayer screens at side_right('ts_lst', 0.9), basicfade
    play voice "voice/天使雷亚/0017170.ogg"
    lst "死神，虽然能割取人的噩梦。"
    play voice "voice/天使雷亚/0017180.ogg"
    lst "但却无法割取死神的噩梦。"
    show ts_lst_ssz_b2 b2 b2_s3
    play voice "voice/天使雷亚/0017190.ogg"
    lst "因为死神，有着比梦更加重要的东西。"
    play voice "voice/天使雷亚/0017200.ogg"
    lst "那就是与约定之人许下的承诺。"
    hide ts_lst_ssz_b2
    pause 1.0 hard
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    $ suppress_overlay = True
    jump day11
