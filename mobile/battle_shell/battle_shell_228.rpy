
# 金币副本
label battle_attack_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg lyz
    with dissolve

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为一诚小桃，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [ycxt_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "attack_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("attack_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=ycxt_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_attack_battle_easy" if checkout_flag else None, 
                    mission_type="currency", 
                    treasures=1500)

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为青木铃音、千川老师，巫女个数4，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [lingyin_role_mirror, qcls_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            # 初始化“遗念镜”祝福
            local_config.battle_blessing = {
                "融化": 0.5,
                "蒸发": 0.5
            }
            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“狂暴之力”时空扭曲
            local_config.tutorial_step = "狂暴之力"

        $ checkout_flag = "attack_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("attack_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=lingyin_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[qcls_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0,
                    inside_label="inside_attack_battle_hard" if checkout_flag else None, 
                    mission_type="currency", 
                    treasures=5000)

    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            # 初始化“遗念镜”祝福
            local_config.battle_blessing = {
                "融化": 0.25,
                "蒸发": 0.25
            }
            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“狂暴之力”时空扭曲
            local_config.tutorial_step = "狂暴之力"

        $ checkout_flag = "attack_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("attack_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0,
                    inside_label="inside_attack_battle_abyss" if checkout_flag else None, 
                    mission_type="currency", 
                    treasures=10000)

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom


# 经验副本
label battle_protect_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg hmx
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为青木铃音，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [lingyin_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "protect_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("protect_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=lingyin_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_protect_battle_easy" if checkout_flag else None, 
                    mission_type="experience", 
                    treasures={"soul_piece": (3, 0.5), 
                               "soul_raise": (5, 0.5)})

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为水之濑凛、花山院琉璃，巫女个数4，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [szl_role_mirror, liuli_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            # 初始化“遗念镜”祝福
            local_config.battle_blessing = {
                "冻结": 0.2,
            }
            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 随机获取我方场上一位角色
            random_index = renpy.random.randint(0, len(local_config.party[:3]) - 1)
            random_role_name = local_config.party[:3][random_index].objectname.split("_role")[0]

            # 初始化“狂暴之力”时空扭曲
            local_config.tutorial_step = "猎杀之印"

        $ checkout_flag = "protect_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("protect_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=szl_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[liuli_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='game_protect_%s' % random_role_name, 
                    stay_turn=0,
                    inside_label="inside_protect_battle_hard" if checkout_flag else None, 
                    mission_type="experience", 
                    treasures={"soul_piece": (8, 0.5), 
                               "soul_raise": (12, 0.5)})

    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            # 初始化“遗念镜”祝福
            local_config.battle_blessing = {
                "冻结": 0.2,
            }
            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 随机获取我方场上一位角色
            random_index = renpy.random.randint(0, len(local_config.party[:3]) - 1)
            random_role_name = local_config.party[:3][random_index].objectname.split("_role")[0]

            # 初始化“狂暴之力”时空扭曲
            local_config.tutorial_step = "猎杀之印"

        $ checkout_flag = "protect_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("protect_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='game_protect_%s' % random_role_name, 
                    stay_turn=0,
                    inside_label="inside_protect_battle_abyss" if checkout_flag else None, 
                    mission_type="experience", 
                    treasures={"soul_piece": (15, 0.5), 
                               "soul_raise": (22, 0.5)})

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom


