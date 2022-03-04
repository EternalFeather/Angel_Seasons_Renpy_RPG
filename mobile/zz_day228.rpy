
label battle_lhx_memory_day228:
    $ flcam.move(0, 0, 0)
    scene set only fight_cg rune1
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    python:
        # 战斗boss为立花希，其他角色为镜像角色（除了希菲尔），所有敌方等级、装备均与队伍中保持相同
        side_enemy_roles = []
        for ori_role in local_config.party:
            if ori_role.name != "希菲尔":
                role = getattr(store, ori_role.objectname + "_mirror")
                # 装备继承
                for cate, outfit in ori_role.outfits.items():
                    if outfit is not None:
                        outfit.enemy_equip_on(role)
                # 技能等级继承
                for skill in ori_role.skills:
                    new_skill = [s for s in role.skills if s.category == skill.category][0]
                    new_skill.level_change(skill.level)
                if len(ori_role.skills_v2) > 0:
                    for skill_v2 in ori_role.skills_v2:
                        new_skill = [s for s in role.skills_v2 if s.category == skill_v2.category][0]
                        new_skill.level_change(skill_v2.level)
                # 等级继承
                role.stats_check(ori_role.level)
                side_enemy_roles.append(role)
            else:
                role = lhx_role_mirror
                # 装备继承
                for cate, outfit in ori_role.outfits.items():
                    if outfit is not None:
                        outfit.enemy_equip_on(role)
                # 技能等级继承
                for skill in ori_role.skills:
                    new_skill = [s for s in role.skills if s.category == skill.category][0]
                    new_skill.level_change(skill.level)
                # 等级继承
                role.stats_check(ori_role.level)

        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)
    
    pause 0.25
    call battle(boss=lhx_role_mirror,
                boss_hp_plus=60000,
                side_enemy=side_enemy_roles, 
                side_hp_plus=20000,
                level=-1,
                boss_first=False, 
                win_condition='normal', 
                stay_turn=0,
                inside_label=None, 
                mission_type="normal", 
                treasures={
                    "eggs": (5, 0.6),
                    "mana_eggs": (2, 0.3),
                    "soul_piece": (15, 0.3),
                    "soul_raise": (15, 0.3),
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
        "梦境试炼突破。"
        "立花希重新加入队伍。"
        python:
            seen_day224_lhx_memory = True
            for role in local_config.release:
                if role.name == "立花希":
                    role.mp = role.max_mp
                    role.hp = role.max_hp + role.extend_max_hp
                    local_config.backup.append(role)
                    local_config.release.remove(role)
            local_config.role_pool.add("lhx_role")

        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom

label day228:
    bookmark
    $ save_name = _("Day 228")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date227 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    with slowdissolve
    pause 1.0 hard
    "随着春天的降临，学校那边也迎来了新的学年。"
    pause 1.0 hard
    scene set only school day restaurant xuejian nobody
    play music second_116 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "开学典礼结束之后，大家一起来到了食堂。"
    "和往常不同的是，这个时间段的食堂几乎没有人流。"
    "于是我也很自然地让希菲尔和雷亚现身了。"
    "趁这个机会让她们也体验一下校园生活。"
    "毕竟这可是花了好大的功夫才成功说服雷亚同行。"
    "果然这位别扭鬼死神还是老样子。"
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b3 b3 b3_s2 onlayer m2:
        xpos 0.3
    me01 "来这里的路上人有点多，抱歉了。"
    play voice "voice/天使雷亚/0005670.ogg"
    lst "也不是因为这个才觉得讨厌的。"
    me01 "那为什么生气了？"
    hide ts_lst_ssz_b3
    show ts_lst_ssz_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/天使雷亚/0005680.ogg"
    lst "就算你说我在生气......"
    me01 "你从刚才开始不是在闹别扭吗？"
    show ts_lst_ssz_b2 b2 b2_a1
    play voice "voice/天使雷亚/0005700.ogg"
    lst "你说谁在闹别扭啊？"
    me01 "昨晚不也一直说“死神才不会上学呢”之类的话吗？"
    show ts_lst_ssz_b2 b2 b2_ga1
    play voice "voice/天使雷亚/0005710.ogg"
    lst "你在胡说些什么完全听不懂......"
    hide ts_lst_ssz_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    me01 "相反希菲尔倒是答应得很爽快呢。"
    play voice "voice/希菲尔/001007850.ogg"
    xfe "是这样吗？"
    me01 "是啊。"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001007860.ogg"
    xfe "虽然凉君教会了希菲尔很多东西，不过还是有很多不明白的地方。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/011001380.ogg"
    xz "最不明白的东西是什么？"
    show ts_xfe_yjz_b2 b2 b2_s2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001007870.ogg"
    xfe "那个，果然还是最厉害的......"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_ga1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/011001390.ogg"
    xz "最厉害的东西......"
    me01 "啊啊啊，都是些不值一提的事情！"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001007880.ogg"
    xfe "才不是不值一提的呢，那是让人心跳加速、快要融化掉的重要东西。"
    play voice "voice/翔子/011001400.ogg"
    xz "不会是犯罪的事吧......"
    me01 "当然不是！"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001007890.ogg"
    xfe "是这样吗？"
    me01 "千真万确。"
    show ts_xfe_yjz_b3 b3 b3_h1 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001007900.ogg"
    xfe "太好了呢~"
    hide ts_xfe_yjz_b3
    hide xz_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/一诚总司/181000240.ogg"
    yczs "......这些孩子突然就冒出来了，不管怎么说还真是让人觉得不可思议啊。"
    $ flcam.move(0, -200, 600, duration=1.5)
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    show xz_dzf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.7
    play voice "voice/翔子/011001410.ogg"
    xz "我倒是已经习惯了呢~"
    show ts_xfe_yjz_b2 b2 b2_s2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001007910.ogg"
    xfe "被找到了......"
    pause 1.0 hard
    show wflash
    play sound xiaoshi_1
    show ts_xfe_yjz_b2 b2 b2_s2:
        xpos 0.5 alpha 1.0
        linear 0.75 alpha 0.0
    pause 2.5 hard
    hide ts_xfe_yjz_b2
    hide xz_dzf_b2
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/121003890.ogg"
    rxl "希菲尔消失了，都怪一诚君你欺负她。"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/181000250.ogg"
    yczs "为什么是我的错啊。"
    show rxl_dzf_b1 b1 b1_ga1
    play voice "voice/日向怜/121003900.ogg"
    rxl "就算再怎么不擅长面对小孩子也不至于这样嘛。"
    show yczs_dzf_b1 b1 b1_n1
    play voice "voice/一诚总司/181000260.ogg"
    yczs "多亏了小桃，我现在已经不是你说的那样了。"
    hide yczs_dzf_b1
    hide rxl_dzf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    me01 "雷亚你不躲起来吗？"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/0005720.ogg"
    lst "也没什么让我觉得讨厌的。"
    with vpunch
    me01 "和刚刚的态度差太多了吧！？"
    show ts_lst_ssz_b2 b2 b2_ga1
    play voice "voice/天使雷亚/0005730.ogg"
    lst "完全不明白你在生什么气。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day228'
    $ seen_day228_school_event01 = False
    $ seen_day228_balltower_event01 = False
    $ seen_day228_myroom_event01 = False

label day228.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day228':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day228.school_event01':
        show set maps winter evening
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day228.balltower_event01':
        show set maps winter night
        $ flcam.move(*overworld.camera_positions['road1'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        school=("day228.school_event01", "not seen_day228_school_event01"),
        cloqks=("day228.balltower_event01", "seen_day228_school_event01 and not seen_day228_balltower_event01"),
        road1=("day228.myroom_event01", "seen_day228_balltower_event01 and not seen_day228_myroom_event01"))
    $ window_animate_outro()
    if _return == 'day228.school_event01':
        with Pause(1.0)
        scene black with dissolve
    elif _return == 'day228.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day228.myroom_event01':
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

label day228.school_event01:
    play sound rill
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 2.0 hard
    scene set only school snow day center room xuejian
    with dissolve
    pause 1.0 hard
    show tyt_wnf_b1 b1 b1_s1 onlayer screens at side_left('tyt'), basicfade
    play voice "voice/藤原瞳/131001360.ogg"
    tyt "呼——"
    hide tyt_wnf_b1
    play music second_108 fadein 3.0 if_changed
    me01 "醒醒啊喂！"
    play sound hite_light
    show wflash onlayer texture
    with vpunch
    pause 0.5 hard
    play sound jump_1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5 ypos 1.13 alpha 0.0
        parallel:
            linear 0.25 ypos 0.98
        parallel:
            linear 0.25 alpha 1.0
    pause 1.0 hard
    play voice "voice/藤原瞳/131001370.ogg"
    tyt "这样一来前辈就永远无法把我攻略了。"
    me01 "正合我意。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131001380.ogg"
    tyt "明明脱了很壮观的。"
    me01 "别用那种遗憾的语气说这话啊。"
    stop music fadeout 5.0
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131001390.ogg"
    tyt "虽然很遗憾，但可能要有一段时间见不到前辈了。"
    me01 "你也要......离开这座城市了吗？"
    play music second_111 fadein 3.0 if_changed
    play voice "voice/藤原瞳/131001400.ogg"
    tyt "不是的，毕竟已经决定了下次再见面的时候就是琉璃从宇宙中心回来的那一刻。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131001420.ogg"
    tyt "更何况我本来也有守护雪见市的使命在身。"
    me01 "有那么忙吗你？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131001430.ogg"
    tyt "如果连我自己都疏于使命的话，会让同样努力着的花山院失望的。"
    me01 "你这个人果然偶尔还是会说些不错的话嘛。"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.25, 20, 2):
        xpos 0.5
    play voice "voice/藤原瞳/131001440.ogg"
    tyt "噗噗噗咕噗~"
    me01 "收回前言！"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131001450.ogg"
    tyt "前辈有空的时候也请去宇宙中心看看，与我不同前辈是应该去的。"
    play voice "voice/藤原瞳/131001460.ogg"
    tyt "能够带去勇气和希望的就只有你了。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131001470.ogg"
    tyt "想到前辈能够代替我为花山院加油的话，我也能放心地去完成我自己的使命了。"
    me01 "我想即使不是我而是别人去看望的话，琉璃也会很开心的。"
    show tyt_wnf_b1 b1 b1_a1
    play voice "voice/藤原瞳/131001480.ogg"
    tyt "还没明白吗，我是让你作为{rb}灵继者{/rb}{rt}elfin{/rt}的代表去助花山院一臂之力的。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131001490.ogg"
    tyt "花山院她正在为了我们{rb}灵继者{/rb}{rt}elfin{/rt}的未来不惜赌上性命踏上前往宇宙的道路。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131001500.ogg"
    tyt "接下来的事情还需要我多说吗？"
    me01 "已经足够了。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131001510.ogg"
    tyt "如果你肯去声援花山院的话，我就开放我的路线给你吧。会在攻略完花山院的时候产生选项的。"
    me01 "到最后还是搞不懂你这个角色的定位啊！！！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day228_school_event01:
        $ seen_day228_school_event01 = True
    $ _overworld_label = 'day228.school_event01'
    jump day228.map

label day228.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene white
    play music second_117 fadein 3.0 if_changed
    with slowerdissolve
    pause 1.0 hard
    scene set only xfe_cg memory4
    with slowdissolve
    pause 1.0 hard
    play voice "voice/诗乃/701000320.ogg"
    stranger "所以我希望至少要将希望托付出去。"
    play voice "voice/诗乃/701000330.ogg"
    stranger "留下我曾作为生命活着的证据。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    scene set only balltower snow evening xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008410.ogg"
    xfe "啊，是凉君呀~"
    play music second_103 fadein 3.0 if_changed
    play sound jiaobu3
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.25, 20):
        xpos 0.5
    "希菲尔看见我的第一眼就朝我的方向跑了过来。"
    play sound jump_1
    show ts_xfe_yjz_b2 b2 b2_sp2:
        xpos 0.5 ypos 1.0 alpha 1.0
        parallel:
            linear 0.25 ypos 1.05
        parallel:
            linear 0.25 alpha 0.0
    with vpunch
    pause 0.5 hard
    "{size=72}噗嗤。{/size}"
    "但却在途中摔倒了。"
    $ flcam.move(0, 800, 1100, duration=1.5)
    pause 0.5 hard
    me01 "没事吧？"
    play sound touch
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp2:
        xpos 0.5 ypos 1.05 alpha 0.0
        parallel:
            linear 0.25 ypos 1.0
        parallel:
            linear 0.25 alpha 1.0
    pause 0.5 hard
    play voice "voice/希菲尔/001008420.ogg"
    xfe "完全没事，下面是雪所以一点也不痛。"
    me01 "还是第一次看到希菲尔你在雪地上摔倒。"
    show ts_xfe_yjz_b2 b2 b2_a1
    play voice "voice/希菲尔/001008430.ogg"
    xfe "可不要小看希菲尔喔，不管是不是在雪地上都是有可能会跌倒的。"
    me01 "......某种意义上来说更担心了。"
    "我用手拂去希菲尔鼻子上的雪。"
    show ts_xfe_yjz_b2 b2 b2_ga3 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001008440.ogg"
    xfe "好痒的说~"
    me01 "希菲尔你是不是发烧了？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008450.ogg"
    xfe "发烧？"
    me01 "是啊，总觉的你的体温有点高。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008460.ogg"
    xfe "没有这回事哟。"
    show ts_xfe_yjz_b2 b2 b2_h3
    play voice "voice/希菲尔/001008470.ogg"
    xfe "凉君，比起这个......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008480.ogg"
    xfe "再来一次吧。"
    me01 "再来一次？"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001008490.ogg"
    xfe "是啊，就是凉君说“找到你了”，然后希菲尔我说“被找到了”之类的对话。"
    me01 "那......找到你了，希菲尔。"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001008500.ogg"
    xfe "嗯，被找到了~"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play sound touch
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg touch1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001008510.ogg"
    xfe "被......抱起来了。"
    me01 "讨厌这样吗？"
    pause 0.1 hard
    scene set only xfe_cg touch2
    with dissolve
    play voice "voice/希菲尔/001008520.ogg"
    xfe "和梦里不一样，现在不行的......心砰砰跳感觉自己快要融化掉了。"
    me01 "果然还是发烧了吧？"
    play voice "voice/希菲尔/001008530.ogg"
    xfe "希菲尔我不会得感冒之类的病，所以不要紧的。"
    me01 "真的吗？"
    play voice "voice/希菲尔/001008540.ogg"
    xfe "嗯，希望凉君能相信希菲尔。"
    pause 0.1 hard
    scene set only xfe_cg touch3
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001008550.ogg"
    xfe "只是现在这种心跳的感觉还是会觉得很害怕。"
    play sound touch
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow evening xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008030.ogg"
    xfe "{rb}灵纹{/rb}{rt}rune{/rt}这种东西呢，是心灵相通、建立起羁绊的双方才能拥有的。"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/001008040.ogg"
    xfe "这不仅仅是得和{rb}灵继者{/rb}{rt}elfin{/rt}之间的关系变得要好而已。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001008050.ogg"
    xfe "还得和{rb}灵纹{/rb}{rt}rune{/rt}本身变得亲密起来才行。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001008060.ogg"
    xfe "但是想要和{rb}灵纹{/rb}{rt}rune{/rt}变得要好的话，不是迷路的孩子就很难办到。"
    play voice "voice/希菲尔/001008070.ogg"
    xfe "因为{rb}灵纹{/rb}{rt}rune{/rt}本身也是一直不知该去往何处的、迷路的孩子。"
    me01 "刚才的这些也是千冬姐告诉你的吗？"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001008080.ogg"
    xfe "在梦里看到的。"
    me01 "是那个可怕的梦？"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001008090.ogg"
    xfe "就是这样的。"
    me01 "那个梦里的场景......会发生吗？"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001008100.ogg"
    xfe "希菲尔我也不知道。"
    me01 "在你的梦中......我在你的身边吗？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008110.ogg"
    xfe "嗯，希菲尔即使是在梦里也一直和凉君在一起的哟。"
    me01 "即使这样......也还是会害怕吗？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008130.ogg"
    xfe "希菲尔我果然，也不是很明白。"
    me01 "希菲尔你很讨厌夏天对吧？"
    show ts_xfe_yjz_b2 b2 b2_s2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001008150.ogg"
    xfe "是啊，夏天可是杀戮兵器啊。"
    me01 "那如果雪见市真的迎来了夏天......希菲尔会怎么样呢？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001008190.ogg"
    xfe "希菲尔我......是只能在冬天存在的。"
    show ts_xfe_yjz_b2 b2 b2_s3
    play voice "voice/希菲尔/001008200.ogg"
    xfe "以前的希菲尔，甚至都没有办法离开千冬的身边。"
    play voice "voice/希菲尔/001008210.ogg"
    xfe "如果千冬不在的话，就什么都做不到。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008220.ogg"
    xfe "正因为希菲尔什么都不懂，到现在才真正明白了。"
    play voice "voice/希菲尔/001008230.ogg"
    xfe "拯救大家的方法......"
    me01 "那个可怕的梦，就是“芬布尔之冬”吗？"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001008240.ogg"
    xfe "嗯，就是这样的。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day228_balltower_event01:
        $ seen_day228_balltower_event01 = True
    $ _overworld_label = 'day228.balltower_event01'
    jump day228.map

label day228.myroom_event01:
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
            screen_direction left
            sleep jump day228.sleep

label day228.sleep:
    menu:
        "早点休息":
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
    jump day228.ritroom

label day228.ritroom:
    default seen_day228_ritroom = False
    play music ritroom_day fadein 3.0 if_changed
    play ambience1 ritroom_fireplace fadein 3.0 if_changed

    if not seen_day228_ritroom:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        scene set ritfrontyard winter night:
            mid winter night
            frontl winter night
            frontr winter night
        $ flcam.move(0, 0, 400)
        $ flcam.move(0, 0, 0, duration=1.5)
        with dissolve
        pause 3.0 hard

        scene set ritroom night:
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
        show ritona b3 fb5 fa1 fc02 onlayer m2:
            xpos 0.5
        me01 "弗兰小姐？"
        ritona "......"
        me01 "那个......弗兰小姐？"
        show ritona b1 fb4 fa2 fc11 s
        ritona "啊，你在啊。"
        me01 "怎么了？一副心不在焉的样子。"
        show ritona b1 fb1 fa5 fc02
        ritona "没什么，倒是你最近是不是有些松懈了。"
        ritona "别以为没有战斗就可以放松警惕，接下来还不知道会发生什么。"
        me01 "我知道的。"
        ritona "算了，反正你的未来什么的怎么样都与我无关。" 
        me01 "冷淡程度还是一点都没有减弱啊......"
        window mode thought
        me01 "开放所有副本困难级难度，收益将进一步提升（高危慎入）。"
        window mode thought
        me01 "接下来将进入「冬之章」的最终剧情，请提前准备好道具和角色练度。"
        window mode thought
        me01 "希菲尔将在接下来的剧情离开队伍，因此可无需对其消耗大量素材（有爱的话请无视）。"
        show ritona b3 fb1 fa0 fc02
        $ flcam.stop()
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
        $ seen_day228_ritroom = True

        python:
            local_config.total_tutorial_flags += [
                "attack_battle_abyss",
                "speed_battle_abyss",
                "protect_battle_abyss",
                "fire_battle_abyss",
                "light_battle_abyss", 
                "water_battle_abyss", 
                "ice_battle_abyss", 
                "rock_battle_abyss", 
                "wind_battle_abyss"
            ]
    else:
        pause 0.5 hard
        scene black with dissolve
        pause 3.0 hard
        scene set ritroom night:
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
        $ camera_move(-5400, 100, 200, duration=3.0)
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
            sleep jump day228.sleep_memory
            shop jump day228.shop
            member jump day228.stats
            teleport jump day228.teleport
            callback jump day228.callback
            roleroom jump day228.roleroom
            memory jump day228.memory


label day228.callback:
    default seen_day228_callback = False
    hide screen investigation_popup
    scene black
    pause 1.0 hard
    
    $ flcam.move(0, 0, 0)
    scene set only fight_cg msk
    with slowdissolve
    pause 0.5 hard
    
    python:
        can_get_roles_1 = "、".join(["「{}」".format(getattr(store, obj).name) for obj in list(local_config.role_pool)[:6]])
        can_get_roles_2 = "、".join(["「{}」".format(getattr(store, obj).name) for obj in list(local_config.role_pool)[6:]])
        outfits_level1 = [outfit for outfit in outfit_list if "_01" in outfit.objectname]
        outfits_level2 = [outfit for outfit in outfit_list if "_02" in outfit.objectname]
        outfits_level3 = [outfit for outfit in outfit_list if "_03" in outfit.objectname]
        outfits_level4 = [outfit for outfit in outfit_list if "_04" in outfit.objectname]

        equip_is_full = local_config.player.is_equipments_full(recall=1)
        equip_is_full_10 = local_config.player.is_equipments_full(recall=10)

    if not seen_day228_callback:
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
        show ritona b9 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)
        window mode thought
        ritona "当前可抽取的角色包括[can_get_roles_1] ..."
        window mode thought
        ritona "[can_get_roles_2]"
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

        $ seen_day228_callback = True
    
    stop music fadeout 2.0
    pause 1.0 hard
    $ mouse_visible = False
    $ _skipping = renpy.seen_audio("video/second_op.mp4")
    $ config.skipping = None
    scene black
    show movie onlayer master
    play movie "video/second_op.mp4" loop
    play music "video/second_op.mp3" loop
    pause 5.0 hard
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
                        call screen send_detective_screen

                    show pooler_move:
                        xalign 0.5
                        yalign 0.35

                    # call screen input_sentence
                    # $ sentence = _return.strip()

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
                    jump day228.ritroom
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
                        call screen send_detective_screen

                    show pooler_move:
                        xalign 0.5
                        yalign 0.35

                    # call screen input_sentence
                    # $ sentence = _return.strip()

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
                    jump day228.ritroom
            "下次一定":
                window mode thgouth
                me01 "相遇即是缘，请好好珍惜这份来之不易的羁绊。"
                pause 0.5 hard
                $ window_animate_outro()
                stop movie
                hide movie
                stop music fadeout 1.0
                $ _skipping = True
                jump day228.ritroom


