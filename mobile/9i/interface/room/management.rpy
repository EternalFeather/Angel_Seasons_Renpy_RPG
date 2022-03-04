
screen management():
    on "show" action SetField(local_config, "currentscreen", "management")

    frame:
        background Solid("#0000FF00")
        xpos -846
        ypos -40

        add "9i/interface/room/images/管理界面.png"

        # 培训栏位
        grid 3 1:
            xalign 0.7165
            yalign 0.2905
            spacing 4
            if local_config.room_level == 1:
                add "9i/interface/room/images/face/0.png"
                add "9i/interface/room/images/face/0.png"
                add "9i/interface/room/images/face/0.png"
                at customzoom2
            else:
                if local_config.manage_roles[0] is None:
                    add "9i/interface/room/images/face/空闲.png" 
                else:
                    add "9i/interface/room/images/face/" + local_config.manage_roles[0].objectname + ".png"
                if local_config.manage_roles[1] is None:
                    add "9i/interface/room/images/face/空闲.png"
                else:
                    add "9i/interface/room/images/face/" + local_config.manage_roles[1].objectname + ".png"
                if local_config.manage_roles[2] is None:
                    add "9i/interface/room/images/face/空闲.png"
                else:
                    add "9i/interface/room/images/face/" + local_config.manage_roles[2].objectname + ".png"
                at customzoom2

        add "9i/interface/room/images/培训遮盖层.png" xalign 0.729 yalign 0.3712

        text "{color=#663300}{size=+6}[local_config.player.currency]{/color}{/size}" xalign 0.78 yalign 0.172
        vbox:
            xalign 1.0
            yalign 0.375
            imagebutton:
                auto "9i/interface/room/images/button/BT_提升宣传_%s.png"
                action [Hide("management"), Hide("roleroom"), Call("publicity")]
            imagebutton:
                auto "9i/interface/room/images/button/BT_全面检查_%s.png"
                action [Hide("management"), Call("room_levelup")]
 
        # 培训按钮
        grid 3 1:
            xalign 0.71
            yalign 0.375
            spacing 25
            imagebutton:
                auto "9i/interface/room/images/button/BT_培训按钮_%s.png"
                action [Hide("management"), Call("train1")]
            imagebutton:
                auto "9i/interface/room/images/button/BT_培训按钮_%s.png"
                action [Hide("management"), Call("train2")]
            imagebutton:
                auto "9i/interface/room/images/button/BT_培训按钮_%s.png"
                action [Hide("management"), Call("train3")]
        
        # 培训遮罩
        if local_config.room_level < 2:
            add "9i/interface/room/images/2级解锁.png" xalign 0.534 yalign 0.375
        if local_config.room_level < 3:
            add "9i/interface/room/images/3级解锁.png" xalign 0.658 yalign 0.375
        if local_config.room_level < 4:
            add "9i/interface/room/images/4级解锁.png" xalign 0.782 yalign 0.375

        # 培训介绍
        if local_config.room_level >= 2:
            text "{color=#ff0000}{size=+6}适应性{/size}{/color}" xcenter 0.528 yalign 0.465 style "mioutline"
        if local_config.room_level >= 3:
            text "{color=#ff0000}{size=+6}领导力{/size}{/color}" xcenter 0.6385 yalign 0.465 style "mioutline"
        if local_config.room_level >= 4:
            text "{color=#ff0000}{size=+6}压制力{/size}{/color}" xcenter 0.75 yalign 0.465 style "mioutline"
        add "9i/interface/room/images/[local_config.room_level]级.png" xalign 0.97 yalign 0.84


