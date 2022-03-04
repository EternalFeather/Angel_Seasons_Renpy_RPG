
init python:
    class OrderBar(object):
        """
        行动条
        """
        def __init__(self, name, max_length, roles):
            self.name = name
            self.max_length = max_length
            self.roles = roles
            self.bar = []

        def update_members(self, go_role, come_role):
            ## 替换行动条中的角色
            # 剔除行动条中离场的角色
            self.roles.remove(go_role)
            self.bar = []
            # 新增入场的角色
            self.roles.append(come_role)
            # 刷新当前行动条
            self.create()
        
        @staticmethod
        def sort_bar(bar):
            bar.sort(key=attrgetter("order"), reverse=True)

        def create(self):
            self.bar = []
            ## 生成预显示的角色行动顺序
            mirror_roles = [copy(role) for role in self.roles if role.hp > 0]
            while len(self.bar) < self.max_length:
                OrderBar.sort_bar(mirror_roles)
                while mirror_roles[0].order < 1000:
                    for member in mirror_roles:
                        member.order += (max(member.battle_speed, 1) + renpy.random.random())
                    OrderBar.sort_bar(mirror_roles)
                self.bar.append(mirror_roles[0].objectname)
                mirror_roles[0].order -= 1000

        def update(self):
            ## 当有拉条、推条等行为发生时，更新行动条顺序
            # 首位不变，其余位置通过拉条计算
            self.bar = self.bar[:1]
            mirror_roles = [copy(role) for role in self.roles if role.hp > 0]
            OrderBar.sort_bar(mirror_roles)
            mirror_roles[0].order -= 1000
            while len(self.bar) < self.max_length:
                OrderBar.sort_bar(mirror_roles)
                while mirror_roles[0].order < 1000:
                    for member in mirror_roles:
                        member.order += (max(member.battle_speed, 1) + renpy.random.random())
                    OrderBar.sort_bar(mirror_roles)
                self.bar.append(mirror_roles[0].objectname)
                mirror_roles[0].order -= 1000

        def move(self):
            # 行动条推进
            # raise NameError({rol.objectname: rol.order for rol in self.roles})
            for member in self.roles:
                if local_config.tutorial_step == "liuli_day219_onfire" and member.objectname == "liuli_role_mirror":
                    member.order += 0
                else:
                    member.order += (max(member.battle_speed, 1) + renpy.random.random())
            self.create()

        def get_real_role(self):
            ## 获取当前行动条顶端的真实角色
            return getattr(store, self.bar[0])