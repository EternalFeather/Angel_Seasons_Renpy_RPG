
screen alt_confirm(message, yes_action=[], no_action=[]):
    zorder 2
    modal True
    default mouse_pos = renpy.get_mouse_pos()
    on "show" action [MouseMove(config.screen_width * 0.5, config.screen_height * 0.5, 0.15), Hide("alt_notify")]

    frame align (0.5, 0.5) xysize (900, 130):
        at gui_dissolve_top
        has vbox
        label message xalign 0.5 ysize 40
        textbutton _("确定") xfill True default True:
            activate_sound None
            action [yes_action, MouseMove(mouse_pos[0], mouse_pos[1], 0.15), Hide("alt_confirm")]
        textbutton _("取消") xfill True:
            activate_sound None
            action [no_action, MouseMove(mouse_pos[0], mouse_pos[1], 0.15), Hide("alt_confirm")]

    key "game_menu":
        action [no_action, MouseMove(mouse_pos[0], mouse_pos[1], 0.15), Hide("alt_confirm")]


screen alt_notify(message):
    zorder 2

    window background Frame("9i/interface/battle/system/frame4.png", 18, 18) align (0.99, 0.02) xysize (480, 125):
        at gui_dissolve_right
        text message align(0.5, 0.5) style "say_dialogue2"

    timer 2.0 action Hide("alt_notify")


screen message_screen(message):
    zorder 2
    on "show" action Hide("alt_notify")

    window background Frame("9i/interface/battle/system/frame4.png", 18, 18) align (0.99, 0.02) xysize (480, 125):
        at gui_dissolve_right
        text message align(0.5, 0.5) style "say_dialogue2"


# 商店界面
screen shop():
    on "hide" action [Hide("alt_notify"), Hide("message_screen")]

    label _("{#shop}SHOP") style "caption_label" at caption_inter

    frame xpos 80 ypos 150 xsize 240 style_group "nav_menu":
        at gui_dissolve_left
        has vbox
        textbutton _("购买") action [With(Dissolve(0.25)), SetField(local_config, "current_mode", "buy")] default True
        textbutton _("贩卖") action [With(Dissolve(0.25)), SetField(local_config, "current_mode", "sell")]
        textbutton _("返回") action [Play("battle_music", "Cancel_Button"), Return()]

    frame xpos 675 ypos 30 xpadding 15 background Frame("9i/interface/battle/system/miniframe.png", 18, 18):
        at gui_dissolve_top
        has hbox
        text _("魔法币") style "say_dialogue2"
        $ currency_number = local_config.player.currency
        text "[currency_number:>6]" text_align 1.0 min_width 150 style "say_dialogue2"

    if local_config.current_mode == "buy":
        use stock_frame("buy")
    elif local_config.current_mode == "sell":
        use stock_frame("sell")

    window xalign 0.1:
        at gui_dissolve_bottom
        text local_config.current_message style "say_dialogue2" size 30 yoffset 8

    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()


screen stock_frame(actiontype):
    python:
        adj = ui.adjustment(1.0, step=100, changed=store_yvalue)
        if actiontype == "buy":
            listitem = local_config.shop_list
        else:
            listitem = local_config.player.items

    style_group "item"

    frame xpos 350 ypos 150 xysize(850, 600):
        at nav_dissolve_top
        has vbox
        if actiontype == "buy":
            label _("可挑选物品：")
        else:
            label _("可出售物品：")
        hbox:
            viewport yadjustment adj:
                has vbox
                for i in listitem:
                    python:
                        item = getattr(store, i)
                    hbox xfill True:
                        if actiontype == "buy":
                            textbutton item.name style "item_button" xsize 645:
                                action Show("alt_confirm", message=_("确定要购买此物品吗？"), yes_action=Function(item.buy, who=local_config.player))
                                hovered SetField(local_config, "current_message", item.info)
                        elif actiontype == "sell":
                            $ has_item_number = listitem[i]
                            textbutton item.name + " x [has_item_number]" style "item_button" xsize 645:
                                action Show("alt_confirm", message=_("确定要出售此物品吗？"), yes_action=Function(item.sell, who=local_config.player))
                                hovered SetField(local_config, "current_message", item.info)
                        
                        if actiontype == "buy":
                            text "[item.cost:>6]"
                        elif actiontype == "sell":
                            text "[item.sellcost:>6]"
            null width 6
            fixed yalign 0.5 xysize (15, 525):
                add Frame("9i/interface/battle/system/vscrollbar.png", 18, 9)
                bar style "vscrollbar" adjustment adj


# 队伍角色状态界面
screen stats():
    tag menu
    on "show" action [SetField(local_config, "current_mode", "Consumables"), SetField(local_config, "chosen_actor", None), SetField(local_config, "chosen_skill", None), SetField(local_config, "chosen_item", None)]
    on "hide" action Hide("alt_notify")
    add Solid("#0006") at gui_dissolve

    if local_config.active_actor:
        $ local_config.current_actor = local_config.active_actor
        # add Transform(local_config.current_actor.objectname, anchor=(0.5, 0.5)) at show_player(0.85)
        add local_config.current_actor.objectname at show_player(0.85)
    else:
        if local_config.current_actor is None:
            $ local_config.current_actor = local_config.party[0]
        # add Transform(local_config.current_actor.objectname, anchor=(0.5, 0.5)) at show_player(0.85)
        add local_config.current_actor.objectname at show_player(0.85)
        
    label _("{#stats}STATS") style "caption_label" at caption_inter

    frame xpos 65 ypos 150 xsize 240 style_group "nav_menu":
        at nav_dissolve_left
        has vbox
        if local_config.current_mode == "Organize":
            if not local_config.chosen_actor and not local_config.chosen_skill and not local_config.chosen_item:
                textbutton _("解散") default True:
                    action Show("alt_confirm", message=_("确定要清除当前的队伍成员吗？"), yes_action=Function(local_config.player.disband))
        textbutton _("状态") default True:
            action [With(Dissolve(0.25)), SelectedIf(local_config.current_mode == "Consumables"), SetField(local_config, "current_mode", "Consumables")]
        textbutton _("队伍"):
            if not local_config.chosen_actor and not local_config.chosen_skill and not local_config.chosen_item:
                action [With(Dissolve(0.25)), SelectedIf(local_config.current_mode == "Organize"), SetField(local_config, "current_mode", "Organize")]
        textbutton _("保存游戏"):
            action ShowMenu("save") activate_sound None
        textbutton _("载入游戏"):
            action ShowMenu("load") activate_sound None
        textbutton _("游戏设置"):
            action ShowMenu("preferences") activate_sound None
        textbutton _("返回"):
            if not local_config.chosen_actor and not local_config.chosen_skill and not local_config.chosen_item:
                action [Return()] activate_sound None

    frame xpos 15 ypos 455 xpadding 15 background Frame("9i/interface/battle/system/miniframe.png", 18, 18):
        at gui_dissolve_top
        has hbox
        text _("魔法币") style "say_dialogue2"
        $ currency_number = local_config.player.currency
        text "[currency_number:>6]" text_align 1.0 min_width 150 style "say_dialogue2"
    if local_config.current_mode == "Organize":
        use backup_frame()
    else:
        use item_frame(local_config.current_mode)
    use attribute_frame(local_config.current_actor)

    window align (0.35, 0.65) ysize 195:
        at gui_dissolve_top
        text local_config.current_message style "say_dialogue2" size 20 yoffset 8
        text local_config.current_ex_message outlines [(1, "#0009", 1, 1), (1, "#000d")] yoffset -15

    use status_frame(local_config.party[0], position=(7, -157), mode=local_config.current_mode)
    if len(local_config.party) > 1:
        use status_frame(local_config.party[1], position=(442, -157), mode=local_config.current_mode)
    if len(local_config.party) > 2:
        use status_frame(local_config.party[2], position=(877, -157), mode=local_config.current_mode)
    if len(local_config.party) > 3:
        use status_frame(local_config.party[3], position=(7, -7), mode=local_config.current_mode)
    if len(local_config.party) > 4:
        use status_frame(local_config.party[4], position=(442, -7), mode=local_config.current_mode)
    if len(local_config.party) > 5:
        use status_frame(local_config.party[5], position=(877, -7), mode=local_config.current_mode)

    key "game_menu" action NullAction()

    key "K_TAB" action NullAction()
    key "hide_windows" action NullAction()


