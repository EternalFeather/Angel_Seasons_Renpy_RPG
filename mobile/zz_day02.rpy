label day02:
    bookmark
    $ save_name = _("Day 02")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_yinghua spring
    with dissolve
    show backend_bg01 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date01 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    $ flcam.move(0, 0, 0)
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only school day gate yinghua
    with slowdissolve
    pause 1.0 hard
    "今天是转学过来的第一天。"
    "看了一眼时间，马上就到早会的时间了，必须抓紧点才行。"
    play ambience1 run_1 noloop
    $ flcam.move(1000, 1800, 1500, duration=2.0, warper='easeout_quint')
    pause 1.5 hard
    scene black
    with dissolve
    $ flcam.move(0, 0, 0)
    play music first_08 fadein 3.0 if_changed
    pause 2.0 hard
    scene set only school day road yinghua
    with slowdissolve
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.5 hard
    "教务室在校舍的一楼。"
    "由于是插班生的缘故，我需要先去和新的老师还有同学们打声招呼。"
    "简单地递交了入学材料之后，我跟着老师的步伐一起迈向了位于三楼的教室。"
    pause 0.5 hard
    scene set only school day corridor yinghua
    with right2left
    "楼道里很宽敞，充满了校园青春的气息。"
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.5 hard
    "根据我的了解，接下来通常就是展开自我介绍的剧情桥段。"
    pause 0.5 hard
    scene black
    with dissolve
    pause 1.0 hard
    "深呼吸。"
    me01 "不振作一点可不行。"
    stop music fadeout 5.0
    "在这里退缩的话会被“她”嘲笑的。"
    pause 1.0 hard

