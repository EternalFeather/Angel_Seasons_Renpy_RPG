
init python:
    import math

    # 持续效果由buff实现、即时效果由skill实现
    class Skill(object):
        """
        技能基础属性：名称、序号、介绍、施法时长、施法动画、施法音效
        技能判定属性：MP消耗、等级、附加效果类型、伤害倍率、技能定位、元素属性、伤害范围、技能选择标签
        """
        def __init__(self, objectname="", name="", sfx="", gfx="", grid=0, vfx="", grid2=0, times=0, xsize=0, info="", mp_cost=0, level=1, effects=[], effects_ratio=[], effects_target=[], 
            damage=[], damage_target="", category="", element=[], number=0):
            # 名称
            self.objectname = objectname
            self.original_name = objectname.capitalize().replace("_", " ")
            self.name = name
            # 序号
            self.number = int(number)
            # 施法时长
            self.grid = int(grid)
            # 施法动画、音效
            self.sfx = sfx
            self.gfx = gfx
            self.vfx = vfx
            self.grid2 = float(grid2) / 1000
            self.times = int(times)
            self.zoom_rate = float(xsize)

            # MP消耗
            self.mp_cost = int(mp_cost)
            # 等级
            self.level = int(level)
            # 介绍
            self.max_level = len(info)
            self.ori_info = info
            self.info = info[self.level - 1]
            # 附加效果类型(能量、治疗、拉条、护盾...){类型：倍率}
            self.effects = {}
            self.ori_effects = effects
            self.ori_effects_ratio = effects_ratio
            self.ori_effects_target = effects_target
            for effect, ratio_time, target in zip(effects, effects_ratio, effects_target):
                # 确认技能等级数值
                if "@" in ratio_time:
                    ratio_time = ratio_time.split("@")[self.level - 1]

                ratio, time = ratio_time.split(":")
                if ratio == "empty":
                    self.effects[effect] = (ratio, target, int(time))
                elif "/" in ratio:
                    if "/" in target:
                        self.effects[effect] = (tuple([float(r) for r in ratio.split("/")]), tuple([t for t in target.split("/")]), int(time))
                    else:
                        self.effects[effect] = (tuple([float(r) for r in ratio.split("/")]), target, int(time))
                elif "." in ratio:
                    self.effects[effect] = (float(ratio), target, int(time))
                else:
                    self.effects[effect] = (int(ratio), target, int(time))
            # 伤害倍率
            self.ori_damage = damage
            dmgs = [d.split(":")[self.level - 1] if ":" in d else d for d in damage]
            self.damage = [float(dmg) for dmg in dmgs]
            # 伤害段数
            self.damage_count = len(self.damage)
            # 技能定位（充能Recharge、普攻General_attack、被动Passive、元素战技Combat_skills、元素爆发Break_out、魔导力回路Magic_circuit）
            self.category = category
            # 元素属性
            self.ori_element = element
            self.element = [e.split(":")[self.level - 1] if ":" in e else e for e in element]
            # 伤害范围（single、single_ally、AOE、self、ally）
            self.damage_target = damage_target
            # 技能选择标签（主动技能沉默时、被动技能破魔时为False）
            self.selectable = True

            if self.gfx != "":
                renpy.image(self.gfx, DynamicDisplayable(self.render_effect, self.gfx, self.grid))
            if self.vfx != "" and "_img" in self.vfx:
                renpy.image(self.vfx, DynamicDisplayable(self.render_effect_v2, self.grid2, self.times, self.zoom_rate))

        def render_effect(self, st, at, image_path, last_frame, width=360, height=360, framerate=24):
            number = int(st * framerate)
            if number < last_frame:
                return Transform("9i/interface/battle/gfx/{}.png".format(image_path), crop=(0, height * number, width, height)), 1.0 / framerate
            else:
                return Null(), None

        def render_effect_v2(self, st, at, grid, times, zoom_rate):
            if st < grid * times:
                number = int(st / grid)
                renpy.predict("9i/interface/battle/vfx/{}/{}.png".format(self.name, number))
                return Transform("9i/interface/battle/vfx/{}/{}.png".format(self.name, number), zoom=zoom_rate), grid
            else:
                return Null(), None

        def render_effect_v3(self, st, at, grid, times, zoom_rate):
            count = int(st // (grid * times))
            loop_start = float(count * grid * times)
            loop_end = float((count + 1) * grid * times)
            if loop_start < st < loop_end:
                number = int((st - loop_start) / grid)
                renpy.predict("9i/interface/battle/vfx/{}/{}.png".format(self.name, number))
                return Transform("9i/interface/battle/vfx/{}/{}.png".format(self.name, number), zoom=zoom_rate), grid
            else:
                return Null(), None

        def level_change(self, tolevel):
            if tolevel > self.max_level:
                return

            self.level = int(tolevel)
            self.info = self.ori_info[self.level - 1]

            self.effects = {}
            for effect, ratio_time, target in zip(self.ori_effects, self.ori_effects_ratio, self.ori_effects_target):
                # 确认技能等级数值
                if "@" in ratio_time:
                    ratio_time = ratio_time.split("@")[self.level - 1]

                ratio, time = ratio_time.split(":")
                if ratio == "empty":
                    self.effects[effect] = (ratio, target, int(time))
                elif "/" in ratio:
                    if "/" in target:
                        self.effects[effect] = (tuple([float(r) for r in ratio.split("/")]), tuple([t for t in target.split("/")]), int(time))
                    else:
                        self.effects[effect] = (tuple([float(r) for r in ratio.split("/")]), target, int(time))
                elif "." in ratio:
                    self.effects[effect] = (float(ratio), target, int(time))
                else:
                    self.effects[effect] = (int(ratio), target, int(time))

            dmgs = [d.split(":")[self.level - 1] if ":" in d else d for d in self.ori_damage]
            self.damage = [float(dmg) for dmg in dmgs]
            self.damage_count = len(self.damage)

            self.element = [e.split(":")[self.level - 1] if ":" in e else e for e in self.ori_element]

        def get_info(self, who):
            if self.category == "Recharge":
                change_mp = (who.max_mp - who.mp) / 2
            else:
                change_mp = self.mp_cost
            return u"\nMP %+3d 伤害倍率 %s 等级 Lv.%s\n%s" % (change_mp, " | ".join([get_icons_v2(dmg) for dmg in self.damage]), str(self.level), self.info)
        
        def get_ex_info(self, who):
            """
            元素属性、单（群）、功能标签
            """
            elements = set(self.element)
            attr_color = []
            if "physical" in elements:
                attr_color.append(__("{color=#9cf}物理{/color}"))
            if "fire" in elements:
                attr_color.append(__("{color=#f30}火{/color}"))
            if "light" in elements:
                attr_color.append(__("{color=#f0f}雷{/color}"))
            if "wind" in elements:
                attr_color.append(__("{color=#6f6}风{/color}"))
            if "ice" in elements:
                attr_color.append(__("{color=#3ff}冰{/color}"))
            if "water" in elements:
                attr_color.append(__("{color=#99f}水{/color}"))
            if "rock" in elements:
                attr_color.append(__("{color=#ff0}岩{/color}"))

            if len(attr_color) == 0:
                attr_color = ""
            else:
                attr_color = " ".join(attr_color)

            if self.damage_target == "AOE":
                target_color = __("{color=#f66}群体{/color}")
            elif self.category == "Passive":
                target_color = __("{color=#f66}被动{/color}")
            elif len(self.damage) > 1:
                target_color = __("{color=#f66}多段{/color}")

            if self.selectable:
                target_color = ""
            else:
                target_color = __("{color=#f66}(失效){/color}")

            type_colors = []
            for dtype in self.effects:
                type_colors.append(dtype)
            type_color = " ".join(type_colors) if len(type_colors) > 0 else ""
            type_color = __("{color=#ccc}%s{/color}" % type_color)
            
            return u"{=bFont}%s{/bFont}{space=12}%s %s %s" % (self.name, attr_color, target_color, type_color)

        # 技能使用
        def use(self, user, target, party, enemy, sudden_attack=False, support=False, ally_environment_effects=None, enemy_environment_effects=None, order_members=None, role_now_stats=None):
            first_target = target

            # 设定技能释放者位置信息
            if user in local_config.enemy:
                slot_x = user.xposition
                slot_y = 0.05
            else:
                slot_y = 0.95
                if user == local_config.party[0]:
                    slot_x = 0.12
                elif user == local_config.party[1]:
                    slot_x = 0.35
                elif user == local_config.party[2]:
                    slot_x = 0.58
            
            # 使用者释放技能名称显示
            if user in local_config.party:
                renpy.show("skillname", at_list=[show_skill], layer="screens", what=Text(self.name.replace("_1", "").replace("_2", ""), style="skill_text"))
            else:
                renpy.show("skillname", at_list=[show_skill(user.xposition)], layer="screens", what=Text(self.name.replace("_1", "").replace("_2", ""), style="skill_text"))
            
            # 非主角协战时技能消耗MP
            if not support:
                user.mp += user.selected_skill.mp_cost
                if "Spiritual" in user.abilities and user.mp < 0:
                    local_config.spi_mp_cost = -user.mp
                if user.mp < 0:
                    user.mp = 0

            current_party = copy(party[:3])
            current_enemy = copy(enemy[:3])

            # -----------技能释放区域-----------
            # 凝神(无动画)
            if self.objectname == "guard" or self.objectname == "guard_spt":
                # 技能音效
                if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                    renpy.music.play(self.sfx, channel="sfx")
                    renpy.pause(0.001)
                
                if (config.skipping == None or config.skip_delay > 5) or self.vfx != "":
                    if user in local_config.party:
                        renpy.show(self.vfx, at_list=[effect_player(user.xposition)], layer="screens")
                    else:
                        renpy.show(self.vfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                    renpy.pause((self.grid2 * self.times + 0.5) * persistent.battlespeed)

                renpy.show("damage", at_list=[show_damage(user.xposition, 0.5)], layer="screens", what=Text("+%s" % int((user.max_mp - user.mp) / 2), style="damage_text", size=100, color="#19f"))
                renpy.pause(0.5 * persistent.battlespeed)
                renpy.hide("damage", layer="screens")

                user.mp += max(1, (user.max_mp - user.mp) / 2)
                user.mp = int(user.mp)
                if user.mp > user.max_mp:
                    user.mp = user.max_mp

                # 蓄能技能会额外附加一层“义”
                if self.objectname == "guard_spt":
                    if "积重鬼怨" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["积重鬼怨"]
                        if (user in local_config.party and buff_roles["enemy"] > 0) or (user in local_config.enemy and buff_roles["ally"] > 0):
                            pass
                        else:
                            buff_obj = getattr(store, "yi")
                            item = (99, 1)
                            for role in party:
                                buff_obj.calculate(role, None, item, "蓄能", "get")
                    else:
                        buff_obj = getattr(store, "yi")
                        item = (99, 1)
                        for role in party:
                            buff_obj.calculate(role, None, item, "蓄能", "get")

            # 有特效技能
            else:
                # 动画特效播放
                # 人物行动特效
                if (config.skipping == None or config.skip_delay > 5) and self.name not in ["虹之律", "碧之律", "翠之律", "霞之律", "绯之律"]:
                    if user in local_config.party and support:
                        renpy.show(user.objectname, at_list=[slide_flash_player(user.xposition)], layer="screens", zorder=-1)
                    elif user in local_config.party and sudden_attack:
                        renpy.show(user.objectname, at_list=[slide_flash_player(user.xposition)], layer="screens", zorder=-1)
                    elif user in local_config.party:
                        renpy.show(user.objectname, at_list=[slide_flash_player(user.xposition)], layer="screens", zorder=-1)
                    else:
                        renpy.show(user.objectname, at_list=[flash_enemy(user.xposition)], layer="enemy_ef")
                    renpy.pause(0.1)

                if self.name == "噗哈哈":
                    user.face = "happy"
                
                if self.damage_target == "special":
                    # 降魔诛乱
                    if self.objectname == "lingyin_combat":
                        damage_skill1 = copy(getattr(store, "lingyin_combat_1"))
                        damage_skill2 = copy(getattr(store, "lingyin_combat_2"))

                        for xi in range(self.level - 1):
                            damage_skill1.level_change(damage_skill1.level + 1)
                            damage_skill2.level_change(damage_skill2.level + 1)
                        
                        if user in local_config.party:
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + damage_skill1.sfx + ".mp3"):
                                renpy.music.play(damage_skill1.sfx, channel="sfx")
                                renpy.pause(0.001)
                            if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                                renpy.show(damage_skill1.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                                renpy.show(damage_skill1.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            target.battle_calculate_aoe(damage_skill1, user, [r for r in current_enemy if r.hp > 0], ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                        else:
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + damage_skill1.sfx + ".mp3"):
                                renpy.music.play(damage_skill1.sfx, channel="sfx")
                                renpy.pause(0.001)
                            if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                                if user in local_config.party:
                                    renpy.show(damage_skill1.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                else:
                                    renpy.show(damage_skill1.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                            elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                                if user in local_config.party:
                                    renpy.show(damage_skill1.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                else:
                                    renpy.show(damage_skill1.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                            target.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                            # 防止群体单次判定多段触发
                            local_config.multi_buff_lock = True
                            shown_actor = target
                            for role in current_enemy:
                                if role.hp > 0 and role != target:
                                    # 技能音效
                                    if renpy.loadable("9i/interface/battle/sfx/" + damage_skill1.sfx + ".mp3"):
                                        renpy.music.play(damage_skill1.sfx, channel="sfx")
                                        renpy.pause(0.001)
                                    if user in local_config.party:
                                        if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                                            renpy.show(damage_skill1.vfx, at_list=[effect_enemy(role.xposition)], layer="screens")
                                        elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                                            renpy.show(damage_skill1.gfx, at_list=[effect_enemy(role.xposition)], layer="screens")
                                        role.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                    else:
                                        renpy.hide(shown_actor.objectname, layer="fg")
                                        renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                        renpy.pause(0.5 * persistent.battlespeed)
                                        if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                                            renpy.show(damage_skill1.vfx, at_list=[effect_player(role.xposition)], layer="screens")
                                        elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                                            renpy.show(damage_skill1.gfx, at_list=[effect_player(role.xposition)], layer="screens")
                                        role.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                        shown_actor = role
                            local_config.multi_buff_lock = False
                        
                        if damage_skill1.vfx != "":
                            renpy.pause((damage_skill1.grid2 * damage_skill1.times + 0.25) * persistent.battlespeed)
                        elif damage_skill1.gfx != "":
                            renpy.pause(damage_skill1.grid / 48.0 * persistent.battlespeed)

                        ori_target = target
                        if target is not None and target.hp < 1:
                            target = user.selected_target

                            # 显示新的友方目标
                            if target in local_config.party and target != shown_actor:
                                renpy.hide(shown_actor.objectname, layer="fg")
                                renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                                renpy.pause(0.5 * persistent.battlespeed)
                        elif target.hp >= 1 and user in local_config.enemy:
                            renpy.hide(shown_actor.objectname, layer="fg")
                            renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")

                        if target is not None:
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + damage_skill2.sfx + ".mp3"):
                                renpy.music.play(damage_skill2.sfx, channel="sfx")
                                renpy.pause(0.001)
                            if user in local_config.party:
                                if (config.skipping == None or config.skip_delay > 5) and damage_skill2.vfx != "":
                                    renpy.show(damage_skill2.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                elif (config.skipping == None or config.skip_delay > 5) and damage_skill2.gfx != "":
                                    renpy.show(damage_skill2.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            else:
                                if (config.skipping == None or config.skip_delay > 5) and damage_skill2.vfx != "":
                                    renpy.show(damage_skill2.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                                elif (config.skipping == None or config.skip_delay > 5) and damage_skill2.gfx != "":
                                    renpy.show(damage_skill2.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                            target.battle_calculate(damage_skill2, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                    # 空间跳跃
                    elif self.objectname == "lst_breakout_1":
                        damage_skill1 = copy(getattr(store, "lst_combat"))
                        damage_skill2 = copy(getattr(store, "lst_breakout_1_1"))

                        for xi in range(self.level - 1):
                            damage_skill1.level_change(damage_skill1.level + 1)
                            damage_skill2.level_change(damage_skill2.level + 1)

                        temp_dict = local_config.skill_log_data.setdefault("空间跳跃", {})
                        
                        # 立刻施放“星空梦影”，并提升友方全体10%攻击、25点速度和10%全属性伤害减免
                        # 技能音效
                        if renpy.loadable("9i/interface/battle/sfx/" + damage_skill1.sfx + ".mp3"):
                            renpy.music.play(damage_skill1.sfx, channel="sfx")
                            renpy.pause(0.001)
                        if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                            if user in local_config.party:
                                renpy.show(damage_skill1.vfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            else:
                                renpy.show(damage_skill1.vfx, at_list=[effect_player(user.xposition)], layer="screens")
                            renpy.pause((damage_skill1.grid2 * damage_skill1.times + 0.25) * persistent.battlespeed)
                        elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                            if user in local_config.party:
                                renpy.show(damage_skill1.gfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            else:
                                renpy.show(damage_skill1.gfx, at_list=[effect_player(user.xposition)], layer="screens")
                            renpy.pause(damage_skill1.grid / 48.0 * persistent.battlespeed)

                        renpy.show("fight_cg-bg star_bridge", layer="bg2")
                        user.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                        user.battle_calculate(damage_skill2, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                        temp_dict[user] = 0
                        # 防止群体单次判定多段触发
                        local_config.multi_buff_lock = True
                        shown_actor = user
                        for role in current_party:
                            if role.hp > 0 and role != user:
                                if user in local_config.party:
                                    renpy.hide(shown_actor.objectname, layer="fg")
                                    renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                    renpy.pause(0.5 * persistent.battlespeed)
                                    role.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support, ani_only_once=True)
                                    role.battle_calculate(damage_skill2, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support, ani_only_once=True)
                                    shown_actor = role
                                else:
                                    role.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support, ani_only_once=True)
                                    role.battle_calculate(damage_skill2, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support, ani_only_once=True)
                                temp_dict[role] = 0
                        local_config.multi_buff_lock = False
                                
                        if user in local_config.party:
                            renpy.hide(shown_actor.objectname, layer="fg")
                            renpy.show(user.objectname, at_list=[show_player(user.xposition)], layer="fg")
                            renpy.pause(0.5 * persistent.battlespeed)

                        if "星空梦影" in local_config.skill_log_data and self.name == "空间跳跃":
                            buff_roles = local_config.skill_log_data["星空梦影"]
                            for role in buff_roles:
                                if role in party[:3]:
                                    temp_ratio_lists = [0.1, 0.15, 0.2, 0.25, 0.3]
                                    # 获得“星桥”
                                    buff_obj = getattr(store, "star_bridge")
                                    if self.level == 5:
                                        item = (2, temp_ratio_lists[self.level - 1])
                                        temp_item = 2
                                    else:
                                        item = (2, temp_ratio_lists[self.level - 1])
                                        temp_item = 1

                                    if "star_bridge_done" in role.buff:
                                        role.buff.pop("star_bridge_done")
                                    buff_obj.calculate(role, None, item, self.name, "get")
                                    # 使得下一次受到的伤害降低
                                    nouse_param, buff_user = buff_roles[role]
                                    buff_roles[role] = (True, buff_user)
                                    temp_dict[role] = temp_item
                    # 星陨离殇
                    elif self.objectname == "lst_breakout_2":
                        damage_skill1 = copy(getattr(store, "lst_breakout_2_1"))
                        damage_skill2 = copy(getattr(store, "lst_breakout_2_2"))

                        for xi in range(self.level - 1):
                            damage_skill1.level_change(damage_skill1.level + 1)
                            damage_skill2.level_change(damage_skill2.level + 1)
                        
                        if user in local_config.party:
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + damage_skill1.sfx + ".mp3"):
                                renpy.music.play(damage_skill1.sfx, channel="sfx")
                                renpy.pause(0.001)
                            if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                                renpy.show(damage_skill1.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                                renpy.show(damage_skill1.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            target.battle_calculate_aoe(damage_skill1, user, [r for r in current_enemy if r.hp > 0], ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                        else:
                            if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                                if user in local_config.party:
                                    renpy.show(damage_skill1.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                else:
                                    renpy.show(damage_skill1.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                            elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                                if user in local_config.party:
                                    renpy.show(damage_skill1.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                else:
                                    renpy.show(damage_skill1.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                            
                            target.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                            # 防止群体单次判定多段触发
                            local_config.multi_buff_lock = True
                            shown_actor = target
                            for role in current_enemy:
                                if role.hp > 0 and role != target:
                                    if user in local_config.party:
                                        if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                                            renpy.show(damage_skill1.vfx, at_list=[effect_enemy(role.xposition)], layer="screens")
                                        elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                                            renpy.show(damage_skill1.gfx, at_list=[effect_enemy(role.xposition)], layer="screens")
                                        role.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                    else:
                                        renpy.hide(shown_actor.objectname, layer="fg")
                                        renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                        renpy.pause(0.5 * persistent.battlespeed)
                                        if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                                            renpy.show(damage_skill1.vfx, at_list=[effect_player(role.xposition)], layer="screens")
                                        elif (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                                            renpy.show(damage_skill1.gfx, at_list=[effect_player(role.xposition)], layer="screens")
                                        role.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                        shown_actor = role
                            local_config.multi_buff_lock = False

                        if damage_skill1.vfx != "":
                            renpy.pause((damage_skill1.grid2 * damage_skill1.times + 0.25) * persistent.battlespeed)
                        elif damage_skill1.gfx != "":
                            renpy.pause(damage_skill1.grid / 48.0 * persistent.battlespeed)

                        if user in local_config.enemy and shown_actor != target:
                            renpy.hide(shown_actor.objectname, layer="fg")
                            renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                        
                        if self.level == 5:
                            attack_times = int(user.mp // 5)
                        else:
                            attack_times = int(user.mp // 10)
                        shown_actor = target
                        for _ in range(attack_times):
                            total_length = len([e for e in enemy[:3] if e.hp > 0])
                            if total_length == 0:
                                break
                            random_index = renpy.random.randint(0, total_length - 1)
                            random_target = [e for e in enemy[:3] if e.hp > 0][random_index]
                            
                            if user in local_config.party:
                                if (config.skipping == None or config.skip_delay > 5) and damage_skill2.vfx != "":
                                    renpy.show(damage_skill2.vfx, at_list=[effect_enemy(random_target.xposition)], layer="screens")
                                elif (config.skipping == None or config.skip_delay > 5) and damage_skill2.gfx != "":
                                    renpy.show(damage_skill2.gfx, at_list=[effect_enemy(random_target.xposition)], layer="screens")
                                # 技能音效
                                if renpy.loadable("9i/interface/battle/sfx/" + damage_skill2.sfx + ".mp3"):
                                    renpy.music.play(damage_skill2.sfx, channel="sfx")
                                    renpy.pause(0.001)
                                random_target.battle_calculate(damage_skill2, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                            else:
                                if shown_actor != random_target:
                                    renpy.hide(shown_actor.objectname, layer="fg")
                                    renpy.show(random_target.objectname, at_list=[show_player(random_target.xposition)], layer="fg")
                                    renpy.pause(0.5 * persistent.battlespeed)
                                    shown_actor = random_target
                                if (config.skipping == None or config.skip_delay > 5) and damage_skill2.vfx != "":
                                    renpy.show(damage_skill2.vfx, at_list=[effect_player(random_target.xposition)], layer="screens")
                                elif (config.skipping == None or config.skip_delay > 5) and damage_skill2.gfx != "":
                                    renpy.show(damage_skill2.gfx, at_list=[effect_player(random_target.xposition)], layer="screens")
                                # 技能音效
                                if renpy.loadable("9i/interface/battle/sfx/" + damage_skill2.sfx + ".mp3"):
                                    renpy.music.play(damage_skill2.sfx, channel="sfx")
                                    renpy.pause(0.001)
                                random_target.battle_calculate(damage_skill2, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)

                        if user in local_config.enemy and shown_actor != target:
                            renpy.hide(shown_actor.objectname, layer="fg")
                            renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                    # 樱雪同梦
                    elif self.objectname == "xfe_combat_1":
                        # 技能音效
                        if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                            renpy.music.play(self.sfx, channel="sfx")
                            renpy.pause(0.001)

                        if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                            if user in local_config.party:
                                renpy.show(self.vfx, at_list=[effect_player(user.xposition)], layer="screens")
                            else:
                                renpy.show(self.vfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            renpy.pause((self.grid2 * self.times + 0.5) * persistent.battlespeed)
                        elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                            if user in local_config.party:
                                renpy.show(self.gfx, at_list=[effect_player(user.xposition)], layer="screens")
                            else:
                                renpy.show(self.gfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            renpy.pause(self.grid / 24.0 * persistent.battlespeed)

                        # 清空自身所有的“羁绊之誓”和能量值
                        if "love" in user.buff:
                            buff_obj = getattr(store, "love")
                            buff_obj.calculate(user, None, None, None, "clean")
                        user.mp = 0

                        for role in party:
                            # 复活我方所有角色，被复活的角色恢复100%生命值和50%能量
                            if role.hp <= 0:
                                role.hp = role.battle_max_hp
                                role.mp = int(0.5 * role.max_mp)
                                role.reborn_calculate(ally_environment_effects)
                            # 祛除我方全体未阵亡角色的减益、控制状态和元素附着，并立刻恢复30点MP和50%生命值上限的生命值
                            else:
                                debuffs = copy(role.debuff)
                                for buff_name in debuffs:
                                    buff_obj = getattr(store, buff_name)
                                    if buff_obj.removeable or buff_name in ["dizziness", "deep_sleepy", "deep_frozen"]:
                                        buff_obj.calculate(role, ally_environment_effects, None, None, "clean")
                                role.ebuff = {}
                                role.mp += 30
                                if role.mp > role.max_mp:
                                    role.mp = role.max_mp
                                role.hp += int(0.5 * role.battle_max_hp)
                                if role.hp > role.battle_max_hp:
                                    role.hp = role.battle_max_hp
                        # 解除变身
                        user.is_phase2 = False
                    # 预见良缘
                    elif self.objectname == "xz_combat":
                        # 技能音效
                        if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                            renpy.music.play(self.sfx, channel="sfx")
                            renpy.pause(0.001)
                        if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                            if user in local_config.party:
                                renpy.show(self.vfx, at_list=[effect_player(user.xposition)], layer="screens")
                            else:
                                renpy.show(self.vfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            renpy.pause((self.grid2 * self.times + 0.5) * persistent.battlespeed)
                        elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                            if user in local_config.party:
                                renpy.show(self.gfx, at_list=[effect_player(user.xposition)], layer="screens")
                            else:
                                renpy.show(self.gfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            renpy.pause(self.grid / 24.0 * persistent.battlespeed)

                        # 随机复活一名阵亡的友方目标，并为其治疗生命上限15%|25%|35%|45%|55%的生命并恢复10|20|30|40|50能量
                        for role in party:
                            if role.hp < 1:
                                temp_hp_lists = [0.15, 0.25, 0.35, 0.45, 0.55]
                                temp_mp_lists = [10, 20, 30, 40, 50]
                                role.full_reset(heal_hp=True, ally_environment_effects=ally_environment_effects, turn_end=False, level_reset=False)
                                
                                role.hp = int(temp_hp_lists[self.level - 1] * role.battle_max_hp)
                                role.mp = temp_mp_lists[self.level - 1]

                                role.face_change()
                                role.reborn_calculate(ally_environment_effects)

                                if role in local_config.party:
                                    renpy.hide(user.objectname, layer="fg")
                                    renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                    renpy.pause(0.5 * persistent.battlespeed)
                                    renpy.music.play("raged", channel="battle_music")
                                    renpy.show("buff_effect", at_list=[show_state(role.xposition)], layer="screens", what=Text("重生", style="effect_text", color="ff9"))
                                    renpy.pause(0.5 * persistent.battlespeed)
                                    renpy.hide(role.objectname, layer="fg")
                                    renpy.show(user.objectname, at_list=[show_player(user.xposition)], layer="fg")
                                    renpy.pause(0.5 * persistent.battlespeed)
                                break
                        temp_selected_skills = user.base_skills if not user.is_phase2 else user.base_skills_v2
                        calculate_xz_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]
                        if calculate_xz_passive.level == 5:
                            # 悉心呵护：为我方场上所有角色恢复30%生命上限的生命值
                            for role in party[:3]:
                                if role.hp > 0:
                                    role.hp += int(role.battle_max_hp * 0.3)
                                    if role.hp > role.battle_max_hp:
                                        role.hp = role.battle_max_hp
                else:
                    damage_target = self.damage_target.split("|")
 
                    # 环境特效
                    if self.name in ["灵能风暴"]:
                        renpy.music.play("雷鸣", channel="battle_music")
                        renpy.pause(0.5 * persistent.battlespeed)
                        if user in local_config.party:
                            renpy.show("thunder_cloud_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=1.3, xpos=0.4, ypos=0.15)], layer="fg_f")
                        else:
                            renpy.show("thunder_cloud_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=0.8, xpos=0.85, ypos=0.15)], layer="fg_f")

                    ## 伤害范围判定     
                    # 敌方单体
                    if "single" in damage_target:
                        # 技能音效
                        if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                            renpy.music.play(self.sfx, channel="sfx")
                            renpy.pause(0.001)
                        if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                            if user in local_config.party:
                                renpy.show(self.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            else:
                                renpy.show(self.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                        elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                            if user in local_config.party:
                                renpy.show(self.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            else:
                                renpy.show(self.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                        target.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                    # 敌方全体
                    if "AOE" in damage_target:
                        if user in local_config.party and target in local_config.enemy:
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                                renpy.music.play(self.sfx, channel="sfx")
                                renpy.pause(0.001)
                            if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                                renpy.show(self.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                                renpy.show(self.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            target.battle_calculate_aoe(self, user, [r for r in current_enemy if r.hp > 0], ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                        else:
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                                renpy.music.play(self.sfx, channel="sfx")
                                renpy.pause(0.001)
                            if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                                if user in local_config.party:
                                    renpy.show(self.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                    if "伤害" not in self.effects:
                                        renpy.pause((self.grid2 * self.times + 0.25) * persistent.battlespeed)
                                else:
                                    renpy.show(self.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                                    if "伤害" not in self.effects:
                                        renpy.pause(self.grid / 48.0 * persistent.battlespeed)
                            elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                                if user in local_config.party:
                                    renpy.show(self.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                    if "伤害" not in self.effects:
                                        renpy.pause((self.grid2 * self.times + 0.25) * persistent.battlespeed)
                                else:
                                    renpy.show(self.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                                    if "伤害" not in self.effects:
                                        renpy.pause(self.grid / 48.0 * persistent.battlespeed)
                            target.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                            # 防止群体单次判定多段触发
                            local_config.multi_buff_lock = True
                            shown_actor = target
                            for role in current_enemy:
                                if role.hp > 0 and role != target:
                                    # 技能音效
                                    if self.name != "噗哈哈":
                                        if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                                            renpy.music.play(self.sfx, channel="sfx")
                                            renpy.pause(0.001)
                                    if user in local_config.party:
                                        if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                                            renpy.show(self.vfx, at_list=[effect_enemy(role.xposition)], layer="screens")
                                            if "伤害" not in self.effects:
                                                renpy.pause((self.grid2 * self.times + 0.25) * persistent.battlespeed)
                                        elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                                            renpy.show(self.gfx, at_list=[effect_enemy(role.xposition)], layer="screens")
                                            if "伤害" not in self.effects:
                                                renpy.pause(self.grid / 48.0 * persistent.battlespeed)
                                        role.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                    else:
                                        if shown_actor != role:
                                            renpy.hide(shown_actor.objectname, layer="fg")
                                            renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                            renpy.pause(0.5 * persistent.battlespeed)
                                        if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                                            renpy.show(self.vfx, at_list=[effect_player(role.xposition)], layer="screens")
                                            if "伤害" not in self.effects:
                                                renpy.pause((self.grid2 * self.times + 0.25) * persistent.battlespeed)
                                        elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                                            renpy.show(self.gfx, at_list=[effect_player(role.xposition)], layer="screens")
                                            if "伤害" not in self.effects:
                                                renpy.pause(self.grid / 48.0 * persistent.battlespeed)
                                        role.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                        shown_actor = role
                            local_config.multi_buff_lock = False

                        # if user in local_config.enemy and target is not None and shown_actor != target:
                        #     renpy.hide(shown_actor.objectname, layer="fg")
                            # renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                        if user in local_config.enemy:
                            renpy.hide(shown_actor.objectname, layer="fg")
                    # 自己
                    if "self" in damage_target:
                        # 技能音效
                        if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                            renpy.music.play(self.sfx, channel="sfx")
                            renpy.pause(0.001)
                        if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                            if user in local_config.party:
                                renpy.show(self.vfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            else:
                                renpy.show(self.vfx, at_list=[effect_player(user.xposition)], layer="screens")
                            renpy.pause((self.grid2 * self.times + 0.25) * persistent.battlespeed)
                        elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                            if user in local_config.party:
                                renpy.show(self.gfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            else:
                                renpy.show(self.gfx, at_list=[effect_player(user.xposition)], layer="screens")
                            renpy.pause(self.grid / 48.0 * persistent.battlespeed)
                        user.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                    # 友方单体
                    if "single_ally" in damage_target:
                        # 技能音效
                        if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                            renpy.music.play(self.sfx, channel="sfx")
                            renpy.pause(0.001)
                        if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                            if user in local_config.party:
                                renpy.show(self.vfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                            else:
                                renpy.show(self.vfx, at_list=[effect_player(user.xposition)], layer="screens")
                            renpy.pause((self.grid2 * self.times + 0.25) * persistent.battlespeed)
                        elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                            if user in local_config.party:
                                renpy.show(self.gfx, at_list=[effect_enemy(local_config.chosen_actor.xposition)], layer="screens")
                            else:
                                renpy.show(self.gfx, at_list=[effect_player(local_config.chosen_actor.xposition)], layer="screens")
                            renpy.pause(self.grid / 48.0 * persistent.battlespeed)
                        local_config.chosen_actor.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                    # 友方全体
                    if "ally" in damage_target:
                        current_party = copy(party[:3])

                        if user in local_config.enemy:
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                                renpy.music.play(self.sfx, channel="sfx")
                                renpy.pause(0.001)
                            if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                                renpy.show(self.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                            elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                                renpy.show(self.gfx, at_list=[effect_player(user.xposition)], layer="screens")
                            user.battle_calculate_aoe(self, user, [r for r in current_party if r.hp > 0], ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                        else:
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + self.sfx + ".mp3"):
                                renpy.music.play(self.sfx, channel="sfx")
                                renpy.pause(0.001)
                            if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                                if user in local_config.party:
                                    renpy.show(self.vfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                                else:
                                    renpy.show(self.vfx, at_list=[effect_player(user.xposition)], layer="screens")
                                renpy.pause((self.grid2 * self.times + 0.25) * persistent.battlespeed)
                            elif (config.skipping == None or config.skip_delay > 5) and self.gfx != "":
                                if user in local_config.party:
                                    renpy.show(self.gfx, at_list=[effect_enemy(user.xposition)], layer="screens")
                                else:
                                    renpy.show(self.gfx, at_list=[effect_player(user.xposition)], layer="screens")
                                renpy.pause(self.grid / 48.0 * persistent.battlespeed)
                            user.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                            # 防止群体单次判定多段触发
                            local_config.multi_buff_lock = True
                            shown_actor = user
                            for role in current_party:
                                if role.hp > 0 and role != user:
                                    if user in local_config.party:
                                        renpy.hide(shown_actor.objectname, layer="fg")
                                        renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                        renpy.pause(0.5 * persistent.battlespeed)
                                        role.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support, ani_only_once=True)
                                        shown_actor = role
                                    else:
                                        role.battle_calculate(self, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                            local_config.multi_buff_lock = False
                                    
                            if user in local_config.party:
                                renpy.hide(shown_actor.objectname, layer="fg")
                                renpy.show(user.objectname, at_list=[show_player(user.xposition)], layer="fg")
                                renpy.pause(0.5 * persistent.battlespeed)

                renpy.hide("skillname", layer="screens")
                renpy.hide("special", layer="screens")
                if self.gfx != "":
                    renpy.hide(self.gfx, layer="screens")
                renpy.hide(user.objectname, layer="screens")
                renpy.hide(user.objectname, layer="enemy_ef")

            ## 行动结束后效果触发区
            if target is not None:
                target = user.selected_target

                # 显示新的友方目标
                if target in local_config.party:
                    renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                    renpy.pause(0.5 * persistent.battlespeed)
                    if first_target != target:
                        local_config.shown_actor = target
                    
            if user in local_config.party:
                party = local_config.party
                enemy = local_config.enemy
            elif user in local_config.enemy:
                party = local_config.enemy
                enemy = local_config.party
            current_party = copy(party[:3])
            current_enemy = copy(enemy[:3])

            if target is not None:
                ## 施放后技能效果
                # ----- 爱意绵延 -----
                if ("爱意绵延", True) in enemy_environment_effects:
                    calculate_aiyi_role = [role for role in enemy[:3] if role.name == "日向爱衣"]
                    if len(calculate_aiyi_role) > 0:
                        calculate_aiyi_role = calculate_aiyi_role[0]
                        under_control = False
                        for buff_name in calculate_aiyi_role.debuff:
                            if buff_name in ["confusion", "dizziness", "frozen", "sleepy", "ridicule"]:
                                under_control = True
                                break
                        if not under_control:
                            select_role_id = renpy.random.randint(0, len(enemy[:3])-1)
                            select_role = enemy[:3][select_role_id]

                            # 有概率随机为任一友方单位驱散1~2个减益或控制状态
                            judge_ratios = [0.15, 0.2, 0.25, 0.3, 0.3]
                            if judge_ratios[self.level - 1] > renpy.random.random():
                                renpy.show("special", at_list=[show_state(calculate_aiyi_role.xposition)], layer="screens", what=Text("爱意绵延", style="skill_text"))

                                debuffs = copy(select_role.debuff)
                                for i, buff_name in enumerate(debuffs):
                                    buff_obj = getattr(store, buff_name)
                                    if buff_obj.removeable:
                                        buff_obj.calculate(select_role, enemy_environment_effects, None, None, "clean")
                                        if self.level in [1, 2, 3, 4]:
                                            break
                                        elif self.level == 5:
                                            if i >= 2:
                                                break
                            # 有50%概率为其清除元素附着
                            if 0.5 > renpy.random.random():
                                select_role.ebuff = {}
                # ----- 预知未来 -----
                # level5：施放过后行动条最靠前的我方角色获得额外20%攻击加成。
                if self.name == "预知未来" and self.level == 5:
                    order_members = party[:3]
                    order_members.sort(key=attrgetter("order"), reverse=True)
                    # 取得行动条最顶端的角色
                    fast_active_actor = order_members[0]
                    if fast_active_actor.hp > 0:
                        buff = getattr(store, "strong")
                        item = (1, 0.2)
                        buff.calculate(fast_active_actor, None, item, self.name + "额外", "get")
                # ----- 再会之音 -----
                if "咒" in local_config.skill_log_data:
                    buff_roles = local_config.skill_log_data["咒"]
                    for role, (flag, damage_number, dtype, other) in buff_roles.items():
                        if flag:
                            temp_selected_skills = role.base_skills if not role.is_phase2 else role.base_skills_v2
                            lhx_passive_skill = [s for s in temp_selected_skills if s.category == "Passive"][0]
                            if dtype == "user":
                                # 降低“接触”效果对应敌方目标防御力
                                buff_obj = getattr(store, "exposed")
                                item = (1, 100)
                                if lhx_passive_skill.level == 5:
                                    item = (1, 150)
                                buff_obj.calculate(other, None, item, "再会之音", "get")
                            elif dtype == "target":
                                # 为“立花希”附加1层风元素护盾，其数值等同于此次伤害的50%，最高不超过“立花希”生命上限的12%|18%
                                if lhx_passive_skill.level == 5:
                                    snumber = int(damage_number) if int(damage_number) <= int(other.battle_max_hp * 0.18) else int(other.battle_max_hp * 0.18)
                                else:
                                    snumber = int(0.5 * damage_number) if int(0.5 * damage_number) <= int(other.battle_max_hp * 0.12) else int(other.battle_max_hp * 0.12)
                                buff_obj = getattr(store, "shield")

                                item = (1, (snumber, "wind", 0.75, 0.5))
                                buff_obj.calculate(other, None, item, "再会之音", "get")
                            buff_roles[role] = (False, None, dtype, other)
                # 魂之殇：记录我方场上所有队友以及所选择的敌方目标当前生命比例，若下回合“立花希”行动开始时，我方有角色所记录的生命比例小于记录的生命比例且未阵亡，则将该角色的生命恢复至该记录数值比例
                if "魂之殇" in local_config.skill_log_data:
                    buff_roles = local_config.skill_log_data["魂之殇"]
                    if (user, target) in buff_roles:
                        hprate, dtype = buff_roles[(user, target)][user]
                        item = (99, hprate)
                        # 为所有场上友方单位附加“殇魂”buff
                        buff_obj = getattr(store, "soul_lock")
                        calculate_lhx_combat_skill = getattr(store, "lhx_combat_1")

                        shown_actor = user
                        for role in party[:3]:
                            if user in local_config.party:
                                renpy.hide(shown_actor.objectname, layer="fg")
                                renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                renpy.pause(0.5 * persistent.battlespeed)
                                if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                                    renpy.show(calculate_lhx_combat_skill.vfx, at_list=[effect_player(role.xposition)], layer="screens")
                                shown_actor = role
                            elif user in local_config.enemy:
                                if (config.skipping == None or config.skip_delay > 5) and self.vfx != "":
                                    renpy.show(calculate_lhx_combat_skill.vfx, at_list=[effect_enemy(role.xposition)], layer="screens")

                            if role != user:
                                buff_roles[(user, target)][role] = (hprate, "ally")
                            buff_obj.calculate(role, None, item, self.name, "get")

                        if user in local_config.party:
                            renpy.hide(shown_actor.objectname, layer="fg")
                            renpy.show(user.objectname, at_list=[show_player(user.xposition)], layer="fg")
                            renpy.pause(0.5 * persistent.battlespeed)
                # 星空梦影：期间场上所有友方单位获得“星桥”，并使得下一次受到的伤害降低10%|15%|20%|25%|30%
                if "星空梦影" in local_config.skill_log_data and self.name == "星空梦影":
                    buff_roles = local_config.skill_log_data["星空梦影"]
                    for role in buff_roles:
                        if role in party[:3]:
                            temp_ratio_lists = [0.1, 0.15, 0.2, 0.25, 0.3]
                            # 获得“星桥”
                            buff_obj = getattr(store, "star_bridge")
                            if self.level == 5:
                                item = (2, temp_ratio_lists[self.level - 1])
                            else:
                                item = (2, temp_ratio_lists[self.level - 1])

                            if "star_bridge_done" in role.buff:
                                role.buff.pop("star_bridge_done")
                            buff_obj.calculate(role, None, item, self.name, "get")
                            # 使得下一次受到的伤害降低
                            nouse_param, buff_user = buff_roles[role]
                            buff_roles[role] = (True, buff_user)
                # 共感：为我方场上全体角色附加“心”，持续2回合
                if "共感" in local_config.skill_log_data and self.name == "共感":
                    buff_roles = local_config.skill_log_data["共感"]
                    if user in local_config.party and "ally" in buff_roles:
                        roles = copy(buff_roles["ally"])
                        for role in roles:
                            # 获得“心”
                            if role == user:
                                buff_obj = getattr(store, "heart_main")
                                if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                                    item = (3, None)
                                else:
                                    item = (2, None)
                                buff_obj.calculate(role, None, item, self.name, "get")
                            else:
                                buff_obj = getattr(store, "heart")
                                item = (99, None)
                                buff_obj.calculate(role, None, item, self.name, "get")
                    elif user in local_config.enemy and "enemy" in buff_roles:
                        roles = copy(buff_roles["enemy"])
                        for role in roles:
                            # 获得“心”
                            if role == user:
                                buff_obj = getattr(store, "heart_main")
                                if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                                    item = (3, None)
                                else:
                                    item = (2, None)
                                buff_obj.calculate(role, None, item, self.name, "get")
                            else:
                                buff_obj = getattr(store, "heart")
                                item = (99, None)
                                buff_obj.calculate(role, None, item, self.name, "get")
                # 空间跳跃：结界中的友方在其回合进行普攻时，有50%|50%|50%|100%|100%概率对同一目标再额外追加一次普攻
                if "空间跳跃" in local_config.skill_log_data and not support and role_now_stats != "confusion":
                    buff_roles = local_config.skill_log_data["空间跳跃"]
                    
                    if self.category == "General_attack" and user in buff_roles:
                        fake_lst_role = None
                        for temp_role in party:
                            if temp_role.name == "雷亚":
                                fake_lst_role = temp_role
                                break
                        temp_selected_skill = fake_lst_role.base_skills if not fake_lst_role.is_phase2 else fake_lst_role.base_skills_v2
                        lst_breakout_skill = [s for s in temp_selected_skill if s.category == "Break_out"][0]
                        if (lst_breakout_skill.level in [1, 2, 3] and 0.5 > renpy.random.random()) or lst_breakout_skill.level in [4, 5]:
                            role_select_skills = user.skills if not user.is_phase2 else user.skills_v2
                            general_skill = [s for s in role_select_skills if s.category == "General_attack"][0]

                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + general_skill.sfx + ".mp3"):
                                renpy.music.play(general_skill.sfx, channel="sfx")
                                renpy.pause(0.001)
                            
                            if user in local_config.party:
                                if (config.skipping == None or config.skip_delay > 5) and general_skill.vfx != "":
                                    renpy.show(general_skill.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                elif (config.skipping == None or config.skip_delay > 5) and general_skill.gfx != "":
                                    renpy.show(general_skill.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            else:
                                if (config.skipping == None or config.skip_delay > 5) and general_skill.vfx != "":
                                    renpy.show(general_skill.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                                elif (config.skipping == None or config.skip_delay > 5) and general_skill.gfx != "":
                                    renpy.show(general_skill.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                            target.battle_calculate(general_skill, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, sp_rull="空间跳跃", support=support)
                # 剑术精通：进入“空灵”状态时施放“青影瞬杀阵”将会追加斩击，每次有20%|30%|40%|40%|50%概率额外附加1次斩击，直到判定失败为止
                if user.name == "水之濑凛" and "ethereal" in user.buff and self.name == "青影瞬杀阵":
                    damage_skill1 = copy(getattr(store, "szl_combat_1"))

                    for xi in range(self.level - 1):
                        damage_skill1.level_change(damage_skill1.level + 1)

                    choice = renpy.random.random()
                    temp_ratio_lists = [0.2, 0.3, 0.4, 0.4, 0.5]
                    while temp_ratio_lists[self.level - 1] > choice and target is not None:
                        if (config.skipping == None or config.skip_delay > 5) and damage_skill1.vfx != "":
                            if user in local_config.party:
                                renpy.show(damage_skill1.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            else:
                                renpy.show(damage_skill1.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                        if (config.skipping == None or config.skip_delay > 5) and damage_skill1.gfx != "":
                            if user in local_config.party:
                                renpy.show(damage_skill1.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            else:
                                renpy.show(damage_skill1.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                        target.battle_calculate(damage_skill1, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)

                        choice = renpy.random.random()
                        ori_target = target
                        target = user.selected_target

                        if ori_target != target and target in local_config.party:
                            renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                            renpy.pause(0.5 * persistent.battlespeed)
                # 幻镜化物：且每次普攻斩击造成伤害时有15%|20%|25%|30%|30%概率对场上其他任一敌人造成本次斩击伤害150%的间接伤害
                if self.name == "念动力场-雷" and user.name == "水之濑凛" and "ethereal" in user.buff and "幻镜化物" in local_config.skill_log_data and role_now_stats != "confusion":
                    buff_damage = local_config.skill_log_data.pop("幻镜化物")
                    target_candidates = [e for e in enemy[:3] if e.hp > 0]
                    random_target = None
                    
                    # 如果原目标已经阵亡
                    if first_target != target:
                        skill_in_flag = True
                        random_index = renpy.random.randint(0, len(target_candidates) - 1)
                        random_target = target_candidates[random_index]
                    # 如果原目标存活，至少剩余其他1名角色
                    elif len(target_candidates) > 1:
                        skill_in_flag = True
                        target_candidates = [e for e in target_candidates if e != target]
                        random_index = renpy.random.randint(0, len(target_candidates) - 1)
                        random_target = target_candidates[random_index]
                    
                    temp_ratio_lists = [0.15, 0.2, 0.25, 0.3, 0.3]
                    temp_selected_skills = user.base_skills if not user.is_phase2 else user.base_skills_v2
                    temp_breakout_skill = [s for s in temp_selected_skills if s.category == "Break_out"][0]
                    if random_target and temp_ratio_lists[temp_breakout_skill.level - 1] > renpy.random.random():
                        renpy.music.play("hit", channel="battle_music")
                        renpy.pause(0.05)

                        if random_target in local_config.party:
                            if random_target != target:
                                renpy.hide(target.objectname, layer="fg")
                                renpy.show(random_target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                                renpy.pause(0.5 * persistent.battlespeed)

                        renpy.show("damage", at_list=[show_damage(random_target.xposition, 0.5)], layer="screens", what=Text("%s" % buff_damage, style="damage_text", size=100, color="#9cf"))
                        renpy.show("buff_effect", at_list=[show_state(random_target.xposition)], layer="screens", what=Text("溅射", style="effect_text", color="ff9"))
                        # 表情更新
                        random_target.face_change(hit=False, hitted=True)
                        # 受到伤害角色抖动特效
                        if random_target in local_config.party:
                            renpy.show(random_target.objectname, at_list=[shake, hide_out], layer="fg")
                        else:
                            renpy.show(random_target.objectname, at_list=[smallshake])
                        renpy.pause(0.75 * persistent.battlespeed)

                        if random_target in local_config.party and random_target != target:
                            renpy.hide(random_target.objectname, layer="fg")
                            renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                            renpy.pause(0.5 * persistent.battlespeed)

                        random_target.hp -= buff_damage
                        if random_target.hp < 1:
                            random_target.hp = 0
                        random_target.death_calculate(user, self, ally_environment_effects, enemy_environment_effects)

                        # 避免能量条溢出边界
                        random_target.hp = int(random_target.hp)
                        random_target.mp = int(random_target.mp)
                        if random_target.hp > random_target.battle_max_hp:
                            random_target.hp = random_target.battle_max_hp
                        elif random_target.hp < 0:
                            random_target.hp = 0
                        if random_target.mp > 100:
                            random_target.mp = 100
                        elif random_target.mp < 0:
                            random_target.mp = 0
                        # 表情恢复
                        random_target.face_change()

                        renpy.hide("damage", layer="screens")
                        renpy.hide("buff_effect", layer="screens")
                # 福祸相生：若开启封印结界则在攻击结束后附加一次对敌方全体的雷元素范围伤害
                if "积重鬼怨" in local_config.skill_log_data and self.name == "福祸相生":
                    buff_roles = local_config.skill_log_data["积重鬼怨"]
                    if (user in local_config.party and "ally" in buff_roles) or (user in local_config.enemy and "enemy" in buff_roles):
                        # 若开启封印结界则在攻击结束后附加一次对敌方全体72%的雷元素范围伤害
                        damage_skill = copy(getattr(store, "qcls_combat_1"))

                        for xi in range(self.level - 1):
                            damage_skill.level_change(damage_skill.level + 1)
                        
                        if (config.skipping == None or config.skip_delay > 5) and damage_skill.vfx != "":
                            if user in local_config.party:
                                renpy.show(damage_skill.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            else:
                                renpy.show(damage_skill.vfx, at_list=[effect_player(target.xposition)], layer="screens")
                            renpy.pause((damage_skill.grid2 * damage_skill.times + 0.25) * persistent.battlespeed)
                        elif (config.skipping == None or config.skip_delay > 5) and damage_skill.gfx != "":
                            if user in local_config.party:
                                renpy.show(damage_skill.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                            else:
                                renpy.show(damage_skill.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                            renpy.pause(damage_skill.grid / 48.0 * persistent.battlespeed)
                        target.battle_calculate(damage_skill, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)

                        # 防止群体单次判定多段触发
                        local_config.multi_buff_lock = True
                        shown_actor = target
                        for role in current_enemy:
                            if role.hp > 0 and role != target:
                                if user in local_config.party:
                                    if (config.skipping == None or config.skip_delay > 5) and damage_skill.vfx != "":
                                        renpy.show(damage_skill.vfx, at_list=[effect_enemy(role.xposition)], layer="screens")
                                        renpy.pause((damage_skill.grid2 * damage_skill.times + 0.25) * persistent.battlespeed)
                                    elif (config.skipping == None or config.skip_delay > 5) and damage_skill.gfx != "":
                                        renpy.show(damage_skill.gfx, at_list=[effect_enemy(role.xposition)], layer="screens")
                                        renpy.pause(damage_skill.grid / 48.0 * persistent.battlespeed)
                                    role.battle_calculate(damage_skill, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                else:
                                    renpy.hide(shown_actor.objectname, layer="fg")
                                    renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                    renpy.pause(0.5 * persistent.battlespeed)
                                    if (config.skipping == None or config.skip_delay > 5) and damage_skill.vfx != "":
                                        renpy.show(damage_skill.vfx, at_list=[effect_player(role.xposition)], layer="screens")
                                        renpy.pause((damage_skill.grid2 * damage_skill.times + 0.25) * persistent.battlespeed)
                                    elif (config.skipping == None or config.skip_delay > 5) and damage_skill.gfx != "":
                                        renpy.show(damage_skill.gfx, at_list=[effect_player(role.xposition)], layer="screens")
                                        renpy.pause(damage_skill.grid / 48.0 * persistent.battlespeed)
                                    role.battle_calculate(damage_skill, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                    shown_actor = role

                        local_config.multi_buff_lock = False

                        if user in local_config.enemy and shown_actor != target:
                            renpy.hide(shown_actor.objectname, layer="fg")
                            renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                # 虚无
                if "积重鬼怨" in local_config.skill_log_data and self.name == "虚无":
                    for role in current_enemy:
                        if role.hp > 0:
                            role._special_calculate(enemy_environment_effects=enemy_environment_effects, mode="chain")
                # 天宫罗阵：每次我方其他角色攻击阶段结束后，若“铃音”未处于无法行动状态则有20%|25%|30%|35%|40%概率触发“协战”，立刻对选中的目标追加1次普攻
                for role in party[:3]:
                    # 30%概率“协战”
                    if ("天宫罗阵", True) in ally_environment_effects and target is not None and user.name != "青木铃音" and target.hp > 0 and role.name == "青木铃音" and role.moveable and role_now_stats != "confusion":
                        role_select_skills = role.skills if not role.is_phase2 else role.skills_v2
                        passive_skill = [s for s in role_select_skills if s.category == "Passive"][0]
                        judge_ratios = [0.2, 0.25, 0.3, 0.35, 0.4]
                        if judge_ratios[passive_skill.level - 1] > renpy.random.random():
                            general_skill = [s for s in role_select_skills if s.category == "General_attack"][0]
                            # 技能音效
                            if renpy.loadable("9i/interface/battle/sfx/" + general_skill.sfx + ".mp3"):
                                renpy.music.play(general_skill.sfx, channel="sfx")
                                renpy.pause(0.001)
                            
                            if role in local_config.party:
                                renpy.hide(user.objectname, layer="fg")
                                renpy.show(role.objectname, at_list=[show_player(role.xposition)], layer="fg")
                                renpy.pause(0.5 * persistent.battlespeed)
                                renpy.show("special", at_list=[show_state(role.xposition)], layer="screens", what=Text("协战", style="skill_text"))
                                if (config.skipping == None or config.skip_delay > 5) and general_skill.vfx != "":
                                    renpy.show(general_skill.vfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                elif (config.skipping == None or config.skip_delay > 5) and general_skill.gfx != "":
                                    renpy.show(general_skill.gfx, at_list=[effect_enemy(target.xposition)], layer="screens")
                                target.battle_calculate(general_skill, role, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                                renpy.hide(role.objectname, layer="fg")
                                renpy.show(user.objectname, at_list=[show_player(user.xposition)], layer="fg")
                            else:
                                renpy.show("special", at_list=[show_state(role.xposition)], layer="screens", what=Text("协战", style="skill_text"))
                                if (config.skipping == None or config.skip_delay > 5) and general_skill.gfx != "":
                                    renpy.show(general_skill.gfx, at_list=[effect_player(target.xposition)], layer="screens")
                                target.battle_calculate(general_skill, role, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, support=support)
                # 微量化改造-四季之律
                if "微量化改造" in local_config.skill_log_data and self.name == "芬布尔之冬":
                    buff_roles = local_config.skill_log_data["微量化改造"]
                    if user in buff_roles:
                        select_skill, temp_breakout_skill, now_is_phase2 = buff_roles.pop(user)
                        if len(local_config.skill_log_data["微量化改造"]) == 0:
                            local_config.skill_log_data.pop("微量化改造")
                        select_skill.use(user=user, target=target, party=party, enemy=enemy, sudden_attack=False, support=True, ally_environment_effects=ally_environment_effects, enemy_environment_effects=enemy_environment_effects, role_now_stats=role_now_stats)

                    # 替换技能
                    if now_is_phase2:
                        skill_lists = copy(user.skills_v2)
                        new_skill_lists = [s if s.category != "Break_out" else temp_breakout_skill for s in skill_lists]
                        user.skills_v2 = new_skill_lists
                    else:
                        skill_lists = copy(user.skills)
                        new_skill_lists = [s if s.category != "Break_out" else temp_breakout_skill for s in skill_lists]
                        user.skills = new_skill_lists
                # 激励
                if "Endurance" in user.abilities and self.category == "Break_out" and 0.12 > renpy.random.random():
                    buff_obj = getattr(store, "strong")
                    item = (1, 0.3)

                    renpy.music.play("raged", channel="battle_music")
                    renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("激励", style="effect_text", color="ff9"))
                    renpy.pause(0.5 * persistent.battlespeed)
                    renpy.hide("buff_effect", layer="screens")

                    for role in current_party[:3]:
                        if role.hp > 0:
                            buff_obj.calculate(role, None, item, "Endurance", "get")

            # 环境特效
            if self.name in ["灵能风暴"]:
                renpy.hide("thunder_cloud_img", layer="fg_f")
            renpy.hide("skillname", layer="screens")
            renpy.hide("special", layer="screens")
            if self.gfx != "":
                renpy.hide(self.gfx, layer="screens")
            renpy.hide(user.objectname, layer="screens")
            renpy.hide(user.objectname, layer="enemy_ef")

            ## 行动结束后效果触发区
            if target is not None:
                target = user.selected_target

                # 显示新的友方目标
                if target in local_config.party:
                    renpy.show(target.objectname, at_list=[show_player(target.xposition)], layer="fg")
                    renpy.pause(0.5 * persistent.battlespeed)
                    if first_target != target:
                        local_config.shown_actor = target

            return


    # 注册技能
    def read_skill(filename):
        skill_list=[]

        f = renpy.file(filename)
        for n, l in enumerate(f):
            l = l.decode("utf-8")
            a = l.rstrip().split(",")
            if a[0] != "":
                setattr(store, a[0], Skill(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9].split("|"), a[10], 1, a[11].split("|"), a[12].split("|"), a[13].split("|"), a[14].split("|"), a[15], a[16], a[17].split("|"), number=n))
                skill_list.append(globals()[a[0]])
        f.close()

        return skill_list
