
label inside_battle10(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "念动力场制造的乱流覆盖了战场，场上所有角色获得{color=#6f6}60%风元素伤害加成{/color}。"
    "与此同时暴走状态下的立花希行动后一定次数后将会引发「妄想颠覆」，使我方全体进入持续1回合的{color=#f00}混乱状态{/color}。"
    "被立花希的元素爆发「接触感应」选中的友方单位，在立花希受到伤害的同时也会受到一定的伤害，请小心应对。"
    "希菲尔是一名{color=#f00}全能型的增伤辅助{/color}，能够通过元素爆发「微量化改造」选择最适合战局的「幻彩音律」进行战斗。"
    "另外当被动技能等级足够高时，还能通过累计{color=#f00}机缘印记{/color}开启强力的技能。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label day216:
    bookmark
    $ save_name = _("Day 216")
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
    show backend_date215 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    play music second_114 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard    
    "转眼间学校迎来了开学季。"
    "结束了假期的我们也再一次回到了熟悉的校园。"
    "虽然不能说有多少憧憬和期待。"
    "但是总归是要收拾好心情开始新的学习生活才是。"
    "当然，也并不是每个人都是这么想的......"
    pause 1.0 hard
    scene set only school day corridor xuejian
    with dissolve
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('chapter five'), _("潘多拉之心"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard

    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051511440.ogg"
    szl "......"
    me01 "哟~"
    hide szl_dzf_b1
    $ flcam.move(5200, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011501270.ogg"
    xz "我、我先走了......"
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_ga1 at walkout_r(0.7)
    pause 0.5 hard
    hide xz_dzf_b2
    "也许是察觉到了尴尬的气氛，翔子先行走进了教室。"
    stop music fadeout 5.0
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051511450.ogg"
    szl "......"
    "虽然没有说话，但可以察觉到水之濑的视线一直不停地扫向这边。"
    "在与我对视之后又慌忙地移开。"
    "这举动似曾相识。"
    pause 1.0 hard
    play music second_108 fadein 3.0 if_changed
    play sound jump_1
    $ flcam.move(0, 0, 0)
    scene set only szl_cg school1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/水之濑/051511460.ogg"
    szl "{size=72}！？{/size}"
    me01 "想逃吗？"
    pause 0.1 hard
    scene set only szl_cg school2
    with dissolve
    me01 "......"
    pause 0.1 hard
    play sound jump_1
    scene set only szl_cg school3
    with dissolve
    play voice "voice/水之濑/051511470.ogg"
    szl "什！"
    play voice "voice/水之濑/051511480.ogg"
    szl "什、什......"
    pause 0.1 hard
    scene set only szl_cg school4
    with dissolve
    play voice "voice/水之濑/051511490.ogg"
    szl "......"
    pause 0.1 hard
    play sound jump_1
    scene set only szl_cg school5
    with dissolve
    me01 "我挪~"
    pause 0.1 hard
    scene set only szl_cg school1
    with dissolve
    play voice "voice/水之濑/051511500.ogg"
    szl "！"
    pause 0.1 hard
    scene set only szl_cg school6
    with dissolve
    play voice "voice/水之濑/051511510.ogg"
    szl "......"
    pause 0.1 hard
    play sound jump_1
    scene set only szl_cg school7
    with dissolve
    me01 "这边吗？"
    pause 0.1 hard
    scene set only szl_cg school3
    with dissolve
    play voice "voice/水之濑/051511520.ogg"
    szl "！！"
    pause 0.1 hard
    play sound jump_1
    scene set only szl_cg school1
    with dissolve
    "不管水之濑怎么避让，下一刻我都会出现在她的视线范围内。"
    pause 0.1 hard
    play sound jump_1
    scene set only szl_cg school3
    with dissolve
    pause 0.5 hard
    play sound jump_1
    scene set only szl_cg school1
    with dissolve
    pause 0.5 hard
    play sound jump_1
    scene set only szl_cg school3
    with dissolve
    pause 0.5 hard
    play sound jump_1
    scene set only szl_cg school1
    with dissolve
    "结果就变成了谜之拉锯战。"
    pause 0.1 hard
    scene set only szl_cg school6
    with dissolve
    pause 0.5 hard
    play sound jump_1
    scene set only szl_cg school7
    with dissolve
    play voice "voice/水之濑/051511530.ogg"
    szl "啊、啊......哈、哈呜......"
    pause 0.1 hard
    play sound rell_fire
    scene set only szl_cg school8
    with dissolve 
    play voice "voice/水之濑/051511540.ogg"
    szl "{size=72}你呀呀呀呀呀呀！！！{/size}" with vpunch
    pause 1.0 hard
    scene set only school day corridor xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_a2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051511550.ogg"
    szl "我现在不想看到你的脸，这种程度的暗示至少给我明白啊！"
    me01 "虽然明白但是我却想看到水之濑你。"
    hide szl_dzf_b2
    show szl_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051511560.ogg"
    szl "......那已经看够了吧。"
    stop music fadeout 5.0
    me01 "还在为之前胜负的事情生气吗？"
    me01 "那个时候因为有特殊的原因所以才耍了点花招，别往心里去。"
    show szl_dzf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051511570.ogg"
    szl "被你这样折腾换作谁都会烦的吧。"
    show szl_dzf_b1 b1 b1_a1
    play voice "voice/水之濑/051511580.ogg"
    szl "......下次给我走着瞧！"
    pause 0.5 hard
    play sound jiaobu2
    show szl_dzf_b1 b1 b1_a1 at walkout_l(0.5)
    pause 1.0 hard
    hide szl_dzf_b1
    "说完这句话，水之濑转身离开了。"
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "虽然不能确定刚才的道歉有没有用。"
    "但至少她说了“下次”，所以目的也算是达到了吧。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day216.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day outside xuejian
    $ flcam.move(4500, -300, 900, duration=1.5)
    with dissolve
    play music second_114 fadein 3.0 if_changed
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/千川老师/141300010.ogg"
    qcls "新年快乐，立花老师~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031304980.ogg"
    lhx "新年快乐，请多关照~"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/141300020.ogg"
    qcls "立花老师能按时来上班真是太好了。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031304990.ogg"
    lhx "我是不会翘班的，所以请放心。"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141300030.ogg"
    qcls "立花老师责任感很强，我也根本没想过会有翘班的可能。"
    show qcls_zf_b1 b1 b1_h3
    play voice "voice/千川老师/141300040.ogg"
    qcls "只是早上大部分时候看上去都是昏昏欲睡的样子，所以担心假期刚结束会不会睡过头。"
    hide lhx_dsf_b3 with None
    pause 0.1 hard
    show lhx_dsf_b2 b2 b2_h2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031305000.ogg"
    lhx "请不要小看我，我不会因为这点小事就退缩的。"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/141300050.ogg"
    qcls "非常感谢，今年也请多多关照了~"
    pause 1.0 hard
    scene black
    with right2left_02
    pause 1.0 hard
    play sound open_door5
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian
    with right2left_02
    pause 0.5 hard
    $ flcam.move(2500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.6)
    pause 0.5 hard
    play voice "voice/爱衣/111300180.ogg"
    aiyi "早上好，立花老师~"
    $ flcam.move(0, 300, 750, duration=1.5)
    show lhx_dzf_b2 b2 b2_n6 onlayer m1 at walkin_l(0.4)
    pause 0.5 hard
    play voice "voice/立花希/031305010.ogg"
    lhx "早上好，今年的爱衣也是一个懂礼貌的好孩子呢。"
    hide lhx_dzf_b2
    hide aiyi_dzf_b1 
    $ flcam.move(-7800, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b1 b1 b1_h1 onlayer m2 at walkin_l(0.2)
    play voice "voice/千波/211300010.ogg"
    qb "早上好飞机场！"
    $ flcam.move(-4800, 300, 750, duration=1.5)
    show lhx_dzf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.4
    play voice "voice/立花希/031305020.ogg"
    lhx "今年的千波也依旧是不知天高地厚。"
    hide qianbo_dzf_b1
    $ flcam.move(800, 0, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n2 onlayer m1:
        xpos 0.6
    show qcls_zf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.67
    play voice "voice/小桃/221300010.ogg"
    ycxt "盯~"
    show lhx_dzf_b2 b2 b2_n3
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/141300060.ogg"
    qcls "啊啦啊啦，别藏在老师的背后，出来好好打招呼吧。"
    show qcls_zf_b1 b1 b1_h1 at walkout_r(0.67)
    pause 0.5 hard
    $ flcam.move(0, 300, 750, duration=1.5)
    pause 0.5 hard
    hide qcls_zf_b1
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221300020.ogg"
    ycxt "早、早上好......"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_h1 onlayer m1:
        xpos 0.4
    play voice "voice/立花希/031305030.ogg"
    lhx "早上好，今年的小桃还是这么害羞呢~"
    hide lhx_dzf_b3
    $ flcam.move(0, 200, 600, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.4)
    pause 0.5 hard
    play voice "voice/爱衣/111300190.ogg"
    aiyi "小桃你去初诣了吗？"
    show ycxt_dzf_b1 b1 b1_n1
    play voice "voice/小桃/221300030.ogg"
    ycxt "嗯，和大哥哥一起。"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221300040.ogg"
    ycxt "一起去参拜什么的，还是第一次。"
    $ flcam.move(-2200, 100, 400, duration=1.5)
    show qianbo_dzf_b1 b1 b1_h2 onlayer m2:
        xpos 0.2
    play voice "voice/千波/211300020.ogg"
    qb "人家已经是大人了，所以初诣这种程度一个人去就够了。"
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(-3500, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/千川老师/141300070.ogg"
    qcls "啊啦啊啦，早上千波的姐姐还说要是千波迷路了会不得了的。"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_down(0.35, 20):
        xpos 0.2
    play voice "voice/千波/211300030.ogg"
    qb "才、才不是因为走散了才变成一个人的！"
    hide qianbo_dzf_b1
    hide qcls_zf_b1
    $ flcam.move(0, 300, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.4
    show ycxt_dzf_b1 b1 b1_n1 onlayer m1:
        xpos 0.6
    play voice "voice/爱衣/111300200.ogg"
    aiyi "爱衣也和大姐姐一起去初诣了哟。"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221300050.ogg"
    ycxt "凉君呢？"
    show aiyi_dzf_b1 b1 b1_ga2
    play voice "voice/爱衣/111300210.ogg"
    aiyi "大哥哥是和立花老师一起的。"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 300, 750, duration=1.5)
    show qianbo_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.2
    show lhx_dzf_b2 b2 b2_n3 onlayer m1:
        xpos 0.4
    play voice "voice/千波/211300040.ogg"
    qb "是这样吗？"
    show lhx_dzf_b2 b2 b2_h3
    play voice "voice/立花希/031305070.ogg"
    lhx "嘛，我是作为监护人陪他一起而已。"
    hide qianbo_dzf_b2
    $ flcam.move(800, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.67
    play voice "voice/千川老师/141300080.ogg"
    qcls "啊啦啊啦，走在一起的话立花老师看起来就像是神野同学的妹妹一样。"
    hide lhx_dzf_b2
    show lhx_dzf_b1 b1 b1_s2 onlayer m1:
        xpos 0.4
    play voice "voice/立花希/031305080.ogg"
    lhx "请不要说让人误会的话。（小声）"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141300090.ogg"
    qcls "大家差不多该换个地方了，园长老师一会儿还有新年的问候呢。"
    $ flcam.move(0, 0, 600, duration=1.5)
    show qianbo_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211300110.ogg"
    qb "好~"
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    show ycxt_dzf_b1 b1 b1_n1 onlayer m1:
        xpos 0.6
    play voice "voice/小桃/221300120.ogg"
    ycxt "爱衣我们也走吧。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111300260.ogg"
    aiyi "嗯。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day216'
    $ seen_day216_balltower_event01 = False
    $ seen_day216_kindergarden_event02 = False
    $ seen_day216_bridge_event01 = False
    $ seen_day216_laboratory_event01 = False

label day216.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day216':
        show set maps winter evening
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day216.balltower_event01':
        show set maps winter evening
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day216.kindergarden_event02':
        show set maps winter evening
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    elif _overworld_label == 'day216.bridge_event01':
        show set maps winter night
        $ flcam.move(*overworld.camera_positions['bridge'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        cloqks=("day216.balltower_event01", "not seen_day216_balltower_event01"),
        kindergarden=("day216.kindergarden_event02", "not seen_day216_kindergarden_event02"),
        bridge=("day216.bridge_event01", "seen_day216_balltower_event01 and seen_day216_kindergarden_event02 and not seen_day216_bridge_event01"),
        laboratory=("day216.laboratory_event01", "seen_day216_bridge_event01 and not seen_day216_laboratory_event01"))
    $ window_animate_outro()
    if _return == 'day216.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day216.kindergarden_event02':
        $ flcam.move(*overworld.camera_positions['kindergarden'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day216.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day216.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
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

label day216.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    show snow_level1 onlayer fg
    play ambience1 niaoming fadein 3.0
    with slowdissolve
    pause 2.0 hard
    scene set only street snow day road1 xuejian
    with slowdissolve
    play sound jiaobu2
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    me01 "......那是？"
    pause 0.5 hard
    stop ambience1 fadeout 3.0
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show alu_ct_b4 b4 b4_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.7
    play voice "voice/阿露/551000090.ogg"
    alu "唔莎~波！" with vpunch
    play music second_106 fadein 3.0 if_changed
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only alu_cg two
    with slowdissolve
    pause 1.0 hard
    me01 "{size=72}唔喔喔！{/size}"
    "我一个横向飞扑避开了攻击。"
    "可是因为惯性的缘故身体像雪橇一样在地上滑行了一段距离才停下来。"
    me01 "搞什么啊！"
    me01 "拜你所赐我的衣服都湿了。"
    play sound ganga03
    pause 0.1 hard
    scene set only alu_cg three
    with dissolve
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......"
    me01 "你看你这一折腾不是又要熔化了吗。"
    play sound enjoy_snow1
    pause 0.1 hard
    scene set only alu_cg four
    with dissolve
    "用雪帮她修复吧。"
    play sound jing03
    pause 0.1 hard
    scene set only alu_cg five
    with dissolve
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street snow day road1 xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show alu_ct_b10 b10 b10_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    me01 "自己会受伤的话，就不要随便喷火啊。"
    hide alu_ct_b10 with None
    show alu_ct_b8 b8 b8_1 onlayer m2 at fly(0.5):
        xpos 0.5
    play voice "voice/阿露/551000030.ogg"
    alu "唔莎唔莎~唔莎唔莎~"
    "感觉像是在说我多管闲事一样。"
    stop music fadeout 5.0
    me01 "下次再这样，我就把你烤熟了吃。"
    "虽然看起来一点也不好吃......"
    pause 0.5 hard
    play music second_148 fadein 3.0 if_changed
    $ flcam.move(2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b2 b2 b2_a1 onlayer m1:
        xpos 0.7
    play voice "voice/希菲尔/001001870.ogg"
    xfe "阿露不能这样，不能攻击凉君啦。"
    hide alu_ct_b8 with None
    show alu_ct_b9 b9 b9_1 onlayer m2 at fly(0.5):
        xpos 0.5
    play voice "voice/阿露/551000040.ogg"
    alu "唔莎~"
    pause 0.5 hard
    play sound fly1
    show alu_ct_b9 b9 b9_1 at fly_away(0.5):
        xpos 0.5
    pause 0.5 hard
    hide alu_ct_b9 with None
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_s2
    show alu_ct_b2 b2 b2_1 onlayer m2:
        xpos 0.73 ypos 0.5 alpha 0.0
        parallel:
            linear 1.0 ypos 0.6
        parallel:
            linear 1.0 alpha 1.0
    pause 1.5 hard
    hide alu_ct_b2 with None
    show alu_ct_b1 b1 b1_1 onlayer m2:
        xpos 0.73 ypos 0.6
    pause 0.5 hard
    play voice "voice/希菲尔/001001880.ogg"
    xfe "阿露说她把凉君当成是跟踪狂了。"
    me01 "希菲尔能和她说话吗？"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001001890.ogg"
    xfe "抓到诀窍的话就能做得到了哟~"
    me01 "完全被驯服了。"
    show ts_xfe_yjz_b2 b2 b2_sp3
    play voice "voice/希菲尔/001001900.ogg"
    xfe "凉君找希菲尔有事吗？"
    me01 "单纯的想见你而已。"
    show alu_ct_b1 b1 b1_2
    play voice "voice/阿露/551000580.ogg"
    alu "唔莎。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_a2 onlayer m1:
        xpos 0.7
    play voice "voice/希菲尔/001001910.ogg"
    xfe "真的个跟踪狂。"
    me01 "要你管！"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/001001920.ogg"
    xfe "凉君，学校那边呢？"
    me01 "今天是开学典礼所以已经结束了。"
    me01 "希菲尔知道我上学的事吗？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1:
        xpos 0.7
    play voice "voice/希菲尔/001001940.ogg"
    xfe "因为一直都在看着凉君的。"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001001950.ogg"
    xfe "除此之外的事情就不知道了，全都“叭咕叭咕”掉了。"
    me01 "那希菲尔你知道翔子吗？"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001001960.ogg"
    xfe "她是凉君新的家人，和凉君住在一起的人吧。"
    me01 "那......"
    "我犹豫了片刻。"
    me01 "名叫雷亚的死神呢？"
    show ts_xfe_yjz_b2 b2 b2_s2
    play voice "voice/希菲尔/001001970.ogg"
    xfe "这个没办法“叭咕叭咕”掉，所以不知道。"
    me01 "......这是什么意思？"
    show ts_xfe_yjz_b2 b2 b2_h2
    play voice "voice/希菲尔/001001980.ogg"
    xfe "硬要说的话......可以去问立花哟~"
    me01 "立花？立花老师吗？"
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎~"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_a2 onlayer m1:
        xpos 0.7
    play voice "voice/希菲尔/001002000.ogg"
    xfe "应付跟踪狂真是麻烦啊~"
    me01 "这样听起来就好像希菲尔是个腹黑所以还是别再学了。"
    show alu_ct_b1 b1 b1_3
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1:
        xpos 0.7
    play voice "voice/希菲尔/001002030.ogg"
    xfe "不管怎样希菲尔会努力完成自己使命的。"
    me01 "使命是指？"
    show alu_ct_b1 b1 b1_5
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h4 onlayer m1:
        xpos 0.7
    play voice "voice/希菲尔/001002040.ogg"
    xfe "叭咕叭咕~"
    me01 "使命就是吃雪吗......"
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow day xuejian2
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    "我们一起来到钟楼广场。"
    "久违地玩起了捉迷藏的游戏。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    me01 "找到你了，希菲尔。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001001300.ogg"
    xfe "被找到了~"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001001310.ogg"
    xfe "最近总能被凉君找到。"
    show ts_xfe_yjz_b2 b2 b2_ga3
    play voice "voice/希菲尔/001001320.ogg"
    xfe "有点不甘心的说。"
    "虽然嘴上这么说，但希菲尔看起来很开心的样子。"
    me01 "谢谢你希菲尔。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "多亏了希菲尔，翔子和爱衣她们才平安无事。"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2 at flu_down(0.15, 20, 2):
        xpos 0.5
    play voice "voice/希菲尔/001001330.ogg"
    xfe "这件事先“叭咕叭咕”掉。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001001340.ogg"
    xfe "那孩子，现在怎么样了？"
    me01 "翔子的话已经没事了。"
    play voice "voice/希菲尔/001001350.ogg"
    xfe "还没有结束......"
    show ts_xfe_yjz_b1 b1 b1_s3
    play voice "voice/希菲尔/001001360.ogg"
    xfe "还没有结束的。"
    me01 "你是说类似的危险还会再次降临吗？"
    play voice "voice/希菲尔/001001370.ogg"
    xfe "就是这样的，所以希菲尔我也不能再这样悠闲地“叭咕叭咕”了。"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h4 onlayer m2 at flu_down(0.15, 20, 2):
        xpos 0.5
    play voice "voice/希菲尔/001001380.ogg"
    xfe "叭咕叭咕~"
    me01 "明明很开心地吃着雪。"
    play sound jump_1
    show ts_xfe_yjz_b3 b3 b3_sp3 at flu_down(0.15, 20):
        xpos 0.5
    show han onlayer m2:
        xalign 0.495 yalign 0.42
    play voice "voice/希菲尔/001001390.ogg"
    xfe "不、不是这样的，只是想要教训一下肠道内的有害细菌而已。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "希菲尔所指的危险究竟是什么？"
    "{rb}灵纹{/rb}{rt}rune{/rt}的暴走也好，星天宫的巫女也罢，今后要面对的事情还很多。"
    "而且至今为止仍然没有关于雷亚的线索。"
    "我究竟遗漏了什么？"
    "那份{rb}共感{/rb}{rt}empathy{/rt}又想要传递给我什么呢？"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    me01 "希菲尔也能够使用{rb}灵纹{/rb}{rt}rune{/rt}吧？"
    show ts_xfe_yjz_b2 b2 b2_s1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/001001400.ogg"
    xfe "这个也先“叭咕叭咕”掉。"
    me01 "不是说不能再悠闲地“叭咕”了吗？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001001410.ogg"
    xfe "一切都是凉君的错哟。"
    me01 "......欸？"
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    play sound xiaoshi_1
    pause 2.0 hard
    "留下了意味深长的话，希菲尔的身影消失在了白雪之中。"
    "真是不懂女孩子的心思啊。"
    "希菲尔看起来是有什么苦衷才不能轻易地告诉我真相。"
    "果然真相只能靠我自己去寻找了吗......"
    stop music fadeout 5.0
    pause 5.0 hard
    if not seen_day216_balltower_event01:
        $ seen_day216_balltower_event01 = True
    $ _overworld_label = 'day216.balltower_event01'
    jump day216.map

label day216.kindergarden_event02:
    $ flcam.move(0, 0, 0)
    scene set only school evening outside xuejian
    play music second_118 fadein 3.0 if_changed
    $ flcam.move(0, 300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111300270.ogg"
    aiyi "啊，大哥哥~"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111300280.ogg"
    aiyi "立花老师，大哥哥来了哟。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031305120.ogg"
    lhx "为什么要拉着我一起......"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111300290.ogg"
    aiyi "因为立花老师好像有话要对大哥哥说。"
    me01 "是这样吗？"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031305130.ogg"
    lhx "其实也......没有什么特别的。"
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "立花老师找我有什么事？"
    show lhx_dzf_b2 b2 b2_ga2
    play voice "voice/立花希/031305140.ogg"
    lhx "没什么......"
    me01 "是很难开口的事吗？"
    show lhx_dzf_b2 b2 b2_ga3
    play voice "voice/立花希/031305150.ogg"
    lhx "......"
    me01 "我倒是不会强迫你说出来。"
    show lhx_dzf_b2 b2 b2_s3
    play voice "voice/立花希/031305160.ogg"
    lhx "也不是。"
    show lhx_dzf_b2 b2 b2_ga2
    play voice "voice/立花希/031305170.ogg"
    lhx "只是单纯地想说关于之前说好一起去新城区的事情......请不要太大惊小怪。"
    me01 "什么啊，这件事情的话不用客气尽管和我说就行了。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031305180.ogg"
    lhx "话说凉君今天见到叫希菲尔了吗？"
    if seen_day216_balltower_event01:
        me01 "见倒是见到了。"
    else:
        me01 "今天倒是没有遇到。"
    show lhx_dzf_b3 b3 b3_s2
    play voice "voice/立花希/031305190.ogg"
    lhx "是吗......"
    me01 "为什么突然问这个？"
    hide lhx_dzf_b3
    show lhx_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031305200.ogg"
    lhx "只是好奇而已。"
    me01 "看你的样子有些奇怪。"
    show lhx_dzf_b1 b1 b1_s1
    play voice "voice/立花希/031305210.ogg"
    lhx "我一直是平常的那样。"
    hide lhx_dzf_b1
    show lhx_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031305220.ogg"
    lhx "但如果说奇怪的话，说不定和记忆有关。"
    me01 "......记忆？"
    show lhx_dzf_b2 b2 b2_s1
    play voice "voice/立花希/031305230.ogg"
    lhx "是的，脑海里突然就浮现出了{rb}某人{/rb}{rt}member{/rt}的画面。"
    me01 "这还真是少女漫画的情节啊。"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111300310.ogg"
    aiyi "{rb}某人{/rb}{rt}member{/rt}？"
    show lhx_dzf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/立花希/031305240.ogg"
    lhx "爱衣还是不知道的比较好。"
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "所以就连你自己也不知道是怎么一回事吗？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031305250.ogg"
    lhx "是的。"
    hide lhx_dzf_b3
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.7
    play voice "voice/千川老师/141300100.ogg"
    qcls "立花老师，找你好久了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305270.ogg"
    lhx "有什么事吗？"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/141300110.ogg"
    qcls "是的......抱歉能请你稍微跟我来一下吗？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305280.ogg"
    lhx "没什么好客气的，毕竟这也是工作的一部分。"
    hide qcls_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b3 b3 b3_n1
    me01 "你先去忙吧。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305290.ogg"
    lhx "别忘了等下的安排。"
    me01 "我知道了。"
    hide lhx_dzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_h3 onlayer m2:
        xpos 0.7
    play voice "voice/千川老师/141300120.ogg"
    qcls "神野同学是来接爱衣的吧？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    me01 "是的，那么我就先接爱衣回去了。"
    show qcls_zf_b1 b1 b1_sp2
    play voice "voice/千川老师/141300130.ogg"
    qcls "这就回去了吗？"
    hide qcls_zf_b1
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show qianbo_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211300120.ogg"
    qb "不经过我的允许就擅自带走爱衣真是好大的胆子！"
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s4 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221300130.ogg"
    ycxt "已经要告别了吗？"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/111300320.ogg"
    aiyi "......爱衣也想跟大家再多玩一会儿，大哥哥也一起可以吗？"
    me01 "这个嘛。"
    show aiyi_dzf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/爱衣/111300330.ogg"
    aiyi "大哥哥~"
    show ycxt_dzf_b1 b1 b1_s2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/221300140.ogg"
    ycxt "凉君~"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211300130.ogg"
    qb "喂！不要诱拐啊！"
    me01 "你在瞎嚷嚷什么啊。"
    hide qianbo_dzf_b1
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/千川老师/141300140.ogg"
    qcls "左拥右抱呢~"
    me01 "您一定是误会了什么。"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141300150.ogg"
    qcls "现在还打算回去吗？"
    hide qcls_zf_b1
    $ flcam.move(0, 200, 600, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.3
    show aiyi_dzf_b1 b1 b1_s4 onlayer m2:
        xpos 0.5
    show ycxt_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111300340.ogg"
    aiyi "大哥哥~"
    play voice "voice/小桃/221300150.ogg"
    ycxt "凉君~"
    show qianbo_dzf_b1 b1 b1_ga1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211300140.ogg"
    qb "和、和你玩一会儿的话也是可以的。"
    me01 "......那就稍微玩一会儿吧。"
    hide qianbo_dzf_b1
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305300.ogg"
    lhx "凉君会变成萝莉控果然是希菲尔的错吗......（小声）"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day216.kindergarden_event03:
    play sound open_door5
    $ flcam.move(0, 0, 0)
    scene set only school evening inside xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305470.ogg"
    lhx "凉君。"
    play music second_108 fadein 3.0 if_changed
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305480.ogg"
    lhx "打扰一下你幼儿园社的活动。"
    me01 "幼儿园社是什么啊？！"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305490.ogg"
    lhx "就是以你和小孩子嬉戏打闹为活动的社团。顺带一提，社员分别是凉君还有这个关系要好的三人组。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/千川老师/141300350.ogg"
    qcls "啊啦啊啦，神野同学独占了爱衣、小桃还有千波呢~"
    hide qcls_zf_b1
    hide lhx_dzf_b2
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111300360.ogg"
    aiyi "爱衣我们变成大哥哥的所有物了吗？"
    $ flcam.move(2250, 300, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221300160.ogg"
    ycxt "诱拐犯？"
    $ flcam.move(0, 200, 600, duration=1.5)
    play sound appear
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/211300150.ogg"
    qb "喂！不要擅自诱拐我们啊！"
    me01 "才没有！"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    hide qianbo_dzf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305500.ogg"
    lhx "回归正题，我现在要和千川老师出去买东西。"
    me01 "有事要通知的话一开始就直说啊，别毫无意义地搅乱事态。"
    hide lhx_dzf_b2
    show lhx_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305510.ogg"
    lhx "凉君什么的，和小孩子嘻嘻哈哈就行了。"
    show lhx_dzf_b1 b1 b1_s1
    play voice "voice/立花希/031305520.ogg"
    lhx "我是这么觉得的。"
    stop music fadeout 5.0
    me01 "......为什么反倒是你生气了。"
    hide lhx_dzf_b1
    show lhx_dzf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031305530.ogg"
    lhx "明天......也会来接爱衣吗？"
    play music second_124 fadein 3.0 if_changed
    me01 "那是自然，有什么问题吗？"
    show lhx_dzf_b2 b2 b2_ga3
    play voice "voice/立花希/031305540.ogg"
    lhx "没什么。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/千川老师/141300360.ogg"
    qcls "立花老师，我们走吧。"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/031305550.ogg"
    lhx "好的。"
    pause 0.5 hard
    play sound jiaobu2
    show qcls_zf_b1 b1 b1_n1 at walkout_r(0.7)
    show lhx_dzf_b2 b2 b2_n1 at walkout_r(0.5)
    pause 0.5 hard
    hide qcls_zf_b1
    hide lhx_dzf_b2
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 1.0 hard
    play music second_108 fadein 3.0 if_changed
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111300370.ogg"
    aiyi "嘻嘻哈哈是什么？"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show qianbo_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211300160.ogg"
    qb "是唧唧我我的意思吗？"
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221300170.ogg"
    ycxt "是一起玩的意思吗？"
    show qianbo_dzf_b1 b1 b1_h4
    play voice "voice/千波/211300170.ogg"
    qb "是侍奉吧！"
    play voice "voice/爱衣/111300380.ogg"
    aiyi "侍奉？"
    play voice "voice/小桃/221300180.ogg"
    ycxt "也是一种游戏吗？"
    show qianbo_dzf_b1 b1 b1_ga2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/千波/211300180.ogg"
    qb "就是凉君一直让我们做的事。"
    me01 "我才没有，倒不如说是我一直在做的事！"
    show ycxt_dzf_b1 b1 b1_n1
    play voice "voice/小桃/221300190.ogg"
    ycxt "还没到告别的时间，试着玩玩看吗？"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211300190.ogg"
    qb "那就让我们来侍奉凉君吧~"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111300390.ogg"
    aiyi "大哥哥，来和爱衣我们嘻嘻哈哈吧？"
    me01 "......这种话还请绝对不要当着别人的面说。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day216_kindergarden_event02:
        $ seen_day216_kindergarden_event02 = True
    $ _overworld_label = 'day216.kindergarden_event02'
    jump day216.map

label day216.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    show snow_level1 onlayer fg
    with dissolve
    play music second_124 fadein 3.0 if_changed
    "黄昏来临之际，天空也开始飘起了雪。"
    pause 1.0 hard
    scene set only bridge evening xuejian
    with dissolve
    pause 1.0 hard
    "脑海里的画面。"
    "毫无疑问是自己小时候的记忆。"
    "可是为什么直到现在才回忆起来呢？"
    "而那记忆中的{rb}某人{/rb}{rt}member{/rt}又会是谁......"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031309190.ogg"
    lhx "雪？"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031309200.ogg"
    lhx "明明刚才还是一片晴朗的。"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031309210.ogg"
    lhx "总觉得自己无论如何也无法适应这里的气候。"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031309220.ogg"
    lhx "然而更讽刺的是回过神来的时候却已经默默接受了。"
    show lhx_dsf_b3 b3 b3_ga3
    stop music fadeout 5.0
    play voice "voice/立花希/031309240.ogg"
    lhx "简直就和你的存在一样——"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg bridge normal
    play music second_103 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001300610.ogg"
    xfe "被找到了~"
    show lhx_dsf_b1 b1 b1_sp1 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031309250.ogg"
    lhx "一开始打算躲起来吗？"
    show lhx_dsf_b1 b1 b1_n1
    play voice "voice/立花希/031309260.ogg"
    lhx "之前怎么找都找不到，这次难道不是你故意出现在我面前的吗？"
    hide lhx_dsf_b1
    pause 0.1 hard
    scene set only xfe_cg bridge angry
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001300620.ogg"
    xfe "......"
    show lhx_dsf_b1 b1 b1_s2 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031309270.ogg"
    lhx "虽然我觉得你真正想见的人并不是我。"
    show lhx_dsf_b1 b1 b1_n1
    play voice "voice/立花希/031309290.ogg"
    lhx "凉君他也很想见你的，所以快去找他吧。"
    hide lhx_dsf_b1
    pause 0.1 hard
    scene set only xfe_cg bridge daze
    with dissolve
    play voice "voice/希菲尔/001300630.ogg"
    xfe "不用了。"
    play voice "voice/希菲尔/001300640.ogg"
    xfe "已经快要和凉君告别了。"
    show lhx_dsf_b2 b2 b2_s4 onlayer screens at side_left('lhx'), basicfade
    play voice "voice/立花希/031309300.ogg"
    lhx "我觉得凉君可不这么认为，所以......"
    hide lhx_dsf_b2
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge evening xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300650.ogg"
    xfe "想说的就是这些而已吗？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031309310.ogg"
    lhx "......"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001300660.ogg"
    xfe "我觉得应该还有别的什么。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300670.ogg"
    xfe "因为你也，喜欢着凉君。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300680.ogg"
    xfe "和我一样......"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_sp1
    show ts_xfe_yjz_b2 b2 b2_n4
    play voice "voice/希菲尔/001300690.ogg"
    xfe "你是在害怕吗？"
    show ts_xfe_yjz_b2 b2 b2_s3
    play voice "voice/希菲尔/001300700.ogg"
    xfe "就像凉君曾经和我不辞而别的时候一样。"
    play voice "voice/希菲尔/001300710.ogg"
    xfe "你也在害怕有一天，他会从你的身边离开。"
    show lhx_dzf_b2 b2 b2_s3
    play voice "voice/立花希/031309320.ogg"
    lhx "......"
    hide lhx_dzf_b2
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300720.ogg"
    xfe "凉君他已经交到了新的朋友。"
    play voice "voice/希菲尔/001300730.ogg"
    xfe "有了新的家人。"
    show ts_xfe_yjz_b1 b1 b1_s3
    play voice "voice/希菲尔/001300740.ogg"
    xfe "所以或许已经......不会在乎那些所谓的回忆了也说不定。"
    play voice "voice/希菲尔/001300750.ogg"
    xfe "甚至可能会因此，成为他的负担。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001300760.ogg"
    xfe "过去的朋友也好，过去的家人也罢......说不定都会成为阻碍凉君前进的绊脚石。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 1.0 hard
    "所以才会说离别是必须的。"
    "明明好不容易再会了，却还是要分开。"
    "看着那样的画面简直就像是......"
    "看着过去的自己一样——"
    pause 1.0 hard
    scene set only bridge evening xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300770.ogg"
    xfe "我呢，也想像凉君那样。"
    play voice "voice/希菲尔/001300780.ogg"
    xfe "试着结交新的朋友。"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001300800.ogg"
    xfe "可到头来却只是害了大家。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300810.ogg"
    xfe "对不起。"
    play voice "voice/希菲尔/001300820.ogg"
    xfe "一直都想像这样向你道歉的。"
    show ts_xfe_yjz_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001300830.ogg"
    xfe "对你做了过分的事，非常抱歉。"
    pause 0.5 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    play sound xiaoshi_1
    pause 1.0 hard
    "留下这番话，希菲尔的身影消失在了白雪之中。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge evening xuejian
    show snow_level1 onlayer fg
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031309330.ogg"
    lhx "是吗......"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031309340.ogg"
    lhx "她是为了向我道歉才会出现在幼儿园的吗。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031309350.ogg"
    lhx "果然是个好孩子嘛~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day216.kindergarden_event04:
    $ flcam.move(0, 0, 0)
    scene set only school evening inside xuejian
    show snow_level1 onlayer fg
    play music second_118 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    me01 "辛苦了千川老师，购物还顺利吗？"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141300490.ogg"
    qcls "啊，是的......"
    me01 "立花老师没有一起吗？"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/141300500.ogg"
    qcls "立花老师说还有一些事情要处理。"
    me01 "是什么其他的工作吗？"
    show qcls_zf_b1 b1 b1_s2
    play voice "voice/千川老师/141300510.ogg"
    qcls "我也不知道......抱歉。"
    me01 "不，打扰到您还请见谅。"
    show qcls_zf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/千川老师/141300520.ogg"
    qcls "对不起......"
    me01 "千川老师不用道歉也没关系的。"
    stop music fadeout 5.0
    pause 0.5 hard
    hide qcls_zf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play music second_106 fadein 3.0 if_changed
    play sound appear
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/211300200.ogg"
    qb "喂！不要搭讪老师啊！！！"
    me01 "果然又是你。"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211300210.ogg"
    qb "不要连我也一起搭讪！"
    hide qianbo_dzf_b1
    $ flcam.move(2250, 300, 750, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/爱衣/111300400.ogg"
    aiyi "搭讪是什么？"
    play voice "voice/小桃/221300200.ogg"
    ycxt "......是唧唧我我的意思吗？"
    play voice "voice/爱衣/111300410.ogg"
    aiyi "比如摸头之类的？"
    play voice "voice/小桃/221300210.ogg"
    ycxt "是这样吗？"
    $ flcam.move(0, 200, 600, duration=1.5)
    show qianbo_dzf_b1 b1 b1_h2 onlayer m2:
        xpos 0.3
    play voice "voice/千波/211300220.ogg"
    qb "摸头只是小孩子的场合，大人的话还会摸头以外的地方。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/111300420.ogg"
    aiyi "是这样吗？"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221300220.ogg"
    ycxt "千波真成熟啊~"
    show qianbo_dzf_b1 b1 b1_ga1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211300230.ogg"
    qb "人、人家才不是希望被摸其他地方呢。"
    "冷静，现在的情况根本不想插嘴。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111300430.ogg"
    aiyi "爱衣很喜欢被大哥哥摸头哟~"
    show ycxt_dzf_b1 b1 b1_n1
    play voice "voice/小桃/221300230.ogg"
    ycxt "小桃也是~"
    play voice "voice/千波/211300240.ogg"
    qb "就、就算被凉君男摸也不会舒服的。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111300450.ogg"
    aiyi "爱衣觉得很舒服啊~"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221300240.ogg"
    ycxt "小桃也是~"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111300460.ogg"
    aiyi "被摸其他地方的话，会更舒服吗？"
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221300250.ogg"
    ycxt "不知道。"
    show qianbo_dzf_b1 b1 b1_ga1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211300250.ogg"
    qb "就、就算舒服人家也绝对不会承认的。"
    show aiyi_dzf_b1 b1 b1_s3
    play voice "voice/爱衣/111300470.ogg"
    aiyi "爱衣想被大哥哥摸。"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221300260.ogg"
    ycxt "爱、爱衣真大胆。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111300480.ogg"
    aiyi "是吗？"
    show qianbo_dzf_b1 b1 b1_ga2
    play voice "voice/千波/211300260.ogg"
    qb "因为爱衣还是小孩子嘛。"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111300490.ogg"
    aiyi "爱衣已经是大人了啦。"
    hide qianbo_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/爱衣/111300500.ogg"
    aiyi "大哥哥，快点摸摸会让爱衣觉得舒服的地方吧~"
    "好像再不插嘴的话事态就快失控了！？"
    hide aiyi_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_a2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011300320.ogg"
    xz "神野君......"
    play sound jing02
    me01 "{size=72}呀啊啊啊！！{/size}" with vpunch 
    "结果还是被翔子听到了！"
    show xz_dzf_b1 b1 b1_ga1
    play voice "voice/翔子/011300330.ogg"
    xz "幼儿园社的活动原来是这样的啊......"
    me01 "翔、翔子你听我解释。"
    show xz_dzf_b1 b1 b1_a2
    play voice "voice/翔子/011300340.ogg"
    xz "就算你被警察逮捕了我也不会救你的。"
    me01 "所以说这都是误会啊。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111300510.ogg"
    aiyi "是啊，都是误会啦。爱衣我们只是想和大哥哥嘻嘻哈哈而已。"
    show xz_dzf_b1 b1 b1_s2
    play voice "voice/翔子/011300350.ogg"
    xz "神野君的晚饭就免了吧......"
    me01 "怎么这样！"
    hide aiyi_dzf_b1
    hide xz_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/立花希/031308880.ogg"
    lhx "你还真是乐此不疲啊。"
    me01 "立花老师？"
    hide lhx_dsf_b2
    $ flcam.move(0, 200, 600, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221300310.ogg"
    ycxt "啊......稍微有点冷了。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111300650.ogg"
    aiyi "活动一下就会暖和起来吧？"
    show qianbo_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千波/211300340.ogg"
    qb "那就大家一起来活动活动吧！"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/221300320.ogg"
    ycxt "要玩些什么好呢？"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111300660.ogg"
    aiyi "大哥哥也一起吧？"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111300670.ogg"
    aiyi "大家一起唧唧我我直到身体暖和起来吧~"
    play sound jing01
    me01 "{size=72}幼儿园社解散！！！{/size}" with vpunch
    show qianbo_dzf_b1 b1 b1_sp1
    show aiyi_dzf_b1 b1 b1_sp1
    show ycxt_dzf_b1 b1 b1_sp1
    "终于喊出来了！"
    "我的心声！"
    hide qianbo_dzf_b1
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031309100.ogg"
    lhx "萝莉控去死好了......"
    pause 0.5 hard
    play sound jiaobu2
    show lhx_dsf_b2 b2 b2_ga1 at walkout_r(0.3)
    pause 1.0 hard
    hide lhx_dsf_b2
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "抱歉爱衣，你和翔子姐姐先回去吧。"
    play voice "voice/爱衣/111300680.ogg"
    aiyi "那大哥哥呢？"
    me01 "我这里还有一些误会必须要解开才行......"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day216.kindergarden_event05:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    show snow_level1 onlayer fg
    play music second_102 fadein 3.0 if_changed
    with slowdissolve
    pause 2.0 hard
    scene set only school evening inside xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dzf_b1 b1 b1_s2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    "透过窗户看着外头飘落的白雪。"
    "明明心中有着各种复杂的情绪却不知如何宣泄。"
    "只能默默地将手伸进口袋里。"
    "握住那把象征着护身符的钥匙。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only items key
    with dissolve
    pause 1.0 hard
    "和希菲尔交谈之后自己更加确信。"
    "也许正是因为有这样的羁绊才让自己再次遇到了凉君。"
    "同时也是因为这样一份羁绊，才让自己无时无刻不在追赶着他的背影。"
    "但还没能来得及搞清楚一切就迎来了抉择。"
    "光顾着害怕，害怕知道真相后可能会失去什么重要的东西。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    scene set only memory_cg winter one alpha
    show snow_level1 onlayer fg
    show sepiagrain onlayer texture
    play music second_135 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "那一天，一个穿着雪白的女孩来到了男孩居住的公寓门口。"
    "每到冬季她就会来找那位男孩玩。"
    "但也许是因为怕生的缘故，她总是站在门口等待男孩经过。"
    "就算其他人经过想要和她搭话，女孩也会立刻跑开。"
    "非常迅速地，一个转眼的功夫就消失不见了。"
    "而我就这样在暗处默默看着这样的她。"
    "因为每天都会留意这里发生的一切，所以我知道男孩此刻已经不在这里了。"
    "在这个冬季到来之前，他就已经离开了这座城市。"
    "听说是因为家人工作的缘故。"
    "当时的我还不能理解离别一词意味着什么。"
    "即便是现在，也很难表达其中夹杂的五味情愫。"
    "那名白雪般的女孩一定还不知道所发生的一切。"
    "所以才会像往常那样偷偷地等在门口，寻找着男孩的踪影。"
    "必须有人去告诉她。"
    "虽然我知道，就算去搭话女孩也会很快地跑开。"
    "但还是鼓起勇气来到了她的面前。"
    "现在想想也觉得不可思议，是因为不愿就这样眼睁睁地看着她难过吗？"
    "还是说，是想要让女孩知道注视着男孩的不是只有她一人呢。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300840.ogg"
    xfe "......凉君？"
    "更加让我感到意外的是，这次女孩并没有跑开。"
    "明明面对除了男孩以外的人都会逃跑，无一例外。"
    "但是看见我的时候却反而主动搭话了。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300850.ogg"
    xfe "不是凉君。"
    play voice "voice/希菲尔/001300860.ogg"
    xfe "但却非常像。"
    show ts_xfe_yjz_b3 b3 b3_ga1
    play voice "voice/希菲尔/001300870.ogg"
    xfe "明明长相和穿着都不一样，却有什么地方很像......"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300880.ogg"
    xfe "你......是谁？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    show sepiagrain onlayer texture
    with dissolve
    pause 1.0 hard
    "当时的我只是畏畏缩缩地报上了自己的名字。"
    "告诉她男孩已经不在这里的消息。"
    "他也许已经......不会再回来了。"
    pause 1.0 hard
    scene set only memory_cg winter one alpha
    show sepiagrain onlayer texture
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_c1 onlayer m2:
        xpos 0.5
    "女孩像是受到了沉重的打击一般。"
    "泪水从眼里夺眶而出。"
    "人原来可以......哭得如此伤心吗？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h3
    play voice "voice/希菲尔/001300890.ogg"
    xfe "你也......喜欢凉君吗？"
    "凉君？是男孩的名字吗？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300900.ogg"
    xfe "没问题的~"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001300910.ogg"
    xfe "如果你也喜欢凉君的话，就一定能够再见面的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300920.ogg"
    xfe "只要继续追赶着凉君的背影，就一定能够实现的~"
    "本想着来安慰女孩的。"
    "可没想到却反过来被安慰了。"
    "明明最伤心的应该是眼前的她才对。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300930.ogg"
    xfe "想要成为{rb}灵继者{/rb}{rt}elfin{/rt}的话，不觉醒{rb}灵纹{/rb}{rt}rune{/rt}的话是不行的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300950.ogg"
    xfe "然后呢，要从谁的身上获得{rb}灵纹{/rb}{rt}rune{/rt}的话，羁绊也是必需的。"
    "......羁绊？"
    play voice "voice/希菲尔/001300960.ogg"
    xfe "嗯，无论是什么样的羁绊都可以。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001300970.ogg"
    xfe "想要成为朋友，想要一起玩耍，像这样看似微不足道的事情也是可以的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001300980.ogg"
    xfe "所以呢，如果你抱着这样的想法，愿望说不定就能实现了。"
    play voice "voice/希菲尔/001300990.ogg"
    xfe "就可以和凉君重逢了也说不定~"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001301000.ogg"
    xfe "成为{rb}灵继者{/rb}{rt}elfin{/rt}的话说不定，就能追上凉君了。"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001301010.ogg"
    xfe "因为你也已经从凉君那里得到了名为羁绊的{rb}灵纹{/rb}{rt}rune{/rt}了。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001301020.ogg"
    xfe "希菲尔也是，不会再悲伤了。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001301030.ogg"
    xfe "我相信着总有一天，还会和凉君再见面的。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "愿望真的会实现吗？"
    "自己真的......能追上那个男孩吗？"
    "所以才会这么在意。"
    "所以才会感到害怕。"
    "不知道。"
    "希菲尔当时所说的话没有办法验证。"
    "真相只能靠自己去寻找。"
    "如果从凉君那里获得的名为羁绊的{rb}灵纹{/rb}{rt}rune{/rt}是真的。"
    "如果这份喜欢是发自内心的话。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black 
    with slowerdissolve
    pause 2.0 hard
    "如果对自己还有那么一点期待的话......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    show lhx_dzf_b3 b3 b3_sp2 onlayer screens at side_right('lhx'), basicfade
    play voice "voice/立花希/031310610.ogg"
    lhx "......雪？"
    hide lhx_dzf_b3
    pause 1.0 hard
    scene set only school evening inside xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310620.ogg"
    lhx "突然就飘过来了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b1
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310640.ogg"
    lhx "难不成你也在附近吗？"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/031310650.ogg"
    lhx "希菲尔。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg angry
    play music second_131 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001301060.ogg"
    xfe "看你又在迷茫了，所以才想着怎样能帮到你。"
    show lhx_dzf_b1 b1 b1_s3 onlayer screens at side_left('lhx', 0.15), basicfade
    play voice "voice/立花希/031310670.ogg"
    lhx "......"
    hide lhx_dzf_b1
    play voice "voice/希菲尔/001301070.ogg"
    xfe "你明明就快要追上凉君了。"
    play voice "voice/希菲尔/001301080.ogg"
    xfe "明明就快要做到连希菲尔我都没办法做到的事情了。"
    pause 0.1 hard
    scene set only xfe_cg daze
    with dissolve
    play voice "voice/希菲尔/001301090.ogg"
    xfe "但是......为什么还是会迷茫呢？"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only school evening inside xuejian
    show snow_level1 onlayer fg
    show lhx_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/立花希/031310680.ogg"
    lhx "我并不是在迷茫，只是在思考而已。"
    show lhx_dzf_b1 b1 b1_s1
    play voice "voice/立花希/031310690.ogg"
    lhx "就像我那名为羁绊的{rb}灵纹{/rb}{rt}rune{/rt}一样。"
    show lhx_dzf_b1 b1 b1_s3
    play voice "voice/立花希/031310700.ogg"
    lhx "凉君也和新的家人建立起了羁绊。"
    show lhx_dzf_b1 b1 b1_s1
    play voice "voice/立花希/031310710.ogg"
    lhx "我只是想确认我的做法会不会有什么不妥而已。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301100.ogg"
    xfe "为什么会这样呢？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_a1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301110.ogg"
    xfe "喜欢凉君的你像这样一直待在他的身边不就行了吗？"
    hide lhx_dzf_b1
    show lhx_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310720.ogg"
    lhx "做不到的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_a2 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301120.ogg"
    xfe "为什么？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310730.ogg"
    lhx "因为凉君他......讨厌{rb}灵纹{/rb}{rt}rune{/rt}。"
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/001301130.ogg"
    xfe "......"
    show lhx_dzf_b3 b3 b3_n3
    play voice "voice/立花希/031310740.ogg"
    lhx "对凉君而言，星天宫给他带来的伤害已经够大的了。"
    hide lhx_dzf_b3
    show lhx_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310760.ogg"
    lhx "我觉得{rb}灵继者{/rb}{rt}elfin{/rt}对于他而言是有别的含义的。"
    hide ts_xfe_yjz_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b1
    show lhx_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310770.ogg"
    lhx "就像我一样，因为有了日向她们这样重要的伙伴，所以才能感同身受。"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031310780.ogg"
    lhx "然而真正喜欢{rb}灵纹{/rb}{rt}rune{/rt}本身的{rb}灵继者{/rb}{rt}elfin{/rt}却是很少的。"
    show lhx_dzf_b2 b2 b2_s3
    play voice "voice/立花希/031310790.ogg"
    lhx "大家都或多或少因为{rb}灵继者{/rb}{rt}elfin{/rt}的身份而遭遇不幸了吧。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310800.ogg"
    lhx "凉君一定也是这样的......他一定也曾经因为{rb}灵纹{/rb}{rt}rune{/rt}的关系而变得不幸了。"
    show lhx_dzf_b3 b3 b3_n3
    play voice "voice/立花希/031310810.ogg"
    lhx "所以我才觉得自己是无法待在他身边的。"
    play voice "voice/立花希/031310820.ogg"
    lhx "因为和凉君不一样，我是喜欢{rb}灵纹{/rb}{rt}rune{/rt}的。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301140.ogg"
    xfe "......"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310830.ogg"
    lhx "也许正如你说的，我一直在追赶着凉君。"
    show lhx_dzf_b2 b2 b2_s3
    play voice "voice/立花希/031310840.ogg"
    lhx "作为曾经的伙伴想要待在他的身边。"
    show lhx_dzf_b2 b2 b2_n6
    play voice "voice/立花希/031310850.ogg"
    lhx "然而这一切全都多亏了{rb}灵纹{/rb}{rt}rune{/rt}的功劳。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310870.ogg"
    lhx "就像是跨越了兄妹的感情一般的——全新的羁绊。我是这么认为的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301150.ogg"
    xfe "谢谢你。"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001301160.ogg"
    xfe "谢谢能够喜欢上{rb}灵纹{/rb}{rt}rune{/rt}。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310920.ogg"
    lhx "......"
    hide lhx_dzf_b2
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301170.ogg"
    xfe "我没办法去很远的地方，所以无法一直追赶着凉君。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001301180.ogg"
    xfe "但你却能够代替我去追赶凉君的身影。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301190.ogg"
    xfe "让凉君不再寂寞。"
    show ts_xfe_yjz_b3 b3 b3_h1
    play voice "voice/希菲尔/001301200.ogg"
    xfe "过去也是，有你陪在身边的凉君才能一直保持着笑容的。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_s3 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301210.ogg"
    xfe "但如果连你也离他而去的话，凉君一定会寂寞的。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310940.ogg"
    lhx "没关系的。"
    hide lhx_dzf_b1
    show lhx_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310960.ogg"
    lhx "就算没有我在身边，现在的凉君也是没有问题的。"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/031310970.ogg"
    lhx "不会迷路，现在的他是能够找到回家之路的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_s3 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301250.ogg"
    xfe "那你自己不会寂寞吗？"
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031310980.ogg"
    lhx "就算寂寞也只是暂时的。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031310990.ogg"
    lhx "我和凉君的羁绊可不只有这样的程度而已~"
    hide ts_xfe_yjz_b3
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031311000.ogg"
    lhx "我最大的愿望是凉君能够得到幸福。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031311010.ogg"
    lhx "只要能够像这样看着像哥哥一样的凉君得到幸福，作为妹妹的我就已经足够幸福了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301260.ogg"
    xfe "这就是......家人？"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031311020.ogg"
    lhx "这点我也不是很清楚。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301270.ogg"
    xfe "希菲尔也不太明白。"
    show lhx_dzf_b2 b2 b2_h1
    play voice "voice/立花希/031311030.ogg"
    lhx "一会儿自称“我”一会儿又自称“希菲尔”，你的存在真的很特别呢。"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_ga1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/希菲尔/001301280.ogg"
    xfe "啊......说错了，希菲尔已经是大人了，所以必须要用“我”称呼自己才行。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031311040.ogg"
    lhx "因为是大人了所以才下定决心要离开凉君的吗？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301290.ogg"
    xfe "就是这样的。"
    show lhx_dzf_b3 b3 b3_ga2
    play voice "voice/立花希/031311050.ogg"
    lhx "我们都在勉强自己啊......"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301300.ogg"
    xfe "是因为在勉强吗？"
    show lhx_dzf_b3 b3 b3_n5
    play voice "voice/立花希/031311060.ogg"
    lhx "失言了......"
    show ts_xfe_yjz_b3 b3 b3_n2
    play voice "voice/希菲尔/001301320.ogg"
    xfe "已经要放弃追赶凉君了吗？"    
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031311070.ogg"
    lhx "......"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301330.ogg"
    xfe "我一直都在看着你们的。"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001301340.ogg"
    xfe "在这座城市，被你追赶着的凉君看上去很幸福。"    
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/031311080.ogg"
    lhx "别说得我像个跟踪狂一样。"
    hide lhx_dzf_b2
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001301350.ogg"
    xfe "今后我也会继续看着你们的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001301360.ogg"
    xfe "希菲尔我也想要守护你们两人的幸福~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard
    "谢谢你，洁白的女孩。"
    "一直以来都给了我勇气。"
    "所以这次......我也下定决心。"
    "与其害怕失去而一味地逃避，不如抛开一切向前迈进。"
    "创造属于自己的回忆。"
    "因为喜欢上了{rb}灵纹{/rb}{rt}rune{/rt}。"
    "所以也想让凉君体会自己的心情。"
    "即使会因此被讨厌，我也想让他知道。"
    "也想大声地告诉他“看吧，这就是我最喜欢的{rb}灵纹{/rb}{rt}rune{/rt}，你有意见吗”。"
    "是的——"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school evening outside xuejian alpha
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 1000, duration=30.0, warper='ease_cubic')
    play music second_138 fadein 3.0 if_changed
    with dissolve
    "已经什么都不需要再考虑了。"
    "即使看不清未来的道路。"
    "也不想再止步不前。"
    "是时候放弃追赶他的背影，而是试着走到他的面前。"
    "因为我也已经......厌倦了为别人而活。"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 1.0 hard

label day216.battle_lhx:
    $ flcam.move(0, 0, 0)
    scene set only school evening inside xuejian
    show snow_level1 onlayer fg
    play sound open_door5
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_a1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    me01 "啊，你终于出来了立花老师。"
    me01 "我还以为你忘了我们刚才约好的事呢。"
    me01 "趁着天还没黑，现在出发的话......"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031311570.ogg"
    lhx "每个人都那么地自以为是。"
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031311580.ogg"
    lhx "日向也说过，要我把自己的感情传达给凉君。"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031311600.ogg"
    lhx "但是又有谁知道这个举动也是需要勇气的。"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031311610.ogg"
    lhx "不是随随便便就能做到的。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031311630.ogg"
    lhx "因为我和凉君已经，是这样的关系了。"
    me01 "立花老师？"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031311640.ogg"
    lhx "一直都想像现在这样说一次。"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031311650.ogg"
    lhx "原本以为只要一直像这样待在凉君的身边就好了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_a1
    play voice "voice/立花希/031311660.ogg"
    lhx "但是......"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "脑海中却总是回荡着这样一个声音。"
    pause 0.5 hard
    play voice "voice/立花希/031311670.ogg"
    pcenter "凉君。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/立花希/031311680.ogg"
    pcenter "喜欢你。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/立花希/031311690.ogg"
    pcenter "我喜欢你！"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school evening inside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    "此时的我更加确信。"
    "那份“喜欢”是源于自己内心最真实的想法。"
    "一味地逃避是没用的。"
    "越是害怕失去的东西就越容易离我而去。"
    "不管是对于我还是希菲尔而言，都已经“失去”过一次了。"
    "那么此刻又有什么好顾虑的呢。"
    "如果说是讨厌{rb}灵纹{/rb}{rt}rune{/rt}的凉君让希菲尔如此难过的话......"
    show lhx_dsf_b1 b1 b1_n1
    "那就让我来帮你。"
    "让凉君“喜欢”上{rb}灵纹{/rb}{rt}rune{/rt}。"
    "因为不仅仅是{rb}灵纹{/rb}{rt}rune{/rt}，我也一直是喜欢希菲尔的。"
    "喜欢喜欢喜欢到没有办法的地步。"
    "看着你就像看着过去的自己一般，让人无论如何都想帮一把。"
    stop music fadeout 5.0
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031311730.ogg"
    lhx "不断烦恼、不断烦恼。到最后连自己都觉得很愚蠢。"
    show lhx_dsf_b1 b1 b1_a1
    play voice "voice/立花希/031311750.ogg"
    lhx "而这些全都是你的错！"
    play voice "voice/立花希/031311760.ogg"
    lhx "所以凉君......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    play sound rune1
    hide lhx_dsf_b1
    show lhx_dsf_b3_rune b3 b3 b3_a2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031311770.ogg"
    lhx "我现在要把你好好地修理一顿！"
    pause 1.0 hard
    play sound rune2
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 5.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg fight1
    play music second_149 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    me01 "{rb}灵纹{/rb}{rt}rune{/rt}？！"
    play voice "voice/立花希/031311780.ogg"
    lhx "恋爱即战争。"
    play voice "voice/立花希/031311790.ogg"
    lhx "我要在这里打倒你！"
    play voice "voice/立花希/031311800.ogg"
    lhx "然后占有你！"
    play voice "voice/立花希/031311810.ogg"
    lhx "把你的存在变成只属于我的东西！"
    pause 0.1 hard
    scene set only lhx_cg fight3
    with dissolve
    play voice "voice/立花希/031311820.ogg"
    lhx "要是我赢了的话，你就是我的所有物。"
    me01 "别开玩叫了！（咬舌）"
    pause 0.1 hard
    scene set only lhx_cg fight2
    with dissolve
    play voice "voice/立花希/031311830.ogg"
    lhx "刚才那番话可以说是我人生中最认真的一次了。"
    play voice "voice/立花希/031311840.ogg"
    lhx "凉君的幸福我才不管。"
    pause 0.1 hard
    scene set only lhx_cg fight1
    $ flcam.move(1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031311850.ogg"
    lhx "太麻烦了，干脆就这样直接把凉君你调教成以我为中心的恋爱傀儡吧。"
    me01 "你的想法很危险啊！"
    play voice "voice/立花希/031311860.ogg"
    lhx "我要把凉君当成仆人一生一世地使唤你。"
    "这个人毫无疑问是个抖S！" with vpunch
    play voice "voice/立花希/031311870.ogg"
    lhx "对我的命令要绝对服从。"
    play voice "voice/立花希/031311880.ogg"
    lhx "我说的话，无论什么都得服从。"
    pause 0.1 hard
    scene set only lhx_cg fight3
    with dissolve
    play voice "voice/立花希/031311890.ogg"
    lhx "这、这样的，那、那样的事也是。"
    play voice "voice/立花希/031311900.ogg"
    lhx "我也要对凉君做这、这样，那、那样的事。"
    play voice "voice/立花希/031311910.ogg"
    lhx "就算你不愿意......也绝对会让你屈服的！"
    play voice "voice/立花希/031311920.ogg"
    lhx "如果我赢了，这就是凉君你的下场，请记好了。"
    me01 "等等......你开玩笑的吧？"
    pause 0.1 hard
    scene set only lhx_cg fight2
    with dissolve
    play voice "voice/立花希/031311930.ogg"
    lhx "我可没有开玩笑。"
    me01 "不不不，你刚刚说的话明显就是哪里有问题吧？！"
    me01 "还有那看起来很危险的{rb}灵纹{/rb}{rt}rune{/rt}又是从哪里来的？"
    play voice "voice/立花希/031311950.ogg"
    lhx "凉君，你不知道吗？"
    pause 0.1 hard
    scene set only lhx_cg fight4
    with dissolve
    $ flcam.move(3200, -2800, 800, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031311960.ogg"
    lhx "女人的占有欲可是是非常强的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001301370.ogg"
    xfe "凉君......"
    pause 1.0 hard
    scene set only school evening outside xuejian alpha
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2 at walkin_r(0.3)
    pause 0.5 hard
    play voice "voice/希菲尔/001301380.ogg"
    xfe "还有追赶着凉君的“她”。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001301410.ogg"
    xfe "正因为在乎着彼此，才会引发纷争的吧。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n2
    play voice "voice/希菲尔/001301430.ogg"
    xfe "这一定就是——芬布尔之冬。"
    play music second_128 fadein 3.0 if_changed
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory4
    with slowdissolve
    pause 1.0 hard
    "天使开始歌唱。"
    $ flcam.move(-1100, -1400, 450, duration=1.5)
    pause 0.5 hard
    "此刻的这座城市，降下了温柔的雪——"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg fight1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031311970.ogg"
    lhx "凉君，做好觉悟了吗？"
    play voice "voice/立花希/031311980.ogg"
    lhx "现在我就用我的{rb}灵纹{/rb}{rt}rune{/rt}来打倒你！"
    play voice "voice/立花希/031311990.ogg"
    lhx "赌上我的一切打倒你。"
    pause 0.1 hard
    scene set only lhx_cg fight2
    with dissolve
    play voice "voice/立花希/031312010.ogg"
    lhx "为了我们最珍贵的羁绊。"
    play voice "voice/立花希/031312030.ogg"
    lhx "为了能够亲手，将这份羁绊延续下去。"
    pause 0.1 hard
    scene set only lhx_cg fight1
    $ flcam.move(1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312050.ogg"
    lhx "我要上了凉君。"
    play voice "voice/立花希/031312060.ogg"
    lhx "还请你配合一下我的任性。"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    pause 1.0 hard
    play sound rune2
    stop ambience1 fadeout 3.0
    stop music fadeout 5.0
    pause 2.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg kindergarden
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        ## 敌方初始化参数
        # Boss为藤原瞳，所有敌方角色技能等级满级，装备“传说”等级12天之印-碧落、风伤套装备6件
        lhx_role_mirror.equip_experience = 99999999
        selected_equipments = ["weapon_num1_04", 
                               "armor_num1_04", 
                               "necklace_num1_04", 
                               "ring_num1_04",
                               "magic_wind_04",
                               "stone_wind_04"]
        for cate in lhx_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments and outfit.category == cate)]
            sample_outfit = enemy_outfits[0]
            sample_outfit.init_params()
            for xi in range(11):
                sample_outfit.level_up(lhx_role_mirror, 100)
            sample_outfit.enemy_equip_on(lhx_role_mirror)
        for xi in range(20):
            lhx_role_mirror.skill_levelup()

        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

        # 灵能异常：全场角色风元素伤害提升60%；敌方行动3回合将会触发“妄想颠覆”，为全体友方附加1回合混乱状态。
        local_config.tutorial_step = "lhx_mana_error_winter_216"
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    
    pause 0.25
    call battle(boss=lhx_role_mirror, 
                boss_hp_plus=30000,
                side_enemy=[], 
                side_hp_plus=0,
                level=32,
                boss_first=True, 
                win_condition='normal', 
                stay_turn=0, 
                inside_label="inside_battle10", 
                mission_type="normal", 
                treasures={
                    "eggs": (4, 0.6),
                    "mana_eggs": (2, 0.3),
                    "soul_piece": (8, 0.3),
                    "soul_raise": (8, 0.3),
                    "wind_break_small": (8, 0.3),
                    "wind_break_large": (5, 0.3)
                })

    if _return == "win":
        "战斗胜利！"
        python:
            if "lhx_role" not in local_config.role_pool:
                local_config.role_pool.add("lhx_role")
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day216.after_battle_lhx

label day216.after_battle_lhx:
    scene black
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg fight1
    play music second_128 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "立花希从掌心发出{rb}念动立场{/rb}{rt}psychokinesis{/rt}。"
    "灵力形成的风压扑面而来。"
    "来不及躲闪，我只能以同样的招式进行抵挡。"
    "令我没有想到的是，在力场碰撞的一瞬间我的风压完全占据了上风。"
    "她的招式......和她的外表一样柔弱。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school fight evening inside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b3_rune b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312080.ogg"
    lhx "果然想靠{rb}念动立场{/rb}{rt}psychokinesis{/rt}分出胜负还是太勉强了。"
    hide lhx_dsf_b3_rune
    show lhx_dsf_b1_rune b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312100.ogg"
    lhx "想要赢凉君的话，就必须用我擅长的手段才行。"
    me01 "......你想干嘛？"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg fight4
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312110.ogg"
    lhx "就让我带你体会一下，这个世界的乐园吧~"
    stop music fadeout 5.0
    play sound rune2
    pause 1.0 hard
    scene white
    with in2out_02_l
    pause 2.0 hard
    play music second_104 fadein 3.0 if_changed
    scene set only lhx_cg fight5
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031312120.ogg"
    lhx "这里吗？这里更舒服吗？"
    me01 "啊~饶了我吧，立花希大人！"
    play voice "voice/立花希/031312130.ogg"
    lhx "叫希姐姐才对吧。"
    me01 "是的！希姐姐大人~"
    play voice "voice/立花希/031312140.ogg"
    lhx "想要我饶了你的话，就趴在地上用你那肮脏的舌头来舔我高贵的玉足吧。"
    pause 0.1 hard
    play sound yangmu
    scene set only lhx_cg fight6
    with dissolve
    me01 "是！十分乐意！！"
    me01 "这都是什么诡异的画面啊？！" with vpunch
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with dissolve
    play music second_150 fadein 3.0 if_changed
    pause 1.0 hard
    play sound hite_heavy
    me01 "......呜哈！" with vpunch
    "就在我尽全力吐槽的同时，身后传来了一阵剧痛。"
    "毫无防备的我就这样硬生生地被那股力量推出去好几米的距离。"
    pause 1.0 hard
    scene set only school fight evening inside xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_h2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031312150.ogg"
    lhx "哦呀哦呀？竟然这么轻易就得手了，你是不是故意放水了？"
    me01 "何等下流的攻击！"
    show lhx_dsf_b2_rune b2 b2 b2_h3
    play voice "voice/立花希/031312160.ogg"
    lhx "顺带一提，如果我赢了的话就让刚才的妄想成为现实。"
    me01 "......虽然不知道你又在打什么鬼主意，但看样子我是绝~对~不能输了！"
    "虽然嘴上这么说，心里还是很清楚的。"
    "立花希的能力不像水之濑那样依赖强大的正面实力，而更多的是对精神层面发起的破坏。"
    "明知道那些都是幻觉却会不自觉地上当，何等难缠的能力。"
    "对善于揣摩人心的立花老师而言，这样的能力太适合她了。"
    "看样子又是一场苦战啊......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    me01 "确认一点。"
    show lhx_dsf_b2_rune b2 b2 b2_sp1
    play voice "voice/立花希/031312170.ogg"
    lhx "什么？"
    me01 "这场比试要怎么样才算分出胜负？"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312180.ogg"
    lhx "终于做好觉悟了吗？"
    me01 "不管怎么样绝对不想输！"
    show lhx_dsf_b3_rune b3 b3 b3_s1
    play voice "voice/立花希/031312190.ogg"
    lhx "刚才那个虽然不是玩笑，但如果能激发你的斗志倒也没有白费。"
    me01 "既然是胜负就有致胜点吧？"
    hide lhx_dsf_b3_rune
    show lhx_dsf_b2_rune b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312200.ogg"
    lhx "是的，直到一方投降或失去战斗能力为止。"
    me01 "再怎么说这也太狠了吧？！"
    pause 0.1 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg fight1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031312210.ogg"
    lhx "那就继续吧~"
    pause 0.1 hard
    scene set only lhx_cg fight4
    $ flcam.move(1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312220.ogg"
    lhx "这一次要让你体验什么样的妄想......不对，是带你去什么样天国呢~"
    "体力上我有着绝对的优势，但是对方的精神攻击却尤为棘手。"
    "制胜点很明确，必须赶在对方使用{rb}思维透视{/rb}{rt}telepathy{/rt}能力之前结束战斗。"
    "用我擅长的{rb}念动立场{/rb}{rt}psychokinesis{/rt}佯攻制造机会，趁机接近对方将其拿下。"
    "就这么办！"
    pause 0.1 hard
    play sound rune2
    $ flcam.move(0, 0, 0)
    scene set only myself_cg four
    with in2out_02
    pause 1.0 hard
    me01 "放弃你的妄想。"
    pause 0.1 hard
    scene set only myself_cg five
    with dissolve
    me01 "变回平常的立花老师吧！"
    pause 0.5 hard
    play ambience1 strong_wind
    scene set only sky evening xuejian
    show snow_level2 onlayer fg
    with slowdissolve
    pause 1.0 hard
    "在我的念波驱使下，高速的风压席卷开来。"
    "这是我用来封住立花希行动的杀手锏。"
    "以她弱小的身形是很难在这样的风压中行动的。"
    "如此一来制服她也只是时间问题。"
    stop ambience1 fadeout 3.0
    pause 0.1 hard
    hide snow_level2
    scene set only lhx_cg fight1
    with dissolve
    play voice "voice/立花希/031312230.ogg"
    lhx "就知道会来这一手！"
    pause 0.1 hard
    scene set only lhx_cg fight2
    with dissolve
    play voice "voice/立花希/031312240.ogg"
    lhx "别以为这样就可以束缚住我，请容我先走一步。"
    pause 0.5 hard
    play sound rune3
    scene black 
    with right2left
    pause 1.0 hard
    "就在我靠近她的同时，立花希也发动了{rb}念动立场{/rb}{rt}psychokinesis{/rt}。"
    "顿时两股风压碰撞开来扬起了漫天的尘土，我的视线也被剥夺了。"
    "紊乱的气流让我五感尽失，一下子失去了目标。"
    "可恶，明明只差一步了。"
    play sound hite_heavy
    with vpunch
    pause 0.5 hard
    play ambience1 strong_wind
    scene set only sky evening xuejian
    show snow_level2 onlayer fg
    with right2left
    pause 1.0 hard
    me01 "呜哈！"
    "背后又一次感受到了强烈的冲击。"
    "这毫无疑问是立花希发起的攻击。"
    "可是为什么同样是身处风暴之中她却能清楚我的位置呢？"
    "在这样的风压中还能行动吗，真是小看她了。"
    "这下情况有些不妙了，此刻自己已经完全被对方玩弄于股掌之间了。"
    "之前从圣护院小姐那里听说过，有一种能够通过灵力流向洞悉周围事物本质的能力——{rb}接触感应{/rb}{rt}psychometry{/rt}。"
    "这家伙到底是有多万能啊！"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    hide snow_level2
    play sound rune2
    scene set only myself_cg four
    with dissolve
    pause 1.0 hard
    "管不了那么多了，既然沙子碍眼就统统吹散了再说。"
    "我加大了灵力的输出，风压强行将眼前的沙暴撕碎了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school fight evening inside xuejian
    show snow_level2 onlayer fg
    with right2left
    pause 0.5 hard
    $ flcam.move(-3500, -200, 600, duration=1.5)
    pause 2.0 hard
    $ flcam.move(3500, -200, 600, duration=1.5)
    pause 2.0 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    $ flcam.move(0, 0, 600, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3_rune b3 b3 b3_sp2 onlayer m2:
        xpos 0.5
    "很好，对方似乎没有跑远。"
    "一定是刚才的攻击还没来得及撤离的缘故吧。"
    "我和立花希四目相对了。"
    "下一秒首先行动的是我。"
    play sound rune2
    show wflash onlayer texture
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    "我再次全力冲了上去。"
    "眼看着与对方的距离越来越近。"
    "胜利就在眼前了！"
    stop music fadeout 5.0
    play sound rune3
    pause 1.0 hard
    hide snow_level2
    scene white
    with slowerdissolve
    pause 2.0 hard
    play music second_104 fadein 3.0 if_changed
    play sound jing01
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg fight7
    with slowdissolve
    pause 1.0 hard
    me01 "诶嘿嘿嘿......我要把你绑起来剥个精光。"
    play voice "voice/立花希/031312250.ogg"
    lhx "不要......快住手。"
    me01 "嘿嘿嘿嘿......给我老实待着别动。"
    pause 1.0 hard
    scene set only school fight evening inside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play sound jing04
    me01 "所以说这都是什么剧情啊？！" with vpunch
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with dissolve
    pause 0.5 hard
    play sound hite_heavy
    with vpunch
    me01 "......呜哈！"
    play music second_150 fadein 3.0 if_changed
    "背后又是猝不及防的一击。"
    pause 1.0 hard
    hide snow_level1
    scene set only lhx_cg fight4
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312260.ogg"
    lhx "哦呀哦呀？好不容易制造的机会，果然还是太年轻了啊？"
    "这、这家伙......"
    pause 0.1 hard
    scene set only lhx_cg fight3
    $ flcam.move(1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312270.ogg"
    lhx "请、请不要对我做下流的事情......"
    me01 "可恶，明知道是你的圈套却毫无办法。"
    pause 0.1 hard
    scene set only lhx_cg fight4
    with dissolve
    play voice "voice/立花希/031312280.ogg"
    lhx "我赢了的话，我要把凉君扒个精光然后尽情地调戏。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only school fight evening inside xuejian
    show snow_level1 onlayer fg
    show lhx_dsf_b2_rune b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312290.ogg"
    lhx "雪越下越大了啊。"
    show lhx_dsf_b2_rune b2 b2 b2_n3
    play voice "voice/立花希/031312300.ogg"
    lhx "机会难得，就让我好好利用一下吧~"
    me01 "......你又想干嘛？"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312310.ogg"
    lhx "虽然想要制造暴风雪是不太可能，但是吹雪的话我还是可以做得到的。"
    pause 0.5 hard
    play sound rune3
    hide snow_level1
    scene white 
    with right2left_02
    "随着飘落的白雪越来越多，立花希的身影再一次消失了。"
    "刚才是沙子，现在又换成雪吗？"
    "这样下去没完没了了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play ambience1 strong_wind fadein 3.0
    scene set only school fight evening inside xuejian
    show snow_level2 onlayer fg
    with right2left_02
    pause 1.0 hard
    "总之现在首要的任务是获取情报。"
    pause 1.0 hard
    hide snow_level2
    scene set only lhx_cg fight4
    with dissolve
    pause 1.0 hard
    me01 "你果然是能够知道我的位置吗？"
    play voice "voice/立花希/031312330.ogg"
    lhx "是的~"
    me01 "在这样的环境中，光凭肉眼不可能做到的吧？"
    play voice "voice/立花希/031312340.ogg"
    lhx "没错，我也和你一样因为吹雪的关系现在什么都看不清。"
    me01 "那到底是如何做到的？"
    play voice "voice/立花希/031312350.ogg"
    lhx "当然是通过{rb}接触感应{/rb}{rt}psychometry{/rt}获得的情报。"
    me01 "可是现在我们并没有接触吧？"
    play voice "voice/立花希/031312360.ogg"
    lhx "是的，所以说我其实是利用了其他的东西。"
    me01 "其他的东西？"
    play voice "voice/立花希/031312370.ogg"
    lhx "我利用流动的空气获取到了你的情报。"
    me01 "这种事也能办得到吗？"
    "不对，再怎么天赋异禀的{rb}灵继者{/rb}{rt}elfin{/rt}也不可能在不接触对方的情况下使用{rb}接触感应{/rb}{rt}psychometry{/rt}。"
    "她说空气？"
    "难道......"
    me01 "你所能感知到的是我残留在空气中的气味、呼吸、还有心跳脉搏的声音。"
    me01 "也就是说，只要是由我的生命体征所产生的行为，你的{rb}接触感应{/rb}{rt}psychometry{/rt}都能够洞悉。"
    me01 "我说的没错吧？"
    pause 0.1 hard
    scene set only lhx_cg fight2
    $ flcam.move(1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312380.ogg"
    lhx "换做是平常的我的话，我肯定没有办法施展这么强大的{rb}接触感应{/rb}{rt}psychometry{/rt}。"
    play voice "voice/立花希/031312390.ogg"
    lhx "但如果是现在的处于“暴走”状态的我的话......"
    pause 0.1 hard
    scene set only lhx_cg fight1
    with dissolve
    play voice "voice/立花希/031312400.ogg"
    lhx "不仅是{rb}念动立场{/rb}{rt}psychokinesis{/rt}，就连{rb}接触感应{/rb}{rt}psychometry{/rt}都被强化了。"
    play voice "voice/立花希/031312410.ogg"
    lhx "可以说是因祸得福吧。"
    play voice "voice/立花希/031312450.ogg"
    lhx "不管怎么样，只要是凉君你在还能呼吸的地方，不管躲到哪里我都能找到！"
    pause 0.1 hard
    scene set only lhx_cg fight4
    $ flcam.move(3200, -2800, 800, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312460.ogg"
    lhx "简而言之，现在的你已经完全被我玩弄于鼓掌之间了~"
    play voice "voice/立花希/031312470.ogg"
    lhx "想要投降的话就趁现在。"
    me01 "如果我投降了会发生什么？"
    play voice "voice/立花希/031312480.ogg"
    lhx "我会做这样那样的事情。"
    me01 "那和输了有什么区别啊！"
    play voice "voice/立花希/031312490.ogg"
    lhx "还想着战胜我吗？"
    play voice "voice/立花希/031312500.ogg"
    lhx "那就不能从正面，而是要耍点花招才行。"
    me01 "......这家伙果然难缠。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school fight evening inside xuejian
    show snow_level2 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312510.ogg"
    lhx "顺带一提我连凉君的作战计划也是了如指掌的。"
    show lhx_dsf_b2_rune b2 b2 b2_n3
    play voice "voice/立花希/031312520.ogg"
    lhx "想用{rb}念动立场{/rb}{rt}psychokinesis{/rt}瞬间把速度提升到最大，然后从侧面向我发起进攻。"
    play voice "voice/立花希/031312530.ogg"
    lhx "以我的实力就算我掌握了你的方位，也会因为突然的攻势而来不及做出反应。"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312550.ogg"
    lhx "确实这样的话即使我使用{rb}念动立场{/rb}{rt}psychokinesis{/rt}回击也会陷入被动。"
    play voice "voice/立花希/031312560.ogg"
    lhx "这样说不定就能出其不意地将我制服。"
    me01 "......真亏你连我的思考都能看穿啊。"
    hide lhx_dsf_b3_rune
    show lhx_dsf_b2_rune b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312570.ogg"
    lhx "我不是都说了，现在的我想要获取凉君的情报简直易如反掌。"
    play voice "voice/立花希/031312580.ogg"
    lhx "就连通过你大脑的神经信号和肌肉的收缩程度来判断你的行动都是可以做到的。"
    me01 "......"
    "感觉已经像是开挂一般的存在了。"
    "就连呼吸和思考都会被对方掌控，这样的战斗还哪有胜利可言？"
    pause 1.0 hard
    play sound rune2
    hide snow_level2
    stop ambience1 fadeout 1.0
    scene white
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1_rune b1 b1 b1_s2 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031312590.ogg"
    lhx "即使如此，凉君......"
    stop music fadeout 5.0
    show lhx_dsf_b1_rune b1 b1 b1_s1
    play voice "voice/立花希/031312600.ogg"
    lhx "我仍无法看穿你的心意。"
    pause 0.5 hard
    hide lhx_dsf_b1_rune with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school fight evening inside xuejian
    show snow_level2 onlayer fg
    play music second_138 fadein 3.0 if_changed
    "......刚刚那是什么？"
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show lhx_dsf_b2_rune b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312610.ogg"
    lhx "所以说凉君。你真的有自信能破解我的{rb}思维透视{/rb}{rt}telepathy{/rt}吗？"
    me01 "......刚才的声音？"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312630.ogg"
    lhx "声音？你在说什么？"
    pause 1.0 hard
    hide snow_level2
    $ flcam.move(0, 0, 0)
    scene white
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowerdissolve
    pause 1.0 hard
    show lhx_dsf_b1_rune b1 b1 b1_s3 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031312640.ogg"
    lhx "无法知道凉君的心意。"
    play voice "voice/立花希/031312650.ogg"
    lhx "不知道他何时会离我而去。"
    show lhx_dsf_b1_rune b1 b1 b1_s1
    play voice "voice/立花希/031312660.ogg"
    lhx "好害怕。"
    show lhx_dsf_b1_rune b1 b1 b1_c1
    play voice "voice/立花希/031312670.ogg"
    lhx "不要。"
    play voice "voice/立花希/031312690.ogg"
    lhx "不要丢下我一个人！"
    pause 0.5 hard
    hide lhx_dsf_b1_rune with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 900)
    scene set only school fight evening inside xuejian
    show snow_level2 onlayer fg
    show lhx_dsf_b2_rune b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031312700.ogg"
    lhx "......你怎么了，凉君？"
    hide lhx_dsf_b2_rune
    show lhx_dsf_b3_rune b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312710.ogg"
    lhx "注意力分散了，请你认真地做我的对手。"
    play voice "voice/立花希/031312720.ogg"
    lhx "请好好看着我！"
    "话说回来，我一直都没有明白这场战斗的真正意义。"
    "为什么立花希就这么想战胜我呢？"
    "为什么她就这么想......把我占为己有呢？"
    pause 1.0 hard
    hide snow_level2
    $ flcam.move(0, 0, 0)
    scene white
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowerdissolve
    pause 1.0 hard
    show lhx_dsf_b1_rune b1 b1 b1_s2 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031312730.ogg"
    lhx "正因为不清楚凉君的心意，我才会渴望羁绊。"
    play voice "voice/立花希/031312740.ogg"
    lhx "只要有了共同的回忆，就能顺理成章地待在他的身边了。"
    show lhx_dsf_b1_rune b1 b1 b1_c1
    play voice "voice/立花希/031312760.ogg"
    lhx "就不会再......迷路了。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "无论是现在眼前的立花希，还是短暂停留的声音。"
    "哪一个都是真实存在的。"
    "是想通过战斗的方式来创造新的羁绊吗。"
    "可是立花老师啊。"
    "难道不正是因为我们之间已经存在着羁绊，才让这场战斗变得有意义的吗。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene white 
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowerdissolve
    pause 0.5 hard
    show lhx_dsf_b1_rune b1 b1 b1_s2 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031312770.ogg"
    lhx "我很感谢{rb}灵纹{/rb}{rt}rune{/rt}。"
    play voice "voice/立花希/031312780.ogg"
    lhx "正因为有了{rb}灵纹{/rb}{rt}rune{/rt}我才能像这样待在凉君的身边。"
    play voice "voice/立花希/031312790.ogg"
    lhx "我最喜欢{rb}灵纹{/rb}{rt}rune{/rt}了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1_rune b1 b1 b1_c1
    play voice "voice/立花希/031312800.ogg"
    lhx "所以我也希望凉君能喜欢上{rb}灵纹{/rb}{rt}rune{/rt}。"
    play voice "voice/立花希/031312810.ogg"
    lhx "喜欢上这份维系着我们的羁绊。"
    stop music fadeout 5.0
    pause 0.5 hard
    hide lhx_dsf_b1_rune with dissolve
    $ flcam.move(0, 0, 0)
    pause 1.0 hard
    nvl clear
    play voice "voice/立花希/031312890.ogg"
    pcenter "我不希望你把{rb}灵纹{/rb}{rt}rune{/rt}当成是会带来不幸的东西——"
    nvl clear
    pause 1.0 hard
    scene set only school evening inside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    play music second_157 fadein 3.0 if_changed
    with slowdissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    me01 "这么晚才注意到，抱歉......"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312900.ogg"
    lhx "......为什么突然道歉啊？"
    show lhx_dsf_b3 b3 b3_a1
    play voice "voice/立花希/031312910.ogg"
    lhx "难道说是你要投降了吗？"
    me01 "不是的，这也是我的作战计划。"
    me01 "就像你说的，恋爱即是战争。"
    me01 "所以......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    play sound touch
    hide lhx_dsf_b2 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031312930.ogg"
    lhx "为什么要突然靠过来啊？"
    me01 "不是能够读取我的想法吗，那你应该知道了才对。"
    me01 "顺带一提，大意的是立花老师你才对。"
    me01 "没有了风暴的掩护，现在你就站在我的面前。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312940.ogg"
    lhx "所以你才从正面攻过来吗......"
    me01 "是啊。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312950.ogg"
    lhx "你是打算这样走过来，然后将我制服吗？"
    me01 "不愧是你，又被看穿了。"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031312960.ogg"
    lhx "你觉得我会让你得逞吗？"
    me01 "不试试看怎么知道呢。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031312970.ogg"
    lhx "那就让你尝尝我的精神攻击。"
    me01 "啊，让我见识一下吧。"
    pause 1.0 hard
    hide snow_level1
    play sound rune3
    $ flcam.move(0, 0, 0)
    scene white 
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowerdissolve
    pause 1.0 hard
    show lhx_dsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5 alpha 0.5
    play voice "voice/立花希/031312980.ogg"
    lhx "凉君，我喜欢你。"
    play voice "voice/立花希/031312990.ogg"
    lhx "对方是凉君的话......对我做这样、那样的事情也可以的。"
    pause 1.0 hard
    scene set only school evening inside xuejian
    show snow_level1 onlayer fg
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/立花希/031313000.ogg"
    lhx "啊、啊咧？"
    play voice "voice/立花希/031313010.ogg"
    lhx "不、不对！刚才的不算！"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313020.ogg"
    lhx "一定是因为暴走的时间太久了，{rb}灵纹{/rb}{rt}rune{/rt}的控制出了点问题......"
    show lhx_dsf_b2 b2 b2_ga2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031313030.ogg"
    lhx "呀！"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    play sound touch
    "我从正面抱住了她。"
    me01 "抓到你了。"
    me01 "这样一来就是我的胜利了。"
    show lhx_dsf_b2 b2 b2_ga2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/031313040.ogg"
    lhx "放、放开我！"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    show lhx_dsf_b1 b1 b1_c1
    play voice "voice/立花希/031313060.ogg"
    lhx "我还不能输！"
    me01 "还真是不死心啊。"
    play voice "voice/立花希/031313070.ogg"
    lhx "不、不能输......我必须赢。"
    play voice "voice/立花希/031313080.ogg"
    lhx "我不想失去凉君。"
    play voice "voice/立花希/031313090.ogg"
    lhx "想要......一直待在身边。"
    play voice "voice/立花希/031313100.ogg"
    lhx "想要一直待在凉君的身边......所以求你了！"
    play voice "voice/立花希/031313110.ogg"
    lhx "如果在比试中赢了的话，就能让你答应我的。"
    play voice "voice/立花希/031313120.ogg"
    lhx "凉君是会遵守约定的。"
    play voice "voice/立花希/031313130.ogg"
    lhx "所以我无论如何......都必须要赢的！"
    me01 "傻瓜，这种事情由我来做也是一样的。"
    me01 "现在是我赢了。"
    me01 "所以相对的，立花老师是我的人了。"
    me01 "我也能让你永远，留在我的身边了。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play sound touch
    play voice "voice/立花希/031313140.ogg"
    lhx "......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg touch1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031313150.ogg"
    lhx "公主抱......"
    me01 "立花老师所说的那些羁绊对我而言，都是十分重要的东西。"
    me01 "是我就算付出生命也必须要守护的东西。"
    pause 0.1 hard
    scene set only lhx_cg touch6
    with dissolve
    play voice "voice/立花希/031313180.ogg"
    lhx "......真的不会半途而废吗？"
    play voice "voice/立花希/031313190.ogg"
    lhx "也会像对待青木翔子还有爱衣那样坚持的吧？"
    me01 "那是当然的。"
    play voice "voice/立花希/031313200.ogg"
    lhx "......"
    me01 "就让我们一起去创造新的回忆吧，只属于我们两个人的......全新的羁绊。"
    pause 0.1 hard
    scene set only lhx_cg touch4
    $ flcam.move(-1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031313220.ogg"
    lhx "凉君......"
    play voice "voice/立花希/031313230.ogg"
    lhx "好的~"
    play voice "voice/立花希/031313240.ogg"
    lhx "真是拿你没办法。"
    play voice "voice/立花希/031313250.ogg"
    lhx "谁叫凉君没了我就老是那么胡来。"
    me01 "不过既然是我赢了，从今以后立花老师就必须对我的命令绝对服从。"
    pause 0.1 hard
    scene set only lhx_cg touch6
    $ flcam.move(0, 0, 0, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031313290.ogg"
    lhx "那、那可......不行。"
    play voice "voice/立花希/031313300.ogg"
    lhx "要是凉君哪天突然说......我们是恋人。"
    play voice "voice/立花希/031313310.ogg"
    lhx "而我却没有办法拒绝的话，不就只能去告凉君欺诈了吗？"
    me01 "你的脑袋里除了这样危险的想法还真是什么都没有了啊。"
    me01 "到时候对你做这样那样的事情也可以的。"
    play voice "voice/立花希/031313330.ogg"
    lhx "既然我输了......就只有任凭凉君处置了。"
    pause 0.1 hard
    play sound yangmu
    scene set only lhx_cg touch2
    $ flcam.move(-1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031313340.ogg"
    lhx "首、首先应该做什么呢？"
    me01 "这个嘛......大概是完成一起去新城区的约定吧。"
    pause 0.1 hard
    scene set only lhx_cg touch5
    with dissolve
    play voice "voice/立花希/031313350.ogg"
    lhx "......"
    me01 "你那鄙视的眼神是怎么回事！"
    play voice "voice/立花希/031313360.ogg"
    lhx "凉君如果成了男朋友的话一定是个怂货。"
    play voice "voice/立花希/031313370.ogg"
    lhx "所以......你打算抱我到什么时候啊？"
    me01 "到你冷静下来为止。"
    play voice "voice/立花希/031313380.ogg"
    lhx "我很冷静，已经回归正轨了。"
    play voice "voice/立花希/031313390.ogg"
    lhx "多亏了凉君说了些让人失望的话。"
    me01 "你要是不想和我一起的话我就先回去了。"
    pause 0.1 hard
    scene set only lhx_cg touch3
    $ flcam.move(-2200, -2800, 800, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031313400.ogg"
    lhx "别、别开玩叫了！（咬舌）"
    play voice "voice/立花希/031313410.ogg"
    lhx "一下子就好......再等等~"
    play voice "voice/立花希/031313420.ogg"
    lhx "这种程度的话......也不是不行。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "立花希把脸凑了过来。"
    "在我的脸颊上亲了一下。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school evening inside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313460.ogg"
    lhx "真拿你没办法。"
    show lhx_dsf_b2 b2 b2_h3 
    play voice "voice/立花希/031313430.ogg"
    lhx "还请不要对我做下流的事。"
    me01 "立花老师。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide lhx_dsf_b3
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 1.0 hard
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141301560.ogg"
    qcls "啊啦啊啦~"
    show wflash onlayer texture
    play sound jump_1
    with vpunch
    play music second_108 fadein 3.0 if_changed
    hide qcls_zf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313480.ogg"
    lhx "凉君，我的眼睛里好像进了什么脏东西，好在现在取出来了。"
    me01 "是吗，这样的话我也算没白忙活。"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031313490.ogg"
    lhx "可是在旁人的眼中可能不是这样的所以很容易就会招来误会。"
    me01 "是啊，搞错的话就麻烦了啊哈哈。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313500.ogg"
    lhx "比如像千川老师这样的明白人，想必不用我们多说也能看出这是一场误会了吧？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show qcls_zf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/千川老师/141301570.ogg"
    qcls "是的，我完全没有想过两位是为了遮羞而导演这场闹剧来辩解哟~"
    stop music fadeout 5.0
    show lhx_dsf_b2 b2 b2_h3
    play voice "voice/立花希/031313510.ogg"
    lhx "竟然忘了千川老师还在，真是大意了......（小声）"
    play music second_111 fadein 3.0 if_changed
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141301580.ogg"
    qcls "不过二位看起来和好如初了呢。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031313520.ogg"
    lhx "本来就没有吵架。"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/141301590.ogg"
    qcls "也是呢，毕竟恋爱即是战争嘛~"
    me01 "看到了吗......刚才的？"
    "难道说{rb}灵继者{/rb}{rt}elfin{/rt}的身份暴露了？"
    show qcls_zf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/千川老师/141301600.ogg"
    qcls "是的，看到二位深情的拥抱真叫人回味无穷。"
    "原来是指这个啊。"
    show lhx_dsf_b2 b2 b2_h3
    play voice "voice/立花希/031313530.ogg"
    lhx "抱歉......让您费心了。"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/141301620.ogg"
    qcls "哪里的话，相反我还想要祝福你们。"
    show lhx_dzf_b2 b2 b2_h3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031313540.ogg"
    lhx "调侃的话就不用了。"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/141301640.ogg"
    qcls "找到答案了吗？"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313570.ogg"
    lhx "托您的福。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day216.kindergarden_event06:
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    show snow_level1 onlayer fg
    with dissolve
    pause 2.0 hard
    scene set only school night outside xuejian
    play music second_142 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031313780.ogg"
    lhx "还是没赶上去新城区。"
    me01 "作为补偿，我送你回家吧？"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313810.ogg"
    lhx "那就麻烦你充当保镖了~"
    me01 "顺便能牵个手吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313820.ogg"
    lhx "......"
    me01 "还是说抱起来更好？"
    show lhx_dsf_b2 b2 b2_h3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031313830.ogg"
    lhx "才、才不要，那不是更让人害羞了吗？"
    me01 "那就留到以后吧。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313840.ogg"
    lhx "......以后？"
    me01 "是啊，等到我们的关系已经不需要再“请示对方”的时候。"
    play voice "voice/立花希/031313850.ogg"
    lhx "......"
    me01 "不明白吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313860.ogg"
    lhx "不......只是觉得心情有些复杂而已。"
    me01 "总之保持平常心就行了。"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031313890.ogg"
    lhx "真是随便啊~"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031313900.ogg"
    lhx "不过我倒是有点好奇约会的时候一般都会做些什么？"
    me01 "大概......就是测体温之类的吧？"
    "至少琉璃是这么说的。"
    "应该没有骗我吧。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313920.ogg"
    lhx "真是不可靠啊。"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031313930.ogg"
    lhx "姑且期待一下好了~"
    me01 "那我们出发吧。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313940.ogg"
    lhx "......"
    me01 "这次又怎么了？"
    show lhx_dsf_b2 b2 b2_n6
    play voice "voice/立花希/031313950.ogg"
    lhx "托凉君的福我现在发现稍微......有一点改变了。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031313960.ogg"
    lhx "就算我不去追赶，凉君也会主动来到我身边了。"
    play voice "voice/立花希/031313980.ogg"
    lhx "就照这个势头调教成跑腿的好了~"
    me01 "是时候先把你那肮脏的思维整理一下了。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day216_bridge_event01:
        $ seen_day216_bridge_event01 = True
    $ _overworld_label = 'day216.bridge_event01'
    jump day216.map

label day216.laboratory_event01:
    $ flcam.move(0, 0, 0)
    play sound phone1
    pause 1.0 hard
    scene set only laboratory inside2 xuejian
    with slowdissolve
    $ flcam.move(3800, -400, 800, duration=1.5)
    play music second_122 fadein 3.0 if_changed
    pause 1.0 hard
    investigation call block shy_yjf_b1 b1 b1_sp1 onlayer m2:
        screen_pos (0.42, 1.0)
        screen_direction right
    nvl clear
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151100020.ogg"
    c.shy_yjf_b1 "怎么了，你主动打电话过来还真是罕见？"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100030.ogg"
    c.shy_yjf_b1 "现在还没有发现灵纹暴走的迹象，所以你还没有行动的必要。"
    play voice "voice/圣护院/151100040.ogg"
    c.shy_yjf_b1 "虽然目前让水之濑行动的次数居多，但对你我依旧还是很信任的。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151100050.ogg"
    c.shy_yjf_b1 "毕竟你的灵纹作为我们工作的后援是最合适不过的。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151100060.ogg"
    c.shy_yjf_b1 "原来如此......今天发生了这样的事吗。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100070.ogg"
    c.shy_yjf_b1 "虽然早就料到目标会是立花希或者日向爱衣的其中一方。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151100080.ogg"
    c.shy_yjf_b1 "也就是说日向爱衣是关键灵继者的可能性更高吗？"
    play voice "voice/圣护院/151100090.ogg"
    c.shy_yjf_b1 "但到目前为止，从她身上都没有感觉到任何灵纹觉醒的迹象。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151100100.ogg"
    c.shy_yjf_b1 "是这样啊......原来如此。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100110.ogg"
    c.shy_yjf_b1 "你的假设倒也是合情合理。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151100130.ogg"
    c.shy_yjf_b1 "那个吊坠没准和这座研究所一样使用了什么特殊的材料。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151100140.ogg"
    c.shy_yjf_b1 "如果立花希的身上也有类似的“信物”的话，这一切就可以顺理成章地解释清楚了。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151100150.ogg"
    c.shy_yjf_b1 "啊我知道的，我并没有打算破坏现在的和平。"
    show shy_yjf_b1 b1 b1_n3
    play voice "voice/圣护院/151100160.ogg"
    c.shy_yjf_b1 "你就继续监视日向爱衣，我会给出进一步指示的。"
    investigation call end
    play sound phone2
    pause 0.5 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151100170.ogg"
    shy "......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151100180.ogg"
    shy "和她的对话在某种意义上和与水之濑一样都很累人。"
    play voice "voice/圣护院/151100190.ogg"
    shy "也许是因为她有点......太过善良了吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian3
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "圣护院朝窗外望去。"
    "天空依旧下着雪。"
    "这场景不禁会让人联想起最近频发的异常气候。"
    "雪见市的形式越来越不安定了。"
    "正因如此，才不得不加快研究的进度。"
    "失败是不被允许的。"
    "这也是一个隶属于星天宫的研究员应该背负的使命。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    scene set only laboratory inside1 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    play music second_124 fadein 3.0 if_changed
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/白羽/711000500.ogg"
    baiyu "原来如此。"
    play voice "voice/白羽/711000510.ogg"
    baiyu "圣护院在这座城市指挥的{rb}灵继者{/rb}{rt}elfin{/rt}们。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711000520.ogg"
    baiyu "其中最有可能和库洛诺斯有所联系的，应该也只有刚刚打电话过来的她了吧......"
    play voice "voice/白羽/711000530.ogg"
    baiyu "圣护院一定也察觉到对方在当双面间谍。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711000540.ogg"
    baiyu "即使如此也还是置之不理，是因为还有利用价值吗？"
    play voice "voice/白羽/711000550.ogg"
    baiyu "把研究所的情报通报给库洛诺斯，同时也把库洛诺斯的情报传递给我们。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000560.ogg"
    baiyu "虽然这么做很大程度上等同于玩火自焚，不过我也暂且和圣护院一样利用一下吧。"
    show baiyu_yjf_b1 b1 b1_n3
    play voice "voice/白羽/711000570.ogg"
    baiyu "如果大和教授始终认为雪见市的异常气候与{rb}灵继者{/rb}{rt}elfin{/rt}的觉醒有关。"
    play voice "voice/白羽/711000580.ogg"
    baiyu "同时怀疑研究所这边之所以垄断气象研究，是为了独占{rb}灵继者{/rb}{rt}elfin{/rt}的话。"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711000590.ogg"
    baiyu "那么为了阻止这一切的他必定会采取某些行动的吧。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000610.ogg"
    baiyu "不只是星天宫研究所，就连库洛诺斯也想要争抢{rb}灵继者{/rb}{rt}elfin{/rt}......"
    show baiyu_yjf_b1 b1 b1_ga2
    play voice "voice/白羽/711000620.ogg"
    baiyu "不过如果对方一直按兵不动的话，也没有比这更好的消息了。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000640.ogg"
    baiyu "不会堆积的雪却停留在人心上......吗。"
    show baiyu_yjf_b1 b1 b1_s2
    play voice "voice/白羽/711000650.ogg"
    baiyu "所以我们才能与之共鸣。"
    play voice "voice/白羽/711000660.ogg"
    baiyu "就像是天使在召唤被选中的勇者一般。"
    show baiyu_yjf_b1 b1 b1_s3
    play voice "voice/白羽/711000670.ogg"
    baiyu "如果真是“那孩子”的歌声催生了这座城市的{rb}灵继者{/rb}{rt}elfin{/rb}。"
    show baiyu_yjf_b1 b1 b1_n1
    play voice "voice/白羽/711000680.ogg"
    baiyu "那像现在这样堆积的白雪，就是纷争的战场准备就绪的前兆了吧。"
    play voice "voice/白羽/711000700.ogg"
    baiyu "由“你”亲手刻画的这条道路。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711000710.ogg"
    baiyu "我一定会让它延续下去的——"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000730.ogg"
    baiyu "不与“那孩子”产生公感的话，就无法获得{rb}灵纹{/rb}{rt}rune{/rt}。"
    show baiyu_yjf_b1 b1 b1_s2
    play voice "voice/白羽/711000740.ogg"
    baiyu "简直......就像小孩子渴望玩伴一样。"
    play voice "voice/白羽/711000750.ogg"
    baiyu "只要大和教授依然对{rb}灵继者{/rb}{rt}elfin{/rb}抱有敌意，他就永远也无法理解这个真相吧。"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711000760.ogg"
    baiyu "亦或者说......即便是他也是会改变的吗？"
    play voice "voice/白羽/711000770.ogg"
    baiyu "也许真的会因为雪见市的这场雪而有所改变也说不定。"
    show baiyu_yjf_b1 b1 b1_s3
    play voice "voice/白羽/711000790.ogg"
    baiyu "第三年的寒冬，我能为“那孩子”做的事情几乎已经没有了......"
    show baiyu_yjf_b1 b1 b1_s4
    play voice "voice/白羽/711000800.ogg"
    baiyu "但我还不想就这样停下。"
    show baiyu_yjf_b1 b1 b1_n2
    play voice "voice/白羽/711000810.ogg"
    baiyu "虽然很抱歉......但还是请青木家的那位稍微协助一下我们的工作吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day217