label day02.school_event01:
    play ambience1 open_door noloop
    pause 3.0 hard
    $ flcam.move(3300, -900, 1100)
    scene set only school day room yinghua
    with cent2side
    pause 1.0 hard
    $ flcam.move(-3400, -900, 1100, duration=3.0)
    pause 3.0 hard
    play music first_17 fadein 3.0 if_changed
    "与我脑中的画面略有差异，此刻教室里弥漫着一股严肃的气氛。"
    "视线从四面八方袭来，最终停留在了我的身上。"
    "原本安静的教室片刻间便被各种细微的议论声充斥着。"
    "这也算正常，毕竟在这个时间点突然转学总会让人有种格格不入的感觉。"
    pause 0.5 hard
    scene black
    with dissolve
    pause 1.0 hard
    "虽然也知道他们并没有恶意。"
    "但即使如此我的内心还是动摇了。"
    $ flcam.move(0, 0, 0)
    pause 1.0
    scene set only school day room yinghua
    with dissolve
    "老师在黑板上写下我的名字，然后将目光投向我的位置。"
    "终于到这个环节了吗，明明进教室的前一刻我还在预演来着，可此时脑中却是一片空白。"
    "什么都想不起来了。"
    pause 1.0 hard
    scene set only lisite_cg normal
    show sepiagrain onlayer texture
    with dissolve
    "或许是因为昨晚遇到的那名自称“死神”的少女让我这几天都彻夜难眠的关系。"
    "在观景台的那次“重逢”，想要立刻恢复常态也是不可能办到的事情。"
    "况且要是以那家伙与人交流的方式作为这座小镇的平均水准来看，要想快速融入恐怕有些难度的......"
    pause 1.0 hard
    scene set only school day room yinghua
    with dissolve
    "只好硬着头皮上了。"
    "这已经不是我第一次转学。"
    "话说之前我都是怎么介绍自己的呢？"
    "时间一分一秒地流逝。"
    "见我一直没有说话，台下的交流声越发明显了。"
    "不妙啊。"
    "我可不想一开始就被贴上“怪人”的标签。"
    "必须要说点什么，可为什么我的嗓子不听使唤了。"
    "即使下定决心想要改变些什么，可到头来却始终没有勇气迈出那一步。"
    "一直以来我所有的人生轨迹都是遵循着命运的安排向前延续着，那么这一次或许也不例外吧。"
    "我果然......还是一点成长也没有啊。"
    stop music fadeout 2.0
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    show rxl_xzf_b1 b1 b1_h2 onlayer screens at side_left('lingyin'), basicfade
    play voice "voice/日向怜/0100720.ogg"
    stranger "神野同学，加油！"
    hide rxl_xzf_b1
    play music first_13 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_a2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/日向怜/0100730.ogg"
    rxl "大家安静一点啊。神野同学会很困扰的，好好听人家自我介绍啦~"
    "说话的并不是生面孔。"
    "是那天在校门口遇到的其中一位女生。"
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.7)
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0500350.ogg"
    lingyin "身为班长的日向同学都这么说了，大家就安静下来听听神野同学的自我介绍吧。"
    "紧接着在她后座的女生，也是那天在校门口见到的另一位，名叫“青木铃音”的同学也站了起来。"
    "两人冲我点了点头。"
    "是让我不要紧张的意思吗？"
    hide rxl_xzf_b2
    hide lingyin_xzf_b2
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    me01 "我叫神野凉，从今天起就要和大家一起在这里学习了。"
    me01 "今后的日子里还请多多关照。"
    play ambience1 guzhang noloop
    pause 3.0 hard
    "此时台下也传来了热烈的掌声，让我心中的不安顿时消散了。"
    pause 1.0 hard
    scene black
    with dissolve
    stop music fadeout 2.0
    play ambience1 rill noloop
    pause 3.0 hard
    scene set only school day road yinghua
    with dissolve
    "我的座位是后排靠窗的位置。"
    "随着铃声的响起早会也结束了。"
    "距离第一节课还有十分钟左右的休息时间。"
    pause 1.0 hard
    scene set only school day room2 yinghua
    with right2left
    pause 0.5 hard
    play music first_04 fadein 3.0 if_changed
    pause 1.0 hard
    scene set only rxl_cg school smile
    with slowdissolve
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0100740.ogg"
    rxl "吓了我一跳啊神野同学。"
    play voice "voice/日向怜/0100750.ogg"
    rxl "虽然听说有转校生，不过没想到竟然是在我们的班级。"
    me01 "我也吓了一跳，没想到竟然那么快就能再见到日向同学你了。"
    play voice "voice/日向怜/0100760.ogg"
    rxl "世界真是小呢~"
    me01 "刚刚托你的福得救了。"
    pause 0.1 hard
    scene set only rxl_cg school surprise
    with dissolve
    play voice "voice/日向怜/0100770.ogg"
    rxl "你指的是什么？"
    me01 "没事，自言自语而已。"
    pause 0.1 hard
    scene set only rxl_cg school smile
    with dissolve
    play voice "voice/日向怜/0100830.ogg"
    rxl "啊对了对了，有一点我很在意，刚刚听老师说你小学的时候也曾在这座城市待过对吧？"
    me01 "确实是这样没错。"
    pause 0.1 hard
    scene set only rxl_cg school angry
    with dissolve
    $ flcam.move(2200, -1800, 900, duration=2.0, warper='ease_quad')
    pause 2.0 hard
    "她突然探出了身子，仔细打量着我。"
    me01 "怎、怎么了？"
    play voice "voice/日向怜/0100840.ogg"
    rxl "神野同学你，莫非......"
    "这是近得不能再近的距离。"
    "甚至连对方的呼吸都能感觉得到。"
    $ flcam.move(0, -100, 400, duration=1.0, warper='ease_quad')
    pause 1.0 hard
    "我慌忙拉开了距离。"
    "她是近视眼吗？"
    me01 "那个，日向同学？"
    pause 0.1 hard
    scene set only rxl_cg school happy
    with dissolve
    play voice "voice/日向怜/0100850.ogg"
    rxl "叫我怜就行了哟~"
    "女孩微笑着回应道。"
    me01 "那......日向怜同学。"
    pause 0.1 hard
    scene set only rxl_cg school angry2
    with dissolve
    play voice "voice/日向怜/0100860.ogg"
    rxl "真是的，姓氏什么的不用那么麻烦，我们已经是同学了吧？"
    me01 "那......怜同学。"
    pause 0.1 hard
    scene set only rxl_cg school happy
    with dissolve
    play voice "voice/日向怜/0100870.ogg"
    rxl "嗯，小凉~"
    "直呼名讳......还擅自在前面加个“小”字？！"
    me01 "那个，这个称呼果然还是太......"
    pause 0.1 hard
    scene set only rxl_cg school smile
    with dissolve
    play voice "voice/日向怜/0100880.ogg"
    rxl "那......凉君？"
    me01 "我这边也不用敬语的。"
    scene set only rxl_cg school happy
    play voice "voice/日向怜/0100890.ogg"
    rxl "这样的话果然还是有点难为情啊~"
    "明明是你自己要求的吧。"
    stop music fadeout 5.0
    play voice "voice/一诚总司/1600010.ogg"
    stranger "从刚刚就听你们在开心地交谈，莫非你们之前就认识？"
    $ flcam.move(0, 0, 0, duration=1.0, warper='ease_quad')
    pause 1.0 hard
    scene set only school day room2 yinghua
    with dissolve
    pause 1.0 hard
    play music first_05 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    "隔壁座的男生津津有味地欣赏着我们交谈的场景。"
    me01 "因为我之前也曾在这座小镇上生活过一段时间，也许是那时候见过面也说不定。"
    show yczs_xzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1600030.ogg"
    stranger "啊，原来如此~"
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.3)
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0101050.ogg"
    rxl "一诚君没在这里的小学就读过，所以没见过小凉吧？"
    me01 "请多指教~"
    hide rxl_xzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_n1
    play voice "voice/一诚总司/1600050.ogg"
    yczs "但是为何偏偏在这种时候转学过来，明明还有一个月左右就放暑假了。"
    show yczs_xzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1600060.ogg"
    yczs "是有什么秘密吗？"
    pause 0.5 hard
    $ flcam.move(2250, -350, 750, duration=1.5)
    show lingyin_xzf_b1 b1 b1_n2 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/青木铃音/0500360.ogg"
    lingyin "一诚同学，我认为刨根问底是恶趣味哟。如果想要更加了解对方的话，就等到关系更进一步的时候再说吧。"
    hide yczs_xzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0500370.ogg"
    lingyin "我们又见面了呢，转校生同学。之后也请多多指教~"
    me01 "这边才是，请多指教。"
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1600070.ogg"
    yczs "什么嘛？这边也是熟人吗？"
    hide lingyin_xzf_b2
    show lingyin_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0500380.ogg"
    lingyin "稍微见过几面。"
    "“青木”这个姓氏倒是让我有些在意。"
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0500390.ogg"
    lingyin "我和日向同学是同级生，所以像称呼她那样称呼我就行了哟~"
    me01 "我知道了，铃音同学。"
    hide yczs_xzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_s2
    play voice "voice/青木铃音/0500400.ogg"
    lingyin "不能去掉敬语吗？"
    me01 "这......"
    show lingyin_xzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0500410.ogg"
    lingyin "开玩笑的。我与一诚同学一样，和神野同学也不是同一所小学的。"
    hide lingyin_xzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.3
        xzoom -1
    play voice "voice/日向怜/0101070.ogg"
    rxl "但要说先认识小凉的是话是我才对哟。"
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0500420.ogg"
    lingyin "如果是指“搭讪”的话，我想可能不只是日向同学你一人尝试过而已哟~"
    me01 "离开这里已经是很久以前的事了，大家或许也早已经不记得我了。所以论“搭讪”的话日向同学应该算是第一个吧。"
    "虽然在此之前已经和另一个奇怪的女孩碰过面了......"
    hide lingyin_xzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/0101080.ogg"
    rxl "看吧看吧，果然我的特权呢~"
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0500430.ogg"
    lingyin "这里为了神野同学你的名誉着想，我想还是澄清一下比较好。"
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/一诚总司/1600090.ogg"
    yczs "神野，教科书都有了吗？"
    me01 "已经买好了。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
        xzoom -1
    play voice "voice/日向怜/0101090.ogg"
    rxl "哇，新书！真好啊~"
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0500440.ogg"
    lingyin "所有人最开始都是新书吧。"
    show yczs_xzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1600100.ogg"
    yczs "到现在还是新书的话，那人的学习态度就可想而知了。"
    show rxl_xzf_b1 b1 b1_a1
    play voice "voice/日向怜/0101100.ogg"
    rxl "为什么要把我的教科书和小凉的教科书放在一起比较啊！"
    show lingyin_xzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0500450.ogg"
    lingyin "装订得像新的一样反而值得表扬一番呢。毕竟那么爱惜自己的书。"
    show yczs_xzf_b1 b1 b1_h1
    play voice "voice/一诚总司/1600110.ogg"
    yczs "{rb}日向亲{/rb}{rt}昵称{/rt}的教科书外面很新里面反而全是涂鸦呢~"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_a2 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/0101110.ogg"
    rxl "不要擅自看别人的教科书啊！"
    hide lingyin_xzf_b2
    show lingyin_xzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0500460.ogg"
    lingyin "这还真是没救了呢，祥瑞御免恶灵退散。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_c1 onlayer m2:
        xpos 0.3
        xzoom -1
    show han onlayer m2:
        xalign 0.28 yalign 0.37
    play voice "voice/日向怜/0101120.ogg"
    rxl "是朋友的话至少帮我说句话啊！"
    hide han
    hide rxl_xzf_b1
    hide yczs_xzf_b1
    hide lingyin_xzf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    "我一脸苦笑地看着眼前的这群人。"
    "之前进入教室时的不安和紧张感，现在已经完全消失了。"
    "托他们的福，或许我真的能够快速融入这个氛围也说不定呢。"
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.3
        xzoom -1
    play voice "voice/日向怜/0101130.ogg"
    rxl "小凉，来和我交换教科书吧，反正看上去也没什么不同吧？"
    me01 "还是不了，我可不想用夏目漱石的额头上写着“肉”字的教科书。"
    pause 1.0 hard
    scene black
    with dissolve
    stop music fadeout 5.0
    pause 1.0 hard
    play ambience1 rill noloop
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day road yinghua
    with slowdissolve
    pause 2.0 hard
    scene set only school day room2 yinghua
    with right2left
    pause 0.5 hard
    "上午的课程结束了，接下来是午餐时间。"
    "学校食堂是最佳的选择，毕竟价格便宜而且分量也足，再怎么说一个人生活的话开销确实是一个不小的问题。"
    show rxl_xzf_b1 b1 b1_n3 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/0101220.ogg"
    rxl "我说小凉~"
    play music first_04 fadein 3.0 if_changed
    hide rxl_xzf_b1
    pause 1.0 hard
    scene set only rxl_cg school smile
    with dissolve
    play voice "voice/日向怜/0101230.ogg"
    rxl "午饭是去食堂吃对吧？"
    me01 "的确是这样打算的。"
    $ flcam.move(2200, -1800, 900, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    "日向怜再一次把身子凑了过来。"
    "和她说话的时候总有种莫名的尴尬。"
    $ flcam.move(1200, -800, 500, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0101240.ogg"
    rxl "我基本上也是去食堂吃午饭的，虽然我觉得这所学校除了食堂应该就没有其他的选择了。"
    me01 "嘛，毕竟对于学生而言买便当的话太奢侈了。"
    pause 0.1 hard
    scene set only rxl_cg school happy
    with dissolve
    play voice "voice/日向怜/0101250.ogg"
    rxl "学校的消费方式似乎也是自给自足的，虽然不知道什么时候就会变成强制的商业模式。"
    me01 "果然还是去食堂吧，在那里的售票机购买餐券就行了吧？"
    pause 0.1 hard
    scene set only rxl_cg school smile
    with dissolve
    play voice "voice/日向怜/0101270.ogg"
    rxl "嗯，是啊。午饭的话就放在柜台的托盘上，菜式都是自助的。"
    me01 "毕竟每个人喜欢的菜色都不一样。"
    play voice "voice/日向怜/0101280.ogg"
    rxl "嗯。"
    me01 "所以要是不搞自助的话，总有种不人道的感觉。"
    play voice "voice/日向怜/0101290.ogg"
    rxl "这么在意的话，一开始就把钱全部存到售票机里面就好了。"
    me01 "那个食堂，很大吗？"
    play voice "voice/日向怜/0101300.ogg"
    rxl "啊、嗯。即使如此也容纳不下所有的学生，所以有的人会选择去中庭吃饭。"
    play voice "voice/日向怜/0101330.ogg"
    rxl "食堂的位置，还不知道吧？"
    "我摇了摇头。"
    play voice "voice/日向怜/0101340.ogg"
    rxl "那我来给你带路吧~"
    stop music fadeout 3.0
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 2.0 hard
    scene set only school day room2 yinghua
    with dissolve
    play music first_13 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_n3 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/0101350.ogg"
    rxl "小铃，今天和小凉一起吃可以吧？"
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_ga3 onlayer m2 at walkin_l(0.3)
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0500470.ogg"
    lingyin "没问题哟，我已经默许了日向同学的“加深感情”大作战了。"
    hide lingyin_xzf_b2
    show yczs_xzf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.7):
        xzoom -1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1600120.ogg"
    yczs "日向亲，莫非你......"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_a2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0101360.ogg"
    rxl "不是这样的！我只是想和小凉聊聊过去的事情而已。"
    show yczs_xzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1600130.ogg"
    yczs "那我也一起没问题吧？"
    show rxl_xzf_b2 b2 b2_a1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/0101370.ogg"
    rxl "诶......"
    show yczs_xzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/1600140.ogg"
    yczs "不要这么露骨地摆出不愿意的表情啊！"
    hide rxl_xzf_b2
    show rxl_xzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
        xzoom -1
    play voice "voice/日向怜/0101380.ogg"
    rxl "因为一诚君你，好像会妨碍我的样子。"
    show yczs_xzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1600150.ogg"
    yczs "这么肥的一只鸭子就摆在那里，撒手不管真的是太可惜了。"
    hide rxl_xzf_b3
    show rxl_xzf_b2 b2 b2_a2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0101390.ogg"
    rxl "果然是来妨碍我的！要搞定小凉的是我！"
    show yczs_xzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1600160.ogg"
    yczs "越弱的狗叫得越响，就这点程度还怎么抓鸭子？"
    "这两个人从刚才开始究竟在说些什么？"
    "有种不好的预感。"
    me01 "两位，我没怎么听懂你们说的。"
    hide yczs_xzf_b1
    hide rxl_xzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0500480.ogg"
    lingyin "不管怎么说，“鸭子先生”总有一天也会明白的。"
    "被烤着吃的时候就已经晚了啊！"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black
    with dissolve

label day02.library_event01:
    play ambience1 rill noloop
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school evening library yinghua
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(-2250, -100, 400, duration=1.5)
    pause 1.0 hard
    "放学后我来到学校的图书馆。"
    "吃饭的时候才知道，原来所谓的“作战”就是社团劝诱。"
    "这里的社团似乎是需要人数支持才能够成立的。"
    "不过可以的话我还是更喜欢图书馆这样清静的地方啊。"
    me01 "让我看看，图书馆的使用规章是......"
    pause 1.0 hard
    show lingyin_xzf_b1 b1 b1_sp1 onlayer screens at side_left('lingyin', 0.055), basicfade
    play voice "voice/青木铃音/0500770.ogg"
    lingyin "啊咧，神野同学？"
    play music first_05 fadein 3.0 if_changed
    hide lingyin_xzf_b1
    pause 0.5 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    me01 "莫非铃音同学是这里的管理员吗？"
    "只见铃音坐在管理员的位置上整理着书籍，该说这一切都太巧合了吧。"
    show lingyin_xzf_b1 b1 b1_h1
    play voice "voice/青木铃音/0500780.ogg"
    lingyin "是的，今天是我值班。"
    "铃音一边说着一边从我手中接过学生证。"
    me01 "抱歉，忙的话就不麻烦你了。"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0500790.ogg"
    lingyin "请不要在意，今天没有多少借书的同学，所以一直很闲的。"
    "环视了一眼四周，确实只有熙熙攘攘的几个身影而已。"
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0500800.ogg"
    lingyin "学生会和普通的社团不同，包含的成员并不多，所以某种意义上来说这边也是有劝诱需求的。"
    show lingyin_xzf_b2 b2 b2_s1
    play voice "voice/青木铃音/0500810.ogg"
    lingyin "尤其是学生会的管理阶层，并不是通过竞选，而是推荐的方式选上的情况也有很多。"
    me01 "再怎么说也不会一开始就推荐转校生吧。"
    show lingyin_xzf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0500820.ogg"
    lingyin "神野同学在其他学校的时候也是学生会的成员吗？"
    me01 "并不是。"
    play voice "voice/青木铃音/0500830.ogg"
    lingyin "社团活动呢？"
    me01 "也没有参加过。"
    hide lingyin_xzf_b2
    show lingyin_xzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0500840.ogg"
    lingyin "果然......"
    me01 "怎么了？"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0500850.ogg"
    lingyin "神野同学你有去过补习班吗？"
    me01 "不、也没有去。"
    "铃音歪着头打量着我。"
    show lingyin_xzf_b1 b1 b1_s1
    play voice "voice/青木铃音/0500860.ogg"
    lingyin "还以为一定是这样的呢。"
    show lingyin_xzf_b1 b1 b1_n1
    play voice "voice/青木铃音/0500870.ogg"
    lingyin "我其实是知道神野同学转校考试成绩的~"
    me01 "诶？"
    show lingyin_xzf_b1 b1 b1_h1
    play voice "voice/青木铃音/0500880.ogg"
    lingyin "我也是从身为学生会干部的姐姐那里听来的。毕竟学生会可是掌握了学生成绩情报的获取手段。"
    "比起城市里的学校，樱华中学的学生似乎有很大的自主管理特权的样子。"
    "果然还是不要和学生会扯上关系比较好。"
    me01 "铃音同学，关于我成绩的事你和其他人说过吗？"
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0500890.ogg"
    lingyin "没有，学生会的成员都有保密的义务，我想一般的学生还是不可能知道的。"
    show lingyin_xzf_b1 b1 b1_h1
    play voice "voice/青木铃音/0500900.ogg"
    lingyin "但神野同学的成绩真的很优秀呢。"
    "所以刚刚才会向我透露有关“劝诱”的情报吗。"
    me01 "成绩的事情能替我保密吗？"
    show lingyin_xzf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0500910.ogg"
    lingyin "虽然是没有问题，但是我想下次考试的时候大家就会知道了。"
    me01 "不是说一般的学生是不会知道的吗？"
    show lingyin_xzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0500920.ogg"
    lingyin "期中和期末考试的前十名都会公布的。"
    me01 "......"
    show lingyin_xzf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0500930.ogg"
    lingyin "怎么了？"
    me01 "没什么，只是突然受到了点打击。"
    play voice "voice/青木铃音/0500940.ogg"
    lingyin "是这样吗......我认为成绩优秀是一件值得骄傲的事情。"
    "成绩优秀的人相对的会在班级里受到更多的关注。"
    "就这一点而言，对于像我这样早已习惯了和“不合群”的气氛相伴的人来说，别人投来的那些目光可以说是致命的。"
    show lingyin_xzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0500950.ogg"
    lingyin "根据神野同学的成绩来看，就算被选为年级代表也不奇怪。"
    show lingyin_xzf_b2 b2 b2_ga3
    play voice "voice/青木铃音/0500960.ogg"
    lingyin "所以，姐姐对于你的关注度也是相当的高，请注意哦~"
    me01 "你姐姐？"
    show lingyin_xzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0500970.ogg"
    lingyin "如果有困扰的话可以随时来找我商量，虽然我和姐姐是站在一边的，但是和神野同学也一样是伙伴哟~"
    "如果学校里的学生都能像铃音同学这样善解人意的话，过去的我也许就不需要为处理人际关系而耗费那么大的劲了吧。"
    show lingyin_xzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0500980.ogg"
    lingyin "对了神野同学，今天为什么会来图书馆呢？"
    stop music fadeout 5.0
    me01 "我想找一些书。"
    show lingyin_xzf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0500990.ogg"
    lingyin "什么样的书呢？"
    me01 "这个有点特殊。"
    show lingyin_xzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0501000.ogg"
    lingyin "对于图书委员的我来说，只要是学校的藏书，没有我找不到的。"
    me01 "那就拜托铃音同学了。"
    me01 "我想找的是这里的学生名册，以及关于观景台历史的书。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening yinghua
    with dissolve
    "为了搞清楚那位名叫“雷亚”的女孩究竟是谁，我想先从樱华镇本地的人员入手才是最佳选择。"
    pause 0.5 hard
    scene black
    with dissolve
    pause 1.0 hard
    scene set only school evening library yinghua
    with dissolve
    pause 2.0 hard
    play music first_08 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0501150.ogg"
    lingyin "话说，为什么要找这些书呢？"
    me01 "因为有些在意的事。"
    show lingyin_xzf_b2 b2 b2_n2
    play voice "voice/青木铃音/0501160.ogg"
    lingyin "为什么想要看这些书呢，可以问一下理由吗？"
    me01 "可以的话我想先保密，等时机成熟了自然会告诉铃音同学的。"
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0501170.ogg"
    lingyin "我知道了，这样的话神野同学想要的书我就先放在这里了，有什么需要的话请再来找我吧。"
    me01 "抱歉，真是麻烦你了。"
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_n1 at walkout_r(0.5)
    play sound move_2
    stop music fadeout 5.0
    pause 2.0 hard
    "接下来......"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    play music first_25 fadein 3.0 if_changed
    show namelist onlayer b2 at basicfade_c2u
    "翻阅了樱华中学历年的学生名册，其中并没有找到名为“雷亚”的女生，果然她并不是这里的学生。"
    "依照她的相貌来看，此刻的她应该是学生的身份无疑，可是一般的女生会选择在大半夜的穿着奇装异服，手持镰刀独自到禁地观景台去吗。"
    "果然要想查清楚她的身份，只能从观景台这一方向入手吗。"
    hide namelist
    pause 1.0 hard
    "干劲上来了。"
    "没有必要一个一个地调查，直接从最有可能的环节入手才是最正确的。"
    "虽说据我所知如今的观景台已经很少有游客知道了，但是显然还是存在例外的。"
    "排除了一些没必要的工作，但是需要确认的资料还是非常之多的。"
    "发自内心地对铃音感到抱歉。"
    stop music fadeout 2.0
    pause 1.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    "............"
    "......"
    "..."
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school evening library yinghua
    with dissolve
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_sp1 onlayer screens at side_left('lingyin'), basicfade
    play voice "voice/青木铃音/0501180.ogg"
    lingyin "神野同学，怎么样了？"
    hide lingyin_xzf_b2
    pause 1.0 hard
    play music first_27 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    me01 "......"
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0501190.ogg"
    lingyin "已经快到傍晚了，还没结束吗？"
    hide lingyin_xzf_b2
    show lingyin_xzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0501200.ogg"
    lingyin "差不多要到闭馆的时间了。"
    "我合上了手中的书本，像个泄了气的皮球一样无精打采地趴在桌子上。"
    "两个小时的工作丝毫没有任何进展。"
    me01 "抱歉铃音同学，在这里坐了这么久。"
    hide lingyin_xzf_b1
    show lingyin_xzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/青木铃音/0501210.ogg"
    lingyin "请不要在意。比起这个，调查还顺利吗？"
    me01 "说来惭愧，并不太顺利。"
    show lingyin_xzf_b2 b2 b2_s1
    "铃音听了也是一脸遗憾的样子。"
    show lingyin_xzf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0501220.ogg"
    lingyin "虽然可以借出去，要怎么办呢？"
    me01 "暂时先这样吧，我想比起在书本中寻找答案，应该还有更好的方法才对。"
    "现在的局势来看，当面问清楚才是最省事的。"
    "只是对于能否好好交流这一点我始终没有太大的信心。"
    show lingyin_xzf_b2 b2 b2_n2
    play voice "voice/青木铃音/0501230.ogg"
    lingyin "那么，这些书要怎么处理呢？"
    me01 "虽然没有完全解决我的问题，但是也帮了不少忙。"
    me01 "让我能了解到不少有价值的东西，这一切都要归功于铃音同学你。"
    show lingyin_xzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0501250.ogg"
    lingyin "这点小事不必道谢，身为图书委员能够履行职责，我也很高兴。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with dissolve
    pause 2.0 hard

label day02.xz_event01:
    play ambience1 zhiliao fadein 5.0 
    $ flcam.move(0, 0, 0)
    scene set only street evening yinghua
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "自称是“死神”的少女雷亚。"
    "她的身上还有着太多的疑点。"
    "例如为什么她会知道我的过去，又为什么会独自一人在观景台等我。"
    "而她手中的那把镰刀又是怎么回事。"
    pause 1.0 hard
    scene set only street evening park
    with right2left
    pause 0.5 hard
    "虽然需要调查的事情还有很多，不过比起这些，眼下还有一件更重要的事情需要去做。"
    "那就是去和真正的“约定之人”的相遇环节。"
    pause 1.0 hard
    play sound move_2
    scene set only home evening xz_yinghua
    with right2left
    pause 0.5 hard
    "印象中就是这里了。"
    "从学生名册中找到的关于”青木翔子“的家庭住址就在眼前。"
    "确认了一眼门牌上的名字，也确实是写着“青木”没错。"
    "这下终于能见到“她”了。"
    "虽然过程并不像想象中的那么顺利，不过终归是来到这一刻了。"
    "那种激动的心情此刻正涌上我的心头。"
    me01 "不能退缩！"
    play sound door_rill
    pause 1.5 hard
    "我一边告诫着自己，一边按响了门铃。"
    stop ambience1 fadeout 3.0
    pause 1.5 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    play sound open_door2
    pause 2.0 hard
    play music first_09 fadein 3.0 if_changed
    show xz_mother_xsf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/翔子母亲/1100010.ogg"
    xz_mother "啊啦小凉，早上好~"
    "开门的是翔子的母亲。"
    "看来是没有找错地方，这也让我松了一口气。"
    me01 "那个......您好。"
    show xz_mother_xsf_b1 b1 b1_sp1
    play voice "voice/翔子母亲/1100020.ogg"
    xz_mother "发生什么事了吗？"
    me01 "怎么说呢，现在已经不是早上了。"
    show xz_mother_xsf_b1 b1 b1_s1
    play voice "voice/翔子母亲/1100030.ogg"
    xz_mother "我真是的，抱歉一直睡到现在。"
    show xz_mother_xsf_b1 b1 b1_n1
    play voice "voice/翔子母亲/1100040.ogg"
    xz_mother "再一会天就黑了，我先去给你们准备晚饭了~"
    me01 "真是麻烦您了。"
    show xz_mother_xsf_b1 b1 b1_h1
    play voice "voice/翔子母亲/1100060.ogg"
    xz_mother "为了庆祝你们重逢，今天我可要大显身手了~"
    pause 0.5 hard
    show xz_mother_xsf_b1 b1 b1_h1 at walkout_l(0.5)
    pause 0.5 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    scene black
    with dissolve
    pause 0.5 hard
    play sound close_door
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening xz_living
    with dissolve
    pause 1.0 hard
    me01 "那个，也让我来帮忙吧。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_mother_xsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子母亲/1100070.ogg"
    xz_mother "这边没问题的，你们就好好地聊聊天吧，毕竟很久没见了吧。"
    show xz_mother_xsf_b1 b1 b1_n1
    play voice "voice/翔子母亲/1100080.ogg"
    xz_mother "不过，记得要在晚饭前过来哟~"
    me01 "我知道了。"
    hide xz_mother_xsf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening xz_room
    with dissolve
    pause 0.5 hard
    stop music fadeout 5.0
    $ flcam.move(0, -100, 400, duration=1.5)
    me01 "这里就是翔子的房间吗？"
    "虽然过去了挺长的一段时间，但刚走进房间的那一刻，那种熟悉的味道我一辈子都不会忘记。"
    "我和翔子从很小的时候就在一起玩耍了，是她将我从孤独的校园生活中解救了出来。"
    "也是她当初在我即将离开的时候极力挽留。"
    "话虽如此，也不知道她现在是不是还在为我当初的决定而生气。"
    "也许她早就已经原谅我了。"
    "亦或者......"
    "已经对我彻底失望了。"
    "当年一起在观景台上许下的约定，对于如今的她而言或许早已经不再是那么的重要了。"
    pause 1.0 hard
    play ambience1 louti noloop
    pause 3.0 hard
    "一阵急促的脚步声从门外传来。"
    pause 1.0 hard
    scene white
    with dissolve
    play sound open_door2
    pause 3.0 hard
    scene set only home evening xz_room_with_xz
    $ flcam.moves([
        (0,      0,   0, 0, 0.0, 'linear'),
        (0,      0,   0, 0, 0.5, 'linear'),
        (0, -14750, 100, 0, 4.5, 'ease_cubic')
    ])
    with dissolve
    play music first_40 fadein 5.0 if_changed
    pause 3.5 hard
    "眼前的女孩。"
    "虽然经过几年的岁月之后有所成长，让我一时间竟快要认不出来了。"
    "但此刻的我却依旧能够确信，眼前的女孩就是那时的“她”。"
    "那个和我一起在观景台许下约定的，那个“她”。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening xz_room
    with dissolve
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_xzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010118.ogg"
    xz "那个凉君，怎么样？"
    play voice "voice/翔子/010119.ogg"
    xz "这件校服......合身吗？"
    me01 "非常合身。"
    hide xz_xzf_b3
    show xz_xzf_b2 b2 b2_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010120.ogg"
    xz "嗯。"
    me01 "我回来了。"
    me01 "很高兴见到你，翔子。"
    hide xz_xzf_b2
    show xz_xzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010123.ogg"
    xz "......嗯。"
    $ flcam.move(0, -450, 1000, duration=1.5)
    pause 0.5 hard
    show xz_xzf_b3 b3 b3_s3
    play voice "voice/翔子/010124.ogg"
    xz "......谢谢你。"
    me01 "笨蛋，不要因为这种小事就哭啊。"
    play voice "voice/翔子/010125.ogg"
    xz "可、可是。"
    me01 "我可是好好地遵守了。"
    me01 "当初在观景台上许下的，重逢的约定。"
    me01 "现在约定实现了不是应该感到高兴才是吗？"
    play voice "voice/翔子/010126.ogg"
    xz "就算你这么说。"
    play voice "voice/翔子/010127.ogg"
    xz "可是凉君你......也在哭啊。"
    show xz_xzf_b3 b3 b3_c1
    play voice "voice/翔子/010128.ogg"
    xz "凉君！"
    play voice "voice/翔子/010130.ogg"
    xz "谢谢你。"
    show xz_xzf_b3 b3 b3_s3
    play voice "voice/翔子/010132.ogg"
    xz "......凉君。"
    play voice "voice/翔子/010133.ogg"
    xz "真的谢谢你，凉君。"
    me01 "没有必要向我道谢，我可是最没有资格被翔子你感谢的人。"
    show xz_xzf_b3 b3 b3_h1
    play voice "voice/翔子/010134.ogg"
    xz "不是的、不是那样的。"
    play voice "voice/翔子/010135.ogg"
    xz "这些年我每天都祈祷着凉君你能够回来。"
    play voice "voice/翔子/010136.ogg"
    xz "能够再陪我说说话，为我加油打气。"
    play voice "voice/翔子/010137.ogg"
    xz "祈祷着你没有把我忘记。"
    hide xz_xzf_b3
    show xz_xzf_b2 b2 b2_c1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010138.ogg"
    xz "所以我也必须要坚强起来才行。"
    play voice "voice/翔子/010139.ogg"
    xz "也多亏了凉君你，到最后我也没有放弃这个想法。"
    pause 1.0 hard
    scene white
    with dissolve
    "我强忍着夺眶而出的泪水。"
    "上前抱住了眼前的女孩。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening xz_room
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_xzf_b2 b2 b2_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010140.ogg"
    xz "......凉君，在这种地方。"
    play voice "voice/翔子/010141.ogg"
    xz "说不定会被谁看到的。"
    me01 "抱歉，这一次就请原谅我吧。"
    me01 "一下就好......请再等一下就好。"
    hide xz_xzf_b2
    show xz_xzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010142.ogg"
    xz "真是无节操呢。嗯，无节操。"
    me01 "分开后的这些年我才真正明白，我真的......离不开翔子你。"
    show xz_xzf_b3 b3 b3_s4
    play voice "voice/翔子/010143.ogg"
    xz "在胡言乱语中夹杂着微妙的告白啊。"
    show xz_xzf_b3 b3 b3_h1
    play voice "voice/翔子/010144.ogg"
    xz "嗯。"
    play voice "voice/翔子/010145.ogg"
    xz "我也已经不再迷茫了。"
    play voice "voice/翔子/010146.ogg"
    xz "我已经不想再成为你的负担了。"
    play voice "voice/翔子/010147.ogg"
    xz "我会永远支持凉君你的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening yinghua
    with dissolve
    pause 2.0 hard

label day02.neighbor_event01:
    play sound close_door
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street night neighbor
    with dissolve
    $ flcam.move(0, -100, 400, duration=1.5)
    play music first_07 fadein 3.0 if_changed
    pause 0.5 hard
    "看样子先前的担忧仿佛完全没有必要。"
    "一切似乎都向着好的方向发展，然而这一些来得太突然，满满的幸福感充斥着全身。"
    "回家的路上，我也是接到了来自翔子母亲的委托。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only home night xz_living
    show sepiagrain onlayer texture
    with dissolve
    pause 1.5 hard
    show xz_mother_xsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子母亲/1100090.ogg"
    xz_mother "小凉，能稍微过来一下吗？"
    show xz_mother_xsf_b1 b1 b1_h1
    play voice "voice/翔子母亲/1100100.ogg"
    xz_mother "我做了一些蛋黄酥，回去之前能替我给邻居带一些吗？"
    show xz_mother_b1 b1 b1_n1
    play voice "voice/翔子母亲/1100110.ogg"
    xz_mother "就算是去给他们打个招呼，连同{rb}小青{/rb}{rt}翔子的昵称{/rt}的份一起。"
    pause 1.0 hard
    $ flcam.move(0, -100, 400)
    scene set only street night neighbor
    with dissolve
    pause 0.5 hard
    "邻居吗......没想到机缘巧合刚好搬到了青木家母口中的邻居附近。"
    "也算是一次难得的机会吧。"
    "之前收了青木家不少照顾，还是要适当帮忙报答一下的。"
    "即便是到了现在我依旧没有缓过来。这一切似乎都是冥冥之中安排好了一般，巧合得有些不自然。"
    hide xz_mother_xsf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    scene black 
    with dissolve
    pause 1.0 hard
    scene set only home night neighbor yinghua
    with right2left
    pause 1.0 hard
    "根据翔子母亲提供的地址，我来到了一栋公寓楼下。"
    "这栋建筑的装潢十分华丽，一看就是有钱人的居所。"
    "就连入口也是安装了电控门。"
    stop music fadeout 5.0
    me01 "那个，对方的门牌是......"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    play sound door_rill
    "确认了手里地址信息，我按下响公寓的门铃。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "..."
    "......"
    "............"
    "可是过了许久也没有人回应。"
    "不在家吗？"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    play sound door_rill
    "再一次按响门铃。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "..."
    "......"
    "还是没有人回应。"
    "这个时间点来拜访或许是被误认为卖报纸或者推销员之类的了吧。"
    "既然这样的话。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    play sound door_rill
    pause 0.5 hard
    me01 "抱歉打扰了，我是樱华日报的募捐志愿者，请问可以配合一下吗？"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "等了一会儿依旧是没有任何动静。"
    "果然凭这种僵硬的说辞，是个人都会无视的吧。"
    "看来今天只能先回去了。"
    play voice "voice/天使莲/0400010.ogg"
    stranger "......募捐？"
    pause 1.0 hard
    play music first_17 fadein 3.0 if_changed
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_n2 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    me01 "呜哇，善良的邻居上钩了！"
    show ts_lian_ssz_b1 b1 b1_ga1
    play voice "voice/天使莲/0400020.ogg"
    stranger "上钩？"
    me01 "啊不是，晚上好，请问你就是莲......小姐吗？"
    play voice "voice/天使莲/0400030.ogg"
    stranger "......"
    me01 "那个......"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_ga1 onlayer m2 at walkout_l(0.7)
    play sound move_2
    pause 1.5 hard
    hide ts_lian_ssz_b1
    "没有回答我的问题，邻居直接转身走了。"
    $ flcam.move(0, -400, 1100, duration=1.5)
    pause 0.5 hard
    me01 "请、请等一下，我是最近刚搬到镇上来的，就住在这附近。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使莲/0400040.ogg"
    ts_lian "刚刚明明说是募捐的。"
    me01 "那、那是因为。"
    me01 "见你一直不肯不出来，就想试探一下是不是真的没人，所以......"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2 at walkout_l(0.5)
    play sound move_2
    pause 1.5 hard
    hide ts_lian_ssz_b1
    "再次转身离开。"
    pause 0.5 hard
    $ flcam.move(-1100, -200, 600, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.45
    play voice "voice/天使莲/0400050.ogg"
    ts_lian "最近的推销员真可怕......"
    "大失败，第一印象很差啊！"
    me01 "用这种方式骗你出来真是抱歉，其实我是专程来送东西的。"
    show ts_lian_ssz_b1 b1 b1_n2
    "我将手中的蛋黄酥递了过去。"
    me01 "这些，不嫌弃的话和家人一起吃吧。"
    show ts_lian_ssz_b1 b1 b1_sp1
    play voice "voice/天使莲/0400060.ogg"
    ts_lian "续订报纸的赠品？"
    me01 "不、不是的，是青木家母托我送过来的见面礼。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400070.ogg"
    ts_lian "......"
    pause 1.0 hard
    $ flcam.move(-1100, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 at flu_down(0.25, 20):
        xpos 0.45
    pause 1.0 hard
    $ flcam.move(-1100, -200, 600, duration=1.5)
    pause 0.5 hard
    "虽然表情还是相当地嫌弃，但她是还是从我手中接过了蛋黄酥。"
    me01 "这个时候来打扰真是抱歉。"
    me01 "见面礼，希望你能喜欢。"
    show ts_lian_ssz_b1 b1 b1_ga1
    play voice "voice/天使莲/0400080.ogg"
    ts_lian "奇怪的人。"
    me01 "我会反省的。"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/0400090.ogg"
    ts_lian "请加油。"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2 at walkout_l(0.45)
    play sound move_2
    pause 1.5 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    "虽然在学校没有翻车，但刚刚的操作也是成功让我获得了“怪人”的称号。"
    "但愿这位“善良”的邻居不是那么地记仇就好了......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard

label day02.starview_event01:
    $ flcam.move(0, 0, 0)
    scene set only street night yinghua
    with dissolve
    play music first_27 fadein 3.0 if_changed
    pause 2.0 hard
    play sound move_1
    scene set only starview night road
    with right2left
    pause 1.0 hard
    "在回家之前，我依旧决定去观景台看看。"
    "本打算在确认没有人之后就迅速离开的。"
    "即使雷亚不在也无所谓。"
    "无论如何我想靠自己的努力被雷亚所接受。"
    "那种被命运牵着鼻子走的无力感，到最后依旧毫无还手之力而妥协的心情我已经不想再体会了。"
    "不仅仅是对雷亚，就连过去的翔子也是一样的。"
    "她明明是在这里等着我的。"
    "她明明，到最后都想留住我的......"
    pause 1.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_memory piecetwo yinghua
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/0600880.ogg"
    xz "凉君，我有个不错的想法~"
    $ flcam.move(0, -100, 400, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    me01 "不错的想法？"
    play voice "voice/翔子/0600890.ogg"
    xz "可以让凉君不用搬家的方法。"
    me01 "什么方法？"
    play voice "voice/翔子/0600900.ogg"
    xz "让凉君受重伤！"
    play voice "voice/翔子/0600910.ogg"
    xz "如果受了重伤的话，就要住在附近的医院里，这样一来我每天都可以去看望你了。"
    play voice "voice/翔子/0600920.ogg"
    xz "这样既不用担心住的地方，也不用担心没东西吃了~"
    me01 "但是那样稍微有点讨厌啊。"
    play voice "voice/翔子/0600930.ogg"
    xz "为什么？"
    me01 "因为......受伤可是很疼的啊。"
    play voice "voice/翔子/0600940.ogg"
    xz "你是男孩子吧，这点小事忍忍就好了。"
    me01 "别说得事不关己啊......"
    play voice "voice/翔子/0600950.ogg"
    xz "只要从这座观景台摔到小镇上就行了。"
    me01 "才、才不要呢......那种事。"
    play voice "voice/翔子/0600960.ogg"
    xz "凉君真是没骨气啊。"
    me01 "所以说我是很普通的啦。"
    play voice "voice/翔子/0600970.ogg"
    xz "那......要怎么样才好。"
    me01 "......"
    play voice "voice/翔子/0600980.ogg"
    xz "要怎么样，才能不和凉君分开呢......"
    me01 "我们不是约好了吗？"
    me01 "我们一定会再见面的。"
    me01 "会重逢的。"
    play voice "voice/翔子/0600990.ogg"
    xz "但是......"
    $ flcam.move(800, -1100, 400, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0601000.ogg"
    xz "那不知要等到什么时候了。"
    play voice "voice/翔子/0601010.ogg"
    xz "凉君，不知道什么时候才能回来。"
    play voice "voice/翔子/0601020.ogg"
    xz "我也不知道，还能等到什么时候......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with dissolve
    pause 3.0 hard
    play voice "voice/天使雷亚/0000550.ogg"
    lst "等你很久了，凉君——"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play music first_18 fadein 3.0 if_changed
    scene set only lisite_cg normal
    with in2out_v2_slow
    pause 2.0 hard
    "那个白色的身影再次出现在我眼前。"
    "尽管不是第一次了，但我还是无法相信自己的眼睛。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0000560.ogg"
    lst "怎么了，一脸苦相？"
    me01 "没什么。"
    "我摇了摇头，努力让自己从回忆中清醒过来。"
    "好不容易才见到的。"
    me01 "今天也来看星星吗？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0000570.ogg"
    lst "都一样。"
    me01 "还是说在等我？"
    play voice "voice/天使雷亚/0000580.ogg"
    lst "都一样。"
    me01 "刚刚不是说等了很久吗？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0000590.ogg"
    lst "虽然确实是等了，但是一看到你的脸就觉得还不如不等所以后悔了。"
    me01 "打击！"
    play voice "voice/天使雷亚/0000600.ogg"
    lst "因为你，在看到我的瞬间显得很难过。"
    me01 "......"
    play voice "voice/天使雷亚/0000610.ogg"
    lst "虽然我的工作是收割噩梦，但是可以的话我希望在对方还没有察觉到噩梦的时候下手。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0000620.ogg"
    lst "你，是因为做了噩梦所以才会那么难受的吧？"
    me01 "你的意思是说我的过去是噩梦吗？"
    me01 "如果这是开玩笑的话可一点也不好笑。"
    play voice "voice/天使雷亚/0000630.ogg"
    lst "我没有开玩笑。"
    me01 "虽然不知道为什么，但是自己的过去被无端地否定了的话我还是不能接受的。"
    me01 "因为你把那些对我而言最重要的回忆说成是......噩梦，这要我怎么可能认同啊。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0000640.ogg"
    lst "是这样吗？"
    me01 "可以的话，我希望你能道歉。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0000650.ogg"
    lst "不要。"
    "被拒绝了。"
    "冷静下来，对方可是女孩子啊。"
    me01 "那个，如果能够说一句“对不起”的话哥哥我会很开心的。"
    play voice "voice/天使雷亚/0000660.ogg"
    lst "不要。"
    "这混账。"
    play voice "voice/天使雷亚/0000670.ogg"
    lst "在这世界上我最最讨厌的事情之一就是道歉了，所以不要。"
    "这个cosplay少女似乎正在叛逆期。"
    me01 "随便了，反正这样的事我也习惯了。"
    play voice "voice/天使雷亚/0000680.ogg"
    lst "那算什么。"
    me01 "雷亚有兄弟姐妹吗？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0000700.ogg"
    lst "死神才没有兄弟姐妹什么的。"
    me01 "这个时间还不回去的话父母可是会担心的。"
    play voice "voice/天使雷亚/0000710.ogg"
    lst "死神才没有家人呢。"
    me01 "你经常在这里出没吗？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0000720.ogg"
    lst "出没......你到底把我当成什么啊。"
    me01 "不是死神吗？"
    play voice "voice/天使雷亚/0000730.ogg"
    lst "......什么啊，你那毫无责任感的回答。"
    me01 "那么换个问法，你经常到这里来吗？"
    play voice "voice/天使雷亚/0000740.ogg"
    lst "是的吧，能看到星星的夜晚我应该都在这里。"
    me01 "也就是说你也见到过其他造访这座观景台的人了？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0000750.ogg"
    lst "有啊。"
    me01 "知道那个人的名字吗？"
    play voice "voice/天使雷亚/0000760.ogg"
    lst "知道啊。"
    me01 "能告诉我吗？"
    play voice "voice/天使雷亚/0000770.ogg"
    lst "神野凉。"
    "是我啊！"
    me01 "除了我之外还有其他人吗？"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0000780.ogg"
    lst "不知道。"
    "这下线索彻底断了。"
    "也就是说翔子她并没有来过这里，而眼前的女孩也没有见过翔子本人。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0000790.ogg"
    lst "今天的你废废的呢。"
    "虽然不知道为什么却被说成废柴了。"
    play voice "voice/天使雷亚/0000800.ogg"
    lst "上次明明是个好机会的......但是，突然就看不到星星了。"
    me01 "你在说什么？"
    play voice "voice/天使雷亚/0000810.ogg"
    lst "不关你的事。"
    me01 "所以说你到底是谁？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0000820.ogg"
    lst "死神呀。"
    play voice "voice/天使雷亚/0000830.ogg"
    lst "割取人噩梦的，死神。"
    me01 "割取噩梦而不是生命？"
    play voice "voice/天使雷亚/0000840.ogg"
    lst "对。"
    me01 "所以什么是噩梦呢？"
    play voice "voice/天使雷亚/0000850.ogg"
    lst "那种问题自己查字典去！"
    me01 "那什么叫割取噩梦呢？"
    play voice "voice/天使雷亚/0000860.ogg"
    lst "虽然我割取过别人的噩梦，但是因为没有被别人割取过所以不知道。"
    "这个死神貌似很不专业啊。"
    me01 "那么......"
    "你为什么要在这里等我？"
    "我们之间的约定又是什么？"
    "就在这一瞬间，我犹豫着是否该这么问。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0000870.ogg"
    lst "在你犹豫该不该问的时候，就是不该问。"
    play voice "voice/天使雷亚/0000880.ogg"
    lst "会犹豫要不要问的问题，就代表着会害怕窥探对方的内心。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0000890.ogg"
    lst "如果随随便便就去窥探的话，那就肯定是无法负起责任的。"
    play voice "voice/天使雷亚/0000900.ogg"
    lst "明明被窥探的一方希望另一方能够负起责任的。"
    play voice "voice/天使雷亚/0000910.ogg"
    lst "想要一起烦恼，一起生气，一起哭泣，一起欢笑的......"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0000920.ogg"
    lst "所以，当你还没准备好去窥探对方内心的时候，就不该问出口。"
    play voice "voice/天使雷亚/0000930.ogg"
    lst "这样的话，对双方来说才是最好的。"
    "她一边说着，手上的镰刀像发出警告一般地散发着银白色的光芒。"
    me01 "那最后一个问题。"
    "我深吸了一口气。"
    me01 "在我确信了是该问的时候，就可以问了吧？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    $ flcam.move(2200, -2800, 900, duration=2.0, warper='ease_quad')
    pause 2.0 hard
    "雷亚的表情变了。"
    "第一次在她的脸上见到如此巨大的变化。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0000940.ogg"
    lst "......可以吧。"
    play voice "voice/天使雷亚/0000950.ogg"
    lst "到那时就算你什么都不问，对方也会主动向你倾诉的吧。"
    stop music fadeout 5.0
    pause 2.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    with dissolve
    pause 1.0 hard
    "当夜空中的星辰被阴云遮住的那一刹那，少女的身影也随之消失了。"
    pause 2.0 hard
    scene black with slowerdissolve
    $ suppress_overlay = True
    jump day03
