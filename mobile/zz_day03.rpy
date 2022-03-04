label day03:
    bookmark
    $ save_name = _("Day 03")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_yinghua spring
    with dissolve
    show backend_bg01 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date02 onlayer m1 at backend_date
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    play ambience1 niaoming fadein 5.0
    $ suppress_overlay = False
    scene set only street day neighbor
    with dissolve
    play sound close_door
    pause 2.0 hard
    scene set only street day yinghua
    with dissolve
    pause 1.0 hard
    play sound move_2
    "尽管现在住的地方离学校并不算很远，但是徒步的话多少还是需要花些时间的。"
    "昨晚在观景台等了许久也没见雷亚回来，那家伙不会真的是死神吧。"
    "托她的福今天又是“元气满满”的一天。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    me01 "......那是？"
    me01 "邻居小姐。"
    play music first_13 fadein 3.0 if_changed
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_ga1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/天使莲/0400150.ogg"
    ts_lian "......又出现了。"
    me01 "别把我说得跟幽灵一样啊。"
    "虽说昨晚的气氛比较尴尬。"
    "但此刻正是挽回形象的好机会，一定要把握住。"
    me01 "昨天没有好好打声招呼，我叫神野凉，是樱华校二年级的转学生。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400170.ogg"
    ts_lian "一年级，{rb}苍衣莲{/rb}{rt}化名{/rt}。"
    me01 "请多指教~"
    show ts_lian_ssz_b1 b1 b1_ga1
    play voice "voice/天使莲/0400180.ogg"
    cyl "怎么好像变成关系很好的样子。"
    "依旧是面无表情地保持着距离。"
    "好、好棘手的孩子。"
    me01 "莲同学是哪个班级的？"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400190.ogg"
    cyl "......"
    me01 "能交到朋友的话真是太好了。"
    play voice "voice/天使莲/0400200.ogg"
    cyl "......"
    me01 "有参加社团活动吗？"
    play voice "voice/天使莲/0400210.ogg"
    cyl "......"
    "啊、啊咧，气氛是不是越来越尴尬了？"
    me01 "那个，莫非你还在为昨晚的事生气吗？"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/0400230.ogg"
    cyl "没有那回事。"
    me01 "作为道歉，下次我会亲自登门拜访的。"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/0400240.ogg"
    cyl "不用麻烦了。"
    me01 "话说回来，能在这个时间遇到你，莲同学莫非和我一样是早上起不来的类型吗？"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400300.ogg"
    cyl "我没有那么厉害。"
    me01 "别这么说嘛，再怎么说也算是同道中人了。"
    show ts_lian_ssz_b1 b1 b1_sp1
    play voice "voice/天使莲/0400310.ogg"
    cyl "是这样吗？"
    me01 "嗯。"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/0400320.ogg"
    cyl "真是遗憾。"
    me01 "那么就再说一次吧，今后还请多多指教。"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/0400330.ogg"
    cyl "我会妥善考虑的。"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2 at walkout_l(0.7)
    pause 2.0 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    stop music fadeout 5.0
    stop ambience1
    pause 1.0 hard

