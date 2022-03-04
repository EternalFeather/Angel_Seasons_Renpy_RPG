label day01:
    bookmark
    $ renpy.show_screen("disable_inputs_for_replay", _layer="key")
    
    $ save_name = _("Day 01")
    $ _window_subtitle = " - 莉斯特（夏之死神）"
    play sound "sound/first_game_start.wav"
    scene black with Dissolve(8.0)

    pause 4.0 hard
    play music first_08 fadein 3.0 if_changed
    scene set only city evening yinghua
    show sepiagrain onlayer texture
    $ flcam.move(1800, 0, 400)
    $ flcam.move(-1800, 0, 400, duration=30.0, warper='ease_quad')
    with slowdissolve
    pause 0.5 hard
    nvl clear
    nvl_narrator "  与喜欢的人重逢真的会是件快乐的事吗？"
    nvl_narrator "  对于那时的我而言还无法完全理解所谓的“喜欢”。"
    nvl_narrator "  然而即便如此，想要在一起的感觉却是真实存在的。"
    nvl_narrator "  或许当时的我们也曾自以为是大人。"
    nvl_narrator "  才会轻易地把“永远”二字挂在嘴边。"
    nvl clear
    nvl_narrator "  在这数年的岁月里，唯有那份思念依然清晰地留在心底。"
    nvl_narrator "  如今的我再次回到这座儿时生活过的小镇，比起其他的事情最值得期待的便是与“她”的重逢。"
    nvl_narrator "  我希望这会是个让人感动的瞬间。"
    nvl clear
    nvl_narrator "  为此我也是做足了周全准备以确保万无一失。"
    nvl_narrator "  口袋里也是特地带上了眼药水。"
    nvl_narrator "  不过最难的环节还要数如何在被察觉到落泪之前将它涂上吧。"
    nvl_narrator "  但是如果、我是说如果，自己真的在她面前哭出来的话......"
    nvl_narrator "  那也一定是一件很幸福的事情吧。"

    pause 1.0 hard
    scene set only street evening yinghua
    show sepiagrain onlayer texture
    $ flcam.move(0, 0, 400)
    $ flcam.move(0, 0, 0, duration=15.0, warper='ease_quad')
    with slowdissolve
    pause 0.5 hard
    nvl clear
    nvl_narrator "  虽然有一段时间没见面了，加之不了解对方的联系方式，这些年我们可谓是毫无联系。"
    nvl_narrator "  但我想只要对方还生活在这座小镇上，我就一定能够一眼将她认出来。"
    nvl_narrator "  脑海里一边想象着“她”长大后的模样。"
    nvl_narrator "  一边满怀期待地向前走着，同时嘴里也在反复地组织着见面后的措辞。"
    nvl_narrator "  虽说脑中早已都是画面，但却无论如何也说不出当时的心情。"
    pause 1.0 hard
    scene black with dissolve
    stop music fadeout 5.0
    pause 1.0 hard