# 道具界面
screen item_frame(current_mode):
    python:
        adj = ui.adjustment(1.0, step=100, changed=store_yvalue)
        listitem = local_config.player.items
        battle_items = ["eggs", "mana_eggs", "mana_potion", "angel_tears", "attack_meal", "defance_meal", "ele_attack_meal", "ele_defance_meal", "magic_meal"]
        role_items = ["soul_piece", "soul_raise"]

    frame xpos 320 ypos 150 xysize (450, 400):
        at gui_dissolve_top
        has vbox
        hbox xfill True:
            label "物品"
            textbutton _("整理") style "small_button" xalign 1.0 yalign 0.5:
                if not local_config.chosen_actor and not local_config.chosen_skill and not local_config.chosen_item:
                    action Show("alt_confirm", message= _("是否对物品进行整理？"), yes_action=Function(local_config.player.item_sort))

        hbox:
            viewport yadjustment adj:
                has vbox
                for i, counts in listitem.items():
                    hbox xfill True:
                        python:
                            item = getattr(store, i)
                            itemname = item.name
                        textbutton itemname + " * [counts]" style "item_button":
                            if (i not in battle_items and local_config.in_battle) or (i not in role_items and not local_config.in_battle):
                                action NullAction()
                            elif not local_config.chosen_actor and not local_config.chosen_skill:
                                if local_config.chosen_item:
                                    action [SelectedIf(local_config.chosen_item==item)]
                                elif item.use_target == "multi":
                                    action [SetField(local_config, "chosen_item", item), Show("alt_confirm", message=_("确认使用该物品吗？"),
                                                yes_action=Function(item.use, who=local_config.player, ally_environment_effects=ally_environment_effects), no_action=SetField(local_config, "chosen_item", None))]
                                    hovered [SetField(local_config, "current_message", item.info), SetField(local_config, "current_ex_message", "")]
                                # elif local_config.in_battle:
                                action [SetField(local_config, "chosen_item", item), Show("message_screen", message=_("请选择物品使用对象。"))]
                                hovered [SetField(local_config, "current_message", item.info), SetField(local_config, "current_ex_message", "")]
                                # else:
                                #     action NullAction()
                                #     hovered [SetField(local_config, "current_message", item.info), SetField(local_config, "current_ex_message", "")]
            null width 6
            fixed yalign 0.5 xysize(15, 325):
                add Frame("9i/interface/battle/system/vscrollbar.png", 18, 9)
                bar style "vscrollbar" adjustment adj


screen backup_frame():
    python:
        adj = ui.adjustment(1.0, step=105, changed=store_yvalue)

    frame xpos 320 ypos 150 xysize (450, 400):
        at gui_dissolve_top
        has vbox
        hbox xfill True:
            label _("队伍")
            textbutton _("排序") style "small_button" xalign 1.0 yalign 0.5:
                action Show("alt_confirm", message= _("是否对队伍成员进行整理？"), yes_action=Function(local_config.player.sort))
        hbox:
            vpgrid cols 4 yadjustment adj:
                for i in local_config.backup:
                    fixed xysize (105, 105):
                        if renpy.loadable("9i/interface/battle/actors/{}/chip.png".format(i.objectname)):
                            add "9i/interface/battle/actors/{}/chip.png".format(i.objectname) pos (1, 1)
                        button style "face_button":
                            if not local_config.chosen_skill:
                                action [Function(i.add)]
                            hovered [SetField(local_config, "current_actor", i), SetField(local_config, "current_message", i.info), SetField(local_config, "current_ex_message", "")]
            null width 6
            fixed yalign 0.5 xysize (15, 325):
                add Frame("9i/interface/battle/system/vscrollbar.png", 18, 9)
                bar style "vscrollbar" adjustment adj


