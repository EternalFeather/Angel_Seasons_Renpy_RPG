# 攻击浮动范围 ratio1: 0.0551 ~ 0.0570; ratio2: 0.27~0.28
# 生命浮动范围 ratio1: 0.0456 ~ 0.0470; ratio2: 0.17~0.18
# 防御浮动范围 ratio1: 0.0227 ~ 0.0239; ratio2: 0.25~0.27

ori = 175
def grow_up(from_level, to_level, ori, ratio1=0.057, ratio2=0.28, exceed=True):
    for level in range(from_level + 1, to_level + 1):
        # 小于20级正常成长
        if level < 20:
            ori *= (1 + ratio1)
        # 否则，被5整除的等级先升星再成长
        elif level % 5 == 0:
            if level == to_level and not exceed:
                ori *= (1 + ratio1)
            else:
                ori *= (1 + ratio1)
                ori *= (1 + ratio2)
        # 否则正常成长
        else:
            ori *= (1 + ratio1)
            
    return ori

# 基础攻击力
grow_up(1, 40, ori, 0.0571, 0.28, False)
# 生命值
grow_up(1, 40, 907, 0.0456, 0.17, False)
# 防御力
grow_up(1, 40, 64, 0.0227, 0.25, False)

# 角色升级所需经验 = 2.5x^3+25x^2-12.5x+165 if x为奇数 else 2.5x^3+22.5x^2-10x+150
# 怪物经验值 = 100+10*(lv+1) if lv <= 20 else 300+20*(lv-20)
# 面板攻击力 = 基础攻击力 x (1 + 百分比攻击加成) + 固定攻击力
# 基础伤害 = 面板攻击力 x (300 / (300 + 防御力))
# 最终抗性 = 怪物抗性 - 抗性削减 if 怪物抗性 >= 抗性削减 else 0.5 x (怪物抗性 - 抗性削减)
# 元素精通加成 = -0.0002 x (元素精通) ^ 2 + 0.4527 x 元素精通 + 1.0058
# 承伤比例 = 角色等级 / 怪物等级
# 物理伤害 = 基础伤害 x 技能伤害倍率 x 额外伤害加成（buff、装备效果、技能效果）x 抗性削弱（加成）x 暴伤(暴击) x 物理伤害倍率 x 承伤比例
# 元素伤害 = 基础伤害 x 技能伤害倍率 x 额外伤害加成 x 抗性削弱（加成）x 暴伤 x 元素反应倍率 x 元素精通加成 x 承伤比例

