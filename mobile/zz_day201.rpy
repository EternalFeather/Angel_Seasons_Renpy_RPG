label day201:
    bookmark
    $ renpy.show_screen("disable_inputs_for_replay", _layer="key")
    
    $ save_name = _("Day 201")
    $ _window_subtitle = " - 希菲尔（冬之妖精）"
    play sound "sound/system/second_menu.wav"
    scene black with Dissolve(8.0)

    $ persistent.youjia = False
    $ persistent.szl_ling = False
    $ persistent.lihuaxi = False
    $ persistent.liuli = False
    $ persistent.xifeier = False
    $ persistent.lisite = False
    $ persistent.lingyin = False

    pause 4.0 hard
    $ suppress_overlay = True

    play music ["<silence 2.411>", "<to 55.348 loop 0>music/prologue.ogg"]
    scene set only sky snow day xuejian
    show snow onlayer texture
    show white onlayer texture:
        alpha 0.3 additive 1
        linear 2.0 alpha 0
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
        on hide:
            1.5
            ease_cubic 3.0 yzoom scale(1.32)

    show screen disable_inputs
    $ flcam.move(0, 0, 0)
    $ renpy.transition(slowdissolve)
    pause 2.0 hard

    hide white
    python hide:
        import re

        sections = parse_monologue('title/system/prologue.txt')
        start_end = False
        for section in sections:
            mode = None
            pause_duration = None

            slow_match = re.match(r'^((?:slow)|(?:slower)) +(?:(\d+)s)?', section.options)
            if slow_match:
                mode = slow_match.group(1)
                pause_duration = int(slow_match.group(2))
                if start_end is False:
                    start_end = True
            
            cam_match = re.match(r'^(\d+)% +(\d+)s', section.options)
            if cam_match:
                cam_percent = 0.01 * int(cam_match.group(1))
                cam_duration = int(cam_match.group(2))
                flcam.move(
                    0,
                    0,
                    400 * (cam_percent),
                    duration=cam_duration,
                    warper='ease_quad')
            
            if start_end:
                renpy.hide('cinemascope', layer='texture')
                renpy.music.stop(fadeout=2.0)
                renpy.pause(3.0, hard=True)
                renpy.music.play(
                    '<from 54.479>music/prologue.ogg',
                    fadein=2.0,
                    loop=False)
                start_end = None
            
            renpy.hide_screen('prologue')
            renpy.show_screen(
                'prologue',
                text='\n'.join(' '.join(t[1]) for t in section.lines),
                duration=pause_duration,
                mode=mode,
                is_last=section is sections[-1])
            
            renpy.pause(pause_duration, hard=not pause_duration)

    hide screen prologue
    $ flcam.move(0, 0, 0)
    scene white with None
    show sky_logo1 onlayer texture at sky_logo1_func
    show sky_logo2 onlayer texture at sky_logo2_func

    pause 3.0 hard

    show black onlayer b1
    with slowerdissolve

    pause 3.5 hard

    hide screen disable_inputs
    $ renpy.end_replay()

    scene black
    with slowerdissolve

    jump day201_2


screen prologue(text, duration=None, mode=None, is_last=False):
    default hiding = False

    if not duration:
        key "dismiss" action SetScreenVariable("hiding", True)

    if hiding:
        timer 1.0 action Return()

    text "[text]" style "prologue_text":
        if mode == "slower":
            style "prologue_slower_text"
        elif mode == "slow":
            style "prologue_slow_text"

        if duration is not None:
            at prologue_text_fade(
                pause_duration=duration,
                in_duration=1.0,
                out_duration=float(not is_last))
        elif not hiding:
            at prologue_text_fadein
        else:
            at prologue_text_fadeout
            slow_cps False

image white = Solid("#fff")
image sky_logo1 = "title/system/logo1.png"
image sky_logo2 = "title/system/logo2.png"

transform sky_logo1_func:
    xcenter 0.5 ycenter 0.5 alpha 1.0
    imagescale(720)
    parallel:
        linear 10.0 zoom 1.65
    parallel:
        4.0
        linear 1.0 alpha 0.0
        5.0

transform sky_logo2_func:
    xcenter 0.5 ycenter 0.5 alpha 0.0
    imagescale(720)
    parallel:
        linear 10.0 zoom 1.65
    parallel:
        4.5
        ease_cubic 1.0 alpha 1.0 
        5.5
        linear 1.0 alpha 0.0


transform prologue_text_fadein:
    alpha 0
    linear 1.0 alpha 1

transform prologue_text_fadeout:
    linear 1.0 alpha 0

transform prologue_text_fade(pause_duration, in_duration, out_duration):
    alpha 0
    linear in_duration alpha 1
    max(0.0, pause_duration - in_duration - out_duration)
    linear out_duration alpha 0

style prologue_text is text:
    xmaximum scale(1110) xcenter 0.5 ycenter 0.5
    font "9i/fonts/浪漫雅圆.ttf"
    size scale(27)
    line_leading scale(6)
    line_spacing scale(6)
    line_overlap_split scale(0)
    color "#fff"
    outlines [(absolute(scale(1.5)), "#333")]
    slow_cps True
    
translate None style prologue_text:
    xmaximum scale(1035)
    size scale(35)
    kerning scale(-1.5)
    line_leading scale(6)
    line_spacing scale(6)
    line_overlap_split scale(-3)

style prologue_slow_text is prologue_text xmaximum None slow_cps 45
translate None style prologue_slow_text slow_cps 36
style prologue_slower_text is prologue_text slow_cps 25
translate None style prologue_slower_text slow_cps 20


label day201_2:
    bookmark
    $ suppress_overlay = False
    stop music fadeout 4.0
    pause 4.0 hard

    $ renpy.block_rollback()
    $ _rollback = True

    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with slowerdissolve
    show snow_level1 onlayer fg
    play music second_102 if_changed
    pause 1.0 hard
    "下雪了。"
    "澄澈的天空飞舞着如同棉絮般纯白的雪花。"
    "结束了在樱华中学学习生涯的我，此刻决定前往升学的目的地——雪见市。"
    "虽说早在半年前便得知翔子已经提前一步来到了这里。"
    "更加巧合的是我们所选择的学校也是同一所。"
    "而我却因为选择留在樱华镇继续寻找雷亚下落的缘故姗姗来迟。"
    "尽管费尽心力却还是一无所获。"
    "从雷亚消失的那个晚上算起也已经过去有一段时间了。"
    "虽说告别对我而言也并不陌生，但是对于离别的不舍还是十分强烈的。"
    "儿时的我也曾跟随父亲来到过雪见市。"
    "虽然这里留给我的印象不是非常深刻，但是多少也有点开始怀念了。"
    "上一次有这种感觉又是什么时候的事呢......"
    "虽然过去的我身边发生了各种各样的事。"
    "而今天，我也终于也要踏上新的旅程了——"
    python:
        local_config = Localturn_params()
        if persistent.development:
            # 金币
            local_config.player.currency = 1000000
            # 道具
            for name in ["soul_piece", 
                         "soul_raise", 
                         "water_break_small", 
                         "water_break_large", 
                         "wind_break_small", 
                         "wind_break_large",
                         "rock_break_small",
                         "rock_break_large",
                         "fire_break_small",
                         "fire_break_large",
                         "ice_break_small",
                         "ice_break_large",
                         "light_break_small",
                         "light_break_large"]:
                local_config.player.items[name] = 99
            # 装备
            legend_equips = [outfit for outfit in outfit_list if "_04" in outfit.objectname]
            for equip in legend_equips:
                for i in range(3):
                    equip.get(who=local_config.player)


