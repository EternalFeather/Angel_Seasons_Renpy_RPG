
label day231:
    bookmark
    $ save_name = _("Day 231")
    pause 4.0 hard

    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True

    $ flcam.move(0, 0, 0)
    scene black
    with dissolve
    pause 2.0 hard
    scene white
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/999997300.ogg"
    xfe "在这个永恒的白色世界里，我在等待着苏醒之时——"
    pause 1.0 hard
    scene set only memory_cg yuki ground
    play music second_151 fadein 3.0 if_changed
    show snow_level1 onlayer fg
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/999997301.ogg"
    xfe "雪白的天空和雪白的大地，这里便是我的故乡。"
    play voice "voice/希菲尔/999997302.ogg"
    xfe "即使没有亲眼见过，但是在母亲的记忆中无时无刻不让我想起眼前的这幅光景。"
    play voice "voice/希菲尔/999997303.ogg"
    xfe "不知会延伸到哪里的雪道。"
    play voice "voice/希菲尔/999997304.ogg"
    xfe "在足迹蔓延之时，母亲对还没有出生的我低语着。"
    play voice "voice/希菲尔/999997305.ogg"
    xfe "听起来就宛如一首歌。"
    pause 1.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only memory_cg xuejian yume
    $ flcam.moves([
        (0,      0,   400, 0, 0.5, 'linear'),
        (0, -1539, 400, 0, 100.0, 'ease_cubic')
    ])
    with dissolve
    nvl clear
    play voice "voice/诗乃/701000650.ogg"
    pcenter "这颗星球，终将毁灭。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000660.ogg"
    pcenter "洁白的雪原，将会变为赤红的荒野。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000670.ogg"
    pcenter "但是唯独这条生命不会终结。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000680.ogg"
    pcenter "必将永远地延续到下一代继续存在。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000690.ogg"
    pcenter "所以如若可以如愿的话，吾希望能让吾的孩子来继承。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000700.ogg"
    pcenter "延续这——白色永恒的梦。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/999997306.ogg"
    xfe "从母亲那里传承下来的，没有终点的梦。"
    play voice "voice/希菲尔/999997307.ogg"
    xfe "我本来，应该是要实现它的。"
    play voice "voice/希菲尔/999997308.ogg"
    xfe "但是，以前懵懂无知的我，在得知母亲的遗愿之前就已经有了新的愿望。"
    play voice "voice/希菲尔/999997309.ogg"
    xfe "就像母亲希望的那样，比起一个人玩耍，两个人的话会更开心。"
    play voice "voice/希菲尔/999997310.ogg"
    xfe "和最喜欢的他一起的话，就会更加开心了。"
    play voice "voice/希菲尔/999997311.ogg"
    xfe "不只是妖精与妖精和睦地相处在一起。"
    play voice "voice/希菲尔/999997312.ogg"
    xfe "我更希望妖精与人类也能够和睦地相处。"
    play voice "voice/希菲尔/999997313.ogg"
    xfe "所以......为了延续生命而让其他的生命来承担痛苦，是绝对不行的。"
    play voice "voice/希菲尔/999997314.ogg"
    xfe "即使我的生命，不被他所在的那颗蓝色星球所喜爱也罢......"
    pause 2.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    nvl clear
    play voice "voice/诗乃/701000710.ogg"
    pcenter "不要紧的。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000720.ogg"
    pcenter "母亲我向你保证。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000730.ogg"
    pcenter "汝的生命亦会被蓝色星球所接受。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000740.ogg"
    pcenter "陪伴在汝身边的他，就是最好的证明。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 0.5 hard
    play voice "voice/诗乃/701000750.ogg"
    pcenter "白色永恒定会蜕变成为蓝色永恒继续延续下去。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011731.ogg"
    xfe "谢谢你......母亲。"
    play voice "voice/希菲尔/001011732.ogg"
    xfe "让我得以降生在这颗星球上。"
    stop music fadeout 5.0
    pause 3.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day231.home_event01:
    play music second_159 fadein 3.0 if_changed
    me01 "雷亚，你的头发好像又变长了？"
    play voice "voice/天使雷亚/550001.ogg"
    lst "......是这样吗？"
    me01 "是啊，洗起来太麻烦了。"
    play voice "voice/天使雷亚/550002.ogg"
    lst "累了吗？"
    me01 "这倒没有。"
    play voice "voice/天使雷亚/550003.ogg"
    lst "很费时间吗？"
    me01 "不，已经搞定了。"
    me01 "话说不痒吗？"
    play voice "voice/天使雷亚/550004.ogg"
    lst "没事~"
    me01 "那闭上眼睛吧。"
    play voice "voice/天使雷亚/550005.ogg"
    lst "嗯。"
    play sound water
    pause 2.0 hard
    me01 "好了，可以睁开眼睛了。"
    play voice "voice/天使雷亚/550006.ogg"
    lst "呼噜呼噜......"
    me01 "呜哇，不要像小狗一样甩头啊，你的头发像鞭子一样打着我了。"
    play voice "voice/天使雷亚/550007.ogg"
    lst "因为有点冷。"
    me01 "是吗......冬天又到了啊。"
    me01 "回浴缸里去吧。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg end xuejian1
    with cent2side
    pause 1.0 hard
    me01 "水温合适吗？"
    pause 0.1 hard
    scene set only lisite_cg end xuejian2
    with dissolve
    play voice "voice/天使雷亚/550008.ogg"
    lst "刚刚好。"
    me01 "要泡进去吗？"
    pause 0.1 hard
    scene set only lisite_cg end xuejian3
    with dissolve
    play voice "voice/天使雷亚/550009.ogg"
    lst "嗯。"
    me01 "雷亚你为什么总是喜欢靠着我这边啊？"
    me01 "到浴缸的另一边不是更宽敞一些吗？"
    pause 0.1 hard
    scene set only lisite_cg end xuejian2
    with dissolve
    play voice "voice/天使雷亚/550010.ogg"
    lst "是这样吗。"
    me01 "是啊。"
    play voice "voice/天使雷亚/550011.ogg"
    lst "没有这回事。"
    me01 "嘛，虽然也不是很重无所谓了。"
    play voice "voice/天使雷亚/550012.ogg"
    lst "{rb}妈妈{/rb}{rt}指翔子{/rt}更重些吗？"
    me01 "重倒是不重......等等，为什么突然问这个啊？！"
    play voice "voice/天使雷亚/550013.ogg"
    lst "因为妈妈经常说想要这样和凉君一起洗的。"
    me01 "为什么翔子她会把这种的事情和你说啊......"
    play voice "voice/天使雷亚/550014.ogg"
    lst "因为，凉君总是和妈妈在一起。"
    me01 "......也没有啦，现在和我在一起的是雷亚你吧？"
    play voice "voice/天使雷亚/550015.ogg"
    lst "嗯。"
    me01 "讨厌和我一起吗？"
    pause 0.1 hard
    scene set only lisite_cg end xuejian4
    with dissolve
    play voice "voice/天使雷亚/550016.ogg"
    lst "......"
    play voice "voice/天使雷亚/550017.ogg"
    lst "......没有。"
    me01 "犹豫了啊。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian5
    with dissolve
    play voice "voice/天使雷亚/550018.ogg"
    lst "才、才没有犹豫......"
    me01 "话说雷亚你差不多也该自己洗头了吧？"
    play voice "voice/天使雷亚/550019.ogg"
    lst "......不要。"
    me01 "不是做不到，而是不想？"
    play voice "voice/天使雷亚/550020.ogg"
    lst "因为妈妈她也说过，凉君经常帮她洗头。"
    me01 "所以为什么这种事情也要说出来啊......"
    play voice "voice/天使雷亚/550021.ogg"
    lst "虽然不是很理解，但总是被炫耀着。"
    play voice "voice/天使雷亚/550022.ogg"
    lst "所以下次我也要试着对妈妈津津乐道地说起这件事~"
    me01 "这样奇怪的对抗心理是怎么回事啊......"
    pause 0.1 hard
    scene set only lisite_cg end xuejian2
    with dissolve
    play voice "voice/天使雷亚/550023.ogg"
    lst "接下来想让凉君帮我洗干净身子。"
    me01 "你也差不多该一个人洗了吧，连爱衣都没有再这样要求过了呢。"
    play voice "voice/天使雷亚/550024.ogg"
    lst "那我就告诉妈妈说凉君硬要给我洗澡。"
    me01 "会被误会的所以还请别这么做。"
    play voice "voice/天使雷亚/550025.ogg"
    lst "......凉君会感到困扰吗？"
    me01 "那是当然的吧。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian4
    with dissolve
    play voice "voice/天使雷亚/550026.ogg"
    lst "我不是太明白......"
    me01 "等雷亚你长大了以后，一定可以明白这份心情的。"
    play voice "voice/天使雷亚/550027.ogg"
    lst "那怎么样才能变成大人呢？"
    me01 "经过时间的流逝，你也一定会成长的。"
    play voice "voice/天使雷亚/550028.ogg"
    lst "我现在就想成为大人~"
    me01 "不，就算你这么说......"
    pause 0.1 hard
    scene set only lisite_cg end xuejian2
    with dissolve
    play voice "voice/天使雷亚/550029.ogg"
    lst "凉君，让我变成大人吧~"
    me01 "何等危险的发言？！"
    play voice "voice/天使雷亚/550030.ogg"
    lst "但是我已经是成熟的大姐姐了。"
    me01 "噗哈哈。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian5
    with dissolve
    play voice "voice/天使雷亚/550031.ogg"
    lst "......被嘲笑了。"
    me01 "不是的，只是你的话让我想起了一些往事而已。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian2
    with dissolve
    play voice "voice/天使雷亚/550032.ogg"
    lst "想起什么了？"
    me01 "想起一个总是很固执地说想要改变，但却始终是个孩子的妖精。"
    play voice "voice/天使雷亚/550033.ogg"
    lst "那是谁的事情？"
    me01 "这个嘛......"
    pause 0.1 hard
    scene set only lisite_cg end xuejian4
    with dissolve
    play voice "voice/天使雷亚/550034.ogg"
    lst "......被抱住了。"
    me01 "梦里的那首歌，还记得吗？"
    pause 0.1 hard
    scene set only lisite_cg end xuejian2
    with dissolve
    play voice "voice/天使雷亚/550035.ogg"
    lst "嗯，就是凉君给我洗澡的时候总是会哼着的那首。"
    play voice "voice/天使雷亚/550036.ogg"
    lst "凉君哼的时候总是在傻笑。"
    me01 "......才、才没有呢。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian5
    with dissolve
    play voice "voice/天使雷亚/550037.ogg"
    lst "但是，我听到那首歌的时候，总有一种非常怀念的感觉......"
    play voice "voice/天使雷亚/550038.ogg"
    lst "一直......都觉得很不可思议。"
    me01 "能明白其中的含义吗？"
    pause 0.1 hard
    scene set only lisite_cg end xuejian2
    with dissolve
    play voice "voice/天使雷亚/550039.ogg"
    lst "......我不明白，凉君知道吗？"
    me01 "是啊，不过我想总有一天你也会明白的。"
    me01 "等到雷亚成为大人的时候，我们就能一起去找“她”了。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian6
    with dissolve
    play voice "voice/天使雷亚/550040.ogg"
    lst "我已经是大人了哟~"
    me01 "噗哈哈。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian5
    with dissolve
    play voice "voice/天使雷亚/550041.ogg"
    lst "......又被嘲笑了。"
    me01 "那个故事稍微有点长......要听吗？"
    pause 0.1 hard
    scene set only lisite_cg end xuejian3
    with dissolve
    play voice "voice/天使雷亚/550042.ogg"
    lst "嗯，我想要听~"
    play voice "voice/天使雷亚/550043.ogg"
    lst "我想要知道这种感觉的真相。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian4
    with dissolve
    play voice "voice/天使雷亚/550044.ogg"
    lst "跟凉君这样靠着，就会觉得很温暖、令我呼吸困难，有种很奇怪的感觉......"
    me01 "不是脑充血吗？"
    pause 0.1 hard
    scene set only lisite_cg end xuejian5
    with dissolve
    play voice "voice/天使雷亚/550045.ogg"
    lst "......笨笨的。"
    me01 "那么，我开始说了。"
    pause 0.1 hard
    scene set only lisite_cg end xuejian2
    $ flcam.move(0, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    me01 "那个呢，“她”是我跟雷亚的恩人。一个冬雪化身的、洁白的妖精——"
    pause 2.0 hard
    stop music fadeout 5.0

label day231.memory_event01:
    $ flcam.move(0, 0, 0)
    scene white 
    with slowerdissolve
    pause 3.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard
    play music second_113 fadein 3.0 if_changed
    scene set only xfe_cg memory eight
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011890.ogg"
    xfe "凉君......"
    play voice "voice/希菲尔/001011900.ogg"
    xfe "还不回雪见市吗？"
    me01 "希菲尔想回去了吗？"
    play voice "voice/希菲尔/001011910.ogg"
    xfe "发问的课是希菲尔我。"
    me01 "和希菲尔一起的话去哪里都无所谓。"
    play voice "voice/希菲尔/001011920.ogg"
    xfe "希菲尔说的可不是这个哟。"
    play voice "voice/希菲尔/001011930.ogg"
    xfe "这场旅程是两个人共同的决定的，所以希菲尔想知道也是理所当然的。"
    me01 "那......我们回去吧。"
    pause 0.1 hard
    scene set only xfe_cg memory seven
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001011940.ogg"
    xfe "......"
    me01 "一起回到大家身边去吧。"
    me01 "我们一起。"
    pause 0.1 hard
    scene set only xfe_cg memory eight
    with dissolve
    "本以为这样的回答会让希菲尔开心。"
    "可出乎我意料的是，希菲尔此时竟然露出了悲伤的表情。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian5
    with dissolve
    pause 1.0 hard
    "在那之后，我和希菲尔为了平息世界各地的{rb}灵纹{/rb}{rt}rune{/rt}暴走而四处奔波。"
    "名义上是为了帮助星天宫，但实际上我只是为了完成希菲尔的心愿罢了。"
    "作为接受我生命的条件，希菲尔希望能够帮大家恢复正常的生活。"
    "不知经过了多久，到过多少未知的地方。"
    "此时早已是春意盎然的季节。"
    "这将会是第一次在雪见市看到欣欣向荣的樱花吗？"
    "无论如何，只要有希菲尔陪在我身边，一切都变得不那么重要了......"
    stop music fadeout 5.0
    pause 1.0 hard
    $ set_replay_scene("label19_4")
    scene white 
    with slowerdissolve   
    pause 1.0 hard
    me01 "稍微......有些累了。"
    me01 "毕竟是一场漫长的旅程。"
    me01 "希菲尔，稍微休息下可以吗？"
    play music second_134 fadein 3.0 if_changed
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg leave one
    with slowdissolve
    pause 1.0 hard
    "雪见市的钟楼广场上开满了绽放的樱花。"
    "明明从小时候开始，这里一直都是一片雪白的景象。"
    "原来，也不是只有白色的时候啊。"
    "太好了。"
    "最后能和希菲尔一起创新的回忆，真是太好了......"
    play voice "voice/希菲尔/001011950.ogg"
    xfe "凉君......不要紧吗？"
    me01 "嗯。"
    play voice "voice/希菲尔/001011960.ogg"
    xfe "哪里痛吗？"
    me01 "不会。"
    play voice "voice/希菲尔/001011970.ogg"
    xfe "哪里难受吗？"
    me01 "没关系的......"
    play voice "voice/希菲尔/001011980.ogg"
    xfe "可是。"
    me01 "真的......没关系的。"
    "回忆和现实仿佛重叠了。"
    "就像希菲尔在白色雪原的大树下一样。"
    "不过这次角色反过来了。"
    "本以为这就是我所期望的结局，也是希菲尔能够接受的结局。"
    "但是......为什么你会是这样的表情呢？"
    "为什么比起我，你却显得更加地悲伤呢。"
    play voice "voice/希菲尔/001011990.ogg"
    xfe "凉君......没办法站起来了吗？"
    play voice "voice/希菲尔/001012000.ogg"
    xfe "已经......没办法两个人一起走下去了吗？"
    pause 0.1 hard
    scene set only xfe_cg leave two
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012010.ogg"
    xfe "希菲尔我想和凉君一起去见见千冬。"
    play voice "voice/希菲尔/001012020.ogg"
    xfe "也想再去见见其他的朋友们。"
    pause 0.1 hard
    scene set only xfe_cg leave one
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    me01 "一定可以的......"
    me01 "稍微休息一下的话，一定还能一起向前迈进的。"
    me01 "两个人一起......"
    me01 "我们也已经很长时间，没有见到大家了。"
    me01 "说不定翔子她现在正在生我的气呢。"
    pause 0.1 hard
    scene set only xfe_cg leave two
    with dissolve
    play voice "voice/希菲尔/001012030.ogg"
    xfe "......"
    me01 "感觉下一次见面的时候，一定会被大家骂一顿的。"
    play voice "voice/希菲尔/001012040.ogg"
    xfe "......"
    me01 "让大家担心了。"
    me01 "不好好道歉的话可不行啊。"
    pause 0.1 hard
    scene set only xfe_cg leave one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012050.ogg"
    xfe "已经......足够了。"
    play voice "voice/希菲尔/001012060.ogg"
    xfe "不用再说谎......也没关系的。"
    play voice "voice/希菲尔/001012070.ogg"
    xfe "温柔的谎言......已经足够了。"
    play voice "voice/希菲尔/001012080.ogg"
    xfe "凉君你其实，从一开始就没打算再和朋友们再见的。"
    play voice "voice/希菲尔/001012090.ogg"
    xfe "所以到现在为止一直，都没有和大家联系过。"
    play voice "voice/希菲尔/001012100.ogg"
    xfe "也没有提起过要回雪见市的事情。"
    play voice "voice/希菲尔/001012110.ogg"
    xfe "从不告诉她们自己的行踪，凉君你一直都在躲猫猫......"
    pause 1.0 hard
    scene set only xfe_cg leave two
    with dissolve
    play voice "voice/希菲尔/001012120.ogg"
    xfe "因为凉君也明白......这样下去自己终有一天，是要和大家告别的。"
    play voice "voice/希菲尔/001012130.ogg"
    xfe "因为不想要面对悲伤的离别......"
    pause 0.1 hard
    scene set only xfe_cg leave one
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012140.ogg"
    xfe "这一点，和过去的希菲尔是一样的。"
    play voice "voice/希菲尔/001012150.ogg"
    xfe "凉君明明......也对希菲尔说过的。"
    play voice "voice/希菲尔/001012160.ogg"
    xfe "说过这样做是不对的。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    me01 "希菲尔。"
    me01 "对不起。"
    pause 1.0 hard
    $ flcam.move(1100, -1400, 450)
    scene set only xfe_cg leave three
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012170.ogg"
    xfe "凉君......"
    play music second_160 fadein 3.0 if_changed
    play voice "voice/希菲尔/001012180.ogg"
    xfe "能一起走到这里，我很开心了。"
    play voice "voice/希菲尔/001012190.ogg"
    xfe "能陪在你的身边，我真的很开心。"
    play voice "voice/希菲尔/001012200.ogg"
    xfe "明明两人的足迹，在春天降临之时就应该消散的。"
    play voice "voice/希菲尔/001012210.ogg"
    xfe "谢谢你。"
    play voice "voice/希菲尔/001012220.ogg"
    xfe "凉君你......已经很努力了。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/001012230.ogg"
    xfe "但是......已经足够了。"
    play voice "voice/希菲尔/001012240.ogg"
    xfe "晚安......凉君~"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    play voice "voice/希菲尔/001012250.ogg"
    xfe "拜拜......凉君。"
    play voice "voice/希菲尔/001012260.ogg"
    xfe "对不起......凉君。"
    play voice "voice/希菲尔/001012270.ogg"
    xfe "希菲尔我又要再一次犯下错误了。"
    play voice "voice/希菲尔/001012280.ogg"
    xfe "在凉君犯下更加严重的错误之前，就让希菲尔我先来......与你道别——"
    play voice "voice/希菲尔/001012290.ogg"
    xfe "......"
    pause 0.1 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg leave five
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012300.ogg"
    xfe "欸？"
    play voice "voice/希菲尔/001012310.ogg"
    xfe "骗人......为什么？"
    play voice "voice/希菲尔/001012320.ogg"
    xfe "没办法变回一个人。"
    play voice "voice/希菲尔/001012330.ogg"
    xfe "这份羁绊......无论如何也无法切断。"
    pause 0.1 hard
    scene set only xfe_cg leave four
    $ flcam.move(-1100, -1400, 450, duration=3.0, warper='ease_quad')
    with dissolve
    pause 3.0 hard
    me01 "谢谢你，希菲尔......"
    me01 "我终于听到了......你的真心。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/希菲尔/001012340.ogg"
    xfe "......真心？"
    me01 "啊，正因为你也相信我不会离你而去，所以才会让我们的羁绊如此地牢固。"
    me01 "无法变回一个人就是最好的证明。"
    play voice "voice/希菲尔/001012350.ogg"
    xfe "才没有，那种事......"
    pause 0.1 hard
    scene set only xfe_cg leave one
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012360.ogg"
    xfe "希菲尔我想要保护凉君。"
    play voice "voice/希菲尔/001012370.ogg"
    xfe "就算赌上性命也一定要救凉君。"
    pause 0.1 hard
    scene set only xfe_cg leave two
    with dissolve
    play voice "voice/希菲尔/001012380.ogg"
    xfe "因为凉君也是这样对我的。"
    play voice "voice/希菲尔/001012390.ogg"
    xfe "所以绝对......不得不分开的。希菲尔我是这么想的。"
    play voice "voice/希菲尔/001012400.ogg"
    xfe "比起让希菲尔继续消耗凉君的生命。"
    pause 0.1 hard
    scene set only xfe_cg leave one
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012410.ogg"
    xfe "用希菲尔的消失来换取凉君的存活一定会是更好的结局！"
    pause 0.1 hard
    $ flcam.move(0, 0, 0, duration=3.0, warper='ease_quad')
    pause 3.0 hard
    me01 "希菲尔......难道你忘记了吗？"
    me01 "现在的我们早已被{rb}共感{/rb}{rt}empathy{/rt}的魔力所连接着。"
    me01 "我们早已是一心同体的了。"
    me01 "我所期望的东西，也是你所期望的。"
    me01 "我们早已是这样的关系了。"
    me01 "妖精与人类和平共处的愿望，早已实现了。"
    pause 0.1 hard
    scene set only xfe_cg leave snow four
    with dissolve
    "白色的结晶从天而降。"
    "不会堆积的，温柔的雪再一次飘落了下来。"
    "梦幻的白色结晶，与粉色的樱花结伴飘落。"
    play voice "voice/希菲尔/001012420.ogg"
    xfe "......这是？"
    me01 "这一定就是我们所期望的世界。"
    me01 "是千冬曾经提到过的光景。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg memory11
    show sepiagrain onlayer texture
    with dissolve
    play voice "voice/诗乃/701000760.ogg"
    "诗乃" "如若可以的话，希望你也能实现那孩子的愿望。"
    pause 2.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg leave snow four
    with dissolve
    pause 1.0 hard
    "原本就不需要牺牲任何的一个人。"
    "即使诞生于不同的两颗星球，仍然可以共存。"
    "白色的永恒，将会与蓝色永恒一同闪耀着生命的光芒。"
    "冬雪和樱花。"
    "两个本来不可能同时出现的生命。"
    "此刻早已铺满了片澄澈的蓝天——"
    pause 2.0 hard
    scene set only sky day xuejian5
    show snow_level1 onlayer fg
    show gui_mm_fall_back onlayer fg
    show gui_mm_fall_front onlayer fg
    with dissolve
    pause 1.0 hard
    "希菲尔夙愿中的世界。"
    "蓝色星球与白色星球的交汇。"
    "人类和妖精，能够共同生存的——温柔的星球。"
    "此刻就在我们的眼前。"
    pause 0.1 hard
    hide snow_level1
    hide gui_mm_fall_front
    hide gui_mm_fall_back
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg leave snow one
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012430.ogg"
    xfe "希菲尔我也......不想和凉君分开。"
    pause 0.1 hard
    scene set only xfe_cg leave snow two
    with dissolve
    play voice "voice/希菲尔/001012440.ogg"
    xfe "但是，凉君你已经......"
    me01 "不要紧的。"
    pause 0.1 hard
    scene set only xfe_cg leave snow five
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012450.ogg"
    xfe "才没有不要紧！"
    play voice "voice/希菲尔/001012460.ogg"
    xfe "再这样下去的话，凉君真的会死掉的。"
    play voice "voice/希菲尔/001012470.ogg"
    xfe "因为希菲尔的错，让凉君消失......"
    play voice "voice/希菲尔/001012480.ogg"
    xfe "可是，明明是这样想的可是......"
    play voice "voice/希菲尔/001012490.ogg"
    xfe "不想要分开。"
    play voice "voice/希菲尔/001012500.ogg"
    xfe "想待在你的身边。"
    play voice "voice/希菲尔/001012510.ogg"
    xfe "永远永远没有改变。"
    play voice "voice/希菲尔/001012520.ogg"
    xfe "唯独这份心意一直没有改变。"
    pause 1.0 hard
    $ flcam.move(2200, -2800, 800, duration=3.0, warper='ease_quad')
    pause 2.0 hard
    play voice "voice/希菲尔/001012530.ogg"
    xfe "不管什么时候......都没有改变过啊！"
    pause 1.0 hard
    scene white 
    with slowerdissolve

label day231.memory_event02:
    pause 2.0 hard
    play voice "voice/千冬/771005140.ogg"
    stranger "找你们很久了哟。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only jsqd_cg end three
    with slowdissolve
    pause 1.0 hard
    play voice "voice/千冬/771005150.ogg"
    jsqd "不用说一些自大的话。"
    play voice "voice/千冬/771005160.ogg"
    jsqd "你们两个不用独自承担一切的。"
    play voice "voice/千冬/771005170.ogg"
    jsqd "因为我是你们两个的姐姐嘛。"
    play voice "voice/千冬/771005180.ogg"
    jsqd "也希望你们能稍微依靠一下身为姐姐的我。"
    "千冬好好地站着。"
    "已经不再需要依靠轮椅了。"
    "能靠自己的双脚行动了。"
    pause 0.1 hard
    scene set only jsqd_cg end four
    with dissolve
    play voice "voice/千冬/771005190.ogg"
    jsqd "凉君你帮助了小希菲尔。"
    play voice "voice/千冬/771005200.ogg"
    jsqd "小希菲尔也帮助了这颗星球上的其他人们。"
    pause 0.1 hard
    scene set only jsqd_cg end three
    with dissolve
    play voice "voice/千冬/771005210.ogg"
    jsqd "所以这一次......轮到我们大家报答你们二位了。"
    "千冬张开双手，手心里捧着某个发光的结晶。"
    "是冰吗？"
    "洁白晶莹的，散发着不可思议光芒的碎片——Astral Air。"
    play voice "voice/千冬/771005220.ogg"
    jsqd "这是母亲和大和先生努力的成果哟。"
    play voice "voice/千冬/771005230.ogg"
    jsqd "我也作为新人研究员稍微帮忙了。"
    play voice "voice/千冬/771005240.ogg"
    jsqd "为了妖精和人类共存的研究，此刻开花结果了。"
    pause 0.1 hard
    scene set only jsqd_cg end four
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千冬/771005250.ogg"
    jsqd "这样一来，妖精与人类终于能够和睦共处了。"
    play voice "voice/千冬/771005260.ogg"
    jsqd "你们两个也不需要再分开了，今后也能一直在一起了。"
    play voice "voice/千冬/771005270.ogg"
    jsqd "能够相互偎依着......向前迈进了。"
    pause 0.1 hard
    scene set only jsqd_cg end three
    with dissolve
    play voice "voice/千冬/771005280.ogg"
    jsqd "但是，请不要一个人踏上路程。"
    play voice "voice/千冬/771005290.ogg"
    jsqd "也不要两个人先行离去。"
    play voice "voice/千冬/771005300.ogg"
    jsqd "时不时地回头看看身后，停下来等一等。"
    pause 0.1 hard
    scene set only jsqd_cg end five
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千冬/771005310.ogg"
    jsqd "我们大家一定也会追上你们两个的——"
    "太好了。"
    "真的，太好了。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    nvl clear
    pcenter "你说是吧，希菲尔。"
    pause 0.1 hard
    nvl clear
    with dissolve
    pause 2.0 hard
    $ end_replay()
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg leave own
    with cent2side
    pause 1.0 hard
    "我睁开双眼。"
    "然而希菲尔的身影却不在身边。"  
    "千冬也是。"
    "就连漫天的飘雪和樱花也没有出现在视线中。"
    pause 0.1 hard
    $ flcam.move(-1100, -1400, 450, duration=3.0, warper='ease_quad')
    pause 2.0 hard
    me01 "是吗......"
    "原来希菲尔早就离开了。"
    "千冬也根本没有来过这里。"
    "刚刚的一切都只是我的梦而已。"
    me01 "希菲尔......"
    me01 "你在哪里啊希菲尔......"
    "就算想起身寻找，身体却僵硬得无法动弹。"
    "只有五感仍在运转着。"
    "已经感觉不到{rb}共感{/rb}{rt}empathy{/rt}了。"
    "羁绊被切断了。"
    "希菲尔又一次，选择了孤身一人......"
    pause 2.0 hard
    scene white 
    with slowerdissolve
    pause 1.0 hard
    "不停地呼唤那个名字。"
    "但不争气的喉咙此刻却只能发出浑浊且低沉的声音。"
    "体力已经虚弱至此了吗。"
    "希菲尔。" 
    "......希菲尔，希菲尔！"
    stop music fadeout 5.0
    pause 2.0 hard

label day231.memory_event03:
    $ set_replay_scene("label20_1")
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian5
    show snow_level1 onlayer fg
    with slowdissolve
    pause 1.0 hard
    me01 "这是......"
    "白色的结晶再次出现。"
    "这不是梦。"
    "也不是幻觉。"
    "能够真实地感受到。"
    "原来如此，你一直......在等着这句话吗。"
    pause 2.0 hard
    hide snow_level1
    scene white 
    with slowerdissolve
    pause 1.0 hard
    me01 "找到你了，希菲尔——"
    play music second_155 fadein 3.0 if_changed
    pause 8.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg final1
    with slowerdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012540.ogg"
    xfe "嗯，被找到了~"
    play voice "voice/希菲尔/001012550.ogg"
    xfe "早上好，凉君。"
    play voice "voice/希菲尔/001012560.ogg"
    xfe "能这样见面，多亏了和凉君一起旅行的关系。"
    pause 0.1 hard
    scene set only xfe_cg final2
    with dissolve
    play voice "voice/希菲尔/001012580.ogg"
    xfe "从大家那里收集回来{rb}灵纹{/rb}{rt}rune{/rt}帮助了希菲尔我哟~"
    play voice "voice/希菲尔/001012590.ogg"
    xfe "所以就算不再借助凉君的生命，我也能独自生存下去了。"
    pause 0.1 hard
    scene set only xfe_cg final3
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012610.ogg"
    xfe "凉君......希菲尔我有个请求。"
    play voice "voice/希菲尔/001012620.ogg"
    xfe "在最后，希望凉君也能把{rb}灵纹{/rb}{rt}rune{/rt}交给希菲尔。"
    me01 "那样的话，是不是就真的再也无法见到希菲尔了？"
    pause 0.1 hard
    scene set only xfe_cg final4
    with dissolve
    play voice "voice/希菲尔/001012630.ogg"
    xfe "......"
    pause 0.1 hard
    scene set only xfe_cg final3
    with dissolve
    play voice "voice/希菲尔/001012640.ogg"
    xfe "......就是这样的。"
    pause 0.1 hard
    scene set only xfe_cg final1
    with dissolve
    play voice "voice/希菲尔/001012650.ogg"
    xfe "希菲尔我从一开始，就是为了让凉君活下去才决定一起旅行的。"
    play voice "voice/希菲尔/001012660.ogg"
    xfe "把大家的{rb}灵纹{/rb}{rt}rune{/rt}叭咕叭咕地吃掉也都是为了这个。"
    pause 0.1 hard
    scene set only xfe_cg final2
    with dissolve
    play voice "voice/希菲尔/001012670.ogg"
    xfe "接下来只要再把凉君的{rb}灵纹{/rb}{rt}rune{/rt}也吞下去的话，希菲尔我就吃饱了哟~"
    pause 0.1 hard
    scene set only xfe_cg final3
    with dissolve
    play voice "voice/希菲尔/001012680.ogg"
    xfe "身为妖精的希菲尔，已经不能再牺牲作为人类的凉君。"
    play voice "voice/希菲尔/001012690.ogg"
    xfe "所以，凉君......"
    me01 "希菲尔。"
    me01 "就在刚才，我做了一场梦。"
    me01 "妖精和人类，是能够生活在一起的。"
    me01 "我们，是能够和睦共处的。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    pause 2.0 hard
    $ flcam.move(1100, -1400, 450)
    scene set only jsqd_cg end three
    show sepiagrain onlayer fg
    with dissolve
    play voice "voice/千冬/771005290.ogg"
    jsqd "请不要两个人先行离去。"
    play voice "voice/千冬/771005300.ogg"
    jsqd "时不时地回头看看身后，停下来等一等。"
    pause 0.1 hard
    scene set only jsqd_cg end five
    $ flcam.move(2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千冬/771005310.ogg"
    jsqd "我们大家一定也会追上你们两个的——"
    pause 1.0 hard
    hide sepiagrain
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg final4
    with dissolve
    pause 1.0
    me01 "未来的大家，一定会为我们创造出那样温柔的世界。"
    play voice "voice/希菲尔/001012700.ogg"
    xfe "......"
    me01 "总有一天，你的愿望一定能够实现的！"
    play voice "voice/希菲尔/001012710.ogg"
    xfe "......真的吗？"
    me01 "是啊，难道你连我都不相信了吗？"
    me01 "希菲尔你，难道连我们大家都无法信任吗。"
    play voice "voice/希菲尔/001012720.ogg"
    xfe "凉君......"
    pause 0.1 hard
    scene set only xfe_cg final6
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012730.ogg"
    xfe "好狡猾啊凉君。"
    play voice "voice/希菲尔/001012740.ogg"
    xfe "希菲尔现在可是非常相信大家的~"
    me01 "所以希菲尔......让我们继续踏上旅程吧。"
    me01 "时不时地回头看看身后，停下来等一等。"
    me01 "为了不抛下身边的任何一个人。"
    me01 "在这颗星球上存在过的足迹，就由这场雪将它延续下去吧。"
    me01 "希菲尔。"
    me01 "接下来要去哪里呢——"
    pause 0.1 hard
    scene set only xfe_cg final5
    with dissolve
    play voice "voice/希菲尔/001012750.ogg"
    xfe "去哪里都可以哟~"
    play voice "voice/希菲尔/001012760.ogg"
    xfe "只要和凉君一起的话，去哪里都行。"
    play voice "voice/希菲尔/001012770.ogg"
    xfe "我们两个已经是，即使春天来临也能去任何地方了。"
    me01 "那么首先。"
    me01 "说声“欢迎回家”吧。"
    pause 0.1 hard
    scene set only xfe_cg final6
    $ flcam.move(-2200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001012780.ogg"
    xfe "......嗯~"
    pause 4.0 hard
    scene white 
    with slowerdissolve
    pause 3.0 hard
    $ end_replay()
    $ suppress_overlay = True
    $ flcam.move(0, 0, 0)
    play voice "voice/希菲尔/900000000.ogg"
    scene set only xfe_cg endback
    with slowerdissolve
    show final onlayer m2 at logo_slide03
    pause 10.0 hard
    stop music fadeout 5.0
    scene black 
    with slowerdissolve
    pause 6.0 hard

    $ persistent.stories.add("冬之章")
    $ persistent.now_story = "秋之章"

    return
