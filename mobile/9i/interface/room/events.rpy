
screen events():
    on "show" action [SetField(local_config, "currentscreen", "events"), SetField(local_config, "event_select", None)]

    frame:
        background Solid("#0000FF00")
        xpos -845
        ypos -40
        
        # 背景图选择
        if local_config.JClevel == '纸醉金迷':
            add "9i/interface/room/images/纸醉金迷.png"
        elif local_config.JClevel == '芝兰之室':
            add "9i/interface/room/images/芝兰之室.png"
        elif local_config.JClevel == '江湖气息':
            add "9i/interface/room/images/江湖气息.png"
        else:
            add "9i/interface/room/images/人迹寥寥.png"
        
        # 任务栏
        grid 3 1:
            xalign 0.903
            yalign 0.86
            spacing 32
            imagebutton:
                auto "9i/interface/room/images/button/BT_任务页面_%s.png"
                action [Hide("events"), Hide("roleroom"), SetField(local_config, "event_select", 0), Call("JC_detail")]
            imagebutton:
                auto "9i/interface/room/images/button/BT_任务页面_%s.png"
                action [Hide("events"), Hide("roleroom"), SetField(local_config, "event_select", 1), Call("JC_detail")]
            imagebutton:
                auto "9i/interface/room/images/button/BT_任务页面_%s.png"
                action [Hide("events"), Hide("roleroom"), SetField(local_config, "event_select", 2), Call("JC_detail")]

        # 显示活动内容
        for i, activity in enumerate(local_config.activities):
            python:
                if i == 0:
                    xxpos = 1065
                    xxalign = 0.66
                elif i == 1:
                    xxpos = 1335
                    xxalign = 0.8
                else:
                    xxpos = 1605
                    xxalign = 0.955
                yypos = 680
                yyalign = 0.9

            text activity.description vertical True xpos xxpos ypos yypos style "mrrw_text"

            if activity.state == "完成":
                add "9i/interface/room/images/完成任务.png" xalign xxalign yalign yyalign
            elif activity.state == "领取":
                add "9i/interface/room/images/领取奖励.png" xalign xxalign yalign yyalign


# 任务接取、领取奖励操作
label JC_detail:
    python:
        index = local_config.event_select
        active = copy(local_config.activities[index])
        # 接任务
        if active.state == "未完成" and active.kind != "不要闲着":
            renpy.say("提示", "是否接受该活动？")
            res = renpy.display_menu([("【确认】", 1), ("【再想想】", 0)])
            if res == 1:
                active.state = "接受"
                renpy.say("提升", "成功接受该任务！")
        # 待完成
        elif active.state == "接受":
            renpy.say("提示", "已经接过该任务了，快去完成领取奖励吧~")
        # 领取奖励
        elif active.state == "领取":
            active.state = "完成"
            renpy.call(active.dtype + "_reward")

    # *-* renpy.call自带bug,无法回溯到当前的python下语句中
    python:
        local_config.activities[index] = active

    $ renpy.retain_after_load()
    call screen roleroom


label training_active_reward:
    "不要闲着活动任务奖励。"
    # play sound "se/金钱.ogg"
    # "任务完成！\n{color=#9DFF9D}金钱↑500{/color}"
    return


label rest_active_reward:
    "养精蓄锐活动任务奖励。"
    # play sound "se/金钱.ogg"
    # "任务完成！\n{color=#9DFF9D}金钱↑500{/color}"
    return


label relation_active_reward:
    "维系关系活动任务奖励。"
    # play sound "se/金钱.ogg"
    # "任务完成！\n{color=#9DFF9D}金钱↑500{/color}"
    return


label beauty_active_reward:
    "护肤美颜活动任务奖励。"
    # play sound "se/金钱.ogg"
    # "任务完成！\n{color=#9DFF9D}金钱↑500{/color}"
    return
