
label day225:
    bookmark
    $ save_name = _("Day 225")
    pause 4.0 hard
    $ flcam.move(0, 0, 0)
    scene set only backend_xuejian second
    with dissolve
    show backend_date224 onlayer m1 at backend_date2
    pause 5.0 hard
    scene black
    with dissolve
    pause 3.0 hard
    $ suppress_overlay = False
    scene set only sky day xuejian2
    with slowdissolve
    pause 1.0 hard
    "持续积攒的疲劳光靠睡眠还是无法彻底消除。"
    "早上起来之后我感觉全身酸痛。"
    "在弗兰小姐和立花老师的帮助下，我总算是找回了自己一直在寻找的羁绊。"
    "当然这一切自然也少不了希菲尔的帮助。"
    "总而言之眼下还有一大堆的事情要去做。"
    "那么首先......"
    pause 1.0 hard
    scene black
    with slowdissolve
    pause 1.0 hard
    $ _overworld_label = 'day225'
    $ seen_day225_store_event01 = False
    $ seen_day225_balltower_event01 = False


label day225.map:
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play music suiro fadein 5.0 if_changed
    scene black
    scene onlayer screens
    with None
    play sound map_out
    show set maps winter day
    if _overworld_label == 'day225':
        $ flcam.move(*overworld.camera_positions['road1'])
    elif _overworld_label == 'day225.store_event01':
        $ flcam.move(*overworld.camera_positions['road2'])
    elif _overworld_label == 'day225.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'])
    $ flcam.move(0, 0, 0, duration=6.0, x_express=map_xy_express(6.0), y_express=map_xy_express(6.0))
    with dissolve
    pause 2.5 hard
    $ _window_animation = 'in'
    window mode map
    me01 "接下来应该去哪里呢......" nointeract
    call screen rughzenhaide(
        road2=("day225.store_event01", "not seen_day225_store_event01"),
        cloqks=("day225.balltower_event01", "seen_day225_store_event01 and not seen_day225_balltower_event01"))
    $ window_animate_outro()
    if _return == 'day225.store_event01':
        $ flcam.move(*overworld.camera_positions['road2'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    elif _return == 'day225.balltower_event01':
        $ flcam.move(*overworld.camera_positions['cloqks'], duration=3.0, warper='easeout_cubic')
        with Pause(2.0)
        scene black with dissolve
    $ _window_animation = None
    stop music fadeout 3.0
    pause 3.0 hard
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True
    jump expression _return

label day225.store_event01:
    $ flcam.move(0, 0, 0)
    play ambience1 jiaobu2 fadein 3.0
    scene set only lisite_cg street normal
    play music first_41 fadein 3.0 if_changed
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/000189.ogg"
    lst "所以现在要去哪里？"
    me01 "这个嘛，找家咖啡店怎么样？"
    play voice "voice/天使雷亚/000190.ogg"
    lst "死神才不会去咖啡店呢。"
    me01 "别这么说嘛，再考虑一下？"
    play voice "voice/天使雷亚/000191.ogg"
    lst "去咖啡店做什么？"
    me01 "应该就是喝个咖啡吧。"
    pause 0.1 hard
    scene set only lisite_cg street angry
    with dissolve
    play voice "voice/天使雷亚/000192.ogg"
    lst "死神才不会喝咖啡呢。"
    me01 "很好喝的，尝尝看如何？"
    pause 0.1 hard
    scene set only lisite_cg street normal
    with dissolve
    play voice "voice/天使雷亚/000193.ogg"
    lst "......是吗？"
    pause 0.1 hard
    scene set only lisite_cg street happy
    with dissolve
    play voice "voice/天使雷亚/000194.ogg"
    lst "那我也要和凉君一样享受轻松的氛围。"
    me01 "你就好好期待吧~"
    pause 0.1 hard
    scene set only lisite_cg street normal
    with dissolve
    play voice "voice/天使雷亚/000195.ogg"
    lst "说起来，天协那边怎么样了？"
    me01 "嘛......毕竟之后离开樱华校就没再打听过了。"
    play voice "voice/天使雷亚/000196.ogg"
    lst "为什么？"
    me01 "现在的后辈们都是我们精心考核的人才，所以应该没什么问题的吧。"
    play voice "voice/天使雷亚/000197.ogg"
    lst "考核？"
    me01 "知道什么是考核吗？"
    pause 0.1 hard
    scene set only lisite_cg street angry
    with dissolve
    play voice "voice/天使雷亚/000198.ogg"
    lst "别把我当成笨蛋，虽然死神是不会参加考核的。"
    me01 "话说回来......这个季节很难看到星星呢。"
    pause 0.1 hard
    scene set only lisite_cg street normal
    with dissolve
    play voice "voice/天使雷亚/000200.ogg"
    lst "因为会下雪？"
    me01 "差不多吧。"
    play voice "voice/天使雷亚/000201.ogg"
    lst "凉君你会冷吗？"
    me01 "有一点。"
    play voice "voice/天使雷亚/000202.ogg"
    lst "所以才没有去看星星？"
    me01 "不是因为这样......只是想看也没有办法看到而已。"
    play voice "voice/天使雷亚/000203.ogg"
    lst "明明之前到了晚上就说要和我一起看星星的。"
    me01 "这个我可没有忘记。"
    pause 0.1 hard
    scene set only lisite_cg street angry
    with dissolve
    play voice "voice/天使雷亚/000204.ogg"
    lst "可是，你刚才说了很难做到。"
    me01 "如果想看的话总会有办法的，人类就是这样特别的生物嘛。"
    pause 0.1 hard
    scene set only lisite_cg street normal
    with dissolve
    play voice "voice/天使雷亚/000206.ogg"
    lst "特别？"
    me01 "依靠人类的智慧，即使是在白天也能够看到星星的。"
    play voice "voice/天使雷亚/000207.ogg"
    lst "......是吗？"
    me01 "是啊。"
    me01 "所以想看星星的话随时都可以告诉我。"
    pause 0.1 hard
    scene set only lisite_cg street happy
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/000210.ogg"
    lst "那么作为交换，凉君觉得冷的话就由我来让你暖和起来。"
    me01 "真的吗？"
    play voice "voice/天使雷亚/000211.ogg"
    lst "嗯~"
    me01 "要怎么做？"
    pause 0.1 hard
    scene set only lisite_cg street angry
    with dissolve
    play voice "voice/天使雷亚/000212.ogg"
    lst "......笨笨的。"
    stop music fadeout 5.0
    stop ambience1 fadeout 3.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 2.0 hard
    scene set only street day city2 xuejian
    with slowdissolve
    pause 1.0 hard
    "也许是因为第一次来这么多人的地方，惊慌的雷亚躲到了我的身后。"
    "由于是休息日，这里的人流量比之前更多了。"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_sp1 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    play voice "voice/天使雷亚/000213.ogg"
    lst "咖啡店门口挂着临时工招聘的牌子。"
    play music second_107 fadein 3.0 if_changed
    me01 "雷亚你知道女仆吗？"
    show ts_lst_ssz_b2 b2 b2_ga1
    play voice "voice/天使雷亚/000214.ogg"
    lst "就算你这么问我......"
    me01 "总之先进去看看吧。"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/000215.ogg"
    lst "那么，我这就和凉君进去放松放松~"
    pause 0.5 hard
    play sound hide_sound
    show ts_lst_ssz_b1 b1 b1_n1 at walkout_l(0.5)
    pause 0.5 hard
    hide ts_lst_ssz_b1
    "雷亚说着就从门口的挡风玻璃中穿了过去。"
    "死神的话这种事情还是能够做得到的啊。"
    "话说......"
    $ flcam.move(-4500, -800, 1100, duration=1.5)
    pause 0.5 hard
    me01 "喂，等等！"
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b3 b3 b3_sp1 onlayer m2 at walkin_l(0.5)
    pause 0.5 hard
    play voice "voice/天使雷亚/000216.ogg"
    lst "怎么了？"
    me01 "还是正常地从正门进去比较好。"
    hide ts_lst_ssz_b3
    show ts_lst_ssz_b2 b2 b2_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/天使雷亚/000218.ogg"
    lst "可是，好像没有被人发现的样子。"
    me01 "那也不能用这种方法，太招摇了吧。"
    show ts_lst_ssz_b2 b2 b2_h1
    play voice "voice/天使雷亚/000219.ogg"
    lst "没有人的地方我比较喜欢~"
    me01 "雷亚还是一如既往地怕生啊。"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/000220.ogg"
    lst "......才没有那回事。"
    me01 "还是说其实是因为想和我单独相处？"
    $ flcam.move(0, 0, 1000, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_s2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/天使雷亚/000221.ogg"
    lst "笨、笨蛋！"
    stop music fadeout 5.0
    pause 1.0 hard
    play voice "voice/日向怜/020036.ogg"
    stranger "诶，凉君？"
    hide ts_lst_ssz_b2
    $ flcam.move(4500, -300, 900, duration=1.5)
    play music first_06 fadein 3.0 if_changed
    pause 0.5 hard
    show rxl_npz_b1 b1 b1_sp1 onlayer m2 at walkin_r(0.7)
    pause 0.5 hard
    play voice "voice/日向怜/020037.ogg"
    rxl "还有雷亚也在~"
    me01 "日向同学，你怎么在这里？"
    hide rxl_npz_b1
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b3 b3 b3_s1 onlayer m1:
        xpos 0.5
    play voice "voice/天使雷亚/000222.ogg"
    lst "......不能和凉君独处了。"
    hide ts_lst_ssz_b3
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/040100.ogg"
    lingyin "神野同学......（小声）"
    play voice "voice/青木铃音/040101.ogg"
    lingyin "那天晚上被我袭击的事情难道你忘记了吗？（小声）"
    me01 "放心吧，我有分寸的。"
    show lingyin_dsf_b2 b2 b2_sp1
    play voice "voice/青木铃音/040102.ogg"
    lingyin "可是雷亚她这不是比起以前现身得更频繁了吗？"
    me01 "......我会反省的。"
    me01 "总之如果发生什么事的话我会保护好她的。"
    show lingyin_dsf_b2 b2 b2_ga3
    play voice "voice/青木铃音/040103.ogg"
    lingyin "请不要太勉强。"
    me01 "还是谢谢你的提醒了。"
    show lingyin_dsf_b2 b2 b2_n1
    play voice "voice/青木铃音/040104.ogg"
    lingyin "要是出了什么事的话，还请立刻通知我们。"
    me01 "嗯，我知道了。"
    hide lingyin_dsf_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b2 b2 b2_ga1 onlayer m1:
        xpos 0.5
    play voice "voice/天使雷亚/000223.ogg"
    lst "......偷偷摸摸地说着悄悄话。"
    me01 "什么事也没有。嗯，什么事也没有。"
    hide ts_lst_ssz_b2 with None
    pause 0.1 hard
    show ts_lst_ssz_b3 b3 b3_ga1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/天使雷亚/000224.ogg"
    lst "......不仅如此还打算用摸头来蒙混过去。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show rxl_npz_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0109880.ogg"
    rxl "了不起了不起，进来吃点东西吧？"
    pause 1.0 hard
    scene black 
    with right2left_02
    pause 1.0 hard

label day225.store_event02:
    play sound shop_rill
    $ flcam.move(0, 0, 0)
    scene set only store day coffee_room yinghua
    with right2left_02
    pause 1.0 hard
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_npz_b1 b1 b1_n3 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/0109890.ogg"
    rxl "来吧不用客气，不会收你钱的。"
    me01 "长得可爱果然可以白吃白喝吗？！"
    show rxl_npz_b1 b1 b1_h1
    play voice "voice/日向怜/0109900.ogg"
    rxl "好啦好啦，快坐快坐~"
    "日向同学一旦化身服务员就挡不住她的那份热情。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show ts_lst_ssz_b3 b3 b3_sp1 onlayer m1:
        xpos 0.5
    play voice "voice/日向怜/020038.ogg"
    rxl "对了雷亚，来这里是有什么事吗？"
    pause 0.5 hard
    play sound hide_sound
    show ts_lst_ssz_b3 b3 b3_s1 at walkout_l(0.5)
    show rxl_npz_b1 b1 b1_sp1
    pause 0.5 hard
    hide ts_lst_ssz_b3
    "听到日向怜的搭话，雷亚迅速躲到了我的身后。"
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    hide rxl_npz_b1
    show rxl_npz_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/020039.ogg"
    rxl "啊哈哈......还是老样子呢~"
    $ flcam.move(0, -300, 750, duration=1.5)
    show lingyin_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.3
    play voice "voice/青木铃音/040105.ogg"
    lingyin "还是说，是因为我的缘故吗？"
    me01 "不是的，怕生是雷亚的天性不是你们的错，对吧雷亚？"
    show ts_lst_ssz_b3 b3 b3_s1 onlayer m1:
        xpos 0.5
    play voice "voice/天使雷亚/000225.ogg"
    lst "我不知道......"
    hide ts_lst_ssz_b3
    hide rxl_npz_b2
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dsf_b2 b2 b2_h1
    play voice "voice/青木铃音/040106.ogg"
    lingyin "难得和神野同学单独出来，就以你们的约会为最优先项目吧。"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show ts_lst_ssz_b2 b2 b2_s2 onlayer m1:
        xpos 0.5
    play voice "voice/天使雷亚/000227.ogg"
    lst "约会......"
    show lingyin_dsf_b2 b2 b2_sp1
    play voice "voice/青木铃音/040107.ogg"
    lingyin "不是这样的吗？"
    show ts_lst_ssz_b2 b2 b2_a1 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/天使雷亚/000228.ogg"
    lst "完全不是。"
    show lingyin_dsf_b2 b2 b2_n2
    play voice "voice/青木铃音/040108.ogg"
    lingyin "我想要为自己赎罪......"
    show ts_lst_ssz_b2 b2 b2_sp1
    play voice "voice/天使雷亚/000229.ogg"
    lst "那是什么？"
    show lingyin_dsf_b2 b2 b2_h1
    play voice "voice/青木铃音/040109.ogg"
    lingyin "意思就是我想要为雷亚你声援哦~"
    hide ts_lst_ssz_b2
    show ts_lst_ssz_b3 b3 b3_s1 onlayer m1:
        xpos 0.5
    play voice "voice/天使雷亚/000230.ogg"
    lst "......"
    me01 "太好了呢，雷亚。"
    hide ts_lst_ssz_b3
    $ flcam.move(-4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show lingyin_dsf_b2 b2 b2_ga1
    play voice "voice/青木铃音/040110.ogg"
    lingyin "真是肮脏......"
    me01 "说好的声援呢！"
    show lingyin_dsf_b2 b2 b2_h1
    play voice "voice/青木铃音/040111.ogg"
    lingyin "我只是代言了所有人的想法而已哟~"
    me01 "这么长时间了我果然还不是铃音同学的对手......"
    hide lingyin_dsf_b2
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show xz_dsf_b1 b1 b1_ga1 onlayer m2:
        xpos 0.5
    xz "......"
    me01 "翔子？！请不要用那种眼神看着我。"
    me01 "还有为什么大家都在啊？"
    hide xz_dsf_b1
    $ flcam.move(4500, -300, 900, duration=1.5)
    pause 0.5 hard
    show rxl_npz_b2 b2 b2_ga1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/020045.ogg"
    rxl "这个嘛，因为店铺经营上的危机所以......啊哈哈。"
    me01 "这么说来之前也看到会长还有水之濑同学在这里打工来着。"
    me01 "既然这样我也来帮忙好了。"
    me01 "毕竟只有你们的话确实太过勉强了。"
    show rxl_npz_b2 b2 b2_a1 at flu_down(0.35, 20):
        xpos 0.7
    play voice "voice/日向怜/020046.ogg"
    rxl "你什么意思啊！"
    hide rxl_npz_b2
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_lst_ssz_b3 b3 b3_ga1 onlayer m1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/天使雷亚/000231.ogg"
    lst "凉君......"
    show ts_lst_ssz_b3 b3 b3_s2
    play voice "voice/天使雷亚/000232.ogg"
    lst "一起放松的事情呢？"
    me01 "抱歉，现在看来不是该放松的时候。"
    hide ts_lst_ssz_b3
    show ts_lst_ssz_b1 b1 b1_s1 onlayer m1:
        xpos 0.5
    play voice "voice/天使雷亚/000233.ogg"
    lst "......"
    show ts_lst_ssz_b1 b1 b1_s2
    play voice "voice/天使雷亚/000234.ogg"
    lst "没什么。"
    me01 "雷亚的话，就在店里找个地方休息一下吧。"
    hide ts_lst_ssz_b1
    show ts_lst_ssz_b2 b2 b2_s4 onlayer m1:
        xpos 0.5
    play voice "voice/天使雷亚/000235.ogg"
    lst "不要。"
    show ts_lst_ssz_b2 b2 b2_n2
    play voice "voice/天使雷亚/000236.ogg"
    lst "既然凉君都在工作，那我也要一起工作。"
    play voice "voice/天使雷亚/000237.ogg"
    lst "这样才算得上一直在一起。"
    me01 "雷亚......谢谢你。"
    show ts_lst_ssz_b2 b2 b2_s4
    play voice "voice/天使雷亚/000238.ogg"
    lst "没什么。"
    $ flcam.move(2250, 0, 750, duration=1.5)
    show rxl_npz_b1 b1 b1_h1 onlayer m2:
        xpos 0.7
    play voice "voice/日向怜/020054.ogg"
    rxl "啊哈哈，我也最喜欢雷亚了~"
    hide ts_lst_ssz_b2 with None
    pause 0.1 hard
    show ts_lst_ssz_b3 b3 b3_sp2 onlayer m1 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/天使雷亚/000239.ogg"
    lst "呀，不、不要抱我！" with vpunch
    stop music fadeout 5.0
    pause 1.0 hard

label day225.store_event03:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    "于是几位女生一起走进了更衣室。"
    "虽然让雷亚独自面对她们有点不太好。"
    "但那毕竟是女子更衣室，还是放弃拯救的念头比较好。"
    pause 1.0 hard
    $ set_replay_scene("label16_1")
    scene set only lisite_cg meidou one
    with slowdissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/000240.ogg"
    lst "所以......这是什么？"
    play music first_04 fadein 3.0 if_changed
    play voice "voice/天使雷亚/000241.ogg"
    lst "凉君，这到底是要做什么？"
    me01 "简单来说就是拉客吧。"
    play voice "voice/天使雷亚/000242.ogg"
    lst "为什么要这么做？"
    me01 "因为要想把生意提上去，首先需要吸引更多的客人光顾。"
    play voice "voice/天使雷亚/000243.ogg"
    lst "那和这身装扮有什么关系？"
    me01 "穿得可爱一些才更容易把客人招来吧。"
    play voice "voice/天使雷亚/000244.ogg"
    lst "为什么我非得做这种事不可？"
    me01 "不是雷亚自己说也要一起帮忙的吗？"
    play voice "voice/天使雷亚/000245.ogg"
    lst "我可没听说要打扮成这样！"
    me01 "难道说你后悔了？"
    pause 0.1 hard
    scene set only lisite_cg meidou two
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/000246.ogg"
    lst "......也不是。"
    me01 "那么，现在就来试着拉客吧~"
    play voice "voice/天使雷亚/000247.ogg"
    lst "不要。"
    me01 "哦，那边正好有客人来了。"
    play voice "voice/天使雷亚/000248.ogg"
    lst "我才不管。"
    me01 "先来个微笑。"
    play voice "voice/天使雷亚/000249.ogg"
    lst "哼~"
    me01 "试着说一句“欢迎光临”。"
    play voice "voice/天使雷亚/000250.ogg"
    lst "死掉就好了。"
    pause 0.1 hard
    scene set only lisite_cg meidou seven
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/other/150001.ogg"
    stranger "合格了！"
    play voice "voice/other/150003.ogg"
    "店长" "原来如此，的确是新面孔。不过这样的新人还是第一次见。"
    pause 0.1 hard
    scene set only lisite_cg meidou five
    with dissolve
    play voice "voice/天使雷亚/000251.ogg"
    lst "这个一脸衰气的人是谁？"
    me01 "不要说那么失礼的话。"
    play voice "voice/other/150004.ogg"
    "店长" "合格了！"
    pause 0.1 hard
    scene set only lisite_cg meidou six
    with dissolve
    play voice "voice/天使雷亚/000252.ogg"
    lst "我在想经营困难可能是店长衰气很重的缘故。"
    me01 "所以说不要把这种失礼的话说出来啊。"
    play voice "voice/other/150007.ogg"
    "店长" "不，说不定正是这样没错。为了经营这家店，大家也都很辛苦。"
    play voice "voice/天使雷亚/000253.ogg"
    lst "有生命的东西迟早会逝去。有形的东西终有一天会消亡，这家咖啡店也是一样的。"
    me01 "以前就说过了，这样的大道理怎么样都无所谓！"
    play voice "voice/other/150008.ogg"
    "店长" "合格了。"
    me01 "......所以说完全不懂您的标准！"
    play voice "voice/other/150009.ogg"
    "店长" "不只是表面的那么简单，随时间的变迁乃是万物常理，正因为如此人们才会追求亘古不变的星空。"
    play voice "voice/other/150010.ogg"
    "店长" "我希望这家咖啡店也能变得像星空一样永恒的存在，希望这里能成为的人们随时都能归来的地方。"
    pause 0.1 hard
    play sound jiaobu2
    scene set only lisite_cg meidou two
    with dissolve
    pause 0.5 hard
    play voice "voice/天使雷亚/000254.ogg"
    lst "多亏了我，那个人也变得精神了。"
    me01 "嘛，从结果来看确实是这样的......"
    play voice "voice/天使雷亚/000255.ogg"
    lst "我的工作很有成效。"
    me01 "你的工作是去拉客吧。"
    play voice "voice/天使雷亚/000256.ogg"
    lst "死神才不会去拉客呢。"
    me01 "别说那种话嘛，你不也乐在其中吗？"
    play voice "voice/天使雷亚/000257.ogg"
    lst "这幅打扮，好不自在的说......"
    me01 "不过，很合适你呢。"
    pause 0.1 hard
    scene set only lisite_cg meidou three
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/000258.ogg"
    lst "......是、是吗？"
    me01 "是啊，怎么看都是一名出色的女仆。"
    pause 0.1 hard
    scene set only lisite_cg meidou two
    with dissolve
    play voice "voice/天使雷亚/000259.ogg"
    lst "你这算是夸我吗，有点微妙啊。"
    me01 "毕竟我很喜欢，雷亚的这身装扮。"
    pause 0.1 hard
    scene set only lisite_cg meidou three
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/000260.ogg"
    lst "......是吗？"
    me01 "嗯。"
    play voice "voice/天使雷亚/000261.ogg"
    lst "我变成女仆的话......凉君会高兴吗？"
    me01 "那是当然的。"
    pause 0.1 hard
    scene set only lisite_cg meidou four
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/000262.ogg"
    lst "那......真拿你没办法，就暂时这样好了。"
    play voice "voice/天使雷亚/000263.ogg"
    lst "当女仆也可以的~"
    play voice "voice/天使雷亚/000264.ogg"
    lst "只有现在......我是凉君的女仆。"
    me01 "试着叫我一声“主人”如何？"
    pause 0.1 hard
    scene set only lisite_cg meidou two 
    with dissolve
    play voice "voice/天使雷亚/000265.ogg"
    lst "我能捅你吗......"
    me01 "现在的雷亚虽然很养眼，但是总感觉冲击力不够。"
    me01 "就没有什么能够瞬间提升气场的方法吗？"
    pause 0.1 hard
    play sound shop_rill
    scene set only lisite_cg meidou ten
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/青木铃音/040119.ogg"
    lingyin "性感大作战怎么样？"
    play voice "voice/青木铃音/040120.ogg"
    lingyin "试着把雷亚的裙子剪短一些吧？"
    me01 "原来如此，确实是提升视觉冲击力的好方法。"
    play voice "voice/青木铃音/040121.ogg"
    lingyin "真是肮脏......"
    me01 "说好的作战呢？！"
    play voice "voice/青木铃音/040122.ogg"
    lingyin "还以为你一定会否决的呢。"
    play voice "voice/翔子/030060.ogg"
    xz "萝莉控是病......这说得一点也没错。"
    me01 "我说，你们两个是专程来嘲讽我的吗？"
    play voice "voice/翔子/030061.ogg"
    xz "毕竟桌子也擦完了椅子也摆好了，可还是没有客人来嘛。"
    play voice "voice/青木铃音/040123.ogg"
    lingyin "所以我们也换上女仆装，机会难得就也试着来拉客了。"
    play voice "voice/翔子/030062.ogg"
    xz "......果然我还是不怎么希望这样的。"
    play voice "voice/青木铃音/040124.ogg"
    lingyin "姐姐，试着拉起裙子展露一下大腿如何？"
    play voice "voice/翔子/030063.ogg"
    xz "性感路线我可不走！"
    play voice "voice/青木铃音/040125.ogg"
    lingyin "害羞的姐姐也好棒~"
    play voice "voice/翔子/030064.ogg"
    xz "别掀我的裙子啊！"
    play sound hite_heavy
    with vpunch
    me01 "为什么是打我！？"
    pause 0.1 hard
    scene set only lisite_cg meidou eight
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/天使雷亚/000266.ogg"
    lst "凉君......"
    me01 "怎么了？"
    play voice "voice/天使雷亚/000267.ogg"
    lst "就这么想看我的腿吗？"
    me01 "我可没这么说！"
    pause 0.1 hard
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/青木铃音/040126.ogg"
    lingyin "因为神野同学是傲娇嘛~"
    me01 "行了，你们不想营业了吗？"
    play voice "voice/翔子/030065.ogg"
    xz "说起来在咖啡店门口拉客本身是不是就有点奇怪？"
    play voice "voice/青木铃音/040127.ogg"
    lingyin "虽说这么做很显眼，不过说不定反而会把客人都吓跑呢。"
    me01 "......说到底这个建议是谁提出来的啊。"
    play voice "voice/青木铃音/040128.ogg"
    lingyin "而计划最大的受益者是神野同学。"
    me01 "如果我没记错的话，铃音同学才是发起人吧。"
    play voice "voice/青木铃音/040129.ogg"
    lingyin "我可没说过要实行“性感大作战”的。"
    me01 "不不不，这是只有你才会想出来的计划吧！"
    play voice "voice/翔子/030067.ogg"
    xz "......有时间相互推卸责任的话，还不如快点开始工作吧。"
    pause 0.1 hard
    scene set only lisite_cg meidou nine
    with dissolve
    play voice "voice/天使雷亚/000268.ogg"
    lst "......真是一点也没能放松。"
    me01 "抱歉雷亚，果然你才是最大的受害者。"
    play voice "voice/青木铃音/040130.ogg"
    lingyin "饱足了眼福的神野同学则是最大的赢家。"
    me01 "喜欢看别人出糗的铃音同学才是。"
    play voice "voice/青木铃音/040131.ogg"
    lingyin "没否认饱了眼福呢~"
    me01 "我投降......"
    "翔子又开始用看垃圾一样的眼神盯着我了，今天的晚饭......还有着落吗。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 1.0 hard
    $ end_replay()
    if not seen_day225_store_event01:
        $ seen_day225_store_event01 = True
    $ _overworld_label = 'day225.store_event01'
    if seen_day225_balltower_event01:
        jump day225.final_end
    jump day225.map

label day225.balltower_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    show snow_level1 onlayer fg
    with dissolve
    pause 2.0 hard
    scene set only balltower snow day xuejian2
    with dissolve
    pause 2.0 hard
    me01 "找到你了，希菲尔。"
    play music second_148 fadein 3.0 if_changed
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    show ts_xfe_yjz_b2 b2 b2_h1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002070.ogg"
    xfe "诶嘿，被找到了~"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show alu_ct_b8 b8 b8_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎~"
    show ts_xfe_yjz_b2 b2 b2_a1 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/希菲尔/001002080.ogg"
    xfe "谁也没有拜托你来找吧。"
    me01 "那边的仿制玩偶给我安静点。"
    hide alu_ct_b8
    $ flcam.move(0, 0, 900, duration=1.5)
    pause 0.5 hard
    hide ts_xfe_yjz_b2
    show ts_xfe_yjz_b3 b3 b3_sp1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002090.ogg"
    xfe "凉君，事情办完了吗？"
    me01 "是啊......之前的事谢谢你了。"
    me01 "那时的歌声是你的对吧？"
    me01 "是你......拯救了雷亚对吧？"
    me01 "那歌声虽然不是很清楚，但总觉得在哪里听过。"
    hide ts_xfe_yjz_b3
    show ts_xfe_yjz_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002110.ogg"
    xfe "和千冬比起来还差得远呢。"
    me01 "对希菲尔来说，千冬一直是什么样的感觉？"
    show ts_xfe_yjz_b2 b2 b2_n1
    play voice "voice/希菲尔/001002120.ogg"
    xfe "她是希菲尔最喜欢的人之一哟~"
    me01 "以前的她也一直像这样穿着{rb}白大褂{/rb}{rt}研究服{/rt}吗？"
    show ts_xfe_yjz_b2 b2 b2_sp1
    play voice "voice/希菲尔/001002130.ogg"
    xfe "白大褂？"
    me01 "抱歉，问了不该问的东西。"
    show ts_xfe_yjz_b2 b2 b2_s2
    play voice "voice/希菲尔/001002150.ogg"
    xfe "希菲尔我果然还有很多不懂的东西......和千冬比起来差得很远。"
    me01 "对能够“叭咕”的东西倒是清楚呢。"
    hide ts_xfe_yjz_b2 with None
    pause 0.1 hard
    show ts_xfe_yjz_b3 b3 b3_h3 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001002160.ogg"
    xfe "那是希菲尔的得意技嘛~"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show alu_ct_b8 b8 b8_1 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000010.ogg"
    alu "唔莎~"
    hide ts_xfe_yjz_b3 with None
    pause 0.1 hard
    show ts_xfe_yjz_b2 b2 b2_ga1 onlayer m2 at flu_down(0.25, 20):
        xpos 0.5
    play voice "voice/希菲尔/001002170.ogg"
    xfe "本小姐要把你整个吞下去。"
    hide ts_xfe_yjz_b2
    $ flcam.move(-4500, 0, 900, duration=1.5)
    pause 0.5 hard
    me01 "那么在此之前，先和希菲尔玩个空接阿露的游戏吧。"
    hide alu_ct_b8
    show alu_ct_b10 b10 b10_2 onlayer m2 at fly(0.5), basicfade:
        xpos 0.3
    play voice "voice/阿露/551000060.ogg" 
    alu "唔莎！"
    $ flcam.move(-2250, 0, 750, duration=1.5)
    show ts_xfe_yjz_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002180.ogg"
    xfe "凉君不行啦，阿露才不是食物呢。"    
    "明明之前差一点就被你吞下去了......"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky day xuejian2
    with dissolve
    pause 1.0 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer screens at side_left('xfe', 0.06), basicfade
    play voice "voice/希菲尔/001002190.ogg"
    xfe "雪好像又变大了......"
    hide ts_xfe_yjz_b1
    me01 "是啊，明明春天马上就要到了。"
    pause 1.0 hard
    scene set only balltower snow day xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    me01 "呐希菲尔，你之前说的“在春天来临之前去哪里都可以”是什么意思呢？"
    show ts_xfe_yjz_b1 b1 b1_s3
    play voice "voice/希菲尔/001002200.ogg"
    xfe "......"
    me01 "我们还能像以前那样玩耍吗？"
    show ts_xfe_yjz_b1 b1 b1_h2
    play voice "voice/希菲尔/001002210.ogg"
    xfe "......如果凉君能找到希菲尔的话，就一定还能再次相遇的。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    play ambience1 zhong_rill fadein 3.0
    scene set only balltower snow day big2
    with dissolve
    pause 2.0 hard
    show ts_xfe_yjz_b1 b1 b1_s2 onlayer screens at side_left('xfe', 0.06), basicfade
    play voice "voice/希菲尔/001002220.ogg"
    xfe "钟声又响了。"
    hide ts_xfe_yjz_b1
    pause 1.0 hard
    stop ambience1 fadeout 3.0
    scene set only balltower snow day xuejian2
    $ flcam.move(0, 0, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show ts_xfe_yjz_b1 b1 b1_n1 onlayer m2:
        xpos 0.5
    play voice "voice/希菲尔/001002230.ogg"
    xfe "拜拜，凉君。"
    pause 0.5 hard
    play sound xiaoshi_1
    show ts_xfe_yjz_b1 b1 b1_n1:
        xpos 0.5 alpha 1.0
        linear 0.75 alpha 0.0
    pause 1.0 hard
    hide ts_xfe_yjz_b1
    "和我告别之后，希菲尔的身影消失在了白雪之中。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard
    if not seen_day225_balltower_event01:
        $ seen_day225_balltower_event01 = True
    $ _overworld_label = 'day225.balltower_event01'
    if seen_day225_store_event01:
        jump day225.final_end
    jump day225.map

label day225.final_end:
    $ flcam.move(0, 0, 0)
    scene set only xfe_cg daze
    play music second_163 fadein 3.0 if_changed
    with slowdissolve
    pause 1.0 hard
    play voice "voice/希菲尔/001001830.ogg"
    xfe "早安，千冬。"
    play voice "voice/希菲尔/001001840.ogg"
    xfe "对不起，千冬......"
    pause 0.1 hard
    scene set only xfe_cg sad
    with dissolve
    play voice "voice/希菲尔/001001850.ogg"
    xfe "但是已经没问题了。"
    pause 0.1 hard
    scene set only xfe_cg normal
    with dissolve
    play voice "voice/希菲尔/001001860.ogg"
    xfe "全都......都没有问题了。"
    pause 1.0 hard
    scene white 
    with slowerdissolve
    $ flcam.move(1100, -5600, 450, duration=50.0, warper='ease_cubic')
    pause 1.0 hard
    scene set only memory_cg xuejian yume
    show snow_level1 onlayer fg
    with slowdissolve
    pause 2.0 hard
    "芬布尔之冬。"
    "漫长的寒冬。"
    "一个只存在于幻想中的世界。"
    "这个愿望。"
    "虽是如此的唐突。"
    "但终归需要有人来实现它......"
    "粉红的樱花将取代洁白的雪花在这颗星球上重新绽放。"
    "到那时，这场冬雪也会一起。"
    "随着春天的到来而消散殆尽。"
    stop music fadeout 5.0
    pause 1.0 hard
    hide snow_level1
    scene black
    with slowerdissolve
    pause 2.0 hard

    $ persistent.lingyin = True
    $ persistent.szl_ling = True
    $ persistent.youjia = True
    $ persistent.lihuaxi = True
    $ persistent.liuli = True
    $ persistent.lisite = True 
    $ persistent.xifeier = True
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    
    jump second_menu
