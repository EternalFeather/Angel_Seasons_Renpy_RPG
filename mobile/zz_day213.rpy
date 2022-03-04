label day213:
    bookmark
    $ save_name = _("Day 213")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date211 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    scene set only sky day xuejian2
    show snow_level1 onlayer fg
    with slowdissolve
    pause 3.0 hard
    hide snow_level1
    scene set only home day lhx_room xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    play music second_108 fadein 3.0 if_changed
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300010.ogg"
    lhx "为什么世界上会有这种季节呢？"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031300020.ogg"
    lhx "冬天什么的还是死掉比较好。"
    hide lhx_dsf_b2
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    scene set only lhx_cg bed1
    with slowdissolve
    pause 1.0 hard
    show rxl_dzf_b2 b2 b2_sp1 onlayer screens at side_right('rxl', 0.90), basicfade
    play voice "voice/日向怜/121300010.ogg"
    rxl "嘴上这么说，看起来挺幸福的啊。"
    hide rxl_dzf_b2
    play voice "voice/立花希/031300030.ogg"
    lhx "被炉这一发明是唯一的救赎。"
    show rxl_dzf_b1 b1 b1_n3 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300020.ogg"
    rxl "毕竟决定要住公寓的时候，就事先准备好这个了。"
    play voice "voice/日向怜/121300030.ogg"
    show rxl_dzf_b1 b1 b1_s1
    rxl "但是立花你就是在这里出生的吧？为什么还会这么怕冷啊？"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300050.ogg"
    lhx "你在说什么蠢话。倒不如说这才让我充分理解了寒冷的恐怖。"
    play voice "voice/立花希/031300060.ogg"
    lhx "那种冰凉和冷漠的感觉一定是用来杀人的，就算说成是杀戮兵器也不为过。"
    show rxl_dzf_b2 b2 b2_ga1 onlayer screens at side_right('rxl', 0.90), basicfade
    play voice "voice/日向怜/121300040.ogg"
    rxl "虽然知道你怕冷，但要维持这样子到什么时候？"
    hide rxl_dzf_b2
    play voice "voice/立花希/031300070.ogg"
    lhx "直到冬天从这个世界上消失为止。"
    show rxl_dzf_b1 b1 b1_ga1 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300050.ogg"
    rxl "差不多要中午了啊。"
    hide rxl_dzf_b1
    pause 0.1 hard
    play sound yangmu
    scene set only lhx_cg bed2
    with dissolve
    play voice "voice/立花希/031300080.ogg"
    lhx "暖呼呼~"
    show rxl_dzf_b2 b2 b2_s1 onlayer screens at side_right('rxl', 0.90), basicfade
    play voice "voice/日向怜/121300060.ogg"
    rxl "我肚子饿了......"
    hide rxl_dzf_b2
    play voice "voice/立花希/031300090.ogg"
    lhx "暖呼呼~"
    show rxl_dzf_b1 b1 b1_n3 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300070.ogg"
    rxl "立花，我们去买东西吧？"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300100.ogg"
    lhx "暖呼呼~"
    show rxl_dzf_b1 b1 b1_h1 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300080.ogg"
    rxl "在店里吃也可以~"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300110.ogg"
    lhx "暖呼呼~"
    play sound jump_1
    with vpunch
    show rxl_dzf_b2 b2 b2_h1 onlayer screens at side_right('rxl', 0.90), basicfade
    play voice "voice/日向怜/121300090.ogg"
    rxl "好了，走吧~"
    hide rxl_dzf_b2
    pause 1.0 hard
    scene set only home day lhx_room xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 1.0 hard
    play sound touch
    show lhx_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 1.04
        parallel:
            linear 1.0 ypos 1.0
        parallel:
            linear 1.0 alpha 1.0
    pause 1.5 hard
    play voice "voice/立花希/031300120.ogg"
    lhx "请不要拉我。"
    play voice "voice/立花希/031300130.ogg"
    lhx "好冷。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121300100.ogg"
    rxl "今天是{encyclopedia=dhr}大晦日{/encyclopedia}，还得买年越荞麦面才行。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300140.ogg"
    lhx "请你一个人去买吧。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121300110.ogg"
    rxl "不是两个人的话吃东西好无聊的嘛~"
    show lhx_dsf_b3 b3 b3_ga1
    play voice "voice/立花希/031300150.ogg"
    lhx "那就拜托你顺便连同我的份也一起买回来吧。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121300120.ogg"
    rxl "一个人去买东西也很无聊啊。"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300160.ogg"
    lhx "你是叫我去死吗？"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show rxl_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121300130.ogg"
    rxl "行了快走了啦~"
    show lhx_dsf_b1 b1 b1_s3
    play voice "voice/立花希/031300170.ogg"
    lhx "这是在叫我自我了断吗？"
    show rxl_dzf_b1 b1 b1_ga1
    play voice "voice/日向怜/121300140.ogg"
    rxl "有工作的时候还不是能正常地出门吗？"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300180.ogg"
    lhx "那是我每天早上抱着必死的觉悟。"
    show rxl_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/日向怜/121300150.ogg"
    rxl "那现在也抱着那样的觉悟出门吧！"
    hide lhx_dsf_b3 with None
    pause 0.1 hard
    show lhx_dsf_b2 b2 b2_s3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031300190.ogg"
    lhx "请不要拉我......"
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    play sound open_door4
    pause 0.5 hard

