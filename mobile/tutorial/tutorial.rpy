
init:
    # tutorial
    image bg tutorial = "tutorial/bg-splash.jpg"
    
    image starter_tutorial_hpmp = "tutorial/starter_hpmp.png"
    image starter_tutorial_target_select = "tutorial/starter_target_select.png"
    image starter_tutorial_general_skill = "tutorial/starter_general_attack.png"
    image starter_tutorial_guard_skill = "tutorial/starter_guard.png"
    image starter_tutorial_passive_skill = "tutorial/starter_passive.png"
    image starter_tutorial_combat_skill = "tutorial/starter_combat.png"
    image starter_tutorial_breakout_skill = "tutorial/starter_breakout.png"
    image starter_tutorial_buff = "tutorial/starter_buff.png"
    image starter_tutorial_element_join = "tutorial/starter_element_join.png"
    image starter_tutorial_element_reaction = "tutorial/starter_element_reaction.png"
    image starter_tutorial_item_use = "tutorial/starter_item_use.png"
    image starter_tutorial_states = "tutorial/starter_states.png"
    image starter_tutorial_abilities = "tutorial/starter_abilities.png"
    image starter_tutorial_change_member = "tutorial/starter_change_member.png"


label tutorial_step1:
    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_hpmp onlayer tutorial
    centered ""
    hide starter_tutorial_hpmp

    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_target_select onlayer tutorial
    centered ""
    hide starter_tutorial_target_select

    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_general_skill onlayer tutorial
    centered ""
    hide starter_tutorial_general_skill

    return True


label tutorial_step2:
    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_guard_skill onlayer tutorial
    centered ""
    hide starter_tutorial_guard_skill

    return True


label tutorial_step3:
    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_passive_skill onlayer tutorial
    centered ""
    hide starter_tutorial_passive_skill

    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_combat_skill onlayer tutorial
    centered ""
    hide starter_tutorial_combat_skill

    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_breakout_skill onlayer tutorial
    centered ""
    hide starter_tutorial_breakout_skill

    return True


label tutorial_step4:
    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_buff onlayer tutorial
    centered ""
    hide starter_tutorial_buff

    return True


label tutorial_step5:
    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_element_join onlayer tutorial
    centered ""
    hide starter_tutorial_element_join

    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_element_reaction onlayer tutorial
    centered ""
    hide starter_tutorial_element_reaction

    return True

label tutorial_step6:
    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_item_use onlayer tutorial
    centered ""
    hide starter_tutorial_item_use

    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_states onlayer tutorial
    centered ""
    hide starter_tutorial_states

    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_abilities onlayer tutorial
    centered ""
    hide starter_tutorial_abilities

    $ renpy.transition(easeinright, layer="tutorial")
    show starter_tutorial_change_member onlayer tutorial
    centered ""
    hide starter_tutorial_change_member

    return True

label tutorial_step7:
    window mode thought
    me01 "战斗中有一定概率触发主角协战。"
    me01 "主角将会以助攻的形式不定期支援所选择角色，并继承其一定的属性加以行动，请合理利用这一机制创造优势。"
    me01 "随着角色羁绊的提升，协战触发的概率也会相应增加。"

    return True