# 角色属性界面
screen attribute_frame(who, xcoord=800):
    frame xysize (600, 547) pos (xcoord, 15) style_group "attributes" at gui_dissolve_top:
        has vbox
        hbox xfill True:
            text "[who.name]" font font_label size 53 min_width 300
            text "Lv：%2d" % (who.level) size 22 yalign 1.0
            text "经验值：%02d" % (who.xp) size 22 yalign 1.0

        label _("属性")

        hbox xfill True:
            vbox:
                button action NullAction() activate_sound None:
                    text "攻击" size 24
                    hovered [SetField(local_config, "current_message", _("攻击力属性，数值越高角色所造成的伤害越高。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "防御" size 24
                    hovered [SetField(local_config, "current_message", _("防御力属性，数值越高角色承受的伤害越低。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "速度" size 24
                    hovered [SetField(local_config, "current_message", _("速度属性，数值越高角色行动的频率越高。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "暴击率" size 24
                    hovered [SetField(local_config, "current_message", _("暴击率属性，数值越高角色造成的暴击概率越高。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "暴击伤害" size 24
                    hovered [SetField(local_config, "current_message", _("暴击伤害属性，数值越高角色暴击时造成的伤害越高。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "效果命中" size 24
                    hovered [SetField(local_config, "current_message", _("效果命中属性，数值越高角色技能所附加的效果更容易命中。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "效果抵抗" size 24
                    hovered [SetField(local_config, "current_message", _("效果抵抗属性，数值越高角色承受的技能负面效果越难命中。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "元素精通" size 24
                    hovered [SetField(local_config, "current_message", _("元素精通属性，数值越高角色所引发的元素反应效果越强（包括：蒸发伤害、融化伤害、感电伤害、冻结概率、超导减抗倍率、超载伤害、扩散减抗倍率、结晶护盾强效等)。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "治疗加成" size 24
                    hovered [SetField(local_config, "current_message", _("治疗加成属性，数值越高角色所受到的治疗效果越强。")), SetField(local_config, "current_ex_message", "")]
                button action NullAction() activate_sound None:
                    text "护盾强度" size 24
                    hovered [SetField(local_config, "current_message", _("护盾强效属性，数值越高角色所获得的护盾强度越大。")), SetField(local_config, "current_ex_message", "")]
            vbox:
                if local_config.in_battle:
                    for attr in ["battle_attack", "battle_defance", "battle_speed"]:
                        $ value1 = int(getattr(who, attr))
                        if attr == "battle_attack":
                            $ value2 = int(getattr(who, "battle_extend_attack"))
                            $ value3 = -value2
                            if value2 >= 0:
                                text "[value1] + [value2]" size 24 min_width 24
                            else:
                                text "[value1] {color=#ff0000}- [value3]{/color}" size 24 min_width 24
                        elif attr == "battle_defance":
                            $ value2 = int(getattr(who, "battle_extend_defance"))
                            $ value3 = -value2
                            if value2 >= 0:
                                text "[value1] + [value2]" size 24 min_width 24
                            else:
                                text "[value1] {color=#ff0000}- [value3]{/color}" size 24 min_width 24
                        else:
                            text "[value1]" size 24 min_width 24
                    for attr in ["battle_critical_rate", "battle_critical_damage", "battle_effect_hitrate", "battle_effect_resistance", "battle_elemental_mastery", "battle_healing_bonus", "battle_shield_strength"]:
                        $ value1 = getattr(who, attr)
                        if value1 >= 0:
                            if attr != "battle_elemental_mastery":
                                $ value1 = get_icons_v2(value1)
                            else:
                                $ value1 = int(value1)
                            text "[value1]" size 24 min_width 24
                        else:
                            if attr != "battle_elemental_mastery":
                                $ value1 = get_icons_v2(value1)
                            else:
                                $ value1 = int(value1)
                            text "{color=#ff0000}[value1]{/color}" size 24 min_width 24
                else:
                    for attr in ["attack", "defance", "speed"]:
                        $ value1 = int(getattr(who, attr))
                        if attr == "attack":
                            $ value2 = int(getattr(who, "extend_attack"))
                            text "[value1] + [value2]" size 24 min_width 24
                        elif attr == "defance":
                            $ value2 = int(getattr(who, "extend_defance"))
                            text "[value1] + [value2]" size 24 min_width 24
                        else:
                            text "[value1]" size 24 min_width 24
                    for attr in ["critical_rate", "critical_damage", "effect_hitrate", "effect_resistance", "elemental_mastery", "healing_bonus", "shield_strength"]:
                        $ value1 = getattr(who, attr)
                        if attr != "elemental_mastery":
                            $ value1 = get_icons_v2(value1)
                        else:
                            $ value1 = int(value1)
                        text "[value1]" size 24 min_width 24
            vbox:
                for attr_name in [_("{color=#9cf}物伤加成{/color}"), _("{color=#f30}火伤加成{/color}"), _("{color=#f0f}雷伤加成{/color}"), _("{color=#6f6}风伤加成{/color}"), _("{color=#3ff}冰伤加成{/color}"), _("{color=#99f}水伤加成{/color}"), _("{color=#ff0}岩伤加成{/color}")]:
                    python:
                        element_string = attr_name.split("}")[1].split("伤加成")[0] + "元素"
                        if element_string == "物元素":
                            element_string = "物理"
                    button action NullAction() activate_sound None:
                        text " [attr_name]" size 24
                        hovered [SetField(local_config, "current_message", _("%s伤害加成属性，数值越高角色所造成的%s伤害越强。" % (element_string, element_string))), SetField(local_config, "current_ex_message", "")]
            vbox:
                if local_config.in_battle:
                    for attr in ["battle_physical_damage_bonus", "battle_fire_damage_bonus", "battle_light_damage_bonus", "battle_wind_damage_bonus", "battle_ice_damage_bonus", "battle_water_damage_bonus", "battle_rock_damage_bonus"]:
                        $ value1 = getattr(who, attr)
                        if value1 >= 0:
                            $ value1 = get_icons_v2(value1)
                            text "[value1]" size 24 min_width 75
                        else:
                            $ value1 = get_icons_v2(value1)
                            text "{color=#ff0000}[value1]{/color}" size 24 min_width 75
                else:
                    for attr in ["physical_damage_bonus", "fire_damage_bonus", "light_damage_bonus", "wind_damage_bonus", "ice_damage_bonus", "water_damage_bonus", "rock_damage_bonus"]:
                        $ value1 = getattr(who, attr)
                        $ value1 = get_icons_v2(value1)
                        text "[value1]" size 24 min_width 75
            vbox:
                for attr_name in [_("{color=#9cf}物抗{/color}"), _("{color=#f30}火抗{/color}"), _("{color=#f0f}雷抗{/color}"), _("{color=#6f6}风抗{/color}"), _("{color=#3ff}冰抗{/color}"), _("{color=#99f}水抗{/color}"), _("{color=#ff0}岩抗{/color}")]:
                    python:
                        element_string = attr_name.split("}")[1].split("抗")[0] + "元素"
                        if element_string == "物元素":
                            element_string = "物理"
                    button action NullAction() activate_sound None:
                        text " [attr_name]" size 24
                        hovered [SetField(local_config, "current_message", _("%s抗性属性，数值越高角色所受到的%s伤害越低。" % (element_string, element_string))), SetField(local_config, "current_ex_message", "")]
            vbox:
                if local_config.in_battle:
                    for attr in ["battle_physical_elemental_resistance", "battle_fire_elemental_resistance", "battle_light_elemental_resistance", "battle_wind_elemental_resistance", "battle_ice_elemental_resistance", "battle_water_elemental_resistance", "battle_rock_elemental_resistance"]:
                        $ value1 = getattr(who, attr)
                        if value1 >= 0:
                            $ value1 = get_icons_v2(value1)
                            text "[value1]" size 24 min_width 75
                        else:
                            $ value1 = get_icons_v2(value1)
                            text "{color=#ff0000}[value1]{/color}" size 24 min_width 75
                else:
                    for attr in ["physical_elemental_resistance", "fire_elemental_resistance", "light_elemental_resistance", "wind_elemental_resistance", "ice_elemental_resistance", "water_elemental_resistance", "rock_elemental_resistance"]:
                        $ value1 = getattr(who, attr)
                        $ value1 = get_icons_v2(value1)
                        text "[value1]" size 24 min_width 75

        label _("天赋 | 套装 | 技能")

        hbox xfill True:
            for i in who.abilities:
                button style "attributes_button" action NullAction() activate_sound None:
                    text i size 24 min_width 105
                    hovered [SetField(local_config, "current_message", ability_dict[i]), SetField(local_config, "current_ex_message", "")]
            if who.equip4effect is not None:
                button style "attributes_button" action NullAction() activate_sound None:
                    text who.equip4effect size 24 min_width 105
                    hovered [SetField(local_config, "current_message", who.equip4effect_info), SetField(local_config, "current_ex_message", "")]
            for j in xrange(6 - len(who.abilities)):
                button style "attributes_button":
                    text "" size 24 min_width 105

        python:
            skill_lists = who.skills if not who.is_phase2 else who.skills_v2
        
        null height 12
        grid 2 3 transpose False style_group "skill":
            for n, i in enumerate(skill_lists):
                textbutton i.name:
                    # if local_config.chosen_actor and local_config.chosen_item:
                    #     if n > 0:
                    #         action [SetVariable("chosen_skill", i), Show("alt_confirm", message=_("该栏位已经有一个技能了，是否覆盖该技能？"),
                    #                 yes_action=[Function(chosen_item.use, who=player, target=chosen_actor)], no_action=SetVariable("chosen_skill", None))]
                    # elif not chosen_actor and not chosen_item:
                    #     activate_sound None
                    #     action [SelectedIf(chosen_skill==i), Function(i.order_change, who=current_actor)]
                    action NullAction()
                    hovered [SetField(local_config, "current_message",  i.get_info(who)), SetField(local_config, "current_ex_message", i.get_ex_info(who))]
            for i in xrange(6 - len(skill_lists)):
                textbutton "":
                    # if chosen_actor and chosen_item:
                    #     action [Show("alt_confirm", message=_("是否学习该技能？"),
                    #             yes_action=[Function(chosen_item.use, who=player, target=chosen_actor)])]
                    action NullAction()


# 角色状态栏
screen status_frame(who, ally_environment_effects=None, order_members=None, position=None, mode=""):
    button xysize (435, 150) style "slot_button2" bottom_padding 0:
        if position[0] < 0:
            xanchor 1.0
            pos (config.screen_width + position[0], position[1])
        elif position[1] < 0:
            yanchor 1.0
            pos (position[0], config.screen_height + position[1])
        elif position[1] < 0 and position[0] < 0:
            yanchor 1.0 xanchor 1.0
            pos (config.screen_width + position[0], config.screen_height + position[1])
        else:
            pos position
        if position[1] < 0:
            at gui_dissolve_bottom
        else:
            at gui_dissolve_top
        
        # 在没有选择技能的时候呼叫了菜单栏（右键）
        if mode in ["Consumables", "Stats"] and not local_config.chosen_skill:
            # 如果已经点击了道具和人物（使用道具给人物）
            if local_config.chosen_item and local_config.chosen_actor:
                action SelectedIf(local_config.chosen_actor==who)
            # 如果选择了道具（道具使用）
            elif local_config.chosen_item:
                action Function(local_config.chosen_item.use, who=local_config.player, target=who, ally_environment_effects=ally_environment_effects) activate_sound None
            # 战斗时替换角色
            elif local_config.active_actor != None and who.hp > 0 and local_config.party.index(who) > 2:
                if local_config.in_battle:
                    action Show("alt_confirm", message=_("是否交换队员顺序？"), yes_action=[Function(who.member_change, target=local_config.active_actor, ally_environment_effects=ally_environment_effects, in_battle=True, order_members=order_members), Return("change")])
                else:
                    action Show("alt_confirm", message=_("是否交换队员顺序？"), yes_action=[Function(who.member_change, target=local_config.active_actor), Return("change")])
            # 非战斗时替换角色顺序
            elif local_config.active_actor == None:
                action [SelectedIf(local_config.chosen_actor==who), Function(who.order_change)]
            else:
                action Show("alt_notify", message=_("只能从队伍成员中选择对象。"))
            
            # 未选择任何东西，以该角色为选择对象
            if not local_config.chosen_item or not local_config.chosen_actor:
                hovered [SetField(local_config, "current_actor", who), SetField(local_config, "current_message", who.info), SetField(local_config, "current_ex_message", "")]
        # 盟友角色选择模式
        elif mode == "Ally":
            if who in [local_config.active_actor, local_config.shown_actor]:
                background Fixed(Frame("9i/interface/battle/system/frame4.png", 18, 18),
                    Transform(Frame("9i/interface/battle/system/frame4.png", 18, 18), additive=0.2), fit_first=True)
            else:
                background Frame("9i/interface/battle/system/frame4.png", 18, 18)
        # 队伍管理模式
        elif mode == "Organize" and not local_config.chosen_skill:
            action [Function(who.pop)]
            hovered [SetField(local_config, "current_actor", who), SetField(local_config, "current_message", who.info), SetField(local_config, "current_ex_message", "")]
        # 敌方角色选择模式
        elif mode == "Enemy":
            background None

        if who == nobody:
            text _("―― Empty ――") align (0.5, 0.5) style "say_label2"
        else:
            vbox spacing -4:
                hbox:
                    text "[who.name]" size 25 style "say_label2" min_width 45

                    # buff显示栏位
                    vbox:
                        hbox:
                            if len(who.ebuff) == 0:
                                null height 27
                            else:
                                python:
                                    element_maps = {
                                                "fire": "火元素",
                                                "light": "雷元素",
                                                "wind": "风元素",
                                                "water": "水元素",
                                                "ice": "冰元素",
                                                "rock": "岩元素",
                                                "physical": "物理"
                                            }

                                    store.element_string = "无元素"
                                    value = ""
                                    for buff_name, string_value in element_maps.items():
                                        if buff_name in who.ebuff:
                                            value = who.ebuff[buff_name]
                                            store.element_string = string_value
                                            break

                                fixed xysize (29, 29):
                                    add "9i/interface/battle/ebuff/%s.png" % buff_name zoom 0.65
                                    button action NullAction():
                                        activate_sound None
                                        hovered [SetField(local_config, "current_message", _("[element_string]附着。")), SetField(local_config, "current_ex_message", "")]
                                text "%d" % value yalign 1.0 size 12 outlines [(1, "#341f1b", 1, 1)]
                        null height 5
                        hbox:
                            $ buff_count = 0
                            for buff, value in who.buff.items():
                                if buff_count < 9:
                                    python:
                                        element_maps = {
                                            "fire": "火元素",
                                            "light": "雷元素",
                                            "wind": "风元素",
                                            "water": "水元素",
                                            "ice": "冰元素",
                                            "rock": "岩元素",
                                            "physical": "物理"
                                        }
                                        time, value_list = value
                                        buff_obj = getattr(store, buff)
                                        new_value_list = []
                                        if not isinstance(value_list, tuple):
                                            if isinstance(value_list, float):
                                                value_list = get_icons_v2(value_list)
                                                new_value_list.append(value_list)
                                            elif value_list:
                                                new_value_list.append(value_list)
                                        else:
                                            for i in value_list:
                                                if isinstance(i, float):
                                                    new_value_list.append(get_icons_v2(i))
                                                elif i in element_maps:
                                                    new_value_list.append(element_maps[i])
                                                elif i:
                                                    new_value_list.append(i)
                                        if time != 99:
                                            new_value_list = tuple(new_value_list) + (time,)
                                        else:
                                            new_value_list = tuple(new_value_list)

                                    fixed xysize (26, 26):
                                        add "9i/interface/battle/buff/%s.png" % buff_obj.objectname zoom 0.65
                                        button action NullAction():
                                            activate_sound None
                                            if len(new_value_list) > 0:
                                                hovered [SetField(local_config, "current_message", _(buff_obj.info % new_value_list)), SetField(local_config, "current_ex_message", "")]
                                            else:
                                                hovered [SetField(local_config, "current_message", _(buff_obj.info)), SetField(local_config, "current_ex_message", "")]
                                    if value[0] != 99:
                                        text "%d" % value[0] yalign 1.0 size 12 outlines [(1, "#341f1b", 1, 1)]
                                    else:
                                        if buff in ["ghost_mask", "love"]:
                                            text "%d" % value[1] yalign 1.0 size 12 outlines [(1, "#341f1b", 1, 1)]
                                        else:
                                            text " " yalign 1.0 size 12 outlines [(1, "#341f1b", 1, 1)]
                                    $ buff_count += 1
                            for buff, value in who.debuff.items():
                                if buff_count < 9:
                                    python:
                                        element_maps = {
                                            "fire": "火元素",
                                            "light": "雷元素",
                                            "wind": "风元素",
                                            "water": "水元素",
                                            "ice": "冰元素",
                                            "rock": "岩元素",
                                            "physical": "物理"
                                        }
                                        time, value_list = value
                                        buff_obj = getattr(store, buff)
                                        new_value_list = []
                                        if not isinstance(value_list, tuple):
                                            if isinstance(value_list, float):
                                                value_list = get_icons_v2(value_list)
                                                new_value_list.append(value_list)
                                            elif value_list:
                                                new_value_list.append(value_list)
                                        else:
                                            for i in value_list:
                                                if isinstance(i, float):
                                                    new_value_list.append(get_icons_v2(i))
                                                elif i in element_maps:
                                                    new_value_list.append(element_maps[i])
                                                elif i:
                                                    new_value_list.append(i)
                                        if time != 99:
                                            new_value_list = tuple(new_value_list) + (time,)
                                        else:
                                            new_value_list = tuple(new_value_list)
                                    fixed xysize (26, 26):
                                        add "9i/interface/battle/buff/%s.png" % buff_obj.objectname zoom 0.65
                                        button action NullAction():
                                            activate_sound None
                                            if len(new_value_list) > 0:
                                                hovered [SetField(local_config, "current_message", _(buff_obj.info % new_value_list)), SetField(local_config, "current_ex_message", "")]
                                            else:
                                                hovered [SetField(local_config, "current_message", _(buff_obj.info)), SetField(local_config, "current_ex_message", "")]
                                    if value[0] != 99:
                                        text "%d" % value[0] yalign 1.0 size 12 outlines [(1, "#341f1b", 1, 1)]
                                    else:
                                        text " " yalign 1.0 size 12 outlines [(1, "#341f1b", 1, 1)]
                            if buff_count == 0:
                                null height 27
                vbox:
                    null height 12
                    hbox:
                        text "HP" line_leading -4 size 30 min_width 45 outlines [(1, "#341f1b", 1, 1)]
                        fixed fit_first True:
                            add Transform(Frame("9i/interface/battle/system/bar_disabled.png", 18, 9), size=(345, 27))
                            if local_config.in_battle:
                                bar value AnimatedValue(who.hp, who.battle_max_hp, 1.0)
                                bar value AnimatedValue(who.hp, who.battle_max_hp, 0.3) left_bar Frame("9i/interface/battle/system/bar_green.png", 18, 9)
                                text "{:0>3}/{:0>3}".format(int(who.hp), int(who.battle_max_hp)) line_leading -7 size 31 xalign 0.9 outlines [(1, "#341f1b", 1, 1)]
                            else:
                                bar value AnimatedValue(who.hp, who.max_hp + who.extend_max_hp, 1.0)
                                bar value AnimatedValue(who.hp, who.max_hp + who.extend_max_hp, 0.3) left_bar Frame("9i/interface/battle/system/bar_green.png", 18, 9)
                                text "{:0>3}/{:0>3}".format(int(who.hp), int(who.max_hp + who.extend_max_hp)) line_leading -7 size 31 xalign 0.9 outlines [(1, "#341f1b", 1, 1)]
                    null height 6
                    hbox:
                        text "MP" line_leading -4 size 30 min_width 45 outlines [(1, "#341f1b", 1, 1)]
                        fixed fit_first True:
                            add Transform(Frame("9i/interface/battle/system/bar_disabled.png", 18, 9), size=(345, 27))
                            bar value AnimatedValue(who.mp, who.max_mp, 1.0)
                            bar value AnimatedValue(who.mp, who.max_mp, 0.3) left_bar Frame("9i/interface/battle/system/bar_blue.png", 18, 9)
                            text "{:0>3}/{:0>3}".format(int(who.mp), int(who.max_mp)) line_leading -7 size 31 xalign 0.9 outlines [(1, "#341f1b", 1, 1)]


# 异界界面
screen teleporter(day):
    $ adj = ui.adjustment(1.0, step=190, changed=store_yvalue)

    frame background Frame("9i/interface/battle/system/frame_back.png", 18, 18) align (0.5, 0.4) xpadding 30 ypadding 30 at gui_dissolve_top:
        has hbox
        vbox:
            label "选择一个异界之门" background "9i/interface/battle/system/frame_label.png" xysize (1440, 66) text_size 30 xpadding 15 ypadding 15
            null height 24
            frame xysize (1443, 747) background Frame("9i/interface/battle/system/frame_front.png", 18, 18) xpadding 30 ypadding 30:
                has vbox yfill True
                hbox style_group "teleporter":
                    vpgrid cols 4 xysize (1350, 510) xfill True spacing 30 yadjustment adj:
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon0.png" xoffset 6 yoffset 6
                            button action [Play("battle_music", "Cancel_Button"), Return()] default True:
                                activate_sound None
                                hovered SetField(local_config, "current_message", _("返回弗兰的精神时光屋"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon1.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_attack_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("金币副本"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon2.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_protect_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("经验副本"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon3.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_speed_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("突破材料副本"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon4.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_fire_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("装备副本-火之间（日之轮-曦禾 | 夏之声-朱明 | 火属性手杖 | 火属性宝石）"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon5.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_light_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("装备副本-雷之间（月之华-琼勾 | 天之印-碧落 | 雷属性手杖 | 雷属性宝石）"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon6.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_water_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("装备副本-水之间（海之澜-沧渊 | 地之轴-方仪 | 水属性手杖 | 水属性宝石）"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon7.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_ice_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("装备副本-冰之间（雪之嚣-玉絮 | 冬之羽-玄英 | 冰属性手杖 | 冰属性宝石）"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon8.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_rock_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("装备副本-岩之间（山之巅-玉嶂 | 秋之韵-素律 | 岩属性手杖 | 岩属性宝石）"))
                            add "9i/interface/battle/system/slot_frame.png"
                        fixed xysize (252, 148):
                            add "9i/interface/battle/system/d_icon9.png" xoffset 6 yoffset 6
                            button action [Stop("music", fadeout=3.0), Jump("battle_wind_%s" % day)]:
                                hovered SetField(local_config, "current_message", _("装备副本-风之间（风之陨-松吹 | 春之花-仑灵 | 风属性手杖 | 风属性宝石）"))
                            add "9i/interface/battle/system/slot_frame.png"

                    fixed yalign 0.5 xysize (27, 480):
                        add Frame("9i/interface/battle/system/scroll_back.png", 18, 9)
                        bar style "alt_vscrollbar" adjustment adj

                null height 6
                window xysize (1350, 180) background Frame("9i/interface/battle/system/frame_info.png", 18, 18):
                    text local_config.current_message

    key "game_menu" action [Play("battle_music", "Cancel_Button"), Return()]

    key "hide_windows" action NullAction()
    key "K_F9" action QuickLoad()


# 战斗界面
screen battle_ui(party, enemy, battleorder, extend_party=None, extend_enemy=None):
    zorder 100

    # 我方角色信息显示
    use status_frame(party[0], position=(7, -7), mode="Ally")
    if len(party) > 1:
        use status_frame(party[1], position=(442, -7), mode="Ally")
    if len(party) > 2:
        use status_frame(party[2], position=(877, -7), mode="Ally")
    
    # 敌方信息显示
    if extend_enemy is not None:
        # 额外角色信息
        if len(enemy) == 1:
            if enemy[0].hp > 0:
                use status_frame(enemy[0], position=(157, 7), mode="Enemy")
            if extend_enemy.hp > 0:
                use status_frame(extend_enemy, position=(727, 7), mode="Enemy")
        elif len(enemy) == 2:
            if len(enemy) > 0 and enemy[0].hp > 0:
                use status_frame(enemy[0], position=(7, 7), mode="Enemy")
            if len(enemy) > 1 and enemy[1].hp > 0:
                use status_frame(enemy[1], position=(442, 7), mode="Enemy")
            if extend_enemy.hp > 0:
                use status_frame(extend_enemy, position=(877, 7), mode="Enemy")
    else:
        if len(enemy) == 1:
            if enemy[0].hp > 0:
                use status_frame(enemy[0], position=(442, 7), mode="Enemy")
        elif len(enemy) == 2:
            if enemy[0].hp > 0:
                use status_frame(enemy[0], position=(157, 7), mode="Enemy")
            if enemy[1].hp > 0:
                use status_frame(enemy[1], position=(727, 7), mode="Enemy")
        else:
            if len(enemy) > 0 and enemy[0].hp > 0:
                use status_frame(enemy[0], position=(7, 7), mode="Enemy")
            if len(enemy) > 1 and enemy[1].hp > 0:
                use status_frame(enemy[1], position=(442, 7), mode="Enemy")
            if len(enemy) > 2 and enemy[2].hp > 0:
                use status_frame(enemy[2], position=(877, 7), mode="Enemy")

    # 行动条显示
    hbox pos (0.72, 0.02) ysize 108:
        at gui_dissolve_top
        for i, absolute_name in enumerate(battleorder.bar):
            python:
                role = getattr(store, absolute_name)
                for xi in range(1, 6):
                    absolute_name = absolute_name.replace("_%s" % str(xi), "")
                total_enemies = len([xrole for xrole in enemy if xrole.hp > 0])
            if role.hp > 0:
                if i == 0 and role == local_config.active_actor:
                    fixed xysize (108, 108):
                        add "9i/interface/battle/actors/{}/chip.png".format(absolute_name.replace("_mirror", "")) pos (3, 3)
                        # 加入边框
                        if role in party:
                            add Transform("9i/interface/battle/system/pframe.png", size=(108, 108))
                        else:
                            add Transform("9i/interface/battle/system/eframe.png", size=(108, 108))
                        text _("回合") size 30 xalign 0.5 yoffset -15 font font_button outlines [(1, "#0009", 1, 1), (1, "#000d")]
                else:
                    fixed xysize (72, 72) yalign (1.0):
                        add "9i/interface/battle/actors/{}/chip.png".format(absolute_name.replace("_mirror", "")) size (66, 66) pos (3, 3)
                        if role in party:
                            add "9i/interface/battle/system/p2frame.png"
                        else:
                            add "9i/interface/battle/system/e2frame.png"
    hbox pos (0.85, 0.02) ysize 108:
        at gui_dissolve_top
        if local_config.tutorial_step == "生存战":
            text _("剩余回合数:[extend_party]") size 30 xalign 0.7 yoffset -15 font font_button outlines [(1, "#0009", 1, 1), (1, "#000d")]
        elif local_config.tutorial_step == "lhx_mana_error_winter_216":
            text _("妄想颠覆倒计时:[extend_party]") size 30 xalign 0.7 yoffset -15 font font_button outlines [(1, "#0009", 1, 1), (1, "#000d")]
        elif local_config.tutorial_step == "winter_loss_stage":
            text _("灵纹失效倒计时:[extend_party]") size 30 xalign 0.7 yoffset -15 font font_button outlines [(1, "#0009", 1, 1), (1, "#000d")]
        elif local_config.tutorial_step == "liuli_day219_onfire":
            text _("超燃过载倒计时:[extend_party]") size 30 xalign 0.7 yoffset -15 font font_button outlines [(1, "#0009", 1, 1), (1, "#000d")]
        else:
            text _("敌方剩余数量:[total_enemies]") size 30 xalign 0.7 yoffset -15 font font_button outlines [(1, "#0009", 1, 1), (1, "#000d")]

    if local_config.partyaction == "auto":
        text _("自动作战") align (0.0, 0.002) color "#f66" outlines [(1, "#0009", 1, 1), (1, "#000d")] font font_name
        key "toggle_afm" action [Play("battle_music", "Cancel_Button"), SetField(local_config, "partyaction", "manual")]
    else:
        key "toggle_afm" action [Play("battle_music", "Click_Button"), SetField(local_config, "partyaction", "auto")]

    if config.skipping:
        text _("快速战斗") align (0.1, 0.002) color "#77f" outlines [(1, "#0009", 1, 1), (1, "#000d")] font font_name

    key "game_menu" action [Play("battle_music", "Cancel_Button"), SetField(local_config, "partyaction", "manual")]
    key "hide_windows" action NullAction()


# 战斗菜单
screen tactics_screen(party, ally_environment_effects, order_members):
    on "show" action [SetField(local_config, "chosen_skill", None), SetField(local_config, "chosen_item", None), SetField(local_config, "chosen_actor", None), SetField(local_config, "current_message", ""), SetField(local_config, "current_ex_message", ""), SetField(local_config, "current_actor", local_config.active_actor)]
    if local_config.tutorial_step == "item_use" and len(local_config.player.items) == 0:
        on "hide" action [SetField(local_config, "current_message", ""), SetField(local_config, "current_ex_message", ""), Hide("message_screen"), SetField(local_config, "tutorial_step", "")]
    else:
        on "hide" action [SetField(local_config, "current_message", ""), SetField(local_config, "current_ex_message", ""), Hide("message_screen")]
    modal True

    $ local_config.current_mode = "Consumables"
    add "halfblack"

    label _("{#strategy}STRATEGY") style "caption_label" at caption_inter

    add Transform(local_config.current_actor.objectname, ycenter=0.5, xcenter=0.85)

    use status_frame(party[0], ally_environment_effects, position=(7, -157), mode="Stats", order_members=order_members)
    if len(party) > 1:
        use status_frame(party[1], ally_environment_effects, position=(442, -157), mode="Stats", order_members=order_members)
    if len(party) > 2:
        use status_frame(party[2], ally_environment_effects, position=(877, -157), mode="Stats", order_members=order_members)
    if len(party) > 3:
        use status_frame(party[3], ally_environment_effects, position=(7, -7), mode="Stats", order_members=order_members)
    if len(party) > 4:
        use status_frame(party[4], ally_environment_effects, position=(442, -7), mode="Stats", order_members=order_members)
    if len(party) > 5:
        use status_frame(party[5], ally_environment_effects, position=(877, -7), mode="Stats", order_members=order_members)

    frame xpos 65 ypos 150 xsize 240 style_group "nav_menu":
        at gui_dissolve_left
        has vbox

        python:
            local_total_tutorial_flags = []
            for tutorial_info in copy(local_config.total_tutorial_flags):
                if "easy" not in tutorial_info and "hard" not in tutorial_info and "abyss" not in tutorial_info:
                    local_total_tutorial_flags.append(tutorial_info)

        textbutton _("自动作战"):
            if not local_config.chosen_actor and not local_config.chosen_item and not local_config.chosen_skill and len(local_total_tutorial_flags) <= 1:
                action [SetField(local_config, "partyaction", "auto"), Return("auto_skill")] hovered [SetField(local_config, "current_message", _("开启自动作战")), SetField(local_config, "current_ex_message", "")]
        textbutton _("快速战斗"):
            if not local_config.chosen_actor and not local_config.chosen_item and not local_config.chosen_skill and len(local_total_tutorial_flags) <= 1:
                action [SetField(config, "skipping", "slow"), SetField(local_config, "partyaction", "auto"), Return("auto_skill")] hovered [SetField(local_config, "current_message", _("开启快速战斗")), SetField(local_config, "current_ex_message", "")]
        textbutton _("游戏选项"):
            if not local_config.chosen_actor and not local_config.chosen_item and not local_config.chosen_skill:
                action ShowMenu("preferences") hovered [SetField(local_config, "current_message", ""), SetField(local_config, "current_ex_message", "")]
        textbutton _("图鉴"):
            if not local_config.chosen_actor and not local_config.chosen_item and not local_config.chosen_skill:
                action Show("encyclopedia") hovered [SetField(local_config, "current_message", ""), SetField(local_config, "current_ex_message", "")]
        if persistent.battlespeed == 1.0:
            textbutton _("加速"):
                if not local_config.chosen_actor and not local_config.chosen_item and not local_config.chosen_skill:
                    action SetField(persistent, "battlespeed", 0.2)
        else:
            textbutton _("取消加速"):
                if not local_config.chosen_actor and not local_config.chosen_item and not local_config.chosen_skill:
                    action SetField(persistent, "battlespeed", 1.0)
        textbutton _("返回"):
            if (not local_config.chosen_actor and not local_config.chosen_item and not local_config.chosen_skill):
                activate_sound None
                action [Play("battle_music", "Cancel_Button"), Return("cancel")] hovered [SetField(local_config, "current_message", ""), SetField(local_config, "current_ex_message", "")]

    use item_frame("Consumables")
    use attribute_frame(local_config.current_actor)

    window align (0.35, 0.645) ysize 195:
        at gui_dissolve_bottom
        text local_config.current_message style "say_dialogue2" size 20 yoffset 8
        text local_config.current_ex_message outlines [(1, "#0009", 1, 1), (1, "#000d")] yoffset -15

    key "game_menu":
        if local_config.chosen_actor != None:
            action [Play("battle_music", "Cancel_Button"), SetField(local_config, "chosen_actor", None), Hide("message_screen")]
        elif local_config.chosen_skill != None:
            action [Play("battle_music", "Cancel_Button"), SetField(local_config, "chosen_skill", None), Hide("message_screen")]
        else:
            action [Play("battle_music", "Closing_Menu"), Return("cancel")]

    key "hide_windows" action NullAction()


screen command_screen(who, enemy):
    if enemy[0].hp > 0:
        button background None xysize (384, 750) anchor (0.5, 0.5) pos (enemy[0].xposition, 0.5):
            action [SetField(local_config, "partytarget", enemy[0])]

    if len(enemy) > 1:
        if enemy[1].hp > 0:
            button background None xysize (384, 750) anchor (0.5, 0.5) pos (enemy[1].xposition, 0.5):
                action [SetField(local_config, "partytarget", enemy[1])]

    if len(enemy) > 2:
        if enemy[2].hp > 0:
            button background None xysize (384, 750) anchor (0.5, 0.5) pos (enemy[2].xposition, 0.5):
                action [SetField(local_config, "partytarget", enemy[2])]

    add smallfloating("9i/interface/battle/system/pointer.png") anchor (0.5, 0.0) pos (local_config.partytarget.xposition, 0.12)

    python:
        skill_lists = who.skills if not who.is_phase2 else who.skills_v2

    frame background Frame("9i/interface/battle/system/frame3.png", 18, 18) xanchor 1.0 xpos config.screen_width - 7 yanchor 1.0 ypos config.screen_height - 7:
        at gui_dissolve_bottom
        has grid 2 3 transpose False style_group "skill"
        for n, i in enumerate(skill_lists):
            python:
                can_use = True

                if local_config.tutorial_step in ["general_skill", "guard_skill", "combat_skill", "item_use"]:
                    if local_config.tutorial_step == "general_skill":
                        if i.category != "General_attack":
                            can_use = False
                    elif local_config.tutorial_step == "guard_skill":
                        if i.category != "Recharge":
                            can_use = False
                    elif local_config.tutorial_step == "combat_skill":
                        if i.category not in ["Combat_skills", "Break_out"]:
                            can_use = False
                    elif local_config.tutorial_step == "item_use":
                        can_use = False
                else:
                    # 最终战场地
                    if local_config.tutorial_step == "winter_loss_stage" and (i.category != "Recharge" and i.name != "怨恨祛除"):
                        can_use = False
                    # mp不足
                    if "Spiritual" not in who.abilities and -i.mp_cost > who.mp:
                        can_use = False
                    # 技能被封印、被动技能
                    if not i.selectable or i.category == "Passive":
                        can_use = False
                    # 单体却未选择目标
                    if (i.damage_target == "single" and local_config.partytarget is None) or (i.damage_target == "single_ally" and local_config.chosen_actor is None):
                        can_use = False
                    # 技能特殊规则
                    if i.name == "接触感应" and "咒" in local_config.skill_log_data:
                        can_use = False
                    if i.name == "虚无":
                        if "积重鬼怨" in local_config.skill_log_data:
                            buff_roles = local_config.skill_log_data["积重鬼怨"]
                            if (who in local_config.party and "ally" in buff_roles) or (who in local_config.enemy and "enemy" in buff_roles):
                                can_use = False
                            elif "ghost_mask" in who.buff:
                                _, buff_number = who.buff["ghost_mask"]
                                if buff_number != 9:
                                    can_use = False
                            else:
                                can_use = False
                        elif "ghost_mask" in who.buff:
                            _, buff_number = who.buff["ghost_mask"]
                            if buff_number != 9:
                                can_use = False
                        else:
                            can_use = False
                    if i.name == "幻镜化物":
                        if "ethereal" in who.buff:
                            can_use = False
                    if i.name == "预见良缘":
                        has_death = False
                        if who in local_config.party:
                            for role in local_config.party:
                                if role.hp < 1:
                                    has_death = True
                                    break
                        elif who in local_config.enemy:
                            for role in local_config.enemy:
                                if role.hp < 1:
                                    has_death = True
                                    break
                        if not has_death:
                            can_use = False
            textbutton i.name selected_background Frame("9i/interface/battle/system/button_disabled.png", 18, 18) text_selected_color "#666":
                # 不显示的条件
                action If(can_use, [Return(i), SelectedIf(False)], false=[Play("battle_music", "Click_Disabled_Button"), SelectedIf(True)])
                hovered [SetField(local_config, "current_message", i.get_info(who)), SetField(local_config, "current_ex_message", i.get_ex_info(who))]
                if n == 0:
                    default True
        for i in xrange(6 - len(skill_lists)):
            textbutton ""

    key "game_menu" action [Play("battle_music", "Open_Menu"), Return("cancel")]
    key 'rollback' action Function(target_change, enemy=enemy, reverse=True)
    key 'rollforward' action Function(target_change, enemy=enemy, reverse=False)
    key "hide_windows" action NullAction()

    window align (0.98, 0.8) ysize 195:
        at gui_dissolve_right
        text local_config.current_message style "say_dialogue2" size 20 yoffset 8
        text local_config.current_ex_message outlines [(1, "#0009", 1, 1), (1, "#000d")] yoffset -15


screen aerowheel(who):
    modal True
    zorder +100

    key "game_menu" action NullAction()

    default skills = who.skills if not who.is_phase2 else who.skills_v2
    default ring_selection_tf = aero_selection_show(i=1, n=len(skills))

    on "show" action Play(channel="audio", file="9i/interface/battle/battle_music/aerowheel.ogg")

    add "9i/interface/battle/system/vignette.png" at imagescale(270), aero_inter
    frame style_prefix "aero" at aero_inter:
        has fixed
        add "9i/interface/battle/system/base.png" at imagescale(540), aero_base
        transform at aero_ring_rotate(-1, 30):
            add "9i/interface/battle/system/aero.png" at imagescale(1080)
        transform at aero_ring_rotate(1, 30):
            add "9i/interface/battle/system/inner ring.png" at imagescale(1080)
        transform at ring_selection_tf:
            add "9i/interface/battle/system/outer ring.png" at imagescale(1080)
            
        for i, skill in enumerate(skills, start=1):
            vbox at aero_button(i, len(skills)):
                $ name = skill.name
                textbutton "[name]":
                    action [Return(skill), Hide("aerowheel")]
                    hovered SetScreenVariable(
                        "ring_selection_tf",
                        aero_selection_replace(i, len(skills)))
                    text_style style.aero_button_text[skill]


screen aerowheel_ingame(skills):
    modal True
    zorder +100

    key "game_menu" action NullAction()

    default ring_selection_tf = aero_selection_show(i=1, n=len(skills))

    on "show" action Play(channel="audio", file="9i/interface/battle/battle_music/aerowheel.ogg")

    add "9i/interface/battle/system/vignette.png" at imagescale(270), aero_inter
    frame style_prefix "aero" at aero_inter:
        has fixed
        add "9i/interface/battle/system/base.png" at imagescale(540), aero_base
        transform at aero_ring_rotate(-1, 30):
            add "9i/interface/battle/system/aero.png" at imagescale(1080)
        transform at aero_ring_rotate(1, 30):
            add "9i/interface/battle/system/inner ring.png" at imagescale(1080)
        transform at ring_selection_tf:
            add "9i/interface/battle/system/outer ring.png" at imagescale(1080)
            
        for i, skill in enumerate(skills, start=1):
            vbox at aero_button(i, len(skills)):
                $ name = skill.name
                textbutton "[name]":
                    action [Return(skill), Hide("aerowheel")]
                    hovered SetScreenVariable(
                        "ring_selection_tf",
                        aero_selection_replace(i, len(skills)))
                    text_style style.aero_button_text[skill]
