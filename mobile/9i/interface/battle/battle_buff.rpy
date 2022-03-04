
init python:
    class Buff(object):
        """
        Buff属性：名称、序号、种类、持续时间
        """
        def __init__(self, objectname="", name="", removeable=True, dtype="", info="", number=0):
            # 名称
            self.objectname = objectname
            self.original_name = objectname.capitalize().replace("_", " ")
            self.name = name
            # 序号
            self.number = int(number)
            # 种类
            self.type = dtype
            # 描述
            self.info = info
            # 是否可驱散
            self.removeable = True if removeable == "True" else False

        def calculate(self, target, ally_environment_effects, item, source, mode, **kargs):
            """
            Buff在战斗中的计算模式
            item值为：（time，value）
            source代表buff附加的来源（避免重复获取）
            mode分为：end、get、clean
            """
            # 获得状态的同时，结算所有增益、减益属性变化
            name = self.objectname
            dtype = self.type
            sources = local_config.buff_source[target.objectname]

            if mode == "get":
                time, value = item

                # 第一次获得状态
                if name not in target.debuff and name not in target.buff:
                    if dtype == "buff":
                        target.buff[name] = item
                    elif dtype == "debuff":
                        target.debuff[name] = item

                    # 来源标注
                    sources[name].add(source)
                    local_config.buff_source[target.objectname] = sources

                    # 若与属性有关的“需回溯”状态，则结算角色属性
                    ## Debuff区 
                    ## 虚弱(可为负)
                    if name == "weak":
                        target.temp_battle_extend_attack_down = int(target.battle_attack * value)
                        target.battle_extend_attack -= target.temp_battle_extend_attack_down
                    ## 破防
                    elif name == "exposed":
                        target.temp_battle_defance_down = value
                        target.battle_extend_defance -= target.temp_battle_defance_down
                    ## 减速
                    elif name == "slow":
                        target.temp_battle_speed_down = value
                        target.battle_speed -= target.temp_battle_speed_down
                    ## 残废
                    elif name == "powerless":
                        val1, val2 = value
                        target.temp_battle_critical_rate_down = val1
                        target.battle_critical_rate -= target.temp_battle_critical_rate_down
                        # if target.battle_critical_rate < 0:
                        #     target.battle_critical_rate = 0.0
                        target.temp_battle_critical_damage_down = val2
                        target.battle_critical_damage -= target.temp_battle_critical_damage_down
                        # if target.battle_critical_damage < 0:
                        #     target.battle_critical_damage = 0.0
                    ## 封印
                    elif name == "seal":
                        target.temp_battle_effect_hitrate_down = value
                        target.battle_effect_hitrate -= target.temp_battle_effect_hitrate_down
                        # if target.battle_effect_hitrate < 0:
                        #     target.battle_effect_hitrate = 0.0
                    ## 崩解
                    elif name == "disintegrate":
                        target.temp_battle_effect_resistance_down = value
                        target.battle_effect_resistance -= target.temp_battle_effect_resistance_down
                        # if target.battle_effect_resistance < 0:
                        #     target.battle_effect_resistance = 0.0
                    ## 流失
                    elif name == "churn":
                        target.temp_battle_elemental_mastery_down = value
                        target.battle_elemental_mastery -= target.temp_battle_elemental_mastery_down
                        # if target.battle_elemental_mastery < 0:
                        #     target.battle_elemental_mastery = 0
                    ## 重伤
                    elif name == "handicapped":
                        target.temp_battle_healing_bonus_down = value
                        target.battle_healing_bonus -= target.temp_battle_healing_bonus_down
                        # if target.battle_healing_bonus < 0:
                        #     target.battle_healing_bonus = 0.0
                    ## 破碎
                    elif name == "broken":
                        target.temp_battle_shield_strength_down = value
                        target.battle_shield_strength -= target.temp_battle_shield_strength_down
                        # if target.battle_shield_strength < 0:
                        #     target.battle_shield_strength = 0.0
                    ## 枯萎
                    elif name == "withered":
                        val1, val2, val3, val4, val5, val6, val7 = value
                        target.temp_battle_fire_damage_bonus_down = val1
                        target.battle_fire_damage_bonus -= target.temp_battle_fire_damage_bonus_down
                        # if target.battle_fire_damage_bonus < 0:
                        #     target.battle_fire_damage_bonus = 0.0
                        target.temp_battle_light_damage_bonus_down = val2
                        target.battle_light_damage_bonus -= target.temp_battle_light_damage_bonus_down
                        # if target.battle_light_damage_bonus < 0:
                        #     target.battle_light_damage_bonus = 0.0
                        target.temp_battle_wind_damage_bonus_down = val3
                        target.battle_wind_damage_bonus -= target.temp_battle_wind_damage_bonus_down
                        # if target.battle_wind_damage_bonus < 0:
                        #     target.battle_wind_damage_bonus = 0.0
                        target.temp_battle_ice_damage_bonus_down = val4
                        target.battle_ice_damage_bonus -= target.temp_battle_ice_damage_bonus_down
                        # if target.battle_ice_damage_bonus < 0:
                        #     target.battle_ice_damage_bonus = 0.0
                        target.temp_battle_water_damage_bonus_down = val5
                        target.battle_water_damage_bonus -= target.temp_battle_water_damage_bonus_down
                        # if target.battle_water_damage_bonus < 0:
                        #     target.battle_water_damage_bonus = 0.0
                        target.temp_battle_rock_damage_bonus_down = val6
                        target.battle_rock_damage_bonus -= target.temp_battle_rock_damage_bonus_down
                        # if target.battle_rock_damage_bonus < 0:
                        #     target.battle_rock_damage_bonus = 0.0
                        target.temp_battle_physical_damage_bonus_down = val7
                        target.battle_physical_damage_bonus -= target.temp_battle_physical_damage_bonus_down
                        # if target.battle_physical_damage_bonus < 0:
                        #     target.battle_physical_damage_bonus = 0.0
                    ## 压制(可为负)
                    elif name == "suppress":
                        val1, val2, val3, val4, val5, val6, val7 = value
                        target.temp_battle_fire_elemental_resistance_down = val1
                        target.battle_fire_elemental_resistance -= target.temp_battle_fire_elemental_resistance_down
                        target.temp_battle_light_elemental_resistance_down = val2
                        target.battle_light_elemental_resistance -= target.temp_battle_light_elemental_resistance_down
                        target.temp_battle_wind_elemental_resistance_down = val3
                        target.battle_wind_elemental_resistance -= target.temp_battle_wind_elemental_resistance_down
                        target.temp_battle_ice_elemental_resistance_down = val4
                        target.battle_ice_elemental_resistance -= target.temp_battle_ice_elemental_resistance_down
                        target.temp_battle_water_elemental_resistance_down = val5
                        target.battle_water_elemental_resistance -= target.temp_battle_water_elemental_resistance_down
                        target.temp_battle_rock_elemental_resistance_down = val6
                        target.battle_rock_elemental_resistance -= target.temp_battle_rock_elemental_resistance_down
                        target.temp_battle_physical_elemental_resistance_down = val7
                        target.battle_physical_elemental_resistance -= target.temp_battle_physical_elemental_resistance_down
                    ## Buff区
                    ## 强壮
                    elif name in ["strong", "strong_attack", "strong_speed", "strong_enemy", "strong_ally"]:
                        target.temp_battle_extend_attack_up = int(target.battle_attack * value)
                        target.battle_extend_attack += target.temp_battle_extend_attack_up
                    ## 坚固
                    elif name == "sturdy":
                        target.temp_battle_defance_up = value
                        target.battle_extend_defance += target.temp_battle_defance_up
                    ## 轻盈
                    elif name in ["flow", "flow_speed", "flow_enemy", "flow_ally"]:
                        target.temp_battle_speed_up = value
                        target.battle_speed += target.temp_battle_speed_up
                        if target.battle_speed >= 1000:
                            target.battle_speed = 999
                    ## 圣裁
                    elif name in ["violence", "violence_attack", "violence_speed", "violence_enemy", "violence_ally"]:
                        val1, val2 = value
                        target.temp_battle_critical_rate_up = val1
                        target.battle_critical_rate += target.temp_battle_critical_rate_up
                        target.temp_battle_critical_damage_up = val2
                        target.battle_critical_damage += target.temp_battle_critical_damage_up
                    ## 解放
                    elif name == "liberate":
                        target.temp_battle_effect_hitrate_up = value
                        target.battle_effect_hitrate += target.temp_battle_effect_hitrate_up
                    ## 法障
                    elif name == "barrier":
                        target.temp_battle_effect_resistance_up = value
                        target.battle_effect_resistance += target.temp_battle_effect_resistance_up
                    ## 掌握
                    elif name == "master":
                        target.temp_battle_elemental_mastery_up = value
                        target.battle_elemental_mastery += target.temp_battle_elemental_mastery_up
                    ## 庇护
                    elif name == "healing":
                        target.temp_battle_healing_bonus_up = value
                        target.battle_healing_bonus += target.temp_battle_healing_bonus_up
                    ## 体甲
                    elif name == "armor":
                        target.temp_battle_shield_strength_up = value
                        target.battle_shield_strength += target.temp_battle_shield_strength_up
                    ## 凝息
                    elif name == "condensed":
                        val1, val2, val3, val4, val5, val6, val7 = value
                        target.temp_battle_fire_damage_bonus_up = val1
                        target.battle_fire_damage_bonus += target.temp_battle_fire_damage_bonus_up
                        target.temp_battle_light_damage_bonus_up = val2
                        target.battle_light_damage_bonus += target.temp_battle_light_damage_bonus_up
                        target.temp_battle_wind_damage_bonus_up = val3
                        target.battle_wind_damage_bonus += target.temp_battle_wind_damage_bonus_up
                        target.temp_battle_ice_damage_bonus_up = val4
                        target.battle_ice_damage_bonus += target.temp_battle_ice_damage_bonus_up
                        target.temp_battle_water_damage_bonus_up = val5
                        target.battle_water_damage_bonus += target.temp_battle_water_damage_bonus_up
                        target.temp_battle_rock_damage_bonus_up = val6
                        target.battle_rock_damage_bonus += target.temp_battle_rock_damage_bonus_up
                        target.temp_battle_physical_damage_bonus_up = val7
                        target.battle_physical_damage_bonus += target.temp_battle_physical_damage_bonus_up
                    ## 御灵
                    elif name == "control":
                        val1, val2, val3, val4, val5, val6, val7 = value
                        target.temp_battle_fire_elemental_resistance_up = val1
                        target.battle_fire_elemental_resistance += target.temp_battle_fire_elemental_resistance_up
                        target.temp_battle_light_elemental_resistance_up = val2
                        target.battle_light_elemental_resistance += target.temp_battle_light_elemental_resistance_up
                        target.temp_battle_wind_elemental_resistance_up = val3
                        target.battle_wind_elemental_resistance += target.temp_battle_wind_elemental_resistance_up
                        target.temp_battle_ice_elemental_resistance_up = val4
                        target.battle_ice_elemental_resistance += target.temp_battle_ice_elemental_resistance_up
                        target.temp_battle_water_elemental_resistance_up = val5
                        target.battle_water_elemental_resistance += target.temp_battle_water_elemental_resistance_up
                        target.temp_battle_rock_elemental_resistance_up = val6
                        target.battle_rock_elemental_resistance += target.temp_battle_rock_elemental_resistance_up
                        target.temp_battle_physical_elemental_resistance_up = val7
                        target.battle_physical_elemental_resistance += target.temp_battle_physical_elemental_resistance_up
                    ## 破魔
                    elif name == "lost" or name == "sp_lost":
                        # 被动技能设定失效
                        if target.is_phase2:
                            skills = target.skills_v2
                        else:
                            skills = target.skills
                        for skill in skills:
                            if skill.category == "Passive":
                                skill.selectable = False
                                passive_skill = skill
                                break
                        
                        if (passive_skill.name, True) in ally_environment_effects:
                            ally_environment_effects.remove((passive_skill.name, True))
                            ally_environment_effects.add((passive_skill.name, False))
                        # 装备4件套装失效
                        target.equip4effect_availabel = False
                        if (target.equip4effect, True) in ally_environment_effects:
                            ally_environment_effects.remove((target.equip4effect, True))
                            ally_environment_effects.add((target.equip4effect, False))
                    # 眩晕
                    elif name == "dizziness":
                        target.moveable = False
                    # 冻结
                    elif name == "frozen":
                        target.moveable = False
                    # 深度冰冻
                    elif name == "deep_frozen":
                        # 解除普通冰冻
                        buff_obj = getattr(store, "frozen")
                        buff_obj.calculate(target, None, None, None, "clean")
                        # 加入减少30点速度
                        target.battle_speed -= 30
                    # 沉睡
                    elif name == "sleepy":
                        target.moveable = False
                    # 深度沉睡
                    elif name == "deep_sleepy":
                        target.moveable = False
                    # 沉默
                    elif name == "silence":
                        # 主动技能不可选择
                        if target.is_phase2:
                            skills = target.skills_v2
                        else:
                            skills = target.skills
                        for skill in skills:
                            if skill.category in ["Combat_skills", "Break_out"]:
                                skill.selectable = False
                    # 嘲讽
                    elif name == "ridicule":
                        # 强制选择目标
                        target.selected_target = kargs["user"]
                    # 护盾
                    elif name == "shield" or name == "sp_shield":
                        _, element, _, _ = value
                        if element not in target.ebuff and source != "波纹裂隙" and element not in ["wind", "rock", "physical"]:
                            target.ebuff = {element: 1}
                    # 间接伤害
                    elif name == "mdamage":
                        buff_roles = local_config.skill_log_data.setdefault("间接伤害", {})
                        mdmg, mkind, mreson, muser = value
                        buff_roles[target] = {mkind: value}
                # 重复获得状态（效果叠加 & 时间稀释）
                else:
                    if name == "ghost_mask":
                        buff_time, buff_effect = target.buff[name]
                        if buff_effect < 9:
                            new_value = buff_effect + value
                            # 当携带的“鬼面”达到9层上限时，解除自身所有控制效果并增加35%行动条
                            if ("积重鬼怨", True) in ally_environment_effects and new_value == 9:
                                for buff_name in ["silence", "dizziness", "confusion", "frozen", "sleepy", "ridicule", "deep_frozen", "deep_sleepy"]:
                                    if buff_name in target.debuff:
                                        buff_obj = getattr(store, buff_name)
                                        buff_obj.calculate(target, ally_environment_effects, None, None, "clean")
                                target.order += 350
                                renpy.show("buff_effect", at_list=[show_state(target.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
                        else:
                            new_value = buff_effect
                        target.buff[name] = (buff_time, new_value)
                    elif name == "yi":
                        buff_time, buff_effect = target.buff[name]
                        new_value = buff_effect + value
                        target.buff[name] = (buff_time, new_value)
                    elif name == "love":
                        buff_time, buff_effect = target.buff[name]
                        if buff_effect < 9:
                            new_value = buff_effect + value
                            target.buff[name] = (buff_time, new_value)
                    elif "star_bridge" in name or (name in ["ethereal", "heart_main"]):
                        buff_time, buff_effect = target.buff[name]
                        target.buff[name] = (max(time, buff_time), buff_effect)

                        sources[name].add(source)
                        local_config.buff_source[target.objectname] = sources
                    # 如果效果未获取过
                    elif source is None or source not in sources[name]:
                        if dtype == "buff":
                            if name != "shield" and name != "sp_shield":
                                buff_time, buff_effect = target.buff[name]
                                if isinstance(buff_effect, tuple) or isinstance(buff_effect, list) or isinstance(buff_effect, set):
                                    new_value = tuple()
                                    for val_old, val_new in zip(buff_effect, value):
                                        if isinstance(val_old, int) or isinstance(val_old, float):
                                            new_value += (val_old + val_new,)
                                        else:
                                            new_value += (val_old,)
                                else:
                                    new_value = buff_effect + value
                                if name in ["strong_attack", "violence_attack", "strong_speed", "violence_speed", "flow_speed", "strong_enemy", "violence_enemy", "flow_enemy", "strong_ally", "violence_ally", "flow_ally"]:
                                    target.buff[name] = (buff_time, new_value)
                                else:
                                    target.buff[name] = (min(buff_time, time, 9), new_value)
                            else:
                                # 护盾受到伤害
                                if source is None:
                                    new_value = value
                                    
                                    # 护盾消失
                                    if new_value[0] <= 0:
                                        if "shield" in target.buff:
                                            shield_buff = getattr(store, "shield")
                                            shield_buff.calculate(target, None, None, None, "clean")
                                        elif "sp_shield" in target.buff:
                                            shield_buff = getattr(store, "sp_shield")
                                            shield_buff.calculate(target, None, None, None, "clean")
                                    else:
                                        target.buff[name] = (time, new_value)
                                # 同属性叠加，异属性替换
                                else:
                                    if "shield" in target.buff:
                                        shield_time, (shield_strength, shield_element, vo1, vo2) = target.buff["shield"]
                                        new_shield_strength, new_shield_element, v1, v2 = value
                                        if shield_element == new_shield_element:
                                            new_value = (shield_time, (shield_strength + new_shield_strength, shield_element, v1, v2))
                                        else:
                                            new_value = value
                                    elif "sp_shield" in target.buff:
                                        shield_time, (shield_strength, shield_element, vo1, vo2) = target.buff["sp_shield"]
                                        new_shield_strength, new_shield_element, v1, v2 = value
                                        if shield_element == new_shield_element:
                                            new_value = (shield_time, (shield_strength + new_shield_strength, shield_element, v1, v2))
                                        else:
                                            new_value = value
                                    else:
                                        new_value = value
                                    target.buff[name] = (time, new_value)
                        elif dtype == "debuff":
                            buff_time, buff_effect = target.debuff[name]
                            if isinstance(buff_effect, tuple) or isinstance(buff_effect, list) or isinstance(buff_effect, set):
                                new_value = tuple()
                                for val_old, val_new in zip(buff_effect, value):
                                    if isinstance(val_old, int) or isinstance(val_old, float):
                                        new_value += (val_old + val_new,)
                                    else:
                                        new_value += (val_old,)
                            else:
                                if buff_effect is not None:
                                    new_value = buff_effect + value
                                else:
                                    new_value = None
                            target.debuff[name] = (min(buff_time, time, 9), new_value)

                        # 来源标注
                        sources[name].add(source)
                        local_config.buff_source[target.objectname] = sources

                        # 若与属性有关的“需回溯”状态，则结算角色属性
                        target.back_param(name, reset=False)
                        ## Debuff区
                        ## 虚弱(可为负)
                        if name == "weak":
                            target.temp_battle_extend_attack_down += int(target.battle_attack * value)
                            target.battle_extend_attack -= target.temp_battle_extend_attack_down
                        ## 破防
                        elif name == "exposed":
                            target.temp_battle_defance_down += value
                            target.battle_extend_defance -= target.temp_battle_defance_down
                        ## 减速
                        elif name == "slow":
                            target.temp_battle_speed_down += value
                            target.battle_speed -= target.temp_battle_speed_down
                        ## 残废
                        elif name == "powerless":
                            val1, val2 = value
                            target.temp_battle_critical_rate_down += val1
                            target.battle_critical_rate -= target.temp_battle_critical_rate_down
                            # if target.battle_critical_rate < 0:
                            #     target.battle_critical_rate = 0.0
                            target.temp_battle_critical_damage_down += val2
                            target.battle_critical_damage -= target.temp_battle_critical_damage_down
                            # if target.battle_critical_damage < 0:
                            #     target.battle_critical_damage = 0.0
                        ## 封印
                        elif name == "seal":
                            target.temp_battle_effect_hitrate_down += value
                            target.battle_effect_hitrate -= target.temp_battle_effect_hitrate_down
                            # if target.battle_effect_hitrate < 0:
                            #     target.battle_effect_hitrate = 0.0
                        ## 崩解
                        elif name == "disintegrate":
                            target.temp_battle_effect_resistance_down += value
                            target.battle_effect_resistance -= target.temp_battle_effect_resistance_down
                            # if target.battle_effect_resistance < 0:
                            #     target.battle_effect_resistance = 0.0
                        ## 流失
                        elif name == "churn":
                            target.temp_battle_elemental_mastery_down += value
                            target.battle_elemental_mastery -= target.temp_battle_elemental_mastery_down
                            # if target.battle_elemental_mastery < 0:
                            #     target.battle_elemental_mastery = 0
                        ## 重伤
                        elif name == "handicapped":
                            target.temp_battle_healing_bonus_down += value
                            target.battle_healing_bonus -= target.temp_battle_healing_bonus_down
                            # if target.battle_healing_bonus < 0:
                            #     target.battle_healing_bonus = 0.0
                        ## 破碎
                        elif name == "broken":
                            target.temp_battle_shield_strength_down += value
                            target.battle_shield_strength -= target.temp_battle_shield_strength_down
                            # if target.battle_shield_strength < 0:
                            #     target.battle_shield_strength = 0.0
                        ## 枯萎
                        elif name == "withered":
                            val1, val2, val3, val4, val5, val6, val7 = value
                            target.temp_battle_fire_damage_bonus_down += val1
                            target.battle_fire_damage_bonus -= target.temp_battle_fire_damage_bonus_down
                            # if target.battle_fire_damage_bonus < 0:
                            #     target.battle_fire_damage_bonus = 0.0
                            target.temp_battle_light_damage_bonus_down += val2
                            target.battle_light_damage_bonus -= target.temp_battle_light_damage_bonus_down
                            # if target.battle_light_damage_bonus < 0:
                            #     target.battle_light_damage_bonus = 0.0
                            target.temp_battle_wind_damage_bonus_down += val3
                            target.battle_wind_damage_bonus -= target.temp_battle_wind_damage_bonus_down
                            # if target.battle_wind_damage_bonus < 0:
                            #     target.battle_wind_damage_bonus = 0.0
                            target.temp_battle_ice_damage_bonus_down += val4
                            target.battle_ice_damage_bonus -= target.temp_battle_ice_damage_bonus_down
                            # if target.battle_ice_damage_bonus < 0:
                            #     target.battle_ice_damage_bonus = 0.0
                            target.temp_battle_water_damage_bonus_down += val5
                            target.battle_water_damage_bonus -= target.temp_battle_water_damage_bonus_down
                            # if target.battle_water_damage_bonus < 0:
                            #     target.battle_water_damage_bonus = 0.0
                            target.temp_battle_rock_damage_bonus_down += val6
                            target.battle_rock_damage_bonus -= target.temp_battle_rock_damage_bonus_down
                            # if target.battle_rock_damage_bonus < 0:
                            #     target.battle_rock_damage_bonus = 0.0
                            target.temp_battle_physical_damage_bonus_down += val7
                            target.battle_physical_damage_bonus -= target.temp_battle_physical_damage_bonus_down
                            # if target.battle_physical_damage_bonus < 0:
                            #     target.battle_physical_damage_bonus = 0.0
                        ## 压制(可为负)
                        elif name == "suppress":
                            val1, val2, val3, val4, val5, val6, val7 = value
                            target.temp_battle_fire_elemental_resistance_down += val1
                            target.battle_fire_elemental_resistance -= target.temp_battle_fire_elemental_resistance_down
                            target.temp_battle_light_elemental_resistance_down += val2
                            target.battle_light_elemental_resistance -= target.temp_battle_light_elemental_resistance_down
                            target.temp_battle_wind_elemental_resistance_down += val3
                            target.battle_wind_elemental_resistance -= target.temp_battle_wind_elemental_resistance_down
                            target.temp_battle_ice_elemental_resistance_down += val4
                            target.battle_ice_elemental_resistance -= target.temp_battle_ice_elemental_resistance_down
                            target.temp_battle_water_elemental_resistance_down += val5
                            target.battle_water_elemental_resistance -= target.temp_battle_water_elemental_resistance_down
                            target.temp_battle_rock_elemental_resistance_down += val6
                            target.battle_rock_elemental_resistance -= target.temp_battle_rock_elemental_resistance_down
                            target.temp_battle_physical_elemental_resistance_down += val7
                            target.battle_physical_elemental_resistance -= target.temp_battle_physical_elemental_resistance_down
                        ## Buff区
                        ## 强壮
                        elif name in ["strong", "strong_attack", "strong_speed", "strong_enemy", "strong_ally"]:
                            target.temp_battle_extend_attack_up += int(target.battle_attack * value)
                            target.battle_extend_attack += target.temp_battle_extend_attack_up
                        ## 坚固
                        elif name == "sturdy":
                            target.temp_battle_defance_up += value
                            target.battle_extend_defance += target.temp_battle_defance_up
                        ## 轻盈
                        elif name in ["flow", "flow_speed", "flow_enemy", "flow_ally"]:
                            target.temp_battle_speed_up += value
                            target.battle_speed += target.temp_battle_speed_up
                            if target.battle_speed >= 1000:
                                target.battle_speed = 999
                        ## 圣裁
                        elif name in ["violence", "violence_attack", "violence_speed", "violence_enemy", "violence_ally"]:
                            val1, val2 = value
                            target.temp_battle_critical_rate_up += val1
                            target.battle_critical_rate += target.temp_battle_critical_rate_up
                            target.temp_battle_critical_damage_up += val2
                            target.battle_critical_damage += target.temp_battle_critical_damage_up
                        ## 解放
                        elif name == "liberate":
                            target.temp_battle_effect_hitrate_up += value
                            target.battle_effect_hitrate += target.temp_battle_effect_hitrate_up
                        ## 法障
                        elif name == "barrier":
                            target.temp_battle_effect_resistance_up += value
                            target.battle_effect_resistance += target.temp_battle_effect_resistance_up
                        ## 掌握
                        elif name == "master":
                            target.temp_battle_elemental_mastery_up += value
                            target.battle_elemental_mastery += target.temp_battle_elemental_mastery_up
                        ## 庇护
                        elif name == "healing":
                            target.temp_battle_healing_bonus_up += value
                            target.battle_healing_bonus += target.temp_battle_healing_bonus_up
                        ## 体甲
                        elif name == "armor":
                            target.temp_battle_shield_strength_up += value
                            target.battle_shield_strength += target.temp_battle_shield_strength_up
                        ## 凝息
                        elif name == "condensed":
                            val1, val2, val3, val4, val5, val6, val7 = value
                            target.temp_battle_fire_damage_bonus_up += val1
                            target.battle_fire_damage_bonus += target.temp_battle_fire_damage_bonus_up
                            target.temp_battle_light_damage_bonus_up += val2
                            target.battle_light_damage_bonus += target.temp_battle_light_damage_bonus_up
                            target.temp_battle_wind_damage_bonus_up += val3
                            target.battle_wind_damage_bonus += target.temp_battle_wind_damage_bonus_up
                            target.temp_battle_ice_damage_bonus_up += val4
                            target.battle_ice_damage_bonus += target.temp_battle_ice_damage_bonus_up
                            target.temp_battle_water_damage_bonus_up += val5
                            target.battle_water_damage_bonus += target.temp_battle_water_damage_bonus_up
                            target.temp_battle_rock_damage_bonus_up += val6
                            target.battle_rock_damage_bonus += target.temp_battle_rock_damage_bonus_up
                            target.temp_battle_physical_damage_bonus_up += val7
                            target.battle_physical_damage_bonus += target.temp_battle_physical_damage_bonus_up
                        ## 御灵
                        elif name == "control":
                            val1, val2, val3, val4, val5, val6, val7 = value
                            target.temp_battle_fire_elemental_resistance_up += val1
                            target.battle_fire_elemental_resistance += target.temp_battle_fire_elemental_resistance_up
                            target.temp_battle_light_elemental_resistance_up += val2
                            target.battle_light_elemental_resistance += target.temp_battle_light_elemental_resistance_up
                            target.temp_battle_wind_elemental_resistance_up += val3
                            target.battle_wind_elemental_resistance += target.temp_battle_wind_elemental_resistance_up
                            target.temp_battle_ice_elemental_resistance_up += val4
                            target.battle_ice_elemental_resistance += target.temp_battle_ice_elemental_resistance_up
                            target.temp_battle_water_elemental_resistance_up += val5
                            target.battle_water_elemental_resistance += target.temp_battle_water_elemental_resistance_up
                            target.temp_battle_rock_elemental_resistance_up += val6
                            target.battle_rock_elemental_resistance += target.temp_battle_rock_elemental_resistance_up
                            target.temp_battle_physical_elemental_resistance_up += val7
                            target.battle_physical_elemental_resistance += target.temp_battle_physical_elemental_resistance_up  
                        ## 破魔
                        elif name == "lost" or name == "sp_lost":
                            # 被动技能设定失效
                            if target.is_phase2:
                                skills = target.skills_v2
                            else:
                                skills = target.skills
                            for skill in skills:
                                if skill.category == "Passive":
                                    skill.selectable = False
                                    passive_skill = skill
                                    break
                            
                            if (passive_skill.name, True) in ally_environment_effects:
                                ally_environment_effects.remove((passive_skill.name, True))
                                ally_environment_effects.add((passive_skill.name, False))
                            # 装备4件套装失效
                            target.equip4effect_availabel = False
                            if (target.equip4effect, True) in ally_environment_effects:
                                ally_environment_effects.remove((target.equip4effect, True))
                                ally_environment_effects.add((target.equip4effect, False))
                        # 眩晕
                        elif name == "dizziness":
                            target.moveable = False
                        # 冻结
                        elif name == "frozen":
                            target.moveable = False
                        # 深度冰冻
                        elif name == "deep_frozen":
                            # 解除普通冰冻
                            buff_obj = getattr(store, "frozen")
                            buff_obj.calculate(target, None, None, None, "clean")
                            # 加入减少30点速度
                            target.battle_speed -= 30
                        # 沉睡
                        elif name == "sleepy":
                            target.moveable = False
                        # 深度沉睡
                        elif name == "deep_sleepy":
                            target.moveable = False
                        # 沉默
                        elif name == "silence":
                            # 主动技能不可选择
                            if target.is_phase2:
                                skills = target.skills_v2
                            else:
                                skills = target.skills
                            for skill in skills:
                                if skill.category in ["Combat_skills", "Break_out"]:
                                    skill.selectable = False
                        # 嘲讽
                        elif name == "ridicule":
                            # 强制选择目标
                            target.selected_target = kargs["user"]
                        # 间接伤害
                        elif name == "mdamage":
                            mdmg, mkind, mreson, muser = value
                            buff_roles = local_config.skill_log_data.setdefault("间接伤害", {})
                            if mkind in buff_roles[target]:
                                old_value = buff_roles[target][mkind]
                                buff_roles[target][mkind] = (max(old_value[0], mdmg), mkind, mreson, muser)
                            else:
                                buff_roles[target][mkind] = value

            # 回合结束的同时，结算buff持续时间，清算buff后恢复属性变化
            elif mode == "end":
                if dtype == "buff" and name in target.buff:
                    buff_time, buff_effect = target.buff[name]
                elif dtype == "debuff" and name in target.debuff:
                    buff_time, buff_effect = target.debuff[name]

                if buff_time != 99:
                    buff_time -= 1

                if "star_bridge" in name and "空间跳跃" in local_config.skill_log_data:
                    buff_roles_2 = local_config.skill_log_data["空间跳跃"]
                    if target in buff_roles_2:
                        buff_roles_2[target] -= 1
                        if buff_roles_2[target] == 0:
                            buff_roles_2.pop(target)
                    if len(local_config.skill_log_data["空间跳跃"]) == 0:
                        local_config.skill_log_data.pop("空间跳跃")
                        renpy.hide("fight_cg-bg star_bridge", layer="bg2")

                # 如果buff效果时间到，将其移除并恢复属性
                if buff_time == 0:
                    if dtype == "buff":
                        target.buff.pop(name)
                    elif dtype == "debuff":
                        target.debuff.pop(name)

                    target.back_param(name)

                    # 来源清算
                    sources[name] = set()
                    local_config.buff_source[target.objectname] = sources

                    # 破魔
                    if (name == "lost" or name == "sp_lost") and local_config.tutorial_step != "winter_loss_stage":
                        # 被动技能设定有效
                        if target.is_phase2:
                            skills = target.skills_v2
                        else:
                            skills = target.skills
                        for skill in skills:
                            if skill.category == "Passive":
                                skill.selectable = True
                                passive_skill = skill
                                break

                        if (passive_skill.name, False) in ally_environment_effects:
                            ally_environment_effects.remove((passive_skill.name, False))
                            ally_environment_effects.add((passive_skill.name, True))
                        # 装备4件套装有效
                        target.equip4effect_availabel = True
                        if (target.equip4effect, False) in ally_environment_effects:
                            ally_environment_effects.remove((target.equip4effect, False))
                            ally_environment_effects.add((target.equip4effect, True))
                    # 眩晕
                    elif name == "dizziness":
                        target.moveable = True
                    # 冻结
                    elif name == "frozen":
                        target.moveable = True
                    # 深度冰冻
                    elif name == "deep_frozen":
                        # 恢复30点速度
                        target.battle_speed += 30
                        if target.battle_speed >= 1000:
                            target.battle_speed = 999
                    # 沉睡
                    elif name == "sleepy":
                        target.moveable = True
                    # 深度沉睡
                    elif name == "deep_sleepy":
                        target.moveable = True
                    # 沉默
                    elif name == "silence":
                        # 主动技能可选择
                        if target.is_phase2:
                            skills = target.skills_v2
                        else:
                            skills = target.skills
                        for skill in skills:
                            if skill.category in ["Combat_skills", "Break_out"]:
                                skill.selectable = True
                    # 咒
                    elif name == "curse":
                        # 咒术清空
                        _, _, _, curse_role = local_config.skill_log_data["咒"].pop(target)
                        local_config.skill_log_data["咒"].pop(curse_role)
                        if len(local_config.skill_log_data["咒"]) == 0:
                            local_config.skill_log_data.pop("咒")
                        # debuff解除
                        decurse = getattr(store, "decurse")
                        decurse.calculate(curse_role, None, None, None, "clean")
                    # 星桥消除
                    elif name == "star_bridge" or name == "star_bridge_done":
                        buff_roles = local_config.skill_log_data["星空梦影"]
                        if target in buff_roles:
                            buff_roles.pop(target)
                        if len(local_config.skill_log_data["星空梦影"]) == 0:
                            local_config.skill_log_data.pop("星空梦影")
                    # 空灵解除
                    elif name == "ethereal":
                        if "sp_domineering" in target.buff:
                            sp_domineering = getattr(store, "sp_domineering")
                            sp_domineering.calculate(target, None, None, None, "clean")
                        # 形态回硕
                        target.is_phase2 = False
                        if "幻镜化物-pose" in local_config.skill_log_data:
                            buff_roles = local_config.skill_log_data["幻镜化物-pose"]
                            for u, p in buff_roles:
                                if u == target:
                                    u.pose = p
                                    buff_roles.remove((u, p))
                                    break
                            if len(buff_roles) == 0:
                                local_config.skill_log_data.pop("幻镜化物-pose")
                    # 心解除
                    elif name == "heart_main":
                        if target in local_config.party and "共感" in local_config.skill_log_data:
                            buff_roles = local_config.skill_log_data["共感"].pop("ally")
                            for role in buff_roles:
                                if role != target and "heart" in role.buff:
                                    buff_obj = getattr(store, "heart")
                                    buff_obj.calculate(role, None, None, None, "clean")
                            if len(local_config.skill_log_data["共感"]) == 0:
                                local_config.skill_log_data.pop("共感")
                        elif target in local_config.enemy and "共感" in local_config.skill_log_data:
                            buff_roles = local_config.skill_log_data["共感"].pop("enemy")
                            for role in buff_roles:
                                if role != target and "heart" in role.buff:
                                    buff_obj = getattr(store, "heart")
                                    buff_obj.calculate(role, None, None, None, "clean")
                            if len(local_config.skill_log_data["共感"]) == 0:
                                local_config.skill_log_data.pop("共感")
                    # 间接伤害
                    elif name == "mdamage":
                        if "间接伤害" in local_config.skill_log_data:
                            local_config.skill_log_data["间接伤害"].pop(target)
                            if len(local_config.skill_log_data["间接伤害"]) == 0:
                                local_config.skill_log_data.pop("间接伤害")
                else:
                    if buff_time != 99 and dtype == "buff":
                        target.buff[name] = (buff_time, buff_effect)
                    elif buff_time != 99 and dtype == "debuff":
                        target.debuff[name] = (buff_time, buff_effect)

            # 强制清除buff(驱散)
            elif mode == "clean":
                if dtype == "buff" and name in target.buff:
                    temp_buff_times, _ = target.buff[name]
                    target.buff.pop(name)
                elif dtype == "debuff" and name in target.debuff:
                    target.debuff.pop(name)
                    
                target.back_param(name)
                
                # 来源清算
                sources[name] = set()
                local_config.buff_source[target.objectname] = sources

                # 破魔
                if (name == "lost" or name == "sp_lost") and local_config.tutorial_step != "winter_loss_stage":
                    # 被动技能设定时效
                    if target.is_phase2:
                        skills = target.base_skills_v2
                    else:
                        skills = target.base_skills
                    for skill in skills:
                        if skill.category == "Passive":
                            skill.selectable = True
                            passive_skill = skill
                            break

                    if (passive_skill.name, False) in ally_environment_effects:
                        ally_environment_effects.remove((passive_skill.name, False))
                        ally_environment_effects.add((passive_skill.name, True))
                    # 装备4件套装有效
                    target.equip4effect_availabel = True
                    if (target.equip4effect, False) in ally_environment_effects:
                        ally_environment_effects.remove((target.equip4effect, False))
                        ally_environment_effects.add((target.equip4effect, True))
                # 眩晕
                elif name == "dizziness":
                    target.moveable = True
                # 冻结
                elif name == "frozen":
                    target.moveable = True
                # 深度冰冻
                elif name == "deep_frozen":
                    # 恢复30点速度
                    target.battle_speed += 30
                # 沉睡
                elif name == "sleepy":
                    target.moveable = True
                # 深度沉睡
                elif name == "deep_sleepy":
                    target.moveable = True
                # 沉默
                elif name == "silence":
                    # 主动技能不可选择
                    if target.is_phase2:
                        skills = target.skills_v2
                    else:
                        skills = target.skills
                    for skill in skills:
                        if skill.category in ["Combat_skills", "Break_out"]:
                            skill.selectable = True
                # 咒
                elif name == "curse":
                    # 咒术清空
                    _, _, _, curse_role = local_config.skill_log_data["咒"].pop(target)
                    local_config.skill_log_data["咒"].pop(curse_role)
                    if len(local_config.skill_log_data["咒"]) == 0:
                        local_config.skill_log_data.pop("咒")
                    # debuff解除
                    if "decurse" in curse_role.debuff:
                        decurse = getattr(store, "decurse")
                        decurse.calculate(curse_role, None, None, None, "clean")
                # 星桥转化
                elif name == "star_bridge" and source == "done":
                    buff_roles = local_config.skill_log_data["星空梦影"]
                    _, buff_user = buff_roles[target]
                    buff_roles[target] = (False, buff_user)
                    # 加入星桥done
                    star_done = getattr(store, "star_bridge_done")
                    item = (temp_buff_times, None)
                    star_done.calculate(target, None, item, "星空梦影", "get")
                # 星桥
                elif name == "star_bridge" or name == "star_bridge_done":
                    buff_roles = local_config.skill_log_data["星空梦影"]
                    if target in buff_roles:
                        buff_roles.pop(target)
                    if len(local_config.skill_log_data["星空梦影"]) == 0:
                        local_config.skill_log_data.pop("星空梦影")

                    if "空间跳跃" in local_config.skill_log_data:
                        buff_roles_2 = local_config.skill_log_data["空间跳跃"]
                        if target in buff_roles_2:
                            buff_roles_2.pop(target)
                        if len(local_config.skill_log_data["空间跳跃"]) == 0:
                            local_config.skill_log_data.pop("空间跳跃")
                            renpy.hide("fight_cg-bg star_bridge", layer="bg2")
                # 空灵解除
                elif name == "ethereal":
                    if "sp_domineering" in target.buff:
                        sp_domineering = getattr(store, "sp_domineering")
                        sp_domineering.calculate(target, None, None, None, "clean")
                    # 形态回硕
                    target.is_phase2 = False
                    if "幻镜化物-pose" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["幻镜化物-pose"]
                        for u, p in buff_roles:
                            if u == target:
                                u.pose = p
                                buff_roles.remove((u, p))
                                break
                        if len(buff_roles) == 0:
                            local_config.skill_log_data.pop("幻镜化物-pose")
                # 心解除
                elif name == "heart_main":
                    if target in local_config.party and "共感" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["共感"].pop("ally")
                        for role in buff_roles:
                            if role != target and "heart" in role.buff:
                                buff_obj = getattr(store, "heart")
                                buff_obj.calculate(role, None, None, None, "clean")
                        if len(local_config.skill_log_data["共感"]) == 0:
                            local_config.skill_log_data.pop("共感")
                    elif target in local_config.enemy and "共感" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["共感"].pop("enemy")
                        for role in buff_roles:
                            if role != target and "heart" in role.buff:
                                buff_obj = getattr(store, "heart")
                                buff_obj.calculate(role, None, None, None, "clean")
                        if len(local_config.skill_log_data["共感"]) == 0:
                            local_config.skill_log_data.pop("共感")
                # 间接伤害
                elif name == "mdamage":
                    if "间接伤害" in local_config.skill_log_data:
                        local_config.skill_log_data["间接伤害"].pop(target)
                        if len(local_config.skill_log_data["间接伤害"]) == 0:
                            local_config.skill_log_data.pop("间接伤害")

    def read_buff(filename):
        buff_list = []

        f = renpy.file(filename)
        for n, l in enumerate(f):
            l = l.decode("utf-8")
            a = l.rstrip().split(",")
            if a[0] != "":
                setattr(store, a[0], Buff(a[0], a[1], a[2], a[3], a[4], number=n))
                buff_list.append(globals()[a[0]])
        f.close()

        return buff_list
