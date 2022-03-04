label day15:
    bookmark
    $ save_name = _("Day 15")
    pause 4.0 hard
    scene set only backend_yinghua winter
    with dissolve
    show backend_bg04 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date14 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    scene set only school evening road yinghua
    with dissolve
    pause 2.0 hard
    scene set only school evening room yinghua
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b3 b3 b3_s2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0141410.ogg"
    rxl "小凉。"
    play music first_23 fadein 3.0 if_changed
    show rxl_dzf_b3 b3 b3_s1
    play voice "voice/日向怜/0141420.ogg"
    rxl "那个，今天......"
    me01 "抱歉，今天的社团活动我不参加了。"
    hide rxl_dzf_b3
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0141430.ogg"
    rxl "嗯，我知道了。"
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_n1 onlayer m2 at walkout_r(0.5)
    pause 0.5 hard
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_s3 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0534010.ogg"
    lingyin "神野同学，你现在要去医院吗？"
    me01 "......就当是这样的吧。"
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1606420.ogg"
    yczs "你那含糊不清的回答算什么啊！"
    me01 "那我先走了。"
    pause 1.0 hard
    play sound open_door
    $ flcam.move(0, 0, 0)
    scene set only school evening corridor yinghua
    with dissolve
    pause 2.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    scene set only school evening room yinghua
    with cent2side
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b3 b3 b3_s3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0141440.ogg"
    rxl "我们就没有什么，能帮得上忙的吗......"
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_s3 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0534020.ogg"
    lingyin "梦她现在是由父亲亲自负责照看的病人。所以我觉得我们所能做的，就是陪着神野同学。"
    show lingyin_dzf_b2 b2 b2_n2
    play voice "voice/青木铃音/0534030.ogg"
    lingyin "作为朋友，现在这个时候我们更应该陪在神野同学的身边。"
    hide lingyin_dzf_b2
    hide rxl_dzf_b3
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/1606430.ogg"
    yczs "......真是的。"
    pause 1.0 hard
    scene black
    with side2cent
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school evening gate yinghua
    with dissolve
    pause 2.0 hard
    play voice "voice/一诚总司/1606440.ogg"
    yczs "等等啊，神野。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_n2 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1606450.ogg"
    yczs "我也正好要回去，一起走吧。"
    "没有拒绝的理由，我就这样默许了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street evening yinghua
    with right2left
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.5
    play voice "voice/一诚总司/1606460.ogg"
    yczs "你现在不是要去探病的吗？"
    me01 "......也许吧。"
    stop music fadeout 5.0
    show yczs_dzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1606470.ogg"
    yczs "没必要瞒着我吧。我也不是因为想凑热闹才问的。"
    me01 "抱歉。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1606480.ogg"
    yczs "呐，神野。"
    play music first_31 fadein 3.0 if_changed
    show yczs_dzf_b1 b1 b1_a1
    play voice "voice/一诚总司/1606490.ogg"
    yczs "又不是已经确定死了。"
    "我停下了脚步。"
    me01 "......一诚你，也已经知道了吗？"
    show yczs_dzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1606500.ogg"
    yczs "不，我只是试探了一下而已。毕竟这也不是什么可以四处张扬的话题。但我想铃音她们也是知道的。"
    me01 "明明是一个到处添油加醋的人。"
    me01 "真是一点都不像你说的话啊。"
    play voice "voice/一诚总司/1606510.ogg"
    yczs "我自己也不是很清楚。不过平时总是对着取景框看的话，不仅是对人的行为，就连他们脸上微妙的感情变化也会变得敏锐的。"
    me01 "刚刚对你那么冷淡真是抱歉......"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/1606520.ogg"
    yczs "这个谢罪还是来得太晚了，回想起来都过了好几秒了啊！"
    me01 "社团活动那边，怎么样了？"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1606530.ogg"
    yczs "不要扯开话题。"
    me01 "真是敏锐啊......"
    show yczs_dzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1606540.ogg"
    yczs "神野。还没有确定会死吧。"
    me01 "......已经确定了。因为梦是这么说的。"
    show yczs_dzf_b1 b1 b1_a1
    play voice "voice/一诚总司/1606550.ogg"
    yczs "笨蛋。我说的才不是这个。"
    play voice "voice/一诚总司/1606560.ogg"
    yczs "你自己还没有相信她会就这样死掉吧。"
    me01 "......"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1606570.ogg"
    yczs "我的妹妹，以前也是这样的。"
    show yczs_dzf_b1 b1 b1_s2
    play voice "voice/一诚总司/1606580.ogg"
    yczs "某一天她突然不见了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening yinghua3
    with dissolve
    pause 2.0 hard
    show yczs_dzf_b1 b1 b1_s1 onlayer screens:
        subpixel True
        xpos 0.87
        xzoom -1
        ypos side_actor_ypos.get('yczs', 0.5)
        yanchor 0.0
        zoom 1.8
    play voice "voice/一诚总司/1606590.ogg"
    yczs "在我从学校回来的路上，没有任何征兆地......"
    play voice "voice/一诚总司/1606600.ogg"
    yczs "她就从我眼前消失了。"
    play voice "voice/一诚总司/1606610.ogg"
    yczs "在那之后也不知道过去了多久。"
    play voice "voice/一诚总司/1606620.ogg"
    yczs "是在哪里遭遇什么事故了吗？还是说被卷入什么事件了？"
    play voice "voice/一诚总司/1606630.ogg"
    yczs "至今为止，我什么都不知道。"
    play voice "voice/一诚总司/1606640.ogg"
    yczs "正因为是什么都不知道，也正因为太没有道理了。"
    play voice "voice/一诚总司/1606650.ogg"
    yczs "所以我认定这一定是外星人搞的鬼，至少当时的我是这么坚信着。"
    play voice "voice/一诚总司/1606670.ogg"
    yczs "即便是现在她回来了，我依然这么相信着。"
    play voice "voice/一诚总司/1606680.ogg"
    yczs "当时的我甚至觉得自己的妹妹或许永远也回不来了。"
    hide yczs_dzf_b1
    pause 1.0 hard
    $ flcam.move(0, -300, 900)
    scene set only street evening yinghua
    show yczs_dzf_b1 b1 b1_n2 onlayer m2:
        xpos 0.5
    with dissolve
    pause 0.5 hard
    play voice "voice/一诚总司/1606690.ogg"
    yczs "但是啊，直到最后我始终相信她是活着。"
    play voice "voice/一诚总司/1606700.ogg"
    yczs "她还活着，我一直都这样相信着。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1606710.ogg"
    yczs "所以啊，神野。"
    show yczs_dzf_b1 b1 b1_a1
    play voice "voice/一诚总司/1606720.ogg"
    yczs "你也相信吧。"
    play voice "voice/一诚总司/1606730.ogg"
    yczs "还活着，绝不会死。"
    play voice "voice/一诚总司/1606740.ogg"
    yczs "不会消失的。"
    play voice "voice/一诚总司/1606750.ogg"
    yczs "请你也这样相信着吧。"
    show yczs_dzf_b1 b1 b1_s1
    play voice "voice/一诚总司/1606760.ogg"
    yczs "虽然我不会说“相信的力量会产生奇迹”这么陈腐的台词。"
    show yczs_dzf_b1 b1 b1_a1
    play voice "voice/一诚总司/1606770.ogg"
    yczs "但如果连你自己都不相信的话，一切就一定不会发生了。"
    play voice "voice/一诚总司/1606780.ogg"
    yczs "连站在起跑线上的资格都没有了。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 3.0 hard

