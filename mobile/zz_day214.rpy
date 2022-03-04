label day214:
    bookmark
    $ save_name = _("Day 214")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date212 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    with slowerdissolve
    play music second_114 fadein 3.0 if_changed
    pause 1.0 hard
    show rxl_dsf_b1 b1 b1_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121300860.ogg"
    rxl "早上好立花。"
    show lhx_dsf_b2 b2 b2_n4 onlayer screens at side_right('lhx'), basicfade
    play voice "voice/立花希/031301250.ogg"
    lhx "......"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_ga1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121300870.ogg"
    rxl "不要那么昏沉沉的了，去洗把脸吧？"
    play voice "voice/立花希/031301260.ogg"
    lhx "......"
    show rxl_dsf_b2 b2 b2_sp1
    play voice "voice/日向怜/121300880.ogg"
    rxl "凉君差不多也要起来了吧。"
    play voice "voice/立花希/031301270.ogg"
    lhx "......"
    hide rxl_dsf_b2
    show rxl_dsf_b1 b1 b1_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121300890.ogg"
    rxl "头发乱糟糟的会被凉君笑话的，去冲个澡吧？"
    play voice "voice/立花希/031301280.ogg"
    lhx "......"
    show rxl_dsf_b1 b1 b1_h3
    play voice "voice/日向怜/121300900.ogg"
    rxl "呵呵呵~"
    hide rxl_dsf_b1
    hide lhx_dsf_b2
    pause 1.0 hard
    scene set only home day lhx_room xuejian
    with dissolve
    pause 1.0 hard
    "一觉醒来，就听到客厅传来了动静。"
    "翻了个身才缓缓察觉自己是在立花老师的房间。"
    "第一次在翔子以外的朋友家留宿......这种感觉真是奇妙。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dsf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/121300910.ogg"
    rxl "早上好，凉君~"
    me01 "早上好，立花老师呢？"
    hide rxl_dsf_b2
    show rxl_dsf_b1 b1 b1_h3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121300920.ogg"
    rxl "她为了凉君去洗身子了哟~"
    me01 "别胡说，你指的是晨浴吧。"
    show rxl_dsf_b1 b1 b1_n4
    play voice "voice/日向怜/121300930.ogg"
    rxl "这不是很清楚嘛。"
    me01 "虽然现在说有些迟，不过突然打扰真是抱歉。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    show rxl_dsf_b1 b1 b1_h2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121300940.ogg"
    rxl "立花的床味道如何？"
    me01 "虽然知道你是别的意思，不过确实是挺舒服的。"
    show rxl_dsf_b1 b1 b1_h1
    play voice "voice/日向怜/121300950.ogg"
    rxl "哪里哪里......比起那个去洗把脸吧？"
    me01 "可是立花老师现在就在里面吧？"
    show rxl_dsf_b1 b1 b1_h3
    play voice "voice/日向怜/121300960.ogg"
    rxl "那就顺便再去洗个澡如何？"
    me01 "你还真是个不折不扣的痴女。"
    hide rxl_dsf_b1 with None
    pause 0.1 hard
    show rxl_dsf_b2 b2 b2_ga1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121300970.ogg"
    rxl "我只是给你制造成为幸运色狼的机会而已啦~"
    me01 "你只是拿我寻开心吧。"
    show rxl_dsf_b2 b2 b2_s2
    play voice "voice/日向怜/121300980.ogg"
    rxl "凉君早上没有睡迷糊的特性，果然要挑逗的话立花才是最佳人选啊~"
    pause 0.5 hard
    play sound open_door5
    pause 1.5 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_dsf_b2 with None
    pause 0.1 hard
    show rxl_dsf_b1 b1 b1_h2 onlayer m2 at flu_down(0.35, 20, 2):
        xpos 0.5
    play voice "voice/日向怜/121300990.ogg"
    rxl "呵呵呵~"
    me01 "这诡异的笑声是怎么回事......"
    show rxl_dsf_b1 b1 b1_h1
    play voice "voice/日向怜/121301000.ogg"
    rxl "立花她好像已经洗完了。"
    me01 "那又如何？"
    show rxl_dsf_b1 b1 b1_h3
    play voice "voice/日向怜/121301010.ogg"
    rxl "凉君，趁现在去洗把脸？"
    me01 "无聊的玩笑已经够了。"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121301020.ogg"
    rxl "睡昏头的立花是不会在意的。"
    me01 "怎么可能会有女孩子不在意......"
    stop music fadeout 5.0
    hide rxl_dsf_b2
    $ flcam.move(0, 0, 0, duration=3.0, warper='ease_cubic')
    pause 3.5 hard
    play voice "voice/立花希/031301290.ogg"
    lhx "衣服......"
    pause 1.0 hard
    $ flcam.move(6000, 1800, 1900, duration=2.0, warper='easeout_quint')
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 0.25 alpha 1
    pause 5.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg xizao1
    with slowdissolve
    pause 1.0 hard
    play music second_108 fadein 3.0 if_changed
    play voice "voice/立花希/031301300.ogg"
    lhx "我的......衣服。"
    with vpunch
    me01 "{size=72}噗哈！{/size}"
    "被眼前的一幕吓到，我把喝到一半的茶都喷了出来。"
    play voice "voice/立花希/031301310.ogg"
    lhx "换洗的衣服......在哪里？"
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/立花希/031301320.ogg"
    lhx "日向......我的衣服。"
    show rxl_dsf_b1 b1 b1_sp1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301030.ogg"
    rxl "找不到了吗？"
    hide rxl_dsf_b1
    play voice "voice/立花希/031301330.ogg"
    lhx "嗯......"
    show rxl_dsf_b1 b1 b1_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301040.ogg"
    rxl "不是因为你自己睡昏头了所以忘记拿了吗？"
    hide rxl_dsf_b1
    play voice "voice/立花希/031301340.ogg"
    lhx "我是不可能会做出那种事......"
    show rxl_dsf_b1 b1 b1_h3 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301050.ogg"
    rxl "立花真是个糊涂虫啊~"
    hide rxl_dsf_b1
    play voice "voice/立花希/031301350.ogg"
    lhx "才不是......"
    "两个人悠闲地对话着。"
    "完全忽略了我的存在。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/立花希/031301360.ogg"
    lhx "衣服......在哪？"
    "卷着浴巾的只有头而已。"
    "其他部位完美地暴露在了空气中。"
    "总之......被看光了。"
    show rxl_dsf_b1 b1 b1_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301060.ogg"
    rxl "凉君，脸好红~"
    hide rxl_dsf_b1
    show rxl_dsf_b1 b1 b1_h3 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301070.ogg"
    rxl "是得好好感谢一下你自己的幸运了吧？"
    hide rxl_dsf_b1
    me01 "我闻到了阴谋的味道！"
    play voice "voice/立花希/031301370.ogg"
    lhx "衣服......在哪里？"
    me01 "那个立花老师......别这副打扮到处转悠比较好。"
    show rxl_dsf_b2 b2 b2_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301080.ogg"
    rxl "衣服的话不是应该在房间里吗？"
    hide rxl_dsf_b2
    play voice "voice/立花希/031301380.ogg"
    lhx "帮我拿过来......"
    show rxl_dsf_b1 b1 b1_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301090.ogg"
    rxl "真拿你没办法啊，立花就在这里等等吧~"
    hide rxl_dsf_b1
    me01 "等等，别丢下我一个人啊？！"
    show rxl_dsf_b1 b1 b1_h2 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301100.ogg"
    rxl "凉君，现在可以去洗把脸了吧？"
    hide rxl_dsf_b1
    me01 "所以说现在不是说这个的时候！"
    with vpunch
    show rxl_dsf_b2 b2 b2_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301110.ogg"
    rxl "立花，你去玄关那里等我吧。"
    hide rxl_dsf_b2
    play voice "voice/立花希/031301390.ogg"
    lhx "嗯......"
    "可恶，逃跑的路线被封锁了！"
    show rxl_dsf_b1 b1 b1_h2 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301120.ogg"
    rxl "凉君，就拜托你好好照顾立花喽~"
    show rxl_dsf_b1 b1 b1_h3
    play voice "voice/日向怜/121301130.ogg"
    rxl "顺便欣赏一下她那水灵的肌肤。"
    hide rxl_dsf_b1
    me01 "果然一切都是你的阴谋！"
    show rxl_dsf_b1 b1 b1_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301140.ogg"
    rxl "立花也是，凉君想要逃跑的话记得追上他~"
    hide rxl_dsf_b1
    play voice "voice/立花希/031301400.ogg"
    lhx "嗯......"
    play voice "voice/立花希/031301410.ogg"
    lhx "我一直都在......追赶着凉君的。"
    play voice "voice/立花希/031301420.ogg"
    lhx "......凉君？"
    pause 0.1 hard
    scene set only lhx_cg xizao2
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031301430.ogg"
    lhx "为什么......凉君会在这里？"
    show rxl_dsf_b1 b1 b1_h2 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301150.ogg"
    rxl "他是来偷情的。"
    hide rxl_dsf_b1
    me01 "偷你妹啊！"
    show rxl_dsf_b1 b1 b1_h3 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301160.ogg"
    rxl "然后立花你自己以这幅姿态出来迎接凉君了。"
    hide rxl_dsf_b1
    play voice "voice/立花希/031301440.ogg"
    lhx "你在说什么梦话......"
    show rxl_dsf_b2 b2 b2_s1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301170.ogg"
    rxl "睡迷糊了的明明是立花你。"
    hide rxl_dsf_b2
    play voice "voice/立花希/031301450.ogg"
    lhx "我才不可能是那样的......"
    show rxl_dsf_b1 b1 b1_h1 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301180.ogg"
    rxl "是凉君来偷情然后立花你主动脱了衣服出来迎接。"
    hide rxl_dsf_b1
    play voice "voice/立花希/031301460.ogg"
    lhx "你在说什么蠢话......"
    show rxl_dsf_b1 b1 b1_h3 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301190.ogg"
    rxl "因为现在的立花你不就是全裸的吗？"
    hide rxl_dsf_b1
    play voice "voice/立花希/031301470.ogg"
    lhx "欸......"
    pause 0.1 hard
    play sound jump_1
    scene set only lhx_cg xizao3
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/立花希/031301480.ogg"
    lhx "......？！"
    play voice "voice/立花希/031301490.ogg"
    lhx "我、我......为什么？"
    "立花希的视线在我和她之间来回往穿梭着。"
    "刚才还无精打采的脸上突然一片通红。"
    play voice "voice/立花希/031301500.ogg"
    lhx "真、真的是......裸体。"
    play voice "voice/立花希/031301510.ogg"
    lhx "在凉君的面前......裸体。"
    show rxl_dsf_b1 b1 b1_h2 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301200.ogg"
    rxl "这就是你想要迎接凉君的证据哟~"
    hide rxl_dsf_b1
    me01 "你给我适可而止吧！"
    show rxl_dsf_b1 b1 b1_n4 onlayer screens at side_left('rxl'), basicfade
    play voice "voice/日向怜/121301210.ogg"
    rxl "跨年参拜的时候让你们两个人独处的我也是为了立花你着想啊。"
    hide rxl_dsf_b1
    pause 0.1 hard
    scene set only lhx_cg xizao5 
    with dissolve
    play voice "voice/立花希/031301520.ogg"
    lhx "骗人......一定是哪里搞错了。"
    play voice "voice/立花希/031301530.ogg"
    lhx "全、全部......被看到了。"
    play voice "voice/立花希/031301540.ogg"
    lhx "被凉君给......看到了。"
    play voice "voice/立花希/031301550.ogg"
    lhx "这一定......是噩梦。"
    "说话已经开始带着哭腔了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home day lhx_room xuejian
    play sound open_door5 
    with dissolve
    pause 1.0 hard
    "立花希转身躲进了自己的房间。"
    "留在原地的只有依旧尴尬的气氛，和香波淡淡的清香。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dsf_b1 b1 b1_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121301220.ogg"
    rxl "......我是不是应该去道个歉比较好。"
    me01 "说的也是......我也一起吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 0.5 hard
    play sound open_door5
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home day lhx_room xuejian
    $ flcam.move(-4500, 0, 900, duration=1.5)
    with dissolve
    play music second_104 fadein 3.0 if_changed
    pause 1.0 hard
    show lhx_dsf_b1 b1 b1_s3 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/立花希/031301560.ogg"
    lhx "不是做梦......"
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031301570.ogg"
    lhx "去死好了......这个世界的一切都毁灭就好了。"
    show lhx_dsf_b1 b1 b1_a1
    play voice "voice/立花希/031301580.ogg"
    lhx "日向什么的掉进比死亡还痛苦的地狱就好了。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    play sound ganga01
    show rxl_dsf_b1 b1 b1_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121301230.ogg"
    rxl "只有我被特殊对待了？！"
    me01 "本来就是你的错吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 2.0 hard
    scene set only home day lhx_room xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    play music second_112 fadein 3.0 if_changed
    with dissolve
    pause 0.5 hard
    show rxl_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121301240.ogg"
    rxl "那么，换个心情去吃早饭吧~"
    hide rxl_dsf_b2 with None
    pause 0.1 hard
    show rxl_dsf_b1 b1 b1_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121301250.ogg"
    rxl "也顺便去初诣吧。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031301590.ogg"
    lhx "昨晚不是刚刚去过的吗？"
    show rxl_dsf_b1 b1 b1_h3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121301260.ogg"
    rxl "跨年参拜和初诣是不一样的。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031301600.ogg"
    lhx "跨年参拜也算是初诣的形式之一吧。"
    play sound jump_1
    show rxl_dsf_b1 b1 b1_h1 at flu_down(0.35, 20, 2):
        xpos 0.5
    play voice "voice/日向怜/121301270.ogg"
    rxl "行了，快走啦~"
    show lhx_dsf_b2 b2 b2_s4 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/立花希/031301610.ogg"
    lhx "不要拉我。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031301620.ogg"
    lhx "......我要先做些准备，凉君你们先出去吧。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    play sound close_door3
    pause 2.0 hard

