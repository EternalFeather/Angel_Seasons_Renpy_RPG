
# image role_ani_bllm = Movie(play="video/bllm_movie.webm", size=(1945, 1105))
# image role_ani_lmly = Movie(play="video/lmly_movie.webm", size=(1945, 1105))
# image role_ani_pql = Movie(play="video/pql_movie.webm", size=(1945, 1105))
# image role_ani_lx = Movie(play="video/lx_movie.webm", size=(1945, 1105))
# image role_ani_yyz = Movie(play="video/yyz_movie.webm", size=(1945, 1105))
image sp_ani_role = Movie(play="video/ms2_portal.mp4", size=(1945, 1105))
image item01e = "items/item01e.png"
image item01 = "items/item01.png"
image roleroom_bg = "9i/interface/room/images/bg/mainmenu.png"


label role_ani(name):
    show black onlayer f2
    with dissolve
    pause 1.0 hard
    hide black

    show sp_role onlayer screens
    $ renpy.pause(2.8)
    hide sp_role
#     if name == "博丽灵梦":
#         show role_ani_bllm onlayer screens
#         $ renpy.pause(5.5)
#         hide role_ani_bllm
#     elif name == "蕾米莉亚":
#         show role_ani_lmly onlayer screens
#         $ renpy.pause(7.0)
#         hide role_ani_lmly
#     elif name == "帕秋莉":
#         show role_ani_pql onlayer screens
#         $ renpy.pause(5.8)
#         hide role_ani_pql
#     elif name == "铃仙":
#         show role_ani_lx onlayer screens
#         $ renpy.pause(9.5)
#         hide role_ani_lx
#     elif name == "幽幽子":
#         show role_ani_yyz onlayer screens
#         $ renpy.pause(3.2)
#         hide role_ani_yyz
    show black onlayer f2
    with dissolve
    pause 3.0 hard
    hide black
    return


# screen input_sentence:
#     modal True

#     default sent = Tooltip("说点什么吧：")
#     text sent.value:
#         xalign 0.5
#         yalign 0.4
#         size 40
#         outlines auto_text_outline()

#     input:
#         default ""
#         length None
#         size 32
#         xalign 0.5
#         yalign 0.5
#         color "#FFD476"
#         outlines auto_text_outline()


screen send_detective_screen:
    # DragGroup确保每个符咒可以拖拽到Pooler。
    draggroup:
        # 符咒
        drag:
            drag_name "Card"
            child "card_sp"
            droppable False
            dragged detective_dragged
            xalign 0.48 yalign 0.95

        # 卡池
        drag:
            drag_name "Pooler"
            child "pooler_sp"
            draggable False
            xalign 0.5 yalign 0.35


label inside_battle3(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "青木铃音的被动技能「天宫罗阵」能够在其友方任意单位行动后概率{color=#f00}协战{/color}。"
    "借助「空间跳跃」结界效果打出{color=#f00}连击{/color}，利用「水」与「冰」发生的{color=#3ff}冻结{/color}反应能够一定程度限制对方行动。"
    "另外小桃的元素战技「灵能风暴」具有一定的{color=#3ff}减速{/color}和{color=#3ff}冻结{/color}效果。「守护誓约」被动加持下的雷亚死亡后将进入第二形态，具有强大的{color=#3ff}冰属性{/color}AOE伤害，能够更容易打出冻结效果。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label day206:
    bookmark
    $ save_name = _("Day 206")
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play sound "sound/system/second_menu.wav"
    scene black with Dissolve(8.0)
    pause 4.0 hard

    $ renpy.block_rollback()
    $ _rollback = True
    
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    pause 2.0 hard
    show backend_date205 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    "今天是周末。"
    "早晨的时候并没有感觉到寒冷。"
    "拜这个所赐我甚至想要一整天都赖在被窝里。"
    "但毕竟与人有约在先。"
    pause 1.0 hard
    play music second_114 fadein 3.0 if_changed
    scene set only aiyi_cg one
    with slowdissolve
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('chapter two'), _("七夕的双子星"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard
    "温暖的源头原来是这个吗。"
    "睁开眼的一刹那就看到爱衣可爱的小脸。"
    pause 0.1 hard
    scene set only aiyi_cg three
    with dissolve
    play voice "voice/爱衣/110101880.ogg"
    aiyi "......"
    me01 "醒了吗爱衣？"
    play voice "voice/爱衣/110101890.ogg"
    aiyi "......大哥哥？"
    me01 "早上好。"
    play voice "voice/爱衣/110101900.ogg"
    aiyi "早上.....好。"
    play voice "voice/爱衣/110101910.ogg"
    aiyi "......"
    pause 0.1 hard
    scene set only aiyi_cg four
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/爱衣/110101920.ogg"
    aiyi "......欸？"
    play voice "voice/爱衣/110101930.ogg"
    aiyi "爱、爱衣......为什么会和大哥哥一起睡？"
    me01 "一定又是昨晚不小心钻进来的吧？"
    play voice "voice/爱衣/110101940.ogg"
    aiyi "是、是这样吗？"
    play voice "voice/爱衣/110101950.ogg"
    aiyi "爱衣我......昨晚起来上厕所。"
    play voice "voice/爱衣/110101960.ogg"
    aiyi "然后......就没有记忆了。"
    play voice "voice/爱衣/110101970.ogg"
    aiyi "说不定是搞错了来到大哥哥的房间。"
    pause 0.1 hard
    scene set only aiyi_cg five
    with dissolve
    play voice "voice/爱衣/110101980.ogg"
    aiyi "对、对不起......"
    me01 "这点小事没必要道歉。"
    pause 0.1 hard
    scene set only aiyi_cg four
    with dissolve
    play voice "voice/爱衣/110101990.ogg"
    aiyi "可以吗？"
    play voice "voice/爱衣/110102000.ogg"
    aiyi "就算一起睡......也不会困扰吗？"
    me01 "不过对你翔子姐姐可要保密。"
    me01 "如果被发现的话肯定又要挨骂的。"
    pause 0.1 hard
    scene set only aiyi_cg two
    with dissolve
    play voice "voice/爱衣/110102010.ogg"
    aiyi "嗯~"
    play voice "voice/爱衣/110102020.ogg"
    aiyi "这是只属于爱衣和大哥哥的秘密。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard
    $ _overworld_label = 'day206'
    $ seen_day206_bridge_event01 = False
    $ seen_day206_street_event01 = False
    $ seen_day206_balltower_event01 = False
    $ seen_day206_shenshe_event01 = False
    $ seen_day206_laboratory_event01 = False

label day206.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day206':
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day206.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'])
    elif _overworld_label == 'day206.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'])
    elif _overworld_label == 'day206.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day206.shenshe_event01':
        $ flcam.move(*overworld.camera_positions['shenshe'])
    elif _overworld_label == 'day206.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    if _overworld_label == 'day206':
        window mode map
        me01 "先去和琉璃会和吧......" nointeract
    else:
        window mode map
        me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        bridge=("day206.bridge_event01", "not seen_day206_bridge_event01"),
        road2=("day206.street_event01", "seen_day206_bridge_event01 and not seen_day206_street_event01"),
        laboratory=("day206.laboratory_event01", "seen_day206_bridge_event01 and not seen_day206_laboratory_event01"),
        cloqks=("day206.balltower_event01", "seen_day206_bridge_event01 and not seen_day206_balltower_event01"),
        shenshe=("day206.shenshe_event01", "seen_day206_bridge_event01 and not seen_day206_shenshe_event01"))
    $ window_animate_outro()
    if _return == 'day206.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day206.street_event01':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day206.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day206.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day206.shenshe_event01':
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

label day206.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only bridge day xuejian
    play music second_112 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040102920.ogg"
    liuli "神野前辈，早上好。"
    me01 "早上好，琉璃你很准时啊。"
    show liuli_dsf_b2 b2 b2_h1
    play voice "voice/琉璃/040102930.ogg"
    liuli "是的，我也是刚到而已。"
    "就好像提前知道了我的位置，琉璃在我刚踏入大桥的一刹那就从我身后出现了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040102940.ogg"
    liuli "神野前辈，你想先去哪里呢？"
    me01 "这点就交给琉璃你决定好了。"
    show liuli_dsf_b3 b3 b3_h1
    play voice "voice/琉璃/040102960.ogg"
    liuli "我明白了，那么事不宜迟我们出发吧~"
    me01 "话说回来，还是头一次看到你穿便服的样子。"
    show liuli_dsf_b3 b3 b3_sp1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/040102970.ogg"
    liuli "为什么突然说这个？"
    me01 "因为很适合。"
    "果然可爱的女生无论穿什么都不会有太大的影响。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    if not seen_day206_bridge_event01:
        $ seen_day206_bridge_event01 = True
    $ _overworld_label = 'day206.bridge_event01'
    jump day206.map

