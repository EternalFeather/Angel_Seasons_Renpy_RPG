
init python:
    job_buffer = [
        ("茶馆", "{size=+10}{color=#ffffff}【茶馆】 {color=#ff0000}5体力{/color}\n城郊有一位种茶的老翁，时常会被周边的泼皮欺负...\n派{color=#FF6347}两名{/color}手下教育一下泼皮们！{/size}{/color}\n{size=+7}{color=#FF6347}【奖励】%s{/color}{/size}"),
        ("咖啡店", "{size=+10}{color=#ffffff}【咖啡店】 {color=#ff0000}5体力{/color}\n城郊有一位咖啡老板，时常会被周边的泼皮欺负...\n派{color=#FF6347}两名{/color}手下教育一下泼皮们！{/size}{/color}\n{size=+7}{color=#FF6347}【奖励】%s{/color}{/size}"),
        ("酒吧", "{size=+10}{color=#ffffff}【酒吧】 {color=#ff0000}5体力{/color}\n城郊有一位酒吧的酒保，时常会被周边的泼皮欺负...\n派{color=#FF6347}两名{/color}手下教育一下泼皮们！{/size}{/color}\n{size=+7}{color=#FF6347}【奖励】%s{/color}{/size}"),
    ]
    job_maps = {
        "茶馆": "tea_help",
        "咖啡店": "coffee_help",
        "酒吧": "bar_help"
    }

    
    class Jobs(object):
        def __init__(self, job_kind, job_state, rewards, description):
            self.kind = job_kind
            self.state = job_state
            self.dtype = job_maps[job_kind]
            self.description = description
            self.rewards = rewards