label day214.neightbor_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    play music second_102 fadein 3.0 if_changed
    with dissolve
    pause 2.0 hard
    scene set only home lhx_room xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301630.ogg"
    lhx "没被凉君发现吧......"
    "放置钥匙的地方，没有被翻动的痕迹。"
    "说到底就算被看见了，他应该也不知道是什么东西吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only items key
    with dissolve
    pause 1.0 hard
    "犹如护身符一般的钥匙。"
    "立花希每天都会带在身上。"
    pause 1.0 hard
    scene set only home day lhx_room xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show rxl_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121301280.ogg"
    rxl "立花，准备好了吗？"
    show lhx_dsf_b1 b1 b1_sp1 onlayer screens at side_right('lhx'), basicfade
    play voice "voice/立花希/031301640.ogg"
    lhx "好了，现在就过去。"
    hide lhx_dsf_b1
    hide rxl_dsf_b2 with None
    pause 0.1 hard
    show rxl_dsf_b1 b1 b1_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121301290.ogg"
    rxl "我在外面等你了哟~"
    stop music fadeout 5.0
    pause 0.5 hard
    scene black
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home lhx_room xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301650.ogg"
    lhx "......"
    play voice "voice/立花希/031301660.ogg"
    lhx "到头来，凉君在这里住下了。"
    play voice "voice/立花希/031301670.ogg"
    lhx "还用了这张床。"
    show lhx_dsf_b1 b1 b1_s2
    play voice "voice/立花希/031301680.ogg"
    lhx "在我的床上。"
    show lhx_dsf_b1 b1 b1_s3
    play voice "voice/立花希/031301690.ogg"
    lhx "......"
    hide lhx_dsf_b1
    $ flcam.move(2200, 2800, 1100, duration=1.5)
    play sound touch
    with vpunch
    pause 1.0 hard
    "不自觉地脸朝下扑了上去。"
    "就这样趴了一会儿。"
    "觉得快要窒息了。"
    "兴奋的同时还在床上打起了滚。"
    "有种享受的快感。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    play music second_108 fadein 3.0 if_changed
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5 ypos 1.04 alpha 0.0
        parallel:
            linear 0.25 ypos 1.0
        parallel:
            linear 0.25 alpha 1.0
    pause 0.5 hard
    play voice "voice/立花希/031301700.ogg"
    lhx "我到底在做什么啊？！"
    pause 1.0 hard
    scene black 
    with slowdissolve
    play sound open_door5
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only home day neighbor xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show rxl_dsf_b1 b1 b1_ga2 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/121301300.ogg"
    rxl "立花你刚才对着凉君睡过的床单拼命地闻着......"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.3
    play sound jing01
    show tanhao onlayer m2 at tanhao_x03_right:
        xzoom -1
    play voice "voice/立花希/031301710.ogg"
    lhx "才、才没有！"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dsf_b1 b1 b1_h1
    play voice "voice/日向怜/121301320.ogg"
    rxl "那么认真地回味啊~"
    hide lhx_dsf_b2 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_a1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/立花希/031301730.ogg"
    lhx "我才没有！"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121301330.ogg"
    rxl "没关系的，我会对凉君保密的~"
    show rxl_dsf_b2 b2 b2_h1
    play voice "voice/日向怜/121301340.ogg"
    rxl "毕竟就连立花你的裸体都已经深深地烙印在凉君的脑海里了。"
    show lhx_dsf_b3 b3 b3_s1
    play voice "voice/立花希/031301740.ogg"
    lhx "趁日向睡着的时候，切开头盖骨取出大脑用洗涤剂把记忆全部消除吧......"
    hide rxl_dsf_b2 with None
    pause 0.1 hard
    show rxl_dsf_b1 b1 b1_c1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/日向怜/121301350.ogg"
    rxl "抱歉......我再也不敢了，请原谅我吧。"
    show lhx_dsf_b3 b3 b3_sp2
    play voice "voice/立花希/031301750.ogg"
    lhx "怎么没有看到凉君，他去哪里了？"
    hide rxl_dsf_b1
    show rxl_dsf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121301360.ogg"
    rxl "他说要先回青木家一趟，好像是去拿换洗的衣物。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031301760.ogg"
    lhx "也就是说他今晚也要住在我们这里吧？"
    hide rxl_dsf_b2
    show rxl_dsf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/121301370.ogg"
    rxl "太好了呢立花~"
    show lhx_dsf_b2 b2 b2_s1
    play voice "voice/立花希/031301770.ogg"
    lhx "开玩笑的话就免了。"
    show rxl_dsf_b1 b1 b1_sp1
    play voice "voice/日向怜/121301380.ogg"
    rxl "立花你......是喜欢凉君的吧？"
    hide lhx_dsf_b2 with None
    pause 0.1 hard
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/立花希/031301780.ogg"
    lhx "开玩叫的话就免了！（咬舌）"
    show rxl_dsf_b1 b1 b1_h1
    play voice "voice/日向怜/121301390.ogg"
    rxl "我会支持你的，毕竟你们两个很般配嘛~"
    hide rxl_dsf_b1
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/立花希/031301790.ogg"
    lhx "......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ _overworld_label = 'day214'
    $ seen_day214_home_event01 = False
    $ seen_day214_shenshe_event01 = False
    $ seen_day214_balltower_event01 = False
    $ seen_day214_laboratory_event01 = False
    $ seen_day214_neightbor_event02 = False

