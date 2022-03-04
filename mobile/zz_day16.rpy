label day16:
    bookmark
    $ save_name = _("Day 16")
    pause 4.0 hard
    scene set only backend_yinghua spring
    with dissolve
    show backend_bg01 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date15 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ set_replay_scene("label3_2")
    $ flcam.move(0, 0, 0)
    $ suppress_overlay = False
    scene set only sky day yinghua
    with dissolve
    play ambience1 niaoming
    pause 2.0 hard
    "观景台的风出人意料的强劲。"
    "是春天的第一道强风吧。"
    "因为不像冬天那么冷，所以不是很在意。"
    "对我这一直坐着而变得僵硬的身体来说反而是好事。"
    pause 2.0 hard
    scene set only starview day starview
    with dissolve
    pause 2.0 hard
    "每天我都会去寻找雷亚凭依的陨石。"
    "但至今为止仍是一无所获，或许陨石根本不在樱华镇也说不定。"
    "樱华校的毕业典礼结束之后，我来到了这里。"
    "周围空无一人，只有草木摇曳的声音。"
    me01 "......回去吧。"
    play sound move_2
    pause 2.0 hard
    scene set only starview day outside
    with dissolve
    pause 2.0 hard
    "毕业后的我打算去城市里就读大学。"
    "同时也为了去别处继续寻找雷亚的踪迹。"
    me01 "这下真的要和观景台说再见了吗......"
    "一年过去了，禁止进入的命令依旧没有解除。从樱华校毕业的我，如今已经没有理由再踏足这个地方了。"
    "校门口聚集着众多毕业的学生们，此刻他们应该也在为自己的成长而欢呼吧。"
    "虽然擅自跑了出来，但也只是为了最后再看一眼这个曾经发生过许多美好故事的地方罢了。"
    pause 1.0 hard
    stop ambience1 fadeout 3.0
    scene set only sky day yinghua
    with dissolve
    pause 2.0 hard
    "就像谁曾经说过的那样，想要把握住美好就应该勇往直前。"
    "可那一天何时才会到来？"
    "我什么时候才能抓住呢？"
    "抓住那无可替代之人的手不放开——"
    play voice "voice/翔子/0618160.ogg"
    stranger "......抱歉，在等人吗？"
    pause 2.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 1.25 alpha 1
    pause 5.0 hard
    play music first_24 fadein 2.0 if_changed
    scene set only xz_cg yume end one
    with slowerdissolve
    pause 3.0 hard
    "少女站在那里。"
    play voice "voice/翔子/0618170.ogg"
    yume "凉君......"
    "少女呼唤了我的名字。"
    "这是我再熟悉不过的人了。"
    "这是我一度就要忘记的，重要之人。"
    "这是，给予我梦想，给予我希望之人。"
    play voice "voice/翔子/0618180.ogg"
    yume "这里，没有樱花呢。"
    play voice "voice/翔子/0618190.ogg"
    yume "没有春之花呢。"
    play voice "voice/翔子/0618200.ogg"
    yume "就如同是结束了，却又没有结束。就像是改变了，却又没有改变一样。"
    pause 0.1 hard
    scene set only xz_cg yume end two
    with dissolve
    $ flcam.move(-2800, -1500, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0618210.ogg"
    yume "在万物的变迁之中，永恒不变的事物确确实实地存在着。"
    play voice "voice/翔子/0618220.ogg"
    yume "直到永远，都会在那里......"
    "我想要喊出声，但是自己的喉咙却不听使唤。"
    "啊，这温柔的魔法，究竟是谁。"
    "是谁让我再一次见到了你。"
    "是谁替我再一次打破了这次元的枷锁见到了你。"
    "“即使消失了也要陪在身边”，是谁又一次实现了我的愿望吗？"
    "也许是注意到了我的诧异，女孩冲我笑了。"
    pause 0.1 hard
    scene set only xz_cg yume end one
    with dissolve
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0618230.ogg"
    yume "我的名字呢，叫作青木·梦。"
    "为什么呢。"
    "一听到这个名字就感到撕心裂肺的疼痛。"
    "空虚的内心在绞痛着。"
    "这种感觉究竟是什么，我不清楚。"
    "虽然不清楚，但那是十分强烈的思念。"
    "就像过去的{rb}我{/rb}{rt}boku{/rt}所承受离别的痛苦那般强烈。"
    play voice "voice/翔子/0618240.ogg"
    yume "谢谢你，凉君。"
    play voice "voice/翔子/0618250.ogg"
    yume "谢谢你，死神。"
    play voice "voice/翔子/0618260.ogg"
    yume "能和你再会，我很高兴。"
    play voice "voice/翔子/0618270.ogg"
    yume "如果还能再见面的话，我会更高兴的。"
    play voice "voice/翔子/0618280.ogg"
    yume "想要和我玩的话，随时都可以跟我说。"
    pause 0.1 hard
    scene set only xz_cg yume end two
    with dissolve
    $ flcam.move(-2800, -1500, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0618290.ogg"
    yume "因为，我喜欢和你在一起。"
    play voice "voice/翔子/0618300.ogg"
    yume "这一定是永远也不会改变的东西。"
    pause 0.1 hard
    scene set only xz_cg yume end one
    with dissolve
    $ flcam.move(-4500, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0618310.ogg"
    yume "因为，我喜欢你——"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only starview day outside
    with slowdissolve
    pause 2.0 hard
    "少女的身影消失了。"
    "如同雷亚的身影消失在夜色中一般。"
    "我没能追上去。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua
    with dissolve
    pause 2.0 hard
    "也许是因为我有了预感。"
    "我们，还会见面的。"
    "能够再会的。"
    "那一定会是件很幸福的事。"
    "但是相对的，就无法与另一个她相见了。"
    "无法与帮助过我的她再见了。"
    "这又是不幸的事。"
    "这是代价。"
    "要得到就势必会失去。"
    "简单而又残酷的等价交换。"
    "这铁律就摆在我的面前。"
    "但是，因为有着约定的光。"
    "只要朝着光的方向不断前进的话。"
    "在那里。"
    "回忆也一定也在延续着——"
    pause 5.0 hard
    stop music fadeout 5.0
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 2.0 hard
    $ end_replay()
    pause 3.0 hard
    $ suppress_overlay = True

    $ persistent.stories.add("夏之章")
    if "冬之章" not in persistent.stories:
        $ persistent.now_story = "冬之章"

    return