label day213.neightbor_event01:
    $ flcam.move(0, 0, 0)
    scene set only home day neighbor xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 1.0 hard
    show lhx_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300200.ogg"
    lhx "这寒冷可是能杀人的。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show rxl_dzf_b2 b2 b2_h1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/日向怜/121300160.ogg"
    rxl "毕竟下着雪呢~"
    show lhx_dsf_b2 b2 b2_s2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031300210.ogg"
    lhx "好想念被炉......"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121300170.ogg"
    rxl "别说这种话了，走着走着就暖和了。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300220.ogg"
    lhx "先不要着急，等我锁上门。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "由于需要采购的商品有点杂乱，两人最终决定分头行动。"
    "立花希负责去商店街购买食材，而日向怜则去神社购买拜年用的香火。"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    play music second_124 fadein 3.0 if_changed
    pause 1.0 hard
    show lhx_dsf_b1 b1 b1_s2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031304720.ogg"
    lhx "......"
    play voice "voice/立花希/031304730.ogg"
    lhx "为什么我会在这里......"
    "这并不是必经之路，和预定的路线不一样。"
    "却又不知为何下意识地还是来到了这里。"
    hide lhx_dsf_b1
    $ flcam.move(0, 0, 0, duration=2.0, warper='ease_cubic')
    pause 2.0 hard
    "立花希拿出了口袋里的钥匙。"
    "那是从她记事的时候就一直带在身上的重要之物。"
    pause 1.0 hard
    hide snow_level1
    scene set only items key
    with slowdissolve
    pause 1.0 hard
    "打开潘多拉魔盒的钥匙——"
    "没有人知道其中埋藏着的是什么样的秘密。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    show lhx_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031304750.ogg"
    lhx "到底......为什么会被选中呢？"
    show lhx_dsf_b2 b2 b2_s1
    play voice "voice/立花希/031304760.ogg"
    lhx "当时许愿的人现在又去了哪里呢。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001300020.ogg"
    stranger "她去了很远的地方哟~"
    show lhx_dsf_b2 b2 b2_sp1 onlayer screens at side_left('lhx'), basicfade
    play voice "voice/立花希/031304770.ogg"
    lhx "......"
    hide lhx_dsf_b2
    play voice "voice/希菲尔/001300030.ogg"
    stranger "就像我和凉君分别的时候一样。"
    play voice "voice/希菲尔/001300040.ogg"
    stranger "你也......在这里和凉君分开了。"
    play voice "voice/希菲尔/001300050.ogg"
    stranger "记忆中的大家......都被迫接受了离别。"
    pause 1.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    hide snow_level1
    pause 5.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg normal
    with slowerdissolve
    play music second_103 fadein 3.0 if_changed
    pause 1.0 hard
    show lhx_dsf_b2 b2 b2_sp1 onlayer screens at side_left('lhx'), basicfade
    play voice "voice/立花希/031304780.ogg"
    lhx "你是......"
    hide lhx_dsf_b2
    play voice "voice/希菲尔/001300060.ogg"
    xfe "已经不是初次见面了呢。"
    show lhx_dsf_b2 b2 b2_s4 onlayer screens at side_left('lhx'), basicfade
    play voice "voice/立花希/031304790.ogg"
    lhx "的确如此......我们之前见过的。"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/031304800.ogg"
    lhx "只是当时还不知道你的名字。"
    hide lhx_dsf_b2
    play voice "voice/希菲尔/001300070.ogg"
    xfe "希菲尔我，就叫希菲尔哟~"
    play voice "voice/希菲尔/001300090.ogg"
    xfe "用“我”称呼的希菲尔，和用“希菲尔“称呼的希菲尔，虽然很像却是不同的。"
    show lhx_dsf_b2 b2 b2_sp1 onlayer screens at side_left('lhx'), basicfade
    play voice "voice/立花希/031304820.ogg"
    lhx "......"
    hide lhx_dsf_b2
    pause 0.1 hard
    scene set only xfe_cg daze
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001300100.ogg"
    xfe "这是连凉君都还不知道的事情。"
    show lhx_dsf_b1 b1 b1_sp1 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031304830.ogg"
    lhx "......难道是双胞胎吗？"
    hide lhx_dsf_b1
    play voice "voice/希菲尔/001300110.ogg"
    xfe "双胞胎？"
    show lhx_dsf_b2 b2 b2_n1 onlayer screens at side_left('lhx'), basicfade
    play voice "voice/立花希/031304840.ogg"
    lhx "你有姐姐或者妹妹吗？"
    hide lhx_dsf_b2
    pause 0.1 hard
    scene set only xfe_cg sad
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001300120.ogg"
    xfe "......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with slowdissolve
    pause 1.0 hard
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031304850.ogg"
    lhx "我还得谢谢你。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/希菲尔/001300130.ogg"
    xfe "......道谢？"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031304860.ogg"
    lhx "是的，谢谢你能和我说这些。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with dissolve
    pause 2.0 hard
    scene set only balltower snow day xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300140.ogg"
    xfe "现在只有两人。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031304870.ogg"
    lhx "......"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg daze
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001300150.ogg"
    xfe "在这颗星球上能够成为我朋友的......只有两个人。"
    pause 0.1 hard
    scene set only xfe_cg normal
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001300160.ogg"
    xfe "能和身为“妖精”的我和睦相处的人，也只有你们两个而已......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowdissolve
    pause 1.0 hard
    "眼前的女孩究竟是谁？"
    "这种熟悉的感觉......究竟是什么？"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/希菲尔/001300170.ogg"
    xfe "现在这里已经交不到朋友了。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001300180.ogg"
    xfe "想要交朋友的话......也只能用其他的办法了。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300190.ogg"
    xfe "凉君也交到了新的朋友。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300200.ogg"
    xfe "所以我也......"
    show ts_xfe_yjz_b1 b1 b1_s3
    play voice "voice/希菲尔/001300210.ogg"
    xfe "希菲尔也......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_s2 onlayer m1:
        xpos 0.3
    play voice "voice/立花希/031304920.ogg"
    lhx "......"
    $ flcam.move(-1250, 0, 900, duration=1.5)
    show lhx_dsf_b2 b2 b2_n1:
        xpos 0.3
        linear 1.0 xpos 0.4
    play sound touch
    pause 1.0 hard
    "立花希上前摸了摸希菲尔的头。"
    show ts_xfe_yjz_b1 b1 b1_sp1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001300220.ogg"
    xfe "啊......"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300230.ogg"
    xfe "不、不行。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_sp1:
        xpos 0.4
        linear 0.5 xpos 0.3
    play sound jump_1
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_ga4 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    show han onlayer m2:
        xalign 0.495 yalign 0.4
    play voice "voice/希菲尔/001300240.ogg"
    xfe "不、不要随便摸希菲尔！"
    pause 0.5 hard
    hide han
    play sound appear
    show ts_xfe_yjz_b3 b3 b3_ga4 at walkout_r(0.5)
    pause 1.0 hard
    hide ts_xfe_yjz_b3
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with dissolve
    pause 1.0 hard
    "希菲尔转身跑开。"
    play sound hite_light
    with vpunch
    "噗通。"
    "可是却在逃跑途中摔了一跤。"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    play sound appear
    show ts_xfe_yjz_b3 b3 b3_ga4 onlayer m2 at flu_down(0.15, 20, 2):
        xpos 0.5
    play voice "voice/希菲尔/001300250.ogg"
    xfe "呜啊啊啊，希菲尔的鼻子！"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b3 b3 b3_sp2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031304930.ogg"
    lhx "你没事吧？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_c1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001300260.ogg"
    xfe "一点也不痛......呜呜。"
    show lhx_dsf_b3 b3 b3_ga3
    play voice "voice/立花希/031304940.ogg"
    lhx "意外地笨拙呢。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300270.ogg"
    xfe "希菲尔我才不笨拙！"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031304950.ogg"
    lhx "明明在什么都没有的平地上也能跌倒。"
    show ts_xfe_yjz_b1 b1 b1_a2
    play voice "voice/希菲尔/001300280.ogg"
    xfe "正因为什么都没有才会跌倒的。"
    show lhx_dsf_b2 b2 b2_sp1
    play voice "voice/立花希/031304960.ogg"
    lhx "不明白你的意思......"
    hide lhx_dsf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300290.ogg"
    xfe "没有积雪的话是很难走的。"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    play sound xiaoshi_1
    "说完，希菲尔的身影从立花希的面前消失了。"
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    show lhx_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.3
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031304970.ogg"
    lhx "真是个不可思议的女孩......"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day213'
    $ seen_day213_neightbor_event02 = False