label day03.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day gate yinghua
    with right2left
    pause 2.0 hard
    "就这样我们一起来到了校门口，此时那里正聚集着许多的学生。"
    "似乎是正在举行什么活动的样子。"
    play music first_17 fadein 3.0 if_changed
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/天使莲/0400340.ogg"
    cyl "莫非......"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.7
    pause 0.5 hard
    "莲把书包紧紧地攥在怀里。"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/0400350.ogg"
    cyl "中招了。"
    me01 "中招了？"
    play voice "voice/天使莲/0400360.ogg"
    cyl "那大概是检查随身物品的环节。"
    hide ts_lian_ssz_b1
    $ flcam.move(0, -400, 1200, duration=2.0, warper='ease_quad')
    pause 2.0 hard
    "我朝着人群的方向看去，果然有几个披着“学生会”字样腕章的人在那里维持着秩序。"
    pause 1.0 hard
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.7
    play voice "voice/天使莲/0400370.ogg"
    cyl "一学期一次的检查，虽然之前在班会上也听说过。"
    me01 "还真是突然啊。"
    me01 "莫非这所学校的秩序很乱吗？"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400380.ogg"
    cyl "我才不知道。"
    me01 "还是单纯因为校规太过严苛了？"
    play voice "voice/天使莲/0400390.ogg"
    cyl "我才不知道。"
    me01 "莲同学你莫非，是不良学生？"
    show ts_lian_ssz_b1 b1 b1_ga1
    play voice "voice/天使莲/0400400.ogg"
    cyl "你还是死掉比较好。"
    me01 "刚刚好像说了很过分的话？！"
    hide ts_lian_ssz_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    "虽说很不情愿，但我们还是排在了队伍的最后。"
    "眼看着前排学生们不情愿地打开书包接受检查。"
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/天使莲/0400410.ogg"
    cyl "......"
    me01 "怎么了？"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/0400420.ogg"
    cyl "没什么。"
    me01 "书包里藏了什么不想让别人看到的东西吗？"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400430.ogg"
    cyl "我想谁都不想让别人看到自己包里的东西吧。"
    "的确是这样没错。"
    "需要检查私人物品的校规我也是第一次见。"
    me01 "这所学校允许携带手机吗？"
    show ts_lian_ssz_b1 b1 b1_sp1
    play voice "voice/天使莲/0400440.ogg"
    cyl "你带了吗？"
    me01 "这倒没有，但如果不带的话多少会有些不方便呢。"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/0400450.ogg"
    cyl "手机是没问题的，只是禁止在上课的时候使用。"
    me01 "那莲同学带着吗？"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400460.ogg"
    cyl "我虽然是有带，但是不告诉你。"
    "被当成套路女生电话的可疑分子了......"
    me01 "也就是说，你还带了什么更厉害的东西？"
    show ts_lian_ssz_b1 b1 b1_sp1
    play voice "voice/天使莲/0400470.ogg"
    cyl "为什么会这么说？"
    me01 "因为我这么觉得。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400480.ogg"
    cyl "这会让我很困扰的。"
    stop music fadeout 5.0
    pause 0.5 hard
    hide ts_lian_ssz_b1
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 2.0 hard
    show xshz_xzf_b1 b1 b1_h1 onlayer screens at side_left('xshz'), basicfade
    play voice "voice/学生会长/0200230.ogg"
    xshz "好了后面的同学，把书包打开放在桌子上。"
    hide xshz_xzf_b1
    pause 0.5 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    "轮到我们了。"
    "虽是这么说，但莲并没有依照指示有所行动，于是我就先她一步把书包放了上去。"
    play music first_14 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xshz_xzf_b1 b1 b1_h2 onlayer m2 at walkin_l(0.5):
        xzoom -1
    pause 0.5 hard
    play voice "voice/学生会长/0200240.ogg"
    xshz "没有问题。好了下一位！"
    show xshz_xzf_b1 b1 b1_h1
    play voice "voice/学生会长/0200250.ogg"
    xshz "对了......你就是神野同学吧？"
    me01 "是我。"
    show xshz_xzf_b1 b1 b1_h2
    play voice "voice/学生会长/0200320.ogg"
    xshz "话说你入学考试的成绩不错呢。"
    me01 "不要啊！"
    show xshz_xzf_b1 b1 b1_sp1
    play voice "voice/学生会长/0200330.ogg"
    xshz "......虽然不知道你为什么那么抗拒。"
    show xshz_xzf_b1 b1 b1_n1
    play voice "voice/学生会长/0200340.ogg"
    xshz "可成绩优秀但生活态度不端正的话还是进不了学生会的，今后还请多多注意。"
    me01 "不是，我没说过要加入学生会吧。"
    show xshz_xzf_b1 b1 b1_h1
    play voice "voice/学生会长/0200350.ogg"
    xshz "我们学生会势要招纳有才能的人，不要否认自己的能力认真考虑加入我们吧。"
    "果然和铃音说的一样，学生会的成员都是帮喜欢拉拢有能力之人的家伙啊。"
    me01 "我会谨慎考虑的，请多多关照。"
    show xshz_xzf_b1 b1 b1_h2
    play voice "voice/学生会长/0200370.ogg"
    xshz "啊，请多多关照。"
    show xshz_xzf_b1 b1 b1_h1
    play voice "voice/学生会长/0200380.ogg"
    xshz "接下来我还要检查随身物品。"
    me01 "抱歉打扰你工作了。"
    play voice "voice/学生会长/0200390.ogg"
    xshz "你能这么说我很开心，这种检查很容易跟学生结仇的。"
    me01 "也是呢。"
    show xshz_xzf_b1 b1 b1_s2
    play voice "voice/学生会长/0200400.ogg"
    xshz "不要误会了。不是因为喜欢才这么做的，再怎么说学生会也是有明智的盘算才决定采用这样的检查。"
    "嗯，果然是一帮可靠的人。"
    hide xshz_xzf_b1
    stop music fadeout 5.0
    stop ambience1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    me01 "没问题的莲同学，学生会的大家都是很亲切的人，就拿出来让她们看一眼......咦，哪里去了？"
    $ flcam.move(4500, 0, 900, duration=3.0, warper='ease_quad')
    pause 3.0 hard
    show ts_lian_ssz_b1 b1 b1_h2 onlayer m2:
        xpos 0.7 ypos 1.02
        pause 1.0
        linear 0.3 xpos 0.67 ypos 1.0
        linear 0.3 xpos 0.64 ypos 1.02
        1.0
        linear 0.3 xpos 0.61 ypos 1.0
        linear 0.3 xpos 0.58 ypos 1.02
        1.0
    pause 5.0 hard
    hide ts_lian_ssz_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    "就在我和执勤同学说话的时候，莲企图趁机溜进校门。"
    play music first_12 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xshz_xzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.5
        xzoom -1
    with vpunch
    play voice "voice/学生会长/0200410.ogg"
    xshz "等等那边的学生！还没有完成检查呢！"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.68
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/天使莲/0400490.ogg"
    cyl "......切。"
    show xshz_xzf_b1 b1 b1_n1
    play voice "voice/学生会长/0200420.ogg"
    xshz "那么，打开书包放到桌子上来。"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/0400500.ogg"
    cyl "请便。"
    show xshz_xzf_b1 b1 b1_a1
    play voice "voice/学生会长/0200430.ogg"
    xshz "这不是神野同学的书包吗？我要检查你的书包。"
    show ts_lian_ssz_b1 b1 b1_ga1
    play voice "voice/天使莲/0400510.ogg"
    cyl "......切。"
    "她极力躲避检查的一系列操作，和预想的一样里面一定是藏了什么不好的东西。"
    hide ts_lian_ssz_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "那个，果然不检查就不能通过吗？"
    show xshz_xzf_b1 b1 b1_s1
    play voice "voice/学生会长/0200440.ogg"
    xshz "......你啊，刚刚没听到我说的话吗？我也不是因为喜欢才这么做的。"
    me01 "就算这样，我也不赞同这样强制的方式。"
    show xshz_xzf_b1 b1 b1_ga1
    play voice "voice/学生会长/0200450.ogg"
    xshz "毕竟规定就是这样，请你放弃吧。"
    me01 "但是......"
    "总之还是为了帮邻居同学解围试着与她争论了一番。"
    "虽然知道自己理亏但是总归还是需要挣扎一下的。"
    me01 "虽然我承认你是在认真工作。"
    me01 "也很感激你对我们学生所做出的贡献。"
    show xshz_xzf_b1 b1 b1_a1
    play voice "voice/学生会长/0200460.ogg"
    xshz "那就拿出态度来证明啊。"
    me01 "可是放走一两个学生也没什么大不了的吧？"
    show xshz_xzf_b1 b1 b1_ga1
    play voice "voice/学生会长/0200470.ogg"
    xshz "也就是说这个学生带着什么不得了的东西对吧？"
    "不小心把真心话说出来了。"
    hide xshz_xzf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.7
    play voice "voice/天使莲/0400520.ogg"
    cyl "......真糟糕。"
    me01 "不、不是的，我可不是说莲同学的包里有什么不好的东西。"
    show ts_lian_ssz_b1 b1 b1_ga1
    play voice "voice/天使莲/0400530.ogg"
    cyl "你还是蒸发掉吧。"
    me01 "我是挥发性的？！" with vpunch
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400540.ogg"
    cyl "......不过暂且感谢你一下。"
    pause 0.5 hard
    show xshz_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5 
        xzoom -1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/学生会长/0200480.ogg"
    xshz "你是苍衣莲同学吧。不管怎么样，把书包打开给我看看就完事了。"
    stop music fadeout 5.0
    "面对学生会同学的步步紧逼。"
    "莲依旧低着头紧紧地抱着书包。"
    hide ts_lian_ssz_b1
    play music first_13 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "我说......已经可以了吧？"
    show xshz_xzf_b1 b1 b1_a1
    play voice "voice/学生会长/0200510.ogg"
    xshz "不行！神野同学你可能不知道，这座樱华校就是因为缺乏合理的娱乐管制所以风气很乱的。"
    show xshz_xzf_b1 b1 b1_s1
    play voice "voice/学生会长/0200520.ogg"
    xshz "过去就是因为有太多像你一样有这种想法的人在，所以学校的风纪才会变差的。"
    show xshz_xzf_b1 b1 b1_s2
    play voice "voice/学生会长/0200550.ogg"
    xshz "嘛，虽然也不是什么暴力的事件，全都是乱涂乱画的可爱恶作剧罢了。"
    play voice "voice/学生会长/0200600.ogg"
    xshz "但是为了那些守护樱华校前辈们的遗产，现在的学生会也不能放过任何企图扰乱风纪的学生。"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/天使莲/0400560.ogg"
    cyl "为了我们大家让你受累了。"
    show xshz_xzf_b1 b1 b1_h2
    play voice "voice/学生会长/0200610.ogg"
    xshz "你能这么说我很开心。"
    show ts_lian_ssz_b1 b1 b1_h1
    play voice "voice/天使莲/0400570.ogg"
    cyl "从今往后也请继续加油。"
    play voice "voice/学生会长/0200620.ogg"
    xshz "谢谢。"
    stop music fadeout 5.0
    show ts_lian_ssz_b1 b1 b1_h2
    play voice "voice/天使莲/0400580.ogg"
    cyl "那么请多保重~"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_h2 onlayer m2 at walkout_r(0.7)
    pause 1.0 hard
    hide ts_lian_ssz_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    play music first_12 fadein 3.0 if_changed
    xshz "请保重......{w=0.5}{nw}"
    play voice "voice/学生会长/0200630.ogg"
    show xshz_xzf_b1 b1 b1_sp2
    extend "诶......喂喂喂！那边的一年级学生不要趁乱逃跑啊！"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/天使莲/0400590.ogg"
    cyl "暴露是一年级的了。"
    show xshz_xzf_b1 b1 b1_a1
    play voice "voice/学生会长/0200640.ogg"
    xshz "樱华校只有一年级的才不需要穿制服，更何况你是个娃娃脸还那么矮。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400600.ogg"
    cyl "何等的屈辱。"
    show xshz_xzf_b1 b1 b1_n1
    play voice "voice/学生会长/0200650.ogg"
    xshz "那么把书包打开放到桌上吧。"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/0400610.ogg"
    cyl "......请便。"
    show xshz_xzf_b1 b1 b1_ga2
    play voice "voice/学生会长/0200660.ogg"
    xshz "都说了，这是神野同学的书包吧！"
    show ts_lian_ssz_b1 b1 b1_ga1
    play voice "voice/天使莲/0400620.ogg"
    cyl "......切。"
    "话题似乎陷入了不可描述的循环之中。"
    show xshz_xzf_b1 b1 b1_a1
    play voice "voice/学生会长/0200670.ogg"
    xshz "赶紧把自己的包打开让我看看！不然铃声响了按你们迟到处理！"
    me01 "我也是吗？"
    show xshz_xzf_b1 b1 b1_s1
    play voice "voice/学生会长/0200680.ogg"
    xshz "本来就是跟你扯一些无意义的话才导致现在的局面吧，给我负责啊。"
    "何等的冤枉啊！"
    "仔细一看，周围似乎除了带着腕章的学生会成员，就只剩我们了。"
    hide xshz_xzf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "莲同学，差不多可以了吧？要是被当成迟到处理的话可不单单是惹这个姐姐生气那么简单的。"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400630.ogg"
    cyl "真遗憾。"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 at flu_down(0.25, 20):
        xpos 0.7
    pause 0.5 hard
    "在我的劝说下，她勉强地打开了书包。"
    pause 0.5 hard
    show xshz_xzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
        xzoom -1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/学生会长/0200690.ogg"
    xshz "总算是听话了呢。"
    show ts_lian_ssz_b1 b1 b1_s1:
        xpos 0.7
        linear 0.6 xpos 0.6
    play voice "voice/天使莲/0400640.ogg"
    cyl "好、完事了。{w=0.5}{nw}"
    show ts_lian_ssz_b1 b1 b1_s1:
        xpos 0.6
        easein 0.3 yoffset scale(-10)
        easein 0.6 yoffset scale(+0)
        linear 0.6 xpos 0.7
    pause 2.0 hard
    show xshz_xzf_b1 b1 b1_sp2
    play voice "voice/学生会长/0200700.ogg"
    xshz "好好让我检查啊，这么快谁能看得见啊！"
    show ts_lian_ssz_b1 b1 b1_ga1:
        xpos 0.7
    play voice "voice/天使莲/0400650.ogg"
    cyl "这个人干活真慢。"
    show xshz_xzf_b1 b1 b1_ga2
    play voice "voice/学生会长/0200710.ogg"
    xshz "......嘲讽的话就我忍了。真期待里面会出现什么东西！"
    "看着脸上爆出青筋的学生会同学，我不禁咽了口口水。"
    "此时的她正往书包里仔细地翻找着。"
    play voice "voice/学生会长/0200720.ogg"
    xshz "苍衣同学，这是什么呢？"
    $ flcam.move(2250, -200, 600, duration=1.5)
    pause 0.5 hard
    show taluo_card onlayer m2 at item_7to6:
        xalign 0.5
    pause 1.0 hard
    show xshz_xzf_b1 b1 b1_n1
    play voice "voice/学生会长/0200730.ogg"
    xshz "能回答我吗？这到底是什么呢？"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/0400660.ogg"
    cyl "这是笔盒。"
    show xshz_xzf_b1 b1 b1_a1
    play voice "voice/学生会长/0200740.ogg"
    xshz "怎么看都不是吧，这不就是卡片游戏之类的吗？"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400670.ogg"
    cyl "这是卡片游戏图案的笔盒。"
    show xshz_xzf_b1 b1 b1_ga2
    play voice "voice/学生会长/0200750.ogg"
    xshz "里面还放着普通得不能再普通的卡片啊！"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/0400680.ogg"
    cyl "这是长的像卡片一样的自动铅笔。"
    play voice "voice/学生会长/0200760.ogg"
    xshz "那这个要按哪里才能出笔芯呢？"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400690.ogg"
    cyl "那里。"
    show xshz_xzf_b1 b1 b1_a1
    play voice "voice/学生会长/0200770.ogg"
    xshz "哪里啊？"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/0400700.ogg"
    cyl "再远一点。"
    play voice "voice/学生会长/0200780.ogg"
    xshz "这里？"
    show ts_lian_ssz_b1 b1 b1_h2
    play voice "voice/天使莲/0400710.ogg"
    cyl "笨蛋才能看见~"
    show xshz_xzf_b1 b1 b1_ga2
    play voice "voice/学生会长/0200790.ogg"
    xshz "......能不能请你到教导处来一下呢。"
    me01 "这是塔罗牌吧？"
    show xshz_xzf_b1 b1 b1_sp1
    play voice "voice/学生会长/0200800.ogg"
    xshz "塔罗牌，是占卜术用的卡片吗？"
    hide taluo_card
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/0400720.ogg"
    cyl "你要占卜吗？"
    show xshz_xzf_b1 b1 b1_s1
    play voice "voice/学生会长/0200810.ogg"
    xshz "不需要。"
    play voice "voice/天使莲/0400730.ogg"
    cyl "将来你的头发会变成金色的。"
    show xshz_xzf_b1 b1 b1_ga2
    play voice "voice/学生会长/0200820.ogg"
    xshz "这是什么意思！"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400740.ogg"
    cyl "占卜的结果你是个傲娇。"
    show xshz_xzf_b1 b1 b1_sp2
    play voice "voice/学生会长/0200830.ogg"
    xshz "能不要擅自决定吗？！" with vpunch
    show ts_lian_ssz_b1 b1 b1_ga1
    play voice "voice/天使莲/0400750.ogg"
    cyl "希望能快点娇起来。"
    show xshz_xzf_b1 b1 b1_ga1
    play voice "voice/学生会长/0200840.ogg"
    xshz "不如说我只能傲了！"
    hide xshz_xzf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "那个......这种事情占卜是算不出来的吧？"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/0400760.ogg"
    cyl "这是占傲娇术。"
    me01 "没有这种占卜吧？"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/0400770.ogg"
    cyl "吵死了。"
    "吵、吵死了？！"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/0400780.ogg"
    cyl "贵安~"
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2 at walkout_l(0.7)
    pause 1.0 hard
    "莲趁机把塔罗牌从她手里抢了回来，迅速地跑向了教学楼。"
    stop music fadeout 5.0
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xshz_xzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.5
        xzoom -1
    play voice "voice/学生会长/0200850.ogg"
    xshz "等等啊！还没说完......"
    play sound rill
    pause 2.0 hard
    "就在这个时候，铃声响了。"
    with vpunch
    show xshz_xzf_b1 b1 b1_ga2
    play voice "voice/学生会长/0200860.ogg"
    xshz "都打铃了啊！明明接下来还要去学生会办公室处理被抓的学生名单啊！"
    me01 "辛、辛苦了。"
    show xshz_xzf_b1 b1 b1_a1
    play voice "voice/学生会长/0200870.ogg"
    xshz "上课迟到的损失你要怎么赔我啊！"
    show xshz_xzf_b1 b1 b1_n1
    play voice "voice/学生会长/0200880.ogg"
    xshz "刚刚那个孩子的名字，是苍衣吧。"
    show xshz_xzf_b1 b1 b1_s1
    play voice "voice/学生会长/0200890.ogg"
    xshz "苍......衣......莲。好了，之后再去班级里把她找出来。"
    me01 "既然这样......还请允许我先走一步了！"
    hide xshz_xzf_b1
    $ flcam.move(0, -600, 1200, duration=1.5, warper='easeout_quint')
    play sound run_1
    pause 1.5 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua
    with dissolve
    "在对方即将把矛头转向我的那一刻，我撒开腿向着教学楼的方向跑去。"
    "尽管身后就是学生会同学尖锐的叫喊声。"
    "对不住了，正义的干部大人！"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard

