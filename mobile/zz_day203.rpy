label day203:
    bookmark
    $ save_name = _("Day 203")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    pause 2.0 hard
    show backend_date202 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black 
    with dissolve
    $ suppress_overlay = False
    pause 2.0 hard
    play voice "voice/爱衣/110100680.ogg"
    stranger "大哥哥......起来了吗？"
    play voice "voice/爱衣/110100690.ogg"
    stranger "还在睡吗......早上了哟，到该起床的时间了哟。"
    play voice "voice/爱衣/110100700.ogg"
    stranger "大哥哥，大哥哥~"
    play voice "voice/爱衣/110100710.ogg"
    stranger "怎么还不起来呢......明明马上就要吃早饭了。"
    play voice "voice/爱衣/110100720.ogg"
    stranger "这个时候该怎么做呢？"
    play voice "voice/爱衣/110100770.ogg"
    stranger "嘿！！！"
    play sound touch
    scene white 
    with slowdissolve
    me01 "噗！" with vpunch
    "肚子上突然感觉到了一阵冲击。"
    pause 1.0 hard
    scene set only home day my_room xuejian
    play music second_114 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, 300, 1000, duration=1.5)
    pause 0.5 hard
    show aiyi_sy_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110100780.ogg"
    aiyi "啊，起来了。"
    "视线里最先映出的是爱衣可爱的脸庞。"
    "然后我才意识到此刻她已经坐到了我的身上。"
    $ flcam.move(-4500, 300, 900, duration=1.5)
    show aiyi_sy_b1 b1 b1_h1
    play voice "voice/爱衣/110100790.ogg"
    aiyi "早上好，大哥哥~"
    me01 "早上好。"
    me01 "是翔子让你来叫我起床的吗？"
    show aiyi_sy_b1 b1 b1_n1
    play voice "voice/爱衣/110100800.ogg"
    aiyi "是啊，赖床可不行。"
    me01 "抱歉。"
    "也许是因为天气太冷的缘故，我和被子之间仿佛有着一股强烈的吸引力。"
    "可即便如此面对爱衣的“叫醒方式”我还是不得不妥协了。"
    show aiyi_sy_b1 b1 b1_sp1
    play voice "voice/爱衣/110100810.ogg"
    aiyi "大哥哥，去洗脸吗？"
    me01 "是啊，爱衣已经洗好了吗？"
    show aiyi_sy_b1 b1 b1_n1
    play voice "voice/爱衣/110100820.ogg"
    aiyi "没有，爱衣也刚刚起来。"
    "起床的第一件事就是来我的房间吗。"
    "真亏翔子能让她来叫我，说明之前的事情已经不生气了吧......"
    show aiyi_sy_b1 b1 b1_h1
    play voice "voice/爱衣/110100830.ogg"
    aiyi "再等一下就可以吃早饭了。"
    me01 "那得赶紧起来准备才行。"
    show aiyi_sy_b1 b1 b1_n1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/爱衣/110100840.ogg"
    aiyi "嗯。"
    me01 "这个房间没有暖气所以很冷吧？"
    show aiyi_sy_b1 b1 b1_s2
    play voice "voice/爱衣/110100850.ogg"
    aiyi "嗯......"
    me01 "那我们就赶紧到暖和一点的地方去吧。"
    show aiyi_sy_b1 b1 b1_sp1
    play voice "voice/爱衣/110100860.ogg"
    aiyi "暖和的地方？"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    play sound touch
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only aiyi_cg two
    with slowdissolve
    pause 1.0 hard
    "本想带着爱衣去大厅的，可没想到她却先一步钻进了我的被窝。"
    me01 "那个......不是要去洗脸吗？"
    play voice "voice/爱衣/110100870.ogg"
    aiyi "欸嘿嘿~"
    me01 "不是特地来叫我起床的吗。"
    play voice "voice/爱衣/110100880.ogg"
    aiyi "稍微再睡一会儿没关系的。"
    "爱衣用手挽住了我的胳膊。"
    "简直就像捧着一个暖宝宝似的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only home day my_room xuejian alpha
    with dissolve
    pause 2.0 hard
    play music second_104 fadein 3.0
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_ga1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010101520.ogg"
    xz "我就想着怎么都没人出来......"
    play voice "voice/翔子/010101530.ogg"
    xz "下流......"
    show xz_dzf_b1 b1 b1_a1
    play voice "voice/翔子/010101540.ogg"
    xz "又把爱衣带到自己的被窝里了。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010101550.ogg"
    xz "果然还是马上赶出去吧。"
    "后果好像很严重啊！" with vpunch
    me01 "听我解释啊翔子......"
    pause 0.5 hard
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_sy_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110100890.ogg"
    aiyi "不是的大姐姐，爱衣昨天是一个人睡的。"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010101560.ogg"
    xz "就算是这样也不能随便跑到神野君的房间里来，你看神野君他也很困扰的。"
    me01 "困扰的话也不至于......"
    hide aiyi_sy_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_a1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010101570.ogg"
    xz "神野君给我闭嘴！"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_n1 onlayer m1:
        xpos 0.5
    show aiyi_sy_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/010101580.ogg"
    xz "不想一个人睡的话，就来和姐姐一起睡吧。"
    show aiyi_sy_b1 b1 b1_h1
    play voice "voice/爱衣/110100900.ogg"
    aiyi "没关系的，爱衣不会再做让大姐姐为难的事了。"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010101590.ogg"
    xz "让我为难什么的......其实也没有。"
    me01 "刚才不是说爱衣来我这里睡的话我会让你很为难吗？"
    hide aiyi_sy_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dzf_b2 with None
    pause 0.1 hard
    show xz_dzf_b1 b1 b1_a1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010101600.ogg"
    xz "闭嘴！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day203'
    $ seen_day203_street_event01 = False
    $ seen_day203_kindergarden_event01 = False

