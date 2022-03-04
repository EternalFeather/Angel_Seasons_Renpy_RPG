
init python:
    class Item(object):
        """
        道具属性：名称、序号、介绍、价格、种类（功能）
        """
        def __init__(self, objectname="", name="", cost=0, info="", use_target="", image="", number=0):
            # 名称
            self.objectname = objectname
            self.original_name = self.objectname.capitalize().replace("_", " ")
            self.name = name
            # 序号
            self.number = int(number)
            # 介绍
            self.info = info
            # 价格
            self.cost = int(cost)
            self.sellcost = self.cost / 5
            # 目标种类（单体single、群体multi）
            self.use_target = use_target
            # 道具解锁
            self.locked = False
            # 图片
            self.image = image
        
        # 购买
        def buy(self, who):
            if self.cost <= who.currency:
                if self.objectname in who.items:
                    who.items[self.objectname] += 1
                else:
                    who.items[self.objectname] = 1
                who.currency -= self.cost
                renpy.music.play("Buy_Item_Money", channel="battle_music")
                store.const_name = self.name
                renpy.show_screen("alt_notify", _("成功购买 【[const_name]】 > w < 。"))
            else:
                renpy.music.play("Click_Disabled_Button", channel="battle_music")
                renpy.show_screen("alt_notify", _("魔法币不足无法购买 T v T 。"))

        # 贩卖
        def sell(self, who):
            who.items[self.objectname] -= 1
            if who.items[self.objectname] == 0:
                who.items.pop(self.objectname)
            who.currency += self.sellcost
            renpy.music.play("sell_item_money", channel="battle_music")
            store.const_name = self.name
            renpy.show_screen("alt_notify", _("成功出售【[const_name]】 > w < 。"))

        # 获得
        def get(self, who):
            if self.objectname in who.items:
                who.items[self.objectname] += 1
            else:
                who.items[self.objectname] = 1

        # 使用
        def use(self, who, target=None, ally_environment_effects=None):
            # 为选中角色恢复生命值上限的30%，并额外恢复1250点生命值
            if self.objectname == "eggs" and self.use_target == "single":
                max_hp = target.battle_max_hp if local_config.in_battle else target.max_hp
                if 0 < target.hp < max_hp:
                    store.recover_hp = int(max_hp * 0.3 + 1250)
                    target.hp += store.recover_hp
                    if target.hp > max_hp:
                        target.hp = max_hp

                    target.face_change()
                    who.items[self.objectname] -= 1
                    if who.items[self.objectname] == 0:
                        who.items.pop(self.objectname)
                    local_config.chosen_item = None
                    store.const_name = target.name
                    renpy.music.play("Health_Potion", channel="battle_music")
                    renpy.hide("message_screen")
                    renpy.show_screen("alt_notify", _("成功为[const_name]回复[recover_hp]点HP。"))

                    if local_config.tutorial_step == "item_use":
                        local_config.tutorial_step = ""
                else:
                    local_config.chosen_item = None
                    renpy.music.play("Click_Disabled_Button", channel="battle_music")
                    renpy.hide("message_screen")
                    renpy.show_screen("alt_notify", _("无法对死亡或满血的角色使用该物品。"))
            # 恢复队伍中所有角色生命上限50%的生命值
            elif self.objectname == "mana_eggs" and self.use_target == "multi":
                for role in local_config.party:
                    max_hp = role.battle_max_hp if local_config.in_battle else role.max_hp
                    if 0 < role.hp < max_hp:
                        store.recover_hp = int(max_hp * 0.5)
                        role.hp += store.recover_hp
                        if role.hp > max_hp:
                            role.hp = max_hp

                        role.face_change()
                        
                who.items[self.objectname] -= 1
                if who.items[self.objectname] == 0:
                    who.items.pop(self.objectname)
                local_config.chosen_item = None
                renpy.music.play("Health_Potion", channel="battle_music")
                renpy.show_screen("alt_notify", _("全体友方角色回复50%HP。"))
            # 复苏选中的角色，为其恢复生命值上限的50%以及50点能量，并额外恢复1250点生命值
            elif self.objectname == "mana_potion" and self.use_target == "single":
                max_hp = target.battle_max_hp if local_config.in_battle else target.max_hp
                if target.hp < 1:
                    target.full_reset(heal_hp=False, ally_environment_effects=ally_environment_effects, turn_end=False, level_reset=False)
                    store.recover_hp = int(max_hp * 0.5) + 1250
                    if store.recover_hp > max_hp:
                        target.hp = max_hp
                    else:
                        target.hp = store.recover_hp
                    target.mp = int(0.5 * target.max_mp)

                    target.face_change()
                    who.items[self.objectname] -= 1
                    if who.items[self.objectname] == 0:
                        who.items.pop(self.objectname)
                    local_config.chosen_item = None
                    store.const_name = target.name

                    # for n, role in enumerate(local_config.party):
                    #     if role.hp < 1:
                    #         local_config.party.remove(role)
                    #         local_config.party.remove(target)
                    #         local_config.party.insert(n, target)
                    #         local_config.party.append(role)
                    #         break
                    target.reborn_calculate(ally_environment_effects=ally_environment_effects)

                    renpy.music.play("Health_Potion", channel="battle_music")
                    renpy.hide("message_screen")
                    renpy.show_screen("alt_notify", _("成功唤醒[const_name]，并回复其[recover_hp]点HP和50点MP。"))
                else:
                    local_config.chosen_item = None
                    renpy.music.play("Click_Disabled_Button", channel="battle_music")
                    renpy.show_screen("alt_notify", _("仍存活的角色无法使用该物品。"))
            # 复苏队伍中所有阵亡的角色，为其恢复生命值上限的100%和100%能量；其余存活的角色清除所有不良状态和元素附着，并恢复生命值上限的100%和100%能量
            elif self.objectname == "angel_tears" and self.use_target == "multi":
                if local_config.in_battle:
                    for role in local_config.party:
                        # 角色阵亡
                        if role.hp < 1:
                            role.full_reset(heal_hp=False, ally_environment_effects=ally_environment_effects, turn_end=False, level_reset=False)
                            role.hp = role.battle_max_hp
                            role.mp = role.max_mp
                            role.face_change()
                            role.reborn_calculate(ally_environment_effects=ally_environment_effects)
                        elif 0 < role.hp < role.battle_max_hp:
                            debuffs = copy(role.debuff)
                            for buff_name, item in debuffs.items():
                                buff_obj = getattr(store, buff_name)
                                if buff_obj.removeable or buff_name in ["lost", "dizziness", "deep_frozen", "deep_sleepy"]:
                                    buff_obj.calculate(role, ally_environment_effects, None, None, "clean")
                            role.ebuff = {}
                            role.hp = role.battle_max_hp
                            role.mp = role.max_mp
                            role.face_change()

                    who.items[self.objectname] -= 1
                    if who.items[self.objectname] == 0:
                        who.items.pop(self.objectname)
                    local_config.chosen_item = None
                    renpy.music.play("Health_Potion", channel="battle_music")
                    renpy.show_screen("alt_notify", _("成功回复全员状态。"))
            # 为角色提供一定量经验值
            elif self.objectname == "soul_piece" and self.use_target == "single":
                if target.level < 40:
                    target.xp += 120290
                    who.items[self.objectname] -= 1
                    if who.items[self.objectname] == 0:
                        who.items.pop(self.objectname)
                    local_config.chosen_item = None
                    store.const_name = target.name
                    renpy.music.play("Health_Potion", channel="battle_music")
                    renpy.hide("message_screen")
                    renpy.show_screen("alt_notify", _("角色[const_name]成功获得120290经验值。"))
                else:
                    local_config.chosen_item = None
                    renpy.music.play("Click_Disabled_Button", channel="battle_music")
                    renpy.hide("message_screen")
                    renpy.show_screen("alt_notify", _("已经达到40级的角色建议不使用该物品。"))
            # 为装备提供一定量经验值
            elif self.objectname == "soul_raise" and self.use_target == "multi":
                local_config.player.equip_experience += 45435
                who.items[self.objectname] -= 1
                if who.items[self.objectname] == 0:
                    who.items.pop(self.objectname)
                local_config.chosen_item = None
                renpy.music.play("Health_Potion", channel="battle_music")
                renpy.hide("message_screen")
                renpy.show_screen("alt_notify", _("成功为装备提供30290经验值。"))
            # 场上的所有角色攻击力提高12%，暴击率提升10%，暴击伤害提升10%，持续2回合
            elif self.objectname == "attack_meal" and self.use_target == "multi":
                for role in local_config.party[:3]:
                    # 攻击力提高12%
                    buff = getattr(store, "strong")
                    item = (2, 0.12)
                    buff.calculate(role, None, item, "meal", "get")
                    # 暴击率提升10%，暴击伤害提升10%
                    buff = getattr(store, "violence")
                    item = (2, (0.1, 0.1))
                    buff.calculate(role, None, item, "meal", "get")

                who.items[self.objectname] -= 1
                if who.items[self.objectname] == 0:
                    who.items.pop(self.objectname)
                local_config.chosen_item = None
                renpy.music.play("Health_Potion", channel="battle_music")
                renpy.show_screen("alt_notify", _("我方角色攻击属性得到增强。"))
            # 场上的所有角色防御力提高150点，治疗效果提升8%，护盾强效提升8%，持续2回合
            elif self.objectname == "defance_meal" and self.use_target == "multi":
                for role in local_config.party[:3]:
                    # 防御力提高150点
                    buff = getattr(store, "sturdy")
                    item = (2, 150)
                    buff.calculate(role, None, item, "meal", "get")
                    # 治疗效果提升8%
                    buff = getattr(store, "healing")
                    item = (2, 0.08)
                    buff.calculate(role, None, item, "meal", "get")
                    # 护盾强度提升8%
                    buff = getattr(store, "armor")
                    item = (2, 0.08)
                    buff.calculate(role, None, item, "meal", "get")

                who.items[self.objectname] -= 1
                if who.items[self.objectname] == 0:
                    who.items.pop(self.objectname)
                local_config.chosen_item = None
                renpy.music.play("Health_Potion", channel="battle_music")
                renpy.show_screen("alt_notify", _("我方角色防御属性得到增强。"))
            # 场上的所有角色物理及各元素伤害提升15%，元素精通提高60点，持续2回合
            elif self.objectname == "ele_attack_meal" and self.use_target == "multi":
                for role in local_config.party[:3]:
                    # 物理及各元素伤害提升15%
                    buff = getattr(store, "condensed")
                    item = (2, (0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15))
                    buff.calculate(role, None, item, "meal", "get")
                    # 元素精通提高60点
                    buff = getattr(store, "master")
                    item = (2, 60)
                    buff.calculate(role, None, item, "meal", "get")

                who.items[self.objectname] -= 1
                if who.items[self.objectname] == 0:
                    who.items.pop(self.objectname)
                local_config.chosen_item = None
                renpy.music.play("Health_Potion", channel="battle_music")
                renpy.show_screen("alt_notify", _("我方角色元素攻击得到增强。"))
            # 场上的所有角色物理及各元素抗性提升25%，效果抵抗提升20%，持续2回合
            elif self.objectname == "ele_defance_meal" and self.use_target == "multi":
                for role in local_config.party[:3]:
                    # 物理及各元素抗性提升25%
                    buff = getattr(store, "control")
                    item = (2, (0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25))
                    buff.calculate(role, None, item, "meal", "get")
                    # 效果抵抗提升20%
                    buff = getattr(store, "barrier")
                    item = (2, 0.2)
                    buff.calculate(role, None, item, "meal", "get")

                who.items[self.objectname] -= 1
                if who.items[self.objectname] == 0:
                    who.items.pop(self.objectname)
                local_config.chosen_item = None
                renpy.music.play("Health_Potion", channel="battle_music")
                renpy.show_screen("alt_notify", _("我方角色元素防御得到增强。"))
            # 场上的所有角色速度提高8点，效果命中提升20%，持续2回合
            elif self.objectname == "magic_meal" and self.use_target == "multi":
                for role in local_config.party[:3]:
                    # 速度提高8点
                    buff = getattr(store, "flow")
                    item = (2, 8)
                    buff.calculate(role, None, item, "meal", "get")
                    # 效果命中提升20%
                    buff = getattr(store, "liberate")
                    item = (2, 0.2)
                    buff.calculate(role, None, item, "meal", "get")

                who.items[self.objectname] -= 1
                if who.items[self.objectname] == 0:
                    who.items.pop(self.objectname)
                local_config.chosen_item = None
                renpy.music.play("Health_Potion", channel="battle_music")
                renpy.show_screen("alt_notify", _("我方角色控场力得到增强。"))
            elif self.objectname == "soul_mirror" and self.use_target == "single":
                if any(s.level < 5 for s in target.skills):
                    selectup_skill = target.skill_levelup()
                    who.items[self.objectname] -= 1
                    if who.items[self.objectname] == 0:
                        who.items.pop(self.objectname)
                    local_config.chosen_item = None
                    store.const_name = target.name
                    renpy.music.play("Health_Potion", channel="battle_music")
                    renpy.hide("message_screen")
                    renpy.show_screen("alt_notify", _("技能「[selectup_skill.name]」强化至Lv.[selectup_skill.level]"))
                else:
                    local_config.chosen_item = None
                    renpy.music.play("Click_Disabled_Button", channel="battle_music")
                    renpy.hide("message_screen")
                    renpy.show_screen("alt_notify", _("技能满级的角色不能使用该物品。"))
            else:
                local_config.chosen_item = None
                renpy.music.play("Click_Disabled_Button", channel="battle_music")
                renpy.hide("message_screen")
                renpy.show_screen("alt_notify", _("该物品无法在此使用。"))


    def read_item(filename):
        item_list = []

        f = renpy.file(filename)
        for n, l in enumerate(f):
            l = l.decode("utf-8")
            a = l.rstrip().split(",")
            if a[0] != "":
                setattr(store, a[0], Item(a[0], a[1], a[2], a[3], a[4], a[5], number=n))
                item_list.append(globals()[a[0]])
        f.close()

        return item_list
