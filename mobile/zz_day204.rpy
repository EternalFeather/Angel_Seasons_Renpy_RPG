
label inside_battle1(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "战斗过程采用回合制对战。"
    show hintarrow onlayer m1:
        xpos 0.85
        ypos 0.85
    "该区域为角色行动区域。"
    "可通过选择技能来触发该角色本轮的行动。"
    hide hintarrow
    pause 0.5 hard
    show hintarrow onlayer m1:
        xpos 0.25
        ypos 0.85
    "该区域为角色状态区域。"
    "用以显示战斗中我方角色的状态信息，另外通过「菜单」按钮也可唤起角色菜单查看具体属性状态或使用道具、自动作战等功能。"
    hide hintarrow
    pause 0.5 hard
    show hintarrow2 onlayer m1:
        xpos 0.35
        ypos 0.38
    "该区域为敌方状态区域。"
    "用以显示战斗中敌方角色的状态信息。"
    pause 0.5 hard
    show hintarrow2 onlayer m1:
        xpos 0.78
        ypos 0.38
    "该区域为行动顺序区域。"
    "用以显示接下来将会行动的角色顺序。"
    "越靠近左边的角色将会优先行动。"
    hide hintarrow2
    pause 0.5 hard
    "双方队伍中最多各存在「六」名角色参与战斗，其中「三」名在场，「三」名候补。"
    "当有在场角色阵亡时，将会由候补队员替补上阵。"
    "玩家也可根据局势自行更换候补角色上场，但同时会损失该角色的行动回合。"
    "游戏的胜负有多种不同的形式，请合理根据游戏胜负判定规划战斗。"
    "本次战斗属于教学战斗，请根据指示完成熟悉相应的战斗机制。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_battle2(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "本次战斗需要在确保我方一诚小桃存活的情况下击倒对手。"
    "合理利用雷亚的{color=#f00}守护结界{/color}保护小桃。"
    "同时借助结界提供的{color=#f00}连击{/color}配合{color=#9cf}融化反应{/color}进行输出是制胜的关键。"
    "{color=#f00}友情提示{/color}：通过「右键」唤起菜单选项中的「加速」按钮可以提升战斗特效的播放速度，改善作战效率和体验。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label day204:
    bookmark
    $ save_name = _("Day 204")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    pause 2.0 hard
    show backend_date203 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    $ suppress_overlay = False
    pause 2.0 hard
    scene set only sky day xuejian2
    with dissolve
    play music second_112 fadein 3.0 if_changed
    pause 2.0 hard
    play sound close_door3
    pause 1.0 hard
    scene set only home day outside xuejian
    with dissolve
    pause 1.0 hard
    play sound jiaobu2
    pause 1.0 hard
    scene set only bridge day xuejian
    with dissolve
    pause 1.0 hard
    "自从来到了这座城市，还是很少有机会像现在这样一人走在街上。"
    "也许正如希菲尔说的那样，此刻的我已不再是孤单一人了。"

label day204.bridge_event01:
    $ flcam.move(0, 0, 0)
    me01 "那是？"
    pause 1.0 hard
    scene set only yj_cg daze2
    with dissolve
    pause 1.0 hard
    "桥下的河滩十分开阔，连接着环城的运河。"
    "友加就蹲在河滩边上，静静地望着流淌的河水发呆。"
    stop music fadeout 5.0
    me01 "你在这里做什么？"
    pause 0.1 hard
    scene set only yj_cg sp2
    $ flcam.move(-2200, -1400, 450, duration=1.0, warper='ease_cubic')
    pause 1.0 hard
    with vpunch
    play voice "voice/植澄友加/020102340.ogg"
    yj "{size=72}呜哇！{/size}"
    pause 1.0 hard
    scene set only bridge day under xuejian
    play music second_119 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_tcf_b3 b3 b3_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/植澄友加/020102350.ogg"
    yj "这不是凉君吗......"
    me01 "哟~刚好路过这里就顺便来打个招呼。"
    show yj_tcf_b3 b3 b3_ga2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/020102360.ogg"
    yj "吓了我一跳，害我差点就掉进河里啦~"
    me01 "那真是抱歉。"
    me01 "话说回来为什么穿着体操服？"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102490.ogg"
    yj "穿体操服的话肯定是因为要跑步啊~"
    me01 "社团活动？"
    show yj_tcf_b2 b2 b2_n3
    play voice "voice/植澄友加/020102500.ogg"
    yj "算是自主练习吧。因为考试期间社团活动暂停了，身体变得迟钝的话就不好了。"
    me01 "考试的准备都没问题了吗？"
    hide yj_tcf_b2
    show yj_tcf_b3 b3 b3_ga4 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102520.ogg"
    yj "额......这个嘛。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg daze2
    with dissolve
    pause 1.0 hard
    "友加没有回答，只是转身蹲到河边继续望着水面发呆。"
    "这也算是一种回应了吧。"
    me01 "你手里的是什么？"
    pause 0.1 hard
    scene set only yj_cg sad2
    with dissolve
    play voice "voice/植澄友加/020102540.ogg"
    yj "......被看见了。"
    me01 "毕竟从刚才就看你一直盯着河面看，换作是谁都会很好奇的。"
    "友加把捏在手里的编制物放到了河面上。"
    pause 0.1 hard
    scene set only yj_cg normal3
    with dissolve
    play voice "voice/植澄友加/020102550.ogg"
    yj "与其说是盯着河面看，不如说是在做这个。"
    me01 "这是？"
    play voice "voice/植澄友加/020102560.ogg"
    yj "草船哟。"
    play voice "voice/植澄友加/020102570.ogg"
    yj "很少见吗？小时候多少都会玩的，凉君以前没有玩过吗？"
    me01 "这个倒是没有。"
    "在我们说话之余，草船顺着河流缓缓飘向了远方。"
    pause 1.0 hard
    scene set only bridge day under xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_tcf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102590.ogg"
    yj "凉君你说过小的时候有来过这座城市对吧？"
    me01 "是啊。"
    show yj_tcf_b1 b1 b1_s2
    play voice "voice/植澄友加/020102600.ogg"
    yj "那没有来过这个河滩吗？感觉这座城市好像也没有其他的河了。"
    me01 "这点倒是没有太多的印象......"
    show yj_tcf_b1 b1 b1_s1
    yj "......"
    show yj_tcf_b1 b1 b1_n1
    play voice "voice/植澄友加/020102690.ogg"
    yj "稍微有些变冷了呢。"
    me01 "你这身打扮是理所当然的吧。"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102700.ogg"
    yj "不过，跑起来就暖和了~"
    me01 "在此之前还是先担心一下自己会不会着凉吧。"
    show yj_tcf_b2 b2 b2_h1
    play voice "voice/植澄友加/020102710.ogg"
    yj "没问题的啦，我可是很快就能火热起来的女孩呢~"
    "这样的发言还真是容易让人误会啊......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day204.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day center room xuejian
    with dissolve
    pause 1.0 hard
    play music second_115 fadein 3.0 if_changed
    "午饭的时候我依照约定来到中庭。"
    "不出我所料，琉璃已经在那里等我了。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b3 b3 b3_n3 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/040101420.ogg"
    liuli "啊，神野前辈~"
    play voice "voice/琉璃/040101430.ogg"
    liuli "顶着寒冷赶过来真是辛苦你了~"
    me01 "想到能和琉璃一起吃饭，这点困难算不了什么。"
    hide liuli_dzf_b3
    show liuli_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101440.ogg"
    liuli "长椅我已经暖好了。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_n2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/藤原瞳/130100170.ogg"
    tyt "花山院？"
    show liuli_dzf_b2 b2 b2_sp1
    play voice "voice/琉璃/040101500.ogg"
    liuli "啊，藤原同学~"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100180.ogg"
    tyt "还在想你怎么不见了，原来在这里啊。"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101510.ogg"
    liuli "你是在找我吗？"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/130100190.ogg"
    tyt "因为你不在教室所以有些在意。"
    show liuli_dzf_b3 b3 b3_n3
    play voice "voice/琉璃/040101520.ogg"
    liuli "我们接下来要在这里吃午饭。"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/130100210.ogg"
    tyt "明明在教室吃就行了。"
    show liuli_dzf_b3 b3 b3_s2
    play voice "voice/琉璃/040101540.ogg"
    liuli "那个......"
    stop music fadeout 5.0
    me01 "中庭也不差吧，毕竟这里比较安静。"
    show tyt_wnf_b1 b1 b1_n2
    "藤原瞳以极其疑惑的眼神看向我。"
    hide liuli_dzf_b3
    play music second_108 fadein 3.0 if_changed
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/130100230.ogg"
    tyt "......你谁？"
    me01 "我们在神社见过面的吧？！"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/130100240.ogg"
    tyt "附近的小孩子？"
    me01 "是大哥哥啦！"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/藤原瞳/130100250.ogg"
    tyt "我对自己的记忆力没有自信。"
    me01 "看出来了。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101560.ogg"
    liuli "这位是神野前辈哟~"
    with vpunch
    "若无其事地开始重新介绍了！？"
    me01 "为什么你在学校也穿着巫女服啊？"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/130100260.ogg"
    tyt "学校同意了~"
    show liuli_dzf_b2 b2 b2_h1
    play voice "voice/琉璃/040101570.ogg"
    liuli "我约好在这里和前辈一起吃午饭。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100270.ogg"
    tyt "这样的话我也来这里吃好了。"
    show liuli_dzf_b2 b2 b2_sp1
    play voice "voice/琉璃/040101580.ogg"
    liuli "欸，但是......"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/130100280.ogg"
    tyt "打扰的话我就回去了。"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101590.ogg"
    liuli "怎、怎么会打扰，只是这样的话不会冷吗？"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.25, 20, 2):
        xpos 0.3
    play voice "voice/藤原瞳/130100290.ogg"
    tyt "被你这么一说才注意到，这里的确冷到难以置信。"
    me01 "不是我说你，你发现得也太晚了吧？"
    hide liuli_dzf_b3
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/130100300.ogg"
    tyt "你谁？"
    me01 "别把自己的记忆丢到阴沟里去啊！"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/130100310.ogg"
    tyt "因为很冷，所以燃烧记忆来取暖。"
    me01 "你的身体到底是什么构造啊！"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101600.ogg"
    liuli "人类真是太伟大了。"
    me01 "这是应该吐槽的地方吗......"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/藤原瞳/130100320.ogg"
    tyt "好冷......好想睡。"
    play sound jump_1
    hide liuli_dzf_b3 with None
    pause 0.1 hard
    show liuli_dzf_b2 b2 b2_sp2 onlayer m2 at flu_up(0.15, 30):
        xpos 0.5
    play voice "voice/琉璃/040101610.ogg"
    liuli "藤原同学，在这种地方睡觉会死掉的。"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/藤原瞳/130100330.ogg"
    tyt "好想冬眠......"
    me01 "话说之前琉璃你没有和藤原同学一起吃过午饭吗？"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101620.ogg"
    liuli "是的，因为藤原同学中午的时候一直在睡觉。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/130100340.ogg"
    tyt "为了补充体力。"
    me01 "那午饭怎么办？"
    play voice "voice/藤原瞳/130100350.ogg"
    tyt "只要有氧气就能活下去。"
    me01 "你其实是宇宙人吧......"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/130100360.ogg"
    tyt "只要好好吃早饭，然后借助睡觉来抑制卡路里的消耗。"
    hide liuli_dzf_b3 with None
    pause 0.1 hard
    show liuli_dzf_b2 b2 b2_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/琉璃/040101630.ogg"
    liuli "果然人类真的好厉害，我太骄傲了！"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100370.ogg"
    tyt "今天偶然发现琉璃不在教室，于是就出来找了。"
    me01 "所以你也要和我们一起吃午饭吗？"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/130100380.ogg"
    tyt "我才发现自己什么吃的都没有带出来。"
    me01 "所以说你注意得太晚了！"
    show liuli_dzf_b2 b2 b2_n1
    play voice "voice/琉璃/040101640.ogg"
    liuli "不介意的话，要喝我的果汁吗？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/130100400.ogg"
    tyt "好不容易来到这里了，我会努力克服的。"
    me01 "除了记忆你还打算牺牲什么啊......"
    show liuli_dzf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/040101660.ogg"
    liuli "藤原同学，冷的话就请坐到长椅上来吧，我已经暖好了。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/130100410.ogg"
    tyt "帮大忙了~"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "就这样，两个人的午餐时光突然变成了三个人。"
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard

