
label zhiban:
    if local_config.present_send:
        "已经慰问过值班人了，{color=#ff0000}本轮{/color}不可再次触发。"
    else:
        "是否决定设置值班人员？（提示：值班能够培养角色好感度，视值班人员的好感度多少有概率触发角色隐藏剧情哟~）"
        menu:
            extend ""
            "【选择角色】":
                $ selected = False
                $ selected_type = 999
            "【慰问】" if local_config.zhiban_role is not None:
                python:
                    i = -1
                    styn = None
                    for value, story_name in local_config.zhiban_role.hiden_story:
                        if local_config.zhiban_role.love >= value:
                            i += 1
                            styn = story_name
                if i == -1:
                    call expression local_config.zhiban_role.objectname + "_zhiban_love_normal" from _call_expression_2
                else:
                    call expression styn + "_level" + str(i) from _call_expression_3
            "【返回】":
                $ renpy.retain_after_load()
                call screen roleroom

        while not selected:
            python:
                selection_candidates = []
                # 如果成员大于四人，显示前四位和【下一页】
                if (selected_type == 999 and len(local_config.party) > 4) or (selected_type == 405):
                    for i, role in enumerate(local_config.party[:4]):
                        selection_candidates.append((role.name, i))
                    selection_candidates.append(("【下一页】", 404))
                # 如果判断为点击下一页，显示后两位和【上一页】
                elif selected_type == 404:
                    for i, role in enumerate(local_config.party[4:]):
                        selection_candidates.append((role.name, i + 4))
                    selection_candidates.append(("【上一页】", 405))
                # 队伍不足4人不显示【下一页】
                else:
                    for i, role in enumerate(local_config.party):
                        selection_candidates.append((role.name, i))

                # 统一按钮【返回】
                selection_candidates.append(("【返回】", 101))

                selected_type = renpy.display_menu(selection_candidates)
                
                # 0~5角色选择；999未选择；101返回；404下一页；405上一页
                if selected_type not in [999, 404, 405]:
                    # 角色选择
                    if selected_type != 101:
                        renpy.play("9i/interface/room/se/值班人设置.ogg", channel='sound')
                        target = local_config.party[selected_type]
                        local_config.zhiban_role = target
                        renpy.say("提示", "成功任命[target.name]为值班人员。")

                    selected = True

    $ renpy.retain_after_load()
    call screen roleroom


label xfe_role_zhiban_love_normal:
    "无好感度事件触发"
    return


label xfe_role_zhiban_love_level0:
    "触发好感度level1事件"
    return

