 
label winter_special_battle(ally_environment_effects, enemy_environment_effects, order_members):
    python:
        xfe_in_flag = any(role.name == "希菲尔" for role in local_config.enemy[:3])

    # 我方前9个回合正常战斗；now winter_status is 0
    if (ally_turns <= 9) and (not xfe_in_flag):
        return
    elif xfe_in_flag and winter_status == 0:
        $ winter_status = 1

    # 我方第10回合之后，
    # 时空扭曲结界干扰使得敌方角色属性加强，攻击提升30%，暴击率提升20%，暴击伤害提升40%，速度提升20
    if winter_status == 0:
        call expression "winter_final_battle_step0"
        $ winter_status = 1
        
        python:
            for role in local_config.party:
                if role.hp > 0:
                    # 清除所有增益效果
                    buffs = copy(role.buff)
                    for buff_name in buffs:
                        if buff_name not in ["love", "ghost_mask", "god", "curse", "soul_lock", "star_bridge", "star_bridge_done", "heart_main", "heart"]:
                            buff_obj = getattr(store, buff_name)
                            buff_obj.calculate(role, ally_environment_effects, None, None, "clean")

            for role in local_config.enemy:
                if role.hp > 0:
                    # 攻击提升30%
                    buff_obj = getattr(store, "strong_enemy")
                    item = (99, 0.3)
                    buff_obj.calculate(role, None, item, "winter_story", "get")
                    # 暴击率提升20%，暴击伤害提升40%
                    buff_obj = getattr(store, "violence_enemy")
                    item = (99, (0.2, 0.4))
                    buff_obj.calculate(role, None, item, "winter_story", "get")
                    # 速度提升20
                    buff_obj = getattr(store, "flow_enemy")
                    item = (99, 20)
                    buff_obj.calculate(role, None, item, "winter_story", "get")
    elif winter_status == 1:
        # 如果希菲尔出场，我方所有技能被封印
        if xfe_in_flag:
            # 眼狩令剧情
            call expression "winter_final_battle_step1"
            
            python:
                local_config.enemy[0].xposition = 0.12
                local_config.enemy[1].xposition = 0.35
                local_config.enemy[2].xposition = 0.58
                if local_config.enemy[0].hp > 0:
                    renpy.show(local_config.enemy[0].objectname, at_list=[show_enemy(local_config.enemy[0].xposition)])
                if local_config.enemy[1].hp > 0:
                    renpy.show(local_config.enemy[1].objectname, at_list=[show_enemy(local_config.enemy[1].xposition)])
                if local_config.enemy[2].hp > 0:
                    renpy.show(local_config.enemy[2].objectname, at_list=[show_enemy(local_config.enemy[2].xposition)])
                order_members.update()
                
            show bottom_black onlayer fg zorder -1 at gui_dissolve_bottom:
                yalign 1.0
            if "healing" in win_condition:
                show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
            else:
                show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")

            $ local_config.tutorial_step = "winter_loss_stage"
            $ extend_turns = 12
            $ winter_status = 2

            python:
                # 我方所有技能被封印
                for role in local_config.party:
                    for s in role.skills:
                        if s.category != "Recharge":
                            s.selectable = False
                            if s.category == "Passive" and (s.name, True) in ally_environment_effects:
                                ally_environment_effects.remove((s.name, True))
                                ally_environment_effects.add((s.name, False))
                    for s in role.skills_v2:
                        if s.category != "Recharge":
                            s.selectable = False
                            if s.category == "Passive" and (s.name, True) in ally_environment_effects:
                                ally_environment_effects.remove((s.name, True))
                                ally_environment_effects.add((s.name, False))

                # 敌方全体复活
                for role in local_config.enemy:
                    role.hp = role.battle_max_hp
                    role.reborn_calculate(enemy_environment_effects)

                    # 攻击提升30%
                    buff_obj = getattr(store, "strong_enemy")
                    item = (99, 0.3)
                    buff_obj.calculate(role, None, item, "winter_story", "get")
                    # 暴击率提升20%，暴击伤害提升40%
                    buff_obj = getattr(store, "violence_enemy")
                    item = (99, (0.2, 0.4))
                    buff_obj.calculate(role, None, item, "winter_story", "get")
                    # 速度提升20
                    buff_obj = getattr(store, "flow_enemy")
                    item = (99, 20)
                    buff_obj.calculate(role, None, item, "winter_story", "get")
    elif winter_status == 2:
        if extend_turns == 0:
            # 他们的愿望
            call expression "winter_final_battle_step2"

            python:
                local_config.enemy[0].xposition = 0.12
                local_config.enemy[1].xposition = 0.35
                local_config.enemy[2].xposition = 0.58
                if local_config.enemy[0].hp > 0:
                    renpy.show(local_config.enemy[0].objectname, at_list=[show_enemy(local_config.enemy[0].xposition)])
                if local_config.enemy[1].hp > 0:
                    renpy.show(local_config.enemy[1].objectname, at_list=[show_enemy(local_config.enemy[1].xposition)])
                if local_config.enemy[2].hp > 0:
                    renpy.show(local_config.enemy[2].objectname, at_list=[show_enemy(local_config.enemy[2].xposition)])
                order_members.update()

            show bottom_black onlayer fg zorder -1 at gui_dissolve_bottom:
                yalign 1.0
            if "healing" in win_condition:
                show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
            else:
                show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")

            $ local_config.tutorial_step = ""
            $ winter_status = 3

            python:
                # 我方解除技能封印，清除所有的减益效果并恢复血量和能量，并获得属性提升
                for role in local_config.party:
                    for s in role.skills:
                        s.selectable = True
                        if s.category == "Passive" and (s.name, False) in ally_environment_effects:
                            ally_environment_effects.remove((s.name, False))
                            ally_environment_effects.add((s.name, True))
                    if len(role.skills_v2) > 0:
                        for s in role.skills_v2:
                            s.selectable = True
                            if s.category == "Passive" and (s.name, False) in ally_environment_effects:
                                ally_environment_effects.remove((s.name, False))
                                ally_environment_effects.add((s.name, True))
                    
                    debuffs = copy(role.debuff)
                    for buff_name in debuffs:
                        buff_obj = getattr(store, buff_name)
                        if buff_obj.removeable:
                            buff_obj.calculate(role, ally_environment_effects, None, None, "clean")

                    role.hp = role.battle_max_hp
                    role.mp = role.max_mp

                    # 攻击提升50%
                    buff_obj = getattr(store, "strong_ally")
                    item = (99, 0.5)
                    buff_obj.calculate(role, None, item, "winter_story", "get")
                    # 暴击率提升30%，暴击伤害提升60%
                    buff_obj = getattr(store, "violence_ally")
                    item = (99, (0.3, 0.6))
                    buff_obj.calculate(role, None, item, "winter_story", "get")
                    # 速度提升40
                    buff_obj = getattr(store, "flow_ally")
                    item = (99, 40)
                    buff_obj.calculate(role, None, item, "winter_story", "get")
                    
                    if "Soul" in role.abilities and role.soulraise == 1:
                        buff = getattr(store, "god")
                        item = (99, 1.0)
                        buff.calculate(role, None, item, "ability-Soul", "get")
                        role.soulraise = 0

                # 敌方属性提升失效
                for role in local_config.enemy:
                    for buff_name in ["strong_enemy", "violence_enemy", "flow_enemy"]:
                        buff_obj = getattr(store, buff_name)
                        buff_obj.calculate(role, None, None, None, "clean")
    return


