
# 调整薪水改变debt和心情
label refreshXS:
    $ local_config.info_role.salary = info_role_xs
    $ local_config.info_role.salary_changed = True
    $ local_config.debt = info_debt

    if local_config.info_role.salary_changed:
        $ local_config.info_role.mood -= local_config.info_role.mood_changed

    $ local_config.debt += info_role_xs

    if local_config.info_role.salary < 500:
        $ paopao_info = "{size=+8}（这个月要省\n  着点花。）{/size}"
        $ local_config.info_role.mood -= 25
        $ info_mood_change = -25
    elif local_config.info_role.salary < 1500:
        $ paopao_info = "{size=+8}有薪水领的感\n    觉真好！{/size}"
        $ local_config.info_role.mood += 5
        $ info_mood_change = 5
    else:
        $ paopao_info = "{size=+8}多谢[local_config.player.name]\n，[local_config.info_role.name]会加倍\n    努力的。{/size}"
        $ local_config.info_role.mood += 15
        $ info_mood_change = 15

    if local_config.info_role.mood > 100:
        $ diff_mood = local_config.info_role.mood - 100
        $ local_config.info_role.mood = 100
        $ info_mood_change -= diff_mood
    elif local_config.info_role.mood < 0:
        $ diff_mood = 0 - local_config.info_role.mood
        $ local_config.info_role.mood = 0
        $ info_mood_change += diff_mood

    $ local_config.info_role.mood_changed = info_mood_change

    # 显示人物提示
    if paopao_info != "":
        show screen paopao(paopao_info=paopao_info)

    $ renpy.retain_after_load()
    call screen roleroom


# 点击平衡薪水，还原debt于薪水值，而后加上1000
label wagetoggle:
    $ info_role_xs = 1000
    
    # 债务恢复
    $ local_config.debt = info_debt
    # 薪水恢复（被二次调整则回溯）
    $ local_config.info_role.salary = info_role_xs
    $ local_config.info_role.salary_changed = True
    # 心情恢复
    if local_config.info_role.salary_changed:
        $ local_config.info_role.mood -= local_config.info_role.mood_changed

    $ local_config.debt += info_role_xs

    $ paopao_info = "{size=+8}有薪水领的感\n    觉真好！{/size}"
    $ local_config.info_role.mood += 5
    $ info_mood_change = 5

    if local_config.info_role.mood > 100:
        $ diff_mood = local_config.info_role.mood - 100
        $ local_config.info_role.mood = 100
        $ info_mood_change -= diff_mood

    $ local_config.info_role.mood_changed = info_mood_change

    if paopao_info != "":
        show screen paopao(paopao_info=paopao_info)

    $ renpy.retain_after_load()
    call screen roleroom


label info:
    if local_config.info_role is None:
        $ info_role_index = 0

    $ local_config.info_role = local_config.party[info_role_index]
    $ info_role_xs = local_config.info_role.salary

    # 如果被二次调整则先回溯
    $ info_debt = local_config.debt
    if local_config.info_role.salary_changed:
        $ info_debt -= local_config.info_role.salary

    # 判断是否是角色切换（重置）
    if not local_config.info_role.watched:
        # 默认薪水为上次保留值判定心情
        if local_config.info_role.salary < 500:
            $ local_config.info_role.mood -= 25
            $ info_mood_change = -25
        elif local_config.info_role.salary < 1500:
            $ local_config.info_role.mood += 5
            $ info_mood_change = 5
        else:
            $ local_config.info_role.mood += 15
            $ info_mood_change = 15

        if local_config.info_role.mood > 100:
            $ diff_mood = local_config.info_role.mood - 100
            $ local_config.info_role.mood = 100
            $ info_mood_change -= diff_mood
        elif local_config.info_role.mood < 0:
            $ diff_mood = 0 - local_config.info_role.mood
            $ local_config.info_role.mood = 0
            $ info_mood_change += diff_mood

        $ local_config.info_role.mood_changed = info_mood_change
        $ local_config.info_role.watched = True

    $ local_config.currentscreen = "info"

    $ renpy.retain_after_load()
    call screen roleroom


