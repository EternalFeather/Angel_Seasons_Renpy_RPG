
# 金币副本
label battle_attack_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        python:
            if persistent.difficult != "easy":
                for role in local_config.party:
                    if role.name == "雷亚":
                        role.skills = [s if s.category != "General_attack" else before_battle_general_attack for s in role.skills]
                        role.skills_v2 = [s if s.category != "General_attack" else before_battle_general_attack_v2 for s in role.skills_v2]
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom


# 经验副本
label battle_protect_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        python:
            if persistent.difficult != "easy":
                for role in local_config.party:
                    if role.name == "雷亚":
                        role.skills = [s if s.category != "General_attack" else before_battle_general_attack for s in role.skills]
                        role.skills_v2 = [s if s.category != "General_attack" else before_battle_general_attack_v2 for s in role.skills_v2]
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom


# 突破材料副本
label battle_speed_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        python:
            if persistent.difficult != "easy":
                for role in local_config.party:
                    if role.name == "雷亚":
                        role.skills = [s if s.category != "General_attack" else before_battle_general_attack for s in role.skills]
                        role.skills_v2 = [s if s.category != "General_attack" else before_battle_general_attack_v2 for s in role.skills_v2]
                    # 蓄能恢复
                    role.skills = [s if s.category != "Recharge" else getattr(store, "guard") for s in role.skills]
                    role.skills_v2 = [s if s.category != "Recharge" else getattr(store, "guard") for s in role.skills_v2]
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom


# 装备副本-火
label battle_fire_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom


# 装备副本-雷
label battle_light_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom


# 装备副本-水
label battle_water_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom


# 装备副本-冰
label battle_ice_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom


# 装备副本-岩
label battle_rock_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom


# 装备副本-风
label battle_wind_209:
    menu:
        "简单（难度较小，奖励也较少）":
            $ persistent.difficult = 'easy'

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
            team_average_level = min(team_average_level - 3, 25)

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

    if _return == "win":
        "战斗胜利！"
        stop music fadeout 5.0
    else:
        jump battle_end

    jump day209.ritroom