label day206.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street day city1 xuejian
    play music second_133 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    me01 "这里给人感觉像是来到了另一个次元。"
    "新城区商业街现代化的建筑别具一格，川流不息的人群更是让格调显得高大上了不少。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103210.ogg"
    liuli "这里的车站人流量很大，不只是新城区的居民，也有很多从外地来的人。"
    me01 "因为是休息日所以都选择出来游玩吗？"
    "似乎就算是寒冷也无法阻挡人流的涌动。"
    "况且今天没有下雪。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103220.ogg"
    liuli "这里的新城区不仅仅是供人们游玩的，也有不少人选择来这里工作。"
    play voice "voice/琉璃/040103230.ogg"
    liuli "如果要去旧城区或是其他地方观光的话，通常会选择这里的电车作为交通工具。"
    me01 "原来如此。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103240.ogg"
    liuli "接下来去购物街吧，就坐落在车站附近。"
    me01 "总感觉人会变得更多的样子......"
    show liuli_dsf_b2 b2 b2_sp1
    play voice "voice/琉璃/040103250.ogg"
    liuli "神野前辈不习惯人多的地方吗？"
    me01 "让你见笑了。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103260.ogg"
    liuli "没有关系的，立花小姐似乎也不太喜欢的样子。"
    show liuli_dsf_b3 b3 b3_n1
    play voice "voice/琉璃/040103270.ogg"
    liuli "那么选择人少一点的商务街会好一点吗？"
    me01 "话虽如此，购物街那边也拜托了，今天想要全部逛个遍。"
    hide liuli_dsf_b3 with None
    pause 0.1 hard
    show liuli_dsf_b2 b2 b2_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/琉璃/040103280.ogg"
    liuli "我知道了，那么就从近的地方开始参观吧~"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day city2 xuejian
    with dissolve
    pause 1.0 hard
    me01 "呜啊，好多人！"
    "来到了购物街，大大小小崭新的店铺罗列在两旁。"
    "放眼望去大多都是年轻人。"
    "一股莫名的疲劳感扑面而来。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103290.ogg"
    liuli "神野前辈......你累了吗？"
    me01 "比起这个琉璃要稍微去玩一下吗？"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103300.ogg"
    liuli "去玩？"
    me01 "这里有各种店铺，不稍微逛逛吗？"
    show liuli_dsf_b3 b3 b3_n1
    play voice "voice/琉璃/040103310.ogg"
    liuli "我的工作是为神野前辈带路，所以就按前辈的意愿行动就好。"
    me01 "不是工作，是约会哟。"
    show liuli_dsf_b3 b3 b3_n4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/040103320.ogg"
    liuli "约会......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103330.ogg"
    liuli "约会的时候应该做些什么呢？"
    me01 "大概......就是玩吧。"
    show liuli_dsf_b1 b1 b1_s2
    play voice "voice/琉璃/040103340.ogg"
    liuli "玩的话......具体该怎么做呢？"
    "琉璃似乎也没有这方面的经验。"
    "这下可伤脑筋了。"
    me01 "琉璃你有什么想做的事情吗？"
    show liuli_dsf_b1 b1 b1_sp1
    play voice "voice/琉璃/040103350.ogg"
    liuli "想做的事情。"
    show liuli_dsf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/040103360.ogg"
    liuli "那、那个......"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103370.ogg"
    liuli "想和神野前辈一起......像这样......散步......之类的。"
    show liuli_dsf_b3 b3 b3_n4
    play voice "voice/琉璃/040103380.ogg"
    liuli "散步......可以吗？"
    me01 "当然没问题。"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103390.ogg"
    liuli "如果感到难受的话，请一定要告诉我。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103400.ogg"
    liuli "不需要和我客气，我会全程通过前辈的体温和脉搏来判断前辈身体状况的。"
    me01 "......那是怎么做到的？"
    show liuli_dsf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/琉璃/040103440.ogg"
    liuli "像这样~"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    play sound touch
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg city one
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/040103450.ogg"
    liuli "像这样抱着对方胳膊的话，就能测量对方的体温和脉搏了。"
    play voice "voice/琉璃/040103480.ogg"
    liuli "神野前辈的体温......稍微有些高啊。"
    play voice "voice/琉璃/040103500.ogg"
    liuli "啊咧......脉搏似乎也跳得越来越快了。"
    me01 "这是当然的吧！"
    "被突然抱住胳膊的话......"
    pause 0.1 hard
    scene set only liuli_cg city three
    with dissolve
    play voice "voice/琉璃/040103510.ogg"
    liuli "啊，说起来......"
    play voice "voice/琉璃/040103520.ogg"
    liuli "这项技能我还是第一次使用。"
    play voice "voice/琉璃/040103530.ogg"
    liuli "身体好热。"
    play voice "voice/琉璃/040103540.ogg"
    liuli "说不定我现在......"
    play voice "voice/琉璃/040103550.ogg"
    liuli "真的很开心。"
    play voice "voice/琉璃/040103560.ogg"
    liuli "为什么呢。"
    play voice "voice/琉璃/040103570.ogg"
    liuli "还是第一次有这样的感觉。"
    "再这样下去情况可能会更加恶化。"
    "话说这个柔软的触感，果然是女孩子才有的吗......"
    pause 0.1 hard
    scene set only liuli_cg city one
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/040103630.ogg"
    liuli "前辈，这样子算是约会吗？"
    me01 "我想想......"
    "调度我残存的精力进行了思考。"
    me01 "大概，就是这样的没错。"
    pause 0.1 hard
    scene set only liuli_cg city two
    with dissolve
    play voice "voice/琉璃/040103640.ogg"
    liuli "太好了~"
    pause 0.1 hard
    scene set only liuli_cg city one
    with dissolve
    play voice "voice/琉璃/040103650.ogg"
    liuli "如果觉得碍事的话请随时告诉我。"
    me01 "怎么会呢。"
    play voice "voice/琉璃/040103660.ogg"
    liuli "累了的话也请告诉我。"
    me01 "你不是一直在观测着吗。"
    pause 0.1 hard
    scene set only liuli_cg city three
    with dissolve
    play voice "voice/琉璃/040103670.ogg"
    liuli "啊，是这样来着。"
    me01 "结果如何？"
    pause 0.1 hard
    scene set only liuli_cg city one
    with dissolve
    play voice "voice/琉璃/040103680.ogg"
    liuli "各种数值都很高。"
    me01 "在这个季节也算是有好处吧。"
    pause 0.1 hard
    scene set only liuli_cg city two
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/琉璃/040103700.ogg"
    liuli "是的~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 2.0 hard
    scene set only street day city3 xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104070.ogg"
    liuli "因为这里的雪和其他地方的不一样，才会吸引这样密集的人群也说不定。"
    show liuli_dsf_b2 b2 b2_sp1
    me01 "虽说不是第一次来雪见市了，不过对于雪的感觉倒是改变了许多。"
    me01 "关于我的过去，你想听吗？"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104080.ogg"
    liuli "是的，比起历史的客观事实，我更想听的是关于居民的故事~"
    play voice "voice/琉璃/040104090.ogg"
    liuli "我想知道这里的居民过去在这里经历的事情，以及对这座城市抱着什么样的感情。"
    me01 "既然是这样的话......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    play music second_135 fadein 3.0 if_changed
    pause 1.0 hard
    "那时候的雪见市，还没有像如今这般地被开发。"
    "到处都是低矮的楼房。"
    "与现在不同，到了冬天雪是会堆积起来。"
    "所以扫雪是必要的工作，因为如果放任不管的话就会影响交通。"
    "虽然也有小孩子会玩打雪仗或是堆雪人，但不久他们便就会意识到，家里的暖炉比起这项游戏更加具有吸引力。"
    "回想起来，在和希菲尔一起玩耍的时光里，我对雪一点都不会感到厌恶。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory0
    show sepiagrain onlayer texture
    with dissolve
    pause 1.0 hard
    "和她一起经历的时光。"
    "冬日的雪道，银白色的世界。"
    "身边只有她一人的光景，正在渐渐地变得清晰起来。"
    "也许在我儿时的都市生活岁月里，唯有这段回忆是我一直珍藏至今的。"
    "无论何时，都不舍得抛弃。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day206_street_event01:
        $ seen_day206_street_event01 = True
    if seen_day206_shenshe_event01 and seen_day206_balltower_event01 and seen_day206_laboratory_event01:
        jump day206.street_event02
    $ _overworld_label = 'day206.street_event01'
    jump day206.map