label day01.school_event01:
    play ambience1 zhiliao fadein 5.0
    $ flcam.move(0, 0, 400)
    scene set only school evening gate yinghua
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.5 hard
    show lingyin_xzf_b2 b2 b2_n1 onlayer screens at side_left('lingyin'), basicfade
    play voice "voice/青木铃音/0500010.ogg"
    stranger "今天不去社团活动可以吗？"
    show rxl_xzf_b1 b1 b1_a1 onlayer screens at side_right('rxl'), basicfade
    play voice "voice/日向怜/0100010.ogg"
    stranger "不是可不可以的问题，是根本就没有拿到屋顶的使用许可嘛，亏我还期待了这么久！"
    hide lingyin_xzf_b2
    hide rxl_xzf_b1
    "完全沉浸在回忆和幻想中的我，被这突如其来的抱怨声给拉回到了现实中来。"
    play music first_13 fadein 3.0 if_changed
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b1 b1 b1_s1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/青木铃音/0500020.ogg"
    stranger "学生会的那些家伙，把天协当成眼中钉。"
    hide lingyin_xzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_a1 onlayer m2 at walkin_l(0.3):
        xzoom -1
    pause 0.5 hard
    play voice "voice/日向怜/0100040.ogg"
    stranger "无论如何，距离七夕也只有短短几天时间了。如果到时侯还是没办法得到屋顶使用权的话......"
    hide rxl_xzf_b1
    $ flcam.move(4500, -300, 900, duration=0.5)
    show lingyin_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0500050.ogg"
    stranger "那就真是我们“天体观测者协会”，简称“天协”名誉扫地的时候了吧。"
    hide lingyin_xzf_b2
    $ flcam.move(-4500, -300, 900, duration=0.5)
    show rxl_xzf_b1 b1 b1_c1 onlayer m2:
        xpos 0.3
    show han onlayer m2:
        xalign 0.235 yalign 0.37
    play voice "voice/日向怜/0100050.ogg"
    stranger "牛郎和织女还在等着我去拯救呢！"
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0500060.ogg"
    stranger "天气预报说七夕那天也会是个难得的好天气呢。"
    hide rxl_xzf_b1
    hide han
    show rxl_xzf_b2 b2 b2_a2 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/0100060.ogg"
    stranger "一定不能放过这次见证鹊桥姻缘的机会！"
    show lingyin_xzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0500070.ogg"
    stranger "所谓的喜鹊，就是七夕时节用翅膀在银河上架起桥梁的鸟吧。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.3
        xzoom -1
    play voice "voice/日向怜/0100070.ogg"
    stranger "我已经受够了待在活动室里打扑克了！"
    show lingyin_xzf_b2 b2 b2_sp1
    play voice "voice/青木铃音/0500080.ogg"
    stranger "那下次玩花牌吧？"
    show rxl_xzf_b1 b1 b1_c1
    show han onlayer m2:
        xalign 0.28 yalign 0.37
    play voice "voice/日向怜/0100080.ogg"
    stranger "才不是在说这个啦！"
    hide lingyin_xzf_b2
    hide han
    hide rxl_xzf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    "回过神来的自己已经站在校门口。"
    "眼前的便是这座小镇上最有名的学府——樱华中学了。"
    "小时候的我曾与“她”约定过将来要一起在这里念书。然而事实却是因为我自己的一些原因中途离开了小镇。"
    "仔细想想当时的我还真是无能到令人愤怒的程度啊。"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0500130.ogg"
    stranger "......"
    "就在我思考之余，视线与其中的一位女生的目光交汇了。"
    hide lingyin_xzf_b2
    $ flcam.move(0, 0, 0, duration=1.5)
    "考虑到一直这样盯着人家看势必会被当成是可疑人物，于是我选择了默默离开。"
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/0100140.ogg"
    stranger "怎么了？突然沉默了。"
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0500140.ogg"
    stranger "那个人，好像正朝着观景台的方向走。"
    hide rxl_xzf_b2
    show rxl_xzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
        xzoom -1
    play voice "voice/日向怜/0100150.ogg"
    stranger "真的耶，好奇怪啊。"
    play voice "voice/日向怜/0100160.ogg"
    stranger "明明接下来就走不通了......"
    show lingyin_xzf_b2 b2 b2_s1
    play voice "voice/青木铃音/0500150.ogg"
    stranger "是来观光的吧，可能是走错路了之类的。"
    hide rxl_xzf_b1
    hide lingyin_xzf_b2
    $ flcam.move(0, 0, 0, duration=1.5)
    "走不通了？"
    "怎么可能？"
    "在我的印象中这分明就是前往观景台唯一的路。"
    "小时候与“她”一起玩耍过的，被我们称作“秘密基地”的地方。"
    "我是绝对不可能搞错的。"
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_xzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.3
        easein 0.05 yoffset scale(-20)
        easein 0.05 yoffset scale(+0)
    show tanhao at tanhao_x03 onlayer m2
    play voice "voice/日向怜/0100170.ogg"
    stranger "哇，已经是这个时间了。再不快点打工要来不及了！"
    pause 0.5 hard
    show lingyin_xzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0500170.ogg"
    stranger "嗯。明天学校见~"
    show rxl_xzf_b1 b1 b1_h1
    play voice "voice/日向怜/0100190.ogg"
    stranger "拜拜~"
    hide lingyin_xzf_b2 with dissolve
    hide rxl_xzf_b1 with dissolve
    pause 0.5 hard
    stop music fadeout 5.0
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 2.0 hard
    scene black with dissolve
    pause 2.0 hard
    stop ambience1 fadeout 2.0

