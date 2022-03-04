
label day226:
    bookmark
    $ save_name = _("Day 226")
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
    show backend_date225 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    with slowdissolve
    pause 2.0 hard
    scene set only school snow day outside xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(4500, 300, 1000, duration=1.5)
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at walkin_l(0.7)
    pause 0.5 hard
    play voice "voice/千波/211000140.ogg"
    qb "{size=72}喂！！{/size}"
    play music second_139 fadein 3.0 if_changed
    me01 "为什么你每次见到我都要大喊大叫的。"
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_n2
    play voice "voice/千波/211000150.ogg"
    qb "为了不被某人小看。"
    me01 "就算你不这么做也没人会小看你吧。"
    hide qianbo_dzf_b1
    show qianbo_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.7
    play voice "voice/千波/211000160.ogg"
    qb "才不想被凉君男小看的哼。"
    me01 "倒不如说小看你我都觉得麻烦。"
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/千波/211000170.ogg"
    qb "即使被凉君男舔脚也不会觉得舒服的哼。"
    me01 "为什么我非要舔你的脚不可啊？！"
    $ flcam.move(4500, 300, 1000, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/211000180.ogg"
    qb "我也终于升入高年级，成为幼儿园里最年长的了。"
    me01 "那还真是遗憾啊。"
    $ flcam.move(2250, 300, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111000860.ogg"
    aiyi "千波说，要想成为高年级里最伟大的存在，就必须成为幼儿园的学生会长才行。"
    me01 "幼儿园有这种职务吗？"
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/小桃/221000130.ogg"
    ycxt "刚才就是这样写在名牌上的。"
    show ycxt_dzf_b1 b1 b1_s3
    play voice "voice/小桃/221000140.ogg"
    ycxt "小桃我，不想升到高年级......"
    me01 "为什么？"
    hide aiyi_dzf_b1
    hide qianbo_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s2
    play voice "voice/小桃/221000150.ogg"
    ycxt "因为这样，明年就要毕业了。"
    show ycxt_dzf_b1 b1 b1_s4 at flu_down(0.25, 20):
        xpos 0.3
    play voice "voice/小桃/221000160.ogg"
    ycxt "小学，好恐怖......"
    me01 "不用担心的，爱衣和千波会陪你一起的。"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221000170.ogg"
    ycxt "小桃的布偶也可以一起？"
    me01 "这个恐怕......"
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/111000870.ogg"
    aiyi "没关系的，老师也说了小桃一定会顺利交到朋友的。"
    me01 "是啊......毕竟小桃那么招人喜欢。"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_h4 onlayer m2:
        xpos 0.7
    play voice "voice/千波/211000190.ogg"
    qb "我也是为了在进入小学后不被小看，不从现在开始作为学生会长建立起威望可不行。"
    show qianbo_dzf_b1 b1 b1_h2 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/千波/211000200.ogg"
    qb "泽村会长可以被触碰的地方，也只有脚了~"
    me01 "你这家伙的未来真叫人担忧。"
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/小桃/221000180.ogg"
    ycxt "奶奶告诉过我的，说舔脚是服从的象征。"
    play voice "voice/爱衣/111000880.ogg"
    aiyi "为什么是这样的呢？"
    show qianbo_dzf_b1 b1 b1_h4
    play voice "voice/千波/211000210.ogg"
    qb "因为很舒服吧。"
    play voice "voice/爱衣/111000890.ogg"
    aiyi "哪一方？"
    show qianbo_dzf_b1 b1 b1_h2 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/千波/211000220.ogg"
    qb "率先妥协的一方~"
    play voice "voice/爱衣/111000900.ogg"
    aiyi "什么意思？"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/221000190.ogg"
    ycxt "试试看的话是不是就知道了？"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_n2
    play voice "voice/千波/211000230.ogg"
    qb "凉君男，快来舔我的脚！"
    me01 "怎么可能照做啊？！"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/211000240.ogg"
    qb "不甘心的话就让我舒服起来吧！"
    me01 "声音太大了，会被误会的！"
    show qianbo_dzf_b1 b1 b1_h2 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/千波/211000250.ogg"
    qb "如果凉君男无论如何都想要的话，让你舔{rb}脚以外的地方{/rb}{rt}脚踝{/rt}也是可以的！"
    hide qianbo_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_ga1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/立花希/031000880.ogg"
    xz "今天的社团活动主题是“舔脚”吗......"
    me01 "不是你想的那样。" with vpunch
    "来的不是千川老师真是太好了。"
    hide xz_dzf_b1
    $ flcam.move(0, 200, 600, duration=1.5)
    show ycxt_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    show qianbo_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/221000200.ogg"
    ycxt "奶奶告诉我说，一般两个人在说悄悄话的话就是告白哟~"
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_h2 onlayer m2:
        xpos 0.7
    play voice "voice/千波/211000260.ogg"
    qb "一定是想要被对方舔才会这么说的啦。"
    me01 "才不是！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day226'
    $ seen_day226_balltower_event01 = False
    $ seen_day226_laboratory_event01 = False
    $ seen_day226_balltower_event02 = False
    $ seen_day226_myroom_event01 = False

label day226.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day226':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day226.balltower_event01':
        show set maps winter evening
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day226.laboratory_event01':
        show set maps winter night
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['laboratory'])
    elif _overworld_label == 'day226.balltower_event02':
        show set maps winter night
        show snow_level1 onlayer fg
        $ flcam.move(*overworld.camera_positions['cloqks'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        cloqks=("day226.balltower_event01", "(not seen_day226_balltower_event01) or (seen_day226_laboratory_event01 and not seen_day226_balltower_event02)"),
        laboratory=("day226.laboratory_event01", "seen_day226_balltower_event01 and not seen_day226_laboratory_event01"),
        road1=("day226.myroom_event01", "seen_day226_balltower_event02 and not seen_day226_myroom_event01"))
    $ window_animate_outro()
    if _return == 'day226.balltower_event01' and _overworld_label == 'day226':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day226.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day226.balltower_event01' and _overworld_label == 'day226.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
        $ _window_animation = None
        stop music fadeout 3.0
        pause 3.0 hard
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        jump expression 'day226.balltower_event02'
    elif _return == 'day226.myroom_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day226.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    show snow_level1 onlayer fg
    play music second_148 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('final chapter'), _("樱雪同梦，白色永恒"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard
    scene set only balltower snow evening xuejian
    with dissolve
    pause 1.0 hard
    me01 "找到你了，希菲尔。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002260.ogg"
    xfe "诶嘿......被找到了~"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show alu_ct_b8 b8 b8_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎~"
    show ts_xfe_yjz_b2 b2 b2_a1 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001002270.ogg"
    xfe "谁、谁也没有希望你能找到。"
    me01 "拜托了，请别再帮阿露翻译了。"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001002280.ogg"
    xfe "但是，阿露也很想加入对话的样子。"
    me01 "如果乖乖作为吉祥物不出声的话我还是能接受。"
    hide alu_ct_b8
    show alu_ct_b2 b2 b2_3 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000740.ogg" 
    alu "唔莎！"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_a2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002290.ogg"
    xfe "吉祥物的宝座才不会让给你呢~"
    me01 "太天真了，论可爱程度的话希菲尔可是比你强太多了。"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/001002300.ogg"
    xfe "希菲尔，很可爱吗？"
    me01 "那是当然的吧。"
    stop music fadeout 5.0
    hide alu_ct_b2
    show alu_ct_b8 b8 b8_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000580.ogg"
    alu "唔莎？"
    play music second_104 fadein 3.0 if_changed
    show ts_xfe_yjz_b3 b3 b3_a1 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001002310.ogg"
    xfe "这个男人，是萝莉控啊。"
    "还是无视这只仿制布偶好了。"
    hide alu_ct_b8
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/001002320.ogg"
    xfe "凉君，你是萝莉控吗？"
    me01 "当然不是。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002330.ogg"
    xfe "是因为希菲尔还不够可爱吗？"
    me01 "这之间没有什么关系吧。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002340.ogg"
    xfe "因为希菲尔完全长不大的说。"
    me01 "没有的事，不如说现在这样才是最可爱的！"
    show ts_xfe_yjz_b2 b2 b2_ga1 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001002350.ogg"
    xfe "这个男人，真是无药可救的萝莉控啊~"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show alu_ct_b2 b2 b2_2 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎~"
    me01 "那个，希菲尔你......"
    me01 "刚刚是在阿露说话前就“翻译”出来了吗？"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001002360.ogg"
    xfe "没有这回事哟~"
    me01 "都是阿露的错，明明以为可以和希菲尔独处的。"
    hide alu_ct_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001003270.ogg"
    xfe "凉君想和希菲尔独处吗？"
    me01 "不小心说出了真心话。"
    show ts_xfe_yjz_b3 b3 b3_ga3
    play voice "voice/希菲尔/001003280.ogg"
    xfe "一直都在说漏嘴了哟~"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show alu_ct_b8 b8 b8_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000740.ogg"
    alu "唔莎~（简直像是在说本小姐是多余的。）"
    hide ts_xfe_yjz_b3
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide alu_ct_b8
    show alu_ct_b2 b2 b2_2 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000740.ogg"
    alu "唔莎~（本小姐可是个会解读气氛的神明呢。）"
    me01 "你比{rb}原来的主人{/rb}{rt}藤原瞳{/rt}好不到哪里去......"
    me01 "等等，为什么我突然能和阿露对话了？"
    "掌握了无聊的技能。"
    pause 1.0 hard
    hide snow_level1
    play voice "voice/阿露/551000090.ogg"
    $ flcam.move(0, 0, 0)
    scene set only alu_cg six
    with dissolve
    with vpunch
    play sound rell_fire
    alu "唔莎~波~！（那就接招吧！）"
    pause 0.1 hard
    play sound rune2
    scene set only alu_cg seven
    with dissolve
    me01 "谁怕谁啊！"
    pause 0.1 hard
    play sound ganga03
    scene set only alu_cg eight
    with dissolve
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......（要、要融化了......）"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow evening xuejian
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    with dissolve
    play voice "voice/希菲尔/001003290.ogg"
    xfe "凉君好厉害，新的必杀技呢~"
    me01 "只是稍微改变了风向而已。"
    "这种程度的火焰，比起琉璃的{rb}冥火{/rb}{rt}pyrokinesis{/rt}还差得远呢。"
    stop music fadeout 5.0
    me01 "再怎么说也不能输给一只仿制玩偶啊。"
    pause 1.0 hard
    hide snow_level1
    play music second_104 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only alu_cg nine
    with dissolve
    with vpunch
    play sound rell_fire
    play voice "voice/希菲尔/001003300.ogg"
    xfe "唔莎波~"
    show wflash onlayer texture
    with vpunch 
    me01 "{size=72}唔喔喔！？{/size}"
    me01 "到底发生了什么！"
    pause 0.1 hard
    play sound ganga01
    scene set only alu_cg ten
    with dissolve
    play voice "voice/希菲尔/001003310.ogg"
    xfe "试着模仿阿露，然后就成功了哟~"
    me01 "都是阿露的错，看你让希菲尔掌握了奇怪的技能。"
    play voice "voice/阿露/551000410.ogg"
    alu "唔、唔莎......（比、比起这个，先快点救救要溶化的本小姐啊......）"
    pause 0.1 hard
    scene set only alu_cg eleven
    with dissolve
    "我们用雪开始修补融化的阿露。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    show snow_level1 onlayer fg
    play music second_148 fadein 3.0 if_changed
    with dissolve
    pause 2.0 hard
    scene set only balltower snow evening xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001003350.ogg"
    xfe "凉君，变得软趴趴的了。"
    me01 "毕竟修复那家伙可是相当累人的。"
    me01 "话说回来希菲尔的{rb}灵纹{/rb}{rt}rune{/rt}可真是厉害。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001003370.ogg"
    xfe "住在这座雪见市的{rb}灵继者{/rb}{rt}elfin{/rt}们，希菲尔一直都在关注着~"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001003380.ogg"
    xfe "一边守护的同时也在学习的，叭咕叭咕~"
    show ts_xfe_yjz_b2 b2 b2_s2
    play voice "voice/希菲尔/001003390.ogg"
    xfe "如果什么都不知道的话是不行的。只会依靠千冬的话，最后只会变成累赘......"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001003400.ogg"
    xfe "......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001003410.ogg"
    xfe "想见......千冬了吗？"
    "我点了点头。"
    play voice "voice/希菲尔/001003420.ogg"
    xfe "千冬她现在，也在为了让希菲尔能够变得精神起来而努力着。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001003430.ogg"
    xfe "所以想要见的话，可能很困难的说......"
    me01 "是吗。"
    play voice "voice/希菲尔/001003440.ogg"
    xfe "......"
    me01 "抱歉，让你为难了。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001003450.ogg"
    xfe "不是的，希菲尔才是应该道歉的。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide ts_xfe_yjz_b1
    $ flcam.move(0, -100, 400, duration=5.0, warper='ease_cubic')
    play ambience1 zhong_rill fadein 3.0
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow evening big
    play music second_140 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "钟声再次响起。"
    "周围已经被染上了橘红色。"
    "雪依旧下着，夕阳的红晕在缤纷的雪花上倒映着。"
    "这样的景色，就宛若梦幻一般。"
    "此时才发现阿露的身影随着钟声一起消失了。"
    "终于能和希菲尔独处了，超开心~"
    pause 1.0 hard
    stop ambience1 fadeout 3.0
    scene set only balltower snow evening xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002430.ogg"
    xfe "凉君也，差不多该回去了。"
    me01 "等等......再待一会儿可以吗？"
    show ts_xfe_yjz_b2 b2 b2_sp1
    play voice "voice/希菲尔/001002440.ogg"
    xfe "不按时回家没关系吗？"
    me01 "稍微晚一点的话应该问题不大。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002450.ogg"
    xfe "那么要来打雪仗吗？"
    me01 "感觉这个游戏都是以我被打成雪人告终的所以还是算了。"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/001002460.ogg"
    xfe "那要做些什么呢？"
    me01 "散步之类的......怎么样？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002470.ogg"
    xfe "情人伞？"
    me01 "不是啦，而且现在也没有伞。"
    stop music fadeout 5.0
    show ts_xfe_yjz_b1 b1 b1_s3
    play voice "voice/希菲尔/001002480.ogg"
    xfe "......"
    me01 "抱歉。"
    play music second_142 fadein 3.0 if_changed
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001002490.ogg"
    xfe "没关系的。"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    play sound touch
    show ts_xfe_yjz_b2 b2 b2_sp1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    "我顺势牵起了希菲尔的手。"
    show ts_xfe_yjz_b2 b2 b2_h3
    play voice "voice/希菲尔/001002500.ogg"
    xfe "凉君的手，比以前要大了许多。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002510.ogg"
    xfe "像这样牵着手一起走的话，也是在玩吗？"
    me01 "是啊，也是在玩。"
    "不如说非常地开心。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002520.ogg"
    xfe "凉君也长高了，并肩走的话已经看不到凉君的脸了。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002530.ogg"
    xfe "看不到脸的话，就没办法和凉君说话了。"
    me01 "因为抬头很累吗？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002540.ogg"
    xfe "不是那样的，但是会有种奇怪的感觉。"
    me01 "既然这样的话，我抱着你吧？"
    me01 "这样就能边走边说话了。"
    show ts_xfe_yjz_b2 b2 b2_sp3
    play voice "voice/希菲尔/001002550.ogg"
    xfe "抱着......"
    me01 "不行吗？"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001002560.ogg"
    xfe "不是的......以前也经常被千冬抱着的。"
    show ts_xfe_yjz_b2 b2 b2_h3 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001002570.ogg"
    xfe "凉君的话......可以的哟~"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 1.0 hard
    play sound touch
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg touch1
    with slowdissolve
    pause 1.0 hard
    "有种不可思议的感觉。"
    "感觉不到重量。"
    "但是这份踏实的触感却让我几乎放弃了思考。"
    "真希望能够就这样一直下去。"
    "想要一直抱着这样的她。"
    play voice "voice/希菲尔/001003480.ogg"
    xfe "凉君，长大了呢~"
    play voice "voice/希菲尔/001003490.ogg"
    xfe "成长到已经能把希菲尔抱起来的程度了呢。"
    pause 0.1 hard
    scene set only xfe_cg touch2
    with dissolve
    play voice "voice/希菲尔/001003500.ogg"
    xfe "我以前，从没有想过这样的事情。"
    play voice "voice/希菲尔/001003510.ogg"
    xfe "以为凉君会和希菲尔一样，一直是这样小小的。"
    play voice "voice/希菲尔/001003520.ogg"
    xfe "以为两人是可以一直这样不改变的。"
    play voice "voice/希菲尔/001003530.ogg"
    xfe "虽然凉君也说过，两人的关系不会改变。"
    pause 0.1 hard
    scene set only xfe_cg touch4
    with dissolve
    play voice "voice/希菲尔/001003540.ogg"
    xfe "但是......"
    pause 0.1 hard
    scene set only xfe_cg touch1
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001003550.ogg"
    xfe "希菲尔觉得，千冬其实也是非常想见凉君你的。"
    play voice "voice/希菲尔/001003560.ogg"
    xfe "从以前开始就是这样了。"
    play voice "voice/希菲尔/001003570.ogg"
    xfe "所以现在一定也是......"
    play voice "voice/希菲尔/001002580.ogg"
    xfe "因为希菲尔我什么都不懂，所以凉君教给我各种各样的游戏。"
    play voice "voice/希菲尔/001002590.ogg"
    xfe "然后，现在的希菲尔也明白了更多的东西。"
    pause 0.1 hard
    scene set only xfe_cg touch2
    with dissolve
    play voice "voice/希菲尔/001002600.ogg"
    xfe "凉君给人的感觉......很温暖。"
    play voice "voice/希菲尔/001002610.ogg"
    xfe "和千冬稍微有点不同。"
    play voice "voice/希菲尔/001002620.ogg"
    xfe "千冬的怀抱很柔软，而凉君的却是很强壮的感觉~"
    play voice "voice/希菲尔/001002630.ogg"
    xfe "是让希菲尔觉得安心的感觉哟。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only balltower snow evening xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002640.ogg"
    xfe "芬布尔之冬......"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001002650.ogg"
    xfe "不会融化的白雪，和冷漠是同一个意思。"
    play voice "voice/希菲尔/001002660.ogg"
    xfe "堆积的白雪，和寒冷也是同一个意思。"
    play voice "voice/希菲尔/001002670.ogg"
    xfe "这样的梦境有朝一日将会成为现实。"
    me01 "希菲尔？"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001002690.ogg"
    xfe "玩耍的时间已经结束了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/001002700.ogg"
    xfe "回去太晚的话，会让喜欢凉君的大家担心的。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001002710.ogg"
    xfe "拜拜，凉君~"
    me01 "现在的希菲尔也已经是我的家人了吧？"
    "希菲尔没有回答。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001002730.ogg"
    xfe "......家人。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001002740.ogg"
    xfe "虽然不太明白，不过凉君和千冬都是对希菲尔而言非常重要的人。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002760.ogg"
    xfe "如果真的如你所说的话......就太好了~"
    stop music fadeout 5.0 
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day226_balltower_event01:
        $ seen_day226_balltower_event01 = True
    $ _overworld_label = 'day226.balltower_event01'
    jump day226.map

label day226.laboratory_event01:
    $ flcam.move(0, 0, 0)
    scene set only laboratory evening inside xuejian
    play music second_129 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/白羽/711001170.ogg"
    baiyu "这大概......就是不被接受的结果吧。"
    play voice "voice/白羽/711001180.ogg"
    baiyu "圣护院也有同样的顾虑。"
    play voice "voice/白羽/711001190.ogg"
    baiyu "其他的部下也和她持有相同的态度。"
    play voice "voice/白羽/711001200.ogg"
    baiyu "这样的话，如果我将这个计划真正的目的告诉她们的话，会得到帮助吗？"
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711001210.ogg"
    baiyu "......不知道。"
    play voice "voice/白羽/711001220.ogg"
    baiyu "即使能够明白对方内心的想法，但是想要左右这样的局面果然还是很困难的。"
    play voice "voice/白羽/711001230.ogg"
    baiyu "单是想到这个就觉得“你”真的好厉害。"
    show baiyu_yjf_b1 b1 b1_s3
    play voice "voice/白羽/711001240.ogg"
    baiyu "为了这个计划我不得不做的就是尽可能地聚集{rb}灵继者{/rb}{rt}elfin{/rt}。"
    play voice "voice/白羽/711001280.ogg"
    baiyu "但结果，还是失去像“你”这样的重要伙伴......"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show baiyu_yjf_b1 b1 b1_s1
    play voice "voice/白羽/711001290.ogg"
    baiyu "请原谅我。"
    play voice "voice/白羽/711001300.ogg"
    baiyu "但是我不会放弃的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    show baiyu_yjf_b1 b1 b1_s2 onlayer screens at side_left('baiyu'), basicfade
    play voice "voice/白羽/711001310.ogg"
    baiyu "妈妈我也会加油的。"
    play voice "voice/白羽/711001320.ogg"
    baiyu "为了能够实现你的愿望——"
    hide baiyu_yjf_b1
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day226.laboratory_event02:
    scene set only laboratory night outside xuejian
    show snow_level1 onlayer fg
    play music second_138 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    play sound phone1
    me01 "我知道了，我会帮忙调查清楚的。"
    me01 "那么再见。"
    play sound phone2
    pause 1.0 hard
    hide snow_level1
    scene set only laboratory inside1 xuejian
    with dissolve
    pause 1.0 hard
    "刚离开钟楼就接到了千川老师的电话。"
    "说是在研究所的方向有异常的{rb}灵纹{/rb}{rt}rune{/rt}波动。"
    "和翔子说明了情况的经过之后，我径直来到了研究所。"
    "果然这里除了念波以外感觉不到其他的什么了。"
    "建筑里没有一个人。"
    pause 0.5 hard
    play sound jiaobu3
    $ flcam.move(-2200, -1400, 800, duration=3.0, warper='ease_cubic')
    pause 2.0 hard
    "静谧的走廊上，只有自己的脚步声。"
    "四周灯光昏暗，就连我自己都不知道道路是通向何方。"
    pause 0.5 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001003650.ogg"
    xfe "在这里哟~"
    play sound xiaoshi_1
    show ts_xfe_yjz_b1 b1 b1_n2:
        xpos 0.5 alpha 1.0
        linear 0.5 alpha 0.0
    pause 1.0 hard
    hide ts_xfe_yjz_b1
    "每当我迷失在岔路口的时候，希菲尔的身影就会出现为我指引方向。"
    "因此即使在黑暗之中，我也能安心地前进了。"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    play sound open_door4
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory evening inside xuejian
    with dissolve
    pause 1.0 hard
    "走廊的尽头是一个房间。"
    "屋内没有灯光。"
    "但是因为窗外的光能够照射进来的缘故，我还能依稀看清屋内的状况。"
    "就在这样朦胧的场景中，一股久违而又熟悉的声音在我脑中回荡开来。"
    pause 1.0 hard
    scene set only memory_cg xuejian yume
    show snow_level1 onlayer fg
    with dissolve
    $ flcam.move(1100, -5600, 450, duration=20.0, warper='ease_cubic')
    play voice "voice/诗乃/701000180.ogg"
    stranger "多亏了你，我才能明白。"
    play voice "voice/诗乃/701000190.ogg"
    stranger "正因为有了相遇，才能唤来春天。"
    play voice "voice/诗乃/701000200.ogg"
    stranger "天狗追逐着月亮，是因为天狗本身心怀寂寞。"
    play voice "voice/诗乃/701000210.ogg"
    stranger "月亮接受天狗，是因为月亮本身同样心怀寂寞。"
    play voice "voice/诗乃/701000220.ogg"
    stranger "是啊......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian4
    with dissolve
    pause 1.0 hard
    play voice "voice/诗乃/701000230.ogg"
    stranger "星星会像这样布满夜空，是因为月亮和天狗相遇了——"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene set only laboratory evening inside xuejian
    with dissolve
    pause 1.0 hard
    "回过神来的我这才发现。"
    "床上有一个身影正在沉睡着。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    play music second_153 fadein 3.0 if_changed
    pause 2.0 hard
    scene set only jsqd_cg bed1
    with slowdissolve
    pause 1.0 hard
    "被月光照亮的她。"
    "身影逐渐清晰起来。"
    pause 0.1 hard
    $ flcam.move(1100, -1400, 450, duration=3.0, warper='ease_quad')
    "拥有着与希菲尔神似的容貌。"
    "名为姬神千冬的女孩。"
    "此刻正安静地睡着。"
    "雪白的长发在月光下闪闪发光。"
    pause 0.1 hard
    scene set only jsqd_cg bed2
    with dissolve
    play voice "voice/千冬/771000010.ogg"
    jsqd "一直想见你。"
    play voice "voice/千冬/771000020.ogg"
    jsqd "我一直在等你。"
    play voice "voice/千冬/771000030.ogg"
    jsqd "一直、一直......在等你——"
    pause 1.0 hard
    play sound rune2
    scene white 
    with slowerdissolve
    pause 2.0 hard

label day226.laboratory_event03:
    $ flcam.move(0, 0, 0)
    scene set only laboratory night outside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000750.ogg"
    liuli "刚才，从研究所里感应到了{rb}灵纹{/rb}{rt}rune{/rt}。"
    "琉璃的吃惊并不是没有原因的。"
    "星天宫研究所的特质玻璃，明明只要是{rb}灵纹{/rb}{rt}rune{/rt}都无法穿透。"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000760.ogg"
    liuli "而且刚才的{rb}灵纹{/rb}{rt}rune{/rt}并不是神野前辈的。"
    show liuli_dsf_b1 b1 b1_s2
    play voice "voice/琉璃/041000770.ogg"
    liuli "里面有除了前辈以外{rb}灵继者{/rb}{rt}elfin{/rt}的可能性......也不是没有。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041000780.ogg"
    liuli "在宇宙中心也听说了研究所目前无人使用，大概是错觉吧......"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000790.ogg"
    liuli "现在来到雪见市之后，我的{rb}灵纹{/rb}{rt}rune{/rt}就一直不太稳定。"
    hide liuli_dsf_b2
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001003660.ogg"
    xfe "......"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000830.ogg"
    liuli "你是什么时候在这里的？"
    hide liuli_dsf_b3
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001003670.ogg"
    xfe "......被找到了。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n4 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001003680.ogg"
    xfe "那你一定也是，迷路的孩子吧？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000840.ogg"
    liuli "不、不是，比起这个......"
    show liuli_dsf_b2 b2 b2_h1
    play voice "voice/琉璃/041000850.ogg"
    liuli "已经很晚了，小朋友还是赶快回家比较好哟~"
    "琉璃温柔地抚摸着希菲尔的头。"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound touch
    show ts_xfe_yjz_b2 b2 b2_sp1 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/琉璃/041000860.ogg"
    liuli "乖孩子乖孩子~"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h4 onlayer m2 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/希菲尔/001003690.ogg"
    xfe "叭咕叭咕~"
    play sound jump_1
    show liuli_dsf_b2 b2 b2_ga4 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/琉璃/041000870.ogg"
    liuli "我的手被吃掉了？！"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_a1 onlayer m2:
        xpos 0.7
    play voice "voice/希菲尔/001003700.ogg"
    xfe "不要随便乱摸希菲尔。"
    play sound touch
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_h1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/琉璃/041000880.ogg"
    liuli "乖孩子乖孩子~"
    show ts_xfe_yjz_b2 b2 b2_s2 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/希菲尔/001003710.ogg"
    xfe "啊，不要摸头......哼！"
    pause 0.5 hard
    hide liuli_dsf_b3
    play sound hide_sound
    show ts_xfe_yjz_b2 b2 b2_s2 at walkout_r(0.7)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    $ flcam.move(5800, 500, 1500, duration=1.5)
    pause 0.5 hard
    play sound ganga02
    with vpunch
    show wflash onlayer texture
    "{size=72}噗嗤。{/size}"
    pause 0.5 hard
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_sp2 onlayer m2 at flu_down(0.15, 20, 2):
        xpos 0.7
    play voice "voice/希菲尔/001003720.ogg"
    xfe "呜啊啊~希菲尔的鼻子啊~"
    "慌慌张张逃跑结果摔倒了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_sp2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000890.ogg"
    liuli "不、不要紧吧？"
    show ts_xfe_yjz_b2 b2 b2_c1 at flu_down(0.25, 20):
        xpos 0.7
    play voice "voice/希菲尔/001003730.ogg"
    xfe "一、一点也不痛喔......呜呜。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000900.ogg"
    liuli "真了不起啊，能自己爬起来。"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001003740.ogg"
    xfe "这里的积雪很少，所以走起路来很困难的。"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000910.ogg"
    liuli "你的家在哪里？我可以带你回家哟~"
    show ts_xfe_yjz_b2 b2 b2_ga1
    play voice "voice/希菲尔/001003750.ogg"
    xfe "这就是“胃”底之蛙吧。"
    show liuli_dsf_b3 b3 b3_s3
    play voice "voice/琉璃/041000920.ogg"
    liuli "你之前不会是吃过青蛙吧......"
    show ts_xfe_yjz_b2 b2 b2_h2
    play voice "voice/希菲尔/001003760.ogg"
    xfe "希菲尔我就算一个人，也可以一下子就回去的哟~"
    show liuli_dsf_b3 b3 b3_sp1
    play voice "voice/琉璃/041000930.ogg"
    liuli "啊，是这个意思吗，但是晚上自己走路的话是很危险......"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    play sound xiaoshi_1
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only laboratory night outside xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000940.ogg"
    liuli "刚才的是？"
    "希菲尔的身影突然消失了。"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041000950.ogg"
    liuli "......真是不可思议的孩子啊。"
    hide liuli_dsf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    play music second_120 fadein 3.0 if_changed
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/藤原瞳/131000880.ogg"
    tyt "叫我吗？"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000960.ogg"
    liuli "啊，不是的，并没有叫你......"
    show liuli_dsf_b2 b2 b2_sp1
    play voice "voice/琉璃/041000970.ogg"
    liuli "藤原同学你也来了吗？"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131000890.ogg"
    tyt "嗯，我在这附近感觉到了大概是从研究所里面传出来的灵能力。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000980.ogg"
    liuli "藤原同学也是？"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131000900.ogg"
    tyt "不过更让我惊讶的还是花山院你，不是在宇宙中心训练吗？"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041000990.ogg"
    liuli "啊，这个嘛......"
    stop music fadeout 5.0
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131000910.ogg"
    tyt "好像已经有几个月没有回来这里了。"
    show liuli_dsf_b1 b1 b1_sp1
    play voice "voice/琉璃/041001000.ogg"
    liuli "这你都记得吗？"
    play music second_142 fadein 3.0 if_changed
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131000990.ogg"
    tyt "那是因为我们是朋友嘛~"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001040.ogg"
    liuli "是的。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131001000.ogg"
    tyt "让花山院你回到这座个城市的理由是什么？"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001050.ogg"
    liuli "这个我也不太清楚，我只是接受了命令而已。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131001010.ogg"
    tyt "那花山院你自己想做的事情是什么？"
    hide tyt_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041001060.ogg"
    liuli "我希望能帮上大家的忙......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131001020.ogg"
    tyt "花山院你，真厉害~"
    show liuli_dsf_b1 b1 b1_s2
    play voice "voice/琉璃/041001090.ogg"
    liuli "并没有这回事。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131001030.ogg"
    tyt "我觉得就是这样的。"
    hide liuli_dsf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131001050.ogg"
    tyt "我至今为止都并不怎么喜欢这样的自己。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131001060.ogg"
    tyt "但是，今后或许会慢慢喜欢上也说不定。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131001070.ogg"
    tyt "看着花山院你的经历之后，我就开始这样认为了。"
    play voice "voice/藤原瞳/131001080.ogg"
    tyt "花山院帮助了我。"
    play voice "voice/藤原瞳/131001090.ogg"
    tyt "所以我也想尽我所能帮助花山院。"
    play voice "voice/藤原瞳/131001100.ogg"
    tyt "花山院为了我们人类而前往宇宙旅行的事情，我也想要为你加油。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131001110.ogg"
    tyt "我深信一定能再会的，就这样等着你。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_c1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001130.ogg"
    liuli "非常感谢你藤原同学，我也早已经不再迷茫了。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001140.ogg"
    liuli "不对......应该说还是会有迷茫，也许今后也会遇到不少的烦恼。"
    hide tyt_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n1
    play voice "voice/琉璃/041001150.ogg"
    liuli "但是，现在的我不会再逃避了。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001170.ogg"
    liuli "这也是我收获的东西。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_h1
    play voice "voice/琉璃/041001180.ogg"
    liuli "我想要亲手实现这个“并不只是为了别人，也是为了自己”的愿望。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard

label day226.memory_event01:
    "一阵歌声传来。"
    "这一刻视线被白色所包围。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg yuki ground
    show snow_level1 onlayer fg
    play music second_154 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    me01 "......这里是？"
    "曾经在翔子的共感世界里看见过的画面。"
    "这片一望无际的雪原究竟是......"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    scene set only jsqd_cg yume1
    with slowdissolve
    pause 1.0 hard
    play voice "voice/千冬/771000040.ogg"
    jsqd "等你很久了哟，凉君。"
    me01 "千冬姐？"
    me01 "不对，这种感觉......是希菲尔吗？"
    play voice "voice/千冬/771000050.ogg"
    jsqd "不是的。"
    play voice "voice/千冬/771000060.ogg"
    jsqd "你所认识的小希菲尔，并不是我。"
    "总觉得有哪里不对。"
    "看着她们就好像看着雷亚和梦一般。"
    pause 0.1 hard
    scene set only jsqd_cg yume2
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千冬/771000080.ogg"
    jsqd "说不定，你也已经从小希菲尔那里听说了。"
    pause 0.1 hard
    scene set only jsqd_cg yume3
    with dissolve
    play voice "voice/千冬/771000090.ogg"
    jsqd "就像你从小希菲尔那里听说了我的事情一样，小希菲尔也告诉了我你的事情。"
    play voice "voice/千冬/771000100.ogg"
    jsqd "过去小希菲尔每次玩耍回来的时候，都会向我讲起你的事情。"
    play voice "voice/千冬/771000110.ogg"
    jsqd "所以我也变得开始在意了，想着总有一天也要见见你。"
    pause 0.1 hard
    scene set only jsqd_cg yume1
    with dissolve
    play voice "voice/千冬/771000120.ogg"
    jsqd "一直，都想向你道谢的。"
    pause 0.1 hard
    scene set only jsqd_cg yume4
    with dissolve
    play voice "voice/千冬/771000130.ogg"
    jsqd "能和小希菲尔一起玩耍......真的谢谢你。"
    pause 0.1 hard
    scene set only jsqd_cg yume1
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千冬/771000140.ogg"
    jsqd "小希菲尔她，从刚见面的那一刻起就是一个不可思议的孩子。"
    play voice "voice/千冬/771000150.ogg"
    jsqd "洁净无瑕、没有沾染上任何的颜色的，纯白色的孩子。"
    pause 0.1 hard
    scene set only jsqd_cg yume2
    with dissolve
    play voice "voice/千冬/771000170.ogg"
    jsqd "但是，除此之外我就对她一无所知了。"
    play voice "voice/千冬/771000180.ogg"
    jsqd "因为我自己的身体一直不太好，所以也没有办法教给那孩子关于外面世界的事情。"
    pause 0.1 hard
    scene set only jsqd_cg yume3
    with dissolve
    play voice "voice/千冬/771000190.ogg"
    jsqd "可以的话，我真希望能够和小希菲尔一起到外面玩耍。"
    play voice "voice/千冬/771000200.ogg"
    jsqd "小希菲尔虽然能够出去外面，但总是只看到她一个人孤独的身影。"
    stop music fadeout 5.0
    play voice "voice/千冬/771000210.ogg"
    jsqd "所以，能够成为小希菲尔朋友的你，我是非常感谢的哟~"
    pause 0.1 hard
    play music second_134 fadein 3.0 if_changed
    scene set only jsqd_cg yume2
    with dissolve
    play voice "voice/千冬/771000260.ogg"
    jsqd "那是一个圣诞夜，母亲给我看了她带回来的，不可思议的陨石。"
    play voice "voice/千冬/771000270.ogg"
    jsqd "我被告知那是来自宇宙星辰的碎片。"
    play voice "voice/千冬/771000280.ogg"
    jsqd "所以我把它当做流星，许下了愿望。"
    play voice "voice/千冬/771000290.ogg"
    jsqd "一个想要朋友的愿望。"
    play voice "voice/千冬/771000300.ogg"
    jsqd "当时的我自己一个人的时间真的太漫长了，觉得非常的寂寞。"
    play voice "voice/千冬/771000310.ogg"
    jsqd "所以，我希望能够有谁来陪在我的身边。"
    play voice "voice/千冬/771000320.ogg"
    jsqd "在那之后，周围突然变得耀眼起来。在我回过神来的时候，已经身处这片雪原上了。"
    pause 0.1 hard
    scene set only jsqd_cg yume1
    with dissolve
    play voice "voice/千冬/771000330.ogg"
    jsqd "在纯白的世界里，邂逅了纯白的“她”。"
    play voice "voice/千冬/771000340.ogg"
    jsqd "我和小希菲尔相遇了——"
    play voice "voice/千冬/771000350.ogg"
    jsqd "我认为这一定是我的愿望实现了，因为小希菲尔是个不可思议的孩子，所以我更加那样觉得。"
    pause 0.1 hard
    scene set only jsqd_cg yume3
    with dissolve
    play voice "voice/千冬/771000390.ogg"
    jsqd "在那之后，你和小希菲尔也相遇了。"
    play voice "voice/千冬/771000400.ogg"
    jsqd "在这座雪见市。"
    pause 0.1 hard
    scene set only jsqd_cg yume1
    with dissolve
    play voice "voice/千冬/771000410.ogg"
    jsqd "这座城市是我母亲对我进行康复治疗的地方，在我治疗的时候小希菲尔偶尔也会独自跑出去。"
    play voice "voice/千冬/771000420.ogg"
    jsqd "我注意到小希菲尔她在冬天的时候比较有活力，但相对的却不太喜欢在夏天活动。"
    play voice "voice/千冬/771000430.ogg"
    jsqd "所以她一定也是最喜欢雪见市的冬天了。"
    pause 0.1 hard
    scene set only jsqd_cg yume2
    with dissolve
    play voice "voice/千冬/771000460.ogg"
    jsqd "我和小希菲尔不同，我的身体无法自由地外出行走。"
    play voice "voice/千冬/771000470.ogg"
    jsqd "也因此我才无法教她如何交朋友。"
    play voice "voice/千冬/771000480.ogg"
    jsqd "但就在那个时候。"
    play voice "voice/千冬/771000490.ogg"
    jsqd "你奇迹般地出现了，来到雪见市。"
    pause 0.1 hard
    scene set only jsqd_cg yume1
    with dissolve
    play voice "voice/千冬/771000500.ogg"
    jsqd "然后你们两个也相遇了，成为朋友。"
    play voice "voice/千冬/771000510.ogg"
    jsqd "小希菲尔非常地开心。"
    play voice "voice/千冬/771000520.ogg"
    jsqd "但在那之后，小希菲尔又和你道别了。"
    play voice "voice/千冬/771000530.ogg"
    jsqd "那时的她非常地伤心。"
    play voice "voice/千冬/771000540.ogg"
    jsqd "虽然在我面前依旧表现得很开朗，但是这样反而让我更难受了。"
    play voice "voice/千冬/771000550.ogg"
    jsqd "所以为了安慰她，我把真实的想法隐藏了起来。"
    play voice "voice/千冬/771000570.ogg"
    jsqd "告诉她不再见面的话比较好，忘记你的话就不会难过了。"
    play voice "voice/千冬/771000580.ogg"
    jsqd "告诉她这场离别是必要的。"
    pause 0.1 hard
    scene set only jsqd_cg yume2
    with dissolve
    play voice "voice/千冬/771000590.ogg"
    jsqd "也许这对于小希菲尔来说是最好的结果。"
    play voice "voice/千冬/771000600.ogg"
    jsqd "如果能够成功忘记你的话，悲伤也会跟着融化消散的吧。"
    pause 0.1 hard
    scene set only jsqd_cg yume3
    with dissolve
    play voice "voice/千冬/771000610.ogg"
    jsqd "但是那想法......果然是错误的。"
    play voice "voice/千冬/771000620.ogg"
    jsqd "我也许让小希菲尔承受了本不该由她背负的痛苦。"
    pause 0.1 hard
    scene set only jsqd_cg yume2
    with dissolve
    play voice "voice/千冬/771000630.ogg"
    jsqd "凉君，唯独这点希望你明白。"
    pause 0.1 hard
    scene set only jsqd_cg yume3
    with dissolve
    play voice "voice/千冬/771000650.ogg"
    jsqd "所以无论如何，请不要讨厌小希菲尔。"
    play voice "voice/千冬/771000670.ogg"
    jsqd "还有就是，我也想要向你道歉。"
    pause 0.1 hard
    scene set only jsqd_cg yume2
    with dissolve
    play voice "voice/千冬/771000680.ogg"
    jsqd "对不起。"
    me01 "和希菲尔成为朋友是我自己的决定。"
    me01 "我很庆幸当时的我也没有放弃。"
    me01 "既然如此现在的我自然更是如此。"
    me01 "无论发生什么，都不会改变。"
    me01 "明明知道自己不向着更好的自己而努力是不行的。"
    me01 "但是啊。"
    me01 "不希望改变的事情，果然还是存在的。"
    play voice "voice/千冬/771000700.ogg"
    jsqd "......"
    pause 0.1 hard
    scene set only jsqd_cg yume4
    $ flcam.move(1100, -1400, 450, duration=3.0, warper='ease_quad')
    with dissolve
    "女孩笑了，那是没有任何的虚假，最纯粹的笑容。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white with slowerdissolve
    pause 2.0 hard

label day226.laboratory_event04:
    $ flcam.move(0, 0, 0)
    scene set only laboratory evening inside xuejian
    with dissolve
    pause 2.0 hard
    scene set only laboratory night outside xuejian
    play music second_140 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    me01 "琉璃，你回来了吗。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001190.ogg"
    liuli "是的。"
    "一走出研究所的大门，就看到了站在门口的琉璃。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131001120.ogg"
    tyt "我也在~"
    me01 "你来这里干什么？"
    hide tyt_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b3 b3 b3_n2
    play voice "voice/琉璃/041001220.ogg"
    liuli "啊不，这些事情都不重要了，请允许我问一件事。"
    play voice "voice/琉璃/041001230.ogg"
    liuli "这里面发生了什么？"
    me01 "硬要说的话，就是某种实验吧。"
    show liuli_dsf_b3 b3 b3_sp1
    play voice "voice/琉璃/040102430.ogg"
    liuli "是这样吗？"
    me01 "就是这样的。"
    play voice "voice/琉璃/040102440.ogg"
    liuli "好厉害......这样一来谜团就解开了。"
    me01 "那太好了。"
    "琉璃还是那个天真善良的好孩子真是帮大忙了。"
    me01 "琉璃接下来打算怎么办？"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001240.ogg"
    liuli "今晚住在附近的旅馆，明天一早就要回宇宙中心去了。"
    me01 "真是辛苦你了。"
    show liuli_dsf_b1 b1 b1_h1
    play voice "voice/琉璃/041001250.ogg"
    liuli "我已经习惯了。"
    me01 "今天也能见到你真的很开心。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001260.ogg"
    liuli "是的，我也是~"
    stop music fadeout 5.0
    pause 0.5 hard
    hide liuli_dsf_b2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n2 onlayer m2:
        xpos 0.3
    play music second_104 fadein 3.0 if_changed
    play voice "voice/藤原瞳/131001140.ogg"
    tyt "前辈，也请对我说一些感动的话吧。"
    me01 "我们如果以不同形式见面的话，可能会成为好朋友的吧。"
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.25, 20):
        xpos 0.3
    play voice "voice/藤原瞳/131001150.ogg"
    tyt "无聊得想睡了啊。"
    "这家伙！"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/琉璃/041001270.ogg"
    liuli "藤原同学，是不是因为穿的太少所以想睡了？"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131001160.ogg"
    tyt "我里面之所以会是真空的，也许是因为我变得圆滑而不再讨厌色情了。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131001170.ogg"
    tyt "现在就让你见识一下吧，我不是可以被简单攻略的角色。"
    hide liuli_dsf_b2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    play sound touch
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.3
    "藤原瞳开始脱身上的巫女服。"
    pause 0.5 hard
    play sound hite_light
    show wflash onlayer texture
    with vpunch
    show tyt_wnf_b1 b1 b1_s1 at flu_down(0.15, 20):
        xpos 0.3
    "我用手刀阻止了她。"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131001180.ogg"
    tyt "这下前辈你就永远都没有办法攻略我了。"
    me01 "那我倒是得好好谢谢你才行。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131001190.ogg"
    tyt "即便如此还是想要攻略我的话，就只能氪金，然后进入隐藏剧情才行了。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131001200.ogg"
    tyt "请~"
    me01 "鬼才会做啊！"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131001210.ogg"
    tyt "我们如果是以不同形式见面的话......"
    me01 "到头来还是搞不懂你这家伙的设定啊！"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day226.laboratory_event05:
    $ flcam.move(0, 0, 0)
    scene set only laboratory night bedroom xuejian
    play music second_151 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771002800.ogg"
    jsqd "辛苦你了凉君，谈话结束了吗？"
    me01 "是啊，不过我也渐渐明白了。"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771002820.ogg"
    jsqd "明白什么了？"
    me01 "月亮和天狗邂逅的含义。"
    me01 "这大概就是我们现在的状态吧。"
    me01 "就如同月亮的阴晴圆缺一般，缺失的那部分最终会被圆满地填上。"
    me01 "因为我们和希菲尔相遇之后，{rb}灵纹{/rb}{rt}rune{/rt}就出现了。"
    me01 "我想希菲尔现在背负着孤独，就是希望有朝一日能够被我们找到吧。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002830.ogg"
    jsqd "嗯，如果真是那样的话就太好了~"
    hide jsqd_dsf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004760.ogg"
    xfe "......"
    me01 "我就知道你一定在这里，希菲尔。"
    me01 "从刚才开始我一直能够感觉得到。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show jsqd_dsf_b1 b1 b1_ga1 onlayer m1:
        xpos 0.5
    play voice "voice/千冬/771002860.ogg"
    jsqd "真是犯罪啊......"
    me01 "为什么啊！"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002870.ogg"
    jsqd "小希菲尔，从今往后你打算怎么办？"
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/001004820.ogg"
    xfe "从今往后？"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002880.ogg"
    jsqd "嗯，要像以前一样和我住在一起吗？"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771002890.ogg"
    jsqd "还是说，和凉君一起住会比较好？"
    me01 "为什么连我也算在内啊。"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771002900.ogg"
    jsqd "讨厌和小希菲尔一起住吗？"
    me01 "当然不是，不如说能够一起住的话真是太幸运了！"
    show jsqd_dsf_b1 b1 b1_ga1
    play voice "voice/千冬/771002910.ogg"
    jsqd "真是犯罪呢......"
    me01 "诱导审问吗？！"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004830.ogg"
    xfe "希菲尔我一个人也没有关系的。"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771002920.ogg"
    jsqd "小希菲尔，至今为止你都在哪里呢？"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001004840.ogg"
    xfe "在钟楼广场躲猫猫哟~"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002930.ogg"
    jsqd "已经不需要再躲着我们了。"
    show ts_xfe_yjz_b2 b2 b2_s3
    play voice "voice/希菲尔/001004850.ogg"
    xfe "但是......"
    hide ts_xfe_yjz_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/千冬/771002940.ogg"
    jsqd "凉君，小希菲尔可以拜托给你吗？"
    me01 "是要我把希菲尔带回家的意思吗？"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771002950.ogg"
    jsqd "嗯，小希菲尔的话一定不会给凉君的家人添麻烦的。"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002960.ogg"
    jsqd "最重要的是，有凉君陪着的话就会很安心，当然我也是这么觉得的。"
    me01 "和千冬姐一起住在这里不行吗？"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771002970.ogg"
    jsqd "不喜欢和小希菲尔一起住吗？"
    me01 "不......所以说这样的话当然是非常欢迎的说。"
    show jsqd_dsf_b1 b1 b1_ga1
    play voice "voice/千冬/771002980.ogg"
    jsqd "真是犯罪呢......"
    me01 "别循环啊！"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771002990.ogg"
    jsqd "小希菲尔待在这里的话，也只会承受更多的寂寞罢了，所以才要拜托给凉君。"
    me01 "星天宫那边会对希菲尔做什么不好的事情吗？"
    show jsqd_dsf_b1 b1 b1_s2
    play voice "voice/千冬/771003000.ogg"
    jsqd "母亲那边的话应该不会再做这样的事情了。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b2 b2 b2_s3 onlayer m2:
        xpos 0.3
    play voice "voice/千冬/771003010.ogg"
    jsqd "不过最重要的还是小希菲尔自己的想法。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004860.ogg"
    xfe "......"
    show jsqd_dsf_b1 b1 b1_sp1
    play voice "voice/千冬/771003020.ogg"
    jsqd "小希菲尔，想要怎么办呢？"
    show jsqd_dsf_b1 b1 b1_n1
    play voice "voice/千冬/771003030.ogg"
    jsqd "不需要多余的考虑，把心里真实的想法说出来就可以了。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001004870.ogg"
    xfe "希菲尔我想要继续待在凉君和千冬的身边。"
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771003040.ogg"
    jsqd "那就决定了~小希菲尔就待在凉君的身边吧。"
    hide jsqd_dsf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/001004890.ogg"
    xfe "可以吗？"
    me01 "当然没问题，翔子和爱衣也一定会欢迎你的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.3
    play voice "voice/希菲尔/001004910.ogg"
    xfe "凉君果然很温柔......不过，真的没关系的。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show jsqd_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/千冬/771003050.ogg"
    jsqd "小希菲尔，想来的时候再来玩吧~"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show jsqd_dsf_b1 b1 b1_h1
    play voice "voice/千冬/771003060.ogg"
    jsqd "你们两个都不需要太勉强，剩下的就交给姐姐我吧~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day226_laboratory_event01:
        $ seen_day226_laboratory_event01 = True
    $ _overworld_label = 'day226.laboratory_event01'
    jump day226.map

label day226.balltower_event02:
    $ flcam.move(0, 0, 0)
    scene set only balltower night big
    show snow_level1 onlayer fg
    with dissolve
    pause 2.0 hard
    scene set only balltower night xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001003770.ogg"
    xfe "......"
    me01 "在回去前，我能问个问题吗？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    play music second_131 fadein 3.0 if_changed
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/001003800.ogg"
    xfe "是关于千冬的事？"
    me01 "没错。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001003810.ogg"
    xfe "......"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001003850.ogg"
    xfe "从以前开始千冬就很想和凉君见面了，所以希菲尔才会决定要帮凉君带路的。"
    play voice "voice/希菲尔/001003860.ogg"
    xfe "原本的话......应该让你们早点见面的。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001003870.ogg"
    xfe "一直都希望能够三个人一起玩耍的。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001003880.ogg"
    xfe "比起一个人玩耍，两个人一定更有趣。"
    play voice "voice/希菲尔/001003890.ogg"
    xfe "要是能三个人一起的话......一定会更快乐的。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001003900.ogg"
    xfe "但结果千冬她，还是没有办法到外面来。"
    play voice "voice/希菲尔/001003910.ogg"
    xfe "而在那之后不久凉君也......不见了。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001003920.ogg"
    xfe "紧接着千冬她......也陷入了沉睡。"
    play voice "voice/希菲尔/001003930.ogg"
    xfe "全部，都是希菲尔的错。"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg daze
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001003940.ogg"
    xfe "都是因为希菲尔我的缘故大家才......"
    play voice "voice/希菲尔/001003960.ogg"
    xfe "这一切本该只是一场梦而已。"
    pause 0.1 hard
    scene set only xfe_cg sad
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001003970.ogg"
    xfe "希菲尔我到头来还是什么都不懂。"
    play voice "voice/希菲尔/001003980.ogg"
    xfe "什么都不知道，迟迟没有做出行动，才给大家带来困扰的......"
    pause 0.1 hard
    scene set only xfe_cg daze
    with dissolve
    play voice "voice/希菲尔/001003990.ogg"
    xfe "明明你们两位一直都在帮助希菲尔我。"
    play voice "voice/希菲尔/001004000.ogg"
    xfe "多亏了千冬，希菲尔才能自由地在外面行动。"
    play voice "voice/希菲尔/001004010.ogg"
    xfe "也多亏了凉君，希菲尔才明白和别人一起玩耍是多么开心的一件事。"
    pause 0.1 hard
    scene set only xfe_cg normal
    with dissolve
    play voice "voice/希菲尔/001004020.ogg"
    xfe "所以这一次......轮到希菲尔了。"
    play voice "voice/希菲尔/001004030.ogg"
    xfe "轮到希菲尔来帮助你们了。"
    pause 0.1 hard
    scene set only xfe_cg sad
    with dissolve 
    play voice "voice/希菲尔/001004170.ogg"
    xfe "已经没有办法再像这样三个人一起玩耍了。"
    play voice "voice/希菲尔/001004180.ogg"
    xfe "希菲尔也已经不再是懵懂无知的小孩子了。"
    play voice "voice/希菲尔/001004200.ogg"
    xfe "{rb}灵纹{/rb}{rt}rune{/rt}会给大家带来很大的负担。"
    play voice "voice/希菲尔/001004210.ogg"
    xfe "所以，原本身体就很差的千冬才会陷入沉睡。"
    pause 0.1 hard
    scene set only xfe_cg daze
    with dissolve
    play voice "voice/希菲尔/001004220.ogg"
    xfe "全部，都是希菲尔的错......"
    play voice "voice/希菲尔/001004230.ogg"
    xfe "如果希菲尔没有和千冬成为朋友的话，就不会让她成为{rb}灵继者{/rb}{rt}elfin{/rt}。"
    pause 0.1 hard
    scene set only xfe_cg normal
    with dissolve
    play voice "voice/希菲尔/001004240.ogg"
    xfe "千冬她告诉了希菲尔很多的事。"
    play voice "voice/希菲尔/001004250.ogg"
    xfe "读了很多书给什么都不懂的希菲尔听。"
    pause 0.1 hard
    scene set only xfe_cg angry
    with dissolve
    play voice "voice/希菲尔/001004270.ogg"
    xfe "妖精与人类和睦相处。"
    play voice "voice/希菲尔/001004280.ogg"
    xfe "但是，最后还是会引发纷争。"
    play voice "voice/希菲尔/001004290.ogg"
    xfe "希菲尔已经......不希望这种事情再次发生了。"
    play voice "voice/希菲尔/001004300.ogg"
    xfe "就算只是一点点，也想让纷争快点停止。"
    play voice "voice/希菲尔/001004310.ogg"
    xfe "仅仅只是像这样出现在你们的面前，说不定又会有谁因此而成为{rb}灵继者{/rb}{rt}elfin{/rt}。"
    pause 0.1 hard
    scene set only xfe_cg sad
    with dissolve
    play voice "voice/希菲尔/001004400.ogg"
    xfe "希菲尔已经......不想再与人变得亲近了。"
    play voice "voice/希菲尔/001004410.ogg"
    xfe "一人躲起来的话......一定更好。"
    play voice "voice/希菲尔/001004420.ogg"
    xfe "所以，只要再等忍耐一下就好。"
    pause 0.1 hard
    scene set only xfe_cg daze
    with dissolve
    play voice "voice/希菲尔/001004430.ogg"
    xfe "{rb}灵纹{/rb}{rt}rune{/rt}总有一天会融化消散。"
    play voice "voice/希菲尔/001004440.ogg"
    xfe "春天降临的话，就会和这座城市的雪一起......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    me01 "傻瓜。"
    me01 "不要说一些寂寞的话。"
    $ flcam.move(0, 0, 0)
    play sound touch
    pause 1.0 hard
    scene set only xfe_cg touch3
    play music second_134 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001004450.ogg"
    xfe "......凉君？"
    me01 "我说过的。"
    me01 "你想要逃走的话，我会像现在这样抓住你。"
    me01 "你想要藏起来的话，不管多少次我都会重新找到你。"
    me01 "虽然过去的我们也许真的什么都不懂，但现在不一样了。"
    me01 "是我们的羁绊让我能再一次遇见希菲尔。"
    me01 "曾经迷路的我们，此刻再一次相遇了。"
    me01 "所以我想说的是，妖精与人类是可以和睦相处的。"
    pause 0.1 hard
    scene set only xfe_cg touch4
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001004660.ogg"
    xfe "......"
    me01 "拜托了希菲尔。"
    me01 "请你无论如何一定要相信我所说的话。"
    me01 "如果再一次让我失去你的话，我一定会因为寂寞而死去的。"
    me01 "所以请答应我，永远留在我的身边可以吗？"
    pause 0.1 hard
    scene set only xfe_cg touch5
    with dissolve
    play voice "voice/希菲尔/001004670.ogg"
    xfe "凉君......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "天空中的雪花缓缓飘落，一片片落向地面。"
    "如果是希菲尔让这座城市降下温柔的雪。"
    "那么此刻这片澄澈的天空，一定就是她内心的写照。"
    pause 1.0 hard
    hide snow_level1
    scene set only alu_cg sky night
    with dissolve
    pause 1.0 hard
    play sound fly2
    play voice "voice/阿露/551000420.ogg"
    alu "唔莎~"
    me01 "好好的气氛都被破坏了......"
    pause 1.0 hard
    scene set only balltower night xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001004680.ogg"
    xfe "没有那回事的哟~"
    play voice "voice/希菲尔/001004690.ogg"
    xfe "阿露，看起来也很开心。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001004700.ogg"
    xfe "希菲尔曾经也尝试过和阿露道别的。但那时候阿露却对希菲尔我说了。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001004710.ogg"
    xfe "关于阿露毕蕾欧的故事......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    with dissolve
    pause 1.0 hard
    "天鹅座的β星——阿露毕蕾欧。"
    "尽管肉眼只能看得见一颗微弱的光点，但实际上却是由两颗距离很近的恒星组成的双生星。"
    "赋予阿露名字的时候，我只是希望它能够一直陪在希菲尔的身边。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower night xuejian
    show ts_xfe_yjz_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/希菲尔/001004720.ogg"
    xfe "阿露，飞走了呢。"
    me01 "也许是去寻找她的下一任主人了吧。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5 
    play voice "voice/希菲尔/001004730.ogg"
    xfe "希菲尔我还不想放弃。"
    play voice "voice/希菲尔/001004740.ogg"
    xfe "妖精与人类，是可以和睦相处的。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001004750.ogg"
    xfe "能不能再一次......相信它呢。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day226_balltower_event02:
        $ seen_day226_balltower_event02 = True
    $ _overworld_label = 'day226.balltower_event02'
    jump day226.map

label day226.myroom_event01:
    $ flcam.move(0, 0, 0)
    scene set only home night my_room xuejian
    play music second_105 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/希菲尔/001005130.ogg"
    xfe "这里就是凉君的房间吗？"
    me01 "猜到了吗。"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001005140.ogg"
    xfe "嗯~因为我一直都在看着凉君的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005150.ogg"
    xfe "凉君，接下来要睡了吗？"
    me01 "嗯，希菲尔也一起吧。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005160.ogg"
    xfe "但是......被子只有一床。"
    me01 "那就给希菲尔好了，我的话就算不盖被子也没问题的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005170.ogg"
    xfe "不行的啦，这样的话凉君会感冒的。"
    me01 "那要怎么办才好？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005180.ogg"
    xfe "希菲尔在哪里都可以睡的哟~"    
    me01 "那我们是一样的。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001005190.ogg"
    xfe "嗯~"
    me01 "哪里都可以的话，和我一起睡也可以吧？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005200.ogg"
    xfe "嗯，没问题......的哟。"
    me01 "那就这么定了。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard

    scene set only home night my_room xuejian
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu ts_xfe_yjz_b2 onlayer m2:
            hide screen investigation_popup
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction left
            sleep jump day226.sleep

label day226.sleep:
    menu:
        "早点休息":
            $ flcam.move(0, -300, 1000, duration=1.5)
            show ts_xfe_yjz_b2 b2 b2_h1
        "{#cancel}再等等":
            xfe "还有什么事情要考虑吗......"
            $ flcam.move(0, -100, 400, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene white
    with slowdissolve
    pause 2.0 hard
    jump day226.memory_event02

label day226.memory_event02:
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    nvl clear
    pcenter "就这样，我们做了同一个梦——"
    pause 0.5 hard
    nvl clear
    with dissolve
    play music second_155 fadein 3.0 if_changed
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg yuki ground
    show snow_level1 onlayer fg
    with slowdissolve
    $ flcam.move(0, 0, 900, duration=15.0, warper='ease_cubic')
    "梦里是那片不可思议的雪原。"
    "四周都是飘落的白雪。"
    "虽然在下着雪，却一点都没有觉得寒冷。"
    "就是这样一个温柔，却又有些寂寞的世界。"
    pause 1.0 hard
    show ts_xfe_yjz_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005220.ogg"
    xfe "希菲尔在那颗星球上最喜欢的季节，就是冬天了哟~"
    me01 "那颗星球是？"
    show ts_xfe_yjz_b2 b2 b2_n4
    play voice "voice/希菲尔/001005230.ogg"
    xfe "那是从这里用肉眼看不到的，遥远的星球......"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001005240.ogg"
    xfe "蓝色的余晖，与这颗星球的黄昏拥有一样颜色的——蓝色的星球。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001005250.ogg"
    xfe "与这颗白色星球最相似的季节，就是那颗蓝色星球上的冬天了。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    "我们在这纯白的世界里手牵着手向前迈进。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory one
    with slowdissolve
    pause 1.0 hard
    "天地皆白。"
    "分不清是白天还是夜晚。"
    "两人在没有昼夜的雪道上前行。"
    "我的脑海里闪过曾经一起撑伞漫步时的画面。"
    play voice "voice/希菲尔/001005260.ogg"
    xfe "凉君......"
    pause 0.1 hard
    scene set only xfe_cg memory four
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005280.ogg"
    xfe "对不起，凉君。"
    play voice "voice/希菲尔/001005290.ogg"
    xfe "谢谢你，凉君。"
    me01 "我更喜欢这个。"
    pause 0.1 hard
    scene set only xfe_cg memory three
    with dissolve
    play voice "voice/希菲尔/001005300.ogg"
    xfe "......欸？"
    me01 "比起道歉，我更喜欢被感谢。"
    pause 0.1 hard
    scene set only xfe_cg memory two
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005310.ogg"
    xfe "嗯。"
    play voice "voice/希菲尔/001005320.ogg"
    xfe "谢谢你，凉君。"
    pause 0.1 hard
    scene set only xfe_cg memory one
    with dissolve
    "希菲尔转过身来。"
    "踮起脚尖，将脸凑了过来。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "随即在我的额头上吻了一下。"
    "与小时候在观景台和翔子道别的时候一样。"
    "那是希望和约定的象征。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory one
    with dissolve
    me01 "希菲尔知道亲吻的涵义吗？"
    pause 0.1 hard
    scene set only xfe_cg memory two
    with dissolve
    play voice "voice/希菲尔/001005330.ogg"
    xfe "千冬读过的书里面有出现过。"
    me01 "那么你觉得是哪一种意思呢？"
    pause 0.1 hard
    scene set only xfe_cg memory three
    with dissolve
    play voice "voice/希菲尔/001005340.ogg"
    xfe "有很多种吗？"
    me01 "是啊。"
    pause 0.1 hard
    scene set only xfe_cg memory one
    with dissolve
    play voice "voice/希菲尔/001005350.ogg"
    xfe "那......希望凉君也能教希菲尔一下。"
    me01 "可以吗？"
    pause 0.1 hard
    scene set only xfe_cg memory two
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005360.ogg"
    xfe "嗯，也想要了解凉君的心意。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "这次换成我在希菲尔的脸颊上亲吻了一下。"
    pause 1.0 hard
    $ flcam.move(-1100, -1400, 450)
    scene set only xfe_cg memory one
    with dissolve
    play voice "voice/希菲尔/001005370.ogg"
    xfe "刚刚的就是......亲吻的含义。"
    play voice "voice/希菲尔/001005380.ogg"
    xfe "凉君教给我的，亲吻......"
    pause 0.1 hard
    scene set only xfe_cg memory two
    with dissolve
    play voice "voice/希菲尔/001005390.ogg"
    xfe "希菲尔虽然一直都是懵懂的白色。"
    pause 0.1 hard
    scene set only xfe_cg memory five
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001005400.ogg"
    xfe "但是和凉君在一起的话，说不定就会沾染上凉君的颜色也说不定呢~"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day227