# 提升名气
label publicity:
    # 每一轮只能提升一次
    if local_config.publish_times < 1:
        play sound "9i/interface/room/se/魔法.ogg"

        python:
            renpy.retain_after_load()
            section = renpy.call_screen("selectpublicity")
            if section != 0:
                local_config.publish_times += 1

        # 循序渐进
        if section == 1:
            python:
                local_config.player.famous += 2
                local_config.player.currency -= 60
                if local_config.player.currency < 0:
                    less_money = -local_config.player.currency
                    renpy.say("提示", "已赊账{color=#ff0000}[less_money]金钱{/color}。")
                    local_config.debt += less_meney
                    local_config.player.currency = 0
            play sound "9i/interface/room/se/属性增加.ogg"
            "组织的名气正在逐步提升。\n{color=#9DD1FF}【名气】↑2{/coler}"
        # 修缮设施
        elif section == 2:
            python:
                local_config.player.hideness += 3
                local_config.player.currency -= 200
                if local_config.player.currency < 0:
                    less_money = -local_config.player.currency
                    renpy.say("提示", "已赊账{color=#ff0000}[less_money]金钱{/color}。")
                    local_config.debt += less_meney
                    local_config.player.currency = 0
            play sound "9i/interface/room/se/属性增加.ogg"
            "对基础设施进行了全面翻新，感觉更自信了。\n{color=#9DD1FF}【隐蔽】↑3{/coler}"
        # 雇佣托儿
        elif section == 3:
            python:
                local_config.player.famous += 4
                local_config.player.hideness -= 1
                local_config.player.currency -= 150
                if local_config.player.currency < 0:
                    less_money = -local_config.player.currency
                    renpy.say("提示", "已赊账{color=#ff0000}[less_money]金钱{/color}。")
                    local_config.debt += less_meney
                    local_config.player.currency = 0
            play sound "9i/interface/room/se/属性增加.ogg"
            "托儿们口无遮拦地大肆吹捧，虽然提升了名气但总觉得有点太招摇了。\n{color=#9DD1FF}【名气】↑4{/color}{color=#f00}【隐蔽】↓1{/color}"
    else:
        "已经宣传过一次了，下次再来吧~"

    $ renpy.retain_after_load()
    call screen roleroom


# 提升名气界面
screen selectpublicity():
    add "9i/interface/room/images/bg/卧室.jpg"
    add "selectpublicity"

    hbox:
        xalign 0.5
        yalign 0.64
        spacing 20
        imagebutton:
            auto "9i/interface/room/images/button/BT_循序渐进_%s.png"
            action [Hide("selectpublicity"), Return(1)]
        imagebutton:
            auto "9i/interface/room/images/button/BT_修缮设施_%s.png"
            action [Hide("selectpublicity"), Return(2)]
        imagebutton:
            auto "9i/interface/room/images/button/BT_雇佣托儿_%s.png"
            action [Hide("selectpublicity"), Return(3)]
    imagebutton:
        xalign 0.93
        yalign 0.25
        auto "9i/interface/room/images/button/BT_右键_%s.png"
        action [Hide("selectpublicity"), Return(0)]
    key "K_ESCAPE" action [Hide("selectpublicity"), Return(0)]


# 全面检查
label room_levelup:
    if local_config.room_level == 1:
        if local_config.player.famous >= 80:
            "是否花费{color=#ff0000}5000金钱{/color}将房间升至{color=#9DD1FF}二级{/color}？"
            menu:
                extend ""
                "【升级】" if local_config.player.currency >= 5000:
                    python:
                        local_config.player.currency -= 5000
                        local_config.room_level = 2
                    play sound "9i/interface/room/se/房间升级.ogg"
                    "成功花费5000金钱升级房间！\n{color=#D81C8E}房间等级提升至2级{/color}"
                "【金钱不足】" if local_config.player.currency < 5000:
                    $ renpy.retain_after_load()
                    call screen roleroom
                "【返回】" if local_config.player.currency >= 5000:
                    $ renpy.retain_after_load()
                    call screen roleroom
        else:
            play sound "9i/interface/room/se/升级失败.ogg"
            "{color=#ff0000}名气{/color}未达到80。"
    elif local_config.room_level == 2:
        if local_config.player.famous >= 240:
            "是否花费{color=#ff0000}20000金钱{/color}将房间升至{color=#9DD1FF}三级{/color}？"
            menu:
                extend ""
                "【升级】" if local_config.player.currency >= 20000:
                    python:
                        local_config.player.currency -= 20000
                        local_config.room_level = 3
                    play sound "9i/interface/room/se/房间升级.ogg"
                    "成功花费20000金钱升级房间！\n{color=#D81C8E}房间等级提升至3级{/color}"
                "【金钱不足】" if local_config.player.currency < 20000:
                    $ renpy.retain_after_load()
                    call screen roleroom
                "【返回】":
                    $ renpy.retain_after_load()
                    call screen roleroom
        else:
            play sound "9i/interface/room/se/升级失败.ogg"
            "{color=#ff0000}名气{/color}未达到240。"
    elif local_config.room_level == 3:
        if local_config.player.famous >= 500:
            "是否花费{color=#ff0000}55000金钱{/color}将房间升至{color=#9DD1FF}四级{/color}？"
            menu:
                extend ""
                "【升级】" if local_config.player.currency >= 55000:
                    python:
                        local_config.player.currency -= 55000
                        local_config.room_level = 4
                    play sound "9i/interface/room/se/房间升级.ogg"
                    "成功花费55000金钱升级！\n{color=#D81C8E}房间等级提升至4级{/color}"
                "【金钱不足】" if local_config.player.currency < 55000:
                    $ renpy.retain_after_load()
                    call screen roleroom
                "【返回】":
                    $ renpy.retain_after_load()
                    call screen roleroom
        else:
            play sound "9i/interface/room/se/升级失败.ogg"
            "{color=#ff0000}名气{/color}未达到500。"

    $ renpy.retain_after_load()
    call screen roleroom


