
screen training():
    on "show" action [SetField(local_config, "currentscreen", "training"), SetField(local_config, "training_role", None)]

    frame:
        background Solid("#0000FF00")
        xpos -845
        ypos -40

        add "9i/interface/room/images/才艺界面.png"
        
        # 事件图标
        grid 3 2:
            xalign 0.97925
            yalign 0.5428
            spacing 25

            for i in range(6):
                python:
                    has_role = False
                    if i < len(local_config.party):
                        role = local_config.party[i]
                        has_role = True

                imagebutton:
                    auto "9i/interface/room/images/button/BT_未获得_%s.png"
                    if has_role:
                        action NullAction()
                        # action [Hide("training"), Hide("roleroom"), SetField(local_config, "training_role", role), Call("train_detail")]
        
        # 角色图标
        grid 3 2:
            xalign 0.978
            yalign 0.545
            yspacing 42.5
            xspacing 56

            for i in range(6):
                python:
                    has_role = False
                    if i < len(local_config.party):
                        role = local_config.party[i]
                        has_role = True

                if has_role:
                    add "9i/interface/room/images/face/[role.objectname].png"
                else:
                    add "9i/interface/room/images/face/0.png"
            # at customzoom


# label train_detail:
#     if local_config.move_points < 5:
#         "{color=#f00}体力不足5。{/color}"
#     elif local_config.training_times >= 3:
#         "{color=#f00}本轮培养角色次数已达上限，做点别的吧。{/color}"
#     else:
#         call expression local_config.training_role.objectname + "_training"
        
#         python:
#             # 判断任务完成情况
#             for activity in local_config.activities:
#                 if activity.kind == "不要闲着" and local_config.training_times >= 1 and activity.state == "未完成":
#                     activity.tasks[-1] = True
#                     activity.check_done()
                    
#     $ renpy.retain_after_load()
#     call screen roleroom


# label xfe_role_training:
#     "希菲尔的训练内容测试"
#     $ xfe_role.xp += 100
#     play sound "se/属性增加.ogg"
#     "【希菲尔经验值】{color=#9DD1FF}↑100{/color}\n【体力】{color=#f00}↓5{/color}"
#     $ local_config.move_points -= 5
#     $ local_config.training_times += 1
#     return