label day15.hospital_event01:
    $ set_replay_scene("label3_1")
    $ flcam.move(0, 0, 0)
    scene white
    with slowdissolve
    pause 2.0 hard
    play voice "voice/翔子/0610470.ogg"
    yume "......"
    play voice "voice/翔子/0610480.ogg"
    yume "啊......"
    play voice "voice/翔子/0610490.ogg"
    yume "我......"
    play voice "voice/翔子/0610500.ogg"
    yume "是吗，我睡着了啊......"
    play voice "voice/翔子/0610510.ogg"
    yume "我还、活着啊......"
    pause 1.0 hard
    scene set only xz_cg bed one
    with cent2side
    pause 2.0 hard
    play music first_39 fadein 3.0 if_changed
    play voice "voice/翔子/0610520.ogg"
    yume "好耀眼......"
    play voice "voice/翔子/0610530.ogg"
    yume "夕阳的，红色......"
    play voice "voice/翔子/0610540.ogg"
    yume "好漂亮......"
    play voice "voice/翔子/0610550.ogg"
    yume "好想看看外面啊......"
    play voice "voice/翔子/0610560.ogg"
    yume "沉入海平面的夕阳......"
    play voice "voice/翔子/0610570.ogg"
    yume "分界线的光......"
    play voice "voice/翔子/0610580.ogg"
    yume "虽然想看......"
    play voice "voice/翔子/0610590.ogg"
    yume "但却好想睡......"
    play voice "voice/翔子/0610600.ogg"
    yume "忍不住地想睡......"
    play voice "voice/翔子/0610610.ogg"
    yume "如果再次闭上眼睛的话......"
    play voice "voice/翔子/0610620.ogg"
    yume "我肯定......"
    pause 0.1 hard
    scene set only xz_cg bed five
    with dissolve
    play voice "voice/神野大和/1900010.ogg"
    stranger "是啊......"
    pause 0.1 hard
    scene set only xz_cg bed six
    with dissolve
    play voice "voice/翔子/0610630.ogg"
    yume "......"
    play voice "voice/翔子/0610640.ogg"
    yume "妖精、先生......"
    play voice "voice/神野大和/1900020.ogg"
    stranger "因为到了家教的时间了，所以过来看看你。"
    play voice "voice/神野大和/1900030.ogg"
    stranger "但是，你睡着了。"
    play voice "voice/神野大和/1900040.ogg"
    stranger "我本来打算回去的，但是看见你醒了也是吃了一惊。"
    play voice "voice/神野大和/1900050.ogg"
    stranger "这次醒来，几乎就是奇迹......"
    play voice "voice/翔子/0610660.ogg"
    yume "嗯。"
    play voice "voice/翔子/0610670.ogg"
    yume "我知道的。"
    play voice "voice/翔子/0610680.ogg"
    yume "毕竟是自己的身体，所以我知道的......"
    play voice "voice/翔子/0610690.ogg"
    yume "如果再睡着的话，一定就不会再醒来了......"
    play voice "voice/神野大和/1900060.ogg"
    stranger "......"
    play voice "voice/神野大和/1900070.ogg"
    stranger "外面，下雪了。"
    play voice "voice/翔子/0610700.ogg"
    yume "是吗......"
    play voice "voice/神野大和/1900080.ogg"
    stranger "今年的第二场雪。"
    play voice "voice/神野大和/1900090.ogg"
    stranger "夕阳那鲜明的赤色，与棉花一般的白色开始交融了。"
    play voice "voice/神野大和/1900100.ogg"
    stranger "到了晚上的话，雪云就会覆盖天空。"
    play voice "voice/神野大和/1900110.ogg"
    stranger "到那时也许就看不到星星了。"
    play voice "voice/翔子/0610710.ogg"
    yume "是吗......"
    play voice "voice/神野大和/1900120.ogg"
    stranger "如果觉得痛苦的话，不用说话也可以。"
    play voice "voice/翔子/0610720.ogg"
    yume "......"
    play voice "voice/神野大和/1900140.ogg"
    stranger "到目前为止能够察觉到我存在的人很少。如果不是从三次元以上的维度的话，想要察觉到我这样的存在是很困难的。"
    play voice "voice/神野大和/1900150.ogg"
    stranger "所以，被三次元所束缚的人类，想要观测我的存在是需要条件的。"
    play voice "voice/神野大和/1900160.ogg"
    stranger "就像是进入梦境一样。"
    play voice "voice/神野大和/1900170.ogg"
    stranger "简单来说，必须要能够打破屏障，进入直视幻觉的状态。"
    play voice "voice/神野大和/1900180.ogg"
    stranger "比如药物、压力、酒精、脑功能障碍、重度失血等。"
    play voice "voice/神野大和/1900190.ogg"
    stranger "或者像你这样的，因为{encyclopedia=lnjx}{rb}疾病{/rb}{rt}灵能具现{/rt}{/encyclopedia}的缘故。"
    play voice "voice/翔子/0610730.ogg"
    yume "......"
    play voice "voice/神野大和/1900200.ogg"
    stranger "哪一种都是由多巴胺和内咖肽分泌过剩导致的。"
    play voice "voice/神野大和/1900210.ogg"
    stranger "那样的话，感官的限制就会被解除，变得对周围的情报无法制御地敏感。"
    play voice "voice/神野大和/1900220.ogg"
    stranger "因此通常情况下察觉不到的、三次元以上的信息也可以接收到了。"
    play voice "voice/神野大和/1900230.ogg"
    stranger "就像音调混乱了的钢琴，不再被乐谱所束缚地演奏一般。"
    play voice "voice/神野大和/1900240.ogg"
    stranger "所以，在樱华镇医院{encyclopedia=bone}降生{/encyclopedia}的你，才能看到我的样子并且与我对话。"
    play voice "voice/翔子/0610740.ogg"
    yume "......"
    play voice "voice/神野大和/1900260.ogg"
    stranger "你......不后悔吗？"
    play voice "voice/翔子/0610750.ogg"
    yume "......"
    play voice "voice/翔子/0610760.ogg"
    yume "嗯。"
    play voice "voice/翔子/0610770.ogg"
    yume "后悔的事情，一件都没有......"
    play voice "voice/神野大和/1900270.ogg"
    stranger "......是吗。"
    play voice "voice/翔子/0610780.ogg"
    yume "嗯。"
    play voice "voice/神野大和/1900280.ogg"
    stranger "这是我最后的课了，你要听吗？"
    play voice "voice/翔子/0610790.ogg"
    yume "嗯。"
    play voice "voice/神野大和/1900290.ogg"
    stranger "“忘记”这件事本身，到底是怎么回事呢？"
    play voice "voice/神野大和/1900300.ogg"
    stranger "让对方忘记自己，又是怎么一种体验呢？"
    play voice "voice/神野大和/1900310.ogg"
    stranger "那一定是，残酷的温柔。"
    play voice "voice/神野大和/1900320.ogg"
    stranger "残酷的温柔，简单来说就是强加于人的温柔。"
    play voice "voice/神野大和/1900330.ogg"
    stranger "因为也算是温柔的代名词，所以谁也没有办法去责怪，但也因此其性质更加恶劣。"
    play voice "voice/神野大和/1900340.ogg"
    stranger "所以啊......"
    play voice "voice/神野大和/1900350.ogg"
    stranger "忘却这件事，本身是没有意义的。"
    play voice "voice/神野大和/1900360.ogg"
    stranger "存在是无法破坏的。"
    play voice "voice/神野大和/1900370.ogg"
    stranger "自己活着的证据，存在的证据，是谁也无法否定的。"
    play voice "voice/神野大和/1900380.ogg"
    stranger "就连神明也做不到。"
    play voice "voice/神野大和/1900390.ogg"
    stranger "存在的力量就是这样无法被夺去的。"
    play voice "voice/神野大和/1900400.ogg"
    stranger "那是超越了过去、现在、以及未来的时空概念，绝对的真理。"
    play voice "voice/神野大和/1900410.ogg"
    stranger "任何次元的情报都可以囊括其中。"
    play voice "voice/神野大和/1900420.ogg"
    stranger "那是比不变的星空更加庄严、永恒的东西。"
    play voice "voice/翔子/0610800.ogg"
    yume "......"
    play voice "voice/神野大和/1900430.ogg"
    stranger "所以，你是不会被遗忘的。"
    play voice "voice/神野大和/1900440.ogg"
    stranger "我们，都不会忘记你的。"
    play voice "voice/翔子/0610810.ogg"
    yume "妖精......先生。"
    play voice "voice/翔子/0610820.ogg"
    yume "你一直像现在这样，教我东西......"
    play voice "voice/翔子/0610830.ogg"
    yume "至今为止，教会我这么多，是为什么......"
    play voice "voice/神野大和/1900450.ogg"
    stranger "理由有两个。"
    play voice "voice/神野大和/1900460.ogg"
    stranger "你的祖母历代供奉的天神，是和我一样的存在。"
    play voice "voice/神野大和/1900470.ogg"
    stranger "所以，你才会一出生就有和我一样的疾病——不，是一样的体质。"
    play voice "voice/神野大和/1900480.ogg"
    stranger "因为现代医学无法治愈，所以只能将其当做特殊体质。"
    play voice "voice/神野大和/1900490.ogg"
    stranger "但我还是可以去学校的，所以你的程度似乎更加严重。"
    play voice "voice/神野大和/1900500.ogg"
    stranger "另一个理由是源于同病相怜，毕竟你的思考方式也和我很像。"
    play voice "voice/神野大和/1900510.ogg"
    stranger "所以我无法放着你不管。"
    play voice "voice/神野大和/1900520.ogg"
    stranger "这是和你一样的我——一位无能的前辈，对后辈的教导。"
    play voice "voice/神野大和/1900530.ogg"
    stranger "对你来说，也许我的存在只会是困扰而已。"
    play voice "voice/翔子/0610840.ogg"
    yume "妖精......先生。"
    play voice "voice/翔子/0610850.ogg"
    yume "嗯，是啊......"
    play voice "voice/翔子/0610860.ogg"
    yume "也许是你多管闲事了......"
    play voice "voice/翔子/0610870.ogg"
    yume "因为那些事情，我都是知道的啊......"
    play voice "voice/翔子/0610880.ogg"
    yume "妖精先生没有必要教我的啊......"
    play voice "voice/翔子/0610890.ogg"
    yume "忘记这件事是没有意义的，我早就......知道了啊。"
    play voice "voice/翔子/0610900.ogg"
    yume "残酷的温柔，我也从最开始就知道了......"
    play voice "voice/翔子/0610910.ogg"
    yume "不是这样的......"
    play voice "voice/翔子/0610920.ogg"
    yume "我许下愿望，希望凉君能忘记我，并不是因为这样的......"
    play voice "voice/翔子/0610930.ogg"
    yume "那一天我对着流星许下的愿望，并不是这样的......"
    play voice "voice/翔子/0610940.ogg"
    yume "这一切并不是对别人的温柔......"
    play voice "voice/翔子/0610950.ogg"
    yume "这是我自己的觉悟罢了......"
    play voice "voice/翔子/0610970.ogg"
    yume "为了能够让自己坚强的，觉悟......"
    play voice "voice/翔子/0610980.ogg"
    yume "为了不让凉君看到我的软弱......"
    play voice "voice/翔子/0610990.ogg"
    yume "为了不让凉君为我担心......"
    play voice "voice/翔子/0611000.ogg"
    yume "为了能够成为凉君最可靠的大姐姐......"
    play voice "voice/翔子/0611010.ogg"
    yume "为了能够化解凉君那份逞强，那份冰冷僵硬的感情......"
    play voice "voice/翔子/0611020.ogg"
    yume "为了能够温暖他的世界......"
    play voice "voice/翔子/0611030.ogg"
    yume "两个人一起......"
    play voice "voice/翔子/0611040.ogg"
    yume "从此不再是孤身一人，而是两个人一起......"
    play voice "voice/翔子/0611050.ogg"
    yume "这就是我的，愿望......"
    play voice "voice/翔子/0611060.ogg"
    yume "我希望凉君，能够忘记我......"
    play voice "voice/翔子/0611070.ogg"
    yume "但是，如果病治好了的话......"
    play voice "voice/翔子/0611080.ogg"
    yume "如果身体好起来了的话......"
    play voice "voice/翔子/0611090.ogg"
    yume "如果我坚强起来的话，我想和凉君结婚......"
    play voice "voice/翔子/0611100.ogg"
    yume "这个愿望，是为了能够和凉君一起欢笑的，咒语啊......"
    play voice "voice/神野大和/1900540.ogg"
    stranger "......是吗。"
    play voice "voice/翔子/0611110.ogg"
    yume "嗯。"
    play voice "voice/翔子/0611120.ogg"
    yume "呐，妖精先生......"
    play voice "voice/翔子/0611130.ogg"
    yume "如果我死了的话，也能变成像妖精先生那样吗......"
    play voice "voice/翔子/0611140.ogg"
    yume "也能够变成你现在这样吗......"
    play voice "voice/神野大和/1900550.ogg"
    stranger "我不知道。"
    play voice "voice/神野大和/1900560.ogg"
    stranger "有像我这样被赋予时间的，也有直接被送还的。"
    play voice "voice/神野大和/1900570.ogg"
    stranger "即使得到了时间，也不代表能够被谁观测到。"
    play voice "voice/神野大和/1900580.ogg"
    stranger "即使是自己想要被谁注意到，也许也根本无法触及的，这就是量子的诅咒。"
    play voice "voice/神野大和/1900590.ogg"
    stranger "所以，和死其实是没有什么区别的。"
    play voice "voice/翔子/0611150.ogg"
    yume "是吗......"
    play voice "voice/翔子/0611160.ogg"
    yume "我本来以为即使是死了，只要能陪在凉君身边，那样也不错的......"
    play voice "voice/翔子/0611170.ogg"
    yume "不过，看来是不行的......"
    play voice "voice/翔子/0611180.ogg"
    yume "即使死了，也没有办法吗......"
    play voice "voice/翔子/0611190.ogg"
    yume "即使消失了，也没有办法吗......"
    play voice "voice/神野大和/1900600.ogg"
    stranger "......"
    play voice "voice/翔子/0611200.ogg"
    yume "呐，妖精先生......"
    play voice "voice/翔子/0611210.ogg"
    yume "我一直以来做的怎么样......"
    play voice "voice/翔子/0611220.ogg"
    yume "我没有让凉君困扰吧......"
    play voice "voice/翔子/0611230.ogg"
    yume "我没有让凉君担心吧......"
    play voice "voice/翔子/0611240.ogg"
    yume "我有帮助到凉君了吗......"
    play voice "voice/翔子/0611250.ogg"
    yume "我有成为他的依靠了吗......"
    play voice "voice/翔子/0611260.ogg"
    yume "我是不是，已经成为凉君最可靠的大姐姐了呢......"
    play voice "voice/翔子/0611270.ogg"
    yume "有没有稍微展现出一点，像大姐姐的地方了呢......"
    play voice "voice/神野大和/1900610.ogg"
    stranger "嗯。"
    play voice "voice/神野大和/1900620.ogg"
    stranger "你很坚强。"
    play voice "voice/神野大和/1900630.ogg"
    stranger "比我要坚强许多。"
    play voice "voice/神野大和/1900650.ogg"
    stranger "你在他面前，一直都很坚强。"
    pause 0.1 hard
    scene set only xz_cg bed seven
    with dissolve
    play voice "voice/翔子/0611280.ogg"
    yume "嗯。"
    play voice "voice/翔子/0611290.ogg"
    yume "太好了......"
    play voice "voice/翔子/0611300.ogg"
    yume "真的，太好了......"
    play voice "voice/神野大和/1900660.ogg"
    stranger "......"
    pause 0.1 hard
    scene set only xz_cg bed three
    with dissolve
    pause 0.5 hard
    play voice "voice/翔子/0611310.ogg"
    yume "妖精......先生？"
    play voice "voice/翔子/0611320.ogg"
    yume "回去了啊......"
    pause 0.1 hard
    scene set only xz_cg bed two
    with dissolve
    play voice "voice/翔子/0611330.ogg"
    yume "谢谢你......"
    play voice "voice/翔子/0611340.ogg"
    yume "至今为止，谢谢你......"
    play voice "voice/翔子/0611350.ogg"
    yume "那......可以了吧......"
    play voice "voice/翔子/0611360.ogg"
    yume "已经......可以了吧......"
    play voice "voice/翔子/0611370.ogg"
    yume "即使软弱......也可以了吧......"
    pause 0.1 hard
    scene set only xz_cg bed four
    with dissolve
    play voice "voice/翔子/0611380.ogg"
    yume "呜......呜......"
    play voice "voice/翔子/0611390.ogg"
    yume "不要啊......"
    $ flcam.move(-750, -1100, 300, duration=1.5, warper='ease_quad')
    pause 1.5 hard
    play voice "voice/翔子/0611400.ogg"
    yume "我不要死......"
    play voice "voice/翔子/0611410.ogg"
    yume "我不想死......"
    play voice "voice/翔子/0611420.ogg"
    yume "我不想消失......"
    play voice "voice/翔子/0611430.ogg"
    yume "我想活下去......"
    play voice "voice/翔子/0611440.ogg"
    yume "我不想和凉君分开......"
    play voice "voice/翔子/0611450.ogg"
    yume "我想陪在凉君身边......"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    play voice "voice/翔子/0611460.ogg"
    yume "我想要和凉君......一起活下去啊！"
    pause 2.0 hard
    scene black
    with slowerdissolve
    pause 3.0 hard
    $ end_replay()

