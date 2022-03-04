
init python:
    import math
    from operator import itemgetter

    # 角色天赋（参考原神、阴阳师）定义
    ability_dict = {
        # 坚韧
        "Fortitude":_("角色的生命每损失上限的25%，则在伤害计算时提升50点防御力，同时在获得治疗和护盾时，提升10%治疗加成和10%护盾强效。"), 
        # 耐心/冷静（Done）
        "Patient":_("当角色选择待机、魔导力回路或是处于无法动作的场合，在伤害计算后获得10%攻击力、暴击率以及60点元素精通加成，持续1回合。"),
        # 魔术/神秘（Done）
        "Sneaking":_("在魔导力回路模式中额外获得一次抽卡机会，结束模式时恢复使用卡牌数x10点MP，最大不超过已损失MP的50%。"),
        # 澎湃（Done）
        "Spiritual":_("可在MP不足的情况下使用元素战技或元素爆发，若透支的MP值超过（包括）20点，在伤害计算后角色进入1回合眩晕。"),
        # 适应（Done）
        "Adaptive":_("当角色受到对应元素、物理伤害时，在伤害结算后有8%的概率获得相当于角色攻击力x60%的固定数值元素、物理护盾（最高不超过生命上限的10%），持续1回合。"),
        # 狂暴/刁蛮（Done）
        "Brutal":_("当角色HP低于上限的10%，使用元素爆发后获得90%行动条提前。"), 
        # 灵魂（Done）
        "Soul":_("战斗开始时获得不可驱散的“天佑”效果。【每场战斗只会触发一次】"),
        # 反射（Done）
        "Reflexes":_("当角色受到非元素反应控制效果的时候，有8%的概率无视控制效果，并将效果转移给施术对象。"),
        # 宁静（Done）
        "Serenity":_("永久获得20%的效果抵抗。战斗结算过程中，每有一名友方单位处于无法动作的效果影响下，额外提供10%的效果抵抗。"),
        # 皮肤（Done）
        "Skin":_("所有元素附着概率变为50%。受到超过自身生命上限30%的非物理元素伤害并依旧存活时，有20%概率在伤害结算后获得30%的对应元素抗性，持续2回合。"),
        # 激励（Done）
        "Endurance":_("在施放元素爆发后，有12%的概率让场上的所有存活的友方单位提升30%的攻击力，持续1回合。"),
        # 恢复/复苏（Done）
        "Recovery":_("当角色生命值低于上限的20%，每次行动前恢复生命上限8%的生命和10点MP。"),
        # 谨慎（Done）
        "Prudent":_("当角色生命值低于50%，伤害结算时防御力提升100点。当角色生命高于50%，伤害结算时暴击率、攻击力提升15%。"),
        # 回响（Done）
        "Conjurer":_("非物理元素技能暴击时，有30%概率在伤害结算时无视目标单位15%的对应元素抗性，同时为自己提供10点MP回复。"),
        # 狩猎（Done）
        "Hunter":_("物理元素技能暴击时，有30%概率在伤害结算时无视目标单位30%的物理抗性，同时为自己提供10点MP回复。"),
        # 灵巧（Done）
        "Flexible":_("当角色处于无法动作效果影响下时，每当有一名敌方角色行动，行动条提前20%。"), 
        # 庇护（Done）
        "Solid":_("当角色受到超过自身生命上限30%的物理伤害并依旧存活时，有20%概率在伤害结算时获得30%的物理抗性。"),
        # 格挡/幸运（Done）
        "Acrobat":_("角色附加的增益、减益效果有25%概率使其持续回合数增加1回合。"),
    }


    class Actor(object):
        """
        角色战斗属性：生命、能量、攻击、防御、速度、暴击率、暴击伤害、效果命中、效果抵抗、元素精通、治疗加成、护盾强度、（火、水、冰、雷、风、岩、物理）元素伤害加成、（火、水、冰、雷、风、岩、物理）元素抗性
        角色作用参数：物件名称、名字、序号、表情、显示坐标、介绍、等级、突破开关、星级、金钱（价格）、稀有度、种族、性格、好感度、心情、名气、隐蔽、善良、威严、随性、薪水、故事、技能、装备、道具、经验值、buff、选中的（技能、目标）、行动条进度
        """
        def __init__(self, objectname="", name="", star=1, support_color="", support_direct="", rarity="SR", category="", currency=0, skills=None, skills_v2=None, abilities=None, 
            hitface="", sufferface="", info="", attack=0, max_hp=0, defance=0, speed=0, critical_rate=0.0, critical_damage=0.0, effect_hitrate=0.0, effect_resistance=0.0, elemental_mastery=0.0,
            healing_bonus=0.0, shield_strength=0.0, fire_damage_bonus=0.0, fire_elemental_resistance=0.0, light_damage_bonus=0.0, light_elemental_resistance=0.0,
            wind_damage_bonus=0.0, wind_elemental_resistance=0.0, ice_damage_bonus=0.0, ice_elemental_resistance=0.0, water_damage_bonus=0.0, water_elemental_resistance=0.0, 
            rock_damage_bonus=0.0, rock_elemental_resistance=0.0, physical_damage_bonus=0.0, physical_elemental_resistance=0.0, prime_attribute=None, number=0):
            # 战斗属性
            # 攻击
            self.attack = float(attack)
            self.base_attack = float(attack)
            self.ori_attack = float(attack)
            # 额外攻击
            self.extend_attack = 0
            self.base_extend_attack = 0
            self.ori_extend_attack = 0
            # 生命
            self.max_hp = float(max_hp)
            self.hp = float(max_hp)
            self.base_max_hp = float(max_hp)
            self.ori_max_hp = float(max_hp)
            # 额外生命
            self.extend_max_hp = 0
            self.base_extend_max_hp = 0
            self.ori_extend_max_hp = 0
            # 能量
            self.max_mp = 100.0
            self.mp = self.max_mp
            # 防御
            self.defance = float(defance)
            self.base_defance = float(defance)
            self.ori_defance = float(defance)
            # 额外防御
            self.extend_defance = 0
            self.base_extend_defance = 0
            self.ori_extend_defance = 0
            # 速度
            self.speed = float(speed)
            self.base_speed = float(speed)
            self.ori_speed = float(speed)
            # 暴击率
            self.critical_rate = float(critical_rate)
            self.base_critical_rate = float(critical_rate)
            self.ori_critical_rate = float(critical_rate)
            # 暴击伤害
            self.critical_damage = float(critical_damage)
            self.base_critical_damage = float(critical_damage)
            self.ori_critical_damage = float(critical_damage)
            # 效果命中
            self.effect_hitrate = float(effect_hitrate)
            self.base_effect_hitrate = float(effect_hitrate)
            self.ori_effect_hitrate = float(effect_hitrate)
            # 效果抵抗
            self.effect_resistance = float(effect_resistance)
            self.base_effect_resistance = float(effect_resistance)
            self.ori_effect_resistance = float(effect_resistance)
            # 元素精通
            self.elemental_mastery = int(elemental_mastery)
            self.base_elemental_mastery = float(elemental_mastery)
            self.ori_elemental_mastery = float(elemental_mastery)
            # 治疗加成
            self.healing_bonus = float(healing_bonus)
            self.base_healing_bonus = float(healing_bonus)
            self.ori_healing_bonus = float(healing_bonus)
            # 护盾强度
            self.shield_strength = float(shield_strength)
            self.base_shield_strength = float(shield_strength)
            self.ori_shield_strength = float(shield_strength)
            # 火元素伤害加成
            self.fire_damage_bonus = float(fire_damage_bonus)
            self.base_fire_damage_bonus = float(fire_damage_bonus)
            self.ori_fire_damage_bonus = float(fire_damage_bonus)
            # 火元素抗性
            self.fire_elemental_resistance = float(fire_elemental_resistance)
            self.base_fire_elemental_resistance = float(fire_elemental_resistance)
            self.ori_fire_elemental_resistance = float(fire_elemental_resistance)
            # 雷元素伤害加成
            self.light_damage_bonus = float(light_damage_bonus)
            self.base_light_damage_bonus = float(light_damage_bonus)
            self.ori_light_damage_bonus = float(light_damage_bonus)
            # 雷元素抗性
            self.light_elemental_resistance = float(light_elemental_resistance)
            self.base_light_elemental_resistance = float(light_elemental_resistance)
            self.ori_light_elemental_resistance = float(light_elemental_resistance)
            # 风元素伤害加成
            self.wind_damage_bonus = float(wind_damage_bonus)
            self.base_wind_damage_bonus = float(wind_damage_bonus)
            self.ori_wind_damage_bonus = float(wind_damage_bonus)
            # 风元素抗性
            self.wind_elemental_resistance = float(wind_elemental_resistance)
            self.base_wind_elemental_resistance = float(wind_elemental_resistance)
            self.ori_wind_elemental_resistance = float(wind_elemental_resistance)
            # 冰元素伤害加成
            self.ice_damage_bonus = float(ice_damage_bonus)
            self.base_ice_damage_bonus = float(ice_damage_bonus)
            self.ori_ice_damage_bonus = float(ice_damage_bonus)
            # 冰元素抗性
            self.ice_elemental_resistance = float(ice_elemental_resistance)
            self.base_ice_elemental_resistance = float(ice_elemental_resistance)
            self.ori_ice_elemental_resistance = float(ice_elemental_resistance)
            # 水元素伤害加成
            self.water_damage_bonus = float(water_damage_bonus)
            self.base_water_damage_bonus = float(water_damage_bonus)
            self.ori_water_damage_bonus = float(water_damage_bonus)
            # 水元素抗性
            self.water_elemental_resistance = float(water_elemental_resistance)
            self.base_water_elemental_resistance = float(water_elemental_resistance)
            self.ori_water_elemental_resistance = float(water_elemental_resistance)
            # 岩元素伤害加成
            self.rock_damage_bonus = float(rock_damage_bonus)
            self.base_rock_damage_bonus = float(rock_damage_bonus)
            self.ori_rock_damage_bonus = float(rock_damage_bonus)
            # 岩元素抗性
            self.rock_elemental_resistance = float(rock_elemental_resistance)
            self.base_rock_elemental_resistance = float(rock_elemental_resistance)
            self.ori_rock_elemental_resistance = float(rock_elemental_resistance)
            # 物理伤害加成
            self.physical_damage_bonus = float(physical_damage_bonus)
            self.base_physical_damage_bonus = float(physical_damage_bonus)
            self.ori_physical_damage_bonus = float(physical_damage_bonus)
            # 物理抗性
            self.physical_elemental_resistance = float(physical_elemental_resistance)
            self.base_physical_elemental_resistance = float(physical_elemental_resistance)
            self.ori_physical_elemental_resistance = float(physical_elemental_resistance)
            # 主属性
            self.prime_attribute = prime_attribute

            # 战斗备份参数
            self.battle_max_hp = None
            self.battle_attack = None
            self.battle_extend_attack = None
            self.battle_defance = None
            self.battle_speed = None
            self.battle_critical_rate = None
            self.battle_critical_damage = None
            self.battle_effect_hitrate = None
            self.battle_effect_resistance = None
            self.battle_elemental_mastery = None
            self.battle_healing_bonus = None
            self.battle_shield_strength = None
            self.battle_fire_damage_bonus = None
            self.battle_fire_elemental_resistance = None
            self.battle_light_damage_bonus = None
            self.battle_light_elemental_resistance = None
            self.battle_wind_damage_bonus = None
            self.battle_wind_elemental_resistance = None
            self.battle_ice_damage_bonus = None
            self.battle_ice_elemental_resistance = None
            self.battle_water_damage_bonus = None
            self.battle_water_elemental_resistance = None
            self.battle_rock_damage_bonus = None
            self.battle_rock_elemental_resistance = None
            self.battle_physical_damage_bonus = None
            self.battle_physical_elemental_resistance = None
           
            # 参数变更数值保留（回溯用）
            self.temp_battle_max_hp_up = 0
            self.temp_battle_attack_up = 0
            self.temp_battle_extend_attack_up = 0
            self.temp_battle_defance_up = 0
            self.temp_battle_speed_up = 0
            self.temp_battle_critical_rate_up = 0.0
            self.temp_battle_critical_damage_up = 0.0
            self.temp_battle_effect_hitrate_up = 0.0
            self.temp_battle_effect_resistance_up = 0.0
            self.temp_battle_elemental_mastery_up = 0
            self.temp_battle_healing_bonus_up = 0.0
            self.temp_battle_shield_strength_up = 0.0
            self.temp_battle_fire_damage_bonus_up = 0.0
            self.temp_battle_fire_elemental_resistance_up = 0.0
            self.temp_battle_light_damage_bonus_up = 0.0
            self.temp_battle_light_elemental_resistance_up = 0.0
            self.temp_battle_wind_damage_bonus_up = 0.0
            self.temp_battle_wind_elemental_resistance_up = 0.0
            self.temp_battle_ice_damage_bonus_up = 0.0
            self.temp_battle_ice_elemental_resistance_up = 0.0
            self.temp_battle_water_damage_bonus_up = 0.0
            self.temp_battle_water_elemental_resistance_up = 0.0
            self.temp_battle_rock_damage_bonus_up = 0.0
            self.temp_battle_rock_elemental_resistance_up = 0.0
            self.temp_battle_physical_damage_bonus_up = 0.0
            self.temp_battle_physical_elemental_resistance_up = 0.0

            self.temp_battle_max_hp_down = 0
            self.temp_battle_attack_down = 0
            self.temp_battle_extend_attack_down = 0
            self.temp_battle_defance_down = 0
            self.temp_battle_speed_down = 0
            self.temp_battle_critical_rate_down = 0.0
            self.temp_battle_critical_damage_down = 0.0
            self.temp_battle_effect_hitrate_down = 0.0
            self.temp_battle_effect_resistance_down = 0.0
            self.temp_battle_elemental_mastery_down = 0
            self.temp_battle_healing_bonus_down = 0.0
            self.temp_battle_shield_strength_down = 0.0
            self.temp_battle_fire_damage_bonus_down = 0.0
            self.temp_battle_fire_elemental_resistance_down = 0.0
            self.temp_battle_light_damage_bonus_down = 0.0
            self.temp_battle_light_elemental_resistance_down = 0.0
            self.temp_battle_wind_damage_bonus_down = 0.0
            self.temp_battle_wind_elemental_resistance_down = 0.0
            self.temp_battle_ice_damage_bonus_down = 0.0
            self.temp_battle_ice_elemental_resistance_down = 0.0
            self.temp_battle_water_damage_bonus_down = 0.0
            self.temp_battle_water_elemental_resistance_down = 0.0
            self.temp_battle_rock_damage_bonus_down = 0.0
            self.temp_battle_rock_elemental_resistance_down = 0.0
            self.temp_battle_physical_damage_bonus_down = 0.0
            self.temp_battle_physical_elemental_resistance_down = 0.0
            
            # 作用参数
            # 名称
            self.objectname = objectname
            self.original_name = objectname.capitalize().replace("_", " ")
            self.name = name
            # 序号
            self.number = int(number)
            # 协战颜色
            self.support_color = support_color
            self.support_direct = support_direct
            # 表情
            self.face = 'normal'
            self.hitface = hitface
            self.sufferface = sufferface
            self.pose = 'default'
            # 角色显示位置的x坐标
            self.xposition = 0.85
            # 介绍
            self.info = info
            # 等级
            self.level = 1
            # 突破开关
            self.break_through = False
            # 星级
            self.star = int(star)
            self.base_star = self.star
            # 稀有度
            self.rarity = rarity
            # 种族
            self.category = category
            # 金钱（主角）、价格（敌人）
            self.currency = int(currency)
            # 性格
            self.character = ""
            # 好感度
            self.love = 0
            # 心情
            self.mood = 80
            self.mood_changed = 0
            # 名气
            self.famous = 80
            # 隐蔽
            self.hideness = 0
            # 善良值
            self.kindness = 0
            # 威严值
            self.majesty = 0
            # 随性值
            self.casual = 0
            # 薪水
            self.salary = 0
            self.watched = False
            self.salary_changed = False
            # 外出故事标签
            self.has_story = False
            # 隐藏剧情（好感度阈值，label_name）
            self.hiden_story = []
            # 技能
            self.is_phase2 = False
            self.skills = [copy(getattr(store, x)) for x in skills] if skills not in [None, [""]] else []
            self.base_skills = [copy(getattr(store, x)) for x in skills] if skills not in [None, [""]] else []
            self.skills_v2 = [copy(getattr(store, x)) for x in skills_v2] if skills_v2 not in [None, [""]] else [] # 拥有变身技能的角色
            self.base_skills_v2 = [copy(getattr(store, x)) for x in skills_v2] if skills_v2 not in [None, [""]] else []
            self.history_skills = {}
            # 天赋
            self.abilities = abilities if abilities not in [None, [""]] else []
            # 装备
            self.outfits = {
                "武器": None,
                "防具": None,
                "项链": None,
                "戒指": None,
                "法杖": None,
                "宝石": None,
            }
            # 后台装备库
            self.equipments = {
                "武器": [],
                "防具": [],
                "项链": [],
                "戒指": [],
                "法杖": [],
                "宝石": [],
            }
            # 装备经验值
            self.equip_experience = 0
            # 装备4件套效果
            self.equip4effect = None
            # 装备4件套效果描述
            self.equip4effect_info = None
            # 装备4件套效果生效
            self.equip4effect_availabel = True
            # 道具({道具名:数量})
            self.items = {}
            # 经验值
            self.xp = 0.0
            # 行动判定标签
            self.moveable = True
            # 重生标签
            self.soulraise = 0
            # 击杀数标签
            self.defeat = 0
            # 阵亡数标签
            self.be_defeat = 0
            # 增益buff(所有增益buff；内容包括(持续回合数，效果数))
            self.buff = {}
            # 减益buff(所有减益buff)
            self.debuff = {}
            # 元素buff(所有元素buff)
            self.ebuff = {}
            # 选中的技能
            self.selected_skill = self.skills[0] if len(self.skills) > 0 else None
            # 选中的目标
            self.selected_target = None
            # 行动条进度
            self.order = 0.0

        # 判断装备库是否已满
        def is_equipments_full(self, return_cate=False, recall=0):
            is_full = False
            full_cate = None
            for cate, value in self.equipments.items():
                if recall == 10 and len(value) >= 90:
                    is_full = True
                    full_cate = cate
                elif recall != 10 and len(value) >= 99:
                    is_full = True
                    full_cate = cate
                    break

            if return_cate:
                return is_full, full_cate
            else:
                return is_full

        # 数据转移（载入时物件id将会变化，届时render效果无法保存）
        def battle_params_match(self, who):
            # 战斗属性
            # 攻击
            self.attack = who.attack
            self.base_attack = who.base_attack
            self.ori_attack = who.ori_attack
            # 额外攻击
            self.extend_attack = who.extend_attack
            self.base_extend_attack = who.base_extend_attack
            self.ori_extend_attack = who.ori_extend_attack
            # 生命
            self.max_hp = who.max_hp
            self.hp = who.hp
            self.base_max_hp = who.base_max_hp
            self.ori_max_hp = who.ori_max_hp
            # 额外生命
            self.extend_max_hp = who.extend_max_hp
            self.base_extend_max_hp = who.base_extend_max_hp
            self.ori_extend_max_hp = who.ori_extend_max_hp
            # 能量
            self.max_mp = who.max_mp
            self.mp = who.mp
            # 防御
            self.defance = who.defance
            self.base_defance = who.base_defance
            self.ori_defance = who.ori_defance
            # 额外防御
            self.extend_defance = who.extend_defance
            self.base_extend_defance = who.base_extend_defance
            self.ori_extend_defance = who.ori_extend_defance
            # 速度
            self.speed = who.speed
            self.base_speed = who.base_speed
            self.ori_speed = who.ori_speed
            # 暴击率
            self.critical_rate = who.critical_rate
            self.base_critical_rate = who.base_critical_rate
            self.ori_critical_rate = who.ori_critical_rate
            # 暴击伤害
            self.critical_damage = who.critical_damage
            self.base_critical_damage = who.base_critical_damage
            self.ori_critical_damage = who.ori_critical_damage
            # 效果命中
            self.effect_hitrate = who.effect_hitrate
            self.base_effect_hitrate = who.base_effect_hitrate
            self.ori_effect_hitrate = who.ori_effect_hitrate
            # 效果抵抗
            self.effect_resistance = who.effect_resistance
            self.base_effect_resistance = who.base_effect_resistance
            self.ori_effect_resistance = who.ori_effect_resistance
            # 元素精通
            self.elemental_mastery = who.elemental_mastery
            self.base_elemental_mastery = who.base_elemental_mastery
            self.ori_elemental_mastery = who.ori_elemental_mastery
            # 治疗加成
            self.healing_bonus = who.healing_bonus
            self.base_healing_bonus = who.base_healing_bonus
            self.ori_healing_bonus = who.ori_healing_bonus
            # 护盾强度
            self.shield_strength = who.shield_strength
            self.base_shield_strength = who.base_shield_strength
            self.ori_shield_strength = who.ori_shield_strength
            # 火元素伤害加成
            self.fire_damage_bonus = who.fire_damage_bonus
            self.base_fire_damage_bonus = who.base_fire_damage_bonus
            self.ori_fire_damage_bonus = who.ori_fire_damage_bonus
            # 火元素抗性
            self.fire_elemental_resistance = who.fire_elemental_resistance
            self.base_fire_elemental_resistance = who.base_fire_elemental_resistance
            self.ori_fire_elemental_resistance = who.ori_fire_elemental_resistance
            # 雷元素伤害加成
            self.light_damage_bonus = who.light_damage_bonus
            self.base_light_damage_bonus = who.base_light_damage_bonus
            self.ori_light_damage_bonus = who.ori_light_damage_bonus
            # 雷元素抗性
            self.light_elemental_resistance = who.light_elemental_resistance
            self.base_light_elemental_resistance = who.base_light_elemental_resistance
            self.ori_light_elemental_resistance = who.ori_light_elemental_resistance
            # 风元素伤害加成
            self.wind_damage_bonus = who.wind_damage_bonus
            self.base_wind_damage_bonus = who.base_wind_damage_bonus
            self.ori_wind_damage_bonus = who.ori_wind_damage_bonus
            # 风元素抗性
            self.wind_elemental_resistance = who.wind_elemental_resistance
            self.base_wind_elemental_resistance = who.base_wind_elemental_resistance
            self.ori_wind_elemental_resistance = who.ori_wind_elemental_resistance
            # 冰元素伤害加成
            self.ice_damage_bonus = who.ice_damage_bonus
            self.base_ice_damage_bonus = who.base_ice_damage_bonus
            self.ori_ice_damage_bonus = who.ori_ice_damage_bonus
            # 冰元素抗性
            self.ice_elemental_resistance = who.ice_elemental_resistance
            self.base_ice_elemental_resistance = who.base_ice_elemental_resistance
            self.ori_ice_elemental_resistance = who.ori_ice_elemental_resistance
            # 水元素伤害加成
            self.water_damage_bonus = who.water_damage_bonus
            self.base_water_damage_bonus = who.base_water_damage_bonus
            self.ori_water_damage_bonus = who.ori_water_damage_bonus
            # 水元素抗性
            self.water_elemental_resistance = who.water_elemental_resistance
            self.base_water_elemental_resistance = who.base_water_elemental_resistance
            self.ori_water_elemental_resistance = who.ori_water_elemental_resistance
            # 岩元素伤害加成
            self.rock_damage_bonus = who.rock_damage_bonus
            self.base_rock_damage_bonus = who.base_rock_damage_bonus
            self.ori_rock_damage_bonus = who.ori_rock_damage_bonus
            # 岩元素抗性
            self.rock_elemental_resistance = who.rock_elemental_resistance
            self.base_rock_elemental_resistance = who.base_rock_elemental_resistance
            self.ori_rock_elemental_resistance = who.ori_rock_elemental_resistance
            # 物理伤害加成
            self.physical_damage_bonus = who.physical_damage_bonus
            self.base_physical_damage_bonus = who.base_physical_damage_bonus
            self.ori_physical_damage_bonus = who.ori_physical_damage_bonus
            # 物理抗性
            self.physical_elemental_resistance = who.physical_elemental_resistance
            self.base_physical_elemental_resistance = who.base_physical_elemental_resistance
            self.ori_physical_elemental_resistance = who.ori_physical_elemental_resistance
            
            # 等级
            self.level = who.level
            # 突破开关
            self.break_through = who.break_through
            # 星级
            self.star = who.star
            self.base_star = who.base_star
            # 金钱（主角）、价格（敌人）
            self.currency = who.currency
            # 性格
            self.character = who.character
            # 好感度
            self.love = who.love
            # 心情
            self.mood = who.mood
            self.mood_changed = who.mood_changed
            # 名气
            self.famous = who.famous
            # 隐蔽
            self.hideness = who.hideness
            # 善良值
            self.kindness = who.kindness
            # 威严值
            self.majesty = who.majesty
            # 随性值
            self.casual = who.casual
            # 薪水
            self.salary = who.salary
            self.watched = who.watched
            self.salary_changed = who.salary_changed
            # 外出故事标签
            self.has_story = who.has_story
            # 隐藏剧情（好感度阈值，label_name）
            self.hiden_story = who.hiden_story
            # 技能
            self.is_phase2 = who.is_phase2
            self.skills = who.skills
            self.base_skills = who.base_skills
            self.skills_v2 = who.skills_v2
            self.base_skills_v2 = who.base_skills_v2
            self.history_skills = who.history_skills
            # 天赋
            self.abilities = who.abilities
            # 装备
            self.outfits = who.outfits
            # 后台装备库
            self.equipments = who.equipments
            # 装备经验值
            self.equip_experience = who.equip_experience
            # 装备4件套效果
            self.equip4effect = who.equip4effect
            # 装备4件套效果描述
            self.equip4effect_info = who.equip4effect_info
            # 装备4件套效果生效
            self.equip4effect_availabel = who.equip4effect_availabel
            # 道具({道具名:数量})
            self.items = who.items
            # 经验值
            self.xp = who.xp
            # 行动判定标签
            self.moveable = who.moveable
            # 重生标签
            self.soulraise = who.soulraise
            # 击杀数标签
            self.defeat = who.defeat
            # 阵亡数标签
            self.be_defeat = who.be_defeat
            # 增益buff(所有增益buff；内容包括(持续回合数，效果数))
            self.buff = who.buff
            # 减益buff(所有减益buff)
            self.debuff = who.debuff
            # 元素buff(所有元素buff)
            self.ebuff = who.ebuff
            # 选中的技能
            self.selected_skill = who.selected_skill
            # 选中的目标
            self.selected_target = who.selected_target
            # 行动条进度
            self.order = who.order

        # 战斗时使用的临时变化属性
        def mirror_params(self):
            self.battle_max_hp = self.max_hp + self.extend_max_hp
            self.battle_attack = self.attack
            self.battle_extend_attack = self.extend_attack
            self.battle_defance = self.defance
            self.battle_extend_defance = self.extend_defance
            self.battle_speed = self.speed
            self.battle_critical_rate = self.critical_rate
            self.battle_critical_damage = self.critical_damage
            self.battle_effect_hitrate = self.effect_hitrate
            self.battle_effect_resistance = self.effect_resistance
            self.battle_elemental_mastery = self.elemental_mastery
            self.battle_healing_bonus = self.healing_bonus
            self.battle_shield_strength = self.shield_strength
            self.battle_fire_damage_bonus = self.fire_damage_bonus
            self.battle_fire_elemental_resistance = self.fire_elemental_resistance
            self.battle_light_damage_bonus = self.light_damage_bonus
            self.battle_light_elemental_resistance = self.light_elemental_resistance
            self.battle_wind_damage_bonus = self.wind_damage_bonus
            self.battle_wind_elemental_resistance = self.wind_elemental_resistance
            self.battle_ice_damage_bonus = self.ice_damage_bonus
            self.battle_ice_elemental_resistance = self.ice_elemental_resistance
            self.battle_water_damage_bonus = self.water_damage_bonus
            self.battle_water_elemental_resistance = self.water_elemental_resistance
            self.battle_rock_damage_bonus = self.rock_damage_bonus
            self.battle_rock_elemental_resistance = self.rock_elemental_resistance
            self.battle_physical_damage_bonus = self.physical_damage_bonus
            self.battle_physical_elemental_resistance = self.physical_elemental_resistance

        def equip_params_rollback(self):
            self.max_hp = self.base_max_hp
            self.extend_max_hp = self.base_extend_max_hp
            self.attack = self.base_attack
            self.extend_attack = self.base_extend_attack
            self.defance = self.base_defance
            self.extend_defance = self.base_extend_defance
            self.speed = self.base_speed
            self.critical_rate = self.base_critical_rate
            self.critical_damage = self.base_critical_damage
            self.effect_hitrate = self.base_effect_hitrate
            self.effect_resistance = self.base_effect_resistance
            self.elemental_mastery = self.base_elemental_mastery
            self.healing_bonus = self.base_healing_bonus
            self.shield_strength = self.base_shield_strength
            self.fire_damage_bonus = self.base_fire_damage_bonus
            self.fire_elemental_resistance = self.base_fire_elemental_resistance
            self.light_damage_bonus = self.base_light_damage_bonus
            self.light_elemental_resistance = self.base_light_elemental_resistance
            self.wind_damage_bonus = self.base_wind_damage_bonus
            self.wind_elemental_resistance = self.base_wind_elemental_resistance
            self.ice_damage_bonus = self.base_ice_damage_bonus
            self.ice_elemental_resistance = self.base_ice_elemental_resistance
            self.water_damage_bonus = self.base_water_damage_bonus
            self.water_elemental_resistance = self.base_water_elemental_resistance
            self.rock_damage_bonus = self.base_rock_damage_bonus
            self.rock_elemental_resistance = self.base_rock_elemental_resistance
            self.physical_damage_bonus = self.base_physical_damage_bonus
            self.physical_elemental_resistance = self.base_physical_elemental_resistance
            self.equip4effect = None
            self.equip4effect_info = None

        # buff属性回溯
        def back_param(self, name, reset=True):
            if name == "weak":
                self.battle_extend_attack += self.temp_battle_extend_attack_down
                if reset:
                    self.temp_battle_extend_attack_down = 0
            elif name == "strong":
                self.battle_extend_attack -= self.temp_battle_extend_attack_up
                if reset:
                    self.temp_battle_extend_attack_up = 0
            elif name == "exposed":
                self.battle_extend_defance += self.temp_battle_defance_down
                if reset:
                    self.temp_battle_defance_down = 0
            elif name == "sturdy":
                self.battle_extend_defance -= self.temp_battle_defance_up
                if reset:
                    self.temp_battle_defance_up = 0
            elif name == "slow":
                self.battle_speed += self.temp_battle_speed_down
                if reset:
                    self.temp_battle_speed_down = 0
            elif name == "flow":
                self.battle_speed -= self.temp_battle_speed_up
                if reset:
                    self.temp_battle_speed_up = 0
            elif name == "powerless":
                self.battle_critical_rate += self.temp_battle_critical_rate_down
                self.battle_critical_damage += self.temp_battle_critical_damage_down
                if reset:
                    self.temp_battle_critical_rate_down = 0.0
                    self.temp_battle_critical_damage_down = 0.0
            elif name == "violence":
                self.battle_critical_rate -= self.temp_battle_critical_rate_up
                self.battle_critical_damage -= self.temp_battle_critical_damage_up
                if reset:
                    self.temp_battle_critical_rate_up = 0.0
                    self.temp_battle_critical_damage_up = 0.0
            elif name == "seal":
                self.battle_effect_hitrate += self.temp_battle_effect_hitrate_down
                if reset:
                    self.temp_battle_effect_hitrate_down = 0.0
            elif name == "liberate":
                self.battle_effect_hitrate -= self.temp_battle_effect_hitrate_up
                if reset:
                    self.temp_battle_effect_hitrate_up = 0.0
            elif name == "disintegrate":
                self.battle_effect_resistance += self.temp_battle_effect_resistance_down
                if reset:
                    self.temp_battle_effect_resistance_down = 0.0
            elif name == "barrier":
                self.battle_effect_resistance -= self.temp_battle_effect_resistance_up
                if reset:
                    self.temp_battle_effect_resistance_up = 0.0
            elif name == "churn":
                self.battle_elemental_mastery += self.temp_battle_elemental_mastery_down
                if reset:
                    self.temp_battle_elemental_mastery_down = 0
            elif name == "master":
                self.battle_elemental_mastery -= self.temp_battle_elemental_mastery_up
                if reset:
                    self.temp_battle_elemental_mastery_up = 0
            elif name == "handicapped":
                self.battle_healing_bonus += self.temp_battle_healing_bonus_down
                if reset:
                    self.temp_battle_healing_bonus_down = 0.0
            elif name == "healing":
                self.battle_healing_bonus -= self.temp_battle_healing_bonus_up
                if reset:
                    self.temp_battle_healing_bonus_up = 0.0
            elif name == "broken":
                self.battle_shield_strength += self.temp_battle_shield_strength_down
                if reset:
                    self.temp_battle_shield_strength_down = 0.0
            elif name == "armor":
                self.battle_shield_strength -= self.temp_battle_shield_strength_up
                if reset:
                    self.temp_battle_shield_strength_up = 0.0
            elif name == "withered":
                self.battle_fire_damage_bonus += self.temp_battle_fire_damage_bonus_down
                self.battle_light_damage_bonus += self.temp_battle_light_damage_bonus_down
                self.battle_wind_damage_bonus += self.temp_battle_wind_damage_bonus_down
                self.battle_ice_damage_bonus += self.temp_battle_ice_damage_bonus_down
                self.battle_water_damage_bonus += self.temp_battle_water_damage_bonus_down
                self.battle_rock_damage_bonus += self.temp_battle_rock_damage_bonus_down
                self.battle_physical_damage_bonus += self.temp_battle_physical_damage_bonus_down
                if reset:
                    self.temp_battle_fire_damage_bonus_down = 0.0
                    self.temp_battle_light_damage_bonus_down = 0.0
                    self.temp_battle_wind_damage_bonus_down = 0.0
                    self.temp_battle_ice_damage_bonus_down = 0.0
                    self.temp_battle_water_damage_bonus_down = 0.0
                    self.temp_battle_rock_damage_bonus_down = 0.0
                    self.temp_battle_physical_damage_bonus_down = 0.0
            elif name == "condensed":
                self.battle_fire_damage_bonus -= self.temp_battle_fire_damage_bonus_up
                self.battle_light_damage_bonus -= self.temp_battle_light_damage_bonus_up
                self.battle_wind_damage_bonus -= self.temp_battle_wind_damage_bonus_up
                self.battle_ice_damage_bonus -= self.temp_battle_ice_damage_bonus_up
                self.battle_water_damage_bonus -= self.temp_battle_water_damage_bonus_up
                self.battle_rock_damage_bonus -= self.temp_battle_rock_damage_bonus_up
                self.battle_physical_damage_bonus -= self.temp_battle_physical_damage_bonus_up
                if reset:
                    self.temp_battle_fire_damage_bonus_up = 0.0
                    self.temp_battle_light_damage_bonus_up = 0.0
                    self.temp_battle_wind_damage_bonus_up = 0.0
                    self.temp_battle_ice_damage_bonus_up = 0.0
                    self.temp_battle_water_damage_bonus_up = 0.0
                    self.temp_battle_rock_damage_bonus_up = 0.0
                    self.temp_battle_physical_damage_bonus_up = 0.0
            elif name == "suppress":
                self.battle_fire_elemental_resistance += self.temp_battle_fire_elemental_resistance_down
                self.battle_light_elemental_resistance += self.temp_battle_light_elemental_resistance_down
                self.battle_wind_elemental_resistance += self.temp_battle_wind_elemental_resistance_down
                self.battle_ice_elemental_resistance += self.temp_battle_ice_elemental_resistance_down
                self.battle_water_elemental_resistance += self.temp_battle_water_elemental_resistance_down
                self.battle_rock_elemental_resistance += self.temp_battle_rock_elemental_resistance_down
                self.battle_physical_elemental_resistance += self.temp_battle_physical_elemental_resistance_down
                if reset:
                    self.temp_battle_fire_elemental_resistance_down = 0.0
                    self.temp_battle_light_elemental_resistance_down = 0.0
                    self.temp_battle_wind_elemental_resistance_down = 0.0
                    self.temp_battle_ice_elemental_resistance_down = 0.0
                    self.temp_battle_water_elemental_resistance_down = 0.0
                    self.temp_battle_rock_elemental_resistance_down = 0.0
                    self.temp_battle_physical_elemental_resistance_down = 0.0
            elif name == "control":
                self.battle_fire_elemental_resistance -= self.temp_battle_fire_elemental_resistance_up
                self.battle_light_elemental_resistance -= self.temp_battle_light_elemental_resistance_up
                self.battle_wind_elemental_resistance -= self.temp_battle_wind_elemental_resistance_up
                self.battle_ice_elemental_resistance -= self.temp_battle_ice_elemental_resistance_up
                self.battle_water_elemental_resistance -= self.temp_battle_water_elemental_resistance_up
                self.battle_rock_elemental_resistance -= self.temp_battle_rock_elemental_resistance_up
                self.battle_physical_elemental_resistance -= self.temp_battle_physical_elemental_resistance_up
                if reset:
                    self.temp_battle_fire_elemental_resistance_up = 0.0
                    self.temp_battle_light_elemental_resistance_up = 0.0
                    self.temp_battle_wind_elemental_resistance_up = 0.0
                    self.temp_battle_ice_elemental_resistance_up = 0.0
                    self.temp_battle_water_elemental_resistance_up = 0.0
                    self.temp_battle_rock_elemental_resistance_up = 0.0
                    self.temp_battle_physical_elemental_resistance_up = 0.0

        # 装备数值重新计算
        def equip_recalculate(self):
            # 对所有的装备重新计算属性增益
            # step1：先回复所有已装备道具的属性加成
            self.equip_params_rollback()
            self.hp = self.max_hp + self.extend_max_hp

            # step2：对现有的装备重新计算加成
            # 百分比最后统计
            ratio_parts = {}
            equip_effect_count = {}
            
            for name, equip in self.outfits.items():
                if equip is not None:
                    # 套装数量统计
                    this_kind = equip.objectname.split("_")[1]
                    if this_kind not in equip_effect_count:
                        equip_effect_count[this_kind] = (1, equip.double_effect, equip.forth_effect)
                    else:
                        num, obj1, obj2 = equip_effect_count[this_kind]
                        equip_effect_count[this_kind] = (num + 1, obj1, obj2)

                    # 主属性
                    for name, number in equip.prime_attribute.items():
                        # 获得对应主属性设定
                        tmp_prime_attribute = None
                        for key, value in outfit_attributes.items():
                            if value["name"] == name:
                                tmp_prime_attribute = key
                                break

                        # 百分比属性记录下来比例
                        if "_ratio" in tmp_prime_attribute:
                            ori_params = tmp_prime_attribute.split("_ratio")[0]
                            # attack|max_hp|defance
                            if ori_params not in ratio_parts:
                                ratio_parts[ori_params] = number
                            else:
                                ratio_parts[ori_params] += number
                        # 数值属性直接加上
                        else:
                            self.attr_change(tmp_prime_attribute, number, change_base=False)

                    # 副属性
                    for name, number in equip.minor_attributes.items():
                        # 获得对应副属性设定
                        tmp_minor_attribute = None
                        for key, value in outfit_attributes.items():
                            if value["name"] == name:
                                tmp_minor_attribute = key
                                break

                        # 百分比属性
                        if "_ratio" in tmp_minor_attribute:
                            ori_params = tmp_minor_attribute.split("_ratio")[0]
                            # attack|max_hp|defance
                            if ori_params not in ratio_parts:
                                ratio_parts[ori_params] = number
                            else:
                                ratio_parts[ori_params] += number
                        # 数值属性
                        else:
                            self.attr_change(tmp_minor_attribute, number, change_base=False)

            # 装备二、四件套属性激活
            for kind, (count, double_effects, forth_effects) in equip_effect_count.items():
                if count >= 4:
                    ef_name, ef_ratio, ef_info = double_effects
                    if ef_name in ["attack", "defance", "max_hp"]:
                        if ef_name not in ratio_parts:
                            ratio_parts[ef_name] = ef_ratio
                        else:
                            ratio_parts[ef_name] += ef_ratio
                    else:
                        self.attr_change(ef_name, ef_ratio, change_base=False)

                    ef_name, ef_info = forth_effects
                    self.equip4effect = ef_name
                    self.equip4effect_info = ef_info
                elif count >= 2:
                    ef_name, ef_ratio, ef_info = double_effects
                    if ef_name in ["attack", "defance", "max_hp"]:
                        if ef_name not in ratio_parts:
                            ratio_parts[ef_name] = ef_ratio
                        else:
                            ratio_parts[ef_name] += ef_ratio
                    else:
                        self.attr_change(ef_name, ef_ratio, change_base=False)

            # 最后计算所有装备的比例加成
            if len(ratio_parts) != 0:
                for name, ratio in ratio_parts.items():
                    if name == "attack":
                        self.attr_change("extend_attack", ratio * self.attack, change_base=False)
                    elif name == "max_hp":
                        self.attr_change("extend_max_hp", ratio * self.max_hp, change_base=False)
                    elif name == "defance":
                        self.attr_change("extend_defance", ratio * self.defance, change_base=False)
            self.hp = self.max_hp + self.extend_max_hp

        # 技能升级
        def skill_levelup(self, change_log=True):
            # 随机获取升级的技能
            canup_skills = []
            canup_skills_v2 = []
            if len(self.skills_v2) > 0:
                for s, s2 in zip(self.skills, self.skills_v2):
                    if s.level < s.max_level and s2.level < s2.max_level:
                        canup_skills.append(s)
                        canup_skills_v2.append(s2)
            else:
                for s in self.skills:
                    if s.level < s.max_level:
                        canup_skills.append(s)
            if len(canup_skills) == 0:
                return

            select_index = renpy.random.randint(0, len(canup_skills) - 1)
            select_up_skill = canup_skills[select_index]
            select_up_skill.level_change(select_up_skill.level + 1)

            # 替换当前的技能v1和v2、以及base备份
            if change_log:
                self.base_skills = copy(self.skills)
            
            if len(canup_skills_v2) > 0:
                # 修改skills_v2
                select_up_skill_v2 = canup_skills_v2[select_index]
                select_up_skill_v2.level_change(select_up_skill_v2.level + 1)
                if change_log:
                    self.base_skills_v2 = copy(self.skills_v2)

            return select_up_skill

        # 设置战斗等级
        def stats_check(self, to_level, limit=True, break_through=True):
            if to_level <= self.level:
                return

            while self.level < to_level:
                # 等级小于20正常成长
                if self.level < 20:
                    # 攻击成长
                    self.attack *= 1.0571
                    self.base_attack = self.attack
                    # 生命成长
                    self.max_hp *= 1.0456
                    self.base_max_hp = self.max_hp
                    self.hp = self.max_hp
                    # 防御成长
                    self.defance *= 1.0227
                    self.base_defance = self.defance
                    self.level += 1
                # 到了突破判定升星
                elif self.level < 40 and self.level % 5 == 0 and not self.break_through:
                    # 攻击成长
                    self.attack *= 1.28
                    self.base_attack = self.attack
                    # 生命成长
                    self.max_hp *= 1.17
                    self.base_max_hp = self.max_hp
                    self.hp = self.max_hp
                    # 防御成长
                    self.defance *= 1.25
                    self.base_defance = self.defance
                    # 主属性成长
                    # 成长区间
                    grow_up = {
                        "生命值加成": ("max_hp", 0.06),
                        "治疗加成": ("healing_bonus", 0.05),
                        "防御力加成": ("defance", 0.08),
                        "攻击力加成": ("attack", 0.06),
                        "元素精通": ("elemental_mastery", 24),
                        "暴击率": ("critical_rate", 0.05),
                        "暴击伤害": ("critical_damage", 0.09),
                        "火元素伤害加成": ("fire_damage_bonus", 0.07),
                        "雷元素伤害加成": ("light_damage_bonus", 0.07),
                        "水元素伤害加成": ("water_damage_bonus", 0.07),
                        "冰元素伤害加成": ("ice_damage_bonus", 0.07),
                        "风元素伤害加成": ("wind_damage_bonus", 0.07),
                        "岩元素伤害加成": ("rock_damage_bonus", 0.07),
                    }
                    if self.prime_attribute is not None and self.prime_attribute in grow_up:
                        params_name, ratio_number = grow_up[self.prime_attribute]

                        # 攻击力/防御力/生命值
                        if self.prime_attribute in ["生命加成", "防御力加成", "攻击力加成"]:
                            ori_prime_attribute = getattr(self, params_name)
                            new_prime_attribute = getattr(self, "extend_" + params_name)
                            base_new_prime_attribute = getattr(self, "base_extend_" + params_name)
                            setattr(self, "extend_" + params_name, new_prime_attribute + ori_prime_attribute * ratio_number)
                            setattr(self, "base_extend_" + params_name, base_new_prime_attribute + ori_prime_attribute * ratio_number)
                            self.hp = self.max_hp
                        else:
                            ori_prime_attribute = getattr(self, params_name)
                            base_ori_prime_attribute = getattr(self, "base_" + params_name)
                            setattr(self, params_name, ori_prime_attribute + ratio_number)
                            setattr(self, "base_" + params_name, base_ori_prime_attribute + ratio_number)

                    # 星级增加
                    self.break_through = True
                    self.star += 1
                # 否则正常成长
                else:
                    if limit:
                        if self.level < 40:
                            # 攻击成长
                            self.attack *= 1.0571
                            self.base_attack = self.attack
                            # 生命成长
                            self.max_hp *= 1.0456
                            self.base_max_hp = self.max_hp
                            self.hp = self.max_hp
                            # 防御成长
                            self.defance *= 1.0227
                            self.base_defance = self.defance
                            self.level += 1
                            self.break_through = False
                        else:
                            return
                    else:
                        # 攻击成长
                        self.attack *= 1.0571
                        self.base_attack = self.attack
                        # 生命成长
                        self.max_hp *= 1.0456
                        self.base_max_hp = self.max_hp
                        self.hp = self.max_hp
                        # 防御成长
                        self.defance *= 1.0227
                        self.base_defance = self.defance
                        self.level += 1
                        self.break_through = False

            if break_through and self.level >= 20 and self.level < 40 and to_level % 5 == 0 and not self.break_through:
                # 攻击成长
                self.attack *= 1.28
                self.base_attack = self.attack
                # 生命成长
                self.max_hp *= 1.17
                self.base_max_hp = self.max_hp
                self.hp = self.max_hp
                # 防御成长
                self.defance *= 1.25
                self.base_defance = self.defance
                # 星级增加
                self.break_through = True
                self.star += 1
            
            # if self.level <= 20 and not self.break_through:
            #     self.star = 1
            # elif self.level >= 20 and self.break_through:
            #     self.star = 2
            # elif self.level >= 25 and self.break_through:
            #     self.star = 3
            # elif self.level >= 30 and self.break_through:
            #     self.star = 4
            # elif self.level >= 35 and self.break_through:
            #     self.star = 5
            # else:
            #     self.star = 5

            self.attack = int(self.attack)
            self.max_hp = int(self.max_hp)
            self.hp = self.max_hp
            self.defance = int(self.defance)

            self.equip_recalculate()

            return
        
        # 等级提升属性更新
        def level_up(self):
            if self.level >= 40:
                return

            to_level = self.level + 1
            
            # 升级所需的经验值
            # 偶数
            if self.level % 2 == 0:
                level_up_exp = 2.5 * math.pow(self.level, 3) + 22.5 * math.pow(self.level, 2) - 10 * self.level + 150
            # 奇数
            else:
                level_up_exp = 2.5 * math.pow(self.level, 3) + 25 * math.pow(self.level, 2) - 12.5 * self.level + 165

            # 突破材料个数
            breakout_quest = {
                "20": (5, 0),
                "25": (8, 4),
                "30": (15, 8),
                "35": (30, 15)
            }
            if str(self.level) in breakout_quest:
                total_need_small, total_need_large = breakout_quest[str(self.level)]

                # 获取角色属性
                role_max_element_resistance = 0
                role_element = None
                for element in ["fire", "water", "ice", "light", "wind", "rock"]:
                    role_attribute_number = getattr(self, "ori_" + element + "_elemental_resistance")
                    if role_attribute_number > role_max_element_resistance:
                        role_max_element_resistance = role_attribute_number
                        role_element = element

                item_small_count, item_large_count = 0, 0
                item_name_small = role_element + "_break_small"
                item_name_large = role_element + "_break_large"
                if item_name_small in local_config.player.items:
                    item_small_count = local_config.player.items[item_name_small]
                if item_name_large in local_config.player.items:
                    item_large_count = local_config.player.items[item_name_large]

            # 等级小于20正常成长
            if self.level < 20:
                if self.xp >= level_up_exp:
                    # 攻击成长
                    self.attack *= 1.0571
                    self.base_attack = self.attack
                    # 生命成长
                    self.max_hp *= 1.0456
                    self.base_max_hp = self.max_hp
                    self.hp = self.max_hp
                    # 防御成长
                    self.defance *= 1.0227
                    self.base_defance = self.defance

                    self.xp -= level_up_exp
                    renpy.music.play("level_up", channel="battle_music")
                    self.level = to_level
                else:
                    return
            # 到了突破判定
            elif self.level % 5 == 0:
                # 突破，例如20->20升星
                if not self.break_through:
                    if item_small_count >= total_need_small and item_large_count >= total_need_large:
                        # 攻击成长
                        self.attack *= 1.28
                        self.base_attack = self.attack
                        # 生命成长
                        self.max_hp *= 1.17
                        self.base_max_hp = self.max_hp
                        self.hp = self.max_hp
                        # 防御成长
                        self.defance *= 1.25
                        self.base_defance = self.defance

                        # 主属性成长
                        # 成长区间
                        grow_up = {
                            "生命值加成": ("max_hp", 0.06),
                            "治疗加成": ("healing_bonus", 0.05),
                            "防御力加成": ("defance", 0.08),
                            "攻击力加成": ("attack", 0.06),
                            "元素精通": ("elemental_mastery", 24),
                            "暴击率": ("critical_rate", 0.05),
                            "暴击伤害": ("critical_damage", 0.09),
                            "火元素伤害加成": ("fire_damage_bonus", 0.07),
                            "雷元素伤害加成": ("light_damage_bonus", 0.07),
                            "水元素伤害加成": ("water_damage_bonus", 0.07),
                            "冰元素伤害加成": ("ice_damage_bonus", 0.07),
                            "风元素伤害加成": ("wind_damage_bonus", 0.07),
                            "岩元素伤害加成": ("rock_damage_bonus", 0.07),
                        }
                        if self.prime_attribute is not None and self.prime_attribute in grow_up:
                            params_name, ratio_number = grow_up[self.prime_attribute]

                            # 攻击力/防御力/生命值
                            if self.prime_attribute in ["生命加成", "防御力加成", "攻击力加成"]:
                                ori_prime_attribute = getattr(self, params_name)
                                new_prime_attribute = getattr(self, "extend_" + params_name)
                                base_new_prime_attribute = getattr(self, "base_extend_" + params_name)
                                setattr(self, "extend_" + params_name, new_prime_attribute + ori_prime_attribute * ratio_number)
                                setattr(self, "base_extend_" + params_name, base_new_prime_attribute + ori_prime_attribute * ratio_number)
                                self.hp = self.max_hp
                            else:
                                ori_prime_attribute = getattr(self, params_name)
                                base_ori_prime_attribute = getattr(self, "base_" + params_name)
                                setattr(self, params_name, ori_prime_attribute + ratio_number)
                                setattr(self, "base_" + params_name, base_ori_prime_attribute + ratio_number)

                        self.star += 1
                        self.break_through = True
                        
                        if total_need_small != 0:
                            local_config.player.items[item_name_small] -= total_need_small
                            if local_config.player.items[item_name_small] == 0:
                                local_config.player.items.pop(item_name_small)
                        if total_need_large != 0:
                            local_config.player.items[item_name_large] -= total_need_large
                            if local_config.player.items[item_name_large] == 0:
                                local_config.player.items.pop(item_name_large)
                # 升级，例如20->21升级
                else:
                    if self.xp >= level_up_exp:
                        # 攻击成长
                        self.attack *= 1.0571
                        self.base_attack = self.attack
                        # 生命成长
                        self.max_hp *= 1.0456
                        self.base_max_hp = self.max_hp
                        self.hp = self.max_hp
                        # 防御成长
                        self.defance *= 1.0227
                        self.base_defance = self.defance

                        self.xp -= level_up_exp
                        renpy.music.play("level_up", channel="battle_music")
                        self.level = to_level
                    else:
                        return
            else:
                # 升级，例如23->24升级
                if self.xp >= level_up_exp:
                    # 攻击成长
                    self.attack *= 1.0571
                    self.base_attack = self.attack
                    # 生命成长
                    self.max_hp *= 1.0456
                    self.base_max_hp = self.max_hp
                    self.hp = self.max_hp
                    # 防御成长
                    self.defance *= 1.0227
                    self.base_defance = self.defance

                    self.xp -= level_up_exp
                    renpy.music.play("level_up", channel="battle_music")
                    self.level = to_level
                else:
                    return

            self.attack = int(round(self.attack))
            self.max_hp = int(round(self.max_hp))
            self.hp = self.max_hp
            self.defance = int(round(self.defance))
            self.xp = int(self.xp)

            self.equip_recalculate()

            return

        # 表情替换
        def face_change(self, hit=False, hitted=False):
            if config.skipping and config.skip_delay <= 5:
                return

            disable = False
            for debuff in self.debuff:
                if debuff in ["confusion", "dizziness", "frozen", "sleepy", "ridicule"]:
                    disable = True
                    break
                
            # hitface：发起攻击时
            if hit:
                self.face = self.hitface
            # sufferface:被攻击时、阵亡时、受到无法行动的buff时
            elif hitted or self.hp < 1 or disable:
                self.face = self.sufferface
            # 其他时候为normal
            else:
                self.face = "normal"

            return

        # 角色候补
        def order_change(self):
            # 角色阵亡
            if self.hp < 1:
                renpy.music.play("Click_Disabled_Button", channel="battle_music")
                renpy.hide_screen("message_screen")
                renpy.show_screen("alt_notify", message=_("HP为0的角色无法进行更换。"))
                local_config.chosen_actor = None
            else:
                if local_config.chosen_actor == None:
                    local_config.chosen_actor = self
                    renpy.show_screen("message_screen", message=_("请选择一个有效的目标。"))
                else:
                    for i in xrange(len(local_config.party)):
                        if local_config.party[i] == self:
                            local_config.party[i] = local_config.chosen_actor
                        elif local_config.party[i] == local_config.chosen_actor:
                            local_config.party[i] = self
                    local_config.chosen_actor = None
                    renpy.hide_screen("message_screen")
                    renpy.show_screen("alt_notify", message=_("角色更换成功。"))

        # 换人
        def member_change(self, target, ally_environment_effects=None, in_battle=False, reborn=False, show_role=True, order_members=None):
            if not reborn:
                renpy.hide(target.objectname, layer="fg")
                # 继承行动条
                self.order = target.order

            for i in xrange(len(local_config.party)):
                if local_config.party[i] == self:
                    local_config.party[i] = target
                elif local_config.party[i] == target:
                    local_config.party[i]= self
  
            if in_battle:
                if not reborn:
                    ## target离场计算
                    ## ---- For Target ----
                    ## 全局效果消除
                    # 被动技能
                    role_select_skills = target.base_skills if not target.is_phase2 else target.base_skills_v2
                    passive_skill = [s for s in role_select_skills if s.category == "Passive"][0]
                    if (passive_skill.name, True) in ally_environment_effects:
                        ally_environment_effects.remove((passive_skill.name, True))
                    elif (passive_skill.name, False) in ally_environment_effects:
                        ally_environment_effects.remove((passive_skill.name, False))

                    # 装备4件套
                    if (target.equip4effect, True) in ally_environment_effects:
                        ally_environment_effects.remove((target.equip4effect, True))
                    elif (target.equip4effect, False) in ally_environment_effects:
                        ally_environment_effects.remove((target.equip4effect, False))

                    # 雪特效
                    if target.name == "希菲尔":
                        remove_snow = True
                        for role in local_config.party[:3] + local_config.enemy[:3]:
                            if role != target and role.name == "希菲尔" and role.hp > 0:
                                remove_snow = False
                                break
                        if remove_snow:
                            renpy.hide("snow_level1", layer="fg_f")

                    # 殇魂消除
                    if "魂之殇" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["魂之殇"]
                        fake_buff_roles = copy(buff_roles)
                        for (u, t) in fake_buff_roles:
                            # 使用者换下时解除buff效果
                            if target == u:
                                temp_buff_roles = buff_roles.pop((u, t))
                                # 清空“殇魂”debuff
                                buff_obj = getattr(store, "desoul_lock")
                                buff_obj.calculate(t, None, None, None, "clean")

                                for role, (dmg, dtype) in temp_buff_roles.items():
                                    # 为角色清空“殇魂”buff
                                    buff_obj = getattr(store, "soul_lock")
                                    buff_obj.calculate(role, None, None, None, "clean")
                        if len(local_config.skill_log_data["魂之殇"]) == 0:
                            local_config.skill_log_data.pop("魂之殇")
                    # 若为咒的目标则消除咒术
                    if "咒" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["咒"]
                        if target in buff_roles:
                            flag, dmg, dtype, other = buff_roles[target]
                            if dtype == "user":
                                for role, (flag, dmg, dtype, other) in buff_roles.items():
                                    if dtype == "user":
                                        buff_obj = getattr(store, "curse")
                                        buff_obj.calculate(role, None, None, None, "clean")
                                    elif dtype == "target":
                                        buff_obj = getattr(store, "decurse")
                                        buff_obj.calculate(role, None, None, None, "clean")
                            else:
                                renpy.music.play("Click_Disabled_Button", channel="battle_music")
                                renpy.show_screen("alt_notify", _("被「咒」选中的角色无法替换。"))
                    # 消除自己庇护下成员的星桥状态
                    if "星空梦影" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["星空梦影"]
                        # 清空user为self的所有buff
                        is_user = False
                        for role, (flag, buff_user) in buff_roles.items():
                            if target == buff_user:
                                is_user = True
                                # buff解除
                                if "star_bridge" in role.buff:
                                    buff_obj = getattr(store, "star_bridge")
                                    buff_obj.calculate(role, None, None, None, "clean")
                                elif "star_bridge_done" in role.buff:
                                    buff_obj = getattr(store, "star_bridge_done")
                                    buff_obj.calculate(role, None, None, None, "clean")
                        # 不是使用者则消除自己的星桥效果
                        if not is_user and target in buff_roles:
                            if "star_bridge" in target.buff:
                                buff_obj = getattr(store, "star_bridge")
                                buff_obj.calculate(target, None, None, None, "clean")
                            elif "star_bridge_done" in target.buff:
                                buff_obj = getattr(store, "star_bridge_done")
                                buff_obj.calculate(target, None, None, None, "clean")
                    # 良缘buff
                    if "heart_main" in target.buff:
                        buff_obj = getattr(store, "heart_main")
                        buff_obj.calculate(target, None, None, None, "clean")
                    # 共感解除
                    if "共感" in local_config.skill_log_data and "ally" in local_config.skill_log_data["共感"]:
                        buff_roles = local_config.skill_log_data["共感"]["ally"]
                        if target in buff_roles:
                            buff_roles.remove(target)
                        if "heart" in target.buff:
                            buff_obj = getattr(store, "heart")
                            buff_obj.calculate(target, None, None, None, "clean")
                        if len(local_config.skill_log_data["共感"]["ally"]) == 0:
                            local_config.skill_log_data["共感"].pop("ally")

                    target._special_calculate(enemy_environment_effects=ally_environment_effects, mode="release")
                    if order_members is not None:
                        order_members.update_members(go_role=target,
                                                     come_role=self)
                
                ## self入场计算
                ## ---- For Self ----
                ## 全局效果加入
                # 被动技能
                role_select_skills = self.skills if not self.is_phase2 else self.skills_v2
                passive_skill = [s for s in role_select_skills if s.category == "Passive"][0]
                ally_environment_effects.add((passive_skill.name, passive_skill.selectable))
                
                # 装备4件套
                ally_environment_effects.add((self.equip4effect, self.equip4effect_availabel))

                self._special_calculate(enemy_environment_effects=ally_environment_effects, mode="chain")

            if not reborn and show_role:
                local_config.active_actor = self
                renpy.show(local_config.active_actor.objectname, at_list=[show_player(local_config.active_actor.xposition)], layer="fg")

        # 自动施法
        def skill_auto(self, target, smart=False, confusion=False, cond=""):
            available_list = self.skills 
            if self.is_phase2:
                available_list = self.skills_v2

            choice_list = []
            recharge_skill, combat_skill, breakout_skill = None, None, None
            for skill in available_list:
                # 如果被混乱直接返回普攻
                if confusion and skill.category == "General_attack":
                    return skill
                if skill.category == "Recharge":
                    recharge_skill = skill
                elif skill.category == "Combat_skills":
                    combat_skill = skill
                elif skill.category == "Break_out":
                    breakout_skill = skill
                # 自动选择技能范围（除了被动技能和魔导力回路）
                if skill.category not in ["Passive", "Magic_circuit"]:
                    if skill.objectname != "xfe_breakout":
                        choice_list.append(skill)

            # 随机选择四季曲律
            if self.mp >= 40 and self.name == "希菲尔":
                random_index = renpy.random.randint(0, 4)
                random_skill = [getattr(store, "xfe_breakout_%d" % num) for num in range(1, 6)][random_index]
                fake_xfe_breakout = [s for s in available_list if s.category == "Break_out"][0]
                for xi in range(fake_xfe_breakout.level - 1):
                    random_skill.level_change(random_skill.level + 1)
                buff_roles = local_config.skill_log_data.setdefault("微量化改造", {})
                buff_roles[local_config.active_actor] = (random_skill, fake_xfe_breakout, self.is_phase2)

            # 根据mp消耗排序
            choice_list.sort(key=attrgetter("mp_cost"))

            ori_choice_list = copy(choice_list)
            # 技能筛选过滤
            for i in ori_choice_list:
                # 能量不足
                if "Spiritual" not in self.abilities and -i.mp_cost > self.mp:
                    choice_list.remove(i)
                # 技能被封印、被动技能
                elif not i.selectable or i.category == "Passive":
                    choice_list.remove(i)
                # 技能特殊规则
                elif i.name == "接触感应" and "咒" in local_config.skill_log_data:
                    choice_list.remove(i)
                elif i.name == "虚无":
                    if "积重鬼怨" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["积重鬼怨"]
                        if (self in local_config.party and "ally" in buff_roles) or (self in local_config.enemy and "enemy" in buff_roles):
                            choice_list.remove(i)
                        elif "ghost_mask" in self.buff:
                            _, buff_number = self.buff["ghost_mask"]
                            if buff_number != 9:
                                choice_list.remove(i)
                        else:
                            choice_list.remove(i)
                    elif "ghost_mask" in self.buff:
                        _, buff_number = self.buff["ghost_mask"]
                        if buff_number != 9:
                            choice_list.remove(i)
                    else:
                        choice_list.remove(i)
                elif i.name == "幻镜化物":
                    if "ethereal" in self.buff:
                        choice_list.remove(i)
                elif i.name == "预见良缘":
                    has_death = False
                    if self in local_config.party:
                        for role in local_config.party:
                            if role.hp < 1:
                                has_death = True
                                break
                    elif self in local_config.enemy:
                        for role in local_config.enemy:
                            if role.hp < 1:
                                has_death = True
                                break
                    if not has_death:
                        choice_list.remove(i)
                # 技能使用过多次
                elif i in self.history_skills and self.history_skills[i] >= 2:
                    choice_list.remove(i)
                    self.history_skills = {}

                ## 基本意识
                # 队友mp值均大于50不使用视线诱导
                # 队友数量少于1时不使用远隔透视
                remove_ycxt_breakout_skill = True
                remove_lingyin_breakout_skill = False
                if self in local_config.party:
                    temp_skill_roles = [r for r in local_config.party[:3] if r.hp > 1]
                    if len(temp_skill_roles) > 1:
                        for role in temp_skill_roles:
                            if role.mp < 30:
                                remove_ycxt_breakout_skill = False
                        if len(temp_skill_roles) < 3 and 0.7 > renpy.random.random():
                            remove_lingyin_breakout_skill = True
                elif self in local_config.enemy:
                    temp_skill_roles = [r for r in local_config.enemy[:3] if r.hp > 1]
                    if len(temp_skill_roles) > 1:
                        for role in temp_skill_roles:
                            if role.mp < 30:
                                remove_ycxt_breakout_skill = False
                        if len(temp_skill_roles) < 3 and 0.7 > renpy.random.random():
                            remove_lingyin_breakout_skill = True
                if (remove_ycxt_breakout_skill or cond == "tutorial_first") and i.name == "视线诱导":
                    if i in choice_list:
                        choice_list.remove(i)
                if remove_lingyin_breakout_skill and i.name == "远隔透视":
                    if i in choice_list:
                        choice_list.remove(i)
                
                remove_skill = True
                if self in local_config.party:
                    temp_skill_roles = [r for r in local_config.party[:3] if r.hp > 1]

                # 催眠状态下只能使用伤害技能
                if self.objectname in local_config.buff_source:
                    sources = local_config.buff_source[self.objectname]
                    if any(["催眠" in source for name, source in sources.items()]) and ("伤害" not in i.effects) and (i in choice_list):
                        choice_list.remove(i)
            
            # 防止不停充能
            if (combat_skill is not None and self.mp >= -(combat_skill.mp_cost)) and (breakout_skill is not None and self.mp >= -(breakout_skill.mp_cost)) and recharge_skill in choice_list:
                choice_list.remove(recharge_skill)
                
            # 保险判定（基本不会出现）
            if len(choice_list) == 0:
                return recharge_skill
            
            # 强化AI意识规则设定
            if smart:
                # AI斩杀判定
                for i in choice_list:
                    if target.hp <= target.max_hp * 0.5 and i.category == "Break_out" and "伤害" in i.effects:
                        return i
                for i in choice_list:
                    if target.hp <= target.max_hp * 0.3 and i.category == "Combat_skills" and "伤害" in i.effects:
                        return i
                for i in choice_list:
                    if target.hp <= target.max_hp * 0.1 and i.category == "General_attack":
                        return i

            choice_index = renpy.random.randint(0, len(choice_list) - 1)
            selected_skill = choice_list[choice_index]
            if selected_skill.category != "Recharge" and selected_skill not in self.history_skills:
                if len(self.history_skills) > 0:
                    self.history_skills = {}
                self.history_skills[selected_skill] = 1
            elif selected_skill.category != "Recharge":
                self.history_skills[selected_skill] += 1
            return selected_skill

        # 道具整理
        def item_sort(self):
            from collections import OrderedDict
            
            # self.items = dict(sorted(self.items.items(), key=lambda x: len(x), reverse=True))
            battle_items = ["eggs", "mana_eggs", "mana_potion", "angel_tears", "attack_meal", "defance_meal", "ele_attack_meal", "ele_defance_meal", "magic_meal"]
            role_items = ["soul_piece", "soul_raise"]
            tmp_listitem = OrderedDict()
            if local_config.in_battle:
                for name in battle_items:
                    if name in self.items:
                        tmp_listitem[name] = self.items[name]
            else:
                for name in role_items:
                    if name in self.items:
                        tmp_listitem[name] = self.items[name]
            for name, count in self.items.items():
                if name not in tmp_listitem:
                    tmp_listitem[name] = count
            self.items = tmp_listitem
            renpy.hide_screen("message_screen")
            renpy.show_screen("alt_notify", _("道具整理完成。"))

        def attr_change(self, name, value, change_base=False):
            attr_name = getattr(self, name)
            setattr(self, name, attr_name + value)
            if change_base:
                base_attr_name = getattr(self, "base_%s" % name)
                setattr(self, "base_%s" % name, base_attr_name + value)

        # 战斗结束重置
        def full_reset(self, heal_hp=True, ally_environment_effects=None, turn_end=True, level_reset=False):
            if heal_hp:
                self.hp = self.max_hp
                self.mp = int(0.5 * self.max_mp)

            self.face = "normal"
            self.is_phase2 = False
            
            # 最终战死亡技能不会恢复
            if local_config.tutorial_step != "winter_loss_stage":
                self.skills = self.base_skills
                for s in self.skills:
                    if not s.selectable:
                        s.selectable = True
                self.skills_v2 = self.base_skills_v2
                for s in self.skills_v2:
                    if not s.selectable:
                        s.selectable = True

            if turn_end:
                self.soulraise = 0
                self.defeat = 0
                self.be_defeat = 0
            
            buffs = copy(self.buff)
            for buff_name, item in buffs.items():
                if not turn_end:
                    if buff_name not in ["love", "ghost_mask"]:
                        buff_obj = getattr(store, buff_name)
                        buff_obj.calculate(self, ally_environment_effects, None, None, "clean")
                else:
                    buff_obj = getattr(store, buff_name)
                    buff_obj.calculate(self, ally_environment_effects, None, None, "clean")

            debuffs = copy(self.debuff)
            for buff_name, item in debuffs.items():
                buff_obj = getattr(store, buff_name)
                buff_obj.calculate(self, ally_environment_effects, None, None, "clean")
            self.ebuff = {}
            self.selected_skill = self.skills[0] if len(self.skills) > 0 else None
            self.selected_target = None
            self.moveable = True

            if level_reset:
                self.level = 1
                self.break_through = False
                self.star = self.base_star

                setattr(self, "attack", self.ori_attack)
                setattr(self, "base_attack", self.ori_attack)
                setattr(self, "extend_attack", self.ori_extend_attack)
                setattr(self, "base_extend_attack", self.ori_extend_attack)
                setattr(self, "max_hp", self.ori_max_hp)
                setattr(self, "base_max_hp", self.ori_max_hp)
                setattr(self, "extend_max_hp", self.ori_extend_max_hp)
                setattr(self, "base_extend_max_hp", self.ori_extend_max_hp)
                setattr(self, "defance", self.ori_defance)
                setattr(self, "base_defance", self.ori_defance)
                setattr(self, "extend_defance", self.ori_extend_defance)
                setattr(self, "speed", self.ori_speed)
                setattr(self, "base_speed", self.ori_speed)
                setattr(self, "critical_rate", self.ori_critical_rate)
                setattr(self, "base_critical_rate", self.ori_critical_rate)
                setattr(self, "critical_damage", self.ori_critical_damage)
                setattr(self, "base_critical_damage", self.ori_critical_damage)
                setattr(self, "effect_hitrate", self.ori_effect_hitrate)
                setattr(self, "base_effect_hitrate", self.ori_effect_hitrate)
                setattr(self, "effect_resistance", self.ori_effect_resistance)
                setattr(self, "base_effect_resistance", self.ori_effect_resistance)
                setattr(self, "elemental_mastery", self.ori_elemental_mastery)
                setattr(self, "base_elemental_mastery", self.ori_elemental_mastery)
                setattr(self, "healing_bonus", self.ori_healing_bonus)
                setattr(self, "base_healing_bonus", self.ori_healing_bonus)
                setattr(self, "shield_strength", self.ori_shield_strength)
                setattr(self, "base_shield_strength", self.ori_shield_strength)
                setattr(self, "fire_damage_bonus", self.ori_fire_damage_bonus)
                setattr(self, "base_fire_damage_bonus", self.ori_fire_damage_bonus)
                setattr(self, "fire_elemental_resistance", self.ori_fire_elemental_resistance)
                setattr(self, "base_fire_elemental_resistance", self.ori_fire_elemental_resistance)
                setattr(self, "light_damage_bonus", self.ori_light_damage_bonus)
                setattr(self, "base_light_damage_bonus", self.ori_light_damage_bonus)
                setattr(self, "light_elemental_resistance", self.ori_light_elemental_resistance)
                setattr(self, "base_light_elemental_resistance", self.ori_light_elemental_resistance)
                setattr(self, "wind_damage_bonus", self.ori_wind_damage_bonus)
                setattr(self, "base_wind_damage_bonus", self.ori_wind_damage_bonus)
                setattr(self, "wind_elemental_resistance", self.ori_wind_elemental_resistance)
                setattr(self, "base_wind_elemental_resistance", self.ori_wind_elemental_resistance)
                setattr(self, "ice_damage_bonus", self.ori_ice_damage_bonus)
                setattr(self, "base_ice_damage_bonus", self.ori_ice_damage_bonus)
                setattr(self, "ice_elemental_resistance", self.ori_ice_elemental_resistance)
                setattr(self, "base_ice_elemental_resistance", self.ori_ice_elemental_resistance)
                setattr(self, "water_damage_bonus", self.ori_water_damage_bonus)
                setattr(self, "base_water_damage_bonus", self.ori_water_damage_bonus)
                setattr(self, "water_elemental_resistance", self.ori_water_elemental_resistance)
                setattr(self, "base_water_elemental_resistance", self.ori_water_elemental_resistance)
                setattr(self, "rock_damage_bonus", self.ori_rock_damage_bonus)
                setattr(self, "base_rock_damage_bonus", self.ori_rock_damage_bonus)
                setattr(self, "rock_elemental_resistance", self.ori_rock_elemental_resistance)
                setattr(self, "base_rock_elemental_resistance", self.ori_rock_elemental_resistance)
                setattr(self, "physical_damage_bonus", self.ori_physical_damage_bonus)
                setattr(self, "base_physical_damage_bonus", self.ori_physical_damage_bonus)
                setattr(self, "physical_elemental_resistance", self.ori_physical_elemental_resistance)
                setattr(self, "base_physical_elemental_resistance", self.ori_physical_elemental_resistance)

                self.outfits = {
                    "武器": None,
                    "防具": None,
                    "项链": None,
                    "戒指": None,
                    "法杖": None,
                    "宝石": None,
                }

                # 装备重新计算
                self.equip_recalculate()
                
        # 经验计算
        def xpchange(self, enemy_levels=None, item_lists=None):
            """
            经验获取的定义：
                1、战斗胜利或使用经验素材道具可以提升经验值；
                2、每个等级的经验值上线按公式计算，超过部分清空并进入升级判定；
                3、升级判定：如果等级达到升星阈值且突破标签为False，则不提供经验加成；
            """
            # 不提供经验条件
            if self.level >= 40:
                pass
            else:
                # 通过道具获取经验
                if item_lists is not None:
                    pass

                # 通过打怪获取经验
                if enemy_levels is not None:
                    # 怪物所提供的总经验值
                    total_exp = 0.0
                    for level in enemy_levels:
                        total_exp += 100 + 10 * (level + 1) if level < 20 else 300 + 20 * (level - 20)

                    self.xp += total_exp * persistent.xp

        def battle_role_init_control(self, user, target, ally_environment_effects, enemy_environment_effects):
            ## 附加效果结算
            battle_user_effect_hitrate = user.battle_effect_hitrate
            battle_target_effect_resistance = target.battle_effect_resistance

            # 攻击者天赋

            # 攻击者装备4件套
            if ("天之印-碧落", True) in ally_environment_effects:
                battle_user_effect_hitrate += 0.25

            ## 防御者天赋
            # 宁静天赋：每有一名友方单位处于无法动作的效果影响下，额外提供10%的效果抵抗
            if "Serenity" in target.abilities:
                if target in local_config.party:
                    for role in local_config.party[:3]:
                        if role.hp > 0 and not role.moveable:
                            battle_target_effect_resistance += 0.1
                elif target in local_config.enemy:
                    for role in local_config.enemy[:3]:
                        if role.hp > 0 and not role.moveable:
                            battle_target_effect_resistance += 0.1

            ## 防御者装备4件套
            # 山之巅-玉嶂
            if ("shield" in target.buff or "sp_shield" in target.buff) and ("山之巅-玉嶂", True) in enemy_environment_effects:
                battle_target_effect_resistance += 0.4

            return battle_user_effect_hitrate, battle_target_effect_resistance

        def battle_role_init(self, user, target, ally_environment_effects, enemy_environment_effects, sp_rull=""):
            battle_user_elemental_mastery = user.battle_elemental_mastery
            # 旧版：元素精通加成 = (-0.0002 x (元素精通) ^ 2 + 0.4527 x 元素精通 + 1.0058) / 100.0
            # battle_elemental_mastery_bonus = (-0.0002 * math.pow(battle_user_elemental_mastery, 2) + 0.4527 * battle_user_elemental_mastery + 1.0058) / 100.0
            # 新版：增幅反应加成 = 1.0 x 2.78 x 元素精通 / (元素精通 + 1400)
            battle_elemental_mastery_bonus = 1.0 * 2.78 * battle_user_elemental_mastery / (battle_user_elemental_mastery + 1400)
            # 新版：剧变反应加成 = 2.4 x 2.78 x 元素精通 / (元素精通 + 1400)
            battle_elemental_mastery_bonus2 = 2.4 * 2.78 * battle_user_elemental_mastery / (battle_user_elemental_mastery + 1400)

            # 战斗伤害参数计算
            battle_user_critical_rate = user.battle_critical_rate
            battle_user_critical_damage = user.battle_critical_damage
            battle_user_origin_attack = float(user.battle_attack)
            battle_user_extend_attack = float(user.battle_extend_attack)
            battle_user_healing_bonus = user.battle_healing_bonus
            battle_user_shield_strength = user.battle_shield_strength

            battle_target_defance = float(target.battle_defance)
            battle_target_extend_defance = float(target.battle_extend_defance)

            # 攻击者天赋：谨慎
            if "Prudent" in user.abilities:
                if user.hp > user.battle_max_hp * 0.5:
                    battle_user_critical_rate += 0.15
                    battle_user_extend_attack += (battle_user_origin_attack * 0.15)

            ## 攻击者装备4件套
            # 日之轮-曦禾
            judgerate = renpy.random.random()
            if user.equip4effect == "日之轮-曦禾" and ("日之轮-曦禾", True) in ally_environment_effects:
                if (not target.moveable and 0.3 > judgerate) or (target.moveable and 0.2 > judgerate):
                    battle_user_extend_attack += (battle_user_origin_attack * 0.2)
            # 山之巅-玉璋
            if ("shield" in user.buff or "sp_shield" in user.buff) and ("山之巅-玉璋", True) in ally_environment_effects:
                battle_user_extend_attack += (battle_user_origin_attack * 0.2)
            # 春之花-仑灵
            if user.equip4effect == "春之花-仑灵" and ("春之花-仑灵", True) in ally_environment_effects:
                if target.hp < 0.2 * target.battle_max_hp:
                    battle_user_healing_bonus += 0.5
                else:
                    battle_user_healing_bonus += 0.2

            # 防御者天赋：坚韧 = 角色的HP每损失上限的25%，则在伤害计算时提升50点防御力，同时在获得治疗和护盾时，提升10%治疗加成和10%护盾强效
            if "Fortitude" in target.abilities:
                hp_ratio = math.floor(((target.battle_max_hp - target.hp) / target.battle_max_hp) / 0.25)
                battle_target_defance += 50 * hp_ratio
                battle_user_healing_bonus += 0.1 * hp_ratio
                battle_user_shield_strength += 0.1 * hp_ratio
            # 谨慎 = 当角色生命值低于50%，伤害结算时防御力提升100点
            if "Prudent" in target.abilities:
                if target.hp < target.battle_max_hp * 0.5:
                    battle_target_defance += 100

            ## 防御者装备4件套
            # 日之轮-曦禾
            judgerate = renpy.random.random()
            if target.equip4effect == "日之轮-曦禾" and ("日之轮-曦禾", True) in enemy_environment_effects:
                if (not target.moveable and 0.3 > judgerate) or (target.moveable and 0.2 > judgerate):
                    battle_target_extend_defance += (battle_target_defance * 0.2)

            # 面板攻击力 = 基础攻击力 x (1 + 百分比攻击加成) + 固定攻击力
            battle_base_attack = battle_user_origin_attack + battle_user_extend_attack
            battle_target_defance += battle_target_extend_defance

            # 冬之羽-玄英
            if user.equip4effect == "冬之羽-玄英" and ("冬之羽-玄英", True) in ally_environment_effects:
                if 0.5 > renpy.random.random():
                    battle_target_defance = 0.55 * battle_target_defance
            # 空间跳跃
            if sp_rull == "空间跳跃":
                fake_lst_role = None
                if user in local_config.party:
                    for temp_role in local_config.party:
                        if temp_role.name == "雷亚":
                            fake_lst_role = temp_role
                else:
                    for temp_role in local_config.enemy:
                        if temp_role.name == "雷亚":
                            fake_lst_role = temp_role
                temp_selected_skill = fake_lst_role.base_skills if not fake_lst_role.is_phase2 else fake_lst_role.base_skills_v2
                fake_lst_skill = [s for s in temp_selected_skill if s.category == "Break_out"][0]

                if fake_lst_skill.level > 1:
                    battle_target_defance -= 150
                    if battle_target_defance < 0:
                        battle_target_defance = 0

            return battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack

        # 战斗计算
        def battle_calculate(self, skill, user, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, sp_rull="", support=False, ani_only_once=False):
            # 只有受到控制效果时变化
            hitted = False

            damage_color_map = {
                "fire": "#f30",
                "water": "#19f",
                "light": "#f0f",
                "ice": "#3ff",
                "wind": "#6f6",
                "rock": "#ff0",
                "physical": "#9cf",
                "蒸发": "#9cf",
                "融化": "#9cf",
                "超载": "#f66",
                "冻结": "#3ff",
                "超导": "#99f",
                "感电": "#f0f",
                "扩散": "#6f6",
                "结晶": "#ff0",
                "治疗": "#2f0",
                "能量": "#19f",
            }

            battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack = self.battle_role_init(user, self, ally_environment_effects, enemy_environment_effects, sp_rull)

            ## 伤害计算（装备、天赋、角色属性、技能倍率、buff加成、元素反应）
            if "伤害" in skill.effects:
                ## 技能特殊判定
                total_skill_damages = copy(skill.damage)
                total_skill_elements = copy(skill.element)
                # 精准掌握：普攻之后有20%|25%|30%|30%|30%概率附加一段攻击60%|60%|60%|80%|100%火元素伤害
                if (("精准掌握", True) in ally_environment_effects) and user.name == "花山院琉璃" and skill.category == "General_attack":
                    temp_selected_skill = user.skills if not user.is_phase2 else user.skills_v2
                    passive_skill = [s for s in temp_selected_skill if s.category == "Passive"][0]
                    ratio_lists = [0.2, 0.25, 0.3, 0.3, 0.3]
                    if ratio_lists[passive_skill.level - 1] > renpy.random.random():
                        temp_damage_lists = [0.6, 0.6, 0.6, 0.8, 1.0]
                        total_skill_damages += [temp_damage_lists[passive_skill.level - 1]]
                        total_skill_elements += ["fire"]

                # 旧版：最终伤害 = 攻击力 x 伤害倍率 x 暴击伤害 x (1 + 技能/天赋/装备额外加成 + 物理/元素伤害加成 + 元素反应加成(蒸发|融化)) x 最终元素抗性 x 承伤比例
                # 攻击力 = 基础攻击力 + 攻击力加成 | 攻击力加成 = 基础攻击力 x (1 + 攻击力加成比例) + 固定攻击力
                # 精通提升= (-0.0002 x (元素精通) ^ 2 + 0.4527 x 元素精通 + 1.0058) / 100.0
                # 防御减免 = (300 / (300 + 防御力)

                # 新版：最终伤害 = 攻击力 x 防御减免 x 伤害倍率 x (1 + 伤害加成) x 暴击伤害 x 增幅反应倍率 x 承伤比例 x 抗性减免
                # 攻击力 = 基础攻击力 + 攻击力加成 | 攻击力加成 = 基础攻击力 x (1 + 攻击力加成比例) + 固定攻击力
                # 防御减免 = 300 / (300 + 防御力)
                # 伤害倍率 = 技能倍率
                # 伤害加成 = 技能/天赋/装备额外加成
                # 暴击伤害期望 = 1 + (暴击率 x 暴击伤害)
                # 增幅反应倍率 = 元素反应提升倍率 = 元素反应基本倍率 x (1 + 精通提升 + 反应提升系数) | 精通提升 = K x 2.78 x 精通 / (精通 + 1400)
                # 承伤比例 = 1 + (攻击者等级 / 被攻击者等级 - 1) * 0.4
                # 抗性减免 = 被攻击者抗性 - 抗性削减 if 被攻击者抗性 >= 抗性削减 else 0.5 x (被攻击者抗性 - 抗性削减)

                inner_react = False
                con_hun_flag = False
                for battle_skill_damage_ratio, battle_skill_element in zip(total_skill_damages, total_skill_elements):
                    battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack = self.battle_role_init(user, self, ally_environment_effects, enemy_environment_effects, sp_rull)
                    battle_user_effect_hitrate, battle_target_effect_resistance = self.battle_role_init_control(user, self, ally_environment_effects, enemy_environment_effects)

                    # 暴击判定
                    judgerate = renpy.random.random()
                    battle_critical = battle_user_critical_rate >= judgerate

                    # 防御减免后倍率(300 / (300 + 防御力)
                    battle_defance_resistance = 300 / (300 + battle_target_defance)
                    # 基础伤害 = 面板攻击力 x 防御减免后倍率)
                    battle_fundamental_damage = battle_base_attack * battle_defance_resistance
                    # 承伤比例 old = 攻击者等级 / 被攻击者等级
                    # 承伤比例 new = 1 + (攻击者等级 / 被攻击者等级 - 1) * 0.4
                    battle_level_damage_rate = 1 + (user.level / self.level - 1) * 0.4
                    # 角色元素伤害加成
                    battle_user_damage_bonus = getattr(user, "battle_%s_damage_bonus" % battle_skill_element) if battle_skill_element else None
                    # 最终元素抗性 = 怪物抗性 - 抗性削减 if 怪物抗性 >= 抗性削减 else 0.5 x (怪物抗性 - 抗性削减)
                    battle_target_elemental_resistance = getattr(self, "battle_%s_elemental_resistance" % battle_skill_element) if battle_skill_element else None

                    # 回响 & 狩猎天赋
                    if battle_critical and ("Conjurer" in user.abilities and battle_skill_element is not None and battle_skill_element != "physical") and 0.3 > renpy.random.random():
                        renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("回响", style="effect_text", color="ff9"))
                        # renpy.pause(0.5 * persistent.battlespeed)
                        # renpy.hide("buff_effect", layer="screens")

                        battle_target_elemental_resistance -= 0.15
                        con_hun_flag = True
                    if battle_critical and ("Hunter" in user.abilities and battle_skill_element == "physical") and 0.3 > renpy.random.random():
                        renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("狩猎", style="effect_text", color="ff9"))
                        # renpy.pause(0.5 * persistent.battlespeed)
                        # renpy.hide("buff_effect", layer="screens")

                        battle_target_elemental_resistance -= 0.3
                        con_hun_flag = True
                    
                    # 抗性负数时->增伤转换
                    if battle_target_elemental_resistance >= 0:
                        battle_resistance_damage_rate = 1 - battle_target_elemental_resistance
                    else:
                        battle_resistance_damage_rate = 1 - (0.5 * battle_target_elemental_resistance)
                    
                    ## 元素反应乘区（蒸发、融化）
                    # 水->火 | 火->冰（蒸发|融化 2.0倍率）
                    battle_user_element_bonus = 0.0
                    if battle_skill_element == "water" and "fire" in self.ebuff:
                        renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("蒸发", style="effect_text", size=80, color=damage_color_map["蒸发"]))
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            battle_user_element_bonus = 1.2 * (1 + battle_elemental_mastery_bonus)
                        else:
                            battle_user_element_bonus = 1.0 * (1 + battle_elemental_mastery_bonus)

                        # “遗念镜”祝福
                        if self in local_config.party and "蒸发" in local_config.battle_blessing:
                            battle_user_element_bonus += local_config.battle_blessing["蒸发"]

                        # 元素消融
                        self.ebuff["fire"] -= 3
                        if self.ebuff["fire"] <= 0:
                            self.ebuff.pop("fire")

                        inner_react = True
                    elif battle_skill_element == "fire" and "ice" in self.ebuff:
                        renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("融化", style="effect_text", size=80, color=damage_color_map["融化"]))
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            battle_user_element_bonus = 1.2 * (1 + battle_elemental_mastery_bonus)
                        else:
                            battle_user_element_bonus = 1.0 * (1 + battle_elemental_mastery_bonus)

                        # “遗念镜”祝福
                        if self in local_config.party and "融化" in local_config.battle_blessing:
                            battle_user_element_bonus += local_config.battle_blessing["融化"]

                        # 50%概率消除冰冻状态
                        if "frozen" in self.debuff and renpy.random.random() > 0.5:
                            buff_obj = getattr(store, "frozen")
                            buff_obj.calculate(self, None, None, None, "clean")
                            self.ebuff.pop("ice")
                        else:
                            self.ebuff["ice"] -= 3
                            if self.ebuff["ice"] <= 0:
                                self.ebuff.pop("ice")

                        inner_react = True
                    # 火->水 | 冰->火（蒸发|融化 1.5倍率）
                    elif battle_skill_element == "fire" and "water" in self.ebuff:
                        renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("蒸发", style="effect_text", size=80, color=damage_color_map["蒸发"]))
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            battle_user_element_bonus = 0.7 * (1 + battle_elemental_mastery_bonus)
                        else:
                            battle_user_element_bonus = 0.5 * (1 + battle_elemental_mastery_bonus)

                        # “遗念镜”祝福
                        if self in local_config.party and "蒸发" in local_config.battle_blessing:
                            battle_user_element_bonus += local_config.battle_blessing["蒸发"]

                        self.ebuff["water"] -= 2
                        if self.ebuff["water"] <= 0:
                            self.ebuff.pop("water")

                        inner_react = True
                    elif battle_skill_element == "ice" and "fire" in self.ebuff:
                        renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("融化", style="effect_text", size=80, color=damage_color_map["融化"]))
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            battle_user_element_bonus = 0.7 * (1 + battle_elemental_mastery_bonus)
                        else:
                            battle_user_element_bonus = 0.5 * (1 + battle_elemental_mastery_bonus)

                        # “遗念镜”祝福
                        if self in local_config.party and "融化" in local_config.battle_blessing:
                            battle_user_element_bonus += local_config.battle_blessing["融化"]

                        self.ebuff["fire"] -= 2
                        if self.ebuff["fire"] <= 0:
                            self.ebuff.pop("fire")

                        inner_react = True

                    ## 特殊机制加成
                    battle_other_bonus = 0.0
                    # 降魔诛乱：对“鬼”、“神”、“天使”造成的伤害增加30%
                    if skill.name == "降魔诛乱" and skill.level == 5 and self.category in ["gost", "god", "angel"]:
                        renpy.show("special", at_list=[show_state(self.xposition)], layer="screens", what=Text("降魔", style="skill_text"))
                        battle_other_bonus += 0.3
                    # 噗哈哈：自身获得减伤
                    if self.name == "藤原瞳" and "ridicule" in user.debuff:
                        temp_selected_skills = self.base_skills if not self.is_phase2 else self.base_skills_v2
                        fake_tyt_combat = [s for s in temp_selected_skills if s.category == "Combat_skills"][0]
                        if fake_tyt_combat.level == 4:
                            battle_skill_damage_ratio -= 0.2
                        elif fake_tyt_combat.level == 5:
                            battle_skill_damage_ratio -= 0.4
                    # 对生命比例高于80%的目标，此次伤害倍率降低15%
                    if skill.name == "不知火":
                        if self.hp / self.battle_max_hp > 0.8:
                            battle_skill_damage_ratio -= 0.15
                        elif self.hp / self.battle_max_hp < 0.5 and skill.level in [3, 4, 5]:
                            battle_skill_damage_ratio += 0.15
                    # 对生命比例低于50%的目标，此次伤害倍率降低15%
                    if skill.name == "冥火":
                        if self.hp / self.battle_max_hp < 0.5:
                            battle_skill_damage_ratio -= 0.15
                        elif self.hp / self.battle_max_hp > 0.8 and skill.level in [3, 4, 5]:
                            battle_skill_damage_ratio += 0.15
                    # 星空梦影
                    if "star_bridge" in self.buff or "star_bridge_done" in self.buff:
                        buff_roles = local_config.skill_log_data["星空梦影"]
                        buff_user_role = None
                        for t, (f, u) in buff_roles.items():
                            buff_user_role = u
                            break
                        
                        # 降低15%|20%|25%|30%|30%受到的伤害
                        temp_ratio_lists = [0.15, 0.2, 0.25, 0.3, 0.3]
                        temp_selected_skill = buff_user_role.skills if not buff_user_role.is_phase2 else buff_user_role.skills_v2
                        temp_combat_skill = [s for s in temp_selected_skill if s.category == "Combat_skills"][0]
                        battle_other_bonus -= temp_ratio_lists[temp_combat_skill.level - 1]

                        # 使得下一次受到的伤害降低10%|15%|20%|25%|30%
                        if "star_bridge" in self.buff:
                            temp_ratio_lists = [0.1, 0.15, 0.2, 0.25, 0.3]
                            temp_selected_skill = buff_user_role.skills if not buff_user_role.is_phase2 else buff_user_role.skills_v2
                            temp_combat_skill = [s for s in temp_selected_skill if s.category == "Combat_skills"][0]

                            battle_other_bonus -= temp_ratio_lists[temp_combat_skill.level - 1]
                            buff_obj = getattr(store, "star_bridge")
                            buff_obj.calculate(self, None, None, "done", "clean")
                    # 白色永恒：在回合结束前的战斗计算阶段提升20%|30%|30%|30%|30%暴击伤害
                    if "白色永恒" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["白色永恒"]
                        if user in local_config.party and "ally" in buff_roles:
                            _, fake_xfe_passive, flag = buff_roles["ally"]
                            if flag:
                                if fake_xfe_passive.level in [2, 3, 4, 5]:
                                    battle_user_critical_damage += 0.3
                                else:
                                    battle_user_critical_damage += 0.2
                        elif user in local_config.enemy and "enemy" in buff_roles:
                            _, fake_xfe_passive, flag = buff_roles["enemy"]
                            if flag:
                                if fake_xfe_passive.level in [2, 3, 4, 5]:
                                    battle_user_critical_damage += 0.3
                                else:
                                    battle_user_critical_damage += 0.2
                    # 秋之韵-素律
                    if user.equip4effect == "秋之韵-素律" and ("秋之韵-素律", True) in ally_environment_effects:
                        if self.hp > 0.7 * self.battle_max_hp:
                            battle_other_bonus += 0.3
                        else:
                            hp_ratio = math.floor(((0.7 * self.battle_max_hp - self.hp) / self.battle_max_hp) / 0.2)
                            battle_other_bonus += 0.1 * hp_ratio
                    # 冬之羽-玄英
                    if user.equip4effect == "冬之羽-玄英" and ("冬之羽-玄英", True) in ally_environment_effects:
                        mp_ratio = math.floor(self.mp / 10)
                        battle_other_bonus += 0.04 * mp_ratio

                    if battle_critical:
                        # single_battle_damage = battle_fundamental_damage * battle_skill_damage_ratio * battle_user_critical_damage * (1.0 + battle_user_damage_bonus + battle_user_element_bonus + battle_other_bonus) * battle_resistance_damage_rate * battle_level_damage_rate
                        single_battle_damage = battle_fundamental_damage * battle_skill_damage_ratio * (1.0 + battle_user_damage_bonus + battle_other_bonus) * battle_user_critical_damage * (1 + battle_user_element_bonus) * battle_level_damage_rate * battle_resistance_damage_rate
                    else:
                        # single_battle_damage = battle_fundamental_damage * battle_skill_damage_ratio * (1.0 + battle_user_damage_bonus + battle_user_element_bonus + battle_other_bonus) * battle_resistance_damage_rate * battle_level_damage_rate
                        single_battle_damage = battle_fundamental_damage * battle_skill_damage_ratio * (1.0 + battle_user_damage_bonus + battle_other_bonus) * (1 + battle_user_element_bonus) * battle_level_damage_rate * battle_resistance_damage_rate

                    ## 伤害结算
                    left_final_damage = int(single_battle_damage)
                    # 护盾抵消（伤害计算优先扣除护盾）
                    if "sp_shield" in self.buff:
                        shield_time, shield_effects = self.buff["sp_shield"]
                        shield_strength, shield_element, _, _ = shield_effects
                        shield_damage_ratio = 1.0
                        # 属性克制（强势1.5倍、弱势0.5倍）
                        if (battle_skill_element == "water" and shield_element == "fire") or (battle_skill_element == "fire" and shield_element == "ice") or (battle_skill_element == "ice" and shield_element == "light") or (battle_skill_element == "light" and shield_element == "water") or (battle_skill_element == "rock" and shield_element == "rock"):
                            shield_damage_ratio = 1.5
                        elif (battle_skill_element == "fire" and shield_element == "water") or (battle_skill_element == "ice" and shield_element == "fire") or (battle_skill_element == "light" and shield_element == "ice") or (battle_skill_element == "water" and shield_element == "light"):
                            shield_damage_ratio = 0.5
                        # 属性调和（0.25倍）
                        elif shield_element not in ["rock", "physical"] and battle_skill_element == shield_element:
                            shield_damage_ratio = 0.25
                        
                        left_shield_strength = int(shield_strength - shield_damage_ratio * left_final_damage)
                        # 更新护盾
                        shield_buff = getattr(store, "sp_shield")
                        item = (shield_time, (left_shield_strength, shield_element, 0.75, 0.5))
                        shield_buff.calculate(self, None, item, None, "get")
                        left_final_damage = 0

                        renpy.music.play("盾档", channel="battle_music")
                        renpy.pause(0.001)

                        # 如果护盾破碎，驱散护盾并结算剩余伤害
                        if "sp_shield" not in self.buff:
                            # 穿透伤害
                            if left_shield_strength < 0:
                                left_final_damage = -int(left_shield_strength/shield_damage_ratio)
                    if "shield" in self.buff:
                        shield_time, shield_effects = self.buff["shield"]
                        shield_strength, shield_element, _, _ = shield_effects
                        shield_damage_ratio = 1.0
                        # 属性克制（强势1.5倍、弱势0.5倍）
                        if (battle_skill_element == "water" and shield_element == "fire") or (battle_skill_element == "fire" and shield_element == "ice") or (battle_skill_element == "ice" and shield_element == "light") or (battle_skill_element == "light" and shield_element == "water") or (battle_skill_element == "rock" and shield_element == "rock"):
                            shield_damage_ratio = 1.5
                        elif (battle_skill_element == "fire" and shield_element == "water") or (battle_skill_element == "ice" and shield_element == "fire") or (battle_skill_element == "light" and shield_element == "ice") or (battle_skill_element == "water" and shield_element == "light"):
                            shield_damage_ratio = 0.5
                        # 属性调和（0.25倍）
                        elif shield_element not in ["rock", "physical"] and battle_skill_element == shield_element:
                            shield_damage_ratio = 0.25

                        left_shield_strength = int(shield_strength - shield_damage_ratio * left_final_damage)
                        # 如果护盾还未消失，更新护盾
                        shield_buff = getattr(store, "shield")
                        item = (shield_time, (left_shield_strength, shield_element, 0.75, 0.5))
                        shield_buff.calculate(self, None, item, None, "get")
                        left_final_damage = 0

                        renpy.music.play("盾档", channel="battle_music")
                        renpy.pause(0.001)

                        # 如果护盾破碎，驱散护盾并结算剩余伤害
                        if "shield" not in self.buff:
                            # 穿透伤害
                            if left_shield_strength < 0:
                                left_final_damage = -int(left_shield_strength/shield_damage_ratio)

                    # 角色伤害承受
                    if left_final_damage > 0.0:
                        # 唤醒沉睡状态
                        if "sleepy" in self.debuff:
                            buff_obj = getattr(store, "sleepy")
                            buff_obj.calculate(self, None, None, None, "clean")
                        # 唤醒深度沉睡
                        if "deep_sleepy" in self.debuff and left_final_damage >= 0.3 * self.battle_max_hp:
                            buff_obj = getattr(store, "deep_sleepy")
                            buff_obj.calculate(self, None, None, None, "clean")

                        ## 装备4件套效果、角色被动技能触发
                        # 处于“咒”状态下的“立花希”受到伤害时 或 处于“咒”状态下的敌方单位受到伤害时
                        if (("再会之音", True) in enemy_environment_effects and self.name == "立花希" and "curse" in self.buff) or (("再会之音", True) in ally_environment_effects and "decurse" in self.debuff):
                            change = renpy.random.random()
                            lhx_passive_skill = [s for s in self.skills if s.category == "Passive"][0]
                            if ((lhx_passive_skill.level == 1 and 0.1 > change) or (lhx_passive_skill.level == 2 and 0.13 > change) or (lhx_passive_skill.level == 3 and 0.16 > change) or (lhx_passive_skill.level in [4, 5] and 0.2 > change)) and "咒" in local_config.skill_log_data:
                                # {"咒": {"lhx_role": (False, None, "user", target), [target.objectname]: (False, None, "target", source)}}
                                temp_dict = local_config.skill_log_data["咒"][self]
                                local_config.skill_log_data["咒"][self] = (True, left_final_damage, temp_dict[2], temp_dict[3])
                        if "咒" in local_config.skill_log_data and sp_rull != "空间跳跃":
                            buff_roles = local_config.skill_log_data["咒"]
                            fake_lhx_role = None
                            buff_select_role = None
                            for role, (flag, damg, dtype, other) in buff_roles.items():
                                if self.name == "立花希" and dtype == "user" and self == role:
                                    fake_lhx_role = role
                                elif dtype == "target":
                                    buff_select_role = role
                            if fake_lhx_role is not None:
                                lhx_breakout_skill = [s for s in fake_lhx_role.skills if s.category == "Break_out"][0]
                                if lhx_breakout_skill.level == 1:
                                    damage_number = int(0.5 * left_final_damage)
                                elif lhx_breakout_skill.level == 2:
                                    damage_number = int(0.6 * left_final_damage)
                                elif lhx_breakout_skill.level == 3:
                                    damage_number = int(0.7 * left_final_damage)
                                elif lhx_breakout_skill.level == 4:
                                    damage_number = int(0.8 * left_final_damage)
                                else:
                                    damage_number = int(left_final_damage)

                                buff_select_role.hp -= damage_number
                                if buff_select_role.hp < 1:
                                    buff_select_role.hp = 0
                                    buff_select_role.death_calculate(fake_lhx_role, skill, enemy_environment_effects, ally_environment_effects, order_members)
                                else:
                                    if lhx_breakout_skill.level == 5 and 0.12 > renpy.random.random():
                                        buff_obj = getattr(store, "handicapped")
                                        item = (1, 0.2)
                                        buff_obj.calculate(buff_select_role, None, item, skill.name, "get")
                                        buff_obj = getattr(store, "broken")
                                        item = (1, 0.2)
                                        buff_obj.calculate(buff_select_role, None, item, skill.name, "get")
                        # ----- 守护誓约 -----
                        if ("守护誓约", True) in enemy_environment_effects and ("star_bridge" in self.buff or "star_bridge_done" in self.buff):
                            buff_roles = local_config.skill_log_data["星空梦影"]

                            if self in buff_roles:
                                temp_flag, temp_buff_user = buff_roles[self]
                                temp_selected_skill = temp_buff_user.base_skills if not temp_buff_user.is_phase2 else temp_buff_user.base_skills_v2
                                lst_passive_skill = [s for s in temp_selected_skill if s.category == "Passive"][0]

                                # temp_ratio_lists = [0.2, 0.3, 0.3, 0.4, 0.4]
                                # # 降低该次伤害的20%|30%|30%|40%|40%
                                # left_final_damage *= temp_ratio_lists[lst_passive_skill.level - 1]
                                # left_final_damage = int(left_final_damage)
                                
                                # 降低施术者15%攻击力和30%暴击率，持续1回合
                                buff_obj = getattr(store, "weak")
                                if lst_passive_skill.level == 1:
                                    item = (2, 0.1)
                                else:
                                    item = (2, 0.15)
                                buff_obj.calculate(user, None, item, "守护誓约", "get")
                                
                                buff_obj = getattr(store, "powerless")
                                if lst_passive_skill.level == 1:
                                    item = (2, (0.2, 0.0))
                                else:
                                    item = (2, (0.3, 0.0))
                                buff_obj.calculate(user, None, item, "守护誓约", "get")

                                # 提升10点速度和20%效果抵抗，持续1回合
                                if lst_passive_skill.level == 4:
                                    buff_obj = getattr(store, "flow")
                                    item = (1, 10)
                                    buff_obj.calculate(self, None, item, "守护誓约", "get")
                                    buff_obj = getattr(store, "barrier")
                                    item = (1, 0.2)
                                    buff_obj.calculate(self, None, item, "守护誓约", "get")
                                elif lst_passive_skill.level == 5:
                                    buff_obj = getattr(store, "flow")
                                    item = (1, 20)
                                    buff_obj.calculate(self, None, item, "守护誓约", "get")
                                    buff_obj = getattr(store, "barrier")
                                    item = (1, 0.3)
                                    buff_obj.calculate(self, None, item, "守护誓约", "get")

                                # 队友生命值低于上限的30%时
                                if lst_passive_skill.level >= 3 and self.hp < self.battle_max_hp * 0.3:
                                    # temp_ratio_lists = [0.0, 0.0, (0.1, 0.12), (0.1, 0.12), (0.2, 0.24)]
                                    # 雷亚将为其承担该伤害的10%|10%|20%（最大不超过雷亚生命上限的12%|12%|24%）
                                    # dmg_ratio1, dmg_ratio2 = temp_ratio_lists[lst_passive_skill.level - 1]
                                    # fake_lst_damage = int(left_final_damage * dmg_ratio1) if int(left_final_damage * dmg_ratio1) <= temp_buff_user.battle_max_hp * dmg_ratio2 else int(temp_buff_user.battle_max_hp * dmg_ratio2)
                                    # left_final_damage -= fake_lst_damage
                                    # temp_buff_user.hp -= fake_lst_damage
                                    # 雷亚将为其承担该伤害
                                    left_final_damage = 0
                                    temp_buff_user.hp -= left_final_damage
                                    # 死亡判定
                                    temp_buff_user.death_calculate(user, lst_passive_skill, ally_environment_effects, enemy_environment_effects, order_members)
                                    
                        # 每次造成伤害有20%|30%|40%|50%|60%的概率获得一层“鬼面”
                        if skill.name == "福祸相生":
                            temp_ratio_lists = [0.2, 0.3, 0.4, 0.5, 0.6]
                            if not local_config.multi_buff_lock and temp_ratio_lists[skill.level - 1] > renpy.random.random():
                                if "积重鬼怨" in local_config.skill_log_data:
                                    buff_roles = local_config.skill_log_data["积重鬼怨"]
                                    if (not (user in local_config.party and "ally" in buff_roles)) and (not (user in local_config.enemy and "enemy" in buff_roles)):
                                        buff_obj = getattr(store, "ghost_mask")
                                        item = (99, 1)
                                        buff_obj.calculate(user, ally_environment_effects, item, "福祸相生", "get")
                                else:
                                    buff_obj = getattr(store, "ghost_mask")
                                    item = (99, 1)
                                    buff_obj.calculate(user, ally_environment_effects, item, "福祸相生", "get")
                        # 每受到暴击伤害时有40%|50%|60%|70%|80%概率额外获得1层“鬼面”
                        if ("积重鬼怨", True) in enemy_environment_effects and not local_config.multi_buff_lock:
                            fake_qcls_role = None
                            if user in local_config.party:
                                for role in local_config.enemy:
                                    if role.name == "千川老师":
                                        fake_qcls_role = role
                                        break
                            else:
                                for role in local_config.party:
                                    if role.name == "千川老师":
                                        fake_qcls_role = role
                                        break
                            temp_selected_skills = fake_qcls_role.base_skills if not fake_qcls_role.is_phase2 else fake_qcls_role.base_skills_v2
                            temp_passive_skill = [s for s in temp_selected_skills if s.category == "Passive"][0]
                            temp_ratio_lists = [0.4, 0.5, 0.6, 0.7, 0.8]
                            if battle_critical and temp_ratio_lists[temp_passive_skill.level - 1] >= renpy.random.random():
                                if "积重鬼怨" in local_config.skill_log_data:
                                    buff_roles = local_config.skill_log_data["积重鬼怨"]
                                    if (not (user in local_config.party and "ally" in buff_roles)) and (not (user in local_config.enemy and "enemy" in buff_roles)):
                                        buff_obj = getattr(store, "ghost_mask")
                                        item = (99, 1)
                                        buff_obj.calculate(user, ally_environment_effects, item, "积重鬼怨", "get")
                                else:
                                    buff_obj = getattr(store, "ghost_mask")
                                    item = (99, 1)
                                    buff_obj.calculate(fake_qcls_role, enemy_environment_effects, item, "积重鬼怨", "get")
                        # 普攻每次斩击造成伤害时有30%概率对场上其他任一敌人造成本次斩击伤害150%的间接伤害
                        if "ethereal" in user.buff:
                            local_config.skill_log_data["幻镜化物"] = int(1.5 * left_final_damage)
                        # 每次斩击有8%|10%|12%|14%|16%固定概率降低对方20%治疗效果和护盾强效，持续1回合
                        if "ethereal" in user.buff and skill.name == "青影瞬杀阵":
                            temp_ratio_lists = [0.08, 0.1, 0.12, 0.14, 0.16]
                            if temp_ratio_lists[skill.level - 1] > renpy.random.random():
                                buff_obj = getattr(store, "handicapped")
                                item = (1, 0.2)
                                buff_obj.calculate(self, None, item, skill.name, "get")
                                buff_obj = getattr(store, "broken")
                                item = (1, 0.2)
                                buff_obj.calculate(self, None, item, skill.name, "get")
                        # 自身受到伤害时对施术者造成此次伤害10%|10%|15%|15%|20%的间接伤害，被嘲讽单位伤害提升至20%|20%|25%|25%|30%
                        if ("不可攻略", True) in enemy_environment_effects and self.name == "藤原瞳":
                            renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("反伤", style="effect_text", color="ff9"))
                            # renpy.pause(0.5 * persistent.battlespeed)

                            temp_selected_skills = self.base_skills if not self.is_phase2 else self.base_skills_v2
                            fake_tyt_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]

                            temp_max_range = [0.1, 0.1, 0.13, 0.13, 0.16]
                            if "ridicule" in user.debuff:
                                temp_ratio_lists = [0.2, 0.2, 0.25, 0.25, 0.3]
                                damage_number = int(temp_ratio_lists[fake_tyt_passive.level - 1] * left_final_damage) if temp_ratio_lists[fake_tyt_passive.level - 1] * left_final_damage <= self.battle_max_hp * temp_max_range[fake_tyt_passive.level - 1] else int(self.battle_max_hp * temp_max_range[fake_tyt_passive.level - 1])
                            else:
                                temp_ratio_lists = [0.1, 0.1, 0.15, 0.15, 0.2]
                                damage_number = int(temp_ratio_lists[fake_tyt_passive.level - 1] * left_final_damage) if temp_ratio_lists[fake_tyt_passive.level - 1] * left_final_damage <= self.battle_max_hp * temp_max_range[fake_tyt_passive.level - 1] else int(self.battle_max_hp * temp_max_range[fake_tyt_passive.level - 1])
                            user.hp -= damage_number
                            if user.hp < 1:
                                user.hp = 0
                            user.death_calculate(self, skill, enemy_environment_effects, ally_environment_effects, order_members)
                        # 共感：期间任一附加了“心”的单位受到伤害时，将平均分担给其他同样拥有此印记的友方
                        if "共感" in local_config.skill_log_data:
                            buff_roles = local_config.skill_log_data["共感"]
                            if self in local_config.party and "ally" in buff_roles:
                                temp_buff_roles = copy(buff_roles["ally"])
                                left_final_damage = left_final_damage // len(temp_buff_roles)

                                fake_xz_role = [role for role in local_config.party[:3] if role.name == "青木翔子"][0]
                                temp_selected_skills = fake_xz_role.base_skills if not fake_xz_role.is_phase2 else fake_xz_role.base_skills_v2
                                fake_xz_breakout = [s for s in temp_selected_skills if s.category == "Break_out"][0]
                                
                                temp_ratio_lists = [0.1, 0.13, 0.16, 0.19, 0.22]
                                for role in temp_buff_roles:
                                    if role != self and role.hp > 0:
                                        role_left_final_damage = int(temp_ratio_lists[fake_xz_breakout.level - 1] * role.battle_max_hp) if left_final_damage > temp_ratio_lists[fake_xz_breakout.level - 1] * role.battle_max_hp else left_final_damage
                                        role.hp -= role_left_final_damage
                                        if role.hp < 1:
                                            role.hp = 0
                                        role.death_calculate(user, skill, ally_environment_effects, enemy_environment_effects, order_members)
                            elif self in local_config.enemy and "enemy" in buff_roles:
                                temp_buff_roles = copy(buff_roles["enemy"])
                                left_final_damage = left_final_damage // len(temp_buff_roles)

                                fake_xz_role = [role for role in local_config.enemy[:3] if role.name == "青木翔子"][0]
                                temp_selected_skills = fake_xz_role.base_skills if not fake_xz_role.is_phase2 else fake_xz_role.base_skills_v2
                                fake_xz_breakout = [s for s in temp_selected_skills if s.category == "Break_out"][0]
                                
                                temp_ratio_lists = [0.1, 0.13, 0.16, 0.19, 0.22]
                                for role in temp_buff_roles:
                                    if role != self and role.hp > 0:
                                        role_left_final_damage = int(temp_ratio_lists[fake_xz_breakout.level - 1] * role.battle_max_hp) if left_final_damage > temp_ratio_lists[fake_xz_breakout.level - 1] * role.battle_max_hp else left_final_damage
                                        role.hp -= role_left_final_damage
                                        if role.hp < 1:
                                            role.hp = 0
                                        role.death_calculate(user, skill, ally_environment_effects, enemy_environment_effects, order_members)
                        # 祝福涓流：使用“流流舞”造成伤害时，每次为生命比例最低的友方角色治疗该次伤害60%|70%|80%|90%|100%的生命；有8%|10%|12%|14%|16%概率降低对方20%效果命中和效果抵抗，持续2回合
                        if ("祝福涓流", True) in ally_environment_effects and skill.name == "流流舞":
                            min_hp_role = user
                            min_hp_ratio = 1.0
                            if user in local_config.party:
                                for role in local_config.party[:3]:
                                    if role.hp > 0 and (role.hp / role.battle_max_hp) < min_hp_ratio:
                                        min_hp_role = role
                                        min_hp_ratio = (role.hp / role.battle_max_hp)
                            elif user in local_config.enemy:
                                for role in local_config.enemy[:3]:
                                    if role.hp > 0 and (role.hp / role.battle_max_hp) < min_hp_ratio:
                                        min_hp_role = role
                                        min_hp_ratio = (role.hp / role.battle_max_hp)

                            temp_selected_skills = user.base_skills if not user.is_phase2 else user.base_skills_v2
                            fake_yj_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]

                            if min_hp_ratio != 1.0:                                
                                # 基础治疗量
                                temp_ratio_lists = [0.6, 0.7, 0.8, 0.9, 1.0]
                                battle_base_healing = temp_ratio_lists[fake_yj_passive.level - 1] * left_final_damage

                                # 暴击判定
                                judgerate = renpy.random.random()
                                battle_critical = battle_user_critical_rate >= judgerate
                                
                                if battle_critical:
                                    single_battle_healing = battle_base_healing * battle_user_critical_damage * (1.0 + battle_user_healing_bonus)
                                    single_battle_healing = int(single_battle_healing)
                                    renpy.show("hcritical", at_list=[show_damage(min_hp_role.xposition, 0.35)], layer="screens", what=Text("治疗暴击", style="effect_text", size=80, color="#ee6"))
                                    renpy.show("healing", at_list=[show_damage(min_hp_role.xposition, 0.5)], layer="healing", what=Text("+%s" % single_battle_healing, style="damage_text", size=150, color=damage_color_map["治疗"]))
                                    # renpy.pause(0.5 * persistent.battlespeed)
                                else:
                                    single_battle_healing = battle_base_healing * (1.0 + battle_user_healing_bonus)
                                    single_battle_healing = int(single_battle_healing)
                                    renpy.show("healing", at_list=[show_damage(min_hp_role.xposition, 0.5)], layer="healing", what=Text("+%s" % single_battle_healing, style="damage_text", size=100, color=damage_color_map["治疗"]))
                                    # renpy.pause(0.5 * persistent.battlespeed)

                                if single_battle_healing > 0:
                                    renpy.music.play("恢复", channel="battle_music")

                                    min_hp_role.hp += single_battle_healing
                                    if min_hp_role.hp > min_hp_role.battle_max_hp:
                                        min_hp_role.hp = min_hp_role.battle_max_hp
                            
                            temp_ratio_lists = [0.08, 0.1, 0.12, 0.14, 0.16]
                            if temp_ratio_lists[fake_yj_passive.level - 1] > renpy.random.random():
                                buff_obj = getattr(store, "seal")
                                item = (2, 0.2)
                                buff_obj.calculate(self, None, item, "祝福涓流", "get")
                                buff_obj = getattr(store, "disintegrate")
                                item = (2, 0.2)
                                buff_obj.calculate(self, None, item, "祝福涓流", "get")
                        # 适应
                        if "Adaptive" in self.abilities and 0.08 > renpy.random.random():
                            renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("适应", style="effect_text", color="ff9"))
                            media_shield_strength = int(0.6 * battle_base_attack)
                            # renpy.pause(0.5 * persistent.battlespeed)
                            # renpy.hide("buff_effect", layer="screens")

                            # 无盾或同属性才能触发
                            if "shield" in self.buff:
                                buff_obj = getattr(store, "shield")
                                shield_time, (shield_strength, shield_element, v1, v2) = self.buff["shield"]
                                if shield_element == battle_skill_element:
                                    item = (2, (media_shield_strength, shield_element, v1, v2))
                                    buff_obj.calculate(self, None, item, "Adaptive", "get")
                            elif "sp_shield" in self.buff:
                                buff_obj = getattr(store, "sp_shield")
                                shield_time, (shield_strength, shield_element, v1, v2) = self.buff["sp_shield"]
                                if shield_element == battle_skill_element:
                                    item = (2, (media_shield_strength, shield_element, v1, v2))
                                    buff_obj.calculate(self, None, item, "Adaptive", "get")
                            else:
                                buff_obj = getattr(store, "shield")
                                item = (2, (media_shield_strength, battle_skill_element, 0.75, 0.5))
                                buff_obj.calculate(self, None, item, "Adaptive", "get")
                        # 皮肤
                        if "Skin" in self.abilities and (left_final_damage / self.battle_max_hp) > 0.3 and (self.hp > left_final_damage) and 0.2 > renpy.random.random():
                            # 在伤害结算后获得30%的对应元素抗性
                            item = None
                            if battle_skill_element == "fire":
                                item = (2, (0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
                            elif battle_skill_element == "light":
                                item = (2, (0.0, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0))
                            elif battle_skill_element == "wind":
                                item = (2, (0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0))
                            elif battle_skill_element == "ice":
                                item = (2, (0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0))
                            elif battle_skill_element == "water":
                                item = (2, (0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0))
                            elif battle_skill_element == "rock":
                                item = (2, (0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0))

                            if item is not None:
                                renpy.music.play("raged", channel="battle_music")
                                renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("抗性提升", style="effect_text", color="ff9"))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                # renpy.hide("buff_effect")

                                buff_obj = getattr(store, "control")
                                buff_obj.calculate(self, None, item, "Skin", "get")
                        # 格挡
                        if "Solid" in self.abilities and (left_final_damage / self.battle_max_hp) > 0.3 and (self.hp > left_final_damage) and 0.2 > renpy.random.random():
                            # 在伤害结算时获得30%的物理抗性
                            item = None
                            if battle_skill_element == "physical":
                                item = (2, (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3))

                            if item is not None:
                                renpy.music.play("raged", channel="battle_music")
                                renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("抗性提升", style="effect_text", color="ff9"))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                # renpy.hide("buff_effect")

                                buff_obj = getattr(store, "control")
                                buff_obj.calculate(self, None, item, "Solid", "get")
                        # 回响 & 狩猎
                        if con_hun_flag:
                            if battle_critical:
                                renpy.show("healing", at_list=[show_damage(user.xposition, 0.5)], layer="screens", what=Text("+10", style="damage_text", size=100, color="#19f"))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                # renpy.hide("healing", layer="screens")

                                user.mp += 10
                                if user.mp > user.max_mp:
                                    user.mp = user.max_mp
                        # 天之印-碧落
                        if user.equip4effect == "天之印-碧落" and ("天之印-碧落", True) in ally_environment_effects:
                            if 0.15 > renpy.random.random():
                                if "domineering" in self.buff or "sp_domineering" in self.buff:
                                    renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("霸体免控", style="effect_text", color="ff9"))
                                    # renpy.pause(0.5 * persistent.battlespeed)
                                    # renpy.hide("buff_effect", layer="screens")
                                else:
                                    buff_lists = ["dizziness", "silence", "sleepy", "handicapped"]
                                    buff_items = [(1, None), (1, None), (1, None), (1, 0.4)]
                                    chosen_index = renpy.random.randint(0, len(buff_lists)-1)
                                    chosen_buff = buff_lists[chosen_index]
                                    chosen_item = buff_items[chosen_index]

                                    buff_obj = getattr(store, chosen_buff)
                                    buff_obj.calculate(self, None, chosen_item, "天之印-碧落", "get")
                        # 地之轴-方仪
                        if self.equip4effect == "地之轴-方仪" and ("地之轴-方仪", True) in enemy_environment_effects and battle_critical:
                            if 0.3 > renpy.random.random():
                                if self in local_config.party:
                                    for role in local_config.party[:3]:
                                        if role.hp > 0:
                                            if "shield" in role.buff:
                                                buff_obj = getattr(store, "shield")
                                                shield_time, (shield_strength, shield_element, v1, v2) = role.buff["shield"]
                                                if shield_element == battle_skill_element:
                                                    item = (1, (int(0.1 * self.battle_max_hp), battle_skill_element, v1, v2))
                                                    buff_obj.calculate(role, None, item, "地之轴-方仪", "get")
                                            elif "sp_shield" in role.buff:
                                                buff_obj = getattr(store, "sp_shield")
                                                shield_time, (shield_strength, shield_element, v1, v2) = role.buff["sp_shield"]
                                                if shield_element == battle_skill_element:
                                                    item = (1, (int(0.1 * self.battle_max_hp), battle_skill_element, v1, v2))
                                                    buff_obj.calculate(role, None, item, "地之轴-方仪", "get")
                                            else:
                                                buff_obj = getattr(store, "shield")
                                                item = (1, (int(0.1 * self.battle_max_hp), battle_skill_element, 0.75, 0.5))
                                                buff_obj.calculate(role, None, item, "地之轴-方仪", "get")
                        # 海之澜-沧渊
                        if user.equip4effect == "海之澜-沧渊" and ("海之澜-沧渊", True) in ally_environment_effects:
                            tmp_buff_lists = [buf_name for buf_name, item_name in self.buff.items() if item_name[0] != 99]
                            if (len(tmp_buff_lists) > 0 and 0.3 > renpy.random.random()) or (len(tmp_buff_lists) == 0 and 0.2 > renpy.random.random()):
                                self.order -= 300
                        # 风之陨-松吹
                        if ("风之陨-松吹", True) in enemy_environment_effects:
                            buff_roles = local_config.skill_log_data.setdefault("风之陨-松吹", {})
                            if user not in buff_roles:
                                if 0.2 > renpy.random.random():
                                    renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("能量损失", style="effect_text", color="ff9"))
                                    # renpy.pause(0.5 * persistent.battlespeed)
                                    # renpy.hide("buff_effect", layer="screens")
                                    user.mp -= 10
                                    if user.mp < 0:
                                        user.mp = 0
                        # 雪之嚣-玉絮
                        if user.equip4effect == "雪之嚣-玉絮" and ("雪之嚣-玉絮", True) in ally_environment_effects:
                            frozen_ratio = 0.2 if "slow" in self.debuff else 0.12

                            # 技能效果命中率 = 技能基础命中 x (1 + 面板效果命中)
                            battle_effect_hitrate_final = frozen_ratio * (1 + battle_user_effect_hitrate)
                            # 技能效果抵抗率 = 1 - 100% / (100% + 面板效果抵抗)
                            battle_effect_resistance_final = 1.0 - 1.0 / (1.0 + battle_target_effect_resistance)

                            # 命中判定
                            if battle_effect_hitrate_final > renpy.random.random():
                                if "domineering" in self.buff or "sp_domineering" in self.buff:
                                    renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("霸体免控", style="effect_text", color="ff9"))
                                    # renpy.pause(0.5 * persistent.battlespeed)
                                    # renpy.hide("buff_effect", layer="screens")
                                # 抵抗判定
                                elif battle_effect_resistance_final < renpy.random.random():
                                    renpy.show("elemental", at_list=[show_state(self.xposition)], layer="screens", what=Text("冻结", style="effect_text", size=80, color=damage_color_map["冻结"]))
                                    buff_obj = getattr(store, "frozen")
                                    item = (1, 0.5)
                                    buff_obj.calculate(self, None, item, "雪之嚣-玉絮", "get")
                                else:
                                    renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("抵抗", style="effect_text", color="ff9"))
                                    # renpy.pause(0.5 * persistent.battlespeed)
                        if self.equip4effect == "雪之嚣-玉絮" and ("雪之嚣-玉絮", True) in enemy_environment_effects:
                            if 0.3 > renpy.random.random():
                                renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("减速", style="effect_text", color="ff9"))
                                buff_obj = getattr(store, "slow")
                                item = (1, 20)
                                buff_obj.calculate(user, None, item, "雪之嚣-玉絮", "get")
                        # 瓦轮刑部结界
                        if "rock_wall" in self.buff:
                            left_final_damage = max(1, int(left_final_damage * 0.1))
                        # 队友守护
                        if "sp_protect" in self.buff:
                            renpy.show("critical", at_list=[show_damage(self.xposition, 0.35)], layer="screens", what=Text("无效", style="effect_text", size=80, color="#ee6"))
                            if local_config.tutorial_step == "虚无封印":
                                left_final_damage = 1
                            else:
                                left_final_damage = 0

                        if "伤害记录" in local_config.skill_log_data and self in local_config.enemy:
                            local_config.skill_log_data["伤害记录"] += left_final_damage
                            yj_role.hp += left_final_damage
                            if yj_role.hp > yj_role.battle_max_hp:
                                yj_role.hp = yj_role.battle_max_hp

                        # 伤害音效、数值显示
                        if battle_critical:
                            renpy.music.play("critical_hit", channel="battle_music")
                            renpy.show("critical", at_list=[show_damage(self.xposition, 0.35)], layer="screens", what=Text("暴击", style="effect_text", size=80, color="#ee6"))
                            renpy.show("damage", at_list=[show_damage(self.xposition, 0.5)], layer="damage", what=Text("%s" % left_final_damage, style="damage_text", size=150, color=damage_color_map[battle_skill_element]))
                        else:
                            renpy.music.play("hit", channel="battle_music")
                            renpy.show("damage", at_list=[show_damage(self.xposition, 0.5)], layer="damage", what=Text("%s" % left_final_damage, style="damage_text", size=100, color=damage_color_map[battle_skill_element]))

                        # 表情更新
                        self.face_change(hit=False, hitted=True)
                        # 受到伤害角色抖动特效
                        if self in local_config.party:
                            renpy.show(self.objectname, at_list=[shake, hide_out], layer="fg")
                        else:
                            renpy.show(self.objectname, at_list=[smallshake])

                        self.hp -= left_final_damage
                        if self.hp < 1:
                            self.hp = 0
                        
                        if sp_rull == "空间跳跃":
                            fake_lst_role = None
                            if user in local_config.party:
                                for temp_role in local_config.party:
                                    if temp_role.name == "雷亚":
                                        fake_lst_role = temp_role
                            else:
                                for temp_role in local_config.enemy:
                                    if temp_role.name == "雷亚":
                                        fake_lst_role = temp_role
                            temp_selected_skill = fake_lst_role.skills if not fake_lst_role.is_phase2 else fake_lst_role.skills_v2
                            fake_lst_skill = [s for s in temp_selected_skill if s.category == "Break_out"][0]

                            if fake_lst_skill.level > 1:
                                temp_ratio_lists = [0.0, 0.2, 0.3, 0.4, 0.4]
                                temp_dmg_healing = int(left_final_damage * temp_ratio_lists[fake_lst_skill.level - 1])
                                renpy.show("healing", at_list=[show_damage(user.xposition, 0.5)], layer="healing", what=Text("+%s" % temp_dmg_healing, style="damage_text", size=100, color=damage_color_map["治疗"]))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                user.hp += temp_dmg_healing
                                if user.hp > user.battle_max_hp:
                                    user.hp = user.battle_max_hp
                        # renpy.pause(0.75 * persistent.battlespeed)
                    else:
                        # 伤害音效、数值显示
                        if battle_critical:
                            renpy.music.play("critical_hit", channel="battle_music")
                            # renpy.pause(0.05)

                            renpy.show("critical", at_list=[show_damage(self.xposition, 0.35)], layer="screens", what=Text("暴击", style="effect_text", size=80, color="#ee6"))
                            renpy.show("damage", at_list=[show_damage(self.xposition, 0.5)], layer="damage", what=Text("0", style="damage_text", size=150, color=damage_color_map[battle_skill_element]))
                        else:
                            renpy.music.play("hit", channel="battle_music")
                            # renpy.pause(0.05)

                            renpy.show("damage", at_list=[show_damage(self.xposition, 0.5)], layer="damage", what=Text("0", style="damage_text", size=100, color=damage_color_map[battle_skill_element]))

                        # 受到伤害角色抖动特效
                        if self in local_config.party:
                            renpy.show(self.objectname, at_list=[shake, hide_out], layer="fg")
                        else:
                            renpy.show(self.objectname, at_list=[smallshake])
                        # renpy.pause(0.75 * persistent.battlespeed)

                    ## 元素反应
                    # 聚变、形态反应（超载：攻击力200%火元素伤害、冻结：20%基础概率冻结、感电：125%攻击固定数值间接伤害、超导：40%物理抗性衰减、扩散：40%对应元素抗性衰减、结晶：攻击力60%元素护盾获得）
                    # 火->雷 or 雷->火 | 超载反应伤害 = 基础伤害 x (1 + 元素精通加成) x 火元素最终抗性
                    battle_overload_damage = 0.0
                    if (battle_skill_element == "fire" and "light" in self.ebuff) or (battle_skill_element == "light" and "fire" in self.ebuff):
                        battle_target_fire_elemental_resistance = self.battle_fire_elemental_resistance
                        if battle_target_fire_elemental_resistance >= 0:
                            battle_fire_resistance_damage_rate = 1 - battle_target_fire_elemental_resistance
                        else:
                            battle_fire_resistance_damage_rate = 1 - (0.5 * battle_target_fire_elemental_resistance)

                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            battle_overload_damage = int(battle_fundamental_damage * (2.4 + battle_elemental_mastery_bonus2) * battle_fire_resistance_damage_rate)
                        else:
                            battle_overload_damage = int(battle_fundamental_damage * (2.0 + battle_elemental_mastery_bonus2) * battle_fire_resistance_damage_rate)

                        if "light" in self.ebuff:
                            self.ebuff["light"] -= 2
                            if self.ebuff["light"] <= 0:
                                self.ebuff.pop("light")
                        elif "fire" in self.ebuff:
                            self.ebuff["fire"] -= 2
                            if self.ebuff["fire"] <= 0:
                                self.ebuff.pop("fire")

                        inner_react = True

                        overload_left_final_damage = battle_overload_damage
                        # 护盾抵消（伤害计算优先扣除护盾）
                        if "sp_shield" in self.buff:
                            shield_time, shield_effects = self.buff["sp_shield"]
                            shield_strength, shield_element, _, _ = shield_effects
                            shield_damage_ratio = 1.0
                            # 属性克制（强势1.5倍、弱势0.5倍）
                            if shield_element == "ice":
                                shield_damage_ratio = 1.5
                            elif shield_element == "water":
                                shield_damage_ratio = 0.5
                            # 属性调和（0.25倍）
                            elif shield_element == "fire":
                                shield_damage_ratio = 0.25

                            left_shield_strength = int(shield_strength - shield_damage_ratio * battle_overload_damage)
                            # 如果护盾还未消失，更新护盾
                            shield_buff = getattr(store, "sp_shield")
                            item = (shield_time, (left_shield_strength, shield_element, 0.75, 0.5))
                            shield_buff.calculate(self, None, item, None, "get")
                            overload_left_final_damage = 0.0

                            # 如果护盾破碎，驱散护盾并结算剩余伤害
                            if "sp_shield" not in self.buff:
                                # 穿透伤害
                                if left_shield_strength < 0:
                                    overload_left_final_damage = -int(left_shield_strength/shield_damage_ratio)
                        if "shield" in self.buff:
                            shield_time, shield_effects = self.buff["shield"]
                            shield_strength, shield_element, _, _ = shield_effects
                            shield_damage_ratio = 1.0
                            # 属性克制（强势1.5倍、弱势0.5倍）
                            if shield_element == "ice":
                                shield_damage_ratio = 1.5
                            elif shield_element == "water":
                                shield_damage_ratio = 0.5
                            # 属性调和（0.25倍）
                            elif shield_element == "fire":
                                shield_damage_ratio = 0.25

                            left_shield_strength = int(shield_strength - shield_damage_ratio * battle_overload_damage)
                            # 更新护盾
                            shield_buff = getattr(store, "shield")
                            item = (shield_time, (left_shield_strength, shield_element, 0.75, 0.5))
                            shield_buff.calculate(self, None, item, None, "get")
                            overload_left_final_damage = 0.0
                            
                            # 如果护盾破碎，驱散护盾并结算剩余伤害
                            if "shield" not in self.buff:
                                # 穿透伤害
                                if left_shield_strength < 0:
                                    overload_left_final_damage = -int(left_shield_strength/shield_damage_ratio)

                        renpy.music.play("critical_hit", channel="battle_music")
                        # renpy.pause(0.05)

                        # 队友守护
                        if "sp_protect" in self.buff:
                            renpy.show("critical", at_list=[show_damage(self.xposition, 0.35)], layer="screens", what=Text("无效", style="effect_text", size=80, color="#ee6"))
                            if local_config.tutorial_step == "虚无封印":
                                overload_left_final_damage = 1
                            else:
                                overload_left_final_damage = 0

                        if overload_left_final_damage > 0.0:
                            renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("超载", style="effect_text", size=80, color=damage_color_map["超载"]))
                            renpy.show("damage", at_list=[show_damage(self.xposition, 0.4)], layer="damage_element", what=Text("%s" % overload_left_final_damage, style="damage_text", size=100, color=damage_color_map["超载"]))
                            # 角色伤害承受
                            # 表情更新
                            self.face_change(hit=False, hitted=True)
                            # 受到伤害角色抖动特效
                            if self in local_config.party:
                                renpy.show(self.objectname, at_list=[shake, hide_out], layer="fg")
                            else:
                                renpy.show(self.objectname, at_list=[smallshake])
                            # renpy.pause(0.75 * persistent.battlespeed)

                            # 解除“瓦轮刑部”结界
                            if "rock_wall" in self.buff:
                                buff_obj = getattr(store, "rock_wall")
                                buff_obj.calculate(self, None, None, None, "clean")

                            if "伤害记录" in local_config.skill_log_data and self in local_config.enemy:
                                local_config.skill_log_data["伤害记录"] += overload_left_final_damage
                                yj_role.hp += overload_left_final_damage
                                if yj_role.hp > yj_role.battle_max_hp:
                                    yj_role.hp = yj_role.battle_max_hp

                            self.hp -= overload_left_final_damage
                            if self.hp < 1:
                                self.hp = 0

                            # “遗念镜”祝福
                            if self in local_config.party and "超载" in local_config.battle_blessing and 0.4 > renpy.random.random():
                                self.order -= local_config.battle_blessing["超载"]
                    # 冻结 = 20% x (1 + 元素精通加成)
                    if (battle_skill_element == "ice" and "water" in self.ebuff) or (battle_skill_element == "water" and "ice" in self.ebuff):
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            reaction_frozen_ratio = 0.3 * (1 + battle_elemental_mastery_bonus)
                        else:
                            reaction_frozen_ratio = 0.2 * (1 + battle_elemental_mastery_bonus)

                        # “遗念镜”祝福
                        if self in local_config.party and "冻结" in local_config.battle_blessing:
                            reaction_frozen_ratio += local_config.battle_blessing["冻结"]

                        # 技能效果命中率 = 技能基础命中 x (1 + 面板效果命中)
                        battle_effect_hitrate_final = reaction_frozen_ratio * (1 + battle_user_effect_hitrate)
                        # 技能效果抵抗率 = 1 - 100% / (100% + 面板效果抵抗)
                        battle_effect_resistance_final = 1.0 - 1.0 / (1.0 + battle_target_effect_resistance)

                        # 命中判定
                        if battle_effect_hitrate_final > renpy.random.random():
                            if "domineering" in self.buff or "sp_domineering" in self.buff:
                                renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("霸体免控", style="effect_text", color="ff9"))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                # renpy.hide("buff_effect", layer="screens")
                            # 抵抗判定
                            elif battle_effect_resistance_final < renpy.random.random():
                                hitted = True
                                renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("冻结", style="effect_text", size=80, color=damage_color_map["冻结"]))
                                buff_obj = getattr(store, "frozen")
                                item = (2, 0.5)
                                buff_obj.calculate(self, None, item, "frozen-reaction", "get")
                                if "ice" in self.ebuff:
                                    self.ebuff["ice"] = max(self.ebuff["ice"], 1)
                                else:
                                    self.ebuff = {"ice": 1}
                            else:
                                renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("抵抗", style="effect_text", color="ff9"))
                                # renpy.pause(0.5)

                        if "water" in self.ebuff:
                            self.ebuff["water"] -= 2
                            if self.ebuff["water"] <= 0:
                                self.ebuff.pop("water")
                        elif "ice" in self.ebuff:
                            self.ebuff["ice"] -= 2
                            if self.ebuff["ice"] <= 0:
                                self.ebuff.pop("ice")

                        inner_react = True
                    # 感电 = 125%攻击固定数值间接伤害 x (1 + 元素精通加成)
                    if (battle_skill_element == "water" and "light" in self.ebuff) or (battle_skill_element == "light" and "water" in self.ebuff):
                        renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("感电", style="effect_text", size=80, color=damage_color_map["感电"]))
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            media_damage_number = int(battle_base_attack * (1.65 + battle_elemental_mastery_bonus2))
                        else:
                            media_damage_number = int(battle_base_attack * (1.25 + battle_elemental_mastery_bonus2))
                        hitted = True
                        buff_obj = getattr(store, "mdamage")
                        item = (2, (media_damage_number, "light", "感电", user))
                        buff_obj.calculate(self, None, item, "induct-reaction", "get")
                        buff_roles = local_config.skill_log_data.setdefault("间接伤害", {})
                        buff_roles[self] = (media_damage_number, "light", "感电", user)

                        if "water" in self.ebuff:
                            self.ebuff["water"] -= 2
                            if self.ebuff["water"] <= 0:
                                self.ebuff.pop("water")
                        elif "light" in self.ebuff:
                            self.ebuff["light"] -= 2
                            if self.ebuff["light"] <= 0:
                                self.ebuff.pop("light")

                        inner_react = True
                    # 超导 = 70%物理抗性衰减
                    if (battle_skill_element == "ice" and "light" in self.ebuff) or (battle_skill_element == "light" and "ice" in self.ebuff):
                        renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("超导", style="effect_text", size=80, color=damage_color_map["超导"]))
                        buff_obj = getattr(store, "suppress")
                        hitted = True
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            tmp_ratio_down = 0.85
                        else:
                            tmp_ratio_down = 0.7
                        item = (2, (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tmp_ratio_down))
                        buff_obj.calculate(self, None, item, "superconduct-reaction", "get")

                        if "ice" in self.ebuff:
                            self.ebuff["ice"] -= 2
                            if self.ebuff["ice"] <= 0:
                                self.ebuff.pop("ice")
                        elif "light" in self.ebuff:
                            self.ebuff["light"] -= 2
                            if self.ebuff["light"] <= 0:
                                self.ebuff.pop("light")

                        inner_react = True
                    # 扩散 = 40%对应元素抗性衰减
                    if battle_skill_element == "wind" and ("fire" in self.ebuff or "light" in self.ebuff or "water" in self.ebuff or "ice" in self.ebuff):
                        renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("扩散", style="effect_text", size=80, color=damage_color_map["扩散"]))
                        buff_obj = getattr(store, "suppress")
                        hitted = True
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            tmp_ratio_down = 0.55
                        else:
                            tmp_ratio_down = 0.4
                        if "fire" in self.ebuff:
                            item = (2, (tmp_ratio_down, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
                        elif "light" in self.ebuff:
                            item = (2, (0.0, tmp_ratio_down, 0.0, 0.0, 0.0, 0.0, 0.0))
                        elif "water" in self.ebuff:
                            item = (2, (0.0, 0.0, 0.0, 0.0, tmp_ratio_down, 0.0, 0.0))
                        elif "ice" in self.ebuff:
                            item = (2, (0.0, 0.0, 0.0, tmp_ratio_down, 0.0, 0.0, 0.0))
                        buff_obj.calculate(self, None, item, "diffusion-reaction", "get")

                        if "ice" in self.ebuff:
                            self.ebuff["ice"] -= 2
                            if self.ebuff["ice"] <= 0:
                                self.ebuff.pop("ice")
                        elif "light" in self.ebuff:
                            self.ebuff["light"] -= 2
                            if self.ebuff["light"] <= 0:
                                self.ebuff.pop("light")
                        elif "fire" in self.ebuff:
                            self.ebuff["fire"] -= 2
                            if self.ebuff["fire"] <= 0:
                                self.ebuff.pop("fire")
                        elif "water" in self.ebuff:
                            self.ebuff["water"] -= 2
                            if self.ebuff["water"] <= 0:
                                self.ebuff.pop("water")

                        inner_react = True
                    # 结晶 = 获得攻击力60%元素护盾
                    if battle_skill_element == "rock" and ("fire" in self.ebuff or "light" in self.ebuff or "water" in self.ebuff or "ice" in self.ebuff):
                        renpy.show("elemental", at_list=[show_state(self.xposition, 0.25)], layer="buff_element", what=Text("结晶", style="effect_text", size=80, color=damage_color_map["结晶"]))
                        if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                            media_shield_strength = int(0.85 * battle_base_attack)
                        else:
                            media_shield_strength = int(0.6 * battle_base_attack)

                        if "fire" in self.ebuff:
                            gain_element = "fire"
                        elif "light" in self.ebuff:
                            gain_element = "light"
                        elif "water" in self.ebuff:
                            gain_element = "water"
                        elif "ice" in self.ebuff:
                            gain_element = "ice"
                        
                        # 无盾或同属性才能触发
                        if "shield" in user.buff:
                            buff_obj = getattr(store, "shield")
                            shield_time, (shield_strength, shield_element, v1, v2) = user.buff["shield"]
                            if shield_element == gain_element:
                                item = (2, (media_shield_strength, shield_element, v1, v2))
                                buff_obj.calculate(user, None, item, "crystallization-reaction", "get")
                        elif "sp_shield" in user.buff:
                            buff_obj = getattr(store, "sp_shield")
                            shield_time, (shield_strength, shield_element, v1, v2) = user.buff["sp_shield"]
                            if shield_element == gain_element:
                                item = (2, (media_shield_strength, shield_element, v1, v2))
                                buff_obj.calculate(user, None, item, "crystallization-reaction", "get")
                        else:
                            buff_obj = getattr(store, "shield")
                            item = (2, (media_shield_strength, gain_element, 0.75, 0.5))
                            buff_obj.calculate(user, None, item, "crystallization-reaction", "get")

                        if "ice" in self.ebuff:
                            self.ebuff["ice"] -= 2
                            if self.ebuff["ice"] <= 0:
                                self.ebuff.pop("ice")
                        elif "light" in self.ebuff:
                            self.ebuff["light"] -= 2
                            if self.ebuff["light"] <= 0:
                                self.ebuff.pop("light")
                        elif "fire" in self.ebuff:
                            self.ebuff["fire"] -= 2
                            if self.ebuff["fire"] <= 0:
                                self.ebuff.pop("fire")
                        elif "water" in self.ebuff:
                            self.ebuff["water"] -= 2
                            if self.ebuff["water"] <= 0:
                                self.ebuff.pop("water")

                        inner_react = True

                    # 元素附着（本身无元素附着 or 附着元素相同）
                    # 发生元素反应后不附着
                    if not inner_react:
                        if ("Skin" not in self.abilities) or ("Skin" in self.abilities and 0.5 > renpy.random.random()):
                            if battle_skill_element in self.ebuff:
                                self.ebuff[battle_skill_element] += 1
                            elif battle_skill_element and battle_skill_element not in ["wind", "rock", "physical"] and len(self.ebuff) == 0:
                                self.ebuff[battle_skill_element] = 1

                    renpy.pause(0.75 * persistent.battlespeed)

            # 治疗 = 技能基础治疗量 x 爆伤 x (1 + 治疗加成)
            if "治疗" in skill.effects:
                battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack = self.battle_role_init(user, self, ally_environment_effects, enemy_environment_effects, sp_rull)
                ratio, target, _ = skill.effects["治疗"]

                if not isinstance(ratio, list):
                    ratio = [ratio]
                if not isinstance(target, list):
                    target = [target]

                for rat, tar in zip(ratio, target):
                    if tar == "base_attack":
                        role_attribute = battle_base_attack
                    else:
                        role_attribute = getattr(self, "battle_%s" % tar)
                    # 基础治疗量
                    battle_base_healing = rat * role_attribute

                    # 暴击判定
                    judgerate = renpy.random.random()
                    battle_critical = battle_user_critical_rate >= judgerate

                    if battle_critical:
                        single_battle_healing = battle_base_healing * battle_user_critical_damage * (1.0 + battle_user_healing_bonus)
                        single_battle_healing = int(single_battle_healing)
                        renpy.show("critical", at_list=[show_state(self.xposition, 0.35)], layer="screens", what=Text("治疗暴击", style="effect_text", size=80, color="#ee6"))
                        renpy.show("healing", at_list=[show_damage(self.xposition, 0.5)], layer="healing", what=Text("+%s" % single_battle_healing, style="damage_text", size=150, color=damage_color_map["治疗"]))
                        # renpy.pause(0.5 * persistent.battlespeed)
                    else:
                        single_battle_healing = battle_base_healing * (1.0 + battle_user_healing_bonus)
                        single_battle_healing = int(single_battle_healing)
                        renpy.show("healing", at_list=[show_damage(self.xposition, 0.5)], layer="healing", what=Text("+%s" % single_battle_healing, style="damage_text", size=100, color=damage_color_map["治疗"]))
                        # renpy.pause(0.5 * persistent.battlespeed)

                    if single_battle_healing > 0:
                        renpy.music.play("恢复", channel="battle_music")
                        # renpy.pause(0.05)

                        self.hp += int(single_battle_healing)
                        if self.hp > self.battle_max_hp:
                            self.hp = self.battle_max_hp

            # 护盾 = 技能基础护盾量 x (1 + 护盾强效)
            if "护盾" in skill.effects:
                battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack = self.battle_role_init(user, self, ally_environment_effects, enemy_environment_effects, sp_rull)
                ratio, target, time = skill.effects["护盾"]
                shield_element = skill.element

                if not isinstance(ratio, tuple):
                    ratio = [ratio]
                if not isinstance(target, tuple):
                    target = [target]

                for rat, tar, ele in zip(ratio, target, shield_element):
                    # 基础护盾量
                    role_attribute = getattr(self, "battle_%s" % tar)
                    battle_base_shield_strength = rat * role_attribute
                    single_battle_shield_strength = battle_base_shield_strength * (1 + battle_user_shield_strength)

                    if single_battle_shield_strength > 0:
                        buff_obj = getattr(store, "shield")
                        item = (time, (int(single_battle_shield_strength), ele, 0.75, 0.5))
                        buff_obj.calculate(self, None, item, skill.name, "get")
            ## 附加buff
            # 拉条
            if "拉条" in skill.effects:
                ratio, target, time = skill.effects["拉条"]

                if ratio > 0.0:
                    # 思维透视
                    if skill.name == "思维透视":
                        disable = False
                        for debuff in self.debuff:
                            if debuff in ["silence", "dizziness", "confusion", "frozen", "sleepy", "ridicule", "deep_frozen", "deep_sleepy"]:
                                disable = True
                                break
                        # 该角色处于“无法行动”状态则改为解除其控制状态
                        if disable:
                            for debuff in ["silence", "dizziness", "confusion", "frozen", "sleepy", "ridicule", "deep_frozen", "deep_sleepy"]:
                                if debuff in self.debuff:
                                    buff_obj = getattr(store, debuff)
                                    buff_obj.calculate(self, None, None, None, "clean")
                            # 恢复20%|25%|30%|35%|40%生命值
                            temp_ratio_lists = [0.2, 0.25, 0.3, 0.35, 0.4]
                            self.hp += int(self.battle_max_hp * temp_ratio_lists[skill.level - 1])
                            if self.hp > self.battle_max_hp:
                                self.hp = self.battle_max_hp
                            if skill.level in [2, 3, 4, 5]:
                                temp_ratio_lists = [10, 15, 20, 20]
                                # 增加0|10|15|20|20点速度
                                buff_obj = getattr(store, "flow")
                                item = (1, temp_ratio_lists[skill.level - 1])
                                buff_obj.calculate(self, None, item, skill.name, "get")
                        else:
                            self.order += int(ratio * 1000)
                            renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
                    else:
                        self.order += int(ratio * 1000)
                        renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
            
            media_buff_anime = set()
            # 强攻
            if "强攻" in skill.effects:
                ratio, target, time = skill.effects["强攻"]
                if ratio > 0.0:
                    media_buff_anime.add("damage_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "strong")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 强袭
            if "强袭" in skill.effects:
                ratio, target, time = skill.effects["强袭"]
                if ratio > 0.0:
                    media_buff_anime.add("damage_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "violence")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 精通
            if "精通" in skill.effects:
                ratio, target, time = skill.effects["精通"]
                if ratio > 0.0:
                    media_buff_anime.add("damage_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "master")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 精防
            if "精防" in skill.effects:
                ratio, target, time = skill.effects["精防"]
                if ratio > 0.0:
                    media_buff_anime.add("defance_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "sturdy")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 属性强效
            if "属性强效" in skill.effects:
                ratio, target, time = skill.effects["属性强效"]
                if ratio > 0.0:
                    media_buff_anime.add("damage_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "condensed")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 属性抗效
            if "属性抗效" in skill.effects:
                ratio, target, time = skill.effects["属性抗效"]
                if ratio > 0.0:
                    media_buff_anime.add("defance_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "control")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 属性抗衰
            if "属性抗衰" in skill.effects:
                ratio, target, time = skill.effects["属性抗衰"]
                if ratio > 0.0:
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "suppress")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 加速
            if "加速" in skill.effects:
                ratio, target, time = skill.effects["加速"]
                if ratio > 0.0:
                    media_buff_anime.add("speed_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "flow")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 减速
            if "减速" in skill.effects:
                ratio, target, time = skill.effects["减速"]
                if ratio > 0.0:
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "slow")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 抗效
            if "抗效" in skill.effects:
                ratio, target, time = skill.effects["抗效"]
                if ratio > 0.0:
                    media_buff_anime.add("resistance_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "barrier")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 命中
            if "命中" in skill.effects:
                ratio, target, time = skill.effects["命中"]
                if ratio > 0.0:
                    media_buff_anime.add("resistance_up_img")
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "liberate")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 命中衰减
            if "命中衰减" in skill.effects:
                ratio, target, time = skill.effects["命中衰减"]
                if ratio > 0.0:
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "seal")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 抗效衰减
            if "抗效衰减" in skill.effects:
                ratio, target, time = skill.effects["抗效衰减"]
                if ratio > 0.0:
                    if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                        time += 1
                    buff = getattr(store, "disintegrate")
                    item = (time, ratio)
                    buff.calculate(self, None, item, skill.name, "get")
            # 充能
            if "充能" in skill.effects:
                ratio, target, time = skill.effects["充能"]
                renpy.show("damage", at_list=[show_damage(self.xposition, 0.5)], layer="screens", what=Text("+%s" % ratio, style="damage_text", size=100, color=damage_color_map["能量"]))
                # renpy.pause(0.5 * persistent.battlespeed)
                self.mp += ratio
                if self.mp > self.max_mp:
                    self.mp = self.max_mp

            media_buff_times = {
                "healing_img": 0.96,
                "shield_img": 1.2,
                "damage_up_img": 1.35,
                "defance_up_img": 1.35,
                "speed_up_img": 0.96,
                "resistance_up_img": 0.72,
                "charge_img": 0.72
            }
            
            if not ani_only_once:
                if len(media_buff_anime) > 0:
                    renpy.music.play("加成", channel="battle_music")
                    # renpy.pause(0.05)
                for anime in media_buff_anime:
                    if anime in ["speed_up_img", "resistance_up_img"]:
                        renpy.show(anime, at_list=[Transform(anchor=(0.5, 0.5), zoom=1.5, xpos=self.xposition, ypos=0.4)], layer="screens")
                    else:
                        renpy.show(anime, at_list=[Transform(anchor=(0.5, 0.5), zoom=2.5, xpos=self.xposition, ypos=0.4)], layer="screens")
                    renpy.pause(media_buff_times[anime] * persistent.battlespeed)
                    renpy.hide(anime, layer="screens")

            ## 技能附加效果
            # 精准掌握：在施放“不知火”时，有30%概率降低目标火元素伤害抗性和元素精通，持续2回合；在施放“冥火”时，有8%|10%|12%|15%|15%固定概率使目标眩晕1回合
            if ("精准掌握", True) in ally_environment_effects and user.name == "花山院琉璃":
                temp_selected_skill = user.skills if not user.is_phase2 else user.skills_v2
                passive_skill = [s for s in temp_selected_skill if s.category == "Passive"][0]

                if skill.name == "不知火" and 0.3 > renpy.random.random():
                    temp_ratio_lists = [0.25, 0.3, 0.3, 0.35, 0.35]
                    buff = getattr(store, "suppress")
                    item = (2, (temp_ratio_lists[passive_skill.level - 1], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
                    buff.calculate(self, None, item, skill.name, "get")

                    temp_ratio_lists = [50, 50, 70, 80, 80]
                    buff = getattr(store, "churn")
                    item = (2, temp_ratio_lists[passive_skill.level - 1])
                    buff.calculate(self, None, item, skill.name, "get")
                elif skill.name == "冥火" and "domineering" not in self.buff and "sp_domineering" not in self.buff:
                    temp_ratio_lists = [0.08, 0.1, 0.12, 0.15, 0.15]
                    if temp_ratio_lists[passive_skill.level - 1] > renpy.random.random():
                        buff = getattr(store, "dizziness")
                        item = (1, None)

                        # 反射天赋触发
                        if "Reflexes" in self.abilities and 0.08 > renpy.random.random():
                            renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("反射", style="effect_text", color="ff9"))
                            # renpy.pause(0.5 * persistent.battlespeed)
                            # renpy.hide("buff_effect", layer="screens")
                            buff.calculate(user, None, item, skill.name, "get")
                        else:
                            buff.calculate(self, None, item, skill.name, "get")
            
            ## 特定技能效果区
            if skill.name == "温柔的祝福":
                # 献祭自身当前生命
                if not local_config.multi_buff_lock:
                    if skill.level == 1:
                        user.hp = max(int(user.hp * 0.8), 1)
                    elif skill.level == 2:
                        user.hp = max(int(user.hp * 0.82), 1)
                    elif skill.level == 3:
                        user.hp = max(int(user.hp * 0.84), 1)
                    elif skill.level == 4:
                        user.hp = max(int(user.hp * 0.86), 1)
                    elif skill.level == 5:
                        user.hp = max(int(user.hp * 0.88), 1)
                # 驱散1个减益或控制效果
                debuffs = copy(self.debuff)
                count = 0
                for buff_name in debuffs:
                    buff_obj = getattr(store, buff_name)
                    if buff_obj.removeable:
                        buff_obj.calculate(self, ally_environment_effects, None, None, "clean")
                        count += 1
                        if buff_obj.objectname in ["silence", "confusion", "frozen", "sleepy", "ridicule"]:
                            # 恢复MP并提升效果抵抗
                            self.mp += 15
                            if self.mp > self.max_mp:
                                self.mp = self.max_mp
                            up_resistance_buff = getattr(store, "barrier")
                            item = (1, 0.4)
                            up_resistance_buff.calculate(self, None, item, skill.name, "get")
                            # 获得行动提前
                            if skill.level == 5:
                                self.order += 200
                        if skill.level in [3, 4, 5]:
                            if count >= 2:
                                break
                        else:
                            break
                # 提升速度
                up_buff = getattr(store, "flow")
                if skill.level in [1, 2, 3]:
                    item = (1, 10)
                    up_buff.calculate(self, None, item, skill.name, "get")
                elif skill.level in [4, 5]:
                    item = (1, 10)
                    up_buff.calculate(self, None, item, skill.name, "get")
            # 牺牲30%|30%|25%|20%|15%当前生命
            if skill.name == "视线诱导":
                if not local_config.multi_buff_lock:
                    temp_ratio_lists = [0.3, 0.3, 0.25, 0.2, 0.15]
                    user.hp = max(int(user.hp * (1.0 - temp_ratio_lists[skill.level - 1])), 1)
            # 随机驱散1|1|1|2|2个减益状态或控制效果，Lv3~5: 同时清除所有的元素附着
            elif skill.name == "碧之律":
                debuffs = copy(self.debuff)
                count = 0
                for buff_name in debuffs:
                    buff_obj = getattr(store, buff_name)
                    if buff_obj.removeable:
                        buff_obj.calculate(self, ally_environment_effects, None, None, "clean")
                    
                    if skill.level in [4, 5]:
                        if count >= 2:
                            break
                    else:
                        break
                if skill.level in [3, 4, 5]:
                    self.ebuff = {}
            # 解开潘多拉的魔咒，记录我方场上所有队友以及所选择的敌方目标当前生命比例，并降低敌方目标30点速度，持续1回合。若下回合“立花希”行动开始时，我方有角色所记录的生命比例小于敌方目标所记录的生命比例且未阵亡，则将低于记录数值的角色生命恢复至敌方记录比例
            elif skill.name == "魂之殇":
                # 记录敌方目标当前生命比例
                target_enemy = user.selected_target
                target_hp_ratio = target_enemy.hp / target_enemy.battle_max_hp
                temp_dict = local_config.skill_log_data.setdefault("魂之殇", {})
                already_in = None
                for (u, t) in temp_dict:
                    if u == user:
                        already_in = (u, t)
                        break
                if already_in is not None:
                    temp_dict.pop(already_in)
                temp_dict[(user, self)] = {
                    user: (target_hp_ratio, "user")
                }
                # 给对方标记“殇魂”debuff
                buff_obj = getattr(store, "desoul_lock")
                item = (99, target_hp_ratio)
                buff_obj.calculate(self, None, item, skill.name, "get")
                # 降低对方30点速度
                buff_obj = getattr(store, "slow")
                item = (1, 30)
                buff_obj.calculate(self, None, item, skill.name, "get")
                if skill.level == 1:
                    # 降低自身30点速度
                    buff_obj = getattr(store, "slow")
                    item = (1, 30)
                    buff_obj.calculate(user, None, item, skill.name, "get")
            # 激活强大的感官灵能控制对方思维，为自身与敌方目标附加1层无法驱散的“咒”效果进入“接触”状态，当自身受到伤害时，对共同持有“咒”的敌方单位造成50%的传导伤害（不会暴击；也不会触发装备4件套效果），持续2回合
            elif skill.name == "接触感应":
                # 为自身与敌方目标附加1层无法驱散的“咒”效果进入“接触”状态
                buff_obj1 = getattr(store, "curse")
                if skill.level == 1:
                    item1 = (2, 0.5)
                elif skill.level == 2:
                    item1 = (2, 0.6)
                elif skill.level == 3:
                    item1 = (2, 0.7)
                elif skill.level == 4:
                    item1 = (2, 0.8)
                else:
                    item1 = (2, 1.0)
                buff_obj1.calculate(user, None, item1, skill.name, "get")
                buff_obj2 = getattr(store, "decurse")
                if skill.level == 1:
                    item2 = (99, 0.5)
                elif skill.level == 2:
                    item2 = (99, 0.6)
                elif skill.level == 3:
                    item2 = (99, 0.7)
                elif skill.level == 4:
                    item2 = (99, 0.8)
                else:
                    item2 = (99, 1.0)
                buff_obj2.calculate(self, None, item2, skill.name, "get")
                # {"咒": {"lhx_role": (False, None, target), [target.objectname]: (False, None, source)}}
                buff_roles = local_config.skill_log_data.setdefault("咒", {})
                buff_roles[user] = (False, None, "user", self)
                buff_roles[self] = (False, None, "target", user)
            # 开启持续1回合的星空结界，场上所有友方单位获得“星桥”，使得下一次受到的伤害降低35%
            elif skill.name == "星空梦影":
                temp_dict = local_config.skill_log_data.setdefault("星空梦影", {})
                temp_dict[self] = (False, user)
            # 消耗9层“鬼面”，开启附带9个禁断之面的“封印结界”笼罩对手
            elif skill.name == "虚无":
                # 消耗9层“鬼面”
                buff_obj = getattr(store, "ghost_mask")
                buff_obj.calculate(user, ally_environment_effects, None, None, "clean")
                # 鬼面加入
                buff_roles = local_config.skill_log_data.setdefault("积重鬼怨", {})
                if user in local_config.party:
                    buff_roles["ally"] = 9
                elif user in local_config.enemy:
                    buff_roles["enemy"] = 9
            # 进入持续2回合的“空灵”状态
            elif skill.name == "幻镜化物":
                buff_obj = getattr(store, "ethereal")
                item = (2, None)
                buff_obj.calculate(user, None, item, skill.name, "get")

                # 立刻获得50%行动提前
                user.order += 500

                if skill.level in [3, 4, 5]:
                    # 期间自身进入“霸体”状态
                    buff_obj = getattr(store, "sp_domineering")
                    item = (99, None)
                    buff_obj.calculate(user, None, item, skill.name, "get")
                    if skill.level in [4, 5]:
                        # 提升80点元素精通
                        buff_obj = getattr(store, "master")
                        item = (2, 80)
                        buff_obj.calculate(user, None, item, skill.name, "get")
                        if skill.level == 5:
                            # 提升60点速度
                            buff_obj = getattr(store, "flow")
                            item = (2, 60)
                            buff_obj.calculate(user, None, item, skill.name, "get")
                # 形态变化
                user.is_phase2 = True
                renpy.music.play("raged", channel="battle_music")
                if "幻镜化物-pose" in local_config.skill_log_data:
                    local_config.skill_log_data["幻镜化物-pose"].append((user, user.pose))
                else:
                    local_config.skill_log_data["幻镜化物-pose"] = [(user, user.pose)]

                if user.pose == "sf":
                    user.pose = "sf_2"
                else:
                    user.pose = "zf_2"
            # 获得“霸体”状态持续1回合，增益角色在行动结束后进入1回合不可驱散的“深度沉睡”状态
            elif skill.name == "催眠":
                # 获得“霸体”状态
                if "sp_domineering" not in self.buff:
                    buff_obj = getattr(store, "domineering")
                    item = (1, None)
                    buff_obj.calculate(self, None, item, skill.name, "get")
                # 增益角色记录
                temp_dict = local_config.skill_log_data.setdefault("催眠", {})
                if self == user and not support:
                    temp_dict[self] = 2
                else:
                    temp_dict[self] = 1
            # 跳过回合并击碎1个禁断之面
            elif skill.name == "怨恨祛除":
                if "积重鬼怨" in local_config.skill_log_data:
                    buff_roles = local_config.skill_log_data["积重鬼怨"]
                    if self in local_config.party and "enemy" in buff_roles:
                        buff_roles["enemy"] -= 1
                        # 消除禁断之面
                        face_number = buff_roles["enemy"]
                        if face_number != 0:
                            renpy.hide("qcls_skill_ally-mask_%d" % face_number)
                        else:
                            renpy.hide("qcls_skill_ally-mask_top")
                            buff_roles.pop("enemy")
                        
                        # 解除封印结界
                        if face_number == 0:
                            if len(local_config.skill_log_data["积重鬼怨"]) == 0:
                                local_config.skill_log_data.pop("积重鬼怨")
                            for role in local_config.party[:3]:
                                role._special_calculate(enemy_environment_effects=ally_environment_effects, mode="release")
                    elif self in local_config.enemy and "ally" in buff_roles:
                        buff_roles["ally"] -= 1
                        # 消除禁断之面
                        face_number = buff_roles["ally"]
                        if face_number != 0:
                            renpy.hide("qcls_skill_enemy-mask_%d" % face_number)
                        else:
                            renpy.hide("qcls_skill_enemy-mask_top")
                            buff_roles.pop("ally")

                        # 解除封印结界
                        if face_number == 0:
                            if len(local_config.skill_log_data["积重鬼怨"]) == 0:
                                local_config.skill_log_data.pop("积重鬼怨")
                            for role in local_config.enemy[:3]:
                                role._special_calculate(enemy_environment_effects=ally_environment_effects, mode="release")
            # 共感
            elif skill.name == "共感":
                # 为我方场上全体角色附加“心”，持续1回合
                temp_dict = local_config.skill_log_data.setdefault("共感", {})
                if self in local_config.party:
                    if "ally" not in temp_dict:
                        temp_dict["ally"] = set([self])
                    else:
                        temp_dict["ally"].add(self)
                elif self in local_config.enemy:
                    if "enemy" not in temp_dict:
                        temp_dict["enemy"] = set([self])
                    else:
                        temp_dict["enemy"].add(self)

            if "混乱" in skill.effects or "眩晕" in skill.effects or "冻结" in skill.effects or "沉睡" in skill.effects or "嘲讽" in skill.effects:
                control_effects = {name: value for name, value in skill.effects.items() if name in ["混乱", "眩晕", "冻结", "沉睡", "嘲讽"]}
                
                for name, (ratios, target, time) in control_effects.items():
                    if isinstance(ratios, float):
                        ratios = [ratios]
                    # 每段判定的基础概率
                    for ratio in ratios:
                        battle_user_effect_hitrate, battle_target_effect_resistance = self.battle_role_init_control(user, self, ally_environment_effects, enemy_environment_effects)

                        # 若敌方带有“减速”效果，则基础概率提升至15%
                        if skill.name == "灵能风暴" and "slow" in self.debuff:
                            ratio = 0.15

                        # 技能效果命中率 = 技能基础命中 x (1 + 面板效果命中)
                        battle_effect_hitrate_final = ratio * (1 + battle_user_effect_hitrate)
                        # 技能效果抵抗率 = 1 - 100% / (100% + 面板效果抵抗)
                        battle_effect_resistance_final = 1.0 - 1.0 / (1.0 + battle_target_effect_resistance)
                        
                        # 判定是否命中
                        if battle_effect_hitrate_final > renpy.random.random():
                            # 霸体免控
                            if "domineering" in self.buff or "sp_domineering" in self.buff:
                                renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("霸体免控", style="effect_text", color="ff9"))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                # renpy.hide("buff_effect", layer="screens")
                            # 判定是否被抵抗
                            elif battle_effect_resistance_final < renpy.random.random():
                                # 反射判定
                                hitted = True
                                buff_roles = None
                                buff_obj = None
                                effect_target = self
                                if "Reflexes" in effect_target.abilities and 0.08 > renpy.random.random():
                                    renpy.show("buff_effect", at_list=[show_state(effect_target.xposition)], layer="screens", what=Text("反射", style="effect_text", color="ff9"))
                                    # renpy.pause(0.5 * persistent.battlespeed)
                                    # renpy.hide("buff_effect", layer="screens")
                                    effect_target = user
                                    hitted = False
                                    buff_roles = local_config.skill_log_data.setdefault("Reflexes", {})

                                if buff_roles is None or (buff_roles is not None and effect_target.objectname not in buff_roles):
                                    # 效果命中目标
                                    if name == "混乱":
                                        buff_obj = getattr(store, "confusion")
                                        item = (1, None)
                                        buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                        buff_text = "混乱"
                                    elif name == "眩晕":
                                        buff_obj = getattr(store, "dizziness")
                                        item = (1, None)
                                        buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                        buff_text = "眩晕"
                                    elif name == "冻结":
                                        # 对已处于“冰冻”状态下的角色有30%概率转换为“深度冰冻”
                                        if "frozen" in effect_target.debuff and skill.name == "灵能风暴" and skill.level == 5:
                                            buff_obj = getattr(store, "deep_frozen")
                                            item = (1, None)
                                            buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                            buff_text = "深度冰冻"
                                        else:
                                            buff_obj = getattr(store, "frozen")
                                            item = (1, 0.5)
                                            buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                            buff_text = "冻结"
                                    elif name == "沉睡":
                                        buff_obj = getattr(store, "sleepy")
                                        item = (1, None)
                                        buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                        buff_text = "沉睡"
                                    elif name == "嘲讽" and "ridicule" not in effect_target.debuff:
                                        buff_obj = getattr(store, "ridicule")
                                        item = (1, None)
                                        buff_obj.calculate(effect_target, None, item, skill.name, "get", user=user)
                                        buff_text = "嘲讽"

                                    if buff_obj is not None and buff_roles is not None:
                                        buff_roles[effect_target.objectname] = buff_obj

                                renpy.music.play("poisoned", channel="battle_music")
                                renpy.show("buff_effect", at_list=[show_state(effect_target.xposition)], layer="screens", what=Text(buff_text, style="effect_text", color="ff9"))
                                # renpy.pause(0.75 * persistent.battlespeed)
                            else:
                                renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("抵抗", style="effect_text", color="ff9"))
                                # renpy.pause(0.5)

            if hitted:
                # 表情更新
                self.face_change(hit=False, hitted=True)
                # 受到伤害角色抖动特效
                if self in local_config.party:
                    renpy.show(self.objectname, at_list=[shake, hide_out], layer="fg")
                else:
                    renpy.show(self.objectname, at_list=[smallshake])
            renpy.pause(0.75 * persistent.battlespeed)
                
            ## 伤害结束后效果判定
            # 阵亡判定
            self.death_calculate(user, skill, ally_environment_effects, enemy_environment_effects, order_members)
            
            # 闪避（最终决战王牌魔导力才有闪避）
            # renpy.music.play("Dodge_sound", channel="battle_music")
            # if self in party:
            #     renpy.show(self.objectname, at_list=[sway_r, hide_out], layer="fg")
            # else:
            #     renpy.show(self.objectname, at_list=[sway_l])
            # renpy.pause(0.5 * persistent.battlespeed)

            # 避免能量条溢出边界
            self.hp = int(self.hp)
            self.mp = int(self.mp)

            if self.hp > self.battle_max_hp:
                self.hp = self.battle_max_hp
            elif self.hp < 0:
                self.hp = 0

            if self.mp > self.max_mp:
                self.mp = self.max_mp
            elif self.mp < 0:
                self.mp = 0

            # 表情恢复
            self.face_change()

            renpy.hide("critical", layer="screens")
            renpy.hide("damage", layer="screens")
            renpy.hide("elemental", layer="screens")
            renpy.hide("special", layer="screens")
            renpy.hide("buff_effect", layer="screens")
            renpy.hide("status", layer="screens")
            renpy.hide("defence", layer="screens")
            renpy.hide("finish", layer="screens")
            renpy.hide("healing", layer="screens")

            return

        # AOE战斗计算
        def battle_calculate_aoe(self, skill, user, use_targets, ally_environment_effects, enemy_environment_effects, order_members, slot_x, slot_y, sp_rull="", support=False):
            # 只有受到控制效果时变化
            hitted = [False for i in range(len(use_targets))]

            damage_color_map = {
                "fire": "#f30",
                "water": "#19f",
                "light": "#f0f",
                "ice": "#3ff",
                "wind": "#6f6",
                "rock": "#ff0",
                "physical": "#9cf",
                "蒸发": "#9cf",
                "融化": "#9cf",
                "超载": "#f66",
                "冻结": "#3ff",
                "超导": "#99f",
                "感电": "#f0f",
                "扩散": "#6f6",
                "结晶": "#ff0",
                "治疗": "#2f0",
                "能量": "#19f",
            }

            # battle_role_inits = []
            # for role in use_targets:
            #     # battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack
            #     role_init_info = role.battle_role_init(user, role, ally_environment_effects, enemy_environment_effects, sp_rull)
            #     battle_role_inits.append(role_init_info)

            ## 伤害计算（装备、天赋、角色属性、技能倍率、buff加成、元素反应）
            if "伤害" in skill.effects:
                ## 技能特殊判定
                total_skill_damages = [copy(skill.damage) for i in range(len(use_targets))]
                total_skill_elements = [copy(skill.element) for i in range(len(use_targets))]

                for total_skill_damage, total_skill_element in zip(total_skill_damages, total_skill_elements):
                    # 精准掌握：普攻之后有20%|25%|30%|30%|30%概率附加一段攻击60%|60%|60%|80%|100%火元素伤害
                    if (("精准掌握", True) in ally_environment_effects) and user.name == "花山院琉璃" and skill.category == "General_attack":
                        temp_selected_skill = user.skills if not user.is_phase2 else user.skills_v2
                        passive_skill = [s for s in temp_selected_skill if s.category == "Passive"][0]
                        ratio_lists = [0.2, 0.25, 0.3, 0.3, 0.3]
                        if ratio_lists[passive_skill.level - 1] > renpy.random.random():
                            temp_damage_lists = [0.6, 0.6, 0.6, 0.8, 1.0]
                            total_skill_damage += [temp_damage_lists[passive_skill.level - 1]]
                            total_skill_element += ["fire"]
                        else:
                            total_skill_damage += [0.0]
                            total_skill_element += ["no"]

                # 旧版：最终伤害 = 攻击力 x 伤害倍率 x 暴击伤害 x (1 + 技能/天赋/装备额外加成 + 物理/元素伤害加成 + 元素反应加成(蒸发|融化)) x 最终元素抗性 x 承伤比例
                # 攻击力 = 基础攻击力 + 攻击力加成 | 攻击力加成 = 基础攻击力 x (1 + 攻击力加成比例) + 固定攻击力
                # 精通提升= (-0.0002 x (元素精通) ^ 2 + 0.4527 x 元素精通 + 1.0058) / 100.0
                # 防御减免 = (300 / (300 + 防御力)

                # 新版：最终伤害 = 攻击力 x 防御减免 x 伤害倍率 x (1 + 伤害加成) x 暴击伤害 x 增幅反应倍率 x 承伤比例 x 抗性减免
                # 攻击力 = 基础攻击力 + 攻击力加成 | 攻击力加成 = 基础攻击力 x (1 + 攻击力加成比例) + 固定攻击力
                # 防御减免 = 300 / (300 + 防御力)
                # 伤害倍率 = 技能倍率
                # 伤害加成 = 技能/天赋/装备额外加成
                # 暴击伤害期望 = 1 + (暴击率 x 暴击伤害)
                # 增幅反应倍率 = 元素反应提升倍率 = 元素反应基本倍率 x (1 + 精通提升 + 反应提升系数) | 精通提升 = K x 2.78 x 精通 / (精通 + 1400)
                # 承伤比例 = 1 + (攻击者等级 / 被攻击者等级 - 1) * 0.4
                # 抗性减免 = 被攻击者抗性 - 抗性削减 if 被攻击者抗性 >= 抗性削减 else 0.5 x (被攻击者抗性 - 抗性削减)
                
                inner_react = [False for i in range(len(use_targets))]
                con_hun_flag = [False for i in range(len(use_targets))]
                # 重复几段伤害
                for battle_act_damage_ratio, battle_act_element in zip(zip(*total_skill_damages), zip(*total_skill_elements)):
                    ## 单轮/全角色计算伤害
                    multi_buff_lock_damage = True
                    for numb, (now_role, battle_skill_damage_ratio, battle_skill_element) in enumerate(zip(use_targets, battle_act_damage_ratio, battle_act_element)):
                        if battle_skill_element != "no":
                            battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack = now_role.battle_role_init(user, now_role, ally_environment_effects, enemy_environment_effects, sp_rull)
                            battle_user_effect_hitrate, battle_target_effect_resistance = now_role.battle_role_init_control(user, now_role, ally_environment_effects, enemy_environment_effects)
                            
                            # 暴击判定
                            judgerate = renpy.random.random()
                            battle_critical = battle_user_critical_rate >= judgerate
                            # 防御减免后倍率(300 / (300 + 防御力)
                            battle_defance_resistance = 300 / (300 + battle_target_defance)
                            # 基础伤害 = 面板攻击力 x 防御减免后倍率)
                            battle_fundamental_damage = battle_base_attack * battle_defance_resistance
                            # 承伤比例 old = 攻击者等级 / 被攻击者等级
                            # 承伤比例 new = 1 + (攻击者等级 / 被攻击者等级 - 1) * 0.4
                            battle_level_damage_rate = 1 + (user.level / now_role.level - 1) * 0.4
                            # 角色元素伤害加成
                            battle_user_damage_bonus = getattr(user, "battle_%s_damage_bonus" % battle_skill_element) if battle_skill_element else None
                            # 最终元素抗性 = 怪物抗性 - 抗性削减 if 怪物抗性 >= 抗性削减 else 0.5 x (怪物抗性 - 抗性削减)
                            battle_target_elemental_resistance = getattr(now_role, "battle_%s_elemental_resistance" % battle_skill_element) if battle_skill_element else None

                            # 回响 & 狩猎天赋
                            if battle_critical and ("Conjurer" in user.abilities and battle_skill_element is not None and battle_skill_element != "physical") and 0.3 > renpy.random.random():
                                renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("回响", style="effect_text", color="ff9"))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                # renpy.hide("buff_effect", layer="screens")

                                battle_target_elemental_resistance -= 0.15
                                con_hun_flag[numb] = True
                            if battle_critical and ("Hunter" in user.abilities and battle_skill_element == "physical") and 0.3 > renpy.random.random():
                                renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("狩猎", style="effect_text", color="ff9"))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                # renpy.hide("buff_effect", layer="screens")

                                battle_target_elemental_resistance -= 0.3
                                con_hun_flag[numb] = True
                            
                            # 抗性负数时->增伤转换
                            if battle_target_elemental_resistance >= 0:
                                battle_resistance_damage_rate = 1 - battle_target_elemental_resistance
                            else:
                                battle_resistance_damage_rate = 1 - (0.5 * battle_target_elemental_resistance)
                        
                            ## 元素反应乘区（蒸发、融化）
                            # 水->火 | 火->冰（蒸发|融化 2.0倍率）
                            battle_user_element_bonus = 0.0
                            if battle_skill_element == "water" and "fire" in now_role.ebuff:
                                renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("蒸发", style="effect_text", size=80, color=damage_color_map["蒸发"]))
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    battle_user_element_bonus = 1.2 * (1 + battle_elemental_mastery_bonus)
                                else:
                                    battle_user_element_bonus = 1.0 * (1 + battle_elemental_mastery_bonus)

                                # “遗念镜”祝福
                                if now_role in local_config.party and "蒸发" in local_config.battle_blessing:
                                    battle_user_element_bonus += local_config.battle_blessing["蒸发"]

                                # 元素消融
                                now_role.ebuff["fire"] -= 3
                                if now_role.ebuff["fire"] <= 0:
                                    now_role.ebuff.pop("fire")

                                inner_react[numb] = True
                            elif battle_skill_element == "fire" and "ice" in now_role.ebuff:
                                renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("融化", style="effect_text", size=80, color=damage_color_map["融化"]))
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    battle_user_element_bonus = 1.2 * (1 + battle_elemental_mastery_bonus)
                                else:
                                    battle_user_element_bonus = 1.0 * (1 + battle_elemental_mastery_bonus)

                                # “遗念镜”祝福
                                if now_role in local_config.party and "融化" in local_config.battle_blessing:
                                    battle_user_element_bonus += local_config.battle_blessing["融化"]

                                # 50%概率消除冰冻状态
                                if "frozen" in now_role.debuff and renpy.random.random() > 0.5:
                                    buff_obj = getattr(store, "frozen")
                                    buff_obj.calculate(now_role, None, None, None, "clean")
                                    now_role.ebuff.pop("ice")
                                else:
                                    now_role.ebuff["ice"] -= 3
                                    if now_role.ebuff["ice"] <= 0:
                                        now_role.ebuff.pop("ice")

                                inner_react[numb] = True
                            # 火->水 | 冰->火（蒸发|融化 1.5倍率）
                            elif battle_skill_element == "fire" and "water" in now_role.ebuff:
                                renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("蒸发", style="effect_text", size=80, color=damage_color_map["蒸发"]))
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    battle_user_element_bonus = 0.7 * (1 + battle_elemental_mastery_bonus)
                                else:
                                    battle_user_element_bonus = 0.5 * (1 + battle_elemental_mastery_bonus)

                                # “遗念镜”祝福
                                if now_role in local_config.party and "蒸发" in local_config.battle_blessing:
                                    battle_user_element_bonus += local_config.battle_blessing["蒸发"]

                                now_role.ebuff["water"] -= 2
                                if now_role.ebuff["water"] <= 0:
                                    now_role.ebuff.pop("water")

                                inner_react[numb] = True
                            elif battle_skill_element == "ice" and "fire" in now_role.ebuff:
                                renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("融化", style="effect_text", size=80, color=damage_color_map["融化"]))
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    battle_user_element_bonus = 0.7 * (1 + battle_elemental_mastery_bonus)
                                else:
                                    battle_user_element_bonus = 0.5 * (1 + battle_elemental_mastery_bonus)

                                # “遗念镜”祝福
                                if now_role in local_config.party and "融化" in local_config.battle_blessing:
                                    battle_user_element_bonus += local_config.battle_blessing["融化"]

                                now_role.ebuff["fire"] -= 2
                                if now_role.ebuff["fire"] <= 0:
                                    now_role.ebuff.pop("fire")

                                inner_react[numb] = True

                            ## 特殊机制加成
                            battle_other_bonus = 0.0
                            # 降魔诛乱：对“鬼”、“神”、“天使”造成的伤害增加30%
                            if skill.name == "降魔诛乱" and skill.level == 5 and now_role.category in ["gost", "god", "angel"]:
                                renpy.show("special_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("降魔", style="skill_text"))
                                battle_other_bonus += 0.3
                            # 噗哈哈：自身获得减伤
                            if now_role.name == "藤原瞳" and "ridicule" in user.debuff:
                                temp_selected_skills = now_role.base_skills if not now_role.is_phase2 else now_role.base_skills_v2
                                fake_tyt_combat = [s for s in temp_selected_skills if s.category == "Combat_skills"][0]
                                if fake_tyt_combat.level == 4:
                                    battle_skill_damage_ratio -= 0.2
                                elif fake_tyt_combat.level == 5:
                                    battle_skill_damage_ratio -= 0.4
                            # 对生命比例高于80%的目标，此次伤害倍率降低15%
                            if skill.name == "不知火":
                                if now_role.hp / now_role.battle_max_hp > 0.8:
                                    battle_skill_damage_ratio -= 0.15
                                elif now_role.hp / now_role.battle_max_hp < 0.5 and skill.level in [3, 4, 5]:
                                    battle_skill_damage_ratio += 0.15
                            # 对生命比例低于50%的目标，此次伤害倍率降低15%
                            if skill.name == "冥火":
                                if now_role.hp / now_role.battle_max_hp < 0.5:
                                    battle_skill_damage_ratio -= 0.15
                                elif now_role.hp / now_role.battle_max_hp > 0.8 and skill.level in [3, 4, 5]:
                                    battle_skill_damage_ratio += 0.15
                            # 星空梦影
                            if "star_bridge" in now_role.buff or "star_bridge_done" in now_role.buff:
                                buff_roles = local_config.skill_log_data["星空梦影"]
                                buff_user_role = None
                                for t, (f, u) in buff_roles.items():
                                    buff_user_role = u
                                    break
                                
                                # 降低15%|20%|25%|30%|30%受到的伤害
                                temp_ratio_lists = [0.15, 0.2, 0.25, 0.3, 0.3]
                                temp_selected_skill = buff_user_role.skills if not buff_user_role.is_phase2 else buff_user_role.skills_v2
                                temp_combat_skill = [s for s in temp_selected_skill if s.category == "Combat_skills"][0]
                                battle_other_bonus -= temp_ratio_lists[temp_combat_skill.level - 1]

                                # 使得下一次受到的伤害降低10%|15%|20%|25%|30%
                                if "star_bridge" in now_role.buff:
                                    temp_ratio_lists = [0.1, 0.15, 0.2, 0.25, 0.3]
                                    temp_selected_skill = buff_user_role.skills if not buff_user_role.is_phase2 else buff_user_role.skills_v2
                                    temp_combat_skill = [s for s in temp_selected_skill if s.category == "Combat_skills"][0]

                                    battle_other_bonus -= temp_ratio_lists[temp_combat_skill.level - 1]
                                    buff_obj = getattr(store, "star_bridge")
                                    buff_obj.calculate(now_role, None, None, "done", "clean")
                            # 白色永恒：在回合结束前的战斗计算阶段提升20%|30%|30%|30%|30%暴击伤害
                            if "白色永恒" in local_config.skill_log_data:
                                buff_roles = local_config.skill_log_data["白色永恒"]
                                if user in local_config.party and "ally" in buff_roles:
                                    _, fake_xfe_passive, flag = buff_roles["ally"]
                                    if flag:
                                        if fake_xfe_passive.level in [2, 3, 4, 5]:
                                            battle_user_critical_damage += 0.3
                                        else:
                                            battle_user_critical_damage += 0.2
                                elif user in local_config.enemy and "enemy" in buff_roles:
                                    _, fake_xfe_passive, flag = buff_roles["enemy"]
                                    if flag:
                                        if fake_xfe_passive.level in [2, 3, 4, 5]:
                                            battle_user_critical_damage += 0.3
                                        else:
                                            battle_user_critical_damage += 0.2
                            # 秋之韵-素律
                            if user.equip4effect == "秋之韵-素律" and ("秋之韵-素律", True) in ally_environment_effects:
                                if now_role.hp > 0.7 * now_role.battle_max_hp:
                                    battle_other_bonus += 0.3
                                else:
                                    hp_ratio = math.floor(((0.7 * now_role.battle_max_hp - now_role.hp) / now_role.battle_max_hp) / 0.2)
                                    battle_other_bonus += 0.1 * hp_ratio
                            # 冬之羽-玄英
                            if user.equip4effect == "冬之羽-玄英" and ("冬之羽-玄英", True) in ally_environment_effects:
                                mp_ratio = math.floor(now_role.mp / 10)
                                battle_other_bonus += 0.04 * mp_ratio

                            if battle_critical:
                                # single_battle_damage = battle_fundamental_damage * battle_skill_damage_ratio * battle_user_critical_damage * (1.0 + battle_user_damage_bonus + battle_user_element_bonus + battle_other_bonus) * battle_resistance_damage_rate * battle_level_damage_rate
                                single_battle_damage = battle_fundamental_damage * battle_skill_damage_ratio * (1.0 + battle_user_damage_bonus + battle_other_bonus) * battle_user_critical_damage * (1 + battle_user_element_bonus) * battle_level_damage_rate * battle_resistance_damage_rate
                            else:
                                # single_battle_damage = battle_fundamental_damage * battle_skill_damage_ratio * (1.0 + battle_user_damage_bonus + battle_user_element_bonus + battle_other_bonus) * battle_resistance_damage_rate * battle_level_damage_rate
                                single_battle_damage = battle_fundamental_damage * battle_skill_damage_ratio * (1.0 + battle_user_damage_bonus + battle_other_bonus) * (1 + battle_user_element_bonus) * battle_level_damage_rate * battle_resistance_damage_rate

                            ## 伤害结算
                            left_final_damage = int(single_battle_damage)
                            # 护盾抵消（伤害计算优先扣除护盾）
                            if "sp_shield" in now_role.buff:
                                shield_time, shield_effects = now_role.buff["sp_shield"]
                                shield_strength, shield_element, _, _ = shield_effects
                                shield_damage_ratio = 1.0
                                # 属性克制（强势1.5倍、弱势0.5倍）
                                if (battle_skill_element == "water" and shield_element == "fire") or (battle_skill_element == "fire" and shield_element == "ice") or (battle_skill_element == "ice" and shield_element == "light") or (battle_skill_element == "light" and shield_element == "water") or (battle_skill_element == "rock" and shield_element == "rock"):
                                    shield_damage_ratio = 1.5
                                elif (battle_skill_element == "fire" and shield_element == "water") or (battle_skill_element == "ice" and shield_element == "fire") or (battle_skill_element == "light" and shield_element == "ice") or (battle_skill_element == "water" and shield_element == "light"):
                                    shield_damage_ratio = 0.5
                                # 属性调和（0.25倍）
                                elif shield_element not in ["rock", "physical"] and battle_skill_element == shield_element:
                                    shield_damage_ratio = 0.25
                                
                                left_shield_strength = int(shield_strength - shield_damage_ratio * left_final_damage)
                                # 更新护盾
                                shield_buff = getattr(store, "sp_shield")
                                item = (shield_time, (left_shield_strength, shield_element, 0.75, 0.5))
                                shield_buff.calculate(now_role, None, item, None, "get")
                                left_final_damage = 0

                                renpy.music.play("盾档", channel="battle_music")

                                # 如果护盾破碎，驱散护盾并结算剩余伤害
                                if "sp_shield" not in now_role.buff:
                                    # 穿透伤害
                                    if left_shield_strength < 0:
                                        left_final_damage = -int(left_shield_strength/shield_damage_ratio)
                            if "shield" in now_role.buff:
                                shield_time, shield_effects = now_role.buff["shield"]
                                shield_strength, shield_element, _, _ = shield_effects
                                shield_damage_ratio = 1.0
                                # 属性克制（强势1.5倍、弱势0.5倍）
                                if (battle_skill_element == "water" and shield_element == "fire") or (battle_skill_element == "fire" and shield_element == "ice") or (battle_skill_element == "ice" and shield_element == "light") or (battle_skill_element == "light" and shield_element == "water") or (battle_skill_element == "rock" and shield_element == "rock"):
                                    shield_damage_ratio = 1.5
                                elif (battle_skill_element == "fire" and shield_element == "water") or (battle_skill_element == "ice" and shield_element == "fire") or (battle_skill_element == "light" and shield_element == "ice") or (battle_skill_element == "water" and shield_element == "light"):
                                    shield_damage_ratio = 0.5
                                # 属性调和（0.25倍）
                                elif shield_element not in ["rock", "physical"] and battle_skill_element == shield_element:
                                    shield_damage_ratio = 0.25

                                left_shield_strength = int(shield_strength - shield_damage_ratio * left_final_damage)
                                # 如果护盾还未消失，更新护盾
                                shield_buff = getattr(store, "shield")
                                item = (shield_time, (left_shield_strength, shield_element, 0.75, 0.5))
                                shield_buff.calculate(now_role, None, item, None, "get")
                                left_final_damage = 0

                                renpy.music.play("盾档", channel="battle_music")

                                # 如果护盾破碎，驱散护盾并结算剩余伤害
                                if "shield" not in now_role.buff:
                                    # 穿透伤害
                                    if left_shield_strength < 0:
                                        left_final_damage = -int(left_shield_strength/shield_damage_ratio)

                            # 角色伤害承受
                            if left_final_damage > 0.0:
                                # 唤醒沉睡状态
                                if "sleepy" in now_role.debuff:
                                    buff_obj = getattr(store, "sleepy")
                                    buff_obj.calculate(now_role, None, None, None, "clean")
                                # 唤醒深度沉睡
                                if "deep_sleepy" in now_role.debuff and left_final_damage >= 0.3 * now_role.battle_max_hp:
                                    buff_obj = getattr(store, "deep_sleepy")
                                    buff_obj.calculate(now_role, None, None, None, "clean")

                                ## 装备4件套效果、角色被动技能触发
                                # 处于“咒”状态下的“立花希”受到伤害时 或 处于“咒”状态下的敌方单位受到伤害时
                                if (("再会之音", True) in enemy_environment_effects and now_role.name == "立花希" and "curse" in now_role.buff) or (("再会之音", True) in ally_environment_effects and "decurse" in now_role.debuff):
                                    change = renpy.random.random()
                                    lhx_passive_skill = [s for s in now_role.skills if s.category == "Passive"][0]
                                    if ((lhx_passive_skill.level == 1 and 0.1 > change) or (lhx_passive_skill.level == 2 and 0.13 > change) or (lhx_passive_skill.level == 3 and 0.16 > change) or (lhx_passive_skill.level in [4, 5] and 0.2 > change)) and "咒" in local_config.skill_log_data:
                                        # {"咒": {"lhx_role": (False, None, "user", target), [target.objectname]: (False, None, "target", source)}}
                                        temp_dict = local_config.skill_log_data["咒"][now_role]
                                        local_config.skill_log_data["咒"][now_role] = (True, left_final_damage, temp_dict[2], temp_dict[3])
                                if "咒" in local_config.skill_log_data and sp_rull != "空间跳跃":
                                    buff_roles = local_config.skill_log_data["咒"]
                                    fake_lhx_role = None
                                    buff_select_role = None
                                    for role, (flag, damg, dtype, other) in buff_roles.items():
                                        if role.name == "立花希" and dtype == "user" and now_role == role:
                                            fake_lhx_role = role
                                        elif dtype == "target":
                                            buff_select_role = role
                                    if fake_lhx_role is not None:
                                        lhx_breakout_skill = [s for s in fake_lhx_role.skills if s.category == "Break_out"][0]
                                        if lhx_breakout_skill.level == 1:
                                            damage_number = int(0.5 * left_final_damage)
                                        elif lhx_breakout_skill.level == 2:
                                            damage_number = int(0.6 * left_final_damage)
                                        elif lhx_breakout_skill.level == 3:
                                            damage_number = int(0.7 * left_final_damage)
                                        elif lhx_breakout_skill.level == 4:
                                            damage_number = int(0.8 * left_final_damage)
                                        else:
                                            damage_number = int(left_final_damage)

                                        buff_select_role.hp -= damage_number
                                        if buff_select_role.hp < 1:
                                            buff_select_role.hp = 0
                                            buff_select_role.death_calculate(fake_lhx_role, skill, enemy_environment_effects, ally_environment_effects, order_members)
                                        else:
                                            if lhx_breakout_skill.level == 5 and 0.12 > renpy.random.random():
                                                buff_obj = getattr(store, "handicapped")
                                                item = (1, 0.2)
                                                buff_obj.calculate(buff_select_role, None, item, skill.name, "get")
                                                buff_obj = getattr(store, "broken")
                                                item = (1, 0.2)
                                                buff_obj.calculate(buff_select_role, None, item, skill.name, "get")
                                # ----- 守护誓约 -----
                                if ("守护誓约", True) in enemy_environment_effects and ("star_bridge" in now_role.buff or "star_bridge_done" in now_role.buff):
                                    buff_roles = local_config.skill_log_data["星空梦影"]

                                    if now_role in buff_roles:
                                        temp_flag, temp_buff_user = buff_roles[now_role]
                                        temp_selected_skill = temp_buff_user.base_skills if not temp_buff_user.is_phase2 else temp_buff_user.base_skills_v2
                                        lst_passive_skill = [s for s in temp_selected_skill if s.category == "Passive"][0]

                                        # 降低施术者15%攻击力和30%暴击率，持续1回合
                                        buff_obj = getattr(store, "weak")
                                        if lst_passive_skill.level == 1:
                                            item = (2, 0.1)
                                        else:
                                            item = (2, 0.15)
                                        buff_obj.calculate(user, None, item, "守护誓约", "get")
                                        
                                        buff_obj = getattr(store, "powerless")
                                        if lst_passive_skill.level == 1:
                                            item = (2, (0.2, 0.0))
                                        else:
                                            item = (2, (0.3, 0.0))
                                        buff_obj.calculate(user, None, item, "守护誓约", "get")

                                        # 提升10点速度和20%效果抵抗，持续1回合
                                        if lst_passive_skill.level == 4:
                                            buff_obj = getattr(store, "flow")
                                            item = (1, 10)
                                            buff_obj.calculate(now_role, None, item, "守护誓约", "get")
                                            buff_obj = getattr(store, "barrier")
                                            item = (1, 0.2)
                                            buff_obj.calculate(now_role, None, item, "守护誓约", "get")
                                        elif lst_passive_skill.level == 5:
                                            buff_obj = getattr(store, "flow")
                                            item = (1, 20)
                                            buff_obj.calculate(now_role, None, item, "守护誓约", "get")
                                            buff_obj = getattr(store, "barrier")
                                            item = (1, 0.3)
                                            buff_obj.calculate(now_role, None, item, "守护誓约", "get")

                                        # 队友生命值低于上限的30%时
                                        if lst_passive_skill.level >= 3 and now_role.hp < now_role.battle_max_hp * 0.3:
                                            # temp_ratio_lists = [0.0, 0.0, (0.1, 0.12), (0.1, 0.12), (0.2, 0.24)]
                                            # 雷亚将为其承担该伤害的10%|10%|20%（最大不超过雷亚生命上限的12%|12%|24%）
                                            # dmg_ratio1, dmg_ratio2 = temp_ratio_lists[lst_passive_skill.level - 1]
                                            # fake_lst_damage = int(left_final_damage * dmg_ratio1) if int(left_final_damage * dmg_ratio1) <= temp_buff_user.battle_max_hp * dmg_ratio2 else int(temp_buff_user.battle_max_hp * dmg_ratio2)
                                            # left_final_damage -= fake_lst_damage
                                            # temp_buff_user.hp -= fake_lst_damage
                                            # 雷亚将为其承担该伤害
                                            left_final_damage = 0
                                            temp_buff_user.hp -= left_final_damage
                                            # 死亡判定
                                            temp_buff_user.death_calculate(user, lst_passive_skill, ally_environment_effects, enemy_environment_effects, order_members)
                                            
                                # 每次造成伤害有20%|30%|40%|50%|60%的概率获得一层“鬼面”
                                if skill.name == "福祸相生":
                                    temp_ratio_lists = [0.2, 0.3, 0.4, 0.5, 0.6]
                                    if not multi_buff_lock_damage and temp_ratio_lists[skill.level - 1] > renpy.random.random():
                                        if "积重鬼怨" in local_config.skill_log_data:
                                            buff_roles = local_config.skill_log_data["积重鬼怨"]
                                            if (not (user in local_config.party and "ally" in buff_roles)) and (not (user in local_config.enemy and "enemy" in buff_roles)):
                                                buff_obj = getattr(store, "ghost_mask")
                                                item = (99, 1)
                                                buff_obj.calculate(user, ally_environment_effects, item, "福祸相生", "get")
                                        else:
                                            buff_obj = getattr(store, "ghost_mask")
                                            item = (99, 1)
                                            buff_obj.calculate(user, ally_environment_effects, item, "福祸相生", "get")
                                # 每受到暴击伤害时有40%|50%|60%|70%|80%概率额外获得1层“鬼面”
                                if ("积重鬼怨", True) in enemy_environment_effects and not multi_buff_lock_damage:
                                    fake_qcls_role = None
                                    if user in local_config.party:
                                        for role in local_config.enemy:
                                            if role.name == "千川老师":
                                                fake_qcls_role = role
                                                break
                                    else:
                                        for role in local_config.party:
                                            if role.name == "千川老师":
                                                fake_qcls_role = role
                                                break
                                    temp_selected_skills = fake_qcls_role.base_skills if not fake_qcls_role.is_phase2 else fake_qcls_role.base_skills_v2
                                    temp_passive_skill = [s for s in temp_selected_skills if s.category == "Passive"][0]
                                    temp_ratio_lists = [0.4, 0.5, 0.6, 0.7, 0.8]
                                    if battle_critical and temp_ratio_lists[temp_passive_skill.level - 1] >= renpy.random.random():
                                        if "积重鬼怨" in local_config.skill_log_data:
                                            buff_roles = local_config.skill_log_data["积重鬼怨"]
                                            if (not (user in local_config.party and "ally" in buff_roles)) and (not (user in local_config.enemy and "enemy" in buff_roles)):
                                                buff_obj = getattr(store, "ghost_mask")
                                                item = (99, 1)
                                                buff_obj.calculate(user, ally_environment_effects, item, "积重鬼怨", "get")
                                        else:
                                            buff_obj = getattr(store, "ghost_mask")
                                            item = (99, 1)
                                            buff_obj.calculate(fake_qcls_role, enemy_environment_effects, item, "积重鬼怨", "get")
                                # 普攻每次斩击造成伤害时有30%概率对场上其他任一敌人造成本次斩击伤害150%的间接伤害
                                if "ethereal" in user.buff:
                                    local_config.skill_log_data["幻镜化物"] = int(1.5 * left_final_damage)
                                # 每次斩击有8%|10%|12%|14%|16%固定概率降低对方20%治疗效果和护盾强效，持续1回合
                                if "ethereal" in user.buff and skill.name == "青影瞬杀阵":
                                    temp_ratio_lists = [0.08, 0.1, 0.12, 0.14, 0.16]
                                    if temp_ratio_lists[skill.level - 1] > renpy.random.random():
                                        buff_obj = getattr(store, "handicapped")
                                        item = (1, 0.2)
                                        buff_obj.calculate(now_role, None, item, skill.name, "get")
                                        buff_obj = getattr(store, "broken")
                                        item = (1, 0.2)
                                        buff_obj.calculate(now_role, None, item, skill.name, "get")
                                # 自身受到伤害时对施术者造成此次伤害10%|10%|15%|15%|20%的间接伤害，被嘲讽单位伤害提升至20%|20%|25%|25%|30%
                                if ("不可攻略", True) in enemy_environment_effects and now_role.name == "藤原瞳":
                                    renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("反伤", style="effect_text", color="ff9"))
                                    # renpy.pause(0.5 * persistent.battlespeed)

                                    temp_selected_skills = now_role.base_skills if not now_role.is_phase2 else now_role.base_skills_v2
                                    fake_tyt_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]

                                    temp_max_range = [0.1, 0.1, 0.13, 0.13, 0.16]
                                    if "ridicule" in user.debuff:
                                        temp_ratio_lists = [0.2, 0.2, 0.25, 0.25, 0.3]
                                        damage_number = int(temp_ratio_lists[fake_tyt_passive.level - 1] * left_final_damage) if temp_ratio_lists[fake_tyt_passive.level - 1] * left_final_damage <= now_role.battle_max_hp * temp_max_range[fake_tyt_passive.level - 1] else int(now_role.battle_max_hp * temp_max_range[fake_tyt_passive.level - 1])
                                    else:
                                        temp_ratio_lists = [0.1, 0.1, 0.15, 0.15, 0.2]
                                        damage_number = int(temp_ratio_lists[fake_tyt_passive.level - 1] * left_final_damage) if temp_ratio_lists[fake_tyt_passive.level - 1] * left_final_damage <= now_role.battle_max_hp * temp_max_range[fake_tyt_passive.level - 1] else int(now_role.battle_max_hp * temp_max_range[fake_tyt_passive.level - 1])
                                    user.hp -= damage_number
                                    if user.hp < 1:
                                        user.hp = 0
                                    user.death_calculate(now_role, skill, enemy_environment_effects, ally_environment_effects, order_members)
                                # 共感：期间任一附加了“心”的单位受到伤害时，将平均分担给其他同样拥有此印记的友方
                                if "共感" in local_config.skill_log_data:
                                    buff_roles = local_config.skill_log_data["共感"]
                                    if now_role in local_config.party and "ally" in buff_roles:
                                        temp_buff_roles = copy(buff_roles["ally"])
                                        left_final_damage = left_final_damage // len(temp_buff_roles)

                                        fake_xz_role = [role for role in local_config.party[:3] if role.name == "青木翔子"][0]
                                        temp_selected_skills = fake_xz_role.base_skills if not fake_xz_role.is_phase2 else fake_xz_role.base_skills_v2
                                        fake_xz_breakout = [s for s in temp_selected_skills if s.category == "Break_out"][0]
                                        
                                        temp_ratio_lists = [0.1, 0.13, 0.16, 0.19, 0.22]
                                        for role in temp_buff_roles:
                                            if role != now_role and role.hp > 0:
                                                role_left_final_damage = int(temp_ratio_lists[fake_xz_breakout.level - 1] * role.battle_max_hp) if left_final_damage > temp_ratio_lists[fake_xz_breakout.level - 1] * role.battle_max_hp else left_final_damage
                                                role.hp -= role_left_final_damage
                                                if role.hp < 1:
                                                    role.hp = 0
                                                role.death_calculate(user, skill, ally_environment_effects, enemy_environment_effects, order_members)
                                    elif role in local_config.enemy and "enemy" in buff_roles:
                                        temp_buff_roles = copy(buff_roles["enemy"])
                                        left_final_damage = left_final_damage // len(temp_buff_roles)

                                        fake_xz_role = [role for role in local_config.enemy[:3] if role.name == "青木翔子"][0]
                                        temp_selected_skills = fake_xz_role.base_skills if not fake_xz_role.is_phase2 else fake_xz_role.base_skills_v2
                                        fake_xz_breakout = [s for s in temp_selected_skills if s.category == "Break_out"][0]
                                        
                                        temp_ratio_lists = [0.1, 0.13, 0.16, 0.19, 0.22]
                                        for role in temp_buff_roles:
                                            if role != now_role and role.hp > 0:
                                                role_left_final_damage = int(temp_ratio_lists[fake_xz_breakout.level - 1] * role.battle_max_hp) if left_final_damage > temp_ratio_lists[fake_xz_breakout.level - 1] * role.battle_max_hp else left_final_damage
                                                role.hp -= role_left_final_damage
                                                if role.hp < 1:
                                                    role.hp = 0
                                                role.death_calculate(user, skill, ally_environment_effects, enemy_environment_effects, order_members)
                                # 祝福涓流：使用“流流舞”造成伤害时，每次为生命比例最低的友方角色治疗该次伤害60%|70%|80%|90%|100%的生命；有8%|10%|12%|14%|16%概率降低对方20%效果命中和效果抵抗，持续2回合
                                if ("祝福涓流", True) in ally_environment_effects and skill.name == "流流舞":
                                    min_hp_role = user
                                    min_hp_ratio = 1.0
                                    if user in local_config.party:
                                        for role in local_config.party[:3]:
                                            if role.hp > 0 and (role.hp / role.battle_max_hp) < min_hp_ratio:
                                                min_hp_role = role
                                                min_hp_ratio = (role.hp / role.battle_max_hp)
                                    elif user in local_config.enemy:
                                        for role in local_config.enemy[:3]:
                                            if role.hp > 0 and (role.hp / role.battle_max_hp) < min_hp_ratio:
                                                min_hp_role = role
                                                min_hp_ratio = (role.hp / role.battle_max_hp)

                                    temp_selected_skills = user.base_skills if not user.is_phase2 else user.base_skills_v2
                                    fake_yj_passive = [s for s in temp_selected_skills if s.category == "Passive"][0]

                                    if min_hp_ratio != 1.0:                            
                                        # 基础治疗量
                                        temp_ratio_lists = [0.6, 0.7, 0.8, 0.9, 1.0]
                                        battle_base_healing = temp_ratio_lists[fake_yj_passive.level - 1] * left_final_damage

                                        # 暴击判定
                                        judgerate = renpy.random.random()
                                        battle_critical_heal = battle_user_critical_rate >= judgerate
                                        
                                        if battle_critical_heal:
                                            single_battle_healing = battle_base_healing * battle_user_critical_damage * (1.0 + battle_user_healing_bonus)
                                            single_battle_healing = int(single_battle_healing)
                                            renpy.show("hcritical", at_list=[show_state(min_hp_role.xposition, 0.35)], layer="screens", what=Text("治疗暴击", style="effect_text", size=80, color="#ee6"))
                                            renpy.show("healing", at_list=[show_damage(min_hp_role.xposition, 0.5)], layer="healing", what=Text("+%s" % single_battle_healing, style="damage_text", size=150, color=damage_color_map["治疗"]))
                                            # renpy.pause(0.5 * persistent.battlespeed)
                                        else:
                                            single_battle_healing = battle_base_healing * (1.0 + battle_user_healing_bonus)
                                            single_battle_healing = int(single_battle_healing)
                                            renpy.show("healing", at_list=[show_damage(min_hp_role.xposition, 0.5)], layer="healing", what=Text("+%s" % single_battle_healing, style="damage_text", size=100, color=damage_color_map["治疗"]))
                                            # renpy.pause(0.5 * persistent.battlespeed)

                                        if single_battle_healing > 0:
                                            renpy.music.play("恢复", channel="battle_music")
                                            # renpy.pause(0.05)

                                            min_hp_role.hp += single_battle_healing
                                            if min_hp_role.hp > min_hp_role.battle_max_hp:
                                                min_hp_role.hp = min_hp_role.battle_max_hp
                                    
                                    temp_ratio_lists = [0.08, 0.1, 0.12, 0.14, 0.16]
                                    if temp_ratio_lists[fake_yj_passive.level - 1] > renpy.random.random():
                                        buff_obj = getattr(store, "seal")
                                        item = (2, 0.2)
                                        buff_obj.calculate(now_role, None, item, "祝福涓流", "get")
                                        buff_obj = getattr(store, "disintegrate")
                                        item = (2, 0.2)
                                        buff_obj.calculate(now_role, None, item, "祝福涓流", "get")
                                # 适应
                                if "Adaptive" in now_role.abilities and 0.08 > renpy.random.random():
                                    renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("适应", style="effect_text", color="ff9"))
                                    media_shield_strength = int(0.6 * battle_base_attack)
                                    # renpy.pause(0.5 * persistent.battlespeed)
                                    # renpy.hide("buff_effect", layer="screens")

                                    # 无盾或同属性才能触发
                                    if "shield" in now_role.buff:
                                        buff_obj = getattr(store, "shield")
                                        shield_time, (shield_strength, shield_element, v1, v2) = now_role.buff["shield"]
                                        if shield_element == battle_skill_element:
                                            item = (2, (media_shield_strength, shield_element, v1, v2))
                                            buff_obj.calculate(now_role, None, item, "Adaptive", "get")
                                    elif "sp_shield" in now_role.buff:
                                        buff_obj = getattr(store, "sp_shield")
                                        shield_time, (shield_strength, shield_element, v1, v2) = now_role.buff["sp_shield"]
                                        if shield_element == battle_skill_element:
                                            item = (2, (media_shield_strength, shield_element, v1, v2))
                                            buff_obj.calculate(now_role, None, item, "Adaptive", "get")
                                    else:
                                        buff_obj = getattr(store, "shield")
                                        item = (2, (media_shield_strength, battle_skill_element, 0.75, 0.5))
                                        buff_obj.calculate(now_role, None, item, "Adaptive", "get")
                                # 皮肤
                                if "Skin" in now_role.abilities and (left_final_damage / now_role.battle_max_hp) > 0.3 and (now_role.hp > left_final_damage) and 0.2 > renpy.random.random():
                                    # 在伤害结算后获得30%的对应元素抗性
                                    item = None
                                    if battle_skill_element == "fire":
                                        item = (2, (0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
                                    elif battle_skill_element == "light":
                                        item = (2, (0.0, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0))
                                    elif battle_skill_element == "wind":
                                        item = (2, (0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0))
                                    elif battle_skill_element == "ice":
                                        item = (2, (0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0))
                                    elif battle_skill_element == "water":
                                        item = (2, (0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0))
                                    elif battle_skill_element == "rock":
                                        item = (2, (0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0))

                                    if item is not None:
                                        renpy.music.play("raged", channel="battle_music")
                                        renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("抗性提升", style="effect_text", color="ff9"))
                                        # renpy.pause(0.5 * persistent.battlespeed)
                                        # renpy.hide("buff_effect")

                                        buff_obj = getattr(store, "control")
                                        buff_obj.calculate(now_role, None, item, "Skin", "get")
                                # 格挡
                                if "Solid" in now_role.abilities and (left_final_damage / now_role.battle_max_hp) > 0.3 and (now_role.hp > left_final_damage) and 0.2 > renpy.random.random():
                                    # 在伤害结算时获得30%的物理抗性
                                    item = None
                                    if battle_skill_element == "physical":
                                        item = (2, (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3))

                                    if item is not None:
                                        renpy.music.play("raged", channel="battle_music")
                                        renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("抗性提升", style="effect_text", color="ff9"))
                                        # renpy.pause(0.5 * persistent.battlespeed)
                                        # renpy.hide("buff_effect")

                                        buff_obj = getattr(store, "control")
                                        buff_obj.calculate(now_role, None, item, "Solid", "get")
                                # 回响 & 狩猎
                                if con_hun_flag[numb]:
                                    if battle_critical:
                                        renpy.show("healing", at_list=[show_damage(user.xposition, 0.5)], layer="screens", what=Text("+10", style="damage_text", size=100, color="#19f"))
                                        # renpy.pause(0.5 * persistent.battlespeed)
                                        # renpy.hide("damage", layer="screens")

                                        user.mp += 10
                                        if user.mp > user.max_mp:
                                            user.mp = user.max_mp
                                # 天之印-碧落
                                if user.equip4effect == "天之印-碧落" and ("天之印-碧落", True) in ally_environment_effects:
                                    if 0.15 > renpy.random.random():
                                        if "domineering" in now_role.buff or "sp_domineering" in now_role.buff:
                                            renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("霸体免控", style="effect_text", color="ff9"))
                                            # renpy.pause(0.5 * persistent.battlespeed)
                                            # renpy.hide("buff_effect", layer="screens")
                                        else:
                                            buff_lists = ["dizziness", "silence", "sleepy", "handicapped"]
                                            buff_items = [(1, None), (1, None), (1, None), (1, 0.4)]
                                            chosen_index = renpy.random.randint(0, len(buff_lists)-1)
                                            chosen_buff = buff_lists[chosen_index]
                                            chosen_item = buff_items[chosen_index]

                                            buff_obj = getattr(store, chosen_buff)
                                            buff_obj.calculate(now_role, None, chosen_item, "天之印-碧落", "get")
                                # 地之轴-方仪
                                if now_role.equip4effect == "地之轴-方仪" and ("地之轴-方仪", True) in enemy_environment_effects and battle_critical:
                                    if 0.3 > renpy.random.random():
                                        if now_role in local_config.party:
                                            for role in local_config.party[:3]:
                                                if role.hp > 0:
                                                    if "shield" in role.buff:
                                                        buff_obj = getattr(store, "shield")
                                                        shield_time, (shield_strength, shield_element, v1, v2) = role.buff["shield"]
                                                        if shield_element == battle_skill_element:
                                                            item = (1, (int(0.1 * now_role.battle_max_hp), battle_skill_element, v1, v2))
                                                            buff_obj.calculate(role, None, item, "地之轴-方仪", "get")
                                                    elif "sp_shield" in role.buff:
                                                        buff_obj = getattr(store, "sp_shield")
                                                        shield_time, (shield_strength, shield_element, v1, v2) = role.buff["sp_shield"]
                                                        if shield_element == battle_skill_element:
                                                            item = (1, (int(0.1 * now_role.battle_max_hp), battle_skill_element, v1, v2))
                                                            buff_obj.calculate(role, None, item, "地之轴-方仪", "get")
                                                    else:
                                                        buff_obj = getattr(store, "shield")
                                                        item = (1, (int(0.1 * now_role.battle_max_hp), battle_skill_element, 0.75, 0.5))
                                                        buff_obj.calculate(role, None, item, "地之轴-方仪", "get")
                                # 海之澜-沧渊
                                if user.equip4effect == "海之澜-沧渊" and ("海之澜-沧渊", True) in ally_environment_effects:
                                    tmp_buff_lists = [buf_name for buf_name, item_name in now_role.buff.items() if item_name[0] != 99]
                                    if (len(tmp_buff_lists) > 0 and 0.3 > renpy.random.random()) or (len(tmp_buff_lists) == 0 and 0.2 > renpy.random.random()):
                                        now_role.order -= 300
                                # 风之陨-松吹
                                if ("风之陨-松吹", True) in enemy_environment_effects:
                                    buff_roles = local_config.skill_log_data.setdefault("风之陨-松吹", {})
                                    if user not in buff_roles:
                                        if 0.2 > renpy.random.random():
                                            renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("能量损失", style="effect_text", color="ff9"))
                                            # renpy.pause(0.5 * persistent.battlespeed)
                                            # renpy.hide("buff_effect", layer="screens")
                                            user.mp -= 10
                                            if user.mp < 0:
                                                user.mp = 0
                                # 雪之嚣-玉絮
                                if user.equip4effect == "雪之嚣-玉絮" and ("雪之嚣-玉絮", True) in ally_environment_effects:
                                    frozen_ratio = 0.2 if "slow" in now_role.debuff else 0.12

                                    # 技能效果命中率 = 技能基础命中 x (1 + 面板效果命中)
                                    battle_effect_hitrate_final = frozen_ratio * (1 + battle_user_effect_hitrate)
                                    # 技能效果抵抗率 = 1 - 100% / (100% + 面板效果抵抗)
                                    battle_effect_resistance_final = 1.0 - 1.0 / (1.0 + battle_target_effect_resistance)

                                    # 命中判定
                                    if battle_effect_hitrate_final > renpy.random.random():
                                        if "domineering" in now_role.buff or "sp_domineering" in now_role.buff:
                                            renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("霸体免控", style="effect_text", color="ff9"))
                                            # renpy.pause(0.5 * persistent.battlespeed)
                                            # renpy.hide("buff_effect", layer="screens")
                                        # 抵抗判定
                                        elif battle_effect_resistance_final < renpy.random.random():
                                            renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("冻结", style="effect_text", size=80, color=damage_color_map["冻结"]))
                                            buff_obj = getattr(store, "frozen")
                                            item = (1, 0.5)
                                            buff_obj.calculate(now_role, None, item, "雪之嚣-玉絮", "get")
                                        else:
                                            renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("抵抗", style="effect_text", color="ff9"))
                                            # renpy.pause(0.5 * persistent.battlespeed)
                                if now_role.equip4effect == "雪之嚣-玉絮" and ("雪之嚣-玉絮", True) in enemy_environment_effects:
                                    if 0.3 > renpy.random.random():
                                        renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("减速", style="effect_text", color="ff9"))
                                        buff_obj = getattr(store, "slow")
                                        item = (1, 20)
                                        buff_obj.calculate(user, None, item, "雪之嚣-玉絮", "get")
                                # 瓦轮刑部结界
                                if "rock_wall" in now_role.buff:
                                    left_final_damage = max(1, int(left_final_damage * 0.1))
                                # 队友守护
                                if "sp_protect" in now_role.buff:
                                    renpy.show("critical", at_list=[show_damage(now_role.xposition, 0.35)], layer="screens", what=Text("无效", style="effect_text", size=80, color="#ee6"))
                                    if local_config.tutorial_step == "虚无封印":
                                        left_final_damage = 1
                                    else:
                                        left_final_damage = 0

                                if "伤害记录" in local_config.skill_log_data and now_role in local_config.enemy:
                                    local_config.skill_log_data["伤害记录"] += left_final_damage
                                    yj_role.hp += left_final_damage
                                    if yj_role.hp > yj_role.battle_max_hp:
                                        yj_role.hp = yj_role.battle_max_hp

                                # 伤害音效、数值显示
                                if battle_critical:
                                    renpy.music.play("critical_hit", channel="battle_music")
                                    renpy.show("critical_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.35)], layer="screens", what=Text("暴击", style="effect_text", size=80, color="#ee6"))
                                    renpy.show("damage_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.5)], layer="damage", what=Text("%s" % left_final_damage, style="damage_text", size=150, color=damage_color_map[battle_skill_element]))
                                else:
                                    renpy.music.play("hit", channel="battle_music")
                                    renpy.show("damage_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.5)], layer="screens", what=Text("%s" % left_final_damage, style="damage_text", size=100, color=damage_color_map[battle_skill_element]))

                                # 表情更新
                                now_role.face_change(hit=False, hitted=True)
                                # 受到伤害角色抖动特效
                                if now_role in local_config.party:
                                    renpy.show(now_role.objectname, at_list=[shake, hide_out], layer="fg")
                                else:
                                    renpy.show(now_role.objectname, at_list=[smallshake])

                                now_role.hp -= left_final_damage
                                if now_role.hp < 1:
                                    now_role.hp = 0
                                
                                if sp_rull == "空间跳跃":
                                    fake_lst_role = None
                                    if user in local_config.party:
                                        for temp_role in local_config.party:
                                            if temp_role.name == "雷亚":
                                                fake_lst_role = temp_role
                                    else:
                                        for temp_role in local_config.enemy:
                                            if temp_role.name == "雷亚":
                                                fake_lst_role = temp_role
                                    temp_selected_skill = fake_lst_role.skills if not fake_lst_role.is_phase2 else fake_lst_role.skills_v2
                                    fake_lst_skill = [s for s in temp_selected_skill if s.category == "Break_out"][0]

                                    if fake_lst_skill.level > 1:
                                        temp_ratio_lists = [0.0, 0.2, 0.3, 0.4, 0.4]
                                        temp_dmg_healing = int(left_final_damage * temp_ratio_lists[fake_lst_skill.level - 1])
                                        renpy.show("healing", at_list=[show_damage(user.xposition, 0.5)], layer="healing", what=Text("+%s" % temp_dmg_healing, style="damage_text", size=100, color=damage_color_map["治疗"]))
                                        # renpy.pause(0.5 * persistent.battlespeed)
                                        user.hp += temp_dmg_healing
                                        if user.hp > user.battle_max_hp:
                                            user.hp = user.battle_max_hp
                                # renpy.pause(0.75 * persistent.battlespeed)
                            else:
                                # 伤害音效、数值显示
                                if battle_critical:
                                    renpy.music.play("critical_hit", channel="battle_music")
                                    renpy.show("critical_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.35)], layer="screens", what=Text("暴击", style="effect_text", size=80, color="#ee6"))
                                    renpy.show("damage_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.5)], layer="damage", what=Text("0", style="damage_text", size=150, color=damage_color_map[battle_skill_element]))
                                else:
                                    renpy.music.play("hit", channel="battle_music")
                                    renpy.show("damage_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.5)], layer="damage", what=Text("0", style="damage_text", size=100, color=damage_color_map[battle_skill_element]))

                                # 受到伤害角色抖动特效
                                if now_role in local_config.party:
                                    renpy.show(now_role.objectname, at_list=[shake, hide_out], layer="fg")
                                else:
                                    renpy.show(now_role.objectname, at_list=[smallshake])
                                # renpy.pause(0.75 * persistent.battlespeed)

                            ## 元素反应
                            # 聚变、形态反应（超载：攻击力200%火元素伤害、冻结：20%基础概率冻结、感电：125%攻击固定数值间接伤害、超导：40%物理抗性衰减、扩散：40%对应元素抗性衰减、结晶：攻击力60%元素护盾获得）
                            # 火->雷 or 雷->火 | 超载反应伤害 = 基础伤害 x (1 + 元素精通加成) x 火元素最终抗性
                            battle_overload_damage = 0.0
                            if (battle_skill_element == "fire" and "light" in now_role.ebuff) or (battle_skill_element == "light" and "fire" in now_role.ebuff):
                                battle_target_fire_elemental_resistance = now_role.battle_fire_elemental_resistance
                                if battle_target_fire_elemental_resistance >= 0:
                                    battle_fire_resistance_damage_rate = 1 - battle_target_fire_elemental_resistance
                                else:
                                    battle_fire_resistance_damage_rate = 1 - (0.5 * battle_target_fire_elemental_resistance)

                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    battle_overload_damage = int(battle_fundamental_damage * (2.4 + battle_elemental_mastery_bonus2) * battle_fire_resistance_damage_rate)
                                else:
                                    battle_overload_damage = int(battle_fundamental_damage * (2.0 + battle_elemental_mastery_bonus2) * battle_fire_resistance_damage_rate)

                                if "light" in now_role.ebuff:
                                    now_role.ebuff["light"] -= 2
                                    if now_role.ebuff["light"] <= 0:
                                        now_role.ebuff.pop("light")
                                elif "fire" in now_role.ebuff:
                                    now_role.ebuff["fire"] -= 2
                                    if now_role.ebuff["fire"] <= 0:
                                        now_role.ebuff.pop("fire")

                                inner_react[numb] = True

                                overload_left_final_damage = battle_overload_damage
                                # 护盾抵消（伤害计算优先扣除护盾）
                                if "sp_shield" in now_role.buff:
                                    shield_time, shield_effects = now_role.buff["sp_shield"]
                                    shield_strength, shield_element, _, _ = shield_effects
                                    shield_damage_ratio = 1.0
                                    # 属性克制（强势1.5倍、弱势0.5倍）
                                    if shield_element == "ice":
                                        shield_damage_ratio = 1.5
                                    elif shield_element == "water":
                                        shield_damage_ratio = 0.5
                                    # 属性调和（0.25倍）
                                    elif shield_element == "fire":
                                        shield_damage_ratio = 0.25

                                    left_shield_strength = int(shield_strength - shield_damage_ratio * battle_overload_damage)
                                    # 如果护盾还未消失，更新护盾
                                    shield_buff = getattr(store, "sp_shield")
                                    item = (shield_time, (left_shield_strength, shield_element, 0.75, 0.5))
                                    shield_buff.calculate(now_role, None, item, None, "get")
                                    overload_left_final_damage = 0.0

                                    # 如果护盾破碎，驱散护盾并结算剩余伤害
                                    if "sp_shield" not in now_role.buff:
                                        # 穿透伤害
                                        if left_shield_strength < 0:
                                            overload_left_final_damage = -int(left_shield_strength/shield_damage_ratio)
                                if "shield" in now_role.buff:
                                    shield_time, shield_effects = now_role.buff["shield"]
                                    shield_strength, shield_element, _, _ = shield_effects
                                    shield_damage_ratio = 1.0
                                    # 属性克制（强势1.5倍、弱势0.5倍）
                                    if shield_element == "ice":
                                        shield_damage_ratio = 1.5
                                    elif shield_element == "water":
                                        shield_damage_ratio = 0.5
                                    # 属性调和（0.25倍）
                                    elif shield_element == "fire":
                                        shield_damage_ratio = 0.25

                                    left_shield_strength = int(shield_strength - shield_damage_ratio * battle_overload_damage)
                                    # 更新护盾
                                    shield_buff = getattr(store, "shield")
                                    item = (shield_time, (left_shield_strength, shield_element, 0.75, 0.5))
                                    shield_buff.calculate(now_role, None, item, None, "get")
                                    overload_left_final_damage = 0.0
                                    
                                    # 如果护盾破碎，驱散护盾并结算剩余伤害
                                    if "shield" not in now_role.buff:
                                        # 穿透伤害
                                        if left_shield_strength < 0:
                                            overload_left_final_damage = -int(left_shield_strength/shield_damage_ratio)

                                renpy.music.play("critical_hit", channel="battle_music")

                                # 队友守护
                                if "sp_protect" in now_role.buff:
                                    renpy.show("critical_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.35)], layer="screens", what=Text("无效", style="effect_text", size=80, color="#ee6"))
                                    if local_config.tutorial_step == "虚无封印":
                                        overload_left_final_damage = 1
                                    else:
                                        overload_left_final_damage = 0

                                if overload_left_final_damage > 0.0:
                                    renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("超载", style="effect_text", size=80, color=damage_color_map["超载"]))
                                    renpy.show("damage_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.4)], layer="damage_element", what=Text("%s" % overload_left_final_damage, style="damage_text", size=100, color=damage_color_map["超载"]))
                                    # 角色伤害承受
                                    # 表情更新
                                    now_role.face_change(hit=False, hitted=True)
                                    # 受到伤害角色抖动特效
                                    if now_role in local_config.party:
                                        renpy.show(now_role.objectname, at_list=[shake, hide_out], layer="fg")
                                    else:
                                        renpy.show(now_role.objectname, at_list=[smallshake])
                                    # renpy.pause(0.75 * persistent.battlespeed)

                                    # 解除“瓦轮刑部”结界
                                    if "rock_wall" in now_role.buff:
                                        buff_obj = getattr(store, "rock_wall")
                                        buff_obj.calculate(now_role, None, None, None, "clean")

                                    if "伤害记录" in local_config.skill_log_data and now_role in local_config.enemy:
                                        local_config.skill_log_data["伤害记录"] += overload_left_final_damage
                                        yj_role.hp += overload_left_final_damage
                                        if yj_role.hp > yj_role.battle_max_hp:
                                            yj_role.hp = yj_role.battle_max_hp

                                    now_role.hp -= overload_left_final_damage
                                    if now_role.hp < 1:
                                        now_role.hp = 0

                                    # “遗念镜”祝福
                                    if now_role in local_config.party and "超载" in local_config.battle_blessing and 0.4 > renpy.random.random():
                                        now_role.order -= local_config.battle_blessing["超载"]
                            # 冻结 = 20% x (1 + 元素精通加成)
                            if (battle_skill_element == "ice" and "water" in now_role.ebuff) or (battle_skill_element == "water" and "ice" in now_role.ebuff):
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    reaction_frozen_ratio = 0.3 * (1 + battle_elemental_mastery_bonus)
                                else:
                                    reaction_frozen_ratio = 0.2 * (1 + battle_elemental_mastery_bonus)

                                # “遗念镜”祝福
                                if now_role in local_config.party and "冻结" in local_config.battle_blessing:
                                    reaction_frozen_ratio += local_config.battle_blessing["冻结"]

                                # 技能效果命中率 = 技能基础命中 x (1 + 面板效果命中)
                                battle_effect_hitrate_final = reaction_frozen_ratio * (1 + battle_user_effect_hitrate)
                                # 技能效果抵抗率 = 1 - 100% / (100% + 面板效果抵抗)
                                battle_effect_resistance_final = 1.0 - 1.0 / (1.0 + battle_target_effect_resistance)

                                # 命中判定
                                if battle_effect_hitrate_final > renpy.random.random():
                                    if "domineering" in now_role.buff or "sp_domineering" in now_role.buff:
                                        renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("霸体免控", style="effect_text", color="ff9"))
                                        # renpy.pause(0.5 * persistent.battlespeed)
                                        # renpy.hide("buff_effect", layer="screens")
                                    # 抵抗判定
                                    elif battle_effect_resistance_final < renpy.random.random():
                                        hitted[numb] = True
                                        renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("冻结", style="effect_text", size=80, color=damage_color_map["冻结"]))
                                        buff_obj = getattr(store, "frozen")
                                        item = (2, 0.5)
                                        buff_obj.calculate(now_role, None, item, "frozen-reaction", "get")
                                        if "ice" in now_role.ebuff:
                                            now_role.ebuff["ice"] = max(now_role.ebuff["ice"], 1)
                                        else:
                                            now_role.ebuff = {"ice": 1}
                                    else:
                                        renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("抵抗", style="effect_text", color="ff9"))
                                        renpy.pause(0.5)

                                if "water" in now_role.ebuff:
                                    now_role.ebuff["water"] -= 2
                                    if now_role.ebuff["water"] <= 0:
                                        now_role.ebuff.pop("water")
                                elif "ice" in now_role.ebuff:
                                    now_role.ebuff["ice"] -= 2
                                    if now_role.ebuff["ice"] <= 0:
                                        now_role.ebuff.pop("ice")

                                inner_react[numb] = True
                            # 感电 = 125%攻击固定数值间接伤害 x (1 + 元素精通加成)
                            if (battle_skill_element == "water" and "light" in now_role.ebuff) or (battle_skill_element == "light" and "water" in now_role.ebuff):
                                renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("感电", style="effect_text", size=80, color=damage_color_map["感电"]))
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    media_damage_number = int(battle_base_attack * (1.65 + battle_elemental_mastery_bonus2))
                                else:
                                    media_damage_number = int(battle_base_attack * (1.25 + battle_elemental_mastery_bonus2))
                                hitted[numb] = True
                                buff_obj = getattr(store, "mdamage")
                                item = (2, (media_damage_number, "light", "感电", user))
                                buff_obj.calculate(now_role, None, item, "induct-reaction", "get")
                                buff_roles = local_config.skill_log_data.setdefault("间接伤害", {})
                                buff_roles[now_role] = (media_damage_number, "light", "感电", user)

                                if "water" in now_role.ebuff:
                                    now_role.ebuff["water"] -= 2
                                    if now_role.ebuff["water"] <= 0:
                                        now_role.ebuff.pop("water")
                                elif "light" in now_role.ebuff:
                                    now_role.ebuff["light"] -= 2
                                    if now_role.ebuff["light"] <= 0:
                                        now_role.ebuff.pop("light")

                                inner_react[numb] = True
                            # 超导 = 70%物理抗性衰减
                            if (battle_skill_element == "ice" and "light" in now_role.ebuff) or (battle_skill_element == "light" and "ice" in now_role.ebuff):
                                renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("超导", style="effect_text", size=80, color=damage_color_map["超导"]))
                                buff_obj = getattr(store, "suppress")
                                hitted[numb] = True
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    tmp_ratio_down = 0.85
                                else:
                                    tmp_ratio_down = 0.7
                                item = (2, (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, tmp_ratio_down))
                                buff_obj.calculate(now_role, None, item, "superconduct-reaction", "get")

                                if "ice" in now_role.ebuff:
                                    now_role.ebuff["ice"] -= 2
                                    if now_role.ebuff["ice"] <= 0:
                                        now_role.ebuff.pop("ice")
                                elif "light" in now_role.ebuff:
                                    now_role.ebuff["light"] -= 2
                                    if now_role.ebuff["light"] <= 0:
                                        now_role.ebuff.pop("light")

                                inner_react[numb] = True
                            # 扩散 = 40%对应元素抗性衰减
                            if battle_skill_element == "wind" and ("fire" in now_role.ebuff or "light" in now_role.ebuff or "water" in now_role.ebuff or "ice" in now_role.ebuff):
                                renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("扩散", style="effect_text", size=80, color=damage_color_map["扩散"]))
                                buff_obj = getattr(store, "suppress")
                                hitted[numb] = True
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    tmp_ratio_down = 0.55
                                else:
                                    tmp_ratio_down = 0.4
                                if "fire" in now_role.ebuff:
                                    item = (2, (tmp_ratio_down, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
                                elif "light" in now_role.ebuff:
                                    item = (2, (0.0, tmp_ratio_down, 0.0, 0.0, 0.0, 0.0, 0.0))
                                elif "water" in now_role.ebuff:
                                    item = (2, (0.0, 0.0, 0.0, 0.0, tmp_ratio_down, 0.0, 0.0))
                                elif "ice" in now_role.ebuff:
                                    item = (2, (0.0, 0.0, 0.0, tmp_ratio_down, 0.0, 0.0, 0.0))
                                buff_obj.calculate(now_role, None, item, "diffusion-reaction", "get")

                                if "ice" in now_role.ebuff:
                                    now_role.ebuff["ice"] -= 2
                                    if now_role.ebuff["ice"] <= 0:
                                        now_role.ebuff.pop("ice")
                                elif "light" in now_role.ebuff:
                                    now_role.ebuff["light"] -= 2
                                    if now_role.ebuff["light"] <= 0:
                                        now_role.ebuff.pop("light")
                                elif "fire" in now_role.ebuff:
                                    now_role.ebuff["fire"] -= 2
                                    if now_role.ebuff["fire"] <= 0:
                                        now_role.ebuff.pop("fire")
                                elif "water" in now_role.ebuff:
                                    now_role.ebuff["water"] -= 2
                                    if now_role.ebuff["water"] <= 0:
                                        now_role.ebuff.pop("water")

                                inner_react[numb] = True
                            # 结晶 = 获得攻击力60%元素护盾
                            if battle_skill_element == "rock" and ("fire" in now_role.ebuff or "light" in now_role.ebuff or "water" in now_role.ebuff or "ice" in now_role.ebuff):
                                renpy.show("elemental_%s" % str(numb), at_list=[show_state(now_role.xposition, 0.25)], layer="buff_element", what=Text("结晶", style="effect_text", size=80, color=damage_color_map["结晶"]))
                                if user.equip4effect == "夏之声-朱明" and ("夏之声-朱明", True) in ally_environment_effects:
                                    media_shield_strength = int(0.85 * battle_base_attack)
                                else:
                                    media_shield_strength = int(0.6 * battle_base_attack)

                                if "fire" in now_role.ebuff:
                                    gain_element = "fire"
                                elif "light" in now_role.ebuff:
                                    gain_element = "light"
                                elif "water" in now_role.ebuff:
                                    gain_element = "water"
                                elif "ice" in now_role.ebuff:
                                    gain_element = "ice"
                                
                                # 无盾或同属性才能触发
                                if "shield" in user.buff:
                                    buff_obj = getattr(store, "shield")
                                    shield_time, (shield_strength, shield_element, v1, v2) = user.buff["shield"]
                                    if shield_element == gain_element:
                                        item = (2, (media_shield_strength, shield_element, v1, v2))
                                        buff_obj.calculate(user, None, item, "crystallization-reaction", "get")
                                elif "sp_shield" in user.buff:
                                    buff_obj = getattr(store, "sp_shield")
                                    shield_time, (shield_strength, shield_element, v1, v2) = user.buff["sp_shield"]
                                    if shield_element == gain_element:
                                        item = (2, (media_shield_strength, shield_element, v1, v2))
                                        buff_obj.calculate(user, None, item, "crystallization-reaction", "get")
                                else:
                                    buff_obj = getattr(store, "shield")
                                    item = (2, (media_shield_strength, gain_element, 0.75, 0.5))
                                    buff_obj.calculate(user, None, item, "crystallization-reaction", "get")

                                if "ice" in now_role.ebuff:
                                    now_role.ebuff["ice"] -= 2
                                    if now_role.ebuff["ice"] <= 0:
                                        now_role.ebuff.pop("ice")
                                elif "light" in now_role.ebuff:
                                    now_role.ebuff["light"] -= 2
                                    if now_role.ebuff["light"] <= 0:
                                        now_role.ebuff.pop("light")
                                elif "fire" in now_role.ebuff:
                                    now_role.ebuff["fire"] -= 2
                                    if now_role.ebuff["fire"] <= 0:
                                        now_role.ebuff.pop("fire")
                                elif "water" in now_role.ebuff:
                                    now_role.ebuff["water"] -= 2
                                    if now_role.ebuff["water"] <= 0:
                                        now_role.ebuff.pop("water")

                                inner_react[numb] = True

                            # 元素附着（本身无元素附着 or 附着元素相同）
                            # 发生元素反应后不附着
                            if not inner_react[numb]:
                                if ("Skin" not in now_role.abilities) or ("Skin" in now_role.abilities and 0.5 > renpy.random.random()):
                                    if battle_skill_element in now_role.ebuff:
                                        now_role.ebuff[battle_skill_element] += 1
                                    elif battle_skill_element and battle_skill_element not in ["wind", "rock", "physical"] and len(now_role.ebuff) == 0:
                                        now_role.ebuff[battle_skill_element] = 1
                        multi_buff_lock_damage = True

                    renpy.pause(0.75 * persistent.battlespeed)

            # 治疗 = 技能基础治疗量 x 爆伤 x (1 + 治疗加成)
            if "治疗" in skill.effects:
                ratio, target, _ = skill.effects["治疗"]
                if not isinstance(ratio, list):
                    ratio = [ratio]
                if not isinstance(target, list):
                    target = [target]

                heal_ratios = [copy(ratio) for i in range(len(use_targets))]
                heal_targets = [copy(target) for i in range(len(use_targets))]

                for battle_heal_ratio, battle_heal_target in zip(zip(*heal_ratios), zip(*heal_targets)):
                    for numb, (now_role, rat, tar) in enumerate(zip(use_targets, battle_heal_ratio, battle_heal_target)):
                        battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack = now_role.battle_role_init(user, now_role, ally_environment_effects, enemy_environment_effects, sp_rull)

                        if tar == "base_attack":
                            role_attribute = battle_base_attack
                        else:
                            role_attribute = getattr(now_role, "battle_%s" % tar)
                        # 基础治疗量
                        battle_base_healing = rat * role_attribute

                        # 暴击判定
                        judgerate = renpy.random.random()
                        battle_critical_heal = battle_user_critical_rate >= judgerate

                        if battle_critical_heal:
                            single_battle_healing = battle_base_healing * battle_user_critical_damage * (1.0 + battle_user_healing_bonus)
                            single_battle_healing = int(single_battle_healing)
                            renpy.show("critical_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.35)], layer="screens", what=Text("治疗暴击", style="effect_text", size=80, color="#ee6"))
                            renpy.show("healing_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.5)], layer="healing", what=Text("+%s" % single_battle_healing, style="damage_text", size=150, color=damage_color_map["治疗"]))
                            # renpy.pause(0.5 * persistent.battlespeed)
                        else:
                            single_battle_healing = battle_base_healing * (1.0 + battle_user_healing_bonus)
                            single_battle_healing = int(single_battle_healing)
                            renpy.show("healing_%s" % str(numb), at_list=[show_damage(now_role.xposition, 0.5)], layer="healing", what=Text("+%s" % single_battle_healing, style="damage_text", size=100, color=damage_color_map["治疗"]))
                            # renpy.pause(0.5 * persistent.battlespeed)

                        if single_battle_healing > 0:
                            renpy.music.play("恢复", channel="battle_music")
                            # renpy.pause(0.05)
                            now_role.hp += int(single_battle_healing)
                            if now_role.hp > now_role.battle_max_hp:
                                now_role.hp = now_role.battle_max_hp
                    renpy.pause(0.5 * persistent.battlespeed)

            # 护盾 = 技能基础护盾量 x (1 + 护盾强效)
            if "护盾" in skill.effects:
                ratio, target, time = skill.effects["护盾"]
                shield_element = skill.element

                shield_ratios = [copy(ratio) for i in range(len(use_targets))]
                shield_targets = [copy(target) for i in range(len(use_targets))]
                shield_elements = [copy(shield_element) for i in range(len(use_targets))]
                
                for battle_shield_ratio, battle_shield_target, battle_shield_element in zip(zip(*shield_ratios), zip(*shield_targets), zip(*shield_elements)):
                    for numb, (now_role, rat, tar, ele) in enumerate(zip(use_targets, battle_shield_ratio, battle_shield_target, battle_shield_element)):
                        battle_elemental_mastery_bonus, battle_elemental_mastery_bonus2, battle_user_critical_rate, battle_user_critical_damage, battle_user_healing_bonus, battle_user_shield_strength, battle_target_defance, battle_base_attack = now_role.battle_role_init(user, now_role, ally_environment_effects, enemy_environment_effects, sp_rull)
                        # 基础护盾量
                        role_attribute = getattr(now_role, "battle_%s" % tar)
                        battle_base_shield_strength = rat * role_attribute
                        single_battle_shield_strength = battle_base_shield_strength * (1 + battle_user_shield_strength)

                        if single_battle_shield_strength > 0:
                            buff_obj = getattr(store, "shield")
                            item = (time, (int(single_battle_shield_strength), ele, 0.75, 0.5))
                            buff_obj.calculate(now_role, None, item, skill.name, "get")
            
            ## 附加buff
            # 拉条
            if "拉条" in skill.effects:
                ratio, target, time = skill.effects["拉条"]

                order_ratios = [copy(ratio) for i in range(len(use_targets))]
                order_targets = [copy(target) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar) in enumerate(zip(use_targets, order_ratios, order_targets)):
                    if rat > 0.0:
                        # 思维透视
                        if skill.name == "思维透视":
                            disable = False
                            for debuff in now_role.debuff:
                                if debuff in ["silence", "dizziness", "confusion", "frozen", "sleepy", "ridicule", "deep_frozen", "deep_sleepy"]:
                                    disable = True
                                    break
                            # 该角色处于“无法行动”状态则改为解除其控制状态
                            if disable:
                                for debuff in ["silence", "dizziness", "confusion", "frozen", "sleepy", "ridicule", "deep_frozen", "deep_sleepy"]:
                                    if debuff in now_role.debuff:
                                        buff_obj = getattr(store, debuff)
                                        buff_obj.calculate(now_role, None, None, None, "clean")
                                # 恢复20%|25%|30%|35%|40%生命值
                                temp_ratio_lists = [0.2, 0.25, 0.3, 0.35, 0.4]
                                now_role.hp += int(now_role.battle_max_hp * temp_ratio_lists[skill.level - 1])
                                if now_role.hp > now_role.battle_max_hp:
                                    now_role.hp = now_role.battle_max_hp
                                if skill.level in [2, 3, 4, 5]:
                                    temp_ratio_lists = [10, 15, 20, 20]
                                    # 增加0|10|15|20|20点速度
                                    buff_obj = getattr(store, "flow")
                                    item = (1, temp_ratio_lists[skill.level - 1])
                                    buff_obj.calculate(now_role, None, item, skill.name, "get")
                            else:
                                now_role.order += int(ratio * 1000)
                                renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
                        else:
                            now_role.order += int(ratio * 1000)
                            renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
            
            media_buff_anime = set()
            # 强攻
            if "强攻" in skill.effects:
                ratio, target, time = skill.effects["强攻"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        media_buff_anime.add("damage_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "strong")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 强袭
            if "强袭" in skill.effects:
                ratio, target, time = skill.effects["强袭"]
                
                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        media_buff_anime.add("damage_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "violence")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 精通
            if "精通" in skill.effects:
                ratio, target, time = skill.effects["精通"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if ratio > 0.0:
                        media_buff_anime.add("damage_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "master")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 精防
            if "精防" in skill.effects:
                ratio, target, time = skill.effects["精防"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        media_buff_anime.add("defance_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "sturdy")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 属性强效
            if "属性强效" in skill.effects:
                ratio, target, time = skill.effects["属性强效"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        media_buff_anime.add("damage_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "condensed")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 属性抗效
            if "属性抗效" in skill.effects:
                ratio, target, time = skill.effects["属性抗效"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        media_buff_anime.add("defance_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "control")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 属性抗衰
            if "属性抗衰" in skill.effects:
                ratio, target, time = skill.effects["属性抗衰"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "suppress")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 加速
            if "加速" in skill.effects:
                ratio, target, time = skill.effects["加速"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        media_buff_anime.add("speed_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "flow")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 减速
            if "减速" in skill.effects:
                ratio, target, time = skill.effects["减速"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "slow")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 抗效
            if "抗效" in skill.effects:
                ratio, target, time = skill.effects["抗效"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        media_buff_anime.add("resistance_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "barrier")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 命中
            if "命中" in skill.effects:
                ratio, target, time = skill.effects["命中"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        media_buff_anime.add("resistance_up_img")
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "liberate")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 命中衰减
            if "命中衰减" in skill.effects:
                ratio, target, time = skill.effects["命中衰减"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "seal")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 抗效衰减
            if "抗效衰减" in skill.effects:
                ratio, target, time = skill.effects["抗效衰减"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    if rat > 0.0:
                        if "Acrobat" in user.abilities and 0.25 > renpy.random.random():
                            time += 1
                        buff = getattr(store, "disintegrate")
                        item = (time, ratio)
                        buff.calculate(now_role, None, item, skill.name, "get")
            # 充能
            if "充能" in skill.effects:
                ratio, target, time = skill.effects["充能"]

                eratios = [copy(ratio) for i in range(len(use_targets))]
                etargets = [copy(target) for i in range(len(use_targets))]
                etimes = [copy(time) for i in range(len(use_targets))]

                for numb, (now_role, rat, tar, time) in enumerate(zip(use_targets, eratios, etargets, etimes)):
                    renpy.show("healing", at_list=[show_damage(now_role.xposition, 0.5)], layer="screens", what=Text("+%s" % ratio, style="damage_text", size=100, color=damage_color_map["能量"]))
                    # renpy.pause(0.5 * persistent.battlespeed)
                    now_role.mp += ratio
                    if now_role.mp > now_role.max_mp:
                        now_role.mp = now_role.max_mp

            media_buff_times = {
                "healing_img": 0.96,
                "shield_img": 1.2,
                "damage_up_img": 1.35,
                "defance_up_img": 1.35,
                "speed_up_img": 0.96,
                "resistance_up_img": 0.72,
                "charge_img": 0.72
            }
            
            if len(media_buff_anime) > 0:
                renpy.music.play("加成", channel="battle_music")
                # renpy.pause(0.05)
            for anime in media_buff_anime:
                if anime in ["speed_up_img", "resistance_up_img"]:
                    renpy.show(anime, at_list=[Transform(anchor=(0.5, 0.5), zoom=1.5, xpos=self.xposition, ypos=0.4)], layer="screens")
                else:
                    renpy.show(anime, at_list=[Transform(anchor=(0.5, 0.5), zoom=2.5, xpos=self.xposition, ypos=0.4)], layer="screens")
                renpy.pause(media_buff_times[anime] * persistent.battlespeed)
                renpy.hide(anime, layer="screens")

            ## 技能附加效果
            multi_buff_lock_effect = False
            for numb, now_role in enumerate(use_targets):
                # 精准掌握：在施放“不知火”时，有30%概率降低目标火元素伤害抗性和元素精通，持续2回合；在施放“冥火”时，有8%|10%|12%|15%|15%固定概率使目标眩晕1回合
                if ("精准掌握", True) in ally_environment_effects and user.name == "花山院琉璃":
                    temp_selected_skill = user.skills if not user.is_phase2 else user.skills_v2
                    passive_skill = [s for s in temp_selected_skill if s.category == "Passive"][0]

                    if skill.name == "不知火" and 0.3 > renpy.random.random():
                        temp_ratio_lists = [0.25, 0.3, 0.3, 0.35, 0.35]
                        buff = getattr(store, "suppress")
                        item = (2, (temp_ratio_lists[passive_skill.level - 1], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
                        buff.calculate(now_role, None, item, skill.name, "get")

                        temp_ratio_lists = [50, 50, 70, 80, 80]
                        buff = getattr(store, "churn")
                        item = (2, temp_ratio_lists[passive_skill.level - 1])
                        buff.calculate(now_role, None, item, skill.name, "get")
                    elif skill.name == "冥火" and "domineering" not in now_role.buff and "sp_domineering" not in now_role.buff:
                        temp_ratio_lists = [0.08, 0.1, 0.12, 0.15, 0.15]
                        if temp_ratio_lists[passive_skill.level - 1] > renpy.random.random():
                            buff = getattr(store, "dizziness")
                            item = (1, None)

                            # 反射天赋触发
                            if "Reflexes" in now_role.abilities and 0.08 > renpy.random.random():
                                renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("反射", style="effect_text", color="ff9"))
                                # renpy.pause(0.5 * persistent.battlespeed)
                                # renpy.hide("buff_effect", layer="screens")
                                buff.calculate(user, None, item, skill.name, "get")
                            else:
                                buff.calculate(now_role, None, item, skill.name, "get")
                ## 特定技能效果区
                if skill.name == "温柔的祝福":
                    # 献祭自身当前生命
                    if not multi_buff_lock:
                        if skill.level == 1:
                            user.hp = max(int(user.hp * 0.8), 1)
                        elif skill.level == 2:
                            user.hp = max(int(user.hp * 0.82), 1)
                        elif skill.level == 3:
                            user.hp = max(int(user.hp * 0.84), 1)
                        elif skill.level == 4:
                            user.hp = max(int(user.hp * 0.86), 1)
                        elif skill.level == 5:
                            user.hp = max(int(user.hp * 0.88), 1)
                    # 驱散1个减益或控制效果
                    debuffs = copy(now_role.debuff)
                    count = 0
                    for buff_name in debuffs:
                        buff_obj = getattr(store, buff_name)
                        if buff_obj.removeable:
                            buff_obj.calculate(now_role, ally_environment_effects, None, None, "clean")
                            count += 1
                            if buff_obj.objectname in ["silence", "confusion", "frozen", "sleepy", "ridicule"]:
                                # 恢复MP并提升效果抵抗
                                now_role.mp += 15
                                if now_role.mp > now_role.max_mp:
                                    now_role.mp = now_role.max_mp
                                up_resistance_buff = getattr(store, "barrier")
                                item = (1, 0.4)
                                up_resistance_buff.calculate(now_role, None, item, skill.name, "get")
                                # 获得行动提前
                                if skill.level == 5:
                                    now_role.order += 200
                            if skill.level in [3, 4, 5]:
                                if count >= 2:
                                    break
                            else:
                                break
                    # 提升速度
                    up_buff = getattr(store, "flow")
                    if skill.level in [1, 2, 3]:
                        item = (1, 10)
                        up_buff.calculate(now_role, None, item, skill.name, "get")
                    elif skill.level in [4, 5]:
                        item = (1, 10)
                        up_buff.calculate(now_role, None, item, skill.name, "get")
                # 牺牲30%|30%|25%|20%|15%当前生命
                if skill.name == "视线诱导":
                    if not multi_buff_lock_effect:
                        temp_ratio_lists = [0.3, 0.3, 0.25, 0.2, 0.15]
                        user.hp = max(int(user.hp * (1.0 - temp_ratio_lists[skill.level - 1])), 1)
                # 随机驱散1|1|1|2|2个减益状态或控制效果，Lv3~5: 同时清除所有的元素附着
                elif skill.name == "碧之律":
                    debuffs = copy(now_role.debuff)
                    count = 0
                    for buff_name in debuffs:
                        buff_obj = getattr(store, buff_name)
                        if buff_obj.removeable:
                            buff_obj.calculate(now_role, ally_environment_effects, None, None, "clean")
                        
                        if skill.level in [4, 5]:
                            if count >= 2:
                                break
                        else:
                            break
                    if skill.level in [3, 4, 5]:
                        now_role.ebuff = {}
                # 解开潘多拉的魔咒，记录我方场上所有队友以及所选择的敌方目标当前生命比例，并降低敌方目标30点速度，持续1回合。若下回合“立花希”行动开始时，我方有角色所记录的生命比例小于敌方目标所记录的生命比例且未阵亡，则将低于记录数值的角色生命恢复至敌方记录比例
                elif skill.name == "魂之殇":
                    # 记录敌方目标当前生命比例
                    target_enemy = user.selected_target
                    target_hp_ratio = target_enemy.hp / target_enemy.battle_max_hp
                    temp_dict = local_config.skill_log_data.setdefault("魂之殇", {})
                    already_in = None
                    for (u, t) in temp_dict:
                        if u == user:
                            already_in = (u, t)
                            break
                    if already_in is not None:
                        temp_dict.pop(already_in)
                    temp_dict[(user, now_role)] = {
                        user: (target_hp_ratio, "user")
                    }
                    # 给对方标记“殇魂”debuff
                    buff_obj = getattr(store, "desoul_lock")
                    item = (99, target_hp_ratio)
                    buff_obj.calculate(now_role, None, item, skill.name, "get")
                    # 降低对方30点速度
                    buff_obj = getattr(store, "slow")
                    item = (1, 30)
                    buff_obj.calculate(now_role, None, item, skill.name, "get")
                    if skill.level == 1:
                        # 降低自身30点速度
                        buff_obj = getattr(store, "slow")
                        item = (1, 30)
                        buff_obj.calculate(user, None, item, skill.name, "get")
                # 激活强大的感官灵能控制对方思维，为自身与敌方目标附加1层无法驱散的“咒”效果进入“接触”状态，当自身受到伤害时，对共同持有“咒”的敌方单位造成50%的传导伤害（不会暴击；也不会触发装备4件套效果），持续2回合
                elif skill.name == "接触感应":
                    # 为自身与敌方目标附加1层无法驱散的“咒”效果进入“接触”状态
                    buff_obj1 = getattr(store, "curse")
                    if skill.level == 1:
                        item1 = (2, 0.5)
                    elif skill.level == 2:
                        item1 = (2, 0.6)
                    elif skill.level == 3:
                        item1 = (2, 0.7)
                    elif skill.level == 4:
                        item1 = (2, 0.8)
                    else:
                        item1 = (2, 1.0)
                    buff_obj1.calculate(user, None, item1, skill.name, "get")
                    buff_obj2 = getattr(store, "decurse")
                    if skill.level == 1:
                        item2 = (99, 0.5)
                    elif skill.level == 2:
                        item2 = (99, 0.6)
                    elif skill.level == 3:
                        item2 = (99, 0.7)
                    elif skill.level == 4:
                        item2 = (99, 0.8)
                    else:
                        item2 = (99, 1.0)
                    buff_obj2.calculate(now_role, None, item2, skill.name, "get")
                    # {"咒": {"lhx_role": (False, None, target), [target.objectname]: (False, None, source)}}
                    buff_roles = local_config.skill_log_data.setdefault("咒", {})
                    buff_roles[user] = (False, None, "user", now_role)
                    buff_roles[now_role] = (False, None, "target", user)
                # 开启持续1回合的星空结界，场上所有友方单位获得“星桥”，使得下一次受到的伤害降低35%
                elif skill.name == "星空梦影":
                    temp_dict = local_config.skill_log_data.setdefault("星空梦影", {})
                    temp_dict[now_role] = (False, user)
                # 消耗9层“鬼面”，开启附带9个禁断之面的“封印结界”笼罩对手
                elif skill.name == "虚无":
                    # 消耗9层“鬼面”
                    buff_obj = getattr(store, "ghost_mask")
                    buff_obj.calculate(user, ally_environment_effects, None, None, "clean")
                    # 鬼面加入
                    buff_roles = local_config.skill_log_data.setdefault("积重鬼怨", {})
                    if user in local_config.party:
                        buff_roles["ally"] = 9
                    elif user in local_config.enemy:
                        buff_roles["enemy"] = 9
                # 进入持续2回合的“空灵”状态
                elif skill.name == "幻镜化物":
                    buff_obj = getattr(store, "ethereal")
                    item = (2, None)
                    buff_obj.calculate(user, None, item, skill.name, "get")

                    # 立刻获得50%行动提前
                    user.order += 500

                    if skill.level in [3, 4, 5]:
                        # 期间自身进入“霸体”状态
                        buff_obj = getattr(store, "sp_domineering")
                        item = (99, None)
                        buff_obj.calculate(user, None, item, skill.name, "get")
                        if skill.level in [4, 5]:
                            # 提升80点元素精通
                            buff_obj = getattr(store, "master")
                            item = (2, 80)
                            buff_obj.calculate(user, None, item, skill.name, "get")
                            if skill.level == 5:
                                # 提升60点速度
                                buff_obj = getattr(store, "flow")
                                item = (2, 60)
                                buff_obj.calculate(user, None, item, skill.name, "get")
                    # 形态变化
                    user.is_phase2 = True
                    renpy.music.play("raged", channel="battle_music")
                    if "幻镜化物-pose" in local_config.skill_log_data:
                        local_config.skill_log_data["幻镜化物-pose"].append((user, user.pose))
                    else:
                        local_config.skill_log_data["幻镜化物-pose"] = [(user, user.pose)]

                    if user.pose == "sf":
                        user.pose = "sf_2"
                    else:
                        user.pose = "zf_2"
                # 获得“霸体”状态持续1回合，增益角色在行动结束后进入1回合不可驱散的“深度沉睡”状态
                elif skill.name == "催眠":
                    # 获得“霸体”状态
                    if "sp_domineering" not in now_role.buff:
                        buff_obj = getattr(store, "domineering")
                        item = (1, None)
                        buff_obj.calculate(now_role, None, item, skill.name, "get")
                    # 增益角色记录
                    temp_dict = local_config.skill_log_data.setdefault("催眠", {})
                    if now_role == user and not support:
                        temp_dict[now_role] = 2
                    else:
                        temp_dict[now_role] = 1
                # 跳过回合并击碎1个禁断之面
                elif skill.name == "怨恨祛除":
                    if "积重鬼怨" in local_config.skill_log_data:
                        buff_roles = local_config.skill_log_data["积重鬼怨"]
                        if now_role in local_config.party and "enemy" in buff_roles:
                            buff_roles["enemy"] -= 1
                            # 消除禁断之面
                            face_number = buff_roles["enemy"]
                            if face_number != 0:
                                renpy.hide("qcls_skill_ally-mask_%d" % face_number)
                            else:
                                renpy.hide("qcls_skill_ally-mask_top")
                                buff_roles.pop("enemy")
                            
                            # 解除封印结界
                            if face_number == 0:
                                if len(local_config.skill_log_data["积重鬼怨"]) == 0:
                                    local_config.skill_log_data.pop("积重鬼怨")
                                for role in local_config.party[:3]:
                                    role._special_calculate(enemy_environment_effects=ally_environment_effects, mode="release")
                        elif now_role in local_config.enemy and "ally" in buff_roles:
                            buff_roles["ally"] -= 1
                            # 消除禁断之面
                            face_number = buff_roles["ally"]
                            if face_number != 0:
                                renpy.hide("qcls_skill_enemy-mask_%d" % face_number)
                            else:
                                renpy.hide("qcls_skill_enemy-mask_top")
                                buff_roles.pop("ally")

                            # 解除封印结界
                            if face_number == 0:
                                if len(local_config.skill_log_data["积重鬼怨"]) == 0:
                                    local_config.skill_log_data.pop("积重鬼怨")
                                for role in local_config.enemy[:3]:
                                    role._special_calculate(enemy_environment_effects=ally_environment_effects, mode="release")
                # 共感
                elif skill.name == "共感":
                    # 为我方场上全体角色附加“心”，持续1回合
                    temp_dict = local_config.skill_log_data.setdefault("共感", {})
                    if now_role in local_config.party:
                        if "ally" not in temp_dict:
                            temp_dict["ally"] = set([now_role])
                        else:
                            temp_dict["ally"].add(now_role)
                    elif now_role in local_config.enemy:
                        if "enemy" not in temp_dict:
                            temp_dict["enemy"] = set([now_role])
                        else:
                            temp_dict["enemy"].add(now_role)

                if "混乱" in skill.effects or "眩晕" in skill.effects or "冻结" in skill.effects or "沉睡" in skill.effects or "嘲讽" in skill.effects:
                    control_effects = {name: value for name, value in skill.effects.items() if name in ["混乱", "眩晕", "冻结", "沉睡", "嘲讽"]}
                    
                    for name, (ratios, target, time) in control_effects.items():
                        if isinstance(ratios, float):
                            ratios = [ratios]
                        # 每段判定的基础概率
                        for ratio in ratios:
                            battle_user_effect_hitrate, battle_target_effect_resistance = now_role.battle_role_init_control(user, now_role, ally_environment_effects, enemy_environment_effects)

                            # 若敌方带有“减速”效果，则基础概率提升至15%
                            if skill.name == "灵能风暴" and "slow" in now_role.debuff:
                                ratio = 0.15

                            # 技能效果命中率 = 技能基础命中 x (1 + 面板效果命中)
                            battle_effect_hitrate_final = ratio * (1 + battle_user_effect_hitrate)
                            # 技能效果抵抗率 = 1 - 100% / (100% + 面板效果抵抗)
                            battle_effect_resistance_final = 1.0 - 1.0 / (1.0 + battle_target_effect_resistance)
                            
                            # 判定是否命中
                            if battle_effect_hitrate_final > renpy.random.random():
                                # 霸体免控
                                if "domineering" in now_role.buff or "sp_domineering" in now_role.buff:
                                    renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("霸体免控", style="effect_text", color="ff9"))
                                    # renpy.pause(0.5 * persistent.battlespeed)
                                    # renpy.hide("buff_effect", layer="screens")
                                # 判定是否被抵抗
                                elif battle_effect_resistance_final < renpy.random.random():
                                    # 反射判定
                                    hitted[numb] = True
                                    buff_roles = None
                                    buff_obj = None
                                    effect_target = now_role
                                    if "Reflexes" in effect_target.abilities and 0.08 > renpy.random.random():
                                        renpy.show("buff_effect", at_list=[show_state(effect_target.xposition)], layer="screens", what=Text("反射", style="effect_text", color="ff9"))
                                        # renpy.pause(0.5 * persistent.battlespeed)
                                        # renpy.hide("buff_effect", layer="screens")
                                        effect_target = user
                                        hitted[numb] = False
                                        buff_roles = local_config.skill_log_data.setdefault("Reflexes", {})

                                    if buff_roles is None or (buff_roles is not None and effect_target.objectname not in buff_roles):
                                        # 效果命中目标
                                        if name == "混乱":
                                            buff_obj = getattr(store, "confusion")
                                            item = (1, None)
                                            buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                            buff_text = "混乱"
                                        elif name == "眩晕":
                                            buff_obj = getattr(store, "dizziness")
                                            item = (1, None)
                                            buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                            buff_text = "眩晕"
                                        elif name == "冻结":
                                            # 对已处于“冰冻”状态下的角色有30%概率转换为“深度冰冻”
                                            if "frozen" in effect_target.debuff and skill.name == "灵能风暴" and skill.level == 5:
                                                buff_obj = getattr(store, "deep_frozen")
                                                item = (1, None)
                                                buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                                buff_text = "深度冰冻"
                                            else:
                                                buff_obj = getattr(store, "frozen")
                                                item = (1, 0.5)
                                                buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                                buff_text = "冻结"
                                        elif name == "沉睡":
                                            buff_obj = getattr(store, "sleepy")
                                            item = (1, None)
                                            buff_obj.calculate(effect_target, None, item, skill.name, "get")
                                            buff_text = "沉睡"
                                        elif name == "嘲讽" and "ridicule" not in effect_target.debuff:
                                            buff_obj = getattr(store, "ridicule")
                                            item = (1, None)
                                            buff_obj.calculate(effect_target, None, item, skill.name, "get", user=user)
                                            buff_text = "嘲讽"

                                        if buff_obj is not None and buff_roles is not None:
                                            buff_roles[effect_target.objectname] = buff_obj

                                    renpy.music.play("poisoned", channel="battle_music")
                                    renpy.show("buff_effect", at_list=[show_state(effect_target.xposition)], layer="screens", what=Text(buff_text, style="effect_text", color="ff9"))
                                    # renpy.pause(0.75 * persistent.battlespeed)
                                else:
                                    renpy.show("buff_effect_%s" % str(numb), at_list=[show_state(now_role.xposition)], layer="screens", what=Text("抵抗", style="effect_text", color="ff9"))
                                    # renpy.pause(0.5)

                if hitted[numb]:
                    # 表情更新
                    now_role.face_change(hit=False, hitted=True)
                    # 受到伤害角色抖动特效
                    if now_role in local_config.party:
                        renpy.show(now_role.objectname, at_list=[shake, hide_out], layer="fg")
                    else:
                        renpy.show(now_role.objectname, at_list=[smallshake])
                    # renpy.pause(0.75 * persistent.battlespeed)
                multi_buff_lock_effect = True
            renpy.pause(0.75 * persistent.battlespeed)
                
            for numb, now_role in enumerate(use_targets):
                ## 伤害结束后效果判定
                # 阵亡判定
                now_role.death_calculate(user, skill, ally_environment_effects, enemy_environment_effects, order_members)
            
                # 闪避（最终决战王牌魔导力才有闪避）
                # renpy.music.play("Dodge_sound", channel="battle_music")
                # if self in party:
                #     renpy.show(self.objectname, at_list=[sway_r, hide_out], layer="fg")
                # else:
                #     renpy.show(self.objectname, at_list=[sway_l])
                # renpy.pause(0.5 * persistent.battlespeed)

                # 避免能量条溢出边界
                now_role.hp = int(now_role.hp)
                now_role.mp = int(now_role.mp)

                if now_role.hp > now_role.battle_max_hp:
                    now_role.hp = now_role.battle_max_hp
                elif now_role.hp < 0:
                    now_role.hp = 0

                if now_role.mp > now_role.max_mp:
                    now_role.mp = now_role.max_mp
                elif now_role.mp < 0:
                    now_role.mp = 0

                # 表情恢复
                now_role.face_change()

                renpy.hide("elemental_%s" % str(numb), layer="buff_element")
                renpy.hide("special_%s" % str(numb), layer="screens")
                renpy.hide("buff_effect_%s" % str(numb), layer="screens")
                renpy.hide("critical_%s" % str(numb), layer="screens")
                renpy.hide("healing_%s" % str(numb), layer="healing")
                renpy.hide("damage_%s" % str(numb), layer="damage")

            renpy.hide("buff_effect", layer="screens")
            renpy.hide("hcritical", layer="screens")
            renpy.hide("healing", layer="healing")
            renpy.hide("status", layer="screens")
            renpy.hide("defence", layer="screens")
            renpy.hide("finish", layer="screens")

            return

        # 复活判定
        def reborn_calculate(self, ally_environment_effects):
            # 判定是否需要轮换上场
            def _all_alive(parties):
                for role in parties:
                    if role.hp < 1:
                        return role
                return None

            if self in local_config.party:
                change_role = _all_alive(local_config.party[:3])
                if change_role is not None:
                    self.member_change(change_role, ally_environment_effects=ally_environment_effects, in_battle=True, reborn=True, show_role=False)
                if self in local_config.party[:3]:
                    self.battle_role_come(ally_environment_effects)
            elif self in local_config.enemy:
                change_role = _all_alive(local_config.enemy[:3])
                if change_role is not None:
                    self.member_change(change_role, ally_environment_effects=ally_environment_effects, in_battle=True, reborn=True)
                    # 显示复活角色上场
                    renpy.show(self.objectname, at_list=[show_enemy(self.xposition)])
                if self in local_config.enemy[:3]:
                    self.battle_role_come(ally_environment_effects)

        # 角色出场判定
        def battle_role_come(self, enemy_environment_effects):
            ## 全局环境效果加入
            # 被动技能
            role_select_skills = self.skills if not self.is_phase2 else self.skills_v2
            passive_skills = [s for s in role_select_skills if s.category == "Passive"]
            if len(passive_skills) > 0:
                passive_skill = passive_skills[0]
                enemy_environment_effects.add((passive_skill.name, passive_skill.selectable))

            # 装备4件套
            enemy_environment_effects.add((self.equip4effect, self.equip4effect_availabel))

            self._special_calculate(enemy_environment_effects=enemy_environment_effects, mode="chain")
            # 微量化改造
            skill_lists = self.skills if not self.is_phase2 else self.skills_v2
            xfe_breakout_skill = getattr(store, "xfe_breakout")
            if xfe_breakout_skill in skill_lists:
                if self in local_config.party:
                    renpy.show(self.objectname, at_list=[show_player(self.xposition)], layer="fg")
                    renpy.pause(0.25 * persistent.battlespeed)
                    renpy.music.play("raged", channel="battle_music")
                    renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("驻场先机", style="effect_text", color="ff9"))
                    renpy.pause(0.75 * persistent.battlespeed)
                    renpy.hide("buff_effect", layer="screens")
                    renpy.hide(self.objectname, layer="fg")
                    renpy.show("snow_level1", layer="fg_f")

                    for role2 in local_config.enemy[:3]:
                        if role2.hp > 0:
                            role2.ebuff = {"ice": 1}
                elif self in local_config.enemy:
                    renpy.music.play("raged", channel="battle_music")
                    renpy.show("buff_effect", at_list=[show_state(self.xposition)], layer="screens", what=Text("驻场先机", style="effect_text", color="ff9"))
                    renpy.pause(0.75 * persistent.battlespeed)
                    renpy.hide("buff_effect", layer="screens")
                    renpy.show("snow_level1", layer="fg_f")

                    for role2 in local_config.party:
                        if role2.hp > 0:
                            role2.ebuff = {"ice": 1}

        # 角色离场判定
        def battle_role_go(self, user, skill, ally_environment_effects, enemy_environment_effects, reborn=False):
            if not reborn:
                ## 清除场上的全局效果
                # 被动技能
                role_select_skills = self.skills if not self.is_phase2 else self.skills_v2
                passive_skills = [s for s in role_select_skills if s.category == "Passive"]
                if len(passive_skills) > 0:
                    passive_skill = passive_skills[0]
                    if (passive_skill.name, True) in enemy_environment_effects:
                        enemy_environment_effects.remove((passive_skill.name, True))
                    elif (passive_skill.name, False) in enemy_environment_effects:
                        enemy_environment_effects.remove((passive_skill.name, False))

                # 装备4件套
                if (self.equip4effect, True) in enemy_environment_effects:
                    enemy_environment_effects.remove((self.equip4effect, True))
                elif (self.equip4effect, False) in enemy_environment_effects:
                    enemy_environment_effects.remove((self.equip4effect, False))

                # 雪特效
                if self.name == "希菲尔":
                    remove_snow = True
                    for role in local_config.party[:3] + local_config.enemy[:3]:
                        if role != self and role.name == "希菲尔" and role.hp > 0:
                            remove_snow = False
                            break
                    if remove_snow:
                        renpy.hide("snow_level1", layer="fg_f")

            # 殇魂消除
            if "魂之殇" in local_config.skill_log_data:
                buff_roles = local_config.skill_log_data["魂之殇"]
                fake_buff_roles = copy(buff_roles)
                for (u, t) in fake_buff_roles:
                    if self == u or self == t:
                        temp_buff_roles = buff_roles.pop((u, t))
                        # 清空“殇魂”debuff
                        buff_obj = getattr(store, "desoul_lock")
                        buff_obj.calculate(t, None, None, None, "clean")

                        for role, (dmg, dtype) in temp_buff_roles.items():
                            # 为角色清空“殇魂”buff
                            buff_obj = getattr(store, "soul_lock")
                            buff_obj.calculate(role, None, None, None, "clean")
                if len(local_config.skill_log_data["魂之殇"]) == 0:
                    local_config.skill_log_data.pop("魂之殇")
            # 缘消除
            if "love" in self.buff:
                buff_obj = getattr(store, "love")
                buff_obj.calculate(self, None, None, None, "clean")
            # 若为咒的目标则消除咒术
            if "咒" in local_config.skill_log_data:
                buff_roles = local_config.skill_log_data["咒"]
                if self in buff_roles:
                    for role, (flag, dmg, dtype, other) in buff_roles.items():
                        if dtype == "user":
                            buff_obj = getattr(store, "curse")
                            buff_obj.calculate(role, None, None, None, "clean")
                        elif dtype == "target":
                            buff_obj = getattr(store, "decurse")
                            buff_obj.calculate(role, None, None, None, "clean")
            # 消除自己庇护下成员的星桥状态
            if "星空梦影" in local_config.skill_log_data:
                buff_roles = local_config.skill_log_data["星空梦影"]
                # 清空user为self的所有buff
                for role, (flag, buff_user) in buff_roles.items():
                    if self == buff_user:
                        # buff解除
                        if "star_bridge" in role.buff:
                            buff_obj = getattr(store, "star_bridge")
                            buff_obj.calculate(role, None, None, None, "clean")
                        elif "star_bridge_done" in role.buff:
                            buff_obj = getattr(store, "star_bridge_done")
                            buff_obj.calculate(role, None, None, None, "clean")
            # 剑术精通：“青影瞬杀阵”击杀目标后水之濑凛自身增加30%|40%|50%|50%|50%行动条，（LV4~5: 并提升30%攻击持续1回合）
            if ("剑术精通", True) in ally_environment_effects and user.name == "水之濑凛" and skill is not None and skill.name == "青影瞬杀阵":
                if skill.level in [4, 5]:
                    # 提升30%攻击
                    buff_obj = getattr(store, "strong")
                    item = (2, 0.3)
                    buff_obj.calculate(user, None, item, "剑术精通", "get")
                temp_ratio_lists = [300, 400, 500, 500, 500]
                # 增加行动条
                user.order += temp_ratio_lists[skill.level - 1]
                renpy.music.play("raged", channel="battle_music")
                renpy.show("buff_effect", at_list=[show_state(user.xposition)], layer="screens", what=Text("行动提前", style="effect_text", color="ff9"))
            # 积重鬼怨消除
            if "积重鬼怨" in local_config.skill_log_data and self.name == "千川老师":
                buff_roles = local_config.skill_log_data["积重鬼怨"]
                if self in local_config.party and "ally" in buff_roles:
                    face_number = buff_roles["ally"]
                    
                    # 消除禁断之面
                    while face_number > 0:
                        face_number -= 1
                        if face_number != 0:
                            renpy.hide("qcls_skill_enemy-mask_%d" % face_number)
                        else:
                            renpy.hide("qcls_skill_enemy-mask_top")
                    buff_roles.pop("ally")
                    
                    if len(local_config.skill_log_data["积重鬼怨"]) == 0:
                        local_config.skill_log_data.pop("积重鬼怨")
                    for role in local_config.enemy[:3]:
                        role._special_calculate(enemy_environment_effects=ally_environment_effects, mode="release")
                        buff_obj = getattr(store, "ghost_mask")
                        if "ghost_mask" in role.buff or "ghost_mask" in role.debuff:
                            buff_obj.calculate(role, None, None, None, "clean")
                elif self in local_config.enemy and "enemy" in buff_roles:
                    face_number = buff_roles["enemy"]
                    
                    # 消除禁断之面
                    while face_number > 0:
                        face_number -= 1
                        if face_number != 0:
                            renpy.hide("qcls_skill_ally-mask_%d" % face_number)
                        else:
                            renpy.hide("qcls_skill_ally-mask_top")
                    buff_roles.pop("enemy")

                    if len(local_config.skill_log_data["积重鬼怨"]) == 0:
                        local_config.skill_log_data.pop("积重鬼怨")
                    for role in local_config.party[:3]:
                        role._special_calculate(enemy_environment_effects=ally_environment_effects, mode="release")
                        buff_obj = getattr(store, "ghost_mask")
                        if "ghost_mask" in role.buff or "ghost_mask" in role.debuff:
                            buff_obj.calculate(role, None, None, None, "clean")
            else:
                self._special_calculate(enemy_environment_effects=enemy_environment_effects, mode="release")
            renpy.pause(1.0 * persistent.battlespeed)
            
        # 阵亡判定
        def death_calculate(self, user, skill, ally_environment_effects, enemy_environment_effects, order_members):
            # 天佑buff
            if self.hp < 1 and self.soulraise == 0 and "god" in self.buff:
                if ("守护誓约", True) in enemy_environment_effects:
                    renpy.show("lst_passive_img", at_list=[Transform(anchor=(0.5, 0.5), zoom=2.0, xpos=self.xposition, ypos=0.4)], layer="screens")
                    renpy.pause(2.16)
                    renpy.hide("lst_passive_img", layer="screens")

                renpy.music.play("raged", channel="battle_music")
                renpy.show("defence", at_list=[show_ability(self.xposition)], layer="screens", what=Text("重生", style="ability_text"))
                renpy.pause(0.5 * persistent.battlespeed)
                self.soulraise = 1
                xpos = self.xposition
                time, ratio = self.buff["god"]

                # 离场判定（重生）
                self.battle_role_go(user, skill, ally_environment_effects, enemy_environment_effects, reborn=True)

                # 清算buff
                god_buff = getattr(store, "god")
                god_buff.calculate(self, None, None, None, "clean")

                self.full_reset(heal_hp=True, ally_environment_effects=enemy_environment_effects, turn_end=False, level_reset=False)
                self.hp = int(self.battle_max_hp * ratio)
                self.xposition = xpos
                self.face_change()

                # 入场判定
                self.battle_role_come(enemy_environment_effects)
                # 1、守护誓约被动判定
                if ("守护誓约", True) in enemy_environment_effects:
                    # “雷亚”在受到致命伤害时进入“架星之梦”形态，以100%生命重生并提升30%暴击率直至再次死亡。（一场战斗只会触发一次）
                    if self.name == "雷亚":
                        self.is_phase2 = True
                        # 空间跳跃重置
                        self.battle_speed -= 60
                        # 提升暴击率
                        self.battle_critical_rate += 0.3

            # 阵亡判定
            elif self.hp < 1:
                self.mp = 0
                self.hp = 0
                user.defeat += 1
                self.be_defeat += 1
                
                # 后台阵亡不算
                if self in local_config.party[:3] or self in local_config.enemy[:3]:
                    if self in local_config.party and self != local_config.shown_actor:
                        renpy.hide(local_config.shown_actor.objectname, layer="fg")
                        renpy.pause(0.5 * persistent.battlespeed)
                        renpy.show(self.objectname, at_list=[show_player(self.xposition)], layer="fg")
                    renpy.music.play("Knockdown_Hard", channel="battle_music")
                    renpy.show("finish", at_list=[show_finish(self.xposition)], layer="screens", what=Text("战斗不能", style="finish_text"))

                self.battle_role_go(user, skill, ally_environment_effects, enemy_environment_effects)

                xpos = self.xposition
                self.full_reset(heal_hp=False, ally_environment_effects=enemy_environment_effects, turn_end=False, level_reset=False)
                self.xposition = xpos

                if self in local_config.party:
                    renpy.transition(wipedown, layer="fg", always=True)
                    renpy.hide(self.objectname, layer="fg")

                    # 清除自身引发的嘲讽状态
                    for role in local_config.enemy:
                        if "ridicule" in role.debuff and role.selected_target == self:
                            buff_obj = getattr(store, "ridicule")
                            buff_obj.calculate(role, None, None, None, "clean")
                else:
                    renpy.transition(wipedown, layer="master", always=True)
                    renpy.hide(self.objectname, layer="master")

                    # 清除自身引发的嘲讽状态
                    for role in local_config.party:
                        if "ridicule" in role.debuff and role.selected_target == self:
                            buff_obj = getattr(store, "ridicule")
                            buff_obj.calculate(role, None, None, None, "clean")

                user.selected_target = None
                # 重新选择目标
                if self in local_config.party:
                    for role in local_config.party:
                        if role.hp > 0:
                            user.selected_target = role
                            break
                elif self in local_config.enemy:
                    for role in local_config.enemy:
                        if role.hp > 0:
                            user.selected_target = role
                            break
                
                renpy.hide("finish", layer="screens")
                    
                # 队员替补
                if self in local_config.party:
                    for role in local_config.party[3:]:
                        if role.hp >= 1:
                            local_config.party.remove(role)
                            local_config.party.remove(self)
                            local_config.party.insert(2, role)
                            local_config.party.append(self)
                            user.selected_target = role

                            role.battle_role_come(enemy_environment_effects)
                            order_members.update_members(go_role=self, come_role=role)
                            break
                elif self in local_config.enemy:
                    for i in xrange(len(local_config.enemy)):
                        if local_config.partytarget.hp >= 1:
                            break
                        local_config.partytarget = local_config.enemy[0+i]
                    for n, role in enumerate(local_config.enemy[3:]):
                        if role.hp >= 1:
                            local_config.enemy.remove(role)
                            if self == local_config.enemy[0]:
                                local_config.enemy.insert(0, role)
                                local_config.enemy[0].xposition = self.xposition
                                renpy.show(local_config.enemy[0].objectname, at_list=[show_enemy(local_config.enemy[0].xposition)])
                            elif self == local_config.enemy[1]:
                                local_config.enemy.insert(1, role)
                                local_config.enemy[1].xposition = self.xposition
                                renpy.show(local_config.enemy[1].objectname, at_list=[show_enemy(local_config.enemy[1].xposition)])
                            elif self == local_config.enemy[2]:
                                local_config.enemy.insert(2, role)
                                local_config.enemy[2].xposition = self.xposition
                                renpy.show(local_config.enemy[2].objectname, at_list=[show_enemy(local_config.enemy[2].xposition)])
                            local_config.enemy.remove(self)
                            local_config.enemy.append(self)
                            user.selected_target = role

                            role.battle_role_come(enemy_environment_effects)
                            order_members.update_members(go_role=self, come_role=role)
                            break
                return

        def _special_calculate(self, enemy_environment_effects, mode):
            if mode == "chain":
                # 积重鬼怨
                if "积重鬼怨" in local_config.skill_log_data:
                    buff_roles = local_config.skill_log_data["积重鬼怨"]

                    # 结界笼罩下
                    if (self in local_config.party and "enemy" in buff_roles) or (self in local_config.enemy and "ally" in buff_roles):
                        fake_qcls_role = None
                        if self in local_config.party:
                            for role in local_config.enemy:
                                if role.name == "千川老师":
                                    fake_qcls_role = role
                                    break
                        else:
                            for role in local_config.party:
                                if role.name == "千川老师":
                                    fake_qcls_role = role
                                    break
                        temp_selected_skills = fake_qcls_role.base_skills if not fake_qcls_role.is_phase2 else fake_qcls_role.base_skills_v2
                        temp_breakout_skill = [s for s in temp_selected_skills if s.category == "Break_out"][0]
                        
                        # {role: 减少的额外攻击力}
                        buff_roles = local_config.skill_log_data.setdefault("虚无", {})
                        # 期间降低10%|15%|20%|25%|30%暴击伤害、15%|20%|25%|30%|35%攻击力、20%|30%|40%|50%|60%效果命中  /  30%治疗效果、30%护盾强效
                        if temp_breakout_skill.level == 1:
                            self.battle_critical_damage -= 0.1
                            change_extend_attack = int(self.battle_attack * 0.15)
                            self.battle_extend_attack -= change_extend_attack
                            self.battle_effect_hitrate -= 0.2
                            buff_roles[self] = change_extend_attack
                        elif temp_breakout_skill.level == 2:
                            self.battle_critical_damage -= 0.15
                            change_extend_attack = int(self.battle_attack * 0.2)
                            self.battle_extend_attack -= change_extend_attack
                            self.battle_effect_hitrate -= 0.3
                            buff_roles[self] = change_extend_attack
                        elif temp_breakout_skill.level == 3:
                            self.battle_critical_damage -= 0.2
                            change_extend_attack = int(self.battle_attack * 0.25)
                            self.battle_extend_attack -= change_extend_attack
                            self.battle_effect_hitrate -= 0.4
                            buff_roles[self] = change_extend_attack
                        elif temp_breakout_skill.level == 4:
                            self.battle_critical_damage -= 0.25
                            change_extend_attack = int(self.battle_attack * 0.3)
                            self.battle_extend_attack -= change_extend_attack
                            self.battle_effect_hitrate -= 0.5
                            self.battle_healing_bonus -= 0.3
                            self.battle_shield_strength -= 0.3
                            buff_roles[self] = change_extend_attack
                        else:
                            self.battle_critical_damage -= 0.3
                            change_extend_attack = int(self.battle_attack * 0.35)
                            self.battle_extend_attack -= change_extend_attack
                            self.battle_effect_hitrate -= 0.6
                            self.battle_healing_bonus -= 0.3
                            self.battle_shield_strength -= 0.3
                            buff_roles[self] = change_extend_attack

                        # 使其所有的装备4件套效果、被动技能失效
                        buff_obj = getattr(store, "sp_lost")
                        item = (99, None)
                        buff_obj.calculate(self, enemy_environment_effects, item, "虚无", "get")

                        ## 被动技能将被替换为“怨恨祛除”
                        # 记录下被替换的技能
                        ori_passive_skill = None
                        for s in self.skills:
                            if s.category == "Passive":
                                ori_passive_skill = s
                                break
                        if ori_passive_skill is not None:
                            buff_roles = local_config.skill_log_data.setdefault("积重鬼怨-技能", {})
                            buff_roles[self] = [ori_passive_skill]

                        new_skills_lists = copy(self.skills)
                        new_passive_skill = getattr(store, "qcls_breakout_1")
                        new_skills_lists = [s if s.category != "Passive" else new_passive_skill for s in new_skills_lists]
                        self.skills = new_skills_lists

                        if len(self.skills_v2) != 0:
                            # 记录下被替换的技能
                            ori_passive_skill = None
                            for s in self.skills_v2:
                                if s.category == "Passive":
                                    ori_passive_skill = s
                                    break
                            if ori_passive_skill is not None:
                                buff_roles = local_config.skill_log_data.setdefault("积重鬼怨-技能", {})
                                buff_roles[self] += [ori_passive_skill]

                            new_skills_lists = copy(self.skills_v2)
                            new_passive_skill = getattr(store, "qcls_breakout_1")
                            new_skill_lists = [s if s.category != "Passive" else new_passive_skill for s in new_skills_lists]
                            self.skills_v2 = new_skill_lists
            elif mode == "release":
                # 积重鬼怨
                if "虚无" in local_config.skill_log_data:
                    fake_qcls_role = None
                    if self in local_config.party:
                        for role in local_config.enemy:
                            if role.name == "千川老师":
                                fake_qcls_role = role
                                break
                    else:
                        for role in local_config.party:
                            if role.name == "千川老师":
                                fake_qcls_role = role
                                break
                    temp_selected_skills = fake_qcls_role.base_skills if not fake_qcls_role.is_phase2 else fake_qcls_role.base_skills_v2
                    temp_breakout_skill = [s for s in temp_selected_skills if s.category == "Break_out"][0]

                    buff_roles = local_config.skill_log_data["虚无"]

                    # 结界笼罩下
                    if self in buff_roles:
                        change_extend_attack = local_config.skill_log_data["虚无"].pop(self)
                        if len(local_config.skill_log_data["虚无"]) == 0:
                            local_config.skill_log_data.pop("虚无")

                        self.battle_extend_attack += change_extend_attack
                        if temp_breakout_skill.level == 1:
                            self.battle_critical_damage += 0.1
                            self.battle_effect_hitrate += 0.2
                        elif temp_breakout_skill.level == 2:
                            self.battle_critical_damage += 0.15
                            self.battle_effect_hitrate += 0.3
                        elif temp_breakout_skill.level == 2:
                            self.battle_critical_damage += 0.2
                            self.battle_effect_hitrate += 0.4
                        elif temp_breakout_skill.level == 2:
                            self.battle_critical_damage += 0.25
                            self.battle_effect_hitrate += 0.5
                            self.battle_healing_bonus += 0.3
                            self.battle_shield_strength += 0.3
                        else:
                            self.battle_critical_damage += 0.3
                            self.battle_effect_hitrate += 0.6
                            self.battle_healing_bonus += 0.3
                            self.battle_shield_strength += 0.3

                        new_skills_lists = copy(self.skills)
                        new_passive_skill = getattr(store, "qcls_breakout_1")
                        ori_passive_skills = local_config.skill_log_data["积重鬼怨-技能"].pop(self)
                        new_skill_lists = [s if s != new_passive_skill else ori_passive_skills[0] for s in new_skills_lists]
                        self.skills = new_skill_lists

                        if len(self.skills_v2) != 0:
                            new_skills_lists = copy(self.skills_v2)
                            new_skill_lists = [s if s != new_passive_skill else ori_passive_skills[1] for s in new_skills_lists]
                            self.skills_v2 = new_skill_lists

                        buff_obj = getattr(store, "sp_lost")
                        buff_obj.calculate(self, enemy_environment_effects, None, None, "clean")

        # 批量移除队员
        def disband(self):
            for role in copy(local_config.party):
                if role.objectname not in local_config.masters:
                    local_config.party.remove(role)
                    local_config.backup.append(role)
            renpy.show_screen("alt_notify", message=_("队伍已清空。"))
            renpy.retain_after_load()

        # 队员添加
        def add(self):
            if len(local_config.party) < 6:
                local_config.backup.remove(self)
                local_config.party.append(self)
                renpy.hide_screen("message_screen")
                renpy.show_screen("alt_notify", message=_("队员添加成功。"))
                renpy.retain_after_load()
            else:
                renpy.hide_screen("message_screen")
                renpy.show_screen("alt_notify", message=_("队员已满。"))

        # 队员移除
        def pop(self):
            if self.objectname not in local_config.masters:
                local_config.party.remove(self)
                local_config.backup.append(self)
                renpy.hide_screen("message_screen")
                renpy.show_screen("alt_notify", message=_("成功将队员加入候补。"))
                renpy.retain_after_load()
            else:
                renpy.hide_screen("message_screen")
                renpy.show_screen("alt_notify", message=_("无法移除章节限定角色。"))

        # 队伍排序
        def sort(self, level=False):
            if level:
                local_config.backup.sort(key=attrgetter("level"), reverse=True)
            else:
                local_config.backup.sort(key=attrgetter("number"), reverse=False)
            renpy.show_screen("alt_notify", _("队伍整理完成。"))
            renpy.retain_after_load()


    # 人物立绘加载
    def render_actor(st, at, actor_name):
        actor = globals()[actor_name]
        for role in local_config.party + local_config.enemy:
            if role.objectname == actor_name:
                actor = role
                break

        absolute_name = actor_name
        for xi in range(1, 6):
            absolute_name = absolute_name.replace("_%s" % str(xi), "")
        
        actor_path = "9i/interface/battle/actors/{}/{}/".format(absolute_name.replace("_mirror", ""), actor.pose)
        layers = [actor_path + "default.png"]

        # if "shield" in actor.buff or "sp_shield" in actor.buff:
        #     layers.insert(1, Transform(zoomshining(actor_path + "default.png")))
        xfe_breakout_dict = {
            "虹之律": "xfe_breakout_red_img",
            "碧之律": "xfe_breakout_blue_img",
            "翠之律": "xfe_breakout_green_img",
            "霞之律": "xfe_breakout_purple_img",
            "绯之律": "xfe_breakout_pink_img",
        }

        if actor.face != None:
            if renpy.loadable(actor_path + "face/{}.png".format(actor.face)):
                layers.append(actor_path + "face/{}.png".format(actor.face))
            elif renpy.loadable(actor_path + "face/normal.png"):
                layers.append(actor_path + "face/normal.png")
        
        # 魂之殇
        if "soul_lock" in actor.buff:
            layers.append(Transform("lhx_combat_2_img", zoom=1.25, xalign=0.5, ypos=0.45))
        # 接触感应
        if "decurse" in actor.debuff:
            layers.append(Transform("lhx_breakout_1_img", zoom=1.5, xalign=0.5, ypos=0.45))
        if "curse" in actor.buff:
            layers.append(Transform("lhx_breakout_2_img", zoom=1.0, xalign=0.5, ypos=0.45))
        # 星桥
        if "star_bridge" in actor.buff or "star_bridge_done" in actor.buff:
            layers.append(Transform("star_brdige_img", zoom=1.5, xalign=0.5, ypos=0.2))
        # 空灵
        if "ethereal" in actor.buff:
            layers.append(Transform("ethereal_lighting_img", zoom=3.0, xalign=0.5, ypos=0.38))
        # 催眠
        if "催眠" in local_config.skill_log_data and actor in local_config.skill_log_data["催眠"]:
            layers.append(Transform("tyt_breakout_1_img", zoom=3.2, xalign=0.5, ypos=0.6))
            layers.append(Transform("tyt_breakout_2_img", zoom=2.2, xalign=0.5, ypos=0.45))
        # 护盾
        if "shield" in actor.buff or "sp_shield" in actor.buff:
            if "shield" in actor.buff:
                time, (_, element, _, _) = actor.buff["shield"]
            elif "sp_shield" in actor.buff:
                time, (_, element, _, _) = actor.buff["sp_shield"]
            layers.append(Transform("shield_%s_img" % element, zoom=3.5, xalign=0.5, ypos=0.25))
        if local_config.tutorial_step == "winter_loss_stage" and actor in local_config.party:
            layers.append(Transform("dream_breaker_img", zoom=1.5, xalign=0.5, ypos=0.32))
        # 微量化改造
        if "微量化改造" in local_config.skill_log_data and actor in local_config.skill_log_data["微量化改造"]:
            layers.append(Transform(xfe_breakout_dict[local_config.skill_log_data["微量化改造"][actor][0].name], zoom=1.5, xalign=0.5, ypos=0.45))

        return Fixed(*layers, fit_first=True, anchor=(0.5, 0.5)), None


    # 人物数据初始化
    def register_actor_image(filename, duplicate=True):
        f = renpy.file(filename)
        for l in f:
            l = l.decode("utf-8")
            a = l.rstrip().split(",")
            if not a[0] == "":
                for file in renpy.list_files():
                    if file.startswith('9i/interface/battle/actors/{}/'.format(a[0])) and file.endswith('/default.png'):
                        renpy.image(a[0], DynamicDisplayable(render_actor, a[0]))
                        if duplicate:
                            renpy.image(a[0] + "_mirror", DynamicDisplayable(render_actor, a[0] + "_mirror"))
                            if a[0] in ["migo_tiny_girl"]:
                                for xi in range(1, 6):
                                    renpy.image(a[0] + "_mirror_" + str(xi), DynamicDisplayable(render_actor, a[0] + "_mirror_" + str(xi)))
                        break
                else:
                    renpy.image(a[0], Placeholder("girl"))
        f.close()


    # 数据加载
    def read_actor(filename, duplicate=True):
        actor_list=[]

        f = renpy.file(filename)
        for n,l in enumerate(f):
            l = l.decode("utf-8")
            a = l.rstrip().split(",")
            if a[0] != "":
                setattr(store, a[0], Actor(a[0], a[1], 1, a[2], a[3], a[4], a[5], a[6], a[7].split("|"), a[8].split("|"), a[9].split("|"), a[10], a[11], a[12], a[13], 
                    a[14], a[15], a[16], a[17], a[18], a[19], a[20], a[21], a[22], a[23], a[24], a[25], a[26], a[27], a[28], a[29], a[30], a[31], a[32], a[33], a[34], 
                    a[35], a[36], a[37], a[38], number=n))
                actor_list.append(globals()[a[0]])

                if duplicate:
                    setattr(store, a[0] + "_mirror", Actor(a[0]+"_mirror", a[1], 1, a[2], a[3], a[4], a[5], a[6], a[7].split("|"), a[8].split("|"), a[9].split("|"), 
                        a[10], a[11], a[12], a[13], a[14], a[15], a[16], a[17], a[18], a[19], a[20], a[21], a[22], a[23], a[24], a[25], a[26], a[27], a[28], a[29], 
                        a[30], a[31], a[32], a[33], a[34], a[35], a[36], a[37], a[38], number=n))
                    if a[0] in ["migo_tiny_girl"]:
                        for xi in range(1, 6):
                            setattr(store, a[0] + "_mirror_" + str(xi), Actor(a[0]+"_mirror_"+str(xi), a[1], 1, a[2], a[3], a[4], a[5], a[6], a[7].split("|"), a[8].split("|"), a[9].split("|"), 
                                a[10], a[11], a[12], a[13], a[14], a[15], a[16], a[17], a[18], a[19], a[20], a[21], a[22], a[23], a[24], a[25], a[26], a[27], a[28], a[29], 
                                a[30], a[31], a[32], a[33], a[34], a[35], a[36], a[37], a[38], number=n))

                for aby in globals()[a[0]].abilities:
                    if aby not in ability_dict.keys():
                        raise NameError(a[0] + ':' + aby + ' is not ability')

        f.close()

        return actor_list
