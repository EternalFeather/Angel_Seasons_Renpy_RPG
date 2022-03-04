
label goout:
    if local_config.move_points < 10:
        "{color=#f00}体力不足10点{/color}，还是早点休息吧。"
        $ renpy.retain_after_load()
        call screen roleroom
    else:
        $ selected = False
        $ selected_type = 999

        scene black
        with dissolve

        while not selected:
            python:
                selection_candidates = []
                party_roles = [role for role in local_config.party if role.has_story]

                if (selected_type == 999 and len(party_roles) > 4) or (selected_type == 405):
                    for i, role in enumerate(party_roles[:4]):
                        selection_candidates.append((role.name, i))
                    selection_candidates.append(("【下一页】", 404))
                elif selected_type == 404:
                    for i, role in enumerate(party_roles[4:]):
                        selection_candidates.append((role.name, i + 4))
                    selection_candidates.append(("【上一页】", 405))
                else:
                    for i, role in enumerate(party_roles):
                        selection_candidates.append((role.name, i))

                selection_candidates.append(("【返回】", 101))
                renpy.say("提示", "好不容易空出了时间，要和谁一起出去呢？\n{color=#ff0000}【外出将会消耗10点体力】{/color}")
                selected_type = renpy.display_menu(selection_candidates)

            if selected_type not in [999, 404, 405]:
                if selected_type != 101:
                    $ target = party_roles[selected_type]
                    call expression target.objectname + "_story" from _call_expression_4

                $ selected = True

        $ renpy.retain_after_load()
        call screen roleroom


label xfe_role_story:
    "带希菲尔外出..."
    return
