
label inside_battle4(enemy_list):
    $ preferences.afm_enable = False
    $ config.skipping = None
    pause 0.5 hard
    "强大的灵纹之力正在撕裂友加的意识，必须尽快击碎灵能屏障救出友加。"
    "对友加身旁的灵能屏障进行攻击，造成的伤害将会转化为等量的「治疗效果」作用在友加身上。"
    "当友加的生命值完全恢复时战斗胜利。"
    "每次友加行动后若友加未处于{color=#f00}无法行动{/color}状态，则灵能屏障都会对其造成间接伤害，并随着回合数的增加伤害将会越来越高。"
    "不稳定的气流随时都会引发{color=#f00}灵能风暴{/color}干扰我方行动。"
    "利用「雷」与「冰」发生的{color=#99f}超导{/color}反应降低屏障的物理抗性，配合「铃音」的「天宫罗阵」可以高效击破目标。"
    "{color=#f00}未拥有{/color}「铃音」的玩家也可以适当利用「控制」效果限制屏障对友加的伤害。"
    "祝您武运昌盛~"
    play music battle1 fadein 3.0 if_changed
    return


label day207:
    bookmark
    $ save_name = _("Day 207")
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play sound "sound/system/second_menu.wav"
    scene black with Dissolve(8.0)

    pause 4.0 hard
    $ renpy.block_rollback()
    $ _rollback = True

    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    pause 2.0 hard
    show backend_date206 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    scene set only sky day xuejian2
    play music second_114 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    $ suppress_overlay = False
    "从今天开始学校进入了期末考试周。"
    "虽然最近发生的事情总归让人有些意想不到。"
    "但眼下避免挂科才是当务之急。"
    pause 1.0 hard
    scene set only school day room xuejian
    with slowdissolve
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('chapter three'), _("听不见你的声音"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    show yj_tcf_b2 b2 b2_s3 onlayer m1:
        xpos 0.5
    play voice "voice/植澄友加/020101030.ogg"
    yj "凉君、翔子你们听我说呀~"
    hide yj_tcf_b2 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_ga1 onlayer m1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/020101040.ogg"
    yj "今天社团竟然没有晨练。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b1 b1 b1_ga1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/翔子/010102700.ogg"
    xz "因为考试临近的缘故吧。"
    $ flcam.move(2250, -350, 900, duration=1.5)
    pause 0.5 hard
    hide yj_tcf_b3 with None
    pause 0.1 hard
    show yj_tcf_b2 b2 b2_sp2 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020101050.ogg"
    yj "就因为这样害得我必须得一个人跑步吗。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010102710.ogg"
    xz "所以才会穿着体操服啊......"
    hide xz_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "既然没有晨练为什么还要换上体操服呢？"
    show yj_tcf_b2 b2 b2_h1
    play voice "voice/植澄友加/020101060.ogg"
    yj "因为我想要晨练嘛~"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010102720.ogg"
    xz "友加你现在是不是该去换衣服了？"
    show yj_tcf_b2 b2 b2_n3
    play voice "voice/植澄友加/020101070.ogg"
    yj "在上课之前我会去的。"
    show xz_dzf_b2 b2 b2_sp1
    play voice "voice/翔子/010102730.ogg"
    xz "一直这副打扮不觉得冷吗？"
    show yj_tcf_b2 b2 b2_s1
    play voice "voice/植澄友加/020101080.ogg"
    yj "比起这个，现在我反而感觉有些心凉......"
    me01 "为什么这么说？"
    show yj_tcf_b2 b2 b2_sp1
    play voice "voice/植澄友加/020101090.ogg"
    yj "你们两个是一起进的教室吧，也就是说果然是一起来学校的？"
    show xz_dzf_b2 b2 b2_s2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/翔子/010102740.ogg"
    xz "......只是碰巧在走廊上遇到而已。"
    show yj_tcf_b2 b2 b2_ga1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020101100.ogg"
    yj "撒谎可不行呀~"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010102750.ogg"
    xz "为、为什么认定就是撒谎啊？"
    show yj_tcf_b2 b2 b2_n1
    play voice "voice/植澄友加/020101110.ogg"
    yj "我在跑步的时候看到你们两个一起进的校门。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/翔子/010102760.ogg"
    xz "从进校门时就看见了吗......"
    show yj_tcf_b2 b2 b2_h2
    play voice "voice/植澄友加/020101120.ogg"
    yj "是啊~"
    me01 "眼睛真好使啊。"
    show yj_tcf_b2 b2 b2_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/020101130.ogg"
    yj "我两只眼睛可都是2.0的哟~"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/010102770.ogg"
    xz "......真是的别说了啦，快换衣服去吧。"
    # me01 "要是学习上也有这份干劲就好了。"
    hide yj_tcf_b2
    # $ flcam.move(4500, -300, 900, duration=1.5)
    # pause 0.5 hard
    # show xz_dzf_b2 b2 b2_n2
    # play voice "voice/翔子/0208810.ogg"
    # xz "另外神野君，我有话想对你说。"
    # me01 "......现在吗？"
    # $ flcam.move(2250, -350, 750, duration=1.5)
    show yj_tcf_b3 b3 b3_h1 onlayer m1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/020101140.ogg"
    yj "翔子你害羞了~"
    show xz_dzf_b2 b2 b2_a2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/翔子/010102780.ogg"
    xz "都、都说不是了！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard

label day207.passwalk_event01:
    play sound open_door5
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day corridor xuejian
    with dissolve
    play music second_124 fadein 3.0 if_changed
    pause 0.5 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0508980.ogg"
    lingyin "虽然我不认为现在还能得到你的原谅。"
    play voice "voice/青木铃音/0508990.ogg"
    lingyin "但是我已经，不会再对雷亚她们出手了。"
    show lingyin_dzf_b1 b1 b1_s1
    play voice "voice/青木铃音/0509000.ogg"
    lingyin "我想说的就是这些。"
    $ flcam.move(4500, -300, 1000, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b1 b1 b1_s3
    play voice "voice/青木铃音/0509030.ogg"
    lingyin "但是，这样也好......"
    play voice "voice/青木铃音/0509040.ogg"
    lingyin "一直以来我给你们添了这么多的麻烦。所以作为星天宫巫女的我保证，以后绝不会再出现在你们面前了。"
    me01 "请等一下......"
    me01 "果然，我还是没办法就这样原谅铃音同学。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0208820.ogg"
    xz "等！？"
    stop music fadeout 5.0
    show lingyin_dzf_b1 b1 b1_s1
    play voice "voice/青木铃音/0509050.ogg"
    lingyin "没关系的姐姐......"
    me01 "就这样不明不白地从我们眼前消失什么的。"
    me01 "这样的道歉我是绝对不会接受的。"
    play music first_29 fadein 3.0 if_changed
    me01 "想用离开的方式抹去自己犯下的错误，那只会一错再错。"
    me01 "所以......"
    me01 "如果不是选择消失，而是继续留在我们身边的话。"
    me01 "我还是可以考虑接受你的道歉。"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    xz "......"
    hide lingyin_dzf_b1
    show lingyin_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    lingyin "......"
    show xz_dzf_b2 b2 b2_s2
    play voice "voice/翔子/0208840.ogg"
    xz "真是老套的台词~"
    hide xz_dzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "所以铃音同学，你的选择是？"
    show lingyin_dzf_b2 b2 b2_c1 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/青木铃音/0509060.ogg"
    lingyin "......好的。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    show xz_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0208920.ogg"
    xz "就是这样......今后也请多多指教了~"
    me01 "这边也是请再多指教一次了，铃音同学。"
    play voice "voice/翔子/0208890.ogg"
    xz "虽然铃音这边已经没问题了，但今后或许还会有类似昨晚的事情发生。"
    play voice "voice/翔子/0208910.ogg"
    xz "所以这也是让我们来监督你的意思。"
    show lingyin_dzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0509070.ogg"
    lingyin "真是默契啊你们两个~"
    "也许正如翔子说的那样，原谅曾经的敌人是需要勇气的。"
    "但我可以确信，那位温柔善良的铃音同学又回来了。"
    "此刻在她的身上已经感觉不到那时的“暴戾”气息，仿佛是被救赎了一般。"
    "在这一刻，眼前仿佛又一次浮现出了在樱华镇时的场景。"
    "七夕的双子星，此刻依旧闪耀在浩瀚的宇宙之巅。"
    pause 1.0 hard
    scene black
    with slowerdissolve
    stop music fadeout 5.0
    pause 2.0 hard

label day207.centergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day center room xuejian
    with dissolve
    pause 1.0 hard
    "午饭时间，我来到了中庭。"
    "不同的是这一次并非只有我一人。"
    play music second_115 fadein 3.0 if_changed
    pause 0.5 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104790.ogg"
    liuli "神野前辈、植澄前辈辛苦你们了~"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104800.ogg"
    liuli "二位的考试情况如何了？"
    me01 "我的话......和平常一样吧，琉璃那边应该完全没有问题吧？"
    hide liuli_dzf_b3
    show liuli_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104810.ogg"
    liuli "是的，今天的情况还是不错的。"
    me01 "友加呢？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show yj_dzf_b3 b3 b3_n1 onlayer m1:
        xpos 0.7
    play voice "voice/植澄友加/020106830.ogg"
    yj "我的话和平常一样。"
    me01 "也就是说......"
    hide yj_dzf_b3 with None
    pause 0.1 hard
    show yj_dzf_b2 b2 b2_ga4 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/植澄友加/020106870.ogg"
    yj "要挂科了呀~"
    me01 "......总算是明白为什么翔子总是唠叨着叫你好好学习了。"
    show liuli_dzf_b1 b1 b1_s2
    play voice "voice/琉璃/040104850.ogg"
    liuli "那、那个......我是不是问了不该问的事情？"
    show yj_dzf_b2 b2 b2_n1
    play voice "voice/植澄友加/020106880.ogg"
    yj "完全没有，托花山院的福姐姐那边也好相处了许多。"
    show yj_dzf_b2 b2 b2_h1
    play voice "voice/植澄友加/020106890.ogg"
    yj "所以，谢谢你了~"
    hide liuli_dzf_b1
    show liuli_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104860.ogg"
    liuli "是、是的......如果能派上用场的话就太好了。"
    hide yj_dzf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "对了琉璃，有件事我想问你。"
    hide liuli_dzf_b3
    show liuli_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104870.ogg"
    liuli "什么事？"
    me01 "关于雪见市的气象研究。"
    hide liuli_dzf_b2
    show liuli_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/040104880.ogg"
    liuli "哈......"
    me01 "总之，边吃边说吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only liuli_cg center normal
    with slowdissolve
    pause 1.0 hard
    play voice "voice/琉璃/040104890.ogg"
    liuli "神野前辈想要知道关于气象研究的哪些内容呢？"
    me01 "姑且先从这不会堆积的雪开始讲解吧。"
    pause 0.1 hard
    scene set only liuli_cg center happy
    with dissolve
    play voice "voice/琉璃/040104920.ogg"
    liuli "那么神野前辈，你准备好了吗？"
    me01 "哦，放马过来吧！"
    stop music fadeout 5.0
    pause 2.0 hard
    scene set only liuli_cg kg_sd one
    with dissolve
    play music second_119 fadein 3.0
    pause 1.0 hard
    play voice "voice/琉璃/040104930.ogg"
    liuli "想了解不会堆积的雪，首先必须先知道天气变化的规律。"
    play voice "voice/琉璃/040104940.ogg"
    liuli "这是因为地球拥有的大气层，吸收了来自太阳的辐射。"
    pause 0.1 hard
    scene set only liuli_cg kg_sd two
    with dissolve
    play voice "voice/琉璃/040104950.ogg"
    liuli "根据吸收太阳辐射量的不同，各地之间就会产生温差。"
    play voice "voice/琉璃/040104960.ogg"
    liuli "这种温差导致了大气的流动，热浪也会随之产生。"
    play voice "voice/琉璃/040104970.ogg"
    liuli "然后随着热浪的移动会造成空气中的水蒸气急剧减少，从而导致极端天气的形成。"
    play voice "voice/琉璃/040104980.ogg"
    liuli "以这点为基础，现在开始下一个说明吧。"
    pause 0.1 hard
    scene set only liuli_cg kg_sd three
    with dissolve
    play voice "voice/琉璃/040104990.ogg"
    liuli "太阳系中还存在着像金星和火星这类存在大气的星球。"
    play voice "voice/琉璃/040105000.ogg"
    liuli "由于这些天体也会接受太阳的辐射，所以天气也会变化。"
    play voice "voice/琉璃/040105020.ogg"
    liuli "位于地球上的这座雪见市现在似乎正是由于某些原因使得热力循环系统很不稳定，而这种循环模式似乎也在其他的行星上出现过。"
    play voice "voice/琉璃/040105040.ogg"
    liuli "也就是说，现在地球上超乎寻常的气候现象，在其他星球上也同样存在。"
    pause 0.1 hard
    play sound yangmu
    scene set only liuli_cg kg_sd four
    with dissolve
    play voice "voice/琉璃/040105060.ogg"
    liuli "因此，只要分析大气构造的差异和相应的地理特性，就能够解释其中的奥秘了。"
    play voice "voice/琉璃/040105080.ogg"
    liuli "为了搞清楚这些突然发生的怪异气候现象，现在的科研小组还在努力提取雪中的成分。"
    play voice "voice/琉璃/040105100.ogg"
    liuli "行星气象学的最终目标就是理解整个行星乃至太阳系中错综复杂的气候变化，并且能够完整地推演整个流程。"
    pause 0.1 hard
    scene set only liuli_cg kg_sd five
    with dissolve
    me01 "那个啊，琉璃......"
    play voice "voice/琉璃/040105110.ogg"
    liuli "有什么问题吗？"
    me01 "已经足够了。"
    play voice "voice/琉璃/040105120.ogg"
    liuli "......是这样吗？"
    me01 "是啊，脑袋已经装不下了。"
    me01 "而且......"
    "一旁的友加已经睡着了。"
    pause 1.0 hard
    scene set only liuli_cg center normal
    with dissolve
    play voice "voice/琉璃/040105130.ogg"
    liuli "那么，还有其他什么想要了解的事吗？"
    me01 "有这些就够了，谢谢你。"
    "看来下次提问之前需要注意把控一下范围。"
    "至少太过复杂的问题是不会再问了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day207'
    $ seen_day207_kindergarden_event01 = False
    $ seen_day207_school_event01 = False

label day207.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day207' or _overworld_label == 'day207.school_event01':
        $ flcam.move(*overworld.camera_positions['school'])
    elif _overworld_label == 'day207.kindergarden_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        kindergarden=("day207.kindergarden_event01", "not seen_day207_kindergarden_event01"),
        school=("day207.school_event01", "not seen_day207_school_event01"),
        bridge=("day207.bridge_event01", "seen_day207_kindergarden_event01 and seen_day207_school_event01"))
    $ window_animate_outro()
    if _return == 'day207.kindergarden_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day207.school_event01':
        $ flcam.move(*overworld.camera_positions['school'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day207.bridge_event01':
        $ flcam.move(*overworld.camera_positions['bridge'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day207.school_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day room2 xuejian
    with slowdissolve
    play music second_118 fadein 3.0 if_changed
    play sound open_door5
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dzf_b2 b2 b2_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/水之濑/050101770.ogg"
    szl "柚子，你在这里吃午饭吗？"
    $ flcam.move(3200, -350, 750, duration=1.5)
    show qbj_dzf_b1 b1 b1_ga2 onlayer m2 at walkin_r(0.8)
    pause 0.5 hard
    play voice "voice/千波姐/160100790.ogg"
    qbj "是啊，因为今天带了便当。"
    show szl_dzf_b2 b2 b2_h3
    play voice "voice/水之濑/050101780.ogg"
    szl "那我也在这里吃好了。"
    show qbj_dzf_b1 b1 b1_sp1
    play voice "voice/千波姐/160100800.ogg"
    qbj "你也带了便当？"
    hide szl_dzf_b2
    show szl_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101790.ogg"
    szl "不，我去便利店买点东西来。"
    show qbj_dzf_b1 b1 b1_ga2
    play voice "voice/千波姐/160100810.ogg"
    qbj "......不用特地为了我做到那个地步啦，回家吃不就好了吗？"
    show szl_dzf_b1 b1 b1_h1
    play voice "voice/水之濑/050101800.ogg"
    szl "就当是考试过后的放松吧，而且在学生会教室吃饭比较安静。"
    show qbj_dzf_b1 b1 b1_n1
    play voice "voice/千波姐/160100820.ogg"
    qbj "原来小凛也是这么想的啊。"
    show szl_dzf_b1 b1 b1_n1
    play voice "voice/水之濑/050101810.ogg"
    szl "柚子也是吗？"
    show qbj_dzf_b1 b1 b1_h1
    play voice "voice/千波姐/160100830.ogg"
    qbj "这可能就是我们都是从一年级开始就一直在学生会工作的关系吧。"
    hide qbj_dzf_b1
    $ flcam.move(2250, -200, 600, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.7
    play voice "voice/日向怜/120102340.ogg"
    rxl "是这样吗？"
    show szl_dzf_b1 b1 b1_s1
    play voice "voice/水之濑/050101820.ogg"
    szl "......是的。"
    hide rxl_dzf_b1
    hide szl_dzf_b1
    $ flcam.move(7300, -300, 900, duration=1.5)
    pause 0.5 hard
    show qbj_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.8
    play voice "voice/千波姐/160100840.ogg"
    qbj "日向同学也来了，要一起吃午饭吗？"
    $ flcam.move(4500, -350, 750, duration=1.5)
    show rxl_dzf_b2 b2 b2_h1 onlayer m1:
        xpos 0.6
    play voice "voice/日向怜/120102350.ogg"
    rxl "我只是跟着水之濑同学过来的，不过既然来了就在这里吃好了。"
    $ flcam.move(2250, -200, 600, duration=1.5)
    show szl_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/050101830.ogg"
    szl "你就是想找个借口监视我对吧。（小声）"
    show qbj_dzf_b1 b1 b1_n1
    play voice "voice/千波姐/160100920.ogg"
    qbj "话说回来各位，考试如何了？"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/050101910.ogg"
    szl "和平常一样。"
    show rxl_dzf_b2 b2 b2_n1
    play voice "voice/日向怜/120102430.ogg"
    rxl "我也和平时一样哟~"
    show qbj_dzf_b1 b1 b1_h1
    play voice "voice/千波姐/160100930.ogg"
    qbj "学生会的成员都是成绩优秀的人，所以日向同学的成绩也很优秀吧。"
    hide qbj_dzf_b1
    $ flcam.move(0, -350, 750, duration=1.5)
    show szl_dzf_b2 b2 b2_ga1
    play voice "voice/水之濑/050101920.ogg"
    szl "反正也只有保健体育拿得出手而已吧。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h3 onlayer m1:
        xpos 0.6
    play voice "voice/日向怜/120102440.ogg"
    rxl "在这点上我可是有不输任何人的自信呢。"
    hide szl_dzf_b2
    $ flcam.move(4500, -350, 750, duration=1.5)
    show qbj_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.8
    play voice "voice/千波姐/160100940.ogg"
    qbj "日向同学为什么会选择来学生会当干部呢？"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_n1 onlayer m1:
        xpos 0.6
    play voice "voice/日向怜/120102450.ogg"
    rxl "因为被老师认可了。"
    $ flcam.move(2250, -200, 600, duration=1.5)
    show szl_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/050101930.ogg"
    szl "也就是说你的组织用某些手段买通了学校的人对吧。"
    show qbj_dzf_b1 b1 b1_sp1
    play voice "voice/千波姐/160100950.ogg"
    qbj "......组织？"
    hide rxl_dzf_b2 with None
    pause 0.1 hard
    show rxl_dzf_b1 b1 b1_a1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.6
    play voice "voice/日向怜/120102460.ogg"
    rxl "才不是，我是凭自己的实力进来的。要证明给你们看吗？"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/050101940.ogg"
    szl "怎么证明......"
    stop music fadeout 5.0
    hide qbj_dzf_b1
    $ flcam.move(0, -350, 750, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_h3
    play voice "voice/日向怜/120102470.ogg"
    rxl "盯——"
    play music second_108 fadein 3.0 if_changed
    pause 0.5 hard
    play sound jing01
    with vpunch
    hide szl_dzf_b3 with None
    pause 0.1 hard
    show szl_dzf_b2 b2 b2_sp2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.4
    play voice "voice/水之濑/050101950.ogg"
    szl "等......你在看什么地方啊！？"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_a1 onlayer m1:
        xpos 0.6
    play voice "voice/日向怜/120102480.ogg"
    rxl "八十八吗......"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_ga4 onlayer m2 at flu_down(0.35, 20):
        xpos 0.4
    play voice "voice/水之濑/050101960.ogg"
    szl "{size=72}？！{/size}"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_h1 onlayer m1:
        xpos 0.6
    play voice "voice/日向怜/120102490.ogg"
    rxl "这就是我的实力哟，顺带一提我可没有用{rb}远隔透视{/rb}{rt}clairvoyance{/rt}。"
    $ flcam.move(2250, -200, 600, duration=1.5)
    show qbj_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.8
    play voice "voice/千波姐/160100960.ogg"
    qbj "clair......什么？"
    show szl_dzf_b3 b3 b3_s2
    play voice "voice/水之濑/050101970.ogg"
    szl "什、什么都没有！"
    play voice "voice/千波姐/160100970.ogg"
    qbj "？"
    hide qbj_dzf_b1
    $ flcam.move(0, -350, 750, duration=1.5)
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_a1 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/050101980.ogg"
    szl "等下！为什么我还得帮你善后啊？！"
    show rxl_dzf_b1 b1 b1_ga1
    play voice "voice/日向怜/120102500.ogg"
    rxl "不是你擅自圆场的吗~"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/050101990.ogg"
    szl "还不是因为你说了{rb}灵纹{/rb}{rt}rune{/rt}的事，引起骚动的话要怎么办啊！"
    show rxl_dzf_b1 b1 b1_s1
    play voice "voice/日向怜/120102510.ogg"
    rxl "你不也说了“监视”还有“组织”什么的吗......"
    show szl_dzf_b3 b3 b3_s1 at flu_down(0.35, 20):
        xpos 0.4
    play voice "voice/水之濑/050102000.ogg"
    szl "呜......"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h1 onlayer m1:
        xpos 0.6
    play voice "voice/日向怜/120102520.ogg"
    rxl "没问题的啦，就算说成是超能力，会长也只会当成是开玩笑的。"
    hide rxl_dzf_b2
    hide szl_dzf_b3
    $ flcam.move(7500, -300, 900, duration=1.5)
    pause 0.5 hard
    show qbj_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.8
    play voice "voice/千波姐/160100980.ogg"
    qbj "......怎么了？突然说起悄悄话。"
    $ flcam.move(4500, -350, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_h1 onlayer m1:
        xpos 0.6
    play voice "voice/日向怜/120102540.ogg"
    rxl "只是在调查而已。"
    play voice "voice/千波姐/160100990.ogg"
    qbj "调查什么？"
    show rxl_dzf_b1 b1 b1_ga1
    play voice "voice/日向怜/120102550.ogg"
    rxl "八十吗......"
    play voice "voice/千波姐/160101000.ogg"
    qbj "欸？"
    show rxl_dzf_b1 b1 b1_h3
    play voice "voice/日向怜/120102560.ogg"
    rxl "泽村同学的胸部尺寸。"
    show qbj_dzf_b1 b1 b1_sp2 at flu_down(0.35, 20):
        xpos 0.8
    play voice "voice/千波姐/160101010.ogg"
    qbj "{size=72}？！{/size}"
    hide qbj_dzf_b1
    $ flcam.move(0, -350, 750, duration=1.5)
    show szl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/050102030.ogg"
    szl "适可而止！"
    play sound hite_light
    show wflash onlayer texture
    with vpunch
    show rxl_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.6
    play voice "voice/日向怜/120102570.ogg"
    rxl "好痛！"
    show rxl_dzf_b1 b1 b1_s1
    play voice "voice/日向怜/120102580.ogg"
    rxl "......小凛你还真是粗暴啊。"
    show szl_dzf_b2 b2 b2_s1
    play voice "voice/水之濑/050102040.ogg"
    szl "哼！"
    show rxl_dzf_b1 b1 b1_h3
    play voice "voice/日向怜/120102590.ogg"
    rxl "顺带一提我是八十三哟~"
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.4
    play voice "voice/水之濑/050102050.ogg"
    szl "没有人问你好吗。"
    $ flcam.move(2250, -200, 600, duration=1.5)
    show qbj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.8
    play voice "voice/千波姐/160101020.ogg"
    qbj "......果然我是最小的。"
    show szl_dzf_b3 b3 b3_s1
    play voice "voice/水之濑/050102060.ogg"
    szl "你这不是害柚子变得消沉了吗？！"
    hide szl_dzf_b3
    hide rxl_dzf_b1
    hide qbj_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    play sound open_door5
    pause 1.0 hard
    show xz_dzf_b2 b2 b2_n1 onlayer m1 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/翔子/010105200.ogg"
    xz "今天的活动室有点热闹啊。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_h1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/120102600.ogg"
    rxl "啊，青木同学~"
    show xz_dzf_b2 b2 b2_sp1
    play voice "voice/翔子/010105210.ogg"
    xz "大家到都齐了，今天有什么工作吗？"
    $ flcam.move(-800, -200, 600, duration=1.5)
    show qbj_dzf_b1 b1 b1_n1 onlayer m1:
        xpos 0.65
    play voice "voice/千波姐/160101030.ogg"
    qbj "考试期间是没有工作的。"
    show xz_dzf_b2 b2 b2_ga1
    play voice "voice/翔子/010105220.ogg"
    xz "只是以防万一问一下而已。"
    hide xz_dzf_b2
    hide rxl_dzf_b1
    $ flcam.move(6500, -350, 750, duration=1.5)
    show szl_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.9
    play voice "voice/水之濑/050102070.ogg"
    szl "青木同学是有事找柚子才来的吧？"
    hide szl_dzf_b2
    hide qbj_dzf_b1
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show rxl_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    show xz_dzf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/日向怜/120102610.ogg"
    rxl "盯——"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/010105230.ogg"
    xz "......日向同学？"
    play voice "voice/日向怜/120102620.ogg"
    rxl "八十六吗......"
    play sound jing01
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_sp2 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/010105240.ogg"
    xz "欸？"
    show rxl_dzf_b1 b1 b1_h1
    play voice "voice/日向怜/120102630.ogg"
    rxl "虽然输给了小凛，但是青木同学的也够大啊~"
    show szl_dzf_b3 b3 b3_a2 onlayer screens at side_right('szl'), basicfade
    play voice "voice/水之濑/050102090.ogg"
    szl "你给我适可而止！"
    hide szl_dzf_b3
    play sound hite_light
    show wflash
    with vpunch
    pause 0.25 hard
    $ flcam.move(-800, -100, 400, duration=1.5)
    show rxl_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.5
        linear 0.5 xpos 0.7
    pause 0.5 hard
    show szl_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/120102640.ogg"
    rxl "{size=72}好痛！{/size}"
    stop music fadeout 5.0
    pause 0.5 hard
    $ flcam.move(2000, -100, 400, duration=1.5)
    show qbj_dzf_b1 b1 b1_s2 onlayer m1:
        xpos 0.9
    play voice "voice/千波姐/160101050.ogg"
    qbj "果然我是最小的......"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.3
    play voice "voice/翔子/010105250.ogg"
    xz "那、那个......你们在说什么？"
    play music second_115 fadein 3.0 if_changed
    show rxl_dzf_b1 b1 b1_h3
    play voice "voice/日向怜/120102650.ogg"
    rxl "在说我是如何凭借实力当上学生会干部的。"
    hide szl_dzf_b3
    show szl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050102100.ogg"
    szl "误会越来越深了......"
    show xz_dzf_b2 b2 b2_n1
    play voice "voice/翔子/010105260.ogg"
    xz "日向同学是老师推荐加入学生会的吧？"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h2 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/120102660.ogg"
    rxl "是啊，虽然我也有自我推荐就是了。"
    show szl_dzf_b2 b2 b2_sp1
    play voice "voice/水之濑/050102110.ogg"
    szl "......看不出你还挺擅长学习的嘛。"
    show rxl_dzf_b2 b2 b2_s1
    play voice "voice/日向怜/120102680.ogg"
    rxl "之前只是因为讨厌学习而已，并不是完全没办法应付。"
    show qbj_dzf_b1 b1 b1_ga2
    play voice "voice/千波姐/160101060.ogg"
    qbj "是吗......果然日向同学也很优秀啊。"
    play sound yangmu
    hide rxl_dzf_b2 with None
    pause 0.1 hard
    show rxl_dzf_b1 b1 b1_h3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/120102690.ogg"
    rxl "会长的小胸部我也喜欢了，所以没有必要消沉~"
    play sound hite_light
    show wflash onlayer texture
    with vpunch
    show rxl_dzf_b1 b1 b1_c1 at flu_down(0.15, 20):
        xpos 0.7
    hide szl_dzf_b2
    show szl_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050102130.ogg"
    szl "你可以闭嘴了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day207_school_event01:
        $ seen_day207_school_event01 = True
    $ _overworld_label = 'day207.school_event01'
    jump day207.map

label day207.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school day inside xuejian2
    play music second_118 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    me01 "下午好。"
    play voice "voice/立花希/030104690.ogg"
    lhx "这不是凉君吗，今天这么早就放学了？"
    me01 "今天是期末考试，结束就回来了。"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/030104710.ogg"
    lhx "是来接爱衣的吗？"
    me01 "不只是这样。"
    show lhx_dzf_b2 b2 b2_sp1
    play voice "voice/立花希/030104720.ogg"
    lhx "还有其他事情吗？"
    me01 "其实也就是来看看你的身体状况怎么样了，有好好休息吗？"
    show lhx_dzf_b2 b2 b2_h3
    play voice "voice/立花希/030104730.ogg"
    lhx "是的，能像这样进行日常的工作就说明我已经没事了~"
    me01 "你说的工作就是指陪小朋友一起玩？"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104740.ogg"
    lhx "不是玩，我的工作是看着小朋友让他们不要到处乱跑。"
    me01 "因为上次小桃的事？"
    show lhx_dzf_b3 b3 b3_n1
    play voice "voice/立花希/030104750.ogg"
    lhx "是的，话说你那边的考试如何？"
    me01 "和平常一样。"
    play voice "voice/立花希/030104760.ogg"
    lhx "不用继续复习了吗？"
    me01 "虽然复习还是必要的，但是比起这个立花老师的身体状况更让我担心。"
    show lhx_dzf_b3 b3 b3_n5 at flu_down(0.35, 20):
        xpos 0.5
    lhx "......"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104780.ogg"
    lhx "还得熟悉一下周围的环境，等这里的工作结束之后我们一起去市中心看看吧。"
    me01 "这个嘛......其实我已经去过了。"
    show lhx_dzf_b2 b2 b2_ga1
    play voice "voice/立花希/030104790.ogg"
    lhx "这是怎么一回事......"
    me01 "休息日的时候稍微去逛了一下子。"
    hide lhx_dzf_b2
    show lhx_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104800.ogg"
    lhx "叛徒。"
    me01 "为什么啊？！"
    hide lhx_dzf_b1
    show lhx_dzf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104810.ogg"
    lhx "是和日向串通好的吗？"
    me01 "这倒不是，是和我们之前在神社见过面的花山院同学一起去的。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104820.ogg"
    lhx "大叛徒！"
    me01 "所以说为什么啊？！" with vpunch
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/030104830.ogg"
    lhx "和我的约定就这样丢到垃圾桶里了吗！"
    me01 "莫非立花老师是看我和其他女孩子一起出去所以生气了？"
    show lhx_dzf_b2 b2 b2_a1
    play voice "voice/立花希/030104840.ogg"
    lhx "......谁也没有生气好吗。"
    me01 "不过虽说去是去过了，但还有好多地方没有来得及逛。"
    me01 "我也觉得有必要再去一次。"
    show lhx_dzf_b2 b2 b2_sp1
    play voice "voice/立花希/030104850.ogg"
    lhx "竟然会这样......"
    me01 "你在惊讶个什么劲啊。"
    show lhx_dzf_b2 b2 b2_n1
    play voice "voice/立花希/030104860.ogg"
    lhx "既然凉君你说到这个份上了，我倒是可以无可奈何地陪你一起去~"
    me01 "这么勉强真是难为你了。"
    hide lhx_dzf_b2 with None
    pause 0.1 hard
    show lhx_dzf_b3 b3 b3_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/030104870.ogg"
    lhx "那就这么说定了~"
    me01 "既然如此那我先一步告辞了。"
    hide lhx_dzf_b3
    show lhx_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104880.ogg"
    lhx "叛徒......"
    me01 "这次是去办点事情。"
    me01 "等到要去新城区的时候我会通知你的。"
    me01 "立花老师你就安心等我的消息吧。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show lhx_dzf_b2 b2 b2_n3
    play voice "voice/立花希/030104890.ogg"
    lhx "......就算你不说我也会立马追上去的。"
    hide lhx_dzf_b2
    show lhx_dzf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/030104900.ogg"
    lhx "我可是无时无刻都在凉君你身后追赶着的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day207_kindergarden_event01:
        $ seen_day207_kindergarden_event01 = True
    $ _overworld_label = 'day207.kindergarden_event01'
    jump day207.map

label day207.bridge_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "此刻的友加正在河滩上奔跑着。"
    "从中庭告别之后就一个人来到了这里。"
    pause 1.0 hard
    scene set only bridge day under xuejian
    with dissolve
    play music second_124 fadein 3.0 if_changed
    play ambience1 jiaobu3 fadein 3.0
    pause 1.0 hard
    "然而脚步却十分沉重，仿佛每迈出一步都是一种煎熬。"
    "不管怎么调整，感觉到的也只有疲劳而已。"
    pause 1.0 hard
    stop ambience1 fadeout 5.0
    scene set only yj_cg daze1
    with slowdissolve
    pause 1.0 hard
    "女孩停下脚步，静静地看着水中自己的倒影。"
    "此刻水面上浮现出的，是自己那无精打采的脸庞。"
    play voice "voice/植澄友加/020104240.ogg"
    yj "回不到......以前那样了吗。"
    play voice "voice/植澄友加/020104250.ogg"
    yj "从什么时候开始就变成现在这样一个人了呢......"
    "寂寞和空虚在心头堆积着。"
    "之所以会选择奔跑。"
    "就是因为觉得这样能稍微转移一下注意力。"
    pause 1.0 hard
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "一个人勉强着。"
    "受够了孤独。"
    "已经忘记了，家的感觉。"
    "上一次脸上挂满笑容是什么时候的事呢？"
    pause 1.0 hard
    scene set only yj_cg daze1
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/020104260.ogg"
    yj "姐姐她......"
    play voice "voice/植澄友加/020104290.ogg"
    yj "我是不是也有点，羡慕翔子了呢。"
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 1.0 hard
    "不行不行！"
    "女孩用力摇了摇头，想要甩开那些不安的情绪。"
    "一旦停止奔跑就会胡思乱想。"
    "明明自己一直是不擅长思考的。"
    "明明应该，是这样的......"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only bridge day under xuejian
    show yj_tcf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/植澄友加/020104300.ogg"
    yj "......跑起来吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg daze2
    with dissolve
    pause 1.0 hard
    "缓缓放下手中编制好的草船。"
    "目送它顺着水流远去。"
    "小船划过的水面荡起层层的波澜。"
    "就如同回忆留下的伤疤，在心中扩散开来......"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge day xuejian
    with dissolve
    pause 1.0 hard
    "虽然之前被研究所谢绝见面，但是我并没有打算就此放弃。"
    "如果对方也是在调查城市里的异常气候的话，说不定也会注意到{rb}灵继者{/rb}{rt}elfin{/rt}的存在。"
    "既然如此，比起一个人调查事情的真相，联合星天宫研究所的力量想必才是一个明智之举。"
    pause 1.0 hard
    scene set only yj_cg daze2
    with dissolve
    pause 1.0 hard
    me01 "......那是？"
    pause 1.0 hard
    scene set only bridge day xuejian
    with dissolve
    pause 1.0 hard
    me01 "那家伙在这里做什么？"
    pause 1.0 hard
    scene set only yj_cg daze2
    with dissolve
    pause 1.0 hard
    me01 "怎么一个人在这里发呆？"
    pause 0.1 hard
    scene set only yj_cg sp2
    $ flcam.move(-2800, -2100, 750, duration=1.5, warper='ease_quad')
    with dissolve
    pause 0.5 hard
    play voice "voice/植澄友加/020102850.ogg"
    yj "{size=72}哇！{/size}" with vpunch
    play music second_118 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge day under xuejian
    with dissolve
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_tcf_b2 b2 b2_sp2 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 1.0
        parallel:
            linear 1.0 ypos 0.95
        parallel:
            linear 1.0 alpha 1.0
    pause 0.5 hard
    play voice "voice/植澄友加/020102860.ogg"
    yj "凉君，你又来吓我。"
    me01 "并没有这个意思，我只是刚好路过而已。"
    show yj_tcf_b2 b2 b2_sp1
    play voice "voice/植澄友加/020102870.ogg"
    yj "今天也要去新城区？"
    me01 "算是吧，倒是你刚考完试就开始社团活动吗？"
    hide yj_tcf_b2 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020102880.ogg"
    yj "是啊，谁叫我最喜欢跑步了嘛~"
    me01 "就你一个人吗？"
    hide yj_tcf_b3
    show yj_tcf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102910.ogg"
    yj "凉君要陪我一起吗？"
    me01 "请容我拒绝，要是被发现会惹老师生气的。"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102920.ogg"
    yj "关于这点我已经放弃抵抗了~"
    show yj_tcf_b2 b2 b2_sp1
    play voice "voice/植澄友加/020102930.ogg"
    yj "{rb}璃之助{/rb}{rt}琉璃的昵称{/rt}没和你一起吗？"
    me01 "是啊，今天是我一个人来的。"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102940.ogg"
    yj "一个人约会吗......"
    me01 "一个人算不上约会吧。"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102950.ogg"
    yj "去买东西？"
    me01 "不，应该算是散步吧。"
    hide yj_tcf_b2
    show yj_tcf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102960.ogg"
    yj "打算去哪里散步？"
    me01 "研究所。"
    show yj_tcf_b3 b3 b3_ga4
    play voice "voice/植澄友加/020102970.ogg"
    yj "去那种地方散步会有趣吗......"
    me01 "这点我承认并不怎么有趣。"
    "尤其是见识了琉璃的行星气象学课程之后。"
    hide yj_tcf_b3
    show yj_tcf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102980.ogg"
    yj "即使这样也要去啊，奇怪的凉君。"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020102990.ogg"
    yj "没有其他想去的地方了吗？"
    me01 "没有。"
    hide yj_tcf_b2
    show yj_tcf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103000.ogg"
    yj "去那种地方是有什么事吗？"
    me01 "是啊，有一些比较在意事情。"
    hide yj_tcf_b3
    show yj_tcf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103010.ogg"
    yj "凉君你......对这座城市的气候很感兴趣吗。"
    me01 "不如说这里的大家对此毫不在意这件事本身就很奇怪。"
    show yj_tcf_b1 b1 b1_n1
    play voice "voice/植澄友加/020103020.ogg"
    yj "一般人的话是不会在意的，毕竟雪见市人们对这场雪的态度都很平静嘛。"
    me01 "为什么这么肯定？"
    hide yj_tcf_b1
    show yj_tcf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103030.ogg"
    yj "因为大家一定都觉得，比起动脑活动筋骨更有趣嘛。"
    me01 "这只是你自己的想法而已吧......"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show yj_tcf_b3 b3 b3_n1
    play voice "voice/植澄友加/020103040.ogg"
    yj "我带你去吧？"
    me01 "去研究所？"
    show yj_tcf_b3 b3 b3_ga4
    play voice "voice/植澄友加/020103050.ogg"
    yj "嗯，虽然我自己也没怎么进去过~"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103060.ogg"
    yj "毕竟打扰到姐姐工作的话就不好了。"
    me01 "姐姐？虽然现在才问有些失礼。"
    me01 "莫非那位圣护院主任就是友加你的姐姐吗？"
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103070.ogg"
    yj "嗯......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg normal3
    with dissolve
    pause 1.0 hard
    "在我们交谈期间，友加扯下了一旁的树叶做起了草船。"
    "她把草船放在水面上，随波逐流。"
    play voice "voice/植澄友加/020103080.ogg"
    yj "我也有些担心姐姐她最近有没有好好吃饭。"
    play voice "voice/植澄友加/020103090.ogg"
    yj "毕竟把身体搞坏了的话就没法好好做研究了嘛。"
    pause 0.1 hard
    scene set only yj_cg daze1
    with dissolve
    "目送着草船缓缓顺着水流飘向下游。"
    "在这过程中友加的视线始终没有移开过。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only bridge day under xuejian
    show yj_tcf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/植澄友加/020103100.ogg"
    yj "我去换个衣服。"
    me01 "在这里换衣服吗？"
    hide yj_tcf_b1 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_ga4 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020103110.ogg"
    yj "这是当然的，就算是我也不能穿着体操服在街上走啊。"
    me01 "可是，这里有地方可以换衣服吗？"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103120.ogg"
    yj "桥下。"
    me01 "在那种地方换真的没问题吗......"
    show yj_tcf_b2 b2 b2_sp1
    play voice "voice/植澄友加/020103130.ogg"
    yj "会有什么问题？"
    me01 "要是被谁看见的话......"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide yj_tcf_b2
    show yj_tcf_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103140.ogg"
    yj "凉君你......会偷看吗？"
    me01 "才不会！"
    hide yj_tcf_b1
    show yj_tcf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103150.ogg"
    yj "那就没问题了，毕竟这个河滩很少会有人来。"
    show yj_tcf_b2 b2 b2_n3
    play voice "voice/植澄友加/020103160.ogg"
    yj "不过为了以防万一，能帮忙把下风吗？"
    me01 "我、我知道了。"
    hide yj_tcf_b2 with None
    pause 0.1 hard
    show yj_tcf_b3 b3 b3_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020103170.ogg"
    yj "可不许偷窥哟~"
    me01 "都说了不会的！"
    hide yj_tcf_b3
    show yj_tcf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103180.ogg"
    yj "那我去去就回~"
    pause 0.5 hard
    play sound jiaobu2
    show yj_tcf_b2 b2 b2_h1 at walkout_l(0.5)
    pause 0.5 hard
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day207.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory day outside xuejian
    with dissolve
    play music second_105 fadein 3.0 if_changed
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103250.ogg"
    yj "......好紧张。"
    me01 "一般姐妹见面会紧张吗？"
    show yj_dsf_b1 b1 b1_n1
    play voice "voice/植澄友加/020103260.ogg"
    yj "果然一般是不会的吧。"
    me01 "翔子和爱衣虽说不是亲姐妹，但给人的感觉却十分自然。"
    me01 "还有一诚同学和小桃给人的感觉也很温馨。"
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/020103270.ogg"
    yj "我和姐姐不太像，在旁人的眼中绝对看不出是亲姐妹。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/020103280.ogg"
    yj "所以说不定和普通的姐妹不大一样。"
    me01 "就算不像，是姐妹这一点也不会改变的。"
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/020103290.ogg"
    yj "......也许是这样的吧。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    me01 "这么无精打采的可不像你啊。"
    hide yj_dsf_b1
    show yj_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103300.ogg"
    yj "欸......"
    me01 "我觉得友加应该是对任何事情都很直率才是。"
    me01 "烦恼的样子可一点都不适合你。"
    hide yj_dsf_b3
    show yj_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103310.ogg"
    yj "说的也是呢......说不定是有点不像我自己。"
    hide yj_dsf_b1 with None
    pause 0.1 hard
    show yj_dsf_b2 b2 b2_ga3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020103320.ogg"
    yj "我可是立刻就会火热起来的女人呢~"
    me01 "这种说法总觉得有些微妙......"
    show yj_dsf_b2 b2 b2_h1
    play voice "voice/植澄友加/020103330.ogg"
    yj "就是比起动脑更喜欢活动身子的女人。"
    me01 "也就是充满活力的意思吧。"
    show yj_dsf_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020103340.ogg"
    yj "是啊~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside1 xuejian
    with dissolve
    pause 1.0 hard
    me01 "这里还是一如既往的安静......"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103350.ogg"
    yj "凉君之前也来过这里吗？"
    me01 "是啊，琉璃带我来的。"
    hide yj_dsf_b3
    show yj_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103360.ogg"
    yj "见到姐姐了？"
    me01 "没有，上次似乎是因为工作的关系谢绝见面了。"
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/020103370.ogg"
    yj "那今天会不会也见不到......"
    me01 "又无精打采了。"
    hide yj_dsf_b1 with None
    pause 0.1 hard
    show yj_dsf_b2 b2 b2_ga3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/020103380.ogg"
    yj "我可是立刻就会火热起来的女人呢。"
    me01 "一点说服力都没有啊......"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103390.ogg"
    yj "姐姐应该就在实验室里，那么......要进去了。"
    hide yj_dsf_b1
    $ flcam.move(0, 0, 800, duration=1.5)
    pause 2.0 hard
    play sound open_door6
    $ flcam.move(0, 0, 0)
    scene black
    with right2left_02
    pause 1.0 hard
    scene set only laboratory inside2 xuejian
    with right2left_02
    pause 1.0 hard
    play music second_122 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1 onlayer m1 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/圣护院/150100010.ogg"
    shy "真是吃惊，你会来找我还真是罕见。"
    "出来迎接我们的是一名身着白大褂的女子。"
    "然而我一眼便认出了，她就是之前在樱华镇阻拦我进入观景台的那位女子。"
    "看着对方淡定的眼神，想必也已经认出我来了。"
    "虽然从进门后的那几番话明显都是对友加说的，但对方的视线却始终停留在我的身上。"
    "直觉告诉我这个人——友加的姐姐她，不简单！"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103400.ogg"
    yj "我也吃了一惊......本以为肯定会被赶出去的。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100020.ogg"
    shy "我有赶你走过吗？"
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/020103410.ogg"
    yj "虽然是没有，不过凉君说他之前没能见到你。"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100030.ogg"
    shy "凉君？是说他吗？"
    show yj_dsf_b1 b1 b1_n1
    play voice "voice/植澄友加/020103420.ogg"
    yj "嗯，他叫神野凉，是我的同班同学。"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103430.ogg"
    yj "然后这边的就是我的姐姐。"
    hide yj_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    "虽然友加自己说她和姐姐不像。"
    "但是比起外在，两个人营造出来的氛围更加违和。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100040.ogg"
    shy "说起来之前也听花山院说过有位叫这个名字的学生来过。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103440.ogg"
    yj "真是的......姐姐你在工作以外的事情上太健忘了。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100050.ogg"
    shy "所以找我有什么事吗？"
    pause 0.5 hard
    hide shy_yjf_b1
    hide yj_dsf_b1
    play sound touch
    $ flcam.move(0, -800, 1100, duration=2.0, warper='ease_cubic')
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only shy_cg one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/圣护院/150100060.ogg"
    shy "我还在工作中，所以希望能快点结束。"
    me01 "我听说这座研究所正在调查雪见市的异常气候对吧？"
    play voice "voice/圣护院/150100070.ogg"
    shy "是的。"
    me01 "现在正在进行的是对前一阵神社异常天气的调查？"
    play voice "voice/圣护院/150100080.ogg"
    shy "你听谁说的？"
    me01 "是琉......花山院同学告诉我的。"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/150100090.ogg"
    shy "是吗，虽然我并没有想要隐瞒的意思，因此也不会追究这件事情。"
    "真正想隐瞒的是调查结果吧......"
    pause 0.1 hard
    scene set only shy_cg four
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    "见我盯着她许久不说话。"
    "圣护院小姐皱起眉头仔细打量着我。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only laboratory inside2 xuejian
    show shy_yjf_b1 b1 b1_n1 onlayer m1:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/150100100.ogg"
    shy "回到最初的问题上来吧......友加，你找我有什么事？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103450.ogg"
    yj "因为姐姐你一直都不回家，所以在想是不是发生了什么事。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150100110.ogg"
    shy "我只是一直在这里工作而已。"
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/020103460.ogg"
    yj "......那好歹也联络我一下。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100120.ogg"
    shy "这样啊......抱歉我忘记了。"
    show yj_dsf_b1 b1 b1_n1
    play voice "voice/植澄友加/020103470.ogg"
    yj "那有好好吃饭吗？"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150100130.ogg"
    shy "我想可能吃了吧。"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b1
    show yj_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103480.ogg"
    yj "可能是什么啊......"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100140.ogg"
    shy "没有吃过的记忆，不过也没有觉得很饿，所以应该是在无意识的时候吃过了吧。"
    "这种程度的记忆似乎比某位巫女大人还要糟糕啊。"
    hide yj_dsf_b3
    show yj_dsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103490.ogg"
    yj "绝对是没吃吧，要我现在去买点什么吗？"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/150100150.ogg"
    shy "别在意。"
    show yj_dsf_b2 b2 b2_a1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/植澄友加/020103500.ogg"
    yj "肯定会在意的！"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100160.ogg"
    shy "为什么？"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103510.ogg"
    yj "你问为什么......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100170.ogg"
    shy "比起这个，不是有事找我吗？"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/020103520.ogg"
    yj "就是刚才说的这件事......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150100180.ogg"
    shy "我的事情不用操心，你也有自己的生活吧。"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/020103530.ogg"
    yj "......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100190.ogg"
    shy "如果是我太久没回去让你不开心的话，我道歉。"
    show yj_dsf_b1 b1 b1_n2
    play voice "voice/植澄友加/020103540.ogg"
    yj "比起道歉......我还是希望你能多注意下自己的身体。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150100200.ogg"
    shy "我会注意的。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/020103550.ogg"
    yj "......真的吗？"
    play voice "voice/圣护院/150100210.ogg"
    shy "我会努力让这件事不再发生的。"
    "真是无法让人安心的回答......"
    "不过从圣护院小姐就算工作再忙也会挤出时间来见妹妹这一点判断，就可以看出她还是很在乎友加的。"
    "明明上次那么果断地把我拒之门外。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100220.ogg"
    shy "那么轮到下一位吧。"
    hide yj_dsf_b1
    show yj_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103560.ogg"
    yj "欸？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100230.ogg"
    shy "意思就是和你的对话结束了，接下来轮到排在你后面的他了。"
    show yj_dsf_b3 b3 b3_ga1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/植澄友加/020103570.ogg"
    yj "姆......"
    hide yj_dsf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100240.ogg"
    shy "还是说，你只是单纯陪友加来的吗？"
    me01 "其实我也有事想问圣护院主任。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100250.ogg"
    shy "是什么事？"
    pause 1.0 hard
    play sound touch
    $ flcam.move(0, 0, 0)
    scene set only shy_cg one 
    with slowdissolve
    pause 1.0 hard
    me01 "目前研究所这边对这座城市的异常气候是怎么看待的？"
    play voice "voice/圣护院/150100260.ogg"
    shy "为什么要问这个？"
    me01 "只是有些在意而已。"
    play voice "voice/圣护院/150100270.ogg"
    shy "为什么要去在意这些？"
    me01 "我对这座城市的气候很感兴趣，听花山院同学说圣护院小姐是研究所的主任，所以觉得应该没有人比你更加了解这些了。"
    play voice "voice/圣护院/150100280.ogg"
    shy "你是从外地来的吧？"
    me01 "为什么这么肯定？"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/150100290.ogg"
    shy "只是从你的反应推测而已，如果是雪见市的居民是不会在意这些的。"
    me01 "我倒觉得这也不是全部人的想法吧。"
    pause 0.1 hard
    scene set only shy_cg three
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/150100300.ogg"
    shy "不对，就是全部。"
    play voice "voice/圣护院/150100310.ogg"
    shy "这就是雪见市这座城市的独特之处，虽然对你来理解起来或许有些困难。"
    show yj_dsf_b3 b3 b3_ga4 onlayer screens at side_right('yj'), basicfade
    play voice "voice/植澄友加/020103580.ogg"
    yj "姐姐......我的话其实也还是有些在意的。"
    hide yj_dsf_b3
    play voice "voice/圣护院/150100320.ogg"
    shy "你不也是和我一样是从外地搬来的吗，就是这么回事。"
    me01 "......我姑且以前也在这里生活过。"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/150100330.ogg"
    shy "出去又回来了吗......真是少见。"
    me01 "在我小的时候积雪还是很多的，但是现在几乎都快看不到了。"
    me01 "明明雪见市是座常冬的城市。"
    play voice "voice/圣护院/150100340.ogg"
    shy "......"
    me01 "这究竟是怎么一回事呢？"
    play voice "voice/圣护院/150100350.ogg"
    shy "这点我也还不清楚，我们也还在调查中。"
    me01 "有什么进展吗？"
    pause 0.1 hard
    scene set only shy_cg four
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/150100360.ogg"
    shy "你为什么会想知道这些？"
    me01 "刚才说了只是感兴趣使然......"
    play voice "voice/圣护院/150100370.ogg"
    shy "你是想通过我的回答来满足自己的好奇心？"
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900)
    scene set only laboratory inside2 xuejian
    show yj_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    with dissolve
    play voice "voice/植澄友加/020103590.ogg"
    yj "也能顺便满足一下我的好奇心。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_s1 onlayer m1:
        xpos 0.5
    "圣护院小姐叹了口气。"
    "一脸很为难的样子。"
    hide yj_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "如果实在不方便透露的话就当打扰你工作了，抱歉......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100380.ogg"
    shy "不，如果只在你想知道范围内的话，告诉你还是可以的。"
    pause 1.0 hard
    play sound touch
    $ flcam.move(0, 0, 0)
    scene set only shy_cg two
    with slowdissolve
    pause 1.0 hard
    play voice "voice/圣护院/150100390.ogg"
    shy "你似乎也知道了，春天已经有两年没有造访过这座城市了。"
    pause 0.1 hard
    scene set only shy_cg one
    with dissolve
    play voice "voice/圣护院/150100400.ogg"
    shy "但是气温却会变化，所以异常的地方就在于即使是在接近夏天温度的环境下依旧能下雪。"
    play voice "voice/圣护院/150100410.ogg"
    shy "这个现象用以往的气象学是无法解释的，或者说能够解释这个现象的研究者还没有出现。"
    play voice "voice/圣护院/150100420.ogg"
    shy "所以我们的研究员正在尝试通过其他方式调查。"
    me01 "也就是所谓的{encyclopedia=xxqxx}行星气象学{/encyclopedia}吗？"
    play voice "voice/圣护院/150100430.ogg"
    shy "这个词也是从花山院那里听说的吗？"
    me01 "是的。"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/150100440.ogg"
    shy "既然这样的话，后续也去问花山院好了，她也知道行星气象学的含义。"
    "出现了吗，学者眼中的理所当然......"
    me01 "新旧城区都曾发生过异常气候，就比如之前神社发生的那件事。"
    me01 "这些事情发生在身边，大家却没有什么反应吗？"
    pause 0.1 hard
    scene set only shy_cg four
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/圣护院/150100450.ogg"
    shy "......"
    me01 "这也是雪见市的魅力所在吗？"
    play voice "voice/圣护院/150100460.ogg"
    shy "......是啊。"
    me01 "就没有考虑过是其他因素造成的吗？"
    play voice "voice/圣护院/150100470.ogg"
    shy "其他因素，比如说？"
    me01 "比如......人为之类的。"
    play voice "voice/圣护院/150100480.ogg"
    shy "你想说的就这些了吗？"
    me01 "圣护院小姐自己对这件事又是怎么看的呢？"
    pause 0.1 hard
    scene set only shy_cg two
    with dissolve
    play voice "voice/圣护院/150100490.ogg"
    shy "不是说过了吗，我们为了了解异常气候的真相也在从各种观点出发进行调查。"
    play voice "voice/圣护院/150100500.ogg"
    shy "郊外的山上也有气象站，那里的观测数据是主要的证据来源，不过......"
    pause 0.1 hard
    scene set only shy_cg one
    with dissolve
    play voice "voice/圣护院/150100510.ogg"
    shy "调查的范围并不仅限于这座城市，行星探测器送来的数据也是参考之一。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    with dissolve
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/020103600.ogg"
    yj "是类似气象卫星的东西？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/150100520.ogg"
    shy "算是吧，区别就在于不只是用来观测地球，也是在调查宇宙的气候吧。"
    hide yj_dsf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100530.ogg"
    shy "话题就到这里为止吧。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100540.ogg"
    shy "一开始也说了我很忙的，你们差不多也该回去了。"
    me01 "能问最后一个问题吗？"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100550.ogg"
    shy "什么？"
    me01 "花山院同学今后会怎么样呢？"
    play voice "voice/圣护院/150100560.ogg"
    shy "怎么样是指？"
    stop music fadeout 5.0
    me01 "刚才听到的行星探测，以后会有研究员搭乘那个东西前往宇宙吗？"
    me01 "从学校毕业之后，她会为了星天宫的研究......为了人类的未来而踏上前往宇宙的路程吗？"
    me01 "也为了弄清楚这座城市异常气候的秘密。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150100570.ogg"
    shy "......花山院自己会不会同意还不知道，不过她也是候选人之一。"
    me01 "还有其他人选吗？"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150100580.ogg"
    shy "不好意思，在此之上我就不能说了。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100590.ogg"
    shy "姑且也算是机密。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with slowdissolve
    show snow_level1 onlayer fg
    pause 1.0 hard
    "离开研究所已经是傍晚了，不知何时空中也开始飘落雪花。"
    "值得庆幸的是今天的收获还算不少。"
    pause 1.0 hard
    scene set only laboratory evening outside xuejian
    with dissolve
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play music second_102 fadein 3.0 if_changed
    play voice "voice/植澄友加/020103610.ogg"
    yj "姐姐的脸色稍微有些难看。"
    show yj_dsf_b1 b1 b1_s2
    play voice "voice/植澄友加/020103620.ogg"
    yj "虽然工作很重要，但还是希望她能爱惜自己的身体。"
    me01 "至少今天她会好好休息的吧。"
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/020103630.ogg"
    yj "谁知道呢，姐姐只说了会注意而已。"
    play voice "voice/植澄友加/020103640.ogg"
    yj "而且姐姐说的话，也没有什么可信度......"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    me01 "不过在我看来圣护院小姐还是很在乎友加你的。"
    hide yj_dsf_b1
    show yj_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103650.ogg"
    yj "......是吗？"
    me01 "是啊。"
    hide yj_dsf_b3
    show yj_dsf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/020103660.ogg"
    yj "......谢谢你。"
    show yj_dsf_b2 b2 b2_h1
    play voice "voice/植澄友加/020103670.ogg"
    yj "就算只是安慰我也很开心了~"
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowdissolve
    pause 2.0 hard

label day207.bridge_event02:
    $ flcam.move(0, 0, 0)
    scene set only bridge night xuejian
    with dissolve
    show snow_level1 onlayer fg
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    me01 "那么我先回去了，自己一个人回家要多加小心。"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021205280.ogg"
    yj "谢谢你，那么明天见了凉君~"
    me01 "明天见。"
    play sound jiaobu2
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian3
    with dissolve
    pause 3.0 hard
    scene set only bridge night under xuejian
    with dissolve
    pause 3.0 hard
    "还是没能顺利地说上话。"
    "虽然是在对话，但却又不是那样的。"
    "友加与她一直追逐着的背影之间。"
    "还是隔着遥不可及的距离。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021205290.ogg"
    yj "明明接下来还想要继续社团活动的......"
    show yj_dsf_b1 b1 b1_s1
    play voice "voice/植澄友加/021205300.ogg"
    yj "必须要快点换衣服才行。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021205310.ogg"
    yj "我真的很奇怪......"
    show yj_dsf_b2 b2 b2_s1
    play voice "voice/植澄友加/021205330.ogg"
    yj "......"
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowdissolve
    pause 1.0 hard
    "友加将手捂在胸口上。"
    "如果，能把这里正在翻滚着的想法，坦率地传达出去。"
    "如果能够回到过去，把心里的想法告诉她的话......"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only bridge night under xuejian
    with dissolve
    show snow_level1 onlayer fg
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021205340.ogg"
    yj "......凉君。"
    "我该怎么办才好。"
    "唯一能够依靠的身影，此刻也离我远去了。"
    "拐过路口的转角，已经快要消失不见了。"
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_c1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021205350.ogg"
    yj "凉君......"
    stop music fadeout 3.0
    pause 0.5 hard
    hide snow_level1
    play sound rune1
    play music second_123 fadein 3.0 if_changed
    scene set only fight_cg rune1
    with dissolve
    show yj_dsf_b2_rune b2 b2 b2_c1 onlayer m2:
        xpos 0.5 alpha 0.8
    pause 1.5 hard
    play voice "voice/植澄友加/021205360.ogg"
    yj "！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian3
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    "一瞬间，有股奇妙的感觉涌上心头。"
    "努力屏住呼吸，条件反射般地蜷缩起身子。"
    show yj_dsf_b1 b1 b1_s1 onlayer screens at side_right('yj'), basicfade
    play voice "voice/植澄友加/021205370.ogg"
    yj "......"
    hide yj_dsf_b1
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only bridge night under xuejian
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021205380.ogg"
    yj "刚才的是......"
    show yj_dsf_b1 b1 b1_s2
    "像是在要站起来的时候突然失去力气险些跌倒在地的感觉。"
    show yj_dsf_b1 b1 b1_s3
    "又像是刚刚捧起，却又要从指间滑落的沙子那般。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_c1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021205390.ogg"
    yj "......"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard

label day207.laboratory_event02:
    "此刻“他”不在身边。"
    "只能自己去寻找答案了。"
    pause 1.0 hard
    play music second_125 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    with dissolve
    show yj_dsf_b1 b1 b1_s1 onlayer screens at side_right('yj'), basicfade
    play voice "voice/植澄友加/021206020.ogg"
    yj "......"
    hide yj_dsf_b1
    "再次来到研究所。"
    "虽说在这么短的时间里连续打扰两次，但是姐姐还是让自己进来了。"
    "尽管如此对方似乎非常忙的样子，此时也是面对着桌子手指飞快地敲击着键盘。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021206030.ogg"
    yj "果然还是回去比较好......（小声）"
    pause 0.5 hard
    play sound touch
    $ flcam.move(0, 0, 0)
    scene set only shy_cg one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/圣护院/151200790.ogg"
    shy "抱歉，让你久等了。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only laboratory inside2 xuejian
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/圣护院/151200800.ogg"
    shy "说吧，怎么了？"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show yj_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021206040.ogg"
    yj "啊......"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151200810.ogg"
    shy "......"
    "看着妹妹一言不发的模样，圣护院叹了口气。"
    hide yj_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151200820.ogg"
    shy "虽然只是我的猜测......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151200830.ogg"
    shy "友加，你的{rb}灵纹{/rb}{rt}rune{/rt}又开始变得不稳定了对吗？"
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yj_dsf_b2 b2 b2_c1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/植澄友加/021206050.ogg"
    yj "{size=72}！？{/size}" with vpunch
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151200840.ogg"
    shy "果然......是这样吗。"
    show yj_dsf_b2 b2 b2_s3 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/植澄友加/021206060.ogg"
    yj "不、不是的姐姐，我......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151200850.ogg"
    shy "......"
    show yj_dzf_b2 b2 b2_c1
    play voice "voice/植澄友加/021206070.ogg"
    yj "不、不是的，不是这样的，我......"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151200860.ogg"
    shy "......你的报告我已经了解了。"
    show yj_dsf_b2 b2 b2_s3
    play voice "voice/植澄友加/021206080.ogg"
    yj "姐、姐......"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151200870.ogg"
    shy "先回去吧，现在的你更需要好好休息。"
    hide yj_dsf_b2
    show yj_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021206090.ogg"
    yj "姐姐......"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/151200880.ogg"
    shy "抱歉，就像刚才说过的我今晚可能不能回去了。"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    hide yj_dsf_b1
    show yj_dsf_b2 b2 b2_c1 onlayer m2:
        xpos 0.3
    play voice "voice/植澄友加/021206100.ogg"
    yj "姐姐！"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151200890.ogg"
    shy "没关系的。"
    play voice "voice/植澄友加/021206110.ogg"
    yj "......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151200900.ogg"
    shy "什么都不会改变。"
    play voice "voice/植澄友加/021206120.ogg"
    yj "姐、姐？"
    pause 2.0 hard
    scene black
    with slowdissolve
    play sound close_door4
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151200910.ogg"
    shy "抱歉，让你久等了。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show szl_dsf_b3 b3 b3_ga1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/水之濑/051200280.ogg"
    szl "什么叫......让你久等了啊！"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151200920.ogg"
    shy "我早就知道你会来，你也应该有话要对我说吧。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051200290.ogg"
    szl "......"
    show szl_dsf_b2 b2 b2_n4
    play voice "voice/水之濑/051200300.ogg"
    szl "为什么不和妹妹好好解释一下？"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151200930.ogg"
    shy "没想到你一上来说的{rb}要事{/rb}{rt}紧急事项{/rt}会是指这个啊？"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051200310.ogg"
    szl "就在刚刚变成这件事了......"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151200950.ogg"
    shy "友加她似乎也已经出现了初步的症状。"
    play voice "voice/圣护院/151200960.ogg"
    shy "照这个状态继续下去的话，不久她的{rb}灵纹{/rb}{rt}rune{/rt}也会暴走。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/151200980.ogg"
    shy "终究只是一次性的觉醒，对于组织来说有必要控制其危害程度到不至于暴走。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051200320.ogg"
    szl "关于这些事我还是知道的。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151200990.ogg"
    shy "如果结局无法改变，说不说明的话也都是一样的。"
    play voice "voice/圣护院/151201000.ogg"
    shy "就目前情况而言，不知情对她才是最好的状态。"
    show szl_dsf_b2 b2 b2_n4
    play voice "voice/水之濑/051200330.ogg"
    szl "......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/151201010.ogg"
    shy "你看起来对这个回答不是很满意啊。"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051200340.ogg"
    szl "毕竟如果她不是{rb}灵继者{/rb}{rt}elfin{/rt}的话，圣护院主任就不会对她这么关心了不是吗？"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151201020.ogg"
    shy "也许吧......"
    show szl_dsf_b3 b3 b3_ga1
    play voice "voice/水之濑/051200350.ogg"
    szl "......"
    $ flcam.move(-2250, -350, 900, duration=1.5)
    pause 0.5 hard
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051200360.ogg"
    szl "你该不会说刚才表现出来的态度，也是因为提前考虑到这些的缘故吗？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151201030.ogg"
    shy "也不全是，我只是希望即便不再是{rb}灵继者{/rb}{rt}elfin{/rt}的她，也能作为一个普通人好好地生活下去。"
    show szl_dsf_b2 b2 b2_n4
    play voice "voice/水之濑/051200370.ogg"
    szl "为什么你不尝试着去保护她呢？"
    show shy_yjf_b1 b1 b1_n2
    play voice "voice/圣护院/151201040.ogg"
    shy "组织没理由让一个半吊子的{rb}灵继者{/rb}{rt}elfin{/rt}加入进来，你也是知道的。"
    play voice "voice/水之濑/051200380.ogg"
    szl "......"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/051200390.ogg"
    szl "你和你妹妹的关系，真让人难以理解啊。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/151201050.ogg"
    shy "没想到你还想要了解这种事情，真是让我吃惊到了。"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051200400.ogg"
    szl "......偶尔吧。"
    hide szl_dsf_b3
    show szl_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051200410.ogg"
    szl "因为碰巧就看到了姐妹、以及家人之间的对话......"
    play voice "voice/水之濑/051200440.ogg"
    szl "我真是不明白，你真正在乎的到底是什么。"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151201080.ogg"
    shy "关于这一点我也有同感。"
    hide szl_dsf_b1
    hide shy_yjf_b1
    $ flcam.move(0, 500, 1100, duration=1.5, warper='ease_cubic')
    pause 1.0 hard
    play sound touch
    pause 1.0 hard
    "圣护院重新坐回了椅子上。"
    $ flcam.move(0, -300, 900, duration=1.5)
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/151201090.ogg"
    shy "只是......"
    show shy_yjf_b1 b1 b1_s3
    play voice "voice/圣护院/151201100.ogg"
    shy "无论事态如何发展，我也有绝对不会动摇的东西......"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show szl_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/051200450.ogg"
    szl "......"
    show shy_yjf_b1 b1 b1_s4
    play voice "voice/圣护院/151201110.ogg"
    shy "怎么了？不是要走了吗？"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051200460.ogg"
    szl "我走了，那么再见。"
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_s1 at walkout_l(0.3)
    pause 0.5 hard
    play sound close_door4
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 2.0 hard
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/151201130.ogg"
    shy "......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day207.bridge_event03:
    play music second_123 fadein 3.0 if_changed
    play sound jiaobu3
    $ flcam.move(0, 0, 0)
    scene set only bridge night under xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021206130.ogg"
    yj "哈......哈......哈......"
    show yj_dsf_b2 b2 b2_c1 onlayer screens at side_right('yj'), basicfade
    play voice "voice/植澄友加/021206140.ogg"
    yj "就算是这样......就算是这样！"
    hide yj_dsf_b2
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowdissolve
    pause 1.0 hard
    "明明自己都已经变成这样子了，还是得不到姐姐的关心吗？"
    "真的已经，无法回到从前了吗？"
    "可为什么姐姐却说“什么都不会改变”呢？"
    "明明一切都已经改变了。"
    "明明已经不再是从前的样子了！"
    "姐姐这个大骗子！"
    "凉君。"
    "对不起。"
    "我果然还是没有办法像你说的那样直率地面对一切。"
    "姐姐的冷漠把我的笑容也一并夺走了。"
    "明明只想要像过去那样陪在她身边，哪怕只是一起吃一顿饭。"
    "明明......只要这样就足够了。"
    "明明......就只剩下这些了。"
    "但是我却已经。"
    "什么都感觉不到了。"
    "我已经......快要听不见她的声音了。"
    pause 1.0 hard
    scene set only sky night xuejian3
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021206150.ogg"
    yj "快停下来啊，我的脑袋！"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day207.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street night road1 xuejian
    with dissolve
    show snow_level1 onlayer fg
    pause 1.0 hard
    me01 "总觉得今天的友加有点不太一样。"
    me01 "似乎有什么事情瞒着我似的。"
    me01 "明明只要说出来我也会想办法帮忙的。"
    play voice "voice/希菲尔/001200010.ogg"
    stranger "......能这样想就足够了。"
    pause 1.0 hard
    play music second_103 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001200020.ogg"
    xfe "被听到心声会觉得害羞吗？"
    me01 "如果对方是希菲尔的话就没问题。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001200030.ogg"
    xfe "那就不说“对不起”了哟~"
    me01 "希菲尔还真是一点都没变。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1  onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001200040.ogg"
    xfe "希菲尔，一直都没变吗？"
    me01 "是啊，对我来说希菲尔一直都是那个希菲尔。"
    me01 "能随时让我坦诚地倾诉烦恼的人。"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001200050.ogg"
    xfe "可凉君却改变了。"
    me01 "或许吧，亦或者说......确实是这样的。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001200070.ogg"
    xfe "这样也挺好的。"
    me01 "希菲尔......"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001200080.ogg"
    xfe "就算是那样，只要继续向前迈进就行了。"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/001200090.ogg"
    xfe "凉君的身边已经......不只是希菲尔一人了。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001200100.ogg"
    xfe "有家人在。"
    play voice "voice/希菲尔/001200110.ogg"
    xfe "有朋友在。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001200120.ogg"
    xfe "对希菲尔来说，凉君是很重要的朋友。"
    play voice "voice/希菲尔/001200130.ogg"
    xfe "所以希菲尔多少也有点明白这种感觉了。"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/001200140.ogg"
    xfe "虽然希菲尔心中的凉君一直都没有改变。"
    play voice "voice/希菲尔/001200150.ogg"
    xfe "想要一起玩耍的心情，没有改变。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001200160.ogg"
    xfe "两人留下的足迹，虽然希望它永远都不消失。"
    play voice "voice/希菲尔/001200170.ogg"
    show ts_xfe_yjz_b1 b1 b1_s1
    xfe "但是，现在的雪却无法堆积起来。"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/001200180.ogg"
    xfe "所以希菲尔也知道，改变是必须的。"
    me01 "这究竟是......"
    "什么意思？"
    play voice "voice/希菲尔/001200200.ogg"
    xfe "大家都在为凉君你加油。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001200210.ogg"
    xfe "希菲尔也是一样的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001200240.ogg"
    xfe "所以一路顺风，凉君。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001200250.ogg"
    xfe "和希菲尔一起无法做到的事，和她们一起的话......一定可以的。"
    play voice "voice/希菲尔/001200260.ogg"
    xfe "只要能让两人的足迹继续延伸下去的话......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_h1
    play voice "voice/希菲尔/001200270.ogg"
    xfe "就算迎来春天，也不再是孤单一人了——"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    play sound xiaoshi_1
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street night road1 xuejian
    with dissolve
    pause 1.0 hard
    "雪停了，随之一同消失的还有希菲尔的身影。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene set only sky night xuejian2
    with dissolve
    pause 1.0 hard    
    me01 "谢谢你希菲尔，我想我知道该怎么做了。"
    pause 0.5 hard
    scene black 
    with slowerdissolve

label day207.bridge_event04:
    play music second_129 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge night under xuejian
    with slowdissolve
    pause 2.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021207420.ogg"
    yj "即使是现在......还是很想见到凉君。"
    play voice "voice/植澄友加/021207430.ogg"
    yj "翔子说过的，这种心情就叫做“喜欢”。"
    play voice "voice/植澄友加/021207410.ogg"
    yj "对不起......"
    me01 "友加？"
    pause 1.0 hard
    play sound touch
    scene set only bridge night under xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5 alpha 0.0 ypos 1.0
        parallel:
            linear 1.0 ypos 0.95
        parallel:
            linear 1.0 alpha 1.0
    pause 0.5 hard
    play voice "voice/植澄友加/021207440.ogg"
    yj "......"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b2 b2 b2_s2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/021207450.ogg"
    yj "......凉、凉君？"
    me01 "那个，我有些话想对你说。"
    hide yj_dzf_b2 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_s2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021207460.ogg"
    yj "啊......嗯。"
    me01 "总觉得放心不下就回来看看，你果然还在这里。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_c1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207470.ogg"
    yj "......"
    me01 "有什么烦恼吗？"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207480.ogg"
    yj "嗯。"
    me01 "可以坐在你的旁边吗？"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207490.ogg"
    yj "嗯。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    with dissolve
    pause 2.0 hard
    scene set only bridge night under xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207500.ogg"
    yj "那、那个，凉君......"
    me01 "怎么了？"
    show yj_dzf_b2 b2 b2_s3
    play voice "voice/植澄友加/021207550.ogg"
    yj "......"
    me01 "话说回来，没想到友加的姐姐这么忙还会抽空给我们见面的机会。"
    show yj_dzf_b2 b2 b2_s2
    play voice "voice/植澄友加/021207570.ogg"
    yj "嗯......说实话我也吓了一跳。"
    "也许就如希菲尔所说的那样，我们一直都被身边的朋友和家人包容着。"
    "没有察觉并不代表着不存在。"
    "我们一直都是被偏爱着的，被同样深爱着的那一方。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    me01 "现在才问有些抱歉，友加你不会冷吗？"
    show yj_dzf_b1 b1 b1_s2
    play voice "voice/植澄友加/021207590.ogg"
    yj "不会的，虽然刚才稍微下了点雪。"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b2 b2 b2_ga4 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/021207600.ogg"
    yj "但现在已经......没关系了。"
    me01 "真的吗？"
    show yj_dzf_b2 b2 b2_s2
    play voice "voice/植澄友加/021207610.ogg"
    yj "嗯。"
    "面对再一次陷入沉默的友加，我没有继续抛出话题。"
    "而是静静地注视着眼前这个女孩。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show yj_dzf_b2 b2 b2_sp1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/021207630.ogg"
    yj "啊......"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    "就在这时，我们的目光交汇了。"
    "友加慌张地移开了视线。"
    me01 "友加？"
    show yj_dzf_b1 b1 b1_sp1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/021207640.ogg"
    yj "呀啊！？"
    "我下意识地伸手触碰了友加的肩膀。"
    "也许是被我的举动吓了一跳，友加下意识地躲开了。"
    me01 "这里的变化还真是挺大的。"
    me01 "和之前我来的时候完全不一样了。"
    hide yj_dzf_b1
    show yj_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207650.ogg"
    yj "嗯、嗯......"
    me01 "这种时候说这些是不是有点不合时宜？"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_ga4 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207660.ogg"
    yj "接着说吧凉君。"
    me01 "但是。"
    hide yj_dzf_b2
    show yj_dzf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207670.ogg"
    yj "如果你不介意......讲给我听的话。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    with dissolve
    pause 1.0 hard
    me01 "过去的我跟随父亲去过各种各样的城市。"
    me01 "也是因为他工作的关系我一直没有时间和父亲说过几句话。"
    me01 "加上那时的我身边也几乎没有能够说上话的朋友。"
    me01 "即使有幸交到了朋友，也会在不久后的某一天迎来离别。"
    me01 "已经习惯这般生活的我，也逐渐改变了。"
    me01 "我开始享受独自一人的日子。一个人的午饭，一个人的街道，还有......一个人的家。"
    me01 "与其烦恼着离别，不如从一开始就不接受，也许这样对谁都是更好的结局。"
    me01 "当时的我就是这么想的，就连对父亲他也是......"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only bridge night under xuejian
    show yj_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    "说到这里，我注意到身旁友加的细微变化。"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    "仿佛是触碰到了什么开关一般。"
    "她脸上的表情开始变得痛苦起来。"
    show yj_dzf_b2 b2 b2_s3
    play voice "voice/植澄友加/021207700.ogg"
    yj "也就是说......"
    play music second_123 fadein 3.0 if_changed
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207710.ogg"
    yj "凉君你也是因为家人工作的关系，才选择留在雪见市的。"
    play voice "voice/植澄友加/021207720.ogg"
    yj "那如果......这个理由不见了的话。"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207730.ogg"
    yj "如果连最初留在雪见市的{rb}理由{/rb}{rt}家人{/rt}也消失的话......"
    me01 "......友加？"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    nvl clear
    play voice "voice/植澄友加/021207740.ogg"
    pcenter "就再也回不去了......彻底地、消失。"
    pause 1.0 hard

label day207.battle_yj:
    $ flcam.move(0, -300, 900)
    scene set only bridge night under xuejian
    show yj_dzf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/植澄友加/021207750.ogg"
    yj "......"
    me01 "等一下友加，不是你想的那样。"
    me01 "我说的这些都是因为......"
    show yj_dzf_b2 b2 b2_c1
    play voice "voice/植澄友加/021207760.ogg"
    yj "怎、怎么这样......"
    pause 0.5 hard
    play sound rune1
    show wflash onlayer texture
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide yj_dzf_b2
    show yj_dzf_b2_rune b2 b2 b2_c1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207770.ogg"
    yj "{size=72}！！！{/size}"
    stop music fadeout 5.0
    play sound rune2
    pause 1.0 hard
    me01 "友加？！"
    $ flcam.move(0, -350, 1100, duration=1.0)
    pause 0.5 hard
    hide yj_dzf_b2_rune
    show yj_dzf_b1_rune b1 b1 b1_c1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021207780.ogg"
    yj "不、不行！！！"
    pause 1.0 hard
    play sound rune2
    pause 1.0 hard
    $ flcam.move(0, -1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 5.0 hard
    play music second_138 fadein 3.0 if_changed
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg rune1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021207790.ogg"
    yj "{size=72}不要啊啊啊！！{/size}"
    "一瞬间狂风大作。"
    "和在神社的时候一样，友加的身边也开始产生不稳定的气流。"
    me01 "友加，快冷静下来！"
    me01 "我想说的不是这些，是你误会了......"
    play voice "voice/植澄友加/021207800.ogg"
    yj "呜、呜呜呜......"
    "灵力构筑起的漩涡挡在了我们之间。"
    "任凭我怎么呼喊都无法将意识传达给对方。"
    "朝内和朝外的两股灵力相互撞击，产生紊乱的气流。"
    "仿佛就要连同空气一起撕裂一般。"
    play voice "voice/植澄友加/021207810.ogg"
    yj "不要、我不要这样......呜、呜呜呜呜。"
    "与上次的情况有所不同，这一次我能清楚地听见对方说的话。"
    "虽然尝试像上次那般使用{rb}念动力场{/rb}{rt}psychokinesis{/rt}平息风暴，但考虑到周遭的空气都被吸附在了友加的身边。"
    "冒然凝聚念波屏障显然是十分危险的事情。"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    "是我刚刚的话让友加的情绪有了波动。"
    "那么能够破解这场危机的关键一定就在那些话中。"
    "但是......"
    me01 "完全没有头绪！"
    me01 "总之在找到答案之前必须想办法让风暴蔓延的速度停下来。"
    "人在最无助的时候往往会不自觉地依靠身边最值得信赖的人。"
    "然而即便是在内心饱受煎熬、快要崩溃的情况下，友加依旧选择一个人留在河滩。"
    "那么对于现在的她而言，那位最有可能依靠的人一定已经不在她的身边了。"
    "这么想的话......"
    "现在能够成为她依靠的，就只剩下我了。"
    me01 "对不起友加！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only yj_cg rune2
    with slowdissolve
    pause 0.5 hard
    play voice "voice/植澄友加/021207820.ogg"
    yj "......"
    me01 "虽然知道可能会因此而被你讨厌。"
    me01 "虽然知道自己可能就要犯下了无可挽回的错误。"
    me01 "但是如果，我是说如果。"
    me01 "还有一丝可能性的话。"
    me01 "请让我成为你的依靠吧！"
    window mode thought
    me01 "前方将进入战斗阶段，每次战斗前建议提前保存以免翻车哟~"
    window mode thought
    me01 "右键SAVE或者右下角的快捷菜单都可以进行保存。"
    stop music fadeout 5.0
    pause 2.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg bridge
    play music "<to 39.548 loop 0>music/in_battle0.mp3" fadein 3.0 if_changed
    with dissolve
    python:
        # 角色装备为随机普通6件，等级3
        yj_role_mirror.equip_experience = 99999999
        for cate in yj_role_mirror.outfits:
            enemy_outfits = [outfit for outfit in outfit_list if ("_01" in outfit.objectname and outfit.category == cate)]
            sample_index = renpy.random.randint(0, len(enemy_outfits)-1)
            sample_outfit = enemy_outfits[sample_index]
            sample_outfit.init_params()
            for xi in range(3):
                sample_outfit.level_up(yj_role_mirror, 100)
            sample_outfit.enemy_equip_on(yj_role_mirror)

        # 替换雷亚普攻为雷属性
        for role in copy(local_config.party):
            if role.name == "雷亚":
                temp_selected_skills, temp_selected_skills_v2 = role.skills, role.skills_v2
                before_battle_general_attack = [s for s in temp_selected_skills if s.category == "General_attack"][0]
                before_battle_general_attack_v2 = [s for s in temp_selected_skills_v2 if s.category == "General_attack"][0]
                now_battle_general_attack = copy(getattr(store, "psychokinesis-light"))
                for xi in range(before_battle_general_attack.level - 1):
                    now_battle_general_attack.level_change(now_battle_general_attack.level + 1)
                role.skills = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills]
                role.base_skills = role.skills
                role.skills_v2 = [s if s.category != "General_attack" else now_battle_general_attack for s in role.skills_v2]
                role.base_skills_v2 = role.skills_v2
            # 队伍数据转移
            new_role_obj = getattr(store, role.objectname)
            new_role_obj.battle_params_match(role)
            local_config.party.remove(role)
            local_config.party.append(new_role_obj)

        # 初始化友加属性
        if len(local_config.party) <= 2:
            yj_role.max_hp = 12000
        else:
            yj_role.max_hp = 16000

        yj_role.hp = 1
        yj_role.mp = 0

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    pause 0.25
    call battle(boss=yj_role_mirror, 
                boss_hp_plus=99999,
                side_enemy=[], 
                side_hp_plus=0,
                level=20,
                boss_first=True, 
                win_condition='sp_healing_yj_role', 
                stay_turn=0, 
                inside_label="inside_battle4", 
                mission_type="normal", 
                treasures={
                    "eggs": (3, 0.6),
                    "mana_eggs": (2, 0.4),
                    "soul_piece": (5, 0.3),
                    "soul_raise": (5, 0.3),
                    "water_break_small": (5, 0.3),
                    "water_break_large": (2, 0.3)
                })

    if _return == "win":
        "战斗胜利！"
        python:
            for role in local_config.party:
                if role.name == "雷亚":
                    role.skills = [s if s.category != "General_attack" else before_battle_general_attack for s in role.skills]
                    role.base_skills = role.skills
                    role.skills_v2 = [s if s.category != "General_attack" else before_battle_general_attack_v2 for s in role.skills_v2]
                    role.base_skills_v2 = role.skills_v2
            if "yj_role" not in local_config.role_pool:
                local_config.role_pool.add("yj_role")
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        stop music fadeout 5.0
    else:
        jump battle_end
    jump day207.after_battle_yj

label day207.after_battle_yj:
    scene black
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    play music second_138 fadein 3.0 if_changed
    scene set only yj_cg rune3
    $ flcam.move(-1600, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021207830.ogg"
    yj "!"
    me01 "抱歉......但我真的没有别的办法了。"
    pause 0.1 hard
    scene set only yj_cg rune2
    play ambience1 strong_wind fadein 3.0
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021207860.ogg"
    yj "......凉君。"
    pause 0.1 hard
    scene set only yj_cg rune4
    with dissolve
    play voice "voice/植澄友加/021207870.ogg"
    yj "没事的、没事的......"
    play voice "voice/植澄友加/021207880.ogg"
    yj "已经......没事了。"
    me01 "想好要怎么做了吗？"
    play voice "voice/植澄友加/021207890.ogg"
    yj "因为如果不那样的话，马上又会消失的。"
    play voice "voice/植澄友加/021207900.ogg"
    yj "就像我的{rb}灵纹{/rb}{rt}rune{/rt}一样。"
    play voice "voice/植澄友加/021207910.ogg"
    yj "虽然早就知道会是这样的结果......"
    play voice "voice/植澄友加/021207920.ogg"
    yj "我可能已经不能像凉君一样，继续作一名{rb}灵继者{/rb}{rt}elfin{/rt}了。"
    play voice "voice/植澄友加/021207930.ogg"
    yj "究竟是从什么时候开始的呢，回忆逐渐开始变得模糊起来。"
    "胸口突然传来一股炙热的灼烧感。"
    "友加体内的灵力正在疯狂地倾斜而出。"
    "灵压之大甚至一度要将我推开。"
    me01 "友加你莫非......"
    me01 "是为了得到你姐姐的认可，才强迫自己成为一名{rb}灵继者{/rb}{rt}elfin{/rt}的吗？"
    pause 0.1 hard
    scene set only yj_cg rune5
    $ flcam.move(-3200, -2800, 900, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021207940.ogg"
    yj "{size=72}唔？！{/size}"
    "我再一次抱住了她。"
    "用残存的体力发动{rb}念动力场{/rb}{rt}psychokinesis{/rt}封锁住喷涌而出的灵力。"
    me01 "听我说友加。"
    me01 "如果你相信{rb}灵纹{/rb}{rt}rune{/rt}是你和姐姐维系的羁绊。"
    me01 "无论用什么方法都行，给我好好守住它们啊！"
    me01 "再也不要......轻易放手了。"
    pause 0.5 hard
    show wflash onlayer texture
    with vpunch
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    "如果换做过去的我......是无论如何也说不出这样的话吧。"
    "毕竟羁绊这种东西就和朋友一样，是有可能会在未来的某一天演变成诀别悲痛的产物。"
    "所以才一直觉得回忆是不需要的东西。"
    pause 0.5 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    "可是现在......却无论如何都想替眼前的女孩守住那份属于她的回忆。"
    "真是讽刺啊......但同时也是多么令人开心。"
    "也许正如希菲尔说的那样，我已经改变了。"
    "如果灵纹也有生命的话，那一定是诞生自我们内心最真实的情感。"
    "不安、暴怒、压抑、悲伤，一切的负面情绪最终导致了灵力的暴走。"
    "人们总是喜欢将罪恶强加给那些所谓的“外因”，却忽视了其背后真正潜藏的根本。"
    "最应该研究的才不是什么异常气候、也不是宇宙真理，而是人心。"
    "或许就连这场温柔的雪，也是发自某人“内心”的写照也说不定。"
    pause 1.0 hard
    $ flcam.move(-1600, -1400, 450)
    scene set only yj_cg rune5
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021207950.ogg"
    yj "......"
    "时间一分一秒地过去，暴走的灵力丝毫没有减弱的趋势。"
    "而相对的我的体力却已经开始渐渐支撑不住了。"
    "即使是这样我依旧没有放开手，继续用我仅存的灵力支撑着友加。"
    stop ambience1 fadeout 5.0
    pause 0.1 hard
    scene set only yj_cg rune4
    with dissolve
    nvl clear
    play voice "voice/植澄友加/021207980.ogg"
    pcenter "......足够了。"
    pause 1.0 hard
    scene white 
    with in2out_02
    pause 1.0 hard
    "友加的眼角渗出了泪水。"
    "这是我第一次看到这位坚强开朗的女孩流泪。"
    "但是她的嘴角却仍保持着微笑。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day207.laboratory_event03:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    play music second_102 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/琉璃/040104730.ogg"
    liuli "那个......圣护院小姐。"
    show liuli_dsf_b1 b1 b1_sp1
    play voice "voice/琉璃/040104740.ogg"
    liuli "......在打电话吗？"
    hide liuli_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show shy_yjf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/150100600.ogg"
    shy "那就拜托你了水之濑，最好现在就赶往现场。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150100610.ogg"
    shy "只能祈祷天命的眷顾了吧。"
    play sound phone2
    pause 1.0 hard
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150100620.ogg"
    shy "......没想到{rb}灵继者{/rb}{rt}elfin{/rt}会接二连三地暴走。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/040104750.ogg"
    liuli "圣护院小姐。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100630.ogg"
    shy "怎么了，原来你在啊。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/040104760.ogg"
    liuli "发生什么事了吗？"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150100640.ogg"
    shy "没什么，比起这个你怎么会在这里，不是去神社了吗？"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/040104770.ogg"
    liuli "那个，关于您妹妹的事......我稍微有些话想说。"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150100650.ogg"
    shy "......"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.3
    play voice "voice/琉璃/040104780.ogg"
    liuli "有件事我想要拜托圣护院小姐。"
    stop music fadeout 5.0
    pause 1.0 ahrd
    scene black 
    with slowerdissolve
    pause 1.0 hard

label day207.bridge_event06:
    $ flcam.move(0, 0, 0)
    play music second_122 fadein 3.0 if_changed
    scene set only bridge night xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dsf_knife_b2 b2 b2_n4 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/水之濑/050101490.ogg"
    szl "......又来迟了一步，真是的。"
    show szl_dsf_knife_b2 b2 b2_s1
    play voice "voice/水之濑/050101500.ogg"
    szl "你真的总会给我添麻烦。"
    show szl_dsf_knife_b2 b2 b2_n2
    play voice "voice/水之濑/050101510.ogg"
    szl "......虽然某种意义上也许交给他也不算坏。"
    play voice "voice/水之濑/050101520.ogg"
    szl "没想到这么快就又发生第二起暴走。"
    hide szl_dsf_knife_b2
    show szl_dsf_knife_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101530.ogg"
    szl "这次是{rb}念动力场{/rb}{rt}psychokinesis{/rt}吗。"
    play voice "voice/水之濑/050101540.ogg"
    szl "不过我觉得你最值得称赞的，是明明和自己没有关系，却还总要掺和进来的勇气。"
    stop music fadeout 5.0
    hide szl_dsf_knife_b1
    show szl_dsf_knife_b2 b2 b2_sp2 onlayer m2:
        xpos 0.5
    pause 0.5 hard
    play voice "voice/水之濑/050101550.ogg"
    szl "......欸？"
    play voice "voice/水之濑/050101560.ogg"
    szl "那孩子是......植澄友加？"
    play music second_123 fadein 3.0 if_changed
    show szl_dsf_knife_b2 b2 b2_n3
    play voice "voice/水之濑/050101570.ogg"
    szl "骗人的吧......竟然是圣护院主任的妹妹。"
    show szl_dsf_knife_b2 b2 b2_s1
    play voice "voice/水之濑/050101580.ogg"
    szl "依然能够感受到她的{rb}灵纹{/rb}{rt}rune{/rt}。"
    play voice "voice/水之濑/050101590.ogg"
    szl "和一诚小桃那时不同，暴走之后没有马上丧失灵力吗。"
    show szl_dsf_knife_b2 b2 b2_n3
    play voice "voice/水之濑/050101600.ogg"
    szl "不是一次性的暴走，而是......真正地觉醒。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dsf_knife_b2
    show szl_dsf_knife_b1 b1 b1_a2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101610.ogg"
    szl "{rb}灵继者{/rb}{rt}elfin{/rt}的诞生——"
    hide szl_dsf_knife_b1
    show szl_dsf_knife_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101620.ogg"
    szl "呐......圣护院主任。"
    show szl_dsf_knife_b2 b2 b2_s1
    play voice "voice/水之濑/050101630.ogg"
    szl "这次，你会怎么做呢......"
    hide szl_dsf_knife_b2
    show szl_dsf_knife_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101640.ogg"
    szl "要连自己的妹妹，也像我一样地利用吗？"
    hide szl_dsf_knife_b1
    show szl_dsf_knife_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/050101650.ogg"
    szl "作为你的棋子。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard

label day207.bridge_event05:
    $ flcam.move(0, 0, 0)
    play music second_134 fadein 3.0 if_changed
    pause 1.0 hard
    "时间仿佛在这一刻停止了。"
    "原本已经濒临奔溃的意识再一次苏醒了过来。"
    "还不能放弃，还不是放弃的时候。"
    "不能让凉君的努力白费。"
    "让他担心了......明明是自己懦弱所导致的后果，却被一个原本毫不相干的人给拯救了。"
    "那么这一次，我也得靠自己的力量守护这份回忆了。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021208000.ogg"
    yj "凉君也一定把这当作是重要的事情对待了。"
    play voice "voice/植澄友加/021208010.ogg"
    yj "是啊，我们都是一样的。"
    pause 1.0 hard
    scene set only yj_cg rune6
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021208020.ogg"
    yj "凉君......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    with slowdissolve
    pause 1.0 hard
    play voice "voice/植澄友加/021208050.ogg"
    yj "凉君。"
    pause 1.0 hard
    play music second_131 fadein 3.0 if_changed
    scene set only bridge night under xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show yj_dzf_b3 b3 b3_h2 onlayer m2:
        xpos 0.5
    me01 "友加，你没事吧？"
    hide yj_dzf_b3
    show yj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208060.ogg"
    yj "对不起凉君，让你卷入这件事。"
    show yj_dzf_b1 b1 b1_s1
    play voice "voice/植澄友加/021208070.ogg"
    yj "但是......已经没关系了。"
    me01 "真的没有问题吗？"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208080.ogg"
    yj "嗯。"
    me01 "所以你已经下定决心了吧？"
    play voice "voice/植澄友加/021208090.ogg"
    yj "嗯......"
    play sound touch
    $ flcam.move(0, -300, 1000, duration=1.5)
    hide yj_dzf_b2 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_sp1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    me01 "现在就出发吧！"
    play voice "voice/植澄友加/021208100.ogg"
    yj "......欸？"
    me01 "现在立刻就去把你的想法告诉她吧。"
    me01 "无论那个人是怎么看待你的，我始终都会站在友加这边的。"
    play voice "voice/植澄友加/021208110.ogg"
    yj "......"
    me01 "难不成你刚刚才说的“决心”其实只是借口而已吗？"
    show yj_dzf_b3 b3 b3_ga1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021208120.ogg"
    yj "不不不不不不不是这样的！"
    hide yj_dzf_b3
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208140.ogg"
    yj "我终于知道了......这是什么样的心情。"
    play voice "voice/植澄友加/021208160.ogg"
    yj "一直以来我只会害怕地选择逃避。"
    hide yj_dzf_b1 with None
    pause 0.1 hard
    show yj_dzf_b3 b3 b3_c2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/植澄友加/021208130.ogg"
    yj "但果然还是喜欢着的！"
    me01 "果然啊。"
    hide yj_dzf_b1
    show yj_dzf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208190.ogg"
    yj "......凉、凉君？"
    me01 "出发吧，现在就去把谱写你人生悲剧的家伙好好地修理一顿。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208200.ogg"
    yj "对、对不起，你说的话好难懂。"
    me01 "给我反抗啊，自己的命运。"
    show yj_dzf_b2 b2 b2_s1
    play voice "voice/植澄友加/021208210.ogg"
    yj "从没想过会在这种地方被说教......"
    me01 "噗哈哈哈~"
    show yj_dzf_b2 b2 b2_s2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/植澄友加/021208220.ogg"
    yj "不要笑我啦~"
    me01 "抱歉抱歉，不过......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    with dissolve
    pause 1.0 hard
    "我抬头望向星空。"
    "{rb}灵纹{/rb}{rt}rune{/rt}的躁动一定就和她的心情是一样的。"
    "不想要失去，却又不得不面对失去的痛苦。"
    "想要逃走的不仅仅是灵纹，也是你的内心。"
    "这一点我可是比任何人都要清楚。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only bridge night under xuejian
    show yj_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/植澄友加/021208230.ogg"
    yj "当然这里面也有姐姐的问题。"
    hide yj_dzf_b1
    show yj_dzf_b3 b3 b3_c2 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208240.ogg"
    yj "现在注意到的时候......总觉得越来越难为情了~"
    show yj_dzf_b3 b3 b3_n3
    play voice "voice/植澄友加/021208270.ogg"
    yj "回过神来的时候，内心就觉得好像被什么东西填满了一样。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208280.ogg"
    yj "明明刚才还很害怕的。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208290.ogg"
    yj "就像凉君说的那样，如果{rb}灵纹{/rb}{rt}rune{/rt}消失的话，那么和某人的羁绊也就不复存在了。"
    hide yj_dzf_b1
    show yj_dzf_b3 b3 b3_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208310.ogg"
    yj "凉君也愿意和我一起分享这样的感觉。"
    play voice "voice/植澄友加/021208320.ogg"
    yj "那时我在想我们其实是一样的。"
    hide yj_dzf_b3
    show yj_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208330.ogg"
    yj "所以才觉得是时候放弃执着于{rb}灵纹{/rb}{rt}rune{/rt}本身了。"
    hide yj_dzf_b2
    show yj_dzf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208340.ogg"
    yj "就算不再是{rb}灵继者{/rb}{rt}elfin{/rt}。"
    hide yj_dzf_b1
    show yj_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/植澄友加/021208360.ogg"
    yj "我也有必须要传达的感情。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day207.laboratory_event04:
    $ flcam.move(0, 0, 0)
    scene set only laboratory inside2 xuejian
    $ flcam.move(-4500, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102140.ogg"
    szl "圣护院主任。"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/150101160.ogg"
    shy "还以为是谁呢，原来是水之濑啊。有什么要向我汇报的吗？"
    play music second_123 fadein 3.0 if_changed
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/050102150.ogg"
    szl "没什么，只是路过所以绕道过来一下。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150101170.ogg"
    shy "你家虽然在新城区但似乎离研究所也有一段距离吧。"
    show szl_dsf_b2 b2 b2_sp1
    play voice "voice/水之濑/050102160.ogg"
    szl "主任你这是要回去？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101180.ogg"
    shy "看就知道了吧，我正在做回家的准备。"
    play voice "voice/水之濑/050102170.ogg"
    szl "真是少见啊，这么早回家......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101190.ogg"
    shy "已经很晚了，不如说这才是正常的举动吧。"
    show szl_dsf_b2 b2 b2_n4
    play voice "voice/水之濑/050102180.ogg"
    szl "所以说这很不正常。因为最近你好像都是住在研究所的。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102190.ogg"
    szl "发生在神社的龙卷风，还有河滩边发生的风暴......明明要调查的事情还有很多。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101200.ogg"
    shy "也是呢，但是现在我的工作是集中观察友加的身体情况。"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102200.ogg"
    szl "我可以理解成是你在担心妹妹的安危吗？"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101210.ogg"
    shy "你好像话里有话啊......"
    show szl_dsf_b2 b2 b2_n4
    play voice "voice/水之濑/050102210.ogg"
    szl "没有那种事。"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101220.ogg"
    shy "友加现在也是重要的研究素材，我会担心也是当然的吧。"
    $ flcam.move(-2500, -350, 900, duration=1.5)
    pause 0.5 hard
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102220.ogg"
    szl "是吗......也就是说你要像对待我一样，把自己妹妹也当成棋子利用吧。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101230.ogg"
    shy "我倒是没想过要把你当成棋子。"
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_n3 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102230.ogg"
    szl "谁知道呢。"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150101240.ogg"
    shy "你会这么想我也是没办法的。毕竟如果友加的能力能够被“利用”的话，组织那边也打算和你一样好好地“利用”一番。"
    hide szl_dsf_b3
    show szl_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102240.ogg"
    szl "看来就算是妹妹，也不会特殊对待呢......"
    show shy_yjf_b1 b1 b1_sp1
    play voice "voice/圣护院/150101250.ogg"
    shy "有什么问题吗？"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102250.ogg"
    szl "没有，不如说是有点安心了。"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101260.ogg"
    shy "听起来都只有讽刺我的话。你来找我就只是为了说友加的事吗？"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/050102260.ogg"
    szl "是啊，这一点我还是比较在意的。如果你的妹妹能够熟练使用{rb}灵纹{/rb}{rt}rune{/rt}的话，是不是也会考虑把她拉拢进星天宫研究所？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101270.ogg"
    shy "这个问题我之前也回答过你了吧。"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/050102270.ogg"
    szl "......"
    show shy_yjf_b1 b1 b1_n3
    play voice "voice/圣护院/150101280.ogg"
    shy "现在首要的任务是观察友加的身体状况，有必要寻找让{rb}灵纹{/rb}{rt}rune{/rt}变稳定的方法。"
    play voice "voice/圣护院/150101290.ogg"
    shy "毕竟在日常生活中，{rb}灵纹{/rb}{rt}rune{/rt}完全消失的先例也是真实存在的。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102280.ogg"
    szl "就算{rb}灵纹{/rb}{rt}rune{/rt}能够留下来，忘记使用方法之类的事情也是司空见惯的。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101300.ogg"
    shy "所以现在我必须去确认友加的情况。"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_n4 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102290.ogg"
    szl "这一切都是为了星天宫？"
    show shy_yjf_b1 b1 b1_n1
    play voice "voice/圣护院/150101310.ogg"
    shy "是的。"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/050102300.ogg"
    szl "因为这说不定就是解开雪见市异常气候的关键？"
    show shy_yjf_b1 b1 b1_s1
    play voice "voice/圣护院/150101320.ogg"
    shy "是啊。"
    show szl_dsf_b2 b2 b2_s2
    play voice "voice/水之濑/050102310.ogg"
    szl "你果然还是希望自己的妹妹能继续当{rb}灵继者{/rb}{rt}elfin{/rt}吗......"
    show shy_yjf_b1 b1 b1_h1
    play voice "voice/圣护院/150101330.ogg"
    shy "那是自然，这样一来我们的研究也能够越来越顺利。"
    show shy_yjf_b1 b1 b1_n3
    play voice "voice/圣护院/150101340.ogg"
    shy "以调查异常气候为目的就是这座星天宫研究所的宗旨。"
    show szl_dsf_b2 b2 b2_n4
    play voice "voice/水之濑/050102320.ogg"
    szl "这也是为什么组织会将这次行动用北欧神话的方式命名为{encyclopedia=fbezd}芬布尔之冬{/encyclopedia}吧。"
    hide shy_yjf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/050102330.ogg"
    szl "被天使召唤的......人类勇士。"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/水之濑/050102340.ogg"
    szl "这么夸张的设定，究竟是谁想出来的......"
    $ flcam.move(-2250, -350, 750, duration=1.5)
    show shy_yjf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/圣护院/150101350.ogg"
    shy "是我们的上司，也是这座研究所的创始人。"
    show shy_yjf_b1 b1 b1_ga1
    play voice "voice/圣护院/150101360.ogg"
    shy "虽然名字中的含义我至今也不曾了解......"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ seen_home_event01 = False
    scene set only home night outside xuejian
    with dissolve
    pause 2.0 hard

label day207.myroom_event01:
    $ flcam.move(0, 0, 0)
    scene black
    pause 1.0 hard
    scene set only home night my_room xuejian
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dsf_b3 onlayer m2:
            hide screen investigation_popup
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            move _("客厅") jump day207.home_event01
            screen_direction left
            sleep jump day207.sleep

label day207.home_event01:
    if not seen_home_event01:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ flcam.move(0, 0, 0)
        scene black 
        pause 1.0 hard
        play music second_105 fadein 3.0 if_changed
        scene set only home night living_room xuejian
        with dissolve
        pause 1.0 hard
        $ flcam.move(0, -300, 900, duration=1.5)
        pause 0.5 hard
        show xz_dsf_b2 b2 b2_n1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010104940.ogg"
        xz "友加说她今晚和姐姐在一起，还强调这是久违的一顿晚餐。"
        hide xz_dsf_b2
        show xz_dsf_b3 b3 b3_h1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010104950.ogg"
        xz "听她的语气似乎有些生气啊。"
        show xz_dsf_b3 b3 b3_s1
        play voice "voice/翔子/010104960.ogg"
        xz "虽然她说她的姐姐是因为工作上的关系才提前回家的。"
        show xz_dsf_b3 b3 b3_n1
        play voice "voice/翔子/010104970.ogg"
        xz "但我觉得她姐姐应该也是一个非常在乎她的人。"
        show xz_dsf_b3 b3 b3_h1
        play voice "voice/翔子/010104980.ogg"
        xz "毕竟作为研究所的主任，应该也担负着不少责任吧。"
        $ flcam.move(0, -300, 1000, duration=1.5)
        pause 0.5 hard
        me01 "如果真是这样那就太好了。"
        hide xz_dsf_b3
        show xz_dsf_b2 b2 b2_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010105010.ogg"
        xz "什么？"
        me01 "没什么。"
        me01 "或许那两个人都只是不够坦率而已。"
        show xz_dsf_b2 b2 b2_s2
        play voice "voice/翔子/010105040.ogg"
        xz "神野君你总会说一些我听不懂的话。"
        me01 "嘛，毕竟我也是亲身踏入过“量子领域”的人。"
        hide xz_dsf_b2 with None
        pause 0.1 hard
        show xz_dsf_b1 b1 b1_h1 onlayer m2 at flu_down(0.35, 20):
            xpos 0.5
        play voice "voice/翔子/010105060.ogg"
        xz "看吧，果然~"
        $ flcam.move(-2250, 300, 750, duration=1.5)
        show aiyi_sy_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        play voice "voice/爱衣/110102180.ogg"
        aiyi "小桃的奶奶说过，翔子姐姐和千波一样是傲娇。"
        hide xz_dsf_b1 with None
        pause 0.1 hard
        show xz_dsf_b2 b2 b2_a1 onlayer m2 at flu_down(0.15, 20):
            xpos 0.5
        play voice "voice/翔子/010105070.ogg"
        xz "{size=72}才不是！{/size}"
        show aiyi_sy_b1 b1 b1_sp1
        play voice "voice/爱衣/110102190.ogg"
        aiyi "大哥哥，傲娇是什么？"
        me01 "就是像你翔子姐姐这样的人。"
        hide xz_dsf_b2
        show xz_dsf_b1 b1 b1_a1 onlayer m2 at flu_down(0.15, 20):
            xpos 0.5
        play voice "voice/翔子/010105080.ogg"
        xz "都说不是了！"
        show aiyi_sy_b1 b1 b1_h1
        play voice "voice/爱衣/110102200.ogg"
        aiyi "大姐姐胸又大又是傲娇。"
        me01 "也就是常说的巨乳傲娇吧。"
        hide aiyi_sy_b1
        $ flcam.move(0, -300, 900, duration=1.5)
        show xz_dsf_b1 b1 b1_ga1
        play voice "voice/翔子/010105090.ogg"
        xz "神野君......"
        "似乎有些太得意忘形了。"
        $ flcam.move(-2250, 300, 750, duration=1.5)
        show aiyi_sy_b1 b1 b1_sp1 onlayer m2:
            xpos 0.3
        play voice "voice/爱衣/110102210.ogg"
        aiyi "巨乳傲娇是什么？"
        hide xz_dsf_b1
        show xz_dsf_b3 b3 b3_h1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010105100.ogg"
        xz "爱、爱衣，我们去睡觉吧~"
        pause 1.0 hard
        show xz_dsf_b3 b3 b3_h1 at walkout_r(0.5)
        show aiyi_sy_b1 b1 b1_sp1 at walkout_r(0.3)
        pause 0.5 hard
        play sound close_door5
        pause 1.0 hard
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
        "翔子红着脸带着爱衣离开了客厅。"
        "是有多想结束这个话题啊......"
        stop music fadeout 5.0
        pause 1.0 hard
        scene black 
        with slowerdissolve
        pause 1.0 hard
        scene set only home night living_room xuejian
        show xz_dsf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        show aiyi_sy_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        $ flcam.move(-2250, -400, 600)
        $ flcam.move(-2250, -100, 400, duration=1.5)
        pause 0.5 hard
        $ seen_home_event01 = True
    else:
        $ flcam.move(0, 0, 0)
        scene black
        pause 1.0 hard
        scene set only home night living_room xuejian
        show xz_dsf_b3 b3 b3_n1 onlayer m1:
            xpos 0.5
        show aiyi_sy_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        $ flcam.move(-2250, -400, 600)
        $ flcam.move(-2250, -100, 400, duration=3.0)
        with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu xz_dsf_b3 onlayer m1:
            camera_pos (scale(2597), scale(-1024), 400)
            screen_pos (0.55, 1.0)
            screen_direction right
            move _("卧室") jump day207.myroom_event01
        object aiyi_sy_b1 onlayer m2 jump day207.aiyi_event01

label day207.aiyi_event01:
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_sy_b1 b1 b1_h1
    aiyi "大哥哥，晚安~"
    $ flcam.move(-2250, -100, 400, duration=3.0)
    jump investigate

label day207.sleep:
    menu:
        "早点休息":
            if not seen_home_event01:
                window mode thought
                me01 "睡觉前还是先去和翔子她们打声招呼吧。"
                $ flcam.move(0, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            hide screen investigation_popup
            show xz_dsf_b3 b3 b3_h1
            play voice "voice/翔子/010001080.ogg"
            xz "晚安~"
        "{#cancel}再等等":
            xz "还有什么事情要考虑吗......"
            $ flcam.move(0, 100, 200, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump day207.memory_event01

label day207.memory_event01:
    nvl clear
    pcenter "在这纯白的世界里。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    pcenter "雪花纷然飘落——"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 1.0 hard
    play music second_117 fadein 3.0 if_changed
    scene set only sky snow day xuejian
    with slowdissolve
    show snow_level1 onlayer fg
    pause 1.0 hard
    "那一天，希菲尔来公寓找我了。"
    "她是我来到雪见市之后交到的第一个朋友。"
    pause 1.0 hard
    scene set only memory_cg winter one
    with dissolve
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201260.ogg"
    xfe "凉君，我来找你玩了~"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201270.ogg"
    xfe "之前没能来找你真是抱歉的说......"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/000201280.ogg"
    xfe "因为千冬她把身体搞坏了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    pause 1.0 hard
    "希菲尔口中的千冬小姐，似乎是一位身体十分虚弱的人。"
    "听希菲尔说千冬是她第一个朋友。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only memory_cg winter one alpha
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201300.ogg"
    xfe "不过呢，现在千冬她又恢复精神了哟~"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/000201310.ogg"
    xfe "所以希菲尔又可以回到这座城市了。"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201330.ogg"
    xfe "这里的空气非常的好吃~"
    me01 "毕竟远离工业区的缘故。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201340.ogg"
    xfe "雪也非常好吃~"
    me01 "会这么认为的也只有希菲尔吧......"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201350.ogg"
    xfe "千冬恢复精神的话，希菲尔也会变得有精神。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201370.ogg"
    xfe "又能和凉君一起玩耍真是太好了~"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/000201380.ogg"
    xfe "......凉君？"
    me01 "我也觉得能再见到希菲尔真是太好了。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000201390.ogg"
    xfe "凉君......稍微有些不一样了？"
    me01 "是吗？"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/000201400.ogg"
    xfe "果然......氛围有些不同了。"
    show ts_xfe_yjz_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/000201410.ogg"
    xfe "现在的凉君变得和千冬一样了......"
    show ts_xfe_yjz_b1 b1 b1_n2
    play voice "voice/希菲尔/000201420.ogg"
    xfe "凉君，发生什么事了吗？"
    me01 "......没什么。"
    "在得知自己不久后将要再一次离开这座城市，我也是犹豫是否应该将真相告诉眼前的这位女孩。"
    "但就在刚才，当看到了她脸上挂着笑容的时候，我无论如何也无法说出口。"
    "离别对于我而言早已是家常便饭。"
    "到目前为止我从未想过去改变些什么。"
    "但如果当时的我能够坦率地对她说出自己的想法。"
    "也许一切......都会有所不同了吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day208