label day15.starview_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua4
    with dissolve
    pause 2.0 hard
    "气温比起白天下降了很多。"
    "白色的结晶从头顶的夜空中飘落下来。"
    "雪花开始飘落。"
    "天空被厚重的云层遮盖着。"
    "今晚并没有星星在闪耀。"
    pause 1.0 hard
    scene set only street night yinghua
    show snow onlayer m1
    with dissolve
    pause 2.0 hard
    "路上没有一个行人。"
    "寂静得甚至能够听到雪花落地的声音。"
    "那雪花如同在眼前飘舞的樱花一般，让我仿佛回到了与翔子初会时的情景。"
    "如果再一次被问到的话，我会怎么回答呢？"
    "我会说，我喜欢凋零的樱花吗？"
    "我会觉得春之花那短暂的生命很美丽吗？"
    "现在的我肯定会这么回答的吧。"
    "一定是和翔子一样的答案的吧。"
    "比起凋零的樱花，我更喜欢初开的樱花。"
    pause 1.0 hard
    scene set only starview night road
    show snow onlayer m1
    with dissolve
    pause 2.0 hard
    "和一诚分开后，我前往医院，确认了依旧是谢绝会面的状态。"
    "之后我还去了图书馆，查尽了一切会导致陷入昏迷的疾病。"
    "翔子在信上写到星光所导致的疾病——是一种天体电波过敏症候群，世界上还只是有假设的些许案例而已。"
    "而且，不仅仅是从天体发出的，就连电磁波本身对人体的影响，医学界都没有明确的定论。"
    "虽然有不少相关的研究者，但却始终没有取得实质上的进展。"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard
    $ set_replay_scene("label4_4")
    $ flcam.move(0, 0, 0)
    scene set only starview night starview
    with dissolve
    show snow onlayer m1
    $ flcam.move(0, 0, 0)
    $ flcam.move(0, -300, 900, duration=15.0, warper='ease_cubic')
    pause 5.0 hard
    "如樱花飘落的雪。"
    "视野中的白与黑。"
    pause 2.0 hard
    stop music fadeout 5.0
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 1.25 alpha 1
    pause 5.0 hard
    "在那里，没有光。"
    "黑白交织的雪景之中。"
    "在那看不见星空的观景台，我依然遇见了“她”——"
    "本来以为不会遇到的。"
    "因为今晚看不到星星。"
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    play music first_36 fadein 3.0 if_changed
    scene set only lisite_cg final one
    with slowerdissolve
    pause 3.0 hard
    "但是，她站在那里。"
    "勉强着自己，逞强着、在这里等我。"
    me01 "雷亚......"
    me01 "我可以......依赖你吗？" 
    pause 0.1 hard
    scene set only lisite_cg final two
    with dissolve
    play voice "voice/天使雷亚/0021980.ogg"
    lst "嗯。" 
    play voice "voice/天使雷亚/0021990.ogg"
    lst "凉君，可以依赖我的。"
    play voice "voice/天使雷亚/0022000.ogg"
    lst "凉君，对我撒娇也可以的。"
    play voice "voice/天使雷亚/0022010.ogg"
    lst "这并不意味着凉君是软弱的，也并不意味着凉君在逃避。"
    pause 0.1 hard
    scene set only lisite_cg final one
    with dissolve
    play voice "voice/天使雷亚/0022020.ogg"
    lst "因为是凉君，所以可以依赖我。"
    play voice "voice/天使雷亚/0022030.ogg"
    lst "因为是凉君，所以对我撒娇也可以的。"
    play voice "voice/天使雷亚/0022040.ogg"
    lst "如果是凉君的话，我也会很开心的。"
    play voice "voice/天使雷亚/0022050.ogg"
    lst "我想要帮助凉君。"
    play voice "voice/天使雷亚/0022060.ogg"
    lst "因为我们已经，可以帮助彼此了。"
    play voice "voice/天使雷亚/0022070.ogg"
    lst "我们已经成为这种关系了......"
    me01 "雷亚。"
    me01 "拜托了......"
    me01 "梦的病，割去吧......"
    me01 "翔子的诅咒，割去吧......"
    me01 "用那把镰刀，割去吧......"
    me01 "那才是困扰着我的、困扰我们的，真正的噩梦。"
    me01 "那家伙明明从出生起就患有疾病，却从来不肯向我提起。"
    me01 "一次也没有向我说过泄气的话。"
    me01 "一次也没有在我面前展现出自己的软弱。"
    me01 "一直都是那样开心地笑着。"
    me01 "一直都是很幸福地露出笑容。"
    me01 "翔子、还有梦她......一直都很坚强。"
    me01 "却也一直都在逞强。"
    me01 "在我面前，摆出一副大姐姐的姿态。"
    me01 "对我说着撒娇也可以的。"
    me01 "明明不可能不痛苦的。"
    me01 "明明不可能不难过的，却又装作没事。"
    me01 "一直是那样的。"
    me01 "勉强着自己。"
    me01 "忍耐着......"
    me01 "明明对我说了，不用逞强也可以的......"
    me01 "真是笨蛋。翔子她，真是个大笨蛋！"
    me01 "而就这样默默地接受了一切的我，更是一个十足的大笨蛋！"
    pause 0.1 hard
    scene set only lisite_cg final two
    with dissolve
    play voice "voice/天使雷亚/0022090.ogg"
    lst "嗯，可以哟~"
    play voice "voice/天使雷亚/0022100.ogg"
    lst "凉君的愿望，我接受了。"
    me01 "拜托了，雷亚......"
    me01 "那疾病，对翔子来说大概就是噩梦了吧。"
    me01 "所以......"
    me01 "割去吧。"
    me01 "将它送还吧。"
    me01 "救救翔子吧。"
    me01 "救救梦吧。"
    pause 0.1 hard
    scene set only lisite_cg final three
    with dissolve
    play voice "voice/天使雷亚/0022110.ogg"
    lst "只是割去疾病的话，是做不到的。"
    play voice "voice/天使雷亚/0022120.ogg"
    lst "如果她的疾病是与生俱来的话，那是无法被否定的存在。"
    play voice "voice/天使雷亚/0022130.ogg"
    lst "如果把疾病送还的话，大概会连她自己也一起送还的。"
    play voice "voice/天使雷亚/0022140.ogg"
    lst "痊愈与归还，并不是等价的。"
    play voice "voice/天使雷亚/0022150.ogg"
    lst "如果疾病消失了的话，她也会消失的。"
    play voice "voice/天使雷亚/0022160.ogg"
    lst "她的存在就是这样的，“与生俱来”就是这么回事的。"
    me01 "怎么会......"
    pause 0.1 hard
    scene set only lisite_cg final one
    with dissolve
    play voice "voice/天使雷亚/0022170.ogg"
    lst "所以凉君。"
    play voice "voice/天使雷亚/0022180.ogg"
    lst "将我送还吧。"
    play voice "voice/天使雷亚/0022190.ogg"
    lst "请用这把镰刀，将我送还吧。"
    pause 0.1 hard
    scene set only lisite_cg final four
    with dissolve
    play voice "voice/天使雷亚/0022210.ogg"
    lst "这样的话，一定能够救她的。"
    play voice "voice/天使雷亚/0022220.ogg"
    lst "将我送还的话，就意味着环绕着我的光也会送还。"
    play voice "voice/天使雷亚/0022230.ogg"
    lst "我的光——流星中蕴含的愿望，就会回到它应该存在的地方。"
    play voice "voice/天使雷亚/0022250.ogg"
    lst "环绕着我的光，会回到你们两人的身上。"
    play voice "voice/天使雷亚/0022260.ogg"
    lst "回到凉君，以及凉君想要守护的她的身上。"
    play voice "voice/天使雷亚/0022270.ogg"
    lst "因为我接受了你们两个人的愿望。"
    play voice "voice/天使雷亚/0022280.ogg"
    lst "我是因为你们的愿望而苏醒的。"
    play voice "voice/天使雷亚/0022290.ogg"
    lst "你们两人的愿望化作了光，我才得以降生。"
    "七年前，在我将要离开樱花镇的那个晚上。"
    "天空划过了第一颗星辰。"
    "那是闪烁着耀眼光芒的流星。"
    play voice "voice/天使雷亚/0022300.ogg"
    lst "那时的凉君，许下了能和“她”再见的愿望。"
    pause 1.0 hard
    scene set only sky evening yinghua3
    with dissolve
    pause 2.0 hard
    show liuxing onlayer m2:
        xpos 0.45 ypos 0.3
    pause 1.0 hard
    "翔子会来送我的吧，会来挽留我的吧。"
    "抱着这样希望的我翘首以盼。"
    "然而，翔子她并没有来。"
    "于是乎我只能把这一切期盼化作愿望托付给了“她”最喜欢的星星。"
    "对那孩子气的、毫无科学依据的咒语，我第一次相信了。"
    "直到现在我才明白。"
    "当时的“她”即使想来也来不了。"
    "因为她的身体已经不允许她外出了。"
    pause 2.0 hard
    scene set only lisite_cg final four
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/0022310.ogg"
    lst "而另一边，因为发烧而沉睡的、曾一样用羡慕的眼神眺望着星空的“她”也许下了心愿。"
    play voice "voice/天使雷亚/0022320.ogg"
    lst "希望凉君能够忘记自己。"
    play voice "voice/天使雷亚/0022330.ogg"
    lst "所以我才会以这个姿态醒来。"
    play voice "voice/天使雷亚/0022340.ogg"
    lst "所以我才会拿着收割噩梦的镰刀在这里等着凉君，为的就是实现她的愿望。"
    play voice "voice/天使雷亚/0022350.ogg"
    lst "而相对的，作为回应凉君你的愿望，我才会以你最想见到的“她”的样子出现在你的面前。"
    "所以雷亚才会知道我的名字。"
    "所以才会出现两个翔子。"
    "都是因为我们许下了愿望。"
    "那个希望我放下过去，重新开始新的人生的翔子——梦。"
    "以及那个希望与我重逢，实现再会约定的翔子。"
    "此刻都在以自己希望的方式努力地活着。"
    pause 0.1 hard
    scene set only lisite_cg final five
    with dissolve
    play voice "voice/天使雷亚/0022360.ogg"
    lst "我的这个姿态，正是你们两人愿望的化身。"
    play voice "voice/天使雷亚/0022370.ogg"
    lst "环绕着我的光芒，正是你们两人约定的象征。"
    pause 0.1 hard
    scene set only lisite_cg final four
    with dissolve
    play voice "voice/天使雷亚/0022380.ogg"
    lst "所以，用这把镰刀将我割去的话。"
    play voice "voice/天使雷亚/0022390.ogg"
    lst "愿望就能归还到你们的身上。"
    play voice "voice/天使雷亚/0022400.ogg"
    lst "那一定，能成为你们的力量。"
    play voice "voice/天使雷亚/0022410.ogg"
    lst "两人小时候的愿望，一定会随着成长化作彼此的力量。"
    play voice "voice/天使雷亚/0022420.ogg"
    lst "凉君，能够得到帮助“她”的力量。"
    play voice "voice/天使雷亚/0022430.ogg"
    lst "而“她”，也能得到回应凉君的力量。"
    play voice "voice/天使雷亚/0022440.ogg"
    lst "那是眼睛所看不见的，不可思议的力量。"
    play voice "voice/天使雷亚/0022450.ogg"
    lst "不可思议的光。"
    play voice "voice/天使雷亚/0022460.ogg"
    lst "但是，确是真实存在的。"
    play voice "voice/天使雷亚/0022470.ogg"
    lst "一定是存在的。"
    play voice "voice/天使雷亚/0022480.ogg"
    lst "星星所拥有的光，人所拥有的光。"
    play voice "voice/天使雷亚/0022490.ogg"
    lst "以及人类的愿望所孕育的光。"
    play voice "voice/天使雷亚/0022500.ogg"
    lst "无论哪种，都是一样的强烈。"
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        1.75
        linear 1.25 alpha 1
    pause 4.0 hard
    scene set only lisite_cg cut1
    show sepiagrain onlayer texture
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/0022510.ogg"
    lst "这样就不用再烦恼了。"
    play voice "voice/天使雷亚/0022520.ogg"
    lst "凉君就不会再悲伤了。"
    play voice "voice/天使雷亚/0022530.ogg"
    lst "我的使命结束了。"
    play voice "voice/天使雷亚/0022550.ogg"
    lst "我结下的羁绊被切断了。"
    pause 0.1 hard
    scene set only lisite_cg cut3
    show sepiagrain onlayer texture
    with dissolve
    $ flcam.move(-1400, -1500, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0022560.ogg"
    lst "要和凉君，永别了......"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg final four
    with dissolve
    pause 2.0 hard
    me01 "这种事情怎么可能做得到！"
    play voice "voice/天使雷亚/0022570.ogg"
    lst "能做到的。"
    me01 "怎么可能做得到......"
    pause 0.1 hard
    scene set only lisite_cg final five
    with dissolve
    stop music fadeout 5.0
    play voice "voice/天使雷亚/0022580.ogg"
    lst "不，是能做到的。"
    me01 "即使这样真的能够拯救翔子，但相对的雷亚你就会消失了！"
    play voice "voice/天使雷亚/0022590.ogg"
    lst "我说过的吧......"
    play music first_33 fadein 3.0 if_changed
    pause 0.1 hard
    scene set only lisite_cg final four
    with dissolve
    $ flcam.move(-1400, -1500, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0022600.ogg"
    lst "凉君依赖我也可以的。"
    play voice "voice/天使雷亚/0022610.ogg"
    lst "对我撒娇也可以的。"
    play voice "voice/天使雷亚/0022620.ogg"
    lst "因为是凉君，所以可以依赖我的。"
    play voice "voice/天使雷亚/0022630.ogg"
    lst "因为是凉君，所以对我撒娇也可以的。"
    play voice "voice/天使雷亚/0022640.ogg"
    lst "因为是凉君，把我的生命托付给你也是可以......"
    "为什么。"
    "为什么现在的雷亚还会保持微笑呢。"
    "为什么此刻的她看上去却是那么的幸福呢。"
    pause 0.1 hard
    scene set only lisite_cg final five
    with dissolve
    play voice "voice/天使雷亚/0022650.ogg"
    lst "因为，已经完全没问题了。"
    play voice "voice/天使雷亚/0022660.ogg"
    lst "我已经没事了。"
    play voice "voice/天使雷亚/0022670.ogg"
    lst "那一定是，能到达约定另一端的存在。"
    pause 0.1 hard
    scene set only lisite_cg final four
    with dissolve
    play voice "voice/天使雷亚/0022680.ogg"
    lst "我们的，羁绊。"
    me01 "羁绊......"
    play voice "voice/天使雷亚/0022690.ogg"
    lst "对，羁绊。"
    me01 "那种东西，如果雷亚消失了不就没有意义了吗！"
    me01 "羁绊也会跟着一起消失的！"
    play voice "voice/天使雷亚/0022700.ogg"
    lst "我并不是消失了。"
    play voice "voice/天使雷亚/0022710.ogg"
    lst "我依旧是存在着的。"
    play voice "voice/天使雷亚/0022720.ogg"
    lst "即使看不见，但我依然是存在的。"
    play voice "voice/天使雷亚/0022730.ogg"
    lst "我就在凉君的身边。"
    play voice "voice/天使雷亚/0022740.ogg"
    lst "那时的“她”——梦，一定也是这样想的。"
    play voice "voice/天使雷亚/0022750.ogg"
    lst "梦一定，也是坚信着自己并不会消失，而是能够陪在凉君身边的。"
    play voice "voice/天使雷亚/0022760.ogg"
    lst "一定也是这么相信着。"
    play voice "voice/天使雷亚/0022770.ogg"
    lst "所以才一直没有展现出软弱的一面。"
    play voice "voice/天使雷亚/0022780.ogg"
    lst "直到最后，都很坚强。"
    play voice "voice/天使雷亚/0022790.ogg"
    lst "没有放弃。"
    play voice "voice/天使雷亚/0022800.ogg"
    lst "想和你在一起的那份心情，是绝对不会放弃的。"
    play voice "voice/天使雷亚/0022810.ogg"
    lst "我也想和她一样。"
    play voice "voice/天使雷亚/0022840.ogg"
    lst "我不想输给梦。"
    play voice "voice/天使雷亚/0022850.ogg"
    lst "喜欢凉君这份心情，我不想输给任何人。"
    me01 "雷亚你，还真是讨厌输啊。"
    play voice "voice/天使雷亚/0022860.ogg"
    lst "嗯。"
    me01 "而且，还是个别扭鬼。"
    play voice "voice/天使雷亚/0022870.ogg"
    lst "嗯。"
    me01 "七年前我们许下了愿望的流星。"
    me01 "找到它的话是不是就能再见面了？"
    play voice "voice/天使雷亚/0022880.ogg"
    lst "我不知道。但是，我想它一定就在樱华镇的附近。"
    play voice "voice/天使雷亚/0022890.ogg"
    lst "因为这个观景台，是我最容易显现的地方。"
    me01 "是吗。"
    play voice "voice/天使雷亚/0022900.ogg"
    lst "嗯。"
    me01 "雷亚，你听好了，这是我们新的约定。"
    me01 "沉睡在某处的，雷亚的陨石。"
    me01 "我一定会找出来的。"
    me01 "找出来，然后将你带回我身边的。"
    me01 "如果你睡着的话，我就把你叫醒。"
    me01 "如果你闹别扭的话，就算是被你讨厌我也会将你拉回来的。"
    me01 "这就是我们的约定，这就是神野凉和雷亚两个人的约定。"
    me01 "你有意见吗！"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0022910.ogg"
    lst "凉君......"    
    play voice "voice/天使雷亚/0022920.ogg"
    lst "都这种时候了，也还是笨笨的呢。"
    play voice "voice/天使雷亚/0022930.ogg"
    lst "我明明说了，即使我消失了也还会留在你身边的。"
    me01 "那样是不够的！"
    me01 "一直活在心里什么的我才不要！"
    me01 "不能拥抱雷亚的话我才不要！"
    me01 "不能抚摸雷亚的头我不能接受！"
    play voice "voice/天使雷亚/0022940.ogg"
    lst "凉君，真是贪心啊......"
    me01 "啊是的，我一直是很贪心的。"
    me01 "所以，只是陪在身边的话是不够的。"
    me01 "不能感受到你的全部是不行的。"
    play voice "voice/天使雷亚/0022950.ogg"
    lst "凉君。"
    pause 0.1 hard
    scene set only lisite_cg final five
    with dissolve
    play voice "voice/天使雷亚/0022960.ogg"
    lst "真的是，笨笨的......"
    me01 "是啊。"
    pause 0.1 hard
    scene set only lisite_cg final seven
    with dissolve
    me01 "只能用这种方式拯救翔子的我，真的是笨得无药可救了。"
    pause 0.1 hard
    scene set only lisite_cg final six
    with dissolve
    play voice "voice/天使雷亚/0022970.ogg"
    lst "凉君......"
    pause 0.1 hard
    scene set only lisite_cg final eight
    with dissolve
    $ flcam.move(-1400, -1500, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0022980.ogg"
    lst "那样的话，凉君。"
    play voice "voice/天使雷亚/0022990.ogg"
    lst "拜托了。"
    play voice "voice/天使雷亚/0023000.ogg"
    lst "在我没有后悔之前，一口气......"
    me01 "一定要等着我。"
    play voice "voice/天使雷亚/0023010.ogg"
    lst "嗯。"
    me01 "这只是短暂的离别。"
    play voice "voice/天使雷亚/0023020.ogg"
    lst "嗯。"
    me01 "马上就会再见的。"
    play voice "voice/天使雷亚/0023030.ogg"
    lst "嗯。"
    play voice "voice/天使雷亚/0023040.ogg"
    lst "我会等着的。"
    play voice "voice/天使雷亚/0023050.ogg"
    lst "我会等着你们两人再一次找到我的。"
    me01 "这是就是我们的约定。"
    play voice "voice/天使雷亚/0023060.ogg"
    lst "嗯，约定......"
    "一定会实现的。"
    "然后收获存在于约定之地的果实。"
    "到达约定的彼端。"
    "再一次将羁绊握在手中。"
    play voice "voice/天使雷亚/0023070.ogg"
    lst "我最喜欢凉君了。"
    play voice "voice/天使雷亚/0023080.ogg"
    lst "我也最喜欢梦了。"
    play voice "voice/天使雷亚/0023090.ogg"
    lst "因为，多亏了你们两人我才能醒来。"
    play voice "voice/天使雷亚/0023100.ogg"
    lst "才能降生在这颗星球上。"
    play voice "voice/天使雷亚/0023110.ogg"
    lst "所以呢。"
    play voice "voice/天使雷亚/0023120.ogg"
    lst "你们两人就像是我的爸爸和妈妈一样。"
    pause 0.1 hard
    scene set only lisite_cg final nine
    with dissolve
    $ flcam.move(-1500, -2800, 900, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/天使雷亚/0023130.ogg"
    lst "是我的家人啊——"
    pause 3.0 hard
    scene white 
    with slowerdissolve
    pause 3.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    $ end_replay()
    pause 5.0 hard
    play music first_61 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    scene end_graph at Pan((0, 3783), (0, 0), 200.0, time_warp=cgease, subpixel=True)
    with slowerdissolve
    pause 5.0 hard
    show logo_first onlayer f2 at end_words
    pause 30.0 hard
    show end_1 onlayer f2 at end_words with slowerdissolve
    show end_pic1 onlayer m2 at end_lpic with slowerdissolve
    pause 20.0 hard
    show end_2 onlayer f2 at end_words with slowerdissolve
    show end_pic2 onlayer m2 at end_rpic with slowerdissolve
    pause 6.0 hard
    show end_3 onlayer f2 at end_words with slowerdissolve
    pause 8.0 hard
    show end_4 onlayer f2 at end_words with slowerdissolve
    pause 8.0 hard
    show end_5 onlayer f2 at end_words with slowerdissolve
    show end_pic3 onlayer m2 at end_lpic with slowerdissolve
    pause 5.0 hard
    show end_6 onlayer f2 at end_words with slowerdissolve
    pause 20.0 hard
    show end_7 onlayer f2 at end_words with slowerdissolve
    show end_pic4 onlayer m2 at end_lpic with slowerdissolve
    pause 20.0 hard
    show end_8 onlayer f2 at end_words with slowerdissolve
    show end_pic5 onlayer m2 at end_rpic with slowerdissolve
    pause 20.0 hard
    show end_9 onlayer f2 at end_words with slowerdissolve
    show end_pic6 onlayer m2 at end_lpic with slowerdissolve
    pause 20.0 hard
    show end_10 onlayer f2 at end_words with slowerdissolve
    show end_pic7 onlayer m2 at end_rpic with slowerdissolve
    pause 35.0 hard
    stop music fadeout 5.0
    scene black
    with slowerdissolve
    pause 5.0 hard

label day15.end_event01:
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    $ set_replay_scene("label5_1")
    scene white
    with slowerdissolve
    pause 3.0 hard
    nvl clear
    play voice "voice/天使雷亚/0090001.ogg"
    pcenter "  就像在做梦一样。"
    nvl clear
    play voice "voice/天使雷亚/0090002.ogg"
    pcenter "  就像在母亲的肚子里一样。"
    nvl clear
    play voice "voice/天使雷亚/0090003.ogg"
    pcenter "  我就这样沉睡着。"
    nvl clear
    pause 2.0 hard
    play music first_39 fadein 3.0 if_changed
    $ flcam.move(0, 0, 1200)
    scene set only lisite_cg end one
    $ flcam.move(0, 0, 0, duration=50.0, warper='ease_quad')
    with slowerdissolve
    pause 3.0 hard
    play voice "voice/天使雷亚/0090005.ogg"
    "这里是初始之地。"
    play voice "voice/天使雷亚/0090006.ogg"
    "生命诞生的源头。"
    play voice "voice/天使雷亚/0090007.ogg"
    "被送走，归还，陷入沉睡。"
    play voice "voice/天使雷亚/0090008.ogg"
    "然后慢慢沉浸于生死混沌，虚实并存的境界之中。"
    play voice "voice/天使雷亚/0090009.ogg"
    "在重力的牵引下缓缓下沉。"
    play voice "voice/天使雷亚/0090010.ogg"
    "慢慢地回旋着。"
    play voice "voice/天使雷亚/0090011.ogg"
    "慢慢地，非常缓慢地，在这个空间中回旋着。"
    play voice "voice/天使雷亚/0090012.ogg"
    "这里很温暖，因为太过温暖，所以连回转都感觉不到。"
    play voice "voice/天使雷亚/0090013.ogg"
    "环抱着的思念仿佛下一刻就要从手中滑落。"
    play voice "voice/天使雷亚/0090014.ogg"
    "仿佛马上就要放开与那个人的回忆了。"
    play voice "voice/天使雷亚/0090015.ogg"
    "我的这个个体，曾经就是这样的。"
    play voice "voice/天使雷亚/0090016.ogg"
    "在不到一年的时间里，那些无可替代的回忆，塑造了我的形体。"
    play voice "voice/天使雷亚/0090017.ogg"
    "如果没有这些回忆的话，我的存在可能已经在途中就归还母胎——我的故乡了吧。"
    play voice "voice/天使雷亚/0090018.ogg"
    "但我依旧在这里。"
    play voice "voice/天使雷亚/0090019.ogg"
    "仍然可以维持着。"
    play voice "voice/天使雷亚/0090020.ogg"
    "被守护着。"
    play voice "voice/天使雷亚/0090021.ogg"
    "到底能存在多久呢。"
    play voice "voice/天使雷亚/0090022.ogg"
    "能维持到百年之后吗，还是说只是几年，亦或者连几天都坚持不了呢。"
    play voice "voice/天使雷亚/0090024.ogg"
    "即使如此，我依然有着能够重生的未来。"
    play voice "voice/天使雷亚/0090025.ogg"
    "我这么相信着。"
    play voice "voice/天使雷亚/0090026.ogg"
    "并不是虚无的泡影幻梦。"
    play voice "voice/天使雷亚/0090027.ogg"
    "我可以确信。"
    play voice "voice/天使雷亚/0090028.ogg"
    "因为我们许下了约定。"
    play voice "voice/天使雷亚/0090029.ogg"
    "因为得到了约定的光。"
    play voice "voice/天使雷亚/0090030.ogg"
    "那是在温暖的沉睡之中，依然能够感觉到的、温柔的光。"
    play voice "voice/天使雷亚/0090031.ogg"
    "所以。"
    play voice "voice/天使雷亚/0090032.ogg"
    "只要朝着光芒的方向继续前进的话。"
    pause 1.0 hard
    scene set only lisite_cg end two
    with dissolve
    pause 2.0 hard
    play voice "voice/天使雷亚/0090033.ogg"
    "在那里，回忆一定还在延续着——"
    pause 2.0 hard
    stop music fadeout 5.0
    scene white
    with slowerdissolve 
    pause 3.0 hard
    $ end_replay()
    $ set_replay_scene("label2_1")
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua
    with slowdissolve
    play music first_33 fadein 3.0 if_changed
    pause 2.0 hard
    play voice "voice/翔子/0611470.ogg"
    xz "我们所居住的太阳系，正在以秒速1 9 k m左右的速度，朝武仙座移动着。"
    play voice "voice/翔子/0611480.ogg"
    xz "在那个方向，离天琴座很近哟~"
    play voice "voice/翔子/0611490.ogg"
    xz "地球正在向着天琴座的织女星移动着。"
    play voice "voice/翔子/0611500.ogg"
    xz "而这颗行星，也正在等待七夕的到来。"
    pause 1.0 hard
    scene set only xz_cg end two
    with slowdissolve
    pause 2.0 hard
    play voice "voice/翔子/0611510.ogg"
    xz "所以呢，雷亚她......"
    me01 "嗯。总有一天我们还能再见的。"
    me01 "大家，都能再见面的。"
    play voice "voice/翔子/0611520.ogg"
    xz "嗯，是呢~"
    $ flcam.move(-1500, -100, 1200, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "雷亚的光化作化成的吊坠，保护着翔子不受其他电磁波的影响。"
    "那股不可思议的力量曾经无数次地拯救了我。"
    "然而现在我却无法再次拥抱她了。"
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    "另一方面，量子冲突似乎也随着雷亚的消失而解除了。"
    "从那以后，我也再也没有见到过有着儿时容貌的翔子。"
    "再也没有见到梦。"
    "也许她也被送还天空了吧。"
    "去寻找她最热爱的星空去了吧。"
    "去追求自己还未实现的梦想了吧。"
    "不同的是，眼前的翔子并不是之前的任何一个。"
    "更确切地说应该是两者的结合体。"
    "拥有健康身体的，温柔可靠的大姐姐。"
    "向往自由的同时，也能成为别人的依靠，两个愿望都被实现了。"
    "时空在这一刻重合了。"
    "约定在这一刻到达了彼方。"
    "我们，长大了......"
    play voice "voice/翔子/0611530.ogg"
    xz "所以，从这颗行星上仰望的七夕之星，他们的光辉也在逐渐增强。"
    play voice "voice/翔子/0611540.ogg"
    xz "越接近，光就越强烈。"
    me01 "可即便如此，要前往那里的话还是需要大概三十二万五千年左右的时间吧。"
    play voice "voice/翔子/0611580.ogg"
    xz "是啊。"
    me01 "这么久的话，大家说不定都已经不在了。"
    me01 "七夕之星也是，我们也是，雷亚也是......"
    scene set only xz_cg end one
    play voice "voice/翔子/0611590.ogg"
    xz "不是的，一定会再见的。"
    play voice "voice/翔子/0611600.ogg"
    xz "即使星星不在那里了，它的光也是不会消失的。"
    play voice "voice/翔子/0611610.ogg"
    xz "星星的光芒永远都会在在那里闪耀着的。"
    play voice "voice/翔子/0611620.ogg"
    xz "即使去几十亿年，几百亿年也会继续存在着的。"
    play voice "voice/翔子/0611630.ogg"
    xz "那束光芒，无论何时都不会消失的。"
    me01 "也就是说想看的时候总能看得到的吗。"
    scene set only xz_cg end two
    play voice "voice/翔子/0611640.ogg"
    xz "嗯，能看到的。"
    play voice "voice/翔子/0611660.ogg"
    xz "所以，在那之前还是先想好应该怎么准备见面时的招呼呢~"
    me01 "翔子你打算怎么办呢？"
    play voice "voice/翔子/0611670.ogg"
    xz "今天的光芒也比平时的更加耀眼啊，之类的~"
    me01 "其他的呢？"
    play voice "voice/翔子/0611680.ogg"
    xz "请你今后也像往常那样多多关照~"
    me01 "所以说为什么要用商业寒暄一样的语气啊......"
    "真是一段让人怀念的对话。"
    "不变的星空下，我们改变了。即使改变了，有些东西依然不会变。"
    "这就是我们的青春，这就是我们的故事。"
    me01 "啊......"
    scene set only xz_cg end one
    play voice "voice/翔子/0611840.ogg"
    xz "怎么了？"
    me01 "刚才，流星......"
    play voice "voice/翔子/0611850.ogg"
    xz "许了什么愿望？"
    me01 "没什么。"
    play voice "voice/翔子/0611860.ogg"
    xz "许了什么愿望？"
    me01 "回家的路上再慢慢和你说吧。"
    scene set only xz_cg end two
    play voice "voice/翔子/0611870.ogg"
    xz "是啊。晚饭还没有准备呢。"
    me01 "我也来帮忙吧。"
    play voice "voice/翔子/0611880.ogg"
    xz "不用了，只是很普通的事情而已。"
    play voice "voice/翔子/0611900.ogg"
    xz "不过在此之前，记得说声“欢迎回来”哟~"
    me01 "嗯。"
    pause 2.0 hard
    scene set only sky night yinghua
    with slowerdissolve
    pause 2.0 hard
    nvl clear
    pcenter "  我牵着翔子的手跟了上去。"
    nvl clear
    pcenter "  此时的观景台依旧是禁止进入的状态，但是我们每天都会来这里。"
    nvl clear
    pcenter "  因为在那里，在下一个季节到来之前，我们的故事仍在继续——"
    nvl clear
    pause 2.0 hard
    scene white 
    with in2out_v2_slow
    stop music fadeout 5.0
    pause 3.0 hard
    $ end_replay()
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    pause 3.0 hard
    $ suppress_overlay = True
    jump day16