label day201_2.bridge_event01:
    pause 1.0 hard
    scene set only bridge day xuejian
    with slowdissolve
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('chapter one'), _("这场雪，宛若恋歌"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard
    "一边回忆着过去的都市生活，我一边向着这次的目的地进发。"
    "走在这座桥上的场景过去也有过吗？"
    "桥的另一头是一片陌生的光景。"
    me01 "改变已经超出了我的想象啊。"
    "稍微驻足了片刻后我加快了脚步，需要赶在天黑前找个能够落脚的地方。"
    pause 1.0 hard
    scene set only sky day xuejian
    with slowdissolve
    pause 1.0 hard
    "雪下得不大，这份寒冷还在能够忍受的范围之内。"
    "雪花落在手心里，在留下寒意之前马上就会融化。"
    stop music fadeout 5.0
    pause 0.5 hard
    play voice "voice/希菲尔/000000050.ogg"
    stranger "凉君——"
    pause 1.0 hard
    $ flcam.move(1000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.25
        linear 0.75 alpha 1
    pause 5.0 hard
    play music second_103 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    hide snow_level1
    scene set only xfe_cg bridge normal
    with slowdissolve
    pause 0.5 hard
    "让人怀念的声音。"
    "不知是什么时候，少女带着纯洁的笑容出现在了我的眼前。"
    "周围很安静，就连风的声音都听不见，没有车辆，也没有行人。"
    "这一切让眼前的一幕看起来仿佛就像是置身于只属于我们两人的世界中一般。"
    me01 "好久不见。"
    play voice "voice/希菲尔/000000060.ogg"
    stranger "嗯，好久不见。"
    play voice "voice/希菲尔/000000070.ogg"
    stranger "凉君，你长高了？"
    play voice "voice/希菲尔/000000080.ogg"
    stranger "感觉已经相当长的时间没有见到凉君了。"
    play voice "voice/希菲尔/000000090.ogg"
    stranger "但是，却有种昨天才刚见过面的感觉。"
    play voice "voice/希菲尔/000000100.ogg"
    stranger "所以呢，无论凉君改变多少、成长多少，我也是能注意到的。"
    pause 0.1 hard
    scene set only xfe_cg bridge happy
    with dissolve
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/希菲尔/000000110.ogg"
    stranger "希菲尔我呢，对“凉君就是凉君”这一点还是很清楚的。"
    "女孩说的话幼稚得令我有种想笑的冲动。"
    "但还是忍住了，取而代之的只是呼出了一团白雾。"
    me01 "希菲尔倒是一点都没变。"
    pause 0.1 hard
    scene set only xfe_cg bridge normal
    with dissolve 
    play voice "voice/希菲尔/000000120.ogg"
    xfe "希菲尔我一直都是这样的。从很久以前开始就一直都没有改变。"
    play voice "voice/希菲尔/000000130.ogg"
    xfe "因为发现了凉君，所以过来打个招呼。"
    me01 "这座桥的另一头，希菲尔你知道吗？"
    play voice "voice/希菲尔/000000140.ogg"
    xfe "知道哟，该怎么说呢......最近也改变了许多。"
    me01 "要一起去看看吗？"
    play voice "voice/希菲尔/000000150.ogg"
    xfe "还是不要看比较好。"
    play voice "voice/希菲尔/000000160.ogg"
    xfe "那边已经，改变太多了。"
    "希菲尔的声音有些失落。"
    pause 0.1 hard
    scene set only xfe_cg bridge daze
    with dissolve
    play voice "voice/希菲尔/000000170.ogg"
    xfe "改变了的东西多了，就会觉得寂寞。"
    play voice "voice/希菲尔/000000180.ogg"
    xfe "虽说永恒不变的东西，也许根本就不存在于这个世界上。"
    play voice "voice/希菲尔/000000190.ogg"
    xfe "就算是这座{encyclopedia=xuejian}雪见市{/encyclopedia}，大概也不例外吧。"
    pause 0.1 hard
    scene set only xfe_cg bridge normal
    with dissolve
    play voice "voice/希菲尔/000000200.ogg"
    xfe "但是呢，不想改变的东西果然还是存在的。"
    play voice "voice/希菲尔/000000210.ogg"
    xfe "也许凉君也的确改变了没错，但是对于希菲尔来说凉君却是没有改变的。"
    pause 0.1 hard
    scene set only xfe_cg bridge sad
    with dissolve
    play voice "voice/希菲尔/000000220.ogg"
    xfe "就像在凉君眼中的希菲尔一直都没有改变一样。"
    pause 0.1 hard
    scene set only xfe_cg bridge normal
    with dissolve
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/000000230.ogg"
    xfe "如果真是这样就好了，我是这么觉得的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only bridge day xuejian
    with slowdissolve
    show snow_level1 onlayer fg
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/希菲尔/000000240.ogg"
    xfe "这座桥，要过去吗？"
    me01 "是啊。"
    play voice "voice/希菲尔/000000250.ogg"
    xfe "凉君，其他的事情都处理完了吗？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian
    with dissolve
    pause 1.0 hard
    "雪花依旧飘落。"
    "马上就要入夜了。"
    pause 2.0 hard
    $ flcam.move(0, 0, 900)
    scene set only bridge day xuejian
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    me01 "虽然不知道你指的是什么，但总会有办法的。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000000260.ogg"
    xfe "要跟希菲尔玩吗？"
    me01 "现在的话还不是时候。"
    show ts_xfe_yjz_b2 b2 b2_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000000270.ogg"
    xfe "那下次，再一起玩吧~"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000000280.ogg"
    xfe "如果......可以的话。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/000000290.ogg"
    xfe "拜拜~"
    hide snow_level1
    pause 2.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    "说完，希菲尔的身影消失在了白雪之中。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day201_2.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with slowdissolve
    show snow_level1 onlayer fg
    pause 2.0 hard
    scene set only home evening outside xuejian
    with dissolve
    pause 2.0 hard
    "一诚给我的地址，应该就是这里了吧。"
    "临行前提前向他打听了这附近的住所情况。"
    "虽然总觉得哪里怪怪的，但因为物美价廉的关系就随口答应了。"
    "现在看来这里的确是物超所值啊。"
    $ flcam.move(0, -100, 400, duration=1.5)
    play sound menling
    pause 2.0 hard
    "这样想着我按响了门铃。"
    "不过话说回来，这旅社怎么看着有点像是私人公寓的样子。"
    pause 1.0 hard
    play sound open_door4
    pause 0.5 hard
    "门开了。"
    hide snow_level1
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening passwalk xuejian
    play music second_104 fadein 3.0 if_changed
    $ flcam.move(0, -200, 600, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/翔子/010000010.ogg"
    xz "你好，请问是哪位？"
    me01 "......翔子？！"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010000030.ogg"
    xz "......"
    me01 "哟，好久不见。"
    play voice "voice/翔子/010000040.ogg"
    xz "......"
    me01 "那个，其实我......"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010000050.ogg"
    xz "请回吧。"
    me01 "欸？"
    "一定是哪里搞错了。"
    "她这是......在赶我走吗？"
    $ camera_move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_a1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010000060.ogg"
    xz "{size=72}请你回去！{/size}"
    show wflash onlayer texture
    with vpunch
    pause 0.5 hard
    me01 "等等，别推我啊！"
    pause 1.0 hard
    scene black
    with right2left_02
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only home evening outside xuejian
    with right2left_02
    show snow_level1 onlayer fg
    play sound close_door2
    pause 1.0 hard
    "门被重重地关上了。"
    me01 "那个......"
    $ flcam.move(0, -100, 400, duration=1.5)
    play sound menling
    pause 2.0 hard
    "我再次按下门铃。"
    "然而等待了许久也没有回应。"
    "这次选择无视吗。"
    me01 "到底是怎么回事啊？！" with vpunch
    "不觉得自己做了什么会被翔子讨厌的事。"
    "时隔半年的第一次见面竟如此地尴尬，这可不是什么好的开始。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with slowdissolve
    pause 1.0 hard
    "晚霞的余晖已经映红了天际，到了晚上还留在外面的话一定会被冻僵的。"
    "而且说不定还会被认为是可疑人物。"
    "总之还是设法在天黑之前到附近找找有没有其他旅社之类的地方吧。"
    "再这样下去，今晚说不定真要露宿街头了。"
    pause 1.0 hard
    play sound open_door4
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only home evening outside xuejian
    with dissolve
    pause 1.0 hard
    show xz_dsf_b3 b3 b3_s1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/翔子/010000070.ogg"
    xz "......"
    "就在我刚决定离开的时候，门又一次打开了。"
    play sound jiaobu2
    show xz_dsf_b3 b3 b3_s1 onlayer m2 at walkout_l(0.5)
    pause 0.5 hard
    hide xz_dsf_b3
    "本以为是翔子反悔了，然而她却径直从我的身旁走过。"
    "都这个时候了，这是要去哪里？"
    "虽说仍旧是一副爱答不理的样子。"
    "混蛋一诚让我这般难堪，下次一定饶不了你！"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard

label day201_2.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street evening road1 xuejian
    with slowdissolve
    show snow_level1 onlayer fg
    play music second_102 fadein 3.0 if_changed
    pause 2.0 hard
    play ambience1 jiaobu2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    "不知不觉地跟在箱翔子的身后走着。"
    "周围全都是陌生却又略显熟悉的景象。"
    "没想到短短的几年时间就已经不再是我记忆中的模样了。"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg bridge normal
    show sepiagrain onlayer texture
    with dissolve
    pause 0.5 hard
    "说实话虽说知道对方的名字，但那位名叫希菲尔的女孩给我的印象是完全没有改变。"
    "如果真是我儿时遇到的玩伴，那此时我们的年纪应该是相仿的才对。"
    "想到这里脑海里突然浮现出了“死神才没有年龄”这样的回复。"
    "真是不可思议啊。"
    "至于她说的“没有改变”又是怎么一回事呢。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only street evening road1 xuejian
    with dissolve
    show snow_level1 onlayer fg
    pause 1.0 hard
    me01 "话说回来......"
    $ flcam.move(-2800, -1400, 600, duration=1.5)
    pause 2.0 hard
    $ flcam.move(2800, -1400, 600, duration=1.5)
    pause 2.0 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    me01 "这里......{w=1.0}{nw}"
    extend "{size=+6}是{/size}{w=0.33}{nw}"
    $ flcam.move(0, -150, 500, duration=0.33)
    extend "{size=+6}哪{/size}{w=0.33}{nw}"
    $ flcam.move(0, -200, 600, duration=0.33)
    extend "{size=+8}里！{/size}"
    with vpunch
    "回过神来的时候已经找不到翔子的身影了。"
    "我跟丢了？"
    "这是何等的失态！"
    "眼瞅着天色越来越暗，必须赶紧找人问下路才行。"
    pause 1.0 hard

label day201_3:
    play ambience1 zhong_rill
    pause 3.5 hard
    "就在这时不远处一阵钟声响起。"
    me01 "总之先去看看吧，说不定还能找个人问问。"
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day201_3'
    $ seen_day201_3_cloqks = False
    $ seen_day201_3_kindergarden_event01 = False

label day201_3.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter evening
    show snow_level1 onlayer fg
    if _overworld_label == 'day201_3':
        $ flcam.move(6100, -1800, 2800)
    elif _overworld_label == 'day201_3.cloqks':
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day201_3.kindergarden_event01':
        $ flcam.move(*_overworld.camera_positions['kindergarden'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    if _overworld_label == 'day201_3':
        show screen investigation_popup(investigation.preg3)
        window mode map
        me01 "现在要去哪里好呢......" nointeract
    elif _overworld_label == 'day201_3.cloqks':
        window mode map
        me01 "现在还是先带孩子们回幼儿园吧。" nointeract
    call screen rughzenhaide(
        cloqks=("day201_3.cloqks", "not seen_day201_3_cloqks"),
        kindergarden=("day201_3.kindergarden_event01", "seen_day201_3_cloqks and not seen_day201_3_kindergarden_event01"))
    $ window_animate_outro()
    if _return == 'day201_3.cloqks':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    elif _return == 'day201_3.kindergarden_event01':
        $ flcam.move(*overworld.camera_positions['kindergarden'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        hide snow_level1
        scene black with dissolve
    $ _window_animation = None
    hide screen investigation_popup
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day201_3.cloqks:
    $ flcam.move(0, 0, 0)
    scene set only balltower snow evening xuejian
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    "顺着钟声的方向，我来到了一座钟楼底下。"
    "可这里除了几个玩耍的小孩子之外并没有其他人。"
    "这么冷的天还跑到外面来吗。"
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    me01 "那个，可以打扰一下吗。"
    play voice "voice/爱衣/110000010.ogg"
    stranger "？"
    me01 "我不是坏人的，能告诉我你的名字吗？"
    "一开口就是诱拐犯的口吻，不妙啊。"
    "就在我为自己不谨慎的发言而懊恼时，女孩却冲我笑了。"
    play music second_105 fadein 3.0 if_changed
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110000020.ogg"
    stranger "可以啊，我叫爱衣，日向爱衣~"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110000030.ogg"
    aiyi "大哥哥你是谁？"
    me01 "初次见面，我的名字叫神野凉。"
    play voice "voice/爱衣/110000040.ogg"
    aiyi "哈鲁哈鲁~凉君？"
    me01 "是神野凉啦。"
    play voice "voice/爱衣/110000050.ogg"
    aiyi "哈鲁哈鲁你找爱衣我有什么事吗？"
    me01 "这样的称呼还是有点......"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/爱衣/110000060.ogg"
    aiyi "那就叫凉君~"
    "听到了对方称呼我为“凉君”的那一刻，脑海里不禁浮现出了雷亚的身影。"
    $ flcam.move(-4500, 300, 1000, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 at flu_down(0.35, 20):
        xpos 0.3
    play sound touch
    pause 0.5 hard
    play voice "voice/爱衣/110000070.ogg"
    aiyi "啊......"
    "不知不觉中我已经开始抚摸爱衣的头了。"
    "是某种怀念的感觉让我不自觉地陷入无意识的状态吗。"
    me01 "抱歉。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/110000080.ogg"
    aiyi "没、没事。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/110000090.ogg"
    aiyi "嘿嘿~"
    stop music fadeout 5.0
    hide aiyi_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound appear
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/千波/210000010.ogg"
    stranger "喂！那边的可疑分子！"
    play music second_106 fadein 3.0 if_changed
    hide qianbo_dzf_b1
    play sound jump_1
    show qianbo_dzf_b2 b2 b2_a3 onlayer m2 at flu_up(0.15, 30):
        xpos 0.5
    play voice "voice/千波/210000020.ogg"
    stranger "你在对爱衣做什么啊！"
    pause 0.5 hard
    $ flcam.move(-2250, 300, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110000100.ogg"
    aiyi "千波。"
    "就在我陶醉之际，名叫千波的女孩打断了我们。"
    "她像是要保护同伴一般挡在了我与爱衣之间。"
    hide aiyi_dzf_b1
    hide qianbo_dzf_b2
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_n2 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    "在她的身后还跟着另一名女孩，只见她畏畏缩缩地站在远处注视着我。"
    "手里紧紧地抱着一个布偶，看上去十分怕生的样子。"
    hide ycxt_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    show qianbo_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    play voice "voice/千波/210000030.ogg"
    qb "这个男人，是诱拐犯吧。"
    me01 "才不是！"
    show qianbo_dzf_b1 b1 b1_ga2
    play voice "voice/千波/210000040.ogg"
    qb "难不成你对爱衣一见钟情了？"
    me01 "谁会对小孩子一见钟情啊。"
    show qianbo_dzf_b1 b1 b1_ga1
    play voice "voice/千波/210000050.ogg"
    qb "难道说难道说，是对人家吗？"
    me01 "你怎么看也是小孩子吧。"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_h3 at flu_down(0.35, 30):
        xpos 0.5
    play voice "voice/千波/210000060.ogg"
    qb "因为是小孩子就把我当笨蛋吗？最近的小孩子发育可是很好的。"
    "名叫千波的女孩在一旁卖弄着自己的姿色，现在的小孩子都不知道在想些什么。"
    "在她身上除了“小屁孩”的影子其他什么都看不到。"
    show qianbo_dzf_b1 b1 b1_ga2
    play voice "voice/千波/210000070.ogg"
    qb "下流的眼神呢。"
    me01 "虽然很抱歉但那绝对是扫兴的眼神。"
    $ flcam.move(2250, 300, 750, duration=1.5)
    show ycxt_dzf_b1 b1 b1_s4 onlayer m2:
        xpos 0.7
    play voice "voice/小桃/220000010.ogg"
    stranger "要诱拐，小桃我们吗......"
    show qianbo_dzf_b1 b1 b1_h2
    play voice "voice/千波/210000080.ogg"
    qb "是啊，我们今天就要被这个男人强暴了！"
    show ycxt_dzf_b1 b1 b1_c1 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/小桃/220000020.ogg"
    ycxt "呜......"
    play sound jump_1
    hide qianbo_dzf_b1
    show qianbo_dzf_b2 b2 b2_a3 onlayer m2 at flu_up(0.15, 30):
        xpos 0.5
    play voice "voice/千波/210000090.ogg"
    qb "喂！别把小桃弄哭啊！"
    me01 "这是我的错吗？！"
    hide qianbo_dzf_b2
    hide ycxt_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110000110.ogg"
    aiyi "大哥哥不是坏人啦，他只是摸了爱衣的头而已。"
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    $ flcam.move(-2250, 300, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/小桃/220000030.ogg"
    ycxt "不是诱拐犯吗？"
    show aiyi_dzf_b1 b1 b1_a1
    play voice "voice/爱衣/110000120.ogg"
    aiyi "不是啦，是千波她搞错了。"
    pause 0.5 hard
    hide aiyi_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    show qianbo_dzf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/千波/210000100.ogg"
    qb "爱衣、小桃，不能被骗了。所有的男人都是狼啊。"
    show qianbo_dzf_b1 b1 b1_n2
    play voice "voice/千波/210000110.ogg"
    qb "就算他拿点心也不能跟着走哟，这里交给我你们两个快点逃！"
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_h2 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, 300, 750, duration=1.5)
    pause 0.5 hard
    play sound yangmu
    show yangmu onlayer m2:
        xalign 0.71 yalign 0.52 zoom 0.7
    play voice "voice/小桃/220000040.ogg"
    ycxt "千波好帅~"
    show qianbo_dzf_b1 b1 b1_a1
    play voice "voice/千波/210000120.ogg"
    qb "行了那边的可疑分子，让我来做你的对手，绝不会让你碰她们一根手指的！"
    hide yangmu
    hide ycxt_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    hide qianbo_dzf_b1 with None
    pause 0.1 hard
    show qianbo_dzf_b2 b2 b2_sp1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    me01 "真乖真乖。"
    play sound jump_1
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at flu_up(0.15, 30):
        xpos 0.5
    play voice "voice/千波/210000130.ogg"
    qb "别摸我的头啊！"
    pause 0.5 hard
    stop music fadeout 5.0
    hide qianbo_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110000130.ogg"
    aiyi "大哥哥找我们有事对吧？"
    me01 "啊对了！"
    play music second_107 fadeout 3.0 if_changed
    me01 "关于今晚住宿的问题......"
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    $ flcam.move(-2250, 300, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/小桃/220000050.ogg"
    ycxt "啊......已经到该回去的时间了？"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110000140.ogg"
    aiyi "已经这么晚了。大哥哥你是来接我们回去的吗？"
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_a1 onlayer m2 at walkin_r(0.7)
    $ flcam.move(0, 200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/千波/210000140.ogg"
    qb "真是让人笑掉大牙了！"
    me01 "你到底想怎样！"
    show qianbo_dzf_b1 b1 b1_ga2
    play voice "voice/千波/210000150.ogg"
    qb "非常老套的手段，用花言巧语勾引我们，然后对我们做一些不正经的事情。"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_ga2 at flu_down(0.35, 20):
        xpos 0.7
    me01 "真乖真乖~"
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 at flu_up(0.15, 30):
        xpos 0.7
    play voice "voice/千波/210000160.ogg"
    qb "别把我当成小孩子！"
    me01 "话说回来，你们在这里做什么？"
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    show ycxt_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    $ flcam.move(0, 200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/爱衣/110000150.ogg"
    aiyi "那个，因为下雪了所以就想来堆雪人玩。"
    show ycxt_dzf_b1 b1 b1_h1
    play voice "voice/小桃/220000060.ogg"
    ycxt "这里的话比起幼儿园更宽敞。"
    show ycxt_dzf_b1 b1 b1_n2
    play voice "voice/小桃/220000070.ogg"
    ycxt "千波说，比起幼儿园这里更好玩。"
    hide ycxt_dzf_b1
    hide aiyi_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    play sound hite_light
    hide qianbo_dzf_b1
    show qianbo_dzf_b2 b2 b2_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    me01 "果然你是主谋吗！"
    play sound jump_1
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_c1 onlayer m2 at flu_up(0.15, 30):
        xpos 0.7
    show han onlayer m2:
        xalign 0.73 yalign 0.48
    play voice "voice/千波/210000170.ogg"
    qb "别敲我的头啊！！"
    hide han
    hide qianbo_dzf_b1
    $ flcam.move(-2250, 300, 750, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.3
    show ycxt_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110000160.ogg"
    aiyi "这里平时也很少有人来，所以积了很多雪哟~"
    play voice "voice/小桃/220000080.ogg"
    ycxt "幼儿园广场上的积雪，都是大家的脚印......"
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_h2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    $ flcam.move(0, 200, 600, duration=1.5)
    play voice "voice/千波/210000180.ogg"
    qb "就是这样，这里是我们的地盘啦，人家是天才吧~"
    "平坦的胸向前一挺。"
    me01 "不过好像也没积多少雪。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/110000170.ogg"
    aiyi "确实是这样......"
    show ycxt_dzf_b1 b1 b1_s1
    play voice "voice/小桃/220000090.ogg"
    ycxt "明明下了一整天雪了。"
    hide qianbo_dzf_b1
    show qianbo_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210000190.ogg"
    qb "这些雪很快就融化了，都是这个男人打扰我们的错。"
    me01 "为什么又是我的错啊，还有不要用“这个男人”来称呼我。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110000180.ogg"
    aiyi "凉君，他叫“凉君”哟~"
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_sp1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/210000200.ogg"
    qb "凉君男？"
    me01 "才不是那么奇怪的名字！"
    show ycxt_dzf_b1 b1 b1_sp1
    play voice "voice/小桃/220000100.ogg"
    ycxt "凉君先生？"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/110000190.ogg"
    aiyi "才不行呢，凉君就是凉君。"
    hide qianbo_dzf_b1
    hide ycxt_dzf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    show aiyi_dzf_b1 b1 b1_h1
    pause 0.5 hard
    play voice "voice/爱衣/110000200.ogg"
    aiyi "爱衣我就叫他“欧尼酱”哟~"
    "刚刚不是还叫“凉君”的吗......"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110000210.ogg"
    aiyi "我们现在回去是不是比较好？"
    me01 "是啊，幼儿园的老师也该着急了吧。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/110000230.ogg"
    aiyi "老师会生气吗？"
    me01 "全都是千波的错所以不用担心的。"
    pause 0.5 hard
    play sound jump_1
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at flu_up(0.15, 30):
        xpos 0.5
    $ flcam.move(-2250, 300, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/千波/210000210.ogg"
    qb "别直接叫我的名字！"
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_s1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    $ flcam.move(0, 200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/小桃/220000110.ogg"
    ycxt "哈啾。"
    pause 0.5 hard
    play ambience1 zhong_rill
    $ flcam.move(0, 0, 0)
    scene set only balltower evening big
    with slowdissolve
    pause 2.0 hard
    "就在这时，钟楼的钟声再次响起。"
    "就好像在催促我们出发一样。"
    stop ambience1 fadeout 5.0
    pause 2.0 hard
    $ flcam.move(-2250, 300, 750)
    scene set only balltower snow evening xuejian alpha
    with dissolve
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    show ycxt_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    pause 0.5 hard
    play voice "voice/爱衣/110000240.ogg"
    aiyi "小桃？"
    play voice "voice/小桃/220000120.ogg"
    ycxt "稍微......有些累了。"
    me01 "要我背你吗？"
    show ycxt_dzf_b1 b1 b1_n2
    play voice "voice/小桃/220000130.ogg"
    ycxt "......可以吗？"
    me01 "小孩子的体重不算什么。"
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.7
    $ flcam.move(0, 200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/千波/210000220.ogg"
    qb "小桃你可不能被骗了，想把你带回家的男人都是这么说的！"
    hide ycxt_dzf_b1 
    hide aiyi_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    hide qianbo_dzf_b1 with None
    pause 0.1 hard
    show qianbo_dzf_b2 b2 b2_sp1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    me01 "真乖真乖~"
    play sound jump_1
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at flu_up(0.15, 30):
        xpos 0.7
    play voice "voice/千波/210000230.ogg"
    qb "别性骚扰啊！！！"
    hide qianbo_dzf_b1
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    "我把小桃连同她手里的布偶一起背了起来。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with dissolve
    pause 0.5 hard
    show ycxt_dzf_b1 b1 b1_h1 onlayer screens at side_left('ycxt'), basicfade
    play voice "voice/小桃/220000140.ogg"
    ycxt "凉君的背......好温暖~"
    hide ycxt_dzf_b1
    pause 0.5 hard
    $ flcam.move(-4500, 300, 900)
    scene set only balltower snow evening xuejian alpha
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    with dissolve
    pause 0.5 hard
    play voice "voice/爱衣/110000250.ogg"
    aiyi "大哥哥......牵手可以吗？"
    me01 "当然可以。"
    $ flcam.move(-4500, 300, 900, duration=1.5, warper='ease_cubic')
    pause 1.0 hard
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/110000260.ogg"
    aiyi "哎嘿~"
    "爱衣握住了我的手，一股温暖从手心里传来。"
    pause 0.5 hard
    hide aiyi_dzf_b1
    $ flcam.move(4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b2 b2 b2_n3 onlayer m2:
        xpos 0.7
    play voice "voice/千波/210000240.ogg"
    qb "我的话......就算一个人走也无所谓的。"
    me01 "那就这样吧。"
    hide qianbo_dzf_b1
    show qianbo_dzf_b2 b2 b2_a3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/千波/210000250.ogg"
    qb "即使一个人也没事的！"
    me01 "毕竟我已经没有手来照顾你了。"
    $ flcam.move(4500, 300, 1000, duration=1.5)
    pause 0.5 hard
    play sound jing01
    show jingya onlayer texture:
        xpos 0.0
    hide qianbo_dzf_b2
    show qianbo_dzf_b1 b1 b1_a2 onlayer m2 at flu_up(0.15, 20):
        xpos 0.7
    play voice "voice/千波/210000260.ogg"
    qb "{size=72}凉君你这个大笨蛋！{/size}"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day201_3.cloqks'
    if not seen_day201_3_cloqks:
        $ seen_day201_3_cloqks = True
    jump day201_3.map

label day201_3.kindergarden_event01:
    $ flcam.move(0, 0, 0)
    scene set only school evening outside xuejian
    with slowdissolve
    show snow_level1 onlayer fg
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_sp1 onlayer m1 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/翔子/010000130.ogg"
    xz "爱衣！"
    play music second_108 fadein 3.0
    pause 0.5 hard
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp2 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    $ flcam.move(-2800, 0, 750, duration=1.5)
    show xz_dsf_b2 b2 b2_s1:
        xpos 0.5
        linear 0.35 xpos 0.45
    play sound touch
    play voice "voice/爱衣/110000270.ogg"
    aiyi "大、大姐姐？"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s2 onlayer m1:
        xpos 0.45
    play voice "voice/翔子/010000140.ogg"
    xz "爱衣，你跑到哪里去了？"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110000280.ogg"
    aiyi "那、那个......广场。"
    show xz_dsf_b3 b3 b3_sp1
    play voice "voice/翔子/010000150.ogg"
    xz "钟楼广场？"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/110000290.ogg"
    aiyi "嗯......让你担心了，对不起。"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.45
    play voice "voice/翔子/010000160.ogg"
    xz "不是向我，先给千川老师道个歉吧。"
    play voice "voice/爱衣/110000300.ogg"
    aiyi "......嗯。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m1:
        xpos 0.45
    play voice "voice/翔子/010000170.ogg"
    xz "反省了吗？"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110000310.ogg"
    aiyi "嗯。"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.45
    play voice "voice/翔子/010000180.ogg"
    xz "以后不要再擅自跑出去了，总之先给千川老师报个平安吧。"
    pause 1.0 hard
    show aiyi_dzf_b1 b1 b1_s4 at walkout_l(0.3)
    pause 1.0 hard
    hide aiyi_dzf_b1
    $ flcam.move(-800, -300, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dsf_b2
    show xz_dsf_b1 b1 b1_sp1 onlayer m1:
        xpos 0.45
    play voice "voice/翔子/010000190.ogg"
    xz "是你......找到她们的吗？"
    me01 "我也是偶然间遇到的。"
    hide xz_dsf_b1 with None
    pause 0.1 hard
    show xz_dsf_b2 b2 b2_s1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.45
    play voice "voice/翔子/010000200.ogg"
    xz "总之谢谢你了。"
    $ flcam.move(-2800, 0, 750, duration=1.5)
    show qianbo_dzf_b1 b1 b1_n2 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/千波/210000270.ogg"
    qb "还没到要感谢的程度。"
    hide xz_dsf_b2
    $ flcam.move(-5200, 300, 900, duration=1.5)
    pause 0.5 hard
    show qianbo_dzf_b1 b1 b1_sp1
    me01 "你还是以爱衣为榜样好好反省一下吧。"
    show qianbo_dzf_b1 b1 b1_sp2 at flu_down(0.35, 20):
        xpos 0.3
    "说完我摸了摸她的头。"
    show qianbo_dzf_b1 b1 b1_n3
    play voice "voice/千波/210000280.ogg"
    qb "......"
    hide qianbo_dzf_b1
    show qianbo_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/千波/210000290.ogg"
    qb "......对不起，爱衣的大姐姐。是人家叫她们两个出去的。"
    $ flcam.move(-2800, 0, 750, duration=1.5)
    show xz_dsf_b1 b1 b1_n1 onlayer m1:
        xpos 0.45
    play voice "voice/翔子/010000210.ogg"
    xz "没关系的，比起这个千波的家人也在担心你吧，不快点回去吗？"
    show qianbo_dzf_b2 b2 b2_s2
    play voice "voice/千波/210000300.ogg"
    qb "......嗯。"
    pause 1.0 hard
    show qianbo_dzf_b2 b2 b2_s2 at walkout_l(0.3)
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian
    with dissolve
    pause 1.0 hard
    show ycxt_dzf_b1 b1 b1_s1 onlayer screens at side_left('ycxt'), basicfade
    play voice "voice/小桃/220000150.ogg"
    ycxt "呼~"
    hide ycxt_dzf_b1
    "小桃在我背后睡着了，也许是玩累了吧。"
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only school evening outside xuejian alpha
    show xz_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/010000220.ogg"
    xz "小桃的奶奶也在里面。"
    me01 "我知道了，还有......"
    show xz_dsf_b1 b1 b1_sp1
    play voice "voice/翔子/010000230.ogg"
    xz "怎么了？"
    me01 "翔子你怎么会在这里？"
    show xz_dsf_b1 b1 b1_s2
    play voice "voice/翔子/010000260.ogg"
    xz "......"
    pause 0.5 hard
    show xz_dsf_b1 b1 b1_s2 at walkout_r(0.5)
    pause 0.5 hard
    "没有回答，翔子犹豫了片刻还是转身走进了幼儿园。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with right2left_02
    play sound open_door5
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school evening inside xuejian
    with right2left_02
    show snow_level1 onlayer fg
    play music second_105 fadein 3.0
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/千川老师/140000060.ogg"
    qcls "谢谢你把她们三人平安带回来。"
    show qcls_zf_b1 b1 b1_n3
    play voice "voice/千川老师/140000070.ogg"
    qcls "虽然大家嘴上没说，但是最应该被责怪的还是我。"
    me01 "这不是老师你的错，幼儿园的小孩子很多，想要全部管理好想必很辛苦吧。"
    show qcls_zf_b1 b1 b1_s1
    play voice "voice/千川老师/140000080.ogg"
    qcls "我们的幼儿园虽然规模还算比较小，但是人手也也的确是不够。"
    me01 "这里的老师很少吗？"
    show qcls_zf_b1 b1 b1_h2
    play voice "voice/千川老师/140000130.ogg"
    qcls "旧城区和新城区虽然都是雪见市的一部分，但是给人感觉却是两个不同的世界。"
    show qcls_zf_b1 b1 b1_h3
    play voice "voice/千川老师/140000140.ogg"
    qcls "虽然对于留在哪边比较好这个问题每个人的想法都不一样，但是年轻人的话果然还是喜欢那边的吧。"
    me01 "千川老师也打算离开这里吗？"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show qcls_zf_b1 b1 b1_sp2
    play voice "voice/千川老师/140000150.ogg"
    qcls "为什么这么说？"
    me01 "因为老师看起来很年轻嘛。"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/140000160.ogg"
    qcls "啊啦啊啦，真会说话呢~"
    show qcls_zf_b1 b1 b1_n1
    play voice "voice/千川老师/140000170.ogg"
    qcls "我不会辞职的，因为我喜欢这所幼儿园。"
    play voice "voice/千川老师/140000180.ogg"
    qcls "而且马上就会来一个新的老师，听说比我还年轻呢。"
    show qcls_zf_b1 b1 b1_h1
    play voice "voice/千川老师/140000190.ogg"
    qcls "我也还不能认输~"
    "新老师啊，不过也正因有这样的老师守护着孩子们，他们才能幸福地成长吧。"
    "有这样的老师一定是这里所有孩子们的福气。"
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowdissolve
    pause 2.0 hard

label day201_3.street_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "从幼儿园出来太阳也已经下山了，搞了半天住宿的问题还是没有解决。"
    pause 1.0 hard
    scene set only street night road1 xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110000320.ogg"
    aiyi "大哥哥，还可以牵手吗？"
    me01 "当然可以。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    pause 0.5 hard
    play voice "voice/爱衣/110000330.ogg"
    aiyi "哎嘿~"
    hide aiyi_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/010000270.ogg"
    xz "你回家的路，也是这边吗？"
    me01 "不，我只是因为被牵着手的缘故......"
    hide xz_dsf_b1
    show xz_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/010000280.ogg"
    xz "爱衣完全跟你混熟了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian
    with dissolve
    pause 2.0 hard
    "比起白天，夜色下的灯光更能够映衬出雪的洁白。"
    "冬日的天空看不到多少星星，取而代之的是无尽的白雪从天际滑落。"
    pause 1.0 hard
    scene set only street night road1 xuejian
    with dissolve
    pause 1.0 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    me01 "不打伞没关系吗？"
    hide xz_dsf_b1
    show xz_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/翔子/010000300.ogg"
    xz "欸？"
    me01 "不光是你们，这里的其他人也是如此。"
    "除了伞就连鞋子也是，大家都和平时一样穿着普通的鞋子。"
    "似乎对这场雪没有丝毫的防备一般。"
    pause 0.5 hard
    $ flcam.move(-4500, -300, 1000, duration=1.5)
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.3
    pause 0.5 hard
    play voice "voice/翔子/010000310.ogg"
    xz "因为这雪，是温柔的雪。"
    play voice "voice/翔子/010000320.ogg"
    xz "触碰后马上就会融化，在察觉到寒冷之前就会消失。"
    show xz_dsf_b3 b3 b3_h1
    play voice "voice/翔子/010000330.ogg"
    xz "就是这样又温柔、又有些寂寞的雪啊。"
    pause 1.0 hard
    hide xz_dsf_b3
    $ flcam.move(0, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/爱衣/110000370.ogg"
    aiyi "大哥哥，要来爱衣家里吗？"
    me01 "这个嘛......"
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/010000390.ogg"
    xz "还没吃晚饭的话，一起吃也行......"
    play voice "voice/翔子/010000400.ogg"
    xz "不过这只是你帮忙找到爱衣的谢礼而已。"
    me01 "那就承蒙款待了。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    pause 0.5 hard
    play voice "voice/爱衣/110000400.ogg"
    aiyi "哇！"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowdissolve
    pause 2.0 hard

label day201_3.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only home night outside xuejian
    show snow_level1 onlayer fg
    with dissolve
    play sound open_door4
    pause 2.0 hard
    hide snow_level1
    scene set only home night passwalk xuejian
    with dissolve
    pause 2.0 hard
    play sound close_door3
    pause 2.0 hard
    "与外面不同，屋子里非常的温暖。"
    pause 2.0 hard
    scene set only home night kitchen xuejian
    with dissolve
    play music second_112 fadein 3.0
    pause 1.0 hard
    "晚饭是翔子准备的。"
    "餐桌上只有我们三个人。"
    "看来这个家里应该只有翔子和爱衣两个人而已。"
    "分开的这些日子里翔子的生活状态通过周围的环境就可以大致推测出来。"
    pause 0.5 hard
    $ flcam.move(-4500, 300, 900, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110000410.ogg"
    aiyi "爱衣我呢，已经能够自己用筷子了。"
    me01 "了不起了不起。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    pause 0.5 hard
    play voice "voice/爱衣/110000330.ogg"
    aiyi "哎嘿~"
    "我摸了摸她的头。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110000430.ogg"
    aiyi "爱衣，已经是大人了哟。"
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_n1 onlayer m1:
        xpos 0.5
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/010000440.ogg"
    xz "爱衣就保持现在小孩子的样子就好。"
    show aiyi_dzf_b1 b1 b1_s2
    play voice "voice/爱衣/110000440.ogg"
    aiyi "爱衣，想要快点变成大人。"
    show xz_dsf_b2 b2 b2_ga2
    play voice "voice/翔子/010000450.ogg"
    xz "突然长大是不可能的。"
    stop music fadeout 5.0
    pause 0.5 hard
    hide xz_dsf_b2
    $ flcam.move(-4500, 300, 900, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110000450.ogg"
    aiyi "大哥哥，能让爱衣成为大人吗？"
    show xz_dsf_b1 b1 b1_sp2 onlayer m1:
        xpos 0.5
        xzoom -1
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    play music second_106 fadein 3.0
    play sound jing01
    show tanhao at tanhao_x05 onlayer m2
    show xz_dsf_b1 b1 b1_sp2 at flu_up(0.15, 30):
        xpos 0.5
    play voice "voice/翔子/010000460.ogg"
    xz "{size=72}噗！{/size}"
    with vpunch
    me01 "爱衣，这种话是不能随便对男人说的。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110000460.ogg"
    aiyi "但千波说过，对喜欢的男孩子可以说。"
    show xz_dsf_b1 b1 b1_s1
    play voice "voice/翔子/010000470.ogg"
    xz "千波的话也不要全信。"
    "千波这孩子到底有多早熟啊！"
    show xz_dsf_b1 b1 b1_a1
    play voice "voice/翔子/010000480.ogg"
    xz "比起这个，爱衣你喜欢这个男人吗？"
    "翔子用手指着我的鼻子。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110000470.ogg"
    aiyi "爱衣喜欢大哥哥哟，毕竟已经被摸过了嘛~"
    show xz_dsf_b1 b1 b1_ga1
    play voice "voice/翔子/010000490.ogg"
    xz "性骚扰......"
    me01 "你听我解释！"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110000480.ogg"
    aiyi "被男孩子摸头，还是第一次呢~"
    show xz_dsf_b1 b1 b1_a2
    play voice "voice/翔子/010000500.ogg"
    xz "还被夺走了第一次......"
    "本想趁此机会商量一下借宿的事情。"
    "可是感觉气氛有些微妙。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black 
    with slowdissolve
    pause 2.0 hard

label day201_3.home_event02:
    $ flcam.move(0, 0, 0)
    scene set only home night living_room xuejian
    with dissolve
    pause 1.0 hard
    "晚饭后，我向翔子解释了之前的误会。"
    "以及现在自己无家可归的窘境。"
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b1 b1 b1_n2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    me01 "其实我也是今天才刚到这里，还没有来得及找到其他的住处。"
    play voice "voice/翔子/010000550.ogg"
    xz "......"
    me01 "如果可以的话......"
    play music second_104 fadein 3.0
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dsf_b1
    show xz_dsf_b2 b2 b2_a2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010000560.ogg"
    xz "我拒绝！"
    me01 "明明已经说不生气的。"
    me01 "至于其他的理由，要听吗？"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s4 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010000580.ogg"
    xz "嘛，只是听听的话。"
    me01 "这个家里果然还是需要男人的吧，毕竟翔子你一个人照顾爱衣也很辛苦，我可以帮你分担一些体力活。"
    me01 "现在大家也还是学生，肯定有自己的生活圈需要打理吧？其他的琐事就交给我好了。"
    me01 "也就是说，你可以把我当成是“工具人”来使唤。"
    "话虽如此，家务这方面对我而言完全就是半吊子。"
    "但一定也有男人才能做到的事情。"
    "两个女孩子一起生活的话，果然还是需要安全感的。"
    me01 "所以......"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010000610.ogg"
    xz "想说的就是这些了吗？"
    me01 "你同意了？"
    show xz_dsf_b2 b2 b2_a2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/翔子/010000620.ogg"
    xz "驳回！"
    me01 "为什么啊？！"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010000630.ogg"
    xz "突然过来要求同居什么的......我怎么可能这么随便就答应啊。"
    me01 "我会尽量不出现在你的视线内，有需要的时候喊我一声就行了。"
    play voice "voice/翔子/010000650.ogg"
    xz "不存在那样的时候。"
    show xz_dsf_b3 b3 b3_s4
    play voice "voice/翔子/010000660.ogg"
    xz "而且这样一来规避视线不就没有意义了吗。"
    show xz_dsf_b3 b3 b3_a1
    me01 "那样的话就把我当成空气就好了。"
    play voice "voice/翔子/010000670.ogg"
    xz "这种事情现实里怎么可能办到？"
    "非要说的话，也不是办不到。"
    pause 1.0 hard
    scene black 
    with dissolve
    pause 1.0 hard
    "但是不是在物理层面上，而是精神层面上的办法。"
    "通过潜移默化的暗示，改变人们的普遍认知从而修改所谓的“常识”。"
    "之前从“梦”口中得知“妖精先生”似乎就是这么说的。"
    pause 1.0 hard
    scene set only home night living_room xuejian
    show xz_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    me01 "无论如何都不行吗？"
    show xz_dsf_b3 b3 b3_s1
    play voice "voice/翔子/010000680.ogg"
    xz "不行。"
    me01 "你就忍心看我在风中露宿街头吗。"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/010000690.ogg"
    xz "这就不关我的事了。"
    me01 "好过分。"
    stop music fadeout 5.0
    "看来被赶出去是既定事实了。"
    pause 0.5 hard
    hide xz_dsf_b2
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110000490.ogg"
    aiyi "大姐姐......"
    play music second_111 fadein 3.0
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110000500.ogg"
    aiyi "爱衣我......想和大哥哥住在一起。"
    show aiyi_dzf_b1 b1 b1_s4 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/110000510.ogg"
    aiyi "想和大哥哥一起生活。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b3 b3 b3_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010000700.ogg"
    xz "爱、爱衣......"
    me01 "住在一起的话，接送爱衣去幼儿园的任务可以交给我来做。"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/110000520.ogg"
    aiyi "哇！"
    show xz_dsf_b3 b3 b3_s2
    play voice "voice/翔子/010000710.ogg"
    xz "别擅自做决定啊......"
    me01 "我虽然不擅长家务，但是像这样日常的工作还是可以交给我的。"
    me01 "翔子你也是，放学以后还要参加社团或者打工什么的吧？"
    hide aiyi_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    show xz_dsf_b3 b3 b3_s1
    play voice "voice/翔子/010000720.ogg"
    xz "我并没有参加社团或者打工。"
    show xz_dsf_b3 b3 b3_s4
    play voice "voice/翔子/010000730.ogg"
    xz "不过有学生会的工作，这样确实也帮忙了......"
    me01 "是吧？"
    show xz_dsf_b3 b3 b3_n2
    play voice "voice/翔子/010000740.ogg"
    xz "但是爱衣是日向同学特地托付给我照顾的，所以没有问题的。"
    "虽然听到日向这个姓氏大致就能猜到了。"
    me01 "但是多少也能减轻你的负担吧？"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_s1 onlayer m1:
        xpos 0.5
    play voice "voice/翔子/010000750.ogg"
    xz "照顾爱衣才不是什么辛苦的事。"
    "真不坦率啊。"
    "自从“梦”消失之后，翔子就变得比以前更加固执了。"
    "这也许就是多重人格的毛病吧。"
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, 0, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/爱衣/110000530.ogg"
    aiyi "要把大哥哥赶出去吗？"
    show xz_dsf_b2 b2 b2_s2
    play voice "voice/翔子/010000760.ogg"
    xz "与其说是赶出去，不如说是请出去。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110000540.ogg"
    aiyi "外面很冷的，大哥哥会被冻僵的。"
    hide xz_dsf_b2
    show xz_dsf_b1 b1 b1_sp2 onlayer m1:
        xpos 0.5
        xzoom -1
    play voice "voice/翔子/010000770.ogg"
    xz "我、我当然也没有打算把他直接丢在大街上。"
    show xz_dsf_b1 b1 b1_s2
    play voice "voice/翔子/010000780.ogg"
    xz "但是，突然发生这样的事。"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/110000550.ogg"
    aiyi "大哥哥是好人哟。"
    show aiyi_dzf_b1 b1 b1_n1
    play voice "voice/爱衣/110000560.ogg"
    aiyi "在钟楼广场的时候来接爱衣了。"
    show aiyi_dzf_b1 b1 b1_s4
    play voice "voice/爱衣/110000570.ogg"
    aiyi "那时真的，非常开心。"
    play voice "voice/爱衣/110000580.ogg"
    aiyi "非常的......温暖。"
    hide aiyi_dzf_b1
    $ flcam.move(-800, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b1 b1 b1_s1
    play voice "voice/翔子/010000790.ogg"
    xz "......总之，明天我会向父亲那边确认一下。"
    show xz_dsf_b1 b1 b1_s2
    play voice "voice/翔子/010000810.ogg"
    xz "所以，神野君。今天你就先住在这里好了。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/110000590.ogg"
    aiyi "大姐姐，明天还得去学校吧？"
    show xz_dsf_b1 b1 b1_h2
    play voice "voice/翔子/010000870.ogg"
    xz "是啊，寒假还没到，爱衣明天也还要去幼儿园，差不多该休息了。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/110000600.ogg"
    aiyi "要烧洗澡水吗？"
    show xz_dsf_b1 b1 b1_h1
    play voice "voice/翔子/010000880.ogg"
    xz "嗯，我马上就去准备。"
    hide xz_dsf_b1
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/110000610.ogg"
    aiyi "大哥哥，要一起来吗？"
    pause 0.5 hard
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b2 b2 b2_a2 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    pause 0.5 hard
    play voice "voice/翔子/010000890.ogg"
    xz "{size=72}绝对不行！{/size}"
    me01 "就算你不发火我也不会进去的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowdissolve
    pause 2.0 hard

label day201_3.myroom_event01:
    $ flcam.move(0, 0, 0)
    default seen_myroom = False
    if not seen_myroom:
        $ seen_myroom = True
        scene set only sky night xuejian
        show snow_level1 onlayer fg
        with dissolve
        pause 2.0 hard
        play sound open_door6
        pause 0.5 hard
        hide snow_level1
        scene set only home night my_room xuejian
        with dissolve
        pause 1.0 hard
        play music second_112 fadein 3.0
        $ flcam.move(0, -300, 900, duration=1.5)
        pause 0.5 hard
        show xz_dsf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
        pause 0.5 hard
        play voice "voice/翔子/010000900.ogg"
        xz "你就用这个房间吧，虽然只是客房。"
        me01 "我其实睡在客厅的沙发上也是可以的。"
        show xz_dsf_b1 b1 b1_s1
        play voice "voice/翔子/010000910.ogg"
        xz "在那种地方睡觉的话，到了早上的时候会着凉的。"
        hide xz_dsf_b1
        show xz_dsf_b2 b2 b2_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010000920.ogg"
        xz "而且不是带行李了吗，换洗衣服之类的有吧？"
        me01 "嗯。"
        hide xz_dsf_b2
        show xz_dsf_b1 b1 b1_n1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010000930.ogg"
        xz "换衣服的时候也在这里吧。有要换洗的衣服就放在更衣室的篮子里就好。"
        me01 "我的话去公共澡堂就行了。"
        show xz_dsf_b1 b1 b1_ga2
        play voice "voice/翔子/010000940.ogg"
        xz "这样不是很浪费钱吗。"
        show xz_dsf_b1 b1 b1_h2
        play voice "voice/翔子/010000950.ogg"
        xz "所以有要洗的衣服就放在篮子里，明早我会一起洗的。"
        hide xz_dsf_b1
        show xz_dsf_b3 b3 b3_s4 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010000960.ogg"
        xz "虽然没洗过男孩子的衣服，但要领应该是一样的。"
        "看到内裤的瞬间不会发出惨叫吧......"
        pause 1.0 hard
        hide xz_dsf_b3
        play sound open_door6
        $ flcam.move(-4500, 300, 900, duration=1.5)
        pause 0.5 hard
        show aiyi_sy_b1 b1 b1_n3 onlayer m2 at walkin_l(0.3)
        pause 0.5 hard
        play voice "voice/爱衣/110000620.ogg"
        aiyi "大哥哥......"
        pause 0.5 hard
        $ flcam.move(-2250, 0, 750, duration=1.5)
        show xz_dsf_b1 b1 b1_ga2 onlayer m1:
            xpos 0.5
            xzoom -1
        play voice "voice/翔子/010000970.ogg"
        xz "爱衣，你怎么起来了？吵到你真是对不起。"
        play voice "voice/爱衣/110000630.ogg"
        aiyi "......"
        show xz_dsf_b1 b1 b1_h2
        play voice "voice/翔子/010000980.ogg"
        xz "已经很晚了，再不睡觉可不行。"
        play voice "voice/爱衣/110000640.ogg"
        aiyi "嗯。"
        hide xz_dsf_b1
        hide aiyi_sy_b1
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
        "揉了揉睡眼，爱衣向我这边靠了过来。"
        $ flcam.move(-4500, 300, 900, duration=1.5)
        show aiyi_sy_b1 b1 b1_n2 onlayer m2:
            xpos 0.3
        play voice "voice/爱衣/110000650.ogg"
        aiyi "大哥哥，刚才去哪里了？"
        me01 "去车站取行李了。"
        show aiyi_sy_b1 b1 b1_s3
        play voice "voice/爱衣/110000660.ogg"
        aiyi "还以为不见了......"
        pause 0.5 hard
        me01 "我不会消失的。"
        show aiyi_sy_b1 b1 b1_h1 at flu_down(0.35, 20):
            xpos 0.3
        pause 0.5 hard
        "我摸了摸她的头，爱衣的脸上再次露出了笑容。"
        pause 0.5 hard
        show xz_dsf_b2 b2 b2_s1 onlayer m1:
            xpos 0.5
        $ flcam.move(-2250, 0, 750, duration=1.5)
        pause 0.5 hard
        play voice "voice/翔子/010000990.ogg"
        xz "虽说爱衣本来也不是怕生的孩子，但是为什么会对你亲近到这种地步呢。"
        show aiyi_sy_b1 b1 b1_sp1
        play voice "voice/爱衣/110000670.ogg"
        aiyi "大哥哥，是要在这里睡吗？"
        stop music fadeout 5.0
        me01 "是的。"
        show xz_dsf_b2 b2 b2_sp1
        show aiyi_sy_b1 b1 b1_n1
        play voice "voice/爱衣/110000680.ogg"
        aiyi "爱衣也可以在这里睡吗？"
        play music second_108 fadein 3.0 if_changed
        hide xz_dsf_b2
        show xz_dsf_b1 b1 b1_n2 onlayer m1:
            xpos 0.5
        play voice "voice/翔子/010001000.ogg"
        xz "爱衣不是有自己的房间吗？"
        show aiyi_sy_b1 b1 b1_s3
        play voice "voice/爱衣/110000690.ogg"
        aiyi "但是......"
        hide xz_dsf_b1
        show xz_dsf_b2 b2 b2_s1 onlayer m1:
            xpos 0.5
        play voice "voice/翔子/010001010.ogg"
        xz "不能说任性的话哟，神野君他应该也累了。"
        me01 "其实一起睡也是可以的。"
        hide aiyi_sy_b1
        $ flcam.move(0, -300, 900, duration=1.5)
        show xz_dsf_b2 b2 b2_a2 at flu_down(0.35, 20):
            xpos 0.5
        pause 0.5 hard
        show fennu onlayer texture:
            xalign 0.56 yalign 0.2 zoom 1.5
        play voice "voice/翔子/010001020.ogg"
        xz "驳回！"
        pause 0.5 hard
        hide xz_dsf_b2
        show xz_dsf_b1 b1 b1_n1 onlayer m1:
            xpos 0.5
        show aiyi_sy_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        $ flcam.move(-2250, 0, 750, duration=1.5)
        pause 0.5 hard
        play voice "voice/翔子/010001030.ogg"
        xz "爱衣回房间吧，睡不着的话姐姐给你讲故事吧。"
        play voice "voice/爱衣/110000700.ogg"
        aiyi "没事的，说了任性的话对不起。"
        show xz_dsf_b1 b1 b1_h1
        play voice "voice/翔子/010001040.ogg"
        xz "嗯，真是个好孩子。"
        show aiyi_sy_b1 b1 b1_n1 at flu_down(0.35, 20):
            xpos 0.3
        "翔子也摸了摸爱衣的头。"
        hide xz_dsf_b1
        $ flcam.move(-4500, 300, 900, duration=1.5)
        show aiyi_sy_b1 b1 b1_h1
        play voice "voice/爱衣/110000710.ogg"
        aiyi "大哥哥晚安~"
        stop music fadeout 5.0
        me01 "晚安。"
        pause 1.0 hard
        show aiyi_sy_b1 b1 b1_h1 at walkout_l(0.3)
        pause 1.0 hard
        play sound close_door3
        pause 2.0 hard
        play music second_105 fadein 3.0
        $ flcam.move(0, -300, 900, duration=1.5)
        pause 0.5 hard
        show xz_dsf_b3 b3 b3_sp1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010001050.ogg"
        xz "这个房间不会冷吧？"
        me01 "没关系的。"
        show xz_dsf_b3 b3 b3_n1
        play voice "voice/翔子/010001060.ogg"
        xz "需要什么其他的东西吗？"
        me01 "有被褥就足够了。"
        show xz_dsf_b3 b3 b3_s4
        play voice "voice/翔子/010001070.ogg"
        xz "是吗。"
        pause 1.0 hard
        scene black
        with slowerdissolve
        pause 1.0 hard
        scene set only home night my_room xuejian
        show xz_dsf_b3 b3 b3_n1 onlayer m2:
            xpos 0.5
        $ flcam.move(0, -400, 600)
        $ flcam.move(0, -100, 400, duration=1.5)
        $ flcam.stop()
        $ camera_move(0, 100, 200, duration=3.0)
        pause 0.5 hard
        show screen investigation_popup(investigation.hint_xz)
        $ suppress_overlay = True
    else:
        scene black
        with dissolve
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
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.1)
            screen_direction left
            sleep jump day201_3.sleep

label day201_3.sleep:
    menu:
        "早点休息":
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
    
    jump day201_4

label day201_4:
    $ suppress_overlay = False
    nvl clear
    pcenter "呐，希菲尔——"
    pause 0.5 hard
    nvl clear
    with dissolve
    play music second_113 fadein 3.0
    scene set only balltower snow day xuejian alpha
    show snow_level1 onlayer fg
    with dissolve
    pause 0.5 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    show ts_xfe_yjz_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000000300.ogg"
    xfe "凉君，我来找你玩了哟~"
    me01 "等你很久了。"
    hide ts_xfe_yjz_b1 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000000310.ogg"
    xfe "那走吧~"
    me01 "手......"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/000000320.ogg"
    xfe "牵着的话......不行吗？"
    me01 "也不是不行。"
    show ts_xfe_yjz_b3 b3 b3_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/000000330.ogg"
    xfe "那走吧！"
    me01 "等一下。"
    show ts_xfe_yjz_b3 b3 b3_sp1
    play voice "voice/希菲尔/000000340.ogg"
    xfe "怎么了？"
    me01 "之前就很在意，希菲尔你穿成这样不冷吗？"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000000350.ogg"
    xfe "？"
    me01 "现在还在下雪，穿这么少没问题吗？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    pause 1.0 hard
    "这座城市飘落的，纯白的雪。"
    "仿佛是在诉说着对冬天的眷恋一般。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian alpha
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b2 b2 b2_s3 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/希菲尔/000000370.ogg"
    xfe "......"
    me01 "天气预报说了，今天也是大雪。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/000000380.ogg"
    xfe "这样啊。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/000000390.ogg"
    xfe "......"
    me01 "要到我的伞里来吗？"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/000000400.ogg"
    xfe "嗯。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/000000410.ogg"
    xfe "虽然不冷，不过还是要进去哟~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky snow day xuejian
    with dissolve
    pause 0.5 hard
    "我们就这样走着。"
    "在这洁白的世界里。"
    pause 1.0 hard
    hide snow_level1
    scene white
    with slowerdissolve
    pause 2.0 hard
    "而这一次，我与她一起撑着伞、牵着手。"
    pause 1.0 hard
    scene set only xfe_cg memory1
    with slowdissolve
    pause 1.0 hard
    "两个人一起。"
    "在这绵延的雪道上，留下两行足迹。"
    me01 "要去哪里好呢？"
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/希菲尔/000000420.ogg"
    xfe "哪里都可以哟。"
    play voice "voice/希菲尔/000000430.ogg"
    xfe "和凉君一起的话，去哪里都行。"
    $ flcam.move(2200, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/希菲尔/000000440.ogg"
    xfe "在春天来临之前，无论去哪里都可以的——"
    pause 2.0 hard
    scene white 
    with slowerdissolve
    stop music fadeout 5.0
    pause 2.0 hard
    $ mouse_visible = False
    $ suppress_overlay = True
    $ _skipping = renpy.seen_audio('video/second_op.mp4')
    $ config.skipping = None
    scene black 
    with slowerdissolve
    pause 3.0 hard
    show movie onlayer master
    play movie "video/second_op.mp4" noloop
    $ renpy.music.play("video/second_op.mp3", synchro_start='movie')
    pause 136.0 hard
    $ _skipping = True
    $ mouse_visible = True
    stop movie
    hide movie
    stop music fadeout 1.0
    $ flcam.move(0, 0, 0)
    pause 4.0 hard
    jump day202