label day206.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only balltower day xuejian
    with dissolve
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104110.ogg"
    liuli "这里是......"
    "相比于之前的商店街，钟楼广场给人的印象倒是冷清了许多。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower day big
    play ambience1 zhong_rill fadein 3.0
    with dissolve
    pause 3.0 hard
    stop ambience1 fadeout 3.0
    scene set only balltower day xuejian alpha
    $ flcam.move(-4500, 300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    play sound appear
    play music second_106 fadein 3.0 if_changed
    show qianbo_dsf_b1 b1 b1_a2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/210100800.ogg"
    qb "{size=72}喂！！{/size}"
    me01 "是你啊......"
    show qianbo_dsf_b1 b1 b1_n1
    play voice "voice/千波/210100810.ogg"
    qb "看到凉君男所以过来打个招呼。"
    me01 "打招呼是用吼的吗。"
    show qianbo_dsf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/210100820.ogg"
    qb "顺便来阻止你对着游客哈~哈~喘粗气的行为。"
    me01 "太口无遮拦的话小心我敲你的脑袋。"
    hide qianbo_dsf_b1
    show qianbo_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/210100830.ogg"
    qb "立花老师敲脑袋好疼的说......"
    stop music fadeout 5.0
    pause 0.5 hard
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qbj_dzf_b1 b1 b1_a1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/千波姐/160100250.ogg"
    stranger "等等千波，怎么突然跑掉了。"
    play music second_115 fadein 3.0 if_changed
    hide qianbo_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show qbj_dzf_b1 b1 b1_sp1
    play voice "voice/千波姐/160100260.ogg"
    stranger "啊，我记得你是......"
    show qbj_dzf_b1 b1 b1_n1
    play voice "voice/千波姐/160100270.ogg"
    stranger "是转到青木同学班上的神野同学吧，我也经常听千波说起你的事。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qianbo_dsf_b1 b1 b1_n2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/210100840.ogg"
    qb "我可是毫无隐瞒地报告了凉君男的所作所为。"
    show qbj_dzf_b1 b1 b1_s2 
    play voice "voice/千波姐/160100280.ogg"
    stranger "在之前幼儿园见过面的，我妹妹千波承蒙你照顾了，真是抱歉。"
    me01 "你就是传说中的学生会长？！"
    hide qianbo_dsf_b1
    show qianbo_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/210100850.ogg"
    qb "这不是什么值得称赞的事啦~"
    "无视这家伙好了。"
    hide qianbo_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "重新介绍下，我叫神野凉，请多指教。"
    show qbj_dzf_b1 b1 b1_h1
    play voice "voice/千波姐/160100310.ogg"
    stranger "嗯，虽然班级不同不过还请多关照~"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qianbo_dsf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/210100860.ogg"
    qb "也不是什么值得关照的人啦。"
    "继续无视。"
    hide qianbo_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show qbj_dzf_b1 b1 b1_n1
    play voice "voice/千波姐/160100320.ogg"
    qbj "在学校如果有什么不明白的事情，可以来找我。"
    me01 "真是帮大忙了，学生会干部果然都是擅长照顾人的类型。"
    show qbj_dzf_b1 b1 b1_ga2
    play voice "voice/千波姐/160100330.ogg"
    qbj "并不是因为是干部才这样的，毕竟也是同级生的关系。"
    show qbj_dzf_b1 b1 b1_h1
    play voice "voice/千波姐/160100350.ogg"
    qbj "青木同学也很擅长照顾人，我也很希望能够帮到神野同学。"
    me01 "......让你费心了。"
    show qbj_dzf_b1 b1 b1_sp1
    play voice "voice/千波姐/160100360.ogg"
    qbj "马上就要考试了，不用复习吗？"
    me01 "晚上会的努力的，现在和朋友外出中。"
    show qbj_dzf_b1 b1 b1_ga2
    play voice "voice/千波姐/160100370.ogg"
    qbj "我也是出来散散心，顺便陪着千波。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qianbo_dsf_b1 b1 b1_a2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/210100870.ogg"
    qb "简直可笑！"
    me01 "别突然大喊大叫的，可笑的是你吧！"
    hide qbj_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    show qianbo_dsf_b1 b1 b1_a3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/210100880.ogg"
    qb "人家才不是因为想加入对话呢！"
    me01 "今天去哪里了？"
    show qianbo_dsf_b1 b1 b1_h2
    play voice "voice/千波/210100890.ogg"
    qb "去商店街购物了哟，对于成熟的女性来说，衣服是不会嫌多的。"
    me01 "穿衣服对你来说太早了吧。"
    play sound jump_1
    show qianbo_dsf_b1 b1 b1_a2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/210100910.ogg"
    qb "不可能裸体度日吧！"
    me01 "反正你穿没穿都差不多。"
    show qianbo_dsf_b1 b1 b1_a2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/千波/210100920.ogg"
    qb "不穿的话会感冒的吧！！！"
    "果然是小孩子啊。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day206_balltower_event01:
        $ seen_day206_balltower_event01 = True
    if seen_day206_shenshe_event01 and seen_day206_street_event01 and seen_day206_laboratory_event01:
        jump day206.street_event02
    $ _overworld_label = 'day206.balltower_event01'
    jump day206.map

label day206.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only shenshe day xuejian
    play music second_120 fadein 3.0 if_changed
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve    
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/藤原瞳/130100940.ogg"
    tyt "等你们很久了。"
    me01 "即使是周末也是一副巫女装扮吗。"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/130100950.ogg"
    tyt "你谁？"
    me01 "喂！"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/130100960.ogg"
    tyt "开玩笑的。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104290.ogg"
    liuli "藤原同学，你现在是在进行神社的工作吗？"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/130100970.ogg"
    tyt "为什么这么问？"
    hide liuli_dsf_b2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "当然是因为看你这一身巫女服的缘故吧。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/130100980.ogg"
    tyt "这是便装。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130100990.ogg"
    tyt "我只是在监督神社的施工进度而已。"
    me01 "从外面看的话已经恢复的差不多了。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/130101000.ogg"
    tyt "嗯，但是里面的状况还比较惨。"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/130101010.ogg"
    tyt "还好神体本身没有出事。"
    me01 "神体？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/130101020.ogg"
    tyt "是供奉在神社里的陨石。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104310.ogg"
    liuli "里面寄宿着星神大人的意识对吧？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130101030.ogg"
    tyt "嗯~那位大人正是我们神社的象征。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/130101080.ogg"
    tyt "虽然无法考证，但是据说陨石中寄宿着星神阿露毕蕾欧的神识。"
    "不会那么巧吧，随口起了个名没想到把那只天鹅捧上天了。"
    me01 "也就是说这座神社的工作就是负责供奉这位神明吗？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/130101100.ogg"
    tyt "是的，这是神社方——星天宫传达的口讯。"
    stop music fadeout 3.0
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 1.0 hard
    if not seen_day206_shenshe_event01:
        $ seen_day206_shenshe_event01 = True
    if seen_day206_balltower_event01 and seen_day206_street_event01 and seen_day206_laboratory_event01:
        jump day206.street_event02
    $ _overworld_label = 'day206.shenshe_event01'
    jump day206.map

label day206.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory day outside xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103810.ogg"
    liuli "这里就是星天宫研究所了。"
    me01 "果然很气派啊。"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103830.ogg"
    liuli "是的，这里离市中心很近。"
    hide liuli_dsf_b2
    pause 1.0 hard
    $ flcam.moves([
        (0,      0,   900, 0, 0.0, 'linear'),
        (4500, -3500, 1500, 0, 4.5, 'ease_cubic')
    ])
    with dissolve
    pause 4.0 hard
    "抬头望向眼前的建筑物。"
    "给人一种望尘莫及的感觉，与周围的其他建筑形成了鲜明的对比。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside1 xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=3.0, warper='ease_cubic')
    play sound jiaobu2
    pause 3.0 hard
    "我们搭乘电梯来到了指定的楼层。"
    "在敞亮的走廊上脚步声特别明显。"
    "据琉璃说研究所高达四十八层之多，这样规模的研究所在全日本也实属罕见了。"
    play music second_124 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103850.ogg"
    liuli "神野前辈，能请你在这里等一下吗？"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103860.ogg"
    liuli "我去向圣护院小姐报告访客信息。"
    me01 "你说的那位圣护院小姐是这里的负责人？"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103870.ogg"
    liuli "是的，因为圣护院小姐就算是周末也会来工作。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103880.ogg"
    liuli "圣护院小姐是综合管理这里的研究员，也就是主任。"
    show liuli_dsf_b3 b3 b3_ga3
    play voice "voice/琉璃/040103890.ogg"
    liuli "她对各种事情都比较了解，应该能解答前辈的问题。"
    me01 "如果是这样的话就太好了。"
    "关于这座城市的异常气候，以及身上突然涌现的灵力。"
    "有一堆的问题还没有解决。"
    "如果对方知道些什么的话，正好能趁机获取一些情报。"
    "也许还能找到关于雷亚的线索也说不定。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg final one
    show sepiagrain onlayer texture
    with dissolve
    pause 1.0 hard
    "樱华镇出现的死神雷亚。"
    pause 1.0 hard
    scene set only xfe_cg bridge normal
    show sepiagrain onlayer texture
    with dissolve
    pause 1.0 hard
    "还有雪见市出现的希菲尔。"
    "她们之间究竟有何种联系呢？"
    "亦或者说，她们究竟是谁？"
    pause 1.0 hard
    scene set only laboratory inside1 xuejian
    with dissolve
    pause 1.0 hard
    "之前在我身上出现的{rb}念动立场{/rb}{rt}psychokinesis{/rt}，似乎也不像是正常的自然科学可以解释的。"
    "也许就和所谓的异常气候一样，是研究所想要解开的谜团之一。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103900.ogg"
    liuli "神野前辈还真是热爱学习呢，想知道关于气象研究成果的居民，你还是第一个。"
    me01 "是这样吗？"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103910.ogg"
    liuli "是的，雪见市的大家似乎不管什么时候下雪都不会感到惊讶。"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103920.ogg"
    liuli "说不定是这座城市的气氛造成的吧，该说是太过悠闲，还是说是大家已经习惯了呢？"
    play voice "voice/琉璃/040103930.ogg"
    liuli "对于雪见市的雪，可能外来的人要更加在意吧，研究所的大家也都是从总本社调过来的。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103950.ogg"
    liuli "在解读出常冬的原因之前，想要作为观光宣传也会很困难的吧。"
    "的确，无法断言常年降雪的原因，多少会让外来人有所顾虑。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103960.ogg"
    liuli "抱歉，话说得太久了，我这就去联系圣护院小姐。"
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_n1 at walkout_r(0.5)
    play sound open_door6
    pause 0.5 hard
    "琉璃走进了实验室，而我则是待在原地等候。"
    pause 1.0 hard
    scene black
    with dissolve
    pause 1.0 hard
    ".........."
    "......"
    "..."
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside1 xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_s1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/琉璃/040103970.ogg"
    liuli "抱歉......圣护院小姐现在似乎很忙的样子。"
    play voice "voice/琉璃/040103980.ogg"
    liuli "其他的研究员们也被各种事务缠身，所以参观的请求也被拒绝了。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040103990.ogg"
    liuli "真的很抱歉，前辈好不容易来一趟......"
    me01 "虽然有些可惜，不过也是没有办法的事。"
    me01 "之所以会如此繁忙是因为最近的研究很棘手吗？"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104000.ogg"
    liuli "不是的，现在似乎是在调查神社的事件。"
    show liuli_dsf_b1 b1 b1_n1
    play voice "voice/琉璃/040104010.ogg"
    liuli "研究所不只是研究雪见市的雪，同时也在调查其他类似的异常气候。"
    me01 "......也就全日本的异常气候都是研究对象吗？"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104020.ogg"
    liuli "是这样的。"
    show liuli_dsf_b3 b3 b3_n2
    play voice "voice/琉璃/040104030.ogg"
    liuli "因为神社前一阵子刚发生那样的事情，所以才会这么忙的。"
    me01 "原来如此。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104040.ogg"
    liuli "神野前辈你累了吧，要找个地方休息一下吗？"
    me01 "没事的，既然如此也只好放弃了。"
    me01 "今天谢谢你了琉璃，可以的话下次希望也能请你继续当我的导游。"
    hide liuli_dsf_b2 with None
    pause 0.1 hard
    show liuli_dsf_b3 b3 b3_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/琉璃/040104050.ogg"
    liuli "好的，到时候也请多多指教~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day206_laboratory_event01:
        $ seen_day206_laboratory_event01 = True
    if seen_day206_balltower_event01 and seen_day206_street_event01 and seen_day206_shenshe_event01:
        jump day206.street_event02
    $ _overworld_label = 'day206.laboratory_event01'
    jump day206.map

label day206.street_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "结束了一天的行程，转眼的功夫天色就暗了下来。"
    "告别了琉璃的我独自一人走在回家的路上。"
    "今天见识了新城区的人潮之后，才感觉到旧城区的街道原来是如此的冷清。"
    "也不知从什么时候开始，天空开始飘起了白雪。"
    pause 1.0 hard
    scene set only street evening road1 xuejian
    with dissolve
    pause 1.0 hard
    me01 "那是......"
    $ flcam.move(0, 0, 750, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    play music second_108 fadein 3.0 if_changed
    show alu_ct_b2 b2 b2_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    "我遇到了那只罕见的生物。"
    me01 "这家伙怎么会在这里？"
    hide alu_ct_b2
    $ flcam.move(-4500, 0, 900, duration=1.5, warper='ease_cubic')
    pause 2.0 hard
    $ flcam.move(4500, 0, 900, duration=1.5, warper='ease_cubic')
    pause 2.0 hard
    $ flcam.move(0, -300, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    show alu_ct_b2 b2 b2_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    pause 0.5 hard
    "希菲尔似乎不在附近。"
    me01 "和主人走散了吗？"
    "我在干什么呢，就算我这么问它也不会回答我的。"
    me01 "天快黑了，还是早点回去会比较好。"
    hide alu_ct_b2 with None
    show alu_ct_b2 b2 b2_2 onlayer m2 at fly(0.5):
        xpos 0.5
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎~"
    me01 "？!"
    "这家伙在说话？！"
    "话说这种生物的叫声原来是这样的吗......"
    hide alu_ct_b2 with None
    show alu_ct_b9 b9 b9_1 onlayer m2 at fly(0.5):
        xpos 0.5
    play voice "voice/阿露/551000020.ogg"
    alu "唔莎~唔莎~"
    me01 "不要停在我肩上啊。"
    play voice "voice/阿露/551000030.ogg"
    alu "唔莎唔莎~唔莎唔莎~"
    me01 "在耳边唔莎唔莎的吵死了......"
    play voice "voice/阿露/551000040.ogg"
    alu "唔莎~~"
    pause 0.5 hard
    play sound fly1
    hide alu_ct_b9 with None
    show alu_ct_b2 b2 b2_2 onlayer m2 at fly_away(0.5):
        xpos 0.5
    pause 1.0 hard
    "飞走了。"
    play sound jiaobu3
    $ flcam.move(0, -100, 400, duration=1.5, warper='ease_cubic')
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with dissolve
    pause 1.0 hard
    "我快步追了上去。"
    "总觉得跟着这家伙就能找到希菲尔。"
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day206.balltower_event02:
    play ambience1 zhong_rill fadein 3.0
    $ flcam.move(0, 0, 0)
    scene set only balltower evening big
    show snow_level1 onlayer fg
    with slowdissolve
    pause 2.0 hard
    "我循着阿露的身影追了过去。"
    stop ambience1 fadeout 5.0
    pause 1.0 hard
    scene set only balltower evening xuejian
    with dissolve
    pause 2.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 5.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory4
    play music second_103 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    "在钟楼下我遇到了那熟悉的身影。"
    "此刻的希菲尔正仰望着钟楼。"
    "那身姿宛若在吟唱着歌曲的雪之妖精一般，梦幻、美妙。"
    pause 1.0 hard
    scene set only balltower evening xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001000120.ogg"
    xfe "......凉君。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/001000130.ogg"
    xfe "是凉君~"
    "希菲尔轻盈地朝我跑了过来。"
    "而我也下意识地摸了摸她的头。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001000140.ogg"
    xfe "诶嘿，好痒的说~"
    show ts_xfe_yjz_b2 b2 b2_s2
    play voice "voice/希菲尔/001000150.ogg"
    xfe "凉君以前明明才和我一样高，现在却能那么轻易就摸到我的头了。"
    me01 "因为我长大了嘛。"
    show ts_xfe_yjz_b2 b2 b2_h3
    play voice "voice/希菲尔/001000160.ogg"
    xfe "嗯，我知道的。"
    me01 "希菲尔倒是没有什么变化。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001000170.ogg"
    xfe "对呀......我没有改变。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001000180.ogg"
    xfe "就算想要改变......也是没有办法改变的。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001000190.ogg"
    xfe "明明不像凉君一样改变的话是不行的。"
    me01 "没有改变也挺好的。"
    me01 "倒不如说，发现希菲尔没有改变我反而更开心了。"
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/001000200.ogg"
    xfe "是这样吗？"
    me01 "是啊。"
    me01 "还有，对不起。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001000210.ogg"
    xfe "欸？"
    me01 "没有与你道别就擅自离开。"
    me01 "我替那时侯的我向你道歉。"
    show ts_xfe_yjz_b2 b2 b2_s3
    play voice "voice/希菲尔/001000220.ogg"
    xfe "......"
    me01 "过去的我能和希菲尔成为朋友真是太好了。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h3
    play voice "voice/希菲尔/001000230.ogg"
    xfe "我果然还是觉得，一切都没有改变。"
    show ts_xfe_yjz_b2 b2 b2_ga3
    play voice "voice/希菲尔/001000240.ogg"
    xfe "什么都没有变。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001000250.ogg"
    xfe "所以现在的凉君也是希菲尔的朋友。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001000260.ogg"
    xfe "虽然分别是令人悲伤的事。但是凉君又一次找到了我，所以果然一切都是没有改变的。"
    me01 "这么说你接受我的道歉了？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001000270.ogg"
    xfe "就是这样的哟~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day206.balltower_event04:
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 2.0 hard
    scene set only balltower night xuejian
    with dissolve
    pause 1.0 hard
    "伴随着入夜钟声的响起，希菲尔的身影也消失了。"
    "仿佛是与眼前的这场雪融为一体似的离开了。"
    "然而这一次我并没有急着离开，而是注视着这个我们曾经一起玩耍的钟楼广场发呆。"
    "她刚刚的那番话一直在我的脑海中回荡。"
    "“一切都没有改变”、“明明不改变是不行的”，她想要传达给我的究竟是一种怎样的情绪呢。"
    "而就是这样充满期望却又略显悲伤的语气，让我不由得陷入了过去与她一同玩耍时的回忆漩涡之中。"
    pause 1.0 hard
    hide snow_level1
    scene black
    with dissolve
    pause 1.0 hard
    "不想改变，唯独那份回忆始终不想要它有所改变。"
    "但如今经历了那么多的我也明白，不继续向前迈进是不行的。"
    "明明约好了的，要朝着约定的方向前进的......"
    nvl clear
    play voice "voice/天使雷亚/0021730.ogg"
    pcenter "凉君——"
    pause 0.5 hard
    nvl clear
    with dissolve
    play voice "voice/天使雷亚/0021740.ogg"
    stranger "怎么了凉君？"
    play voice "voice/天使雷亚/0021750.ogg"
    stranger "一直看着星空发呆。"
    pause 1.0 hard
    scene set only balltower night xuejian
    show snow_level1 onlayer fg
    with cent2side
    pause 1.0 hard
    play music first_30 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound xiaoshi_1
    show ts_lst_ssz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5 alpha 0.0
        linear 1.0 alpha 0.7
    pause 3.0 hard
    me01 "雷......亚......"
    me01 "果然那时候在神社救下小桃的那束光就是你吗。"
    me01 "就是你再一次赐予了我，拯救重要之人的力量吗。"
    me01 "呐雷亚你知道吗，我真的......好想你。"
    me01 "这一次我们终于可以......"
    stop music fadeout 5.0
    pause 0.5 hard
    play voice "voice/青木铃音/0507970.ogg"
    stranger "果然是你，神野同学。"
    pause 2.0 hard
    play music second_123 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    hide snow_level1
    scene set only lingyin_cg one
    with dissolve
    pause 1.0 hard
    me01 "铃音......同学？"
    play voice "voice/青木铃音/0507980.ogg"
    lingyin "是我。"
    "眼前的少女虽然长相和声音都和铃音一模一样。"
    "但是那冰冷的眼神竟让我第一时间没有认出对方。"
    "在夜空下她手里的薙刀反射着星光，倒映在飘落的白雪之上。"
    "那锋芒格外的渗人。"
    me01 "你这身打扮......你也是星天宫的巫女吗。"
    play voice "voice/青木铃音/0507990.ogg"
    lingyin "是的。"
    me01 "你也能看得到雷亚的存在吗。"
    play voice "voice/青木铃音/0508010.ogg"
    lingyin "是的。"
    me01 "虽然不知道你现在出现究竟想干什么，但不惜埋伏这么久想必也是早就对我有所怀疑了吧。"
    pause 0.1 hard
    scene set only lingyin_cg three
    $ flcam.move(-2200, -1500, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/0508020.ogg"
    lingyin "不需要恭维我，不如说突然打断你们的谈话真是抱歉。"
    me01 "如果你只是单纯地也想加入进来的话我倒是很欢迎。"
    pause 0.1 hard
    scene set only lingyin_cg one
    with dissolve
    play voice "voice/青木铃音/0508030.ogg"
    lingyin "这样的想法是很花心的哟。"
    me01 "想必你来这里也是有话要对我说吧。"
    play voice "voice/青木铃音/0508040.ogg"
    lingyin "没有，这只是一种手段而已。"
    me01 "手段？"
    play voice "voice/青木铃音/0508050.ogg"
    lingyin "是的。"
    me01 "这是......什么意思？"
    pause 0.1 hard
    scene set only lingyin_cg one
    with dissolve
    play voice "voice/青木铃音/0508070.ogg"
    lingyin "因为我很困扰，为什么“天使”的力量会降临在你这个凡人的身上，所以就稍微观察了一下。"
    play voice "voice/青木铃音/0508080.ogg"
    lingyin "另外我确信如果是神野同学你的话是肯定不会报警的。毕竟一旦这里像观景台一样被封锁了，想要再见到她的话对你来说也会很困难的。"
    play voice "voice/青木铃音/0508090.ogg"
    lingyin "因为这里......是个充满回忆的地方嘛。"
    me01 "......"
    pause 0.1 hard
    play sound jiaobu
    scene set only lingyin_cg two
    $ flcam.move(-4400, -2800, 800, duration=3.0, warper='ease_quad')
    with dissolve
    pause 3.0 hard
    "铃音缓缓向我走来。"
    "一种不安瞬间涌上心头。"
    with vpunch
    me01 "雷亚，快逃！！！"
    pause 0.1 hard
    scene set only lingyin_cg three
    with dissolve
    stop music fadeout 5.0
    play voice "voice/青木铃音/0508100.ogg"
    lingyin "没用的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower night xuejian alpha
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5 alpha 0.7
    play music second_125 fadein 3.0 if_changed
    me01 "怎么了雷亚！就像在观景台的时候一样，消失回去啊！"
    play voice "voice/天使雷亚/0009240.ogg"
    lst "做不到......"
    show ts_lst_ssz_b1 b1 b1_s3
    play voice "voice/天使雷亚/0009250.ogg"
    lst "虽然不知道为什么。但是，做不到......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    hide snow_level1
    scene set only lingyin_cg two
    with right2left_02
    pause 1.0 hard
    play voice "voice/青木铃音/0508110.ogg"
    lingyin "我想也是。"
    pause 0.1 hard
    scene set only lingyin_cg three
    $ flcam.move(-2200, -1500, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/0508120.ogg"
    lingyin "名为雷亚的死神，如果一旦被名为“羁绊”的念波所牵引，其灵体自然就无处遁形了。"
    play voice "voice/青木铃音/0508130.ogg"
    lingyin "简单来说就是，创造了名为“羁绊”念波的神野同学你此刻，才是封锁了她逃跑可能性的罪魁祸首。"
    me01 "你说......什么......"
    me01 "雷亚，她说的这些都是真的吗？"
    play voice "voice/青木铃音/0508150.ogg"
    lingyin "就让我用这把薙刀——由{encyclopedia=yuntie}陨铁{/encyclopedia}打造的祭器来结束这一切吧。"
    me01 "快逃啊雷亚！"
    play voice "voice/青木铃音/0508160.ogg"
    lingyin "都说了这是不可能的。"
    pause 0.1 hard
    scene set only lingyin_cg two
    with dissolve
    play voice "voice/青木铃音/0508180.ogg"
    lingyin "这股力量对于我们来说是不必要的存在。"
    me01 "我说......"
    me01 "天使也好死神也罢，虽然不明白铃音同学你为什么这么痛恨她们这般的存在。"
    me01 "但是啊，雷亚她绝不是不必要的存在！"
    pause 0.1 hard
    scene set only lingyin_cg three
    with dissolve
    play voice "voice/青木铃音/0508190.ogg"
    lingyin "但她也并非如你所想像的那样，就是真实存在的实体。"
    play voice "voice/青木铃音/0508200.ogg"
    lingyin "换句话说，她就是幻觉。"
    play voice "voice/青木铃音/0508210.ogg"
    lingyin "是梦境一样的存在。"
    play voice "voice/青木铃音/0508220.ogg"
    lingyin "而这对于我们来说......就是如同噩梦一般的存在。"
    play voice "voice/青木铃音/0508230.ogg"
    lingyin "正因为是噩梦，所以才要快点醒来没错吧？"
    pause 0.1 hard
    scene set only lingyin_cg two
    with dissolve
    play voice "voice/青木铃音/0508240.ogg"
    lingyin "或许现在与你站在同一立场的姐姐也会得出和你一样的结论，可没想到连神野同学你也会如此固执。"
    play voice "voice/青木铃音/0508260.ogg"
    lingyin "既然你也见识过了她收割噩梦的能力，为什么却又不肯相信我说的话呢？"
    me01 "正因为我见证了雷亚所做的一切，我才会如此坚信。"
    me01 "雷亚她，不过是想要完成翔子的心愿而已。"
    me01 "正因为她的存在，我与翔子、还有“梦”的约定才能够实现。"
    me01 "是雷亚拯救了梦，也拯救了你的姐姐。"
    me01 "现在的翔子也是因为雷亚才......"
    pause 0.1 hard
    scene set only lingyin_cg three
    with dissolve
    play voice "voice/青木铃音/0508300.ogg"
    lingyin "你说的这些不仅是对于人类本身，乃至于万物而言都是噩梦般的存在。"
    play voice "voice/青木铃音/0508320.ogg"
    lingyin "毕竟在樱华镇的时候，作为居民的我们也都已经察觉到这股“噩梦”的力量了。"
    me01 "果然在樱华镇的那时，铃音同学你就早已经知道了雷亚的存在。"
    me01 "所以对于我和日向同学前往观景台的事情才会那么反对吧。"
    me01 "明明自己还说这些都是一些“超自然”现象的。"
    play voice "voice/青木铃音/0508330.ogg"
    lingyin "超自然？你是想说科学无法解释的吧。"
    play voice "voice/青木铃音/0508340.ogg"
    lingyin "请不要让我发笑了。"
    play voice "voice/青木铃音/0508350.ogg"
    lingyin "单纯只是科技跟不上而已吧，这些都是那帮无法踏足这片领域之人无聊的说辞罢了。"
    play voice "voice/青木铃音/0508360.ogg"
    lingyin "现在的情况也好，我手中这把能将天使送还的祭器也罢，都是真实存在于这个世界上的。"
    "有哪里不对劲，刚刚铃音身上散发出来的气息在一瞬间改变了。"
    "空气中充斥着污秽暴戾的气息。"
    "这莫非就是万夜花口中的“祟”吗......"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower night xuejian alpha
    show snow_level1 onlayer fg
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5 alpha 0.7
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/0009260.ogg"
    lst "我不知道......"
    play voice "voice/天使雷亚/0009270.ogg"
    lst "我也不清楚自己究竟是什么样的存在......"
    play voice "voice/天使雷亚/0009280.ogg"
    lst "唯一能明白的只有与凉君的约定，以及......"
    play voice "voice/天使雷亚/0009290.ogg"
    lst "和{rb}她{/rb}{rt}梦{/rt}的约定而已。"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/0009300.ogg"
    lst "所以，当凉君第一次说我是“死神”的时候。"
    play voice "voice/天使雷亚/0009310.ogg"
    lst "我真的很开心。"
    play voice "voice/天使雷亚/0009320.ogg"
    lst "本来就算不是死神也无所谓的。"
    show ts_lst_ssz_b1 b1 b1_c1
    play voice "voice/天使雷亚/0009330.ogg"
    lst "本来无论是什么都无所谓的。"
    play voice "voice/天使雷亚/0009340.ogg"
    lst "只要你能认可我的存在就好，不管那是什么......"
    pause 1.0 hard

label day206.battle_lingyin:
    $ flcam.move(0, 0, 0)
    hide snow_level1
    scene set only lingyin_cg one
    with dissolve
    play voice "voice/青木铃音/0508410.ogg"
    lingyin "这下你也明白了吧？"
    me01 "啊啊，这下我彻底明白了。"
    play voice "voice/青木铃音/0508420.ogg"
    lingyin "那能麻烦你从那里让开吗？"
    play voice "voice/青木铃音/0508430.ogg"
    lingyin "继续站在那里的话，说不定连你也会被我斩断的。"
    me01 "多亏你的话让我明白了。"
    me01 "雷亚！你是谁并不重要，此刻对我而言，你就是我最重要的伙伴。"
    me01 "我只说一遍，即使无法消失也无所谓，现在你要做的就是跑得越远越好。"
    me01 "无论我发生什么事，都不要回头。这一次我一定会......保护好你的。"
    stop music fadeout 5.0
    $ flcam.move(-2200, -1500, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/青木铃音/0508440.ogg"
    lingyin "才不会让你得逞！"
    play music second_126 fadein 3.0 if_changed
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play sound hite_knife
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lingyin_cg fite three
    with slowerdissolve
    pause 1.0 hard
    "一道斩击落下，但疼痛的感觉并未如期而至。"
    me01 "这是......"
    "凭空出现在手中的镰刀化解了迎面而来的一击。"
    "仔细一看这正是雷亚手中时常握着的那把镰刀。"
    me01 "雷亚，趁现在赶紧逃！"
    pause 0.1 hard
    scene set only lingyin_cg fite one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/0508460.ogg"
    lingyin "这把镰刀，和我手中的薙刀是一样的材质。"
    play voice "voice/青木铃音/0508470.ogg"
    lingyin "能将灵魂送还的祭器——或者说是解放灵体的道具。"
    play voice "voice/青木铃音/0508480.ogg"
    lingyin "话虽如此，两者还是有着本质上的差距。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "手上的压力增强了。"
    play voice "voice/青木铃音/0508490.ogg"
    lingyin "这把镰刀和我的薙刀不同，毕竟持有她的主人自始至终就只是虚幻的存在而已。"
    pause 0.1 hard
    scene set only lingyin_cg fite two
    with dissolve
    play voice "voice/青木铃音/0508500.ogg"
    lingyin "所以......"
    play voice "voice/青木铃音/0508510.ogg"
    lingyin "这种事也能办得到的。"
    "铃音将握住刀刃的手松开。"
    pause 0.1 hard
    scene set only lingyin_cg fite four
    $ flcam.move(500, 3200, 900, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "随即握住了镰刀那锐利的锋刃。"
    play voice "voice/青木铃音/0508520.ogg"
    lingyin "能够像这样握住却不感觉到疼痛，恰恰证明了这只是幻觉。"
    "刀刃嵌进了手掌却没有流出鲜血。"
    "从铃音的表情也丝毫看不出痛苦的样子。"
    play voice "voice/青木铃音/0508530.ogg"
    lingyin "不会痛也不会受伤，只要这样期待着就会成为现实。"
    play voice "voice/青木铃音/0508550.ogg"
    lingyin "被这把镰刀刺过却没有痛感的经历，你也有过吧？"
    pause 0.1 hard
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/青木铃音/0508590.ogg"
    lingyin "但与这把镰刀不同，我的薙刀可不是幻觉。"
    play voice "voice/青木铃音/0508600.ogg"
    lingyin "即使你祈祷着不会受伤，但还是不会如你所愿的。"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    stop music fadeout 5.0
    pause 2.0 hard
    
    $ flcam.move(0, 0, 0)
    scene set only fight_cg balltower
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        lingyin_role_mirror.pose = "wnf"
        for role in copy(local_config.party):
            role.stats_check(15)
            if role.name == "雷亚":
                temp_selected_skills, temp_selected_skills_v2 = role.skills, role.skills_v2
                before_battle_general_attack = [s for s in temp_selected_skills if s.category == "General_attack"][0]
                before_battle_general_attack_v2 = [s for s in temp_selected_skills_v2 if s.category == "General_attack"][0]
                now_battle_general_attack = copy(getattr(store, "psychokinesis-water"))
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
    call battle(boss=lingyin_role_mirror, 
                boss_hp_plus=5000, 
                side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3], 
                side_hp_plus=0, 
                level=15, 
                boss_first=True, 
                win_condition='normal', 
                stay_turn=0, 
                inside_label="inside_battle3", 
                mission_type="normal", 
                treasures={"eggs": (3, 0.5)})

    if _return == "win":
        "战斗胜利！"
        python:
            for role in local_config.party:
                if role.name == "雷亚":
                    role.skills = [s if s.category != "General_attack" else before_battle_general_attack for s in role.skills]
                    role.base_skills = role.skills
                    role.skills_v2 = [s if s.category != "General_attack" else before_battle_general_attack_v2 for s in role.skills_v2]
                    role.base_skills_v2 = role.skills_v2
            if "lingyin_role" not in local_config.role_pool:
                local_config.role_pool.add("lingyin_role")

        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day206.after_battle_lingyin

label day206.after_battle_lingyin:
    scene black
    with dissolve
    pause 1.0 hard
    play music second_126 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only lingyin_cg fite four
    pause 1.0 hard
    "铃音突然泄去了手中的力道。"
    "由于突然的重心变化，我失去平衡向前倾倒。"
    "而她则是以一记灵活的身法躲过了迎面扑来的我。"
    "并迅速用刀柄砸向了我的腹部。"
    play sound punch
    with vpunch
    pause 0.5 hard
    scene black 
    with dissolve
    pause 1.0 hard
    "被这沉重的一击打倒在地的我。"
    "此时整个腹部正隐隐作痛，好在对方用的是刀柄而没有造成致命伤。"
    "然而即便如此，疼痛感却如同洪水一般不断涌向全身。"
    "压倒性的实力差距。"
    "我想要站起来，但是身体却不争气地瘫软在地。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lingyin_cg three
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/0508620.ogg"
    lingyin "就请你在那里老实待着吧。"
    "铃音将我身旁的镰刀踢到了一边。"
    "然后径直向雷亚的方向走去。"
    pause 0.1 hard
    scene set only lingyin_cg two
    with dissolve
    play voice "voice/青木铃音/0508630.ogg"
    lingyin "因为姐姐的关系说实话我并不希望加害于你。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower night xuejian
    show snow_level1 onlayer fg
    show ts_lst_ssz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5 alpha 0.7
    with dissolve
    pause 0.5 hard
    show lingyin_wnf_b1 b1 b1_a1 onlayer screens at side_left('lingyin', 0.0), basicfade
    play voice "voice/青木铃音/0508610.ogg"
    lingyin "那么......"
    hide lingyin_wnf_b1
    show ts_lst_ssz_b2 b2 b2_c2
    play voice "voice/天使雷亚/0009410.ogg"
    lst "凉君他明明......是我的朋友，明明是我的朋友。"
    play voice "voice/天使雷亚/0009420.ogg"
    lst "第一次靠自己交到的，重要的朋友。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(-2200, -1500, 450)
    scene set only lingyin_cg three
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/0508680.ogg"
    lingyin "是吗......"
    play voice "voice/青木铃音/0508690.ogg"
    lingyin "朋友......"
    pause 0.1 hard
    scene set only lingyin_cg two
    with dissolve
    play voice "voice/青木铃音/0508700.ogg"
    lingyin "只要看着你们，自己就会变得急躁起来。"
    play voice "voice/青木铃音/0508710.ogg"
    lingyin "这么轻易地就说朋友什么的......"
    pause 0.1 hard
    scene set only lingyin_cg one
    $ flcam.move(-4400, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/0508730.ogg"
    lingyin "明明连自己是什么东西都不明白！"
    pause 1.0 hard
    scene white 
    with slowdissolve
    stop music fadeout 5.0
    pause 1.0 hard
    play sound hite_knife2
    pause 2.0 hard
    "最后只听到薙刀划过空气的声音。"
    "接下来便是一片沉寂。"
    pause 1.0 hard
    play music first_24 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(2800, 3600, 1100)
    scene set only lingyin_cg final one
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    play voice "voice/翔子/0208140.ogg"
    xz "......很痛的啊。"
    "翔子的身影出现在了铃音的身后。"
    "她用手紧紧地握住了挥舞到一半的薙刀。"
    "也就在这一刻鲜血迸溅而出。"
    play voice "voice/翔子/0208150.ogg"
    xz "真是......痛得让人想要哭出来了。"
    play voice "voice/翔子/0208160.ogg"
    xz "即使祈祷着不会痛，但果然还是会痛的。"
    play voice "voice/青木铃音/0508740.ogg"
    lingyin "这、这不是当然的吗......"
    play voice "voice/青木铃音/0508750.ogg"
    lingyin "这可是......真的啊。"
    play voice "voice/翔子/0208170.ogg"
    xz "我知道。"
    pause 0.1 hard
    scene set only lingyin_cg final two
    with dissolve
    play voice "voice/翔子/0208180.ogg"
    xz "祭典的时候我可是用它跳的舞嘛。"
    pause 0.1 hard
    scene set only lingyin_cg final four
    with dissolve
    play voice "voice/青木铃音/0508760.ogg"
    lingyin "既然知道......就赶紧放开啊，姐姐！"
    play voice "voice/翔子/0208190.ogg"
    xz "做不到呢。"
    play voice "voice/青木铃音/0508770.ogg"
    lingyin "这不是做不做得到的问题，不赶快放开的话姐姐的手会......"
    pause 0.1 hard
    scene set only lingyin_cg final three
    with dissolve
    play voice "voice/翔子/0208200.ogg"
    xz "比起这个。"
    play voice "voice/翔子/0208210.ogg"
    xz "你到底在干什么，铃音！"
    play voice "voice/翔子/0208220.ogg"
    xz "运动神经那么差的你，却挥舞着这种东西！"
    pause 0.1 hard
    scene set only lingyin_cg final one
    with dissolve
    play voice "voice/青木铃音/0508780.ogg"
    lingyin "那、那是......"
    pause 0.1 hard
    scene set only lingyin_cg final five
    with dissolve
    play voice "voice/青木铃音/0508790.ogg"
    lingyin "为了帮助姐姐完成星天宫巫女的使命......所以无关运动神经我也必须要试试看。"
    play voice "voice/翔子/0208230.ogg"
    xz "才不想要听那种无聊的理由笨蛋！"
    play voice "voice/青木铃音/0508800.ogg"
    lingyin "姐姐你也见过观景台的“她”了对吧？"
    play voice "voice/翔子/0208240.ogg"
    xz "好像是这样的。"
    play voice "voice/青木铃音/0508810.ogg"
    lingyin "果然你也被噩梦影响了不是吗？"
    play voice "voice/翔子/0208250.ogg"
    xz "也不像你说的那么严重。"
    play voice "voice/青木铃音/0508811.ogg"
    lingyin "那现在你会觉得痛苦吗？"
    play voice "voice/翔子/0208270.ogg"
    xz "或许有一点吧。"
    play voice "voice/青木铃音/0508830.ogg"
    lingyin "赶快离开这里不好吗......"
    pause 0.1 hard
    scene set only lingyin_cg final six
    with dissolve
    play voice "voice/翔子/0208290.ogg"
    xz "可以的话我也是这么想的。"
    play voice "voice/翔子/0208300.ogg"
    xz "我可是从刚才开始就觉得浑身难受，真是糟糕透了。"
    pause 0.1 hard
    scene set only lingyin_cg final four
    with dissolve
    play voice "voice/青木铃音/0508840.ogg"
    lingyin "那就快点离开这里！"
    play voice "voice/翔子/0208320.ogg"
    xz "不是说了做不到了吗！"
    play voice "voice/青木铃音/0508850.ogg"
    lingyin "够了，痛苦的话就快点离开！"
    pause 0.1 hard
    scene set only lingyin_cg final three
    with dissolve
    play voice "voice/翔子/0208330.ogg"
    xz "要我说多少遍你才会明白！"
    play voice "voice/翔子/0208340.ogg"
    xz "我说过做不到就是做不到，你只管听我的就是了！"
    play voice "voice/翔子/0208350.ogg"
    xz "不然的话，对坏孩子要好好修理才行。"
    pause 0.1 hard
    scene set only lingyin_cg final three
    with dissolve
    play voice "voice/青木铃音/0508860.ogg"
    lingyin "请、请住手！"
    play voice "voice/翔子/0208360.ogg"
    xz "你先放弃的话，我就松手。"
    pause 0.1 hard
    scene set only lingyin_cg final five
    with dissolve
    play voice "voice/青木铃音/0508870.ogg"
    lingyin "请不要说这种孩子气的蠢话了。"
    play voice "voice/翔子/0208370.ogg"
    xz "愚蠢的是你吧，整这一出幼稚的闹剧真是让人火大。"
    pause 0.1 hard
    scene set only lingyin_cg final three
    with dissolve
    play voice "voice/青木铃音/0508880.ogg"
    lingyin "我才不是小孩子！"
    play voice "voice/青木铃音/0508890.ogg"
    lingyin "她是本就不该出现在这里的！"
    play voice "voice/翔子/0208380.ogg"
    xz "即使如此，我也要阻止你。"
    play voice "voice/青木铃音/0508900.ogg"
    lingyin "为什么啊！"
    play voice "voice/翔子/0208390.ogg"
    xz "因为其实你也不想做这种事的。"
    pause 0.1 hard
    scene set only lingyin_cg final one
    with dissolve
    play voice "voice/青木铃音/0508910.ogg"
    lingyin "......"
    play voice "voice/青木铃音/0508920.ogg"
    lingyin "为什么......你会这么认为？"
    play voice "voice/翔子/0208400.ogg"
    xz "因为你在哭啊！"
    play voice "voice/青木铃音/0508930.ogg"
    lingyin "眼泪什么的......我才没有。"
    play voice "voice/翔子/0208410.ogg"
    xz "你的心在哭泣，我能看见的。"
    pause 0.1 hard
    scene set only lingyin_cg final five
    with dissolve
    play voice "voice/青木铃音/0508940.ogg"
    lingyin "这一定是......你的幻觉。"
    pause 0.1 hard
    scene set only lingyin_cg final six
    with dissolve
    play voice "voice/翔子/0208430.ogg"
    xz "就算是幻觉，我也是知道的。"
    play voice "voice/翔子/0208440.ogg"
    xz "即使是幻觉也曾在某一刻真实存在过。"
    play voice "voice/翔子/0208460.ogg"
    xz "即使刻意隐瞒，却也通过这把薙刀传达过来了。"
    pause 0.1 hard
    scene set only lingyin_cg final five
    with dissolve
    play voice "voice/翔子/0208470.ogg"
    xz "你的身体颤抖得比我还要厉害。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene white
    with slowerdissolve
    pause 2.0 hard
    play music second_157 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lingyin_cg kiss one
    with dissolve
    "那一刻，手中的薙刀滑落在了地上。"
    pause 0.1 hard
    scene set only lingyin_cg kiss two
    with dissolve
    play voice "voice/翔子/0208480.ogg"
    xz "我又怎会不明白呢。"
    play voice "voice/翔子/0208490.ogg"
    xz "我们不是已经约好了吗，决不要对身为姐姐的我有所隐瞒。"
    play voice "voice/翔子/0208500.ogg"
    xz "在烦恼些什么。"
    play voice "voice/翔子/0208510.ogg"
    xz "你到底在忍受些什么。"
    play voice "voice/翔子/0208520.ogg"
    xz "求求你了，告诉我吧。"
    play voice "voice/翔子/0208530.ogg"
    xz "即使现在不说也没有关系。"
    play voice "voice/翔子/0208540.ogg"
    xz "但是总有一天也请你一定要告诉我。"
    play voice "voice/翔子/0208550.ogg"
    xz "不然的话，我是不会原谅你的。"
    pause 0.1 hard
    scene set only lingyin_cg kiss four
    with dissolve
    play voice "voice/青木铃音/0508950.ogg"
    lingyin "姐姐你......好残忍。"
    play voice "voice/青木铃音/0508960.ogg"
    lingyin "真是非常地......残忍。"
    play voice "voice/青木铃音/0508970.ogg"
    lingyin "我已经开始，有些讨厌姐姐你了。"
    pause 0.1 hard
    scene set only lingyin_cg kiss three
    with dissolve
    play voice "voice/翔子/0208560.ogg"
    xz "那样的话或许也不错呢~"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    "铃音靠在翔子的怀里哭了。"
    "就像是绷紧的弦突然断了一样，整个身子都松弛了下来。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    show xz_xsf_b1 b1 b1_s3 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/0208580.ogg"
    xz "......到头来还是哭了啊。"
    show xz_xsf_b1 b1 b1_s2
    play voice "voice/翔子/0208590.ogg"
    xz "从以前开始，铃音就是一个爱撒娇的孩子。我不理会她的话就会躲起来哭。"
    show xz_xsf_b1 b1 b1_s1
    play voice "voice/翔子/0208600.ogg"
    xz "那个时候我就会四下寻找，像这样安抚着她。"
    show xz_xsf_b1 b1 b1_s2
    play voice "voice/翔子/0208610.ogg"
    xz "嘛，虽然以前也只有亲额头的程度。"
    show xz_xsf_b1 b1 b1_ga3
    play voice "voice/翔子/0208620.ogg"
    xz "像这样的安慰......还是第一次呢。"
    show xz_xsf_b1 b1 b1_n2
    play voice "voice/翔子/0208650.ogg"
    xz "神野君......"
    play voice "voice/翔子/0208660.ogg"
    xz "可以的话，请不要对任何人说起这件事。"
    hide xz_xsf_b1
    pause 1.0 hard
    scene set only balltower night xuejian alpha
    with dissolve
    pause 1.0 hard
    me01 "翔子你的手......"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_xsf_b1 b1 b1_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0208670.ogg"
    xz "没事的，虽然流了点血但伤口没有看起来的那么严重。"
    "她取出手帕压住手心。"
    pause 1.0 hard
    inventory add blood_handkerchief
    pause 2.0 hard
    "一瞬间的功夫布料就被染红了。"
    me01 "虽然现在才说有点不太好，但是你也太乱来了！"
    hide xz_xsf_b1
    show xz_xsf_b2 b2 b2_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0208690.ogg"
    xz "对恩人你说什么呢。"
    me01 "这份恩情我一定会偿还的。"
    hide xz_xsf_b2
    show xz_xsf_b1 b1 b1_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0208700.ogg"
    xz "总是欠人情的你到什么时候才能还清呢~"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    me01 "总之，现在就让我来帮你把伤口包扎下吧。"
    hide xz_xsf_b1
    show xz_xsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0208710.ogg"
    xz "嗯。"
    me01 "爱衣那边交给我，现在先带你去医院吧。"
    hide xz_xsf_b3
    show xz_xsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0208720.ogg"
    xz "不要以为这样子......恩情就能抵消了。"
    me01 "我知道的，即使花费一生我也会弥补的。"
    me01 "铃音同学现在怎么样？"
    hide xz_xsf_b1
    show xz_xsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0208730.ogg"
    xz "应该是灵力使用过度加上情绪激动的缘故，现在睡着了。"
    me01 "是这样的话就太好了。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    "幻觉吗......"
    "雷亚也好、“梦”也罢，就算是幻觉也没有关系。"
    "即便无法打破量子的束缚，但我相信她们依旧是真实存在着的。"
    "无论何时都不要放弃。"
    "哪怕是会为此付出生命的代价也在所不惜。"
    "这是翔子不顾安危也要向我传达的事情。"    
    "无论何时，我们始终都是一家人。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day206.memory01:
    show dreamglass1 onlayer texture with slowerdissolve
    nvl clear
    nvl_narrator "　又是这里......"
    nvl_narrator "　已经记不清是第几次了。"
    pause 1.0 hard
    nvl clear
    hide dreamglass2
    with slowerdissolve
    pause 2.0 hard

label day206.ritroom:
    default seen_day206_ritroom = False
    play music ritroom_day fadein 3.0 if_changed
    play ambience1 ritroom_fireplace fadein 3.0 if_changed

    if not seen_day206_ritroom:
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
        ritona "吼呀，今天怎么有兴致来这里了？"
        me01 "弗兰小姐之前也说过的吧，以后这里就是我的修炼场所之类的话。"
        show ritona b1 fb4 fa2 fc11 s
        ritona "欸......我说过吗？"
        me01 "那个，你也差不多该对自己说过的话负责了吧。"
        show ritona b1 fb4 fa1 fc11 s
        ritona "所以，究竟发生了什么？"
        me01 "扯开话题还是一如既往的在行啊......"
        show ritona b1 fb4 fa2 fc13 s
        ritona "......"
        me01 "其实是在最近的战斗过程中我重要的伙伴受伤了。"
        me01 "我认为都是因为我没有足够的力量保护她们，才会让她们为了我受伤。"
        show ritona b3 fb5 fa1 fc02
        ritona "......"
        me01 "弗兰小姐？"
        show ritona b1 fb1 fa5 fc02
        ritona "虽然很想吐槽你的“弱”，但似乎当时的情况也确实不能怪你。"
        me01 "......"
        show ritona b1 fb5 fa9 fc11
        ritona "干嘛用那种眼神看着我？"
        me01 "不，我只是在想弗兰小姐偶尔也会说些不错的话嘛。"
        me01 "话说配音什么的不能想想办法吗。"
        show ritona b1 fb4 fa2 fc11 s
        ritona "要、要你管！" with vpunch
        ritona "没有配音的角色一样也是有灵魂的！！！"
        me01 "好的好的我知道了，你先别激动。"
        show ritona b1 fb1 fa2 fc15 s
        ritona "总、总之，当务之急就是帮你摆脱被动挨打的尴尬境地，我特地为你准备了一些好东西。"
        me01 "什么东西？"
        show ritona b1 fb4 fa1 fc02 s
        $ flcam.move(-4980, 2610, 850, duration=1.5)
        ritona "就是这个！"
        play sound egg_reveal
        show white onlayer texture
        hide ritroom-eggscover
        pause 1.0 hard
        hide white
        $ flcam.move(-5500, 3000, 1200)
        with Dissolve(1.5)
        pause 0.5 hard
        me01 "这......这难道是？！"
        ritona "哼哼哼~"
        ritona "你想的没错，这就是......"
        $ flcam.move(-5500, 2900, 1350, duration=0.75)
        me01 "RPG游戏中一定会出现的能够恢复角色元气的招牌道具——煮鸡蛋吗？！" with vpunch
        $ flcam.move(-1300, -1000, 1150, duration=0.5)
        show ritona b3 fb1 fa0 fc13 s
        ritona "......你这突然的开窍让我这个充当解说的npc很为难啊。"
        me01 "{size=+6}我懂的，无论在哪个时代，展开冒险之前的准备都是很重要的吧。{/size}"
        ritona "不，等等......"
        me01 "{size=+8}但是，这些东西可不是白拿的，一定有什么严酷的考验在等待着我。{/size}"
        ritona "所以说......"
        me01 "{size=+15}事不宜迟，为了变强我什么都愿意做！{/size}"
        $ flcam.move(-1185, -1065, 1220, duration=0.5)
        show ritona b3 fb1 fa0 fc15 s
        ritona "{size=+25}所以说给我冷静一点啊！！！{/size}" with vpunch
        show ritona b1 fb1 fa0 fc12 s
        ritona "听好了，这些可不是普通的鸡蛋。"
        show ritona b1 fb1 fa4 fc13 s
        ritona "全都是被我改良过的——上乘的鸡蛋。"
        me01 "本来还在期待着会孵出高级生物这样的设定，这不还是鸡蛋吗？！"
        show ritona b1 fb1 fa5 fc13 s
        ritona "高级生物？不得不说你的脑洞才是最让我感到惊讶。"
        show ritona b9 fb1 fa1 fc12 s
        ritona "听好了，通过向鸡蛋内注入不同元素的灵力，就能大幅提升鸡蛋的功效。"
        ritona "例如采用火属性对鸡蛋进行加热的话，就会激活里面蕴含的灵基物质。"
        ritona "服用的时候不但效果显著，而且更加鲜美入味......"
        me01 "也就是说煮熟了更好吃对吧？"
        $ flcam.move(-1185, -1065, 1240, duration=0.5)
        show ritona b9 fb1 fa2 fc11 s
        ritona "......"
        me01 "{cps=*0.5}………………………………………………………{w=1.0}{/cps}{nw}"
        extend "弗兰小姐？"
        $ flcam.move(-1085, -1165, 1300, duration=0.75)
        show ritona b9 fb1 fa2 fc13 s
        ritona "你这么一说好像确实......"
        me01 "搞了半天只是煮个鸡蛋而已吗？！" with vpunch
        $ flcam.move(-1185, -1065, 1140, duration=0.75)
        show ritona b9 fb3 fa5 fc13 s
        ritona "总、总之我向你推荐的东西绝对不会错的。"
        me01 "总觉得有点可疑啊......"
        show ritona b9 fb3 fa5 fc12
        ritona "行了别吐槽了，你看因为你的关系这鸡蛋都凉透了。"
        me01 "{size=+25}这是我的问题吗？！{/size}" with vpunch
        pause 0.5 hard
        scene black with dissolve
        pause 3.0 hard
        scene set ritroom day:
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
        show item-egg x3 onlayer m1:
            xpos 0.26
            xanchor 0.5
            ypos 0.65
            zoom 0.24
        show ritona b3 fb1 fa5 fc02 onlayer m2:
            xpos 0.5
        $ flcam.move(-5400, -100, 400)
        $ flcam.move(-5300, -100, 600, duration=1.5)
        with dissolve
        me01 "那么，应该怎么做才能获得煮......不对是魔法鸡蛋呢？"
        show ritona b3 fb1 fa5 fc11
        ritona "煮......哦不对，魔法鸡蛋制作的精髓在于对灵力的把控。"
        show ritona b3 fb1 fa5 fc12
        ritona "首先先试看看向鸡蛋内注入你擅长的{rb}灵纹{/rb}{rt}rune{/rt}力吧。"
        me01 "我、我知道了。"
        $ flcam.move(-5300, -100, 700, duration=0.5)
        "为什么有种被忽悠了的感觉......"
        show ritona b3 fb1 fa0 fc02
        $ flcam.move(-5400, -100, 400, duration=1.5)
        "尝试合成魔法（？）鸡蛋。"
        $ flcam.stop()
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
        show hintarrow onlayer m1:
            xpos 0.26
            ypos 0.65
        show screen investigation_popup(investigation.hint1)
        $ seen_day206_ritroom = True
        $ local_config.shop_list = ["eggs"]
    else:
        pause 0.5 hard
        scene black with dissolve
        pause 3.0 hard
        scene set ritroom day:
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
        show item-egg x3 onlayer m1:
            xpos 0.26
            xanchor 0.5
            ypos 0.65
            zoom 0.24
        show ritona b3 fb1 fa0 fc02 onlayer m2:
            xpos 0.5
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-14575.0), scale(-0.0), 0.0) to (scale(+14575.0), scale(+0.0), 1350.0)
        menu ritona onlayer m2:
            camera_pos (scale(-4140), scale(-1010), 800)
            screen_pos (0.5, 1.0)
            screen_direction left
            sleep jump day206.sleep
            shop jump day206.shop
            member jump day206.stats
            teleport jump day206.teleport
            callback jump day206.callback
            roleroom jump day206.roleroom
        object item-egg onlayer m1 jump day206.look_eggs:
            showif (not seen_day206_look_eggs)

label day206.look_eggs:
    default use_boiled_egg = False
    default seen_day206_look_eggs = False
    $ seen_day206_look_eggs = True
    $ flcam.move(-2985, -840, 1000, duration=1.5)
    hide hintarrow
    hide screen investigation_popup
    window mode thought
    show ritona b9 fb1 fa5 fc03
    ritona "这些是早上刚买的新鲜鸡蛋。"
    window mode thought
    ritona "你就试着拿它们进行练习吧。"
    show ritona b9 fa3 fc03
    ritona "顺带一提这些都是我今天的食材，你要是胆敢浪费的话......"
    "咽口水......"
    window mode thought
    me01 "通过「物品」-「鸡蛋」-「使用」进行魔法鸡蛋的炼制。"
    show ritona b3 fb1 fa0 fc03
    pause 0.5 hard
    $ flcam.stop()
    $ flcam.move(-5805, 3015, 1200, duration=1.5)
    show item-egg x2:
        "item-egg x3"
        0.5
        "item-egg x2" with dissolve
    pause 1.0 hard
    inventory add egg raw
    pause 1.0 hard
    hide screen iv_item_notify
    $ flcam.stop()
    $ camera_move(-4700, 100, 600, duration=1.5)
    pause 0.5 hard
    show screen investigation_popup(investigation.hint2)
    jump investigate
    
label day206.examine_egg:
    default seen_examine_egg = 0
    $ flcam.start()
    hide screen investigation_popup
    if seen_examine_egg == 0:
        window mode thought
        show ritona b9 fb1 fa0 fc02
        ritona "不同的{rb}灵纹{/rb}{rt}rune{/rt}拥有不同的灵力属性。"
        window mode thought
        ritona "想要驾驭好灵力首先必须学会如何控制。"
        window mode thought
        ritona "鸡蛋光滑的表面会对灵力的流动产生干扰，这也是一种很好的试炼。"
    elif seen_examine_egg == 1:
        window mode thought
        show ritona b9 fb1 fa0 fc03
        ritona "太过刚猛的灵力会让鸡蛋破碎，而太过柔弱的灵力又会流失鸡蛋的养分。"
        window mode thought
        ritona "可别小看了煮鸡蛋这一平凡的举动。"
    else:
        window mode thought
        show ritona b9 fb1 fa3 fc02
        ritona "剩下的东西就靠你自己摸索了。"
        window mode thought
        ritona "以上。"
    show ritona b3
    $ flcam.stop()
    pause 0.5 hard
    $ seen_examine_egg += 1
    jump investigate

label day206.use_egg:
    $ flcam.move(-2010, -760, 1000, duration=1.5)
    hide investigation_popup
    window mode thought
    show ritona b9 fb1 fa5 fc02
    ritona "好的，那就让我们开始吧。"
    window mode thought
    show ritona b9 fb1 fa1 fc02
    ritona "把它握在手中注入灵力。"
    show callflash onlayer texture
    pause 1.0 hard
    hide callflash
    window mode thought
    show ritona b3 fb1 fa0 fc02
    inventory add egg boiled
    $ flcam.stop()
    $ camera_move(-4700, 100, 600, duration=1.5)
    pause 0.5 hard
    window mode thought
    me01 "通过「物品」-「魔法鸡蛋」-「使用」查看自己炼制的魔法鸡蛋。"
    jump investigate

label day206.use_boiled_egg:
    $ camera_push()
    $ flcam.move(-2985, -840, 1000, duration=1.5)
    show ritona b3 fb1 fa1 fc02
    ritona "......"
    window mode thought
    ritona "没想到我只是口头上描述一下就被学会了。"
    window mode thought
    show ritona b3 fb1 fa3 fc03
    ritona "这家伙，还是有点意思的。"
    window mode thought
    show ritona b3 fb1 fa1 fc03
    ritona "也许，这就是命运也说不定啊......"
    $ flcam.stop()
    $ camera_pop_move(duration=1.5)
    pause 0.5 hard
    $ use_boiled_egg = True
    python:
        local_config.shop_list += ["mana_eggs", "soul_mirro"]
    jump investigate

label day206.callback:
    default seen_day206_callback = False
    hide screen investigation_popup
    scene black
    pause 1.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg msk
    with slowdissolve
    pause 0.5 hard

    python:
        can_get_roles = "、".join(["「{}」".format(getattr(store, obj).name) for obj in local_config.role_pool])
        outfits_level1 = [outfit for outfit in outfit_list if "_01" in outfit.objectname]
        outfits_level2 = [outfit for outfit in outfit_list if "_02" in outfit.objectname]
        outfits_level3 = [outfit for outfit in outfit_list if "_03" in outfit.objectname]
        outfits_level4 = [outfit for outfit in outfit_list if "_04" in outfit.objectname]

        equip_is_full = local_config.player.is_equipments_full(recall=1)
        equip_is_full_10 = local_config.player.is_equipments_full(recall=10)

    if not seen_day206_callback:
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
        show ritona b9 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)
        window mode thought
        ritona "这里是时空裂缝，也是我们往返异时空的必经之地。"
        window mode thought
        ritona "一起邂逅更多的羁绊吧。"
        window mode thought
        ritona "当前可抽取的角色包括[can_get_roles]"
        show ritona b3
        pause 0.15 hard
        show ritona b3 at walkout_r(0.75)
        pause 0.5 hard
        hide ritona b3
        $ flcam.move(0, 0, 0, duration=1.5)
        pause 0.5 hard

        show white onlayer texture:
            additive 1
            alpha 0
            1.75
            linear 0.25 alpha 1
        pause 5.0 hard

        $ seen_day206_callback = True

    stop music fadeout 2.0
    pause 1.0 hard
    hide white
    $ mouse_visible = False
    $ _skipping = renpy.seen_audio("video/second_op.mp4")
    $ config.skipping = None
    scene black
    show movie onlayer master
    # if not seen_206_callback:
    play movie "video/second_op.mp4" loop
    play music "video/second_op.mp3" loop
    $ seen_day206_callback_tutorial = False
    # $ renpy.music.play("video/second_op.mp3", synchro_start='movie', loop=True)
    
    pause 5.0 hard
    # else:
    #     play movie "<from 24.0>video/df_op.webm" loop
    #     pause 2.0 hard
    $ _window_animation = 'in'
    $ mouse_visible = True

    while True:
        $ detect_drop = False
        $ drag_name = ""

        menu:
            "召唤":
                if equip_is_full:
                    window mode thgouth
                    me01 "装备栏已接近上限，优先清理一下无用道具防止装备无法获取的情况出现。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day206.ritroom
                elif local_config.player.currency >= 160:
                    $ local_config.player.currency -= 160
                    
                    while not detect_drop:
                        if not seen_day206_callback_tutorial:
                            show screen investigation_popup(investigation.hint3)
                            $ seen_day206_callback_tutorial = True
                        call screen send_detective_screen

                    show pooler_move:
                        xalign 0.5
                        yalign 0.35

                    # call screen input_sentence
                    # $ sentence = _return.strip()

                    hide screen investigation_popup
                    pause 0.5 hard
                    show wflash onlayer m2
                    play sound chain_voice
                    show chain1 with vpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain2 with hpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain3 with vpunch
                    pause 0.25 hard
                    show wflash onlayer m2
                    play ambience1 pent_charge fadein 1.0
                    show cut_pentblack:
                        xalign 0.5 yalign 0.5
                        zoom 0
                        rotate 0
                        parallel:
                            ease 0.3 zoom 1.0
                        parallel:
                            linear 4.0 rotate 360
                            repeat
                    pause 2.0 hard
                    show white onlayer screens
                    with slowdissolve
                    pause 2.0 hard
                    hide chain1
                    hide chain2
                    hide chain3
                    hide cut_pentblack
                    hide white
                    stop ambience1 fadeout 2.0

                    python:
                        sp_ratio = renpy.random.random()
                        # 角色
                        if sp_ratio <= persistent.ratio_table["role"]:
                            chosen_member_idx = renpy.random.randint(0, len(local_config.role_pool) - 1)
                            chosen_member_objectname = list(local_config.role_pool)[chosen_member_idx]
                            chosen_member = getattr(store, chosen_member_objectname)
                            chosen_name = chosen_member.name

                            renpy.pause(1.0, hard=True)
                            renpy.show("black", layer="f2")
                            renpy.transition(dissolve)
                            renpy.pause(1.0, hard=True)
                            renpy.hide("black", layer="f2")
                            renpy.show("sp_ani_role", layer="screens")
                            renpy.music.play("video/ms2_portal.mp3", synchro_start='movie', channel='sound', loop=False)
                            renpy.pause(0.4)
                            renpy.hide("sp_ani_role", layer="screens")
                            renpy.show("black", layer="f2")
                            renpy.transition(dissolve)
                            renpy.pause(3.0, hard=True)
                            renpy.hide("black", layer="f2")

                            renpy.show(chosen_member.objectname, at_list=[show_player(0.5)], layer="m2")
                            renpy.pause(1.0, hard=True)

                            renpy.say(chosen_name, "我的名字是「[chosen_name]」")
                            renpy.say(chosen_name, "以后请多多指教~")

                            # 已拥有角色：技能等级加1
                            if chosen_name in [obj.name for obj in (local_config.party + local_config.backup)]:
                                for role in local_config.party + local_config.backup:
                                    if role.name == chosen_name:
                                        if any(s.level < 5 for s in role.skills):
                                            selectup_skill = role.skill_levelup()
                                            renpy.say(chosen_name, "技能「[selectup_skill.name]」强化至Lv.[selectup_skill.level]")
                                        else:
                                            local_config.player.currency += 1500
                                        break
                            # 未拥有角色：加入后补队伍
                            elif chosen_name in [getattr(store, obj).name for obj in local_config.role_pool]:
                                local_config.backup.append(chosen_member)
                                renpy.say(chosen_name, "「[chosen_name]」加入队伍")
                            else:
                                local_config.player.currency += 1500

                            renpy.hide(chosen_member.objectname, layer="m2")
                            renpy.pause(0.75, hard=True)
                        # # 道具
                        # elif sp_ratio <= persistent.ratio_table["items"]:
                        #     chosen_item_idx = renpy.random.randint(0, len(local_config.shop_list) - 1)
                        #     chosen_item_objectname = local_config.shop_list[chosen_item_idx]
                        #     chosen_item = getattr(store, chosen_item_objectname)
                        #     chosen_item.get(who=local_config.player)
                        #     chosen_name = chosen_item.name

                        #     if chosen_item.image not in [None, ""]:
                        #         if chosen_item.image == "item01":
                        #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.7, xalign=0.5, yalign=0.5)], layer="m2")
                        #         else:
                        #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.3, xalign=0.5, yalign=0.5)], layer="m2")
                        #         renpy.pause(1.0, hard=True)

                        #     renpy.say(chosen_name, "获得物品「[chosen_name]」")

                        #     renpy.hide(chosen_item.image, layer="m2")
                        #     renpy.pause(0.75, hard=True)
                        # 装备
                        else:
                            if renpy.random.random() <= 0.25:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level1) - 1)
                                chosen_equip = outfits_level1[chosen_equip_idx]
                            elif renpy.random.random() <= 0.5:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level2) - 1)
                                chosen_equip = outfits_level2[chosen_equip_idx]
                            elif renpy.random.random() <= 0.75:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level3) - 1)
                                chosen_equip = outfits_level3[chosen_equip_idx]
                            else:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level4) - 1)
                                chosen_equip = outfits_level4[chosen_equip_idx]
                            
                            chosen_equip_objectname = chosen_equip.objectname
                            chosen_equip.get(who=local_config.player)
                            chosen_name = chosen_equip.name
                            
                            renpy.show(chosen_equip_objectname, at_list=[Transform(zoom=1.0, xalign=0.5, yalign=0.5)], layer="m2")
                            renpy.pause(1.0, hard=True)

                            equip_level = ""
                            if "_01" in chosen_equip_objectname:
                                equip_level = "普通"
                            elif "_02" in chosen_equip_objectname:
                                equip_level = "稀有"
                            elif "_03" in chosen_equip_objectname:
                                equip_level = "史诗"
                            else:
                                equip_level = "传说"
                            renpy.say(me01, "获得「[equip_level]」[chosen_equip.category]「[chosen_name]」")

                            renpy.hide(chosen_equip_objectname, layer="m2")
                            renpy.pause(0.75, hard=True)

                    hide pooler_move
                else:
                    window mode thought
                    me01 "魔法币不足500是无法进入异空间的，无论在哪个世界穷是永远的痛！"
                    me01 "快去「异界」获取更多魔法币吧。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day206.ritroom
            "十连召唤":
                if equip_is_full_10:
                    window mode thgouth
                    me01 "装备栏已接近上限，优先清理一下无用道具防止装备无法获取的情况出现。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day206.ritroom
                elif local_config.player.currency >= 1500:
                    $ local_config.player.currency -= 1500

                    while not detect_drop:
                        if not seen_day206_callback_tutorial:
                            show screen investigation_popup(investigation.hint3)
                            $ seen_day206_callback_tutorial = True
                        call screen send_detective_screen

                    show pooler_move:
                        xalign 0.5
                        yalign 0.35

                    # call screen input_sentence
                    # $ sentence = _return.strip()

                    hide screen investigation_popup
                    pause 0.5 hard
                    show wflash onlayer m2
                    play sound chain_voice
                    show chain1 with vpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain2 with hpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain3 with vpunch
                    pause 0.25 hard
                    show wflash onlayer m2
                    play ambience1 pent_charge fadein 1.0
                    show cut_pentblack:
                        xalign 0.5 yalign 0.5
                        zoom 0
                        rotate 0
                        parallel:
                            ease 0.3 zoom 1.0
                        parallel:
                            linear 4.0 rotate 360
                            repeat
                    pause 2.0 hard
                    show white onlayer screens
                    with slowdissolve
                    pause 2.0 hard
                    hide chain1
                    hide chain2
                    hide chain3
                    hide cut_pentblack
                    hide white
                    stop ambience1 fadeout 2.0
                    
                    python:
                        for i in xrange(10):
                            sp_ratio = renpy.random.random()
                            # 角色
                            if sp_ratio <= persistent.ratio_table["role"]:
                                chosen_member_idx = renpy.random.randint(0, len(local_config.role_pool) - 1)
                                chosen_member_objectname = list(local_config.role_pool)[chosen_member_idx]
                                chosen_member = getattr(store, chosen_member_objectname)
                                chosen_name = chosen_member.name

                                renpy.pause(1.0, hard=True)
                                renpy.show("black", layer="f2")
                                renpy.transition(dissolve)
                                renpy.pause(1.0, hard=True)
                                renpy.hide("black", layer="f2")
                                renpy.show("sp_ani_role", layer="screens")
                                renpy.music.play("video/ms2_portal.mp3", synchro_start='movie', channel='sound', loop=False)
                                renpy.pause(0.4)
                                renpy.hide("sp_ani_role", layer="screens")
                                renpy.show("black", layer="f2")
                                renpy.transition(dissolve)
                                renpy.pause(3.0, hard=True)
                                renpy.hide("black", layer="f2")

                                renpy.show(chosen_member.objectname, at_list=[show_player(0.5)], layer="m2")
                                renpy.pause(1.0, hard=True)

                                renpy.say(chosen_name, "我的名字是「[chosen_name]」{w=1.0}{nw}")
                                renpy.say(chosen_name, "以后请多多指教~{w=1.0}{nw}")

                                # 已拥有角色：技能等级加1
                                if chosen_name in [obj.name for obj in (local_config.party + local_config.backup)]:
                                    for role in local_config.party + local_config.backup:
                                        if role.name == chosen_name:
                                            if any(s.level < 5 for s in role.skills):
                                                selectup_skill = role.skill_levelup()
                                                renpy.say(chosen_name, "技能「[selectup_skill.name]」强化至Lv.[selectup_skill.level]")
                                            else:
                                                local_config.player.currency += 1500
                                            break
                                # 未拥有角色：加入后补队伍
                                elif chosen_name in [getattr(store, obj).name for obj in local_config.role_pool]:
                                    local_config.backup.append(chosen_member)
                                    renpy.say(chosen_name, "「[chosen_name]」加入队伍{w=1.0}{nw}")
                                else:
                                    local_config.player.currency += 1500

                                renpy.hide(chosen_member.objectname, layer="m2")
                                renpy.pause(0.75, hard=True)
                            # 道具
                            # elif sp_ratio <= persistent.ratio_table["items"]:
                            #     chosen_item_idx = renpy.random.randint(0, len(local_config.shop_list) - 1)
                            #     chosen_item_objectname = local_config.shop_list[chosen_item_idx]
                            #     chosen_item = getattr(store, chosen_item_objectname)
                            #     chosen_item.get(who=local_config.player)
                            #     chosen_name = chosen_item.name

                            #     if chosen_item.image not in [None, ""]:
                            #         if chosen_item.image == "item01":
                            #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.7, xalign=0.5, yalign=0.5)], layer="m2")
                            #         else:
                            #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.3, xalign=0.5, yalign=0.5)], layer="m2")
                            #         renpy.pause(1.0, hard=True)

                            #     renpy.say(chosen_name, "获得物品「[chosen_name]」{w=1.0}{nw}")

                            #     renpy.hide(chosen_item.image, layer="m2")
                            #     renpy.pause(0.75, hard=True)
                            # 装备
                            else:
                                if renpy.random.random() <= 0.25:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level1) - 1)
                                    chosen_equip = outfits_level1[chosen_equip_idx]
                                elif renpy.random.random() <= 0.5:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level2) - 1)
                                    chosen_equip = outfits_level2[chosen_equip_idx]
                                elif renpy.random.random() <= 0.75:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level3) - 1)
                                    chosen_equip = outfits_level3[chosen_equip_idx]
                                else:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level4) - 1)
                                    chosen_equip = outfits_level4[chosen_equip_idx]
                                
                                chosen_equip_objectname = chosen_equip.objectname
                                chosen_equip.get(who=local_config.player)
                                chosen_name = chosen_equip.name
                                
                                renpy.show(chosen_equip_objectname, at_list=[Transform(zoom=1.0, xalign=0.5, yalign=0.5)], layer="m2")
                                renpy.pause(1.0, hard=True)
                                
                                equip_level = ""
                                if "_01" in chosen_equip_objectname:
                                    equip_level = "普通"
                                elif "_02" in chosen_equip_objectname:
                                    equip_level = "稀有"
                                elif "_03" in chosen_equip_objectname:
                                    equip_level = "史诗"
                                else:
                                    equip_level = "传说"
                                renpy.say(chosen_name, "获得「[equip_level]」[chosen_equip.category]「[chosen_name]」{w=1.0}{nw}")

                                renpy.hide(chosen_equip_objectname, layer="m2")
                                renpy.pause(0.75, hard=True)

                    hide pooler_move
                else:
                    window mode thought
                    me01 "魔法币不足4500是无法进入多重异空间的，无论在哪个世界穷是永远的痛！"
                    me01 "快去「异界」获取更多魔法币吧。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day206.ritroom
            "下次一定":
                window mode thgouth
                me01 "相遇即是缘，请好好珍惜这份来之不易的羁绊。"
                pause 0.5 hard
                $ window_animate_outro()
                stop movie
                hide movie
                stop music fadeout 1.0
                $ _skipping = True
                jump day206.ritroom