# 突破材料副本
label battle_speed_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg yym
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为藤原瞳，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [tyt_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "speed_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("speed_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=tyt_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_speed_battle_easy" if checkout_flag else None, 
                    mission_type="breakout",
                    treasures={"water_break_small": (5, 0.3),
                               "water_break_large": (1, 0.1),
                               "wind_break_small": (5, 0.3),
                               "wind_break_large": (1, 0.1),
                               "rock_break_small": (5, 0.3),
                               "rock_break_large": (1, 0.1),
                               "fire_break_small": (5, 0.3),
                               "fire_break_large": (1, 0.1),
                               "ice_break_small": (5, 0.3),
                               "ice_break_large": (1, 0.1),
                               "light_break_small": (5, 0.3),
                               "light_break_large": (1, 0.1)})

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为植诚友加、一诚小桃，巫女个数4，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [yj_role_mirror, ycxt_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            # 初始化“遗念镜”祝福
            local_config.battle_blessing = {
                "超载": 800,
            }
            for role in copy(local_config.party):
                # 替换角色的凝神为蓄能
                role.skills = [s if s.category != "Recharge" else getattr(store, "guard_spt") for s in role.skills]
                role.skills_v2 = [s if s.category != "Recharge" else getattr(store, "guard_spt") for s in role.skills_v2]
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“迅捷之影”时空扭曲
            local_config.tutorial_step = "迅捷之影"

        $ checkout_flag = "speed_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("speed_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=yj_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[ycxt_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0,
                    inside_label="inside_speed_battle_hard" if checkout_flag else None, 
                    mission_type="breakout",
                    treasures={"water_break_small": (8, 0.5),
                               "water_break_large": (5, 0.3),
                               "wind_break_small": (8, 0.5),
                               "wind_break_large": (5, 0.3),
                               "rock_break_small": (8, 0.5),
                               "rock_break_large": (5, 0.3),
                               "fire_break_small": (8, 0.5),
                               "fire_break_large": (5, 0.3),
                               "ice_break_small": (8, 0.5),
                               "ice_break_large": (5, 0.3),
                               "light_break_small": (8, 0.5),
                               "light_break_large": (5, 0.3)})
    
    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            # 初始化“遗念镜”祝福
            local_config.battle_blessing = {
                "超载": 800,
            }
            for role in copy(local_config.party):
                # 替换角色的凝神为蓄能
                role.skills = [s if s.category != "Recharge" else getattr(store, "guard_spt") for s in role.skills]
                role.skills_v2 = [s if s.category != "Recharge" else getattr(store, "guard_spt") for s in role.skills_v2]
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“迅捷之影”时空扭曲
            local_config.tutorial_step = "迅捷之影"

        $ checkout_flag = "speed_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("speed_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0,
                    inside_label="inside_speed_battle_abyss" if checkout_flag else None, 
                    mission_type="breakout",
                    treasures={"water_break_small": (8, 0.9),
                               "water_break_large": (5, 0.3),
                               "wind_break_small": (8, 0.9),
                               "wind_break_large": (5, 0.3),
                               "rock_break_small": (8, 0.9),
                               "rock_break_large": (5, 0.3),
                               "fire_break_small": (8, 0.9),
                               "fire_break_large": (5, 0.3),
                               "ice_break_small": (8, 1.0),
                               "ice_break_large": (5, 0.3),
                               "light_break_small": (8, 0.9),
                               "light_break_large": (5, 0.3)})

    if _return == "win":
        "战斗胜利！"
        python:
            if persistent.difficult != "easy":
                for role in local_config.party:
                    # 蓄能恢复
                    role.skills = [s if s.category != "Recharge" else getattr(store, "guard") for s in role.skills]
                    role.skills_v2 = [s if s.category != "Recharge" else getattr(store, "guard") for s in role.skills_v2]
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom


# 装备副本-火
label battle_fire_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg msk
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为日向爱衣，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [aiyi_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "fire_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("fire_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=aiyi_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_fire_battle_easy" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num3_01": (3, 0.5),
                               "num3_02": (2, 0.3),
                               "num3_03": (1, 0.1),
                               "num10_01": (3, 0.5),
                               "num10_02": (2, 0.3),
                               "num10_03": (1, 0.1),
                               "magic_fire_01": (3, 0.3),
                               "magic_fire_02": (2, 0.2),
                               "magic_fire_03": (1, 0.1),
                               "stone_fire_01": (3, 0.3),
                               "stone_fire_02": (2, 0.2),
                               "stone_fire_03": (1, 0.1)})

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为花山院琉璃，巫女个数5，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [liuli_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为火属性
                if role != liuli_role_mirror:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_sfire"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“阴燃之火”时空扭曲
            local_config.tutorial_step = "阴燃之火"

        $ checkout_flag = "fire_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("fire_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=liuli_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='fire-normal', 
                    stay_turn=0,
                    inside_label="inside_fire_battle_hard" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num3_01": (3, 0.9),
                               "num3_02": (2, 0.6),
                               "num3_03": (1, 0.3),
                               "num10_01": (3, 0.5),
                               "num10_02": (2, 0.3),
                               "num10_03": (1, 0.1),
                               "magic_fire_01": (3, 0.6),
                               "magic_fire_02": (2, 0.4),
                               "magic_fire_03": (1, 0.2),
                               "stone_fire_01": (3, 0.6),
                               "stone_fire_02": (2, 0.4),
                               "stone_fire_03": (1, 0.2)})

    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为火属性
                if "migo_tiny_girl_mirror" in role.objectname:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_sfire"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“阴燃之火”时空扭曲
            local_config.tutorial_step = "阴燃之火"

        $ checkout_flag = "fire_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("fire_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='fire-normal', 
                    stay_turn=0,
                    inside_label="inside_fire_battle_abyss" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num3_03": (4, 0.6),
                               "num3_04": (2, 0.3),
                               "num10_03": (4, 0.6),
                               "num10_04": (2, 0.3),
                               "magic_fire_03": (4, 0.6),
                               "magic_fire_04": (2, 0.3),
                               "stone_fire_03": (4, 0.6),
                               "stone_fire_04": (2, 0.3)})

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom


# 装备副本-雷
label battle_light_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg yyc
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为千川老师，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [qcls_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "light_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("light_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=qcls_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_light_battle_easy" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num1_01": (3, 0.5),
                               "num1_02": (2, 0.3),
                               "num1_03": (1, 0.1),
                               "num4_01": (3, 0.5),
                               "num4_02": (2, 0.3),
                               "num4_03": (1, 0.1),
                               "magic_light_01": (3, 0.3),
                               "magic_light_02": (2, 0.2),
                               "magic_light_03": (1, 0.1),
                               "stone_light_01": (3, 0.3),
                               "stone_light_02": (2, 0.2),
                               "stone_light_03": (1, 0.1)})

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为水之濑凛，巫女个数5，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [szl_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为雷属性
                if role != szl_role_mirror:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_slight"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“嗜能之雷”时空扭曲
            local_config.tutorial_step = "嗜能之雷"

        $ checkout_flag = "light_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("light_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=szl_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='light-normal', 
                    stay_turn=0,
                    inside_label="inside_light_battle_hard" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num1_01": (3, 0.9),
                               "num1_02": (2, 0.6),
                               "num1_03": (1, 0.3),
                               "num4_01": (3, 0.5),
                               "num4_02": (2, 0.3),
                               "num4_03": (1, 0.1),
                               "magic_light_01": (3, 0.6),
                               "magic_light_02": (2, 0.4),
                               "magic_light_03": (1, 0.2),
                               "stone_light_01": (3, 0.6),
                               "stone_light_02": (2, 0.4),
                               "stone_light_03": (1, 0.2)})

    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为火属性
                if "migo_tiny_girl_mirror" in role.objectname:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_slight"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“嗜能之雷”时空扭曲
            local_config.tutorial_step = "嗜能之雷"

        $ checkout_flag = "light_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("light_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='light-normal', 
                    stay_turn=0,
                    inside_label="inside_light_battle_abyss" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num1_03": (4, 0.6),
                               "num1_04": (2, 0.3),
                               "num4_03": (4, 0.6),
                               "num4_04": (2, 0.3),
                               "magic_light_03": (4, 0.6),
                               "magic_light_04": (2, 0.3),
                               "stone_light_03": (4, 0.6),
                               "stone_light_04": (2, 0.3)})

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom


# 装备副本-水
label battle_water_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg hyz
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为青木翔子，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [xz_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "water_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("water_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=xz_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_water_battle_easy" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num2_01": (3, 0.5),
                               "num2_02": (2, 0.3),
                               "num2_03": (1, 0.1),
                               "num6_01": (3, 0.5),
                               "num6_02": (2, 0.3),
                               "num6_03": (1, 0.1),
                               "magic_water_01": (3, 0.3),
                               "magic_water_02": (2, 0.2),
                               "magic_water_03": (1, 0.1),
                               "stone_water_01": (3, 0.3),
                               "stone_water_02": (2, 0.2),
                               "stone_water_03": (1, 0.1)})

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为植诚友加，巫女个数5，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [yj_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为水属性
                if role != yj_role_mirror:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_swater"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“迟滞之水”时空扭曲
            local_config.tutorial_step = "迟滞之水"

        $ checkout_flag = "water_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("water_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=yj_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='water-normal', 
                    stay_turn=0,
                    inside_label="inside_water_battle_hard" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num2_01": (3, 0.9),
                               "num2_02": (2, 0.6),
                               "num2_03": (1, 0.3),
                               "num6_01": (3, 0.5),
                               "num6_02": (2, 0.3),
                               "num6_03": (1, 0.1),
                               "magic_water_01": (3, 0.6),
                               "magic_water_02": (2, 0.4),
                               "magic_water_03": (1, 0.2),
                               "stone_water_01": (3, 0.6),
                               "stone_water_02": (2, 0.4),
                               "stone_water_03": (1, 0.2)})

    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为水属性
                if "migo_tiny_girl_mirror" in role.objectname:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_swater"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“迟滞之水”时空扭曲
            local_config.tutorial_step = "迟滞之水"

        $ checkout_flag = "water_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("water_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='water-normal', 
                    stay_turn=0,
                    inside_label="inside_water_battle_abyss" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num2_03": (4, 0.6),
                               "num2_04": (2, 0.3),
                               "num6_03": (4, 0.6),
                               "num6_04": (2, 0.3),
                               "magic_water_03": (4, 0.6),
                               "magic_water_04": (2, 0.3),
                               "stone_water_03": (4, 0.6),
                               "stone_water_04": (2, 0.3)})

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom


# 装备副本-冰
label battle_ice_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg fsl
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为一诚小桃，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [ycxt_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "ice_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("ice_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=ycxt_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_ice_battle_easy" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num8_01": (3, 0.5),
                               "num8_02": (2, 0.3),
                               "num8_03": (1, 0.1),
                               "num12_01": (3, 0.5),
                               "num12_02": (2, 0.3),
                               "num12_03": (1, 0.1),
                               "magic_ice_01": (3, 0.3),
                               "magic_ice_02": (2, 0.2),
                               "magic_ice_03": (1, 0.1),
                               "stone_ice_01": (3, 0.3),
                               "stone_ice_02": (2, 0.2),
                               "stone_ice_03": (1, 0.1)})

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为雷亚，巫女个数5，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [lst_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为冰属性
                if role != lst_role_mirror:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_sice"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“凝结之冰”时空扭曲
            local_config.tutorial_step = "凝结之冰"

        $ checkout_flag = "ice_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("ice_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=lst_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='ice-normal', 
                    stay_turn=0,
                    inside_label="inside_ice_battle_hard" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num8_01": (3, 0.9),
                               "num8_02": (2, 0.6),
                               "num8_03": (1, 0.3),
                               "num12_01": (3, 0.5),
                               "num12_02": (2, 0.3),
                               "num12_03": (1, 0.1),
                               "magic_ice_01": (3, 0.6),
                               "magic_ice_02": (2, 0.4),
                               "magic_ice_03": (1, 0.2),
                               "stone_ice_01": (3, 0.6),
                               "stone_ice_02": (2, 0.4),
                               "stone_ice_03": (1, 0.2)})

    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为冰属性
                if "migo_tiny_girl_mirror" in role.objectname:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_sice"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“凝结之冰”时空扭曲
            local_config.tutorial_step = "凝结之冰"

        $ checkout_flag = "ice_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("ice_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='ice-normal', 
                    stay_turn=0,
                    inside_label="inside_ice_battle_abyss" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num8_03": (4, 0.6),
                               "num8_04": (2, 0.3),
                               "num12_03": (4, 0.6),
                               "num12_04": (2, 0.3),
                               "magic_ice_03": (4, 0.6),
                               "magic_ice_04": (2, 0.3),
                               "stone_ice_03": (4, 0.6),
                               "stone_ice_04": (2, 0.3)})

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom


# 装备副本-岩
label battle_rock_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg fxt
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为藤原瞳，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [tyt_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "rock_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("rock_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=tyt_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_rock_battle_easy" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num5_01": (3, 0.5),
                               "num5_02": (2, 0.3),
                               "num5_03": (1, 0.1),
                               "num11_01": (3, 0.5),
                               "num11_02": (2, 0.3),
                               "num11_03": (1, 0.1),
                               "magic_rock_01": (3, 0.3),
                               "magic_rock_02": (2, 0.2),
                               "magic_rock_03": (1, 0.1),
                               "stone_rock_01": (3, 0.3),
                               "stone_rock_02": (2, 0.2),
                               "stone_rock_03": (1, 0.1)})

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为希菲尔，巫女个数5，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [xfe_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为岩属性
                if role != xfe_role_mirror:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_srock"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“坚毅之岩”时空扭曲
            local_config.tutorial_step = "坚毅之岩"

        $ checkout_flag = "rock_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("rock_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=xfe_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='rock-normal', 
                    stay_turn=0,
                    inside_label="inside_rock_battle_hard" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num5_01": (3, 0.9),
                               "num5_02": (2, 0.6),
                               "num5_03": (1, 0.3),
                               "num11_01": (3, 0.5),
                               "num11_02": (2, 0.3),
                               "num11_03": (1, 0.1),
                               "magic_rock_01": (3, 0.6),
                               "magic_rock_02": (2, 0.4),
                               "magic_rock_03": (1, 0.2),
                               "stone_rock_01": (3, 0.6),
                               "stone_rock_02": (2, 0.4),
                               "stone_rock_03": (1, 0.2)})

    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为岩属性
                if "migo_tiny_girl_mirror" in role.objectname:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_srock"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“坚毅之岩”时空扭曲
            local_config.tutorial_step = "坚毅之岩"

        $ checkout_flag = "rock_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("rock_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='rock-normal', 
                    stay_turn=0,
                    inside_label="inside_rock_battle_abyss" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num5_03": (4, 0.6),
                               "num5_04": (2, 0.3),
                               "num11_03": (4, 0.6),
                               "num11_04": (2, 0.3),
                               "magic_rock_03": (4, 0.6),
                               "magic_rock_04": (2, 0.3),
                               "stone_rock_03": (4, 0.6),
                               "stone_rock_04": (2, 0.3)})

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom


# 装备副本-风
label battle_wind_228:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'
        "一般（难度适中，奖励也适中）":
            $ persistent.difficult = 'hard'
        "困难（难度较大，奖励也较多）":
            $ persistent.difficult = 'abyss'

    $ flcam.move(0, 0, 0)
    scene set only fight_cg dld
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    if persistent.difficult == 'easy':
        python:
            # 战斗boss为青木铃音，巫女个数2，所有敌方角色技能提升等级4，装备“普通”随机等级1装备6件
            enemy_roles = [lingyin_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    sample_outfit.enemy_equip_on(role)
                for xi in range(4):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level - 3, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

        $ checkout_flag = "wind_battle_easy" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("wind_battle_easy")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=lingyin_role_mirror, 
                    boss_hp_plus=100 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1], 
                    side_hp_plus=0,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='normal', 
                    stay_turn=0, 
                    inside_label="inside_wind_battle_easy" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num7_01": (3, 0.5),
                               "num7_02": (2, 0.3),
                               "num7_03": (1, 0.1),
                               "num9_01": (3, 0.5),
                               "num9_02": (2, 0.3),
                               "num9_03": (1, 0.1),
                               "magic_wind_01": (3, 0.3),
                               "magic_wind_02": (2, 0.2),
                               "magic_wind_03": (1, 0.1),
                               "stone_wind_01": (3, 0.3),
                               "stone_wind_02": (2, 0.2),
                               "stone_wind_03": (1, 0.1)})

    elif persistent.difficult == 'hard':
        python:
            # 战斗boss为立花希，巫女个数5，所有敌方角色技能提升等级8，装备“稀有”随机等级6装备6件
            enemy_roles = [lhx_role_mirror, migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4]
            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_02" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(5):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为风属性
                if role != lhx_role_mirror:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_swind"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(8):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level = min(team_average_level, 40)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“济世之风”时空扭曲
            local_config.tutorial_step = "济世之风"

        $ checkout_flag = "wind_battle_hard" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("wind_battle_hard")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=lhx_role_mirror,
                    boss_hp_plus=300 * team_average_level, 
                    side_enemy=[migo_tiny_girl_mirror, migo_tiny_girl_mirror_1, migo_tiny_girl_mirror_2, migo_tiny_girl_mirror_3, migo_tiny_girl_mirror_4], 
                    side_hp_plus=50 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='wind-normal', 
                    stay_turn=0,
                    inside_label="inside_wind_battle_hard" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num7_01": (3, 0.9),
                               "num7_02": (2, 0.6),
                               "num7_03": (1, 0.3),
                               "num9_01": (3, 0.5),
                               "num9_02": (2, 0.3),
                               "num9_03": (1, 0.1),
                               "magic_wind_01": (3, 0.6),
                               "magic_wind_02": (2, 0.4),
                               "magic_wind_03": (1, 0.2),
                               "stone_wind_01": (3, 0.6),
                               "stone_wind_02": (2, 0.4),
                               "stone_wind_03": (1, 0.2)})

    elif persistent.difficult == 'abyss':
        python:
            # 战斗boss为角色镜像，巫女个数补充到6，所有敌方角色技能提升等级12，装备“史诗”随机等级12装备6件
            boss_role = getattr(store, local_config.masters[0] + "_mirror")
            side_roles = [getattr(store, rolename + "_mirror") for rolename in local_config.masters[1:]] + [getattr(store, role.objectname + "_mirror") for role in local_config.party if role.objectname not in local_config.masters]
            enemy_roles = [boss_role] + side_roles
            side_roles_migo = [getattr(store, "migo_tiny_girl_mirror_%d" % (idx + 1)) for idx in range(6-len(enemy_roles))]
            enemy_roles += side_roles_migo
            side_roles += side_roles_migo

            for role in enemy_roles:
                role.equip_experience = 99999999
                for cate in role.outfits:
                    enemy_outfits = [outfit for outfit in outfit_list if ("_03" in outfit.objectname and outfit.category == cate)]
                    sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
                    sample_outfit = enemy_outfits[sample_index]
                    sample_outfit.init_params()
                    for xi in range(11):
                        sample_outfit.level_up(role, 100)
                    sample_outfit.enemy_equip_on(role)
                # 巫女普攻变为风属性
                if "migo_tiny_girl_mirror" in role.objectname:
                    now_battle_general_attack = copy(getattr(store, "psychokinesis_ex_swind"))
                    role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                for xi in range(12):
                    role.skill_levelup()

            # 计算masters的角色平均等级，或全队最高等级
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
            team_average_level += 3
            team_average_level = min(team_average_level, 43)

            for role in copy(local_config.party):
                # 队伍数据转移
                new_role_obj = getattr(store, role.objectname)
                new_role_obj.battle_params_match(role)
                local_config.party.remove(role)
                local_config.party.append(new_role_obj)

            # 初始化“济世之风”时空扭曲
            local_config.tutorial_step = "济世之风"

        $ checkout_flag = "wind_battle_abyss" in local_config.total_tutorial_flags
        if checkout_flag:
            play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
            python:
                local_config.total_tutorial_flags.remove("wind_battle_abyss")
        else:
            play music battle1 fadein 3.0 if_changed

        call battle(boss=boss_role,
                    boss_hp_plus=600 * team_average_level, 
                    side_enemy=side_roles, 
                    side_hp_plus=100 * team_average_level,
                    level=team_average_level,
                    boss_first=True, 
                    win_condition='wind-normal', 
                    stay_turn=0,
                    inside_label="inside_wind_battle_abyss" if checkout_flag else None, 
                    mission_type="equipment", 
                    treasures={"num7_03": (4, 0.6),
                               "num7_04": (2, 0.3),
                               "num9_03": (4, 0.6),
                               "num9_04": (2, 0.3),
                               "magic_wind_03": (4, 0.6),
                               "magic_wind_04": (2, 0.3),
                               "stone_wind_03": (4, 0.6),
                               "stone_wind_04": (2, 0.3)})

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day228.ritroom