label day204.school_event02:
    $ flcam.move(0, 0, 0)
    play sound rill
    pause 1.0 hard
    scene set only school day corridor xuejian
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/0506220.ogg"
    stranger "请等一下，水之濑前辈。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001160.ogg"
    szl "我还想是谁呢，原来是青木妹妹啊。"
    play music first_22 fadein 3.0 if_changed
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show lingyin_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    play voice "voice/青木铃音/0506230.ogg"
    lingyin "你这是要回去了吗？"
    hide szl_dzf_b2
    show szl_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001170.ogg"
    szl "是啊。"
    show lingyin_dzf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0506240.ogg"
    lingyin "姐姐的演讲不打算参加了吗？"
    hide szl_dzf_b1
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001180.ogg"
    szl "她在练习时付出了多少努力，我之前就听你提到过了。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001190.ogg"
    szl "你没有理由说谎，而且凭借努力换来的成果失败可能性几乎为零。"
    hide lingyin_dzf_b2
    show lingyin_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0506250.ogg"
    lingyin "所以才没必要看吗？"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001200.ogg"
    szl "是啊。"
    show lingyin_dzf_b1 b1 b1_s1
    play voice "voice/青木铃音/0506260.ogg"
    lingyin "......早知道这样，我就不应该把姐姐每天练习的事情告诉前辈你的。"
    show szl_dzf_b2 b2 b2_n2
    play voice "voice/水之濑/1001210.ogg"
    szl "没有这回事，不管你说还是不说我都不会去看的。"
    play voice "voice/青木铃音/0506270.ogg"
    lingyin "......"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001220.ogg"
    szl "毕竟我接下来还有重要的工作要去完成。"
    hide lingyin_dzf_b1
    show lingyin_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0506280.ogg"
    lingyin "明白了，谢谢你一直以来帮助姐姐。"
    show szl_dzf_b3 b3 b3_n3
    play voice "voice/水之濑/1001250.ogg"
    szl "对了......姑且还是向你告知一下。"
    show lingyin_dzf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0506310.ogg"
    lingyin "......什么事？"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001260.ogg"
    szl "之前我去了你说的观景台，但是没有见到你所说的“死神”。"
    show lingyin_dzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0506320.ogg"
    lingyin "那一定是因为害怕水之濑前辈，所以躲起来了吧。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001270.ogg"
    szl "......我看上去很可怕吗？"
    show lingyin_dzf_b2 b2 b2_ga2
    play voice "voice/青木铃音/0506330.ogg"
    lingyin "不是的，根据神野同学的描述来看，对方是有点怕生的性格。"
    show szl_dzf_b3 b3 b3_s1
    play voice "voice/水之濑/1001280.ogg"
    szl "这一点还真像人啊。"
    hide lingyin_dzf_b2
    show lingyin_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0506390.ogg"
    lingyin "......"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001330.ogg"
    szl "想说的话都说完了吗？"
    show lingyin_dzf_b1 b1 b1_s3
    play voice "voice/青木铃音/0506400.ogg"
    lingyin "那个......"
    show szl_dzf_b2 b2 b2_sp1
    play voice "voice/水之濑/1001340.ogg"
    szl "？"
    show lingyin_dzf_b1 b1 b1_n2
    play voice "voice/青木铃音/0506410.ogg"
    lingyin "我去见一下那位“死神”吧？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001350.ogg"
    szl "......可以吗？先不说在观景台的时候，现在的“她”似乎也不是你的敌人吧？"
    hide lingyin_dzf_b1
    show lingyin_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0506430.ogg"
    lingyin "不用担心。"
    play voice "voice/青木铃音/0506440.ogg"
    lingyin "就当是配合水之濑前辈的工作了。"
    show lingyin_dzf_b2 b2 b2_n2
    play voice "voice/青木铃音/0506450.ogg"
    lingyin "只要是为了姐姐的话，这点小事不算什么。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/1001360.ogg"
    szl "这样啊。"
    play voice "voice/青木铃音/0506460.ogg"
    lingyin "是的。"
    hide lingyin_dzf_b2
    show lingyin_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0506470.ogg"
    lingyin "水之濑前辈，如果“死神”的真面目真的如同总本社所说的那样，到时候......"
    show szl_dzf_b2 b2 b2_n3
    play voice "voice/水之濑/1001370.ogg"
    szl "我知道。"
    play voice "voice/水之濑/1001380.ogg"
    szl "到那时候......就抹杀掉。"
    show szl_dzf_b2 b2 b2_s4
    play voice "voice/水之濑/1001390.ogg"
    szl "对我们人类来说，那些只不过是梦幻罢了。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/1001400.ogg"
    szl "所以，是绝对不能允许她们出现在普通人的视线中的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day204.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian2
    with dissolve
    pause 1.0 hard
    play music second_115 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/030102370.ogg"
    lhx "小朋友们午睡时间结束后，我这里的工作也就告一段落了。"
    $ flcam.move(2250, 150, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/110101530.ogg"
    aiyi "今天大哥哥说他会来接我哟~"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030102390.ogg"
    lhx "约好了对吧。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/爱衣/110101540.ogg"
    aiyi "嗯~"
    play voice "voice/立花希/030102400.ogg"
    lhx "爱衣真的很喜欢凉君呢。"
    play voice "voice/爱衣/110101550.ogg"
    aiyi "嗯，因为大哥哥他很温柔。"
    show lhx_dzf_b3 b3 b3_n3
    play voice "voice/立花希/030102410.ogg"
    lhx "偶尔也会有人说那种木头温柔啊。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110101560.ogg"
    aiyi "立花老师？"
    hide lhx_dzf_b3 with None
    pause 0.1 hard
    show lhx_dzf_b2 b2 b2_n5 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/030102450.ogg"
    lhx "谢谢你，不是叫我飞机场老师。"
    play voice "voice/爱衣/110101570.ogg"
    aiyi "那样叫会比较好吗？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030102460.ogg"
    lhx "请千万不要那样做，我的忍耐也差不多快到极限了。"
    stop music fadeout 5.0
    hide lhx_dzf_b3
    hide aiyi_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/千川老师/140100290.ogg"
    qcls "大事不好了，飞机场老师！"
    $ flcam.move(2250, -150, 750, duration=1.5)
    show lhx_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030102470.ogg"
    lhx "我是不是可以生气了......"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/140100300.ogg"
    qcls "有看见小桃吗？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030102480.ogg"
    lhx "......欸？"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/140100310.ogg"
    qcls "从刚才开始就在找她，可怎么找也找不到。"
    hide qcls_zf_b1
    hide lhx_dzf_b3
    play music second_106 fadein 3.0 if_changed
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/210100630.ogg"
    qb "喂！！！你把小桃藏哪里去了你这个飞机场！"
    $ flcam.move(-2250, 150, 750, duration=1.5)
    show lhx_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030102490.ogg"
    lhx "我确实可以开始生气了！"
    play sound hite_light
    show wflash onlayer texture
    with vpunch 
    show qianbo_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.3
    show han onlayer m2:
        xpos 0.2 ypos 0.38
    play voice "voice/千波/210100640.ogg"
    qb "别敲我的脑袋啊！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day204.school_event03:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "刚一放学我的手机就响了起来。"
    play sound phone1
    pause 1.0 hard
    scene set only school day room xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(3800, -400, 800, duration=1.5)
    pause 1.0 hard
    investigation call block lhx_dzf_b2 b2 b2_n2 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    nvl clear
    show lhx_dzf_b2 b2 b2_n2
    play voice "voice/立花希/030102500.ogg"
    c.lhx_dzf_b2 "凉君，听得见吗？"
    play music second_122 fadein 3.0 if_changed
    c.me01 "立花老师？"
    show lhx_dzf_b2 b2 b2_n5
    play voice "voice/立花希/030102510.ogg"
    c.lhx_dzf_b2 "是的，不是飞机场老师。"
    c.me01 "这样称呼你比较好吗。"
    show lhx_dzf_b2 b2 b2_ga1
    play voice "voice/立花希/030102520.ogg"
    c.lhx_dzf_b2 "叫了的话我就再也不和你说话了。"
    c.me01 "开个玩笑的，你找我有什么事吗？"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/030102530.ogg"
    c.lhx_dzf_b2 "是的，我想你那边差不多也到放学时间了。"
    show lhx_dzf_b2 b2 b2_a1
    play voice "voice/立花希/030102560.ogg"
    c.lhx_dzf_b2 "有一位幼儿园的小朋友不见了。"
    c.me01 "不见了？"
    show lhx_dzf_b2 b2 b2_n2
    play voice "voice/立花希/030102570.ogg"
    c.lhx_dzf_b2 "没错，不见的是小桃。"
    play voice "voice/立花希/030102580.ogg"
    c.lhx_dzf_b2 "幼儿园里怎么找也找不到，我想应该是跑到外面去了。"
    c.me01 "又是这样吗......"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/030102590.ogg"
    c.lhx_dzf_b2 "我也是从千川老师那里听说的，以前似乎也发生过类似的事情，不过基本上都是三个人一起。"
    c.me01 "也就是说这次擅自跑出去的只有小桃一个人？"
    show lhx_dzf_b2 b2 b2_s1
    play voice "voice/立花希/030102600.ogg"
    c.lhx_dzf_b2 "是的。"
    c.me01 "这就奇怪了，平时怕生的小桃是不可能独自一人离开幼儿园的。"
    show lhx_dzf_b2 b2 b2_s2
    play voice "voice/立花希/030102610.ogg"
    c.lhx_dzf_b2 "所以在来接爱衣之前，能拜托你路过钟楼广场的时候顺便留意一下吗？"
    c.me01 "原来如此，想要分头寻找提高效率吗。"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/030102620.ogg"
    c.lhx_dzf_b2 "就是这样的。"
    c.me01 "我知道了，为了确保万无一失我会留意的。"
    show lhx_dzf_b2 b2 b2_ga2
    play voice "voice/立花希/030102660.ogg"
    c.lhx_dzf_b2 "帮大忙了~"
    c.me01 "那么在惊动警察之前尽快把事情解决吧，如果有什么突发状况的话就拜托立花老师冒充一下小朋友搪塞过去。"
    show lhx_dzf_b2 b2 b2_ga1
    play voice "voice/立花希/030102700.ogg"
    c.lhx_dzf_b2 "幻听的部分就不管了，就这样。"
    investigation call end
    pause 0.5 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    "一个人跑出去了吗......这种事情发生在小桃身上还真是奇怪。"
    "究竟是什么样的原因还不得而知。"
    "无论如何现在必须赶紧行动起来了。"
    play sound open_door5
    pause 0.5 hard
    "顾不上思考，我起身冲出了教室。"
    stop music fadeout 2.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard
    $ _overworld_label = 'day204'
    $ seen_day204_balltower_event01 = False
    $ seen_day204_school_event04 = False
    $ seen_day204_street_event01 = False
    $ seen_day204_shenshe_event03 = False
    $ seen_day204_shenshe_event01 = False

label day204.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day204':
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day204.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day204.street_event01':
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day204.school_event04':
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day204.shenshe_event02':
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    if _overworld_label == 'day204':
        window mode map
        me01 "先去哪里找好呢......" nointeract
    else:
        window mode map
        me01 "接下来应该去哪里找呢......" nointeract
    call screen rughzenhaide(
        road1=("day204.street_event01", "not seen_day204_street_event01"),
        school=("day204.school_event04", "not seen_day204_school_event04"),
        cloqks=("day204.balltower_event01", "not seen_day204_balltower_event01"),
        shenshe=("day204.shenshe_event03", "seen_day204_shenshe_event01 and not seen_day204_shenshe_event03"))
    $ window_animate_outro()
    if _return == 'day204.street_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day204.school_event04' and _overworld_label == 'day204':
        with Pause(1.0)
        scene black with dissolve
    elif _return == 'day204.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day204.school_event04' and _overworld_label != 'day204':
        $ flcam.move(*overworld.camera_positions['school'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day204.shenshe_event03':
        $ flcam.move(*overworld.camera_positions['shenshe'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day204.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only balltower day big
    with dissolve
    pause 1.0 hard
    "到达钟楼之后，我仔细检查了之前她们玩耍过的地方。"
    "因为没有下雪的缘故，视野还算不错。"
    pause 1.0 hard
    scene set only balltower day xuejian
    with dissolve
    pause 1.0 hard
    "然而即便如此仍旧一无所获。"
    me01 "看来只能去别处找找看了。"
    me01 "......那是？"
    stop music fadeout 5.0
    $ flcam.move(7100, 3500, 1100, duration=5.0, warper='ease_cubic')
    pause 5.0 hard
    "走近一看，是一个布偶。"
    inventory add doll
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only items doll
    with slowdissolve
    play music second_123 fadein 3.0 if_changed
    pause 1.0 hard
    "毫无疑问是小桃的。"
    "也就是说她确来过这里。"
    "但现在却是只留下了布偶。"
    "在我的印象中这只布偶一直是在小桃怀中抱着的。"
    "这种种迹象让我产生了不好的预感。"
    "明明从不离手的布偶，为什么会被丢在这种地方。"
    "是被卷入什么事件中了吗？"
    "诱拐？！"
    "也有可能只是路过的时候不小心掉在这里了。"
    "可恶，线索太少了......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day204_balltower_event01:
        $ seen_day204_balltower_event01 = True
    if seen_day204_school_event04 and seen_day204_street_event01:
        jump day204.shenshe_event01
    $ _overworld_label = 'day204.balltower_event01'
    jump day204.map

label day204.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street day road1 xuejian
    with dissolve
    pause 1.0 hard
    play music second_124 fadein 3.0 if_changed
    $ flcam.move(2250, -150, 750, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    show qcls_zf_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/千川老师/140100320.ogg"
    qcls "小桃到底跑到哪里去了......"
    play voice "voice/立花希/030102730.ogg"
    lhx "小桃会去的地方还有什么头绪吗？"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/140100340.ogg"
    qcls "也就只有钟楼广场了吧，第一次好像也是去了那里。"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/030102740.ogg"
    lhx "那里的话我已经拜托凉君去确认了。"
    show qcls_zf_b1 b1 b1_sp2
    play voice "voice/千川老师/140100350.ogg"
    qcls "神野同学吗？"
    show lhx_dzf_b2 b2 b2_s1
    play voice "voice/立花希/030102750.ogg"
    lhx "是的，之前也拜托他帮忙。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/140100370.ogg"
    qcls "......说起来小桃最近也经常说起她哥哥的事情。"
    $ flcam.move(2250, -150, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/140100380.ogg"
    qcls "似乎是想要和哥哥搞好关系。"
    play voice "voice/千川老师/140100390.ogg"
    qcls "我觉得可能是在看到神野同学和爱衣的关系之后。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/140100400.ogg"
    qcls "把他们的关系与自己的做了比较。"
    play voice "voice/千川老师/140100410.ogg"
    qcls "毕竟神野同学和小桃的哥哥好像是同级生。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030102780.ogg"
    lhx "这么说的话，小桃是想引起家人注意才跑出幼儿园的？"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/140100420.ogg"
    qcls "说不定是那样。"
    play voice "voice/千川老师/140100440.ogg"
    qcls "毕竟家人无论少了谁，都会感到寂寞的吧。"
    hide qcls_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    show lhx_dzf_b3 b3 b3_s1
    play voice "voice/立花希/030102810.ogg"
    lhx "这种感受......我也是一样的。（小声）"
    play voice "voice/立花希/030102850.ogg"
    lhx "说不定现在的我也......（小声）"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day204_street_event01:
        $ seen_day204_street_event01 = True
    if seen_day204_school_event04 and seen_day204_balltower_event01:
        jump day204.shenshe_event01
    $ _overworld_label = 'day204.street_event01'
    jump day204.map

label day204.school_event04:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian3
    with dissolve
    play music second_124 fadein 3.0 if_changed
    pause 1.0 hard
    play sound jiaobu4
    show yj_tcf_b1 b1 b1_s1 onlayer screens at side_right('yj'), basicfade
    play voice "voice/植澄友加/020101610.ogg"
    yj "哈、哈......一诚君！"
    hide yj_tcf_b1
    pause 0.5 hard
    scene set only school day outside xuejian2
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/一诚总司/180101110.ogg"
    yczs "......嗯？"
    pause 0.5 hard
    show yj_tcf_b2 b2 b2_s1 onlayer m2 at walkin_l(0.3)
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/植澄友加/020101620.ogg"
    yj "太好了......追上了。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180101120.ogg"
    yczs "怎么回事，上气不接下气的。你是跑过来的吗？"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101630.ogg"
    yj "是啊，还以为一诚君你去了社团，去找你结果也没看见人。"
    play voice "voice/一诚总司/180101130.ogg"
    yczs "我早退了，随便找个理由就......感觉有点提不起兴致。"
    show yj_tcf_b1 b1 b1_n2
    play voice "voice/植澄友加/020101640.ogg"
    yj "也是呢，从其他部员口中听说你回去了，吓了我一跳。"
    show yczs_dzf_b1 b1 b1_n2
    play voice "voice/一诚总司/180101140.ogg"
    yczs "你穿着体操服到外面来很显眼啊。"
    show yj_tcf_b1 b1 b1_s1
    play voice "voice/植澄友加/020101650.ogg"
    yj "比起这个，我有话要对一诚君说。"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/180101150.ogg"
    yczs "什么事？"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show yj_tcf_b1 b1 b1_a1
    play voice "voice/植澄友加/020101680.ogg"
    yj "身为哥哥你可要振作一点啊！"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180101180.ogg"
    yczs "你说谁是哥哥啊。"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_a1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101690.ogg"
    yj "你就是小桃独一无二的哥哥吧！"
    play voice "voice/一诚总司/180101190.ogg"
    yczs "......那又怎么样。"
    show yj_tcf_b2 b2 b2_s1
    play voice "voice/植澄友加/020101700.ogg"
    yj "小桃失踪的原因说不定就和一诚君你有关。"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/180101200.ogg"
    yczs "小桃她......失踪了？"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101710.ogg"
    yj "嗯，我听凉君说的，现在大家好像都在找她。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180101210.ogg"
    yczs "之前好像也有过一次......为什么那家伙总是会乱跑啊。"
    play voice "voice/一诚总司/180101220.ogg"
    yczs "为什么就不能老老实实地待在幼儿园啊！"
    show yj_tcf_b1 b1 b1_s1
    play voice "voice/植澄友加/020101720.ogg"
    yj "就是因为不知道原因所以才来找一诚君你的，你那边有什么头绪吗？"
    show yczs_dzf_b1 b1 b1_s2
    play voice "voice/一诚总司/180101270.ogg"
    yczs "说起来那天早上......"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101770.ogg"
    yj "怎么了？"
    play voice "voice/一诚总司/180101280.ogg"
    yczs "那天早上被小桃邀请一起过圣诞节、跨年之类的......"
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 0.25 alpha 1
    pause 0.5 hard
    scene set only street day road1 xuejian
    show sepiagrain onlayer texture
    $ flcam.move(0, 0, 600)
    show ycnn_sf_b1 b1 b1_n1 onlayer m2:
        xpos 0.6
    show ycxt_dzf_b1 b1 b1_s4 onlayer m1:
        xpos 0.7
    show yczs_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/小桃/220100520.ogg"
    ycxt "大哥哥......"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100680.ogg"
    yczs "怎么了？"
    show ycxt_dzf_b1 b1 b1_s3
    play voice "voice/小桃/220100530.ogg"
    ycxt "一、一起去幼儿园不行吗......"
    yczs "......"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/220100540.ogg"
    ycxt "圣诞节呢？"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100690.ogg"
    yczs "还有这样的日子来着，到时候我要去朋友家过。"
    show ycxt_dzf_b1 b1 b1_s4
    play voice "voice/小桃/220100550.ogg"
    ycxt "那新年呢......"
    play voice "voice/一诚总司/180100700.ogg"
    yczs "还有寒假作业必须要完成。"
    play voice "voice/小桃/220100560.ogg"
    ycxt "初诣......"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100710.ogg"
    yczs "太麻烦了，还是在家里呆着吧。"
    show ycxt_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/小桃/220100570.ogg"
    ycxt "呜......"
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 0.25 alpha 1
    pause 0.5 hard
    $ flcam.move(-2250, -350, 900)
    scene set only school day outside xuejian2
    show yj_tcf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    show yczs_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/植澄友加/020101780.ogg"
    yj "她邀请你一起？"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180101290.ogg"
    yczs "是啊，但是被我拒绝了。"
    show yj_tcf_b2 b2 b2_s1
    play voice "voice/植澄友加/020101790.ogg"
    yj "......"
    show yczs_dzf_b1 b1 b1_s2
    play voice "voice/一诚总司/180101300.ogg"
    yczs "明明是头一次被邀请一起去初诣的。"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101800.ogg"
    yj "那小桃......会不会是到神社去了呢？"
    show yj_tcf_b1 b1 b1_s1
    play voice "voice/植澄友加/020101810.ogg"
    yj "想着初诣的事情......"
    show yj_tcf_b1 b1 b1_n2
    play voice "voice/植澄友加/020101820.ogg"
    yj "想要和哥哥你一起去参拜。"
    hide yj_tcf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180101310.ogg"
    yczs "......"
    play sound jiaobu3
    show yczs_dzf_b1 b1 b1_s1 at walkout_r(0.5)
    pause 1.0 hard
    hide yczs_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_tcf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101830.ogg"
    yj "啊......跑掉了。"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101840.ogg"
    yj "是去神社了吧，因为在城外的山上所以必须尽快才行。"
    hide yj_tcf_b1
    show yj_tcf_b3 b3 b3_h1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101850.ogg"
    yj "嗯......这不是有好好做个哥哥的嘛~"
    show yj_tcf_b3 b3 b3_s1
    play voice "voice/植澄友加/020101860.ogg"
    yj "稍微有点......羡慕啊。"
    $ flcam.move(-4500, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide yj_tcf_b3
    show yj_tcf_b1 b1 b1_s3 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020101870.ogg"
    yj "如果是姐姐的话，也会为了我这么做吗......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day204_school_event04:
        $ seen_day204_school_event04 = True
    if seen_day204_balltower_event01 and seen_day204_street_event01:
        jump day204.shenshe_event01
    $ _overworld_label = 'day204.school_event04'
    jump day204.map

label day204.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only shenshe day xuejian
    with dissolve
    play music second_120 fadein 3.0 if_changed
    play ambience1 niaoming
    pause 1.0 hard
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/琉璃/040101870.ogg"
    liuli "藤原同学，下午好~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/藤原瞳/130100510.ogg"
    tyt "早中晚安~虽然刚才还在学校见到过的。"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_ga3 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/040101880.ogg"
    liuli "藤原同学走得好快啊，本来还想一起走的结果就被丢下了。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/130100520.ogg"
    tyt "因为总觉得这样能够让卡路里得到最大程度的利用。"
    show liuli_dzf_b3 b3 b3_h1
    play voice "voice/琉璃/040101890.ogg"
    liuli "所以休息时间和上课都一直在睡，就是为了保存体力来处理神社的工作对吧~"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/藤原瞳/130100530.ogg"
    tyt "就是这样。"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/130100540.ogg"
    tyt "话说花山院你来这里有什么事吗？"
    hide liuli_dzf_b3 with None
    pause 0.1 hard
    show liuli_dzf_b2 b2 b2_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/琉璃/040101910.ogg"
    liuli "啊、啊咧？不是藤原同学叫我来帮忙的吗？"
    play voice "voice/藤原瞳/130100550.ogg"
    tyt "我忘记了。"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_ga3 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/040101920.ogg"
    liuli "藤原同学还真是很健忘呢......"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/130100560.ogg"
    tyt "这都是为了节约能量才选择的反应。"
    show liuli_dzf_b3 b3 b3_s5
    play voice "voice/琉璃/040101930.ogg"
    liuli "那、那个？怎么感觉和刚才说的有些矛盾......"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100610.ogg"
    tyt "花山院，你过来一下。"
    hide liuli_dzf_b3
    show liuli_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/040101980.ogg"
    liuli "要开始工作了吗？"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/130100620.ogg"
    tyt "在那之前有东西要给你看......"
    pause 1.0 hard
    stop ambience1 fadeout 3.0
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only ycxt_cg one
    with dissolve
    pause 1.0 hard
    play voice "voice/小桃/220100880.ogg"
    ycxt "呼......"
    pause 1.0 hard
    scene set only shenshe day inside xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101990.ogg"
    liuli "这、这孩子怎么了？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/130100630.ogg"
    tyt "我捡回来的。"
    play sound jump_1
    hide liuli_dzf_b3 with None
    pause 0.1 hard
    show liuli_dzf_b2 b2 b2_c1 onlayer m2 at flu_up(0.15, 30):
        xpos 0.5
    show tanhao onlayer m2 at tanhao_x07_rev(0.55, 0.3):
        xzoom -1
    play voice "voice/琉璃/040102000.ogg"
    liuli "{size=72}欸？！{/size}"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100640.ogg"
    tyt "她在钟楼广场上睡着了，怎么叫也叫不醒，所以就把她带回来了。"
    show liuli_dzf_b2 b2 b2_s1
    play voice "voice/琉璃/040102010.ogg"
    liuli "是、是这样啊，那附近有她的家人吗？"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/130100650.ogg"
    tyt "广场上只有这孩子一个人，看起来很冷的样子就没办法放着不管。"
    play voice "voice/藤原瞳/130100660.ogg"
    tyt "本来想让她在内屋睡的，但是内屋还需要打扫所以......"
    show liuli_dzf_b2 b2 b2_n1
    play voice "voice/琉璃/040102030.ogg"
    liuli "藤原同学真是个温柔的人呢~"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/130100680.ogg"
    tyt "我觉得换作是谁都会担心的。"
    hide tyt_wnf_b1
    hide liuli_dzf_b2
    $ flcam.move(0, 300, 1100, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only ycxt_cg one
    with dissolve
    pause 1.0 hard
    play voice "voice/小桃/220100890.ogg"
    ycxt "嗯、嗯嗯......"
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900)
    scene set only shenshe day inside xuejian
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    with dissolve
    pause 1.0 hard
    play voice "voice/藤原瞳/130100720.ogg"
    tyt "啊，她醒了。"
    hide tyt_wnf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 1.12
        parallel:
            linear 1.0 ypos 1.07
        parallel:
            linear 1.0 alpha 1.0
    play voice "voice/小桃/220100900.ogg"
    ycxt "......这里是？"
    $ flcam.move(-2250, 150, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/130100740.ogg"
    tyt "这里是神社。"
    play voice "voice/小桃/220100910.ogg"
    ycxt "神社？"
    show ycxt_dzf_b2 b2 b2_s2
    play voice "voice/小桃/220100920.ogg"
    ycxt "小桃我，明明应该在钟楼广场的。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/130100750.ogg"
    tyt "是我把你带过来的~"
    show ycxt_dzf_b2 b2 b2_sp1
    play voice "voice/小桃/220100940.ogg"
    ycxt "大姐姐你们......是谁？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100760.ogg"
    tyt "我只是个做好事不留名的无名之辈而已。"
    show ycxt_dzf_b2 b2 b2_s4
    play voice "voice/小桃/220100990.ogg"
    ycxt "......布偶，不见了。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show liuli_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/040102140.ogg"
    liuli "布偶？"
    show ycxt_dzf_b2 b2 b2_s4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/小桃/220100950.ogg"
    ycxt "救......救命！"
    stop music fadeout 3.0
    hide liuli_dzf_b2
    show liuli_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/040102110.ogg"
    liuli "......诶？"
    hide tyt_wnf_b1
    hide liuli_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b2 b2 b2_c1
    play music second_123 fadein 3.0 if_changed
    play voice "voice/小桃/220100960.ogg"
    ycxt "诱、诱拐犯......"
    $ flcam.move(2250, 150, 750, duration=1.5)
    play sound jump_1
    show liuli_dzf_b2 b2 b2_c1 onlayer m2 at flu_up(0.15, 30):
        xpos 0.7
    play voice "voice/琉璃/040102120.ogg"
    liuli "欸？！"
    $ flcam.move(0, 150, 600, duration=1.5)
    show tyt_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/130100780.ogg"
    tyt "仔细想想从某种意义上来说确实是这样......"
    hide liuli_dzf_b2
    hide tyt_wnf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    show wflash onlayer texture
    with vpunch
    play voice "voice/小桃/220100970.ogg"
    ycxt "哥哥......哥哥！！！"
    play voice "voice/小桃/220100980.ogg"
    ycxt "救救我......哥哥！！！"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play voice "voice/小桃/220101120.ogg"
    ycxt "哥哥送的布偶......还给我！"
    pause 1.0 hard
    play sound rune2
    $ flcam.move(0, 0, 0)
    scene set only ycxt_cg two
    with in2out_02
    pause 2.0 hard
    show tyt_wnf_b1 b1 b1_sp1 onlayer screens at side_left('tyt'), basicfade
    play voice "voice/藤原瞳/130100820.ogg"
    tyt "什......"
    hide tyt_wnf_b1
    show liuli_dzf_b2 b2 b2_sp1 onlayer screens at side_right('liuli', 0.92), basicfade
    play voice "voice/琉璃/040102160.ogg"
    liuli "这、这是？！"
    hide liuli_dzf_b2
    show tyt_wnf_b1 b1 b1_sp1 onlayer screens at side_left('tyt'), basicfade
    play voice "voice/藤原瞳/130100830.ogg"
    tyt "突然就刮起了风！"
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/130100860.ogg"
    tyt "是这孩子的灵能力！？还是说是其他什么不一样的......"
    show tyt_wnf_b1 b1 b1_a2
    play voice "voice/藤原瞳/130100870.ogg"
    tyt "星天宫一直在寻找的，未知的力量——"
    stop music fadeout 5.0
    hide tyt_wnf_b1
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    $ seen_day204_shenshe_event01 = True

label day204.school_event05:
    play sound phone2
    pause 1.0 hard
    scene set only school day corridor xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101020.ogg"
    szl "邮件？不对是电话。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    show szl_dzf_b2 b2 b2_sp2
    play voice "voice/水之濑/050101030.ogg"
    szl "对方是......难道说！"
    play music second_146 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    show szl_dzf_b2 b2 b2_n2 onlayer screens at side_right('szl', 0.89), basicfade
    play voice "voice/水之濑/050101040.ogg"
    szl "您好。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/050101050.ogg"
    szl "是吗，果然是这样......"
    hide szl_dzf_b2
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only school day corridor xuejian
    show szl_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/050101060.ogg"
    szl "在城外感知到了异常的{rb}灵纹{/rb}{rt}rune{/rt}反应。"
    show szl_dzf_b2 b2 b2_n3
    play voice "voice/水之濑/050101070.ogg"
    szl "地点是......是吗，稍微有点远啊。"
    play voice "voice/水之濑/050101080.ogg"
    szl "希望能赶上就好了......"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/050101090.ogg"
    szl "我知道了，我马上过去。"
    play voice "voice/水之濑/050101100.ogg"
    szl "我也试着尽点人事吧。"
    show szl_dzf_b2 b2 b2_s4
    play voice "voice/水之濑/050101110.ogg"
    szl "但我把话说在前头，善后可是你们的工作。"
    play voice "voice/水之濑/050101120.ogg"
    szl "圣护院小姐......应该叫你。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101130.ogg"
    szl "植澄主任。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day204.shenshe_event02:
    $ flcam.move(0, 0, 0)
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play music second_125 fadein 3.0 if_changed
    play voice "voice/小桃/220101130.ogg"
    ycxt "哥哥......哥哥！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only ycxt_cg two
    with dissolve
    pause 1.0 hard
    "一诚小桃的脑海中此刻想着的只有一件事。"
    "希望自己也能像凉君与爱衣的关系一样从哥哥那里得到更多的温暖。"
    "想要一直待在他的身边。"
    "没错。"
    "布偶只是借口罢了。"
    "只是布偶的话是不够。"
    "只是那样的话，是完全不够的。"
    "因为自己的懦弱，在哥哥面前几乎无法顺利地交流。"
    "就算鼓起勇气搭话，换来的也只是零星的几句搪塞。"
    "明明不想让大家担心的。"
    "可结果还是忍不住哭了。"
    "这是为什么呢？"
    "是小桃的错吗？"
    "和哥哥的关系就注定只能是这样了吗？"
    "因为小桃至始至终都是一个“坏孩子”吗......"
    pause 0.5 hard
    $ flcam.move(-750, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/小桃/220101140.ogg"
    ycxt "一定......是这样没错。"
    "因为自己是坏孩子。"
    "因为自己擅自跑出去让大家担心了。"
    "可是......"
    "之前迷路的时候，凉君来找我了。"
    "所以这次......总司哥哥也会出现的吧？"
    "这样期待着。"
    play voice "voice/小桃/220101150.ogg"
    ycxt "哥哥他说不定，也会来接我的。"
    "可结果却反而又让大家担心了。"
    "害怕、好害怕，此刻真的成了迷路的孩子。"
    "给总司哥哥添麻烦了。"
    "给大家添麻烦了。"
    "果然小桃是坏孩子。"
    "因为是坏孩子，才会被讨厌的吧......"
    play voice "voice/小桃/220101160.ogg"
    ycxt "对不起、对不起......"
    play voice "voice/小桃/220101170.ogg"
    ycxt "小桃......不会再做坏事了。"
    play voice "voice/小桃/220101180.ogg"
    ycxt "会当个好孩子的。"
    play voice "voice/小桃/220101190.ogg"
    ycxt "不会再擅自出走了。"
    play voice "voice/小桃/220101200.ogg"
    ycxt "所以求求你，不要讨厌我！"
    pause 0.5 hard
    $ flcam.move(-1400, -2800, 800, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/小桃/220101210.ogg"
    ycxt "{size=72}哥哥！{/size}"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    $ seen_examine_doll = 0

label day204.kindergarden_event02:
    $ flcam.move(0, 0, 0)
    scene set only school evening outside xuejian alpha
    play music second_129 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110101590.ogg"
    aiyi "啊......大哥哥你回来了吗。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110101600.ogg"
    aiyi "大哥哥，那个......小桃她好像一个人跑到外面去了。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/110101610.ogg"
    aiyi "然后呢，爱衣有种不好的预感。"
    me01 "这些我都知道了，不过你放心，我马上就会把她带回来的。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110101620.ogg"
    aiyi "已经知道小桃在哪里了吗？"
    me01 "虽然还不是很确定，但有种预感告诉我她一定就在那里。"
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    show screen investigation_popup(investigation.preg4)
    pause 0.5 hard
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu aiyi_dzf_b1 onlayer m2:
            camera_pos (scale(-2097), scale(+200), 600)
            screen_pos (0.5, 1.15)
            screen_direction left

label day204.examine_doll:
    hide screen investigation_popup
    if seen_examine_doll == 0:
        window mode thought
        me01 "从布偶的完整程度来看，应该不像是遇到了什么事故的样子。"
        window mode thought
        me01 "从外观上似乎找不到什么突破口。"
    elif seen_examine_doll == 1:
        window mode thought
        me01 "布偶的周围散发着一股淡淡的檀香木的气息。"
        window mode thought
        me01 "总觉得是一股熟悉的味道。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    $ seen_examine_doll += 1
    jump investigate

label day204.use_doll:
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    hide screen investigation_popup
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "这个布偶能交给爱衣你暂时保管吗？"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110101630.ogg"
    aiyi "嗯......"
    show aiyi_dzf_b1 b1 b1_n1 at flu_down(0.35, 20):
        xpos 0.5
    pause 1.0 hard
    hide aiyi_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at walkin_l(0.7)
    pause 0.5 hard
    play voice "voice/千波/210100650.ogg"
    qb "喂！你这个诱拐犯！！"
    me01 "我就觉得你这家伙差不多要出来了。"
    hide qianbo_dzf_b1 with None
    pause 0.1 hard
    play sound jump_1
    show qianbo_dzf_b2 b2 b2_a3 onlayer m2 at flu_up(0.15, 20):
        xpos 0.7
    play voice "voice/千波/210100660.ogg"
    qb "你把小桃藏哪里去了！"
    me01 "这件事和我可没有关系。"
    hide qianbo_dzf_b2
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110101640.ogg"
    aiyi "小桃她，不会出什么事吧......"
    me01 "不用担心，我一定会把她平安带回来的。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/110101650.ogg"
    aiyi "......"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110101660.ogg"
    aiyi "大哥哥，请一定要帮帮小桃。"
    me01 "放心地交给我吧！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 1.0 hard
    "虽说最应该站出来的并不是我。"
    "如果是一诚的话他会怎么做呢。"
    pause 1.0 hard
    scene set only school evening outside xuejian alpha
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve    
    pause 0.5 hard
    show lhx_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030103640.ogg"
    lhx "凉君你快去吧，剩下的交给我就好。"
    me01 "我知道了，爱衣和就拜托你了。"
    hide lhx_dzf_b3
    $ flcam.move(2250, 0, 750, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s1 onlayer m1:
        xpos 0.5
    show qianbo_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/110101680.ogg"
    aiyi "......嗯，千波我们走吧。"
    show qianbo_dzf_b1 b1 b1_a3
    play voice "voice/千波/210100670.ogg"
    qb "凉君男，回来之后再找你算账！"
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s1 at walkout_r(0.5)
    show qianbo_dzf_b1 b1 b1_a3 at walkout_r(0.7)
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.3
    me01 "怎么说呢......"
    me01 "谢谢你替我解围。"
    play sound jump_1
    show lhx_dzf_b3 b3 b3_n5 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/立花希/030103700.ogg"
    lhx "为、为什么凉君你要为这种事情向我道谢啊。"
    me01 "正因为是立花老师，我才能放心地把这里交给你。"
    play voice "voice/立花希/030103710.ogg"
    lhx "......"
    show lhx_dzf_b3 b3 b3_a1
    play voice "voice/立花希/030103720.ogg"
    lhx "别说肉麻的话了！"
    me01 "那么我出发了。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030103730.ogg"
    lhx "那么......放心去吧。"
    pause 1.0 hard
    scene black
    with slowerdissolve
    play sound jiaobu4
    pause 3.0 hard
    $ _overworld_label = 'day204.shenshe_event02'
    $ seen_day204_shenshe_event03 = False
    jump day204.map

label day204.shenshe_event03:
    $ flcam.move(0, 0, 0)
    stop music fadeout 5.0
    scene set only shenshe evening xuejian2
    play ambience1 strong_wind fadein 2.0
    show snow_level2 onlayer fg  
    with dissolve
    me01 "这是......"
    play music second_127 fadein 3.0 if_changed
    "一来到神社的门口就感受到从正面袭来的风压。"
    $ flcam.move(0, -200, 1100, duration=2.5, warper='ease_cubic')
    pause 3.0 hard
    "巨大的风暴夹杂着泥沙，将周围的树木和建筑全都覆盖了。"
    me01 "这、这是什么！"
    "龙卷风吗？从来没有见过眼前的这番景象。"
    play voice "voice/琉璃/040102210.ogg"
    stranger "那、那个......"
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_sp2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    me01 "琉璃？为什么你会在这里？"
    show liuli_dzf_b2 b2 b2_c1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/琉璃/040102220.ogg"
    liuli "我们三人从刚才开始就一直在这里的。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/藤原瞳/130100880.ogg"
    tyt "非常的不可思议......"
    me01 "三个人？也就是说此刻风暴里的那位是......"
    me01 "小桃？！"
    show liuli_dzf_b2 b2 b2_sp1
    play voice "voice/琉璃/040102240.ogg"
    liuli "前辈你怎么会在这里？"
    me01 "我是为了接小桃回去的，可这到底发生了什么？"
    hide liuli_dzf_b2
    hide tyt_wnf_b1
    $ flcam.move(0, -100, 400, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    "在风最强烈的中心地带，小桃的身影就伫立在那里。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    hide snow_level2
    scene set only ycxt_cg four
    with dissolve
    pause 1.0 hard
    "她这是在哭吗？"
    "看嘴型似乎是在说些什么，但是因为风暴的缘故完全听不到任何的声音。"
    me01 "小桃！听得见吗！"
    pause 0.1 hard
    scene set only ycxt_cg two 
    with dissolve
    $ flcam.move(-1100, -1400, 750, duration=1.5, warper='ease_quad')
    play voice "voice/小桃/220101220.ogg"
    ycxt "......"
    "不行，完全没有办法传达。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    show snow_level2 onlayer fg
    with dissolve
    "时间一分一秒地流逝，但是风力却丝毫没有减弱。"
    "虽说此时位于台风眼的小桃暂时没有生命危险。"
    "但再这样放任下午不仅神社会被摧毁，届时再想救出小桃就是难上加难了。"
    "必须先解决掉这麻烦的风暴。"
    pause 1.0 hard
    scene set only shenshe evening xuejian2
    with dissolve
    pause 1.0 hard
    "可是离小桃越近风暴就越强烈，就算想要强行冲进去也会被瞬间掀翻在地。"
    "要怎么样才能将她从这股风压中剥离出来呢？"
    "做不到的吧，光凭我一个人的力量......"
    stop ambience1 fadeout 3.0
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level2
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ seen_day204_shenshe_event03 = True

label day204.kindergarden_event03:
    $ flcam.move(0, 0, 0)
    scene set only bridge evening xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001003590.ogg"
    xfe "一直勉强着自己的她。" 
    play voice "voice/希菲尔/001003600.ogg"
    xfe "明明彼此都是拥有“心”的人。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001003610.ogg"
    xfe "但是却依旧发生了纷争，这就是芬布尔之冬吗。"
    play voice "voice/希菲尔/001003620.ogg"
    xfe "不过，一定不要紧的。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001003630.ogg"
    xfe "因为你们，都不是孤单一人的。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play music second_128 fadein 3.0 if_changed
    scene set only xfe_cg memory4
    with dissolve
    pause 1.0 hard
    "天使开始歌唱。"
    $ flcam.move(-1100, -1400, 750, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "寄托着冬雪的思念。"
    "这座城市降下了温柔的雪——"
    pause 1.0 hard
    $ flcam.move(1000, 1500, 1800, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 5.0 hard
    play sound rune2
    pause 1.0 hard
    scene set only myself_cg one
    with slowdissolve
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 2.0 hard
    "怎么回事？"
    "突然感觉自己的体内有一股力量涌了上来了。"
    "从张开的手掌上发出了{encyclopedia=psychokinesis}{rb}念动力场{/rb}{/encyclopedia}{rt}psychokinesis{/rt}。"
    "利用念波的物理效应制造屏障来抵消风压。"
    me01 "这不可思议的力量究竟是什么？"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only school evening inside xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_sp1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010103100.ogg"
    xz "......欸？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only items necklace
    with dissolve
    pause 1.0 hard
    "胸口的挂件发出了淡淡的光芒。"
    "仿佛夜空里的星辰一般闪耀着。"
    show xz_dzf_b3 b3 b3_s2 onlayer screens at side_left('xz', 0.0), basicfade
    play voice "voice/翔子/010103110.ogg"
    xz "到底......发生了什么？"
    hide xz_dzf_b3
    pause 1.0 hard
    scene set only school evening inside xuejian
    with dissolve
    play music second_124 fadein 3.0 if_changed
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/千川老师/140100500.ogg"
    qcls "青木同学，辛苦你了。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010103120.ogg"
    xz "千川老师，神野君他出了什么事吗？"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/140100510.ogg"
    qcls "神野同学的话去找小桃了。"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010103130.ogg"
    xz "小桃又迷路了吗？"
    play voice "voice/千川老师/140100530.ogg"
    qcls "是的，不过这次只有她一人......"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010103140.ogg"
    xz "那个老实的小桃居然会一个人跑出去，真是让人难以置信。"
    hide qcls_zf_b1
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110101710.ogg"
    aiyi "小桃她一定是因为有很重要的事情。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/110101720.ogg"
    aiyi "所以才会鼓起勇气一个人努力的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 3.0 hard
    scene set only school evening inside xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110101740.ogg"
    aiyi "啊，下雪了。"
    $ flcam.move(-1500, 300, 750, duration=1.5)
    show qianbo_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.6
    play voice "voice/千波/210100720.ogg"
    qb "不会堆积的雪。"
    $ flcam.move(0, 0, 650, duration=1.5)
    show qcls_zf_b1 b1 b1_n4 onlayer m1:
        xpos 0.7
    play voice "voice/千川老师/140100550.ogg"
    qcls "稍微变得有些冷了呢。"
    $ flcam.move(0, 0, 600, duration=1.5)
    show xz_dzf_b1 b1 b1_h1 onlayer m1:
        xpos 0.4
    play voice "voice/翔子/010103170.ogg"
    xz "大家，在感冒之前先进屋吧。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_h2 onlayer m1:
        xpos 0.4
    play voice "voice/翔子/010103180.ogg"
    xz "然后，等神野君他们回来。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110101750.ogg"
    aiyi "......但是，要等的话还是在门口比较好。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110101760.ogg"
    aiyi "这样的话，就能在第一时间迎接他们了~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day204.battle_ycxt_first:
    scene white 
    with slowerdissolve
    play sound rune2
    pause 2.0 hard
    "总算是暂时控制住了风暴的蔓延。"
    "之后就只剩下把小桃救出来而已。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only myself_cg one
    with dissolve
    pause 1.0 hard
    play music second_138 fadein 3.0 if_changed
    "但是以我目前的能力，光是阻挡风的蔓延就已经是尽全力了。"
    "更糟糕的是，拖太久的话不仅是小桃，就连自己身后的琉璃和藤原瞳都会受伤的。"
    "一定还有办法的，就像是突然觉醒的力量一样，一定还有什么能够拯救这个孩子的方法。"
    "虽然很勉强，但也只能再试试看了。"
    pause 1.0 hard
    scene set only shenshe evening xuejian2
    play ambience1 strong_wind
    show snow_level2 onlayer fg
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "小桃！能听见我说话的吗！"
    me01 "大哥哥我来接你了！一起回去吧！"
    me01 "幼儿园的大家都在等着你！"
    pause 1.0 hard
    hide snow_level2
    $ flcam.move(0, 0, 0)
    scene set only ycxt_cg three
    with dissolve
    pause 1.0 hard
    play voice "voice/小桃/220101230.ogg"
    ycxt "哥哥......哥哥。"
    play voice "voice/小桃/220101240.ogg"
    ycxt "对不起......哥哥。"
    pause 0.1 hard
    scene set only ycxt_cg four
    with dissolve
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 0.5 hard
    play voice "voice/小桃/220101250.ogg"
    ycxt "小桃不会再做坏事了。"
    play voice "voice/小桃/220101260.ogg"
    ycxt "所以，请不要讨厌小桃。"
    play voice "voice/小桃/220101270.ogg"
    ycxt "来救救小桃。"
    play voice "voice/小桃/220101280.ogg"
    ycxt "哥哥！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only shenshe evening xuejian2
    show snow_level2 onlayer fg
    with dissolve
    pause 1.0 hard
    "还是不行。"
    "无论我如何呼唤，声音始终无法传达到她那里。"
    "风速之大已经在我与小桃之间构筑起了一道屏障，隔绝了声音的传播。"
    "小桃传达出来最后的信息，也就只有她口中的“哥哥”了。"
    pause 1.0 hard
    hide snow_level2
    scene set only myself_cg three
    with dissolve
    pause 1.0 hard
    me01 "就算这样，怎么可能放着不管！"
    "接下来就剩下最后也是最糟糕的办法了。"
    "就是利用{rb}念动力场{/rb}{rt}psychokinesis{/rt}直接轰击风暴的中心，打乱气流的流动从而瓦解风暴本身。"
    "通过改变部分风的流向从而使两股风力相互抵消。"
    "但这也就意味着处于风暴中心的小桃可能会因此受到两股风暴猛烈的冲击。"
    "可是如果继续放任风暴扩散的话，等到风墙稳固之后就没有办法再阻止了。"
    "这是一场赌注，输了后果可谓是空前惨烈。"
    "胜利的关键是控制力。"
    "任何外部施加的作用力在与风暴表面高速运动的空气摩擦之后产生的热量会集中在漩涡的中心。"
    "因此为了避免高温对小桃造成伤害，就必须尽可能控制风压的平衡。"
    "没时间犹豫了，再拖下去小桃会无法呼吸的。"
    pause 0.1 hard
    play sound rune2
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 0.5 hard
    "作战开始！"
    "集中注意力，把一切都交给意念，迅捷的同时更要谨慎。"
    "把身体里所有能够感知的力量都集中到了手掌。"
    "利用{rb}念动力场{/rb}{rt}psychokinesis{/rt}制造的屏障将小桃和风暴包裹住。"
    me01 "琉璃、藤原同学，虽然很突然但请你们助我一臂之力。"
    me01 "必须赶在风暴肆虐前救出小桃才行。"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    stop ambience1 fadeout 3.0
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    scene set only fight_cg shenshe
    with dissolve
    python:
        if "eggs" not in local_config.player.items:
            local_config.player.items["eggs"] = 1
        local_config.player.skills += [psychokinesis]
        ycxt_role_mirror.pose = "no_dool"
        local_config.party = [liuli_role_mirror, tyt_role_mirror]
        for role in local_config.party:
            role.stats_check(5)
        ycxt_role_mirror.skills = [s for s in ycxt_role_mirror.skills if s.category != "Passive"]
        # 总教学
        local_config.total_tutorial_flags += ["HP/MP", "general_skill", "guard_skill", "combat_breakout_skill", "item_use", "buff", "element"]

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=ycxt_role_mirror, 
                boss_hp_plus=10000, 
                side_enemy=[], 
                level=5, 
                win_condition='battle_tutorial', 
                stay_turn=0, 
                inside_label="inside_battle1", 
                mission_type="normal", 
                treasures={"eggs": (2, 1.0)})
    
    if _return == "win":
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day204.after_battle_ycxt_first

label day204.after_battle_ycxt_first:
    scene black
    with dissolve
    pause 1.0 hard
    play music second_129 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only ycxt_cg three
    with dissolve
    pause 1.0 hard
    play voice "voice/小桃/220101290.ogg"
    ycxt "呜呜......"
    play voice "voice/小桃/220101300.ogg"
    ycxt "小桃我......到底怎么了？"
    play voice "voice/小桃/220101310.ogg"
    ycxt "这里是......哪里？"
    play voice "voice/小桃/220101320.ogg"
    ycxt "什么都看不见......"
    play voice "voice/小桃/220101330.ogg"
    ycxt "什么都听不见......"
    "小桃的啜泣声被风暴掩盖了。"
    "风暴的中心空气很稀薄。"
    "在这种环境下一般是听不到声音的。"
    "不止是声音，杂乱的气流遮挡了光线，现在她的眼里应该是漆黑一片。"
    "迷路的孩子无助地哭泣着。"
    pause 0.1 hard
    scene set only ycxt_cg four
    with dissolve
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 0.5 hard
    play voice "voice/小桃/220101340.ogg"
    ycxt "好黑......好可怕！"
    play voice "voice/小桃/220101350.ogg"
    ycxt "哥哥......哥哥！"
    pause 0.1 hard
    scene set only ycxt_cg three
    with dissolve
    $ flcam.move(-2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 0.5 hard
    play voice "voice/小桃/220101360.ogg"
    ycxt "救救我......哥哥！"
    pause 1.0 hard

label day204.battle_ycxt_second:
    scene white
    with slowdissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/030104300.ogg"
    stranger "小桃。"
    play voice "voice/天使雷亚/030104310.ogg"
    stranger "原来如此。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only shenshe evening inside xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound rune1
    show ts_lst_ssz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/天使雷亚/030104320.ogg"
    lst "你真的......很喜欢你的哥哥。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_s3
    play voice "voice/天使雷亚/030104330.ogg"
    lst "和我......是一样的。"
    play voice "voice/天使雷亚/030104350.ogg"
    lst "我也，最喜欢凉君了。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    "大量的魔力消耗让我的意识开始模糊了。"
    "在风暴中心夹杂着微弱的光，雷亚的身影浮现在了我的脑海中。"
    "这是幻觉吗，因为极度虚弱的缘故让我再一次见到了你。"
    "这一次又得依靠你的力量了吗。"
    "飘散的白雪乘着念动力场包裹在小桃的四周，形成了一道隔绝风刃和高温的屏障。"
    "温柔的雪、约定的光，曾经的羁绊此刻都来到了我的身边——"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    stop music fadeout 3.0
    pause 3.0 hard
    play sound rune2
    pause 1.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg shenshe
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        if "eggs" not in local_config.player.items:
            local_config.player.items["eggs"] = 2
        else:
            local_config.player.items["eggs"] += 2
        local_config.masters = ["lst_role"]
        ycxt_role.pose = 'no_dool'
        ycxt_role_mirror.pose = 'no_dool'
        for skill in ycxt_role.skills:
            if skill.category == "Passive":
                skill.selectable = False
        for skill in ycxt_role_mirror.skills:
            if skill.category == "Passive":
               skill.selectable = False
        local_config.party = [lst_role, ycxt_role]
        for role in copy(local_config.party):
            if role.name == "雷亚":
                temp_selected_skills, temp_selected_skills_v2 = role.skills, role.skills_v2
                before_battle_general_attack = [s for s in temp_selected_skills if s.category == "General_attack"][0]
                before_battle_general_attack_v2 = [s for s in temp_selected_skills_v2 if s.category == "General_attack"][0]
                now_battle_general_attack = copy(getattr(store, "psychokinesis-fire"))
                for xi in range(before_battle_general_attack.level - 1):
                    now_battle_general_attack.level_change(now_battle_general_attack.level + 1)
                role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                role.base_skills = role.skills
                role.skills_v2 = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills_v2]
                role.base_skills_v2 = role.skills_v2
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)
        
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=ycxt_role_mirror, 
                boss_hp_plus=1000,
                side_enemy=[], 
                level=5,
                win_condition='protect_ycxt', 
                stay_turn=0, 
                inside_label="inside_battle2", 
                mission_type="normal", 
                treasures={"eggs": (2, 0.5)})

    if _return == "win":
        "战斗胜利！"
        python:
            for role in local_config.party:
                if role.name == "雷亚":
                    role.skills = [s if s.category != "General_attack" else before_battle_general_attack for s in role.skills]
                    role.base_skills = role.skills
                    role.skills_v2 = [s if s.category != "General_attack" else before_battle_general_attack_v2 for s in role.skills_v2]
                    role.base_skills_v2 = role.skills_v2
            if "ycxt_role" not in local_config.role_pool:
                local_config.role_pool.add("lst_role")
                local_config.role_pool.add("ycxt_role")
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 3.0
    else:
        jump battle_end
    jump day204.after_battle_ycxt_second

label day204.after_battle_ycxt_second:
    scene white
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/030104360.ogg"
    lst "接下来......只要一起回去就好。"
    play voice "voice/天使雷亚/030104370.ogg"
    lst "小桃你回到哥哥的身边。"
    play voice "voice/天使雷亚/030104380.ogg"
    lst "而我......也要回到那个人的身边去了。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    play ambience1 strong_wind fadein 3.0
    show snow_level2 onlayer fg
    with dissolve
    pause 1.0 hard
    "{rb}念动立场{/rb}{rt}psychokinesis{/rt}无法维持太久，虽然在一瞬间撑开了风障，但是此刻的我已经没有余力将小桃带出来了。"
    "必须有人穿过狭窄的缝隙，冒着随时可能粉身碎骨的危险......到达小桃的那头。"
    "但此刻现场无论是谁，经过刚才的战斗身体和精神的负荷都已经到达极限了。"
    "灵力反噬带来的疼痛已经让我无法再发出声音了。"
    "难道真的没有办法了吗。"
    "难道又只能眼睁睁地看着重要之人从我的眼前消失，却什么也做不了吗。"
    pause 1.0 hard
    hide snow_level2
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "谁来救救她，是谁都行，请不要再让她哭泣了。"
    stop ambience1 fadeout 3.0
    pause 2.0 hard
    play voice "voice/小桃/220101400.ogg"
    ycxt "{size=72}哥哥！{/size}"
    pause 2.0 hard
    play sound touch
    scene set only ycxt_cg nisang1
    play music second_130 fadein 3.0 if_changed
    with slowdissolve
    pause 2.0 hard
    play voice "voice/小桃/220101410.ogg"
    ycxt "哥哥......哥哥！"
    play voice "voice/一诚总司/180101320.ogg"
    yczs "小桃......"
    play voice "voice/一诚总司/180101330.ogg"
    yczs "抱歉，我来晚了。"
    play voice "voice/一诚总司/180101340.ogg"
    yczs "抱歉，我不是一个好哥哥。"
    play voice "voice/小桃/220101420.ogg"
    ycxt "呜呜......"
    play voice "voice/小桃/220101430.ogg"
    ycxt "哥哥没有错。"
    play voice "voice/小桃/220101440.ogg"
    ycxt "错的是小桃。"
    play voice "voice/小桃/220101460.ogg"
    ycxt "都怪小桃擅自从哥哥身边逃走。"
    pause 0.1 hard
    scene set only ycxt_cg nisang2
    with dissolve
    play voice "voice/一诚总司/180101350.ogg"
    yczs "小桃......不是你从我的身边逃走。"
    play voice "voice/一诚总司/180101360.ogg"
    yczs "选择逃走的人......是我。"
    play voice "voice/一诚总司/180101370.ogg"
    yczs "一直以来我都在逃避。"
    play voice "voice/一诚总司/180101380.ogg"
    yczs "我一直认为......只要有奶奶陪在你身边就好了。"
    play voice "voice/一诚总司/180101390.ogg"
    yczs "虽然我也曾想过为身为妹妹的你做点什么，但是到头来我还是什么都做不到！"
    play voice "voice/一诚总司/180101400.ogg"
    yczs "不懂怎么面对小孩子。"
    play voice "voice/一诚总司/180101410.ogg"
    yczs "不懂怎么对待女孩子。"
    play voice "voice/一诚总司/180101420.ogg"
    yczs "所以总觉得把一切都交给奶奶的话，这说不定就是我唯一能为你做的事了。"
    play voice "voice/一诚总司/180101430.ogg"
    yczs "就算我在你身边，也不会有好结果出现。"
    play voice "voice/一诚总司/180101440.ogg"
    yczs "一直以来，我都是这样想的......"
    pause 0.1 hard
    scene set only ycxt_cg nisang4
    with dissolve
    play voice "voice/小桃/220101470.ogg"
    ycxt "......"
    play voice "voice/一诚总司/180101450.ogg"
    yczs "就这样，在我察觉到的时候已经变成这样子了。"
    play voice "voice/一诚总司/180101460.ogg"
    yczs "这让我更加不知道该如何面对你这个妹妹了。"
    play voice "voice/一诚总司/180101470.ogg"
    yczs "不知道要怎么样才能当个好哥哥了。"
    play voice "voice/小桃/220101480.ogg"
    ycxt "是、这样子吗？"
    pause 0.1 hard
    scene set only ycxt_cg nisang3
    with dissolve
    $ flcam.move(300, -750, 250, duration=1.5, warper='ease_quad')
    pause 0.5 hard
    play voice "voice/小桃/220101520.ogg"
    ycxt "对不起......"
    play voice "voice/一诚总司/180101580.ogg"
    yczs "小桃？"
    play voice "voice/小桃/220101550.ogg"
    ycxt "老是给哥哥你添麻烦。"
    play voice "voice/一诚总司/180101590.ogg"
    yczs "不对、不是这样的。"
    play voice "voice/一诚总司/180101600.ogg"
    yczs "你没必要放在心上。"
    play voice "voice/一诚总司/180101610.ogg"
    yczs "因为我还是只一个什么都不懂的小鬼而已。"
    play voice "voice/一诚总司/180101620.ogg"
    yczs "从以前就是一个不懂事的小鬼！"
    play voice "voice/一诚总司/180101630.ogg"
    yczs "明明不变得成熟的话是不行的。"
    play voice "voice/一诚总司/180101640.ogg"
    yczs "因为我可是......你的哥哥啊。"
    play voice "voice/小桃/220101560.ogg"
    ycxt "......哥哥。"
    play voice "voice/一诚总司/180101660.ogg"
    yczs "让你寂寞了，对不起。"
    play voice "voice/一诚总司/180101670.ogg"
    yczs "我是这样的一个哥哥，对不起。"
    pause 0.1 hard
    scene set only ycxt_cg nisang5
    with dissolve
    play voice "voice/小桃/220101570.ogg"
    ycxt "不对......"
    play voice "voice/小桃/220101580.ogg"
    ycxt "哥哥你来了。"
    play voice "voice/小桃/220101590.ogg"
    ycxt "来救小桃了。"
    pause 0.1 hard
    scene set only ycxt_cg nisang6
    $ flcam.move(300, -1400, 450, duration=3.0, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/小桃/220101610.ogg"
    ycxt "这样的哥哥，我最喜欢了！"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "风暴平息了。"
    "温柔的雪花飘落到兄妹两人的肩上。"
    "在傍晚的天空中闪耀的第一颗星星，在白雪的点缀下显得格外耀眼。"
    "与此同时附着在我身上的那股不可思议的力量也消失了。"
    "就好像是完成使命沉睡了一般。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day204.shenshe_event04:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    play music second_129 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    show szl_dzf_b3 b3 b3_n2 onlayer screens at side_left('szl'), basicfade
    play voice "voice/水之濑/050101140.ogg"
    szl "风......停了。"
    hide szl_dzf_b3
    pause 1.0 hard
    scene set only shenshe evening xuejian3
    with dissolve
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101150.ogg"
    szl "躲在暗处观察......本以为会发生什么有趣的事情。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/050101160.ogg"
    szl "利用立场抑制风压的能力......吗。"
    play voice "voice/水之濑/050101190.ogg"
    szl "风暴什么的......明明只要一击就能解决掉的。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101210.ogg"
    szl "但是这么做就难免会造成损伤，是为了不伤害那孩子吗。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101220.ogg"
    szl "如果你的力量没有觉醒的话，又会是什么样的结果呢？"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101240.ogg"
    szl "用我的{rb}灵纹{/rb}{rt}rune{/rt}的话......"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101290.ogg"
    szl "另外一位也是他的同伴吧。"
    play voice "voice/水之濑/050101300.ogg"
    szl "为什么都选择这座城市呢。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/050101310.ogg"
    szl "虽然不知道原因......但希望你们还是不要妨碍我的工作。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard

label day204.school_event06:
    scene set only school night outside xuejian2
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_h1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/日向怜/120102000.ogg"
    rxl "那么，没想到会在这里遇到你啊~"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show szl_dzf_b2 b2 b2_n2 onlayer m2 at walkin_l(0.5)
    play voice "voice/水之濑/050101320.ogg"
    szl "怎么？在考试结束之前都没有其他学生会的工作了，身为干部也得专注于复习。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102010.ogg"
    rxl "不是指那个啦，本来还期待你那边会有什么有趣的事情呢，结果什么都没有嘛~"
    play music second_122 fadein 3.0 if_changed
    $ flcam.move(2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_sp1
    play voice "voice/水之濑/050101330.ogg"
    szl "什么事情？"
    show rxl_dzf_b1 b1 b1_ga1
    play voice "voice/日向怜/120102020.ogg"
    rxl "刚才的事情。"
    show szl_dzf_b2 b2 b2_n2
    play voice "voice/水之濑/050101340.ogg"
    szl "......"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102030.ogg"
    rxl "水之濑同学，刚才是去神社了对吧？"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/050101350.ogg"
    szl "......"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102040.ogg"
    rxl "想说谎也没用的哟~不要小瞧了我的{rb}{encyclopedia=clairvoyance}远隔透视{/encyclopedia}{/rb}{rt}clairvoyance{/rt}。"
    show szl_dzf_b2 b2 b2_n2
    play voice "voice/水之濑/050101360.ogg"
    szl "......你果然也是知道些什么的样子。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102050.ogg"
    rxl "毕竟排除目击者是我的工作呢~"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101370.ogg"
    szl "不管怎么说，你会出现在这里也就是说你已经把我的事告诉在场的三人了吧？"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102060.ogg"
    rxl "不是的，知道真相的只有我一个哟~"
    play voice "voice/日向怜/120102070.ogg"
    rxl "我觉得在我了解你的情况之后再决定是否告诉他们也不迟。"
    show szl_dzf_b3 b3 b3_s1
    play voice "voice/水之濑/050101380.ogg"
    szl "是吗......也就是说你的目的不是拉拢{rb}灵继者{/rb}{rt}elfin{/rt}。"
    show szl_dzf_b3 b3 b3_n2
    play voice "voice/水之濑/050101390.ogg"
    szl "而是向世人隐瞒{rb}灵继者{/rb}{rt}elfin{/rt}的存在对吧。"
    show rxl_dzf_b1 b1 b1_ga2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/120102080.ogg"
    rxl "啊......我的口风果然有问题。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102090.ogg"
    rxl "不过嘛，不管哪个机构都想要{rb}灵继者{/rb}{rt}elfin{/rt}吧？毕竟在各种地方都很方便。"
    play voice "voice/日向怜/120102100.ogg"
    rxl "你所属的组织不也是一样的想法吗？"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101400.ogg"
    szl "......"
    show rxl_dzf_b2 b2 b2_s1
    play voice "voice/日向怜/120102110.ogg"
    rxl "你不说的话，我就完全搞不懂你是有“饲主”的，还是“野生”的了。"
    show szl_dzf_b2 b2 b2_n2
    play voice "voice/水之濑/050101410.ogg"
    szl "我和你不一样，口风没那么松。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102120.ogg"
    rxl "原来你那边是保密主义的吗。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101420.ogg"
    szl "你们组织的目的是什么？"
    show rxl_dzf_b1 b1 b1_a1
    play voice "voice/日向怜/120102130.ogg"
    rxl "这句话我原封不动地还给你。"
    hide szl_dzf_b3
    show szl_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101430.ogg"
    szl "既然大家都不愿意说，这样耗下去也不是办法......"
    show rxl_dzf_b1 b1 b1_sp1
    play voice "voice/日向怜/120102140.ogg"
    rxl "你这是要回去复习考试了？"
    hide szl_dzf_b1
    show szl_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101440.ogg"
    szl "丑话说在前头，想用{rb}远隔透视{/rb}{rt}clairvoyance{/rt}跟踪我是没有用的。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102150.ogg"
    rxl "也是呢，对方也是{rb}灵继者{/rb}{rt}elfin{/rt}的话，自然会用念波来干扰。"
    play voice "voice/日向怜/120102160.ogg"
    rxl "就算是更高级的{rb}{encyclopedia=psychometry}接触感应{/encyclopedia}{/rb}{rt}psychometry{/rt}也很容易被识破。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101450.ogg"
    szl "也就是说你的同伴里，有能够使用{rb}接触感应{/rb}{rt}psychometry{/rt}的人呢。"
    hide rxl_dzf_b2 with None
    pause 0.1 hard
    show rxl_dzf_b1 b1 b1_h3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/120102170.ogg"
    rxl "......看来要给我的嘴装上拉链了。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/050101460.ogg"
    szl "那么我先走了。"
    show rxl_dzf_b1 b1 b1_h1
    play voice "voice/日向怜/120102180.ogg"
    rxl "我也回家复习吧~"
    hide szl_dzf_b2
    show szl_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101470.ogg"
    szl "明明讨厌学习的你却会好好复习。"
    show rxl_dzf_b1 b1 b1_h3 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/日向怜/120102190.ogg"
    rxl "当然是复习保健体育呀，你能来帮忙吗？"
    show szl_dzf_b1 b1 b1_s1
    play voice "voice/水之濑/050101480.ogg"
    szl "......果断拒绝！"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ seen_day204_call = False

label day204.home_event01:
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    pause 1.0 hard
    scene set only home night my_room xuejian
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dsf_b3 onlayer m2:
            hide screen investigation_popup
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction left
            sleep jump day204.sleep
        call lhx_dsf_b2 jump day204.call_lhx_rxl:
            sensitive (not seen_day204_call)

label day204.sleep:
    menu:
        "早点休息":
            if not seen_day204_call:
                window mode thought
                me01 "睡觉之前还是先和立花老师通个电话吧。"
                $ flcam.move(0, -100, 400, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            show xz_dsf_b3 b3 b3_h1
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

    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump day204.memory01

label day204.call_lhx_rxl:
    hide xz_dsf_b3
    $ flcam.move(3800, -400, 800, duration=1.5)
    pause 1.0 hard
    show callflash onlayer texture
    pause 3.0 hard
    hide callflash
    investigation call block lhx_dsf_b2 b2 b2_n1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    nvl clear
    play music second_131 fadein 3.0 if_changed
    show lhx_dsf_b2 b2 b2_n1
    c.me01 "立花老师，有好好休息吗？"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/030104470.ogg"
    c.lhx_dsf_b2 "刚刚不用特地送我回来的。"
    c.me01 "不必在意，今天的事情也让你费了不少心吧。"
    show lhx_dsf_b2 b2 b2_ga3
    play voice "voice/立花希/030104480.ogg"
    c.lhx_dsf_b2 "感觉就算我在场也帮不上什么忙......"
    c.me01 "不是那样的，立花老师也帮了很大的忙。"
    c.me01 "总之今天就早点休息吧，不然体力会跟不上的。"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/030104500.ogg"
    c.lhx_dsf_b2 "我也不打算勉强自己，所以正是这样打算的~"
    hide lhx_dsf_b2
    investigation call block rxl_dsf_b1 b1 b1_h3 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show rxl_dsf_b1 b1 b1_h3
    play voice "voice/日向怜/120101950.ogg"
    c.rxl_dsf_b1 "对对，为了不让你太勉强自己，今天我陪你洗澡哦~"
    c.me01 "......"
    hide rxl_dsf_b1
    investigation call block lhx_dsf_b2 b2 b2_ga2 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show lhx_dsf_b2 b2 b2_ga2
    play voice "voice/立花希/030104530.ogg"
    c.lhx_dsf_b2 "全力拒绝......"
    hide lhx_dsf_b2
    investigation call block rxl_dsf_b1 b1 b1_h1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show rxl_dsf_b1 b1 b1_h1
    play voice "voice/日向怜/120101960.ogg"
    c.rxl_dsf_b1 "我会帮你脱掉衣服然后擦洗身子的。"
    hide rxl_dsf_b1
    investigation call block lhx_dsf_b2 b2 b2_a1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show lhx_dsf_b2 b2 b2_a1
    play voice "voice/立花希/030104540.ogg"
    c.lhx_dsf_b2 "敢进来的话我就二话不说地把你丢到宇宙空间去！"
    hide lhx_dsf_b2
    investigation call block rxl_dsf_b1 b1 b1_h3 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show rxl_dsf_b1 b1 b1_h3
    play voice "voice/日向怜/120101970.ogg"
    c.rxl_dsf_b1 "嘴上这么说其实你是想让凉君来帮忙的吧，就那么想要和凉君在一起啊~"
    play sound jump_1
    hide rxl_dsf_b1
    investigation call block lhx_dsf_b2 b2 b2_ga2 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show lhx_dsf_b2 b2 b2_ga2
    play voice "voice/立花希/030104550.ogg"
    c.lhx_dsf_b2 "才、才不是这样的！"
    hide lhx_dsf_b2
    investigation call block rxl_dsf_b1 b1 b1_h1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show rxl_dsf_b1 b1 b1_h1
    play voice "voice/日向怜/120101980.ogg"
    c.rxl_dsf_b1 "变得有精神了呢~"
    hide rxl_dsf_b1
    investigation call block lhx_dsf_b2 b2 b2_s4 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/030104560.ogg"
    c.lhx_dsf_b2 "真是越来越累，我要回房间去了。"
    c.me01 "那么再见了......"
    show lhx_dsf_b2 b2 b2_h1
    play voice "voice/立花希/030104570.ogg"
    c.lhx_dsf_b2 "好的，明天见~"
    hide lhx_dsf_b2
    investigation call block rxl_dsf_b1 b1 b1_h1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    show rxl_dsf_b1 b1 b1_h1
    play voice "voice/日向怜/120101990.ogg"
    c.rxl_dsf_b1 "拜拜~"
    investigation call end
    stop music fadeout 5.0
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -100, 400, duration=3.0)
    $ seen_day204_call = True
    pause 0.5 hard
    jump investigate

label day204.memory01:
    show dreamglass1 onlayer texture with slowerdissolve
    nvl clear
    nvl_narrator "　黑暗。"
    nvl_narrator "　无意识的空间。"
    nvl_narrator "　这是谁眼中的世界呢？"
    nvl_narrator "　为什么。"
    nvl_narrator "　为什么我会在这里。"
    nvl_narrator "　诡异而奇特的光景。"
    nvl_narrator "　无数的记忆碎片扑面而来\n将我吞噬。"
    nvl clear
    nvl_narrator "　群星般闪耀。"
    nvl_narrator "　白雪般晶莹。"
    nvl_narrator "　这些都是谁的记忆？"
    nvl_narrator "　真相。"
    nvl_narrator "　这个世界的真相。"
    nvl_narrator "　光与影的交错。"
    nvl clear
    pcenter "――我不明白。"
    nvl clear
    nvl_narrator "　要想扑灭黑暗，就必须吹熄蜡烛。"
    nvl_narrator "　将光明与黑暗一并送还。"
    nvl_narrator "　这是注定了的答案。"
    nvl_narrator "　守护。"
    nvl_narrator "　守护所谓的正义。"
    nvl_narrator "　我们的敌人......又是谁呢？"
    nvl clear
    nvl_narrator "　好困。"
    nvl_narrator "　身体好沉重。"
    nvl_narrator "　就好像置身大海深处一般。"
    nvl_narrator "　仿佛下一刻意识就要被剥离。"
    nvl_narrator "　听不到声音。"
    nvl_narrator "　闻不到气味。"
    nvl_narrator "　感受不到冷暖。"
    nvl_narrator "　有的只是不停划过的记忆碎片。"
    nvl_narrator "　愤怒、悲伤、孤独，这些就是你的过去。"
    nvl_narrator "　面对命运，我们真的......束手无策吗？"
    pause 1.0 hard
    hide dreamglass2
    with slowerdissolve
    pause 2.0 hard

label day204.memory02:
    play music WTDSB fadein 3.0 if_changed
    scene first_battle_cg-bg one:
        align (0.5, 0.5)
        zoom (1280./2560. * 1.2)
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('Truth'), _("真相"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard
    $ flcam.move(2370, -2928, 1645)
    $ flcam.move(0, 0, 0, duration=7.0, warper='ease_quad')
    with dissolve
    "世界联军" "梅尔·M·科莉娅！你已经被我们包围了，快投降吧！"
    "世界联军" "你的手下都已经被我们的人解决了，现在的你早已是孤立无援了。"
    "世界联军" "这下你就算是插翅也难逃了！"
    mel "逃？我想汝等是搞错了什么吧。"
    mel "因为......"
    show wflash onlayer texture
    play sound swish1
    pause 0.1 hard
    scene first_battle_cg-bg two at right, supersnapzoomout
    pause 0.1 hard
    play sound swish1
    show wflash onlayer texture
    pause 0.1 hard
    scene first_battle_cg-bg two at left, supersnapzoomout
    pause 0.1 hard
    play sound swish1
    show wflash onlayer texture
    pause 0.1 hard
    scene first_battle_cg-bg two at supersnapzoomout:
        align (900./2560., 100./1430.)
    pause 0.1 hard
    play sound swish1
    show wflash onlayer texture
    pause 0.1 hard
    scene first_battle_cg-bg two at top, slowerzoomout2:
        align (2000./2560., 600./1430.)
    "世界联军" "这是......"
    "世界联军" "{rb}共感{/rb}{rt}empathy{/rt}？！"
    "世界联军" "何等恐怖的灵压，光是站在这里就好像已经被杀死了无数次一样。"
    play sound swish
    show wflash onlayer texture
    pause 0.1 hard
    scene set first_battle_cg three:
        queen role01
    $ flcam.move(0, 0, 400)
    $ flcam.move(0, 1300, 0, duration=1.5, warper='power_in_time_warp_real')
    pause 0.5 hard
    fl "与其用这种方式恐吓我们，不如反省一下自己的计划是否真的万无一失如何......梅尔？"
    mel "汝是......哈哈，总算见到一个适合聊天的对象了呢。"
    mel "汝和他们不一样，更确切的来说，孤才是汝的同伴不是吗？"
    fl "我可不记得有过你这样杀人不眨眼的同伴。"
    mel "啊哈哈，孤方才只是开了个玩笑。"
    mel "孤有一个提议，不如汝加入孤的麾下吧？"
    mel "这样一来，至少汝身后的伙伴们就可以免于一死了~"
    mel "抛弃这个肮脏的世界，与孤一起远走世外岂不自在？"
    mel "如何？孤觉得倒是个不错的提议呢！"
    fl "住口！这种要求......"
    "世界联军" "别和她废话了，她这么说也只不过是拖延时间的借口罢了。"
    "世界联军" "此之谓伪善，是她最擅长的伎俩了吧。"
    mel "啊哈哈哈......汝等真这么想孤也是没有办法的。"
    mel "既然汝执意要与孤为敌，孤也只有放弃了。"
    fl "大家小心！"
    scene black
    show wflash onlayer texture
    pause 0.1 hard
    play sound hit1
    scene black
    play music tension fadein 3.0 if_changed
    fl "！！"
    "耳边传来了类似空间被撕裂一般的闷响声。"
    "仿佛五脏六腑都被焚烧殆尽。"
    "能够真实地感受到的恐惧。"
    "好难受。"
    "明明只有一个人，却如此的棘手。"

label day204.memory03:
    $ persistent.break_title = True
    $ flcam.move(0, 0, 400)
    scene set first_battle_cg three:
        queen role01
    $ flcam.move(0, 1300, 0, duration=1.5, warper='power_in_time_warp_real')
    pause 0.5 hard
    mel "虽然很可惜，不过汝执意要与孤为敌也只好得罪了。"
    mel "咦......？"
    $ camera_move(1500, 14750, 800, duration=5.0, warper='power_in_time_warp_real')
    stop music fadeout 3.0
    "此时梅尔才察觉到了异样，她缓缓低下了头。"
    "世界联军" "现在才察觉到，已经太迟了！"
    "黑色的陨铁如同禁锢的冰霜一般，牢牢地固定在了梅尔全身的关节处。"
    "这种特殊的材质能够吸附灵力的波动，即使对方再强大也会多少受到影响。"
    "世界联军" "结束了梅尔！{rb}念动立场{/rb}{rt}psychokinesis{/rt}！"
    play sound heavyrainswoosh2
    show wflash onlayer texture
    show hr3 onlayer f2:
        xpos -0.04339
        ypos 1195
        alpha 1.0
    show hr2 onlayer f2:
        xpos -0.1953
        ypos 328
        rotate -33
        zoom 1.251
        alpha 2
    $ flcam.move(0, 13750, 0, duration=1.0, warper='power_in_time_warp_real')
    play music deathofdignity fadein 1.0 if_changed
    mel "......"
    "下一秒，无数的针雨就向梅尔飞来。"
    scene white
    pause 0.3 hard
    play sound melanojumpswish
    $ flcam.move(2970, 1650, 0)
    scene set first_battle_cg four:
        bush bush01 
        role2 role02 
        rain rain01
    $ flcam.move(3870, -1050, 1380, duration=0.5, warper='power_in_time_warp_real')
    play ambience1 heavyrainfollow fadein 3.0
    "世界联军" "什？！"
    $ flcam.move(6000, 848.4, 0, duration=2.0, warper='power_in_time_warp_real')
    "世界联军" "怎、怎么可能......！！"
    fl "......"
    "世界联军" "还是第一次见到连陨铁都无法束缚住的天使。"
    "世界联军" "这就是实力的差距吗。"
    "肉眼已经无法跟上她的动作了，就连灵力汇聚起来的针雨也逐渐被甩开。"
    "但是......"
    $ flcam.move(3870, -1050, 1380, duration=1.0, warper='power_in_time_warp_real')
    mel "哎呀呀......这个真烦人呢。"
    "世界联军" "用{rb}远隔透视{/rb}{rt}clairvoyance{/rt}操控的{rb}念动立场{/rb}{rt}psychokinesis{/rt}，即使你跑到天涯海角也能够跟过去。"
    "世界联军" "看到了吗梅尔，这就是联军大家齐心协力想要打倒你的决心。"
    mel "啊啦，那还真是辛苦汝等了。"
    mel "那么既然如此，孤不回应一下的话岂不是会很寂寞了吗。"
    pause 0.5 hard
    scene black
    play sound swish
    $ mouse_visible = False
    $ suppress_overlay = True
    $ _skipping = renpy.seen_audio("video/ms2_melanojump.mp4")
    scene black
    pause 1.0 hard
    show movie onlayer master
    play movie "video/ms2_melanojump.mp4"
    play ambience1 "video/ms2_melanojump.mp3"
    pause 3.0 hard
    $ mouse_visible = True
    $ suppress_overlay = False
    $ _skipping = True
    stop movie
    hide movie
    stop ambience1 fadeout 1.0
    $ flcam.move(0, 0, 0)
    scene set only first_battle_cg_normal six
    "世界联军" "消、消失了？！"
    "世界联军" "侦察班，快找到那家伙的位置！"
    "世界联军" "检测到{rb}灵纹{/rb}{rt}rune{/rt}波动......在上面！"
    show wflash onlayer texture
    play sound swish
    pause 0.1 hard
    scene first_battle_cg-bg seven:
        zoom 0.5
        yoffset scale(-720)
    fl "？！"
    show first_battle_cg-bg seven:
        zoom 0.5
        easein 1.0 yoffset 0
    pause 1.0 hard
    "世界联军" "什、什么时候？！"
    "世界联军" "{rb}幻镜化物{/rb}{rt}apports{/rt}吗？！"
    show wflash onlayer texture
    pause 0.1 hard
    show hr3 at center, supersnapzoomout:
        align (1280./2560., 720./1440.)
    play sound heavyrainswoosh2
    "世界联军" "但、但是即便如此，你也还是没办法逃过陨铁和{rb}灵继者{/rb}{rt}elfin{/rt}的联合攻击！"
    show wflash onlayer texture
    pause 0.1 hard
    scene set only first_battle_cg_normal eight
    "世界联军" "太好了，直接命中！"
    "世界联军" "结、结束了吗......"
    stop music fadeout 3.0
    stop ambience1 fadeout 3.0
    pause 2.0 hard
    scene black
    with dissolve
    nvl clear
    pcenter "　　——psi_missing"
    nvl clear
    play sound heavyrainlanding fadeout 1.0
    pause 6.0 hard
    "世界联军" "......欸？"
    $ flcam.move(0, 0, 400)
    scene set first_battle_cg three:
        queen role01
    $ flcam.move(0, 1300, 0, duration=1.5, warper='power_in_time_warp_real')
    pause 0.5 hard
    mel "啊啦啊啦~"
    mel "要是被打中的话可不是闹着玩的呢~"
    "世界联军" "什......什么？！"
    "世界联军" "利用我们的攻击化解了陨铁的束缚！"
    "世界联军" "面对我们的全力一击竟然毫发无伤......"
    play music stabbinghits fadein 3.0 if_changed
    mel "弗兰小姐，汝等的立场和实力孤都大致了解了。"
    mel "人类那些所谓的“讨伐”背后肮脏的理由孤也毫无兴趣。"
    mel "不过，孤希望汝能够明白。"
    mel "现在可不仅仅是......胜利或者失败的问题。"
    mel "汝等最好从开始就不要有与孤一战的念头。"
    mel "毕竟汝等这种夹杂了“私欲”的人性是无法彻底消灭孤的。"
    mel "不如说汝等才是......孤真正的信徒。"
    "世界联军" "真的......没有办法战胜她吗。"
    fl "利用人性的弱点，让众人臣服于你就是你的目的了吗？"
    fl "既然如此你又何必装模作样地对我好言相劝呢？"
    fl "我们的信念从一开始......就无法相互包容的！"
    mel "也是呢，不过......"
    mel "汝口中想要保护的“人性”，汝当真明白了吗。"
    mel "不过无论如何，如果汝等执意要与孤为敌的话。"
    mel "比起争论，不如让汝等亲自“死”一次来的简单吧。"
    "世界联军" "她在......说什么？"
    "世界联军" "小心，有什么要来了......"
    pause 0.5 hard
    scene black
    with dissolve
    stop music fadeout 10.0
    $ mouse_visible = False
    $ suppress_overlay = True
    $ _skipping = renpy.seen_audio("video/ms2_nuke.mp4")
    scene black
    pause 3.0 hard
    show movie onlayer master
    play movie "video/ms2_nuke.mp4" noloop
    $ renpy.music.play("video/ms2_nuke.mp3", synchro_start='movie', loop=False)
    pause 30.0 hard
    $ mouse_visible = True
    $ suppress_overlay = False
    $ _skipping = False
    stop movie
    hide movie
    stop music fadeout 1.0
    scene black
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    if persistent.break_title:
        # $ renpy.quit(True)
        $ persistent.restart_place = "day204.memory04"
        $ renpy.save(persistent.restart_place)
        return

label day204.memory04:
    bookmark
    "........."
    "......"
    $ mouse_visible = False
    $ suppress_overlay = True
    $ _skipping = renpy.seen_audio("video/ms2_nuke_reverse.mp4")
    scene black
    show movie onlayer master
    play movie "video/ms2_nuke_reverse.mp4" noloop
    $ renpy.music.play("video/ms2_nuke_reverse.mp3", synchro_start='movie', loop=False)
    pause 6.0 hard
    $ mouse_visible = True
    $ suppress_overlay = False
    $ _skipping = True
    stop movie
    hide movie
    stop music fadeout 1.0
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    $ flcam.move(0, 0, 400)
    scene set first_battle_cg three:
        queen role01
    $ flcam.move(0, 1300, 0, duration=1.5, warper='power_in_time_warp_real')
    pause 0.5 hard
    mel "看到了吗，这就是汝等的下场。"
    fl "......"
    "世界联军" "......"
    "刚刚......"
    nvl clear
    pcenter "——发生了什么？"
    pause 1.0 hard
    play music linesaredrawn fadein 1.5 if_changed
    scene white
    with dissolve
    "最初的记忆，是刹那间绽放的耀眼的光。"
    "与黑暗和邪恶相悖的，纯白色光芒......"
    "无人幸免。"
    "不管是我，还是联盟的大家，亦或是其他无辜的人类。"
    "所有的人仿佛都在那一刻被抹去了。"
    "数以万计的人，仅仅是一瞬间就......"
    "是她让我们看到了自己内心的恐惧吗。"
    "不，这种充斥着全身上下的死亡恐惧，恰恰说明了刚刚的一切都不是幻觉。"
    "我们刚刚，是从死亡的边缘擦肩而过的吗......"
    scene black
    with dissolve
    $ flcam.move(0, 0, 0)
    scene set only first_battle_cg_normal nine
    with slowdissolve
    show vig1 onlayer texture
    "对方已经获得了毁灭世界的能力。"
    "可是为什么她没有这么做呢？"
    "如果一开始她的目的就是我的话，为什么又要在世界各地引起骚动呢？"
    "仅仅是为了引我上钩吗？"
    show vig2 onlayer texture
    "不对，没那么简单。"
    "她说过充斥着“欲望”的人性都是她的信徒。"
    "也许从一开始这场战斗就毫无意义。"
    "人性的黑暗是无法被彻底消灭的，所以她才会毫无畏惧地出现在我们面前。"
    show vig3 onlayer texture
    "她那股夸张的能力，也巧好说明了问题的人性扭曲的强大。"
    "只有最纯粹的正义才能与之对抗。"
    "不、不对。这是一个充满矛盾的立场。"
    "当人性背离了“邪恶”，就没有所谓的“正义”存在了。"
    "相反只有真正理解了“邪恶”之人，才有资格行使最正确的“正义”。"
    "联军看似团结，实则内部的愚昧与分歧早已根深蒂固。"
    "从一开始胜利的天平就已经倾斜了......"

label day204.memory05:
    scene white
    $ mouse_visible = False
    $ suppress_overlay = True
    $ _skipping = renpy.seen_audio("video/ms2_portal.mp4")
    show movie onlayer master
    play movie "video/ms2_portal.mp4" noloop
    play ambience2 "video/ms2_portal.mp3" noloop
    pause 4.0 hard
    $ mouse_visible = True
    $ suppress_overlay = False
    $ _skipping = True
    stop movie
    hide movie
    scene white
    pause 0.5 hard
    show first_battle_cg-bg ten:
        contains:
            subpixel True
            "first_battle_cg-bg ten"
            zoom 3.0
            align (1720.0/2560, 350.0/1440)
            yoffset -200
            alpha 0
            parallel:
                easein 0.3 alpha 1
            parallel:
                easein 0.7 yoffset 0
        contains:
            subpixel True
            "first_battle_cg-bg ten"
            zoom 3.0
            align (1950.0/2560, 350.0/1440)
            yoffset 200
            alpha 0
            0.7
            easein 0.7 yoffset 0 alpha 1
        contains:
            subpixel True
            "first_battle_cg-bg ten"
            zoom 2.0
            align (1950.0/2560, 850.0/1440)
            xoffset -200
            alpha 0
            1.4
            easein 0.7 xoffset 0 alpha 1
        contains:
            subpixel True
            "first_battle_cg-bg ten"
            zoom 0.55
            align (0.5, 0.5)
            alpha 0
            2.1
            ease 0.7 zoom 0.5 alpha 1
    mel "那么诸位，孤还有要事在身，就不奉陪了。"
    mel "对了，下次见面的时候，希望能够稍微“有趣”一些呢~"
    mel "汝是叫弗兰对吧。"
    mel "不管汝最后如何选择。"
    show first_battle_cg-bg eleven:
        align (1100./2560., 100./1440.)
        zoom 1.3
    mel "都要活得潇洒一些哟~"
    scene black
    with None
    $ mouse_visible = False
    $ suppress_overlay = True
    $ _skipping = renpy.seen_audio("video/ms2_portal_reverse.mp4")
    show movie onlayer master
    play movie "video/ms2_portal_reverse.mp4" noloop
    play ambience2 "video/ms2_portal_reverse.mp3"
    pause 3.0 hard
    $ mouse_visible = True
    $ suppress_overlay = False
    $ _skipping = True
    stop movie
    hide movie
    stop ambience2 fadeout 1.0
    scene black
    pause 4.0 hard
    nvl clear
    pcenter "　　――下次见面的时候{p}　　　　　　我......又该如何选择呢？"
    pause 1.0 hard

label day204.memory06:
    scene black
    with dissolve
    $ flcam.move(-900, -1733, 1120)
    scene set first_battle_cg twelve:
        partner angry01
    $ flcam.move(-900, -2733, 0, duration=1.5, warper='power_in_time_warp_real')
    fl "公主！您没事吧？！振作一点......"
    fl "公主！"
    fl "公主......大人！！！"
    $ flcam.move(-460, -3500, 1200, duration=3.0, warper='power_in_time_warp_real')
    "公主" "弗......兰......"
    "公主" "大家......"
    "公主" "大家都......"
    fl "那都是幻觉，不要被欺骗了！"
    "公主" "赢不了的......"
    "公主" "谁来都没用......"
    pause 0.5 hard
    scene black
    with dissolve
    nvl clear
    pcenter "  啊啊，果然是这样吗......"
    pause 1.0 hard
    $ flcam.move(-500, -4160, 1140, duration=3.0, warper='power_in_time_warp_real')
    scene set first_battle_cg twelve:
        partner normal02
    $ flcam.move(-500, -4160, 1150, duration=3.0, warper='power_in_time_warp_real')
    fl "十分抱歉......公主殿下。"
    scene set first_battle_cg twelve:
        partner normal01
    $ flcam.move(-870, -3250, 1250, duration=1.5, warper='power_in_time_warp_real')
    "公主" "呜呜......呜呜呜！"
    fl "已经没事了，真的......没事了。"
    fl "我会一直在您身边的。"
    $ flcam.move(-900, -2733, 0, duration=3.0, warper='power_in_time_warp_real')
    "公主" "啊......啊啊啊，对、对不起......呜......呜啊啊！"
    "公主" "对......不起......没能帮上你的忙......对不起！"
    fl "没事的......"
    fl "全都交给我就行了。"
    fl "我一定会找到，能够彻底打败梅尔的{rb}灵继者{/rb}{rt}elfin{/rt}给您看的。"
    fl "下一次......我绝不会再输了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day204.memory07:
    nvl clear
    pcenter "　　刚才那些......"
    pause 0.5 hard
    nvl clear
    pcenter "    究竟是谁的记忆呢......"
    pause 1.0 hard
    play music scene_thinking fadein 5.0 if_changed
    scene set ritfrontyard spring day:
        mid spring day
        frontl spring day
        frontr spring day
    $ flcam.move(0, 0, 400)
    $ flcam.move(0, 0, 0, duration=1.5)
    with dissolve
    pause 1.0 hard
    me01 "这里是......？"
    $ flcam.move(0, 200, 300, duration=1.5)
    play sound wood_door_knock
    pause 2.0 hard
    "看起来是十分古老的欧式建筑。"
    "没有多想，我随手敲响了房门。"
    play sound wood_door_knock
    pause 2.0 hard
    me01 "不好意思打扰了，请问有人在吗？"
    pause 2.0 hard
    play sound wood_door_open
    scene set 02ritona:
        front
    $ flcam.moves([
        (0,      0,   0, 0, 0.0, 'linear'),
        (0,      0,   0, 0, 0.5, 'linear'),
        (0, -14750, 300, 0, 4.5, 'ease_cubic')
    ])
    with dissolve
    pause 3.5 hard
    "门开了。"
    "是一位看起来和我差不多年纪的女孩。"
    scene set ritfrontyard spring day:
        mid spring day
        frontl spring day
        frontr spring day
    show ritona b3 fb1 fa0 fc01 onlayer m2:
        xpos 0.5
        xzoom -1
    $ flcam.move(0, 0, 0)
    $ flcam.move(0, 200, 300, duration=1.5)
    me01 "那个......莫非我打扰到你休息了？"
    show ritona b1 fb1 fa1 fc02
    stranger "......"
    show ritona b1 fb1 fa1 fc11
    stranger "这就是你来这里想说的话吗？"
    show ritona b1 fb1 fa1 fc13
    stranger "真是有趣的人类。"
    me01 "你说人类......莫非你是？"
    show ritona b1 fb1 fa0 fc11
    stranger "没错，我并不是人类。"
    stranger "确切地说，我并不是诞生在这颗星球上的生命。"
    me01 "天......使？"
    show ritona b1 fb1 fa5 fc02
    stranger "你好像知道些什么......"
    me01 "啊那个......抱歉。"
    show ritona b3 fb4 fa0 fc11
    stranger "我并不是要责怪你的意思，能够来到这里想必你也不是一般的人。"
    me01 "来到......这里？"
    me01 "我只记得我好像是睡着了，然后就......"
    show ritona b1 fb4 fa5 fc11
    stranger "睡着了？"
    show ritona b1 fb4 fa5 fc12
    stranger "就这样？"
    me01 "是的。"
    show ritona b1 fb4 fa5 fc02
    stranger "......"
    me01 "......"
    show ritona b4 fb3 fa9 fc11
    stranger "你是从何得知“天使”这个词的？"
    me01 "是一名自称是“星天宫”神官的人告诉我的。"
    me01 "听起来是个非常厉害的机构，具体的细节我也不是很清楚。"
    show ritona b3 fb4 fa0 fc11
    stranger "星天宫......吗。"
    stranger "你的情况我大致了解了。"
    show ritona b3 fb4 fa0 fc01
    stranger "那么你来找我究竟有什么事？"
    me01 "那个，虽然刚才也说过了并不是我自己来的，只是因为一些原因才......"
    me01 "我想看看能不能找到“那段记忆”的主人。"
    show ritona b1 fb4 fa5 fc01
    stranger "......"
    me01 "那个......你还好吗？"
    show ritona b1 fb4 fa5 fc11
    stranger "弗兰·A·克里伍德，这是我的名字，你也可以叫我弗兰。"
    me01 "我知道了弗兰小姐。我叫神野凉，是一名日本的普通学生。"
    show ritona b1 fb4 fa5 fc01
    ritona "学生？真的假的？"
    ritona "现在星天宫的招人条件越来越草率了。"
    me01 "那个......其实我并不是星天宫的成员。"
    show ritona b1 fb5 fa9 fc11
    ritona "欸？"
    me01 "所以说，我只是睡着了碰巧来到这里的。"
    me01 "具体的情况我也不是很清楚。"
    show ritona b3 fb1 fa0 fc01
    ritona "......"
    ritona "你......很特别，跟我来吧。"
    me01 "那个......还有一个问题可以吗？"
    show ritona b1 fb5 fa9 fc11
    ritona "什么？"
    me01 "为什么你说话没有声音呢？"
    me01 "这个游戏里几乎所有的女性角色都有配音的吧？"
    show ritona b1 fb4 fa2 fc11 s
    ritona "欸......？"
    show ritona b1 fb4 fa2 fc13 s
    ritona "啊，那是因为......"
    me01 "因为？"
    ritona "我是主角嘛，主角不都是没有配音的吗，就像你一样。"
    me01 "......原来如此，你这么说的话倒也符合常理。"
    me01 "可是身为女性角色却没有配音的话，是很难引起大家注意的不是吗。"
    ritona "......"
    me01 "弗兰小姐？"
    show ritona b1 fb1 fa2 fc15 s
    ritona "总、总之，这个问题不要再问了，老老实实跟我来吧！"
    with vpunch
    me01 "呜哇！不要扯我的衣服啊！"
    hide ritona
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day204.memory08:
    default seen_day204_stats = False
    play music ritroom_day fadein 3.0 if_changed
    play ambience1 ritroom_fireplace fadein 3.0 if_changed

    if not seen_day204_stats:
        scene set ritroom day:
            eggs
            eggscover
            windchime
            midl
            midc
            midr
            midt
            front1
            front2
            front3
            front6
            front4
            front5
        $ flcam.move(-14575, 0, 0)
        $ flcam.move(14575, 0, 0, duration=3.0, warper='ease_cubic')
        with dissolve
        pause 3.5 hard
        $ flcam.move(-5400, -100, 400, duration=1.5)
        pause 0.25 hard
        show ritona b3 fb5 fa1 fc12 s onlayer m2:
            xpos 0.5
        show ritona b1 fb1 fa0 fc11 s
        ritona "这里是我的研究所，以后你找我的话就来这里吧。"
        me01 "我还能再来吗？"
        show ritona b3 fb5 fa1 fc02
        ritona "谁知道呢，又不是我拉你来的。"
        me01 "......"
        me01 "有种很敷衍的感觉。"
        show ritona b1 fb2 fa5 fc12
        ritona "我说你啊，心里话能不能别随便说出来。"
        ritona "不知道这样很失礼的吗？"
        me01 "抱歉......"
        me01 "因为之前使用过{rb}念动力场{/rb}{rt}psychokinesis{/rt}，所以至今都没有缓过神来。"
        show ritona b1 fb5 fa2 fc01
        ritona "你......参加过战斗吗？"
        me01 "嘛，算是吧。虽然大多是时候都是毫无还手之力的那种。"
        show ritona b1 fb1 fa5 fc01
        ritona "嘿~是这样啊......"
        me01 "那个，弗兰小姐，你那眼神莫非是在嘲笑我吗？"
        show ritona b2 fb1 fa5 fc12
        ritona "你脑子生锈了吗？"
        me01 "竟然直接开骂了！"
        ritona "你在说什么傻话啊，用脑子啊脑子。"
        me01 "什么意思？"
        show ritona b1 fb1 fa5 fc02
        ritona "明明不是星天宫的成员却被卷入战斗。"
        ritona "在什么都不知道的情况下，想要活下去的话就动动脑子。"
        me01 "哈啊......"
        show ritona b1 fb4 fa3 fc11
        ritona "真是的，真不知道你是怎么活过来的。"
        me01 "说来惭愧......"
        show ritona b1 fb4 fa3 fc01
        ritona "真拿你没办法，既然来都来了我就勉强帮你下好了。"
        me01 "真的吗？！"
        $ flcam.move(-5160, -120, 450, duration=0.33)
        show ritona b1 fb4 fa3 fc12
        ritona "总{w=0.33}{nw}"
        $ flcam.move(-4920, -105, 500, duration=0.33)
        extend "而{w=0.33}{nw}"
        $ flcam.move(-4680, -90, 550, duration=0.33)
        extend "言{w=0.33}{nw}"
        $ flcam.move(-4440, -75, 600, duration=0.33)
        extend "之......"
        show ritona b1 fb4 fa3 fc01
        ritona "先从打扫房间开始吧。"
        with vpunch
        me01 "你其实只是想找个人帮你打扫房间吧喂！"
        show ritona b1 fb4 fa2 fc12 s
        ritona "愚、愚蠢之徒！我可是很忙的！"
        ritona "如果我想的话，打扫房间这种事还不是......"
        me01 "还不是？"
        ritona "......"
        show ritona b1 fb4 fa1 fc11 s
        ritona "那么我们先从{rb}灵纹{/rb}{rt}rune{/rt}的基础知识开始讲起吧~"
        me01 "别扯开话题啊！果然只是想让我给你打工的吧？！"
        show ritona b1 fb4 fa2 fc12 s
        ritona "总、总之，这里以后就是你修炼的场所了，我会帮助你成为更出色的{rb}灵继者{/rb}{rt}elfin{/rt}的，你就放心好了。"
        me01 "总感觉前途一片黑暗啊......"
        show ritona b1 fb1 fa1 fc01
        $ flcam.stop()
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
        show screen investigation_popup(investigation.hint2)
    else:
        pause 0.5 hard
        scene black with dissolve
        pause 3.0 hard
        scene set ritroom day:
            eggs
            eggscover
            windchime
            midl
            midc
            midr
            midt
            front1
            front2
            front3
            front6
            front4
            front5
        show ritona b3 fb1 fa0 fc02 onlayer m2:
            xpos 0.5
        $ flcam.move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-14575.0), scale(-0.0), 0.0) to (scale(+14575.0), scale(+0.0), 1350.0)
        menu ritona onlayer m2:
            camera_pos (scale(-4140), scale(-510), 800)
            screen_pos (0.5, 1.0)
            screen_direction left
            member jump day204.stats
            sleep jump day204.memory_sleep

label day204.stats:
    $ seen_day204_stats = True
    hide screen investigation_popup
    
    python:
        for role in local_config.party:
            role.hp = role.max_hp
            role.mp = role.max_mp

    $ local_config.current_mode == "Consumables"
    $ local_config.current_actor = local_config.party[0]

    call screen stats
    jump investigate

label day204.memory_sleep:
    menu:
        "结束梦境":
            hide screen investigation_popup
            if not seen_day204_stats:
                window mode thought
                me01 "还是先按照芙兰的指示看看角色信息吧。"
                $ camera_move(-5400, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(-5400, -100, 400, duration=1.5)
            pause 0.5 hard
            show ritona b1 fb4 fa3 fc01
            ritona "我们还会再见的，神野凉......"
        "{#cancel}再等等":
            ritona "还有什么事情要考虑的吗？"
            $ camera_move(-5400, 100, 200, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard

    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump day204_2

label day204_2:
    play music second_103 fadein 3.0 if_changed
    "温柔的雪花继续飘落。"
    "已经记不清是第几个冬季了。"
    pause 1.0 hard
    scene set only balltower snow day big
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "我和希菲尔经常会来到钟楼广场上玩耍。"
    "那可能是我在雪见市待过的，最快乐的时光了。"
    "离开樱华镇，告别了翔子之后，我感觉一切都变了。"
    "变得陌生，变得可怕了。"
    "是希菲尔的笑容让我重新找回了对羁绊的渴望。"
    pause 1.0 hard
    scene set only balltower snow day xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1:
        xpos 0.5
    show alu_ct_b1 b1 b1_1 onlayer m2:
        xpos 0.53 ypos 0.6
    play voice "voice/希菲尔/000201430.ogg"
    xfe "凉君，你看你看~"
    me01 "这是......什么？"
    "一只奇怪的生物停在了希菲尔的肩上。"
    show ts_xfe_yjz_b2 b2 b2_sp1
    play voice "voice/希菲尔/000201440.ogg"
    xfe "雪兔？"
    me01 "这是你自己做的吗？"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/000201450.ogg"
    xfe "不是做的哟，是抓到的~"
    me01 "抓到的？"
    show ts_xfe_yjz_b2 b2 b2_h4
    play voice "voice/希菲尔/000201460.ogg"
    xfe "虽然也不是很清楚，但是看它啪嗒啪嗒地飞着，就“叭咕”下去了哟~"
    me01 "这个......会飞吗？"
    show ts_xfe_yjz_b2 b2 b2_sp1
    play voice "voice/希菲尔/000201470.ogg"
    xfe "是吗？"
    me01 "所以说发问的是我吧......"
    pause 0.5 hard
    play sound fly1
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(-550, -900, 250)
    scene set only alu_cg one
    with dissolve
    pause 1.0 hard
    me01 "啊......飞走了。"
    "用耳朵啪嗒啪嗒地飞走了。"
    "那个原来是翅膀吗......"
    pause 0.5 hard
    play sound jump_1
    show xfe sd1 onlayer m2:
        xpos 0.15 ypos 0.0
    with vpunch
    play voice "voice/希菲尔/000201480.ogg"
    xfe "叭咕！"
    "希菲尔纵身一跃，用嘴叼住了飞行中的不明生物。"
    "那姿势就像是接飞盘的小狗一样。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian
    show snow_level1 onlayer fg
    show alu_ct_b6 b6 b6_1 onlayer m2:
        xpos 0.49 ypos 0.68
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1 at flu_down(0.25, 20):
        xpos 0.5
    with dissolve
    play voice "voice/希菲尔/000201490.ogg"
    xfe "乖孩子乖孩子~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    pause 1.0 hard
    "从那以后，经常能看到希菲尔和雪兔一起出现的场景。"
    "对方似乎也是放弃了逃跑的念头，老老实实地待在希菲尔的肩膀上。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian
    with dissolve
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1:
        xpos 0.5
    show alu_ct_b1 b1 b1_1 onlayer m2:
        xpos 0.53 ypos 0.6
    pause 0.5 hard
    me01 "被调教得听话了吗。"
    me01 "总觉得很般配。"
    "因为两边都是白色的，所以看起来更像是融为一体的感觉。"
    show ts_xfe_yjz_b2 b2 b2_sp1
    play voice "voice/希菲尔/000201500.ogg"
    xfe "这只鸟是叫雪兔对吧？"
    me01 "没有饲主的话就没有名字吧。"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/000201520.ogg"
    xfe "没有名字的话，好可怜的说......"
    me01 "这样的话就由希菲尔给它取个名字吧。"
    show ts_xfe_yjz_b2 b2 b2_sp1
    play voice "voice/希菲尔/000201530.ogg"
    xfe "希菲尔来取？"
    me01 "感觉你们已经是好朋友了。"
    show ts_xfe_yjz_b2 b2 b2_h3
    show alu_ct_b1 b1 b1_4
    play voice "voice/希菲尔/000201540.ogg"
    xfe "朋友......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m1:
        xpos 0.5
    show alu_ct_b1 b1 b1_3
    play voice "voice/希菲尔/000201550.ogg"
    xfe "那就叫它凉君！"
    me01 "这样真的好吗？"
    show ts_xfe_yjz_b3 b3 b3_n1
    play voice "voice/希菲尔/000201560.ogg"
    xfe "嗯，因为希菲尔的朋友，就是凉君嘛~"
    me01 "但是名字一样的话很容易混淆的。"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/000201570.ogg"
    xfe "是这样吗？"
    me01 "是啊。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1:
        xpos 0.5
    play voice "voice/希菲尔/000201580.ogg"
    xfe "这样啊，那就叫凉君一号~"
    me01 "我竟然是二号？！"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/000201590.ogg"
    xfe "不是的，凉君就是凉君呀~"
    me01 "总觉得很讨厌啊。"
    show ts_xfe_yjz_b2 b2 b2_s1
    show alu_ct_b1 b1 b1_2
    play voice "voice/希菲尔/000201600.ogg"
    xfe "取名字好难的说......"
    me01 "就从希菲尔最喜欢的东西入手吧，像是吃的东西之类的。"
    show ts_xfe_yjz_b2 b2 b2_h1
    show alu_ct_b1 b1 b1_5
    play voice "voice/希菲尔/000201610.ogg"
    xfe "雪雪！"
    me01 "你平时就吃这个吗？！"
    show ts_xfe_yjz_b2 b2 b2_h4
    play voice "voice/希菲尔/000201620.ogg"
    xfe "兔兔！"
    me01 "能不能不要用那么随便的名字。"
    show ts_xfe_yjz_b2 b2 b2_a1
    show alu_ct_b1 b1 b1_2
    play voice "voice/希菲尔/000201630.ogg"
    xfe "希菲尔已经拼尽全力去思考了哟。"
    me01 "那就叫{rb}阿露{/rb}{rt}阿露毕蕾欧{/rt}吧？"
    me01 "夜晚的星辰，是银河中的一员。"
    show ts_xfe_yjz_b2 b2 b2_h1
    show alu_ct_b1 b1 b1_4
    play voice "voice/希菲尔/000201640.ogg"
    xfe "嗯~"
    "看样子应该是挺喜欢这个名字的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day big
    with dissolve
    play ambience1 zhong_rill fadein 3.0
    pause 1.0 hard
    "随着钟声的响起。"
    "一天中最快乐的时光也结束了。"
    stop ambience1 fadeout 5.0
    pause 1.0 hard
    scene set only balltower snow day xuejian
    $ flcam.move(0, 0, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    "希菲尔抬头望向钟楼。"
    "之前也是，每当这个时候希她会投以羡慕的眼光。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/000201660.ogg"
    xfe "这座钟楼，每当特定的时间就会响起。"
    play voice "voice/希菲尔/000201670.ogg"
    xfe "经年累月，一直以来都是如此。"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/000201680.ogg"
    xfe "从比一百年还要久远的过去就一直，没有改变......"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/000201690.ogg"
    xfe "这是......多么让人羡慕的事情。"
    play voice "voice/希菲尔/000201700.ogg"
    xfe "不会改变的事物......真是让人羡慕。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201710.ogg"
    xfe "希菲尔也希望雪见市的这场雪，能和这座钟楼一样继续持续下去，不要改变。"
    me01 "希菲尔你喜欢冬天吗？"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h4 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201720.ogg"
    xfe "叭咕叭咕~"
    me01 "别吃雪啊......"
    show ts_xfe_yjz_b3 b3 b3_n1
    play voice "voice/希菲尔/000201730.ogg"
    xfe "因为雪非常的好吃，所以希菲尔最喜欢冬天了哟~"
    me01 "就算吃坏肚子也没关系吗。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201740.ogg"
    xfe "那样的话，就不能和凉君玩了？"
    me01 "是啊。"
    show ts_xfe_yjz_b2 b2 b2_s2
    play voice "voice/希菲尔/000201750.ogg"
    xfe "是这样的话，我就忍耐吧......"
    me01 "抱歉我只是开个玩笑，所以别摆出垂头丧气的表情嘛。"
    me01 "希菲尔好像是特殊的体质，就算吃雪也不会弄坏肚子。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201760.ogg"
    xfe "真的吗？"
    me01 "大概吧......"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201770.ogg"
    xfe "那以后也能和凉君一起玩吗？"
    "我并没有回答她。"
    "对于从小就和父亲漂泊四方的我来说，告别可谓是家常便饭。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    pause 1.0 hard
    play music second_117 fadein 3.0 if_changed
    "回去的路上我和希菲尔一起撑着伞漫步在无人的街道上。"
    "就在那时，我向她告白了......"
    pause 1.0 hard
    hide snow_level1
    scene set only xfe_cg memory1
    with dissolve
    pause 1.0 hard
    "并不是只是因为单纯的喜欢才这么做的。"
    "我和希菲尔说了我的身世。"
    "担心有一天会和她分开。"
    "以及我没有朋友，不主动与人亲近的原因。"
    "本来一直都是孤身一人，被疏远对我而言也不是什么大事。"
    "但此刻我却害怕希菲尔会像其他人那样离我而去。"
    "因为唯独她我不想失去。"
    "所以本来是不想说的。"
    "但不知为何，对她我不想有任何隐瞒。"
    "记得那时她是这么说的——"
    pause 0.1 hard
    scene set only xfe_cg memory2
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/000201780.ogg"
    xfe "妖精和人类，是能够和平共处的哟~"
    play voice "voice/希菲尔/000201790.ogg"
    xfe "是能成为朋友的。"
    pause 0.1 hard
    scene set only xfe_cg memory3
    with dissolve
    play voice "voice/希菲尔/000201800.ogg"
    xfe "千冬给希菲尔讲的故事里，就是这样的......"
    play voice "voice/希菲尔/000201810.ogg"
    xfe "妖精和人类在迎来春天之前，是可以幸福生活在一起的。"
    play voice "voice/希菲尔/000201820.ogg"
    xfe "我想如果没有纷争或者痛苦的话，一定也能在迎来春天之后开开心心地生活在一起。"
    play voice "voice/希菲尔/000201830.ogg"
    xfe "所以呢，希菲尔和凉君也是可以变成那样的~"
    pause 0.1 hard
    scene set only xfe_cg memory1
    with dissolve
    $ flcam.move(1800, -2100, 750, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/000201870.ogg"
    xfe "降生于妖精之星的雪花，以及降生于人类星球的雪花是能够成为好朋友的。"
    pause 0.1 hard
    scene set only xfe_cg memory2
    with dissolve
    play voice "voice/希菲尔/000201880.ogg"
    xfe "形态不同的两种雪花，变成一家人，随之诞生的就是希菲尔。"
    pause 0.1 hard
    scene set only xfe_cg memory1
    with dissolve
    play voice "voice/希菲尔/000201890.ogg"
    xfe "妖精和人类，是可以和平共处的。"
    play voice "voice/希菲尔/000201900.ogg"
    xfe "所以不管凉君改变了多少，都没有关系的。"
    play voice "voice/希菲尔/000201910.ogg"
    xfe "凉君你，是能够和别人成为好朋友的。"
    play voice "voice/希菲尔/000201920.ogg"
    xfe "希菲尔我，也能和凉君成为朋友。"
    play voice "voice/希菲尔/000201930.ogg"
    xfe "在春天降临之前......可以的话，就算春天降临后也一直在一起吧~"
    pause 0.1 hard
    scene set only xfe_cg memory2
    with dissolve
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/000201940.ogg"
    xfe "不管什么季节，希菲尔都会成为凉君的好朋友——"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day205
