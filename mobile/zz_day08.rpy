label day08:
    bookmark
    $ save_name = _("Day 08")
    pause 4.0 hard
    scene set only backend_yinghua autumn
    with dissolve
    show backend_bg03 onlayer b1 at backend_bg
    pause 2.0 hard
    show backend_date07 onlayer m1 at backend_date
    pause 5.0 hard
    scene black 
    with dissolve
    pause 2.0 hard
    $ suppress_overlay = False
    play music first_27 fadein 3.0 if_changed
    $ flcam.move(-1500, -2000, 600)
    scene set only hospital day room yinghua alpha
    with dissolve
    pause 1.0 hard
    nvl clear
    pcenter "  少女坐在病床上，眺望着窗外。"
    nvl clear
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only beach day yinghua2
    with dissolve
    pause 1.0 hard
    "阳光照射在海面上，耀眼到甚至会让看着的人觉得头晕目眩。"
    "少女稍微移开了视线，看着一旁那细长的、向着远方无限蔓延的海岸线。"
    play voice "voice/翔子/0601520.ogg"
    stranger "人越来越少了啊......"
    "八月的时候还到处都是人的海滩，如今到了九月却已经是空无一人。"
    "取代了喧闹声，剩下的只有潮水拍打海岸的声响了。"
    play voice "voice/翔子/0601530.ogg"
    stranger "......还想再去一次海边啊。"
    "在那片海滩上留下自己的足迹。"
    "一定是件非常幸福的事吧。"
    "但也正因为知道那是无法实现的愿望，所以才会这么觉得。"
    play voice "voice/翔子/0601540.ogg"
    stranger "好想，再到外面去啊......"
    "因为经常擅自跑出去的关系，所以被下了禁足令。"
    "虽然本来就是禁止的。"
    "少女因为无视了这些规矩，所以回来后护士和医生都很生气。"
    "现在即便只是在走廊上散步，也会立刻被人带回病房。"
    play voice "voice/翔子/0601550.ogg"
    stranger "......你们的恪尽职守还真是辛苦了呢。"
    "医院是一个无聊的地方。"
    "晚上九点熄灯，所有的自由都将被剥夺。"
    "而且连电视和收音机也没有。"
    "因为没有灯光自然也没有办法看书。"
    "已经无聊到无可奈何的地步了。"
    play voice "voice/翔子/0601560.ogg"
    stranger "要不干脆到屋顶上去吧。"
    "晒晒太阳应该还是会被允许的吧。"
    pause 1.0 hard
    scene set only hospital day room yinghua alpha
    with dissolve
    pause 0.5 hard
    "少女刚想要起身，突然发现膝盖使不上力气。"
    "还没来得及反应，就又躺回到了床上。"
    play voice "voice/翔子/0601570.ogg"
    stranger "......以为身体状况还不错的。"
    "现在已经是开学的日子了。"
    "同龄的小伙伴们此刻应该都去学校了吧。"
    "反正也不会有人来看望自己。"
    "所以，作为给自己的补偿，怎么样也得开心地度过每一天。"
    play voice "voice/翔子/0601580.ogg"
    stranger "没办法呢......嗯，没办法。"
    "即使生活如此枯燥，少女也坚信每一天依然有它存在的意义。"
    "所以，即便只能躺在病床上，她也从来没有抱怨过。"
    "再次闭上眼睛。"
    pause 1.0 hard
    scene white
    with slowerdissolve
    pause 2.0 hard
    nvl clear
    pcenter "  下一次也一定，还能睁开的。"
    nvl clear
    pcenter "  一直以来都是这么祈祷着。"
    nvl clear
    pcenter "  于是乎就在睡梦中，少女迎来了自己的生日。"
    nvl clear
    stop music fadeout 5.0
    pause 2.0 hard
    scene black
    with slowerdissolve
    pause 3.0 hard
    scene set only home day myself yinghua
    with cent2side
    pause 2.0 hard
    me01 "最近经常做些奇怪的梦。"
    "名为雷亚的死神少女——"
    "在那次七夕之别后就一直没见她的踪影了。"
    pause 1.0 hard
    play sound close_door
    scene set only street day neighbor
    with dissolve
    pause 2.0 hard
    play ambience1 move_2 fadein 3.0
    scene set only sky day yinghua
    with dissolve
    pause 1.0 hard
    "被镰刀刺进胸口时的那种感觉。"
    "还有为什么当时的你也会流泪。"
    "明明还有一堆问题憋在心里的。"
    pause 1.0 hard
    scene set only street day yinghua
    with dissolve
    pause 1.0 hard
    "雷亚她知道我过去，同时也为了割取我的噩梦一直以来都在观景台等着我。"
    "但是在我的印象中并没有遇到过穿着如此奇特的少女。"
    "而且那家伙明明是一副小孩子的模样，却总以大人的方式和我说话。"
    "不过，那一晚......"
    pause 1.0 hard
    stop ambience1
    scene set only lisite_cg cut3
    show sepiagrain onlayer texture
    with dissolve
    pause 1.0 hard
    "在我被割去噩梦之后，雷亚她就消失了。"
    "一转眼的功夫就不见了。"
    "可能是因为我当时太过恐惧，或者单纯地只是看漏了。"
    "但是说来也奇怪，那家伙几乎每次都是在不经意间就消失了。"
    "真是不可思议。"
    "在那之后，雷亚就好像躲着我似的不再出现在观景台了。"
    pause 1.0 hard
    scene set only school day gate yinghua
    with dissolve
    pause 1.0 hard
    "总之，在一切都没有弄清楚之前，我还是会继续去找她的。"
    "即使她现在不想见我，我也会想办法找到她。"
    "别以为夺走了别人的东西能那么轻易地逃掉啊！"
    pause 1.0 hard