label day214.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    if _overworld_label == 'day214':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['road2'])
    elif _overworld_label == 'day214.home_event01':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day214.shenshe_event01':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['shenshe'])
    elif _overworld_label == 'day214.balltower_event01':
        show set maps winter day
        $ flcam.move(*overworld.camera_positions['cloqks'])
    elif _overworld_label == 'day214.laboratory_event01':
        show set maps winter night
        $ flcam.move(*overworld.camera_positions['laboratory'])
    elif _overworld_label == 'day214.neightbor_event02':
        show set maps winter night
        $ flcam.move(*overworld.camera_positions['road2'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该先去哪里呢......" nointeract
    call screen rughzenhaide(
        road1=("day214.home_event01", "not seen_day214_home_event01"),
        cloqks=("day214.balltower_event01", "not seen_day214_balltower_event01"),
        shenshe=("day214.shenshe_event01", "not seen_day214_shenshe_event01 and seen_day214_home_event01"),
        laboratory=("day214.laboratory_event01", "not seen_day214_laboratory_event01 and seen_day214_balltower_event01 and seen_day214_shenshe_event01"),
        road2=("day214.neightbor_event02", "not seen_day214_neightbor_event02 and seen_day214_shenshe_event01 and seen_day214_balltower_event01"))
    $ window_animate_outro()
    if _return == 'day214.home_event01':
        $ flcam.move(*overworld.camera_positions['road1'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day214.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day214.shenshe_event01':
        $ flcam.move(*overworld.camera_positions['shenshe'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day214.laboratory_event01':
        $ flcam.move(*overworld.camera_positions['laboratory'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day214.neightbor_event02':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day214.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only home day outside xuejian
    play music second_114 fadein 3.0 if_changed
    with slowdissolve
    pause 2.0 hard
    scene set only street day train station xuejian
    $ flcam.move(-4500, 300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/爱衣/111100620.ogg"
    aiyi "爱衣我非常喜欢这里的电车，就像游乐园的设施一样。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101680.ogg"
    xz "没错，可以悠闲地观赏街边的景色，在观光客眼中也很有人气的。"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101690.ogg"
    xz "不过城里人还是比较喜欢自己开车出门。"
    show aiyi_dzf_b1 b1 b1_sp1
    play voice "voice/爱衣/111100630.ogg"
    aiyi "大哥哥也喜欢电车吗？"
    me01 "毕竟是第一次坐也不太清楚。"
    hide xz_dsf_b3
    show xz_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101700.ogg"
    xz "没坐过吗？"
    me01 "是啊。"
    hide aiyi_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101710.ogg"
    xz "神野君过去来这里的时候是什么样的呢......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    play sound train
    pause 1.0 hard
    "翔子的话还没说完，远处就传来了电车的机器轰鸣声。"
    "没有选择继续话题，翔子只是摇了摇头便拉着爱衣上了车。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day214_home_event01:
        $ seen_day214_home_event01 = True
    $ _overworld_label = 'day214.home_event01'
    jump day214.map

label day214.shenshe_event01:
    $ flcam.move(0, 0, 0)
    scene set only shenshe day xuejian2
    play music second_120 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    "在我们抵达神社的时候，其他前来参拜的人也成群结队地涌了过来。"
    "路边摆满了各种商铺地摊，应该是藤原瞳为了提高收入搞出来的吧。"
    $ flcam.move(-4500, 300, 900, duration=1.5)
    pause 0.5 hard
    show aiyi_dzf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/爱衣/111100650.ogg"
    aiyi "大姐姐，那里有好长的队伍。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show xz_dsf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/翔子/011101750.ogg"
    xz "看样子都是来参拜的客人。"
    me01 "那我们也过去吧。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "就这样我们排到了队伍的最末端。"
    "不愧是新年的第一天，参拜的队伍空前的长。"
    "有不少家庭结伴而行，让这里充满了温馨的氛围。"
    pause 1.0 hard
    scene set only shenshe day xuejian2
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101760.ogg"
    xz "爱衣，想吃点什么我可以去买。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111100660.ogg"
    aiyi "不用，没事的~"
    hide xz_dsf_b2
    show xz_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101770.ogg"
    xz "难得的初诣，想吃什么都可以的。"
    show aiyi_dzf_b1 b1 b1_h1
    play voice "voice/爱衣/111100670.ogg"
    aiyi "那等会儿大家一起去吃吧。"
    show xz_dsf_b3 b3 b3_sp1
    play voice "voice/翔子/011101780.ogg"
    xz "等一下也可以吗？这里的队伍看起来还得排很久的。"
    show aiyi_dzf_b1 b1 b1_s1
    play voice "voice/爱衣/111100680.ogg"
    aiyi "但是，不好好排队的话就没法参拜了。"
    $ flcam.move(-2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b3 b3 b3_h1
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    show xz_dsf_b3 b3 b3_n1
    play voice "voice/翔子/011101790.ogg"
    xz "爱衣真是个懂事的孩子~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    play sound canbai
    with dissolve
    pause 1.0 hard
    "终于轮到我们了。"
    "我和翔子还有爱衣，大家一起摇响神社的铃铛。"
    "同时将香油钱投进钱箱，闭目合掌鞠躬。"
    "话说今年大家都会许些什么愿望呢？"
    "新的一年真叫人期待。"
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    scene set only shenshe day xuejian2
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101810.ogg"
    xz "神野君刚才许了什么愿望？"
    me01 "愿世界和平......之类的。"
    hide xz_dsf_b2
    show xz_dsf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101820.ogg"
    xz "......这种愿望不行的啦，太敷衍是不会灵验的。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/爱衣/111100690.ogg"
    aiyi "大姐姐许了什么愿望？"
    hide xz_dsf_b1
    show xz_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011101830.ogg"
    xz "保密哟~爱衣呢？"
    show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/爱衣/111100700.ogg"
    aiyi "也是保密的哟~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "随着参拜的结束，我们来到了周围的商铺前。"
    "在品尝美食之前先求个护身符。"
    "希望今年也能为我们带来好运。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene set only shenshe day xuejian2
    $ flcam.move(4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    play voice "voice/琉璃/041401040.ogg"
    stranger "啊......"
    play music second_107 fadein 3.0 if_changed
    show liuli_wnf_b3 b3 b3_h1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/琉璃/041401050.ogg"
    liuli "果然是神野前辈~"
    me01 "琉璃，抱歉一开始没有注意到你。"
    hide liuli_wnf_b3
    show liuli_wnf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401070.ogg"
    liuli "我对自己稀薄的存在感有些不安了。"
    "刚想继续聊下去，忽然意识到了自己正陪着翔子她们逛商铺的。"
    hide liuli_wnf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/011102010.ogg"
    xz "没关系的，反正还有很多时间。神野君你就和朋友一起去逛逛吧。"
    "也许是看出了我的为难，翔子先开口了。"
    me01 "抱歉了翔子。"
    pause 0.5 hard
    play sound jiaobu2
    show xz_dsf_b2 b2 b2_n1 onlayer m2 at walkout_r(0.5)
    pause 1.0 hard
    hide xz_dsf_b2
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_wnf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401080.ogg"
    liuli "对不起......我是不是打扰到你们了？"
    me01 "没有的事。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/藤原瞳/131400010.ogg"
    tyt "花山院，原来你在这里啊~"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/131400020.ogg"
    tyt "看你突然跑了过来，还以为发生了什么事了。"
    hide liuli_wnf_b1
    show liuli_wnf_b3 b3 b3_ga3 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401120.ogg"
    liuli "因为看见神野前辈所以就......非常抱歉。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131400040.ogg"
    tyt "所以......你说的那个“神野前辈”是谁？"
    me01 "喂！"
    hide liuli_wnf_b3
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131400050.ogg"
    tyt "非常感谢您今日的参拜，也很感谢对小店的照顾。"
    me01 "说起来除了参拜好像还什么都没买。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131400060.ogg"
    tyt "这个肚兜，真是没用。"
    me01 "你这么说的话绘马匾和护身符就不买了吧。"
    me01 "毕竟我是个{rb}废柴{/rb}{rt}重音{/rt}肚兜嘛。"
    play sound ganga01
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131400070.ogg"
    tyt "是我太肤浅了真的非常抱歉，神野前辈真是我们的大神明~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_wnf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401140.ogg"
    liuli "刚才还在担心二位会不会吵起来，能和解真是太好了~"
    "虽然完全是建立在金钱关系上的友好。"
    me01 "有这么多来客的话，香油钱也会有很多吧？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131400080.ogg"
    tyt "这可是能和夏日祭相媲美的，星天宫年初的压轴活动。"
    me01 "琉璃呢？"
    hide liuli_wnf_b2
    show liuli_wnf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401150.ogg"
    liuli "我是受藤原同学的请求来帮忙的，刚刚还在店里卖东西来着。"
    show tyt_wnf_b1 b1 b1_s2
    play voice "voice/藤原瞳/131400090.ogg"
    tyt "现在是休息时间，我们正在讨论吃午饭的事情。"
    hide tyt_wnf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_wnf_b3
    show liuli_wnf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401160.ogg"
    liuli "神野前辈，可以的话要一起吃吗？"
    me01 "我也一起真的可以吗？"
    hide liuli_wnf_b1
    show liuli_wnf_b3 b3 b3_h1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401170.ogg"
    liuli "这是今年新款的饮料，前辈要尝一下吗？"
    hide liuli_wnf_b3
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    show bottle onlayer texture_c2u
    pause 0.5 hard
    "琉璃拿出了一个罐装的饮料递给我。"
    me01 "这装饰蛮可爱的嘛。"
    hide bottle
    pause 1.0 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/藤原瞳/131400100.ogg"
    tyt "这是我画的，加入了“绘马匾”的元素~"
    me01 "没想到藤原同学你还擅长绘画。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131400110.ogg"
    tyt "我的特长说到底也只有睡觉而已。"
    me01 "话不多说我们先去吃点东西吧。"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131400200.ogg"
    tyt "不只是吃东西，也别忘了买绘马匾和护身符。"
    me01 "你还真只惦记着钱啊......"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131400210.ogg"
    tyt "在此之前要不要先抽个签呢？"
    me01 "求签吗......听起来不错。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401280.ogg"
    liuli "前辈今年是第一次求签吗？"
    me01 "是啊。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131400220.ogg"
    tyt "那就强烈推荐你试试看，花山院也一起吧？"
    hide liuli_wnf_b1
    show liuli_wnf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401290.ogg"
    liuli "可以吗？可是我只是来帮忙的而已。"
    show tyt_wnf_b1 b1 b1_n1
    play voice "voice/藤原瞳/131400230.ogg"
    tyt "现在在休息中所以没关系的。"
    hide liuli_wnf_b3
    show liuli_wnf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401300.ogg"
    liuli "但是我的钱包放在后院了。"
    me01 "琉璃的那份也由我来出吧。"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131400240.ogg"
    tyt "就知道你会这么说~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    me01 "那么首先由我开始。"
    pause 0.5 hard
    play sound canbai
    pause 2.0 hard
    scene set only shenshe day xuejian2
    $ flcam.move(4500, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show liuli_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401310.ogg"
    liuli "怎么样？"
    hide liuli_wnf_b1
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 1.0 hard
    show qian onlayer texture_c2u
    pause 1.0 hard
    me01 "{size=72}大大凶？！{/size}" with vpunch
    hide qian
    pause 1.0 hard
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_wnf_b1 b1 b1_sp1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/琉璃/041401320.ogg"
    liuli "......欸？"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/藤原瞳/131400250.ogg"
    tyt "就是那个比大凶还要险恶的，换句话说也就是最坏的运势——传说中的大大凶吗。"
    me01 "人生第一次抽签，居然就抽到了大大凶......"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131400260.ogg"
    tyt "真是恭喜您了，拍手拍手拍手。"
    hide liuli_wnf_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "当心我把签塞进你的嘴里去！"
    show tyt_wnf_b1 b1 b1_sp1
    play voice "voice/藤原瞳/131400270.ogg"
    tyt "明明我还好心给你安利。"
    me01 "所以说都是你的馊主意。"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131400280.ogg"
    tyt "噗~"
    me01 "喂，你刚刚笑了吧？"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131400290.ogg"
    tyt "我只是想说“噗哈”而已。"
    me01 "看来你不是很想要我的香油钱了。"
    show tyt_wnf_b1 b1 b1_s3
    play voice "voice/藤原瞳/131400300.ogg"
    tyt "我真是太肤浅了，前辈真是神明大人。"
    me01 "你知道就好。"
    show tyt_wnf_b1 b1 b1_h1
    play voice "voice/藤原瞳/131400310.ogg"
    tyt "真不愧是“噗哈”之神呢~"
    me01 "不绑签了，我还是把你绑在树上吧。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_wnf_b2 b2 b2_sp2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401330.ogg"
    liuli "前、前辈，请冷静一点！"
    hide tyt_wnf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_wnf_b2 b2 b2_h1
    play voice "voice/琉璃/041401340.ogg"
    liuli "那、那么接下来就轮到我了，前辈请一定要保持冷静。"
    play sound canbai
    show liuli_wnf_b2 b2 b2_h1 at flu_down(0.15, 20):
        xpos 0.7
    pause 0.5 hard
    play sound jing03
    pause 0.5 hard
    "大吉。"
    "不愧是琉璃，好孩子的运气都不会差。"
    "话说我到底在期待什么......"
    hide liuli_wnf_b2
    show liuli_wnf_b3 b3 b3_n3 onlayer m2:
        xpos 0.7
    me01 "快停下！不、不要用这种眼神看着我。"
    hide liuli_wnf_b3
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/藤原瞳/131400360.ogg"
    tyt "人生第一次抽签就是大大凶，噗哈~"
    me01 "我看该找哪棵树把你绑起来呢？"
    show tyt_wnf_b1 b1 b1_n2
    play voice "voice/藤原瞳/131400370.ogg"
    tyt "这概率就和彩票连续抽中一等奖是一样，前辈的运气还真是不错呢~"
    me01 "大大凶是倒数一吧！"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131400380.ogg"
    tyt "噗哈~"
    me01 "我记得这里好像就有棵树......"
    hide tyt_wnf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_wnf_b2 b2 b2_sp2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/琉璃/041401390.ogg"
    liuli "前、前辈，请冷静一下！"
    me01 "不过，抽签什么的说到底也只是迷信而已。"
    show liuli_wnf_b2 b2 b2_sp1
    play voice "voice/琉璃/041401400.ogg"
    liuli "已经不在意了吗？"
    me01 "是啊，从一开始我就没打算太在意的啊哈哈。"
    hide liuli_wnf_b2
    show liuli_wnf_b3 b3 b3_h1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041401410.ogg"
    liuli "那真是太好了。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show tyt_wnf_b1 b1 b1_h1 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/藤原瞳/131400390.ogg"
    tyt "噗哈哈~"
    me01 "接下来就只剩下把这家伙五花大绑了。"
    play sound jump_1
    show liuli_wnf_b3 b3 b3_ga1 at flu_down(0.15, 20):
        xpos 0.7
    show han onlayer m2:
        xalign 0.74 yalign 0.36
    play voice "voice/琉璃/041401420.ogg"
    liuli "这不还是很在意吗？！请快点冷静下来。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day214.shenshe_event02:
    $ flcam.move(0, 0, 0)
    scene set only shenshe day xuejian2
    with dissolve
    pause 1.0 hard
    "在琉璃的极力劝阻下，最终还是避免了对巫女实施五花大绑计划。"
    play music second_120 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    me01 "你在看什么呢？"
    show lhx_dsf_b1 b1 b1_sp1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/031301820.ogg"
    lhx "呀！"
    "立花希被我突然的问候吓了一跳，慌忙地把手里的钥匙收到背后。"
    me01 "这是公寓的钥匙？"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301830.ogg"
    lhx "不是。"
    me01 "嘛，倒是无所谓了。"
    show lhx_dsf_b2 b2 b2_s1
    play voice "voice/立花希/031301840.ogg"
    lhx "话说，既然到了的话先通知我一声啊。"
    me01 "抱歉，我这不是来找你了吗。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301850.ogg"
    lhx "你那边的事情都处理好了吗？"
    me01 "是啊，毕竟翔子事先就已经把衣服都准备好了。"
    me01 "不需要花太多时间。"
    show lhx_dsf_b3 b3 b3_ga1
    play voice "voice/立花希/031301860.ogg"
    lhx "连内裤都是她在整理的吗？"
    me01 "这个嘛......"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301870.ogg"
    lhx "青木同学还真是擅长照顾人。"
    me01 "虽然嘴上倒是挺喜欢抱怨的。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031301880.ogg"
    lhx "凉君不在爱衣她不会寂寞吗？"
    me01 "这一点我倒是觉得不用担心。"
    me01 "话说怎么就你一个人，日向同学呢？"
    show lhx_dsf_b2 b2 b2_s1
    play voice "voice/立花希/031301920.ogg"
    lhx "就在凉君来之前遇到了水之濑凛和泽村柚子。"
    play voice "voice/立花希/031301930.ogg"
    lhx "她们似乎也来初诣的，所以日向就和她们一起行动了。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031301940.ogg"
    lhx "明明擅自拉上我来的也是日向，真是爱给我添麻烦......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301950.ogg"
    lhx "还说要制造二人世界什么的。（小声）"
    play voice "voice/立花希/031301960.ogg"
    lhx "不要这么明显地帮我啊。（小声）"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031301970.ogg"
    lhx "更何况我也没有期待会发生什么......（小声）"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "你怎么了？"
    show lhx_dsf_b2 b2 b2_s1
    play voice "voice/立花希/031301990.ogg"
    lhx "没什么。"
    me01 "那么现在怎么办？"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031302000.ogg"
    lhx "实在冷得受不了了，无论如何先暖暖身子吧。"
    hide lhx_dsf_b2
    pause 1.0 hard
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_wnf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041300070.ogg"
    liuli "继昨天之后二位又一次大驾光临，祝你们新年快乐~"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302020.ogg"
    lhx "新年吉祥，请多关照~"
    hide lhx_dsf_b2
    hide liuli_wnf_b3
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131300050.ogg"
    tyt "喝完甜酒之后别忘了去买绘马匾和护身符。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302030.ogg"
    lhx "身子也暖和了，我们回去吧。"
    show tyt_wnf_b1 b1 b1_s3 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/藤原瞳/131300060.ogg"
    tyt "至少投点香油钱......"
    me01 "真拿你没办法，临走的时候会给的。"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.15, 20):
        xpos 0.3
    play voice "voice/藤原瞳/131300070.ogg"
    tyt "非常感谢，前辈真是神明大人~"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302040.ogg"
    lhx "我的话喝点甜酒就够了。"
    show tyt_wnf_b1 b1 b1_s1
    play voice "voice/藤原瞳/131300080.ogg"
    tyt "这个飞机场，真是派不上用场。"
    show lhx_dsf_b3 b3 b3_ga1
    play voice "voice/立花希/031302050.ogg"
    lhx "我好像幻听了，如果不是幻听的话我可能已经发飙了。"
    hide lhx_dsf_b3
    hide tyt_wnf_b1
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_wnf_b2 b2 b2_c1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041300090.ogg"
    liuli "两、两位请不要吵架！"
    me01 "没错，会给其他客人添麻烦的。"
    hide liuli_wnf_b2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show tyt_wnf_b1 b1 b1_s1 onlayer m2:
        xpos 0.3
    play voice "voice/藤原瞳/131300110.ogg"
    tyt "香油钱就拜托了。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show lhx_dsf_b2 b2 b2_h2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302090.ogg"
    lhx "如果你叫我神明大人的话，我就考虑考虑。"
    show tyt_wnf_b1 b1 b1_h1 at flu_down(0.35, 20):
        xpos 0.3
    play voice "voice/藤原瞳/131300120.ogg"
    tyt "拜托你了，飞机场一样的年糕神大人。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302100.ogg"
    lhx "总有一天我必须和这个守财奴巫女做个了断......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day214_shenshe_event01:
        $ seen_day214_shenshe_event01 = True
    $ _overworld_label = 'day214.shenshe_event01'
    jump day214.map

label day214.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    show snow_level1 onlayer fg
    with dissolve
    pause 2.0 hard
    scene set only balltower snow day xuejian2
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001100080.ogg"
    stranger "还在......迷茫吗？"
    pause 0.5 hard
    play music second_103 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100090.ogg"
    xfe "还在烦恼是不是应该放弃吗？"
    me01 "希菲尔......"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100100.ogg"
    xfe "凉君，新年快乐~"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001100110.ogg"
    xfe "但是，“今年也多多关照”之类的话就不说了。"
    me01 "是这样吗？"
    show ts_xfe_yjz_b2 b2 b2_s3
    play voice "voice/希菲尔/001100120.ogg"
    xfe "就是这样的。"
    me01 "希菲尔你莫非是要离开雪见市了？"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100130.ogg"
    xfe "凉君是这样认为的吗？"
    me01 "不知道......但是无论如何我都不希望这样的事情发生。"
    me01 "我不想和希菲尔分开。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100140.ogg"
    xfe "凉君，真是优柔寡断。"
    show ts_xfe_yjz_b2 b2 b2_ga3
    play voice "voice/希菲尔/001100150.ogg"
    xfe "这点和以前一样完全没有改变。"
    me01 "可是大家都说我改变了。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001100160.ogg"
    xfe "对我来说凉君是没有改变。"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001100170.ogg"
    xfe "对希菲尔来说凉君并没有改变。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100180.ogg"
    xfe "一起玩耍的记忆，没有改变......"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100190.ogg"
    xfe "一直、都不希望它有所改变......"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001100200.ogg"
    xfe "不管是凉君、这座城市、还是这场雪......"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001100210.ogg"
    xfe "一直希望两人的足迹能够延续下去，永远也不会消失。"
    show ts_xfe_yjz_b1 b1 b1_s3
    play voice "voice/希菲尔/001100220.ogg"
    xfe "但是，现在的雪已经无法维持了。"
    play voice "voice/希菲尔/001100230.ogg"
    xfe "温柔的雪已经，无法继续维持下去了。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001100240.ogg"
    xfe "想要在这样的雪道上留下足迹，恐怕已经......做不到了。"
    me01 "即使如此我还是想和以前一样和希菲尔一起玩。"
    show ts_xfe_yjz_b1 b1 b1_sp1
    xfe "......"
    me01 "希菲尔？"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100250.ogg"
    xfe "......没什么。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100260.ogg"
    xfe "如果凉君不再寂寞的话，希菲尔也就不会寂寞了。"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001100270.ogg"
    xfe "只要凉君快乐的话，希菲尔也会很快乐的。"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100280.ogg"
    xfe "因为凉君已经找到了......能陪你一起玩耍的新伙伴了。"
    play voice "voice/希菲尔/001100290.ogg"
    xfe "已经有了新的家人。"
    show ts_xfe_yjz_b3 b3 b3_h1
    play voice "voice/希菲尔/001100300.ogg"
    xfe "即使春天降临......也不再是孤单一人了。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_h2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001100310.ogg"
    xfe "拜拜，凉君。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001100320.ogg"
    xfe "新的家人们，都在等着凉君你呢~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day214_balltower_event01:
        $ seen_day214_balltower_event01 = True
    $ _overworld_label = 'day214.balltower_event01'
    jump day214.map

label day214.neightbor_event02:
    $ flcam.move(0, 0, 0)
    scene set only home night lhx_room xuejian
    play music second_105 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302840.ogg"
    lhx "刚才日向打电话来。"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031302850.ogg"
    lhx "说是要住在朋友那里，今天就不回来了。"
    me01 "大过年的去打扰别人真的好吗？"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302860.ogg"
    lhx "凉君你这是五十步笑百步。"
    me01 "抱歉......"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302910.ogg"
    lhx "日向不在，只做两人份的晚饭倒是轻松了些。"
    me01 "立花老师一个人做没问题吗？"
    hide lhx_dsf_b1
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302920.ogg"
    lhx "虽然平时都是我和日向轮流做的，但是嫌麻烦的时候也会去外面吃。"
    me01 "简单的料理还是没问题的吧。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302930.ogg"
    lhx "荞麦面以外的东西我也是会做的。"
    me01 "需要我帮忙吗？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031302940.ogg"
    lhx "不用，凉君你也不擅长做这种事情吧？"
    me01 "请不要用和翔子一样的语气挖苦我。"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/031302950.ogg"
    lhx "我姑且还是有自己做饭的，毕竟在幼儿园的时候也是有大展身手的必要。"
    me01 "既然这样的话料理就交给你了。"
    show lhx_dsf_b2 b2 b2_h2
    play voice "voice/立花希/031302960.ogg"
    lhx "请先行买单~"
    me01 "要收钱的吗。"
    show lhx_dsf_b2 b2 b2_ga3
    play voice "voice/立花希/031302970.ogg"
    lhx "开玩笑的，食材方面凉君也已经分担过了。"
    me01 "毕竟我也给你添了不少麻烦，这种程度还是应该的。"
    show lhx_dsf_b2 b2 b2_n1
    play voice "voice/立花希/031302980.ogg"
    lhx "那么在吃饭前凉君先去洗个澡吧。"
    me01 "可以借用浴室吗？"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031302990.ogg"
    lhx "总比让你现在这样脏着身子要好得多。"
    me01 "那就这样决定了。"
    show lhx_dsf_b2 b2 b2_sp1
    play voice "voice/立花希/031303000.ogg"
    lhx "凉君是淋浴派吗？"
    me01 "在翔子家的时候泡澡已经成了日常事宜了。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031303010.ogg"
    lhx "毕竟在一般的家庭里习惯晚上泡澡的还是比较多的。"
    play voice "voice/立花希/031303020.ogg"
    lhx "今天晚上也可以试着泡澡的，反正等一下我也要去泡~"
    me01 "但是，立花老师你不是早上冲过澡了吗？"
    show lhx_dsf_b2 b2 b2_h3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031303040.ogg"
    lhx "虽说我是淋浴派的，但是......（小声）"
    me01 "怎么了？"
    show lhx_dsf_b2 b2 b2_s2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/立花希/031303050.ogg"
    lhx "什么都没有。"
    me01 "那我先去烧洗澡水了。"
    show lhx_dsf_b2 b2 b2_h2
    play voice "voice/立花希/031303060.ogg"
    lhx "走好~"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    show snow_level1 onlayer fg
    with dissolve
    pause 2.0 hard
    hide snow_level1
    scene set only home night lhx_room xuejian
    with dissolve
    pause 2.0 hard
    me01 "噢噢，闻起来味道不错嘛~"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303070.ogg"
    lhx "机会难得就试着做成正月餐的形式了，但是很多东西都是现成的就是了。"
    me01 "也就是说有不少是立花老师亲手做的料理吧？"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031303080.ogg"
    lhx "嘛，有是有......"
    me01 "是哪个？"
    show lhx_dsf_b2 b2 b2_s2
    play voice "voice/立花希/031303090.ogg"
    lhx "你问这个做什么？"
    me01 "当然是马上尝尝看。"
    show lhx_dsf_b2 b2 b2_s4
    play voice "voice/立花希/031303100.ogg"
    lhx "反正你是想嘲笑我的吧。"
    me01 "你把我当成什么人了......"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303110.ogg"
    lhx "这个煎蛋卷是我做的。"
    hide lhx_dsf_b3 with None
    pause 0.1 hard
    show lhx_dsf_b2 b2 b2_h3 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031303120.ogg"
    lhx "姑、姑且算是自信之作。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_ga2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303130.ogg"
    lhx "不过......虽然外观好看，还请不要期待味道。"
    me01 "我可以吃吗？"
    show lhx_dsf_b3 b3 b3_ga1
    play voice "voice/立花希/031303140.ogg"
    lhx "好不容易准备的你要是不吃的话，我恐怕就要发飙了。"
    me01 "那我就不客气了。"
    show lhx_dsf_b3 b3 b3_sp2
    play voice "voice/立花希/031303150.ogg"
    lhx "......"
    "立花希目不转睛地看着我夹起煎蛋卷送进嘴里。"
    "叭咕。"
    with vpunch
    me01 "{size=72}噢噢！{/size}"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303160.ogg"
    lhx "反正一定是觉得青木同学做的饭比较好吃吧。"
    me01 "才不是呢，这个真的很好吃啊！"
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031303170.ogg"
    lhx "......反正你也只是来安慰我的。"
    me01 "立花老师你不吃吗？"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303180.ogg"
    lhx "要吃......我开动了~"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    "就这样我们一起吃完了新年的第一顿晚饭。"
    "虽然猜到了，但立花老师的饭量真是小得惊人。"
    "每吃一口，都要间隔好长一段时间。"
    pause 1.0 hard
    hide snow_level1
    scene set only home night lhx_room xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    me01 "多谢款待~"
    show lhx_dsf_b2 b2 b2_h1
    play voice "voice/立花希/031303190.ogg"
    lhx "粗茶淡饭而已。"
    me01 "真是太满足了。"
    hide lhx_dsf_b2
    show lhx_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303200.ogg"
    lhx "不用特意说些奉承我的话。"
    me01 "我只是坦率地表达了自己的想法而已。"
    me01 "我来帮忙洗碗吧？"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303210.ogg"
    lhx "不用，反正这个你也不擅长。"
    me01 "确认一下，难道我在你的眼里就这么废材吗？"
    show lhx_dsf_b3 b3 b3_n1
    play voice "voice/立花希/031303220.ogg"
    lhx "如果你想反驳的话，就让我看看你的实力吧。"
    me01 "求之不得！"
    me01 "相对的这次轮到立花老师去洗澡了。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303230.ogg"
    lhx "不，我也要一起帮忙。"
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303240.ogg"
    lhx "凉君负责来洗碗我负责收拾，这样应该更有效率。"
    me01 "噢，搭档~"
    show lhx_dsf_b3 b3 b3_ga3
    play voice "voice/立花希/031303250.ogg"
    lhx "倒也不是这么夸张的组合。"
    me01 "觉得帅气的只有我一个？！"
    show lhx_dsf_b3 b3 b3_ga2
    play voice "voice/立花希/031303260.ogg"
    lhx "虽然确实不坏......"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    scene set only home night lhx_room xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b3 b3 b3_sp2 onlayer m2:
        xpos 0.5
    me01 "立花老师，你不是要去泡澡吗？"
    show lhx_dsf_b3 b3 b3_sp1
    play voice "voice/立花希/031303270.ogg"
    lhx "等下我会去的，话说为什么凉君要一直提醒我啊？"
    me01 "......也没为什么特别的。"
    show lhx_dsf_b3 b3 b3_ga2
    play voice "voice/立花希/031303280.ogg"
    lhx "该不会是想偷窥我换衣服吧？"
    me01 "别开玩叫了！（咬舌）"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303290.ogg"
    lhx "凉君什么的，去当你的幸运色狼就好了。"
    me01 "那个早上的时候已经体验过了。"
    show lhx_dsf_b2 b2 b2_h3 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/立花希/031303300.ogg"
    lhx "......请不要让我想起那个。"    
    me01 "是你自己引出的话题吧。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303310.ogg"
    lhx "凉君你觉得那个事故算是幸运吗？"
    me01 "不是说不想回忆的吗？"
    me01 "与其说是幸运，不如说是惊讶吧......"
    show lhx_dsf_b3 b3 b3_ga1
    play voice "voice/立花希/031303320.ogg"
    lhx "对现在的凉君而言，不成体统的我恐怕已经被深深地烙印在你的脑海里了吧。"
    hide lhx_dsf_b3
    show lhx_dsf_b1 b1 b1_c1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303330.ogg"
    lhx "这样下去，凉君一定会把我当成深夜点心享用的。"
    show lhx_dsf_b1 b1 b1_s1
    play voice "voice/立花希/031303340.ogg"
    lhx "请不要对我做下流的事情~"
    me01 "不得不说你的脑洞才是最让我感到惊讶的......"
    hide lhx_dsf_b1
    show lhx_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303350.ogg"
    lhx "为什么凉君总是那么冷淡啊！"
    me01 "为何你反而生气了？"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303360.ogg"
    lhx "反正我就是个飞机场......"
    me01 "那个，立花老师。"
    me01 "莫非是因为我说“对你的身体没兴趣”之类的所以生气的吧？"
    pause 0.5 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg bed4
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031303370.ogg"
    lhx "暖呼呼~"
    me01 "果然和日向同学说的一样，话锋不对就捂暖。"
    pause 1.0 hard
    scene set only home night lhx_room xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show lhx_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303380.ogg"
    lhx "吃蜜柑吗？"
    me01 "蜜柑啊......"
    show lhx_dsf_b2 b2 b2_ga1
    play voice "voice/立花希/031303390.ogg"
    lhx "要吃还是不吃，到底是哪个？"
    me01 "当然要吃，那我就不客气了~"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide lhx_dsf_b2
    show lhx_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303400.ogg"
    lhx "反应那么迟钝，是困了吗？"
    show lhx_dsf_b3 b3 b3_s2
    play voice "voice/立花希/031303410.ogg"
    lhx "可是时间还很早。"
    me01 "从昨天的跨年参拜开始就一直很累人。"
    hide lhx_dsf_b3
    show lhx_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/立花希/031303420.ogg"
    lhx "跨年参拜确实很累。"
    me01 "况且今天还去了初诣。"
    show lhx_dsf_b2 b2 b2_h1
    play voice "voice/立花希/031303430.ogg"
    lhx "那我也早点休息好了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lhx_cg bed3
    with slowdissolve
    pause 1.0 hard
    play voice "voice/立花希/031303440.ogg"
    lhx "暖呼呼~"
    me01 "可别在被炉里睡着了。"
    play voice "voice/立花希/031303450.ogg"
    lhx "被炉加蜜柑才是冬天应该有的样子嘛~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard
    if not seen_day214_neightbor_event02:
        $ seen_day214_neightbor_event02 = True
    $ _overworld_label = 'day214.neightbor_event02'
    if seen_day214_laboratory_event01:
        jump day214.myroom_event01
    jump day214.map

label day214.laboratory_event01:
    $ flcam.move(0, 0, 0)
    play sound jiaobu2
    scene set only laboratory inside1 xuejian
    with slowdissolve
    pause 1.0 hard
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/琉璃/041500010.ogg"
    liuli "啊......水之濑前辈。"
    play music second_118 fadein 3.0 if_changed
    $ flcam.move(2250, 0, 750, duration=1.5)
    show szl_dsf_b3 b3 b3_sp1 onlayer m1 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/水之濑/051503830.ogg"
    szl "你连这种日子也要来见主任吗？"
    show szl_dsf_b3 b3 b3_s2
    play voice "voice/水之濑/051503840.ogg"
    szl "虽说我也没有什么资格说你就是了。"
    show liuli_dsf_b2 b2 b2_n1
    play voice "voice/琉璃/041500020.ogg"
    liuli "去年受大家的各种照顾，所以想来问候一下~"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500030.ogg"
    liuli "也祝水之濑前辈新年快乐，今年还请多多关照~"
    hide szl_dsf_b3
    show szl_dsf_b1 b1 b1_s2 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051503850.ogg"
    szl "可我什么也没有做，也没打算去做什么......"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051503860.ogg"
    szl "但是......也祝你新年快乐。"
    hide liuli_dsf_b3 with None
    pause 0.1 hard
    show liuli_dsf_b2 b2 b2_h1 onlayer m2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/琉璃/041500040.ogg"
    liuli "是，十分感谢~"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show liuli_dsf_b2 b2 b2_sp1
    play voice "voice/琉璃/041500050.ogg"
    liuli "水之濑前辈是顺道过来的吗？"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_n1 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051503870.ogg"
    szl "算是吧。倒是你......"
    show szl_dsf_b3 b3 b3_s2
    play voice "voice/水之濑/051503880.ogg"
    szl "难不成一整天都在走访问候吗？"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500060.ogg"
    liuli "不，并不是那样的。"
    show liuli_dsf_b3 b3 b3_h1
    play voice "voice/琉璃/041500070.ogg"
    liuli "到刚才为止，我都在神社帮忙。"
    show szl_dsf_b3 b3 b3_sp1
    play voice "voice/水之濑/051503890.ogg"
    szl "......这点倒是有些意外。"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500080.ogg"
    liuli "意外？"
    show szl_dsf_b3 b3 b3_n1
    play voice "voice/水之濑/051503900.ogg"
    szl "因为我也去了神社，刚从初诣赶回来的。"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500090.ogg"
    liuli "......"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_ga1 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051503910.ogg"
    szl "你那是什么表情啊？"
    hide liuli_dsf_b3 with None
    pause 0.1 hard
    show liuli_dsf_b2 b2 b2_sp2 onlayer m2 at flu_down(0.15, 20, 2):
        xpos 0.7
    play voice "voice/琉璃/041500100.ogg"
    liuli "啊不是的，对不起......"
    show liuli_dsf_b2 b2 b2_ga3
    play voice "voice/琉璃/041500110.ogg"
    liuli "因为我以为水之濑前辈和圣护院小姐一样，是对这种例行活动丝毫不感兴趣的类型。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s3 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051503920.ogg"
    szl "......这一点我倒不否认。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500120.ogg"
    liuli "也没有和家人一起过节的习惯。"
    show szl_dsf_b1 b1 b1_s2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051503930.ogg"
    szl "......所以说我们不要再继续这个话题了。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_s2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    play voice "voice/琉璃/041500140.ogg"
    liuli "所以说？"
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_n4 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051503940.ogg"
    szl "请、请不要在意这个。"
    show szl_dsf_b3 b3 b3_s2
    play voice "voice/水之濑/051503950.ogg"
    szl "我只是在刚好很闲的时候，被拉出去的而已。"
    show liuli_dsf_b2 b2 b2_ga3
    play voice "voice/琉璃/041500150.ogg"
    liuli "......是朋友的邀请吧？"
    show szl_dsf_b3 b3 b3_n4
    play voice "voice/水之濑/051503960.ogg"
    szl "也可以说是朋友。"
    play voice "voice/琉璃/041500160.ogg"
    liuli "哈、哈......"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s1 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051503980.ogg"
    szl "话说回来，这孩子......（小声）"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500170.ogg"
    liuli "啊、是的，怎么了？"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s2 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051503990.ogg"
    szl "没什么......因为是无关紧要的事情所以还是不说了。"
    show liuli_dsf_b1 b1 b1_h1
    play voice "voice/琉璃/041500180.ogg"
    liuli "不管是什么请随便说。"
    show szl_dsf_b1 b1 b1_s3
    play voice "voice/水之濑/051504000.ogg"
    szl "......"
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_s2 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504010.ogg"
    szl "我记得，你和神野凉......"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500190.ogg"
    liuli "神野前辈吗？"
    show szl_dsf_b3 b3 b3_ga2
    play voice "voice/水之濑/051504020.ogg"
    szl "嗯，你们相当的......要好对吧？"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_h1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500200.ogg"
    liuli "是的，很荣幸能和他说不少的话。"
    show szl_dsf_b3 b3 b3_s2
    play voice "voice/水之濑/051504030.ogg"
    szl "......"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s3 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504040.ogg"
    szl "你觉得他是个什么样的人？"
    hide liuli_dsf_b3
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500220.ogg"
    liuli "欸？"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_a1 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504050.ogg"
    szl "能告诉我你知道的吗？"
    show liuli_dsf_b2 b2 b2_ga3 at flu_down(0.35, 20):
        xpos 0.67
    play voice "voice/琉璃/041500230.ogg"
    liuli "啊，好的。那个......"
    hide szl_dsf_b3
    $ flcam.move(4500, 0, 900, duration=1.5)
    pause 0.5 hard
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500240.ogg"
    liuli "前辈是个很温柔的人，第一次见面就愿意和我这样孤僻的人做朋友。"
    show liuli_dsf_b1 b1 b1_h1
    play voice "voice/琉璃/041500250.ogg"
    liuli "就连午饭也和我一起吃。"
    hide liuli_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_s4 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504060.ogg"
    szl "......"
    play voice "voice/水之濑/051504070.ogg"
    szl "对花山院问些这些东西，我真是......（小声）"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051504080.ogg"
    szl "而且之前也说了奇怪的话。（小声）"
    show szl_dsf_b2 b2 b2_s3
    play voice "voice/水之濑/051504090.ogg"
    szl "明明这些都和我没有关系的。（小声）"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500260.ogg"
    liuli "那个......水之濑前辈？"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_s2 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504100.ogg"
    szl "我在听的，就这样继续吧。"
    show liuli_dsf_b2 b2 b2_sp2 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/琉璃/041500270.ogg"
    liuli "啊好的，那个......"
    show szl_dsf_b3 b3 b3_n4
    play voice "voice/水之濑/051504110.ogg"
    szl "结果还是忍不住继续听下去了。（小声）"
    hide liuli_dsf_b2
    show liuli_dsf_b3 b3 b3_n4 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500280.ogg"
    liuli "真不可思议。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504120.ogg"
    szl "怎么说？"
    hide liuli_dsf_b3
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500290.ogg"
    liuli "一抱着神野前辈的胳膊，身体就会变热。"
    show szl_dsf_b2 b2 b2_sp2
    play voice "voice/水之濑/051504130.ogg"
    szl "{size=72}什？！{/size}"
    show liuli_dsf_b1 b1 b1_s1
    play voice "voice/琉璃/041500300.ogg"
    liuli "这究竟是为什么呢？"
    $ flcam.move(2250, 0, 900, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_h2
    play voice "voice/水之濑/051504140.ogg"
    szl "{rb}这个{/rb}{rt}抱着胳膊{/rt}我还想问呢？！"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_ga3 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500340.ogg"
    liuli "啊，这都是为了测量体温和脉搏。"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s2 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504180.ogg"
    szl "......我竟然会如此地失态，真是狼狈啊。（小声）"
    show liuli_dsf_b2 b2 b2_sp1
    play voice "voice/琉璃/041500350.ogg"
    liuli "？"
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_ga1 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504190.ogg"
    szl "不用在意，然后怎么样了？"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500360.ogg"
    liuli "前辈他似乎不擅长应付人群。之前一起走在大街上的时候就看到他一副很疲惫的样子。"
    show liuli_dsf_b1 b1 b1_n1
    play voice "voice/琉璃/041500370.ogg"
    liuli "啊对了！前辈还告诉了我很多关于雪见市以前的事情。"
    show szl_dsf_b3 b3 b3_sp1
    play voice "voice/水之濑/051504200.ogg"
    szl "......以前的事？为什么身为转校生的他，会知道这种事情？"
    show liuli_dsf_b1 b1 b1_s2
    play voice "voice/琉璃/041500380.ogg"
    liuli "是的，听说前辈小的时候也来过雪见市。"
    play voice "voice/水之濑/051504210.ogg"
    szl "......"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500390.ogg"
    liuli "所以才告诉我很多他之前在这里发生过的往事。"
    show liuli_dsf_b2 b2 b2_h1
    play voice "voice/琉璃/041500400.ogg"
    liuli "说是久违地又回来了。"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500410.ogg"
    liuli "但不管是自己还是这座城市都改变了，他这样说。"
    hide szl_dsf_b3
    show szl_dsf_b1 b1 b1_s3 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504220.ogg"
    szl "是吗......他也是一样。"
    show liuli_dsf_b1 b1 b1_sp1
    play voice "voice/琉璃/041500420.ogg"
    liuli "？"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051504230.ogg"
    szl "没什么。"
    hide liuli_dsf_b1
    show liuli_dsf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500430.ogg"
    liuli "哈啊......"
    play voice "voice/琉璃/041500440.ogg"
    liuli "话说回来，水之濑前辈。"
    show szl_dsf_b2 b2 b2_sp1
    play voice "voice/水之濑/051504340.ogg"
    szl "怎、怎么了？"
    hide liuli_dsf_b2
    show liuli_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500450.ogg"
    liuli "虽然这个时候问不太合适。"
    hide liuli_dsf_b1
    show liuli_dsf_b3 b3 b3_n2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500460.ogg"
    liuli "但是为什么，水之濑前辈会那么在意神野前辈呢？"
    hide liuli_dsf_b3
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide szl_dsf_b2 with None
    pause 0.1 hard
    show szl_dsf_b3 b3 b3_n4 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051504350.ogg"
    szl "......"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s1 onlayer m1:
        xpos 0.5
    "水之濑陷入了沉默，为了缓解尴尬只能转移视线。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show liuli_dsf_b2 b2 b2_sp2 onlayer m2:
        xpos 0.7
    play voice "voice/琉璃/041500480.ogg"
    liuli "啊！"
    show szl_dsf_b2 b2 b2_sp1
    show liuli_dsf_b2 b2 b2_h1
    play voice "voice/琉璃/041500490.ogg"
    liuli "水之濑前辈也想和神野前辈搞好关系对吧？"
    show szl_dsf_b2 b2 b2_h2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051504360.ogg"
    szl "才、才不是！"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_s2 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504370.ogg"
    szl "不是那样的，请不要误会了。"
    show szl_dsf_b3 b3 b3_n3
    play voice "voice/水之濑/051504380.ogg"
    szl "我只是想要更多地了解敌人而已！"
    show liuli_dsf_b2 b2 b2_sp1
    play voice "voice/琉璃/041500500.ogg"
    liuli "敌人......吗？"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s1 onlayer m1:
        xpos 0.5
    play voice "voice/水之濑/051504390.ogg"
    szl "没错。"
    hide liuli_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_s3
    play voice "voice/水之濑/051504400.ogg"
    szl "他和我的立场不同。（小声）"
    play voice "voice/水之濑/051504410.ogg"
    szl "就算有一点好感。（小声）"
    show szl_dsf_b2 b2 b2_s1
    play voice "voice/水之濑/051504420.ogg"
    szl "到头来也只能是利害关系不一致的对手而已......（小声）"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    if not seen_day214_laboratory_event01:
        $ seen_day214_laboratory_event01 = True
    $ _overworld_label = 'day214.laboratory_event01'
    if seen_day214_neightbor_event02:
        jump day214.myroom_event01
    jump day214.map

label day214.myroom_event01:
    default seen_lhx_event01 = False
    $ flcam.move(0, 0, 0)
    scene black
    with slowdissolve
    pause 1.0 hard
    scene set only home lhx_room xuejian
    show lhx_dsf_b3 b3 b3_n1 onlayer m2:
        xpos 0.5
    $ flcam.move(0, -400, 600)
    $ flcam.move(0, -100, 400, duration=3.0)
    with dissolve

    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False

    investigation:
        bounds (scale(-200.0), scale(-0.0), 0.0) to (scale(+200.0), scale(+0.0), 684.0)
        menu lhx_dsf_b3 onlayer m2:
            hide screen investigation_popup
            camera_pos (scale(-2097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            move _("浴室") jump day214.lhx_event01
            screen_direction left
            sleep jump day214.sleep

label day214.lhx_event01:
    if not seen_lhx_event01:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ seen_lhx_event01 = True
        $ flcam.move(0, 0, 0)
        scene set only sky night xuejian2
        play music second_105 fadein 3.0 if_changed
        show snow_level1 onlayer fg
        with dissolve
        play sound water
        pause 1.0 hard
        show lhx_dsf_b3 b3 b3_h2 onlayer screens at side_right('lhx'), basicfade
        play voice "voice/立花希/031303550.ogg"
        lhx "凉君泡过的洗澡水......"
        play voice "voice/立花希/031303560.ogg"
        lhx "......"
        play voice "voice/立花希/031303570.ogg"
        lhx "暖呼呼~"
        hide lhx_dsf_b3
        "噗噜噗噜噗噜。"
        "整个人都泡了进去。"
        show lhx_dsf_b3 b3 b3_ga2 onlayer screens at side_right('lhx'), basicfade
        play voice "voice/立花希/031303580.ogg"
        lhx "{size=72}我在做什么啊？！{/size}"
        hide lhx_dsf_b3
    else:
        $ flcam.move(0, 0, 0)
        scene set only sky night xuejian2
        play music second_105 fadein 3.0 if_changed
        show snow_level1 onlayer fg
        with dissolve
        pause 1.0 hard
        show lhx_dsf_b3 b3 b3_ga2 onlayer screens at side_right('lhx'), basicfade
        "噗噜噗噜噗噜。"
        hide lhx_dsf_b3

    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black 
    with slowerdissolve
    pause 2.0 hard
    jump day214.myroom_event01

label day214.sleep:
    menu:
        "早点休息":
            if not seen_lhx_event01:
                window mode thought
                me01 "立花老师不知道睡了没有。"
                $ flcam.move(0, -100, 400, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            show lhx_dsf_b3 b3 b3_h1
            play voice "voice/翔子/010001080.ogg"
            lhx "晚安~"
        "{#cancel}再等等":
            xz "还有什么事情要考虑吗......"
            $ flcam.move(0, -100, 400, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    jump day214.ritroom

label day214.ritroom:
    default seen_day214_ritroom = False
    play music ritroom_day fadein 3.0 if_changed
    play ambience1 ritroom_fireplace fadein 3.0 if_changed

    if not seen_day214_ritroom:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        scene set ritfrontyard summer evening:
            mid spring day
            frontl summer evening
            frontr summer evening
        $ flcam.move(0, 0, 400)
        $ flcam.move(0, 0, 0, duration=1.5)
        with dissolve
        pause 3.0 hard

        scene set ritroom evening:
            eggs
            eggscover
            windchime
            midl
            midc
            midr
            midt
            front1
            front2
            front3
            front6
            front4
            front5
        $ flcam.move(-14575, 0, 0)
        $ flcam.move(14575, 0, 0, duration=3.0, warper='ease_cubic')
        with dissolve
        pause 3.5 hard
        $ flcam.move(-5400, -100, 400, duration=1.5)
        pause 0.25 hard
        show ritona b3 fb5 fa1 fc12 s onlayer m2:
            xpos 0.5
        show ritona b1 fb1 fa0 fc11 s
        ritona "怎么了，看你一脸疲惫？"
        me01 "没什么，也许是最近遇到了太多事情了吧。"
        show ritona b3 fb5 fa1 fc02
        ritona "不管怎样反正与我无关。"
        me01 "弗兰小姐你还是一如既往的冷淡啊。"
        show ritona b1 fb2 fa5 fc12
        ritona "我说你有什么事自己扛着就不冷淡了吗？"
        ritona "本来好心想帮你，可是看到你的样子我就放弃了。"
        me01 "抱歉......"
        show ritona b1 fb5 fa2 fc01
        ritona "行了，我也并不是想要怪你。"
        ritona "想必是遇到了很棘手的敌人了吧？"
        me01 "弗兰小姐你还真是敏锐，明明就是一个家里蹲......"
        show ritona b1 fb4 fa2 fc12 s
        ritona "要、要你管，又不是我自愿待在这里的。"
        ritona "这里面有很深层次的原因。"
        me01 "好的我明白。"
        show ritona b1 fb2 fa5 fc12
        ritona "你这样敷衍让我很伤心啊。"
        show ritona b1 fb4 fa3 fc01
        ritona "真拿你没办法，我就再帮你一次好了。"
        me01 "你说帮我，是要给我介绍强有力的伙伴还是要给我能够一击秒杀BOSS的装备？"
        show ritona b1 fb1 fa5 fc13 s
        ritona "不得不说你的脑洞依旧让我很为难......"
        me01 "什么嘛，既然都不是的话那会是啥？"
        show ritona b3 fb1 fa5 fc02 s
        ritona "总之你先跟我来吧。"
        window mode thought
        me01 "通过「移动」功能跟上芙兰。"
        $ flcam.stop()
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
        $ seen_day214_ritbackyard = False
        $ seen_day214_shop = False
        $ seen_day214_ritroom = True
    else:
        pause 0.5 hard
        scene black with dissolve
        pause 3.0 hard
        scene set ritroom evening:
            eggs
            eggscover
            windchime
            midl
            midc
            midr
            midt
            front1
            front2
            front3
            front6
            front4
            front5
        show ritona b3 fb1 fa0 fc02 onlayer m2:
            xpos 0.5
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-14575.0), scale(-0.0), 0.0) to (scale(+14575.0), scale(+0.0), 1350.0)
        menu ritona onlayer m2:
            camera_pos (scale(-4140), scale(-1010), 800)
            screen_pos (0.5, 1.0)
            screen_direction left
            move _("后院") jump day214.ritbackyard
            sleep jump day214.sleep_memory
            shop jump day214.shop
            member jump day214.stats
            teleport jump day214.teleport
            callback jump day214.callback
            roleroom jump day214.roleroom


label day214.ritbackyard:
    if not seen_day214_ritbackyard:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ flcam.move(-5165, -0, 400, duration=1.5)
        show flora b2 fa0 fb1 fc11
        ritona "行了，我们出发吧。"
        show ritona b1 fb4 fa3 fc11
        ritona "先说好和你想的还是有不少差距的。"
        show ritona b3 fb4 fc12
        ritona "再怎么说今后的战斗也都是你自己的事情，我是不会介入太多的。"
        me01 "明明已经介入得得够多了......"
        show ritona fa5 fc03
        ritona "你说什么？"
        me01 "没有，什么都没有！"
        $ flcam.move(-2010, -760, 1000, duration=1.5)
        show ritona b3 fb4 fa5 fc02 s
        ritona "......"
        pause 0.5 hard
        scene black
        with dissolve
        stop ambience1 fadeout 1.0
        pause 1.0 hard
        $ renpy.block_rollback()
        scene set ritbackyard autumn night:
            fieldc autumn night
            fieldl autumn night
            fieldr autumn night
            frontc autumn night
            frontl autumn night
            frontr autumn night
            mid autumn night
        show ritona b3 fb1 fa0 fc01 onlayer m2:
            xpos 0.3
            xzoom -1
        $ flcam.move(-4600, -1100, 1300)
        $ flcam.move(-4600, -800, 1100, duration=1.5)
        with dissolve
        show ritona b4 fb1 fa8 fc11
        ritona "现在的温度正好合适。"
        show ritona b4 fb1 fa8 fc01
        $ flcam.move(-4200, 0, 0, duration=3.0)
        "院子里长满了各种各样的花草树木。"
        "看起来就像是一座公园一般。"
        $ flcam.move(4200, 0, 0, duration=3.0, warper='ease_cubic')
        show ritona b4 fb1 fa8 fc11
        ritona "这里是我闲来无事种植的药草。"
        show ritona b4 fb1 fa9 fc01
        $ flcam.move(-3300, -800, 1100, duration=1.5, warper='ease_cubic')
        ritona "也许对你今后的战斗会有帮助。"
        ritona "想必你也见识到了各种截然不同的{rb}灵继者{/rb}{rt}elfin{/rt}特有的作战方式。"
        me01 "硬要说区别的话也没什么，总之都挺棘手的。"
        show ritona b3 fb5 fa5 fc02 s
        ritona "......"
        show ritona b2 fb1 fa5 fc02 s
        ritona "该说你是装傻还是真傻，这么重要的事情竟然毫不在意。"
        ritona "听好了，虽然你目前只是掌握了最基础的物理系{rb}灵纹{/rb}{rt}rune{/rt}，但是能够带来各种负面效果的灵魂系{rb}灵纹{/rb}{rt}rune{/rt}反而更容易对你造成威胁。"
        show ritona b3 fb1 fa5 fc02 s
        ritona "总之你先去那里采一株草药给我吧。"
        $ flcam.stop()
        $ camera_move(1400, 800, 300, duration=1.5)
        pause 1.5 hard
        show hintarrow onlayer m1:
            xcenter 0.8
            ypos 0.7
        $ seen_day214_ritbackyard = True
    else:
        scene black
        with dissolve
        stop ambience1 fadeout 1.0
        pause 1.0 hard
        $ renpy.block_rollback()
        scene set ritbackyard autumn night:
            fieldc autumn night
            fieldl autumn night
            fieldr autumn night
            frontc autumn night
            frontl autumn night
            frontr autumn night
            mid autumn night
        show ritona b3 fb1 fa0 fc01 onlayer m2:
            xpos 0.3
            xzoom -1
        $ flcam.move(80, 600, 500)
        $ flcam.move(1400, 800, 300, duration=3.0)
        with dissolve
    
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    investigation:
        bounds (scale(-4100.0), scale(-0.0), 0.0) to (scale(+4100.0), scale(+0.0), 1350.0)
        object ritbackyard-fieldc onlayer m1 jump day214.look_casllion
        menu ritona onlayer m2:
            camera_pos (scale(-2030), scale(-510), 800)
            screen_pos (0.3, 1.0)
            screen_direction right
            move _("室内") jump day214.ritroom


label day214.look_casllion hide:
    hide hintarrow
    if 'casllion dirty' not in investigation.inventory and 'casllion clean' not in investigation.inventory:
        $ flcam.move(5350, 1900, 900, duration=1.5)
        show ritona b3 fb5 fa0 fc02
        ritona "没错，就是这样。"
        $ flcam.move(-3300, -800, 1100, duration=1.5)
        window mode thought
        show ritona b4 fb1 fa1 fc01
        ritona "通过采集这些未加工的药草，能够帮助你炼制强大的{rb}灵纹{/rb}{rt}rune{/rt}药剂。"
        $ flcam.move(1400, 800, 300, duration=1.5)
        ritona "最后就是加工的过程了。"
        window mode thought
        me01 "通过「物品」-「普通药草」-「使用」进行提炼。"
        show ritona b4 fb1 fa0 fc01
        $ flcam.stop()
        pause 0.5 hard
        inventory add casllion dirty
    else:
        $ camera_push()
        $ flcam.move(-1975, -825, 1000, duration=1.5)
        show ritona b4 fb1 fa0 fc01
        ritona "这些药草可是我花了好长的时间精心培育的。"
        show ritona b1 fb4 fa5 fc01
        ritona "你可得好好感谢我啊。"
        me01 "刚刚不是还说不会过度地干涉吗......"
        show ritona b3 fb5 fa0 fc02
        $ flcam.stop()
        $ camera_pop_move(duration=1.5)
        pause 0.5 hard
    jump investigate


label day214.use_casllion:
    $ flcam.move(-1975, -825, 1000, duration=1.5)
    window mode thought
    show ritona b4 fb1 fa0 fc02
    ritona "首先让我们将这些药草洗净。"
    window mode thought
    ritona "然后注入你自己的元素之力在其中。"
    show callflash onlayer texture
    pause 1.0 hard
    window mode thought
    show ritona b4 fb1 fa0 fc03
    ritona "行了，这样一来药草就能识别你的{rb}灵纹{/rb}{rt}rune{/rt}之力并施加相应的庇护了。"
    ritona "当然如果你的灵力纯度更高一些的话，药草还能够产生其他神奇的功效。"
    ritona "这些就等你变强之后再向你解释吧。"
    hide callflash
    pause 0.5 hard
    $ flcam.stop()
    inventory add casllion clean
    jump investigate


label day214.callback:
    default seen_day214_callback = False
    hide screen investigation_popup
    scene black
    pause 1.0 hard

    $ flcam.move(0, 0, 0)
    scene set only fight_cg msk
    with slowdissolve
    pause 0.5 hard

    python:
        can_get_roles = "、".join(["「{}」".format(getattr(store, obj).name) for obj in local_config.role_pool])
        outfits_level1 = [outfit for outfit in outfit_list if "_01" in outfit.objectname]
        outfits_level2 = [outfit for outfit in outfit_list if "_02" in outfit.objectname]
        outfits_level3 = [outfit for outfit in outfit_list if "_03" in outfit.objectname]
        outfits_level4 = [outfit for outfit in outfit_list if "_04" in outfit.objectname]

        equip_is_full = local_config.player.is_equipments_full(recall=1)
        equip_is_full_10 = local_config.player.is_equipments_full(recall=10)

    if not seen_day214_callback:
        $ flcam.move(0, -100, 400, duration=1.5)
        pause 0.5 hard
        show ritona b9 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)
        window mode thought
        ritona "当前可抽取的角色包括[can_get_roles]"
        show ritona b3
        pause 0.15 hard
        show ritona b3 at walkout_r(0.75)
        pause 0.5 hard
        hide ritona b3
        $ flcam.move(0, 0, 0, duration=1.5)
        pause 0.5 hard

        show white onlayer texture:
            additive 1
            alpha 0
            1.75
            linear 0.25 alpha 1
        pause 5.0 hard

        $ seen_day214_callback = True
    
    stop music fadeout 2.0
    pause 1.0 hard
    $ mouse_visible = False
    $ _skipping = renpy.seen_audio("video/second_op.mp4")
    $ config.skipping = None
    scene black
    show movie onlayer master
    play movie "video/second_op.mp4" loop
    play music "video/second_op.mp3" loop
    pause 5.0 hard
    $ _window_animation = 'in'
    $ mouse_visible = True
    
    while True:
        $ detect_drop = False
        $ drag_name = ""

        menu:
            "召唤":
                if equip_is_full:
                    window mode thgouth
                    me01 "装备栏已接近上限，优先清理一下无用道具防止装备无法获取的情况出现。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day206.ritroom
                elif local_config.player.currency >= 160:
                    $ local_config.player.currency -= 160
                    
                    while not detect_drop:
                        call screen send_detective_screen

                    show pooler_move:
                        xalign 0.5
                        yalign 0.35

                    # call screen input_sentence
                    # $ sentence = _return.strip()

                    pause 0.5 hard
                    show wflash onlayer m2
                    play sound chain_voice
                    show chain1 with vpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain2 with hpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain3 with vpunch
                    pause 0.25 hard
                    show wflash onlayer m2
                    play ambience1 pent_charge fadein 1.0
                    show cut_pentblack:
                        xalign 0.5 yalign 0.5
                        zoom 0
                        rotate 0
                        parallel:
                            ease 0.3 zoom 1.0
                        parallel:
                            linear 4.0 rotate 360
                            repeat
                    pause 2.0 hard
                    show white onlayer screens
                    with slowdissolve
                    pause 2.0 hard
                    hide chain1
                    hide chain2
                    hide chain3
                    hide cut_pentblack
                    hide white
                    stop ambience1 fadeout 2.0

                    python:
                        sp_ratio = renpy.random.random()
                        # 角色
                        if sp_ratio <= persistent.ratio_table["role"]:
                            chosen_member_idx = renpy.random.randint(0, len(local_config.role_pool) - 1)
                            chosen_member_objectname = list(local_config.role_pool)[chosen_member_idx]
                            chosen_member = getattr(store, chosen_member_objectname)
                            chosen_name = chosen_member.name

                            renpy.pause(1.0, hard=True)
                            renpy.show("black", layer="f2")
                            renpy.transition(dissolve)
                            renpy.pause(1.0, hard=True)
                            renpy.hide("black", layer="f2")
                            renpy.show("sp_ani_role", layer="screens")
                            renpy.music.play("video/ms2_portal.mp3", synchro_start='movie', channel='sound', loop=False)
                            renpy.pause(0.4)
                            renpy.hide("sp_ani_role", layer="screens")
                            renpy.show("black", layer="f2")
                            renpy.transition(dissolve)
                            renpy.pause(3.0, hard=True)
                            renpy.hide("black", layer="f2")

                            renpy.show(chosen_member.objectname, at_list=[show_player(0.5)], layer="m2")
                            renpy.pause(1.0, hard=True)

                            renpy.say(chosen_name, "我的名字是「[chosen_name]」")
                            renpy.say(chosen_name, "以后请多多指教~")

                            # 已拥有角色：技能等级加1
                            if chosen_name in [obj.name for obj in (local_config.party + local_config.backup)]:
                                for role in local_config.party + local_config.backup:
                                    if role.name == chosen_name:
                                        if any(s.level < 5 for s in role.skills):
                                            selectup_skill = role.skill_levelup()
                                            renpy.say(chosen_name, "技能「[selectup_skill.name]」强化至Lv.[selectup_skill.level]")
                                        else:
                                            local_config.player.currency += 1500
                                        break
                            # 未拥有角色：加入后补队伍
                            elif chosen_name in [getattr(store, obj).name for obj in local_config.role_pool]:
                                local_config.backup.append(chosen_member)
                                renpy.say(chosen_name, "「[chosen_name]」加入队伍")
                            else:
                                local_config.player.currency += 1500

                            renpy.hide(chosen_member.objectname, layer="m2")
                            renpy.pause(0.75, hard=True)
                        # # 道具
                        # elif sp_ratio <= persistent.ratio_table["items"]:
                        #     chosen_item_idx = renpy.random.randint(0, len(local_config.shop_list) - 1)
                        #     chosen_item_objectname = local_config.shop_list[chosen_item_idx]
                        #     chosen_item = getattr(store, chosen_item_objectname)
                        #     chosen_item.get(who=local_config.player)
                        #     chosen_name = chosen_item.name

                        #     if chosen_item.image not in [None, ""]:
                        #         if chosen_item.image == "item01":
                        #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.7, xalign=0.5, yalign=0.5)], layer="m2")
                        #         else:
                        #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.3, xalign=0.5, yalign=0.5)], layer="m2")
                        #         renpy.pause(1.0, hard=True)

                        #     renpy.say(chosen_name, "获得物品「[chosen_name]」")

                        #     renpy.hide(chosen_item.image, layer="m2")
                        #     renpy.pause(0.75, hard=True)
                        # 装备
                        else:
                            if renpy.random.random() <= 0.25:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level1) - 1)
                                chosen_equip = outfits_level1[chosen_equip_idx]
                            elif renpy.random.random() <= 0.5:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level2) - 1)
                                chosen_equip = outfits_level2[chosen_equip_idx]
                            elif renpy.random.random() <= 0.75:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level3) - 1)
                                chosen_equip = outfits_level3[chosen_equip_idx]
                            else:
                                chosen_equip_idx = renpy.random.randint(0, len(outfits_level4) - 1)
                                chosen_equip = outfits_level4[chosen_equip_idx]
                            
                            chosen_equip_objectname = chosen_equip.objectname
                            chosen_equip.get(who=local_config.player)
                            chosen_name = chosen_equip.name
                            
                            renpy.show(chosen_equip_objectname, at_list=[Transform(zoom=1.0, xalign=0.5, yalign=0.5)], layer="m2")
                            renpy.pause(1.0, hard=True)

                            equip_level = ""
                            if "_01" in chosen_equip_objectname:
                                equip_level = "普通"
                            elif "_02" in chosen_equip_objectname:
                                equip_level = "稀有"
                            elif "_03" in chosen_equip_objectname:
                                equip_level = "史诗"
                            else:
                                equip_level = "传说"
                            renpy.say(me01, "获得「[equip_level]」[chosen_equip.category]「[chosen_name]」")

                            renpy.hide(chosen_equip_objectname, layer="m2")
                            renpy.pause(0.75, hard=True)

                    hide pooler_move
                else:
                    window mode thought
                    me01 "魔法币不足500是无法进入异空间的，无论在哪个世界穷是永远的痛！"
                    me01 "快去「异界」获取更多魔法币吧。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day214.ritroom
            "十连召唤":
                if equip_is_full_10:
                    window mode thgouth
                    me01 "装备栏已接近上限，优先清理一下无用道具防止装备无法获取的情况出现。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day206.ritroom
                elif local_config.player.currency >= 1500:
                    $ local_config.player.currency -= 1500

                    while not detect_drop:
                        call screen send_detective_screen

                    show pooler_move:
                        xalign 0.5
                        yalign 0.35

                    # call screen input_sentence
                    # $ sentence = _return.strip()

                    pause 0.5 hard
                    show wflash onlayer m2
                    play sound chain_voice
                    show chain1 with vpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain2 with hpunch
                    pause 0.25 hard
                    play sound chain_voice
                    show chain3 with vpunch
                    pause 0.25 hard
                    show wflash onlayer m2
                    play ambience1 pent_charge fadein 1.0
                    show cut_pentblack:
                        xalign 0.5 yalign 0.5
                        zoom 0
                        rotate 0
                        parallel:
                            ease 0.3 zoom 1.0
                        parallel:
                            linear 4.0 rotate 360
                            repeat
                    pause 2.0 hard
                    show white onlayer screens
                    with slowdissolve
                    pause 2.0 hard
                    hide chain1
                    hide chain2
                    hide chain3
                    hide cut_pentblack
                    hide white
                    stop ambience1 fadeout 2.0
                    
                    python:
                        for i in xrange(10):
                            sp_ratio = renpy.random.random()
                            # 角色
                            if sp_ratio <= persistent.ratio_table["role"]:
                                chosen_member_idx = renpy.random.randint(0, len(local_config.role_pool) - 1)
                                chosen_member_objectname = list(local_config.role_pool)[chosen_member_idx]
                                chosen_member = getattr(store, chosen_member_objectname)
                                chosen_name = chosen_member.name

                                renpy.pause(1.0, hard=True)
                                renpy.show("black", layer="f2")
                                renpy.transition(dissolve)
                                renpy.pause(1.0, hard=True)
                                renpy.hide("black", layer="f2")
                                renpy.show("sp_ani_role", layer="screens")
                                renpy.music.play("video/ms2_portal.mp3", synchro_start='movie', channel='sound', loop=False)
                                renpy.pause(0.4)
                                renpy.hide("sp_ani_role", layer="screens")
                                renpy.show("black", layer="f2")
                                renpy.transition(dissolve)
                                renpy.pause(3.0, hard=True)
                                renpy.hide("black", layer="f2")

                                renpy.show(chosen_member.objectname, at_list=[show_player(0.5)], layer="m2")
                                renpy.pause(1.0, hard=True)

                                renpy.say(chosen_name, "我的名字是「[chosen_name]」{w=1.0}{nw}")
                                renpy.say(chosen_name, "以后请多多指教~{w=1.0}{nw}")

                                # 已拥有角色：技能等级加1
                                if chosen_name in [obj.name for obj in (local_config.party + local_config.backup)]:
                                    for role in local_config.party + local_config.backup:
                                        if role.name == chosen_name:
                                            if any(s.level < 5 for s in role.skills):
                                                selectup_skill = role.skill_levelup()
                                                renpy.say(chosen_name, "技能「[selectup_skill.name]」强化至Lv.[selectup_skill.level]")
                                            else:
                                                local_config.player.currency += 1500
                                            break
                                # 未拥有角色：加入后补队伍
                                elif chosen_name in [getattr(store, obj).name for obj in local_config.role_pool]:
                                    local_config.backup.append(chosen_member)
                                    renpy.say(chosen_name, "「[chosen_name]」加入队伍{w=1.0}{nw}")
                                else:
                                    local_config.player.currency += 1500

                                renpy.hide(chosen_member.objectname, layer="m2")
                                renpy.pause(0.75, hard=True)
                            # 道具
                            # elif sp_ratio <= persistent.ratio_table["items"]:
                            #     chosen_item_idx = renpy.random.randint(0, len(local_config.shop_list) - 1)
                            #     chosen_item_objectname = local_config.shop_list[chosen_item_idx]
                            #     chosen_item = getattr(store, chosen_item_objectname)
                            #     chosen_item.get(who=local_config.player)
                            #     chosen_name = chosen_item.name

                            #     if chosen_item.image not in [None, ""]:
                            #         if chosen_item.image == "item01":
                            #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.7, xalign=0.5, yalign=0.5)], layer="m2")
                            #         else:
                            #             renpy.show(chosen_item.image, at_list=[Transform(zoom=0.3, xalign=0.5, yalign=0.5)], layer="m2")
                            #         renpy.pause(1.0, hard=True)

                            #     renpy.say(chosen_name, "获得物品「[chosen_name]」{w=1.0}{nw}")

                            #     renpy.hide(chosen_item.image, layer="m2")
                            #     renpy.pause(0.75, hard=True)
                            # 装备
                            else:
                                if renpy.random.random() <= 0.25:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level1) - 1)
                                    chosen_equip = outfits_level1[chosen_equip_idx]
                                elif renpy.random.random() <= 0.5:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level2) - 1)
                                    chosen_equip = outfits_level2[chosen_equip_idx]
                                elif renpy.random.random() <= 0.75:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level3) - 1)
                                    chosen_equip = outfits_level3[chosen_equip_idx]
                                else:
                                    chosen_equip_idx = renpy.random.randint(0, len(outfits_level4) - 1)
                                    chosen_equip = outfits_level4[chosen_equip_idx]
                                
                                chosen_equip_objectname = chosen_equip.objectname
                                chosen_equip.get(who=local_config.player)
                                chosen_name = chosen_equip.name
                                
                                renpy.show(chosen_equip_objectname, at_list=[Transform(zoom=1.0, xalign=0.5, yalign=0.5)], layer="m2")
                                renpy.pause(1.0, hard=True)
                                
                                equip_level = ""
                                if "_01" in chosen_equip_objectname:
                                    equip_level = "普通"
                                elif "_02" in chosen_equip_objectname:
                                    equip_level = "稀有"
                                elif "_03" in chosen_equip_objectname:
                                    equip_level = "史诗"
                                else:
                                    equip_level = "传说"
                                renpy.say(chosen_name, "获得「[equip_level]」[chosen_equip.category]「[chosen_name]」{w=1.0}{nw}")

                                renpy.hide(chosen_equip_objectname, layer="m2")
                                renpy.pause(0.75, hard=True)

                    hide pooler_move
                else:
                    window mode thought
                    me01 "魔法币不足4500是无法进入多重异空间的，无论在哪个世界穷是永远的痛！"
                    me01 "快去「异界」获取更多魔法币吧。"
                    pause 0.5 hard
                    $ window_animate_outro()
                    stop movie
                    hide movie
                    stop music fadeout 1.0
                    $ _skipping = True
                    jump day214.ritroom
            "下次一定":
                window mode thgouth
                me01 "相遇即是缘，请好好珍惜这份来之不易的羁绊。"
                pause 0.5 hard
                $ window_animate_outro()
                stop movie
                hide movie
                stop music fadeout 1.0
                $ _skipping = True
                jump day214.ritroom


label day214.shop:
    hide investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day city3 xuejian
    with slowdissolve
    pause 1.0 hard

    if not seen_day214_shop and 'casllion clean' in investigation.inventory:
        window mode thought
        show ritona b9 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)
        ritona "刚刚你所炼制的药草我已经帮你制作成了许多道具。"
        ritona "虽然可能只是冰山一角，但想必对你今后的战斗也是大有帮助。"
        ritona "记得多准备一些以免翻车哟~"
        python:
            local_config.shop_list += ["mana_potion"]
        $ seen_day214_shop = True
    else:
        show ritona b3 fb1 fa0 fc02 onlayer m2 at walkin_r(0.75)

    python:
        config.skipping = None
        renpy.block_rollback()
        _rollback = True

        local_config.current_message = ""
        local_config.current_mode = "buy"
        renpy.retain_after_load()
        _rollback = False

    if _return != False:
        call screen shop
    pause 0.5 hard
    jump day214.ritroom