label day206.shop:
    default seen_day206_shop = False
    default seen_day206_mana_eggs = False
    hide investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day city3 xuejian
    with slowdissolve
    pause 1.0 hard
    show ritona b9 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)

    if not seen_day206_shop:
        window mode thought
        ritona "这里是我的私人仓库，想要什么的话就和我说吧。"
        ritona "当然这里的东西可不是免费的。"
        $ seen_day206_shop = True

        if not seen_day206_mana_eggs and use_boiled_egg:
            window mode thought
            ritona "我会根据你现在的实力为你提供相对适合你的道具。"
            ritona "当然也包括刚刚你制作的魔法鸡蛋。"
            $ seen_day206_mana_eggs = True
    elif not seen_day206_mana_eggs and use_boiled_egg:
        window mode thought
        ritona "我会根据你现在的实力为你提供相对适合你的道具。"
        ritona "当然也包括刚刚你制作的魔法鸡蛋。"
        $ seen_day206_mana_eggs = True

    python:
        config.skipping = None
        renpy.block_rollback()
        _rollback = True

        local_config.current_message = ""
        local_config.current_mode = "buy"
        renpy.retain_after_load()
        _rollback = False

    if _return != False:
        call screen shop
    pause 0.5 hard
    jump day206.ritroom


label day206.stats:
    hide screen investigation_popup

    python:
        for role in local_config.party:
            role.hp = role.max_hp + role.extend_max_hp
            role.mp = role.max_mp
    $ local_config.current_mode == "Consumables"
    $ local_config.current_actor = local_config.party[0]

    call screen stats
    jump investigate