label day08.school_event01:
    scene set only school day room2 yinghua
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    play music first_06 fadein 3.0 if_changed
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/日向怜/0140220.ogg"
    rxl "早上好，小凉~"
    me01 "早上好。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_a1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140230.ogg"
    rxl "真是的，为什么无精打采的？"
    play voice "voice/日向怜/0140240.ogg"
    rxl "早上的问候应该是要笑着说出来才对吧。"
    me01 "......说的是呢。"
    show rxl_dzf_b1 b1 b1_n3
    play voice "voice/日向怜/0140250.ogg"
    rxl "就是啊~"
    me01 "那......早上好日向同学。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_h3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140260.ogg"
    rxl "嗯，做得不错~"
    hide rxl_dzf_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.3)
    pause 0.5 hard
    play voice "voice/青木铃音/0533090.ogg"
    lingyin "神野同学，不来问候我一下吗？"
    me01 "早上好，铃音同学。"
    show lingyin_dzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0533100.ogg"
    lingyin "永别了，神野同学~"
    hide lingyin_dzf_b2
    play sound hite_2
    show lingyin sd1 onlayer b2 at basicfade_c2u:
        xpos 0.08
    "铃音笑着拿出薙刀架在了我的脖子上。"
    with vpunch
    me01 "为、为什么会这样啊！？"
    pause 0.5 hard
    show lingyin sd2
    with dissolve
    play voice "voice/青木铃音/0533110.ogg"
    lingyin "啊，不好了。一不小心说出真心话了。"
    me01 "就这么想把我一刀两断吗！"
    pause 0.5 hard
    hide lingyin sd2
    pause 2.0 hard
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    show rxl_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140270.ogg"
    rxl "小铃，那把薙刀是怎么回事？"
    play voice "voice/青木铃音/0533120.ogg"
    lingyin "跟书包弄错了所以把这个带过来了。"
    "我觉得这是绝不可能发生的事情。"
    hide lingyin_dzf_b2
    hide rxl_dzf_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_s1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/一诚总司/1606140.ogg"
    yczs "不过我也能理解铃音为什么生气。毕竟我们都以为你谈恋爱了。"
    me01 "......诶？"
    hide yczs_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140280.ogg"
    rxl "我、我可还什么都没有说啊。"
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    $ flcam.move(-2250, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533130.ogg"
    lingyin "我和一诚同学跟你相处的时间也算挺长的了。即使日向同学你不说我们也清楚的。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_c1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    show han onlayer m2:
        xalign 0.47 yalign 0.37
    play voice "voice/日向怜/0140290.ogg"
    rxl "反正我就是不擅长隐瞒事情啊！"
    pause 0.5 hard
    hide han
    hide rxl_dzf_b1
    hide lingyin_dzf_b2
    stop music fadeout 5.0
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "那个......"
    "这些人到底在说什么啊？"
    play sound hite_2
    show lingyin sd1 onlayer b2 at basicfade_c2u:
        xpos 0.19
        zoom 1.3
    play voice "voice/青木铃音/0533140.ogg"
    lingyin "拜托你能给出一个让我们认可的理由。"
    me01 "薙刀越来越近了啊！"
    pause 1.0 hard
    hide lingyin sd1
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140300.ogg"
    rxl "......小凉，如果觉得难为情的话就由我来说吧？"
    me01 "所以到底要是什么事啊？"
    $ flcam.move(0, -450, 1000, duration=1.5)
    pause 0.5 hard
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140310.ogg"
    rxl "小凉你呢，喜欢上了那位小学女生了。"
    play music first_13 fadein 3.0 if_changed
    me01 "......小学生？你说雷亚吗？"
    show rxl_dzf_b2 b2 b2_s2
    play voice "voice/日向怜/0140320.ogg"
    rxl "小凉你爱上了观景台的幼女。"
    me01 "为什么突然从小学女生改口成幼女了啊！"
    hide rxl_dzf_b2
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.7
    show lingyin_dzf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/一诚总司/1606160.ogg"
    yczs "简单来说就是萝莉控吧。"
    show lingyin_dzf_b1 b1 b1_n3
    play voice "voice/青木铃音/0533150.ogg"
    lingyin "......真是下流。"
    me01 "我可不想被男女通吃的铃音同学这么说。"
    show lingyin_dzf_b1 b1 b1_h1
    play voice "voice/青木铃音/0533160.ogg"
    lingyin "我的目标可不仅仅只是幼女而已哟~"
    me01 "所以说幼女不是我的目标啊！"
    show lingyin_dzf_b1 b1 b1_n2
    play voice "voice/青木铃音/0533170.ogg"
    lingyin "神野同学，请认真地回答我。你真的喜欢上观景台的幼~女了吗？"
    me01 "这其中一定是有什么误会。"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/1606170.ogg"
    yczs "就因为对方是幼~女吧？"
    me01 "所以说为什么要刻意加上重音啊！"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/1606180.ogg"
    yczs "因为你是萝莉控吧。"
    me01 "都说了不是的。"
    hide lingyin_dzf_b1
    hide yczs_dzf_b1
    $ flcam.move(-2800, -100, 400, duration=1.5)
    pause 0.5 hard
    play sound hite_2
    show lingyin sd1 onlayer b2 at basicfade_c2u:
        xpos 0.075
        zoom 1.3
    play voice "voice/青木铃音/0533180.ogg"
    lingyin "神野同学，到底是怎样呢？"
    me01 "要被刺了要被刺了已经被刺了！"
    pause 1.0 hard
    hide lingyin sd1
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140330.ogg"
    rxl "我会永远支持小凉你的......即使世间的风评不太好。"
    me01 "所以说你一定是误会了！"
    hide rxl_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/1606190.ogg"
    yczs "其实你是真的喜欢幼~女的吧？"
    "是非的界限越来越暧昧了。"
    hide yczs_dzf_b1
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.3
    show rxl_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    show yczs_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    me01 "我说啊，我对恋爱什么的也不是很了解。所以也说不清楚自己是不是真的喜欢上观景台的那个幼（咳），女孩。"
    me01 "但是我想要找她，仅此而已。"
    hide rxl_dzf_b2
    hide yczs_dzf_b1
    show lingyin_dzf_b1 b1 b1_h1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide lingyin_dzf_b1
    play sound hite_2
    show lingyin sd1 onlayer b2 at basicfade_c2u:
        xpos 0.08
    play voice "voice/青木铃音/0533190.ogg"
    lingyin "就是说，你果然在要找一个小学生幼女对吧？"
    me01 "脖子已经开始流血了啊！"
    pause 1.0 hard
    hide lingyin sd1
    pause 1.0 hard
    $ flcam.move(-2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_ga1 onlayer m2:
        xpos 0.5
    show lingyin_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/日向怜/0140340.ogg"
    rxl "小铃，谢谢你的提醒。"
    play voice "voice/日向怜/0140350.ogg"
    rxl "但如果再这样让小凉困扰的话，我也会生气的。"
    show lingyin_dzf_b1 b1 b1_sp1
    play voice "voice/青木铃音/0533200.ogg"
    lingyin "日向同学。"
    hide rxl_dzf_b2
    show rxl_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140370.ogg"
    rxl "毕竟对他而言，儿时的愿望也已经实现了。"
    show rxl_dzf_b3 b3 b3_n1
    play voice "voice/日向怜/0140380.ogg"
    rxl "对方也已经和小凉成为好朋友了。"
    show lingyin_dzf_b1 b1 b1_n3
    play voice "voice/青木铃音/0533210.ogg"
    lingyin "......"
    "铃音犹豫着想要说什么，但最终还是选择了沉默。"
    hide lingyin_dzf_b1
    hide rxl_dzf_b3
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/1606200.ogg"
    yczs "好像捡回了一条命啊。"
    me01 "别幸灾乐祸啊！"
    show yczs_dzf_b1 b1 b1_ga1
    play voice "voice/一诚总司/1606210.ogg"
    yczs "火灾和恋爱自古以来就是看热闹之人的终极目标。"
    show yczs_dzf_b1 b1 b1_n2
    play voice "voice/一诚总司/1606220.ogg"
    yczs "观景台的女孩，是神野你的初恋对象吧？"
    me01 "翔子与我只是儿时的玩伴而已。而且我离开的时候距离我们认识也只过了差不多两三个月左右的时间而已。"
    "等等，关于和翔子的过去似乎没有完全消失。"
    "这究竟是怎么一回事呢......"
    hide yczs_dzf_b1
    $ flcam.move(-2250, -200, 600, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    show lingyin_dzf_b1 b1 b1_sp1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0533220.ogg"
    lingyin "意外的短暂啊。"
    play voice "voice/日向怜/0140390.ogg"
    rxl "还以为你们在一起很久了。"
    me01 "当时也只是在观景台才有机会见面的。"
    me01 "在学校里因为各种原因全都错过了。"
    hide rxl_dzf_b2
    hide lingyin_dzf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show yczs_dzf_b1 b1 b1_s1 onlayer m2:
        xpos 0.7
    play voice "voice/一诚总司/1606230.ogg"
    yczs "这就是命运的邂逅吧~"
    hide yczs_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0533230.ogg"
    lingyin "至于那位观景台的不可思议女孩，能找到她吗？"
    me01 "虽然我也没有把握，但无论如何我都必须试看看。"
    pause 1.0 hard
    stop music fadeout 5.0
    scene black 
    with dissolve
    pause 1.0 hard
    "首先是收集情报。"
    "大家的反应先不说，还记得翔子这一点倒是让我有些惊讶。"
    "毕竟按照雷亚说的，那段与翔子的回忆就是我的噩梦根源，然而此时脑海中却还保留着这些记忆。"
    "我究竟忘记了些什么呢？"
    "虽说死神这个设定是我先提出来的，但拥有能够改变他人记忆能力的雷亚，其真身很可能是类似{encyclopedia=lapulasi}拉普拉斯妖{/encyclopedia}一般的存在。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only school day room2 yinghua
    with dissolve
    pause 1.0 hard
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    play music first_04 fadein 3.0 if_changed
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140400.ogg"
    rxl "小凉，要不我们也来帮忙吧？"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140410.ogg"
    rxl "毕竟还要到小学那头去调查......小凉一个人的话会很困难吧？"
    show rxl_dzf_b1 b1 b1_h1
    play voice "voice/日向怜/0140420.ogg"
    rxl "而且，人多的话一定能更快找到的。"
    me01 "抱歉，帮大忙了。"
    hide rxl_dzf_b1
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_h1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/0533250.ogg"
    lingyin "如果日向同学要帮忙的话，也请让我也一起加入吧。"
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_h1 onlayer m2:
        xpos 0.5
    show yczs_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(0, -200, 600, duration=1.5)
    pause 0.5 hard
    play voice "voice/一诚总司/1606240.ogg"
    yczs "我的话虽然什么忙都帮不上，但是还是会给你们加油的。"
    me01 "你和你手里的相机不要惹麻烦就行了。"
    show yczs_dzf_b1 b1 b1_h1
    play voice "voice/一诚总司/1606250.ogg"
    yczs "不必担心，毕竟幼女又不是什么超自然现象。"
    hide yczs_dzf_b1
    hide lingyin_dzf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140430.ogg"
    rxl "小凉，要不今天就开始行动吧？"
    me01 "说的也是，在放学之前就先思考下对策吧。"
    hide rxl_dzf_b2
    show rxl_dzf_b1 b1 b1_n3 onlayer m2:
        xpos 0.5
    play voice "voice/日向怜/0140440.ogg"
    rxl "那放学后的天协活动，就是大家一起去找观景台的女孩~"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 2.0 hard

label day08.library_event01:
    play sound rill
    scene set only school day road yinghua
    with dissolve
    pause 2.0 hard
    "虽然依旧是什么都想不起来，但总觉得能够依靠肌肉记忆碰碰运气。"
    "所谓的“肌肉记忆”就是残留在人体内的潜意识电信号。"
    "这种信号不像神经传感是受大脑控制的，因此很难察觉到。"
    "但要是能通过一些外界的刺激强化反馈，说不定就能找到一些线索。"
    pause 1.0 hard
    play music first_05 fadein 3.0 if_changed
    scene set only school day library yinghua
    with dissolve
    pause 1.0 hard
    "第一个想到的地方就是樱华校的图书馆了。"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dzf_b2 b2 b2_n1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533360.ogg"
    lingyin "这是第二次来樱华校图书馆看毕业相册了呢。"
    show lingyin_dzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0533370.ogg"
    lingyin "虽然七月份的时候，我并不知道神野同学为什么要调查学生名册。"
    play voice "voice/青木铃音/0533380.ogg"
    lingyin "但是这一次，我会祈祷你能够找到的。"
    me01 "谢谢你铃音同学。"
    hide lingyin_dzf_b2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 1.0 hard
    "当时为了寻找雷亚的线索也是翻遍了图书馆的毕业相册。"
    "不过这一次不同，要找的目标是谁连我自己也不知道。"
    "只能期待奇迹发生了......"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b2 b2 b2_n1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/日向怜/0140580.ogg"
    rxl "我现在去小学那边调查毕业相册。如果知道了什么的话会用手机联系的。"
    hide rxl_dzf_b2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "日向怜是除我以外唯一一个去过观景台的人。"
    "如果、我是说如果她也见过那个“她”的话，也许就能帮得上忙了。"
    "等等，那天去过观景台的不是还有一个人吗。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show rxl_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.7
    show lingyin_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    me01 "铃音同学，怎么没有看到翔子？她今天请假了吗？"
    show lingyin_dzf_b2 b2 b2_s2
    play voice "voice/青木铃音/0532750.ogg"
    lingyin "是的，参加完学生会的会议后就回去了。"
    me01 "出什么事了？"
    show rxl_dzf_b1 b1 b1_sp1
    play voice "voice/日向怜/0139300.ogg"
    rxl "小翔的伤还没好吗？"
    me01 "受伤了？"
    show lingyin_dzf_b2 b2 b2_s1
    play voice "voice/青木铃音/0532760.ogg"
    lingyin "是的......姐姐在神社帮忙的时候经常会不小心受伤。"
    show lingyin_dzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0532770.ogg"
    lingyin "不过不必担心，父亲也说了今天就能摘掉绷带了。"
    me01 "是这样的话再好不过。"
    show lingyin_dzf_b2 b2 b2_h1
    play voice "voice/青木铃音/0532780.ogg"
    lingyin "是的，所以也不用太过担心。"
    hide rxl_dzf_b1
    show rxl_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0139310.ogg"
    rxl "我从一开始就没有担心的。"
    show lingyin_dzf_b2 b2 b2_h3
    play voice "voice/青木铃音/0532790.ogg"
    lingyin "这样的日向同学我最喜欢了~"
    hide rxl_dzf_b2 with None
    pause 0.1 hard
    show rxl_dzf_b1 b1 b1_sp2 onlayer m2 at flu_down(0.15, 20):
        xpos 0.7
    show tanhao at tanhao_x07 onlayer m2
    play voice "voice/日向怜/0139320.ogg"
    rxl "小翔不在还请不要把我当成百合的对象！"
    hide rxl_dzf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "铃音同学，樱华校的毕业相册能不能拜托你帮忙调查呢？"
    show lingyin_dzf_b2 b2 b2_n1
    play voice "voice/青木铃音/0533420.ogg"
    lingyin "我知道了，那神野同学准备做什么呢？"
    me01 "我想去医院一趟。"
    me01 "毕竟有点在意翔子那边的情况。"
    stop music fadeout 5.0 
    pause 1.0 hard
    scene black 
    with dissolve
    pause 2.0 hard

label day08.hospital_event01:
    $ flcam.move(0, 0, 0)
    scene set only hospital day outside
    with dissolve
    pause 2.0 hard
    scene set only hospital day passwalk
    with dissolve
    pause 1.0 hard
    "现在这个时候医院里的人并不多，但是想要靠自己找人还是没那么容易的。"
    "这里是樱华镇最大的综合医院，听铃音同学说她的父亲就是这里的医生。"
    me01 "应该问谁好呢，真是伤脑筋啊。"
    play voice "voice/护士/2200010.ogg"
    stranger "......请问有什么事吗？"
    play music first_13 fadein 3.0 if_changed
    $ flcam.move(0, -400, 900, duration=1.5)
    pause 0.5 hard
    show nurse_dzf_b1 b1 b1_n1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/护士/2200020.ogg"
    nurse "是来看病的吗？是的话请在那边挂号。"
    me01 "我是来找人的，名字叫青木翔子。"
    show nurse_dzf_b1 b1 b1_sp1
    play voice "voice/护士/2200030.ogg"
    nurse "青木......难道是青木医生的女儿吗？"
    play voice "voice/护士/2200040.ogg"
    nurse "你是青木翔子的朋友吗？"
    me01 "算是吧。"
    show nurse_dzf_b1 b1 b1_n1
    play voice "voice/护士/2200050.ogg"
    nurse "她还真是精力充沛呢。有时候连身为医生的我们都不知道该怎么应付。"
    me01 "那个，青木医生是什么样的人呢？"
    play voice "voice/护士/2200070.ogg"
    nurse "是个很热爱工作的人。"
    show nurse_dzf_b1 b1 b1_h1
    play voice "voice/护士/2200080.ogg"
    nurse "顺带一提，我是他的粉丝~"
    show nurse_dzf_b1 b1 b1_n1
    play voice "voice/护士/2200090.ogg"
    nurse "以后请注意不要在医院里到处闲逛哦~"
    pause 0.5 hard
    show nurse_dzf_b1 b1 b1_n1 at walkout_r(0.5)
    pause 1.5 hard
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "说完她便带着我离开了门诊大厅。"
    pause 1.0 hard
    stop music fadeout 5.0
    $ flcam.move(0, 0, 0)
    scene set only sky day yinghua
    with dissolve
    pause 1.0 hard
    "顺着走廊来到了西区大楼。"
    "和刚刚的接待处不同，这里非常安静。"
    "我们在了三楼的一间病房前停了下来。"
    "门口的牌子上写着“青木翔子”。"
    "护士小姐简单地向我传达了探病的注意事项后便离开了。"
    pause 1.0 hard
    scene black 
    with dissolve
    play sound open_door2
    pause 1.0
    scene set only hospital day room yinghua
    with right2left
    pause 2.0 hard
    "病房是单人间。"
    "并不是特别宽敞。"
    "最里面是一扇很大的窗户。"
    "整体给人一种视野开阔的感觉。"
    pause 1.0 hard
    scene set only xz_cg hsp surprise
    with slowdissolve
    pause 2.5 hard
    play music first_27 fadein 3.0 if_changed
    "女孩半躺在床上。"
    "睡衣的领口露出犹如雪花一般白皙的肌肤，跟房间的白色相比显得更加清澈美丽。"
    "纤细的身材，洁白的秀发。"
    "眼前的女孩并不是翔子，应该说并不是我前些日止见到的那位翔子。"
    "但是总感觉在哪里见过。"
    "女孩身上并没有绑着石膏或者绷带，也没有看出像是受过伤的样子，这一切都不符合铃音的描述。"
    "可是为什么门牌上写的的确翔子的本名。"
    "而且那名护士似乎也不像是在开玩笑的样子。"
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 1.75 alpha 1
    pause 3.0 hard
    scene set only xz_memory piecezero yinghua
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0601630.ogg"
    stranger "想要找我玩的时候就说出来。"
    play voice "voice/翔子/0601640.ogg"
    stranger "因为，我喜欢和你在一起。"
    pause 1.0 hard
    $ flcam.move(-1500, -2000, 600)
    scene set only xz_cg hsp surprise
    with slowdissolve
    pause 2.0 hard
    play voice "voice/翔子/0601650.ogg"
    stranger "......诶？"
    "她惊讶地看向我。"
    "彼此的目光在此刻交汇在了一起。"
    pause 1.0 hard
    show white onlayer texture:
        additive 1
        alpha 0
        0.25
        linear 1.75 alpha 1
    pause 3.0 hard
    $ flcam.move(0, 0, 0)
    scene set only xz_memory piecezero yinghua
    with dissolve
    pause 1.0 hard
    play voice "voice/翔子/0601660.ogg"
    stranger "那我们约好了。"
    play voice "voice/翔子/0601670.ogg"
    stranger "我们一定要再次相见。"
    play voice "voice/翔子/0601680.ogg"
    stranger "一定要在这座观景台再次相见。"
    play voice "voice/翔子/0601690.ogg"
    stranger "就像牛郎和织女那样，即使暂时分开了到最后也一定要再次相遇！"
    play voice "voice/翔子/0601710.ogg"
    stranger "然后结婚，对我唯命是从！"
    pause 1.0 hard
    $ flcam.move(-1500, -2000, 600)
    scene set only xz_cg hsp surprise
    with slowdissolve
    pause 2.0 hard
    play voice "voice/翔子/0601720.ogg"
    stranger "你是？"
    "果然是她！"
    "那接近亿万分之一的奇迹发生了。我的肌肉记忆告诉我，眼前的女孩和我失去的记忆有关系。"
    "在我被雷亚收割噩梦的那晚之后，我就再也没有过这样的感觉了。"
    "她就是我要找的，观景台的“她”。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    $ flcam.move(0, 0, 0, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0601730.ogg"
    stranger "吓了一跳啊......嗯，吓了一跳。"
    play voice "voice/翔子/0601740.ogg"
    stranger "怎么突然就闯进来了。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0601750.ogg"
    stranger "你就是......神野凉君？"
    me01 "是、是的。"
    play voice "voice/翔子/0601760.ogg"
    stranger "我从青木医生那里听说的。啊对了，青木医生就是我的主治医生。"
    play voice "voice/翔子/0601780.ogg"
    stranger "你是来探望我的吧？"
    "我点了点头。"
    "虽说是这么回事，但却也并不是。"
    "如果眼前的女孩就是观景台的“她”，那我之前遇到的翔子又是怎么回事？"
    "那个陪我度过了学校、海滩、庆典，陪我去过观景台的翔子又是谁呢？"
    "可如今这种感觉又是如此的真实，当年与我在观景台许下约定的人就是眼前的女孩没错。"
    "这世上怎么可能同时存在两个具有相同记忆的人。"
    "虽然也可能存在平行时空这一说法，但是想要观测到位于不同时空的同一个体显然是不符合科学常识的。"
    "根据{encyclopedia=xuedinge}薛定谔的猫{/encyclopedia}的解释，在“观测”这一行为确定实施之前，任何因果逻辑都是具有不确定性的。"
    "根据现在的结果推断，此时两位翔子之中一定有一位是因为某种契机而被我偶然“观测”到的。"
    "也就是说此时的两人正处在一种相互纠缠、而又具有独立自主意识的量子纠缠态。"
    "本来这一切都是理论上存在的东西，可雷亚的出现让我重新对这一切有了新的认知。"
    "此刻多么离奇的假设都是有可能成立的。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0601790.ogg"
    stranger "果然是这样，谢谢你了~"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0601800.ogg"
    stranger "坐吧。那边的椅子都是可以用的。"
    "我用机器般生硬的动作照办了。"
    "比起我而言对方显得格外地自然。"
    "似乎一点也不抗拒我这个陌生人的突然造访。"
    pause 0.1 hard
    scene set only xz_cg hsp happy
    with dissolve
    play voice "voice/翔子/0601810.ogg"
    stranger "我到这座医院之后，还是第一次有人来探望我呢。"
    play voice "voice/翔子/0601820.ogg"
    stranger "所以该说是有些高兴，还是有些害羞呢。总有种奇怪的感觉。"
    me01 "那个......"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0601830.ogg"
    stranger "嗯？"
    me01 "虽然很突然，但是你记得我吗？"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0601850.ogg"
    stranger "诶？"
    me01 "我们以前应该是见过面的，你记得吗？"
    play voice "voice/翔子/0601860.ogg"
    stranger "那个......"
    me01 "小时候，那是在我们小的时候。"
    me01 "就在这座樱华镇，我们都是彼此最重要的玩伴。"
    play voice "voice/翔子/0601870.ogg"
    stranger "玩伴？"
    me01 "还记得观景台吗？"
    play voice "voice/翔子/0601880.ogg"
    stranger "观景台是？"
    me01 "就在山坡上的那座。"
    play voice "voice/翔子/0601890.ogg"
    stranger "山坡上，你是指学校的方向吗？"
    me01 "没错！"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0601900.ogg"
    stranger "原来那里还有座观景台啊。"
    me01 "你果然也......忘记了吗？"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0601910.ogg"
    stranger "忘记了是指？"
    "虽然这一切都在我的意料之中，但多少还是有些失落。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0601920.ogg"
    stranger "说起来，我还没有问你呢。"
    play voice "voice/翔子/0601930.ogg"
    stranger "你为什么会来探望我呢？"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0601940.ogg"
    stranger "我和你是今天第一次......"
    me01 "从现在算起的七年前。"
    "我打断了她的话。"
    me01 "七年前的我还住在这座小镇上。"
    pause 0.1 hard
    scene set only xz_cg hsp normal
    with dissolve
    play voice "voice/翔子/0601950.ogg"
    stranger "这样啊。"
    me01 "但因为家里的原因我最后还是离开了。"
    play voice "voice/翔子/0601960.ogg"
    stranger "呼嗯。"
    me01 "但是现在我又回来了。"
    play voice "voice/翔子/0601970.ogg"
    stranger "呼嗯。"
    me01 "而回来以后的第一件事就是去见你。"
    pause 0.1 hard
    scene set only xz_cg hsp surprise
    with dissolve
    play voice "voice/翔子/0601980.ogg"
    stranger "......"
    me01 "你真的，什么都不记得了吗？"
    me01 "那时的我们不是在观景台做过约定的吗？"
    me01 "七夕那天，我们不是一起发过誓的吗？"
    me01 "说我们一定会再见面的。"
    me01 "再次见面，然后......"
    stop music fadeout 5.0
    pause 0.1 hard
    scene set only xz_cg hsp daze
    with dissolve
    play voice "voice/翔子/0602000.ogg"
    stranger "我想大概是你认错人了。"
    $ flcam.move(-1500, -2000, 600, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/翔子/0602010.ogg"
    stranger "因为，我也是不久前才刚搬到这座医院来。"
    pause 0.1 hard
    scene set only xz_cg hsp sad
    with dissolve
    play voice "voice/翔子/0602020.ogg"
    stranger "樱华镇，我也是第一次来的。"
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day08.hospital_event02:
    $ flcam.move(0, 0, 0)
    scene set only hospital evening passwalk
    with dissolve
    pause 2.0 hard
    "离开了病房，我失落地徘徊在走廊上。"
    "虽然知道自己凭借不确定的线索就这样断言着实有些草率。"
    "但那种感觉总有它存在的意义。"
    play voice "voice/翔子/0232000.ogg"
    stranger "在干什么呢，那边的可疑之人。"
    play music first_14 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_a1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    me01 "为什么我就成了可疑之人了？"
    show xz_dzf_b2 b2 b2_n2
    play voice "voice/翔子/0232010.ogg"
    xz "你难道不是在医院踩点，好为之后的“犯罪”做准备吗？"
    me01 "别乱说，我可是特地来找你的。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232020.ogg"
    xz "那就好好待在接待室啊，这不是让我到处找吗。"
    me01 "那是因为......我很闲啊。"
    "另一位翔子的事情还是暂时不要告诉她的好。"
    "毕竟连我都没有搞清楚是怎么回事。"
    "冒然干涉量子领域是很危险的行为。"
    show xz_dzf_b3 b3 b3_n2
    play voice "voice/翔子/0232030.ogg"
    xz "你是因为很闲才来探望我的吧？"
    me01 "当然不是。比起这个绷带摘掉了吗？"
    hide xz_dzf_b3
    show xz_dzf_b2 b2 b2_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232040.ogg"
    xz "嗯。虽然还算不上痊愈，不过总算可以摆脱那个不自在的状态了。"
    me01 "之后只要上点药就行了吧？"
    hide xz_dzf_b2
    show xz_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232050.ogg"
    xz "是啊。所以还得去药房一趟。"
    me01 "这座医院是分为中央大楼和西区大楼对吧？"
    show xz_dzf_b1 b1 b1_sp1
    play voice "voice/翔子/0232060.ogg"
    xz "是的。虽然中间是有连通的走廊可以通过的。"
    me01 "这是樱华镇唯一的一家医院吗？"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232080.ogg"
    xz "我也不知道，毕竟也没去过其他的医院。"
    hide xz_dzf_b2
    stop music fadeout 5.0
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    "取药的地方位于中央大楼的一楼。"
    "一般的门诊和外科治疗都在那里，翔子她刚才想必也是在那里接受治疗的吧。"
    "特地来西区大楼单纯是为了找我吗？"
    "还是说......"
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    me01 "西区大楼这边都住着些什么样的病人呢？"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232100.ogg"
    xz "平面图上不是写着吗？"
    me01 "还没来得及仔细看就被翔子你叫住了。"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    xz "......"
    show xz_dzf_b3 b3 b3_n2
    play voice "voice/翔子/0232120.ogg"
    xz "西区大楼里的大都是长期住院的患者，一般都是身患重病之人。所以还是不要随意闯入比较好。"
    pause 1.0 hard
    scene black
    with dissolve
    pause 2.0 hard
    $ flcam.move(0, 0, 0)
    scene set only hospital evening outside
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/翔子/0232320.ogg"
    xz "啊啦，这么快就来了，真让人意外啊。"
    pause 0.5 hard
    play music first_25 fadein 3.0 if_changed
    show lingyin_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533520.ogg"
    lingyin "我以为两位会一直到傍晚才出来的。"
    me01 "辛苦你了，铃音同学。"
    show xz_dzf_b1 b1 b1_h2
    play voice "voice/翔子/0232330.ogg"
    xz "嘛，有些事情耽误了。"
    play voice "voice/青木铃音/0533530.ogg"
    lingyin "虽然姐姐也说了，让我如果太晚的话就先回去。"
    hide xz_dzf_b1
    hide lingyin_dsf_b2
    $ flcam.move(-2250, -500, 1100, duration=1.5)
    pause 0.5 hard
    "我回头看向医院。"
    "靠海的方位就是西区大楼，因此在正门的地方看得不是很清楚。"
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    show xz_dzf_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    show lingyin_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    me01 "抱歉，能问二位一些事情吗？"
    show xz_dzf_b1 b1 b1_n2
    show lingyin_dsf_b2 b2 b2_n2
    play voice "voice/青木铃音/0533550.ogg"
    lingyin "什么事？"
    me01 "医院每年都会有很多病人搬过来吗？"
    hide xz_dzf_b1
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232350.ogg"
    xz "是这么听说的。"
    play voice "voice/青木铃音/0533560.ogg"
    lingyin "今年七月刚转来了一批，父亲是这么说的。"
    me01 "能查到对方入院前都在哪里吗？"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_n2 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232370.ogg"
    xz "这个问父亲的话应该可以知道的吧。"
    hide lingyin_dsf_b2
    show lingyin_dsf_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0533570.ogg"
    lingyin "发生什么事了吗？"
    me01 "有一点。"
    hide lingyin_dsf_b1
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0232380.ogg"
    xz "你的脸色看上去不像是只有一点啊。"
    me01 "......"
    hide xz_dzf_b3
    show xz_dzf_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232390.ogg"
    xz "到底怎么了？"
    pause 0.5 hard
    show lingyin_dsf_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/青木铃音/0533580.ogg"
    lingyin "姐姐，刨根问底是......"
    show xz_dzf_b2 b2 b2_s1
    play voice "voice/翔子/0232400.ogg"
    xz "是恶趣味吧。虽然我也没有打算强行逼问出来。"
    show xz_dzf_b2 b2 b2_n2
    play voice "voice/翔子/0232410.ogg"
    xz "但是稍微商量一下的话不也挺好吗？"
    play voice "voice/青木铃音/0533590.ogg"
    lingyin "作为朋友的立场吗？"
    hide xz_dzf_b2
    show xz_dzf_b3 b3 b3_s1 onlayer m2:
        xpos 0.5
    play voice "voice/翔子/0232420.ogg"
    xz "作为学生会的伙伴。"
    show lingyin_dsf_b1 b1 b1_n1
    play voice "voice/青木铃音/0533600.ogg"
    lingyin "毕竟我们大家既是同伴，也是朋友呢~"
    me01 "谢谢你们。"
    show xz_dzf_b3 b3 b3_n2
    play voice "voice/翔子/0232430.ogg"
    xz "无须多礼，不要犹豫来跟我们商量商量吧。"
    me01 "可以留到下次吗？"
    hide xz_dzf_b3
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    "翔子耸了耸肩。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening yinghua2
    with dissolve
    pause 1.0 hard
    "如果只是我一个人才能观测到的异样倒也罢了，可是现实中的其他人又是如何看待另一位翔子的存在呢？"
    "还有一点，按照铃音她们的说法，病人是从七月份才转移过来的，也就是说和我搬回来的时间基本一致。"
    "这之间会有什么联系吗？"
    "在西区大楼里见到的翔子似乎也不认识我。"
    "可是看她的反应又不像是第一次见面的样子。"
    "依照现在的线索推测最有可能的只有两种情况。一是她在隐瞒“认识我”这个事实，再者就是......她也是雷亚镰刀下的“受害者”。"
    pause 1.0 hard
    $ flcam.move(4500, -200, 600)
    scene set only hospital evening outside
    show lingyin_dsf_b2 b2 b2_n1 onlayer m2:
        xpos 0.7
    with right2left
    pause 1.0 hard
    play voice "voice/青木铃音/0533610.ogg"
    lingyin "如果还有其他需要帮忙的话，随时都可以来找我商量哟~"
    me01 "我喜欢你，铃音同学。"
    $ flcam.move(4500, -300, 900, duration=1.5)
    show lingyin_dsf_b2 b2 b2_a1 onlayer m2 at flu_down(0.15, 30):
        xpos 0.7
    play voice "voice/青木铃音/0533620.ogg"
    lingyin "嘿！"
    $ flcam.move(0, -100, 400, duration=0.5)
    hide lingyin_dsf_b2
    play sound hite_3
    show lingyin sd3 onlayer b2 at basicfade_c2u:
        xpos 0.175
        zoom 1.3
    with vpunch
    "被手刀劈了。"
    hide lingyin sd3
    pause 1.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dsf_b2 b2 b2_h1 onlayer m2:
        xpos 0.7
    play voice "voice/青木铃音/0533630.ogg"
    lingyin "不用那些奇怪的套路，普普通通地来找我商量吧~"
    pause 0.5 hard
    show xz_dzf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    $ flcam.move(2250, -350, 750, duration=1.5)
    pause 0.5 hard
    play voice "voice/翔子/0232460.ogg"
    xz "......比起铃音你刚才的话更让我惊讶啊！"
    hide lingyin_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    me01 "翔子。"
    show xz_dzf_b2 b2 b2_sp2
    play sound punch
    show wflash onlayer f1
    with vpunch
    "{size=72}咚嗙！！！{/size}"
    play voice "voice/翔子/0232470.ogg"
    xz "我、我我我我才不需要那样的道谢！"
    me01 "我还什么都没说吧？！"
    pause 1.0 hard
    stop music fadeout 2.0
    scene black
    with slowdissolve
    pause 2.0 hard

label day08.starview_event01:
    play ambience1 zhiliao
    $ flcam.move(0, 0, 0)
    scene set only starview night road
    with dissolve
    pause 2.0 hard
    scene set only starview night starview
    with dissolve
    pause 2.0 hard
    $ flcam.move(2250, -200, 600, duration=1.5)
    pause 0.5 hard
    "虽说没抱多大希望能够见到雷亚。"
    "但在我刚踏入观景台的那一刻，就能隐约看到围栏上那熟悉的身影。"
    "这是我几天以来第一次见到这位死神少女。"
    me01 "呐，雷亚。"
    stop ambience1 fadeout 2.0
    pause 2.0 hard
    play music first_42 fadein 3.0 if_changed
    $ flcam.move(0, 0, 0)
    scene set only lisite_cg angry
    with dissolve
    play voice "voice/天使雷亚/0016130.ogg"
    lst "什么事，喷喷。"
    me01 "别随便起绰号啊。"
    play voice "voice/天使雷亚/0016140.ogg"
    lst "那，笨笨。"
    me01 "你好像心情不太好的样子。"
    play voice "voice/天使雷亚/0016150.ogg"
    lst "也没有心情不好。"
    me01 "是在生我的气吗？"
    pause 0.1 hard
    scene set only lisite_cg surprise
    with dissolve
    play voice "voice/天使雷亚/0016160.ogg"
    lst "为什么这么说？"
    me01 "因为我记起观景台的“她”了。"
    play voice "voice/天使雷亚/0016170.ogg"
    lst "观景台的“她”是指谁？"
    me01 "青木翔子。"
    pause 0.1 hard
    scene set only lisite_cg daze
    with dissolve
    play voice "voice/天使雷亚/0016180.ogg"
    lst "......"
    play voice "voice/天使雷亚/0016190.ogg"
    lst "是吗。"
    me01 "我今天见到她了。"
    pause 1.0 hard
    scene set only starview night starview
    with dissolve
    pause 0.5 hard
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016200.ogg"
    lst "但是你好像不是很高兴。"
    show ts_lst_ssz_b1 b1 b1_n2
    play voice "voice/天使雷亚/0016210.ogg"
    lst "你不是一直都想见她的吗？"
    show ts_lst_ssz_b1 b1 b1_a1
    play voice "voice/天使雷亚/0016220.ogg"
    lst "凉君你......不是一直都很在乎她的吗？"
    "雷亚从围栏上跳了下来，一步步朝我走来。"
    "最后在很近的距离停下脚步抬头看着我。"
    stop music fadeout 5.0
    $ flcam.move(0, -350, 1000, duration=1.5)
    show ts_lst_ssz_b1 b1 b1_sp1
    "我顺势抱住了她。"
    play voice "voice/天使雷亚/0016230.ogg"
    lst "......"
    play voice "voice/天使雷亚/0016240.ogg"
    lst "............"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016250.ogg"
    lst "不......"
    play sound liandao
    $ flcam.move(0, -100, 400, duration=1.5)
    show ts_lst_ssz_b2 b2 b2_sp2 at flu_down(0.15, 30):
        xpos 0.5
    play voice "voice/天使雷亚/0016260.ogg"
    lst "不要！！"
    play sound punch
    show wflash onlayer f1
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b2_d b2 b2_a1 onlayer m2:
        xpos 0.5
    with vpunch
    "{size=72}咚！！！{/size}"
    pause 0.5 hard
    me01 "好痛！"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_a2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016270.ogg"
    lst "你、你在干什么啊！"
    $ flcam.move(0, 0, 900, duration=1.5)
    show ts_lst_ssz_b1_d b1 b1_sp1
    me01 "只是想抱抱你而已。"
    $ flcam.move(0, -200, 600, duration=1.5)
    play sound punch
    show wflash onlayer f1
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_a1 onlayer m2:
        xpos 0.5
    with vpunch
    "{size=72}咚！！！{/size}"
    me01 "那个柄尖打人很痛的。"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_a2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016280.ogg"
    lst "吵死了变态君！"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky night yinghua2
    with dissolve
    pause 1.0 hard
    "明知会被打却还是照做了，这也恰好说明了我受到的打击有多么大。"
    "因为“她”已经忘了我。"
    "一切都是我的自作多情罢了。"
    pause 1.0 hard
    $ flcam.move(0, 0, 900)
    play music first_42 fadein 3.0 if_changed
    scene set only starview night starview
    show ts_lst_ssz_b1_d b1 b1_s2 onlayer m2:
        xpos 0.5
    with dissolve
    play voice "voice/天使雷亚/0016290.ogg"
    lst "今晚的你真是笨笨笨笨的呢。"
    "追加到四个了。"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0016300.ogg"
    lst "在你转身的时候就刺下去好了。"
    me01 "是我不好，还请千万不要这么做。"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016310.ogg"
    lst "凉君，是因为跟她见面所以兴奋过度了吗？"
    me01 "我觉得恰好是完全相反。"
    show ts_lst_ssz_b2_d b2 b2_s3
    play voice "voice/天使雷亚/0016320.ogg"
    lst "伤心吗？"
    me01 "大概是的。"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016330.ogg"
    lst "是我的错？"
    me01 "不是的。"
    show ts_lst_ssz_b1_d b1 b1_sp1
    play voice "voice/天使雷亚/0016340.ogg"
    lst "那......是她的错？"
    me01 "也不是。"
    "先是兴奋而又期待，而后又自顾自地消沉，这些都是因为我的咎由自取。"
    me01 "“她”已经，不记得我了。"
    show ts_lst_ssz_b1_d b1 b1_s2
    play voice "voice/天使雷亚/0016350.ogg"
    lst "......"
    me01 "我真傻。"
    me01 "一个人擅自去期待那些根本不存在的情节。"
    play voice "voice/天使雷亚/0016360.ogg"
    lst "......"
    me01 "到头来也只是白忙活一场。"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0016370.ogg"
    lst "......"
    me01 "见到你的第一眼我就觉得，雷亚你和“她”长得真像。"
    me01 "和小时候的翔子，几乎是一模一样的。"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016390.ogg"
    lst "所以，你才会很期待吗？"
    play voice "voice/天使雷亚/0016400.ogg"
    lst "因为我和“她”长得很像，并且也与凉君相遇了。"
    show ts_lst_ssz_b2_d b2 b2_n2
    play voice "voice/天使雷亚/0016410.ogg"
    lst "所以才没有放弃吗？"
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016420.ogg"
    lst "才会认为你们是能够再见面的。"
    play voice "voice/天使雷亚/0016430.ogg"
    lst "才会认为，“她”也能记得凉君你的。"
    me01 "也许吧。"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0016440.ogg"
    lst "......"
    me01 "不高兴吗？"
    show ts_lst_ssz_b1_d b1 b1_s1
    play voice "voice/天使雷亚/0016450.ogg"
    lst "才不是。"
    me01 "我说了什么让你不开心的话吗？"
    hide ts_lst_ssz_b1_d
    show ts_lst_ssz_b2_d b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016460.ogg"
    lst "嗯。"
    me01 "我说了什么？"
    show ts_lst_ssz_b2_d b2 b2_s4
    play voice "voice/天使雷亚/0016470.ogg"
    lst "......笨笨的。"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    hide ts_lst_ssz_b2_d
    show ts_lst_ssz_b1_d b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/0016480.ogg"
    lst "也许，我也说了不好的话。"
    me01 "我不太明白。"
    show ts_lst_ssz_b1_d b1 b1_n2
    play voice "voice/天使雷亚/0016500.ogg"
    lst "不明白就好。"
    show ts_lst_ssz_b1_d b1 b1_s3
    play voice "voice/天使雷亚/0016510.ogg"
    lst "因为这不是和你。"
    play voice "voice/天使雷亚/0016520.ogg"
    lst "而是我与“她”之间的约定——"
    pause 2.0 hard
    stop music fadeout 5.0
    $ flcam.move(0, 0, 0)
    scene black
    with slowerdissolve
    $ suppress_overlay = True
    jump day09
