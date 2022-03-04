
init 1 python:
    import pickle

    class Localturn_params(object):
        def __init__(self):
            self.debug_flag = False

            # ------ Battle功能专区 ------
            self.player = syl_role
            self.player_join_rate = 0.05    # 主角协战概率
            self.current_mode = None
            self.chosen_actor = None
            self.chosen_skill = None
            self.chosen_item = None
            self.active_actor = None
            self.current_actor = None
            self.spi_mp_cost = 0           # 透支的MP数
            self.partyaction = "manual"
            self.partytarget = None
            self.shown_actor = None
            self.master_skill = None
            self.multi_buff_lock = False
            self.in_battle = False
            self.current_message = ""
            self.current_ex_message = ""
            self.skill_log_data = {}       # 技能记录中间数值
            self.player.currency = 5000
            self.buff_source = {}
            self.enemy = []
            self.party = []
            self.masters = []
            self.backup = []
            self.release = []
            self.role_pool = set()
            self.shop_list = []
            self.battle_config = {}
            # 战斗祝福
            self.battle_blessing = {}
            # 教学步骤
            self.tutorial_step = ""
            # 教学要素
            self.total_tutorial_flags = ["support"]

            # ------- Room功能专区 -------
            # 局部参数
            self.activities = []
            self.jobs = []
            self.move_points = 50
            self.zhiban_role = None
            self.currentscreen = "management"
            self.publish_times = 0
            self.training_times = 0
            self.training_role = None
            self.event_select = None
            self.info_role = None
            self.present_send = False
            
            # 全局参数
            self.debt = 0
            self.innumber = 1
            self.room_level = 1
            self.manage_roles = [None, None, None]
            self.move_points = 50
            self.JClevel = ""
            self.next_story = ""

            # 备份原始参数
            self.base_activities = []
            self.base_jobs = []
            self.base_move_points = 50
            self.base_currentscreen = "management"
            self.base_publish_times = 0
            self.base_training_times = 0
            self.base_training_role = None
            self.base_event_select = None
            self.base_info_role = None
            self.base_present_send = False
            self.base_zhiban_role = None

            self.base_debt = 0
            self.base_innumber = 1
            self.base_room_level = 1
            self.base_manage_roles = [None, None, None]
            self.base_move_points = 50
            self.base_JClevel = ""
            
        def reset(self):
            self.activities = self.base_activities
            self.jobs = self.base_jobs
            self.move_points = self.base_move_points
            self.currentscreen = self.base_currentscreen
            self.publish_times = self.base_publish_times
            self.training_times = self.base_training_times
            self.training_role = self.base_training_role
            self.event_select = self.base_event_select
            self.info_role = self.base_info_role
            self.present_send = self.base_present_send
            self.zhiban_role = self.base_zhiban_role

        def battle_params_reset(self):
            self.current_mode = None
            self.chosen_actor = None
            self.chosen_skill = None               # 选择的操作（技能or菜单）
            self.chosen_item = None
            self.active_actor = None               # 行动角色
            self.current_actor = None              # 状态显示角色
            self.spi_mp_cost = 0
            self.current_message = ""         
            self.current_ex_message = ""
            self.partyaction = "manual"            # 我方的行动角色
            self.partytarget = None                # 选中的敌方目标
            self.shown_actor = None                # 当前结算角色（显示）
            self.enemy = []
            self.master_skill = None
            self.skill_log_data = {}
            self.in_battle = False
            self.multi_buff_lock = False
            self.buff_source = {}
            self.battle_config = {}
            self.battle_blessing = {}

        # 清空主控制流
        def reset_main_control_bar(self):
            renpy.set_return_stack([])

        # -------- Room Part --------

        def end_init(self, player, party):
            self.reset_main_control_bar()
            # 金钱扣除债务部分
            player.currency -= self.debt
            # 值班人好感度、心情变化
            if self.zhiban_role is not None:
                self.zhiban_role.love += 5
                self.zhiban_role.mood -= 5
                if self.zhiban_role.mood < 0:
                    self.zhiban_role.mood = 0
            # 房间局部变量重置
            self.reset()
            # 人物重置薪水调整、浏览标签置为False；心情标签置零
            for role in party:
                role.watched = False
                role.salary_changed = False
                role.mood_changed = 0
            # 拜访次数加1
            self.innumber += 1

        def start_init(self, player, party):
            # 重置体力
            self.move_points = self.base_move_points
            # 负债情况下：清空债务；清空培训槽；清空角色工资
            if player.currency < 0:
                self.debt = self.base_debt
                self.manage_roles = self.base_manage_roles
                for role in party:
                    role.salary = 0
                    role.mood -= 25
                    if role.mood < 0:
                        role.mood = 0

            if player.kindness >= player.majesty and player.kindness >= player.casual:
                player.character = "善良"
            if player.majesty >= player.kindness and player.majesty >= player.casual:
                player.character = "严肃"
            if player.casual >= player.kindness and player.casual >= player.majesty:
                player.character = "随性"

            if player.currency >= 50000 and player.character == '随性':
                self.JClevel = "纸醉金迷"
            elif player.hideness >= 20 and player.character == '善良':
                self.JClevel = "芝兰之室"
            elif player.famous >= 100 and player.character == '严肃':
                self.JClevel = "江湖气息"
            else:
                self.JClevel = "人迹寥寥"

            # 初始化activities
            # 事件分为：无人物事件、单人物事件、多人物事件
            # 1、随机第一个人（0.5）
            # 2、随机第二个人（0.2）
            # 3、随机活动内容
            while len(self.activities) < 3:
                party_buffer = copy(party)
                active_first, active_second, event_buffer = None, None, None

                rand_index_fir = renpy.random.randint(0, 2 * len(party_buffer) - 1)
                # 选中单人或双人事件
                if rand_index_fir < len(party_buffer):
                    active_first = party_buffer.pop(rand_index_fir)

                    index = renpy.random.random()
                    # 选中双人事件
                    if index <= 0.2:
                        event_buffer = activity_buffer["multi"]
                        while active_second != active_first:
                            rand_index_sec = renpy.random.randint(0, len(party) - 1)
                            active_second = party[rand_index_sec]

                        event_index = renpy.random.randint(0, len(event_buffer) - 1)
                        event_info = event_buffer[event_index]
                        event_kind, event_description = event_info[0], event_info[1] % (active_first.name, active_second.name)
                    # 选中单人事件
                    else:
                        event_buffer = activity_buffer["single"]
                        event_index = renpy.random.randint(0, len(event_buffer) - 1)
                        event_info = event_buffer[event_index]
                        event_kind, event_description = event_info[0], event_info[1] % active_first.name

                # 选中无人事件
                else:
                    event_buffer = activity_buffer["none"]
                    event_index = renpy.random.randint(0, len(event_buffer) - 1)
                    event_info = event_buffer[event_index]
                    event_kind, event_description = event_info[0], event_info[1]

                event = Activities(active_kind=event_kind, active_state="未完成", active_description=event_description)
                self.activities.append(event)

            # 初始化jobs
            # 事件分为：随机3~8个委托任务
            # 1、随机任务数量（3~8）
            # 2、随机任务内容（随机奖励道具&数量）
            job_number = renpy.random.randint(3, 8)
            while len(self.jobs) < job_number:
                available_items = [item for item in item_list if not item.locked]
                available_items.sort(key=attrgetter("cost"), reverse=True)
                maxi_item_cost = max([item.cost for item in available_items])
                
                # 道具刷到的概率说明
                # {10%: level-3; 20%: level-2; 70%: level-1}
                # {level-1: range<=0.5; level-2: range<=0.85; level-3: range<1}
                available_item_level1 = [item for item in available_items if item.cost / maxi_item_cost <= 0.5]
                available_item_level2 = [item for item in available_items if (item.cost / maxi_item_cost > 0.5 and item.cost / maxi_item_cost <= 0.85)]
                available_item_level3 = [item for item in available_items if item.cost / maxi_item_cost > 0.85]

                # 选择任务奖励数量（1~3）
                rewards, reward_unique = [], set()
                select_count = 0
                has_level3, has_level2 = False, False
                reward_numbers = renpy.random.randint(1, 3)

                while len(rewards) < reward_numbers:
                    index = renpy.random.random()
                    
                    # 选中第一档奖励
                    if index <= 0.7:
                        # 选择任务奖励道具 & 数量
                        reward_index = renpy.random.randint(0, len(available_item_level1) - 1)
                        reward_item = available_item_level1[reward_index]
                        reward_count_index = renpy.random.randint(2, 3)

                        if reward_item not in reward_unique:
                            rewards.append((reward_item, reward_count_index))
                            reward_unique.add(reward_item)
                    # 选中第二档奖励
                    elif index <= 0.9:
                        if len(available_item_level2) > 0 and not has_level2:
                            reward_index = renpy.random.randint(0, len(available_item_level2) - 1)
                            reward_item = available_item_level2[reward_index]
                            reward_count_index = renpy.random.randint(1, 2)

                            if reward_item not in reward_unique:
                                rewards.append((reward_item, reward_count_index))
                                reward_unique.add(reward_item)
                                has_level2 = True
                    # 选中第三档奖励
                    else:
                        if len(available_item_level3) > 0 and not has_level3:
                            reward_index = renpy.random.randint(0, len(available_item_level3) - 1)
                            reward_item = available_item_level3[reward_index]
                            reward_count_index = 1
                            
                            if reward_item not in reward_unique:
                                rewards.append((reward_item, reward_count_index))
                                reward_unique.add(reward_item)
                                has_level3 = True

                    # 防止无限循环
                    select_count += 1
                    if select_count % 5 == 0:
                        reward_numbers -= 1

                # 选择任务类型
                job_index = renpy.random.randint(0, len(job_buffer) - 1)
                job_info = job_buffer[job_index]
                job_kind, job_description = job_info[0], job_info[1] % " ".join(["%sx%s" % (s1.name, s2) for s1, s2 in iter(rewards)])

                job = Jobs(job_kind=job_kind, job_state="待接受", rewards=rewards, description=job_description)
                self.jobs.append(job)

        def load(self):
            # pickle.load(open("local_config.pkl", "rb"))
            renpy.load("local_config.save")
            return

        def save(self):
            # path = open("local_config.pkl", "wb")
            # pickle.dump(self, path)
            renpy.save("local_config.save")
            return True

    # local_config = Localturn_params()
