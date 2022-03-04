
label day227:
    bookmark
    $ save_name = _("Day 227")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date226 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only home snow day outside xuejian
    play music second_114 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/希菲尔/001005410.ogg"
    xfe "凉君，今天不用去学校吗？"
    me01 "今天是休息日，希菲尔有什么安排？"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001005420.ogg"
    xfe "叭咕叭咕巡回哟~"
    me01 "也就是出去玩对吧。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005430.ogg"
    xfe "就是这样的。要是在路上遇到有困难的人就去帮助他们。"
    me01 "那我今天的工作就是陪着希菲尔一起出门。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/001005440.ogg"
    xfe "嗯~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard
    $ _overworld_label = 'day227'
    $ seen_day227_balltower_event01 = False
    $ seen_day227_home_event01 = False

label day227.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day227':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day227.balltower_event01':
        show set maps winter evening
        $ flcam.move(*overworld.camera_positions['cloqks'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        cloqks=("day227.balltower_event01", "not seen_day227_balltower_event01"),
        road1=("day227.home_event01", "seen_day227_balltower_event01 and not seen_day227_home_event01"))
    $ window_animate_outro()
    if _return == 'day227.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day227.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day227.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian2
    play music second_134 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    "我们最初的邂逅，就是从这座钟楼广场开始的。"
    "那一日我与希菲尔相遇了。"
    "在这纯白的季节里，遇见了同样纯白的她。"
    pause 1.0 hard
    scene set only balltower snow day big2
    with dissolve
    pause 1.0 hard
    "随之而来的，我们的故事也就此拉开了序幕——"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only ycxt_cg two
    with dissolve
    pause 1.0 hard
    "在神社的风暴中拯救了迷路的小桃。"
    pause 2.0 hard
    scene set only yj_cg rune1
    with dissolve
    pause 1.0 hard
    "在城区的河滩下安慰灵力暴走的友加。"
    pause 2.0 hard
    scene set only lingyin_cg final one
    with dissolve
    pause 1.0 hard
    "在翔子的帮助下从铃音手中救下了雷亚。"
    pause 2.0 hard
    scene set only lhx_cg fight1
    with dissolve
    pause 1.0 hard
    "接受了立花希所谓的“恋爱战争”。"
    pause 2.0 hard
    scene set only szl_cg fight dzf5
    with dissolve
    pause 1.0 hard
    "以及接受了水之濑那不计其数的“比试”。"
    pause 2.0 hard
    scene set only liuli_cg fight angry1
    with dissolve
    pause 1.0 hard
    "成功为花山院琉璃排除了迷茫，与她一同踏上前往宇宙之旅。"
    pause 2.0 hard
    scene set only lisite_cg normal
    with dissolve
    pause 1.0 hard
    "最后还找回了曾经不惜牺牲自己，拯救了翔子、拯救了梦的死神雷亚。"
    pause 2.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "在这里，在这座雪见市，我收获了人生中最为珍贵的几个瞬间。"
    "也收获了新的羁绊。"
    "而这一切的背后，都是因为有希菲尔默默地支持着我。"
    "就是这样一位洁白无瑕、天真可爱的冬之妖精。"
    "在我最孤独的时候来到了我的身边，让我有了勇气去面对未来将要发生的一切。"
    "也许正是她的出现，从八年前开始就已经改变了我的一生。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory4
    with dissolve
    pause 1.0 hard
    "或许如今的这一切早已不同。"
    "亦或许曾经的那点滴从未改变。"
    "在这样扑朔迷离却又充满美好幻想的季节里我们并肩前行，身后留下的是两行清晰的足迹。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    scene set only balltower snow evening xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005450.ogg"
    xfe "不知不觉走着天就黑了。"
    me01 "今天的一切都很和平真是太好了。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001005460.ogg"
    xfe "太好了呢~"
    "一股香味飘来。"
    "是商贩们在广场不远处摆起了摊位。"
    show ts_xfe_yjz_b2 b2 b2_sp3
    me01 "希菲尔吃过拉面吗？"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001005470.ogg"
    xfe "没有的。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp1
    me01 "稍微吃吃看如何？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005480.ogg"
    xfe "凉君肚子饿了吗？"
    me01 "有一点，希菲尔呢？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005490.ogg"
    xfe "希菲尔不太明白“饥饿”是什么感觉。"
    me01 "换句话说也不是不能吃对吧？"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h4 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001005500.ogg"
    xfe "当然了，叭咕叭咕~"
    me01 "那就一起去吧。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005510.ogg"
    xfe "但是已经是傍晚了，大家还在家里等着凉君吃晚饭的。"
    me01 "翔子做的料理很好吃，所以稍微吃点其他东西也不会影响。"
    me01 "而且算上希菲尔的话，份量也刚刚好。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005530.ogg"
    xfe "既然这样的话，那就奉陪了。"
    me01 "知道什么是拉面吗？"
    hide ts_xfe_yjz_b3 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_a1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001005540.ogg"
    xfe "可不要小瞧了希菲尔。之前在这座城市巡游的时候，吃的东西也是调查过的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 1.0 hard
    "就这样我们来到店铺前，点了一碗热气腾腾的拉面。"
    pause 1.0 hard
    scene set only xfe_cg noodles one
    with slowdissolve
    pause 1.0 hard
    me01 "希菲尔，你先请吧。"
    "我将送上来的拉面摆在了希菲尔面前。"
    "对方则是用生疏的手势拿着筷子盯了好久。"
    play voice "voice/希菲尔/001005550.ogg"
    xfe "冒、冒着热气的说......"
    play voice "voice/希菲尔/001005560.ogg"
    xfe "看起来......超级烫的样子。"
    "希菲尔小心地把脸凑了上去，吸了一小口汤汁。"
    pause 0.1 hard
    scene set only xfe_cg noodles two
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005570.ogg"
    xfe "呼啊......"
    play voice "voice/希菲尔/001005580.ogg"
    xfe "呼诶呀啊啊......"
    "接触到食物的一刻，希菲尔全身都变得软趴趴的。"
    me01 "不、不要紧吧？！"
    "我下意识捡起地上的积雪递给了她。"
    "希菲尔叭咕叭咕地将它们吞下。"
    pause 0.1 hard
    scene set only xfe_cg noodles three
    with dissolve
    play voice "voice/希菲尔/001005590.ogg"
    xfe "复活了哟~"
    pause 0.1 hard
    scene set only xfe_cg noodles four
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005600.ogg"
    xfe "呜呜......吓了一跳。"
    me01 "很怕烫吗？"
    play voice "voice/希菲尔/001005610.ogg"
    xfe "才不是烫这么简单，希菲尔觉得自己刚才差一点就蒸发掉了。"
    play voice "voice/希菲尔/001005620.ogg"
    xfe "剩下的就交给凉君了。"
    me01 "怎么说呢，抱歉。"
    pause 0.1 hard
    scene set only xfe_cg noodles three
    with dissolve
    play voice "voice/希菲尔/001005630.ogg"
    xfe "别这么说，味道还是非常好吃的哟~"
    play voice "voice/希菲尔/001005631.ogg"
    xfe "所以呢，凉君。"
    "希菲尔用筷子夹起碗里的面条递到了我嘴边。"
    pause 0.1 hard
    scene set only xfe_cg noodles five
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005632.ogg"
    xfe "啊~"
    play voice "voice/希菲尔/001005633.ogg"
    xfe "千冬有告诉我像这样喂别人吃东西的方法。"
    me01 "可是希菲尔除了雪好像就没看你吃过其他的东西了。"
    pause 0.1 hard
    scene set only xfe_cg noodles three
    with dissolve
    play voice "voice/希菲尔/001005635.ogg"
    xfe "没有的事，很好吃的东西也会去吃的哟~"
    pause 0.1 hard
    scene set only xfe_cg noodles one
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005636.ogg"
    xfe "啊......掉下来了。"
    "筷子夹着的面条因为那生疏的手法而滑落到汤里。"
    pause 0.1 hard
    scene set only xfe_cg noodles four
    with dissolve
    play voice "voice/希菲尔/001005637.ogg"
    xfe "再来一次。"
    "明明不太习惯用筷子，希菲尔却还是坚持要继续喂我。"
    pause 0.1 hard
    scene set only xfe_cg noodles five
    with dissolve
    play voice "voice/希菲尔/001005638.ogg"
    xfe "好吃的东西剩下的话就会很浪费，所以希望凉君能把它们全部都吃掉。"
    play voice "voice/希菲尔/001005639.ogg"
    xfe "可是连希菲尔的份都吃掉的话，晚饭就......"
    me01 "一碗拉面而已小事一桩。"
    play voice "voice/希菲尔/001005641.ogg"
    xfe "不愧是男孩子~"
    pause 0.1 hard
    scene set only xfe_cg noodles three
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005642.ogg"
    xfe "凉君，啊~"
    me01 "的确很烫。"
    pause 0.1 hard
    scene set only xfe_cg noodles one
    with dissolve
    play voice "voice/希菲尔/001005643.ogg"
    xfe "不要紧吗？"
    me01 "不要紧的。"
    pause 0.1 hard
    scene set only xfe_cg noodles five
    with dissolve
    play voice "voice/希菲尔/001005644.ogg"
    xfe "不愧是男孩子呢。"
    "在我和希菲尔的共同努力下，终于是全部吃完了。"
    me01 "多谢款待~"
    pause 0.1 hard
    scene set only xfe_cg noodles three
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005645.ogg"
    xfe "粗茶淡饭而已。"
    me01 "下次有机会的话再吃点别的吧。"
    play voice "voice/希菲尔/001005646.ogg"
    xfe "嗯，我很期待的~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 1.0 hard
    "天空倒映着美丽的余晖。"
    "而春天也在此刻悄然降临这座城市......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day227_balltower_event01:
        $ seen_day227_balltower_event01 = True
    $ _overworld_label = 'day227.balltower_event01'
    jump day227.map

label day227.home_event01:
    default seen_day227_livingroom_event01 = False
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    pause 1.0 hard
    scene set only home night my_room xuejian
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu ts_xfe_yjz_b2 onlayer m2:
            hide screen investigation_popup
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            move _("客厅") jump day227.livingroom_event01
            screen_direction left
            sleep jump day227.sleep

label day227.livingroom_event01:
    if not seen_day227_livingroom_event01:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        $ flcam.move(0, 300, 900, duration=1.5)
        play music second_105 fadein 3.0 if_changed
        with dissolve
        pause 0.5 hard
        show aiyi_dzf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
        pause 0.5 hard
        play voice "voice/爱衣/111001020.ogg"
        aiyi "大哥哥。"
        show aiyi_dzf_b1 b1 b1_sp1
        play voice "voice/爱衣/111001030.ogg"
        aiyi "小希菲尔在吗？"
        hide aiyi_dzf_b1
        $ flcam.move(4500, 0, 900, duration=1.5)
        pause 0.5 hard
        show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
            xpos 0.7
        "听到呼唤的希菲尔，身影逐渐显现出来。"
        hide ts_xfe_yjz_b1
        show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
            xpos 0.7
        play voice "voice/希菲尔/001006020.ogg"
        xfe "找希菲尔吗？"
        $ flcam.move(2250, 300, 750, duration=1.5)
        show aiyi_dzf_b1 b1 b1_h1 onlayer m2 at flu_down(0.35, 20):
            xpos 0.5
        play voice "voice/爱衣/111001040.ogg"
        aiyi "嗯~晚饭做好了，小希菲尔也一起来吧。"
        show ts_xfe_yjz_b2 b2 b2_s2
        play voice "voice/希菲尔/001006030.ogg"
        xfe "希菲尔我就算不吃东西也没关系。"
        show ts_xfe_yjz_b2 b2 b2_ga3 at flu_down(0.25, 20):
            xpos 0.7
        play voice "voice/希菲尔/001006040.ogg"
        xfe "所以不用在意希菲尔。"
        show aiyi_dzf_b1 b1 b1_n1
        play voice "voice/爱衣/111001050.ogg"
        aiyi "不行啦，因为必须和家人一起吃的才叫做晚饭嘛。"
        $ flcam.move(2250, 300, 900, duration=1.5)
        pause 0.5 hard
        hide ts_xfe_yjz_b2
        show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
            xpos 0.7
        play voice "voice/希菲尔/001006050.ogg"
        xfe "家人......"
        show aiyi_dzf_b1 b1 b1_h1
        play voice "voice/爱衣/111001060.ogg"
        aiyi "晚饭准备的是从外面挑选的，小希菲尔最喜欢的雪哟~"
        me01 "原来如此，作成刨冰了吗？"
        show aiyi_dzf_b1 b1 b1_s4
        play voice "voice/爱衣/111001070.ogg"
        aiyi "啊......那样的话说不定更好。可是，没有蜂蜜的话没办法做。"
        show ts_xfe_yjz_b1 b1 b1_s2
        play voice "voice/希菲尔/001006060.ogg"
        xfe "刨冰......"
        hide ts_xfe_yjz_b1
        show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
            xpos 0.7
        play voice "voice/希菲尔/001006070.ogg"
        xfe "那个有听凉君说过的。"
        pause 1.0 hard
        scene white 
        with slowerdissolve
        pause 1.0 hard
        $ flcam.move(0, 0, 900)
        scene set only balltower snow day xuejian alpha
        show sepiagrain onlayer texture
        show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
            xpos 0.5
        play voice "voice/希菲尔/001006080.ogg"
        xfe "要怎么样才能吃到刨冰呢？"
        me01 "这得等到夏天去店里买吧。"
        show ts_xfe_yjz_b2 b2 b2_sp3
        play voice "voice/希菲尔/001006090.ogg"
        xfe "夏天......"
        me01 "再怎么说这个季节也买不到吧。"
        pause 1.0 hard
        $ flcam.move(2250, 300, 750)
        scene set only home night living_room xuejian
        show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
            xpos 0.5
        show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
            xpos 0.7
        play voice "voice/爱衣/111001080.ogg"
        aiyi "虽然没有蜂蜜，不过有酱油或者其他的调味料哟。"
        "那样真的会好吃吗......"
        play voice "voice/爱衣/111001090.ogg"
        aiyi "大哥哥也一起来吧，大家一起吃饭了。"
        stop music fadeout 5.0
        pause 1.0 hard
        scene black 
        with slowerdissolve
        pause 2.0 hard
        scene set only home night kitchen xuejian
        play music second_111 fadein 3.0 if_changed
        $ flcam.move(2250, 300, 750, duration=1.5)
        with dissolve
        pause 0.5 hard
        show aiyi_dzf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.5)
        show ts_xfe_yjz_b2 b2 b2_sp1 onlayer m2 at walkin_r(0.7)
        pause 0.5 hard
        play voice "voice/爱衣/111001100.ogg"
        aiyi "小希菲尔稍微等等，我现在就去给你准备吃的。"
        show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.25, 20):
            xpos 0.5
        "爱衣把雪放到碗里，看起来像是过家家一样。"
        show aiyi_dzf_b1 b1 b1_n1
        play voice "voice/爱衣/111001110.ogg"
        aiyi "也有调味料，小希菲尔喜欢什么味道呢？"
        show ts_xfe_yjz_b2 b2 b2_h1
        play voice "voice/希菲尔/001006100.ogg"
        xfe "希菲尔我最喜欢原味的雪了~"
        show aiyi_dzf_b1 b1 b1_s1
        play voice "voice/爱衣/111001120.ogg"
        aiyi "......没能做成刨冰，抱歉。"
        hide ts_xfe_yjz_b2
        show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
            xpos 0.7
        play voice "voice/希菲尔/001006110.ogg"
        xfe "没关系的，那个就当作是期待留到下次再吃吧。"
        show ts_xfe_yjz_b3 b3 b3_h4 at flu_down(0.25, 20, 2):
            xpos 0.7
        play voice "voice/希菲尔/001006120.ogg"
        xfe "叭咕叭咕~"
        $ flcam.move(2250, 300, 900, duration=1.5)
        pause 0.5 hard
        show aiyi_dzf_b1 b1 b1_sp1
        play voice "voice/爱衣/111001130.ogg"
        aiyi "好吃吗小希菲尔？因为是从外面拿进来的关系似乎有些融化了。"
        hide ts_xfe_yjz_b3
        show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
            xpos 0.7
        play voice "voice/希菲尔/001006130.ogg"
        xfe "雪在快要融化的时候才是最好吃的。"
        show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.25, 20):
            xpos 0.5
        play voice "voice/爱衣/111001140.ogg"
        aiyi "太好了~"
        stop music fadeout 5.0
        pause 1.0 hard
        scene black 
        with slowerdissolve
        pause 2.0 hard
        $ seen_day227_livingroom_event01 = True
        jump day227.home_event01
    else:
        $ flcam.move(0, 0, 0)
        scene black
        with dissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        show ts_xfe_yjz_b2 b2 b2_n1 onlayer m1:
            xpos 0.5
        show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        $ flcam.move(-2250, -400, 600)
        $ flcam.move(-2250, -100, 400, duration=3.0)
        with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu ts_xfe_yjz_b2 onlayer m1:
            camera_pos (scale(2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction right
            move _("卧室") jump day227.home_event01

label day227.sleep:
    menu:
        "早点休息":
            if not seen_day227_livingroom_event01:
                window mode thought
                me01 "还是先去吃晚饭吧。"
                $ flcam.move(0, -100, 400, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            show ts_xfe_yjz_b2 b2 b2_h1
        "{#cancel}再等等":
            xfe "还有什么事情要考虑吗......"
            $ flcam.move(0, -100, 400, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    jump day227.memory_event01

label day227.memory_event01:
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    "梦里依旧是那片熟悉的景象。"
    "天地皆白，无穷无尽的雪原。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg yuki ground
    show snow_level1 onlayer fg
    play music second_154 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    me01 "怎么了希菲尔，今天好像没什么精神。"
    me01 "是因为一整天都在外面太累了吗？"
    me01 "还是身体不舒服呢？"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory one
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001006360.ogg"
    xfe "......"
    me01 "如果是那样的话直接告诉我就好了，我也不会勉强你出现在大家面前了。"
    play voice "voice/希菲尔/001006480.ogg"
    xfe "不是的。"
    me01 "现在感觉怎么样？"
    pause 0.1 hard
    scene set only xfe_cg memory two
    with dissolve
    play voice "voice/希菲尔/001006490.ogg"
    xfe "已经没事了，有凉君在身边所以不要紧的。"
    pause 0.1 hard
    scene set only xfe_cg memory four
    with dissolve
    play voice "voice/希菲尔/001006500.ogg"
    xfe "我只是......有点害怕。"
    play voice "voice/希菲尔/001006510.ogg"
    xfe "希菲尔会变得像现在这样奇怪，也许就是因为被大家“观测”到的缘故。"
    play voice "voice/希菲尔/001006520.ogg"
    xfe "因为总是能够看到......那可怕的梦。"
    play voice "voice/希菲尔/001006530.ogg"
    xfe "自己......将变得不再是自己。"
    play voice "voice/希菲尔/001006540.ogg"
    xfe "希菲尔我虽然一直想要改变，但是不想往坏的方面改变。"
    "我握紧了她颤抖的小手。"
    me01 "这样的话还会害怕吗？"
    pause 0.1 hard
    scene set only xfe_cg memory two
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001006550.ogg"
    xfe "和刚刚说的一样，有凉君在的话就什么都不害怕了。"
    play voice "voice/希菲尔/001006560.ogg"
    xfe "最可惜的是没有好好地向大家说明一起吃晚饭的感想......凉君感觉那会是怎么样的呢？"
    me01 "我觉得应该会是很美好的感觉。"
    play voice "voice/希菲尔/001006580.ogg"
    xfe "具体是什么样的呢？"
    me01 "打个比方的话就像是春天的樱花......之类的。"
    pause 0.1 hard
    scene set only xfe_cg memory three
    with dissolve
    play voice "voice/希菲尔/001006590.ogg"
    xfe "春天的......樱花。"
    me01 "春天到来之后，希菲尔也和大家一起去赏花吧。"
    play voice "voice/希菲尔/001006600.ogg"
    xfe "那样很开心吗？"
    me01 "那是必须的。"
    play voice "voice/希菲尔/001006610.ogg"
    xfe "比吃雪还开心？"
    me01 "因为没吃过雪所以具体也不太清楚......"
    play voice "voice/希菲尔/001006620.ogg"
    xfe "比一起吃拉面还开心吗？"
    me01 "是啊。"
    pause 0.1 hard
    scene set only xfe_cg memory four
    with dissolve
    play voice "voice/希菲尔/001006630.ogg"
    xfe "可怕的梦无论何时看了都会觉得害怕......我想这大概与“害怕”本身是没有关系的。"
    me01 "的确，无论是谁终归是很难战胜自己最不擅长应付的东西。"
    me01 "就连我也是这样的。"
    me01 "但是啊......"
    me01 "害怕的时候就更应该依靠身边的人，所以我也想成为希菲尔的依靠。"
    pause 0.1 hard
    scene set only xfe_cg memory one
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001006640.ogg"
    xfe "凉君真的很可靠。"
    play voice "voice/希菲尔/001006650.ogg"
    xfe "希菲尔总是被帮助的那一方。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ renpy.pause(2.0, hard=True)
    play sound touch
    "希菲尔踮起脚尖，将脸凑了过来。"
    "再一次对着我的额头轻轻地吻了一下。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory two
    with dissolve
    play voice "voice/希菲尔/001006660.ogg"
    xfe "千冬也对希菲尔说了，这个空间是宣誓爱情的地方。"
    play voice "voice/希菲尔/001006670.ogg"
    xfe "因为星光本身就像是戒指一样。"
    play voice "voice/希菲尔/001006680.ogg"
    xfe "希菲尔虽然不太明白爱是什么，不过对于“喜欢凉君”这件事还是清楚的。"
    play voice "voice/希菲尔/001006690.ogg"
    xfe "凉君教给我的......亲吻的含义。"
    play voice "voice/希菲尔/001006700.ogg"
    xfe "要是还有机会的话，希望也能继续教我。"
    pause 0.1 hard
    scene set only xfe_cg memory five
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001006710.ogg"
    xfe "继续教给什么都不懂的希菲尔我更多的......"
    play voice "voice/希菲尔/001006720.ogg"
    xfe "表达“喜欢”的方式。"
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day228
