
label inside_attack_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的金币副本属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_attack_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的金币副本被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequattack}狂暴之力{/encyclopedia}的影响，结界中的敌人具备更强大的实力。"
    "随着时间的推移，敌方角色的属性将有所提升。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，我方角色所引发的{color=#9cf}蒸发{/color}和{color=#9cf}融化{/color}反应伤害倍率提升50%。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_attack_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的金币副本充斥着更加浓烈的扭曲结界。"
    "敌方阵容为「时空之境」的镜像配置。"
    "而受{encyclopedia=niequattack}狂暴之力{/encyclopedia}的影响，敌方角色将拥有更加强大的实力。"
    "随着时间的推移，敌方角色的属性将有所提升。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%。且我方角色所引发的{color=#9cf}蒸发{/color}和{color=#9cf}融化{/color}反应伤害倍率提升25%。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_protect_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的经验副本属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_protect_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的经验副本被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequprotect}猎杀之印{/encyclopedia}的影响，对方角色的攻击将会有50%概率强制锁定我受保护角色。"
    "当该角色阵亡时战斗判定为失败。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，且我方角色所引发的{color=#9cf}冻结{/color}反应基础概率提升20%。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_protect_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的经验副本充斥着更加浓烈的扭曲结界。"
    "敌方阵容为「时空之境」的镜像配置。"
    "而受{encyclopedia=niequprotect}猎杀之印{/encyclopedia}的影响，对方角色的攻击将会有100%概率强制锁定我方某位角色。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%。且我方角色所引发的{color=#9cf}冻结{/color}反应基础概率提升10%。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_speed_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的突破材料副本属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_speed_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的突破材料副本被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequspeed}迅捷之影{/encyclopedia}的影响，双方角色每次使用{color=#f00}凝神{/color}且未处于{color=#f00}封印结界{/color}笼罩下时，则为其他友方角色和自己附加一层“义”。"
    "当其中一方率先达到10层“义”时，下一个回合开始时全队所有角色获得100%攻击加成、50%暴击率加成、100%暴击伤害加成和50点速度提升（死亡时重置且重新叠加）。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，且我方角色所引发的{color=#9cf}超载{/color}有40%概率击退敌方80%行动条。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_speed_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的突破材料副本被扭曲的时空结界所笼罩。"
    "敌方阵容为「时空之境」的镜像配置。"
    "受{encyclopedia=niequspeed}迅捷之影{/encyclopedia}的影响，双方角色每次使用{color=#f00}凝神{/color}且未处于{color=#f00}封印结界{/color}笼罩下时，则为其他友方角色和自己附加一层“义”。"
    "当我方达到10层或敌方达到8层“义”时，下一个回合开始时全队所有角色获得100%攻击加成、50%暴击率加成、100%暴击伤害加成和50点速度提升（死亡时重置且重新叠加）。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%，且我方角色所引发的{color=#9cf}超载{/color}有40%概率击退敌方40%行动条。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_fire_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的装备副本-火属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_fire_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的装备副本-火被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequfire}阴燃之火{/encyclopedia}的影响，敌方角色的{color=#f30}火元素抗性{/color}大幅提升，且在每位角色回合结束时若该角色未附着任何元素，则为其附着3层{color=#f30}火元素{/color}。"
    "当我方角色身上的火元素附着达到5层时，在角色下一回合开始时清空元素附着并对其造成生命上限30%的间接伤害。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，我方所有角色获得40%{color=#99f}水元素伤害加成{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_fire_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的装备副本-火被扭曲的时空结界所笼罩。"
    "敌方阵容为「时空之境」的镜像配置。"
    "受{encyclopedia=niequfire}阴燃之火{/encyclopedia}的影响，敌方角色的{color=#f30}火元素抗性{/color}大幅提升，且在每位角色回合结束时若该角色未附着任何元素，则为其附着3层{color=#f30}火元素{/color}，当角色已附着火元素，则层数加一。"
    "当我方角色身上的火元素附着达到5层时，在角色下一回合开始时清空元素附着并对其造成生命上限30%的间接伤害。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%，我方所有角色获得20%{color=#99f}水元素伤害加成{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_light_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的装备副本-雷属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_light_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的装备副本-雷被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequlight}嗜能之雷{/encyclopedia}的影响，敌方角色的{color=#f0f}雷元素抗性{/color}大幅提升，且在每位角色回合结束时若该角色未附着任何元素，则为其附着3层{color=#f0f}雷元素{/color}。"
    "附带了雷元素的我方角色在回合开始时，将被削减5*雷元素层数的能量值。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，我方所有角色获得40%{color=#3ff}冰元素伤害加成{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_light_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的装备副本-雷被扭曲的时空结界所笼罩。"
    "敌方阵容为「时空之境」的镜像配置。"
    "受{encyclopedia=niequlight}嗜能之雷{/encyclopedia}的影响，敌方角色的{color=#f0f}雷元素抗性{/color}大幅提升，且在每位角色回合结束时若该角色未附着任何元素，则为其附着3层{color=#f0f}雷元素{/color}。"
    "附带了雷元素的我方角色在回合开始时，将被削减5*雷元素层数的能量值。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%，我方所有角色获得20%{color=#3ff}冰元素伤害加成{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_water_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的装备副本-水属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_water_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的装备副本-水被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequwater}迟滞之水{/encyclopedia}的影响，敌方角色的{color=#99f}水元素抗性{/color}大幅提升，且在每位角色回合结束时若该角色未附着任何元素，则为其附着3层{color=#99f}水元素{/color}。"
    "附着了水元素的我方角色在回合开始时受到5*水元素层数速度降低和10%*水元素层数效果抵抗衰减。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，我方所有角色获得40%{color=#f0f}雷元素伤害加成{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_water_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的装备副本-水被扭曲的时空结界所笼罩。"
    "敌方阵容为「时空之境」的镜像配置。"
    "受{encyclopedia=niequwater}迟滞之水{/encyclopedia}的影响，敌方角色的{color=#99f}水元素抗性{/color}大幅提升，且在每位角色回合结束时若该角色未附着任何元素，则为其附着3层{color=#99f}水元素{/color}。"
    "附着了水元素的我方角色在回合开始时受到5*水元素层数速度降低和10%*水元素层数效果抵抗衰减。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%，我方所有角色获得20%{color=#f0f}雷元素伤害加成{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_ice_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的装备副本-冰属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_ice_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的装备副本-冰被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequice}凝结之冰{/encyclopedia}的影响，敌方角色的{color=#3ff}冰元素抗性{/color}大幅提升，且在每位角色回合结束时若该角色未附着任何元素，则为其附着3层{color=#3ff}冰元素{/color}。"
    "附带了冰元素的我方角色行动开始时有5%*冰元素层数的固定概率被「冻结」。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，我方所有角色获得40%{color=#f30}火元素伤害加成{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_ice_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的装备副本-冰被扭曲的时空结界所笼罩。"
    "敌方阵容为「时空之境」的镜像配置。"
    "受{encyclopedia=niequice}凝结之冰{/encyclopedia}的影响，敌方角色的{color=#3ff}冰元素抗性{/color}大幅提升，且在每位角色回合结束时若该角色未附着任何元素，则为其附着3层{color=#3ff}冰元素{/color}。"
    "附带了冰元素的我方角色行动开始时有5%*冰元素层数的固定概率被「冻结」。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%，我方所有角色获得20%{color=#f30}火元素伤害加成{/color}。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_rock_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的装备副本-岩属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_rock_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的装备副本-岩被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequrock}坚毅之岩{/encyclopedia}的影响，敌方角色的{color=#9cf}物理抗性{/color}和{color=#ff0}岩元素抗性{/color}大幅提升。"
    "敌方每位角色行动结束时若未处于护盾庇护下，有15%固定概率为自己附加一层岩元素护盾，护盾量相当于其已损失生命值的8%，持续2回合。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，我方所有角色获得40%{color=#f30}火{/color}、{color=#99f}水{/color}、{color=#f0f}雷{/color}、{color=#3ff}冰{/color}、{color=#6f6}风{/color}元素伤害加成。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_rock_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的装备副本-岩被扭曲的时空结界所笼罩。"
    "敌方阵容为「时空之境」的镜像配置。"
    "受{encyclopedia=niequrock}坚毅之岩{/encyclopedia}的影响，敌方角色的{color=#9cf}物理抗性{/color}和{color=#ff0}岩元素抗性{/color}大幅提升。"
    "敌方每位角色行动结束时若未处于护盾庇护下，有15%固定概率为自己附加一层岩元素护盾，护盾量相当于其已损失生命值的8%，持续2回合。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%，我方所有角色获得20%{color=#f30}火{/color}、{color=#99f}水{/color}、{color=#f0f}雷{/color}、{color=#3ff}冰{/color}、{color=#6f6}风{/color}元素伤害加成。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_wind_battle_easy(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "简单难度的装备副本-风属于常规战斗。"
    "以{color=#f00}击败所有对手{/color}为胜利条件，相反{color=#f00}所有友方无法战斗{/color}则为失败条件。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_wind_battle_hard(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "一般难度下的装备副本-风被扭曲的时空结界所笼罩。"
    "受{encyclopedia=niequrock}济世之风{/encyclopedia}的影响，敌方角色的{color=#f30}火{/color}、{color=#99f}水{/color}、{color=#f0f}雷{/color}、{color=#3ff}冰{/color}、{color=#6f6}风{/color}元素抗性大幅提升。"
    "敌方每位角色行动结束时有15%固定概率为自己恢复一定的生命值，恢复量相当于其已损失生命值的8%。"
    "临行前弗兰前辈托付的镇物「遗念镜」能够抵御一部分污秽之力。"
    "在{color=#f00}遗念镜{/color}的祝福加持下，我方所有角色获得40%{color=#9cf}物理{/color}、{color=#ff0}岩{/color}元素伤害加成。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return

label inside_wind_battle_abyss(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    "困难难度下的装备副本-风被扭曲的时空结界所笼罩。"
    "敌方阵容为「时空之境」的镜像配置。"
    "受{encyclopedia=niequrock}济世之风{/encyclopedia}的影响，敌方角色的{color=#f30}火{/color}、{color=#99f}水{/color}、{color=#f0f}雷{/color}、{color=#3ff}冰{/color}、{color=#6f6}风{/color}元素抗性大幅提升。"
    "敌方每位角色行动结束时有15%固定概率为自己恢复一定的生命值，恢复量相当于其已损失生命值的8%。"
    "同时{color=#f00}遗念镜{/color}的祝福效果下降50%，我方所有角色获得20%{color=#9cf}物理{/color}、{color=#ff0}岩{/color}元素伤害加成。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return