label day228.memory:
    menu:
        "立花希篇":
            if not seen_day224_lhx_memory:
                stop music fadeout 5.0
                stop ambience1 fadeout 3.0
                jump battle_lhx_memory_day228
        "取消":
            jump investigate

    jump day228.ritroom


label day228.shop:
    hide investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day city3 xuejian
    with slowdissolve
    pause 1.0 hard
    show ritona b3 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)

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
    jump day228.ritroom


label day228.stats:
    hide screen investigation_popup
    
    python:
        for role in local_config.party:
            role.hp = role.max_hp + role.extend_max_hp
            role.mp = role.max_mp
    $ local_config.current_mode == "Consumables"
    $ local_config.current_actor = local_config.party[0]

    call screen stats
    jump investigate


label day228.roleroom:
    hide screen investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)

    python:
        local_config.start_init(local_config.player, local_config.party)
        local_config.next_story = "day228.ritroom"
    
    call info


label day228.teleport:
    hide screen investigation_popup

    python:
        current_message = ""
        
    call screen teleporter("228")
    jump investigate


label day228.sleep_memory:
    menu:
        "结束梦境":
            python:
                ms_average_level = 0
                breakout_flag = []
                outfits_levels = []
                for par_name in local_config.masters:
                    for role in local_config.party:
                        if role.objectname == par_name:
                            ms_average_level += role.level
                            if role.level < 40 and role.level % 5 == 0 and (not role.break_through):
                                breakout_flag.append(False)
                            else:
                                breakout_flag.append(True)
                            for categ, outfit in role.outfits.items():
                                if outfit is not None:
                                    outfits_levels.append(outfit.level)
                                else:
                                    outfits_levels.append(0)
                ms_average_level /= len(local_config.masters)

            if len([role for role in local_config.party if role.name != "希菲尔"]) < 3 or (ms_average_level < 40) or any([l < 12 for l in outfits_levels]):
                window mode thought
                me01 "下一次的敌人可能会比较棘手，还是去「异界」和「养成屋」多准备一下吧。"
                window mode thought
                me01 "确保队伍成员除「希菲尔」外至少在{color=#ff0000}三名{/color}以上，且平均等级在{color=#ff0000}40级{/color}、且装备等级均在12级以上比较稳妥。"
                menu:
                    "继续前进（不推荐）" if len([role for role in local_config.party if role.name != "希菲尔"]) >= 3:
                        pass
                    "再准备准备":
                        $ camera_move(-5400, 100, 200, duration=3.0)
                        pause 0.5 hard
                        jump investigate
            $ flcam.move(-5400, -100, 400, duration=1.5)
            pause 0.5 hard
            show ritona b1 fb4 fa3 fc01
            ritona "......"
            ritona "夏之死神和冬之妖精......吗。"
            show ritona b3 fb5 fa1 fc02
            ritona "神野凉。"
            ritona "你还真是位不可思议的家伙啊。"
        "{#cancel}再等等":
            ritona "还有什么事情要考虑的吗？"
            $ camera_move(-5400, 100, 200, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    stop ambience1 fadeout 3.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    pause 1.0 hard

    nvl clear
    pcenter "公主大人。"
    pause 0.5 hard
    nvl clear
    with dissolve
    pcenter "我们所未能达成的夙愿。"
    pause 0.5 hard
    nvl clear
    with dissolve
    pcenter "说不定真的可以实现了......"
    pause 0.5 hard
    nvl clear
    with dissolve

    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True

    pause 2.0 hard
    jump day228.memory_event01

label day228.memory_event01:
    $ flcam.move(0, 0, 0)
    scene set only memory_cg yuki ground
    show snow_level1 onlayer fg
    play music second_154 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    me01 "找到你了，希菲尔。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008610.ogg"
    xfe "诶嘿......被发现了。"
    me01 "身体还难受吗？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001008620.ogg"
    xfe "不会的，在这里的话就没问题。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001008630.ogg"
    xfe "在这颗星球上的话，希菲尔都能一直保持精神的哟~"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001008640.ogg"
    xfe "凉君能来真是太好了。"
    play voice "voice/希菲尔/001008650.ogg"
    xfe "在被凉君找到之前，全都是可怕的梦。"
    pause 0.1 hard
    scene set only xfe_cg memory four
    with dissolve
    play voice "voice/希菲尔/001008660.ogg"
    xfe "无论希菲尔我怎么找，始终都找不到凉君的身影。"
    play voice "voice/希菲尔/001008670.ogg"
    xfe "在这白色的雪原上，希菲尔我一直都是孤单一人。"
    me01 "现在有我在你的身边，所以不用担心了。"
    pause 0.1 hard
    scene set only xfe_cg memory two
    with dissolve
    play voice "voice/希菲尔/001008680.ogg"
    xfe "嗯，凉君在身边的话就不害怕了~"
    play voice "voice/希菲尔/001008690.ogg"
    xfe "就算春天降临了，也一定......不用害怕的。"
    me01 "希菲尔觉得春天很可怕吗？"
    play voice "voice/希菲尔/001008710.ogg"
    xfe "虽然比夏天要好一些，但是比起冬天还是差很多。"
    play voice "voice/希菲尔/001008720.ogg"
    xfe "但即便如此......就算现在害怕春天，将来说不定也会喜欢上的。"
    pause 0.1 hard
    scene set only xfe_cg memory five
    $ flcam.move(-1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001008730.ogg"
    xfe "因为希菲尔我很喜欢待在凉君身边时候温暖的感觉。"
    play voice "voice/希菲尔/001008740.ogg"
    xfe "如果这就是所谓的春天的话，希菲尔一定能喜欢上的~"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001008750.ogg"
    xfe "还想......再和凉君一起前进。"
    play voice "voice/希菲尔/001008760.ogg"
    xfe "那样的话就能够保持现在这样的心情去迎接春天了。"
    play voice "voice/希菲尔/001008770.ogg"
    xfe "也许还会因此喜欢上春天也说不定。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory two
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001009870.ogg"
    xfe "和凉君一起的话，无论是什么季节......感觉都能喜欢上。"
    play voice "voice/希菲尔/001009880.ogg"
    xfe "春天、夏天、秋天、冬天。"
    play voice "voice/希菲尔/001009890.ogg"
    xfe "不只是下雪的季节，冰雪消融的季节也一定......能喜欢上的。"
    pause 0.1 hard
    scene set only xfe_cg memory five
    $ flcam.move(-1100, -1400, 450, duration=1.5)
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001009900.ogg"
    xfe "那时候一定......就是染上凉君颜色的意思了~"
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True

    python:
        # 希菲尔离开队伍
        local_config.masters = ["lst_role"]
        # 确保雷亚在队伍中的第一位
        leiya_in_party = False
        for i, role in enumerate(copy(local_config.party)):
            if role.name == "雷亚":
                if i != 0:
                    local_config.party.remove(role)
                    local_config.party.insert(0, role)
                leiya_in_party = True
                break
        # 雷亚不再队伍中则加入
        if not leiya_in_party:
            for role in copy(local_config.backup):
                if role.name == "雷亚":
                    local_config.backup.remove(role)
                    local_config.party.insert(0, role)

        for role in local_config.party:
            if role.name == "希菲尔":
                local_config.party.remove(role)
                local_config.release.append(role)

        for role in local_config.backup:
            if role.name == "希菲尔":
                local_config.backup.remove(role)
                if role not in local_config.release:
                    local_config.release.append(role)

        local_config.role_pool.remove("xfe_role")

    jump day229
