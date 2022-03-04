
label inside_battle7(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "擅长居合道的水之濑凛具有优秀的攻击属性颇为棘手。"
    "此战为「防守战」，胜利条件为在一定的回合数内保证队伍成员的存活。"
    "尽可能利用「雷亚」的{color=#f00}星空梦影{/color}进行{color=#f00}减伤{/color}以及使用{color=#f00}护盾{/color}能够大大提升队伍的生存空间。"
    "与此同时利用「冰」与「水」引发的{color=#3ff}冻结{/color}反应能有效限制敌人的行动；利用「岩」元素与其他元素引发的{color=#ff0}结晶{/color}反应也能够为队伍成员提供吸收伤害的护盾。"
    "另外芙兰前辈提供的新道具「魔法药草」也能在队伍成员阵亡的情况下进行{color=#f00}复苏{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label inside_battle8(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "被偷袭的水之濑并没有办法发挥出完全的实力，趁现在击败她是最佳时机。"
    "水之濑的元素爆发「幻镜化物」期间免疫控制效果，需多加留意。"
    "尽可能使用{color=#f00}星空梦影{/color}结界提供的{color=#f00}减伤buff{/color}抵挡，同时要当心「雷」与「火」引发的{color=#f66}超载{/color}反应伤害将无视免伤机制。"
    "输出方面多借助{color=#6f6}扩散{/color}反应的减抗效果配合「空间跳跃」的结界能够达到不俗的伤害。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label inside_battle9(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "在巫女神乐的作用下「藤原瞳」获得伤害免疫。"
    "{color=#f00}优先解决{/color}她身边的「见习巫女」能够破除结界的效果。"
    "与此同时巫女的实力得到了强化，所有攻击均为{color=#f00}范围群体伤害{/color}，需要特别留意。"
    "巫女上场的顺序依次为{color=#f30}「火」{/color}、{color=#f0f}「雷」{/color}、{color=#99f}「水」{/color}、{color=#3ff}「冰」{/color}、{color=#6f6}「风」{/color}，应合理避免威胁较大的元素反应。"
    "利用「雷亚」与「青木翔子」配合打出{color=#3ff}冻结{/color}反应可以限制对方行动，同时与「日向爱衣」的{color=#f30}火元素{/color}伤害配合打出{color=#9cf}融化{/color}、{color=#9cf}蒸发{/color}反应能够最大化伤害输出。"
    "「日向爱衣」能够为团队成员{color=#f00}驱散负面、控制效果{/color}，「青木翔子」能够{color=#f00}治疗{/color}我方单位，合理利用该机制能够有不错的拉扯效果。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label day215:
    bookmark
    $ save_name = _("Day 215")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date213 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only home day lhx_room xuejian
    play music second_114 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_n4 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031303590.ogg"
    lhx "......"
    me01 "起来了吗立花老师。"
    play voice "voice/立花希/031303600.ogg"
    lhx "......"
    me01 "早上好。"
    show lhx_dsf_b2 b2 b2_n4 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031303610.ogg"
    lhx "......"
    me01 "还很困吗？"
    play voice "voice/立花希/031303620.ogg"
    lhx "......"
    me01 "去洗把脸吧。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303630.ogg"
    lhx "......"
    me01 "早餐马上就好。"
    show lhx_dsf_b3 b3 b3_n4 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031303640.ogg"
    lhx "......"
    show lhx_dsf_b3 b3 b3_n4 at walkout_r(0.5)
    pause 0.5 hard
    play sound open_door5
    hide lhx_dsf_b3
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "虽然有点担心昨天的事情再次发生。"
    "但是身为女孩子再怎么说也不会连续两次......"
    pause 0.5 hard
    play sound open_door5
    play voice "voice/立花希/031303650.ogg"
    lhx "衣服......"
    pause 1.0 hard
    scene set only lhx_cg xizao1
    play music second_108 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031303660.ogg"
    lhx "我的衣服......在哪里？"
    with vpunch
    "大意了，这家伙完全不是一般的女孩子？！"
    play voice "voice/立花希/031303670.ogg"
    lhx "替换的衣服......在哪？"
    me01 "刚才不是拿在手上的吗？"
    play voice "voice/立花希/031303680.ogg"
    lhx "丢进洗衣机不见了。"
    me01 "那就自己去房间里再拿一件！"
    play voice "voice/立花希/031303690.ogg"
    lhx "去帮我拿......日向。"
    me01 "抱歉，我不是日向。"
    play voice "voice/立花希/031303700.ogg"
    lhx "......"
    pause 0.1 hard
    scene set only lhx_cg xizao2
    $ flcam.move(1100, -1400, 450, duration=1.5)
    with dissolve
    pause 0.5 hard
    play voice "voice/立花希/031303710.ogg"
    lhx "为什么凉君你会在这里啊？"
    me01 "就算你这么问......"
    play voice "voice/立花希/031303720.ogg"
    lhx "非法入侵吗？"
    me01 "快醒过来！"
    play voice "voice/立花希/031303730.ogg"
    lhx "为什么要把视线移开？"
    me01 "这种事情请别让我来说明。"
    play voice "voice/立花希/031303740.ogg"
    lhx "不肯看我这边，就是在思考下流事情的证据。"
    play voice "voice/立花希/031303750.ogg"
    lhx "果然是非法入侵吗？"
    me01 "现在可是有个比那更大的罪名摆在我面前。"
    play voice "voice/立花希/031303760.ogg"
    lhx "难道你是来偷情的？"
    me01 "唯独不想被这幅样子的你数落。"
    play voice "voice/立花希/031303770.ogg"
    lhx "这幅样子？"
    pause 0.1 hard
    play sound jump_1
    scene set only lhx_cg xizao3
    $ flcam.move(0, 0, 0, duration=1.5)
    with dissolve
    pause 0.5 hard
    play voice "voice/立花希/031303780.ogg"
    lhx "！？"
    play voice "voice/立花希/031303790.ogg"
    lhx "我的......裸体？"
    play voice "voice/立花希/031303800.ogg"
    lhx "在凉君......面前。"
    play voice "voice/立花希/031303810.ogg"
    lhx "为、为什么？"
    play voice "voice/立花希/031303820.ogg"
    lhx "我知道了。"
    pause 0.1 hard
    scene set only lhx_cg xizao4
    $ flcam.move(1100, -1400, 450, duration=1.5)
    with dissolve
    pause 0.5 hard
    play voice "voice/立花希/031303830.ogg"
    lhx "这一定是噩梦的延续。"
    play voice "voice/立花希/031303840.ogg"
    lhx "肯定是那样没错的。"
    play voice "voice/立花希/031303850.ogg"
    lhx "毕竟刚才做的梦，就是被凉君侵犯的情节。"
    me01 "你做的都是哪门子的春梦啊！？"
    play voice "voice/立花希/031303860.ogg"
    lhx "反正都这样了，不如反过来让我来侵犯凉君。"
    play voice "voice/立花希/031303870.ogg"
    lhx "这样一定，就能从噩梦中醒来了。"
    me01 "别黑化啊！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    play sound open_door5
    "立花希一边骂骂咧咧，一边走向了自己房间。"
    pause 1.0 hard
    scene set only home day lhx_room xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/立花希/031303880.ogg"
    lhx "不是梦......"
    show lhx_dsf_b1 b1 b1_s3
    play voice "voice/立花希/031303890.ogg"
    lhx "感受到了来自现实的羞辱。"
    me01 "别抱怨了，我刚刚可是全程闭着眼睛的。"
    hide lhx_dsf_b1 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_a1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/031303900.ogg"
    lhx "为什么不看啊！"
    me01 "生气的理由变得有些奇怪了？！"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031303910.ogg"
    lhx "去死好了......让凉君堕入比死还痛苦的地狱去吧。"
    stop music fadeout 5.0
    "诅咒又开始蔓延了......"
    pause 1.0 hard
    play sound rune1
    $ flcam.move(7500, 0, 1500, duration=1.5)
    pause 1.0 hard
    "突然一阵灵力波动打破了这份尴尬的氛围。"
    "似乎有一股不安从胸口蔓延开来。"
    play music second_126 fadein 3.0 if_changed
    $ flcam.move(0, 0, 600, duration=1.0)
    pause 0.5 hard
    "这种感觉是......"
    "和之前小桃还有友加暴走时候的感觉一样。"
    "不安、恐惧的能量波动。"
    "立花老师还不知道{rb}灵纹{/rb}{rt}rune{/rt}的存在，不能冒然地把她牵扯进来。"
    "看来只能我自己去解决了。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    me01 "抱歉立花老师，我得出去一趟。"
    me01 "我会尽量赶在晚饭前回来的。"
    play voice "voice/立花希/031303960.ogg"
    lhx "......"
    hide lhx_dsf_b3
    $ flcam.move(5500, 0, 1100, duration=1.5)
    pause 1.0 hard
    play sound close_door2
    with vpunch
    pause 2.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303980.ogg"
    lhx "刚才的确感觉到了异常的{rb}灵纹{/rb}{rt}rune{/rt}波动。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_s3
    pause 0.1 hard
    play sound rune2
    show lhx_dsf_b3 b3 b3_rs1 with dissolve
    play voice "voice/立花希/031303990.ogg"
    lhx "本来还想在屋子里待上一整天的......"
    stop music fadeout 3.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 3.0 hard
    $ _overworld_label = 'day215'
    $ seen_day215_home_event01 = False
    $ seen_day215_bridge_event01 = False

label day215.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    show snow_level1 onlayer fg
    if _overworld_label == 'day215':
        $ flcam.move(*overworld.camera_positions['road2'])
    elif _overworld_label == 'day215.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该先去哪里呢......" nointeract
    call screen rughzenhaide(
        bridge=("day215.battle_szl_first", "not seen_day215_bridge_event01"),
        road1=("day215.home_event01", "not seen_day215_home_event01 and seen_day215_bridge_event01"))
    $ window_animate_outro()
    if _return == 'day215.battle_szl_first':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day215.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
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

label day215.battle_szl_first:
    $ flcam.move(0, 0, 0)
    play sound jiaobu3
    scene set only bridge day xuejian alpha
    show snow_level1 onlayer fg
    $ flcam.move(5200, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show szl_dzf_b1 b1 b1_a1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/水之濑/051504760.ogg"
    szl "......"
    me01 "水之濑同学？"
    show szl_dzf_b1 b1 b1_s1
    play voice "voice/水之濑/051504770.ogg"
    szl "......"
    stop music fadeout 5.0
    $ flcam.move(5200, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dzf_b1
    show szl_dzf_b2 b2 b2_s4 onlayer m2:
        xpos 0.7
    "水之濑没有说话，而是以一个眼神示意我往河滩的方向移动。"
    "虽然对于她的突然出现心里多少有些不安，可我还是跟了上去。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play music second_125 fadein 3.0 if_changed
    scene set only bridge day under xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_b3 b3 b3_s1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    me01 "抱歉了水之濑同学，今天的我可功夫和你分胜负。"
    play voice "voice/水之濑/051504780.ogg"
    szl "......"
    hide szl_dzf_b3
    show szl_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051504790.ogg"
    szl "今天又......"
    show szl_dzf_b1 b1 b1_n2
    play voice "voice/水之濑/051504800.ogg"
    szl "被你给抢先了。"
    me01 "抢先了......你在说什么？"
    show szl_dzf_b1 b1 b1_s1
    play voice "voice/水之濑/051504810.ogg"
    szl "......"
    me01 "难不成水之濑同学你也是......"
    hide szl_dzf_b1
    show szl_dzf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    show szl_dzf_b2 b2 b2_s4
    play voice "voice/水之濑/051504830.ogg"
    szl "就是你想的那样吧。"
    show szl_dzf_b2 b2 b2_n2
    play voice "voice/水之濑/051504840.ogg"
    szl "可以问你一个问题吗？"
    me01 "什么？"
    show szl_dzf_b2 b2 b2_n3
    play voice "voice/水之濑/051504850.ogg"
    szl "并不喜欢{rb}灵纹{/rb}{rt}rune{/rt}的你。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/051504860.ogg"
    szl "并不喜欢应付这种局面的你......"
    show szl_dzf_b2 b2 b2_s2
    play voice "voice/水之濑/051504870.ogg"
    szl "但为什么总要执着于这些和你无关的事情呢？"
    me01 "我只是觉得如果自己不做点什么的话。"
    me01 "就又会失去什么重要的东西了。"
    me01 "我已经......不想再体会失去的感觉了。"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051504880.ogg"
    szl "也是呢......"
    hide szl_dzf_b3
    show szl_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051504890.ogg"
    szl "尽管如此我也有任务在身。"
    hide szl_dzf_b1
    show szl_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051504900.ogg"
    szl "所以这次还请你不要来碍事！"
    me01 "刚才我也说了今天可没空与你比试，还有更重要的事等着我去处理。"
    hide szl_dzf_b2
    show szl_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051504920.ogg"
    szl "那样的话......"
    stop music fadeout 5.0
    pause 0.5 hard
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dzf_b1 with None
    pause 0.1 hard
    show jingya onlayer texture:
        xpos 0.0
    show szl_dzf_knife_b3_rune b3 b3 b3_a2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/水之濑/051504930.ogg"
    szl "{rb}幻镜化物{/rb}{rt}apports{/rt}！"
    play sound rune3
    pause 1.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    hide snow_level1
    pause 3.0 hard
    play music second_150 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf1
    with in2out_02_l
    pause 1.5 hard
    me01 "太刀！？"
    me01 "是什么时候？"
    play voice "voice/水之濑/051504940.ogg"
    szl "放马过来吧。"
    me01 "......"
    play voice "voice/水之濑/051504950.ogg"
    szl "对我来说，现在的你是碍事之人！"
    play voice "voice/水之濑/051504960.ogg"
    szl "这就足够了吧，战斗理由什么的。"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    $ flcam.move(2200, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051504970.ogg"
    szl "而且我现在正好......很闲啊。"
    play voice "voice/水之濑/051504980.ogg"
    szl "托某位爱管闲事之人的福。"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play voice "voice/水之濑/051504990.ogg"
    szl "就请你配合我一下吧。"
    play voice "voice/水之濑/051505000.ogg"
    szl "帮我打发下时间。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "可恶，明明没有时间在这里耗着才对。"
    "却偏偏遇上了最棘手的敌人。"
    "这家伙认真起来可是超级难缠的啊！"
    "不过既然她也是{rb}灵继者{/rb}{rt}elfin{/rt}的话。"
    "既然她也是阻挡我前进之人的话。"
    "那么现在......"
    pause 1.0 hard
    play sound rune2
    $ flcam.move(0, 0, 0)
    scene set only myself_cg four
    with slowdissolve
    pause 1.0 hard
    me01 "也只有上了——"
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
    scene set only fight_cg bridge2
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        # 角色装备为传说6件秋之韵-素律、雷伤套，等级10，技能满级
        szl_role_mirror.equip_experience = 99999999
        selected_equipments = ["weapon_num11_04", 
                               "armor_num11_04", 
                               "necklace_num11_04", 
                               "ring_num11_04",
                               "magic_light_04",
                               "stone_light_04"]
        for cate in szl_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments and outfit.category == cate)]
            sample_outfit = enemy_outfits[0]
            sample_outfit.init_params()
            for xi in range(9):
                sample_outfit.level_up(szl_role_mirror, 100)
            sample_outfit.enemy_equip_on(szl_role_mirror)
        for xi in range(20):
            szl_role_mirror.skill_levelup()

        ## 必输剧情-生存战
        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

        local_config.tutorial_step = "生存战"

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=szl_role_mirror, 
                boss_hp_plus=999999,
                side_enemy=[], 
                side_hp_plus=0,
                level=32,
                boss_first=True, 
                win_condition='stay', 
                stay_turn=10, 
                inside_label="inside_battle7", 
                mission_type="normal", 
                treasures={
                    "eggs": (2, 0.6),
                    "soul_piece": (2, 0.3),
                    "soul_raise": (2, 0.3),
                    "light_break_small": (3, 0.3),
                    "light_break_large": (1, 0.3)
                })

    if _return == "win":
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day215.after_battle_szl_first

label day215.after_battle_szl_first:
    scene black
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play music second_150 fadein 3.0 if_changed
    "我从掌心发出{rb}念动立场{/rb}{rt}psychokinesis{/rt}。"
    "强大的风压直逼水之濑的跟前。"
    "然而......"
    pause 1.0 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    scene set only szl_cg fight dzf3
    with dissolve
    "就在我还担心立场会不会伤到水之濑的时候，一道斩击轻而易举地将其一分为二了。"
    "以肉眼完全无法跟上的速度，甚至没有看到刀身被拔出的动作。"
    "但凌然的剑气却早已呼啸而过。"
    "这速度可谓是流光一般。"
    "如此精湛的剑技令人不寒而栗。"
    "不妙啊......"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    with dissolve
    play voice "voice/水之濑/051505010.ogg"
    szl "不愧是你。"
    me01 "不，要我说刚才那一下如果水之濑同学认真的话我可能已经输了吧。"
    "虽然很不甘心，眼前的对手不是我一个人能够应付得了的。"
    "不同于小桃和友加，水之濑那精湛的剑技加上对灵力冷静且熟练的操控，像我这样的半吊子一瞬间便可以分出胜负。"
    "能在一瞬间做到收挥自如的战技。"
    "莫非这就是——{encyclopedia=juhe}居合{/encyclopedia}。"
    pause 1.0 hard
    scene set only bridge day under xuejian alpha
    show snow_level1 onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_knife_b3_rune b3 b3 b3_n2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    "没有给我太多思考的时间，下一道斩击迎面袭来。"
    "虽然对方的攻击刻意避开了我的身体，但是伴随而来的剑气依旧是把我整个人都推了出去。"
    "怎么回事，就算是剑术再怎么精湛的剑士，也不可能同时完成拔刀加挥砍两个高难度动作。"
    "刚刚的攻击如果不使用{rb}念动立场{/rb}{rt}psychokinesis{/rt}的话，一般人感觉根本无法躲开。"
    "从斩击的威力来看，一定是从比现在更近的距离发起的。"
    "这究竟是怎么回事？"
    show szl_dzf_knife_b3_rune b3 b3 b3_n1
    play voice "voice/水之濑/051505020.ogg"
    szl "我用的可不仅仅是{rb}灵纹{/rb}{rt}rune{/rt}那么简单。"
    show szl_dzf_knife_b3_rune b3 b3 b3_n2
    play voice "voice/水之濑/051505030.ogg"
    szl "如你所见，我还混入了居合道剑术。"
    hide szl_dzf_knife_b3_rune
    show szl_dzf_knife_b2_rune b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505040.ogg"
    szl "但是果然......你也不赖。"
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505050.ogg"
    szl "这种程度的斩击你都能躲开。"
    me01 "那还真是谢谢你的手下留情。"
    play sound rune2
    show wflash onlayer texture
    pause 0.5 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only myself_cg four
    with dissolve
    pause 1.0 hard
    "没时间松懈，我只能连续不断地利用{rb}念动立场{/rb}{rt}psychokinesis{/rt}抵挡剑气。"
    "虽然知道没有什么胜算，但是这是当下唯一能够牵制对方的办法了。"
    "不快点找到突破口的话......"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    with dissolve
    play sound hite_knife3
    show knife onlayer texture
    pause 0.5 hard
    "数道斩击再次浮现。"
    play sound hite_knife3
    show knife2 onlayer texture
    pause 0.5 hard
    "仅仅就在一瞬间，全力施展的力场就被瓦解了。"
    "怎么办，拼尽全力却是连牵制都算不上。"
    "再加上{rb}幻镜化物{/rb}{rt}apports{/rt}的加持，想要拉开身位也几乎是不可能的事情。"
    "难道真的无计可施了吗？"
    me01 "但是......"
    pause 1.0 hard
    scene white
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_cg end one
    show sepiagrain onlayer fg
    with dissolve
    pause 0.5 hard
    scene set only lisite_cg final one
    with dissolve
    pause 0.5 hard
    scene set only xz_cg yume end one
    with dissolve
    pause 0.5 hard
    scene set only xfe_cg bridge normal
    with dissolve
    pause 0.5 hard
    hide sepiagrain
    scene black
    with dissolve
    pause 1.0 hard
    scene set only myself_cg five
    $ flcam.move(-1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    me01 "怎么能就这样放弃！"
    "就算暂时没有对策，只要能继续牵制住的话。"
    "再厉害的对手也总会有露出破绽的时候。"
    "一定要仔细观察对方的动作，千万不能看漏了任何关键细节。"
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 1.0 hard
    "对于现在的水之濑而言，完全可以直接结束战斗。"
    "但是她并没有这么做。"
    "这样的行为也能够理解，毕竟拖延时间才是她的目的。"
    "既然如此，执着于胜负的她此刻的“不求胜”说不定就是我致胜的关键。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg fight dzf2
    with dissolve
    play voice "voice/水之濑/051505060.ogg"
    szl "你怎么了，战局一边倒啊~"
    play voice "voice/水之濑/051505070.ogg"
    szl "{rb}念动立场{/rb}{rt}psychokinesis{/rt}并不是那么没用的{rb}灵纹{/rb}{rt}rune{/rt}吧？"
    play voice "voice/水之濑/051505080.ogg"
    szl "呐神野君......"
    play voice "voice/水之濑/051505090.ogg"
    szl "如果这场胜负我赢了。"
    pause 0.1 hard
    scene set only szl_cg fight dzf1
    $ flcam.move(2200, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051505100.ogg"
    szl "你就加入星天宫吧。"
    me01 "为什么非得听你的不可？"
    play voice "voice/水之濑/051505110.ogg"
    szl "当然我也知道你有你的顾虑。"
    play voice "voice/水之濑/051505120.ogg"
    szl "但是如果我赢的话......就请你离开你现在的组织。"
    play voice "voice/水之濑/051505130.ogg"
    szl "这才是所谓的胜负。"
    me01 "如果我拒绝呢？"
    pause 0.1 hard
    scene set only szl_cg fight dzf2
    $ flcam.move(3200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051505140.ogg"
    szl "那样的话......"
    me01 "等等，不要突然摆出“那就杀掉你”这样危险的姿势啊！"
    me01 "我说了只是如果吧。"
    "从水之濑刚刚的话中能够得到几个线索。"
    "首先她希望我加入星天宫，也就是说她自己本身也是星天宫的一员。"
    "而且翔子和铃音曾提到过水之濑之前送了一位研究所的{rb}客人{/rb}{rt}藤原瞳{/rt}来过家里。"
    "另外这座桥是通往新城区的必经之路，而她在我察觉到灵力的同时就提前在这里阻拦我。"
    "也就是说这场暴走的背后一定和星天宫的研究所脱不了干系。"
    "不难推测出圣护院主任她们一直在瞒着我进行着什么秘密行动。"
    "最后，她刚刚要我离开原来的组织。"
    "也就是说她对我的了解也只有擅长的{rb}灵纹{/rb}{rt}rune{/rt}这方面而已。"
    "圣护院主任说过，世界各地的{rb}灵继者{/rb}{rt}elfin{/rt}是分属于不同的组织管辖的，也就是说她把我当成其他势力的人了吗？"
    "过去了这么久，{rb}灵纹{/rb}{rt}rune{/rt}的感应越来越微弱，已经不能再这样耗下去了。"
    "可是执着于胜负的水之濑不是那么容易就能打发的......还提出了这样的条件。"
    "为什么这家伙就这么想拉我入伙呢。"
    "等等，同伴......"
    pause 1.0 hard

label day215.battle_szl_second:
    $ flcam.move(0, 0, 0)
    scene set only bridge evening under xuejian alpha
    show snow_level1 onlayer fg
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_knife_b2_rune b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    me01 "我知道了，投降了投降。"
    me01 "我同意加入星天宫。"
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505150.ogg"
    szl "......"
    "我中断了念波举起双手。"
    show szl_dzf_knife_b3_rune b3 b3 b3_ga1
    play voice "voice/水之濑/051505160.ogg"
    szl "......怎么了突然？"
    me01 "毕竟再怎么样我也不是水之濑同学的对手。"
    me01 "而且你也那么明显地放水了。"
    hide szl_dzf_knife_b3_rune
    show szl_dzf_knife_b2_rune b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505170.ogg"
    szl "也是啊，不管怎么样你的攻击对我是完全无效的。"
    me01 "相对的，水之濑的每一次攻击却都能将我击败。"
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505200.ogg"
    szl "那样完美地避开了数次攻击的你，还真敢说啊。"
    hide szl_dzf_knife_b3_rune
    show szl_dzf_knife_b2_rune b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505210.ogg"
    szl "能使用{rb}念动立场{/rb}{rt}psychokinesis{/rt}来回避斩击，能做到这种事情的人......"
    me01 "但是总而言之还是没办法坚持太久的。"
    show szl_dzf_knife_b2_rune b2 b2 b2_ga1
    play voice "voice/水之濑/051505220.ogg"
    szl "这点程度就撑不住了吗？意外地没有体力啊。"
    me01 "水之濑同学，如果我同意加入星天宫。"
    me01 "你能答应我不要为难我身边的人吗？"
    me01 "换句话说，我能够把她们托付给你吗？"
    stop music fadeout 5.0
    hide szl_dzf_knife_b2_rune
    show szl_dzf_knife_b3_rune b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505230.ogg"
    szl "......"
    "水之濑没有回答。"
    "萦绕在她周身的{rb}灵纹{/rb}{rt}rune{/rt}波动也随即停止了。"
    play sound rune3
    show wflash onlayer texture
    hide szl_dzf_knife_b3_rune
    show szl_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    "随着灵力的消散她手中的刀也消失不见了。"
    $ flcam.move(0, -200, 750, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b3 b3 b3_s3
    play voice "voice/水之濑/051505240.ogg"
    szl "......原来如此。"
    hide szl_dzf_b3
    show szl_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505250.ogg"
    szl "那这里已经没你什么事了。"
    me01 "拉拢新的{rb}灵继者{/rb}{rt}elfin{/rt}入伙的话水之濑同学也会受到组织的嘉奖吗？"
    hide szl_dzf_b1
    show szl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505260.ogg"
    szl "......怎么样都好吧，那种事。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051505270.ogg"
    szl "再见。"
    pause 0.5 hard
    play sound jiaobu2
    show szl_dzf_b2 b2 b2_s1 at walkout_r(0.5)
    pause 1.5 hard
    hide szl_dzf_b2
    "水之濑的身影缓缓从我的身边经过。"
    "没有了对胜负的执着，我们之间的战斗也自然而然地迎来了终结。"
    "是啊，从刚刚的交手和谈吐间我意识到了。"
    "面对这样一个集正义、冷静、强大于一身的水之濑凛，凭我一人是无论如何都没有胜算的。"
    "但是啊，水之濑——"
    "胜负有的时候不是依靠实力就可以获得那么简单的，特别是像我这样不要脸的吊车尾！"
    pause 0.5 hard
    play sound touch
    show wflash onlayer texture
    with vpunch
    $ flcam.move(5200, -300, 900, duration=1.5)
    pause 0.5 hard
    show jingya onlayer texture:
        xpos 0.0
    show szl_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051505280.ogg"
    szl "{size=72}？！{/size}"
    play sound rune2
    "在水之濑从我身旁经过的一瞬间，我发动了{rb}念动立场{/rb}{rt}psychokinesis{/rt}。"
    "这个距离就算反应再快也来不及做出防守。"
    pause 1.0 hard
    $ flcam.move(5200, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 4.0 hard
    hide snow_level1
    play music second_161 fadein 3.0 if_changed
    pause 1.0 hard
    "孤注一掷并不是我原本的计划，但这却是眼下唯一可行的行动了。"
    "想要战胜凌驾于绝对正义之上的存在，那就从心理上寻找突破。"
    "能够战胜兼备居合道和{rb}幻镜化物{/rb}{rt}apports{/rt}的水之濑凛唯一的办法。"
    "如果说这样一个完美的人本身没有丝毫破绽的话，那她的优点——对伙伴的信任就是可以利用的唯一手段。"
    "说白了就是“偷袭”......这一次就让我来当个彻彻底底的反派吧。"
    "既然你我都有不可退让的理由，那就把一切都赌在这一次。"
    "即使这样还是输给了你，我也无悔了。"
    "毕竟这样优秀且完美的你，一定也能替我守护好我所在乎的一切——"
    "典型的道德绑架，此刻的我对于胜负早已没有了后顾之忧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge evening under xuejian alpha
    show snow_level1 onlayer fg
    $ flcam.move(5200, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dzf_knife_b1_rune b1 b1 b1_a2 onlayer m2:
        xpos 0.7
    play voice "voice/水之濑/051505290.ogg"
    szl "{rb}幻镜化物{/rb}{rt}apports{/rt}！"
    $ flcam.move(5200, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dzf_knife_b1_rune with None
    pause 0.1 hard
    show szl_dzf_knife_b3_rune b3 b3 b3_sp1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    me01 "没那么容易！"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    pause 1.0 hard
    hide snow_level1
    stop music fadeout 3.0
    play sound rune2
    scene white
    with slowerdissolve
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg bridge2
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        ## 敌方初始化参数
        # Boss为水之濑凛，巫女个数2，所有敌方角色技能等级12，巫女装备稀有随机等级10装备6件；水之濑装备为史诗6件秋之韵-素律、雷伤套
        selected_equipments = ["weapon_num11_03", 
                               "armor_num11_03", 
                               "necklace_num11_03", 
                               "ring_num11_03",
                               "magic_light_03",
                               "stone_light_03"]
        enemy_roles = [szl_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
        for role in enemy_roles:
            role.equip_experience = 99999999
            for cate in role.outfits:
                if role.name == "水之濑凛":
                    enemy_outfits = [outfit for outfit in outfit_list if (outfit.objectname in selected_equipments and outfit.category == cate)]
                    sample_outfit = enemy_outfits[0]
                else:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                sample_outfit.init_params()
                for xi in range(9):
                    sample_outfit.level_up(role, 100)
                sample_outfit.enemy_equip_on(role)

            # 巫女的技能替换成火属性
            if role.name != "水之濑凛":
                now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_fire"))
                role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
            else:
                for xi in range(20):
                    role.skill_levelup()

        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=szl_role_mirror, 
                boss_hp_plus=30000,
                side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                side_hp_plus=8000,
                level=30,
                boss_first=True,
                win_condition='normal',
                stay_turn=0,
                inside_label="inside_battle8", 
                mission_type="normal", 
                treasures={
                    "eggs": (3, 0.6),
                    "mana_eggs": (1, 0.3),
                    "soul_piece": (8, 0.3),
                    "soul_raise": (8, 0.3),
                    "light_break_small": (5, 0.3),
                    "light_break_large": (5, 0.3)
                })

    if _return == "win":
        "战斗胜利！"
        python:
            if "szl_role" not in local_config.role_pool:
                local_config.role_pool.add("szl_role")
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day215.after_battle_szl_second

label day215.after_battle_szl_second:
    scene white
    with dissolve
    pause 1.0 hard
    $ set_replay_scene("label11_1")
    $ flcam.move(-1100, -1400, 450)
    scene set only szl_cg fight dzf6
    play music second_161 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/水之濑/051505300.ogg"
    szl "......"
    pause 0.1 hard
    scene set only szl_cg fight dzf9
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "即便是在这种情况下使用{rb}念动立场{/rb}{rt}psychokinesis{/rt}提升速度的我，却依旧慢了一步。"
    "从刀身的状况可以看出，水之濑比我更快地握住了刀。"
    "而我却只是抓住她握刀的手。"
    play voice "voice/水之濑/051505310.ogg"
    szl "是我的......胜利呢。"
    "在最后还是失算了。"
    "本来以为只要使用{rb}增幅念动立场{/rb}{rt}hypnos-psychokinesis{/rt}就一定能夺下太刀的。"
    "还是没能到达吗......"
    "现在的我双手已经被牵制住了，无法施展任何{rb}灵纹{/rb}{rt}rune{/rt}。"
    "而一旦等我{rb}念动立场{/rb}{rt}psychokinesis{/rt}消失，水之濑再次夺回太刀的控制权，那我将必输无疑。"
    me01 "还没完呢。"
    pause 0.1 hard
    scene set only szl_cg fight dzf6
    with dissolve
    play voice "voice/水之濑/051505320.ogg"
    szl "别开玩笑了！"
    play voice "voice/水之濑/051505330.ogg"
    szl "竟然用这样卑鄙的手段。"
    play voice "voice/水之濑/051505340.ogg"
    szl "竟然这样轻易地欺骗我。"
    me01 "抱歉......"
    pause 0.1 hard
    scene set only szl_cg fight dzf8
    with dissolve
    play voice "voice/水之濑/051505350.ogg"
    szl "平时的话，我是绝不会上这种当的。"
    play voice "voice/水之濑/051505360.ogg"
    szl "一定会将你，将为了胜利不惜做到这个地步的你......"
    play voice "voice/水之濑/051505370.ogg"
    szl "理所当然地暴揍一顿。"
    me01 "你真是这么想的吗？"
    pause 0.1 hard
    scene set only szl_cg fight dzf5
    with dissolve
    play voice "voice/水之濑/051505380.ogg"
    szl "......事到如今你还想说什么？"
    play voice "voice/水之濑/051505390.ogg"
    szl "就算你还想使什么手段，我也不会再上当了。"
    play voice "voice/水之濑/051505400.ogg"
    szl "结果就是这样的。"
    me01 "多谢提醒。"
    play voice "voice/水之濑/051505410.ogg"
    szl "......"
    me01 "我确实还有“手段”没使出来。"
    me01 "这么早下结论可不像你的风格啊。"
    me01 "你应该比我更清楚的吧？"
    me01 "这场胜负......还没有分出来！"
    stop music fadeout 5.0
    play voice "voice/水之濑/051505420.ogg"
    szl "......也不知道你是认真的还是装的。"
    me01 "我们走着瞧吧。"
    play voice "voice/水之濑/051505430.ogg"
    szl "你以为已经使出全力的你还有胜算吗？"
    play voice "voice/水之濑/051505440.ogg"
    szl "还是说，你是故意没有拿出来......"
    me01 "那么我来了。"
    play voice "voice/水之濑/051505450.ogg"
    szl "......"
    play music second_142 fadein 3.0 if_changed
    pause 0.1 hard
    scene set only szl_cg fight dzf7
    $ flcam.move(-2200, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051505470.ogg"
    szl "{size=72}唔！{/size}"
    "我将身子往前靠了上去。"
    "双唇重合的瞬间我的视线里是早已紧闭双眼的水之濑。"
    "女孩子的体香还有那柔软的触感全都向我袭来。"
    pause 0.1 hard
    scene set only szl_cg fight dzf5
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051505480.ogg"
    szl "这就是......你的底牌吗？"
    play voice "voice/水之濑/051505490.ogg"
    szl "愚蠢的人，你以为就凭这种程度我就会畏怯吗？"
    play voice "voice/水之濑/051505510.ogg"
    szl "所谓的底牌，是为了“结束”而施展的东西吧？"
    pause 0.1 hard
    scene set only szl_cg fight dzf8
    with dissolve
    play voice "voice/水之濑/051505520.ogg"
    szl "而你的......"
    play voice "voice/水之濑/051505530.ogg"
    szl "这个吻。"
    play voice "voice/水之濑/051505540.ogg"
    szl "......却更像是为了“开始”的东西。"
    me01 "也许就如你说的那样。"
    me01 "就在刚刚我觉得就算是输给水之濑你也没什么好难过的。"
    me01 "但是有些东西我必须要自己去面对才行，就像水之濑同学追求的胜负一样。"
    me01 "当然我也不希望这一切就这样结束。"
    me01 "和水之濑的“胜负”，我希望能够继续这样进行下去。"
    "就像友加以{rb}灵纹{/rb}{rt}rune{/rt}作为维系和姐姐之间的羁绊一样。"
    "我和水之濑之间最直接有效的羁绊就是“胜负”。"
    me01 "为了开始的东西......听起来也不错呢。"
    pause 0.1 hard
    scene set only szl_cg fight dzf9
    $ flcam.move(-2200, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051505550.ogg"
    szl "好吧......"
    play voice "voice/水之濑/051505560.ogg"
    szl "那我就配合你。"
    stop music fadeout 5.0
    pause 1.0 hard 
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ end_replay()
    if not seen_day215_bridge_event01:
        $ seen_day215_bridge_event01 = True
    $ _overworld_label = 'day215.bridge_event01'
    jump day215.map

label day215.home_event01:
    $ flcam.move(0, 0, 0)
    play sound door_rill
    scene set only home evening passwalk xuejian
    with slowdissolve
    pause 2.0 hard
    play sound open_door4
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/翔子/011000530.ogg"
    xz "神野君......好像不是。"
    play music second_108 fadein 3.0 if_changed
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.3)
    pause 0.5 hard
    play voice "voice/藤原瞳/131000010.ogg"
    tyt "早午晚日安。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011000550.ogg"
    xz "......藤原同学？"
    play voice "voice/翔子/011000560.ogg"
    xz "那个......有什么事吗？"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131000020.ogg"
    tyt "对不起......"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011000570.ogg"
    xz "欸？"
    stop music fadeout 5.0
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/131000030.ogg"
    tyt "你没有听到吗？"
    show xz_dsf_b2 b2 b2_ga2
    play voice "voice/翔子/011000580.ogg"
    xz "是有听到你的道歉，但是不知道理由。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000040.ogg"
    tyt "不是指那个，你就没有听到什么其他的声音吗？"
    play sound canbai
    play music second_146 fadein 3.0 if_changed
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 1.0 hard
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011000590.ogg"
    xz "铃声？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131000050.ogg"
    tyt "没错......这是神乐铃。"
    hide xz_dsf_b3
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_a1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/藤原瞳/131000070.ogg"
    tyt "星天式镇恶神，射弓负箭之段。（注释：这是古代巫女通过神乐镇压恶神的仪式咒语）"
    play ambience1 canbai
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    "一边挥舞着神乐铃，藤原瞳一边开始了咏唱。"
    "用以送还不从之神的神乐仪式，对普通人则是具有催眠的功效。"
    stop ambience1 fadeout 5.0
    play sound rune2
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900)
    scene set only home evening passwalk xuejian
    show tyt_wnf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    with slowdissolve
    pause 1.0 hard
    play voice "voice/藤原瞳/131000080.ogg"
    tyt "这是能送还鬼神，镇压作祟的仪式。"
    play voice "voice/藤原瞳/131000090.ogg"
    tyt "本来不只是神乐铃，像弓箭等祭器也是能够进行的。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131000100.ogg"
    tyt "但只是让人睡着的话，用这个就足够了。"
    show xz_dsf_b3 b3 b3_s3 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/011000600.ogg"
    xz "......"
    hide xz_dsf_b3
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000110.ogg"
    tyt "我并没有打算加害于你。"
    play voice "voice/藤原瞳/131000120.ogg"
    tyt "只是要稍微借用一下你的东西。"
    show tyt_wnf_b1 b1 b1_n2 at flu_down(0.35, 20):
        xpos 0.3
    "看着倒地的翔子。"
    "藤原瞳的视线落在了翔子胸口的吊坠上。"
    "那是雷亚留下来的东西。"
    "曾经拯救了她的星辰之力——"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131000140.ogg"
    tyt "虽然我不懂科学，也不太了解{rb}灵纹{/rb}{rt}rune{/rt}之类的东西......"
    play voice "voice/藤原瞳/131000150.ogg"
    tyt "但是仅凭星天宫巫女的力量，是无法窥探到这其中蕴藏的灵力。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131000170.ogg"
    tyt "从神野前辈告诉我的话来判断，可能就需要借助{rb}思维透视{/rb}{rt}telepathy{/rt}或者{rb}共感{/rb}{rt}empathy{/rt}才能做到吧。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show alu_ct_b2 b2 b2_3 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131000180.ogg"
    tyt "阿露，屋里应该还有个叫爱衣的孩子，去把她找出来。"
    hide alu_ct_b2 with None
    show alu_ct_b2 b2 b2_2 onlayer m2 at fly(0.5):
        xpos 0.5
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎~（了解~）"
    hide tyt_wnf_b1
    play sound fly1
    show alu_ct_b2 b2 b2_2 onlayer m2 at fly_away(0.5):
        xpos 0.5
    pause 0.5 hard
    hide alu_ct_b2 with None
    scene black 
    with slowerdissolve
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening passwalk xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 2.0 hard
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 2.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show alu_ct_b12 b12 b12_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/阿露/551000580.ogg"
    alu "唔莎？（主人不见了？）"
    hide alu_ct_b12
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound appear
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/希菲尔/001001420.ogg"
    xfe "参上了哟~"
    play music second_106 fadein 3.0 if_changed
    $ flcam.move(2250, 0, 750, duration=1.5)
    show alu_ct_b10 b10 b10_2 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/阿露/551000060.ogg"
    alu "唔莎！？（白色恶魔！？）"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/希菲尔/001001430.ogg"
    xfe "是阿露耶~"
    hide alu_ct_b10
    hide ts_xfe_yjz_b3
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    play sound appear2
    show xfe sd2 onlayer texture_c2u:
        xpos 0.2
    with vpunch
    pause 0.5 hard
    play voice "voice/阿露/551000740.ogg"
    alu "唔莎！（别以为每次都能被你抓到！）"
    play voice "voice/希菲尔/001001440.ogg"
    xfe "等等~"
    "希菲尔像火箭一样扑了上去。"
    hide xfe sd2 with None
    show xfe sd1 onlayer texture:
        xpos 0.15 yalign 0.0
    play sound jump_1
    with vpunch 
    play voice "voice/希菲尔/001001450.ogg"
    xfe "{size=72}叭咕！{/size}"
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......（又被抓到了......）"
    play voice "voice/阿露/551000090.ogg"
    pause 0.8 hard
    hide xfe sd1 with None
    show xfe sd3 onlayer texture:
        xpos 0.15 yalign 0.0
    play sound rell_fire
    with vpunch
    alu "唔莎~波！（接招！）"
    hide xfe sd3 with None
    show xfe sd4 onlayer texture:
        xpos 0.15 yalign 0.0
    play sound ganga03
    play voice "voice/希菲尔/001001460.ogg"
    xfe "嚼啊嚼啊吞~"
    play sound jing02
    with vpunch
    play voice "voice/阿露/551000060.ogg"
    alu "唔莎？！（火焰被吃掉了？！）"
    hide xfe sd4 with None
    show xfe sd5 onlayer texture:
        xpos 0.2 yalign 0.0
    play sound ganga03
    with vpunch
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......（本小姐要溶化了......）"
    hide xfe sd5 with None
    show xfe sd6 onlayer texture:
        xpos 0.22 yalign 0.35
    play voice "voice/希菲尔/001001470.ogg"
    xfe "阿露！现在马上帮你修好！"
    hide xfe sd6 with None
    show xfe sd7 onlayer texture:
        xpos 0.22 yalign 0.0
    play sound jing03
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎！（复活了！）"
    hide xfe sd7 with None
    play sound appear2
    show xfe sd8 onlayer texture:
        xpos 0.22 yalign 0.35
    play voice "voice/阿露/551000740.ogg"
    alu "唔莎！（那就继续逃跑！）"
    hide xfe sd8 with None
    play sound jump_1
    show xfe sd1 onlayer texture:
        xpos 0.15 yalign 0.0
    with vpunch 
    play voice "voice/希菲尔/001001480.ogg"
    xfe "{size=72}叭咕！{/size}"
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......（竟然又被抓到了......）"
    pause 0.5 hard
    show xfe sd1:
        easeout 1.0 alpha 0.0 yalign 0.5
    pause 1.5 hard
    hide xfe sd1 with None
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111000600.ogg"
    aiyi "那、那个......你们是谁？"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1:
        xpos 0.5
    show alu_ct_b13 b13 b13_1 onlayer m2:
        xpos 0.48 ypos 0.638
    play voice "voice/希菲尔/001001490.ogg"
    xfe "#@%&"
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......（本小姐不会逃跑了，拜托你放开......）"
    pause 0.5 hard
    hide alu_ct_b13 with None
    show alu_ct_b2 b2 b2_1 onlayer m2 at fly_away(0.638):
        xpos 0.48
    pause 1.5 hard
    hide alu_ct_b13 with None
    play sound fly1
    show alu_ct_b2 b2 b2_1 onlayer m2:
        xpos 0.53 ypos 0.5 alpha 0.0
        parallel:
            linear 1.0 ypos 0.6
        parallel:
            linear 1.0 alpha 1.0
    pause 1.5 hard
    hide alu_ct_b2 with None
    show alu_ct_b1 b1 b1_5 onlayer m2:
        xpos 0.53 ypos 0.6
    pause 0.5 hard
    play voice "voice/阿露/551000040.ogg"
    alu "唔莎~（从今天开始你就是本小姐决定侍奉的主人~）"
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎~（请多多关照~）"
    show aiyi_dzf_b1 b1 b1_sp2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/爱衣/111000610.ogg"
    aiyi "啊......大姐姐？"
    stop music fadeout 5.0
    pause 0.5 hard
    play sound jiaobu4
    show aiyi_dzf_b1 b1 b1_sp2 at walkout_l(0.3)
    pause 1.5 hard
    hide aiyi_dzf_b1
    play music second_103 fadein 3.0
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide alu_ct_b1
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001001510.ogg"
    xfe "这两人就是和凉君一起生活的“家人”。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001001520.ogg"
    xfe "虽然希菲尔我不擅长和凉君以外的人说话。"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_h1
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001001530.ogg"
    xfe "没关系，只是睡着了而已。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001001540.ogg"
    xfe "而且凉君也来了，所以已经不用担心了。"
    play voice "voice/爱衣/111000620.ogg"
    aiyi "大哥哥他......是来帮助爱衣我们的吗？"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001001550.ogg"
    xfe "就是这样的哟~"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111000630.ogg"
    aiyi "是吗......"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001001560.ogg"
    xfe "你也喜欢凉君吗？"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/111000640.ogg"
    aiyi "嗯，最喜欢了~"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001001570.ogg"
    xfe "那太好了。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111000650.ogg"
    aiyi "那个......姐姐你是？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001001580.ogg"
    xfe "希菲尔我就叫希菲尔喔，凉君也是这么叫我的。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111000660.ogg"
    aiyi "那么希菲尔你也喜欢大哥哥吗？"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001001590.ogg"
    xfe "嗯，最喜欢了哟~"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.53
    play voice "voice/希菲尔/001001600.ogg"
    xfe "但是希菲尔我没办法成为凉君的家人。"
    show aiyi_dzf_b1 b1 b1_n1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/111000670.ogg"
    aiyi "一定可以的！"
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/001001610.ogg"
    xfe "......"
    $ flcam.move(-2250, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111000680.ogg"
    aiyi "只要结婚了的话，就能变成一家人了哟~"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001001620.ogg"
    xfe "结婚？"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111000690.ogg"
    aiyi "就是变得非常亲密的关系。"
    play voice "voice/爱衣/111000700.ogg"
    aiyi "而且呢，如果结婚的话，新的家人也会诞生的。"
    show ts_xfe_yjz_b2 b2 b2_h3
    play voice "voice/希菲尔/001001630.ogg"
    xfe "原来是这样啊......"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111000710.ogg"
    aiyi "希菲尔一定也是这样子诞生的。"
    show ts_xfe_yjz_b2 b2 b2_n4
    play voice "voice/希菲尔/001001640.ogg"
    xfe "嗯~"
    hide aiyi_dzf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001001650.ogg"
    xfe "希菲尔的诞生，是因为有千冬。"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/001001660.ogg"
    xfe "同时也多亏了“她”的缘故。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001001670.ogg"
    xfe "因为和千冬还有“她”都变得亲密的缘故，才能以现在这幅模样诞生的——"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day215.home_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    me01 "虽然之前就一直怀疑了。"
    me01 "你果然也是星天宫的巫女吗？"
    play music second_126 fadein 3.0 if_changed
    pause 1.0 hard
    scene set only home evening outside xuejian
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131000200.ogg"
    tyt "......"
    me01 "千方百计想要拖住我的幕后黑手就是你吧？"
    me01 "你这样做对得起琉璃吗？"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131000210.ogg"
    tyt "我并不是花山院的好伙伴。"
    me01 "所以说你到底是谁？"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000220.ogg"
    tyt "星天宫总本社的大神主......是我的祖父。"
    me01 "大神主......那很伟大吗？"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131000230.ogg"
    tyt "讲真的......很伟大~"
    me01 "那么，这位很伟大的大人物为什么要加害我们呢？"
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/131000240.ogg"
    tyt "因为利害不一致。"
    me01 "利害？什么意思？"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131000250.ogg"
    tyt "告诉你的话祖父会生气的，所以保密。"
    me01 "你果然也是{rb}灵继者{/rb}{rt}elfin{/rt}。"
    me01 "现在我能很明显地察觉到你身上的灵力。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131000260.ogg"
    tyt "这样啊......"
    play voice "voice/藤原瞳/131000270.ogg"
    tyt "应该是刚才神乐仪式的关系，所以每天例行的净身失去了效果。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show alu_ct_b2 b2 b2_2 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎。（找到你了，主人。）"
    me01 "为什么这只烦人的天鹅也会在这里？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000280.ogg"
    tyt "阿露，日向爱衣和吊坠呢？"
    hide alu_ct_b2 with None
    show alu_ct_b12 b12 b12_1 onlayer m2 at fly(0.5):
        xpos 0.5
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......（出了一些的意外......）"
    hide alu_ct_b12
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "奇怪的生物配上奇怪的巫女，你们这是什么组合啊？！"
    me01 "还有，不管你们找爱衣还有翔子的吊坠有何目的，我都不会让你得逞的。"
    play voice "voice/藤原瞳/131000290.ogg"
    tyt "也就是说你要妨碍我吗？"
    me01 "那是当然的。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show alu_ct_b2 b2 b2_3 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    show tyt_wnf_b1 b1 b1_a1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/藤原瞳/131000300.ogg"
    tyt "阿露，烧掉这男人那不灵光的脑袋。"
    hide alu_ct_b2 with None
    show alu_ct_b8 b8 b8_1 onlayer m2 at fly(0.5):
        xpos 0.5
    play voice "voice/阿露/551000020.ogg"
    alu "唔莎、唔莎。（才不要呢，自己工作自己做啊。）"
    stop music fadeout 5.0
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131000310.ogg"
    tyt "不照做的话今晚就没有胡萝卜吃了。"
    hide tyt_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    play music second_106 fadein 3.0 if_changed
    hide alu_ct_b8 with None
    show alu_ct_b10 b10 b10_1 onlayer m2 at fly(0.5):
        xpos 0.5
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎！（就交给本小姐吧！）"
    me01 "唔莎唔莎的吵死了，能打得过我的话就来试试看吧。"
    play sound rune3
    scene set only fight_cg thunder
    show alu_ct_b7 b7 b7_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    "气氛一度紧张了起来。"
    "人与雪兔之间的大战一触即发。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening outside xuejian
    $ flcam.move(-2250, 0, 750, duration=1.5)
    with dissolve
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s3 onlayer m2:
        xpos 0.3
    show alu_ct_b10 b10 b10_2 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/藤原瞳/131000320.ogg"
    tyt "好冷，好想睡......拿不到工钱的工作好想赶快结束掉。"
    me01 "就算成了反派，你的性格依旧那么随意啊......"
    hide alu_ct_b10
    hide tyt_wnf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound appear
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/希菲尔/001001680.ogg"
    xfe "参上了哟~"
    $ flcam.move(0, 0, 600, duration=1.5)
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    show alu_ct_b7 b7 b7_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.4 xzoom -1
    play voice "voice/阿露/551000060.ogg"
    alu "唔莎！（主人，刚刚的意外就是这个白色恶魔！）"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131000330.ogg"
    tyt "阿露，交给你了。"
    hide alu_ct_b7 with None
    show alu_ct_b6 b6 b6_1 onlayer m2 at fly(0.5):
        xpos 0.4 xzoom -1
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......（本小姐不是她的对手......）"
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/131000340.ogg"
    tyt "不加油的话晚上就没有胡萝卜大放送了。"
    hide tyt_wnf_b1
    hide ts_xfe_yjz_b2
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    hide alu_ct_b6 with None
    show alu_ct_b10 b10 b10_1 onlayer m2 at fly(0.5):
        xpos 0.4 xzoom -1
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎！（就交给本小姐吧！）"
    play sound fly2
    show alu_ct_b10 b10 b10_1 at fly_away(0.5):
        xpos 0.4 xzoom -1
    pause 1.0 hard
    hide alu_ct_b10
    "受到了食物的诱惑，阿露似乎又重新燃起了斗志。"
    "随即朝着希菲尔就是一个飞扑。"
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show xfe sd1 onlayer texture:
        xpos 0.15 ypos 0.0
    with vpunch 
    play voice "voice/希菲尔/001001690.ogg"
    xfe "{size=72}叭咕！{/size}"
    pause 0.5 hard
    hide xfe sd1 with dissolve
    pause 1.0 hard
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play sound fly1
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
    "被制服后的阿露恭敬地停在希菲尔的肩膀上。"
    "熟悉的画面......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎~（今天开始你就是我的主人了~）"
    "虽然不知道在说什么，不过看样子似乎是叛变了。"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001001700.ogg"
    xfe "阿露也来一起帮助凉君吧~"
    stop music fadeout 5.0
    hide tyt_wnf_b1
    hide alu_ct_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "能来帮忙真是太好了希菲尔。"
    me01 "不过这里太危险了，带着阿露先躲到安全的地方去吧。"
    me01 "这里交给我就行了。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001001710.ogg"
    xfe "凉君果然......很温柔。"
    play voice "voice/希菲尔/001001720.ogg"
    xfe "这样做的话，对凉君而言比较好吗？"
    me01 "是的，拜托了。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001001730.ogg"
    xfe "那样的话希菲尔就照做了哟~"
    $ flcam.move(4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001001740.ogg"
    xfe "即使这样希菲尔也会，一直守护着凉君你的~"
    pause 0.5 hard
    show wflash onlayer texture
    play sound xiaoshi_1
    show ts_xfe_yjz_b1 b1 b1_h2:
        xpos 0.7 alpha 1.0
        linear 1.0 alpha 0.0
    pause 2.0 hard
    hide ts_xfe_yjz_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131000350.ogg"
    tyt "和阿露一起......消失了？"
    me01 "碍事的雪兔已经不在了，这样的话就是一对一了。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000360.ogg"
    tyt "......"
    me01 "打败你之后还有一大堆的问题，做好觉悟吧。"
    play music second_124 fadein 3.0 if_changed
    show xz_dsf_b3 b3 b3_s3 onlayer screens at side_right('xz'), basicfade
    play voice "voice/翔子/011000610.ogg"
    xz "我也有问题想问......"
    hide xz_dsf_b3
    hide tyt_wnf_b1
    $ flcam.move(5200, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_s1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/翔子/011000620.ogg"
    xz "真是的......到底发生了什么？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_s4 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111000720.ogg"
    aiyi "大姐姐，你没事吧？"
    $ flcam.move(0, 0, 600, duration=1.5)
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131000370.ogg"
    tyt "这么快就摆脱了催眠，看来青木同学也不是一般人。"
    hide tyt_wnf_b1
    hide aiyi_dzf_b1
    $ flcam.move(5200, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_s3
    play voice "voice/翔子/011000630.ogg"
    xz "神野君......发生什么事了？"
    me01 "比起这个，先回房间里去吧。"
    me01 "这里很危险的。"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011000640.ogg"
    xz "在那之前先告诉我发生了什么。"
    me01 "等一切都结束了我会告诉你的。"
    me01 "现在连我自己也没有完全弄明白。"
    me01 "所以听话，先回屋里等我。"
    $ flcam.move(2500, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "爱衣，翔子就拜托你了。"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111000730.ogg"
    aiyi "嗯......大姐姐我们进去吧？"
    stop music fadeout 5.0
    hide xz_dsf_b2
    hide aiyi_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_a1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131000380.ogg"
    tyt "不会让你们得逞的！"
    play music second_146 fadein 3.0 if_changed
    play sound canbai
    show tyt_wnf_b1 b1 b1_a1 at flu_down(0.15, 20):
        xpos 0.3
    pause 1.0 hard
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000390.ogg"
    tyt "吊坠和爱衣，哪一个都不能放过。"
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/131000400.ogg"
    tyt "现在就让你见识一下，我不是一个毫无存在感的角色。"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    stop music fadeout 5.0
    stop sound fadeout 2.0
    hide snow_level1
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg home_xuejian
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        ## 敌方初始化参数
        # Boss为藤原瞳，巫女个数5，所有敌方角色技能等级12，装备“稀有”随机等级10装备6件
        enemy_roles = [tyt_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4]
        for role in enemy_roles:
            role.equip_experience = 99999999
            for cate in role.outfits:
                enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                sample_outfit = enemy_outfits[sample_index]
                sample_outfit.init_params()
                for xi in range(9):
                    sample_outfit.level_up(role, 100)
                sample_outfit.enemy_equip_on(role)
            for xi in range(12):
                role.skill_levelup()

        # 巫女技能替换
        for role, element in zip([migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4], ["fire", "light", "water", "ice", "wind"]):
            now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_%sm" % element))
            role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]

        team_average_level = 0
        if len(local_config.masters) > 0:
            for role_name in local_config.masters:
                role_obj = [r for r in local_config.party if r.objectname == role_name][0]
                team_average_level += role_obj.level
            team_average_level /= len(local_config.masters)
        else:
            for role in local_config.party:
                if role.level > team_average_level:
                    team_average_level = role.level
        team_average_level = int(team_average_level)

        # 爱衣、翔子加入我方，等级等于雷亚角色等级，角色技能等级满级，装备“史诗”随机等级10装备6件；除雷亚外其余角色暂离队
        temp_log_party = copy(local_config.party)
        ally_roles = [aiyi_role_mirror, xz_role_mirror]
        for role in ally_roles:
            role.equip_experience = 99999999
            role.stats_check(to_level=team_average_level, limit=True)
            for cate in role.outfits:
                enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                sample_outfit = enemy_outfits[sample_index]
                sample_outfit.init_params()
                for xi in range(9):
                    sample_outfit.level_up(role, 100)
                sample_outfit.enemy_equip_on(role)
            for xi in range(20):
                role.skill_levelup()

        for role in copy(local_config.party):
            if len(local_config.masters) > 0:
                for role_name in local_config.masters:
                    if role.objectname != role_name:
                        local_config.party.remove(role)
                        break
            else:
                local_config.party = local_config.party[:4]
        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

        local_config.party.insert(1, aiyi_role_mirror)
        local_config.party.insert(2, xz_role_mirror)

        local_config.tutorial_step = "enemy_protect_tyt_role_mirror"

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=tyt_role_mirror, 
                boss_hp_plus=10000,
                side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4], 
                side_hp_plus=5000,
                level=30,
                boss_first=True, 
                win_condition='normal',
                stay_turn=0,
                inside_label="inside_battle9", 
                mission_type="normal", 
                treasures={
                    "eggs": (3, 0.6),
                    "mana_eggs": (1, 0.3),
                    "soul_piece": (5, 0.3),
                    "soul_raise": (5, 0.3),
                    "fire_break_small": (5, 0.3),
                    "fire_break_large": (3, 0.3),
                    "water_break_small": (5, 0.3),
                    "water_break_large": (3, 0.3),
                    "ice_break_small": (5, 0.3),
                    "ice_break_large": (3, 0.3),
                    "light_break_small": (5, 0.3),
                    "light_break_large": (3, 0.3),
                    "wind_break_small": (5, 0.3),
                    "wind_break_large": (3, 0.3),
                    "rock_break_small": (5, 0.3),
                    "rock_break_large": (3, 0.3),
                })

    if _return == "win":
        "战斗胜利！"
        "「希菲尔」加入队伍！"
        python:
            # 希菲尔加入队伍 & masters
            local_config.masters += ["xfe_role"]
            xfe_role.stats_check(to_level=team_average_level, limit=True)
            xfe_role.equip_experience = 99999999
            for cate in xfe_role.outfits:
                enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                sample_outfit = enemy_outfits[sample_index]
                sample_outfit.init_params()
                for xi in range(7):
                    experience = (2000 + 500 * sample_outfit.rarity) + sample_outfit.level * (1000 + 250 * sample_outfit.rarity)
                    sample_outfit.level_up(xfe_role, experience)
                sample_outfit.enemy_equip_on(xfe_role)
            xfe_role.equip_experience = 0

            # 希菲尔被动技能默认满级
            select_up_skill = [s for s in xfe_role.skills if s.category == "Passive"][0]
            select_up_skill.level_change(5)
            xfe_role.base_skills = copy(xfe_role.skills)
            select_up_skill_v2 = [s for s in xfe_role.skills_v2 if s.category == "Passive"][0]
            select_up_skill_v2.level_change(5)
            xfe_role.base_skills_v2 = copy(xfe_role.skills_v2)

            local_config.party.insert(1, xfe_role)

            # 爱衣、翔子离队
            for role in copy(local_config.party):
                if role.objectname in ["aiyi_role_mirror", "xz_role_mirror"]:
                    role.full_reset(heal_hp=True, ally_environment_effects=None, turn_end=True, level_reset=True)
                    local_config.party.remove(role)

            now_party_objnames = [role.objectname for role in local_config.party]
            for role in temp_log_party:
                if role.objectname not in now_party_objnames:
                    if len(local_config.party) >= 6:
                        local_config.backup.append(role)
                    else:
                        local_config.party.append(role)

            for rolename in ["xfe_role", "aiyi_role", "xz_role"]:
                if rolename not in local_config.role_pool:
                    local_config.role_pool.add(rolename)

        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day215.after_battle_tyt

label day215.after_battle_tyt:
    scene black
    with slowdissolve
    pause 1.0 hard
    play music second_146 fadein 3.0 if_changed
    $ flcam.move(-4500, 0, 1000)
    scene set only home evening outside xuejian
    show snow_level1 onlayer fg
    play sound canbai
    show tyt_wnf_b1 b1 b1_a1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.3
    with dissolve
    pause 1.0 hard
    play voice "voice/藤原瞳/131000410.ogg"
    tyt "星天式拔除清、净杓大麻之段！"
    play ambience1 canbai
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 2.0 hard
    "神乐铃再次响起，藤原瞳双手合十开始咏唱。"
    "在这铃声的影响下，我的手脚开始不听使唤了。"
    "不仅如此，意识也逐渐变得模糊起来。"
    stop ambience1 fadeout 5.0
    play sound rune2
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900)
    scene set only home evening outside xuejian
    show snow_level1 onlayer fg
    show tyt_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    with dissolve
    pause 1.0 hard
    me01 "你都做了什么？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000420.ogg"
    tyt "这是巫女神乐。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131000430.ogg"
    tyt "清净身心，改过己身。"
    play voice "voice/藤原瞳/131000440.ogg"
    tyt "夺回青木同学的吊坠以及带走日向爱衣，这就是我的任务。"
    me01 "......为什么？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000450.ogg"
    tyt "在那孩子以及吊坠上附着的灵能力都被解放了。"
    play voice "voice/藤原瞳/131000460.ogg"
    tyt "你们把那股力量叫做{rb}灵纹{/rb}{rt}rune{/rt}。"
    hide tyt_wnf_b1
    $ flcam.move(2250, 0, 750, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    show xz_dsf_b3 b3 b3_s3 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/011000650.ogg"
    xz "......"
    show xz_dsf_b3 b3 b3_c1
    play voice "voice/翔子/011000660.ogg"
    xz "唔、唔......"
    show aiyi_dzf_b1 b1 b1_sp2
    play voice "voice/爱衣/111000740.ogg"
    aiyi "大姐姐？"
    hide aiyi_dzf_b1
    $ flcam.move(5200, -300, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/011000670.ogg"
    xz "......不要！"
    pause 1.0 hard
    hide snow_level1
    play sound rune2
    scene white 
    with in2out_02_l
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening outside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131000470.ogg"
    tyt "这是？！"
    play voice "voice/藤原瞳/131000480.ogg"
    tyt "不是那位大人的力量。"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_a2
    play voice "voice/藤原瞳/131000510.ogg"
    tyt "这种力量，之前从来没有见过！"
    play voice "voice/藤原瞳/131000520.ogg"
    tyt "从来不知道还有这样的光芒——"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    play sound rune2
    scene white
    with in2out_v2_slow
    pause 2.0 hard

label day215.memory_event01:
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "这声音，是雪。"
    "雪花飘落的声音——"
    play music second_147 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0) 
    scene set only memory_cg yuki ground
    show snow_level1 onlayer fg
    $ flcam.move(0, -500, 1100, duration=40.0, warper='ease_cubic')
    with slowdissolve
    pause 1.0 hard
    "天地皆白。"
    "回过神来的我独自站在无边无际的雪原上。"
    "看不见尽头的纯白里，孤独和不安渐渐吞噬着我。"
    "讨厌迷路。"
    "不想要一个人。"
    "忍不住想要去寻找。"
    "能够和我一起前进的人。"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg end one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/诗乃/701000010.ogg"
    stranger "遥远的过去。"
    play voice "voice/诗乃/701000020.ogg"
    stranger "在流星划过天际之时，冬季悄然降临。"
    play voice "voice/诗乃/701000030.ogg"
    stranger "那是孤独且漫长的冬季。"
    play voice "voice/诗乃/701000040.ogg"
    stranger "漫无尽头的冬季。"
    play voice "voice/诗乃/701000050.ogg"
    stranger "让许多生命都陨落的寒冬。"
    play voice "voice/诗乃/701000060.ogg"
    stranger "因为迎来春天之时我的生命也将陨落。"
    play voice "voice/诗乃/701000070.ogg"
    stranger "所以希望托付给你。"
    play voice "voice/诗乃/701000080.ogg"
    stranger "至少，想留下存在的证据。"
    play voice "voice/诗乃/701000090.ogg"
    stranger "想和某个人一起延续足迹。"
    play voice "voice/诗乃/701000100.ogg"
    stranger "我认为这并非偶然。"
    play voice "voice/诗乃/701000110.ogg"
    stranger "就如同那孩子向往的一样。"
    play voice "voice/诗乃/701000120.ogg"
    stranger "托你的福，我才能真正明白。"
    play voice "voice/诗乃/701000130.ogg"
    stranger "正因为有相遇，才能唤来春天。"
    play voice "voice/诗乃/701000140.ogg"
    stranger "天狗追逐着月亮，是因为天狗心怀寂寞。"
    play voice "voice/诗乃/701000150.ogg"
    stranger "月亮接受了天狗，是因为月亮同样忍受着孤独。"
    play voice "voice/诗乃/701000160.ogg"
    stranger "对......"
    pause 0.1 hard
    scene set only xfe_cg memory7
    with slowdissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000170.ogg"
    stranger "星星之所以会像这样布满夜空，是因为月亮和天狗都不再孤身一人——"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening outside xuejian
    show snow_level1 onlayer fg
    with dissolve
    "回到现实中的我，脸颊上已是布满了泪水。"
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111000750.ogg"
    aiyi "大、大哥哥......大姐姐她！"
    hide aiyi_dzf_b1
    $ flcam.move(3200, -200, 600, duration=1.5)
    pause 0.5 hard
    me01 "不要紧，只是睡着了。"
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_c1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111000760.ogg"
    aiyi "是吗......太好了~"
    play sound touch
    "我抱起失去意识的翔子。"
    me01 "我们进屋吧。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/111000770.ogg"
    aiyi "大哥哥......谢谢你一直守护着我们。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with dissolve
    pause 1.0 hard
    "可以肯定的一点，刚刚的画面是某人留下的记忆。"
    "而我借助吊坠里残存的灵力触碰到了这份{rb}共感{/rb}{rt}empathy{/rt}。"
    "看到了某人的内心。"
    "在那虚华若梦的白色世界里，究竟是谁编织出来的梦境呢？"
    "而又是为什么，那些雪花会如此地寂寞呢......"
    pause 1.0 hard
    scene set only home evening outside xuejian
    with dissolve
    pause 1.0 hard
    me01 "还打算继续战斗吗？"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/藤原瞳/131000530.ogg"
    tyt "阿露跟着那孩子一起走了对吧？"
    me01 "毕竟希菲尔才是阿露现在的主人。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131000540.ogg"
    tyt "是吗......连新的羁绊都有了吗。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131000550.ogg"
    tyt "神明大人原本就是候鸟。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131000560.ogg"
    tyt "能有一个新的归属，我想应该要祝福她。毕竟这也是阿露成长的表现。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131000570.ogg"
    tyt "这次的事我很抱歉，在这里给你谢罪。"
    me01 "也就是说你已经放弃了？"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131000580.ogg"
    tyt "是的，虽然在被前辈责备的时候我就已经决定放弃了。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131000590.ogg"
    tyt "况且本来就没什么心情继续的。"
    pause 0.5 hard
    play sound jiaobu2
    show tyt_wnf_b1 b1 b1_s2 at walkout_l(0.5)
    pause 1.5 hard
    hide tyt_wnf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    me01 "等等......我还有事想问你。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131000600.ogg"
    tyt "我把我现在立场上能说的都说完了。"
    me01 "不是你想的那样。"
    me01 "任务失败的你会受到星天宫的惩罚吗？"
    show tyt_wnf_b1 b1 b1_sp1
    "听了我的话，藤原瞳愣了一下。"
    "但是很快又恢复了平静。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131000610.ogg"
    tyt "为了斩断束缚，我不得不去面对。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131000620.ogg"
    tyt "我希望你能明白，把我变成现在这样的并不是前辈你，而是花山院。"
    me01 "感觉偶尔和你说说话也不错呢。"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/藤原瞳/131000630.ogg"
    tyt "我讨厌色色的事。"
    me01 "谁也没在说那种事好吗？！"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131000640.ogg"
    tyt "我们若是以另一种方式见面的话，或许真的能成为朋友吧。"
    me01 "虽然不想承认，但是现在的你也是我的朋友不是吗？"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/131000650.ogg"
    tyt "......"
    me01 "朋友的朋友也是朋友。"
    me01 "我们两个都是琉璃的朋友。"
    me01 "所以......"
    $ flcam.move(-4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131000660.ogg"
    tyt "是啊，说不定真是这样的~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    
    $ persistent.lingyin = True
    $ persistent.szl_ling = True
    $ persistent.youjia = True
    $ persistent.lihuaxi = True
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    
    jump second_menu