label day203.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day203':
        $ flcam.move(6100, -1800, 2800)
    elif _overworld_label == 'day203.street_event01':
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day203.kindergarden_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    if _overworld_label == 'day203':
        window mode map
        me01 "那么，早饭也吃完了，是时候出发去学校了......" nointeract
    elif _overworld_label == 'day203.street_event01' or _overworld_label == 'day203.kindergarden_event01':
        window mode map
        me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        road1=("day203.street_event01", "not seen_day203_street_event01"),
        kindergarden=("day203.kindergarden_event01", "seen_day203_street_event01 and not seen_day203_kindergarden_event01"),
        school=("day203.school_event01", "seen_day203_street_event01 and seen_day203_kindergarden_event01"))
    $ window_animate_outro()
    if _return == 'day203.school_event01':
        $ flcam.move(*overworld.camera_positions['school'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day203.street_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day203.kindergarden_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day203.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street day road1 xuejian
    with dissolve
    pause 1.0 hard
    play music second_114 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180100520.ogg"
    yczs "我先走了。"
    pause 0.5 hard
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show ycnn_sf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/一诚奶奶/370100010.ogg"
    ycnn "总司，现在去上学吗？"
    play voice "voice/一诚总司/180100530.ogg"
    yczs "是啊。"
    play voice "voice/一诚奶奶/370100020.ogg"
    ycnn "比平常的话要晚一些。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100540.ogg"
    yczs "今天没有社团的晨练，所以迟了点出门。"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100030.ogg"
    ycnn "是在等奶奶我吗？"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100550.ogg"
    yczs "才不是。"
    show ycnn_sf_b1 b1 b1_n1
    play voice "voice/一诚奶奶/370100040.ogg"
    ycnn "那我也和总司一起走吧，一直跟到黄泉之下为止。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100560.ogg"
    yczs "拜托别说这种让人笑不出来的表达方式。"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100050.ogg"
    ycnn "奶奶我还很健康，所以是可以拿得出手的玩笑哦~"
    show yczs_dzf_b1 b1 b1_n1
    play voice "voice/一诚总司/180100570.ogg"
    yczs "毕竟您还加入家庭委员会了嘛。"
    show ycnn_sf_b1 b1 b1_n1
    play voice "voice/一诚奶奶/370100060.ogg"
    ycnn "我打算到总司毕业为止都继续坚持下去的，我会好好把学校建设成你理想中的样子。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100580.ogg"
    yczs "你要把学校怎么样啊。"
    play voice "voice/一诚奶奶/370100070.ogg"
    ycnn "全部都聘用一些巨乳女教师吧~"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/180100590.ogg"
    yczs "我才没有那种兴趣！"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100080.ogg"
    ycnn "哎呀呀，害羞了。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100600.ogg"
    yczs "说起来奶奶您根本就没有那种权利吧。"
    show ycnn_sf_b1 b1 b1_s1
    play voice "voice/一诚奶奶/370100090.ogg"
    ycnn "被小看了我可是很困扰的，大家可是都说家庭委员会是由我一手撑起来的。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100610.ogg"
    yczs "我想人家是希望您快点隐退吧。"
    show ycnn_sf_b1 b1 b1_n1
    play voice "voice/一诚奶奶/370100100.ogg"
    ycnn "周围有人抱怨的时候，我都会装作耳朵不好搪塞过去所以没关系。"
    play voice "voice/一诚总司/180100620.ogg"
    yczs "行了啦，我去学校了。"
    stop music fadeout 5.0
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100110.ogg"
    ycnn "等一下，正好我们现在也要去幼儿园。"
    hide ycnn_sf_b1
    hide yczs_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_n2 onlayer m1:
        xpos 0.7
    play music second_102 fadein 3.0 if_changed
    ycxt "......"
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show ycnn_sf_b1 b1 b1_n1 onlayer m2:
        xpos 0.6
    show yczs_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180100630.ogg"
    yczs "小桃一直藏在奶奶的身后吗，我都没发现......"
    play voice "voice/一诚奶奶/370100120.ogg"
    ycnn "呐小桃，你应该也有话想对哥哥说吧？"
    show ycxt_dzf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/小桃/220100460.ogg"
    ycxt "嗯、嗯......"
    pause 0.5 hard
    show ycnn_sf_b1 b1 b1_n1 at walkout_l(0.6)
    pause 0.5 hard
    hide ycnn_sf_b1
    show ycxt_dzf_b1 b1 b1_n1:
        xpos 0.7
        linear 1.0 xpos 0.6
    $ flcam.move(-1200, 0, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/小桃/220100470.ogg"
    ycxt "哥、哥哥......"
    show ycxt_dzf_b1 b1 b1_s3
    play voice "voice/小桃/220100480.ogg"
    ycxt "请、请和小桃一起......"
    play voice "voice/小桃/220100490.ogg"
    ycxt "去、去幼儿园......"
    hide yczs_dzf_b1
    $ flcam.move(2500, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s4 at flu_down(0.15, 20):
        xpos 0.6
    play voice "voice/小桃/220100500.ogg"
    ycxt "......"
    play sound hide_sound
    show ycxt_dzf_b1 b1 b1_s4:
        xpos 0.6
        linear 0.5 xpos 0.7
    show ycnn_sf_b1 b1 b1_n1 onlayer m2:
        xpos 0.6
    show yczs_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/180100640.ogg"
    yczs "......"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100650.ogg"
    yczs "那我先去学校了。"
    play voice "voice/一诚奶奶/370100130.ogg"
    ycnn "不和奶奶我们一起走吗？"
    play voice "voice/一诚总司/180100660.ogg"
    yczs "算了吧，小桃看起来很怕我的样子。"
    show ycxt_dzf_b1 b1 b1_s2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/220100510.ogg"
    ycxt "......"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100140.ogg"
    ycnn "小桃只是害羞而已，你也明白的吧。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100670.ogg"
    yczs "都是一家人，有什么好害羞的。"
    $ flcam.move(0, 0, 750, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s4
    play voice "voice/小桃/220100520.ogg"
    ycxt "哥、哥哥......"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100680.ogg"
    yczs "怎么了？"
    show ycxt_dzf_b1 b1 b1_s3
    play voice "voice/小桃/220100530.ogg"
    ycxt "一、一起去幼儿园不行吗......"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/220100540.ogg"
    ycxt "圣诞节也是。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100690.ogg"
    yczs "还有这样的节日来着，到时候我要去朋友家过。"
    show ycxt_dzf_b1 b1 b1_s4
    play voice "voice/小桃/220100550.ogg"
    ycxt "那新年呢......"
    play voice "voice/一诚总司/180100700.ogg"
    yczs "还有寒假作业必须要完成。"
    play voice "voice/小桃/220100560.ogg"
    ycxt "初诣呢......"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100710.ogg"
    yczs "太麻烦了，还是在家里呆着吧。"
    show ycxt_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/小桃/220100570.ogg"
    ycxt "呜......"
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show ycnn_sf_b1 b1 b1_s1
    play voice "voice/一诚奶奶/370100150.ogg"
    ycnn "总司！"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100720.ogg"
    yczs "又怎么了。"
    play voice "voice/一诚奶奶/370100160.ogg"
    ycnn "就因为你总是这么对她，小桃才不敢接近你的吧。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100730.ogg"
    yczs "总之，就是讨厌我的意思吧。"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/220100580.ogg"
    ycxt "啊，不是的......"
    $ flcam.move(0, 0, 750, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100740.ogg"
    yczs "那是什么意思？"
    show ycxt_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/小桃/220100590.ogg"
    ycxt "......"
    play sound hide_sound
    show ycxt_dzf_b1 b1 b1_c1 at walkout_r(0.7)
    pause 0.5 hard
    hide ycxt_dzf_b1
    pause 1.0 hard
    hide ycnn_sf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100750.ogg"
    yczs "哎......"
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_c1 onlayer m1:
        xpos 0.7
    show ycnn_sf_b1 b1 b1_n1 onlayer m2:
        xpos 0.6
    play voice "voice/一诚奶奶/370100170.ogg"
    ycnn "看吧，小桃她也说了并不讨厌总司。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100760.ogg"
    yczs "您是怎么看出来的啊......"
    play voice "voice/一诚奶奶/370100180.ogg"
    ycnn "无论是圣诞节还是初诣，都想和你在一起哦~"
    play voice "voice/一诚总司/180100770.ogg"
    yczs "和我这种人在一起过有什么开心的。"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100190.ogg"
    ycnn "因为这就是家人。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100780.ogg"
    yczs "不管怎么样，再这样陪小桃耗下去的话就要迟到了。"
    show ycxt_dzf_b1 b1 b1_s4 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/220100600.ogg"
    ycxt "对、对不起......"
    show ycnn_sf_b1 b1 b1_s1
    play voice "voice/一诚奶奶/370100200.ogg"
    ycnn "喂，总司！"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100790.ogg"
    yczs "是是，是我错了，我差不多要去学校了。"
    show ycnn_sf_b1 b1 b1_n1
    play voice "voice/一诚奶奶/370100210.ogg"
    ycnn "是吗是吗，总司比起小桃更喜欢学校里的女孩子。"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/180100800.ogg"
    yczs "才不是这样的！"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100220.ogg"
    ycnn "因为总司和奶奶我一样，喜欢巨乳呢~"
    show yczs_dzf_b1 b1 b1_sp2
    play voice "voice/一诚总司/180100810.ogg"
    yczs "不觉得很奇怪吗这个！"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/220100610.ogg"
    ycxt "哥哥你喜欢巨乳？"
    show ycnn_sf_b1 b1 b1_n1
    play voice "voice/一诚奶奶/370100230.ogg"
    ycnn "要好好记住哦~"
    show yczs_dzf_b1 b1 b1_sp2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/一诚总司/180100820.ogg"
    yczs "让她记住这个要做什么啊！？"
    show ycxt_dzf_b1 b1 b1_n2
    play voice "voice/小桃/220100620.ogg"
    ycxt "等小桃的胸部也变大了，哥哥就会喜欢我了吗？"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100240.ogg"
    ycnn "嗯嗯，一定是这样的。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100830.ogg"
    yczs "奶奶你都对小桃说了些什么啊。"
    show ycnn_sf_b1 b1 b1_s1
    play voice "voice/一诚奶奶/370100250.ogg"
    ycnn "总司你才是，要对小桃温柔一些。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100840.ogg"
    yczs "就算我想这样做......也办不到。"
    show ycnn_sf_b1 b1 b1_sp1
    play voice "voice/一诚奶奶/370100260.ogg"
    ycnn "为什么？"
    play voice "voice/一诚总司/180100850.ogg"
    yczs "怎么样都好吧。"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100270.ogg"
    ycnn "不告诉我的话，我就向家庭委员会的人们揭发你是巨乳控。"
    show yczs_dzf_b1 b1 b1_sp1
    play voice "voice/一诚总司/180100860.ogg"
    yczs "别这样......还有我才不是巨乳控！"
    $ flcam.move(0, 0, 750, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_n2
    play voice "voice/小桃/220100630.ogg"
    ycxt "喜欢飞机场吗？"
    show yczs_dzf_b1 b1 b1_sp2
    play voice "voice/一诚总司/180100870.ogg"
    yczs "才不是！"
    show ycxt_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/小桃/220100640.ogg"
    ycxt "抽泣！"
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show ycnn_sf_b1 b1 b1_s1
    play voice "voice/一诚奶奶/370100280.ogg"
    ycnn "都怪总司你老是大吼大叫，这不是又把她吓哭了吗......真是个坏哥哥。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100880.ogg"
    yczs "奶奶您就继续这样宠着小桃吧。"
    show ycnn_sf_b1 b1 b1_n1
    play voice "voice/一诚奶奶/370100290.ogg"
    ycnn "奶奶我该发火的时候还是会发火，该严厉的时候还是会严厉的。"
    play voice "voice/一诚奶奶/370100300.ogg"
    ycnn "总司，对待你的时候也是一样的。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100890.ogg"
    yczs "......啊啊，是吗。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100900.ogg"
    yczs "所以我才会......变得不擅长和小桃相处吧。"
    show ycnn_sf_b1 b1 b1_sp1
    play voice "voice/一诚奶奶/370100310.ogg"
    ycnn "什么意思？"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100910.ogg"
    yczs "什么都没有，那我走了。"
    pause 0.5 hard
    play sound jiaobu3
    show yczs_dzf_b1 b1 b1_s1 at walkout_l(0.3)
    pause 2.0 hard
    $ flcam.move(3500, 0, 750, duration=1.5)
    pause 0.5 hard
    show ycnn_sf_b1 b1 b1_s1
    play voice "voice/一诚奶奶/370100320.ogg"
    ycnn "啊啊......逃走了。"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/220100650.ogg"
    ycxt "哥哥......"
    show ycxt_dzf_b1 b1 b1_s4
    play voice "voice/小桃/220100660.ogg"
    ycxt "果然是不喜欢......小桃的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day203.street_event01'
    if not seen_day203_street_event01:
        $ seen_day203_street_event01 = True
    jump day203.map

label day203.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    play ambience1 niaoming
    scene set only school day outside xuejian
    with slowdissolve
    pause 1.0 hard
    play music second_118 fadein 3.0 if_changed
    $ flcam.move(2500, -300, 900, duration=1.5)
    pause 0.5 hard
    show ycnn_sf_b1 b1 b1_n1 onlayer m2:
        xpos 0.6
    play voice "voice/一诚奶奶/370100330.ogg"
    ycnn "早上好，老师。"
    $ flcam.move(-800, -150, 750, duration=1.5)
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030102270.ogg"
    lhx "早上好，小桃的奶奶。"
    $ flcam.move(0, 0, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n2 onlayer m1:
        xpos 0.7
    play voice "voice/一诚奶奶/370100340.ogg"
    ycnn "老师，今天这孩子也拜托了~"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030102290.ogg"
    lhx "好的，虽然只是绵薄之力，但还是请您放心交给我吧。"
    play voice "voice/小桃/220100670.ogg"
    ycxt "......"
    play voice "voice/一诚奶奶/370100350.ogg"
    ycnn "小桃别藏了，你的问候呢？"
    show ycxt_dzf_b1 b1 b1_s2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/220100680.ogg"
    ycxt "早、早上好......飞机场老师。"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100360.ogg"
    ycnn "乖、乖，做得不错~"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030102300.ogg"
    lhx "哪里做得不错了，看来我必须在那个绰号深入人心之前彻底击碎它！"
    hide lhx_dzf_b2
    hide ycnn_sf_b1
    hide ycxt_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/210100500.ogg"
    qb "早上好，飞机场~"
    $ flcam.move(-3000, 250, 750, duration=1.5)
    show lhx_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.45
    play voice "voice/立花希/030102310.ogg"
    lhx "终于连“老师”也消失了，你这小屁孩真够胆。"
    $ flcam.move(0, 0, 600, duration=1.5)
    show qianbo_dzf_b1 b1 b1_h4
    show ycnn_sf_b1 b1 b1_n1 onlayer m2:
        xpos 0.6
    show ycxt_dzf_b1 b1 b1_n2 onlayer m1:
        xpos 0.7
    play voice "voice/千波/210100510.ogg"
    qb "小桃，走吧~"
    play voice "voice/小桃/220100690.ogg"
    ycxt "嗯、嗯......"
    pause 0.5 hard
    play sound jiaobu3
    show qianbo_dzf_b1 b1 b1_h4 at walkout_r(0.3)
    show ycxt_dzf_b1 b1 b1_n2 at walkout_r(0.7)
    pause 2.0 hard
    hide qianbo_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(800, -150, 750, duration=1.5)
    pause 0.5 hard
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100370.ogg"
    ycnn "那我也差不多要回去了。"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/030102320.ogg"
    lhx "好的，一直以来接送小桃真是辛苦您了。"
    play voice "voice/一诚奶奶/370100380.ogg"
    ycnn "那孩子的父母工作都很忙，基本都是我在照顾她。"
    show ycnn_sf_b1 b1 b1_s1
    play voice "voice/一诚奶奶/370100410.ogg"
    ycnn "真希望总司能多陪陪她。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.45
    play voice "voice/立花希/030102340.ogg"
    lhx "是这样啊。"
    show ycnn_sf_b1 b1 b1_h1
    play voice "voice/一诚奶奶/370100440.ogg"
    ycnn "那么再见了，飞机场老师~"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.45
    play voice "voice/立花希/030102360.ogg"
    lhx "......请不要再这样称呼我了。感觉这样下去会一发不可收拾的。"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    scene black
    with right2left_02
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(2250, 250, 750, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    show qianbo_dzf_b1 b1 b1_h4 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/220100700.ogg"
    ycxt "千波，今天是你一个人来的吗？"
    show qianbo_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/210100520.ogg"
    qb "是啊，人家已经是大人了嘛，也差不多该从家人的接送中毕业了。"
    play sound yangmu
    show ycxt_dzf_b1 b1 b1_h2 at flu_down(0.15, 20):
        xpos 0.5
    show yangmu onlayer m2:
        xalign 0.49 yalign 0.53 zoom 0.7
    play voice "voice/小桃/220100710.ogg"
    ycxt "千波好帅气~"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 30):
        xpos 0.7
    play voice "voice/千波/210100530.ogg"
    qb "人家才不是因为寂寞才这样做的呢！"
    hide yangmu
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/220100720.ogg"
    ycxt "千、千波你，觉得寂寞了吗？"
    show qianbo_dzf_b1 b1 b1_ga1
    play voice "voice/千波/210100540.ogg"
    qb "妈妈睡过头了，姐姐她在学校那边还有工作。"
    show ycxt_dzf_b1 b1 b1_n2
    play voice "voice/小桃/220100730.ogg"
    ycxt "但、但是，她们会来接你的吧？"
    hide qianbo_dzf_b1 
    show qianbo_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210100550.ogg"
    qb "无所谓了，人家已经是大人了，一个人也能回家的！"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/220100740.ogg"
    ycxt "千波好厉害啊~"
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_h4 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210100560.ogg"
    qb "小桃是你奶奶接送的吧，懂得又多人又温柔，真是一位好奶奶呢。"
    show ycxt_dzf_b1 b1 b1_n2
    play voice "voice/小桃/220100750.ogg"
    ycxt "嗯、嗯......"
    hide qianbo_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s1
    play voice "voice/小桃/220100760.ogg"
    ycxt "但是，哥哥他......"
    play voice "voice/小桃/220100860.ogg"
    ycxt "该怎么样才好呢......"
    show ycxt_dzf_b1 b1 b1_s4
    play voice "voice/小桃/220100870.ogg"
    ycxt "要怎么做......才能搞好关系呢？"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day203.kindergarden_event01'
    if not seen_day203_kindergarden_event01:
        $ seen_day203_kindergarden_event01 = True
    jump day203.map

label day203.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day room xuejian
    with dissolve
    pause 1.0 hard
    play music second_119 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b2 b2 b2_h1 onlayer m1 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/植澄友加/020101180.ogg"
    yj "凉君，午饭时间到了哟~"
    me01 "你看起来好像很高兴的样子。"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020101190.ogg"
    yj "这可是我除了社团活动和体育课以外最喜欢的时间了呀。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010102800.ogg"
    xz "神野君，今天怎么安排呢？"
    me01 "我打算去中庭。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show yczs_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180100970.ogg"
    yczs "......中庭？去那做什么？"
    me01 "吃饭。"
    hide yj_dzf_b3 with None
    pause 0.1 hard
    show yj_dzf_b2 b2 b2_sp1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020101200.ogg"
    yj "在便利店买面包？"
    me01 "是啊。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/180100980.ogg"
    yczs "真是奇怪的家伙啊......那里很冷不适合吃饭的。"
    me01 "嘛，总会慢慢习惯的。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/180100990.ogg"
    yczs "是吗，你还真是精力充沛啊......"
    hide xz_dzf_b2
    hide yczs_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020101210.ogg"
    yj "凉君，难道是因为在顾虑我们吗？"
    me01 "为什么这么说？"
    show yj_dzf_b1 b1 b1_s2
    play voice "voice/植澄友加/020101220.ogg"
    yj "不和我们一起吃，是不是我们做了什么对不起凉君的事情。"
    me01 "绝对没有这回事，去中庭完全是我自己的原因。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010102820.ogg"
    xz "神野君，真的要去中庭吃午饭吗？"
    me01 "是啊。"
    "昨天那个女孩子，如果还能见到的话就太好了。"
    stop music fadeout 5.0
    pause 1.0 hard
    play sound open_door5
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day203.school_event02:
    $ flcam.move(0, 0, 0)
    scene set only school day center room xuejian
    with slowdissolve
    pause 1.0 hard
    play music second_115 fadein 3.0 if_changed
    "虽然在便利店买东西的时候也需要排队，但并没有食堂那么拥挤。"
    "随便买了个面包，我就径直向中庭走去。"
    "可即使是这样那里也有人捷足先登了。"
    pause 1.0 hard
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "坐在长椅上的女同学。"
    "手里拿着灌装果汁。"
    "是昨天遇到的那位女孩。"
    "为什么她也要特地来这里吃午饭呢？"
    "孤零零的身影看起来很孤单。"
    "虽然我也没有资格说别人，但是对方怎么看也不像是会被孤立的人。"
    "就在我四下寻找其他座位的同时，女孩与我的视线重合了。"
    pause 1.0 hard
    scene set only school day center room xuejian alpha
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100030.ogg"
    stranger "啊......"
    show liuli_dzf_b1 b1 b1_n1 at flu_down(0.15, 20):
        xpos 0.5
    "和上次一样，女孩向我鞠了个躬。"
    hide liuli_dzf_b1
    show liuli_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100040.ogg"
    stranger "那个，你现在要在这里吃饭吗？"
    "也许是注意到了我手中的面包，她如是问道。"
    show liuli_dzf_b3 b3 b3_n1
    play voice "voice/琉璃/040100050.ogg"
    stranger "我马上就吃完了，不介意的话请坐在这里吧。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b3 b3 b3_n1 at flu_down(0.15, 20):
        xpos 0.5
    me01 "不用特地让给我，不介意的话一起吃吧？"
    show liuli_dzf_b3 b3 b3_s2
    play voice "voice/琉璃/040100060.ogg"
    stranger "我不会妨碍到你吗？"
    me01 "完全不会。"
    hide liuli_dzf_b3
    show liuli_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100070.ogg"
    stranger "谢谢你~"
    me01 "那就这么定了。"
    show liuli_dzf_b2 b2 b2_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/琉璃/040100080.ogg"
    stranger "好、好的，再次谢谢你。"
    "我走到长椅的另一端坐了下来。"
    hide liuli_dzf_b2
    show liuli_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100090.ogg"
    stranger "那个，要坐在我旁边吗？"
    me01 "可以吗？"
    "总觉得很难拒绝她的好意，于是我靠了上去。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 2.0 hard
    scene set only liuli_cg center normal
    with dissolve
    pause 0.5 hard
    play voice "voice/琉璃/040100100.ogg"
    stranger "啊，对不起。"
    me01 "为什么要道歉？"
    play voice "voice/琉璃/040100110.ogg"
    stranger "还没告诉你我的名字呢。"
    pause 0.1 hard
    scene set only liuli_cg center happy
    with dissolve
    play voice "voice/琉璃/040100120.ogg"
    stranger "我叫花山院琉璃，是一年级的学生。"
    me01 "我是二年级的神野凉，请多指教。"
    pause 0.1 hard
    scene set only liuli_cg center normal
    with dissolve
    play voice "voice/琉璃/040100130.ogg"
    liuli "是我的前辈呢~"
    me01 "虽然是这样，但我也是昨天才转学过来的。"
    pause 0.1 hard
    scene set only liuli_cg center sp
    with dissolve
    play voice "voice/琉璃/040100140.ogg"
    liuli "啊，难怪之前都没见你来过这里。"
    pause 0.1 hard
    scene set only liuli_cg center sad
    with dissolve
    me01 "花山院同学经常会来这里吃午饭吗？"
    play voice "voice/琉璃/040100390.ogg"
    liuli "这个嘛......因为我不太擅长与人打交道，所以经常无法顺利融入群体。"
    play voice "voice/琉璃/040100400.ogg"
    liuli "就算勉强能和同学说上话，可到最后也会因为话题变得生硬而搞砸......"
    "某种程度上和以前的我有些相似。"
    pause 0.1 hard
    scene set only liuli_cg center normal
    with dissolve
    play voice "voice/琉璃/040100420.ogg"
    liuli "我想那一定是因为我的努力还不够的关系。"
    play voice "voice/琉璃/040100430.ogg"
    liuli "总有一天我也希望能真正成为大家的伙伴。"
    me01 "我倒是觉得琉璃你现在的交流方式已经完全没有问题了。"
    "为了增加亲切感，我故意用名字称呼了对方。"
    pause 0.1 hard
    scene set only liuli_cg center shy
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/040100530.ogg"
    liuli "是、是这样吗？"
    play voice "voice/琉璃/040100540.ogg"
    liuli "还是第一次被别人这样说。"
    "这么可爱的女生要是被大家忽视了那该多可惜啊。"
    me01 "其实只要勇敢一些，主动去和大家交朋友的话，琉璃你也一定会很受欢迎的。"
    pause 0.1 hard
    scene set only liuli_cg center sp
    with dissolve
    play voice "voice/琉璃/040100780.ogg"
    liuli "......"
    pause 0.1 hard
    scene set only liuli_cg center normal
    with dissolve
    play voice "voice/琉璃/040100660.ogg"
    liuli "非常感谢，前辈果然是个温柔的人呢~"
    me01 "对了琉璃......"
    stop music fadeout 5.0
    me01 "如果你不介意的话，明天也和我一起在这里吃午饭吧？"
    pause 0.1 hard
    scene set only liuli_cg center sp
    with dissolve
    play voice "voice/琉璃/040100790.ogg"
    liuli "前、前辈？"
    me01 "可以吗？"
    play music second_107 fadein 3.0 if_changed
    pause 0.1 hard
    scene set only liuli_cg center happy
    with dissolve
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/琉璃/040100800.ogg"
    liuli "好、好的，请多指教~"
    pause 0.1 hard
    scene set only liuli_cg center sp
    with dissolve
    play voice "voice/琉璃/040100810.ogg"
    liuli "但、但是，在这里吃的话前辈不会冷吗？"
    me01 "毕竟我以前也在这座城市生活过。"
    me01 "那个时候的积雪比现在还要高。"
    me01 "这种程度的寒冷对我来说就是小事一桩。"
    me01 "所以比起我琉璃你才需要多注意别着凉了才是。"
    pause 0.1 hard
    scene set only liuli_cg center happy
    with dissolve
    play voice "voice/琉璃/040100850.ogg"
    liuli "非、非常感谢！"
    "能结识这样一个乖巧的后辈真是幸运啊。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 2.0 hard

label day203.school_event03:
    play sound rill
    $ flcam.move(0, 0, 0)
    scene set only school day room xuejian
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_h1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/120100330.ogg"
    rxl "终于到放学的时间了~"
    play music second_118 fadein 3.0 if_changed
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show szl_dzf_b1 b1 b1_n2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/水之濑/050100160.ogg"
    stranger "你好像很高兴啊。"
    show rxl_dzf_b2 b2 b2_s1
    play voice "voice/日向怜/120100340.ogg"
    rxl "因为上课很无聊嘛~"
    hide szl_dzf_b1
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100180.ogg"
    stranger "也就是说你是讨厌学习本身吧。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/120100360.ogg"
    rxl "是哟，我喜欢的也就只有体育了吧。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100190.ogg"
    stranger "喜欢活动身体吗？"
    show rxl_dzf_b1 b1 b1_h1
    play voice "voice/日向怜/120100370.ogg"
    rxl "不是，我喜欢的是保健体育~"
    show szl_dzf_b3 b3 b3_s1
    play voice "voice/水之濑/050100200.ogg"
    stranger "......就在刚刚我对你的看法产生了180度的转变。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/120100380.ogg"
    rxl "那么，放学后该干嘛呢？"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100210.ogg"
    stranger "虽然知道你很想出去玩，但在那之前要先完成学生会的工作才行。那个......昨天刚加入学生会的日向怜同学。"
    hide rxl_dzf_b2 
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/120100410.ogg"
    rxl "这样啊，我以为昨天在学生会介绍完就结束了，现在终于要迎来第一份工作了吗。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100260.ogg"
    stranger "第一份工作就是让你好好认清自己的身份，跟我来吧。"
    play sound jiaobu2
    show szl_dzf_b3 b3 b3_s1 at walkout_l(0.3)
    pause 2.0 hard
    hide szl_dzf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show rxl_dzf_b1 b1 b1_sp2 at flu_up(0.15, 30):
        xpos 0.5
    play voice "voice/日向怜/120100440.ogg"
    rxl "等、等等我，真是冷淡啊。"
    pause 1.0 hard
    scene black 
    with right2left_02
    play sound open_door5
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day corridor xuejian
    with right2left_02
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_a1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/水之濑/050100270.ogg"
    stranger "好慢。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show rxl_dzf_b2 b2 b2_h1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/120100510.ogg"
    rxl "对不起啦~"
    show szl_dzf_b2 b2 b2_n2
    play voice "voice/水之濑/050100280.ogg"
    stranger "那我们走吧。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/120100530.ogg"
    rxl "昨天没有来参加学生会议的是隔壁班的青木翔子对吧？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100310.ogg"
    stranger "你加入学生会的目的就是接近青木同学吗？"
    show rxl_dzf_b1 b1 b1_h3
    play voice "voice/日向怜/120100550.ogg"
    rxl "欸......为什么你会这么认为？"
    hide szl_dzf_b3
    show szl_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100320.ogg"
    stranger "直觉而已......"
    stop music fadeout 5.0
    play voice "voice/日向怜/120100560.ogg"
    rxl "不是{rb}灵纹{/rb}{rt}rune{/rt}？"
    hide szl_dzf_b1
    show szl_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100340.ogg"
    stranger "你是小孩子吗？只是直觉而已。"
    play music second_108 fadein 3.0 if_changed
    show rxl_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/120100580.ogg"
    rxl "据说直觉很准是女性荷尔蒙旺盛的象征，所以水之濑同学的胸才那么大啊~"
    hide rxl_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    play sound jump_1
    hide szl_dzf_b3 with None
    pause 0.1 hard
    show szl_dzf_b2 b2 b2_sp2 onlayer m2 at flu_up(0.15, 30):
        xpos 0.3
    play voice "voice/水之濑/050100350.ogg"
    szl "你在看哪里！？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/120100590.ogg"
    rxl "性方面很生疏呢~"
    show szl_dzf_b2 b2 b2_ga1
    play voice "voice/水之濑/050100360.ogg"
    szl "你是那种专讲黄段子的类型吗......"
    show rxl_dzf_b1 b1 b1_sp1
    play voice "voice/日向怜/120100610.ogg"
    rxl "学生会介绍的第一份工作是什么？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100380.ogg"
    szl "因为考试临近了所以要为此做好准备，比如通知社团停止活动之类的。"
    show rxl_dzf_b1 b1 b1_sp2
    play voice "voice/日向怜/120100620.ogg"
    rxl "欸......考试？"
    show rxl_dzf_b1 b1 b1_c1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/120100640.ogg"
    rxl "没听说过......"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100410.ogg"
    szl "看来你不擅长学习是真的啊。"
    show rxl_dzf_b1 b1 b1_h2
    play voice "voice/日向怜/120100650.ogg"
    rxl "保健体育的话我很擅长哟~"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100560.ogg"
    szl "这个玩笑我已经听腻了。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/120100820.ogg"
    rxl "真是冷淡啊......"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050100580.ogg"
    szl "已经这么晚了，快去会议室吧。"
    show rxl_dzf_b2 b2 b2_s1
    play voice "voice/日向怜/120100840.ogg"
    rxl "是~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day203.school_event04:
    $ flcam.move(0, 0, 0)
    scene set only school day room xuejian
    with dissolve
    pause 1.0 hard
    play music second_119 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180100430.ogg"
    yczs "那么，我也差不多要去社团活动了。"
    "记得以前一诚好像就是摄影部的成员。"
    "比起超自然研究会似乎正常了不少。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dzf_b2 b2 b2_h4 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020100920.ogg"
    yj "我也去社团活动吧。今天天气不错，我也要跑起来喽~"
    me01 "考试快到了，不趁现在活动的话之后就没机会了。"
    hide yj_dzf_b2 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_sp1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100930.ogg"
    yj "欸......考试？"
    hide yj_dzf_b3
    hide yczs_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010101750.ogg"
    xz "期末考试啊。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show yj_dzf_b3 b3 b3_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020100940.ogg"
    yj "那个能吃吗？"
    show xz_dzf_b2 b2 b2_s1
    play voice "voice/翔子/010101760.ogg"
    xz "对友加来说似乎不怎么好吃就是了......"
    $ flcam.move(0, -200, 600, duration=1.5)
    show yczs_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/一诚总司/180100470.ogg"
    yczs "据说考试期间，会全面停止社团活动。"
    show yj_dzf_b3 b3 b3_ga1 at flu_down(0.15, 20):
        xpos 0.5
    show han onlayer m2:
        xpos 0.425 ypos 0.29
    play voice "voice/植澄友加/020100950.ogg"
    yj "没听说过啊！！！"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/010101770.ogg"
    xz "考试期间一般都会这样的吧......"
    show yczs_dzf_b1 b1 b1_n1
    play voice "voice/一诚总司/180100480.ogg"
    yczs "神野你才刚转过来就要参加期末考试，很辛苦吧。"
    me01 "嘛，总会有办法的。"
    show xz_dzf_b2 b2 b2_sp1
    play voice "voice/翔子/010101780.ogg"
    xz "你觉得考试“很好吃”吗？"
    me01 "大概会比友加要轻松一些吧。"
    hide xz_dzf_b2
    hide yczs_dzf_b1
    hide han
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020100960.ogg"
    yj "好过分呀凉君，明明还不清楚我成绩的说。"
    me01 "难道说你的成绩实际上很优秀？"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s2 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020100970.ogg"
    yj "用这样难以置信的目光看着我的话我可是会很受伤的。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show yczs_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/180100490.ogg"
    yczs "毕竟植澄同学成绩优秀什么的，我还是第一次听说。"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/010101790.ogg"
    xz "我也是......"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_ga3 onlayer m1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/020100980.ogg"
    yj "我也是啊......"
    me01 "至少本人出来反对一下！"
    hide xz_dzf_b2
    hide yczs_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_h1 onlayer m1 at flu_down(0.15, 30):
        xpos 0.5
    play voice "voice/植澄友加/020100990.ogg"
    yj "但是我的体育成绩很优秀哦~"
    me01 "这点我倒是完全不觉得意外。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day203.kindergarden_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "放学后，依旧是我去接送爱衣。"
    "考试临近学生会那边似乎也开始繁忙起来了，因此翔子并没有与我同行。"
    pause 1.0 hard
    scene set only school day outside xuejian
    with dissolve
    pause 1.0 hard
    play music second_112 fadein 3.0 if_changed
    me01 "今天也辛苦了，立花老师。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101260.ogg"
    lhx "你也是，辛苦了~"
    me01 "在这里休息吗？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101270.ogg"
    lhx "目前我还在工作中。"
    me01 "要等到小朋友全都回去为止才算结束对吧。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101280.ogg"
    lhx "就是这样的，不过有一半已经走了。"
    me01 "话说回来，立花老师你也是刚到雪见市来的吧？自己一个人住吗？"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/030101330.ogg"
    lhx "如果可以的话我倒是希望能够处理掉日向......"
    me01 "日向？日向怜吗？"
    show lhx_dzf_b2 b2 b2_s2
    play voice "voice/立花希/030101340.ogg"
    lhx "那家伙有严重的自来熟，和她在一个屋檐下的话我的生活都会变得乱七八糟的。"
    show lhx_dzf_b2 b2 b2_s3
    play voice "voice/立花希/030101350.ogg"
    lhx "我泡澡的时候，日向也会跟进来。"
    "听到这里，我下意识地看向了立花希那平平的胸。"
    play sound jump_1
    hide lhx_dzf_b2 with None
    pause 0.1 hard
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/030101360.ogg"
    lhx "你在想象什么啊？"
    me01 "什么都没想。嗯，什么都没想。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101370.ogg"
    lhx "不只是泡澡，就连我换衣服的时候日向都会来偷看。"
    play voice "voice/立花希/030101380.ogg"
    lhx "我头一回感受到了贞操的危机。"
    me01 "不过那家伙只是单纯地寻你开心吧。"
    me01 "毕竟......"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101400.ogg"
    lhx "你又在想象什么啊！"
    me01 "什么都没有，嗯什么都没有。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101420.ogg"
    lhx "再这样下去的话我可能就要被迫搬出公寓了。"
    me01 "要来和我一起住吗？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101430.ogg"
    lhx "你在图谋些什么啊？"
    show lhx_dzf_b3 b3 b3_n3
    play voice "voice/立花希/030101460.ogg"
    lhx "这种羞人的设定不符合我的性格。"
    show lhx_dzf_b3 b3 b3_s1
    play voice "voice/立花希/030101440.ogg"
    lhx "还是算了吧。"
    me01 "果然比起我还是和日向住一起更有安全感不是吗。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101480.ogg"
    lhx "这话让人不敢相信是出自凉君之口呢。"
    me01 "在你眼里我就不能说出一些正能量的话吗......"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/030101490.ogg"
    lhx "是的，我本来以为你是不擅长交际的类型。"
    me01 "虽然是没有错......但那些都是过去式了。"
    me01 "因为人是会改变的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    $ _overworld_label = 'day203_2'
    $ seen_day203_shenshe_event01 = False
    $ seen_day203_kindergarden_event03 = False

label day203.map2:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day203_2':
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    elif _overworld_label == 'day203_2.kindergarden_event03':
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    elif _overworld_label == 'day203_2.shenshe_event01':
        $ flcam.move(*overworld.camera_positions['shenshe'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    show lhx_dzf_b2 b2 b2_n1 onlayer screens at side_map('lhx'), basicfade
    $ _window_animation = 'in'
    if _overworld_label == 'day203_2':
        window mode map
        lhx "青木同学还需要一段时间才能赶过来，现在要做些什么好呢......" nointeract
    elif _overworld_label == 'day203_2.kindergarden_event03' or _overworld_label == 'day203_2.shenshe_event01':
        window mode map
        me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        shenshe=("day203.shenshe_event01", "not seen_day203_shenshe_event01"),
        kindergarden=("day203.kindergarden_event03", "not seen_day203_kindergarden_event03"))
    hide lhx_dzf_b2
    $ window_animate_outro()
    if _return == 'day203.shenshe_event01':
        $ flcam.move(*overworld.camera_positions['shenshe'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day203.kindergarden_event03' and _overworld_label == 'day203_2':
        with Pause(1.0)
        scene black with dissolve
    elif _return == 'day203.kindergarden_event03' and _overworld_label != 'day203_2':
        $ flcam.move(*overworld.camera_positions['kindergarden'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day203.kindergarden_event03:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian
    $ flcam.move(4500, 300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210100300.ogg"
    qb "{size=72}喂！！！{/size}"
    play music second_108 fadein 3.0 if_changed
    me01 "为什么你每次登场都要大喊大叫的！"
    show qianbo_dzf_b1 b1 b1_sp2
    play voice "voice/千波/210100310.ogg"
    qb "啊，是凉君男！"
    me01 "差不多该把这个奇怪的称呼丢掉了吧。"
    show qianbo_dzf_b1 b1 b1_ga2
    play voice "voice/千波/210100320.ogg"
    qb "我还以为是哪个对着幼儿园女生流口水的变态大叔呢。"
    me01 "一般会有这种家伙吗......"
    show qianbo_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/210100330.ogg"
    qb "最近小孩的发育可是很好的哟~"
    me01 "是是是我知道了，拜托你别再摆弄那些毫无意义的姿势，小不点的身体我已经看腻了。"
    stop music fadeout 5.0
    $ flcam.move(2250, 250, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110100960.ogg"
    aiyi "大哥哥，你来接我了吗？"
    me01 "是啊。"
    play music second_115 fadein 3.0 if_changed
    hide qianbo_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/爱衣/110100980.ogg"
    aiyi "那在大姐姐来之前就继续和我们一起玩吧。"
    pause 1.0 hard
    scene black
    with right2left_02
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian2
    with right2left_02
    pause 1.0 hard
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m1 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/爱衣/110100990.ogg"
    aiyi "今天大姐姐在学校有工作吗？"
    me01 "是啊。"
    $ flcam.move(2250, 250, 750, duration=1.5)
    show qianbo_dzf_b1 b1 b1_h4 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210100340.ogg"
    qb "是学生会的工作对吧？"
    me01 "为什么你这家伙会知道学生会啊。"
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/小桃/220100260.ogg"
    ycxt "奶奶说了，学生会聚集着许多非常优秀的学生对吧？"
    show qianbo_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/千波/210100360.ogg"
    qb "是啊，学生会很伟大的，而且我的姐姐可是学生会长哟~"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110101000.ogg"
    aiyi "千波的姐姐真的非常出色呢~"
    show qianbo_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/210100370.ogg"
    qb "是啊，所以她的妹妹也一定很出色。"
    me01 "欸，被你这么一说我倒想看看那位“优秀的妹妹”是什么样了。"
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 30):
        xpos 0.7
    play voice "voice/千波/210100380.ogg"
    qb "不就在你面前吗？！"
    me01 "真遗憾。"
    $ flcam.move(2250, 250, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n1 onlayer m1:
        xpos 0.5
    play voice "voice/小桃/220100280.ogg"
    ycxt "刚才说的这些小桃也都知道，是奶奶告诉我的。"
    me01 "小桃的奶奶还真是见多识广。"
    hide qianbo_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/小桃/220100290.ogg"
    ycxt "嗯，诶嘿嘿~"
    stop music fadeout 5.0
    play voice "voice/小桃/220100310.ogg"
    ycxt "奶奶还说，{rb}柚子会长{/rb}{rt}千波的姐姐{/rt}是飞机场。"
    play music second_108 fadein 3.0 if_changed
    show ycxt_dzf_b1 b1 b1_n1
    play voice "voice/小桃/220100320.ogg"
    ycxt "还有翔子姐姐是巨乳。"
    "收回前言，这是什么奶奶啊！"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/220100330.ogg"
    ycxt "大家都说奶奶是智囊，什么都知道。"
    $ flcam.move(-2250, 250, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110101040.ogg"
    aiyi "巨乳和飞机场是什么？"
    me01 "这些爱衣还不需要知道。"
    $ flcam.move(0, 200, 600, duration=1.5)
    show qianbo_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210100420.ogg"
    qb "要说我和姐姐最不同的地方的话，那就是胸了。"
    me01 "你的是？"
    show qianbo_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/210100430.ogg"
    qb "火辣身材！"
    me01 "去看眼科吧。"
    show ycxt_dzf_b1 b1 b1_n1
    play voice "voice/小桃/220100340.ogg"
    ycxt "奶奶说千波和立花老师一样是飞机场。"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a3 at flu_up(0.15, 30):
        xpos 0.7
    play voice "voice/千波/210100440.ogg"
    qb "人家才不是飞机场！"
    play voice "voice/爱衣/110101050.ogg"
    aiyi "身材火辣是什么呢？"
    me01 "这个问题还是不要问我比较好。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110101060.ogg"
    aiyi "那就去问大姐姐好了~"
    with vpunch
    me01 "{size=72}不行！！！{/size}"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/220100360.ogg"
    ycxt "还有呢还有呢，奶奶告诉我......"
    hide aiyi_dzf_b1
    hide qianbo_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/小桃/220100370.ogg"
    ycxt "吃卷心菜会丰胸，因为有很多必须的营养物质。"
    play voice "voice/小桃/220100380.ogg"
    ycxt "还有按摩也不错，说是要像画圈圈一样温柔地揉。"
    me01 "小桃......以后还是不要和你奶奶说话了。"
    hide ycxt_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210100460.ogg"
    qb "凉君！"
    me01 "又干什么？"
    show qianbo_dzf_b1 b1 b1_a3
    play voice "voice/千波/210100470.ogg"
    qb "你快揉揉我的胸！"
    me01 "自己吃你的卷心菜去！"
    play sound ganga01
    show qianbo_dzf_b1 b1 b1_a2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/210100480.ogg"
    qb "麻烦你像画圆圈一样温柔地揉！"
    me01 "小声点！被听到的话会被误会的！"
    hide qianbo_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/140100240.ogg"
    qcls "那个......"
    play sound jing02
    with vpunch
    me01 "我什么也没干！！！"
    pause 1.0 hard
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp2
    play voice "voice/千川老师/140100250.ogg"
    qcls "哈、哈？我只是想说有人来接小桃和千波了......"
    me01 "......"
    "果然，陪这些小孩玩耍是真的累人。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if seen_day203_shenshe_event01:
        jump day203.kindergarden_event04
    $ _overworld_label = 'day203_2.kindergarden_event03'
    $ seen_day203_kindergarden_event03 = True
    jump day203.map2

label day203.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only street evening road1 xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/030101550.ogg"
    lhx "比起河滩附近的地方，这次还是先往山里的方向去看看吧。"
    me01 "了解。"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030101580.ogg"
    lhx "快走吧，这个季节太阳下山很快的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 1.0 hard
    "难得的机会，我和立花老师这两位“初来乍到”的新人决定四下逛逛。"
    "当然这是在经过千川老师的同意之后的举动。"
    "熟悉环境的同时还能顺便互相了解一下对方。"
    "能当个称职的导游就好了......"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only shenshe evening xuejian
    with dissolve
    pause 1.0 hard
    play music second_120 fadein 3.0 if_changed
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101590.ogg"
    lhx "这里是？"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n3 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101600.ogg"
    lhx "虽然听说这座城市有神社，但是没想到会建在这种地方。"
    hide lhx_dsf_b3
    $ flcam.move(0, -800, 1100, duration=3.0, warper='ease_cubic')
    pause 2.5 hard
    "坐落在山麓上的神社。"
    "远离商店街的嘈杂，也导致这里几乎看不到人烟。"
    me01 "不论是哪里的神社，给人的感觉都差不多。"
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101610.ogg"
    lhx "是这样吗？"
    me01 "是啊。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101630.ogg"
    lhx "这里看起来很萧条啊......还在使用中吗？"
    me01 "估计热闹的也只有在跨年祭祀的时候了吧。"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101660.ogg"
    lhx "神社的名字是......星天宫的样子。"
    "虽然之前就听万夜花小姐说起过“星天宫”是一个遍布全世界的大型机构。"
    "可没想到这方圆几百里内大大小小的神社几乎都与它有关。"
    play voice "voice/立花希/030101680.ogg"
    lhx "名字里有“星”字的话，应该是和星之神有关吧。"
    me01 "是这样吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101670.ogg"
    lhx "你不知道吗？"
    me01 "平时也没有太在意，找个人问问好了。"
    play voice "voice/立花希/030101690.ogg"
    lhx "问谁？"
    me01 "那边好像有人的样子。"
    "立花希顺着我手指的方向看去。"
    hide lhx_dsf_b2
    $ flcam.move(4500, -800, 1100, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    "不远处就站着一位身着巫女服的女生。"
    "话说回来我也没太在意，她是什么时候开始就站在那里的？"
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101700.ogg"
    lhx "刚才还没在那里的，看来是刚好从正殿走出来的样子。"
    me01 "要过去吗？"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101710.ogg"
    lhx "还是算了，我对神社没什么兴趣。"
    hide lhx_dsf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_sp1 onlayer screens at side_left('liuli', 0.22), basicfade
    play voice "voice/琉璃/040100900.ogg"
    liuli "啊......"
    hide liuli_dzf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/040100910.ogg"
    liuli "果然是神野前辈~"
    me01 "琉璃？"
    hide liuli_dzf_b1
    show liuli_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100920.ogg"
    liuli "中午的事真的非常感谢~"
    me01 "我倒觉得我没做什么值得被感谢的事。"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100930.ogg"
    liuli "能和我一起吃饭真是太感谢你了。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101720.ogg"
    lhx "哼......"
    hide liuli_dzf_b3
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "怎么了？"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101750.ogg"
    lhx "看她穿的校服，是你们学校的学生吗？"
    me01 "嗯，她是比我小一年级的学妹。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101760.ogg"
    lhx "比起同级生，你居然对年纪小的下手了吗。"
    me01 "你在说什么啊......"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/030101770.ogg"
    lhx "凉君你是好这口的吗！"
    me01 "才不是呢。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101780.ogg"
    lhx "看来你的校园生活挺挺丰富的嘛。"
    me01 "话说你是在生气吗......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100940.ogg"
    liuli "那个......旁边的这位是？"
    me01 "是邻家的小孩子。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101790.ogg"
    lhx "你想吵架吗？"
    hide liuli_dzf_b1
    show liuli_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100950.ogg"
    liuli "啊我知道了，是幼儿园的那位吧。"
    show lhx_dsf_b3 b3 b3_n1
    play voice "voice/立花希/030101800.ogg"
    lhx "真亏你能猜到。"
    show liuli_dzf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/040100960.ogg"
    liuli "是的，因为幼儿园和我们的学校很近，我也经常从那里经过。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101810.ogg"
    lhx "我叫立花希。"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040100970.ogg"
    liuli "立花你是那里的小朋友对吧~"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/030101820.ogg"
    lhx "感觉我得为这份屈辱而做点什么了！"
    me01 "要带上小黄帽了吗？（注释：日本幼儿园的小朋友一般都佩戴小黄帽。）"
    hide lhx_dsf_b2 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/立花希/030101830.ogg"
    lhx "你想打架吗？"
    show liuli_dzf_b3 b3 b3_s5
    play voice "voice/琉璃/040100980.ogg"
    liuli "那个......是我误会了什么吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101840.ogg"
    lhx "我是在幼儿园帮忙的，才不是那里的小朋友。"
    show liuli_dzf_b3 b3 b3_sp1
    play voice "voice/琉璃/040100990.ogg"
    liuli "是、是这样的吗？"
    show lhx_dsf_b2 b2 b2_h2
    play voice "voice/立花希/030101850.ogg"
    lhx "就是这样的，不如说没有其他的可能了。"
    hide liuli_dzf_b3 with None
    pause 0.1 hard
    show liuli_dzf_b2 b2 b2_c1 onlayer m2 at flu_down(0.25, 20, 2):
        xpos 0.5
    play voice "voice/琉璃/040101000.ogg"
    liuli "抱、抱歉！"
    me01 "立花老师因为长得很可爱所以也经常会被大家误会，所以不需要太在意的。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101860.ogg"
    lhx "你再不收敛点我就要发飙了。"
    show liuli_dzf_b2 b2 b2_sp1
    play voice "voice/琉璃/040101020.ogg"
    liuli "立花小姐是神野前辈的朋友吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    lhx "......"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/030101870.ogg"
    lhx "差不多吧。"
    me01 "犹豫了一下让我很受伤啊。"
    hide lhx_dsf_b2
    hide liuli_dzf_b2
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/藤原瞳/130100010.ogg"
    stranger "花山院？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/130100020.ogg"
    stranger "这些人是谁？"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/130100030.ogg"
    stranger "是附近的大哥哥和小朋友吗？"
    $ flcam.move(0, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101880.ogg"
    lhx "我才不是大哥哥。"
    me01 "她说的大哥哥是我吧！"
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101030.ogg"
    liuli "是神野前辈和立花小姐，他们都是我的朋友。"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/030101890.ogg"
    lhx "连我......也是你的朋友吗。"
    hide lhx_dsf_b2
    $ flcam.move(2250, 0, 750, duration=1.5)
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    pause 0.5 hard
    play voice "voice/琉璃/040101040.ogg"
    liuli "她叫藤原瞳，是我的同学同时也是好朋友。"
    me01 "原来如此，这不是能正常交朋友的吗。"
    show liuli_dzf_b3 b3 b3_s1
    play voice "voice/琉璃/040101050.ogg"
    liuli "啊是的......虽然说不定只有我单方面这么想。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100040.ogg"
    tyt "离群的伙伴。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/130100050.ogg"
    tyt "我也一样。"
    play voice "voice/琉璃/040101070.ogg"
    liuli "我倒觉得藤原同学你并不是......"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/130100060.ogg"
    tyt "一样的，所以是伙伴。"
    play voice "voice/藤原瞳/130100070.ogg"
    tyt "花山院是朋友~"
    hide liuli_dzf_b3 with None
    pause 0.1 hard
    show liuli_dzf_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/040101080.ogg"
    liuli "是、是的！非常感谢。"
    "因为有着共同的遭遇所以关系自然就变好了吗。"
    hide liuli_dzf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    show tyt_wnf_b1 b1 b1_n1:
        xpos 0.7
        linear 0.5 xpos 0.5
    pause 0.5 hard
    play voice "voice/藤原瞳/130100080.ogg"
    tyt "两位是客人吗？"
    me01 "你说客人？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101900.ogg"
    lhx "是不是把我们当成是参拜客了？"
    me01 "我们只是路过而已。"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/130100090.ogg"
    tyt "拿不到香油钱......"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101910.ogg"
    lhx "你穿着巫女服，是在这里工作吗？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100100.ogg"
    tyt "虽然现在已经结束了。"
    me01 "话说回来，琉璃你又为什么会在这里？"
    hide lhx_dsf_b2
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/040101090.ogg"
    liuli "这里是藤原同学的神社，我只是来帮忙打扫而已。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/130100110.ogg"
    tyt "其实我一个人也没问题的。"
    hide liuli_dzf_b3
    show liuli_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/040101100.ogg"
    liuli "如果打扰的话我以后会注意的。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100120.ogg"
    tyt "倒不是打扰。"
    hide liuli_dzf_b1
    hide tyt_wnf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101920.ogg"
    lhx "这么说来，花山院同学还真是热心肠呢。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101120.ogg"
    liuli "是、是这样吗？"
    show liuli_dzf_b1 b1 b1_n1
    play voice "voice/琉璃/040101130.ogg"
    liuli "直接叫我琉璃就好了，立花小姐既然是在幼儿园帮忙的话应该是比我年长的。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/030101930.ogg"
    lhx "我明白了{rb}琉之助{/rb}{rt}昵称{/rt}~"
    hide lhx_dsf_b2
    $ flcam.move(2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/藤原瞳/130100130.ogg"
    tyt "天色暗下来了，{rb}琉之助{/rb}{rt}模仿{/rt}不回家没问题吗？"
    hide liuli_dzf_b1
    show liuli_dzf_b3 b3 b3_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101170.ogg"
    liuli "也是呢，打扰了这么久真是不好意思。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/130100140.ogg"
    tyt "帮了我不少忙，所以不需要道歉的。"
    show liuli_dzf_b3 b3 b3_n1
    play voice "voice/琉璃/040101180.ogg"
    liuli "藤原同学真是个温柔的人。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100150.ogg"
    tyt "是你太客气了。"
    hide liuli_dzf_b3
    show liuli_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101220.ogg"
    liuli "那么藤原同学，明天学校见~"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/130100160.ogg"
    tyt "嗯，拜拜~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    jump day203.shenshe_event02

label day203.shenshe_event02:
    $ flcam.move(0, 0, 0)
    scene set only street evening road1 xuejian
    with dissolve
    play music second_118 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_h1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/040101230.ogg"
    liuli "藤原同学的神社除了祭祀之外，{encyclopedia=chuyi}初诣{/encyclopedia}的时候也会有很多人的样子。"
    me01 "这么说来明年的初诣也快到了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/030101990.ogg"
    lhx "璃之助也会去参拜吗？"
    show liuli_dzf_b2 b2 b2_n1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/琉璃/040101240.ogg"
    liuli "不只是参拜，我希望也能帮忙做一些工作。"
    show lhx_dsf_b2 b2 b2_sp1
    play voice "voice/立花希/030102000.ogg"
    lhx "想穿巫女装吗？"
    hide lhx_dsf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101260.ogg"
    liuli "我扮巫女的话也不知道合不合适呢。"
    me01 "放心好了，我敢保证一定很适合你的。"
    hide liuli_dzf_b3
    show liuli_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101270.ogg"
    liuli "太、太好了。"
    me01 "到时候我也会去给你加油的。"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040101280.ogg"
    liuli "神野前辈，非常期待你的到来。"
    "努力的孩子真是招人喜欢。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    if seen_day203_kindergarden_event03:
        jump day203.kindergarden_event04
    $ _overworld_label = 'day203_2.shenshe_event01'
    $ seen_day203_shenshe_event01 = True
    jump day203.map2

label day203.kindergarden_event04:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/000100100.ogg"
    xfe "凉君......"
    pause 1.0 hard
    play music second_103 fadein 3.0 if_changed
    scene set only street evening road1 xuejian alpha
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000100110.ogg"
    xfe "已经和过去......不一样了。"
    play voice "voice/希菲尔/000100120.ogg"
    xfe "在你的身边......有很多的人围绕着你。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/000100130.ogg"
    xfe "改变了呢。"
    play voice "voice/希菲尔/000100140.ogg"
    xfe "同时也成长了呢。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000100150.ogg"
    xfe "没关系的。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_h1
    play voice "voice/希菲尔/000100160.ogg"
    xfe "今后也一定，能交到更多朋友的。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard

label day203.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only home night outside xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    play sound open_door6
    pause 1.0 hard
    hide snow_level1
    scene set only home night passwalk xuejian
    with dissolve
    pause 1.0 hard
    play sound close_door3
    pause 1.0 hard
    $ flcam.move(-2250, 0, 750, duration=1.5)
    play music second_105 fadein 3.0 if_changed
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.3)
    show xz_dsf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/爱衣/110101130.ogg"
    aiyi "大哥哥欢迎回来~"
    play voice "voice/翔子/010101940.ogg"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010101950.ogg"
    xz "饭已经做好了，在此之前要洗好手哟。"
    me01 "我是小孩子吗......"
    show xz_dsf_b3 b3 b3_h1
    play voice "voice/翔子/010101960.ogg"
    xz "开玩笑的啦~"
    "虽然已经不是第一天了，但是这个状态有点像一家三口的感觉让我有点不好意思。"
    pause 1.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home night kitchen xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    stop music fadeout 5.0
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110101160.ogg"
    aiyi "呐呐，大姐姐。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010101970.ogg"
    xz "怎么了？"
    play music second_108 fadein 3.0 if_changed
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110101170.ogg"
    aiyi "大姐姐是火辣身材吗？"
    play sound jump_1
    show xz_dsf_b2 b2 b2_ga1 at flu_down(0.15, 20):
        xpos 0.5
    show wflash onlayer texture
    with vpunch 
    show tanhao at tanhao_x055 onlayer m2
    play voice "voice/翔子/010101980.ogg"
    xz "{size=72}噗哈！！！{/size}"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110101180.ogg"
    aiyi "小桃的奶奶说大姐姐是巨乳。"
    show xz_dsf_b2 b2 b2_ga2
    play voice "voice/翔子/010101990.ogg"
    xz "是、是这样啊......"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110101190.ogg"
    aiyi "所以大姐姐，火辣身材是什么？"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010102000.ogg"
    xz "这、这个......"
    play voice "voice/爱衣/110101200.ogg"
    aiyi "巨乳又是什么？"
    show xz_dsf_b3 b3 b3_s1
    play voice "voice/翔子/010102010.ogg"
    xz "那、那是......"
    me01 "爱衣，对这两点优势皆具备的人咨询是没有办法得到真相的。"
    hide xz_dsf_b3
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/110101210.ogg"
    aiyi "是这样吗？"
    me01 "是啊，你看翔子她也很困扰。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110101220.ogg"
    aiyi "大姐姐因为是巨乳所以很困扰吗？"
    me01 "是啊，肩膀会很酸的。"
    hide aiyi_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dsf_b3 with None
    pause 0.1 hard
    show xz_dsf_b1 b1 b1_a2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play sound ganga01
    play voice "voice/翔子/010102020.ogg"
    xz "不是在说这个吧？！"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110101230.ogg"
    aiyi "那如果是问大哥哥巨乳的事情，大姐姐就不会困扰了吗？"
    me01 "你说的没有错。"
    hide xz_dsf_b1 with None
    pause 0.1 hard
    show xz_dsf_b2 b2 b2_a1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010102030.ogg"
    xz "才不是！！！"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110101240.ogg"
    aiyi "那么大哥哥，你觉得大姐姐是巨乳吗？"
    me01 "......果然这个问题还是不要问我了，翔子她在瞪着我。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110101250.ogg"
    aiyi "千波在说她姐姐的时候也提到了飞机场。"
    hide xz_dsf_b2
    show xz_dsf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010102040.ogg"
    xz "是、是这样吗......"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110101260.ogg"
    aiyi "还说了揉胸的话就会变大。"
    show xz_dsf_b1 b1 b1_sp3
    play voice "voice/翔子/010102050.ogg"
    xz "是、是这样啊......"
    "两眼都在冒金星了，翔子她现在一定很想快点结束这个尴尬的话题吧。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110101270.ogg"
    aiyi "大姐姐，胸很大呢~"
    hide xz_dsf_b1
    show xz_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010102060.ogg"
    xz "我、我才不知道。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/110101280.ogg"
    aiyi "是谁帮忙揉的吗？"
    hide xz_dsf_b3 with None
    pause 0.1 hard
    show xz_dsf_b2 b2 b2_ga1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010102070.ogg"
    xz "才不是！"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110101290.ogg"
    aiyi "爱衣要是请谁帮忙揉的话，也会变得像姐姐一样大吗？"
    show xz_dsf_b2 b2 b2_a1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010102080.ogg"
    xz "才不会！！！"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110101300.ogg"
    aiyi "呐，大哥哥~"
    play sound jing02
    with vpunch
    me01 "别在这个时候把话题丢给我啊！"
    stop music fadeout 5.0  
    pause 1.0 hard 
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home night my_room xuejian
    with dissolve
    pause 2.0 hard
    scene set only sky night xuejian2
    with dissolve
    pause 1.0 hard
    "不知从何时起，天空已经放晴了。"
    "我躺在床上盯着手里全新的教科书发呆。"
    "马上就要考试了，也该好好学习下了。"
    "至于雪见市的这场雪，还有很多的疑点。"
    "希菲尔的话应该知道些什么吧。"
    pause 1.0 hard
    $ seen_living_room = False

label day203.myroom_event01:
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
            move _("客厅") jump day203.livingroom_event01
            screen_direction left
            sleep jump day203.sleep

label day203.livingroom_event01:
    if not seen_living_room:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        $ flcam.move(0, -300, 900, duration=1.5)
        with slowdissolve
        pause 0.5 hard
        show xz_dsf_b3 b3 b3_s1 onlayer m1:
            xpos 0.5
        play voice "voice/翔子/010102470.ogg"
        xz "哈啊......"
        play music second_111 fadein 3.0 if_changed
        show xz_dsf_b3 b3 b3_s3
        play voice "voice/翔子/010102480.ogg"
        xz "刚才真的好险，在神野君的面前还是会紧张啊。"
        play voice "voice/翔子/010102490.ogg"
        xz "为什么会这样呢......明明已经和“另一个我”说好了的，但是还是很不安。"
        play voice "voice/翔子/010102530.ogg"
        xz "如果，不更注意一点的话。"
        play voice "voice/翔子/010102550.ogg"
        xz "那样的话，我......"
        $ flcam.move(-2250, 0, 750, duration=1.5)
        show aiyi_sy_b1 b1 b1_sp1 onlayer m2:
            xpos 0.3
        play voice "voice/爱衣/110101310.ogg"
        aiyi "大姐姐，怎么了吗？"
        hide xz_dsf_b3
        show xz_dsf_b1 b1 b1_sp1 onlayer m1:
            xpos 0.5
        play voice "voice/翔子/010102570.ogg"
        xz "爱、爱衣，你不是回房间了吗？"
        show aiyi_sy_b1 b1 b1_n1
        play voice "voice/爱衣/110101320.ogg"
        aiyi "在睡觉之前我想跟大姐姐还有大哥哥说声晚安。"
        hide xz_dsf_b1
        show xz_dsf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        play voice "voice/翔子/010102580.ogg"
        xz "是吗......真是好孩子呢~"
        show aiyi_sy_b1 b1 b1_sp1
        play voice "voice/爱衣/110101330.ogg"
        aiyi "大哥哥呢？"
        hide xz_dsf_b3
        show xz_dsf_b2 b2 b2_n1 onlayer m1:
            xpos 0.5
        play voice "voice/翔子/010102590.ogg"
        xz "现在应该在洗澡吧，我会转告他的爱衣先回去睡吧。"
        show aiyi_sy_b1 b1 b1_h1
        play voice "voice/爱衣/110101340.ogg"
        aiyi "不嘛，我要和大姐姐一起等。"
        show xz_dsf_b2 b2 b2_s2
        play voice "voice/翔子/010102600.ogg"
        xz "我也不是非等神野君不可的。"
        show aiyi_sy_b1 b1 b1_s2
        play voice "voice/爱衣/110101350.ogg"
        aiyi "大姐姐......很伤心吗？"
        show xz_dsf_b2 b2 b2_sp1
        play voice "voice/翔子/010102610.ogg"
        xz "欸？"
        play voice "voice/爱衣/110101360.ogg"
        aiyi "爱衣刚才就感觉到了，大姐姐好像很伤心的样子，发生什么了吗？"
        show xz_dsf_b2 b2 b2_n1
        play voice "voice/翔子/010102620.ogg"
        xz "不是的，并不是什么伤心的事。"
        show aiyi_sy_b1 b1 b1_sp1
        play voice "voice/爱衣/110101370.ogg"
        aiyi "那是高兴的事吗？"
        hide xz_dsf_b2 with None
        pause 0.1 hard
        show xz_dsf_b1 b1 b1_sp2 onlayer m1 at flu_down(0.15, 20):
            xpos 0.5
        play voice "voice/翔子/010102630.ogg"
        xz "也不是什么高兴的事情！"
        $ flcam.move(-2250, 0, 900, duration=1.5)
        pause 0.5 hard
        show aiyi_sy_b1 b1 b1_s2
        play voice "voice/爱衣/110101380.ogg"
        aiyi "大姐姐在见到大哥哥的时候总是一副不知道是开心还是难过的表情。"
        hide xz_dsf_b1
        show xz_dsf_b3 b3 b3_s1 onlayer m1:
            xpos 0.5
        play voice "voice/翔子/010102640.ogg"
        xz "......那个呢，因为我们的过去有一段青涩的回忆。"
        show aiyi_sy_b1 b1 b1_sp1
        play voice "voice/爱衣/110101390.ogg"
        aiyi "青涩的回忆，是发生了什么事吗？"
        hide xz_dsf_b3
        show xz_dsf_b2 b2 b2_s2 onlayer m1:
            xpos 0.5
        play voice "voice/翔子/010102650.ogg"
        xz "嗯，稍微有点......"
        play voice "voice/爱衣/110101410.ogg"
        aiyi "大姐姐，脸红透了哟~"
        show xz_dsf_b2 b2 b2_s1
        play voice "voice/翔子/010102670.ogg"
        xz "才没那回事......"
        pause 0.5 hard
        $ flcam.move(-3200, 0, 750, duration=3.0)
        show xz_dsf_b2 b2 b2_s1:
            xpos 0.5
            linear 0.5 xpos 0.4
        pause 0.5 hard
        show aiyi_sy_b1 b1 b1_s2 at flu_down(0.35, 20):
            xpos 0.3
        pause 1.0 hard
        play voice "voice/爱衣/110101420.ogg"
        aiyi "摸着爱衣的头，是准备糊弄过去吗？"
        show xz_dsf_b2 b2 b2_s2
        play voice "voice/翔子/010102680.ogg"
        xz "嗯......是啊，今晚的这件事情是不能对爱衣说的。"
        play voice "voice/翔子/010102690.ogg"
        xz "这是只属于姐姐我和他之间的秘密呢~"
        stop music fadeout 5.0
        pause 1.0 hard
        scene black
        with slowerdissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        show xz_dsf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        show aiyi_sy_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        $ flcam.move(-2250, -400, 600)
        $ flcam.move(-2250, -100, 400, duration=1.5)
        pause 0.5 hard
        $ seen_living_room = True
    else:
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        show xz_dsf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        show aiyi_sy_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        $ flcam.move(-2250, -400, 600)
        $ flcam.move(-2250, -100, 400, duration=3.0)
        with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dsf_b3 onlayer m1:
            camera_pos (scale(2597), scale(-1024), 400)
            screen_pos (0.55, 1.0)
            screen_direction right
            move _("卧室") jump day203.myroom_event01
        object aiyi_sy_b1 onlayer m2 jump day203.aiyi_event01

label day203.aiyi_event01:
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_sy_b1 b1 b1_h1
    aiyi "大哥哥，晚安~"
    $ flcam.move(-2250, -100, 400, duration=3.0)
    jump investigate

label day203.sleep:
    menu:
        "早点休息":
            if not seen_living_room:
                window mode thought
                me01 "睡觉前还是先去和翔子她们打声招呼吧。"
                $ flcam.move(0, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            hide screen investigation_popup
            show xz_dsf_b3 b3 b3_h1
            play voice "voice/翔子/010001080.ogg"
            xz "晚安~"
        "{#cancel}再等等":
            xz "还有什么事情要考虑吗......"
            $ flcam.move(0, 100, 200, duration=3.0)
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
    jump day203_2

label day203_2:
    nvl clear
    pcenter "雪......"
    pause 0.5 hard
    nvl clear
    with dissolve
    pcenter "雪花纷然飘落。"
    pause 0.5 hard
    nvl clear
    with dissolve
    pcenter "过去的场景渐渐浮现在眼前。"
    pause 0.5 hard
    nvl clear
    with dissolve
    pause 2.0 hard
    play music second_117 fadein 3.0 if_changed
    scene set only balltower snow day xuejian alpha
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "过去的我每次放假的时候，都会去找希菲尔玩。"
    "甚至每次从学校回来的时候，都会刻意路过这里。"
    "对我而言，那时候和她一起玩耍的时光就是我快乐的源泉。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201060.ogg"
    xfe "凉君，今天也来{encyclopedia=bagu}叭咕叭咕{/encyclopedia}吧~"
    me01 "才不要呢。"
    show ts_xfe_yjz_b3 b3 b3_h4 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201070.ogg"
    xfe "叭咕叭咕~"
    "希菲尔开始吃起地上的积雪。"
    me01 "不要随便乱吃啊！莫非是肚子饿了吗？"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/000201080.ogg"
    xfe "是这样吗？"
    me01 "发问的是我吧。"
    show ts_xfe_yjz_b3 b3 b3_h4 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201090.ogg"
    xfe "叭咕叭咕~"
    me01 "如果肚子饿了的话，我去拿点东西给你吃吧。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/000201100.ogg"
    xfe "拿什么？"
    me01 "点心还有剩下的，等我一下。"
    "我从包里拿出一个盒子。"
    play voice "voice/希菲尔/000201110.ogg"
    xfe "这是什么？"
    me01 "年糕。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201120.ogg"
    xfe "年糕？"
    me01 "嗯，是一种在正月吃的年菜。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201130.ogg"
    xfe "碗里漂浮着白色的东西。"
    me01 "嗯，那个就是年糕了。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201140.ogg"
    xfe "白色的，就像雪一样~"
    play sound yangmu
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h5 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201150.ogg"
    xfe "好像很好吃的样子......"
    "希菲尔两眼闪着金光。"
    me01 "那么，请用吧。"
    show ts_xfe_yjz_b3 b3 b3_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201160.ogg"
    xfe "要开动了哟~"
    hide ts_xfe_yjz_b3
    $ flcam.move(0, 0, 0, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    "因为希菲尔拿筷子的手势不太熟练。"
    "所以她选择直接把脸贴近碗的边缘，然后把年糕一口含进嘴里。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show ts_xfe_yjz_b2 b2 b2_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201170.ogg"
    xfe "呼哇啊啊......"
    show ts_xfe_yjz_b2 b2 b2_c1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201180.ogg"
    xfe "呼呀啊啊啊......"
    "吃了一口之后，希菲尔的身体就变得软趴趴的了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    me01 "希、希菲尔？！"
    "情急之下我取了一把地上的积雪递给了她。"
    show ts_xfe_yjz_b2 b2 b2_s1 at flu_down(0.25, 20, 2):
        xpos 0.5
    pause 0.5 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201190.ogg"
    xfe "复活了哟！"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201200.ogg"
    xfe "......吓了一大跳。"
    me01 "难道是因为太烫了？"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/000201210.ogg"
    xfe "嗯......和雪完全不一样。"
    me01 "毕竟是年糕嘛。"
    "似乎不能再让她吃了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    play sound jiaobu
    pause 2.0 hard
    hide snow_level1
    scene set only xfe_cg memory1
    with dissolve
    pause 1.0 hard
    "今天我们的活动依旧是在雪中散步。"
    "在那条雪道上留下崭新的足迹。"
    "希菲尔说她是不能被其他人找到的。"
    "所以我们特地选择了在人烟稀少的钟楼附近见面。"
    "而这里也就真正成为了属于我们两人玩耍的秘密场所。"
    pause 1.0 hard
    scene set only balltower snow day xuejian alpha
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve    
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    me01 "找到你了，希菲尔。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201220.ogg"
    xfe "被找到了~"
    "我们最常玩的游戏就是躲猫猫。"
    "虽然钟楼广场没有什么适合躲藏的地方，但是我每一次都需要花上一番功夫才能找到她。"
    "那雪白的身影，就仿佛就与雪融为了一体。"
    "每次找到她的时候，对方脸上总是挂满了灿烂的笑容。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201230.ogg"
    xfe "凉君，没有找到人家......"
    "相反如果一直没找到她的话，希菲尔就会一边哭一边跑到我的跟前。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "那时的我，也许就是在不知不觉中被这份笑容所拯救了也说不定。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg normal
    with dissolve
    pause 1.0 hard
    "想要一直这样看着她。"
    "只要有她这一个朋友就够了。"
    pause 0.1 hard
    scene set only xfe_cg happy
    $ flcam.move(1100, -1400, 450, duration=3.0, warper='ease_quad')
    with dissolve
    pause 1.5 hard
    "我始终坚信与希菲尔在一起的时候是与寂寞无缘的。"
    "或许正是因为在我的内心深处，一直渴望着有人能够真正走进我的世界——"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day204