label day01.starview_event01:
    scene set only sky evening yinghua
    with slowdissolve
    pause 2.0 hard
    "虽然对她们的话有些在意，但没有过多的思考我还是决定继续朝着原先既定的路线前进。"
    play ambience1 move_1 fadein 3.0
    play music first_18 fadein 3.0 if_changed
    pause 1.0 hard
    scene set only starview evening road 
    with up2down
    pause 2.0 hard
    scene set only starview evening guardrail 
    with right2left
    pause 2.0 hard
    stop ambience1 fadeout 3.0
    me01 "......不是吧。"
    $ flcam.move(-3400, -1200, 1100, duration=3.0, warper='ease_quad')
    pause 3.0 hard
    "前往观景台的路果然被铁丝网封住了。"
    "上面贴着的是禁止进入的告示，声明方写着“星天宫”。"
    "这样正式的查封在这里还是第一次见到。"
    $ flcam.move(0, 0, 0, duration=3.0, warper='ease_quad')
    pause 3.0 hard
    me01 "可是为什么......"
    "这里应该是免费向游客开放的才对。"
    "虽然不是什么著名的景点，但从这里俯瞰下去的{encyclopedia=yinghua}樱华镇{/encyclopedia}夜景也算得上是别具一格了。"
    "与“她”一起仰望过的星空也是......何等的令人怀念。"
    "不知从何时起，夏日的夜空对我而言已经成为了“她”的代名词。"
    "也正因如此我才会决定回来，才会决定要再与“她”一起欣赏这夏夜的美景。"
    "这些年来我始终都幻想着两人能够有一天，一起向着那被“她”比作“炸面包”的银河再次敞开双臂拥抱。"
    "而比起当时的我，此刻的这双手一定能更加靠近那些星辰吧。"
    me01 "可恶，怎么能这样就放弃！"
    "明明还期待着在拂晓之际，“她”会装作很生气的样子在这里等我。"
    "一边吐槽着“怎么这么久才来”之类的话一边拍打着我的胸口宣泄不满。"
    "不过话说回来，现在就连“她”是不是还记得我都无法断言。"
    "但即使如此，心里却还总是有种莫名的自信，相信对方一定没有把我忘记。"
    "毕竟我们曾是那么地形影不离，那么地......"
    pause 1.0 hard
    stop music fadeout 5.0
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 5.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_memory pieceone yinghua
    with dissolve
    play music first_27 fadein 3.0 if_changed
    pause 0.5 hard
    play voice "voice/翔子/0600450.ogg"
    stranger "凉君你要搬家了吗？"
    me01 "嗯。"
    play voice "voice/翔子/0600460.ogg"
    stranger "要离开这座小镇了吗？"
    me01 "嗯。"
    play voice "voice/翔子/0600470.ogg"
    stranger "为什么！"
    me01 "因为父亲的关系，他马上就要跳槽了。"
    play voice "voice/翔子/0600480.ogg"
    stranger "跳槽？"
    me01 "就是换个地方工作的意思。"
    play voice "voice/翔子/0600490.ogg"
    stranger "要去哪里工作呢？"
    me01 "似乎是要去城里的样子。"
    play voice "voice/翔子/0600500.ogg"
    stranger "那地方很远吗？"
    me01 "或许吧。"
    play voice "voice/翔子/0600510.ogg"
    stranger "有多远？"
    me01 "这个我也不知道。"
    "现在想来，这距离大概就像是无论怎么伸手都无法触及的星星一般遥远。"
    play voice "voice/翔子/0600520.ogg"
    stranger "我们......要分开了吗？"
    me01 "......"
    $ flcam.move(800, -1100, 400, duration=1.0, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0600530.ogg"
    stranger "这种事我才不允许！"
    me01 "就算你这么说......"
    play voice "voice/翔子/0600540.ogg"
    stranger "要跳槽的明明是家长，为什么却连凉君你也必须得离开呢！"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    me01 "没办法啊......我还是小孩子嘛。"
    play voice "voice/翔子/0600550.ogg"
    stranger "如果觉得自己是小孩子就什么都会被原谅的话就大错特错了！"
    me01 "这句话用在这里好像怪怪的。"
    play voice "voice/翔子/0600560.ogg"
    stranger "凉君你就什么想法都没有吗！"
    me01 "我当然也不想离开啊。"
    play voice "voice/翔子/0600570.ogg"
    stranger "那样的话，凉君你一个人留下来吧。"
    me01 "行不通的啦，而且我现在住的地方也要解约了。"
    play voice "voice/翔子/0600580.ogg"
    stranger "解约？"
    me01 "就是马上就要没有地方住了的意思。"
    play voice "voice/翔子/0600590.ogg"
    stranger "所以凉君也要不见了吗？"
    me01 "嗯。"
    $ flcam.move(800, -1100, 400, duration=1.0, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0600600.ogg"
    stranger "这种事我才不允许！"
    me01 "所以说啊......"
    play voice "voice/翔子/0600610.ogg"
    stranger "凉君你住在这里就好了嘛~"
    play voice "voice/翔子/0600620.ogg"
    stranger "如果没有地方住的话，就住在这座观景台就好了。这样一来我们就能一整天都开开心心地玩耍了。"
    me01 "行、行不通的啦。"
    play voice "voice/翔子/0600630.ogg"
    stranger "不试试看就放弃的话可不行的啦！"
    me01 "可是这里也没有东西吃。"
    play voice "voice/翔子/0600640.ogg"
    stranger "你是男孩子不忍耐一下是不行的！"
    me01 "石头可不能当饭吃的哟。"
    play voice "voice/翔子/0600650.ogg"
    stranger "那边的蘑菇看起来就挺好吃的~"
    me01 "吃下去一定会大笑不止的。"
    play voice "voice/翔子/0600660.ogg"
    stranger "那样的话一整天都能快快乐乐的了~"
    me01 "这个代价对我来说还是太沉重了。"
    play voice "voice/翔子/0600670.ogg"
    stranger "凉君怨言太多了。"
    me01 "没办法啊，我也只是个普通的小孩子而已。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0600680.ogg"
    stranger "凉君，你不伤心吗......"
    play voice "voice/翔子/0600690.ogg"
    stranger "明明可能再也不能见面了。"
    play voice "voice/翔子/0600700.ogg"
    stranger "明明我们......就要永别了。"
    pause 2.0 hard
    scene set only sky night yinghua
    with dissolve
    pause 2.0 hard
    "还是第一次看到她那么消沉。"
    "在我的印象中她一直是开朗、天真、充满笑容的女孩。"
    "也许是因为真的很难过的缘故吧。"
    pause 2.0 hard
    scene set only xz_memory pieceone yinghua
    with dissolve
    me01 "我一定会回来的！"
    $ flcam.move(800, -1100, 400, duration=1.0, warper='ease_quad')
    pause 1.0 hard
    me01 "这绝对不是什么永别。"
    me01 "会回来的。"
    me01 "我一定，会再一次回到这里。"
    me01 "一定会再一次，回到“翔子”你身边的！"
    play voice "voice/翔子/0600710.ogg"
    xz "......真的吗？"
    me01 "虽然现在还没有办法保证，但兑现的概率应该也有消费税那样的程度。"
    $ flcam.move(1100, -1400, 500, duration=0.5, warper='ease_quad')
    with vpunch
    play voice "voice/翔子/0600720.ogg"
    xz "{size=72}呜哇————！{/size}"
    "大哭。"
    $ flcam.move(800, -1100, 400, duration=1.0, warper='ease_quad')
    pause 1.0 hard
    me01 "没、没事的，几年后的消费税一定会变成100%的。"
    play voice "voice/翔子/0600730.ogg"
    xz "那我就祈祷消费税能够快点升高吧。"
    "她将来一定能够成为一名伟大的政治家吧。"
    play voice "voice/翔子/0600740.ogg"
    xz "还有，消费税是什么？"
    me01 "......"
    play voice "voice/翔子/0600750.ogg"
    xz "我们，还能再见面吗？"
    me01 "嗯。"
    play voice "voice/翔子/0600760.ogg"
    xz "绝对，绝——对，能够再见面吗？"
    me01 "嗯。"
    play voice "voice/翔子/0600770.ogg"
    xz "能向那颗星星发誓吗？"
    play voice "voice/翔子/0600780.ogg"
    xz "向着牛郎星和织女星发誓吗？"
    me01 "可是牛郎和织女每年也只有在七夕的时候才能见面吧？"
    $ flcam.move(1100, -1400, 500, duration=0.5, warper='ease_quad')
    with vpunch
    play voice "voice/翔子/0600790.ogg"
    xz "{size=72}呜哇————！{/size}"
    "大哭。"
    $ flcam.move(800, -1100, 400, duration=1.0, warper='ease_quad')
    pause 1.0 hard
    me01 "没、没关系的。毕竟他们最后还是在一起了嘛。"
    play voice "voice/翔子/0600800.ogg"
    xz "......真的吗？"
    me01 "嗯。"
    play voice "voice/翔子/0600810.ogg"
    xz "真的是真的？"
    me01 "真的是真的。"
    play voice "voice/翔子/0600820.ogg"
    xz "那我们约好了~"
    play voice "voice/翔子/0600830.ogg"
    xz "我们一定要再次相见。"
    play voice "voice/翔子/0600840.ogg"
    xz "一定要在这座观景台再次相见。"
    play voice "voice/翔子/0600850.ogg"
    xz "就像牛郎和织女那样，即使暂时分开了到最后也一定要再次相遇！"
    "当时的我只是默默地点了点头。"
    "毕竟她是笑着提出这个约定的。"
    "那样带着笑容的“她”我最喜欢了。"
    play voice "voice/翔子/0600870.ogg"
    xz "然后结婚，对我唯命是从！"
    me01 "这点还是饶了我吧......"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with dissolve
    pause 1.0 hard
    "是啊，我们一定会再相遇的。"
    "因为那时候就已经约好了的。"
    me01 "啊......"
    play sound grass
    pause 1.0 hard
    "回过神来的我被护栏边的灌木丛划伤了手。"
    "不知不觉就已经闯了进来，也许是因为不甘心就这么放弃了。"
    "周围没有路灯，在黑暗中方向感也变得有些混乱。"
    "我一边拨开身旁的杂草，一边朝着观景台的方向走去。"
    play ambience1 move_1 fadein 3.0
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.75 alpha 1
    pause 4.0 hard
    "在搬家前夜，我们最后一次在这里见面的场景。"
    "此刻仿佛又浮现在了眼前。"
    "当时的我们在这里许下了“一定会再次相见”的约定。"
    "在这片星空下，她笑了。"
    "笑着哭了。"
    "那是充满着矛盾却又让人沉醉的表情。"
    "也许当时我也哭了。"
    "直到现在我才真正明白其中的含义。"
    "原来我一直......都喜欢着“她”。"
    stop music fadeout 5.0
    stop ambience1
    "所以才会对重逢那么地执着吧。"
    pause 3.0 hard
    show sepiagrain onlayer texture
    nvl clear
    play voice "voice/天使雷亚/0000010.ogg"
    pcenter "  欢迎回来，凉君————"
    pause 2.0 hard

label day01.lst_event01:
    play music first_28 fadein 3.0 if_changed
    scene set only lisite_cg normal
    with in2out_v2_slow
    pause 3.0 hard
    "“她”在等我。"
    "就和当时约定好的一样。"
    play voice "voice/天使雷亚/0000020.ogg"
    stranger "稍微，等得有些累了。"
    "夏日的星辰勾勒出异彩斑斓的夜空。"
    "在这样的星空下。"
    "我们又见面了。"
    "虽然时隔数载之后的初次见面让我有些不知所措。"
    "但从相遇的那一刻起这一系列的机缘巧合让我不得不有理由相信。"
    "眼前的她就是我要找的人。"
    "我看了一眼她身上的服饰，款式相当的奇特。"
    "手中更是握着一把意义不明的巨型镰刀。"
    "还没等我开口询问，女孩先一步说道。"
    pause 0.1 hard
    scene set only lisite_cg happy
    with dissolve
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0000030.ogg"
    stranger "好久不见，凉君。"
    "就连声音也与记忆中的别无二致。"
    play voice "voice/天使雷亚/0000040.ogg"
    stranger "谢谢你遵守了约定。"
    "惊讶之余，我偷偷撰在手里的眼药水也顺势滑落到了地上。"
    stop music fadeout 2.0
    play voice "voice/天使雷亚/0000050.ogg"
    stranger "谢谢你还能记得我。"
    pause 1.0 hard
    show white onlayer texture 
    with dissolve
    pause 1.5 hard
    nvl clear
    play voice "voice/天使雷亚/0000060.ogg"
    pcenter "  这样一来，我也终于能履行我的使命了——"
    pause 1.0 hard
    $ mouse_visible = False
    $ suppress_overlay = True
    $ _skipping = renpy.seen_audio("video/first_op.mp4")
    $ config.skipping = None
    scene black
    with slowerdissolve
    pause 3.0 hard
    show movie onlayer master
    play movie "video/first_op.mp4" noloop
    $ renpy.music.play("video/first_op.mp3", synchro_start='movie', loop=False)
    pause 115.0 hard
    $ _skipping = True
    $ mouse_visible = True
    $ suppress_overlay = False
    stop movie
    hide movie
    stop music fadeout 1.0
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg normal
    with slowdissolve
    play music first_18 fadein 3.0 if_changed
    pause 0.5 hard
    "就像是直接把我记忆中的画面抽离出来一般，眼前的女孩无论是容貌还是言行都和我印象中的“她”大相径庭。"
    "唯一让我觉得违和的就是她的穿着和手里的那把镰刀。"
    me01 "你是......"
    me01 "“她”吗？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0000070.ogg"
    stranger "“她”？"
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0000080.ogg"
    stranger "“她”是谁？"
    me01 "这个......"
    play voice "voice/天使雷亚/0000090.ogg"
    stranger "你是在问我的名字吗？"
    me01 "啊......那个，是这样的。"
    "竟然在气势上被一位怎么看都比我年幼的女孩给镇住了，此刻的我只能僵硬地点了点头。"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0000100.ogg"
    stranger "我的名字是“雷亚”。"
    play voice "voice/天使雷亚/0000110.ogg"
    lst "这样可以了吗？"
    "没想到这么轻易地就问到了女孩的名字。"
    "而且听名字也完全不像是本地人。"
    "可为什么她总能给我一种熟悉的感觉，而且又为什么会独自来到这座本该是谢绝游客进入的观景台呢？"
    "或者说，这些都已经无所谓了。"
    "眼前的女孩不是“翔子”。"
    "不是与我约定之人。"
    "可为什么从见面开始她却总能勾起我的回忆呢？"
    "她所说的“使命”指的又是什么？"
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0000120.ogg"
    lst "接下来轮到我了。"
    play voice "voice/天使雷亚/0000130.ogg"
    lst "你是叫神野凉吧？"
    me01 "你认识我？"
    play voice "voice/天使雷亚/0000140.ogg"
    lst "果然。"
    me01 "我能问个问题吗？"
    play voice "voice/天使雷亚/0000150.ogg"
    lst "随意。"
    me01 "为什么你会知道{rb}我{/rb}{rt}ore{/rt}的名字呢？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0000160.ogg"
    lst "凉君已经开始自称{rb}我{/rb}{rt}ore{/rt}了吗？"
    "虽说只是一个在称呼上微不足道的改变。"
    "但借此我也更加确信，眼前的女孩一定与我的过去有关。"
    "她一定也认识那个还管自己叫{rb}我{/rb}{rt}boku{/rt}的神野凉。"
    me01 "我们果然是认识的吗？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0000170.ogg"
    lst "嗯。"
    me01 "从什么时候开始的？"
    play voice "voice/天使雷亚/0000180.ogg"
    lst "很久以前就认识了，很久以前。"
    me01 "你一直在这里等我吗？"
    play voice "voice/天使雷亚/0000200.ogg"
    lst "嗯。"
    me01 "为什么？"
    play voice "voice/天使雷亚/0000210.ogg"
    lst "因为约好了。"
    me01 "所以你果然是......"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0000220.ogg"
    lst "果然是，什么？"
    me01 "你说等我......是从什么时候开始的？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0000230.ogg"
    lst "都说了很久以前，不是说过了吗？"
    me01 "几年前的事？"
    play voice "voice/天使雷亚/0000240.ogg"
    lst "这种事早忘了。"
    me01 "如果是很久以前的话，那当时的你多大？"
    play voice "voice/天使雷亚/0000250.ogg"
    lst "我可没有年龄这种东西。"
    me01 "等、等一下。"
    me01 "没有年龄......是什么意思？"
    play voice "voice/天使雷亚/0000270.ogg"
    lst "就是字面上的意思。"
    play voice "voice/天使雷亚/0000260.ogg"
    lst "就是说我之前见过你并不代表那时的我就是比现在的我要小，明白了吗？"
    me01 "能说得明白点吗？"
    play voice "voice/天使雷亚/0000280.ogg"
    lst "我觉得没有更明白的说法了。"
    me01 "就比如你是死神所以年龄才不会增长之类的。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0000290.ogg"
    lst "死神......"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0000300.ogg"
    lst "如果你能接受的话，就当是这样好了。"
    "总感觉有些敷衍啊。"
    me01 "也就是说因为你是死神，所以上一次见面的时候也是一样的年纪吗？"
    pause 0.1 hard
    scene set only lisite_cg happy
    with dissolve
    play voice "voice/天使雷亚/0000310.ogg"
    lst "就是这样的吧。"
    me01 "哈哈哈，再怎么说“死神”这个设定也太奇怪了吧。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0000320.ogg"
    lst "不是你自己说的吗。"
    me01 "你说的死神就是那个“死神”吗？"
    play voice "voice/天使雷亚/0000330.ogg"
    lst "虽然不知道你说的是哪个“死神”，不过像我这样的死神就只有我一个。"
    "有种在问禅的感觉。"
    me01 "你这身装扮是Cosplay？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0000340.ogg"
    lst "......Cosplay？"
    me01 "不是吗？"
    pause 0.1 hard
    scene set only lisite_cg normal
    with dissolve
    play voice "voice/天使雷亚/0000350.ogg"
    lst "完全不明白你在说些什么。"
    me01 "那把镰刀是你自己做的？"
    play voice "voice/天使雷亚/0000360.ogg"
    lst "虽说一开始就在我这里了，但我想一定是别的谁做的吧。"
    me01 "不会是真家伙吧......"
    play voice "voice/天使雷亚/0000370.ogg"
    lst "虽然不知道对你来说什么才叫真的，但对我来说是独一无二的真货。"
    me01 "也就是说......能斩断物体？"
    play voice "voice/天使雷亚/0000380.ogg"
    lst "能啊。"
    "咽口水。"
    play voice "voice/天使雷亚/0000390.ogg"
    lst "要试试看吗？"
    me01 "等等等等，你不会是想拿我当试验品吧？！"
    play voice "voice/天使雷亚/0000400.ogg"
    lst "不是你自己想让我砍的吗？"
    me01 "我要是因此丧命的话你不就真成死神了吗？"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0000410.ogg"
    lst "都说了我就是死神，明明你自己也承认了的。"
    "生气了。"
    me01 "总之先假设雷亚酱是死神好了~"
    play voice "voice/天使雷亚/0000420.ogg"
    lst "居然加了“酱”。"
    "越来越生气了。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0000430.ogg"
    lst "明明我才是大姐姐的说......"
    me01 "可是你怎么看都没有我年长吧。"
    pause 0.1 hard
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0000440.ogg"
    lst "为什么？"
    me01 "因为你也说了自己没有年龄吧？"
    play voice "voice/天使雷亚/0000450.ogg"
    lst "死神才没有什么年龄。"
    me01 "这么说好了，你现在在哪里上学？"
    play voice "voice/天使雷亚/0000460.ogg"
    lst "死神才不会去上学。"
    me01 "爸爸和妈妈呢？"
    play voice "voice/天使雷亚/0000470.ogg"
    lst "死神才没有爸爸和妈妈。"
    "这完全没办法交流啊。"
    me01 "那我再退一步，现在就当你刚刚说的那些都是真的好了。"
    play voice "voice/天使雷亚/0000480.ogg"
    lst "明明就是真的。"
    me01 "所以你来这里做什么？"
    pause 0.1 hard
    scene set only lisite_cg happy
    with dissolve
    play voice "voice/天使雷亚/0000490.ogg"
    lst "我没说过吗。"
    "褪去了刚刚严肃的表情，她的嘴角微微上扬。"
    "露出了不符合她气质的、意味深长的笑容。"
    play voice "voice/天使雷亚/0000500.ogg"
    lst "我一直......在等你啊。"
    play voice "voice/天使雷亚/0000510.ogg"
    lst "为了完成我们的约定。"
    play voice "voice/天使雷亚/0000520.ogg"
    lst "不仅如此。"
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/天使雷亚/0000530.ogg"
    lst "也为了完成“割去你噩梦”的约定。"
    stop music fadeout 5.0
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with slowdissolve
    pause 0.5 hard
    play voice "voice/天使雷亚/0000540.ogg"
    lst "因为我是割去人们噩梦的死神——"
    pause 2.0 hard
    scene black with slowerdissolve
    $ suppress_overlay = True
    jump day02