label day206.roleroom:
    default seen_day206_roleroom = False
    hide screen investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)

    if not seen_day206_roleroom:
        show roleroom_bg onlayer master
        with slowdissolve
        pause 1.0 hard
        show ritona b9 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)
        window mode thought
        ritona "这里是伙伴们的房间，能够{color=#ff0000}强化角色{/color}和{color=#ff0000}升级、穿戴装备{/color}。"
        ritona "同时与角色互动将会提升角色的{color=#ff0000}好感度{/color}，好感度的变化会解锁一些角色专属的{color=#ff0000}剧情{/color}。（功能将在“秋之章”开放）"
        ritona "角色的相应属性和定位都会显示在此，请放心食用~"
        ritona "人与人之间最重要的就是信任，现在好好和你的伙伴们搞好关系吧。"
        hide ritona

        $ seen_day206_roleroom = True

        python:
            local_config.start_init(local_config.player, local_config.party)
            local_config.next_story = "day206.ritroom"
    
    hide roleroom_bg
    # call screen roleroom
    call info


label day206.teleport:
    default seen_day206_teleport = False
    hide screen investigation_popup
    if not seen_day206_teleport:
        window mode thought
        show ritona b3 fb1 fa0 fc02
        ritona "这里是精神时光屋，为了以后能够应付更加棘手的对手，你就好好在这里修炼吧。"
        ritona "精神时光屋的副本能够获取经验、金币、突破材料、装备等游戏道具，帮助你提升实力以适应之后的战斗。"
        ritona "副本难度分为三个等级，分别是「简单」、「一般」和「困难」，随着难度的提升奖励也会变得更加丰厚。"
        show ritona b3 fb1 fa3 fc03
        ritona "困难程度的副本将会伴随着一定程度的「时空扭曲」，对战斗要求进一步提高。"
        ritona "希望你不要太快就把自己交代了才好......"
        # ritona "考虑到你宅男的身份我特地给你联动了{encyclopedia=hxx}幻想乡{/encyclopedia}的各位伙伴们来安排试炼。"
        # ritona "顺带一提，她们可比我{rb}好不到哪里去{/rb}{rt}没有声优{/rt}，可别太期待哟~"
        $ seen_day206_teleport = True

        python:
            local_config.total_tutorial_flags += [
                "attack_battle_easy",
                "speed_battle_easy",
                "protect_battle_easy",
                "fire_battle_easy",
                "light_battle_easy",
                "water_battle_easy", 
                "ice_battle_easy", 
                "rock_battle_easy", 
                "wind_battle_easy"
            ]

    python:
        current_message = ""

    call screen teleporter("206")
    jump investigate