# 才艺培训(影响生命、防御、效果抵抗)
label train1:
    if local_config.room_level >= 2:
        if local_config.manage_roles[0] is not None:
            python:
                role = local_config.manage_roles[0]
            "{color=#9DD1FF}[role.name] vit：1 res：1{/color}\n每次增益情况：{color=#9DD1FF}【vit】↑2 【res】↑1{/color}\n每次费用：{color=#9DD1FF}3000金币{/color}和{color=#9DD1FF}1点隐蔽{/color}"
        else:
            "每次增益情况：{color=#9DD1FF}【vit】↑2 【res】↑1{/color}\n每次费用：{color=#9DD1FF}3000金币{/color}和{color=#9DD1FF}1点隐蔽{/color}"
        menu:
            extend ""
            "【选择角色】" if local_config.player.currency > 0:
                $ selected = False
                $ selected_type = 999
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
                        renpy.play("9i/interface/room/se/训练加入.ogg", channel='sound')
                        target = local_config.party[selected_type]
                        local_config.manage_roles[0] = target
                        renpy.say("提示", "成功为[target.name]报名适应性培训。")
                        local_config.debt += 3000

                    selected = True
                    
        $ renpy.retain_after_load()
        call screen roleroom
    else:
        "升级房间至{color=#ff0000}2级{/color}即可解锁适应性培训。"

    $ renpy.retain_after_load()
    call screen roleroom


# 魅力培训(影响速度、效果命中、元素精通)
label train2:
    if local_config.room_level >= 3:
        if local_config.manage_roles[1] is not None:
            python:
                role = local_config.manage_roles[1]
            "{color=#9DD1FF}[role.name] mnt：1{/color}\n每次增益情况：{color=#9DD1FF}【mnt】↑1{/color}\n每次费用：{color=#9DD1FF}5000金币{/color}和{color=#9DD1FF}2点隐蔽{/color}"
        else:
            "每次增益情况：{color=#9DD1FF}【mnt】↑1{/color}\n每次费用：{color=#9DD1FF}5000金币{/color}和{color=#9DD1FF}2点隐蔽{/color}"
        menu:
            extend ""
            "【选择角色】" if local_config.player.currency > 0:
                $ selected = False
                $ selected_type = 999
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
                        renpy.play("9i/interface/room/se/训练加入.ogg", channel='sound')
                        target = local_config.party[selected_type]
                        local_config.manage_roles[1] = target
                        renpy.say("提示", "成功为[target.name]报名领导力培训。")
                        local_config.debt += 5000

                    selected = True
                    
        $ renpy.retain_after_load()
        call screen roleroom
    else:
        "升级房间至{color=#ff0000}3级{/color}即可解锁领导力培训。"

    $ renpy.retain_after_load()
    call screen roleroom


# 武功培训(影响攻击力、暴击率、暴击伤害)
label train3:
    if local_config.room_level >= 4:
        if local_config.manage_roles[2] is not None:
            python:
                role = local_config.manage_roles[2]
            "{color=#9DD1FF}[role.name] agi：1 dex：1{/color}\n每次增益情况：{color=#9DD1FF}【agi】↑2 【dex】↑2{/color}\n每次费用：{color=#9DD1FF}3000金币{/color}和{color=#9DD1FF}1点隐蔽{/color}"
        else:
            "每次增益情况：{color=#9DD1FF}【agi】↑2 【dex】↑2{/color}\n每次费用：{color=#9DD1FF}3000金币{/color}和{color=#9DD1FF}1点隐蔽{/color}"
        menu:
            extend ""
            "【选择角色】" if local_config.player.currency > 0:
                $ selected = False
                $ selected_type = 999
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
                        renpy.play("9i/interface/room/se/训练加入.ogg", channel='sound')
                        target = local_config.party[selected_type]
                        local_config.manage_roles[0] = target
                        renpy.say("提示", "成功为[target.name]报名压制力培训。")
                        local_config.debt += 3000

                    selected = True
                    
        $ renpy.retain_after_load()
        call screen roleroom
    else:
        "升级房间至{color=#ff0000}4级{/color}即可解锁压制力培训。"

    $ renpy.retain_after_load()
    call screen roleroom


