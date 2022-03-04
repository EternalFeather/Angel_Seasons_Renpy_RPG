
label inside_battle15(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "「相遇之缘」战斗是发生在平行时空下的镜像世界中，角色将与{color=#f00}自己的镜像{/color}进行战斗并最终超越自身。"
    "镜像的装备、技能等级均与队伍中角色持平。"
    "另外特定的{color=#f00}剧情角色{/color}无法参与战斗并会出现在对方阵容中，请妥善应对。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label battle_lst_memory_day224:
    $ flcam.move(0, 0, 0)
    scene set only fight_cg rune1
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    python:
        # 战斗boss为雷亚，其他角色为镜像角色（除了希菲尔），所有敌方等级、装备均与队伍中保持相同
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
                role = lst_role_mirror
                # 装备继承
                for cate, outfit in ori_role.outfits.items():
                    if outfit is not None:
                        outfit.enemy_equip_on(role)
                # 技能等级继承
                for skill in ori_role.skills:
                    new_skill = [s for s in role.skills if s.category == skill.category][0]
                    new_skill.level_change(skill.level)
                for skill_v2 in ori_role.skills_v2:
                    new_skill = [s for s in role.skills_v2 if s.category == skill_v2.category][0]
                    new_skill.level_change(skill_v2.level)
                # 等级继承
                role.stats_check(ori_role.level)

        for role in copy(local_config.party):
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)
    
    pause 0.25
    call battle(boss=lst_role_mirror,
                boss_hp_plus=60000,
                side_enemy=side_enemy_roles, 
                side_hp_plus=20000,
                level=-1,
                boss_first=False, 
                win_condition='normal',
                stay_turn=0,
                inside_label="inside_battle15" if not seen_day224_lst_memory else None, 
                mission_type="normal", 
                treasures={
                    "angel_tears": (1, 1.0),
                    "eggs": (5, 0.6),
                    "mana_eggs": (3, 0.3),
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
        "雷亚重新加入队伍。"
        python:
            seen_day224_lst_memory = True
            for role in local_config.release:
                if role.name == "雷亚":
                    role.mp = role.max_mp
                    role.hp = role.max_hp + role.extend_max_hp
                    local_config.backup.append(role)
                    local_config.release.remove(role)
            local_config.role_pool.add("lst_role")

        stop music fadeout 5.0
    else:
        jump battle_end

    jump day224.ritroom


label battle_lhx_memory_day224:
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
                inside_label="inside_battle15" if not seen_day224_lhx_memory else None, 
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

    jump day224.ritroom


label day224:
    bookmark
    $ save_name = _("Day 224")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date223 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only home snow day outside xuejian
    play music second_102 fadein 3.0 if_changed
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    play ambience1 niaoming fadein 3.0
    "又是新的一天。"
    "然而此时我的脑海里却是空荡荡的。"
    "对于之前立花老师的事情我还是没有办法完全释怀。"
    stop ambience1 fadeout 3.0
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    show jingya onlayer texture:
        xpos 0.0
    show alu_ct_b4 b4 b4_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/阿露/551000090.ogg"
    alu "唔莎~波！"
    play sound rell_fire 
    with vpunch
    pause 1.0 hard
    play music second_108 fadein 3.0 if_changed
    me01 "{size=72}又来？！{/size}"
    hide jingya
    hide alu_ct_b4
    $ flcam.move(1100, 1400, 450, duration=1.5)
    play sound shoot2 
    with vpunch
    pause 0.5 hard
    "我下意识向一旁闪避开。"
    show wflash onlayer texture 
    "像雪橇一样在地上滑行了一段距离后才停下。"
    "结果搞得浑身都是积雪。"
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001002770.ogg"
    xfe "阿露她又变得有精神了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show alu_ct_b10 b10 b10_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/阿露/551000040.ogg"
    alu "唔莎~"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/希菲尔/001002780.ogg"
    xfe "不仅是胡萝卜大放送，还有胡萝卜周年庆呀～"
    me01 "这和我有什么关系？！"
    hide alu_ct_b10
    show alu_ct_b8 b8 b8_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/阿露/551000580.ogg"
    alu "唔莎？"
    show ts_xfe_yjz_b2 b2 b2_s2
    play voice "voice/希菲尔/001002790.ogg"
    xfe "不是那样的阿露，虽然现在的凉君看起来的确很奇怪，但他并不是萝莉控。"
    "总觉得在讨论什么不得了的东西......"
    hide alu_ct_b8
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp1
    play voice "voice/希菲尔/001002800.ogg"
    xfe "凉君，有什么心事吗？"
    stop music fadeout 5.0
    me01 "希菲尔你知道{rb}灵纹{/rb}{rt}rune{/rt}吗？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001002810.ogg"
    xfe "知道哟~"
    me01 "也是千冬告诉你的吗？"
    play music second_140 fadein 3.0 if_changed
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001002830.ogg"
    xfe "就是这样的哟~"
    me01 "既然如此我有问题想要请教你。"
    show ts_xfe_yjz_b2 b2 b2_sp1
    play voice "voice/希菲尔/001002840.ogg"
    xfe "？"
    me01 "总觉得最近我体内的{rb}灵纹{/rb}{rt}rune{/rt}不太稳定，但是我也不知道是为什么。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001002850.ogg"
    xfe "不要紧的。"
    $ flcam.move(4500, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001002860.ogg"
    xfe "一定是春天已经临近了，所以凉君体内的{rb}灵纹{/rb}{rt}rune{/rt}才会变得不安分的。"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001002870.ogg"
    xfe "习惯的话应该就能变回平常的样子了。"
    me01 "这也是千冬告诉你的？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001002880.ogg"
    xfe "......不是的。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001002890.ogg"
    xfe "希菲尔我自己也不清楚。"
    play voice "voice/希菲尔/001002900.ogg"
    xfe "只是梦到了而已。"
    me01 "梦到了？"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001002910.ogg"
    xfe "凉君，突然出现真是抱歉。但是希望你能继续帮助那些迷路的孩子们。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show alu_ct_b2 b2 b2_2 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎~"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_a1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/希菲尔/001002920.ogg"
    xfe "虽然阿露还想再玩，不过让凉君为难的话希菲尔可是会把你吞下去的。"
    hide alu_ct_b2
    show alu_ct_b13 b13 b13_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.5
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......"
    hide alu_ct_b13
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001002930.ogg"
    xfe "拜拜凉君~"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001002940.ogg"
    xfe "春天会如期而至的，所以不必太过担心。"
    show wflash onlayer texture
    play sound xiaoshi_1
    show ts_xfe_yjz_b1 b1 b1_h1:
        xpos 0.7 alpha 1.0
        linear 0.5 alpha 0.0
    pause 1.0 hard
    hide ts_xfe_yjz_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    stop music fadeout 5.0
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 1.0 hard
    $ _overworld_label = 'day224'
    $ seen_day224_balltower_event01 = False
    $ seen_day224_home_event01 = False

label day224.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day224':
        show set maps winter day
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day224.balltower_event01':
        show set maps winter evening
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['cloqks'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        cloqks=("day224.balltower_event01", "not seen_day224_balltower_event01"),
        road1=("day224.home_event01", "seen_day224_balltower_event01 and not seen_day224_home_event01"))
    $ window_animate_outro()
    if _return == 'day224.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day224.home_event01':
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

label day224.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    show snow_level1 onlayer fg
    with slowdissolve
    play music first_25 fadein 3.0 if_changed
    pause 1.0 hard
    "抬头仰望天空，我独自漫步在这悠长的雪道上。"
    "这样的孤独感已经多久没有体会过了呢？"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    with dissolve
    pause 1.0 hard
    "来到了钟楼广场。"
    "这里依旧是空无一人，安静得甚至能够听到钟摆的声音。"
    me01 "哈啊。"
    "我叹了一口气，白雾在我的眼前扩散开来融入白雪之中。"
    me01 "我到底在干什么？"
    me01 "这样消沉一点也不像我。"
    me01 "明明说好不再摆出这样的表情了，再这样下去要被翔子、被梦嘲笑的。"
    me01 "至今为止发生过的一切就像是一场梦。"
    me01 "我究竟应该如何......才能在这宛如梦境一般的世界线中把握住命运的方向呢？"
    stop music fadeout 5.0
    play sound jiaobu
    pause 3.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_s1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play music first_30 fadein 3.0 if_changed
    play voice "voice/天使莲/170199.ogg"
    ts_lian "的确......以人类的角度来看我们就像是幻觉一般的存在。"
    me01 "苍衣......同学？"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170200.ogg"
    ts_lian "是我，好久不见了。"
    me01 "你怎么回来雪见市？"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/170201.ogg"
    ts_lian "我只是来打个招呼而已。"
    me01 "难道不是有事情想要拜托我吗？"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170202.ogg"
    ts_lian "不是的，我是专程来问候凉同学的。"
    me01 "抱歉，现在我没有心情闲聊。"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/170203.ogg"
    ts_lian "是因为一直都没办法找到陨石对吧？"
    me01 "为什么你会......"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/170204.ogg"
    ts_lian "你觉得在这样的大雪中真的能找到吗？"
    me01 "我不知道。"
    me01 "但是立花老师确实是这样说的。"
    me01 "说实话现在的我已经感觉我永远也无法找到”她“了。"
    me01 "我之所以会来这里也只是想找个让自己不放弃的理由罢了。"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/170205.ogg"
    ts_lian "重视到这种程度了吗。"
    play voice "voice/天使莲/170206.ogg"
    ts_lian "对雷亚她......"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/170207.ogg"
    ts_lian "你的身边明明已经......有了新的伙伴。"
    play voice "voice/天使莲/170208.ogg"
    ts_lian "明明也已经成功拯救“梦”了。"
    play voice "voice/天使莲/170209.ogg"
    ts_lian "然而为何......还要执着于那本就不应该存在于世上的梦幻呢？"
    me01 "梦幻......吗。"
    me01 "也许真的如你所说的那样没错。"
    me01 "但是我可是很贪心的啊。"
    me01 "无论是谁，对于失去了的东西总会不自觉地想要夺回来。"
    me01 "雷亚也好、梦也罢，还有立花老师。"
    me01 "她们都是为了帮助我才从我的眼前消失的，而我怎么可能因为这点挫折就轻易放弃了。"
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/170210.ogg"
    ts_lian "可是就连星天宫的搜查队都没有办法做到，仅凭你一个人......而且是在这大雪之中。"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/170212.ogg"
    ts_lian "要找到陨石——找到雷亚的话。"
    play voice "voice/天使莲/170211.ogg"
    ts_lian "至少在我看来是不可能完成的任务。"
    me01 "虽然现在才问有点奇怪，苍衣同学和雷亚是同样的存在对吧？"
    me01 "这个时候出现在我的面前真的没问题吗？"
    me01 "甚至还能正常地去上课。"
    show ts_lian_ssz_b1 b1 b1_s2
    play voice "voice/天使莲/170213.ogg"
    ts_lian "这种程度的话对我来说还是可以的，虽然会有点累。"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170217.ogg"
    ts_lian "如果你想要更科学的解释可以去问大和君。"
    show ts_lian_ssz_b1 b1 b1_h1
    play voice "voice/天使莲/170218.ogg"
    ts_lian "因为大和君是教授嘛~"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170219.ogg"
    ts_lian "大和君也是一位，被星星所眷顾的人。"
    me01 "父亲他......"
    me01 "真是搞不懂那家伙。"
    me01 "明明口中总是念叨着有母亲在身边就足够幸福了。"
    me01 "可为什么还要不顾一切地开展研究。"
    me01 "明明到最后就连母亲也保护不了......"
    show ts_lian_ssz_b1 b1 b1_s1
    play voice "voice/天使莲/170220.ogg"
    ts_lian "这也许就是你所谓的“贪得无厌”的感觉吧。"
    me01 "话说那家伙......现在过得还好吗？"
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/170221.ogg"
    ts_lian "在意的话直接去问他本人不就好了吗？"
    me01 "就算我去见他，那个人也会用敷衍的态度打发我吧。"
    show ts_lian_ssz_b1 b1 b1_h2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/天使莲/170222.ogg"
    ts_lian "咯咯咯咯......因为大和君也是废柴人类嘛~"
    show ts_lian_ssz_b1 b1 b1_n1
    play voice "voice/天使莲/170223.ogg"
    ts_lian "就算见到你也不知道应该用什么样的表情面对你。"
    me01 "嘛，多少我也能够理解。"
    me01 "因为我也是一样的。"
    stop music fadeout 5.0
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/170224.ogg"
    ts_lian "而且现在，比起大和君你更想见到的应该是雷亚吧？"
    me01 "都是对我而言重要的人就不要用天秤来衡量了。"
    play music first_36 fadein 3.0 if_changed
    show ts_lian_ssz_b1 b1 b1_s3
    play voice "voice/天使莲/170225.ogg"
    ts_lian "也许你也意识到了，想要和雷亚相遇的话，“羁绊”是必须的。"
    play voice "voice/天使莲/170226.ogg"
    ts_lian "能够渡过天河的鹊桥......是能够连接起次元的。"
    play voice "voice/天使莲/170227.ogg"
    ts_lian "不管怎么说，我认为用现在的方法是没有办法找到雷亚的。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_lian_ssz_b1 b1 b1_n2
    play voice "voice/天使莲/170228.ogg"
    ts_lian "请许下愿望吧。"
    play voice "voice/天使莲/170229.ogg"
    ts_lian "就像雷亚她......曾经对这颗星球许下的承诺一样。"
    play voice "voice/天使莲/170230.ogg"
    ts_lian "如果你真的是被这颗星球——被这座城市的冬雪眷顾的话，一定可以做到的。"
    pause 0.5 hard
    play sound xiaoshi_1
    show ts_lian_ssz_b1 b1 b1_n2:
        xpos 0.5 alpha 1.0
        linear 1.0 alpha 0.0
    pause 1.0 hard
    hide ts_lian_ssz_b1
    hide snow_level1
    scene white
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only kls_cg sad
    with slowdissolve
    pause 1.0 hard
    play voice "voice/天使莲/170231.ogg"
    ts_lian "曾经被你亲手送还的，那孩子......"
    pause 0.1 hard
    scene set only kls_cg normal
    with dissolve
    play voice "voice/天使莲/170232.ogg"
    ts_lian "只要你用心呼唤的话......她也一定也会回应你的吧。"
    stop music fadeout 3.0
    pause 3.0 hard
    hide snow_level1
    scene black
    with slowdissolve
    pause 2.0 hard
    if not seen_day224_balltower_event01:
        $ seen_day224_balltower_event01 = True
    $ _overworld_label = 'day224.balltower_event01'
    jump day224.map

label day224.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    play music first_36 fadein 3.0 if_changed
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    show xz_dsf_b3 b3 b3_s2 onlayer screens at side_left('xz', 0.03), basicfade
    play voice "voice/翔子/010778.ogg"
    stranger "太阳开始下山了呢......"
    hide xz_dsf_b3
    pause 1.0 hard
    scene set only home snow evening outside xuejian big
    $ flcam.move(2250, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.6
    play voice "voice/翔子/010779.ogg"
    xz "远方的街道也......沉浸在金色的光晕之中。"
    play voice "voice/翔子/010780.ogg"
    xz "空气变冷了，温度也下降了。"
    show xz_dsf_b3 b3 b3_s1
    play voice "voice/翔子/010781.ogg"
    xz "马上就到......能看见星星的时间了。"
    hide xz_dsf_b3
    $ flcam.move(-2250, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b3 b3 b3_n1 onlayer m2 at walkin_l(0.4)
    pause 0.5 hard
    play voice "voice/水之濑/030345.ogg"
    szl "就算这样，也还是会继续等下去的吧。"
    $ flcam.move(0, -350, 750, duration=1.5)
    show xz_dsf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.6
    play voice "voice/翔子/010782.ogg"
    xz "......欸？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show lingyin_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.2
    play voice "voice/青木铃音/040417.ogg"
    lingyin "加上我们的话，寒冷多少也会缓和一些吧~"
    play voice "voice/翔子/010783.ogg"
    xz "......你们两个，为什么？"
    play voice "voice/翔子/010784.ogg"
    xz "你们不是......赶去樱华镇调查事情了吗？"
    show lingyin_dsf_b2 b2 b2_ga3
    play voice "voice/青木铃音/040418.ogg"
    lingyin "是的，虽然是这样不过也就刚刚才赶回来的而已。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/030347.ogg"
    szl "毕竟我们，还有更重要的事情要处理。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s2 onlayer m1:
        xpos 0.6
    play voice "voice/翔子/010785.ogg"
    xz "为什么大家......"
    show lingyin_dsf_b2 b2 b2_n1
    play voice "voice/青木铃音/040421.ogg"
    lingyin "听说最近的新闻里也提到这座城市又开始积雪了。"
    hide xz_dsf_b3
    $ flcam.move(-6500, -200, 600, duration=1.5)
    show rxl_dsf_b1 b1 b1_n4 onlayer m2:
        xpos 0.0
    play voice "voice/日向怜/020351.ogg"
    rxl "大家因为在意所以就过来看看了。"
    show lingyin_dsf_b2 b2 b2_h1
    play voice "voice/青木铃音/040422.ogg"
    lingyin "是的，意识到的时候马上就觉得不一样了。"
    play voice "voice/青木铃音/010786.ogg"
    lingyin "我们都是来声援的。"
    show szl_dsf_b2 b2 b2_ga1
    play voice "voice/水之濑/030350.ogg"
    szl "虽然要声援的对象，现在好像还不知道在哪里的样子。"
    show lingyin_dsf_b2 b2 b2_n1
    play voice "voice/青木铃音/040423.ogg"
    lingyin "即使是这样，我也觉得还是可以帮上忙的。"
    $ flcam.move(-1250, -200, 500, duration=1.5)
    show xz_dsf_b3 b3 b3_h1 onlayer m1:
        xpos 0.55
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010787.ogg"
    xz "像这样大家一起会比较暖和。"
    play voice "voice/翔子/010791.ogg"
    xz "所以......"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_s2 onlayer m1:
        xpos 0.4
    play voice "voice/水之濑/030353.ogg"
    szl "这样真的可以吗？"
    show xz_dsf_b3 b3 b3_s4
    play voice "voice/翔子/010792.ogg"
    xz "......"
    $ flcam.move(0, -100, 400, duration=1.5)
    show shy_yjf_b1 b1 b1_h2 onlayer m1:
        xpos 0.82
    play voice "voice/圣护院/100259.ogg"
    shy "担心的话，就更应该把祝福寄托给那位被大家牵挂的死神，以及她的“主人”才对吧？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with dissolve
    pause 1.0 hard
    nvl clear
    play voice "voice/翔子/010795.ogg"
    pcenter "{rb}凉君{/rb}{rt}梦称呼的方式{/rt}......"
    pause 0.5 hard
    nvl clear
    with dissolve
    play voice "voice/翔子/010796.ogg"
    pcenter "或许我们真的......是被许多人守护着的。"
    pause 0.5 hard
    nvl clear
    with dissolve
    play voice "voice/翔子/010797.ogg"
    pcenter "所以我，也想要成为大家的力量。"
    pause 0.5 hard
    nvl clear
    with dissolve
    play voice "voice/翔子/010799.ogg"
    pcenter "我决定了。"
    pause 0.5 hard
    nvl clear
    with dissolve
    play voice "voice/翔子/010798.ogg"
    pcenter "也想成为守护谁的力量。"
    pause 0.5 hard
    nvl clear
    with dissolve
    play voice "voice/翔子/010800.ogg"
    pcenter "我的意志......也一定可以传达到的。"
    pause 0.5 hard
    nvl clear
    with dissolve
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard

label day224.balltower_event02:
    scene set only balltower night xuejian
    show snow_level1 onlayer fg
    play music first_23 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "大概是因为疲劳以及严寒的缘故，我完全没有意识到时间的流逝。"
    "手脚也已经没有知觉了。"
    "因为没有信心在休息之后还能再一次站起来，于是强迫自己不停地坚持。"
    "四下寻找过后，我又一次回到了这座钟楼。"
    "雷亚不喜欢人多的地方，所以如果真的像立花老师说的那样。"
    "这座钟楼一定是最适合她的地方。"
    "之前和铃音战斗的时候也是在这里。"
    "但是现在疲劳和绝望已经占据了我的大脑。"
    me01 "就这样倒下的话......"
    "也许就能像在梦中见到希菲尔一样，再次和雷亚重逢了也说不定。"
    "意识渐渐开始变得模糊起来。"
    "睡着的话，等待我的只有被冻死吧。"
    me01 "可恶。"
    "就算用手拨开层层的积雪，也只是让视线中的黑暗变得更加广阔。"
    "到底要怎么做......"
    me01 "不能停止！"
    "就如苍衣同学说的那样，单凭我一个人的力量说不定永远也无法做到，但是......"
    "即使是硬着头皮，我也只能前进了。"
    "这是我唯一能为她做的事情了。"
    "就在我正想要起身迈开脚步的时候，膝盖不听使唤地摊倒在地上。"
    stop music fadeout 5.0
    "脚和腰都使不上力气了。"
    "就连继续前进也做不到了吗......"
    pause 1.0 hard
    hide snow_level1
    scene black 
    with side2cent
    pause 1.0 hard
    "听不到周围的声音。"
    "感觉一切仿佛都归于虚无了。"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 2.0 hard
    play music first_24 fadein 3.0 if_changed
    "从虚无中诞生宇宙。"
    "在宇宙中孕育新的生命。"
    "正因为是虚无的事物，才蕴含着最真实的灵魂。"
    "那是万物伊始的姿态。"
    me01 "这种感觉是......终于要来了吗？"
    "曾经也体验过这样的事。"
    "就像是摆脱了肉体的束缚一般轻盈。"
    "如果世界上真的有所谓的奇迹的话。"
    "请再让我见到，那个我无时无刻不在牵挂着的身影吧——"
    pause 2.0 hard
    scene set only lisite_cg final one
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/001541.ogg"
    lst "今晚的你，也是特别笨笨的呢~"
    me01 "......见面的第一句就是这个吗？"
    pause 0.1 hard
    scene set only lisite_cg final three
    with dissolve
    play voice "voice/天使雷亚/001542.ogg"
    lst "宇宙的诞生怎么样都好。"
    me01 "别说一些破坏气氛的话嘛。"
    play voice "voice/天使雷亚/001543.ogg"
    lst "你就那么喜欢物理吗？"
    me01 "我喜欢的是你啊！"
    pause 0.1 hard
    scene set only lisite_cg final two
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/001544.ogg"
    lst "......"
    me01 "有问题吗？"
    play voice "voice/天使雷亚/001545.ogg"
    lst "凉君你是大骗子。"
    play voice "voice/天使雷亚/001546.ogg"
    lst "凉君喜欢的明明是梦。"
    me01 "所以说不要让我用天秤来衡量啊。"
    pause 0.1 hard
    scene set only lisite_cg final three
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/001547.ogg"
    lst "那我回去了。"
    me01 "请等一下。"
    play voice "voice/天使雷亚/001548.ogg"
    lst "还有什么事吗？"
    me01 "我有一个请求。"
    play voice "voice/天使雷亚/001549.ogg"
    lst "是什么？"
    me01 "雷亚你会回到我身边的吧？"
    pause 0.1 hard
    scene set only lisite_cg final two
    with dissolve
    play voice "voice/天使雷亚/001550.ogg"
    lst "......"
    me01 "如果我和八年前一样，许下“我们一定会再见面”的愿望的话，雷亚你就会再一次回到我身边对吧？"
    me01 "死神是绝对会遵守约定的对吧？"
    pause 0.1 hard
    scene set only lisite_cg final three
    with dissolve
    play voice "voice/天使雷亚/001551.ogg"
    lst "呼嗯~"
    play voice "voice/天使雷亚/001552.ogg"
    lst "不要......"
    me01 "为什么啊？"
    play voice "voice/天使雷亚/001553.ogg"
    lst "不为什么。"
    me01 "如果你能同意的话大哥哥我会很开心的。"
    pause 0.1 hard
    scene set only lisite_cg final two
    with dissolve
    play voice "voice/天使雷亚/001554.ogg"
    lst "不要。"
    me01 "那就拒绝我。"
    play voice "voice/天使雷亚/001555.ogg"
    lst "不要。"
    me01 "你这不还是舍不得我吗？"
    pause 0.1 hard
    scene set only lisite_cg final three
    with dissolve
    play voice "voice/天使雷亚/001556.ogg"
    lst "完全搞不懂你在说什么。"
    me01 "完全搞不懂的人是我啊！"
    play voice "voice/天使雷亚/001557.ogg"
    lst "......"
    me01 "雷亚你是我和翔子的愿望创造的死神对吧？"
    me01 "那样的话留在我们身边不是理所当然的事情吗？"
    me01 "换句话说，与我们在一起的你，才是存在的唯一方式不是吗？"
    me01 "回到我身边来吧，大家、你的朋友们都在期待着你回来呢。"
    pause 0.1 hard
    scene set only lisite_cg final two
    with dissolve
    play voice "voice/天使雷亚/001558.ogg"
    lst "我不明白。"
    play voice "voice/天使雷亚/001564.ogg"
    lst "但是......并不只是这样的。"
    play voice "voice/天使雷亚/001565.ogg"
    lst "我真正的愿望，并不仅仅是想要成为凉君的朋友。"
    play voice "voice/天使雷亚/001566.ogg"
    lst "......不只是朋友。"
    pause 0.1 hard
    scene set only lisite_cg final one
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/001567.ogg"
    lst "而是......更进一步的。"
    play voice "voice/天使雷亚/001568.ogg"
    lst "在那之上的。"
    me01 "在那之上的？"
    pause 0.1 hard
    scene set only lisite_cg final three
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/001569.ogg"
    lst "......笨笨的。"
    me01 "我知道了。"
    play voice "voice/天使雷亚/001570.ogg"
    lst "你......知道了吗？"
    me01 "是啊。"
    play voice "voice/天使雷亚/001571.ogg"
    lst "知道了......我想要和凉君成为什么样的关系？"
    me01 "是啊。"
    play voice "voice/天使雷亚/001572.ogg"
    lst "不行！！！"
    play voice "voice/天使雷亚/001574.ogg"
    lst "你、你不可以知道。"
    play voice "voice/天使雷亚/001575.ogg"
    lst "如、如果凉君知道的话。"
    play voice "voice/天使雷亚/001576.ogg"
    lst "凉君你就出轨了。"
    play voice "voice/天使雷亚/001577.ogg"
    lst "就会变得下流了。"
    play voice "voice/天使雷亚/001578.ogg"
    lst "而我就会变成正太控了。"
    me01 "......哈哈哈。"
    pause 0.1 hard
    scene set only lisite_cg final one
    with dissolve 
    play voice "voice/天使雷亚/001579.ogg"
    lst "所以结果是怎么样的？"
    me01 "谢谢你雷亚。"
    me01 "能够喜欢上这样废废的、笨笨的我。"
    pause 0.1 hard
    scene set only lisite_cg final two
    with dissolve
    play voice "voice/天使雷亚/001581.ogg"
    lst "没什么。"
    me01 "等着吧，我马上就来接你回去。"
    me01 "不是在这里，而是在我生活着的世界里。"
    play voice "voice/天使雷亚/001582.ogg"
    lst "不要。"
    play voice "voice/天使雷亚/001583.ogg"
    lst "因为这里也是......现实。"
    play voice "voice/天使雷亚/001585.ogg"
    lst "没有我的话，就不会有这个时空。"
    play voice "voice/天使雷亚/001586.ogg"
    lst "没有凉君的话，就不会有我的存在。"
    play voice "voice/天使雷亚/001587.ogg"
    lst "没有了梦的话，也不会有现在的我们。"
    play voice "voice/天使雷亚/001588.ogg"
    lst "月亮也好，星星也罢，就连宇宙也是一样的。"
    play voice "voice/天使雷亚/001589.ogg"
    lst "名为{rb}命运{/rb}{rt}Steins{/rt}的东西就是这样理所当然的东西。"
    pause 0.1 hard
    scene set only lisite_cg final one
    with dissolve
    play voice "voice/天使雷亚/001590.ogg"
    lst "不要忘记了凉君。"
    play voice "voice/天使雷亚/001591.ogg"
    lst "虽然我也希望凉君你能够看着我。"
    play voice "voice/天使雷亚/001592.ogg"
    lst "但如果这一切是以让凉君变得伤痕累累为代价的话我就不希望它发生。"
    play voice "voice/天使雷亚/001593.ogg"
    lst "所以......请不要再做这样笨笨的事情了。"
    play voice "voice/天使雷亚/001594.ogg"
    lst "凉君要是不在了，我们建立起的羁绊也会消失的。"
    pause 0.1 hard
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/001595.ogg"
    lst "正因为有凉君，我们才能像现在这样存在着。"
    play voice "voice/天使雷亚/001596.ogg"
    lst "这也是命中注定的事情。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower night xuejian
    show snow_level1 onlayer fg
    with cent2side
    pause 1.0 hard
    "立花老师也好、苍衣同学也好。"
    "即使有了大家的帮助，我还是......没能做到吗？"
    "这样的话我们的羁绊又有什么意义？"
    "不能把你留在身边的话，我们的约定还有什么意义？"
    "我讨厌这样无能的自己。"
    "拯救意味着失去，即使能够改变过去，但世界线总会收束。"
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowdissolve
    stop music fadeout 5.0
    pause 1.0 hard
    "一切的观测结果都只会向着命运希望我们看到的那样前进。"
    "身为观测者的我们也在被世界所观测着。"
    "现在的我们也只是汇聚了过去万千种可能性的其中之一的结果罢了。"
    "如果无法跳出“有我”的视角达到更高的“无我”。"
    "就注定无法超越名为“现实”的这一道屏障，从而打破量子束缚到达平行存在的其他世界线。"
    me01 "然而这是绝对无法实现的事情。"
    me01 "因为观测自己这件事，除了本人以外还有谁能够做到呢......"
    pause 1.0 hard
    play voice "voice/希菲尔/001301440.ogg"
    stranger "嗯，我一直都是这样看着的哟——"
    pause 1.0 hard
    play music second_134 fadein 3.0 if_changed
    scene set only xfe_cg normal
    with dissolve
    play voice "voice/希菲尔/001301450.ogg"
    xfe "希菲尔我也想要守护你们的幸福。"
    play voice "voice/希菲尔/001301470.ogg"
    xfe "在最后无论如何都想说出来。"
    pause 0.1 hard
    scene set only xfe_cg happy
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001301480.ogg"
    xfe "谢谢你们~"
    play voice "voice/希菲尔/001301540.ogg"
    xfe "雪的足迹......一定会继续延续下去的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory4
    with slowdissolve
    pause 1.0 hard
    "希菲尔开始歌唱。"
    "那熟悉而优美的旋律回荡在四周。"
    "歌声飘向远方，划破天际，就像鹊桥一般连接在银河的两端。"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    "那一夜，隔岸相望的两颗心在此刻成为了永恒。"
    stop music fadeout 5.0
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    jump day224.ritroom

label day224.ritroom:
    default seen_day224_ritroom = False
    default seen_day224_memory_space = False
    default seen_day224_lst_memory = False
    default seen_day224_lhx_memory = False
    play music ritroom_day fadein 3.0 if_changed
    play ambience1 ritroom_fireplace fadein 3.0 if_changed

    if not seen_day224_ritroom:
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
        show ritona b1 fb2 fa5 fc12 onlayer m2:
            xpos 0.5
        ritona "今天你来的方式有些特别啊。"
        me01 "弗兰小姐，我怎么会？"
        show ritona b1 fb5 fa2 fc01
        ritona "我还想问你呢，怎么突然就出现在这里了。"
        me01 "我只记得刚刚在钟楼广场听到了希菲尔的歌声，然后就......"
        show ritona b1 fb1 fa5 fc01
        ritona "歌声......吗，嘿~"
        show ritona b3 fb5 fa1 fc02
        ritona "不管怎么样反正也与我无关。"
        me01 "弗兰小姐你的冷淡还依旧是老样子啊。"
        show ritona b1 fb4 fa3 fc01
        ritona "行了，她把你送过来一定有什么特殊的意义在里面。"
        me01 "......"
        show ritona b1 fb5 fa2 fc01
        ritona "发生什么事了？"
        me01 "我一个人果然......什么都办不到。"
        show ritona b1 fb2 fa5 fc12
        ritona "......"
        ritona "虽说不用你特别强调我也是知道的，但你也不用说得那么直接嘛。"
        me01 "只能眼睁睁地看着自己在意的人一个接一个地消失。"
        me01 "而我却只能被迫地接受这样残酷的事实一次，又一次。"
        ritona "......那个。"
        me01 "弗兰小姐，我究竟要怎么做才能改变这一切呢？"
        me01 "我究竟要如何努力，才能先命运一步守住那些对我而言的重要之人呢。"
        show ritona b3 fb5 fa1 fc12 s
        ritona "你也......渴望改变过去吗？"
        me01 "那是当然！"
        show ritona b1 fb4 fa3 fc01 at flu_down(0.15, 20):
            xpos 0.5
        play sound hite_light
        with vpunch
        me01 "{size=72}好痛！{/size}"
        me01 "干嘛突然打我？"
        show ritona b2 fb1 fa5 fc12
        ritona "你脑子生锈了吗？"
        ritona "时间穿越这种很明显不可行的事情你竟然还抱有幻想。"
        ritona "我不打你换做其他人也会这么做的。"
        me01 "抱歉......"
        me01 "我只是不想再看到自己这样狼狈不堪。"
        me01 "我已经不想再体会失去谁的感觉了。"
        me01 "更不想......白白浪费掉那些曾经为了我而离去的伙伴对我给予的帮助。"
        me01 "立花老师也是，她明明有权利选择另一条继续存在下去的路。"
        show ritona b1 fb1 fa5 fc02
        ritona "且不说是不是为了帮你找回羁绊，那孩子的消失也是注定了的结果。"
        me01 "这是什么意思？"
        show ritona b1 fb4 fa3 fc11
        ritona "你啊......没听过天机不可泄露吗？"
        me01 "既然如此你为什么还要说出来。"
        show ritona b1 fb4 fa2 fc11 s
        ritona "......"
        me01 "......"
        show ritona b1 fb4 fa2 fc13 s
        ritona "那是因为......"
        me01 "某种意义上而言弗兰小姐在保密工作上已经足够失职了吧。"
        ritona "打击！"
        show ritona b1 fb4 fa3 fc01
        ritona "我知道了啦，告诉你也无妨。"
        ritona "反正星天宫那帮家伙应该也不会猜到是我说的......（小声）"
        me01 "我听到了啊喂！"
        show ritona b1 fb1 fa0 fc12 s
        ritona "听好了，那位名叫立花希的女孩其实原本就在与你第一次分别的时候就永远地离开了这个世界。"
        ritona "从小就体弱多病的她，更是在母亲离世后因为伤心过度而患上了绝症。"
        show ritona b3 fb5 fa1 fc02
        ritona "那本应该是她度过的，最后一个冬天了。"
        show ritona b1 fb1 fa0 fc11 s
        ritona "但是呢，在她临走前还是把对那位名叫希菲尔的少女和你的思念，通过愿望的形式保存了下来。"
        ritona "愿望这种念波本就是难以被观测到的，跨越了时间的、不可思议的光。"
        ritona "在你走后这份思念就一直尘封在了她随身携带钥匙的那个盒子里。"
        show ritona b3 fb5 fa1 fc02
        ritona "潘多拉的魔盒里所承载的希望，说的就是这样的东西。"
        ritona "然而作为播撒希望的代价，她最终可能收获的也只有绝望而已。"
        show ritona b3 fb5 fa1 fc12 s
        ritona "幸运的是就是与此同时，身为死神的雷亚也许下了让你以及你身边之人能够得到幸福的愿望。"
        ritona "就这样两股力量相遇了。"
        show ritona b1 fb2 fa5 fc12
        ritona "于是便诞生了现在的立花希。"
        me01 "怎么......会这样。"
        show ritona b1 fb4 fa3 fc01
        ritona "不管怎么说，想要再见到雷亚的话，立花希这个个体就不得不从现在的世界线上消失。"
        ritona "她之所以会选择离开也是不想让你为难。"
        ritona "毕竟她也知道你拼命想要找回的人，同时也是赋予她生命的存在。"
        me01 "可即使是这样，我却还是搞砸了。"
        me01 "这样的我怎么还有脸面去面对翔子、面对雷亚。"
        me01 "怎么还有脸......去面对立花老师。"
        show ritona b1 fb2 fa5 fc12
        ritona "我说你好歹是个男孩子，也是时候坚强点面对现实了吧。"
        me01 "......可是。"
        ritona "......"
        show ritona b1 fb4 fa3 fc01
        ritona "啊啊！真拿你没办法。"
        ritona "我怎么就碰上了你这么个不争气的家伙啊。"
        ritona "本来还想着让你替我拯救世界......咳咳。"
        show ritona b3 fb1 fa5 fc02 s
        ritona "总之先跟我来吧。"
        me01 "......去哪？"
        show ritona b4 fb1 fa9 fc01
        ritona "你不是想要改变这一切吗？"
        ritona "唯独这一次，说什么也要帮你战胜命运。"
        me01 "芙兰小姐你果然，是个大好人啊......"
        show ritona b3 fb1 fa0 fc02
        window mode thought
        "角色「雷亚」和「立花希」离开队伍。"
        window mode thought
        "想要夺回与她们的羁绊，就去时空之境接受试炼吧。"
        window mode thought
        "同时永远不要忘记，无论何时请珍惜身边重要之人。"
        $ flcam.stop()
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
        $ seen_day224_ritroom = True
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
            sleep jump day224.sleep_memory
            shop jump day224.shop
            member jump day224.stats
            teleport jump day224.teleport
            callback jump day224.callback
            roleroom jump day224.roleroom
            memory jump day224.memory


label day224.callback:
    default seen_day224_callback = False
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

    if not seen_day224_callback:
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
        show ritona b9 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)
        window mode thought
        ritona "当前可抽取的角色包括[can_get_roles_1]"
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

        $ seen_day224_callback = True
    
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
                    jump day224.ritroom
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
                    jump day224.ritroom
            "下次一定":
                window mode thgouth
                me01 "相遇即是缘，请好好珍惜这份来之不易的羁绊。"
                pause 0.5 hard
                $ window_animate_outro()
                stop movie
                hide movie
                stop music fadeout 1.0
                $ _skipping = True
                jump day224.ritroom


label day224.memory:
    if not seen_day224_memory_space:
        ritona "相遇即是缘分，这里就是记录着人们命运的时空之境。"
        ritona "过去与未来，一切的可能性汇聚成了复杂的世界系统。"
        ritona "能否在纷杂的世界线中找到那份遗失的羁绊，此刻也只能赌上一切去换取那不到1%的可能性。"
        $ seen_day224_memory_space = True
    else:
        pass

    menu:
        "雷亚篇":
            if not seen_day224_lst_memory:
                stop music fadeout 5.0
                stop ambience1 fadeout 3.0
                jump battle_lst_memory_day224
            else:
                ritona "恭喜你完成了试炼，守住了自己的珍贵羁绊。"
        "立花希篇":
            if not seen_day224_lhx_memory:
                stop music fadeout 5.0
                stop ambience1 fadeout 3.0
                jump battle_lhx_memory_day224
            else:
                ritona "恭喜你完成了试炼，守住了自己的珍贵羁绊。"
        "取消":
            jump investigate

    jump day224.ritroom


label day224.shop:
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
    jump day224.ritroom


label day224.stats:
    hide screen investigation_popup
    
    python:
        for role in local_config.party:
            role.hp = role.max_hp + role.extend_max_hp
            role.mp = role.max_mp
    $ local_config.current_mode == "Consumables"
    $ local_config.current_actor = local_config.party[0]

    call screen stats
    jump investigate


label day224.roleroom:
    hide screen investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)

    python:
        local_config.start_init(local_config.player, local_config.party)
        local_config.next_story = "day224.ritroom"
    
    call info


label day224.teleport:
    hide screen investigation_popup

    python:
        current_message = ""
        
    call screen teleporter("224")
    jump investigate


label day224.sleep_memory:
    menu:
        "结束梦境":
            if not seen_day224_lst_memory:
                window mode thought
                me01 "先去时空之境试炼拯救「雷亚」吧。"
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

    $ renpy.block_rollback()
    $ _rollback = True

    jump day225
