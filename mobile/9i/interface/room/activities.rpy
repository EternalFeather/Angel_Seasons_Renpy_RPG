
init python:
    activity_buffer = {
        # 无人物事件
        "none": [
            ("不要闲着", "{size=-4}不要闲着{/size}\n\n\n培养一次角色\n奖励{color=#D35120}五百金钱{/color}"), 
            ("养精蓄锐", "{size=-4}养精蓄锐{/size}\n\n\n好好犒劳下自己{color=#D35120}\n体力恢复十点{/color}")
        ],
        # 单人物事件
        "single": [
            ("护肤美颜", "{size=-4}护肤美颜\n\n\n为{color=#D35120}%s{/color}\n准备一次皮肤保养\n开销{color=#D35120}四百金钱{/color}{/size}")
        ],
        # 多人物事件
        "multi": [
            ("维系关系", "{size=-4}维系关系\n\n\n{color=#D35120}%s{/color}和{color=#D35120}%s{/color}\n因为一些小事闹矛盾了\n尝试调解下气氛吧{/size}")
        ]
    }
    activity_maps = {
        "不要闲着": "training_active",
        "维系关系": "relation_active",
        "护肤美颜": "beauty_active",
        "养精蓄锐": "rest_active"
    }

    
    class Activities(object):
        def __init__(self, active_kind="不要闲着", active_state="未完成", active_description=""):
            self.kind = active_kind
            self.state = active_state
            self.dtype = activity_maps[active_kind]
            self.description = active_description
            self.tasks = [False]

        def check_done(self):
            if all(self.tasks):
                self.state = "领取"
