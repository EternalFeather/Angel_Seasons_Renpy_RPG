
screen roleroom():
    zorder -1
    on "show" action Show(local_config.currentscreen)

    add "9i/interface/room/images/bg/mainmenu.png"

    python:
        has_activities = False
        if len(local_config.activities) > 0:
            for activity in local_config.activities:
                if activity.state == "领取":
                    has_activities = True
                    break

    # 右上角菜单栏
    hbox:
        xalign 1.0
        yalign 0.0
        imagebutton:
            auto "9i/interface/room/images/button/BT_date_%s.png"
            action Show("preferences")
    hbox:
        xalign 0.92
        yalign 0.033
        text "第[local_config.innumber]次造访" style "blackoutline" size 30

    # 管理、才艺、活动、手下4个功能标签
    grid 1 4:
        xalign 0.6325
        yalign 0.39
        spacing 15
        imagebutton:
            auto "9i/interface/room/images/button/BT_管理_%s.png"
            # action [Show("management"), Hide("training"), Hide("events"), Hide("info")]
            action Function(renpy.show_screen, _screen_name="paopao", paopao_info="此功能将在春之章开启")
        imagebutton:
            auto "9i/interface/room/images/button/BT_才艺_%s.png"
            # action [Hide('management'), Show("training"), Hide("events"), Hide("info")]
            action Function(renpy.show_screen, _screen_name="paopao", paopao_info="此功能将在春之章开启")
        imagebutton:
            auto "9i/interface/room/images/button/BT_活动_%s.png"
            # action [Hide('management'), Hide("training"), Show("events"), Hide("info")]
            action Function(renpy.show_screen, _screen_name="paopao", paopao_info="此功能将在春之章开启")
        imagebutton:
            auto "9i/interface/room/images/button/BT_信息_%s.png"
            action [Hide('management'), Hide("training"), Hide("events"), Call("info")]
    # 有活动可领取的时候提示红点
    if has_activities:
        add "9i/interface/room/images/reddot.png" xalign 0.654 yalign 0.465

    # 结束按钮
    imagebutton:
        xalign 1.0
        yalign 0.87
        auto "9i/interface/room/images/button/BT_结束_%s.png"
        action [Hide('management'), Hide("training"), Hide("events"), Hide("info"), Hide("roleroom"), Function(local_config.end_init, player=local_config.player, party=local_config.party), Jump(local_config.next_story)]
    hbox:
        xalign 0.98
        yalign 0.77
        text "{color=#cc3300}{size=+16}剩余体力：[local_config.move_points]{/size}{/color}" style "tilistyle"

    # 外出按钮（触发支线事件）
    imagebutton:
        xalign 0.745
        yalign 0.25
        auto "9i/interface/room/images/button/BT_外出_%s.png"
        # action [Hide('management'), Hide("training"), Hide("events"), Hide("info"), Hide("roleroom"), Call("goout")]
        action Function(renpy.show_screen, _screen_name="paopao", paopao_info="此功能将在春之章开启")
    
    # 委托按钮（提升属性）
    imagebutton:
        xalign 0.805
        yalign 0.5
        auto "9i/interface/room/images/button/BT_委托_%s.png"
        # action [Hide('management'), Hide("training"), Hide("events"), Hide("info"), Hide("roleroom"), Call("tasks")]
        action Function(renpy.show_screen, _screen_name="paopao", paopao_info="此功能将在春之章开启")
    # 有委托事件的时候提示红点
    if len(local_config.jobs) > 0:
        add "9i/interface/room/images/reddot.png" xalign 0.812 yalign 0.46

    # 装备按钮
    imagebutton:
        xalign 0.745
        yalign 0.75
        auto "9i/interface/room/images/button/BT_装备_%s.png"
        action [Hide('management'), Hide("training"), Hide("events"), Hide("info"), Hide("roleroom"), Call("equip_outfit")]
    
    # 值班人员委派按钮
    imagebutton:
        xalign 1.0
        yalign 0.16
        auto "9i/interface/room/images/button/BT_值班人_%s.png"
        # action [Hide('management'), Hide("training"), Hide("events"), Hide("info"), Hide("roleroom"), Call("zhiban")]
        action Function(renpy.show_screen, _screen_name="paopao", paopao_info="此功能将在春之章开启")
    if local_config.zhiban_role is None:
        add "9i/interface/room/images/值班提示.png" xalign 0.998 yalign 0.28
    else:
        add "9i/interface/room/images/face/[local_config.zhiban_role.objectname].png" xalign 0.976 yalign 0.28 zoom 0.47
    
    # 底部属性显示界面
    hbox:
        xalign 0.12
        yalign 0.962
        imagebutton:
            idle "9i/interface/room/images/bar_jinqian.png"
            action NullAction()
        imagebutton:
            idle "9i/interface/room/images/bar_zhaiwu.png"
            action NullAction()
        imagebutton:
            idle "9i/interface/room/images/bar_koubei.png"
            action NullAction()
        imagebutton:
            idle "9i/interface/room/images/bar_mingqi.png"
            action NullAction()
        imagebutton:
            idle "9i/interface/room/images/bar_yinbi.png"
            action NullAction()
    
    text "{size=+5}[local_config.player.currency]{/size}" style "zhibanstyle" xpos 230 yalign 0.956
    if local_config.player.currency - local_config.debt < 0:
        text "{size=+5}{color=#E46248}[local_config.debt]{/color}{/size}" style "zhibanstyle" xpos 500 yalign 0.956
    else:
        text "{size=+5}{color=#CD87D0}[local_config.debt]{/color}{/size}" style "zhibanstyle" xpos 500 yalign 0.956
    text "{size=+5}[local_config.player.character]{/size}" style "zhibanstyle" xpos 700 yalign 0.955
    text "{size=+5}[local_config.player.famous]{/size}" style "zhibanstyle" xpos 890 yalign 0.955
    if local_config.player.hideness > 0:
        text "{size=+5}{color=#CD87D0}[local_config.player.hideness]{/color}{/size}" style "zhibanstyle" xpos 1090 yalign 0.955
    else:
        text "{size=+5}{color=#E46248}[local_config.player.hideness]{/color}{/size}" style "zhibanstyle" xpos 1090 yalign 0.955
    
    key "game_menu" action NullAction()