label day213.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day213':
        show set maps winter evening
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day213.neightbor_event02':
        show set maps winter night
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['road2'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        road2=("day213.street_event01", "not seen_day213_neightbor_event02"),
        shenshe=("day213.shenshe_event01", "seen_day213_neightbor_event02"))
    $ window_animate_outro()
    if _return == 'day213.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day213.shenshe_event01':
        $ flcam.move(*overworld.camera_positions['shenshe'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day213.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street day city3 xuejian
    show snow_level1 onlayer fg
    play music second_118 fadein 3.0 if_changed
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_h3 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/日向怜/121300230.ogg"
    rxl "这不是凉君吗？真巧啊~"
    me01 "哟~"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300240.ogg"
    rxl "邂逅了野生的凉君，立花你也该稍微打起点精神了吧。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300310.ogg"
    lhx "我明明一个人能走，可是日向你老是抓着我的袖子不放。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300250.ogg"
    rxl "因为感觉不这样的话你立刻就会逃走嘛~"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300320.ogg"
    lhx "不是我的错，都是这冬天不好。"
    me01 "立花老师很怕冷吗？"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300260.ogg"
    rxl "凉君你也明白的吧，立花在冬天就是一只特别需要别人照顾的宠物~"
    me01 "是这样吗......"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b2 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031300330.ogg"
    lhx "日向......开玩笑也差不多行了。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300270.ogg"
    rxl "嗯，多亏了有凉君在立花也不会逃跑了吧。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_ga1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031300340.ogg"
    lhx "为什么会这么想啊？凉君什么的根本无所谓吧。"
    me01 "二位也是来买东西的？"
    show rxl_dzf_b2 b2 b2_h3
    play voice "voice/日向怜/121300280.ogg"
    rxl "嘛，毕竟是年末了嘛~"
    hide rxl_dzf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_n1
    play voice "voice/立花希/031300350.ogg"
    lhx "顺便打算找个地方吃晚饭，你那边呢？"
    me01 "我姑且算是吃过了。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300360.ogg"
    lhx "叛徒......"
    me01 "为什么啊？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_c1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300290.ogg"
    rxl "好饿啊~"
    show lhx_dsf_b2 b2 b2_s1
    play voice "voice/立花希/031300370.ogg"
    lhx "我没怎么觉得......"
    show rxl_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/日向怜/121300300.ogg"
    rxl "立花是低能耗的呢，身高和胸部。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300380.ogg"
    lhx "我只是还在发育而已......明年两边都会长一倍左右。"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300390.ogg"
    lhx "凉君是在家里吃的吧。"
    me01 "是啊，翔子做的。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300400.ogg"
    lhx "真是幸福啊。只管睡觉饭就自动做好了。"
    show rxl_dzf_b1 b1 b1_h1
    play voice "voice/日向怜/121300310.ogg"
    rxl "立花也是到刚才为止都躺在被炉里来着。"
    me01 "我也不是什么都没干，这不现在也帮忙出来买东西。"
    hide rxl_dzf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300410.ogg"
    lhx "青木同学和爱衣她们也一起来了吗？"
    me01 "不，她们在家里大扫除。"
    show lhx_dsf_b2 b2 b2_ga3
    play voice "voice/立花希/031300420.ogg"
    lhx "......碍手碍脚的凉君被赶出来了啊。"
    me01 "才不是，不过现在确实是在为今晚要住哪里而烦恼。"
    show lhx_dsf_b2 b2 b2_sp1
    play voice "voice/立花希/031300430.ogg"
    lhx "真的被赶出来了吗？"
    me01 "嘛......今天翔子的父母突然说要回来，我在那里也不方便。"
    "虽然翔子说了没关系，但是我还是以朋友聚会的借口推辞了。"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/031300440.ogg"
    lhx "凉君你其实是不想打扰青木家的团聚吧~"
    me01 "不愧是立花老师。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300330.ogg"
    rxl "是担心家里容不下外人吗？"
    me01 "当然不是，我只是希望他们能有更多的时间单独相处而已。"
    "比起说我，自己的妹妹也该好好照顾下吧！"
    "虽然想这么吐槽，但是可能让爱衣留在翔子身边或许才是最好的选择。"
    "至少要保证她能过个好年......"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300450.ogg"
    lhx "这个提案是凉君决定的？"
    me01 "算是吧。"
    hide rxl_dzf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031300460.ogg"
    lhx "这点担忧对于青木家和爱衣来说也许是多余的......"
    me01 "是这样吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300470.ogg"
    lhx "就是这样。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_h1
    play voice "voice/立花希/031300480.ogg"
    lhx "我在幼儿园看到爱衣很仰慕凉君你，所以我能这么确信。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300510.ogg"
    lhx "所以我觉得凉君应该也没有介意的必要。"
    me01 "嘛，总之既然事情都决定了，就这样吧。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300530.ogg"
    lhx "凉君你果然变了啊......（小声）"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300370.ogg"
    rxl "那么凉君你正月期间打算怎么办？"
    me01 "所以正在为这个烦恼。"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300540.ogg"
    lhx "我觉得你露宿街头就好了。"
    me01 "......不得不说这也许是最坏的打算了。"
    play sound ganga01
    show rxl_dzf_b1 b1 b1_sp2
    play voice "voice/日向怜/121300380.ogg"
    rxl "不......这样真的好吗？"
    me01 "随意在路边找个地方睡好了。"
    stop music fadeout 5.0
    show rxl_dzf_b1 b1 b1_sp2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/日向怜/121300390.ogg"
    rxl "这样会和凉君永别的！"
    me01 "那在钟楼广场睡好了。"
    play voice "voice/日向怜/121300400.ogg"
    rxl "我觉得结果是一样的。"
    me01 "啊、啊哈哈，总之我先去看看还有没有可以借宿的地方了。"
    hide rxl_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    play music second_108 fadein 3.0 if_changed
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_ga2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/031300560.ogg"
    lhx "别开玩叫了！（咬舌）"
    me01 "为什么会在这时候咬到舌头啊。"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031300570.ogg"
    lhx "为什么就没有其他选择了？"
    me01 "你有更好的建议？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300410.ogg"
    rxl "立花的意思是，如果无处可去的话就来我们的公寓吧。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300580.ogg"
    lhx "既然日向都这么说的话也没办法，就含泪让凉君住在我们公寓吧。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300420.ogg"
    rxl "虽然很傲娇但是这样也不错啊。"
    me01 "这样真的好吗？"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300590.ogg"
    lhx "只要凉君不弄出什么差错就好了。"
    me01 "这点担心倒是挺多余的。"
    hide rxl_dzf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_a1
    play voice "voice/立花希/031300600.ogg"
    lhx "为什么会多余啊！"
    me01 "莫非你在期待些什么？"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031300610.ogg"
    lhx "凉君什么的被冻死在街上就好了......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.3
    play sound yangmu
    show yangmu onlayer m2:
        xalign 0.23 yalign 0.43
    play voice "voice/日向怜/121300430.ogg"
    rxl "如果正月和立花独处的话，说不定就会发生新年的第一次了~"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031300620.ogg"
    lhx "为了避免贞操受到威胁，还请凉君务必来我们这里阻止她。"
    me01 "感觉面对你们两个人我已经无力吐槽了，总之打扰了。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day213.neightbor_event02:
    $ flcam.move(0, 0, 0)
    scene set only home evening neighbor xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    play sound open_door4
    pause 2.0 hard
    hide snow_level1
    scene set only home night lhx_room xuejian
    with dissolve
    play music second_112 fadein 3.0 if_changed
    pause 2.0 hard
    scene set only lhx_cg bed3
    with dissolve
    pause 1.0 hard
    show rxl_dzf_b2 b2 b2_h1 onlayer screens at side_right('rxl', 0.90), basicfade
    play voice "voice/日向怜/121300440.ogg"
    rxl "这荞麦面真好吃啊~"
    hide rxl_dzf_b2
    me01 "没想到你们两个人都会做料理。"
    play voice "voice/立花希/031300630.ogg"
    lhx "荞麦面这种程度再怎么样还是会做的。"
    show rxl_dzf_b1 b1 b1_n3 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300450.ogg"
    rxl "早饭的烤土司也很简单。"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300640.ogg"
    lhx "早饭什么的有吃过吗？"
    show rxl_dzf_b1 b1 b1_h3 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300460.ogg"
    rxl "虽然立花你每次都睡迷糊了，但还是有吃的。"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300650.ogg"
    lhx "没有记忆。"
    me01 "立花老师在早上真的没什么状态啊。"
    play voice "voice/立花希/031300660.ogg"
    lhx "比起这个，青木家那边怎么样了？"
    me01 "我打过电话了，翔子的父母还有铃音大家都在，看来挺热闹的样子。"
    me01 "据说是要一直待到正月初三左右。"
    play voice "voice/立花希/031300670.ogg"
    lhx "......"
    pause 1.0 hard
    scene set only home night lhx_room xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300480.ogg"
    rxl "这不是挺好的吗立花，凉君似乎也会暂时住在我们这里哟~"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031300680.ogg"
    lhx "真是麻烦啊。"
    me01 "如果打扰的话我明天就去找找看附近有没有其他旅馆之类的。"
    hide lhx_dsf_b2 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_a1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/立花希/031300690.ogg"
    lhx "别开玩叫了。（咬舌）"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300490.ogg"
    rxl "立花在动摇的时候就会咬到舌头呢~"
    hide rxl_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031300700.ogg"
    lhx "才没有这种事......我一直是很冷静的。"
    "傲娇和爱逞强这些特点已经很明显了。"
    "不得不说这些和雷亚还真是一模一样。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "不过是从什么时候开始的？"
    "从什么时候开始有这样的感觉呢？"
    "从立花老师的身上总能看到雷亚的影子。"
    pause 1.0 hard
    scene set only home night lhx_room xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300500.ogg"
    rxl "凉君，在完事之前就住在这里吧？"
    stop music fadeout 5.0
    me01 "如果你们不嫌弃的话......"
    play music second_104 fadein 3.0 if_changed
    show rxl_dzf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121300510.ogg"
    rxl "真是好色啊~"
    me01 "完全不明白你在说什么。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300520.ogg"
    rxl "毕竟立花也希望你住下来。"
    me01 "是这样吗？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg bed4
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031300710.ogg"
    lhx "暖呼呼~"
    show rxl_dzf_b1 b1 b1_sp2 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300530.ogg"
    rxl "默默地捂着暖。"
    hide rxl_dzf_b1
    me01 "看起来很幸福的样子。"
    play voice "voice/立花希/031300720.ogg"
    lhx "我现在还因为某人的错在生气呢。"
    play sound ganga01
    show rxl_dzf_b1 b1 b1_ga1 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300540.ogg"
    rxl "凉君，不道歉可不行啊。"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300730.ogg"
    lhx "尽说这些蠢话，该道歉的是日向你啦。"
    show rxl_dzf_b1 b1 b1_sp1 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300550.ogg"
    rxl "是说我碍事了？"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300740.ogg"
    lhx "的确碍事。"
    show rxl_dzf_b1 b1 b1_c1 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300560.ogg"
    rxl "呜呜，新年的第一次......"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300750.ogg"
    lhx "不明白你的意思。"
    show rxl_dzf_b1 b1 b1_h2 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300570.ogg"
    rxl "真的？"
    hide rxl_dzf_b1
    pause 1.0 hard
    scene set only home night lhx_room xuejian
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031300760.ogg"
    lhx "不......虽然知道你在想什么，但是不需要说明。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300580.ogg"
    rxl "就这么想和凉君单独相处啊？"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031300770.ogg"
    lhx "已经说过了不要再胡乱猜测了！"
    show rxl_dzf_b1 b1 b1_ga1
    play voice "voice/日向怜/121300590.ogg"
    rxl "不否定啊~"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031300780.ogg"
    lhx "我只是懒得反驳你而已。"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031300790.ogg"
    lhx "总之，为了保护我的贞操，凉君必须待在这里。"
    show rxl_dzf_b1 b1 b1_n2
    play voice "voice/日向怜/121300600.ogg"
    rxl "强行联系起来了啊。"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031300800.ogg"
    lhx "只是万不得已的保护措施而已。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300610.ogg"
    rxl "嘛算了，话说凉君你要睡哪？"
    me01 "哪里都行吧，玄关或者走廊我都可以的。"
    show rxl_dzf_b2 b2 b2_ga1
    play voice "voice/日向怜/121300620.ogg"
    rxl "就算只是寄宿......你也不用那样作践自己的。"
    hide rxl_dzf_b2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031300810.ogg"
    lhx "用我的房间也可以的。"
    me01 "等等，这样是不是太快了，我还没有心理准备。"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031300820.ogg"
    lhx "你在说什么啊？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300630.ogg"
    rxl "当然是色情的东西吧~"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031300830.ogg"
    lhx "我会去日向的房间睡。"
    show rxl_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121300640.ogg"
    rxl "从色情的层面上？"
    show lhx_dsf_b1 b1 b1_a1
    play voice "voice/立花希/031300840.ogg"
    lhx "才不是！"
    show rxl_dzf_b1 b1 b1_h3
    play voice "voice/日向怜/121300650.ogg"
    rxl "明明都说了贞操危机什么的，却要来投奔我啊。"
    hide lhx_dsf_b1 
    show lhx_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031300850.ogg"
    lhx "本来从凉君说要住下的时候开始，我不就只能和日向睡同一个房间了吗？"
    play sound jump_1
    show rxl_dzf_b1 b1 b1_sp2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121300660.ogg"
    rxl "也就是说立花的目的是想和我独处吗？"
    show lhx_dsf_b3 b3 b3_a1
    play voice "voice/立花希/031300860.ogg"
    lhx "这是绝对绝对不可能的，如果你敢对我做了什么的话就把你丢到宇宙空间去！"
    show rxl_dzf_b1 b1 b1_h3
    play voice "voice/日向怜/121300670.ogg"
    rxl "这样一来就可以和凉君过二人世界了呢~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg bed4
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031300870.ogg"
    lhx "暖呼呼~"
    show rxl_dzf_b1 b1 b1_ga1 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300680.ogg"
    rxl "每次话锋不对就一副满不在乎的样子去捂暖。"
    hide rxl_dzf_b1
    me01 "虽然你们似乎已经有结论了，不过让我睡立花老师的房间真的可以吗？"
    play voice "voice/立花希/031300880.ogg"
    lhx "是的，床也可以用。"
    me01 "真的吗？"
    play voice "voice/立花希/031300890.ogg"
    lhx "是的，反正又不会睡掉一块。"
    show rxl_dzf_b1 b1 b1_h2 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/121300690.ogg"
    rxl "凉君，不如搜搜看立花的房间吧。"
    hide rxl_dzf_b1
    play voice "voice/立花希/031300900.ogg"
    lhx "我又没藏着什么被搜到会困扰的东西。"
    play sound jing01
    play voice "voice/立花希/031300910.ogg"
    lhx "......说不定有那么一件。"
    play voice "voice/立花希/031300920.ogg"
    lhx "如果是那钥匙的话.....（小声）"
    me01 "钥匙？"
    pause 1.0 hard
    scene set only home night lhx_room xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300700.ogg"
    rxl "说到钥匙我忘了重要的事情。"
    me01 "有什么安排吗？"
    hide rxl_dzf_b2 with None
    pause 0.1 hard
    show rxl_dzf_b1 b1 b1_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/日向怜/121300720.ogg"
    rxl "那还用说吗，当然是大家一起去跨年参拜啊~"
    play sound jump_1
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/立花希/031300940.ogg"
    lhx "别说蠢话了！"
    me01 "为什么说这是蠢话？"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031300950.ogg"
    lhx "是的，为什么非得在这么冷的时间段从被炉里走出来啊？"
    show rxl_dzf_b1 b1 b1_n3
    play voice "voice/日向怜/121300730.ogg"
    rxl "别管怕冷的立花了。凉君，我们去参拜吧~"
    me01 "说的也是，难得这附近就有个神社，正好也可以求个签什么的。"
    show lhx_dsf_b3 b3 b3_a1
    play voice "voice/立花希/031300960.ogg"
    lhx "请不要说些脑子有问题的话。"
    me01 "我倒觉得这是个好主意。"
    hide rxl_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    lhx "......"
    me01 "立花老师不用勉强跟来，就在被炉里等我们回来吧。"
    show lhx_dsf_b1 b1 b1_a1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/立花希/031300980.ogg"
    lhx "别开玩叫了！（咬舌）"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300740.ogg"
    rxl "立花的想法真是好懂~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day213_neightbor_event02:
        $ seen_day213_neightbor_event02 = True
    $ _overworld_label = "day213.neightbor_event02"
    jump day213.map

label day213.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only shenshe night xuejian2
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    play music second_120 fadein 3.0 if_changed
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_s2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031300990.ogg"
    lhx "好冷......"
    me01 "嘛，毕竟是这个时间。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show rxl_dzf_b2 b2 b2_h2 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/日向怜/121300750.ogg"
    rxl "而且还在下雪。"
    show lhx_dsf_b2 b2 b2_s3
    play voice "voice/立花希/031301000.ogg"
    lhx "人多得像垃圾山一样。"
    me01 "真是有趣的比喻......"
    hide lhx_dsf_b2
    hide rxl_dzf_b2
    $ flcam.move(0, 1400, 1100, duration=2.0, warper='ease_cubic')
    pause 2.5 hard
    "神社院内挤满了前来参拜的游客。"
    "平时不怎么热闹的神社在今天这个时间也迎来了另一番的景象。"
    "看来与立花老师不同，还是有不少人选择了出门参拜而不是躲在被炉里。"
    $ flcam.move(4500, -300, 900, duration=1.5, warper='ease_cubic')
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121300760.ogg"
    rxl "毕竟是一年只有一次的活动，不好好享受就浪费了。"
    me01 "日向同学的话果然更适合这种热闹的氛围。"
    show rxl_dzf_b2 b2 b2_h2
    play voice "voice/日向怜/121300770.ogg"
    rxl "不如说热闹的氛围才符合过年嘛~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301010.ogg"
    lhx "这就是你神经大条的证据吧......"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_dzf_b2 with None
    pause 0.1 hard
    show rxl_dzf_b1 b1 b1_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121300780.ogg"
    rxl "粗细和硬度都不如凉君的啊~"
    me01 "不要突然开车啊！"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121300790.ogg"
    rxl "我指的当然是反射神经啦~"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301020.ogg"
    lhx "还以为是黄段子......"
    hide rxl_dzf_b2 with None
    pause 0.1 hard
    show rxl_dzf_b1 b1 b1_a1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/121300820.ogg"
    rxl "如果欲望上头的话，说不定就不冷了呢。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    pause 0.5 hard
    me01 "行了，赶紧去参拜吧。"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301050.ogg"
    lhx "在那之前我想喝点热的东西，手都冻僵了......"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/121300830.ogg"
    rxl "前面似乎有派发免费甜酒的地方。"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301060.ogg"
    lhx "那就快点走吧。"
    hide lhx_dsf_b3
    hide rxl_dzf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 1.0 hard
    show liuli_wnf_b3 b3 b3_h1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/041300010.ogg"
    liuli "请用甜酒~"
    show liuli_wnf_b3 b3 b3_n1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/041300020.ogg"
    liuli "感谢各位在寒冷的夜晚也能来拜访贵社。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show rxl_dzf_b2 b2 b2_h3 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300840.ogg"
    rxl "你就是立花说过的那个活力十足的孩子吧？"
    $ flcam.move(0, 0, 600, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/立花希/031301070.ogg"
    lhx "我倒不记得有提到过那么愉快的孩子来着......"
    me01 "琉璃你是在这里帮忙的吗？"
    show liuli_wnf_b3 b3 b3_h1
    play voice "voice/琉璃/041300030.ogg"
    liuli "是的，感谢前辈遵守了约定~"
    me01 "毕竟之前也说过要来初诣的。"
    show lhx_dsf_b2 b2 b2_h2
    play voice "voice/立花希/031301080.ogg"
    lhx "我也好好遵守约定了~"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h3 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/121300850.ogg"
    rxl "明明刚刚死活都不肯出门的。"
    hide rxl_dzf_b1
    hide liuli_wnf_b3
    hide lhx_dsf_b2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/藤原瞳/131300010.ogg"
    tyt "喝完甜酒后别忘了去参拜，还有购买绘马和护身符。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131300020.ogg"
    tyt "如果只看不买的话，我就要考虑收甜酒的费用了。"
    me01 "不是说好免费的吗？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131300030.ogg"
    tyt "这是提高收入的诱饵。"
    me01 "真是个暴利的神社啊。"
    show tyt_wnf_b1 b1 b1_s3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/藤原瞳/131300040.ogg"
    tyt "好冷、好想睡......好想冬眠。"
    pause 1.0 hard
    play sound jiaobu2
    show tyt_wnf_b1 b1 b1_s3 at walkout_r(0.3)
    pause 1.0 hard
    hide tyt_wnf_b1
    me01 "还是搞不懂这家伙......"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_wnf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041300040.ogg"
    liuli "最近藤原同学因为布置会场的事情一直很忙，应该是累了吧。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_n5 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031301090.ogg"
    lhx "毕竟这么冷，想要冬眠的心情我完全可以理解。"
    me01 "那就趁现在喝完甜酒身子暖和的时候赶紧去参拜吧。"
    hide lhx_dsf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_wnf_b3 b3 b3_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/琉璃/041300050.ogg"
    liuli "请慢走~"
    hide liuli_wnf_b3
    show liuli_wnf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041300060.ogg"
    liuli "今年承蒙关照了，非常感谢各位能够成为我的朋友。"
    me01 "新的一年也请多多指教~"
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day213.shenshe_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    show snow_level1 onlayer fg
    with dissolve
    pause 2.0 hard
    scene set only shenshe night xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    me01 "话说日向同学呢？"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301150.ogg"
    lhx "我想故意走散应该是日向怜的恶作剧吧，毕竟这是她的恶趣味。"
    me01 "恶作剧？也包括贞操危机吗？"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301160.ogg"
    lhx "......"
    me01 "立花老师？"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301170.ogg"
    lhx "......凉君你要在我们这里住到初三对吧？"
    me01 "有什么问题吗？"
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031301180.ogg"
    lhx "请不要对我做下流的事......"
    me01 "你想多了。"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301190.ogg"
    lhx "你真正的目的到底是什么？"
    me01 "你的贞操？"
    show lhx_dsf_b3 b3 b3_ga2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031301200.ogg"
    lhx "......"
    me01 "抱歉，我是开玩笑的。"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301210.ogg"
    lhx "这种事我当然知道......"
    hide lhx_dsf_b1
    $ flcam.move(0, 0, 1300, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    play ambience1 new_year
    "就在我们聊天的过程中，新年的钟声悄然而至。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    stop ambience1 fadeout 5.0
    show lhx_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301220.ogg"
    lhx "凉君，新年快乐~"
    me01 "今年也请多多关照，立花老师。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301230.ogg"
    lhx "好的，希望来年也能被更多地关照。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_h1
    play voice "voice/立花希/031301240.ogg"
    lhx "毕竟我们是一心同体的搭档嘛~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day214