label day206.sleep:
    hide screen investigation_popup
    menu:
        "结束梦境":
            python:
                ms_average_level = 0
                breakout_flag = []
                for par_name in local_config.masters:
                    for role in local_config.party:
                        if role.objectname == par_name:
                            ms_average_level += role.level
                            if role.level < 40 and role.level % 5 == 0 and (not role.break_through):
                                breakout_flag.append(False)
                            else:
                                breakout_flag.append(True)
                ms_average_level /= len(local_config.masters)
                
            if not use_boiled_egg:
                window mode thought
                me01 "还是先掌握如何制作魔法鸡蛋吧。"
                $ camera_move(-5400, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            if not seen_day206_shop:
                window mode thought
                me01 "弗兰似乎在商店等着我们的样子，还是先去看看吧。"
                $ camera_move(-5400, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            if not seen_day206_callback:
                window mode thought
                me01 "在继续冒险之前先去看看弗兰前辈为我们准备了什么惊喜吧。"
                window mode thought
                me01 "通过「召唤」界面进入剧情。"
                $ camera_move(-5400, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            if not seen_day206_roleroom:
                window mode thought
                me01 "通过「召唤」功能获取的角色将在「队伍」-「队伍菜单」中，可以随时添加或替换队伍中的角色。"
                window mode thought
                me01 "另外抽取或刷到的装备可以通过「养成屋」中的装备功能实现穿戴。"
                window mode thought
                me01 "现在就前往「养成屋」看看吧。"
                $ camera_move(-5400, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            if (ms_average_level < 20) or (not all(breakout_flag)):
                window mode thought
                me01 "下一次的敌人可能会比较棘手，还是去「异界」和「养成屋」多准备一下吧。"
                window mode thought
                me01 "确保队伍的平均等级在{color=#ff0000}20级突破{/color}以上比较稳妥。"
                menu:
                    "继续前进（不推荐）":
                        pass
                    "再准备准备":
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
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard

    $ persistent.lingyin = True
    $ persistent.youjia = True
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    jump second_menu