screen info():
    on "hide" action [Hide("paopao"), Hide("currentXS"), Return()]

    frame:
        background Solid("#0000FF00")
        xpos -845
        ypos -40
        add "9i/interface/room/images/手下界面.png"

    python:
        left_number = 12 - len(local_config.party)

        def cal_level(attack, hp, defance, speed, name):
            role_result = {}

            # 攻击评级：158以上为S，140以上为A，125以上为B，115以上为C，115以下为D
            if attack >= 158:
                role_result["伤害等级"] = ("S", "#FAE000")
            elif attack >= 140:
                role_result["伤害等级"] = ("A", "#E3523E")
            elif attack >= 125:
                role_result["伤害等级"] = ("B", "#9BD87A")
            elif attack >= 115:
                role_result["伤害等级"] = ("C", "#33A2FF")
            else:
                role_result["伤害等级"] = ("D", "#494B48")

            # 生命评价
            if hp >= 1300:
                role_result["生存能力"] = ("S", "#FAE000")
            elif hp >= 1200:
                if defance >= 70:
                    role_result["生存能力"] = ("S", "#FAE000")
                else:
                    role_result["生存能力"] = ("A", "#E3523E")
            elif hp >= 1100:
                if defance >= 70:
                    role_result["生存能力"] = ("A", "#E3523E")
                else:
                    role_result["生存能力"] = ("B", "#9BD87A")
            elif hp >= 1000:
                if defance >= 70:
                    role_result["生存能力"] = ("B", "#9BD87A")
                else:
                    role_result["生存能力"] = ("C", "#33A2FF")
            else:
                if defance >= 70:
                    role_result["生存能力"] = ("C", "#33A2FF")
                else:
                    role_result["生存能力"] = ("D", "#494B48")

            # 行动力评价
            if speed > 115:
                role_result["行动速度"] = ("S", "#FAE000")
            elif speed >= 111:
                role_result["行动速度"] = ("A", "#E3523E")
            elif speed >= 108:
                role_result["行动速度"] = ("B", "#9BD87A")
            elif speed >= 103:
                role_result["行动速度"] = ("C", "#33A2FF")
            else:
                role_result["行动速度"] = ("D", "#494B48")

            # 角色定位
            role_attribute_maps = {
                "日向爱衣": ("辅助", "{color=#f30}火{/color}"),
                "立花希": ("坦克", "{color=#6f6}风{/color}"),
                "青木铃音": ("输出", "{color=#6f6}风{/color}"),
                "花山院琉璃": ("输出", "{color=#f30}火{/color}"),
                "雷亚": ("全能", "{color=#3ff}冰{/color}"),
                "千川老师": ("控场", "{color=#f0f}雷{/color}"),
                "水之濑凛": ("输出", "{color=#f0f}雷{/color}"),
                "藤原瞳": ("坦克", "{color=#ff0}岩{/color}"),
                "希菲尔": ("全能", "{color=#f30}火{/color}"),
                "青木翔子": ("治疗", "{color=#19f}水{/color}"),
                "一诚小桃": ("控场", "{color=#3ff}冰{/color}"),
                "植澄友加": ("辅助", "{color=#19f}水{/color}")
            }

            role_result["角色定位"], role_result["元素掌握"] = role_attribute_maps[name] 

            return role_result
        '''
        S: #FAE000
        A: #E3523E
        B: #9BD87A
        C: #33A2FF
        D: #494B48
        '''
        role_attribute = cal_level(local_config.info_role.ori_attack, local_config.info_role.ori_max_hp, local_config.info_role.ori_defance, local_config.info_role.ori_speed, local_config.info_role.name)
        role_attack_level, role_attack_level_color = role_attribute["伤害等级"]
        role_health_level, role_health_level_color = role_attribute["生存能力"]
        role_speed_level, role_speed_level_color = role_attribute["行动速度"]
        role_level = role_attribute["角色定位"]
        role_element = role_attribute["元素掌握"]

        elemental_maps = {
            "火": "fire",
            "水": "water",
            "雷": "light",
            "冰": "ice",
            "风": "wind", 
            "岩": "rock"
        }
        # 突破材料个数
        breakout_quest = {
            "20": (5, 0),
            "25": (8, 4),
            "30": (15, 8),
            "35": (30, 15)
        }
        
        item_small_count, item_large_count = 0, 0
        total_need_small, total_need_large = None, None
        if str(local_config.info_role.level) in breakout_quest:
            total_need_small, total_need_large = breakout_quest[str(local_config.info_role.level)]

        # 获取当前拥有的材料数量
        item_name_small = elemental_maps[role_element.split("}")[1].split("{")[0]] + "_break_small"
        item_name_large = elemental_maps[role_element.split("}")[1].split("{")[0]] + "_break_large"
        if item_name_small in local_config.player.items:
            item_small_count = local_config.player.items[item_name_small]
        if item_name_large in local_config.player.items:
            item_large_count = local_config.player.items[item_name_large]

    grid 6 2:
        spacing -13
        xalign 0.252
        yalign 0.8565
        yspacing -29

        for i, role in enumerate(local_config.party):
            imagebutton:
                at customzoom6
                idle "9i/interface/room/images/face/" + role.objectname + ".png"
                action [SetField(local_config, "info_role", role), SetVariable("info_role_index", i), Hide("currentXS"), Hide("paopao"), Hide("info"), Call("info")]

        for _ in xrange(left_number):
            imagebutton:
                at customzoom6
                idle "9i/interface/room/images/face/0.png"

    add "9i/interface/room/images/人物覆盖.png" xalign -0.01 yalign 0.8644
        
    # 选择框
    grid 6 2:
        xspacing 23
        xalign 0.258
        yalign 0.833
        yspacing -1

        for i in range(len(local_config.party)):
            if info_role_index == i:
                add "9i/interface/room/images/selected.png"
            else:
                add "9i/interface/room/images/selected0.png"

        for _ in xrange(left_number):
            add "9i/interface/room/images/selected0.png"

        at customzoom8

    # 角色候选显示
    grid 1 2:
        xalign 0.07
        yalign 0.7865
        yspacing 15

        python:
            can_use_1 = False
            can_use_2 = False
            if local_config.info_role.level < 20:
                can_use_1 = True
            elif local_config.info_role.level < 40:
                if local_config.info_role.level % 5 == 0:
                    if not local_config.info_role.break_through:
                        can_use_2 = True
                    else:
                        can_use_1 = True
                else:
                    can_use_1 = True
                    local_config.info_role.break_through = False

        textbutton "升级" text_selected_color "#666":
            action If(can_use_1, [Function(local_config.info_role.level_up), SelectedIf(False)], false=SelectedIf(True))
        textbutton "突破" text_selected_color "#666":
            action If(can_use_2, [Function(local_config.info_role.level_up), SelectedIf(False)], false=SelectedIf(True))
    
    # 主界面
    frame:
        background Solid("#0000FF00")
        xpos -560
        ypos 34

        hbox:
            xalign 0.402
            yalign 0.235
            add "9i/interface/room/images/face/[local_config.info_role.objectname].png"
            at customzoom
            
        text "{color=#381414}{size=+8}[local_config.info_role.name]{/size}{/color}" xalign 0.415 yalign 0.465 style "mioutline"
        imagebutton:
            xalign 0.4 
            yalign 0.532
            idle "9i/interface/room/images/[local_config.info_role.star]星.png"
        
        hbox:
            xalign 0.705
            yalign 0.34
            spacing -25

            vbox:
                grid 2 7:
                    spacing 10
                    yspacing 5
                    text "等级" style "blackoutline" size 30
                    text "{color=#f5f5f5} [local_config.info_role.level]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "稀有度" style "blackoutline" size 30
                    text "{color=#f5f5f5} [local_config.info_role.rarity]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "伤害等级" style "blackoutline" size 30
                    text "{color=[role_attack_level_color]} [role_attack_level]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "生存能力" style "blackoutline" size 30
                    text "{color=[role_health_level_color]} [role_health_level]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "行动速度" style "blackoutline" size 30
                    text "{color=[role_speed_level_color]} [role_speed_level]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "角色定位" style "blackoutline" size 30
                    text "{color=#f5f5f5} [role_level]{/color}" size 30 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "元素掌握" style "blackoutline" size 30
                    text "{color=#f5f5f5} [role_element]{/color}" size 30 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
            vbox:
                grid 2 8:
                    spacing 10
                    yspacing 5
                    python:
                        store.info_role_max_hp = int(local_config.info_role.max_hp)
                        store.info_role_attack = int(local_config.info_role.attack)
                        store.info_role_defance = int(local_config.info_role.defance)
                        info_role_xp = int(local_config.info_role.xp)
                        info_left_length = 6 - len(str(info_role_xp))
                        info_left_string = "0" * info_left_length

                        level_up_exp = 0
                        if local_config.info_role.level % 2 == 0:
                            level_up_exp = 2.5 * math.pow(local_config.info_role.level, 3) + 22.5 * math.pow(local_config.info_role.level, 2) - 10 * local_config.info_role.level + 150
                        # 奇数
                        else:
                            level_up_exp = 2.5 * math.pow(local_config.info_role.level, 3) + 25 * math.pow(local_config.info_role.level, 2) - 12.5 * local_config.info_role.level + 165
                        level_up_exp = int(level_up_exp)
                        left_length = 6 - len(str(level_up_exp))
                        left_string = "0" * left_length

                    text "生命值" style "blackoutline" size 30
                    text "{color=#f5f5f5}[info_role_max_hp]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "攻击力" style "blackoutline" size 30
                    text "{color=#f5f5f5}[info_role_attack]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "防御力" style "blackoutline" size 30
                    text "{color=#f5f5f5}[info_role_defance]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    text "好感度" style "blackoutline" size 30
                    text "{color=#f5f5f5}[local_config.info_role.love]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    
                    if str(local_config.info_role.level) in breakout_quest and (not local_config.info_role.break_through):
                        text "小材料数" style "blackoutline" size 30
                        text "{color=#f5f5f5}[item_small_count]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                        text "所需材料" style "blackoutline" size 30
                        text "{color=#f5f5f5}[total_need_small]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                        text "大材料数" style "blackoutline" size 30
                        text "{color=#f5f5f5}[item_large_count]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                        text "所需材料" style "blackoutline" size 30
                        text "{color=#f5f5f5}[total_need_large]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                    else:
                        text "经验值" style "blackoutline" size 30
                        if local_config.info_role.xp > 999999:
                            text "{color=#f5f5f5}999999{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                        else:
                            text "{color=#f5f5f5}[info_left_string][info_role_xp]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                        text "升级经验" style "blackoutline" size 30
                        text "{color=#f5f5f5}[left_string][level_up_exp]{/color}" size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                        text " " style "blackoutline" size 30
                        text " " size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]
                        text " " style "blackoutline" size 30
                        text " " size 35 outlines [(0, "#0006", 6, 6), (4, "#000c"), (2, "000")]

        # 心情指标
        # if local_config.info_role.mood >= 75:
        #     add "up" xalign 0.71 yalign 0.41
        #     add "9i/interface/room/images/face/Q_LZG_laugh.png" xalign 0.8625 yalign 0.516 zoom 0.34
        # elif local_config.info_role.mood <= 25:
        #     add "down" xalign 0.71 yalign 0.41
        #     add "9i/interface/room/images/face/Q_LZG_sad.png" xalign 0.8625 yalign 0.516 zoom 0.34
        # else:
        add "9i/interface/room/images/face/Q_LZG_normal.png" xalign 0.8625 yalign 0.516 zoom 0.34
        
        # 薪水调节拉条
        if local_config.player.currency > 0:
            button:
                xalign 0.832
                yalign 0.18

                vbar value VariableValue("info_role_xs", 2000, offset=0, action=Call("refreshXS")):
                    ysize 315
                    xsize 58
                    hovered Show("currentXS")
                    unhovered Hide("currentXS")

                    style_prefix "vslider"
                    top_bar Frame("9i/interface/room/images/slider/vertical_idle_bar.png", 58, 315)
                    bottom_bar Frame("9i/interface/room/images/slider/vertical_idle_bar.png", 58, 315)
                    thumb "9i/interface/room/images/slider/vertical_idle_thumb.png"
        else:
            button:
                xalign 0.832
                yalign 0.18

                vbar value VariableValue("info_role_xs", 0, offset=0, action=NullAction()):
                    ysize 315
                    xsize 58
                    hovered Show("currentXS")
                    unhovered Hide("currentXS")

                    style_prefix "vslider"
                    top_bar Frame("9i/interface/room/images/slider/vertical_idle_bar.png", 58, 315)
                    bottom_bar Frame("9i/interface/room/images/slider/vertical_idle_bar.png", 58, 315)
                    thumb "9i/interface/room/images/slider/vertical_idle_thumb.png"

    imagebutton:
        xalign 0.56
        yalign 0.23

        if local_config.info_role.salary == 1000:
            idle "9i/interface/room/images/button/BT_保持_hover.png"
            if local_config.player.currency > 0:
                action Call("wagetoggle")
        else:
            idle "9i/interface/room/images/button/BT_保持_idle.png"
            if local_config.player.currency > 0:
                action Call("wagetoggle")


screen paopao(paopao_info):
    zorder 100
    timer 3.0 action [SetVariable("paopao_info", ""), Hide("paopao")]

    frame:
        background Solid("#0000FF00")
        xpos -560
        ypos 34
        if paopao_info != "":
            add "9i/interface/room/images/对话框.png" xcenter 0.895 yalign 0.39
            text paopao_info style "blackoutline" xcenter 0.895 yalign 0.378 at sideways3


screen currentXS():
    frame:
        background Solid("#0000FF00")
        xpos -560
        ypos 34
        add "9i/interface/room/images/薪水提示.png" xalign 0.793 yalign 0.125
        text "{size=+8}[info_role_xs]{/size}" style "blackoutline" xcenter 0.768 yalign 0.132