label day214.stats:
    hide screen investigation_popup

    python:
        for role in local_config.party:
            role.hp = role.max_hp + role.extend_max_hp
            role.mp = role.max_mp
    $ local_config.current_mode == "Consumables"
    $ local_config.current_actor = local_config.party[0]

    call screen stats
    jump investigate


label day214.roleroom:
    hide screen investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)

    python:
        local_config.start_init(local_config.player, local_config.party)
        local_config.next_story = "day214.ritroom"
    
    call info


label day214.teleport:
    hide screen investigation_popup

    python:
        current_message = ""
        
    call screen teleporter("214")
    jump investigate


label day214.sleep_memory:
    menu:
        "结束梦境":
            python:
                ms_average_level = 0
                breakout_flag = []
                outfits_levels = []
                for par_name in local_config.masters:
                    for role in local_config.party:
                        if role.objectname == par_name:
                            ms_average_level += role.level
                            if role.level < 40 and role.level % 5 == 0 and (not role.break_through):
                                breakout_flag.append(False)
                            else:
                                breakout_flag.append(True)
                            for categ, outfit in role.outfits.items():
                                if outfit is not None:
                                    outfits_levels.append(outfit.level)
                                else:
                                    outfits_levels.append(0)
                ms_average_level /= len(local_config.masters)
            
            if 'casllion clean' not in investigation.inventory:
                window mode thought
                me01 "还是先跟上去看看究竟有什么好东西吧。"
                $ camera_move(-5400, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            elif not seen_day214_shop:
                window mode thought
                me01 "刚刚提炼的草药似乎可以在商店里购买了，去看看吧。"
                $ camera_move(-5400, 100, 200, duration=3.0)
                pause 0.5 hard
                jump investigate
            elif (ms_average_level < 30) or (not all(breakout_flag)) or any([l < 8 for l in outfits_levels]):
                window mode thought
                me01 "下一次的敌人可能会比较棘手，还是去「异界」和「养成屋」多准备一下吧。"
                window mode thought
                me01 "确保队伍的平均等级在{color=#ff0000}30级突破{/color}以上、且装备等级均在8级以上比较稳妥。"
                menu:
                    "继续前进（不推荐）":
                        pass
                    "再准备准备":
                        $ camera_move(-5400, 100, 200, duration=3.0)
                        pause 0.5 hard
                        jump investigate
            $ flcam.move(-5400, -100, 400, duration=1.5)
            pause 0.5 hard
            show ritona b1 fb4 fa3 fc01
            ritona "我们还会再见的，神野凉......"
        "{#cancel}再等等":
            ritona "还有什么事情要考虑的吗？"
            $ camera_move(-5400, 100, 200, duration=3.0)
            pause 0.5 hard
            jump investigate

    stop music fadeout 5.0
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard

    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True


label day214.memory_event01:
    $ flcam.move(0, 0, 0)
    nvl clear
    pcenter "是从什么时候开始？"
    pause 0.5 hard
    nvl clear
    with dissolve
    pcenter "我的梦里全都是她的身影？"
    pause 1.0 hard
    nvl clear
    with dissolve
    scene white
    with slowerdissolve
    pause 1.0 hard
    pcenter "又是从什么时候开始。"
    pause 0.5 hard
    nvl clear
    with dissolve
    pcenter "我才明白那笑容背后的孤独呢。"
    pause 1.0 hard
    nvl clear
    with dissolve
    scene set only balltower snow day xuejian
    show snow_level1 onlayer fg
    $ flcam.move(0, 0, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1:
        xpos 0.5
    show alu_ct_b1 b1 b1_1 onlayer m2:
        xpos 0.53 ypos 0.6
    play voice "voice/希菲尔/001000730.ogg"
    xfe "凉君凉君，有大发现哟~"
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_n1 onlayer m1:
        xpos 0.5
    play voice "voice/希菲尔/001000740.ogg"
    xfe "这孩子能从嘴巴里面喷出火来。" 
    play music second_104 fadein 3.0 if_changed
    me01 "什么？"
    show ts_xfe_yjz_b3 b3 b3_h1
    show alu_ct_b1 b1 b1_5
    play voice "voice/希菲尔/001000750.ogg"
    xfe "能够吐出火焰哟~"
    me01 "再怎么说这也是不可能的事情。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_sp1 onlayer m1:
        xpos 0.5
    show alu_ct_b1 b1 b1_4
    play voice "voice/希菲尔/001000770.ogg"
    xfe "是这样吗？"
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg alu1
    with slowdissolve
    pause 0.5 hard
    play voice "voice/阿露/551000090.ogg"
    play sound rell_fire
    pause 0.1 hard
    scene set only xfe_cg alu2
    with dissolve
    alu "{size=72}唔莎~波！{/size}"
    play sound jing01
    show wflash onlayer texture
    with vpunch
    me01 "唔喔喔！？"
    "滚烫的火焰从阿露的口中喷出。"
    pause 0.1 hard
    play sound ganga03
    scene set only xfe_cg alu3
    with dissolve
    play voice "voice/阿露/551000410.ogg" 
    alu "唔、唔莎......"
    pause 0.1 hard
    scene set only xfe_cg alu4
    with dissolve
    play voice "voice/希菲尔/001000790.ogg"
    xfe "阿露，我马上帮你修好！"
    "希菲尔捡起地上的积雪往阿露身上撒。"
    play sound jing03
    pause 0.1 hard
    scene set only xfe_cg alu5
    with dissolve
    play voice "voice/阿露/551000420.ogg" 
    alu "唔莎~"
    "复活了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m1:
        xpos 0.5
    show alu_ct_b1 b1 b1_3 onlayer m2:
        xpos 0.53 ypos 0.6
    with dissolve
    pause 0.5 hard
    me01 "真是随便的生态法则。"
    stop music fadeout 5.0
    "已经不是常理能够解释的程度了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play ambience1 zhong_rill
    scene set only balltower snow day big
    with dissolve
    pause 1.0 hard
    "离别的钟声再次响起。"
    "无论何时它总能如期而至。"
    pause 1.0 hard
    scene set only balltower snow day xuejian
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    play music second_103 fadein 3.0 if_changed
    stop ambience1 fadeout 5.0
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_s1 onlayer m1:
        xpos 0.5
    play voice "voice/希菲尔/001000800.ogg"
    xfe "阿露回去了。"
    me01 "是啊。"
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b2 b2 b2_n2 onlayer m1:
        xpos 0.5
    play voice "voice/希菲尔/001000810.ogg"
    xfe "凉君也是，到了该回去的时间了。"
    me01 "那希菲尔呢？"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001000820.ogg"
    xfe "嗯，希菲尔也......"
    show ts_xfe_yjz_b2 b2 b2_s2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001000830.ogg"
    xfe "不小心又叫自己“希菲尔”了。"
    me01 "希菲尔一直以来不都是这样称呼自己的吗？"
    show ts_xfe_yjz_b2 b2 b2_s1
    play voice "voice/希菲尔/001000840.ogg"
    xfe "想要改掉......"
    me01 "为什么？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b1 b1 b1_n2 onlayer m1:
        xpos 0.5
    play voice "voice/希菲尔/001000850.ogg"
    xfe "我也想......变成大人。"
    show ts_xfe_yjz_b1 b1 b1_h1
    play voice "voice/希菲尔/001000860.ogg"
    xfe "已经不再只是懵懂无知的小孩子了。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001000870.ogg"
    xfe "和凉君。"
    play voice "voice/希菲尔/001000880.ogg"
    xfe "还有千冬一样。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 900)
    scene set only memory_cg winter one
    show sepiagrain onlayer texture
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b2 b2 b2_h4 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/希菲尔/001000890.ogg"
    xfe "“可以来玩”千冬这样对我说了，所以我就来了。"
    me01 "千冬？"
    show ts_xfe_yjz_b2 b2 b2_h1
    play voice "voice/希菲尔/001000900.ogg"
    xfe "她是第一个发现希菲尔的人哟~"
    play voice "voice/希菲尔/001000910.ogg"
    xfe "所以希菲尔也最喜欢千冬了~"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer m1:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/希菲尔/001000920.ogg"
    xfe "明明你们都在成长，却只有我还只是个小孩子。"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001000930.ogg"
    xfe "为什么会这样呢？"
    show ts_xfe_yjz_b1 b1 b1_n1
    play voice "voice/希菲尔/001000940.ogg"
    xfe "所以想要稍微模仿千冬看看。"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001000950.ogg"
    xfe "千冬她用“我”来称呼自己。"
    me01 "希菲尔是真的很喜欢那位叫作“千冬”的人啊。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b1
    show ts_xfe_yjz_b3 b3 b3_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001000960.ogg"
    xfe "嗯，她是希菲尔憧憬的人~"
    show ts_xfe_yjz_b3 b3 b3_n1
    play voice "voice/希菲尔/001000970.ogg"
    xfe "很温柔，也很聪明。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001000980.ogg"
    xfe "教会了什么都不懂的希菲尔很多很多东西。"
    show ts_xfe_yjz_b1 b1 b1_s2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/希菲尔/001000990.ogg"
    xfe "啊......又说了“希菲尔”。"
    me01 "不必在意。"
    show ts_xfe_yjz_b1 b1 b1_s3
    play voice "voice/希菲尔/001001000.ogg"
    xfe "会在意的。"
    me01 "对我来说现在的希菲尔也没有什么不好的。"
    show ts_xfe_yjz_b1 b1 b1_sp1
    play voice "voice/希菲尔/001001010.ogg"
    xfe "是这样吗？"
    me01 "就是这样的。"
    me01 "如果世上总有必须要改变的东西存在，那么相对的也一定存在不希望改变的东西。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg bridge normal
    show sepiagrain onlayer fg
    with slowdissolve
    pause 1.0 hard
    me01 "这座桥的另一头，希菲尔你知道吗？"
    play voice "voice/希菲尔/001001020.ogg"
    xfe "知道哟，该怎么说呢......最近也改变了许多。"
    me01 "要一起去看看吗？"
    play voice "voice/希菲尔/001001030.ogg"
    xfe "还是不要看比较好。"
    play voice "voice/希菲尔/001001040.ogg"
    xfe "那边已经，改变太多了。"
    pause 0.1 hard
    scene set only xfe_cg bridge daze
    with dissolve
    play voice "voice/希菲尔/000000170.ogg"
    xfe "改变了的东西多了，就会觉得寂寞。"
    play voice "voice/希菲尔/000000180.ogg"
    xfe "虽说永恒不变的东西，也许根本就不存在于这个世界上。"
    play voice "voice/希菲尔/000000190.ogg"
    xfe "就算是这座雪见市，大概也不例外吧。"
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
    hide sepiagrain
    scene white with slowerdissolve
    pause 2.0 hard
    "回忆交织在了一起。"
    "一切都宛若是昨天才发生的一般。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    scene set only balltower snow day xuejian
    show snow_level1 onlayer fg
    show ts_xfe_yjz_b1 b1 b1_sp1 onlayer m2:
        xpos 0.5
    me01 "对希菲尔而言，也有不想改变的东西吧？"
    show ts_xfe_yjz_b1 b1 b1_s1
    play voice "voice/希菲尔/001001120.ogg"
    xfe "嗯......和凉君的关系不想改变。"
    show ts_xfe_yjz_b1 b1 b1_s2
    play voice "voice/希菲尔/001001130.ogg"
    xfe "因为离别......是会让人寂寞的东西。"
    show ts_xfe_yjz_b1 b1 b1_s1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001001140.ogg"
    xfe "叭咕叭咕~"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day215
