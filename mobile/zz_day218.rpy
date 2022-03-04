
label day218:
    bookmark
    $ save_name = _("Day 218")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date217 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only laboratory day outside xuejian
    with slowdissolve
    pause 2.0 hard
    scene set only laboratory inside2 xuejian
    with dissolve
    pause 2.0 hard
    play sound open_door4
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/白羽/711300010.ogg"
    baiyu "哈喽哈喽，圣护院~"
    play music second_122 fadein 3.0 if_changed
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_s1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/圣护院/151300820.ogg"
    shy "辛苦你了，白羽所长。"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711300020.ogg"
    baiyu "真是累死我了，快给我倒杯咖啡~"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151300830.ogg"
    shy "想喝的话请自己去售货机买。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711300030.ogg"
    baiyu "你还是这么冷淡啊......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151300840.ogg"
    shy "比起这个，行星探测计划似乎确实会以失败告终。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711300040.ogg"
    baiyu "最近也是一直问题不断......本以为只是时间问题，可这次的预言算是彻底说明问题了。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151300850.ogg"
    shy "明明还有很多残局需要收拾，真亏你还能过来啊。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300050.ogg"
    baiyu "麻烦的事情交给部下们去做了~比起这个，今后的事情......"
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711300060.ogg"
    baiyu "随着研究队伍的解散，组织决定要为下一次的行星探测项目召集人手。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300070.ogg"
    baiyu "然后呢，你和花山院都被选中了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151300860.ogg"
    shy "......"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300080.ogg"
    baiyu "恭喜，对你而言也算是晋升了。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151300870.ogg"
    shy "......我之所以被选上也不过是沾了花山院的光而已。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300090.ogg"
    baiyu "是因为你的能力出众啦~"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151300880.ogg"
    shy "不管怎么说我就姑且接受了吧。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151300890.ogg"
    shy "那么，我在这里担任主任时期进行的其他计划怎么办？"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300100.ogg"
    baiyu "这些当然我会接手的。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151300900.ogg"
    shy "......所长你不参与行星探测项目吗？"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711300110.ogg"
    baiyu "是啊，毕竟我这边也已经没有闲功夫了。"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711300120.ogg"
    baiyu "命运之日，已经临近了。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151300910.ogg"
    shy "......"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711300130.ogg"
    baiyu "剩下的交给我，你就安心准备奔赴宇宙研究中心吧。"
    play voice "voice/白羽/711300140.ogg"
    baiyu "必要的人手你随便带多少都没关系。"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151300920.ogg"
    shy "......"
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711300150.ogg"
    baiyu "......不满？"
    play voice "voice/圣护院/151300930.ogg"
    shy "不是。"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151300950.ogg"
    shy "今后会由所长接手芬布尔之冬计划。（小声）"
    play voice "voice/圣护院/151300960.ogg"
    shy "为了人类的未来而汇聚{rb}灵继者{/rb}{rt}elfin{/rt}。（小声）"
    play voice "voice/圣护院/151300970.ogg"
    shy "虽然也想理所当然地带走水之濑和千川，但是......（小声）"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/白羽/711300210.ogg"
    baiyu "我的脸上粘了什么东西吗？"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151301040.ogg"
    shy "那倒不是，我只是觉得擅长心理学的所长不参与行星探测真是太可惜了。"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711300220.ogg"
    baiyu "嘛，就当你是在夸奖我好了。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151301100.ogg"
    shy "还有一件事，是关于立花希的。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711300230.ogg"
    baiyu "那孩子似乎对我们的做法相当地反感啊。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151301110.ogg"
    shy "是的，所以还请您选个合适的时间和她见一面。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300240.ogg"
    baiyu "我的话今天就可以哟~"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151301120.ogg"
    shy "那么我就这样传达了。"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711300250.ogg"
    baiyu "要是能够顺利将她拉进组织里来就再好不过了。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151301130.ogg"
    shy "心理诱导一直是所长你的专长吧。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711300260.ogg"
    baiyu "别说得我像欺诈师一样啊......"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711300270.ogg"
    baiyu "而且{rb}灵继者{/rb}{rt}elfin{/rt}本身的心智也有所不同，不能一概而论。"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151301140.ogg"
    shy "的确......从水之濑身上就能看出来。（小声）"
    play voice "voice/圣护院/151301180.ogg"
    shy "站在{rb}灵继者{/rb}{rt}elfin{/rt}立场上的她，一直被组织当作是独特的生命体。（小声）"
    play voice "voice/圣护院/151301200.ogg"
    shy "而我......却对她的身世一无所知。（小声）"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day218.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside1 xuejian
    with dissolve
    pause 1.0 hard
    show baiyu_yjf_b1 b1 b1_s1 onlayer screens at side_left('baiyu'), basicfade
    play voice "voice/白羽/711300290.ogg"
    baiyu "就快到了......"
    hide baiyu_yjf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/白羽/711300300.ogg"
    baiyu "等着我......"
    play voice "voice/白羽/711300310.ogg"
    baiyu "等到这三年的寒冬褪去，等到残酷的季节褪去......"
    $ flcam.move(0, -450, 1000, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711300320.ogg"
    baiyu "紧随其后的——天狗之冬定会来临的。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day218'
    $ seen_day218_school_event01 = False
    $ seen_day218_kindergarden_event01 = False
    $ seen_day218_street_event01 = False

label day218.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day218':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['laboratory'])
    elif _overworld_label == 'day218.school_event01':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day218.kindergarden_event01':
        show set maps winter evening
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    elif _overworld_label == 'day218.street_event01':
        show set maps winter evening
        $ flcam.move(*overworld.camera_positions['road2'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        school=("day218.school_event01", "not seen_day218_school_event01"),
        kindergarden=("day218.kindergarden_event01", "seen_day218_school_event01 and not seen_day218_kindergarden_event01"),
        road2=("day218.street_event01", "seen_day218_kindergarden_event01 and not seen_day218_street_event01"),
        laboratory=("day218.laboratory_event02", "seen_day218_street_event01"))
    $ window_animate_outro()
    if _return == 'day218.school_event01':
        $ flcam.move(*overworld.camera_positions['school'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day218.kindergarden_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day218.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day218.laboratory_event02':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day218.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian3
    with slowdissolve
    pause 2.0 hard
    scene set only school day room xuejian
    with dissolve
    pause 1.0 hard
    play sound phone1
    pause 2.0 hard
    play music second_118 fadein 3.0 if_changed # or second_124
    $ flcam.move(3800, -400, 800, duration=1.5)
    pause 1.0 hard
    investigation call block lhx_dzf_b2 b2 b2_n1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    nvl clear
    c.me01 "哟立花老师，幼儿园的工作还顺利吗？"
    show lhx_dzf_b2 b2 b2_ga1
    play voice "voice/立花希/031308880.ogg"
    c.lhx_dzf_b2 "你还真是乐此不疲啊......"
    c.me01 "感觉你对我好像有什么误会。"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031308890.ogg"
    c.lhx_dzf_b2 "就这么喜欢幼儿园社的活动吗？"
    c.me01 "说实话这一点我也是相当困扰。"
    play voice "voice/立花希/031308910.ogg"
    c.lhx_dzf_b2 "午饭似乎也因此只能吃便当了，真是太好了呢~"
    c.me01 "你是特地打电话来挖苦我的吗......"
    show lhx_dzf_b2 b2 b2_s1
    play voice "voice/立花希/031308960.ogg"
    c.lhx_dzf_b2 "今天希菲尔没有来我这里。"
    c.me01 "是这样啊。"
    show lhx_dzf_b2 b2 b2_n6
    play voice "voice/立花希/031308970.ogg"
    c.lhx_dzf_b2 "想见她吗？"
    c.me01 "当然。"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031309000.ogg"
    c.lhx_dzf_b2 "真是这样的话是不是直接告诉她本人比较好呢？"
    show lhx_dzf_b2 b2 b2_s2
    play voice "voice/立花希/031309010.ogg"
    c.lhx_dzf_b2 "虽然重视家人很有必要。"
    play voice "voice/立花希/031309020.ogg"
    c.lhx_dzf_b2 "但我认为重视家人以外的其他人也对凉君来说同样重要。"
    c.me01 "你在说什么傻话啊。对我来说希菲尔也好立花老师也好，你们也都是我最最重要的家人啊。"
    show lhx_dzf_b2 b2 b2_sp1
    c.lhx_dzf_b2 "......"
    c.me01 "回归正题，刚刚圣护院主任告诉我她的上司白羽小姐想要见我们，说是因为上次爱衣的事情想要给个说法。"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031309040.ogg"
    c.lhx_dzf_b2 "抱歉，今天的事情有点多给忘记了。"
    c.me01 "那等我放学了一起过去吧？到时候时间上应该会比较充裕一些了吧？"
    show lhx_dzf_b2 b2 b2_s2
    play voice "voice/立花希/031309060.ogg"
    c.lhx_dzf_b2 "说不定吧。"
    c.me01 "那就放学后见了。"
    investigation call end
    pause 0.5 hard
    play sound phone2
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day218_school_event01:
        $ seen_day218_school_event01 = True
    $ _overworld_label = 'day218.school_event01'
    jump day218.map

label day218.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school evening outside xuejian
    play music second_108 fadein 3.0 if_changed
    $ flcam.move(0, 300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/爱衣/111300630.ogg"
    aiyi "大哥哥，久等了~"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show qianbo_dzf_b1 b1 b1_a3 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211300300.ogg"
    qb "人家才没有在等你！"
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221300290.ogg"
    ycxt "外面好冷......"
    show qianbo_dzf_b1 b1 b1_sp1
    play voice "voice/千波/211300310.ogg"
    qb "是吗？这种程度不算什么。"
    show aiyi_dzf_b1 b1 b1_ga2
    play voice "voice/爱衣/111300640.ogg"
    aiyi "毕竟千波连感冒都没有得过呢。"
    show qianbo_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211300320.ogg"
    qb "因为人家可是拥有连病菌见了都感到惭愧的美貌嘛。"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221300300.ogg"
    ycxt "奶奶说过，笨蛋是不会感冒的。"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211300330.ogg"
    qb "千波我才不是笨蛋！"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221300310.ogg"
    ycxt "啊......又开始觉得冷了。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111300650.ogg"
    aiyi "那就大家一起活动一下暖和起来吧？"
    show qianbo_dzf_b1 b1 b1_h4
    play voice "voice/千波/211300340.ogg"
    qb "去广场上吧。"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221300320.ogg"
    ycxt "要玩什么好呢？"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111300660.ogg"
    aiyi "大哥哥也一起吗？"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/爱衣/111300670.ogg"
    aiyi "大家一起唧唧我我到身体暖和起来吧~"
    play sound jing02
    with vpunch
    me01 "{size=72}幼儿园社解散第二弹！{/size}"
    show qianbo_dzf_b1 b1 b1_sp1
    show ycxt_dzf_b1 b1 b1_sp1
    show aiyi_dzf_b1 b1 b1_sp1
    "晚饭......还留得住吗。"
    hide qianbo_dzf_b1
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031309100.ogg"
    lhx "萝莉控去死好了......"
    me01 "又来？！"
    pause 0.5 hard
    play sound jiaobu2
    show lhx_dsf_b2 b2 b2_ga1 at walkout_l(0.3)
    pause 0.5 hard
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "......抱歉爱衣，等下你跟翔子先回去吧。"
    play voice "voice/爱衣/111300680.ogg"
    aiyi "那大哥哥呢？"
    me01 "我有点事情要去新城区一趟。"
    me01 "替我转告你翔子姐姐，就说晚饭不用准备我的份了。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day218_kindergarden_event01:
        $ seen_day218_kindergarden_event01 = True
    $ _overworld_label = 'day218.kindergarden_event01'
    jump day218.map

label day218.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street evening road1 xuejian
    with dissolve
    play sound jiaobu3
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "等等我立花老师！"
    play music second_104 fadein 3.0 if_changed
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s1 onlayer m2 at walkin_r(0.3)
    pause 0.5 hard
    play voice "voice/立花希/031309110.ogg"
    lhx "反正凉君你这个萝莉控也不会把我放在眼里的。"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031309120.ogg"
    lhx "毕竟我的身心可都是很成熟的。"
    me01 "你在说什么？"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031309140.ogg"
    lhx "凉君喜欢娇小的女孩子......"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031309150.ogg"
    lhx "说不定正因为内在是小孩子的关系，所以才会更加被宠爱的吧。"
    show lhx_dsf_b2 b2 b2_n3
    play voice "voice/立花希/031309160.ogg"
    lhx "都说性格会写在脸上......太像小孩子的话是不是身高也会被限制呢？"
    me01 "不，这绝对是你想多了。"
    show lhx_dsf_b2 b2 b2_h2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/立花希/031309170.ogg"
    lhx "相对的，成熟的我形象也一直都是高大伟岸的吧。"
    play voice "voice/立花希/031309180.ogg"
    lhx "来年说不定就会拥有超越凉君的身高了。"
    "初诣的时候也说过类似的话，结果到头来连一厘米也没有长。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day218_street_event01:
        $ seen_day218_street_event01 = True
    $ _overworld_label = 'day218.street_event01'
    jump day218.map

label day218.laboratory_event02:
    $ flcam.move(0, 0, 0)
    scene set only laboratory evening outside xuejian
    with slowdissolve
    pause 2.0 hard
    scene set only laboratory inside2 xuejian
    with dissolve
    play music second_122 fadein 3.0 if_changed
    play sound open_door4
    pause 1.0 hard    
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/白羽/711300330.ogg"
    baiyu "我是所长白羽，大家好好相处吧~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031309510.ogg"
    lhx "感觉好微妙......"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300340.ogg"
    baiyu "二位就是立花希小姐和神野凉君对吧？"
    show lhx_dsf_b3 b3 b3_sp1
    play voice "voice/立花希/031309520.ogg"
    lhx "是的，但是为什么感觉你和凉君有点自来熟？"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711300350.ogg"
    baiyu "这是因为听圣护院说了他的事情，现在的组织里他也算是个名人了吧~"
    me01 "名人......"
    "虽然身为千冬的母亲早已经见过面了。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300360.ogg"
    baiyu "啊对了，在进入正题之前有个问题可以确认下吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031309530.ogg"
    lhx "是什么问题？"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711300370.ogg"
    baiyu "二位是刚吵完架吗？"
    lhx "......"
    me01 "......为什么您会知道？"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300380.ogg"
    baiyu "因为二位的表情默契得很有趣啊。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031309540.ogg"
    lhx "为什么光凭这点就能知道？"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300390.ogg"
    baiyu "是匹配心理学哟。"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031309550.ogg"
    lhx "心理学？"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300400.ogg"
    baiyu "是啊，意思就是能够配得上女人美貌的并不仅限于帅哥，比如社会地位什么也很重要的。"
    play voice "voice/白羽/711300410.ogg"
    baiyu "据说如果男女之间的相性默契达到像跷跷板一样看似对立却甩都甩不掉的话，做情侣就能够天长地久了呢。"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031309560.ogg"
    lhx "你的意思是说我的身体魅力和凉君的社会地位很契合吗？"
    play voice "voice/白羽/711300420.ogg"
    baiyu "嗯，因为你是萝莉，而神野君是萝莉控嘛~"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031309570.ogg"
    lhx "你想吵架吗......"
    me01 "萝莉控哪来的社会地位啊！"
    me01 "再说了事实根本不是您说的那样！"
    hide lhx_dsf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711300430.ogg"
    baiyu "是吗？我倒是听说你经常去幼儿园来着。"
    me01 "......那是因为要去接爱衣放学。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711300440.ogg"
    baiyu "你这不是挺受小孩子欢迎的吗？"
    me01 "这个......"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711300450.ogg"
    baiyu "你不也是乐在其中的吗？"
    me01 "雅蠛蝶，别看我~"
    "心理学好可怕......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031309580.ogg"
    lhx "趁这个机会我要确认清楚，凉君是只喜欢身材娇小的女孩子吗？"
    me01 "为什么连你也跟着起哄啊？！"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031309590.ogg"
    lhx "我会成为你的目标吗？"    
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300460.ogg"
    baiyu "绝对是正中红心吧，千川邀请你做老师可能也是看中你的身材娇小这一点吧~"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031309600.ogg"
    lhx "大家都一样没有眼光......"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711300470.ogg"
    baiyu "所以我也拜托你了，能协助我们吗？"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300480.ogg"
    baiyu "当然不只是立花小姐，我希望神野君你也是。"
    show lhx_dsf_b3 b3 b3_n2
    play voice "voice/立花希/031309610.ogg"
    lhx "在此之前请先告诉我们......"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711300490.ogg"
    baiyu "你是想知道{rb}灵纹{/rb}{rt}rune{/rt}的事情吧？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n3 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031309620.ogg"
    lhx "是的，根据具体内容我会决定是否协助你们。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711300500.ogg"
    baiyu "虽然我觉得圣护院主任告诉你们的已经是目前为止组织对外公开的全部信息，不论是{rb}灵继者{/rb}{rt}elfin{/rt}的存在还是{rb}灵纹{/rb}{rt}rune{/rt}的相关事宜目前组织也都还在研究中。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711300510.ogg"
    baiyu "甚至可以说是遇到了前所未有的瓶颈。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300520.ogg"
    baiyu "但是考虑到既然有求于你，就让我用我所擅长的领域来给你讲解吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory baiyu1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031309640.ogg"
    lhx "怎么变得和上课一样了。"
    me01 "超心理学？"
    play voice "voice/白羽/711300530.ogg"
    baiyu "是的，比起普通的心理学我更擅长的是超心理学。"
    play voice "voice/立花希/031309650.ogg"
    lhx "是指研究超自然个体心理习性的学问吧，虽然过去被认为是心理学的一种，但是随着热度逐渐褪去就被遗忘了。"
    play voice "voice/白羽/711300540.ogg"
    baiyu "不过在那之后，也有像我这样的传承者存在。"
    play voice "voice/立花希/031309660.ogg"
    lhx "也就是说那个超自然个体和{rb}灵纹{/rb}{rt}rune{/rt}是存在关联的？"
    play voice "voice/白羽/711300550.ogg"
    baiyu "是啊，因为{rb}灵纹{/rb}{rt}rune{/rt}的学术来源就是从超心理学中剥离出来的。"
    pause 0.1 hard
    scene set only laboratory baiyu2
    with dissolve
    play voice "voice/白羽/711300570.ogg"
    baiyu "超能力是以ESP和PK为基础的。"
    play voice "voice/白羽/711300580.ogg"
    baiyu "ESP是超感——就是指能够察觉到平常看不到的东西的能力。"
    play voice "voice/白羽/711300590.ogg"
    baiyu "PK是念力——也就是能够操纵通常无法移动的物体的能力。"
    play voice "voice/白羽/711300600.ogg"
    baiyu "最具代表性的就是ESP中的{rb}思维透视{/rb}{rt}telepathy{/rt}，和PK中的{rb}念动立场{/rb}{rt}psychokinesis{/rt}。"
    play voice "voice/白羽/711300620.ogg"
    baiyu "然后，除此之外的其他{rb}灵纹{/rb}{rt}rune{/rt}全部都是由二者演化而来的。"
    play voice "voice/立花希/031309670.ogg"
    lhx "是指根据周围环境和目标合理选择灵力具现化的强度和精度的能力对吧？"
    pause 0.1 hard
    scene set only laboratory baiyu1
    with dissolve
    play voice "voice/白羽/711300650.ogg"
    baiyu "果然很优秀呢~"
    play voice "voice/立花希/031309680.ogg"
    lhx "这种东西也只能算杂学而已。"
    play voice "voice/白羽/711300660.ogg"
    baiyu "那么接下来我就说明一下这些超能力是怎么样产生的吧。"
    pause 0.1 hard
    scene set only laboratory baiyu2
    with dissolve
    play voice "voice/白羽/711300670.ogg"
    baiyu "在超心理学上，人的思维是被看成电信号的一种能量脉冲波。"
    play voice "voice/白羽/711300680.ogg"
    baiyu "这种流形态的波在学术上被称为念波。"
    play voice "voice/白羽/711300700.ogg"
    baiyu "这是任何人都会发出的电磁波。"
    play voice "voice/白羽/711300710.ogg"
    baiyu "而{rb}灵继者{/rb}{rt}elfin{/rt}散发出的电磁波比起一般人而言更为强大。"
    play voice "voice/白羽/711300720.ogg"
    baiyu "与此同时念波的波长和频率因人而异。"
    play voice "voice/白羽/711300730.ogg"
    baiyu "所以就会衍生出擅长{rb}思维透视{/rb}{rt}telepathy{/rt}或者是{rb}念动立场{/rb}{rt}psychokinesis{/rt}的不同情况。"
    play voice "voice/立花希/031309700.ogg"
    lhx "也就是说过大的念波输出就会暴走？"
    play voice "voice/白羽/711300750.ogg"
    baiyu "完全正确！"
    pause 0.1 hard
    scene set only laboratory baiyu3
    with dissolve
    me01 "......"
    play voice "voice/立花希/031309710.ogg"
    lhx "凉君开始犯困了......"
    play voice "voice/白羽/711300760.ogg"
    baiyu "嘛，对没有兴趣的人来说这是相当无聊的话题吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only laboratory inside2 xuejian
    play music second_124 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031309720.ogg"
    lhx "很可惜，我对此其实也没多大兴趣。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show baiyu_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/白羽/711300770.ogg"
    baiyu "这些内容不是你想知道的吗？"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031309730.ogg"
    lhx "是的，我想知道的是为什么只有少数人能够觉醒{rb}灵纹{/rb}{rt}rune{/rt}。"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711300780.ogg"
    baiyu "你认为这点和超心理学相悖了？"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031309740.ogg"
    lhx "我是这么认为的......"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711300790.ogg"
    baiyu "那样的话，就是你看走眼了呢。"
    show lhx_dsf_b3 b3 b3_sp2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031309750.ogg"
    lhx "......"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711300800.ogg"
    baiyu "超心理学是研究心理作用能否影响客观事实的学问。"
    play voice "voice/白羽/711300840.ogg"
    baiyu "因为现实不单是靠经典物理学运作的。"
    me01 "也就是说超心理学中认为人的内心想法能够改变真实世界客观事实的案例是存在的吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031309760.ogg"
    lhx "对此你们得出了什么结论？"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300850.ogg"
    baiyu "想要知道更多的话，就接受邀请来协助我们吧~"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031309770.ogg"
    lhx "......"
    hide lhx_dsf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "白羽小姐，能再问你一个问题吗？"
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711300860.ogg"
    baiyu "啊啦，你还醒着啊~"
    me01 "现在雪见市的异常气候，星天宫打算怎么处理？"
    me01 "换句话说，那些暴走的{rb}灵继者{/rb}{rt}elfin{/rt}们会被如何处置呢？"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711300870.ogg"
    baiyu "......"
    show baiyu_yjf_b1 b1 b1_ga1
    play voice "voice/白羽/711300880.ogg"
    baiyu "哼~"
    me01 "......您那是什么眼神啊，难道是会有什么不好的结果吗？"
    play voice "voice/白羽/711300890.ogg"
    baiyu "你们还真是优秀啊，不愧是圣护院看上的人。"
    me01 "什么意思？"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300900.ogg"
    baiyu "他们都是被天使选中的人。"
    play voice "voice/白羽/711300910.ogg"
    baiyu "也就是说，能够获得作为人类的勇士被星天宫征召的资格。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031309820.ogg"
    lhx "......说了那么多，结果还是劝诱啊。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711300920.ogg"
    baiyu "如果你们接受的话，将会和花山院一起离开雪见市。"
    play voice "voice/白羽/711300930.ogg"
    baiyu "然后在某个地方接受特殊训练。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711300940.ogg"
    baiyu "虽然本来是花山院的任务，但我觉得立花小姐也同样能够胜任。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711300950.ogg"
    baiyu "比起星天宫所属的大多数{rb}灵继者{/rb}{rt}elfin{/rt}而言你都要更适合。"
    play voice "voice/立花希/031309830.ogg"
    lhx "反正就是因为我身材娇小吧，这话已经听腻了。"
    me01 "那个......您说的训练是指？"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711300990.ogg"
    baiyu "你们现在还是无关人员吧，如果不加入星天宫的话我就不能详细说明的。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031309840.ogg"
    lhx "简而言之就是劝诱的手段吧。"
    show baiyu_yjf_b1 b1 b1_sp1
    play voice "voice/白羽/711300900.ogg"
    baiyu "刚刚不就说这是被天使选中的吗？"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031309850.ogg"
    lhx "至于答复改日再决定吧。"
    show baiyu_yjf_b1 b1 b1_h1
    play voice "voice/白羽/711301000.ogg"
    baiyu "期待能给出好的答案~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day218.laboratory_event03:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside3 xuejian
    play music second_122 fadein 3.0 if_changed
    $ flcam.move(0, -200, 600, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.3
    show shy_yjf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    show szl_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/圣护院/151401180.ogg"
    shy "总部那边好像已经正式决定终止这次计划，向下一个行星探测目标转移。"
    show szl_dsf_b1 b1 b1_s3
    play voice "voice/水之濑/051400170.ogg"
    szl "下一个是？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151401190.ogg"
    shy "这将会是一次全新的行星探测计划。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141400240.ogg"
    qcls "......还要继续吗？"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151401200.ogg"
    shy "虽然预言说这次的计划会失败，但总不可能因此就放弃了。毕竟上头还有巨额的投资在那里。"
    hide qcls_zf_b1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400180.ogg"
    szl "所以下一次就非成功不可吗？"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151401210.ogg"
    shy "是的。"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051400190.ogg"
    szl "不过就算是星天宫的新项目，也和我没有多大关系就是了。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151401220.ogg"
    shy "也不能说是毫无关系，毕竟这个计划维系着全人类的未来。"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400200.ogg"
    szl "虽然牵涉到宇宙开发，组织多少会用这种夸大其词的言论，但实际上对我们的生活不是毫无影响的吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401230.ogg"
    shy "并非是毫无影响，尤其是对你们{rb}灵继者{/rb}{rt}elfin{/rt}而言。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400210.ogg"
    szl "......"
    $ flcam.move(0, -200, 600, duration=1.5)
    show qcls_zf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141400250.ogg"
    qcls "星天宫进行的行星探测计划，对我们{rb}灵继者{/rb}{rt}elfin{/rt}有什么特殊的意义吗？"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151401240.ogg"
    shy "是啊，无论是计划的过程还是结果都指示着你们的未来，我是这么认为的。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400220.ogg"
    szl "......那么模棱两可的措辞，又是因为是机密的缘故吗？"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151401250.ogg"
    shy "至少现在是的。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151401260.ogg"
    shy "但是下一次的行星探测计划正式启动的话，你们自然能够了解到其中的详情了吧。"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151401270.ogg"
    shy "不、不只是下一个，对于今后的宇宙开发而言，{rb}灵继者{/rb}{rt}elfin{/rt}的协助更是不可或缺的。"
    play voice "voice/圣护院/151401280.ogg"
    shy "所以在新的计划中才会首选花山院。"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141400260.ogg"
    qcls "花山院同学她......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151401290.ogg"
    shy "比约定的时间还要早，不过已经不能再有更多的犹豫了，为此星天宫总部那边也已经采取强制措施了。"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400230.ogg"
    szl "......原来是这么一回事。"
    hide qcls_zf_b1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151401300.ogg"
    shy "水之濑，虽说你对星天宫本身没兴趣，但是组织的那些伎俩你也早就识破了不是吗？"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400300.ogg"
    szl "......别奉承我，就全当是被我碰巧说中了吧。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151401310.ogg"
    shy "是的，不过有一点你错了。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401320.ogg"
    shy "针对把{rb}灵继者{/rb}{rt}elfin{/rt}变回人类的研究也并不是没有。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show qcls_zf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141400280.ogg"
    qcls "......过去有谁在进行这类研究吗？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151401340.ogg"
    shy "是的，听说主要是由神野教授负责的。"
    hide qcls_zf_b1
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401350.ogg"
    shy "{rb}黄昏症候群{/rb}{rt}twilight syndrome{/rt}——这是他提出的假设。"
    play voice "voice/圣护院/151401370.ogg"
    shy "具体的理论我也不清楚，但是听到的结论是{rb}灵纹{/rb}{rt}rune{/rt}是人类进化而诞生的产物。"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_a2 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400310.ogg"
    szl "等等，你是说{rb}灵继者{/rb}{rt}elfin{/rt}的诞生只是纯粹的偶然吗？"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151401380.ogg"
    shy "现阶段只能这么认为，你可以把这个当成是研究员们全体的意见。"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051400320.ogg"
    szl "......"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151401410.ogg"
    shy "一脸无法接受的表情啊。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show qcls_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141400290.ogg"
    qcls "我也不能接受......这不是能用一个“偶然”就打发的事情。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141400300.ogg"
    qcls "毕竟我们{rb}灵继者{/rb}{rt}elfin{/rt}或多或少，都曾因为{rb}灵纹{/rb}{rt}rune{/rt}的关系而受伤过。"
    play voice "voice/千川老师/141400310.ogg"
    qcls "与我们的意愿无关，只能选择接受命运并继续生活下去......"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151401420.ogg"
    shy "我从来不觉得{rb}灵纹{/rb}{rt}rune{/rt}的诞生是没有意义的，相反我认为这是被选择的光荣证明。"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/051400330.ogg"
    szl "会这么想也只是因为主任你不是当事人而已......"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151401430.ogg"
    shy "我不会因为自己是旁观者就把问题想得太简单，{rb}灵继者{/rb}{rt}elfin{/rt}这样的存在到底意味着什么，这些事情我是无论如何都要会去追查清楚的。"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151401440.ogg"
    shy "正因如此，我才接受了星天宫的这个计划。"
    play voice "voice/圣护院/151401450.ogg"
    shy "也因为友加的关系，我变得比以前更加渴望真相了。"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400340.ogg"
    szl "看不出来你还会担心妹妹啊......"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401460.ogg"
    shy "算是吧。"
    show qcls_zf_b1 b1 b1_h3
    play voice "voice/千川老师/141400320.ogg"
    qcls "一旦发生与自己重要之人扯上关系的事情，本来看不透的内心也变得明朗了起来。"
    show szl_dsf_b3 b3 b3_n3
    play voice "voice/水之濑/051400350.ogg"
    szl "不管怎么说主任就是根木头，可能研究者都是这样的人吧。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151401480.ogg"
    shy "我的事怎么样都好，差不多也该进入正题了。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151401490.ogg"
    shy "花山院那边我已经告知她了，为了开展新的计划我们将会离开雪见市。"
    play voice "voice/圣护院/151401500.ogg"
    shy "回到本部的宇宙研究中心去。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151401510.ogg"
    shy "我离开以后这个研究所的其他事宜将由所长接手。"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151401520.ogg"
    shy "由白羽教授她本人亲自指挥。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show qcls_zf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    show szl_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151401530.ogg"
    shy "所以我希望你们也能为自己今后的前程考虑考虑。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400370.ogg"
    szl "......"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141400330.ogg"
    qcls "......"
    show shy_yjf_b1 b1 b1_n3
    play voice "voice/圣护院/151401540.ogg"
    shy "新项目是以{rb}灵继者{/rb}{rt}elfin{/rt}为首的次世代行星探测。"
    show shy_yjf_b1 b1 b1_s2
    play voice "voice/圣护院/151401550.ogg"
    shy "为此除了需要花山院的帮助，你们自然也不例外。"
    show shy_yjf_b1 b1 b1_h3
    play voice "voice/圣护院/151401560.ogg"
    shy "水之濑、千川......要和我一起来吗？"
    play voice "voice/圣护院/151401570.ogg"
    shy "虽然雪见市的计划半途而废了，但是这一次将会关系到未来。"
    show shy_yjf_b1 b1 b1_ga2
    play voice "voice/圣护院/151401580.ogg"
    shy "在这样的计划中也能有你们一起的话，对我来说也是一件非常欣慰的事情。"
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_n3 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051400380.ogg"
    szl "到头来......还是舍不得我们这些棋子。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151401590.ogg"
    shy "你要这么认为我也是没有办法的。"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141400340.ogg"
    qcls "主任并非是想利用我们，交往至今我很清楚这一点。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/141400350.ogg"
    qcls "但是，我暂时还不能离开这座城市。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141400370.ogg"
    qcls "因为这里还有幼儿园的孩子们。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151401600.ogg"
    shy "......是这样吗。"
    play voice "voice/圣护院/151401610.ogg"
    shy "那水之濑你呢？"
    show szl_dsf_b3 b3 b3_s2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/水之濑/051400390.ogg"
    szl "......让我再考虑考虑。"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151401620.ogg"
    shy "我知道了，那么有答案了就告诉我吧。"
    show shy_yjf_b1 b1 b1_h2
    play voice "voice/圣护院/151401630.ogg"
    shy "不只是你们，毕竟这无论对谁而言都是难以抉择的事情。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 1.0 hard
    
    $ persistent.lingyin = True
    $ persistent.szl_ling = True
    $ persistent.youjia = True
    $ persistent.lihuaxi = True
    $ persistent.liuli = True
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    
    jump second_menu