label day03.school_event02:
    scene set only school day road yinghua
    with dissolve
    pause 2.0 hard
    scene set only school day room2 yinghua
    with dissolve
    pause 2.0 hard
    play music first_06 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/0103650.ogg"
    rxl "终于等到了，放学的时间！"
    play voice "voice/日向怜/0103660.ogg"
    rxl "提问 ： 说到放学会想到什么呢？"
    show rxl_xzf_b1 b1 b1_n3
    play voice "voice/日向怜/0103670.ogg"
    rxl "小凉，你知道吗？"
    me01 "是社团活动吧？"
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.3)
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0501660.ogg"
    lingyin "说到樱华校放学后的事情，就是社团活动呢~"
    show rxl_xzf_b1 b1 b1_h1
    play voice "voice/日向怜/0103680.ogg"
    rxl "小凉和小铃回答正确！"
    hide lingyin_xzf_b1
    show yczs_xzf_b1 b1 b1_ga1 onlayer m2 at walkin_r(0.7)
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1600800.ogg"
    yczs "今天又要参加纸牌部的活动了吗？"
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0103690.ogg"
    rxl "这种社团不存在的吧！我们可是樱华校代代相传的天协部员啊！"
    show yczs_xzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1600810.ogg"
    yczs "天妇罗爱好者协会，简称天协~"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_c1 onlayer m2:
        xpos 0.5
    show han onlayer m2:
        xalign 0.47 yalign 0.37
    play voice "voice/日向怜/0103700.ogg"
    rxl "是天体观测爱好者协会啊！"
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0501670.ogg"
    lingyin "将来大概会改名成天文部或者天体观测部。"
    show yczs_xzf_b1 b1 b1_n1
    play voice "voice/一诚总司/1600820.ogg"
    yczs "这样的话就不叫天协而变成天部了吧。"
    show lingyin_xzf_b1 b1 b1_h1
    play voice "voice/青木铃音/0501680.ogg"
    lingyin "和天上的神仙有一样的名号呢~"
    hide han
    hide rxl_xzf_b1
    show rxl_xzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0103710.ogg"
    rxl "在天文爱好者来看真是个光荣的名号呢。"
    me01 "毕竟天文活动和神话本来就是相互关联的。"
    hide rxl_xzf_b2
    hide yczs_xzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0501690.ogg"
    lingyin "听日向同学说，神野同学似乎是打算加入天协吧？"
    me01 "如果不嫌弃的话请多多关照。"
    hide lingyin_xzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.7
    with vpunch
    play voice "voice/一诚总司/1600830.ogg"
    yczs "{size=72}你说什么！？{/size}"
    me01 "别突然叫那么大声啊。"
    show yczs_xzf_b1 b1 b1_h1
    play voice "voice/一诚总司/1600850.ogg"
    yczs "为什么不和我一起揣着幽灵探测器冲入废弃的墓地开始充满惊奇的旅行啊！"
    me01 "谁要做那么危险又不讨好的社团活动啊。"
    show yczs_xzf_b1 b1 b1_sp2
    play voice "voice/一诚总司/1600860.ogg"
    yczs "好过分！"
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/日向怜/0103720.ogg"
    rxl "那么也差不多该去活动室了~"
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0501700.ogg"
    lingyin "一诚同学，那么我们明天学校再见吧~"
    me01 "这样好了，下次我答应和你一起去冒险。"
    hide lingyin_xzf_b2 
    hide rxl_xzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_xzf_b1 b1 b1_a1
    play voice "voice/一诚总司/1600870.ogg"
    yczs "说好了哦，我们可是约好了的，千万别忘记了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard

label day03.starview_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky evening yinghua
    with slowdissolve
    pause 3.0 hard
    scene set only sky night yinghua2
    with slowdissolve
    pause 3.0 hard
    "社团活动结束已经很晚了。"
    "天体观测爱好者协会，除了一些简单的天文知识科普以外，大部分的时间都是在聊天。"
    "还期待一个由学生组成的社团能够有什么大的动作，我果然还是太天真了。"
    "毕竟在我心中真正称得上“天协”的也许就只有这座观景台而已。"
    "在这里可是能够亲眼目睹即便是依靠科学和精密的仪器都无法捕捉到的，最美丽的星空。"
    play ambience1 zhiliao fadein 5.0
    play sound move_1
    play music first_19 fadein 3.0 if_changed
    pause 1.0 hard
    scene set only starview night road
    with dissolve
    pause 2.0 hard
    "告别了学校的众人，我依照惯例独自一人向着观景台的方向走去。"
    "雷亚她到底是幻觉还是真实存在的呢？"
    "虽然见过了两次面，但每次告别的方式都让我感到惊讶。"
    "如果她真的只是我的幻觉，那至今为止我与雷亚的所有遭遇在别人眼里不就成了自言自语的闹剧了吗？"
    "真是让人无法接受的结论啊。"
    pause 1.0 hard
    scene set only starview night starview
    with right2left
    pause 2.0 hard
    "正如活动的时候大家说的那样，今晚的夜空格外明朗。"
    "不需要过多地集中注意力就能够清楚地看见漫天的星辰。"
    "这是第几次了呢？"
    "上一次满怀期待地在这么近的距离仰望星空......又是什么时候的事情呢？"
    pause 1.0 hard
    stop music fadeout 5.0
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 4.0 hard
    play music first_27 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only xz_memory piecethree yinghua
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0601030.ogg"
    tiny_xz "中午好，凉君。"
    me01 "这个时间已经到该说晚上好的时候了。"
    play voice "voice/翔子/0601040.ogg"
    tiny_xz "注意得真仔细呢，凉君。"
    me01 "是这样吗？"
    play voice "voice/翔子/0601050.ogg"
    tiny_xz "嗯，细心的，书呆子。"
    me01 "你这是在夸我吗？"
    play voice "voice/翔子/0601060.ogg"
    tiny_xz "嗯。"
    play voice "voice/翔子/0601070.ogg"
    tiny_xz "所以只要我和凉君加在一起的话，一定可以成为这座小镇上最优秀的学生了吧。"
    me01 "我在学校里也经常被大家称作优等生的。"
    play voice "voice/翔子/0601080.ogg"
    tiny_xz "那都是骗人的，不能被骗了。"
    me01 "我觉得他们应该不会骗我吧。"
    play voice "voice/翔子/0601090.ogg"
    tiny_xz "凉君，被谁说成是优等生呢？"
    me01 "班主任老师......之类的。"
    play voice "voice/翔子/0601100.ogg"
    tiny_xz "那个人就是万恶之源啊。"
    me01 "没有的事，老师是非常好的人。"
    play voice "voice/翔子/0601110.ogg"
    tiny_xz "让你这么认为就是那家伙的目的。"
    me01 "这话说的有些过分了吧。"
    play voice "voice/翔子/0601120.ogg"
    tiny_xz "不行啊凉君，要小心不能被那甜言蜜语蛊惑才行。"
    me01 "为什么要把他们说的那么坏呢？"
    pause 1.0 hard
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    "“她”抬头望向夜空中那宛若炸面包状的星云说道。"
    play voice "voice/翔子/0601130.ogg"
    tiny_xz "......老师就是这么回事的嘛。"
    "一边说着，一边就像是要从银河摘取星辰一般地，伸出了她那双纤细的手臂。"
    play voice "voice/翔子/0601140.ogg"
    tiny_xz "学校什么的，就是这么回事的啊。"
    me01 "你讨厌上学吗？"
    play voice "voice/翔子/0601150.ogg"
    tiny_xz "......"
    pause 1.0 hard
    scene set only xz_memory piecethree yinghua
    with dissolve
    pause 1.0 hard
    "她把视线从星空移回到了我的身上。"
    play voice "voice/翔子/0601160.ogg"
    tiny_xz "凉君。"
    me01 "怎么了？"
    $ flcam.move(800, -1100, 400, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0601170.ogg"
    tiny_xz "凉君你呢，才不是什么优等生。"
    play voice "voice/翔子/0601180.ogg"
    tiny_xz "所以呢，我会教你的。"
    $ flcam.move(1100, -1400, 500, duration=0.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0601190.ogg"
    tiny_xz "为了让凉君你能够成为真正的优等生，作为姐姐的我会教给凉君更多东西的。"
    "明明比我年幼却总是自称“姐姐”。"
    me01 "教我什么？"
    play voice "voice/翔子/0601200.ogg"
    tiny_xz "凉君不知道的事情。"
    me01 "什么样的事情？"
    play voice "voice/翔子/0601210.ogg"
    tiny_xz "这得等到凉君成为了真正的优等生之后才能告诉你。"
    play voice "voice/翔子/0601220.ogg"
    tiny_xz "所以呢，现在还是秘密。"
    play voice "voice/翔子/0601230.ogg"
    tiny_xz "在凉君成为真正的优等生，稍微再长大一些之前，这还是秘密哟~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    "在那之后，我也许真的从她那里学到了不少东西。"
    "两人一起仰望星空的这个夏季。"
    "跟她在一起这件事情本身，即使经历了岁月的洗礼，仍然能够使我感到快乐。"
    stop music fadeout 5.0
    "我说不定，真的能够成为优等生。"
    pause 2.0 hard
    scene white
    with dissolve
    pause 3.0 hard
    play voice "voice/天使雷亚/0000960.ogg"
    lst "中午好，凉君——"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play music first_23 fadein 3.0 if_changed
    scene set only lisite_cg normal
    with in2out_v2_slow
    pause 2.0 hard
    "见到她之后的第一句话是这样的。"
    "眼前的一幕又与回忆重合了。"
    me01 "已经到了该说晚上好的时间了。"
    play voice "voice/天使雷亚/0000970.ogg"
    lst "注意得真仔细呢，凉君。"
    me01 "是这样吗？"
    play voice "voice/天使雷亚/0000980.ogg"
    lst "嗯，细心的，书呆子。"
    me01 "果然是这样吗？"
    play voice "voice/天使雷亚/0000990.ogg"
    lst "嗯。"
    me01 "我和你加在一起的话，就能成为这座小镇上最优秀的学生了吧？"
    play voice "voice/天使雷亚/0001000.ogg"
    lst "不会哟。"
    "她否定了。"
    play voice "voice/天使雷亚/0001010.ogg"
    lst "死神才不会成为优等生呢。"
    me01 "我小的时候可是经常被大家称作优等生的。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0001020.ogg"
    lst "是这样吗？"
    me01 "但实际上我除了学习以外，其他地方可能都达不到优秀甚至及格的水平。"
    play voice "voice/天使雷亚/0001030.ogg"
    lst "呼嗯~"
    me01 "所以当时也没有什么朋友愿意和我一起玩。"
    me01 "转校回来的这几天我突然有了许多的朋友。甚至就连那个傲娇的学生会委员长，对我的评价也是很高的呢。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001040.ogg"
    lst "傲娇的学生委员长是谁？"
    me01 "是个说不定会喜欢我的女孩子。"
    pause 0.1 hard
    scene set only lisite_cg daze 
    with dissolve
    play voice "voice/天使雷亚/0001050.ogg"
    lst "......"
    me01 "过去的我完全没有察觉到这样的感情。"
    play voice "voice/天使雷亚/0001060.ogg"
    lst "是吗。"
    me01 "我并不是恋爱方面的优等生。"
    me01 "所以......"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001090.ogg"
    lst "所以，怎么样？"
    me01 "没什么。"
    "这是不能轻易就说出口的事情。"
    "毕竟眼前的女孩并不是翔子。"
    "虽然有很多跟记忆重合的地方，但是从现实的角度出发她们都不可能是同一个人。"
    me01 "雷亚你......是本地人吗？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0001100.ogg"
    lst "突然之间怎么了？"
    me01 "如果惹你不开心了的话我道歉，但我真的很在意。"
    play voice "voice/天使雷亚/0001110.ogg"
    lst "为什么在意呢？"
    me01 "因为你的名字，很少见。"
    play voice "voice/天使雷亚/0001120.ogg"
    lst "是这样吗？"
    me01 "嗯。"
    play voice "voice/天使雷亚/0001130.ogg"
    lst "嘛......毕竟我可不是日本人。"
    me01 "那果然是外国人吗？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001140.ogg"
    lst "不，是死神。"
    me01 "国籍呢？护照呢？"
    play voice "voice/天使雷亚/0001150.ogg"
    lst "死神才没有什么国籍呢。"
    me01 "你住在哪里？"
    play voice "voice/天使雷亚/0001160.ogg"
    lst "死神才没有住处呢。"
    me01 "你一直是这样......一个人吗？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0001170.ogg"
    lst "不行吗？"
    me01 "也不是不行。"
    me01 "如果你觉得我是坏人不想告诉我的话就算了。"
    play voice "voice/天使雷亚/0001180.ogg"
    lst "没有什么想不想说的，刚刚不是都回答你了吗？"
    me01 "那我走了之后你就会回去吗？"
    play voice "voice/天使雷亚/0001190.ogg"
    lst "死神才不需要回家呢。"
    "好像无论什么事都可以用“死神”这一说法来敷衍过去。"
    me01 "你身上的服饰，非常地奇特啊。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0001200.ogg"
    lst "是这样吗？"
    me01 "嗯。"
    pause 0.1 hard
    scene set only lisite_cg happy
    with dissolve
    play voice "voice/天使雷亚/0001210.ogg"
    lst "因为我是死神嘛~"
    me01 "你平时在街上不会也这么穿吧？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001220.ogg"
    lst "死神才不会上街呢。"
    me01 "那把镰刀，不觉得很重吗？"
    play voice "voice/天使雷亚/0001230.ogg"
    lst "不会啊。"
    me01 "你为什么会拿着那样的东西出门呢？"
    play voice "voice/天使雷亚/0001240.ogg"
    lst "不知道。"
    me01 "是因为死神所以才拿着镰刀？"
    play voice "voice/天使雷亚/0001250.ogg"
    lst "说不定是这样没错，也说不定不是。我醒来的时候就已经拿着了。"
    me01 "你说它是用来割取噩梦的是吧？"
    play voice "voice/天使雷亚/0001260.ogg"
    lst "嗯。"
    me01 "这么有趣的设定是从小说里面看到的？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0001270.ogg"
    lst "一直以来我就怀疑，你压根就没相信过我是死神吧。"
    me01 "没有的事。"
    play voice "voice/天使雷亚/0001290.ogg"
    lst "看着你那敷衍的表情总觉得很不爽。"
    me01 "那个，你能稍微把眼睛闭起来吗？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0002450.ogg"
    lst "......诶？"
    me01 "闭上眼睛。"
    play voice "voice/天使雷亚/0002460.ogg"
    lst "为什么？"
    me01 "不为什么。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0002470.ogg"
    lst "不要。"
    "被拒绝了。"
    me01 "雷亚你总说我不相信你是死神，可自己却不肯配合我。"
    play voice "voice/天使雷亚/0002480.ogg"
    lst "嗯。"
    me01 "明明只要闭上眼睛就好了，就一小会儿，哥哥我可是有奖励的哟。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0002490.ogg"
    lst "不要。"
    "这个混账。"
    play voice "voice/天使雷亚/0002500.ogg"
    lst "这个世界上我最最讨厌的事情之一就是被别人命令了，所以不要！"
    "如果这一切都是我的幻觉那还真是相当棘手啊。"
    me01 "究竟要怎样你才肯闭上眼睛呢？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0002510.ogg"
    lst "不如说为什么我非得闭上眼睛不可啊？"
    me01 "因为我要做一个实验。"
    play voice "voice/天使雷亚/0002520.ogg"
    lst "那是什么？"
    me01 "连实验都不知道吗？"
    play voice "voice/天使雷亚/0002530.ogg"
    lst "能砍了你吗？"
    me01 "玩笑归玩笑，可别真的拿起镰刀啊！"
    play voice "voice/天使雷亚/0002540.ogg"
    lst "今天的你笨笨的呢。"
    "和废废的相比哪个更糟。"
    me01 "雷亚你是死神吧？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0002550.ogg"
    lst "既然你都这么说了，就当是这样吧。"
    me01 "我呢，并不相信死神这种超自然的存在。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0002560.ogg"
    lst "明明是你自己先说的。"
    me01 "但是呢，如果做了那个实验的话，我大概就能相信雷亚的话都是真的了。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0002570.ogg"
    lst "......是这样吗？"
    me01 "没错。"
    "看她的表情似乎有些动摇了。"
    me01 "拜托了，这并不是命令而是请求。我希望能够把雷亚当成真正的死神来对待。"
    me01 "能够当做真正的......朋友一样对待。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0002580.ogg"
    lst "这样的话就算我不是死神也无所谓吧。"
    me01 "但是到目前为止我始终觉得雷亚你的存在对我而言就是一个幻觉。"
    play voice "voice/天使雷亚/0002590.ogg"
    lst "幻觉？"
    me01 "如果你真的只是我幻想出来的话，那我也没有必要特意为了一个不存在的人每天都来这里。"
    me01 "难道不是这样的吗？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0002600.ogg"
    lst "为、为什么会变成这样啊！"
    me01 "雷亚也觉得自己不是幻觉对吧？"
    play voice "voice/天使雷亚/0002610.ogg"
    lst "这是当然的吧，我就好好地在这里存在着的啊。"
    me01 "就算你这么说，我也不能仅凭你的几句话就轻易相信。"
    me01 "所以说，只要你肯闭上眼睛的话一切就都会解决了。"
    play voice "voice/天使雷亚/0002620.ogg"
    lst "......"
    me01 "很快就结束的。"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0002630.ogg"
    lst "......真的？"
    me01 "真的。"
    play voice "voice/天使雷亚/0002640.ogg"
    lst "骗我的话能砍了你吗？"
    me01 "到时候随你怎么处置都可以。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0002650.ogg"
    lst "嗯。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    with dissolve
    "虽然依旧有些犹豫，但雷亚还是闭上了眼睛。"
    play sound move_2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    "我一步一步地向前走去，来到她的跟前。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    "大概是察觉到了我的气息，雷亚下意识地退后了几步。"
    "但是尽管如此还是遵守约定紧闭着双眼。"
    "我来到她跟前，从微微颤抖的肩膀可以察觉到她的不安。"
    "和小孩子差不多的身高。"
    "稚气的脸庞。"
    "果然和小时候的翔子一样，非常的可爱。"
    stop music fadeout 5.0
    "让我不由得觉得平时用大人的口吻说话，也只是她在逞强罢了。"
    pause 1.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 4.0 hard
    play music first_31 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    "我抱了上去。"
    "胸口处先是传来了一阵颤抖。"
    "随之而来的是温暖的触感。"
    "那是绝不同于幻觉所能带来的温暖。"
    "柔软、纤细。"
    "或许这一切打一开始就是场美丽的梦幻也说不定。"
    "包含着思念、渴望和美好的......温柔的骗局。"
    "仔细一想的话，这样的实验的意义就不成立了。"
    "如果说这份温暖并不是现实而是梦境的话，也实在是太令人感到可惜了吧。"
    play voice "voice/天使雷亚/0002660.ogg"
    lst "一......"
    stop music fadeout 5.0
    "耳边传来了雷亚的声音。"
    play voice "voice/天使雷亚/0002670.ogg"
    lst "一、一、一、一......"
    me01 "一？"
    play voice "voice/天使雷亚/0002680.ogg"
    lst "你打算一直抱到什么时候啊！！"
    play sound punch
    with vpunch
    "{size=72}磅！！{/size}"
    pause 1.0 hard
    scene set only starview night starview
    with dissolve
    pause 1.0 hard
    me01 "好痛！"
    me01 "你干什么啊！"
    play music first_12 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2_d b2 b2_a1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/天使雷亚/0002690.ogg"
    lst "这、这是我的台词吧！"
    me01 "刚刚是用刀柄敲的我吗？"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_a2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0002700.ogg"
    lst "不是用锋利的那一端你还真得感谢我！"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0002710.ogg"
    lst "刚、刚刚那是......什么？"
    me01 "实验啊。"
    show ts_lst_ssz_b1_d b1 b1_a1
    play voice "voice/天使雷亚/0002720.ogg"
    lst "才没听说过这种实验！"
    show ts_lst_ssz_b1_d b1 b1_s2
    play voice "voice/天使雷亚/0002730.ogg"
    lst "没、没听说过要拥抱的。"
    me01 "雷亚不是说愿意配合我的吗？"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0002740.ogg"
    lst "这种事情才不可能！"
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.1 hard
    show ts_lst_ssz_b1_d b1 b1_s1 at flu_down(0.25, 20):
        xpos 0.5
    "我缓缓地站起身，雷亚随即惊慌地后退了几步。"
    me01 "这样的反应会让我很受伤的。"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0002750.ogg"
    lst "明、明明是你自己不好。"
    me01 "嘛，没有提前告诉你实验的内容是我不对。"
    show ts_lst_ssz_b3 b3 b3_s1
    play voice "voice/天使雷亚/0002760.ogg"
    lst "就算道歉了也不原谅你的。"
    show ts_lst_ssz_b3 b3 b3_a1
    play voice "voice/天使雷亚/0002770.ogg"
    lst "如、如果你敢有第二次的话，绝对不会原谅你的！"
    me01 "抱歉，是我不好。"
    hide ts_lst_ssz_b3
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0002780.ogg"
    lst "......"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0002790.ogg"
    lst "能明白我不是幻觉就好。"
    me01 "不、确切的来说还没有办法证明。"
    pause 0.1 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    hide ts_lst_ssz_b1 with None
    pause 0.1 hard
    play sound liandao
    show ts_lst_ssz_b1_d b1 b1_a1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/天使雷亚/0002800.ogg"
    lst "你说什么！"
    me01 "等等等等，先把镰刀放下啊喂！"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0002810.ogg"
    lst "因为这和刚开始说好的不一样！"
    me01 "我原本也以为只要这样就能够确认的，但是仔细思考了之后发现证据还不够。"
    show ts_lst_ssz_b2_d b2 b2_ga1
    play voice "voice/天使雷亚/0002820.ogg"
    lst "也就是说你只是单纯想惹我生气是吧......"
    me01 "冷静一点，镰刀已经架到脖子上了啊！"
    show ts_lst_ssz_b2_d b2 b2_a1
    play voice "voice/天使雷亚/0002830.ogg"
    lst "再有下次就直接砍下去。"
    me01 "明白了，我发誓、我会发誓的！"
    $ flcam.move(0, -150, 750, duration=1.5)
    show ts_lst_ssz_b2_d b2 b2_a1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    "雷亚缓缓移开了手里的镰刀。"
    show ts_lst_ssz_b2_d b2 b2_s1
    play voice "voice/天使雷亚/0002840.ogg"
    lst "真是的......吓了我一跳。"
    me01 "那么事不宜迟，我们开始下一个实验吧。"
    play sound liandao
    $ flcam.move(0, 0, 900, duration=1.5)
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_a1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/天使雷亚/0002850.ogg"
    lst "你没听清我刚才说的话吗！"
    "镰刀又回到脖子上了。"
    me01 "不是的不是的，并不是拥抱实验！"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0002860.ogg"
    lst "那你还想做什么呢，变态君？"
    "好像解锁了奇怪的称号啊。"
    stop music fadeout 3.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    play music first_08 fadein 3.0 if_changed
    me01 "雷亚你知道七夕吗？"
    play voice "voice/天使雷亚/0001300.ogg"
    lst "知道啊。"
    me01 "真的吗？"
    play voice "voice/天使雷亚/0001310.ogg"
    lst "嗯。"
    me01 "我以为不是什么法定假日，大家一定不会去注意的。"
    play voice "voice/天使雷亚/0001320.ogg"
    lst "毕竟也不是什么重要到值得在意的日子。"
    me01 "对于一般人确实是这样吧。"
    play voice "voice/天使雷亚/0001330.ogg"
    lst "嗯。"
    pause 1.0 hard
    scene set only lisite_cg normal
    with dissolve
    pause 1.0 hard
    me01 "七月七日，一年中只有在这一天，牛郎和织女才可以相会。"
    me01 "雷亚你也喜欢星星吧？"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0001370.ogg"
    lst "并没有。"
    me01 "在闹什么别扭啊？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0001380.ogg"
    lst "才、才没有在闹别扭！"
    me01 "那你是在生闷气吗？"
    play voice "voice/天使雷亚/0001390.ogg"
    lst "生、生闷气什么的......"
    me01 "哈哈。"
    play voice "voice/天使雷亚/0001400.ogg"
    lst "你在笑什么啊！"
    me01 "等等，先别急着举起镰刀。"
    me01 "再怎么说一个女孩子家总拿那玩意儿指着别人是会被嫌弃的。"
    play voice "voice/天使雷亚/0001410.ogg"
    lst "被你当作小孩子一样说教真是让人不爽！"
    me01 "虽然是想把你当成同级生看待的，但是你刚才的所作所为完全就是小孩子嘛。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0001420.ogg"
    lst "我才不是小孩子......"
    me01 "我知道，是死神吧。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0001430.ogg"
    lst "把我当成笨蛋更让我不爽了！"
    play voice "voice/天使雷亚/0001440.ogg"
    lst "早知道就应该快点把你的噩梦给割掉了。（小声）"
    "她转过头去，嘴里小声嘟囔着什么。"
    me01 "果然是刚才的事情惹你不开心了？"
    play voice "voice/天使雷亚/0001450.ogg"
    lst "怎么样都行吧！不用你管！"
    me01 "这个点了还不回家吗？"
    play voice "voice/天使雷亚/0001470.ogg"
    lst "死神才不需要回家呢。"
    me01 "那、我可是要回去了哟。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0001480.ogg"
    lst "这样啊。"
    me01 "明天还能再见到你吗？"
    play voice "voice/天使雷亚/0001490.ogg"
    lst "不知道。"
    play voice "voice/天使雷亚/0001500.ogg"
    lst "在你回去之前可以让我捅一下吗？"
    me01 "当然不行。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0001510.ogg"
    lst "果然还是应该在你没有察觉的情况下朝你的背上狠狠地来一刀吗。（小声？）"
    "我听到了啊！"
    me01 "那个，雷亚。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    "女孩继续用她那双深邃的眼睛注视着我。"
    me01 "和我一起走吧？"
    pause 0.5 hard
    scene set only lisite_cg surprise
    with dissolve
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    me01 "我送你回家。"
    play voice "voice/天使雷亚/0001520.ogg"
    lst "......"
    me01 "时间已经很晚了，一个人走夜路的话很危险的。"
    pause 0.1 hard
    scene set only lisite_cg happy
    with dissolve
    play voice "voice/天使雷亚/0001530.ogg"
    lst "毕竟是男孩子呢~"
    play voice "voice/天使雷亚/0001540.ogg"
    lst "再见了，凉君。"
    play voice "voice/天使雷亚/0001550.ogg"
    lst "刚刚本来是打算在你转身的瞬间狠狠地捅你一刀的，看来是没有那个机会了。"
    play voice "voice/天使雷亚/0001560.ogg"
    lst "你的噩梦，相当的棘手呢。"
    stop ambience1 fadeout 3.0
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 1.0 hard
    $ suppress_overlay = True
    jump day04
