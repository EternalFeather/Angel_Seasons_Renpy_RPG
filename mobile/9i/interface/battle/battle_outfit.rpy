
init python:
    outfit_dict_map = {
        "宝石": "stone",
        "法杖": "magic",
        "防具": "armor",
        "戒指": "ring",
        "武器": "weapon",
        "项链": "necklace"
    }
    # 装备属性种类
    outfit_attributes = {
        # 固定攻击
        "extend_attack": {
            "name": "攻击",
            "prime_L0": 33,
            "prime_plus_L0": 11,
            "prime_L1": 49,
            "prime_plus_L1": 17,
            "prime_L2": 65,
            "prime_plus_L2": 22,
            "prime_L3": 81,
            "prime_plus_L3": 27,
            "minor_min": 22,
            "minor_max": 28,
        },
        # 攻击加成
        "attack_ratio": {
            "name": "攻击加成",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        # 固定防御
        "extend_defance": {
            "name": "防御",
            "prime_L0": 6,
            "prime_plus_L0": 3,
            "prime_L1": 8,
            "prime_plus_L1": 4,
            "prime_L2": 11,
            "prime_plus_L2": 5,
            "prime_L3": 14,
            "prime_plus_L3": 6,
            "minor_min": 4,
            "minor_max": 5,
        },
        # 防御加成
        "defance_ratio": {
            "name": "防御加成",
            "prime_L0": 0.07,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.08,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.09,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.03,
            "minor_max": 0.04,
        },
        # 固定生命
        "extend_max_hp": {
            "name": "生命",
            "prime_L0": 137,
            "prime_plus_L0": 46,
            "prime_L1": 206,
            "prime_plus_L1": 69,
            "prime_L2": 274,
            "prime_plus_L2": 92,
            "prime_L3": 342,
            "prime_plus_L3": 114,
            "minor_min": 80,
            "minor_max": 100,
        },
        # 生命加成
        "max_hp_ratio": {
            "name": "生命加成",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        # 暴击率
        "critical_rate": {
            "name": "暴击率",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        # 暴击伤害
        "critical_damage": {
            "name": "暴击伤害",
            "prime_L0": 0.05,
            "prime_plus_L0": 0.02,
            "prime_L1": 0.09,
            "prime_plus_L1": 0.03,
            "prime_L2": 0.11,
            "prime_plus_L2": 0.04,
            "prime_L3": 0.14,
            "prime_plus_L3": 0.05,
            "minor_min": 0.03,
            "minor_max": 0.04,
        },
        # 速度
        "speed": {
            "name": "速度",
            "prime_L0": 6,
            "prime_plus_L0": 1,
            "prime_L1": 8,
            "prime_plus_L1": (1, 2),
            "prime_L2": 10,
            "prime_plus_L2": 2,
            "prime_L3": 13,
            "prime_plus_L3": 3,
            "minor_min": 2,
            "minor_max": 3,
        },
        # 效果命中
        "effect_hitrate": {
            "name": "效果命中",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.03,
            "minor_max": 0.04,
        },
        # 效果抵抗
        "effect_resistance": {
            "name": "效果抵抗",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.03,
            "minor_max": 0.04,
        },
        # 元素精通
        "elemental_mastery": {
            "name": "元素精通",
            "prime_L0": 21,
            "prime_plus_L0": 5,
            "prime_L1": 23,
            "prime_plus_L1": 6,
            "prime_L2": 25,
            "prime_plus_L2": 7,
            "prime_L3": 28,
            "prime_plus_L3": 10,
            "minor_min": 4,
            "minor_max": 5,
        },
        # 治疗加成
        "healing_bonus": {
            "name": "治疗加成",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        # 护盾强效
        "shield_strength": {
            "name": "护盾强效",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.03,
            "minor_max": 0.04,
        },
        # 元素伤害加成
        "fire_damage_bonus": {
            "name": "火元素伤害",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        "light_damage_bonus": {
            "name": "雷元素伤害",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        "wind_damage_bonus": {
            "name": "风元素伤害",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        "water_damage_bonus": {
            "name": "水元素伤害",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        "ice_damage_bonus": {
            "name": "冰元素伤害",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        "rock_damage_bonus": {
            "name": "岩元素伤害",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        },
        "physical_damage_bonus": {
            "name": "物理伤害",
            "prime_L0": 0.04,
            "prime_plus_L0": 0.01,
            "prime_L1": 0.06,
            "prime_plus_L1": (0.01, 0.02),
            "prime_L2": 0.08,
            "prime_plus_L2": 0.02,
            "prime_L3": 0.1,
            "prime_plus_L3": 0.03,
            "minor_min": 0.02,
            "minor_max": 0.03,
        }
    }
    # 装备两件套效果
    double_effects = {
        # 武器/防具/项链/戒指两件套效果
        "1": ("attack", 0.15, "攻击加成15%"),
        "2": ("defance", 0.3, "防御加成30%"),
        "3": ("max_hp", 0.15, "生命加成15%"),
        "4": ("critical_rate", 0.15, "暴击率15%"),
        "5": ("effect_hitrate", 0.15, "效果命中15%"),
        "6": ("effect_resistance", 0.15, "效果抵抗15%"),
        "7": ("elemental_mastery", 80, "元素精通80"),
        "8": ("healing_bonus", 0.15, "治疗加成15%"),
        "9": ("shield_strength", 0.2, "护盾强效20%"),
        # 法杖 + 宝石两件套效果
        "10": ("ice_damage_bonus", 0.15, "冰元素伤害加成15%"),
        "11": ("light_damage_bonus", 0.15, "雷元素伤害加成15%"),
        "12": ("fire_damage_bonus", 0.15, "火元素伤害加成15%"),
        "13": ("wind_damage_bonus", 0.15, "风元素伤害加成15%"),
        "14": ("water_damage_bonus", 0.15, "水元素伤害加成15%"),
        "15": ("rock_damage_bonus", 0.15, "岩元素伤害加成15%"),
    }
    # 装备四件套效果
    forth_effects = {
        # 控制：效果命中15%
        "1": ("天之印-碧落", "结算时，提升25%效果命中；造成伤害时，有15%基础概率随机附加眩晕、沉默、沉睡、减疗40%，持续1回合。"),
        # 防御：防御加成30%
        "2": ("地之轴-方仪", "受到暴击伤害时，有30%概率在伤害结算后为场上存活的友方单位提供1回合对应元素护盾（已拥有不同属性护盾的角色除外），该护盾能够吸收被攻击角色10%生命上限的伤害。"),
        # 元素配合：攻击、生命、护盾强效、攻击、效果抵抗、生命
        "3": ("日之轮-曦禾", "攻击时，有20%概率在结算时提升20%攻击，若目标处于无法动作状态，触发概率提升10%。被攻击时，有20%概率提升20%防御，若自身处于无法动作状态，触发概率提升10%。"),
        "4": ("月之华-琼勾", "我方角色行动结束时，若我方场上有角色处于无法动作状态，使其提升20点速度，持续1回合。（携带装备的队员不在场依然可以触发该效果）"),
        "5": ("山之巅-玉嶂", "处于护盾庇护下的所有友方角色，在伤害计算时提升20%攻击力和40%效果抵抗。"),
        "6": ("海之澜-沧渊", "造成伤害时，有20%概率击退目标30%行动条，若目标身上带有增益效果，触发概率提升10%。"),
        "7": ("风之陨-松吹", "战斗开始时，为队伍中全部的友方单位提供无法驱散的物理护盾持续1回合，护盾量相当于携带该装备角色生命上限的12%。当装备携带者在场上存活且任一友方单位受到伤害时，有20%概率削减施术者10点能量，多段攻击或群攻技能最多触发一次。"), 
        "8": ("雪之嚣-玉絮", "造成伤害时，有12%（若目标带有减速效果则为20%）基础概率冻结1回合；装备携带者受到攻击时，有30%概率使施术者减速20点，持续1回合。"),
        # 传说套装
        # 辅助、奶妈：治疗加成15%
        "9": ("春之花-仑灵", "治疗时，额外提供20%（若目标HP值低于20%，改为提供50%）治疗加成；每次行动结束后，有20%概率为场上所有存活的友方单位恢复20点能量。"),
        # 辅助、元素增伤：元素精通80
        "10": ("夏之声-朱明", "友方角色引发的超载、感电反应造成的伤害提升40%；蒸发、融化反应加成系数提高20%；扩散、超导反应额外降低目标15%对应元素抗性；冻结反应基础概率提升10%；结晶反应提供的护盾量提升25%。"),
        # 输出、爆发：暴击15%
        "11": ("秋之韵-素律", "伤害计算时，若目标当前生命值比例大于70%，提升30%伤害；若目标当前生命值比例小于70%，生命值每降低20%提升10%伤害。"),
        # 输出、多段：暴击15%
        "12": ("冬之羽-玄英", "攻击时，有50%概率无视对方45%防御；使用技能后每10点能量额外提升该技能4%的伤害。"),
    }


    class Outfit(object):
        """
        属性：名称、序号、介绍、等级、稀有度、经验值、主属性、副属性、二件套属性、四件套属性、类型、价格
        """
        def __init__(self, objectname="", name="", rarity=0, prime_attribute_list=[], double_effect_idx=0, forth_effect_idx=0,
            base_cost=0, category="", number=0):
            # 名称
            self.objectname = objectname
            self.original_name = self.objectname.capitalize().replace("_", " ")
            self.name = name
            # 序号
            self.number = int(number)
            # 等级
            self.level = 0
            # 稀有度(0~4)
            self.rarity = int(rarity)
            # 经验值
            self.xp = 0.0
            # 价格
            self.cost = int(base_cost)
            # 主属性：{名称：数值}
            self.prime_attribute = {}
            self.prime_attribute_list = prime_attribute_list
            # 副属性：{名称1：数值1, 名称2:数值2 ...}
            self.minor_attributes = {}
            # 二件套属性
            self.double_effect = double_effects[double_effect_idx]
            # 四件套属性
            self.forth_effect = forth_effects[forth_effect_idx] if forth_effect_idx in forth_effects else None
            # 类型
            self.category = category
            # 装备锁
            self.locked = False
        
        # 属性重置
        def reset_params(self):
            self.level = 0
            self.xp = 0.0
            self.prime_attribute = {}
            self.minor_attributes = {}
        
        # 初始化主属性、品级、附加价格
        def init_params(self):
            # 初始化价格
            self.cost += 500 * self.rarity

            # 初始化主属性
            if len(self.prime_attribute_list) > 0:
                chosen_index = renpy.random.randint(0, len(self.prime_attribute_list) - 1)
            else:
                chosen_index = 0
            chosen_prime_attribute = self.prime_attribute_list[chosen_index]
            tmp_prime_attribute = outfit_attributes[chosen_prime_attribute]
            self.prime_attribute[tmp_prime_attribute["name"]] = tmp_prime_attribute.get("prime_L%d" % self.rarity)

            # 初始化副属性
            attr_number = renpy.random.randint(2, 4)
            copy_outfit_attributes = list(outfit_attributes.keys())

            while len(self.minor_attributes) < attr_number:
                chosen_index = renpy.random.randint(0, len(outfit_attributes) - 1)
                chosen_attribute = copy_outfit_attributes[chosen_index]
                tmp_attr = outfit_attributes[chosen_attribute]

                chosen_name = tmp_attr["name"]
                chosen_number_min = tmp_attr["minor_min"]
                chosen_number_max = tmp_attr["minor_max"]

                # 小数2选1，整数范围内n选1
                chosen_minor_number = 0
                if isinstance(chosen_number_min, float):
                    chosen_index_number = renpy.random.randint(0, 1)
                    if chosen_index_number == 0:
                        chosen_minor_number = chosen_number_min
                    else:
                        chosen_minor_number = chosen_number_max
                elif isinstance(chosen_number_min, int):
                    chosen_minor_number = renpy.random.randint(chosen_number_min, chosen_number_max)
                
                if (chosen_name not in self.minor_attributes) and not ("伤害" in chosen_name and chosen_name != "暴击伤害" and any(("伤害" in attr and attr != "暴击伤害") for attr in self.minor_attributes)):
                    self.minor_attributes[chosen_name] = chosen_minor_number

        # 获得
        def get(self, who):
            if len(who.equipments[self.category]) < 99:
                getted_item = copy(self)
                getted_item.reset_params()
                getted_item.init_params()
                who.equipments[getted_item.category].append(getted_item)

        # 购买（初始化主属性）
        def buy(self, who):
            if len(who.equipments[self.category]) >= 99:
                renpy.music.play("Click_Disabled_Button", channel="battle_music")
                renpy.show_screen("alt_notify", _("装备栏已接近上限无法购买 T v T 。"))
            elif self.cost <= who.currency:
                getted_item = copy(self)
                getted_item.reset_params()
                getted_item.init_params()
                who.equipments.append(getted_item)
                who.currency -= self.cost
                renpy.music.play("Buy_Item_Money", channel="battle_music")
                store.const_name = self.name
                renpy.show_screen("alt_notify", _("成功购买装备 【[const_name]】 > w < 。"))
            else:
                renpy.music.play("Click_Disabled_Button", channel="battle_music")
                renpy.show_screen("alt_notify", _("魔法币不足无法购买 T v T 。"))

        # 出售
        def sell(self, who):
            local_config.player.currency += self.cost
            local_config.player.equip_experience += int(self.xp * 0.8)
            local_config.player.equipments[self.category].remove(self)

        # 装备
        def equip_on(self, who):
            # 装备装上
            local_config.player.equipments[self.category].remove(self)
            who.outfits[self.category] = self
            who.equip_recalculate()

        # 敌方装备
        def enemy_equip_on(self, who):
            who.outfits[self.category] = self
            who.equip_recalculate()

        def equip_off(self, who):
            local_config.player.equipments[self.category].append(who.outfits[self.category])
            who.outfits[self.category] = None
            who.equip_recalculate()

        def enemy_equip_off(self, who):
            who.outfits[self.category] = None
            who.equip_recalculate()

        # 强化
        def level_up(self, who, experience):
            if self.level >= 15:
                return

            to_level = self.level + 1
            # 经验值减少
            who.equip_experience -= experience
            self.xp += experience
            # 等级提升
            self.level = to_level

            # 主属性增加
            prime_attribute_name = list(self.prime_attribute.keys())[0]
            tmp_prime_attribute = None
            for name, value in outfit_attributes.items():
                if value["name"] == prime_attribute_name:
                    tmp_prime_attribute = value
                    break
            prime_attribute_up_number = tmp_prime_attribute.get("prime_plus_L%d" % self.rarity)
            if isinstance(prime_attribute_up_number, tuple):
                if to_level % 2 != 0:
                    prime_attribute_up_number = prime_attribute_up_number[0]
                else:
                    prime_attribute_up_number = prime_attribute_up_number[1]
            self.prime_attribute[prime_attribute_name] += prime_attribute_up_number

            # 副属性随机增加
            if to_level % 3 == 0:
                if len(self.minor_attributes) < 4:
                    if any(("伤害" in attr and attr != "暴击伤害") for attr in self.minor_attributes):
                        copy_outfit_attributes = {name: value for name, value in outfit_attributes.items() if (value["name"] not in self.minor_attributes and "damage_bonus" not in name)}
                    else:
                        copy_outfit_attributes = {name: value for name, value in outfit_attributes.items() if value["name"] not in self.minor_attributes}
                    chosen_index = renpy.random.randint(0, len(copy_outfit_attributes) - 1)
                    chosen_attribute = list(copy_outfit_attributes.keys())[chosen_index]
                    tmp_attr = copy_outfit_attributes[chosen_attribute]

                    chosen_name = tmp_attr["name"]
                    chosen_number_min = tmp_attr["minor_min"]
                    chosen_number_max = tmp_attr["minor_max"]

                    # 小数2选1，整数范围内n选1
                    chosen_minor_number = 0
                    if isinstance(chosen_number_min, float):
                        chosen_index_number = renpy.random.randint(0, 1)
                        if chosen_index_number == 0:
                            chosen_minor_number = chosen_number_min
                        else:
                            chosen_minor_number = chosen_number_max
                    elif isinstance(chosen_number_min, int):
                        chosen_minor_number = renpy.random.randint(chosen_number_min, chosen_number_max)
                    
                    if chosen_name not in self.minor_attributes:
                        self.minor_attributes[chosen_name] = chosen_minor_number
                else:
                    chosen_index = renpy.random.randint(0, len(self.minor_attributes) - 1)
                    name = list(self.minor_attributes.keys())[chosen_index]
                    number = copy(self.minor_attributes[name])
                    for key, value in outfit_attributes.items():
                        if value["name"] == name:
                            tmp_minor_attribute = value
                            break
                    minor_attribute_up_number_min = tmp_minor_attribute["minor_min"]
                    minor_attribute_up_number_max = tmp_minor_attribute["minor_max"]

                    chosen_minor_up_number = 0
                    if isinstance(minor_attribute_up_number_min, float):
                        chosen_index_number = renpy.random.randint(0, 1)
                        if chosen_index_number == 0:
                            chosen_minor_up_number = minor_attribute_up_number_min
                        else:
                            chosen_minor_up_number = minor_attribute_up_number_max
                    elif isinstance(minor_attribute_up_number_min, int):
                        chosen_minor_up_number = renpy.random.randint(minor_attribute_up_number_min, minor_attribute_up_number_max)

                    self.minor_attributes[name] += chosen_minor_up_number


    # 装备图片初始化
    def register_outfit_image(duplicate=False):
        for dtype, dname in outfit_dict_map.items():
            for file in renpy.list_files():
                if file.startswith('9i/interface/battle/outfits/{}/'.format(dtype)) and file.endswith('.png'):
                    renpy.image(dname + "_" + file.split("/")[-1].split(".png")[0], file)
                    if duplicate:
                        renpy.image(dname + "_" + file.split("/")[-1].split(".png")[0], file)


    def read_outfit(filename):
        outfit_list = []

        f = renpy.file(filename)
        for n, l in enumerate(f):
            l = l.decode("utf-8")
            a = l.rstrip().split(",")
            if a[0] != "":
                setattr(store, a[0], Outfit(a[0], a[1], a[2], a[3].split("|"), a[4], a[5], a[6], a[7], number=n))
                outfit_list.append(globals()[a[0]])
        f.close()

        return outfit_list