label battle(boss, boss_hp_plus, side_enemy, side_hp_plus=0, level=None, boss_first=False, win_condition='normal', stay_turn=0, inside_label=None, mission_type="normal", treasures=None):
    # 参数说明
    # params: boss | 战斗的boss单位
    # params: side_enemy | 战斗的非boss单位
    # params: level | 平均等级
    # params: boss_first | boss在最后出场或是先出场
    # params: win_condition | 胜利条件（normal、stay、must_lose、winter_special、protect_stay、protect、healing_role）
    # params: stay_turn | 拖延战回合数
    # params: inside_label | 剧情内对话label
    # params: mission_type | 副本战斗类型（普通剧情战、金币副本、经验副本、突破材料副本、装备副本、卡牌副本）
    # params: treasures | 战斗掉落物（装备、金币掉落倍数、经验书、升星素材、元素卡牌）；数据样式：{名称: (最大数量，概率边界【按照从小到大排列】)}
    window hide

    python:
        config.skipping = None
        _rollback = False
        
        # 战斗参数初始化
        local_config.battle_params_reset()
        # 我方角色战斗临时属性初始化
        for role in local_config.party:
            role.mirror_params()
        
        if level == -1:
            boss.max_hp += boss_hp_plus
            boss.hp = boss.max_hp
            for role in side_enemy:
                role.max_hp += side_hp_plus
                role.hp = role.max_hp
            if boss_first:
                local_config.enemy = [boss] + side_enemy
            else:
                local_config.enemy = side_enemy + [boss]
        else:
            # 敌方角色等级属性设定
            if side_enemy and not isinstance(side_enemy, list):
                side_enemy = [side_enemy]
            for role in side_enemy:
                # 必输剧情
                if win_condition == "must_lose":
                    enemy_level = level + 5
                    role.stats_check(to_level=enemy_level, limit=False)
                    role.max_hp += side_hp_plus
                    role.hp = role.max_hp
                # 正常战斗、持久战
                else:
                    role.stats_check(to_level=level, limit=False)
                    role.max_hp += side_hp_plus
                    role.hp = role.max_hp
                local_config.enemy.append(role)
            if boss and not isinstance(boss, list):
                boss = [boss]
            for role in boss:
                # 必输剧情
                if win_condition == "must_lose":
                    enemy_level = level + 10
                    role.stats_check(to_level=enemy_level, limit=False)
                    role.max_hp += boss_hp_plus
                    role.hp = role.max_hp
                # 正常战斗、持久战
                else:
                    role.stats_check(to_level=level, limit=False)
                    role.max_hp += boss_hp_plus
                    role.hp = role.max_hp
                if boss_first:
                    local_config.enemy.insert(1, role)
                else:
                    local_config.enemy.append(role)

        # 敌方角色战斗临时属性初始化
        for role in local_config.enemy:
            role.mirror_params()

        if "healing" in win_condition:
            healing_selected_role = getattr(store, win_condition.split("healing_")[1].split("_light")[0])
            healing_selected_role.mirror_params()

        # 战斗角色初始化
        for role in local_config.party + local_config.enemy:
            role.hp = role.battle_max_hp
            # buff来源初始化
            local_config.buff_source[role.objectname] = {buff.objectname: set() for buff in buff_list}
            # MP初始化
            if win_condition != "battle_tutorial":
                role.mp = int(role.max_mp * 0.5)
            else:
                role.mp = 0
            # 技能选择初始化
            role.selected_skill = role.skills[0] if len(role.skills) > 0 else None
            # 角色表情初始化
            role.face_change()

        # 我方行动角色、敌方目标角色默认
        local_config.active_actor = local_config.party[0]
        local_config.partytarget = local_config.enemy[0]
        
        # 敌方前排角色初始化
        # 预加载敌方前排角色的模型的缓存
        if len(local_config.enemy) == 1:
            local_config.enemy[0].xposition = 0.35
            renpy.show(local_config.enemy[0].objectname, at_list=[show_enemy(local_config.enemy[0].xposition)])
        if len(local_config.enemy) == 2:
            local_config.enemy[0].xposition = 0.2
            local_config.enemy[1].xposition = 0.5
            renpy.show(local_config.enemy[0].objectname, at_list=[show_enemy(local_config.enemy[0].xposition)])
            renpy.show(local_config.enemy[1].objectname, at_list=[show_enemy(local_config.enemy[1].xposition)])
        elif len(local_config.enemy) > 2:
            local_config.enemy[0].xposition = 0.12
            local_config.enemy[1].xposition = 0.35
            local_config.enemy[2].xposition = 0.58
            renpy.show(local_config.enemy[0].objectname, at_list=[show_enemy(local_config.enemy[0].xposition)])
            renpy.show(local_config.enemy[1].objectname, at_list=[show_enemy(local_config.enemy[1].xposition)])
            renpy.show(local_config.enemy[2].objectname, at_list=[show_enemy(local_config.enemy[2].xposition)])
        
        # 行动条初始化
        for member in local_config.party[:3] + local_config.enemy[:3]:
            member.order = max(member.battle_speed, 1) + renpy.random.random()
        order_members = OrderBar(name="battle_bar", 
                                 max_length=6, 
                                 roles=local_config.party[:3] + local_config.enemy[:3])
        order_members.create()

        extend_turns = None
        if win_condition == "stay":
            enemy_turns = 0
            extend_turns = stay_turn - enemy_turns
        elif local_config.tutorial_step == "lhx_mana_error_winter_216":
            extend_turns = 5
        elif local_config.tutorial_step == "liuli_day219":
            extend_turns = 5

    show bottom_black onlayer fg zorder -1 at gui_dissolve_bottom:
        yalign 1.0
    # 显示界面（行动条+状态栏）
    if "healing" in win_condition:
        show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
    else:
        show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")
    
    $ local_config.in_battle = True
    $ persistent.in_battle = True
    
    # 插入剧情
    if inside_label is not None:
        call expression inside_label pass (enemy_list=local_config.enemy)
    
    # -----------战斗开始-----------
    # 战斗局部变量定义
    $ ally_turns = 0                     # 我方总行动次数
    if win_condition != "stay":
        $ enemy_turns = 0                # 敌方总行动次数
    $ battle_result = None               # 战斗结果
    if win_condition == "winter_special":
        $ winter_status = 0              # 冬の篇决战判定系数
    $ ally_environment_effects = set()   # 我方全局环境效果参数
    $ enemy_environment_effects = set()  # 敌方全局环境效果参数

    $ temp_local_defance_bonus = 0       # 特殊全局加成数记录
    $ ally_love_signal = False           # 我方羁绊之誓印记
    $ tutorial_final_turn = 0

    $ healing_damage = 200              # 保护友加战斗时的间接伤害数值
    if local_config.tutorial_step == "liuli_day219":
        $ liuli_buff_counts = [0.7, 0.4, 0.1]
        $ liuli_fire_phase = False

    # 全局环境效果参数初始化：技能、装备4件套、魔导力回路
    # 先机技能判定区：天赋、技能、装备4件套
    python:
        ## 全局环境效果
        # 被动技能
        for role in local_config.party[:3]:
            passive_skill = [s for s in role.skills if s.category == "Passive"]
            if len(passive_skill) > 0:
                passive_skill = passive_skill[0]
                ally_environment_effects.add((passive_skill.name, passive_skill.selectable))
        for role in local_config.enemy[:3]:
            passive_skill = [s for s in role.skills if s.category == "Passive"]
            if len(passive_skill) > 0:
                passive_skill = passive_skill[0]
                enemy_environment_effects.add((passive_skill.name, passive_skill.selectable))

        # 装备4件套
        for role in local_config.party[:3]:
            ally_environment_effects.add((role.equip4effect, role.equip4effect_availabel))
        for role in local_config.enemy[:3]:
            enemy_environment_effects.add((role.equip4effect, role.equip4effect_availabel))
        
        ## 先机
        # 天赋-灵魂、宁静
        for role in local_config.party + local_config.enemy:
            if "Soul" in role.abilities:
                buff = getattr(store, "god")
                item = (99, 1.0)
                buff.calculate(role, None, item, "ability-Soul", "get")
            if "Serenity" in role.abilities:
                role.battle_effect_resistance += 0.2
        # 装备4件套-风之陨-松吹
        has_ally_wind_equip4effect = False
        for role in local_config.party:
            if role.equip4effect == "风之陨-松吹":
                has_ally_wind_equip4effect = True
        has_enemy_wind_equip4effect = False
        for role in local_config.enemy:
            if role.equip4effect == "风之陨-松吹":
                has_enemy_wind_equip4effect = True
        if has_ally_wind_equip4effect:
            for role in local_config.party:
                buff = getattr(store, "sp_shield")
                item = (1, (int(0.12 * role.battle_max_hp), "physical", 0.75, 0.5))
                buff.calculate(role, None, item, "风之陨-松吹", "get")
        if has_enemy_wind_equip4effect:
            for role in local_config.enemy:
                buff = getattr(store, "sp_shield")
                item = (1, (int(0.12 * role.battle_max_hp), "physical", 0.75, 0.5))
                buff.calculate(role, None, item, "风之陨-松吹", "get")
        # 月之华-琼勾
        for role in local_config.party[3:]:
            if role.equip4effect == "月之华-琼勾":
                ally_environment_effects.add((role.equip4effect, role.equip4effect_availabel))
        for role in local_config.enemy[3:]:
            if role.equip4effect == "月之华-琼勾":
                enemy_environment_effects.add((role.equip4effect, role.equip4effect_availabel))
        # 技能
        for role in local_config.party + local_config.enemy:
            skill_lists = role.skills if not role.is_phase2 else role.skills_v2
            # 空间跳跃
            if "lst_breakout_1" in [s.objectname for s in skill_lists]:
                # 永久提升60点速度
                role.battle_speed += 60
                lst_breakout = [s for s in skill_lists if s.name == "空间跳跃"][0]
                if lst_breakout.level == 5:
                    temp_battlespeed = persistent.battlespeed
                    persistent.battlespeed = 0.2

                    if role in local_config.party:
                        renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                        renpy.pause(0.25 * persistent.battlespeed)
                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("先机", style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 【先机】：施放“空间跳跃”
                        lst_breakout.use(user=role, target=local_config.enemy[0], party=local_config.party, enemy=local_config.enemy, sudden_attack=False, support=False, ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, order_members=order_members, role_now_stats="normal")
                        renpy.pause(0.25)
                        renpy.hide("buff_effect", layer="screens")
                        renpy.hide(role.objectname, layer="fg")
                    elif role in local_config.enemy:
                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("先机", style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)
                        renpy.hide("buff_effect", layer="screens")
                        
                        # 【先机】：施放“空间跳跃”
                        lst_breakout.use(user=role, target=local_config.party[0], party=local_config.enemy, enemy=local_config.party, sudden_attack=False, support=False, ally_environment_effects=enemy_environment_effects, enemy_environment_effects=ally_environment_effects, order_members=order_members, role_now_stats="normal")
                        renpy.pause(0.25)
                    persistent.battlespeed = temp_battlespeed
            # 积重鬼怨
            qcls_skill_obj = getattr(store, "qcls_passive")
            our_qcls_skill = [s for s in skill_lists if s.name == qcls_skill_obj.name]
            if len(our_qcls_skill) > 0:
                our_qcls_skill = our_qcls_skill[0]
                if our_qcls_skill.level == 5:
                    if role in local_config.party:
                        renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                        renpy.pause(0.25 * persistent.battlespeed)
                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("先机", style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)
                        renpy.hide("buff_effect", layer="screens")
                        renpy.hide(role.objectname, layer="fg")
                    elif role in local_config.enemy:
                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("先机", style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)
                        renpy.hide("buff_effect", layer="screens")
                    # 战斗开始时获得6层“鬼面”（鬼面上限为9层）
                    buff_obj = getattr(store, "ghost_mask")
                    item = (99, 7)
                    buff_obj.calculate(role, None, item, "积重鬼怨", "get")
            # 微量化改造：天空开始下起皑皑白雪，战斗开始时为场上的所有敌方角色附加1层冰元素附着
            xfe_breakout_skill = getattr(store, "xfe_breakout")
            if xfe_breakout_skill in skill_lists and (role in local_config.party[:3] or role in local_config.enemy[:3]):
                if role in local_config.party:
                    renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                    renpy.pause(0.25 * persistent.battlespeed)
                    renpy.music.play("raged", channel="battle_music")
                    renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("驻场先机", style="effect_text", color="ff9"))
                    renpy.pause(0.75 * persistent.battlespeed)
                    renpy.hide("buff_effect", layer="screens")
                    renpy.hide(role.objectname, layer="fg")
                elif role in local_config.enemy:
                    renpy.music.play("raged", channel="battle_music")
                    renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("驻场先机", style="effect_text", color="ff9"))
                    renpy.pause(0.75 * persistent.battlespeed)
                    renpy.hide("buff_effect", layer="screens")
                renpy.show("snow_level1", layer="fg_f")
                if role in local_config.party:
                    for role2 in local_config.enemy:
                        if role2.hp > 0:
                            role2.ebuff = {"ice": 1}
                elif role in local_config.enemy:
                    for role2 in local_config.party:
                        if role2.hp > 0:
                            role2.ebuff = {"ice": 1}
            # 白色永恒
            if role.name == "希菲尔":
                if role in local_config.party:
                    buff_roles = local_config.skill_log_data.setdefault("白色永恒", {})
                elif role in local_config.enemy:
                    buff_roles = local_config.skill_log_data.setdefault("白色永恒", {})
            # 波纹裂隙
            ycxt_passive_skill = getattr(store, "ycxt_passive")
            if ycxt_passive_skill.objectname in [s.objectname for s in skill_lists]:
                if role in local_config.party:
                    renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                    renpy.pause(0.25 * persistent.battlespeed)
                    renpy.music.play("raged", channel="battle_music")
                    renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("先机", style="effect_text", color="ff9"))
                    renpy.pause(0.75 * persistent.battlespeed)
                    renpy.hide("buff_effect", layer="screens")
                    renpy.hide(role.objectname, layer="fg")
                    for role_ally in local_config.party:
                        if role_ally.hp > 0:
                            role_ally.mp += 20
                            if role_ally.mp > role_ally.max_mp:
                                role_ally.mp = role_ally.max_mp
                elif role in local_config.enemy:
                    renpy.music.play("raged", channel="battle_music")
                    renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("先机", style="effect_text", color="ff9"))
                    renpy.pause(0.75 * persistent.battlespeed)
                    renpy.hide("buff_effect", layer="screens")
                    for role_enemy in local_config.enemy:
                        if role_enemy.hp > 0:
                            role_enemy.mp += 20
                            if role_enemy.mp > role_enemy.max_mp:
                                role_enemy.mp = role_enemy.max_mp
        ## 环境变量
        # 猎杀之印
        if "protect" in win_condition:
            protect_role_name = win_condition.split("_")[-1]
            protect_role = getattr(store, protect_role_name + "_role")

            # 角色获得守护buff
            buff_obj = getattr(store, "protect")
            item = (99, None)
            buff_obj.calculate(protect_role, None, item, "猎杀之印", "get")
        # 迅捷之影
        if local_config.tutorial_step == "迅捷之影":
            for role in local_config.enemy:
                role.skills = [s if s.category != "Recharge" else getattr(store, "guard_spt") for s in role.skills]
                role.skills_v2 = [s if s.category != "Recharge" else getattr(store, "guard_spt") for s in role.skills_v2]
        # 阴燃之火
        if "fire" in win_condition:
            # 敌方角色的火元素抗性大幅提升
            for role in local_config.enemy:
                role.battle_fire_elemental_resistance += 0.6
            # 我方所有角色获得40%|20%水元素伤害加成
            for role in local_config.party:
                if persistent.difficult == "hard":
                    role.battle_water_damage_bonus += 0.4
                elif persistent.difficult == "abyss":
                    role.battle_water_damage_bonus += 0.2
        # 嗜能之雷
        if "light" in win_condition:
            # 敌方角色的雷元素抗性大幅提升
            for role in local_config.enemy:
                role.battle_light_elemental_resistance += 0.6
            # 我方所有角色获得40%|20%冰元素伤害加成
            for role in local_config.party:
                if persistent.difficult == "hard":
                    role.battle_ice_damage_bonus += 0.4
                elif persistent.difficult == "abyss":
                    role.battle_ice_damage_bonus += 0.2
        # 迟滞之水
        if "water" in win_condition:
            # 敌方角色的水元素抗性大幅提升
            for role in local_config.enemy:
                role.battle_water_elemental_resistance += 0.6
            # 我方所有角色获得40%|20%雷元素伤害加成
            for role in local_config.party:
                if persistent.difficult == "hard":
                    role.battle_light_damage_bonus += 0.4
                elif persistent.difficult == "abyss":
                    role.battle_light_damage_bonus += 0.2
        # 凝结之冰
        if "ice" in win_condition:
            # 敌方角色的冰元素抗性大幅提升
            for role in local_config.enemy:
                role.battle_ice_elemental_resistance += 0.6
            # 我方所有角色获得40%|20%火元素伤害加成
            for role in local_config.party:
                if persistent.difficult == "hard":
                    role.battle_fire_damage_bonus += 0.4
                elif persistent.difficult == "abyss":
                    role.battle_fire_damage_bonus += 0.2
        # 坚毅之岩
        if "rock" in win_condition:
            # 敌方角色的物理、岩元素抗性大幅提升
            for role in local_config.enemy:
                role.battle_rock_elemental_resistance += 0.6
                role.battle_physical_elemental_resistance += 0.6
            # 我方所有角色获得40%|20%火、雷、水、冰、风元素伤害加成
            for role in local_config.party:
                if persistent.difficult == "hard":
                    role.battle_fire_damage_bonus += 0.4
                    role.battle_light_damage_bonus += 0.4
                    role.battle_water_damage_bonus += 0.4
                    role.battle_ice_damage_bonus += 0.4
                    role.battle_wind_damage_bonus += 0.4
                elif persistent.difficult == "abyss":
                    role.battle_fire_damage_bonus += 0.2
                    role.battle_light_damage_bonus += 0.2
                    role.battle_water_damage_bonus += 0.2
                    role.battle_ice_damage_bonus += 0.2
                    role.battle_wind_damage_bonus += 0.2
        # 济世之风
        if "wind" in win_condition:
            # 敌方角色的火、雷、水、冰、风元素抗性大幅提升
            for role in local_config.enemy:
                role.battle_fire_elemental_resistance += 0.6
                role.battle_light_elemental_resistance += 0.6
                role.battle_water_elemental_resistance += 0.6
                role.battle_ice_elemental_resistance += 0.6
                role.battle_wind_elemental_resistance += 0.6
            # 我方所有角色获得40%|20%物理、岩元素伤害加成
            for role in local_config.party:
                if persistent.difficult == "hard":
                    role.battle_physical_damage_bonus += 0.4
                    role.battle_rock_damage_bonus += 0.4
                elif persistent.difficult == "abyss":
                    role.battle_physical_damage_bonus += 0.2
                    role.battle_rock_damage_bonus += 0.2
        # 冬之章最终战
        if win_condition == "winter_special":
            for role in local_config.party:
                # 50%防御加成
                role.battle_extend_defance += 0.5 * role.battle_defance
                # 8000点生命值加成
                role.battle_max_hp += 8000
                role.hp = role.battle_max_hp
        # 瓦轮刑部
        if local_config.tutorial_step == "瓦轮刑部":
            # 敌方全体获得“固若金汤”
            buff_obj = getattr(store, "rock_wall")
            item = (99, 0.9)
            for role in local_config.enemy:
                buff_obj.calculate(role, None, item, "瓦轮刑部", "get")
        # 巫女神乐
        if "enemy_protect" in local_config.tutorial_step:
            protect_role_objname = local_config.tutorial_step.split("enemy_protect_")[1]
            for role in local_config.enemy:
                if role.objectname == protect_role_objname:
                    buff_obj = getattr(store, "sp_protect")
                    item = (99, None)
                    buff_obj.calculate(role, None, item, "巫女神乐", "get")
                    break
        # 虚无封印
        if local_config.tutorial_step == "虚无封印":
            for role in local_config.enemy:
                buff_obj = getattr(store, "sp_protect")
                item = (99, None)
                buff_obj.calculate(role, None, item, "妄想颠覆", "get")
        # 妄想颠覆
        if local_config.tutorial_step == "lhx_mana_error_winter_216":
            for role in local_config.party + local_config.enemy:
                role.battle_wind_damage_bonus += 0.6
        if local_config.tutorial_step == "shield_buff_217":
            for role in local_config.enemy:
                if role.name == "水之濑凛":
                    role.battle_ice_elemental_resistance -= 0.4
                    break

        if "healing" in win_condition:
            local_config.skill_log_data["伤害记录"] = 0.0

        # 先机计算界面参数，初始化行动条
        order_members.update()

    # 显示界面（行动条+状态栏）
    if "healing" in win_condition:
        show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
    else:
        show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")

    while True:
        $ config.allow_skipping = True
        
        # 特殊规则执行区域
        ## 拉锯战获胜方式
        if win_condition == "stay" and enemy_turns >= stay_turn:
            $ battle_result = "win"
            python:
                for effect in media_skill_effect:
                    renpy.hide(effect.vfx, layer="screens")
            $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)
        ## 冬の篇最终战役判定方式
        if win_condition == "winter_special":
            call winter_special_battle(ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, order_members=order_members)
        ## 教学获胜方式
        if win_condition == "battle_tutorial" and (len(local_config.total_tutorial_flags) == 0 or local_config.total_tutorial_flags == ["support"]) and "eggs" not in local_config.player.items:
            $ battle_result = "win"
            python:
                for effect in media_skill_effect:
                    renpy.hide(effect.vfx, layer="screens")
            $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)

        # （结束点）如果检测到战斗结束，则返回战斗结果
        if battle_result is not None:
            return battle_result

        # 获取行动条最顶端角色（行动角色）
        python:
            # 取得行动条最顶端的角色
            local_config.active_actor = order_members.get_real_role()
            # MP修正
            for role in local_config.party + local_config.enemy:
                if role.mp > role.max_mp:
                    role.mp = role.max_mp

        # 如果角色达到行动条件
        if local_config.active_actor.hp > 0 and local_config.active_actor.order >= 1000:
            $ qcls_buff_roles = None
            $ role_now_stats = "normal"
            # 透支计算清空
            $ local_config.spi_mp_cost = 0
            # 松吹判定重置
            $ local_config.skill_log_data["风之陨-松吹"] = {}

            # 特效预加载
            python:
                if local_config.active_actor.name == "千川老师":
                    renpy.start_predict("images/虚无/mask_top.png")
                    for number in range(1, 9):
                        renpy.start_predict("images/虚无/mask_{}.png".format(str(number)))

            # 角色状态特效
            $ media_skill_effect = []
            $ already_shown = False
            # 回合开始前角色动态判定区
            python:
                # 不可攻略（藤原瞳）：生命比例每降低25%，则提升50点防御力
                if tyt_role in local_config.party and ("不可攻略", True) in ally_environment_effects:
                    hp_ratio = math.floor(((tyt_role.battle_max_hp - tyt_role.hp) / tyt_role.battle_max_hp) / 0.25)
                    # 数值回硕
                    tyt_role.battle_extend_defance -= temp_local_defance_bonus
                    # 记录本次加成数
                    temp_local_defance_bonus = hp_ratio * 50
                    # 动态数值加成
                    tyt_role.battle_extend_defance += temp_local_defance_bonus
                # 恢复天赋：当角色HP低于上限的20%，每次行动前恢复生命上限8%的HP和10点MP
                if "Recovery" in local_config.active_actor.abilities and local_config.active_actor in local_config.party and local_config.active_actor.hp > 0 and local_config.active_actor.hp < local_config.active_actor.battle_max_hp * 0.2:
                    # 显示人物
                    if local_config.active_actor in local_config.party and local_config.shown_actor is not None and local_config.shown_actor != local_config.active_actor:
                        renpy.hide(local_config.shown_actor.objectname, layer="fg")
                        renpy.pause(0.25)
                        renpy.show(local_config.active_actor.objectname, at_list=[show_player(local_config.active_actor.xposition)], layer="fg")
                        local_config.shown_actor = local_config.active_actor
                        already_shown = True

                    renpy.show("damage", at_list=[show_damage(local_config.active_actor.xposition, 0.5)], layer="screens", what=Text("+%s" % int(local_config.active_actor.battle_max_hp * 0.08), style="damage_text", size=100, color="#2f0"))
                    renpy.pause(0.5 * persistent.battlespeed)
                    renpy.hide("damage", layer="screens")

                    local_config.active_actor.hp += int(local_config.active_actor.battle_max_hp * 0.08)
                    if local_config.active_actor.hp > local_config.active_actor.battle_max_hp:
                        local_config.active_actor.hp = local_config.active_actor.battle_max_hp

                    renpy.show("damage", at_list=[show_damage(local_config.active_actor.xposition, 0.5)], layer="screens", what=Text("+10", style="damage_text", size=100, color="#19f"))
                    renpy.pause(0.5 * persistent.battlespeed)
                    renpy.hide("damage", layer="screens")

                    local_config.active_actor.mp += 10
                    if local_config.active_actor.mp > local_config.active_actor.max_mp:
                        local_config.active_actor.mp = local_config.active_actor.max_mp
                        
            # 我方行动回合
            if local_config.active_actor in local_config.party[:3]:
                # HP/MP教学
                if win_condition == "battle_tutorial":
                    if local_config.active_actor.moveable:
                        if ally_turns == tutorial_final_turn + 0:
                            $ local_config.total_tutorial_flags.remove("HP/MP")
                            call tutorial_step1
                            $ local_config.total_tutorial_flags.remove("general_skill")
                            $ local_config.tutorial_step = "general_skill"
                            "现在请选择普攻(General Attack)对敌方发起攻击。"
                        elif ally_turns == tutorial_final_turn + 1:
                            $ local_config.tutorial_step = "general_skill"
                        elif ally_turns == tutorial_final_turn + 2:
                            $ local_config.total_tutorial_flags.remove("guard_skill")
                            call tutorial_step2
                            $ local_config.tutorial_step = "guard_skill"
                            "现在请选择充能(Recharge)技能进行能量恢复。"
                        elif ally_turns == tutorial_final_turn + 3:
                            $ local_config.tutorial_step = "guard_skill"
                        elif ally_turns == tutorial_final_turn + 4:
                            $ local_config.total_tutorial_flags.remove("combat_breakout_skill")
                            call tutorial_step3
                            $ local_config.tutorial_step = "combat_skill"
                            "现在请选择元素战技或元素爆发。"
                    else:
                        $ tutorial_final_turn += 1
                    
                    python:
                        for role in local_config.party:
                            if local_config.active_actor.moveable and role.hp <= 0.75 * role.battle_max_hp:
                                renpy.show_screen("investigation_popup", string=investigation.preg5)
                                local_config.total_tutorial_flags.remove("item_use")
                                local_config.tutorial_step = "item_use"
                                renpy.call("tutorial_step6")

                $ media_flag = False     # 技能释放计算中间判定参数
                $ local_config.current_actor = local_config.active_actor
                # 我方行动次数加1
                $ ally_turns += 1

                python:
                    local_config.active_actor.selected_skill = local_config.active_actor.skills[0]
                    # 显示人物
                    if not already_shown:
                        if local_config.active_actor == local_config.shown_actor:
                            renpy.show(local_config.active_actor.objectname, at_list=[hide_out], layer="fg")
                        else:
                            if local_config.shown_actor and local_config.shown_actor.hp > 0:
                                renpy.hide(local_config.shown_actor.objectname, layer="fg")
                                renpy.pause(0.25)
                            renpy.show(local_config.active_actor.objectname, at_list=[show_player(local_config.active_actor.xposition)], layer="fg")
                            local_config.shown_actor = local_config.active_actor
                
                # 更新血条和行动条
                if "healing" in win_condition:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
                else:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")
                
                python:
                    ## 行动前判定（技能特效、间接伤害、眩晕、冻结、沉睡、混乱、嘲讽）
                    ## 全局技能特效判定
                    # 魂之殇
                    if local_config.active_actor.name == "立花希" and "魂之殇" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["魂之殇"]
                        # 获取判定“殇魂”
                        temp_buff_roles = None
                        debuff_target = None
                        fake_buff_roles = copy(buff_roles)
                        for (u, t) in fake_buff_roles:
                            if u == local_config.active_actor:
                                temp_buff_roles = buff_roles.pop((u, t))
                                debuff_target = t
                        if temp_buff_roles is not None:
                            renpy.show("skillname", at_list=[show_skill], layer="screens", what=Text("魂之殇", style="skill_text"))
                            # 清空“殇魂”debuff
                            buff_obj = getattr(store, "desoul_lock")
                            buff_obj.calculate(debuff_target, None, None, None, "clean")

                            lhx_combat_skill = [s for s in local_config.active_actor.skills if s.category == "Combat_skills"][0]

                            # 为所有角色回复生命比例
                            for role, (dmg, dtype) in temp_buff_roles.items():
                                if 0 < role.hp / role.battle_max_hp < dmg:
                                    back_hp = int(role.battle_max_hp * dmg)
                                    if back_hp - role.hp > int(local_config.active_actor.battle_max_hp * 0.25) and lhx_combat_skill.level == 1:
                                        role.hp += int(local_config.active_actor.battle_max_hp * 0.25)
                                    elif back_hp - role.hp > int(local_config.active_actor.battle_max_hp * 0.25) and lhx_combat_skill.level == 2:
                                        role.hp += int(local_config.active_actor.battle_max_hp * 0.25)
                                    elif back_hp - role.hp > int(local_config.active_actor.battle_max_hp * 0.35) and lhx_combat_skill.level == 3:
                                        role.hp += int(local_config.active_actor.battle_max_hp * 0.35)
                                    elif back_hp - role.hp > int(local_config.active_actor.battle_max_hp * 0.45) and lhx_combat_skill.level == 4:
                                        role.hp += int(local_config.active_actor.battle_max_hp * 0.45)
                                    elif back_hp - role.hp > int(local_config.active_actor.battle_max_hp * 0.55) and lhx_combat_skill.level == 5:
                                        role.hp += int(local_config.active_actor.battle_max_hp * 0.55)
                                    else:
                                        role.hp = int(role.battle_max_hp * dmg)
                                if role.hp > role.battle_max_hp:
                                    role.hp = role.battle_max_hp
                                # 为角色清空“殇魂”buff
                                buff_obj = getattr(store, "soul_lock")
                                buff_obj.calculate(role, None, None, None, "clean")
                        if len(local_config.skill_log_data["魂之殇"]) == 0:
                            local_config.skill_log_data.pop("魂之殇")
                    # 白色永恒
                    if ("白色永恒", True) in ally_environment_effects and "白色永恒" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["白色永恒"]
                        random_signal = renpy.random.randint(1, 4)

                        calculate_xfe_role = None
                        for role in local_config.party[:3]:
                            if role.name == "希菲尔":
                                calculate_xfe_role = role
                                break

                        if calculate_xfe_role is not None:
                            temp_selected_skills = calculate_xfe_role.base_skills if not calculate_xfe_role.is_phase2 else calculate_xfe_role.base_skills_v2
                            fake_xfe_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]

                            # 第一次获得印记
                            if "ally" not in buff_roles:
                                local_config.skill_log_data["白色永恒"]["ally"] = (random_signal, fake_xfe_passive, False)
                            else:
                                lasttime_signal, fake_xfe_passive, flag = buff_roles["ally"]
                                buff_times = 0
                                if "love" in calculate_xfe_role.buff:
                                    dtime, buff_times = calculate_xfe_role.buff["love"]
                                # 命中
                                if buff_times != 9 and lasttime_signal == random_signal:
                                    renpy.music.play("结缘", channel="battle_music")
                                    renpy.pause(0.05)

                                    # 立刻恢复自身10|20|20|20|20点MP值并在回合结束前的战斗计算阶段提升20%暴击伤害，与此同时“希菲尔”将获得1层“羁绊之誓”
                                    if fake_xfe_passive.level in [2, 3, 4, 5]:
                                        local_config.active_actor.mp += 20
                                    else:
                                        local_config.active_actor.mp += 10
                                    if local_config.active_actor.mp > local_config.active_actor.max_mp:
                                        local_config.active_actor.mp = local_config.active_actor.max_mp

                                    local_config.skill_log_data["白色永恒"]["ally"] = (random_signal, fake_xfe_passive, True)
                                    # 希菲尔获得1层“羁绊之誓”
                                    if fake_xfe_passive.level in [3, 4, 5]:
                                        renpy.show("get_love_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=3.5, xpos=calculate_xfe_role.xposition, ypos=0.45)], layer="screens")
                                        renpy.pause(0.84 * persistent.battlespeed)
                                        renpy.hide("get_love_img", layer="screens")

                                        buff_obj = getattr(store, "love")
                                        item = (99, 1)
                                        buff_obj.calculate(calculate_xfe_role, None, item, "白色永恒", "get")

                                        if "love" in calculate_xfe_role.buff:
                                            dtime, buff_times = calculate_xfe_role.buff["love"]

                                            if (fake_xfe_passive.level == 3 and buff_times == 3) or (fake_xfe_passive.level == 4 and buff_times in [3, 6]) or (fake_xfe_passive.level == 5 and buff_times in [3, 6, 9]):
                                                if buff_times != 9:
                                                    renpy.music.play("喜提良缘", channel="battle_music")
                                                    renpy.pause(0.05)
                                                    if local_config.active_actor != calculate_xfe_role:
                                                        renpy.hide(local_config.active_actor.objectname, layer="fg")
                                                        renpy.show(calculate_xfe_role.objectname, at_list=[show_player(calculate_xfe_role.xposition)], layer="fg")
                                                        renpy.pause(0.5 * persistent.battlespeed)

                                                # 祛除自身所有减益、控制效果和元素附着，并击退敌方全体25%行动条
                                                if buff_times == 3:
                                                    renpy.show("buff_effect", at_list=[show_state(calculate_xfe_role.xposition)], layer="screens", what=Text("喜提良缘", style="effect_text", color="ff9"))
                                                    renpy.show("get_middle_love_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=3.5, xpos=calculate_xfe_role.xposition, ypos=0.45)], layer="screens")
                                                    renpy.pause(0.96 * persistent.battlespeed)
                                                    renpy.hide("get_middle_love_img", layer="screens")
                                                    renpy.hide("buff_effect", layer="screens")

                                                    debuffs = copy(calculate_xfe_role.debuff)
                                                    for buff_name in debuffs:
                                                        buff_obj = getattr(store, buff_name)
                                                        if buff_obj.removeable or buff_name in ["dizziness", "deep_sleepy"]:
                                                            buff_obj.calculate(calculate_xfe_role, ally_environment_effects, None, None, "clean")
                                                    calculate_xfe_role.ebuff = {}
                                                    
                                                    for role in local_config.enemy[:3]:
                                                        if role.hp > 0:
                                                            renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("行动推后", style="effect_text", color="ff9"))
                                                            renpy.pause(0.5 * persistent.battlespeed)
                                                            role.order -= 250
                                                # 为我方全体恢复生命上限20%的生命值并提升40%攻击，持续1回合
                                                elif buff_times == 6:
                                                    renpy.show("buff_effect", at_list=[show_state(calculate_xfe_role.xposition)], layer="screens", what=Text("喜提良缘", style="effect_text", color="ff9"))
                                                    renpy.show("get_middle_love_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=3.5, xpos=calculate_xfe_role.xposition, ypos=0.45)], layer="screens")
                                                    renpy.pause(0.96 * persistent.battlespeed)
                                                    renpy.hide("get_middle_love_img", layer="screens")
                                                    renpy.hide("buff_effect", layer="screens")

                                                    shown_actor = calculate_xfe_role
                                                    for role in local_config.party[:3]:
                                                        if role.hp > 0:
                                                            if role != shown_actor:
                                                                renpy.hide(shown_actor.objectname, layer="fg")
                                                                renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                                                renpy.pause(0.5 * persistent.battlespeed)

                                                            renpy.music.play("恢复", channel="battle_music")
                                                            renpy.pause(0.05)
                                                            renpy.show("damage", at_list=[show_damage(role.xposition, 0.5)], layer="screens", what=Text("+%s" % int(role.battle_max_hp * 0.2), style="damage_text", size=100, color="#2f0"))
                                                            renpy.pause(0.5 * persistent.battlespeed)
                                                            role.hp += int(role.battle_max_hp * 0.2)
                                                            if role.hp > role.battle_max_hp:
                                                                role.hp = role.battle_max_hp

                                                            renpy.music.play("加成", channel="battle_music")
                                                            renpy.pause(0.05)
                                                            renpy.show("damage_up_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=1.5, xpos=role.xposition, ypos=0.4)], layer="screens")
                                                            renpy.pause(1.35 * persistent.battlespeed)
                                                            renpy.hide("damage_up_img", layer="screens")
                                                            
                                                            buff_obj = getattr(store, "strong")
                                                            item = (1, 0.4)
                                                            buff_obj.calculate(role, None, item, "白色永恒-结缘6", "get")
                                                            shown_actor = role
                                                    if shown_actor != local_config.active_actor:
                                                        renpy.hide(shown_actor.objectname, layer="fg")
                                                        renpy.show(local_config.active_actor.objectname, at_list=[show_player(local_config.active_actor.xposition)], layer="fg")
                                                        renpy.pause(0.5 * persistent.battlespeed)

                                                    if ally_love_signal:
                                                        buff_obj = getattr(store, "love")
                                                        buff_obj.calculate(calculate_xfe_role, None, None, None, "clean")
                                                # 技能“芬布尔之冬”替换为“樱雪同梦”
                                                elif buff_times == 9 and not ally_love_signal:
                                                    renpy.music.play("最终缘毕", channel="battle_music")
                                                    renpy.pause(0.5 * persistent.battlespeed)
                                                    renpy.transition(Dissolve(1.0, alpha=True), layer="screens", always=True)
                                                    renpy.show("black", layer="screens")
                                                    renpy.pause(0.75 * persistent.battlespeed)
                                                    renpy.show("get_final_love_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=1.8, xalign=0.5, yalign=0.45)], layer="screens")
                                                    renpy.pause(2.7)
                                                    renpy.transition(Dissolve(1.0, alpha=True), layer="screens", always=True)
                                                    renpy.hide("get_final_love_img", layer="screens")
                                                    renpy.pause(0.75)
                                                    renpy.hide("black", layer="screens")
                                                    renpy.pause(0.5 * persistent.battlespeed)

                                                    calculate_xfe_role.is_phase2 = True
                                                    ally_love_signal = True

                                                renpy.hide("buff_effect", layer="screens")
                                                if local_config.active_actor != calculate_xfe_role:
                                                    renpy.hide(calculate_xfe_role.objectname, layer="fg")
                                                    renpy.show(local_config.active_actor.objectname, at_list=[show_player(local_config.active_actor.xposition)], layer="fg")
                                # 未命中
                                else:
                                    local_config.skill_log_data["白色永恒"]["ally"] = (random_signal, fake_xfe_passive, False)

                    # 嗜能之雷
                    if "light" in win_condition and "light" in local_config.active_actor.ebuff:
                        light_name, light_times = local_config.active_actor.ebuff["light"]
                        local_config.active_actor.mp -= 5 * light_times
                        if local_config.active_actor.mp < 0:
                            local_config.active_actor.mp = 0
                    # 迟滞之水
                    if "water" in win_condition and "water" in local_config.active_actor.ebuff:
                        water_name, water_times = local_config.active_actor.ebuff["water"]
                        buff_obj = getattr(store, "slow")
                        item = (2, 5 * water_times)
                        buff_obj.calculate(local_config.active_actor, None, item, "迟滞之水", "get")
                        buff_obj = getattr(store, "disintegrate")
                        item = (2, 0.1 * water_times)
                        buff_obj.calculate(local_config.active_actor, None, item, "迟滞之水", "get")
                    # 凝结之冰
                    if "ice" in win_condition and "ice" in local_config.active_actor.ebuff:
                        ice_name, ice_times = local_config.active_actor.ebuff["ice"]
                        if "frozen" not in local_config.active_actor.debuff and "deep_frozen" not in local_config.active_actor.debuff and (0.05 * ice_times) > renpy.random.random():
                            buff_obj = getattr(store, "frozen")
                            item = (1, 0.5)
                            buff_obj.calculate(local_config.active_actor, None, item, "凝结之冰", "get")
                    # 迅捷之影：率先达到10层“义”时，全队所有角色获得100%攻击加成、50%暴击率加成、100%暴击伤害加成和50点速度提升
                    if "yi" in local_config.active_actor.buff:
                        yi_buff_time, yi_buff_effect = local_config.active_actor.buff["yi"]
                        if yi_buff_effect == 10:
                            for role in local_config.party:
                                for buff_name, buff_item in {"strong_speed": (99, 1.0), "violence_speed": (99, (0.5, 1.0)), "flow_speed": (99, 50)}.items():
                                    buff_obj = getattr(store, buff_name)
                                    buff_obj.calculate(role, None, buff_item, "迅捷之影", "get")
                                buff_obj = getattr(store, "yi")
                                buff_obj.calculate(role, None, None, None, "clean")

                    # 间接伤害判定
                    damage_color_map = {
                        "fire": "#f30",
                        "water": "#19f",
                        "light": "#f0f",
                        "ice": "#3ff",
                        "wind": "#6f6",
                        "rock": "#ff0",
                        "physical": "#9cf",
                    }
                    if "mdamage" in local_config.active_actor.debuff:
                        if "间接伤害" in local_config.skill_log_data:
                            buff_roles = local_config.skill_log_data["间接伤害"]
                            if local_config.active_actor in buff_roles:
                                for element, value in buff_roles.items():
                                    damage, element, reason, damage_user = value

                                    renpy.music.play("hit", channel="battle_music")
                                    renpy.pause(0.05)
                                    renpy.show("damage", at_list=[show_damage(local_config.active_actor.xposition, 0.4)], layer="screens", what=Text("%s" % damage, style="damage_text", size=100, color=damage_color_map[element]))

                                    # 受到伤害角色抖动特效
                                    renpy.show(local_config.active_actor.objectname, at_list=[shake, hide_out], layer="fg")
                                    renpy.pause(0.75 * persistent.battlespeed)
                                    
                                    # 队友守护
                                    if "sp_protect" in local_config.active_actor.buff:
                                        renpy.show("critical", at_list=[show_damage(local_config.active_actor.xposition, 0.35)], layer="screens", what=Text("无效", style="effect_text", size=80, color="#ee6"))
                                        if local_config.tutorial_step == "虚无封印":
                                            damage = 1
                                        else:
                                            damage = 0

                                    local_config.active_actor.hp -= damage
                                    if local_config.active_actor.hp < 0:
                                        local_config.active_actor.hp = 0

                                    # 唤醒沉睡状态
                                    if "sleepy" in local_config.active_actor.debuff:
                                        buff_obj = getattr(store, "sleepy")
                                        buff_obj.calculate(local_config.active_actor, None, None, None, "clean")
                                    # 唤醒深度沉睡
                                    if "deep_sleepy" in local_config.active_actor.debuff and damage >= 0.3 * local_config.active_actor.battle_max_hp:
                                        buff_obj = getattr(store, "deep_sleepy")
                                        buff_obj.calculate(local_config.active_actor, None, None, None, "clean")

                                    # 判断是否还活着
                                    local_config.active_actor.death_calculate(damage_user, None, enemy_environment_effects, ally_environment_effects)
                    # 阴燃之火
                    if "fire" in win_condition and "fire" in local_config.active_actor.ebuff:
                        fire_number = local_config.active_actor.ebuff["fire"]
                        if fire_number >= 5:
                            local_config.active_actor.ebuff = {}
                            damage = int(local_config.active_actor.battle_max_hp * 0.3)

                            renpy.music.play("hit", channel="battle_music")
                            renpy.pause(0.05)
                            renpy.show("damage", at_list=[show_damage(local_config.active_actor.xposition, 0.5)], layer="screens", what=Text("%s" % damage, style="damage_text", size=100, color="#f30"))

                            # 受到伤害角色抖动特效
                            renpy.show(local_config.active_actor.objectname, at_list=[shake, hide_out], layer="fg")
                            renpy.pause(0.75 * persistent.battlespeed)

                            # 队友守护
                            if "sp_protect" in local_config.active_actor.buff:
                                renpy.show("critical", at_list=[show_damage(local_config.active_actor.xposition, 0.35)], layer="screens", what=Text("无效", style="effect_text", size=80, color="#ee6"))
                                if local_config.tutorial_step == "虚无封印":
                                    damage = 1
                                else:
                                    damage = 0

                            local_config.active_actor.hp -= damage
                            if local_config.active_actor.hp < 0:
                                local_config.active_actor.hp = 0

                            # 唤醒沉睡状态
                            if "sleepy" in local_config.active_actor.debuff:
                                buff_obj = getattr(store, "sleepy")
                                buff_obj.calculate(local_config.active_actor, None, None, None, "clean")
                            # 唤醒深度沉睡
                            if "deep_sleepy" in local_config.active_actor.debuff and damage >= 0.3 * local_config.active_actor.battle_max_hp:
                                buff_obj = getattr(store, "deep_sleepy")
                                buff_obj.calculate(local_config.active_actor, None, None, None, "clean")

                            # 判断是否还活着
                            damage_user = [role for role in local_config.enemy if role.hp > 0][0]
                            local_config.active_actor.death_calculate(damage_user, None, enemy_environment_effects, ally_environment_effects)

                    order_members.update()
                $ _rollback = False
                # 更新血条和行动条
                if "healing" in win_condition:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
                else:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")
                
                if local_config.active_actor.hp <= 0:
                    pass
                # 眩晕判定
                elif "dizziness" in local_config.active_actor.debuff:
                    $ role_now_stats = "dizziness"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("眩晕"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                # 冰冻判定
                elif "frozen" in local_config.active_actor.debuff or "deep_frozen" in local_config.active_actor.debuff:
                    $ role_now_stats = "frozen"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("冻结"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                # 沉睡判定
                elif "sleepy" in local_config.active_actor.debuff or "deep_sleepy" in local_config.active_actor.debuff:
                    $ role_now_stats = "sleepy"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("沉睡"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects,  None, None, "end")
                # 混乱判定
                elif "confusion" in local_config.active_actor.debuff:
                    $ role_now_stats = "confusion"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("混乱"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 随机选择攻击目标（排除自己）
                        candidate_targets = [role for role in local_config.party[:3] + local_config.enemy[:3] if role.hp > 0 and role.objectname != local_config.active_actor.objectname]
                        select_target_idx = renpy.random.randint(0, len(candidate_targets) - 1)
                        local_config.active_actor.selected_target = candidate_targets[select_target_idx]
                        # 获取攻击技能（普攻）
                        local_config.active_actor.selected_skill = local_config.active_actor.skill_auto(local_config.active_actor.selected_target, smart=False, confusion=True, cond="tutorial_first" if win_condition == "battle_tutorial" else "")
                        # 如果攻击对象是我方，显示被攻击角色
                        if local_config.active_actor.selected_target in local_config.party:
                            renpy.hide(local_config.active_actor.objectname, layer="fg")
                            renpy.pause(0.25)
                            renpy.show(local_config.active_actor.selected_target.objectname, at_list=[show_player(local_config.active_actor.selected_target.xposition)], layer="fg")
                        # 自动战斗特效选择
                        if config.skipping is None or config.skip_delay > 5:
                            if local_config.active_actor.selected_skill.gfx != "":
                                renpy.start_predict("9i/interface/battle/gfx/{}.png".format(local_config.active_actor.selected_skill.gfx))
                        # 技能使用结算
                        local_config.active_actor.selected_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.party, enemy=local_config.enemy, sudden_attack=False, support=False, ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                        renpy.pause(0.25)
                        # 被攻击后角色换回
                        if local_config.active_actor.selected_target is not None and local_config.active_actor.selected_target in local_config.party and local_config.active_actor.selected_target != local_config.shown_actor:
                            renpy.hide(local_config.active_actor.selected_target.objectname, layer="fg")
                            renpy.pause(0.25)
                            renpy.show(local_config.shown_actor.objectname, at_list=[show_player(local_config.shown_actor.xposition)], layer="fg")

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                # 嘲讽判定
                elif "ridicule" in local_config.active_actor.debuff:
                    $ role_now_stats = "ridicule"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("嘲讽"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 获取攻击技能（普攻）
                        local_config.active_actor.selected_skill = local_config.active_actor.skill_auto(local_config.active_actor.selected_target, smart=False, confusion=True, cond="tutorial_first" if win_condition == "battle_tutorial" else "")
                        # 自动战斗特效选择
                        if config.skipping is None or config.skip_delay > 5:
                            if local_config.active_actor.selected_skill.gfx != "":
                                renpy.start_predict("9i/interface/battle/gfx/{}.png".format(local_config.active_actor.selected_skill.gfx))
                        # 技能使用结算
                        local_config.active_actor.selected_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.party, enemy=local_config.enemy, sudden_attack=False, support=False, ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                        renpy.pause(0.25)

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                # 进入正常战斗操作流程
                else:
                    python:
                        # AI模式自动战斗
                        if local_config.partyaction == "auto":
                            # 指定攻击目标
                            local_config.active_actor.selected_target = local_config.partytarget
                            local_config.active_actor.selected_skill = local_config.active_actor.skill_auto(local_config.active_actor.selected_target, smart=True, confusion=False, cond="tutorial_first" if win_condition == "battle_tutorial" else "")
                        # 技能选择
                        else:
                            if _preferences.skip_after_choices == False:
                                config.skipping = None
                            
                            # 直到选择技能为止一直等待
                            local_config.active_actor.selected_skill = "cancel"
                            while local_config.active_actor.selected_skill == "cancel" or (local_config.active_actor.selected_skill not in ["auto_skill", "call_magic", "change"] and "xfe_breakout" in local_config.active_actor.selected_skill.objectname):
                                # 隐藏菜单界面
                                renpy.hide_screen("tactics_screen")
                                # 返回技能选择界面
                                local_config.active_actor.selected_skill = renpy.call_screen("command_screen", who=local_config.active_actor, enemy=local_config.enemy)

                                # 打开菜单界面
                                if local_config.active_actor.selected_skill == "cancel":
                                    if win_condition == "battle_tutorial" and "item_use" in local_config.total_tutorial_flags:
                                        pass
                                    else:
                                        renpy.hide_screen("investigation_popup")
                                        renpy.hide_screen("command_screen")
                                        renpy.hide_screen("battle_ui", layer="fg")
                                        local_config.active_actor.selected_skill = renpy.call_screen("tactics_screen", party=local_config.party, ally_environment_effects=ally_environment_effects, order_members=order_members)
                                        renpy.pause(0.25)
                                        if "healing" in win_condition:
                                            renpy.show_screen("battle_ui", local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
                                        else:
                                            renpy.show_screen("battle_ui", local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")
                                elif "xfe_breakout" in local_config.active_actor.selected_skill.objectname:
                                    # 能量扣除
                                    if not media_flag:
                                        media_flag = True
                                        local_config.active_actor.mp += local_config.active_actor.selected_skill.mp_cost
                                        if local_config.active_actor.mp < 0:
                                            local_config.active_actor.mp = 0

                                    # 微量化改造
                                    skill_names = ["xfe_breakout_%d" % num for num in range(1, 6)]
                                    select_skill = renpy.call_screen("aerowheel_ingame", skills=[getattr(store, name) for name in skill_names])
                                    temp_selected_skills = local_config.active_actor.base_skills if not local_config.active_actor.is_phase2 else local_config.active_actor.base_skills_v2
                                    fake_xfe_breakout = [s for s in temp_selected_skills if s.category == "Break_out"][0]
                                    for xi in range(fake_xfe_breakout.level - 1):
                                        select_skill.level_change(select_skill.level + 1)
                                    buff_roles = local_config.skill_log_data.setdefault("微量化改造", {})
                                    buff_roles[local_config.active_actor] = (select_skill, fake_xfe_breakout, local_config.active_actor.is_phase2)

                                    # 替换技能
                                    if local_config.active_actor.is_phase2:
                                        skill_lists = copy(local_config.active_actor.skills_v2)
                                        new_skill_lists = [s if s.category != "Break_out" else select_skill for s in skill_lists]
                                        local_config.active_actor.skills_v2 = new_skill_lists
                                    else:
                                        skill_lists = copy(local_config.active_actor.skills)
                                        new_skill_lists = [s if s.category != "Break_out" else select_skill for s in skill_lists]
                                        local_config.active_actor.skills = new_skill_lists

                            # 指定攻击目标
                            local_config.active_actor.selected_target = local_config.partytarget

                        if local_config.active_actor.selected_skill == "auto_skill":
                            local_config.active_actor.selected_skill = local_config.active_actor.skill_auto(local_config.active_actor.selected_target, smart=True, confusion=False, cond="tutorial_first" if win_condition == "battle_tutorial" else "")

                        # 换人操作
                        if local_config.active_actor.selected_skill == "change":
                            renpy.hide(local_config.active_actor.objectname, layer="fg")
                        # 呼叫魔导力回路
                        elif local_config.active_actor.selected_skill == "call_magic":
                            pass
                        # 技能施放
                        else:
                            # 自动战斗特效选择
                            if config.skipping == None or config.skip_delay > 5:
                                if local_config.active_actor.selected_skill.gfx != "":
                                    renpy.start_predict("9i/interface/battle/gfx/{}.png".format(local_config.active_actor.selected_skill.gfx))

                            # 回合计算
                            local_config.active_actor.selected_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.party, enemy=local_config.enemy, sudden_attack=False, support=False, ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                            renpy.pause(0.25)

                            # 不知火
                            # 若自身生命比例低于10%，则额外免能量释放一次“冥火”
                            if local_config.active_actor.selected_skill.name == "不知火" and local_config.active_actor.selected_skill.level == 5 and local_config.active_actor.hp / local_config.active_actor.battle_max_hp < 0.1:
                                extend_skill = getattr(store, "liuli_breakout")
                                extend_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.party, enemy=local_config.enemy, sudden_attack=False, support=True, ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                                renpy.pause(0.25)
                            # 冥火
                            # 若自身生命比例低于10%，则额外免能量释放一次“不知火”
                            elif local_config.active_actor.selected_skill.name == "冥火" and local_config.active_actor.selected_skill.level == 5 and local_config.active_actor.hp / local_config.active_actor.battle_max_hp < 0.1:
                                extend_skill = getattr(store, "liuli_combat")
                                extend_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.party, enemy=local_config.enemy, sudden_attack=False, support=True, ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                                renpy.pause(0.25)

                            # 推条
                            if "群体推条" in local_config.active_actor.selected_skill.effects:
                                ratio, target, time = local_config.active_actor.selected_skill.effects["群体推条"]
                                if ratio > 0.0:
                                    for role in local_config.enemy[:3]:
                                        if role.hp > 0:
                                            role.order -= int(ratio * 1000)
                                            renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("行动推后", style="effect_text", color="ff9"))

                            # buff结算
                            if local_config.active_actor.hp > 0:
                                # 如果是特殊原因获得的buff不加入计算
                                sources2 = None
                                if "Reflexes" in local_config.skill_log_data:
                                    sources2 = local_config.skill_log_data["Reflexes"]
                                cand_buffs = copy(local_config.active_actor.buff)
                                for buff_name in cand_buffs:
                                    # 如果该轮加入自身的buff不加入计算
                                    sources = local_config.buff_source[local_config.active_actor.objectname][buff_name]
                                    if local_config.active_actor.selected_skill.name not in sources:
                                        buff_obj = getattr(store, buff_name)
                                        if sources2 is not None and local_config.active_actor.objectname in sources2:
                                            temp_buff_name = sources2.pop(local_config.active_actor.objectname)
                                            if len(local_config.skill_log_data["Reflexes"]) == 0:
                                                local_config.skill_log_data.pop("Reflexes")
                                            if temp_buff_name != buff_obj:
                                                buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                                        else:
                                            buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                                cand_buffs = copy(local_config.active_actor.debuff)
                                for buff_name in cand_buffs:
                                    buff_obj = getattr(store, buff_name)
                                    if sources2 is not None and local_config.active_actor.objectname in sources2:
                                        temp_buff_name = sources2.pop(local_config.active_actor.objectname)
                                        if len(local_config.skill_log_data["Reflexes"]) == 0:
                                            local_config.skill_log_data.pop("Reflexes")
                                        if temp_buff_name != buff_obj:
                                            buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")
                                    else:
                                        buff_obj.calculate(local_config.active_actor, ally_environment_effects, None, None, "end")

                            renpy.block_rollback()
                            _rollback = True

                            if local_config.active_actor.selected_skill.name == "虚无":
                                # 鬼面加入
                                if "积重鬼怨" in local_config.skill_log_data:
                                    qcls_buff_roles = local_config.skill_log_data["积重鬼怨"]

                    # 面具显示 & 怨恨祛除显示
                    if local_config.active_actor.selected_skill not in ["auto_skill", "call_magic", "change"]:
                        if qcls_buff_roles and "ally" in qcls_buff_roles:
                            # 开启附带9个禁断之面的“封印结界”笼罩对手
                            show set block qcls_skill_enemy:
                                mask_top
                                mask_1
                                mask_2
                                mask_3
                                mask_4
                                mask_5
                                mask_6
                                mask_7
                                mask_8

                            python:
                                # 解除“妄想颠覆”结界
                                for role in local_config.enemy:
                                    if "sp_protect" in role.buff:
                                        buff_obj = getattr(store, "sp_protect")
                                        buff_obj.calculate(role, None, None, None, "clean")
                    
                python:
                    order_members.update()

                $ _rollback = False
                # 更新行动条和血量
                if "healing" in win_condition:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
                else:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")

                python:
                    # 回合结束时触发的判定
                    if "积重鬼怨" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["积重鬼怨"]
                        if "enemy" in buff_roles:
                            buff_roles["enemy"] -= 1
                            # 消除禁断之面
                            face_number = buff_roles["enemy"]
                            if face_number != 0:
                                renpy.hide("qcls_skill_ally-mask_%d" % face_number)
                            else:
                                renpy.hide("qcls_skill_ally-mask_top")
                                buff_roles.pop("enemy")

                            # 解除封印结界
                            if face_number == 0:
                                if len(local_config.skill_log_data["积重鬼怨"]) == 0:
                                    local_config.skill_log_data.pop("积重鬼怨")
                                for role in local_config.party[:3]:
                                    role._special_calculate(enemy_environment_effects=ally_environment_effects, mode="release")
                    # 悉心呵护
                    if ("悉心呵护", True) in ally_environment_effects and "共感" in local_config.skill_log_data and local_config.active_actor.hp > 0:
                        buff_roles = local_config.skill_log_data["共感"]
                        if "ally" in buff_roles:
                            calculate_xz_role = [role for role in local_config.party[:3] if role.name == "青木翔子"]
                            if len(calculate_xz_role) > 0:
                                calculate_xz_role = calculate_xz_role[0]

                                # 附带了“心”状态的友方单位在回合结束时恢复“青木翔子”生命上限8%|8%|8%|12%|12%的生命值，并额外获得效果抵抗和速度提升，持续1回合
                                if local_config.active_actor in buff_roles["ally"]:
                                    renpy.music.play("恢复", channel="battle_music")
                                    renpy.pause(0.05)
                                    renpy.show("healing_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=2.5, xpos=local_config.active_actor.xposition, ypos=0.4)], layer="screens")
                                    renpy.pause(0.96 * persistent.battlespeed)
                                    renpy.hide("healing_img", layer="screens")

                                    temp_selected_skills = calculate_xz_role.base_skills if not calculate_xz_role.is_phase2 else calculate_xz_role.base_skills_v2
                                    calculate_xz_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]
                                    temp_ratio_lists = [0.08, 0.08, 0.08, 0.12, 0.12]
                                    
                                    healing_number_gonggan = int(temp_ratio_lists[calculate_xz_passive.level - 1] * calculate_xz_role.battle_max_hp)
                                    renpy.show("damage", at_list=[show_damage(local_config.active_actor.xposition, 0.5)], layer="screens", what=Text("+%s" % healing_number_gonggan, style="damage_text", size=100, color="#2f0"))
                                    renpy.pause(0.5 * persistent.battlespeed)

                                    local_config.active_actor.hp += healing_number_gonggan
                                    if local_config.active_actor.hp > local_config.active_actor.battle_max_hp:
                                        local_config.active_actor.hp = local_config.active_actor.battle_max_hp
                                    if calculate_xz_passive.level in [2, 3, 4, 5]:
                                        buff_obj = getattr(store, "barrier")
                                        item = (1, 0.3)
                                        buff_obj.calculate(local_config.active_actor, None, item, "悉心呵护", "get")
                                        if calculate_xz_passive.level in [3, 4, 5]:
                                            temp_ratio_lists = [0, 0, 10, 20, 20]
                                            buff_obj = getattr(store, "flow")
                                            item = (1, temp_ratio_lists[calculate_xz_passive.level - 1])
                                            buff_obj.calculate(local_config.active_actor, None, item, "悉心呵护", "get")
                    # 波纹裂隙
                    if local_config.active_actor.name == "一诚小桃" and local_config.active_actor.hp > 0 and any([role.name == "一诚小桃" for role in local_config.party[:3]]) and ("波纹裂隙", True) in ally_environment_effects and ("shield" not in local_config.active_actor.buff and "sp_shield" not in local_config.active_actor.buff):
                        temp_selected_skills = local_config.active_actor.base_skills if not local_config.active_actor.is_phase2 else local_config.active_actor.base_skills_v2
                        fake_ycxt_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]
                        temp_ratio_lists = [0.2, 0.2, 0.25, 0.25, 0.3]
                        if temp_ratio_lists[fake_ycxt_passive.level - 1] > renpy.random.random():
                            ycxt_select_skill = getattr(store, "ycxt_passive_1")
                            for xi in range(fake_ycxt_passive.level - 1):
                                ycxt_select_skill.level_change(ycxt_select_skill.level + 1)
                            local_config.active_actor.battle_calculate(ycxt_select_skill, local_config.active_actor, ally_environment_effects, enemy_environment_effects, order_members, slot_x=None, slot_y=None, support=False)
                            renpy.pause(0.25)
                    # 催眠
                    if "催眠" in local_config.skill_log_data:
                        qcls_buff_roles = local_config.skill_log_data["催眠"]
                        if local_config.active_actor in qcls_buff_roles:
                            time_number = qcls_buff_roles.pop(local_config.active_actor)
                            time_number -= 1
                            # 增益角色在行动结束后进入1回合不可驱散的“深度沉睡”状态
                            if time_number == 0:
                                # 清除霸体效果
                                if "domineering" in local_config.active_actor.buff:
                                    buff_obj = getattr(store, "domineering")
                                    buff_obj.calculate(local_config.active_actor, None, None, None, "clean")
                                # 进入1回合不可驱散的“深度沉睡”状态
                                buff_obj = getattr(store, "deep_sleepy")
                                item = (1, 0.3)
                                buff_obj.calculate(local_config.active_actor, None, item, "催眠", "get")

                                renpy.music.play("poisoned", channel="battle_music")
                                renpy.show("buff_effect", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text("深度睡眠", style="effect_text", color="ff9"))
                            # 施术者回合跳过
                            else:
                                local_config.skill_log_data["催眠"][local_config.active_actor] = time_number
                    # 澎湃天赋效果
                    if local_config.spi_mp_cost > 20:
                        buff = getattr(store, "dizziness")
                        item = (1, None)
                        buff.calculate(local_config.active_actor, None, item, "澎湃", "get")
                        renpy.music.play("poisoned", channel="battle_music")
                        renpy.show("buff_effect", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text("眩晕", style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)
                    # 灵巧天赋效果
                    for role in local_config.enemy[:3]:
                        if role.hp > 0 and not role.moveable and "Flexible" in role.abilities:
                            renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
                            renpy.pause(0.5 * persistent.battlespeed)
                            renpy.hide("buff_effect", layer="screens")
                            role.order += 200
                    # 月之华-琼勾
                    if ("月之华-琼勾", True) in ally_environment_effects:
                        for role in local_config.party[:3]:
                            if role.hp > 0 and not role.moveable:
                                buff_obj = getattr(store, "flow")
                                item = (1, 20)
                                buff_obj.calculate(role, None, item, "月之华-琼勾", "get")
                    # 春之花-仑灵
                    if local_config.active_actor.equip4effect == "春之花-仑灵" and ("春之花-仑灵", True) in ally_environment_effects:
                        if 0.2 > renpy.random.random():
                            for role in local_config.party[:3]:
                                if role.hp > 0:
                                    role.mp += 20

                    # 阴燃之火
                    if "fire" in win_condition:
                        if persistent.difficult == "abyss" and "fire" in local_config.active_actor.ebuff:
                            local_config.active_actor.ebuff["fire"] += 1
                        elif len(local_config.active_actor.ebuff) == 0:
                            local_config.active_actor.ebuff = {"fire": 3}
                    # 嗜能之雷
                    if "light" in win_condition and len(local_config.active_actor.ebuff) == 0:
                        local_config.active_actor.ebuff = {"light": 3}
                    # 迟滞之水
                    if "water" in win_condition and len(local_config.active_actor.ebuff) == 0:
                        local_config.active_actor.ebuff = {"water": 3}
                    # 凝结之冰
                    if "ice" in win_condition and len(local_config.active_actor.ebuff) == 0:
                        local_config.active_actor.ebuff = {"ice": 3}

                    if local_config.tutorial_step in ["liuli_day219", "liuli_day219_onfire"]:
                        if liuli_fire_phase:
                            liuli_temp_role = None
                            for role in local_config.enemy:
                                if role.name == "花山院琉璃":
                                    liuli_temp_role = role
                                    break

                            if liuli_temp_role is not None:
                                if "shield" in role.buff:
                                    extend_turns -= 1
                                    if extend_turns == 0:
                                        # 场上全体友方受到生命上限30%火元素间接伤害（承受伤害的角色生命值不低于1），恢复花山院琉璃10%生命上限的生命值
                                        shown_actor = local_config.active_actor
                                        renpy.music.play("raged", channel="battle_music")
                                        renpy.show("buff_effect", at_list=[show_ability(liuli_temp_role.xposition)], layer="screens", what=Text("超燃过载", style="ability_text"))
                                        renpy.pause(0.5 * persistent.battlespeed)
                                        renpy.hide("buff_effect", layer="screens")

                                        for role in local_config.party[:3]:
                                            if role.hp > 0:
                                                if shown_actor != role:
                                                    renpy.hide(shown_actor.objectname, layer="fg")
                                                    renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                                    renpy.pause(0.5 * persistent.battlespeed)

                                                damage = int(role.battle_max_hp * 0.6)
                                                renpy.music.play("hit", channel="battle_music")
                                                renpy.pause(0.05)
                                                renpy.show("damage", at_list=[show_damage(role.xposition, 0.5)], layer="screens", what=Text("%s" % damage, style="damage_text", size=100, color="#f30"))

                                                # 受到伤害角色抖动特效
                                                renpy.show(role.objectname, at_list=[shake, hide_out], layer="fg")
                                                renpy.pause(0.75 * persistent.battlespeed)

                                                role.hp -= damage
                                                if local_config.active_actor.hp < 0:
                                                    local_config.active_actor.hp = 1

                                                # 唤醒沉睡状态or深度沉睡
                                                if "sleepy" in role.debuff or "deep_sleepy" in role.debuff:
                                                    buff_obj = getattr(store, "sleepy")
                                                    buff_obj.calculate(role, None, None, None, "clean")
                                                shown_actor = role
                                        if shown_actor != local_config.shown_actor:
                                            renpy.hide(shown_actor.objectname, layer="fg")
                                            renpy.show(local_config.shown_actor.objectname, at_list=[show_player(local_config.shown_actor.xposition)], layer="fg")
                                            renpy.pause(0.5 * persistent.battlespeed)
                                        
                                        for role in local_config.enemy:
                                            if role.name == "花山院琉璃":
                                                role.hp += int(role.battle_max_hp * 0.1)
                                                buff_obj = getattr(store, "shield")
                                                buff_obj.calculate(role, None, None, None, "clean")

                                        extend_turns = 5
                                else:
                                    liuli_fire_phase = False
                                    local_config.tutorial_step = "liuli_day219"
                                    extend_turns = 5
                        else:
                            for role in local_config.enemy:
                                if role.name == "花山院琉璃":
                                    for buffc in liuli_buff_counts:
                                        now_hp_ratio = role.hp / role.battle_max_hp
                                        if now_hp_ratio <= buffc:
                                            # 进入「超燃凝聚态」
                                            liuli_fire_phase = True
                                            local_config.tutorial_step = "liuli_day219_onfire"
                                            renpy.show("buff_effect", at_list=[show_ability(role.xposition)], layer="screens", what=Text("超燃凝聚", style="ability_text"))
                                            renpy.pause(0.5 * persistent.battlespeed)
                                            renpy.hide("buff_effect", layer="screens")
                                            # 获得基于攻击力300%的火元素护盾
                                            temp_shield_strength = (role.battle_attack + role.battle_extend_attack) * 3.0
                                            buff_obj = getattr(store, "shield")
                                            item = (1, (int(temp_shield_strength), "fire", 0.75, 0.5))
                                            buff_obj.calculate(role, None, item, "超燃凝聚态", "get")
                                            liuli_buff_counts.remove(buffc)
                                            break

                    if local_config.tutorial_step == "winter_loss_stage":
                        extend_turns -= 1

                    # 表情重置
                    local_config.active_actor.face_change()

                # 循环结束判定：胜利条件
                $ alive_enemy_number = len(local_config.enemy)
                python:
                    for role in local_config.enemy:
                        if role.hp <= 0:
                            alive_enemy_number -= 1

                # 常规获胜方式：全灭敌人
                if alive_enemy_number == 0:
                    $ battle_result = "win"
                    python:
                        for effect in media_skill_effect:
                            renpy.hide(effect.vfx, layer="screens")
                    $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)

                # 循环结束判定：失败条件
                $ alive_party_number = len(local_config.party)
                python:
                    for role in local_config.party:
                        if role.hp <= 0:
                            alive_party_number -= 1

                # 常规失败方式：我方全灭
                if alive_party_number == 0:
                    $ battle_result = "lose"
                    python:
                        for effect in media_skill_effect:
                            renpy.hide(effect.vfx, layer="screens")
                    $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)
                # 保护模式失败方式
                elif "protect" in win_condition:
                    if protect_role.hp <= 0:
                        $ battle_result = "lose"
                        python:
                            for effect in media_skill_effect:
                                renpy.hide(effect.vfx, layer="screens")
                        $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)

                # 主角协战（非自动战斗触发）    
                if local_config.partyaction != "auto" and local_config.active_actor is not None and local_config.active_actor.selected_skill not in ["auto_skill", "call_magic", "change"] and battle_result is None and local_config.active_actor.moveable and local_config.active_actor.selected_target is not None and local_config.active_actor.selected_target.hp > 0:
                    if renpy.random.random() <= local_config.player_join_rate:
                        $ master_skill = renpy.call_screen("aerowheel", who=local_config.player)
                        if "support" in local_config.total_tutorial_flags:
                            $ local_config.total_tutorial_flags.remove("support")
                            call tutorial_step7
                            $ local_config.tutorial_step = "support"

                        python:
                            support(heroine=local_config.active_actor)
                            if master_skill is not None:
                                master_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.party, enemy=local_config.enemy, sudden_attack=False, support=True, ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, order_members=order_members, role_now_stats=role_now_stats)

                        # 循环结束判定：胜利条件
                        $ alive_enemy_number = len(local_config.enemy)
                        python:
                            for role in local_config.enemy:
                                if role.hp <= 0:
                                    alive_enemy_number -= 1

                        # 常规获胜方式：全灭敌人
                        if alive_enemy_number == 0:
                            $ battle_result = "win"
                            python:
                                for effect in media_skill_effect:
                                    renpy.hide(effect.vfx, layer="screens")
                            $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)

                        # 循环结束判定：失败条件
                        $ alive_party_number = len(local_config.party)
                        python:
                            for role in local_config.party:
                                if role.hp <= 0:
                                    alive_party_number -= 1

                        # 常规失败方式：我方全灭
                        if alive_party_number == 0:
                            $ battle_result = "lose"
                            python:
                                for effect in media_skill_effect:
                                    renpy.hide(effect.vfx, layer="screens")
                            $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)

                        # 保护模式失败方式
                        elif "protect" in win_condition:
                            if protect_role.hp <= 0:
                                $ battle_result = "lose"
                                python:
                                    for effect in media_skill_effect:
                                        renpy.hide(effect.vfx, layer="screens")
                                $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)
            # 敌方行动回合
            elif local_config.active_actor in local_config.enemy[:3]:
                # 敌方行动次数加1
                $ enemy_turns += 1
                if win_condition == "stay":
                    $ extend_turns = stay_turn - enemy_turns
                
                python:
                    ## 行动前判定（技能特效、间接伤害、眩晕、冻结、沉睡、混乱、嘲讽）
                    # 迅捷之影：率先达到8层“义”时，全队所有角色获得100%攻击加成、50%暴击率加成、100%暴击伤害加成和50点速度提升
                    if "yi" in local_config.active_actor.buff:
                        yi_buff_time, yi_buff_effect = local_config.active_actor.buff["yi"]
                        if persistent.difficult == "hard":
                            if yi_buff_effect == 10:
                                total_roles = local_config.enemy
                                for role in total_roles:
                                    for buff_name, buff_item in {"strong_speed": (99, 1.0), "violence_speed": (99, (0.5, 1.0)), "flow_speed": (99, 50)}.items():
                                        buff_obj = getattr(store, buff_name)
                                        buff_obj.calculate(role, None, buff_item, "迅捷之影", "get")
                                    buff_obj = getattr(store, "yi")
                                    buff_obj.calculate(role, None, None, None, "clean")
                        elif persistent.difficult == "abyss":
                            if yi_buff_effect == 8:
                                total_roles = local_config.enemy
                                for role in total_roles:
                                    for buff_name, buff_item in {"strong_speed": (99, 1.0), "violence_speed": (99, (0.5, 1.0)), "flow_speed": (99, 50)}.items():
                                        buff_obj = getattr(store, buff_name)
                                        buff_obj.calculate(role, None, buff_item, "迅捷之影", "get")
                                    buff_obj = getattr(store, "yi")
                                    buff_obj.calculate(role, None, None, None, "clean")
                    if local_config.tutorial_step == "shield_buff_217" and local_config.active_actor.name == "水之濑凛":
                        if 0.2 > renpy.random.random():
                            buff_obj = getattr(store, "dizziness")
                            item = (1, None)
                            buff_obj.calculate(local_config.active_actor, None, item, "day217", "get")
                        qcls_flag = False
                        for role in local_config.enemy[:3]:
                            if role.name == "千川老师" and role.hp > 0:
                                qcls_flag = True
                                break
                        if qcls_flag:
                            # 水之濑凛获得自身攻击比例120%雷元素护盾
                            if "shield" in local_config.active_actor.buff:
                                temp_shield_strength = (local_config.active_actor.battle_attack + local_config.active_actor.battle_extend_attack) * 1.2
                                buff_obj = getattr(store, "shield")
                                item = (2, (int(temp_shield_strength), "light", 0.75, 0.5))
                                buff_obj.calculate(local_config.active_actor, None, item, None, "get")
                            else:
                                temp_shield_strength = (local_config.active_actor.battle_attack + local_config.active_actor.battle_extend_attack) * 1.2
                                buff_obj = getattr(store, "shield")
                                item = (2, (int(temp_shield_strength), "light", 0.75, 0.5))
                                buff_obj.calculate(local_config.active_actor, None, item, "千川老师", "get")
                    if local_config.tutorial_step == "liuli_day219" and local_config.active_actor.name == "花山院琉璃":
                        if not liuli_fire_phase:
                            for buffc in liuli_buff_counts:
                                now_hp_ratio = local_config.active_actor.hp / local_config.active_actor.battle_max_hp
                                if now_hp_ratio <= buffc:
                                    # 进入「超燃凝聚态」
                                    liuli_fire_phase = True
                                    local_config.tutorial_step = "liuli_day219_onfire"
                                    renpy.show("buff_effect", at_list=[show_ability(local_config.active_actor.xposition)], layer="screens", what=Text("超燃凝聚", style="ability_text"))
                                    renpy.pause(0.5 * persistent.battlespeed)
                                    renpy.hide("buff_effect", layer="screens")
                                    # 获得基于攻击力300%的火元素护盾
                                    temp_shield_strength = (local_config.active_actor.battle_attack + local_config.active_actor.battle_extend_attack) * 3.0
                                    buff_obj = getattr(store, "shield")
                                    item = (1, (int(temp_shield_strength), "fire", 0.75, 0.5))
                                    buff_obj.calculate(local_config.active_actor, None, item, "超燃凝聚态", "get")
                                    liuli_buff_counts.remove(buffc)
                                    break
                    # 虚无封印
                    if local_config.tutorial_step == "虚无封印":
                        if "积重鬼怨" in local_config.skill_log_data:
                            qcls_buff_roles = local_config.skill_log_data["积重鬼怨"]
                            if "ally" not in qcls_buff_roles:
                                # 重新恢复“妄想颠覆”结界
                                buff_obj = getattr(store, "sp_protect")
                                item = (99, None)
                                buff_obj.calculate(local_config.active_actor, None, item, "妄想颠覆", "get")
                        else:
                            if "sp_protect" not in local_config.active_actor.buff:
                                # 重新恢复“妄想颠覆”结界
                                buff_obj = getattr(store, "sp_protect")
                                item = (99, None)
                                buff_obj.calculate(local_config.active_actor, None, item, "妄想颠覆", "get")
                    ## 被动、全局技能特效判定
                    # 魂之殇
                    if local_config.active_actor.name == "立花希" and "魂之殇" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["魂之殇"]
                        # 获取判定“殇魂”
                        temp_buff_roles = None
                        debuff_target = None
                        fake_buff_roles = copy(buff_roles)
                        for (u, t) in fake_buff_roles:
                            if u == local_config.active_actor:
                                temp_buff_roles = buff_roles.pop((u, t))
                                debuff_target = t
                                break
                        if temp_buff_roles is not None:
                            renpy.show("skillname", at_list=[show_skill(local_config.active_actor.xposition)], layer="screens", what=Text("魂之殇", style="skill_text"))
                            # 清空“殇魂”debuff
                            buff_obj = getattr(store, "desoul_lock")
                            buff_obj.calculate(debuff_target, None, None, None, "clean")

                            lhx_combat_skill = [s for s in local_config.active_actor.skills if s.category == "Combat_skills"][0]

                            # 为所有角色回复生命比例（敌方角色减少为15%）
                            for role, (dmg, dtype) in temp_buff_roles.items():
                                if 0 < role.hp / role.battle_max_hp < dmg:
                                    back_hp = int(role.battle_max_hp * dmg)
                                    if back_hp - role.hp > int(local_config.active_actor.battle_max_hp * 0.15):
                                        role.hp += int(local_config.active_actor.battle_max_hp * 0.15)
                                    else:
                                        role.hp = int(role.battle_max_hp * dmg)
                                if role.hp > role.battle_max_hp:
                                    role.hp = role.battle_max_hp
                                # 为角色清空“殇魂”buff
                                buff_obj = getattr(store, "soul_lock")
                                buff_obj.calculate(role, None, None, None, "clean")
                        if len(local_config.skill_log_data["魂之殇"]) == 0:
                            local_config.skill_log_data.pop("魂之殇")
                    # 白色永恒
                    if ("白色永恒", True) in enemy_environment_effects and "白色永恒" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["白色永恒"]
                        random_signal = renpy.random.randint(1, 4)
                        
                        calculate_xfe_role = None
                        for role in local_config.enemy[:3]:
                            if role.name == "希菲尔":
                                calculate_xfe_role = role
                                break

                        if calculate_xfe_role is not None:
                            temp_selected_skills = calculate_xfe_role.base_skills if not calculate_xfe_role.is_phase2 else calculate_xfe_role.base_skills_v2
                            fake_xfe_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]

                            # 第一次获得印记
                            if "enemy" not in buff_roles:
                                local_config.skill_log_data["白色永恒"]["enemy"] = (random_signal, fake_xfe_passive, False)
                            else:
                                lasttime_signal, fake_xfe_passive, flag = buff_roles["enemy"]
                                # 命中
                                if lasttime_signal == random_signal:
                                    renpy.music.play("结缘", channel="battle_music")
                                    renpy.pause(0.05)

                                    # 立刻恢复自身10|20|20|20|20点MP值并在回合结束前的战斗计算阶段提升20%暴击伤害，与此同时“希菲尔”将获得1层“羁绊之誓”
                                    if fake_xfe_passive.level in [2, 3, 4, 5]:
                                        local_config.active_actor.mp += 20
                                    else:
                                        local_config.active_actor.mp += 10
                                    if local_config.active_actor.mp > local_config.active_actor.max_mp:
                                        local_config.active_actor.mp = local_config.active_actor.max_mp

                                    local_config.skill_log_data["白色永恒"]["enemy"] = (random_signal, fake_xfe_passive, True)
                                    # “希菲尔”将获得1层“羁绊之誓”
                                    if fake_xfe_passive.level in [3, 4, 5]:
                                        renpy.show("get_love_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=3.5, xpos=calculate_xfe_role.xposition, ypos=0.45)], layer="screens")
                                        renpy.pause(0.96 * persistent.battlespeed)
                                        renpy.hide("get_love_img", layer="screens")

                                        buff_obj = getattr(store, "love")
                                        item = (99, 1)
                                        buff_obj.calculate(calculate_xfe_role, None, item, "白色永恒", "get")

                                        if "love" in calculate_xfe_role.buff:
                                            dtime, buff_times = calculate_xfe_role.buff["love"]

                                            if (fake_xfe_passive.level == 3 and buff_times == 3) or (fake_xfe_passive.level == 4 and buff_times in [3, 6]):
                                                renpy.music.play("喜提良缘", channel="battle_music")
                                                renpy.pause(0.05)
                                                renpy.show("buff_effect", at_list=[show_state(calculate_xfe_role.xposition)], layer="screens", what=Text("喜提良缘", style="effect_text", color="ff9"))
                                                renpy.show("get_middle_love_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=3.5, xpos=calculate_xfe_role.xposition, ypos=0.45)], layer="screens")
                                                renpy.pause(0.84 * persistent.battlespeed)
                                                renpy.hide("get_middle_love_img", layer="screens")
                                                renpy.hide("buff_effect", layer="screens")
                                                
                                                # 祛除自身所有减益、控制效果和元素附着，并击退敌方全体25%行动条
                                                if buff_times == 3:
                                                    debuffs = copy(calculate_xfe_role.debuff)
                                                    for buff_name in debuffs:
                                                        buff_obj = getattr(store, buff_name)
                                                        if buff_obj.removeable or buff_name in ["dizziness", "deep_sleepy"]:
                                                            buff_obj.calculate(calculate_xfe_role, ally_environment_effects, None, None, "clean")
                                                    calculate_xfe_role.ebuff = {}

                                                    shown_actor = local_config.shown_actor
                                                    for role in local_config.party[:3]:
                                                        if role.hp > 0:
                                                            if shown_actor != role:
                                                                renpy.hide(shown_actor.objectname, layer="fg")
                                                                renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                                                renpy.pause(0.5 * persistent.battlespeed)
                                                            renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("行动推后", style="effect_text", color="ff9"))
                                                            renpy.pause(0.5 * persistent.battlespeed)
                                                            role.order -= 250
                                                            shown_actor = role
                                                    if shown_actor != local_config.shown_actor:
                                                        renpy.hide(shown_actor.objectname, layer="fg")
                                                        renpy.show(local_config.shown_actor.objectname, at_list=[show_player(local_config.shown_actor.xposition)], layer="fg")
                                                        renpy.pause(0.5 * persistent.battlespeed)
                                                # 为我方全体恢复生命上限20%的生命值并提升40%攻击，持续1回合
                                                elif buff_times == 6:
                                                    for role in local_config.enemy[:3]:
                                                        if role.hp > 0:
                                                            renpy.music.play("恢复", channel="battle_music")
                                                            renpy.pause(0.05)
                                                            renpy.show("damage", at_list=[show_damage(role.xposition, 0.5)], layer="screens", what=Text("+%s" % int(role.battle_max_hp * 0.2), style="damage_text", size=100, color="#2f0"))
                                                            renpy.pause(0.5 * persistent.battlespeed)
                                                            role.hp += int(role.battle_max_hp * 0.2)
                                                            if role.hp > role.battle_max_hp:
                                                                role.hp = role.battle_max_hp

                                                            renpy.music.play("加成", channel="battle_music")
                                                            renpy.pause(0.05)
                                                            renpy.show("damage_up_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=1.5, xpos=role.xposition, ypos=0.4)], layer="screens")
                                                            renpy.pause(1.35 * persistent.battlespeed)
                                                            renpy.hide("damage_up_img", layer="screens")

                                                            buff_obj = getattr(store, "strong")
                                                            item = (1, 0.4)
                                                            buff_obj.calculate(role, None, item, "白色永恒-结缘6", "get")
                                                    buff_obj = getattr(store, "love")
                                                    buff_obj.calculate(calculate_xfe_role, None, None, None, "clean")
                                                renpy.hide("buff_effect", layer="screens")
                                    # 未命中
                                    else:
                                        local_config.skill_log_data["白色永恒"]["enemy"] = (random_signal, fake_xfe_passive, False)

                    # 间接伤害判定
                    if "mdamage" in local_config.active_actor.debuff:
                        damage_color_map = {
                            "fire": "#f30",
                            "water": "#19f",
                            "light": "#f0f",
                            "ice": "#3ff",
                            "wind": "#6f6",
                            "rock": "#ff0",
                            "physical": "#9cf",
                        }

                        if "间接伤害" in local_config.skill_log_data:
                            buff_roles = local_config.skill_log_data["间接伤害"]
                            if local_config.active_actor in buff_roles:
                                for element, value in buff_roles.items():
                                    damage, element, reason, damage_user = value
                                
                                    renpy.music.play("hit", channel="battle_music")
                                    renpy.pause(0.05)
                                    renpy.show("damage", at_list=[show_damage(local_config.active_actor.xposition, 0.4)], layer="screens", what=Text("%s" % damage, style="damage_text", size=100, color=damage_color_map[element]))

                                    # 受到伤害角色抖动特效
                                    renpy.show(local_config.active_actor.objectname, at_list=[smallshake])
                                    renpy.pause(0.75 * persistent.battlespeed)
                                    
                                    if "伤害记录" in local_config.skill_log_data:
                                        local_config.skill_log_data["伤害记录"] += damage
                                        healing_selected_role.hp += damage
                                        if healing_selected_role.hp > healing_selected_role.battle_max_hp:
                                            healing_selected_role.hp = healing_selected_role.battle_max_hp
                                    
                                    # 队友守护
                                    if "sp_protect" in local_config.active_actor.buff:
                                        renpy.show("critical", at_list=[show_damage(local_config.active_actor.xposition, 0.35)], layer="screens", what=Text("无效", style="effect_text", size=80, color="#ee6"))
                                        if local_config.tutorial_step == "虚无封印":
                                            damage = 1
                                        else:
                                            damage = 0

                                    local_config.active_actor.hp -= damage
                                    if local_config.active_actor.hp < 0:
                                        local_config.active_actor.hp = 0

                                    # 唤醒沉睡状态
                                    if "sleepy" in local_config.active_actor.debuff:
                                        buff_obj = getattr(store, "sleepy")
                                        buff_obj.calculate(local_config.active_actor, None, None, None, "clean")
                                    # 唤醒深度沉睡
                                    if "deep_sleepy" in local_config.active_actor.debuff and damage >= 0.3 * local_config.active_actor.battle_max_hp:
                                        buff_obj = getattr(store, "deep_sleepy")
                                        buff_obj.calculate(local_config.active_actor, None, None, None, "clean")

                                    # 判断是否还活着
                                    local_config.active_actor.death_calculate(damage_user, None, ally_environment_effects, enemy_environment_effects)
                
                python:
                    order_members.update()

                $ _rollback = False
                # 更新血条和行动条
                if "healing" in win_condition:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
                else:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")
                
                # 超燃凝聚态
                if (local_config.active_actor.hp <= 0) or (local_config.tutorial_step == "liuli_day219_onfire"):
                    pass
                # 眩晕判定
                elif "dizziness" in local_config.active_actor.debuff:
                    $ role_now_stats = "dizziness"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("眩晕"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                # 冰冻判定
                elif "frozen" in local_config.active_actor.debuff or "deep_frozen" in local_config.active_actor.debuff:
                    $ role_now_stats = "frozen"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("冻结"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                # 沉睡判定
                elif "sleepy" in local_config.active_actor.debuff or "deep_sleepy" in local_config.active_actor.debuff:
                    $ role_now_stats = "sleepy"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("沉睡"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                # 混乱判定
                elif "confusion" in local_config.active_actor.debuff:
                    $ role_now_stats = "confusion"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition, 0.05)], layer="screens", what=Text(_("混乱"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 随机选择攻击目标
                        candidate_targets = [role for role in local_config.party[:3] + local_config.enemy[:3] if role.hp > 0 and role.objectname != local_config.active_actor.objectname]
                        select_target_idx = renpy.random.randint(0, len(candidate_targets) - 1)
                        local_config.active_actor.selected_target = candidate_targets[select_target_idx]
                        # 获取攻击技能（普攻）
                        local_config.active_actor.selected_skill = local_config.active_actor.skill_auto(local_config.active_actor.selected_target, smart=False, confusion=True, cond="tutorial_first" if win_condition == "battle_tutorial" else "")
                        # 如果攻击对象是我方，显示被攻击角色
                        if local_config.active_actor.selected_target in local_config.party:
                            if local_config.shown_actor != local_config.active_actor.selected_target:
                                renpy.hide(local_config.shown_actor.objectname, layer="fg")
                                renpy.pause(0.25)
                                renpy.show(local_config.active_actor.selected_target.objectname, at_list=[show_player(local_config.active_actor.selected_target.xposition)], layer="fg")
                        # 自动战斗特效选择
                        if config.skipping is None or config.skip_delay > 5:
                            if local_config.active_actor.selected_skill.gfx != "":
                                renpy.start_predict("9i/interface/battle/gfx/{}.png".format(local_config.active_actor.selected_skill.gfx))
                        # 技能使用结算
                        local_config.active_actor.selected_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.enemy, enemy=local_config.party, sudden_attack=False, support=False, ally_environment_effects=enemy_environment_effects, enemy_environment_effects=ally_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                        renpy.pause(0.25)
                        # 被攻击角色换回
                        if local_config.active_actor.selected_target is not None and local_config.active_actor.selected_target in local_config.party and local_config.active_actor.selected_target != local_config.shown_actor:
                            renpy.hide(local_config.active_actor.selected_target.objectname, layer="fg")
                            renpy.pause(0.25)
                            renpy.show(local_config.shown_actor.objectname, at_list=[show_player(local_config.shown_actor.xposition)], layer="fg")

                        # buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                # 嘲讽判定
                elif "ridicule" in local_config.active_actor.debuff:
                    $ role_now_stats = "ridicule"
                    python:
                        if persistent.skip_inserts == None:
                            config.allow_skipping = False
                        elif persistent.skip_inserts == False:
                            config.skipping = None

                        renpy.music.play("raged", channel="battle_music")
                        renpy.show("flow", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text(_("嘲讽"), style="effect_text", color="ff9"))
                        renpy.pause(0.75 * persistent.battlespeed)

                        # 获取攻击技能（普攻）
                        local_config.active_actor.selected_skill = local_config.active_actor.skill_auto(local_config.active_actor.selected_target, smart=False, confusion=True, cond="tutorial_first" if win_condition == "battle_tutorial" else "")
                        # 如果攻击对象是我方，显示被攻击角色
                        if local_config.active_actor.selected_target in local_config.party:
                            if local_config.shown_actor != local_config.active_actor.selected_target:
                                renpy.hide(local_config.shown_actor.objectname, layer="fg")
                                renpy.pause(0.25)
                                renpy.show(local_config.active_actor.selected_target.objectname, at_list=[show_player(local_config.active_actor.selected_target.xposition)], layer="fg")
                        # 自动战斗特效选择
                        if config.skipping is None or config.skip_delay > 5:
                            if local_config.active_actor.selected_skill.gfx != "":
                                renpy.start_predict("9i/interface/battle/gfx/{}.png".format(local_config.active_actor.selected_skill.gfx))
                        # 技能使用结算
                        local_config.active_actor.selected_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.enemy, enemy=local_config.party, sudden_attack=False, support=False, ally_environment_effects=enemy_environment_effects, enemy_environment_effects=ally_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                        renpy.pause(0.25)
                        # 被攻击角色换回
                        if local_config.active_actor.selected_target != local_config.shown_actor:
                            renpy.hide(local_config.active_actor.selected_target.objectname, layer="fg")
                            renpy.pause(0.25)
                            renpy.show(local_config.shown_actor.objectname, at_list=[show_player(local_config.shown_actor.xposition)], layer="fg")

                        # 行动结束后buff结算
                        if local_config.active_actor.hp > 0:
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                # 进入正常战斗操作流程
                else:
                    python:
                        # 指定攻击目标
                        # 强制锁定守护角色
                        if local_config.tutorial_step == "猎杀之印" and "game_" in win_condition and "protect" in win_condition:
                            if persistent.difficult == "hard" and 0.5 > renpy.random.random():
                                for prole in local_config.party[:3]:
                                    if prole.hp > 0 and "protect" in prole.buff:
                                        local_config.active_actor.selected_target = prole
                                        break
                            elif persistent.difficult == "abyss":
                                for prole in local_config.party[:3]:
                                    if prole.hp > 0 and "protect" in prole.buff:
                                        local_config.active_actor.selected_target = prole
                                        break
                            else:
                                target_list = local_config.party[:3]
                                choice_target = None
                                while choice_target is None:
                                    target_idx = renpy.random.randint(0, len(target_list) - 1)
                                    temp_choice_target = target_list[target_idx]
                                    if temp_choice_target.hp > 0:
                                        choice_target = temp_choice_target
                                local_config.active_actor.selected_target = choice_target
                        else:
                            target_list = local_config.party[:3]
                            choice_target = None
                            while choice_target is None:
                                target_idx = renpy.random.randint(0, len(target_list) - 1)
                                temp_choice_target = target_list[target_idx]
                                if temp_choice_target.hp > 0:
                                    choice_target = temp_choice_target
                            local_config.active_actor.selected_target = choice_target

                        # AI模式技能选择
                        local_config.active_actor.selected_skill = local_config.active_actor.skill_auto(local_config.active_actor.selected_target, smart=True, confusion=False, cond="tutorial_first" if win_condition == "battle_tutorial" else "")

                        # 显示我方技能作用对象
                        if local_config.active_actor.selected_target != local_config.shown_actor:
                            if local_config.shown_actor:
                                renpy.hide(local_config.shown_actor.objectname, layer="fg")
                                renpy.pause(0.25)
                            renpy.show(local_config.active_actor.selected_target.objectname, at_list=[show_player(local_config.active_actor.selected_target.xposition)], layer="fg")
                            local_config.shown_actor = local_config.active_actor.selected_target
                      
                        # 自动战斗特效选择
                        if config.skipping == None or config.skip_delay > 5:
                            if local_config.active_actor.selected_skill.gfx != "":
                                renpy.start_predict("9i/interface/battle/gfx/{}.png".format(local_config.active_actor.selected_skill.gfx))

                        # 回合计算
                        local_config.active_actor.selected_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.enemy, enemy=local_config.party, sudden_attack=False, support=False, ally_environment_effects=enemy_environment_effects, enemy_environment_effects=ally_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                        renpy.pause(0.25)

                        # 不知火/冥火
                        # 若自身生命比例低于10%，则额外免能量释放一次“冥火”
                        if local_config.active_actor.selected_skill.name == "不知火" and local_config.active_actor.selected_skill.level == 5 and local_config.active_actor.hp / local_config.active_actor.battle_max_hp < 0.1:
                            extend_skill = getattr(store, "liuli_breakout")
                            extend_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.enemy, enemy=local_config.party, sudden_attack=False, support=True, ally_environment_effects=enemy_environment_effects, enemy_environment_effects=ally_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                            renpy.pause(0.25)
                        # 冥火
                        # 若自身生命比例低于10%，则额外免能量释放一次“不知火”
                        elif local_config.active_actor.selected_skill.name == "冥火" and local_config.active_actor.selected_skill.level == 5 and local_config.active_actor.hp / local_config.active_actor.battle_max_hp < 0.1:
                            extend_skill = getattr(store, "liuli_combat")
                            extend_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.enemy, enemy=local_config.party, sudden_attack=False, support=True, ally_environment_effects=enemy_environment_effects, enemy_environment_effects=ally_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                            renpy.pause(0.25)

                        # 推条
                        if "群体推条" in local_config.active_actor.selected_skill.effects:
                            ratio, target, time = local_config.active_actor.selected_skill.effects["群体推条"]
                            if ratio > 0.0:
                                for role in local_config.party[:3]:
                                    if role.hp > 0:
                                        role.order -= int(ratio * 1000)
                                        renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("行动推后", style="effect_text", color="ff9"))

                        # buff结算
                        if local_config.active_actor.hp > 0:
                            sources2 = None
                            if "Reflexes" in local_config.skill_log_data:
                                sources2 = local_config.skill_log_data["Reflexes"]
                            cand_buffs = copy(local_config.active_actor.buff)
                            for buff_name in cand_buffs:
                                sources = local_config.buff_source[local_config.active_actor.objectname][buff_name]
                                if local_config.active_actor.selected_skill.name not in sources:
                                    buff_obj = getattr(store, buff_name)
                                    if sources2 is not None and local_config.active_actor.objectname in sources2:
                                        temp_buff_name = sources2.pop(local_config.active_actor.objectname)
                                        if len(local_config.skill_log_data["Reflexes"]) == 0:
                                            local_config.skill_log_data.pop("Reflexes")
                                        if temp_buff_name != buff_obj:
                                            buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                                    else:
                                        buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                            cand_buffs = copy(local_config.active_actor.debuff)
                            for buff_name in cand_buffs:
                                buff_obj = getattr(store, buff_name)
                                if sources2 is not None and local_config.active_actor.objectname in sources2:
                                    temp_buff_name = sources2.pop(local_config.active_actor.objectname)
                                    if len(local_config.skill_log_data["Reflexes"]) == 0:
                                        local_config.skill_log_data.pop("Reflexes")
                                    if temp_buff_name != buff_obj:
                                        buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")
                                else:
                                    buff_obj.calculate(local_config.active_actor, enemy_environment_effects, None, None, "end")

                        renpy.block_rollback()
                        _rollback = True
                        
                        if local_config.active_actor.selected_skill.name == "虚无":
                            # 鬼面加入
                            if "积重鬼怨" in local_config.skill_log_data:
                                qcls_buff_roles = local_config.skill_log_data["积重鬼怨"]

                    # healing特殊规则
                    if "healing" in win_condition:
                        $ healing_selected_role.hp -= healing_damage
                        if healing_selected_role.hp < 1:
                            $ healing_selected_role.hp = 0
                            $ battle_result = "lose"
                            python:
                                for effect in media_skill_effect:
                                    renpy.hide(effect.vfx, layer="screens")
                            $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)
                        elif enemy_turns % 2 == 0:
                            $ healing_damage += 100

                        if "sp" in win_condition and 0.5 > renpy.random.random():
                            python:
                                extend_skill = getattr(store, "ycxt_combat")
                                extend_skill.use(user=local_config.active_actor, target=local_config.active_actor.selected_target, party=local_config.enemy, enemy=local_config.party, sudden_attack=False, support=True, ally_environment_effects=enemy_environment_effects, enemy_environment_effects=ally_environment_effects, order_members=order_members, role_now_stats=role_now_stats)
                                renpy.pause(0.25)
                
                    # 面具显示
                    if qcls_buff_roles and "enemy" in qcls_buff_roles:
                        # 开启附带9个禁断之面的“封印结界”笼罩对手
                        show set block qcls_skill_ally:
                            mask_top
                            mask_1
                            mask_2
                            mask_3
                            mask_4
                            mask_5
                            mask_6
                            mask_7
                            mask_8
                
                python:
                    order_members.update()

                $ _rollback = False
                # 更新行动条和血量
                if "healing" in win_condition:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_enemy=healing_selected_role, _layer="fg")
                else:
                    show screen battle_ui(local_config.party, local_config.enemy, order_members, extend_party=extend_turns, _layer="fg")

                python:
                    # 回合结束时触发的判定
                    if "积重鬼怨" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["积重鬼怨"]
                        if "ally" in buff_roles:
                            buff_roles["ally"] -= 1
                            # 消除禁断之面
                            face_number = buff_roles["ally"]
                            if face_number != 0:
                                renpy.hide("qcls_skill_enemy-mask_%d" % face_number)
                            else:
                                renpy.hide("qcls_skill_enemy-mask_top")
                                buff_roles.pop("ally")

                            if face_number == 0:
                                if len(local_config.skill_log_data["积重鬼怨"]) == 0:
                                    local_config.skill_log_data.pop("积重鬼怨")
                                for role in local_config.enemy[:3]:
                                    role._special_calculate(enemy_environment_effects=enemy_environment_effects, mode="release")
                    # 悉心呵护
                    if ("悉心呵护", True) in enemy_environment_effects and "共感" in local_config.skill_log_data and local_config.active_actor.hp > 0:
                        buff_roles = local_config.skill_log_data["共感"]
                        if "enemy" in buff_roles:
                            calculate_xz_role = [role for role in local_config.enemy[:3] if role.name == "青木翔子"]
                            if len(calculate_xz_role) > 0:
                                calculate_xz_role = calculate_xz_role[0]

                                # 附带了“心”状态的友方单位在回合结束时恢复“青木翔子”生命上限8%|8%|8%|12%|12%的生命值，并额外获得效果抵抗和速度提升，持续1回合
                                if local_config.active_actor in buff_roles["enemy"]:
                                    renpy.music.play("恢复", channel="battle_music")
                                    renpy.pause(0.05)
                                    renpy.show("healing_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=2.5, xpos=local_config.active_actor.xposition, ypos=0.4)], layer="screens")
                                    renpy.pause(0.96 * persistent.battlespeed)
                                    renpy.hide("healing_img", layer="screens")

                                    temp_selected_skills = calculate_xz_role.base_skills if not calculate_xz_role.is_phase2 else calculate_xz_role.base_skills_v2
                                    calculate_xz_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]
                                    temp_ratio_lists = [0.08, 0.08, 0.08, 0.12, 0.12]
                                    
                                    healing_number_gonggan = int(temp_ratio_lists[calculate_xz_passive.level - 1] * calculate_xz_role.battle_max_hp)
                                    renpy.show("damage", at_list=[show_damage(local_config.active_actor.xposition, 0.5)], layer="screens", what=Text("+%s" % healing_number_gonggan, style="damage_text", size=100, color="#2f0"))
                                    renpy.pause(0.5 * persistent.battlespeed)

                                    local_config.active_actor.hp += healing_number_gonggan
                                    if local_config.active_actor.hp > local_config.active_actor.battle_max_hp:
                                        local_config.active_actor.hp = local_config.active_actor.battle_max_hp
                                    if calculate_xz_passive.level in [2, 3, 4, 5]:
                                        buff_obj = getattr(store, "barrier")
                                        item = (1, 0.3)
                                        buff_obj.calculate(local_config.active_actor, None, item, "悉心呵护", "get")
                                        if calculate_xz_passive.level in [3, 4, 5]:
                                            temp_ratio_lists = [0, 0, 10, 20, 20]
                                            buff_obj = getattr(store, "flow")
                                            item = (1, temp_ratio_lists[calculate_xz_passive.level - 1])
                                            buff_obj.calculate(local_config.active_actor, None, item, "悉心呵护", "get")
                    # 波纹裂隙
                    if local_config.active_actor.name == "一诚小桃" and local_config.active_actor.hp > 0 and any([role.name == "一诚小桃" for role in local_config.enemy[:3]]) and ("波纹裂隙", True) in enemy_environment_effects and ("shield" not in local_config.active_actor.buff and "sp_shield" not in local_config.active_actor.buff):
                        temp_selected_skills = local_config.active_actor.base_skills if not local_config.active_actor.is_phase2 else local_config.active_actor.base_skills_v2
                        fake_ycxt_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]
                        temp_ratio_lists = [0.2, 0.2, 0.25, 0.25, 0.3]
                        if temp_ratio_lists[fake_ycxt_passive.level - 1] > renpy.random.random():
                            ycxt_select_skill = getattr(store, "ycxt_passive_1")
                            for xi in range(fake_ycxt_passive.level - 1):
                                ycxt_select_skill.level_change(ycxt_select_skill.level + 1)
                            local_config.active_actor.battle_calculate(ycxt_select_skill, local_config.active_actor, enemy_environment_effects, ally_environment_effects, order_members, slot_x=None, slot_y=None, support=False)
                            renpy.pause(0.25)
                    if "催眠" in local_config.skill_log_data:
                        qcls_buff_roles = local_config.skill_log_data["催眠"]
                        if local_config.active_actor in qcls_buff_roles:
                            time_number = qcls_buff_roles.pop(local_config.active_actor)
                            time_number -= 1
                            # 增益角色在行动结束后进入1回合不可驱散的“深度沉睡”状态
                            if time_number == 0:
                                # 清除霸体效果
                                if "domineering" in local_config.active_actor.buff:
                                    buff_obj = getattr(store, "domineering")
                                    buff_obj.calculate(local_config.active_actor, None, None, None, "clean")
                                # 进入1回合不可驱散的“深度沉睡”状态
                                buff_obj = getattr(store, "deep_sleepy")
                                item = (1, 0.3)
                                buff_obj.calculate(local_config.active_actor, None, item, "催眠", "get")

                                renpy.music.play("poisoned", channel="battle_music")
                                renpy.show("buff_effect", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text("深度睡眠", style="effect_text", color="ff9"))
                            # 施术者回合跳过
                            else:
                                local_config.skill_log_data["催眠"][local_config.active_actor] = time_number
                    # 澎湃天赋效果
                    if local_config.spi_mp_cost > 20:
                        buff = getattr(store, "dizziness")
                        item = (1, None)
                        buff.calculate(local_config.active_actor, None, item, "澎湃", "get")
                    # 灵巧天赋效果
                    for role in local_config.party[:3]:
                        if role.hp > 0 and not role.moveable and "Flexible" in role.abilities:
                            if role != local_config.shown_actor:
                                renpy.hide(local_config.shown_actor.objectname, layer="fg")
                                renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                renpy.pause(0.5 * persistent.battlespeed)

                            renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
                            renpy.pause(0.5 * persistent.battlespeed)
                            renpy.hide("buff_effect", layer="screens")
                            role.order += 200

                            if role != local_config.shown_actor:
                                renpy.hide(role.objectname, layer="fg")
                                renpy.show(local_config.shown_actor.objectname, at_list=[show_player(local_config.shown_actor.xposition)], layer="fg")
                                renpy.pause(0.5 * persistent.battlespeed)
                    # 月之华-琼勾
                    if ("月之华-琼勾", True) in enemy_environment_effects:
                        for role in local_config.enemy[:3]:
                            if role.hp > 0 and not role.moveable:
                                buff_obj = getattr(store, "flow")
                                item = (1, 20)
                                buff_obj.calculate(role, None, item, "月之华-琼勾", "get")
                    # 春之花-仑灵
                    if local_config.active_actor.equip4effect == "春之花-仑灵" and ("春之花-仑灵", True) in enemy_environment_effects:
                        if 0.2 > renpy.random.random():
                            for role in local_config.enemy[:3]:
                                if role.hp > 0:
                                    role.mp += 20

                    # 时空扭曲：狂暴之力-提升5%攻击力，提升3%暴击率，提升4%暴击伤害
                    if local_config.tutorial_step == "狂暴之力" and enemy_turns % 6 == 0:
                        for role in local_config.enemy[:3]:
                            if role.hp > 0:
                                buff_obj = getattr(store, "strong_attack")
                                item = (99, 0.05)
                                buff_obj.calculate(role, None, item, "狂暴之力-{}".format(str(enemy_turns//6)), "get")
                                buff_obj = getattr(store, "violence_attack")
                                item = (99, (0.03, 0.04))
                                buff_obj.calculate(role, None, item, "狂暴之力-{}".format(str(enemy_turns//6)), "get")

                    # 坚毅之岩
                    if 0.15 > renpy.random.random():
                        if "rock" in win_condition:
                            if "shield" in local_config.active_actor.buff:
                                buff_obj = getattr(store, "shield")
                                shield_time, (shield_strength, shield_element, v1, v2) = local_config.active_actor.buff["shield"]
                                if shield_element == "rock":
                                    media_shield_strength = int((local_config.active_actor.battle_max_hp - local_config.active_actor.hp) * 0.08)
                                    item = (2, (media_shield_strength, shield_element, v1, v2))
                                    buff_obj.calculate(local_config.active_actor, None, item, "坚毅之岩", "get")
                            elif "sp_shield" in local_config.active_actor.buff:
                                buff_obj = getattr(store, "sp_shield")
                                shield_time, (shield_strength, shield_element, v1, v2) = local_config.active_actor.buff["sp_shield"]
                                if shield_element == "rock":
                                    media_shield_strength = int((local_config.active_actor.battle_max_hp - local_config.active_actor.hp) * 0.08)
                                    item = (2, (media_shield_strength, shield_element, v1, v2))
                                    buff_obj.calculate(local_config.active_actor, None, item, "坚毅之岩", "get")
                            else:
                                media_shield_strength = int((local_config.active_actor.battle_max_hp - local_config.active_actor.hp) * 0.08)
                                buff_obj = getattr(store, "shield")
                                item = (2, (media_shield_strength, gain_element, 0.75, 0.5))
                                buff_obj.calculate(local_config.active_actor, None, item, "坚毅之岩", "get")
                        elif "wind" in win_condition and local_config.active_actor.hp < local_config.active_actor.battle_max_hp:
                            healing_number = int((local_config.active_actor.battle_max_hp - local_config.active_actor.hp) * 0.08)
                            renpy.show("damage", at_list=[show_damage(local_config.active_actor.xposition, 0.5)], layer="screens", what=Text("+%s" % healing_number, style="damage_text", size=100, color="#2f0"))
                            renpy.pause(0.5 * persistent.battlespeed)
                            renpy.hide("damage", layer="screens")

                            local_config.active_actor.hp += healing_number
                            if local_config.active_actor.hp > local_config.active_actor.battle_max_hp:
                                local_config.active_actor.hp = local_config.active_actor.battle_max_hp

                    # 瓦轮刑部
                    if local_config.tutorial_step == "瓦轮刑部":
                        alive_enemy_number = len([role for role in local_config.enemy if role.hp > 0])
                        if alive_enemy_number > 0 and enemy_turns % (alive_enemy_number * 3) == 0:
                            buff_obj = getattr(store, "rock_wall")
                            item = (99, 0.9)
                            for role in local_config.enemy:
                                if role.hp > 0:
                                    buff_obj.calculate(role, None, item, "瓦轮刑部", "get")
                    
                    # 敌方行动3回合将会触发“妄想颠覆”，为全体友方附加1回合混乱状态
                    if local_config.tutorial_step == "lhx_mana_error_winter_216":
                        extend_turns -= 1
                        if extend_turns == 0:
                            extend_turns = 5
                            buff_obj = getattr(store, "confusion")
                            item = (1, None)
                            for role in local_config.party[:3]:
                                if role.hp > 0:
                                    buff_obj.calculate(role, None, item, "妄想颠覆", "get")

                    # 表情重置
                    local_config.active_actor.face_change()

                # 循环结束判定：胜利条件
                $ alive_enemy_number = len(local_config.enemy)
                python:
                    for role in local_config.enemy:
                        if role.hp <= 0:
                            alive_enemy_number -= 1

                # 常规获胜方式：全灭敌人
                if alive_enemy_number == 0:
                    $ battle_result = "win"
                    python:
                        for effect in media_skill_effect:
                            renpy.hide(effect.vfx, layer="screens")
                    $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)

                # 循环结束判定：失败条件
                $ alive_party_number = len(local_config.party)
                python:
                    for role in local_config.party:
                        if role.hp <= 0:
                            alive_party_number -= 1

                # 常规失败方式：我方全灭
                if alive_party_number == 0:
                    $ battle_result = "lose"
                    python:
                        for effect in media_skill_effect:
                            renpy.hide(effect.vfx, layer="screens")
                    $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)
                # 保护模式失败方式
                elif "protect" in win_condition:
                    if protect_role.hp <= 0:
                        $ battle_result = "lose"
                        python:
                            for effect in media_skill_effect:
                                renpy.hide(effect.vfx, layer="screens")
                        $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)
            
            # healing特殊规则
            if "healing" in win_condition:
                if healing_selected_role.hp == healing_selected_role.battle_max_hp:
                    $ battle_result = "win"
                    python:
                        for effect in media_skill_effect:
                            renpy.hide(effect.vfx, layer="screens")
                    $ renpy.call("battle_end", enemy=local_config.enemy, mission_type=mission_type, treasures=treasures, win_condition=win_condition)

            # 行动结束后判定
            python:
                if win_condition == "battle_tutorial":
                    if "buff" in local_config.total_tutorial_flags:
                        for role in local_config.enemy + local_config.party:
                            if len(role.buff) != 0 or len(role.debuff) != 0:
                                local_config.total_tutorial_flags.remove("buff")
                                renpy.call("tutorial_step4")
                                break

                if win_condition == "battle_tutorial":
                    if "element" in local_config.total_tutorial_flags:
                        for role in local_config.enemy + local_config.party:
                            if len(role.ebuff) != 0:
                                local_config.total_tutorial_flags.remove("element")
                                renpy.call("tutorial_step5")
                                break

                if "enemy_protect" in local_config.tutorial_step:
                    protect_role_objname = local_config.tutorial_step.split("enemy_protect_")[1]
                    unprotect_left_enemies = [role for role in local_config.enemy if (role.objectname != protect_role_objname and role.hp > 0)]
                    protect_role_obj = [role for role in local_config.enemy if role.objectname == protect_role_objname][0]
                    if len(unprotect_left_enemies) == 0:
                        buff_obj = getattr(store, "sp_protect")
                        buff_obj.calculate(protect_role_obj, None, None, None, "clean")

            if local_config.tutorial_step in ["general_skill", "guard_skill", "combat_skill", "item_use", "support"]:
                $ local_config.tutorial_step = ""

            if local_config.active_actor is not None:
                python:
                    # 狂暴：当角色HP低于上限的10%，使用元素爆发后获得90%行动条提前
                    if "Brutal" in local_config.active_actor.abilities and local_config.active_actor.selected_skill not in ["auto_skill", "call_magic", "change"] and local_config.active_actor.selected_skill.category == "Break_out":
                        if local_config.active_actor.hp / local_config.active_actor.battle_max_hp < 0.1:
                            local_config.active_actor.order += 900
                            renpy.show("buff_effect", at_list=[show_state(local_config.active_actor.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
                            renpy.pause(0.5 * persistent.battlespeed)
                            renpy.hide("buff_effect", layer="screens")

                    # 行动角色的行动条清空
                    local_config.active_actor.order -= 1000
                    local_config.active_actor = None

            python:
                for effect in media_skill_effect:
                    renpy.hide(effect.vfx, layer="screens")

                # order_members.create(show=True)
                # raise NameError(order_members.bar, {rol.objectname: rol.order for rol in order_members.roles})

                # 隐藏我方全体
                # for role in local_config.party:
                #     renpy.hide(role.objectname, layer="fg")
                #     role.xposition = 0.85

        # 无角色达到行动条件
        else:
            python:
                # 行动角色已经阵亡
                if local_config.active_actor.hp <= 0:
                    local_config.active_actor.order -= 1000
                    local_config.active_actor = None
                # 所有角色行动条按速度推进
                order_members.move()


label battle_end(enemy, mission_type, treasures, win_condition):
    $ config.skipping = None
    # 战斗结束时隐藏角色 & 特效
    python:
        if local_config.shown_actor != None:
            renpy.hide(local_config.shown_actor.objectname, layer="fg")
            renpy.pause(0.25)
        for i in enemy:
            renpy.hide(i.objectname)

        # 积重鬼怨消除
        if "积重鬼怨" in local_config.skill_log_data:
            buff_roles = local_config.skill_log_data["积重鬼怨"]
            if "ally" in buff_roles:
                face_number = buff_roles["ally"]
                
                # 消除禁断之面
                while face_number > 0:
                    face_number -= 1
                    if face_number != 0:
                        renpy.hide("qcls_skill_enemy-mask_%d" % face_number)
                    else:
                        renpy.hide("qcls_skill_enemy-mask_top")
                buff_roles.pop("ally")
            elif "enemy" in buff_roles:
                face_number = buff_roles["enemy"]
                
                # 消除禁断之面
                while face_number > 0:
                    face_number -= 1
                    if face_number != 0:
                        renpy.hide("qcls_skill_ally-mask_%d" % face_number)
                    else:
                        renpy.hide("qcls_skill_ally-mask_top")
                buff_roles.pop("enemy")
            
    hide bottom_black
    hide snow_level1
    hide screen cancel_screen

    # 隐藏战斗残余画面
    $ renpy.hide_screen("battle_ui", layer="fg")
    scene onlayer fg
    with right2left

    python:
        # 我方参数重置
        for role in local_config.party + local_config.backup:
            role.full_reset(heal_hp=True, ally_environment_effects=ally_environment_effects, turn_end=True, level_reset=False)
        # 敌方参数和等级重置
        for role in local_config.enemy:
            role.full_reset(heal_hp=True, ally_environment_effects=enemy_environment_effects, turn_end=True, level_reset=True)
        if "healing" in win_condition:
            healing_selected_role.full_reset(heal_hp=True, ally_environment_effects=ally_environment_effects, turn_end=True, level_reset=True)
        # 战斗参数重置
        local_config.battle_params_reset()
        persistent.in_battle = False
        local_config.tutorial_step = ""

    ## 战斗胜利
    if battle_result == "win":
        stop music fadeout 1.0
        play battle_music "Win_Game"

        ## 普通剧情战、金币副本、经验副本、突破材料副本、装备副本、卡牌升级素材
        # 普通剧情战（经验+金币+战斗道具）
        if mission_type == "normal":
            python:
                # 获得经验值
                for role in local_config.party:
                    role.xpchange(enemy_levels=[e.level for e in enemy])

                # 获得金币
                # renpy.music.play("Get_Item", channel="battle_music")
                gain_currency = sum([role.currency for role in enemy])
                local_config.player.currency += gain_currency
                annotator("共获得[gain_currency]魔法币")

                # 道具掉落概率
                gain_items = {}
                for name, (max_count, ratio) in treasures.items():
                    for i in range(max_count):
                        if ratio > renpy.random.random():
                            if name not in gain_items:
                                gain_items[name] = 1
                            else:
                                gain_items[name] += 1

                for iname, inumber in gain_items.items():
                    if iname in local_config.player.items:
                        local_config.player.items[iname] += inumber
                    else:
                        local_config.player.items[iname] = inumber
            $　get_index = len(gain_items) - 1
            while get_index >= 0:
                python:
                    get_img_name = ""
                    chosen_item = None
                    get_inumber = 0
                    for i, (iname, inumber) in enumerate(gain_items.items()):
                        if i == get_index:
                            get_img_name = iname
                            chosen_item = getattr(store, iname)
                            get_inumber = inumber
                            get_index -= 1
                            break

                if get_img_name == "eggs":
                    inventory add egg raw
                elif get_img_name == "mana_eggs":
                    inventory add egg boiled
                elif get_img_name == "mana_potion":
                    inventory add casllion clean
                elif get_img_name == "angel_tears":
                    inventory add angeltear
                elif get_img_name == "soul_piece":
                    inventory add soul piece
                elif get_img_name == "soul_raise":
                    inventory add soul raisa
                elif get_img_name == "water_break_large":
                    inventory add water big
                elif get_img_name == "water_break_small":
                    inventory add water tiny
                elif get_img_name == "wind_break_large":
                    inventory add wind big
                elif get_img_name == "wind_break_small":
                    inventory add wind tiny
                elif get_img_name == "rock_break_large":
                    inventory add rock big
                elif get_img_name == "rock_break_small":
                    inventory add rock tiny
                elif get_img_name == "fire_break_large":
                    inventory add fire big
                elif get_img_name == "fire_break_small":
                    inventory add fire tiny
                elif get_img_name == "ice_break_large":
                    inventory add ice big
                elif get_img_name == "ice_break_small":
                    inventory add ice tiny
                elif get_img_name == "light_break_large":
                    inventory add light big
                elif get_img_name == "light_break_small":
                    inventory add light tiny

                "共获得物品 [chosen_item.name]*[get_inumber]"

        # 金币副本（金币）
        elif mission_type == "currency":
            python:
                # 获得经验值
                for role in local_config.party:
                    role.xpchange(enemy_levels=[e.level for e in enemy])

                # 获得金币
                # renpy.music.play("Get_Item", channel="battle_music")
                local_config.player.currency += int(treasures * persistent.drop_rate)
                annotator("共获得[treasures]魔法币")
            
        # 经验副本（经验道具）
        elif mission_type == "experience":
            python:
                # 获得经验值
                for role in local_config.party:
                    role.xpchange(enemy_levels=[e.level for e in enemy])

                # 道具掉落概率
                gain_items = {}
                for name, (max_count, ratio) in treasures.items():
                    for i in range(max_count):
                        if ratio > renpy.random.random():
                            if name not in gain_items:
                                gain_items[name] = int(1 * persistent.drop_rate)
                            else:
                                gain_items[name] += int(1 * persistent.drop_rate)

                for iname, inumber in gain_items.items():
                    if iname in local_config.player.items:
                        local_config.player.items[iname] += inumber
                    else:
                        local_config.player.items[iname] = inumber

            $　get_index = len(gain_items) - 1
            while get_index >= 0:
                python:
                    get_img_name = ""
                    chosen_item = None
                    get_inumber = 0
                    for i, (iname, inumber) in enumerate(gain_items.items()):
                        if i == get_index:
                            get_img_name = iname
                            chosen_item = getattr(store, iname)
                            get_inumber = inumber
                            get_index -= 1
                            break

                if get_img_name == "soul_piece":
                    inventory add soul piece
                elif get_img_name == "soul_raise":
                    inventory add soul raisa

                "共获得物品 [chosen_item.name]*[get_inumber]"

        # 突破材料副本（突破材料）
        elif mission_type == "breakout":
            python:
                # 获得经验值
                for role in local_config.party:
                    role.xpchange(enemy_levels=[e.level for e in enemy])

                # 道具掉落概率
                gain_items = {}
                for name, (max_count, ratio) in treasures.items():
                    for i in range(max_count):
                        if ratio > renpy.random.random():
                            if name not in gain_items:
                                gain_items[name] = 1 * persistent.drop_rate
                            else:
                                gain_items[name] += 1 * persistent.drop_rate

                for iname, inumber in gain_items.items():
                    if iname in local_config.player.items:
                        local_config.player.items[iname] += inumber
                    else:
                        local_config.player.items[iname] = inumber

            $　get_index = len(gain_items) - 1
            while get_index >= 0:
                python:
                    get_img_name = ""
                    chosen_item = None
                    get_inumber = 0
                    for i, (iname, inumber) in enumerate(gain_items.items()):
                        if i == get_index:
                            get_img_name = iname
                            chosen_item = getattr(store, iname)
                            get_inumber = inumber
                            get_index -= 1
                            break

                if get_img_name == "water_break_large":
                    inventory add water big
                elif get_img_name == "water_break_small":
                    inventory add water tiny
                elif get_img_name == "wind_break_large":
                    inventory add wind big
                elif get_img_name == "wind_break_small":
                    inventory add wind tiny
                elif get_img_name == "rock_break_large":
                    inventory add rock big
                elif get_img_name == "rock_break_small":
                    inventory add rock tiny
                elif get_img_name == "fire_break_large":
                    inventory add fire big
                elif get_img_name == "fire_break_small":
                    inventory add fire tiny
                elif get_img_name == "ice_break_large":
                    inventory add ice big
                elif get_img_name == "ice_break_small":
                    inventory add ice tiny
                elif get_img_name == "light_break_large":
                    inventory add light big
                elif get_img_name == "light_break_small":
                    inventory add light tiny

                "共获得物品 [chosen_item.name]*[get_inumber]"

        # 装备副本（装备）
        elif mission_type == "equipment":
            python:
                # 获得经验值
                for role in local_config.party:
                    role.xpchange(enemy_levels=[e.level for e in enemy])
                
                # 全部装备概率计算
                treasures_count = {}
                for name, (max_count, ratio) in treasures.items():
                    if "num" in name:
                        all_match_outfits = [oft for oft in outfit_list if name in oft.objectname]
                        for i in range(max_count * persistent.drop_rate):
                            if ratio > renpy.random.random():
                                chosen_equip_idx = renpy.random.randint(0, len(all_match_outfits) - 1)
                                chosen_equip = all_match_outfits[chosen_equip_idx]
                                chosen_equip.get(who=local_config.player)
                                if chosen_equip.objectname in treasures_count:
                                    treasures_count[chosen_equip.objectname] += 1
                                else:
                                    treasures_count[chosen_equip.objectname] = 1
                    else:
                        chosen_equip = [oft for oft in outfit_list if name == oft.objectname][0]
                        for i in range(max_count * persistent.drop_rate):
                            if ratio > renpy.random.random():
                                chosen_equip.get(who=local_config.player)
                                if chosen_equip.objectname in treasures_count:
                                    treasures_count[chosen_equip.objectname] += 1
                                else:
                                    treasures_count[chosen_equip.objectname] = 1
                
                get_number = 0
                if len(treasures_count) <= 9:
                    for i, (outfit_name, count) in enumerate(treasures_count.items()):
                        get_number += count
                        renpy.show(outfit_name, at_list=[Transform(zoom=0.5, xalign=0.1+i*0.1, yalign=0.4)], layer="m2")
                        renpy.show("buff_effect_%d" % i, at_list=[Transform(zoom=0.5, xalign=0.152+i*0.096, yalign=0.45)], layer="screens", what=Text("[count]", style="effect_text", color="ff9"))
                elif len(treasures_count) <= 18:
                    for i, (outfit_name, count) in enumerate(treasures_count.items()):
                        if i >= 9:
                            break
                        get_number += count
                        renpy.show(outfit_name, at_list=[Transform(zoom=0.5, xalign=0.1+i*0.1, yalign=0.4)], layer="m2")
                        renpy.show("buff_effect_%d" % i, at_list=[Transform(zoom=0.5, xalign=0.152+i*0.096, yalign=0.45)], layer="screens", what=Text("[count]", style="effect_text", color="ff9"))
                    for i, (outfit_name, count) in enumerate(treasures_count.items()):
                        if i <= 9:
                            continue
                        get_number += count
                        renpy.show(outfit_name, at_list=[Transform(zoom=0.5, xalign=0.1+i*0.1, yalign=0.6)], layer="m2")
                        renpy.show("buff_effect_%d" % i, at_list=[Transform(zoom=0.5, xalign=0.152+i*0.096, yalign=0.65)], layer="screens", what=Text("[count]", style="effect_text", color="ff9"))
                else:
                    for i, (outfit_name, count) in enumerate(treasures_count.items()):
                        if i >= 9:
                            break
                        get_number += count
                        renpy.show(outfit_name, at_list=[Transform(zoom=0.5, xalign=0.1+i*0.1, yalign=0.3)], layer="m2")
                        renpy.show("buff_effect_%d" % i, at_list=[Transform(zoom=0.5, xalign=0.152+i*0.096, yalign=0.35)], layer="screens", what=Text("[count]", style="effect_text", color="ff9"))
                    for i, (outfit_name, count) in enumerate(treasures_count.items()):
                        if i >= 18:
                            break
                        get_number += count
                        renpy.show(outfit_name, at_list=[Transform(zoom=0.5, xalign=0.1+i*0.1, yalign=0.5)], layer="m2")
                        renpy.show("buff_effect_%d" % i, at_list=[Transform(zoom=0.5, xalign=0.152+i*0.096, yalign=0.55)], layer="screens", what=Text("[count]", style="effect_text", color="ff9"))
                    for i, (outfit_name, count) in enumerate(treasures_count.items()):
                        if i <= 18:
                            continue
                        get_number += count
                        renpy.show(outfit_name, at_list=[Transform(zoom=0.5, xalign=0.1+i*0.1, yalign=0.7)], layer="m2")
                        renpy.show("buff_effect_%d" % i, at_list=[Transform(zoom=0.5, xalign=0.152+i*0.096, yalign=0.75)], layer="screens", what=Text("[count]", style="effect_text", color="ff9"))
                        
                renpy.say(me01, "获得装备*[get_number]")
                equip_is_full, full_cate = local_config.player.is_equipments_full(return_cate=True)
                if equip_is_full:
                    renpy.say(me01, "[full_cate]装备栏已接近上限，优先清理一下无用道具防止新装备无法获取的情况出现。")

                for i, outfit in enumerate(treasures_count):
                    renpy.hide(outfit, layer="m2")
                    renpy.hide("buff_effect_%d" % i)
                renpy.pause(0.75, hard=True)
            
        # 卡牌副本（卡牌升级素材）
    # 战斗失败
    elif battle_result == "lose":
        if win_condition != "must_lose":
            jump gameend
        else:
            $ battle_result = "win"

    $ preferences.afm_enable = True

    return


label gameend:
    stop music fadeout 1.0
    scene black
    with dissolve
    play battle_music "Defeat_sound"
    show expression Text("Game Over", style="say_label", size=225, color="#f33", outlines=[(1, "f339")]):
        align (0.5, 0.5)
    with dissolve
    pause
    scene black
    with dissolve
    $ renpy.full_restart()
