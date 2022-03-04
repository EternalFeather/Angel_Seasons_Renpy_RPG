
label tasks:
    call screen tasks
    $ renpy.retain_after_load()
    call screen roleroom


screen tasks():
    add "9i/interface/room/images/bg/mainmenu.png"

    imagebutton:
        xalign 0.88
        yalign 0.162
        auto "9i/interface/room/images/button/BT_右键_%s.png"
        action Hide("tasks"), Return()

    key "K_ESCAPE" action Hide("tasks"), Return()

    python:
        show_jobs = []
        for job in local_config.jobs:
            if job.state == "待接受":
                show_jobs.append(job)
            if len(show_jobs) >= 3:
                break

    vbox:
        xcenter 0.5
        ycenter 0.5

        if len(show_jobs) > 0:
            for job in show_jobs:
                imagebutton:
                    auto "9i/interface/room/images/button/BT_weituo_%s.png"
                    action Call("enter_task", task_job=job)

        for _ in xrange(3 - len(show_jobs)):
            imagebutton:
                idle "9i/interface/room/images/button/BT_weituo_grey.png"
                action NullAction()

    if len(show_jobs) > 0:
        for i, job in enumerate(show_jobs):
            if i == 0:
                text job.description xpos 460 ycenter 0.24 style "blackoutline"
            elif i == 1:
                text job.description xpos 460 ycenter 0.495 style "blackoutline"
            else:
                text job.description xpos 460 ycenter 0.75 style "blackoutline"

    for j in xrange(3 - len(show_jobs)):
        if j + len(show_jobs) == 0:
            text "{color=#ffffff}{size=+8}暂无委托在榜{/color}" xcenter 0.49 ycenter 0.24 style "blackoutline"
        elif j + len(show_jobs) == 1:
            text "{color=#ffffff}{size=+8}暂无委托在榜{/size}{/color}" xcenter 0.49 ycenter 0.495 style "blackoutline"
        else:
            text "{color=#ffffff}{size=+8}暂无委托在榜{/size}{/color}" xcenter 0.49 ycenter 0.75 style "blackoutline"


label enter_task(task_job):
    call expression task_job.dtype + "_job" from _call_expression_1
    $ task_job.state = "完成"
    return


label tea_help_job:
    "茶馆任务！"
    return


label coffee_help_job:
    "咖啡屋任务！"
    return


label bar_help_job:
    "酒吧任务！"
    return
