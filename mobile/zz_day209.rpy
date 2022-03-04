label day209:
    bookmark
    $ save_name = _("Day 209")
    $ suppress_overlay = True
    $ renpy.block_rollback()
    $ _rollback = False
    play sound "sound/system/second_menu.wav"
    scene black with Dissolve(8.0)
    pause 4.0 hard
    
    $ suppress_overlay = False
    $ renpy.block_rollback()
    $ _rollback = True

    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with slowdissolve
    play ambience1 jiaobu2 fadein 3.0
    pause 1.0 hard
    "距离圣诞节也只剩几天的时间了。"
    "此时我独自漫步在大街上。"
    "上次因为有琉璃带路的关系并没有在这里停留太长的时间。"
    "下次邀请立花老师一起来吧。"
    pause 1.0 hard
    stop ambience1 fadeout 3.0
    scene set only street day city2 xuejian
    with dissolve
    show cinemascope onlayer texture:
        subpixel True
        yzoom scale(1.32)
        easein_cubic 3.0 yzoom scale(1.0)
    with Pause(0.5)
    show screen chapter_marker(_('chapter four'), _("胜利是什么"))
    pause 6.0 hard
    show cinemascope:
        ease_cubic 3.0 yzoom scale(1.32)
    pause 3.0 hard
    
    $ flcam.move(3200, 300, 1100, duration=3.0, warper='ease_cubic')
    pause 3.0 hard
    me01 "......那是？"
    pause 1.0 hard
    $ flcam.move(-1100, -1400, 450)
    scene set only szl_cg shop1
    with slowdissolve
    play music second_107 fadein 3.0 if_changed
    pause 1.0 hard
    play voice "voice/水之濑/051501250.ogg"
    szl "......"
    me01 "水之濑......同学？"
    pause 0.1 hard
    play sound shop_rill
    scene set only szl_cg shop2
    with dissolve
    play voice "voice/千波姐/161500010.ogg"
    qbj "小凛~你现在......诶？"
    play voice "voice/千波姐/161500020.ogg"
    qbj "神野君......那、那个，欢迎光临？"
    me01 "不是这样的，我只是刚好路过而已。"
    "我看了一眼店面的招牌......果然这里就是传说中的女仆咖啡厅。"
    play voice "voice/千波姐/161500030.ogg"
    qbj "虽说我们的工作是招揽客人和店门前的清扫工作。"
    play voice "voice/千波姐/161500040.ogg"
    qbj "可没想到竟然把不是客人的神野同学也吸引来了。"
    pause 0.1 hard
    scene set only szl_cg shop6
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051501260.ogg"
    szl "才不是我招来的......"
    play voice "voice/水之濑/051501270.ogg"
    szl "我只是按照吩咐负责店门前的清扫工作而已，是他擅自路过的。"
    pause 0.1 hard
    scene set only szl_cg shop7
    with dissolve
    play voice "voice/千波姐/161500050.ogg"
    qbj "不过被熟人看见的话，果然还是有点害羞呢，这种打扮......"
    play voice "voice/水之濑/051501280.ogg"
    szl "我无所谓。"
    pause 0.1 hard
    scene set only szl_cg shop4
    $ flcam.move(-1100, -1400, 450, duration=3.0, warper='ease_quad')
    with dissolve
    pause 3.0 hard
    me01 "......"
    play voice "voice/水之濑/051501290.ogg"
    szl "怎么了？"
    me01 "没、没什么......只是觉得有些意外。"
    play voice "voice/水之濑/051501300.ogg"
    szl "怎么说？"
    me01 "没想到二位会接受这样的兼职。"
    play voice "voice/水之濑/051501310.ogg"
    szl "不行吗？"
    me01 "不是这个意思。"
    me01 "倒不如说，这个可爱的女仆装配上水之濑的气质简直完美。"
    me01 "因为身材很好所以看起来就像是量身定做的一般。"
    play voice "voice/水之濑/051501320.ogg"
    szl "......"
    play voice "voice/水之濑/051501330.ogg"
    szl "你还真会恭维人，虽然和你的脸完全不相称。"
    me01 "虽然你的话有些打击人，但我也只是说实话而已。"
    play voice "voice/水之濑/051501340.ogg"
    szl "......是吗。"
    me01 "所以水之濑同学平时都会来这里打工吗？"
    pause 0.1 hard
    scene set only szl_cg shop6
    with dissolve
    play voice "voice/水之濑/051501350.ogg"
    szl "怎么样都好吧......"
    "正因为和平时古板的优等生有些不同才会有这样的反差萌吧。"
    "就和翔子与“梦”给人的感觉一样。"
    me01 "什么时候开始的？"
    play voice "voice/水之濑/051501360.ogg"
    szl "就今天，被柚子拜托的。"
    me01 "是这样啊......可惜了。"
    me01 "会长呢？"
    pause 0.1 hard
    scene set only szl_cg shop7
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千波姐/161500060.ogg"
    qbj "唔嗯，我是因为有熟人在这里打工才......"
    play voice "voice/千波姐/161500070.ogg"
    qbj "说是因为年末到了人手不够，所以才被叫来帮忙的。"
    play voice "voice/千波姐/161500080.ogg"
    qbj "对方说可以的话能多叫点人手......"
    me01 "原来如此，所以也拜托了水之濑同学吧。"
    play voice "voice/千波姐/161500090.ogg"
    qbj "嗯，然后小凛也答应了。"
    play voice "voice/水之濑/051501370.ogg"
    szl "......"
    me01 "果然水之濑同学其实也是那种乐于助人的类型嘛。"
    play voice "voice/水之濑/051501380.ogg"
    szl "只是刚好很闲而已......再说和你没关系吧。"
    pause 0.1 hard
    scene set only szl_cg shop6
    $ flcam.move(-1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051501390.ogg"
    szl "比起这个柚子，不是还有其他工作的吗？"
    play voice "voice/千波姐/161500100.ogg"
    qbj "啊、嗯......清扫结束了吗？"
    play voice "voice/水之濑/051501400.ogg"
    szl "还差一点点，基本上完成了。"
    play voice "voice/千波姐/161500110.ogg"
    qbj "店长说，结束了就可以休息了。"
    play voice "voice/千波姐/161500120.ogg"
    qbj "就这样，我先走了~"
    play voice "voice/水之濑/051501410.ogg"
    szl "我知道了，也是时候下班了。"
    me01 "既然这样那我也走了......"
    pause 0.1 hard
    scene set only szl_cg shop7
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    play voice "voice/千波姐/161500130.ogg"
    qbj "啊、好的，学校再见了~"
    pause 0.1 hard
    play sound shop_rill
    scene set only szl_cg shop5
    with dissolve
    pause 1.0 hard
    me01 "水之濑同学也是，之后学校见。"
    pause 0.1 hard
    scene set only szl_cg shop8
    $ flcam.move(-3200, -2200, 750, duration=3.0, warper='ease_quad')
    with dissolve
    pause 3.0 hard
    play voice "voice/水之濑/051501420.ogg"
    szl "......"
    me01 "水之濑同学？"
    me01 "......你不说话难道是因为舍不得让我走吗？"
    play voice "voice/水之濑/051501420.ogg"
    szl "......"
    pause 0.1 hard
    scene set only szl_cg shop8
    with dissolve
    me01 "抱歉，刚刚那个只是开个玩笑而已。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowdissolve
    play sound shop_rill
    pause 1.0 hard
    "水之濑凛没有回答，而是转身走进店里。"
    "留下我一个人在原地不知所措。"
    "从她那微妙的表情中完全不知道是在生气还是单纯在思考该说什么。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day city2 xuejian
    play music second_133 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    with dissolve
    pause 0.5 hard
    show szl_dsf_b1 b1 b1_n2 onlayer m2 at walkin_r(0.5)
    pause 0.5 hard
    me01 "那个......你真的没有生气吗？"
    hide szl_dsf_b1
    show szl_dsf_b3 b3 b3_n3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510230.ogg"
    szl "某种意义上算有吧......"
    me01 "某种意义上？"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s4 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510240.ogg"
    szl "刚才遇到你的瞬间我就决定好了......"
    me01 "决定拉拢我当客人？"
    hide szl_dsf_b2 with None
    pause 0.1 hard
    show szl_dsf_b3 b3 b3_n4 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051510250.ogg"
    szl "我才没有那样说！"
    me01 "不过话说回来，水之濑同学你无论穿什么衣服都很好看呢。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    play sound jump_1
    show szl_dsf_b3 b3 b3_ga3 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/水之濑/051510270.ogg"
    szl "哈？！你突然间胡说些什么啊......"
    me01 "所以说我只是把真实的想法说出来而已。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_a2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510280.ogg"
    szl "错、错觉而已！"
    show szl_dsf_b2 b2 b2_s2
    play voice "voice/水之濑/051510290.ogg"
    szl "想和我套近乎什么的......才没有那么容易。"
    me01 "抱歉，我也没想到会这样。"
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510300.ogg"
    szl "那就不要擅自说一些让人害羞的话！"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_s1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510310.ogg"
    szl "行了......快走吧。"
    play sound jiaobu2
    show szl_dsf_b2 b2 b2_s1 at walkout_r(0.5)
    pause 0.5 hard
    hide szl_dsf_b2
    $ flcam.move(0, -100, 400, duration=1.5)
    pause 0.5 hard
    me01 "去哪里......等等我啊喂！"
    pause 1.0 hard
    scene black
    with slowerdissolve
    pause 2.0 hard

label day209.street_event01:
    $ flcam.move(0, 0, 0)
    scene set only street day city3 xuejian
    $ flcam.move(0, -300, 900, duration=1.5)
    with slowdissolve
    pause 0.5 hard
    show szl_dsf_b2 b2 b2_n2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510360.ogg"
    szl "......"
    me01 "我们这是要去哪里，水之濑同学？"
    hide szl_dsf_b2 
    show szl_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510370.ogg"
    szl "真没水准啊。"
    me01 "为什么突然开始数落起我来了？！"
    show szl_dsf_b3 b3 b3_a1
    play voice "voice/水之濑/051510380.ogg"
    szl "虽说没有计划，但也没必要一直在意目的地吧。"
    me01 "不是......明明是你让我跟着你的。"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_a1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510400.ogg"
    szl "可以“较量”的地方，应该有很多选择才对。"
    me01 "......较量？"
    show szl_dsf_b2 b2 b2_s4
    play voice "voice/水之濑/051510410.ogg"
    szl "我想想~"
    "水之濑的视线飞快地向四周扫荡着。"
    show szl_dsf_b2 b2 b2_s1
    me01 "......你说的较量是怎么回事？"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dsf_b2
    show szl_dsf_b3 b3 b3_ga1 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510420.ogg"
    szl "稍微安静点。"
    hide szl_dsf_b3
    show szl_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510430.ogg"
    szl "这不是约会......只是普通的“较量”。（小声）"
    hide szl_dsf_b1
    show szl_dsf_b2 b2 b2_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510440.ogg"
    szl "和神野君约会什么的......（小声）"
    me01 "那个水之濑同学......这样下去的话会天就要黑了。"
    play sound jump_1
    hide szl_dsf_b2 with None
    pause 0.1 hard
    show szl_dsf_b3 b3 b3_n4 onlayer m2 at flu_down(0.15, 20):
        xpos 0.5
    play voice "voice/水之濑/051510450.ogg"
    szl "都说了安静点！"
    me01 "抱歉......"
    hide szl_dsf_b3
    show szl_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510460.ogg"
    szl "你觉得......那个怎么样？"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 1.0 hard
    me01 "那、那个是？！"
    me01 "你是认真的吗......"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black
    with dissolve
    pause 1.0 hard
    scene set only szl_cg game1
    with slowerdissolve
    play music second_139 fadein 3.0 if_changed
    pause 1.0 hard
    me01 "没想到你说的“较量”就是指这个......"
    play voice "voice/水之濑/051510470.ogg"
    szl "会集中不了的所以请别和我说话，这种游戏还是第一次玩。"
    me01 "嘛，虽然我也是第一次。"
    me01 "但是水之濑同学......你这样的姿势真的没问题吗？"
    play voice "voice/水之濑/051510480.ogg"
    szl "区区几个瓶子而已完全没问题，即便是你也做到了不是吗？"
    play voice "voice/水之濑/051510490.ogg"
    szl "接下来只要把剩下的全部击倒就行了吧。虽然第一次投球只击中了一个，但是这次一定没问题的。"
    me01 "不是，我的意思是说......"
    play voice "voice/水之濑/051510500.ogg"
    szl "我难道没有说叫你安静一点吗？"
    me01 "可是这样的话，真的就跟普通的约会一摸一样了。"
    pause 0.1 hard
    scene set only szl_cg game2
    $ flcam.move(-2200, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    with vpunch
    play voice "voice/水之濑/051510510.ogg"
    szl "{size=72}！{/size}"
    pause 1.0 hard
    scene white
    with slowdissolve
    play sound ball
    with vpunch 
    "{size=72}嘎砰！{/size}"
    "球从水之濑的手里滑落。"
    pause 0.1 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg game3
    with dissolve
    play voice "voice/水之濑/051510520.ogg"
    szl "......所、所以说不是那样的！"
    pause 0.1 hard
    scene set only szl_cg game4
    with dissolve
    play voice "voice/水之濑/051510530.ogg"
    szl "只是较量而已，较量！"
    play voice "voice/水之濑/051510540.ogg"
    szl "虽然确实，周围有很多情侣......"
    play voice "voice/水之濑/051510550.ogg"
    szl "而且我们看起来大概也是那样的感觉没错......"
    me01 "果然水之濑同学也察觉到了吗。"
    pause 0.1 hard
    scene set only szl_cg game3 
    $ flcam.move(-2200, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051510560.ogg"
    szl "......就是因为太过明显了所以我才那么困扰的啊！"
    me01 "也就是说现在，水之濑同学想用“击倒瓶子”的数量来和我决出胜负吗？"
    pause 0.1 hard
    scene set only szl_cg game1
    with dissolve
    play voice "voice/水之濑/051510570.ogg"
    szl "是啊，这一次全部击倒的话......我就可以击败你了！"
    me01 "那也得你能做得到才行。"
    play voice "voice/水之濑/051510590.ogg"
    szl "没有我击不倒的瓶子。"
    me01 "但是水之濑同学你至今为止一次也没有击出过全中。"
    me01 "不要说全中，就连一半都没有击倒过。"
    pause 0.1 hard
    scene set only szl_cg game3
    $ flcam.move(-4200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051510600.ogg"
    szl "你能打出来的话我也可以的！"
    me01 "......我那也只是碰巧的而已。"
    pause 0.1 hard
    scene set only szl_cg game1
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051510610.ogg"
    szl "绝对要打出来给你看。"
    play voice "voice/水之濑/051510620.ogg"
    szl "不管是哪种项目，打倒对手才是胜利者！"
    play voice "voice/水之濑/051510630.ogg"
    szl "集中......让精神更加细致、敏锐。"
    play voice "voice/水之濑/051510640.ogg"
    szl "然后与球合二为一。"
    me01 "这样的话水之濑同学不也会被一起丢出去吗？"
    play voice "voice/水之濑/051510650.ogg"
    szl "......我倒是真想把你丢出去！"
    me01 "等等，这样做的话无论如何都是违反规则的！"
    me01 "还有我觉得你还是快点投出去比较好......"
    "两侧球道上的人都在等着水之濑投掷。"
    "视线全部集中了过来。"
    play voice "voice/水之濑/051510660.ogg"
    szl "好......我上了，看好！"
    me01 "等下！"
    play voice "voice/水之濑/051510670.ogg"
    szl "你就算想扰乱我的注意力也是没有用的。"
    play voice "voice/水之濑/051510680.ogg"
    szl "都到这个地步了，接下来就只有勇往直前将{rb}对手{/rb}{rt}瓶子{/rt}击倒了！"
    me01 "这样的姿势......会被看到裙子里面的。"
    pause 0.1 hard
    scene set only szl_cg game2
    $ flcam.move(-2200, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051510690.ogg"
    szl "{size=72}！{/size}"
    pause 0.5 hard
    scene white 
    with dissolve
    pause 1.0 hard
    play sound ball
    with vpunch
    "{size=72}嘎砰！{/size}"
    "球再一次脱手。"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg game3
    with slowdissolve
    play voice "voice/水之濑/051510700.ogg"
    szl "你、你在看哪里啊！？"
    me01 "总之先冷静下来吧。"
    me01 "不是我故意要看的，都怪水之濑同学的裙子太短了。"
    play voice "voice/水之濑/051510710.ogg"
    szl "我也没想到会到这里来，所以没办法的吧......"
    me01 "那么请不要再做幅度那么大的姿势了，毕竟真被看到的话就不好了。"
    play voice "voice/水之濑/051510720.ogg"
    szl "就算你不说我也不会再给你看的！"
    pause 0.1 hard
    scene set only szl_cg game4
    with dissolve
    play voice "voice/水之濑/051510740.ogg"
    szl "集中、集中......"
    play voice "voice/水之濑/051510750.ogg"
    szl "虽然我也有好好穿的，但是......"
    play voice "voice/水之濑/051510760.ogg"
    szl "再不投的话、再不快点投的话，又会被神野君......"
    pause 0.1 hard
    scene set only szl_cg game3
    $ flcam.move(-4200, -2800, 800, duration=3.0, warper='ease_quad')
    with dissolve
    pause 2.5 hard
    play voice "voice/水之濑/051510770.ogg"
    szl "{size=72}不、不要啊！{/size}"
    pause 0.5 hard
    scene white 
    with slowdissolve
    play sound ball
    with vpunch 
    pause 1.0 hard
    "就这样，水之濑的计分表上又一次被写上了“——”符号。（注释：表示球落槽，一分未得）"
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg game1
    with slowdissolve
    pause 0.5 hard
    "连续几轮的较量之后，都是以我的完胜告终。"
    "已经是最后一次机会了。"
    play voice "voice/水之濑/051510780.ogg"
    szl "......"
    me01 "这次内裤没问题吗？"
    play voice "voice/水之濑/051510790.ogg"
    szl "......你没耍什么花招吧？"
    me01 "就算是为了看你的内裤，我也不至于做出这么卑鄙的事情吧。"
    pause 0.1 hard
    scene set only szl_cg game3
    $ flcam.move(-2200, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051510800.ogg"
    szl "才不是说这个，我是说刚才你投出去的球好像拐弯了？"
    me01 "那个啊，我在投球的时候刻意扭动了手腕，这样的话球就会旋转。"
    me01 "顺带一提这个技巧是我刚才模仿旁边的人学会的。"
    pause 0.1 hard
    scene set only szl_cg game4
    with dissolve
    play voice "voice/水之濑/051510830.ogg"
    szl "......"
    me01 "再说了，如果真的要做什么手脚获胜的话根本不用这么麻烦。"
    me01 "直接上去掀裙子的话不是更方便吗？"
    pause 0.1 hard
    scene set only szl_cg game2
    $ flcam.move(0, 0, 0, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play sound ball
    play voice "voice/水之濑/051510830.ogg"
    szl "{size=72}！{/size}" with vpunch
    me01 "等等我开玩笑的，当然不会那么做！"
    pause 0.1 hard
    scene set only szl_cg game4
    with dissolve
    play voice "voice/水之濑/051510840.ogg"
    szl "平常心、平常心......"
    me01 "只是打保龄球而已不用这么认真吧。"
    "现在的我们在周围人眼里应该就是一对脑子有问题的情侣。"
    "话说为什么旁边两个球道的人都不见了！？"
    pause 0.1 hard
    scene set only szl_cg game1
    with dissolve
    play voice "voice/水之濑/051510850.ogg"
    szl "这样的话......我也会试着把球旋转起来。"
    me01 "这可不是那么轻易就能掌握的技巧。"
    play voice "voice/水之濑/051510860.ogg"
    szl "不就是扭一下手腕而已吗，小菜一碟！"
    $ flcam.move(-4200, -2800, 800, duration=1.5, warper='ease_quad')
    pause 1.0 hard
    play voice "voice/水之濑/051510870.ogg"
    szl "我是绝对不会输给你的！"
    pause 1.0 hard
    scene white 
    with slowdissolve
    pause 1.0 hard
    play sound ball
    with vpunch
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg game3
    with dissolve
    play voice "voice/水之濑/051510880.ogg"
    szl "不仅是手腕就连手指也很疼啊！"
    "水之濑刚才那一下投球漂亮地滚进了旁边的滑道里。"
    me01 "我觉得......可能15磅的球对于水之濑同学来说太沉了。"
    play voice "voice/水之濑/051510890.ogg"
    szl "你不也是用一样的球吗？"
    me01 "我是男孩子吧，腕力根本就不一样。"
    pause 0.1 hard
    scene set only szl_cg game4
    with dissolve
    play voice "voice/水之濑/051510900.ogg"
    szl "我绝对会让它旋转起来的！"
    pause 0.1 hard
    scene set only szl_cg game1
    with dissolve
    play voice "voice/水之濑/051510920.ogg"
    szl "看好了！"
    me01 "看内裤吗？"
    pause 0.1 hard
    scene set only szl_cg game3
    with dissolve
    play voice "voice/水之濑/051510930.ogg"
    szl "那么想看的话，倒是也给我看看你的啊！"
    me01 "已经完全搞不懂你的逻辑了？！"
    pause 0.1 hard
    scene set only szl_cg game4
    with dissolve
    play voice "voice/水之濑/051510940.ogg"
    szl "不是常说决胜内裤吗？"
    me01 "那东西不是这个意思吧......"
    play voice "voice/水之濑/051510950.ogg"
    szl "总、总之我要上了。"
    me01 "请便。"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    play sound ball
    with vpunch
    pause 2.0 hard

label day209.street_event02:
    $ flcam.move(0, 0, 0)
    scene set only sky evening xuejian2
    with dissolve
    pause 1.0 hard
    "我们就这样进行了四场“惨烈”的对决。"
    "至于结果......"
    pause 1.0 hard
    scene set only street day city3 xuejian
    with dissolve
    play music second_133 fadein 3.0 if_changed
    $ flcam.move(0, -300, 900, duration=1.5)
    pause 0.5 hard
    show szl_dsf_b1 b1 b1_s3 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510960.ogg"
    szl "......"
    me01 "我的完胜啊。"
    show szl_dsf_b1 b1 b1_c1
    play voice "voice/水之濑/051510970.ogg"
    szl "{size=72}呜！{/size}"
    "因为都是初学者的缘故，我们刚刚的比赛在专业人士的眼里恐怕就是一场闹剧吧。"
    "但是无论如何，水之濑凛的完败是不灭的事实。"
    $ flcam.move(0, -300, 1000, duration=1.5)
    pause 0.5 hard
    hide szl_dsf_b1 with None
    pause 0.1 hard
    show szl_dsf_b3 b3 b3_a2 onlayer m2 at flu_down(0.35, 20):
        xpos 0.5
    play voice "voice/水之濑/051510980.ogg"
    szl "还没有结束，我还没有输！"
    hide szl_dsf_b3
    show szl_dsf_b2 b2 b2_a2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051510990.ogg"
    szl "刚才那个只是热身而已！"
    me01 "还要比吗......"
    show szl_dsf_b2 b2 b2_h2
    play voice "voice/水之濑/051511000.ogg"
    szl "是、是啊，真正的较量现在才刚刚开始！"
    hide szl_dsf_b2
    show szl_dsf_b1 b1 b1_s2 onlayer m2:
        xpos 0.5
    play voice "voice/水之濑/051511010.ogg"
    szl "所以，那个......"
    pause 0.1 hard
    $ flcam.move(0, 0, 0)
    scene set only szl_cg game5
    with slowdissolve
    pause 0.5 hard
    play voice "voice/水之濑/051511020.ogg"
    szl "下、下一个就是那个！"
    me01 "......吊娃娃机。"
    pause 0.1 hard
    scene set only szl_cg game6
    with dissolve
    play voice "voice/水之濑/051511030.ogg"
    szl "之前看柚子玩过，是要把毛绒娃娃抓起来对吧。"
    me01 "毛绒娃娃，你想要吗？"
    play voice "voice/水之濑/051511040.ogg"
    szl "抓到的话就塞给你。"
    play voice "voice/水之濑/051511050.ogg"
    szl "至少要塞给你4只！"
    play voice "voice/水之濑/051511060.ogg"
    szl "今晚你就好好抱着毛绒娃娃哭着入睡吧。"
    play voice "voice/水之濑/051511070.ogg"
    szl "也让你好好体会下我刚才的心情！"
    me01 "一点威严都没有啊......"
    pause 0.1 hard
    play sound jing01
    scene set only szl_cg game7
    with dissolve
    play voice "voice/水之濑/051511080.ogg"
    szl "那么我先来，看好了！"
    me01 "等等，那要是我抓到的话该怎么办呢？"
    play voice "voice/水之濑/051511090.ogg"
    szl "我会收下的......"
    me01 "那个......也就是说，抓到的娃娃就送给对方？"
    play voice "voice/水之濑/051511100.ogg"
    szl "你觉得能抓得到的话就尽管试试看吧！"
    me01 "这完全就是约会做的事情嘛。"
    pause 0.1 hard
    play sound jing02
    scene set only szl_cg game8
    with dissolve
    with vpunch
    play voice "voice/水之濑/051511110.ogg"
    szl "都说了不是！是较量！这样连我自己都开始在意起来了！"
    pause 0.1 hard
    play sound ganga01
    scene set only szl_cg game9
    with dissolve
    me01 "不管怎么样，这个胜负我接受了。"
    pause 0.1 hard
    scene set only szl_cg game10
    with dissolve
    play voice "voice/水之濑/051511120.ogg"
    szl "......"
    me01 "今天就彻底陪水之濑同学玩个够吧。"
    pause 0.1 hard
    scene set only szl_cg game11
    with dissolve
    play voice "voice/水之濑/051511140.ogg"
    szl "我才是......求之不得。（小声）"
    play voice "voice/水之濑/051511150.ogg"
    szl "有你陪我的话，不管多少次我都会奉陪的......（小声）"
    stop music fadeout 5.0
    pause 1.0 hard
    scene black 
    with slowerdissolve
    pause 2.0 hard

label day209.home_event01:
    $ flcam.move(0, 0, 0)
    scene set only sky night xuejian2
    with slowdissolve
    pause 1.0 hard
    "回到家的时候已经是晚上了。"
    "虽然水之濑非常在意自己的失败。"
    "但还是老老实实地放我回去了。"
    pause 1.0 hard
    $ seen_living_room = False

label day209.myroom_event01:
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
            move _("客厅") jump day209.livingroom_event01
            screen_direction left
            sleep jump day209.sleep

label day209.livingroom_event01:
    if not seen_living_room:
        $ suppress_overlay = False
        $ renpy.block_rollback()
        $ _rollback = True
        $ seen_living_room = True
        $ flcam.move(0, 0, 0)
        scene black
        pause 1.0 hard
        scene set only home night living_room xuejian
        with dissolve
        play music second_105 fadein 3.0 if_changed
        $ flcam.move(-2250, 0, 750, duration=1.5)
        pause 0.5 hard
        show xz_dsf_b2 b2 b2_n1 onlayer m2:
            xpos 0.5
        show aiyi_dzf_b1 b1 b1_n1 onlayer m2:
            xpos 0.3
        play voice "voice/翔子/010105840.ogg"
        xz "爱衣还不去洗澡吗？"
        play voice "voice/爱衣/110102510.ogg"
        aiyi "等大姐姐你忙完就去~"
        hide xz_dsf_b2
        show xz_dsf_b3 b3 b3_h1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010105850.ogg"
        xz "那就一起吧。"
        show aiyi_dzf_b1 b1 b1_h1
        play voice "voice/爱衣/110102520.ogg"
        aiyi "嗯，大哥哥也和爱衣一起吧？"
        hide xz_dsf_b3 with None
        pause 0.1 hard
        show xz_dsf_b1 b1 b1_a2 onlayer m2 at flu_down(0.15, 20):
            xpos 0.5
        play voice "voice/翔子/010105860.ogg"
        xz "{size=72}驳回！{/size}"
        show aiyi_dzf_b1 b1 b1_s4
        play voice "voice/爱衣/110102530.ogg"
        aiyi "大姐姐，为什么？"
        show xz_dsf_b1 b1 b1_sp2
        play voice "voice/翔子/010105870.ogg"
        xz "就算你这么问......"
        play voice "voice/爱衣/110102540.ogg"
        aiyi "为什么只有大哥哥不行呢？"
        hide xz_dsf_b1
        show xz_dsf_b2 b2 b2_s2 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010105880.ogg"
        xz "等爱衣长大一点就会明白了。"
        hide xz_dsf_b2
        $ flcam.move(-4500, 300, 900, duration=1.5)
        show aiyi_dzf_b1 b1 b1_n1
        play voice "voice/爱衣/110102550.ogg"
        aiyi "大哥哥等等也要洗澡的吧？"
        me01 "是啊。"
        show aiyi_dzf_b1 b1 b1_h1
        play voice "voice/爱衣/110102560.ogg"
        aiyi "那就大家一起洗吧？"
        $ flcam.move(-2250, 0, 750, duration=1.5)
        show xz_dsf_b2 b2 b2_ga2 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010105890.ogg"
        xz "爱衣，不能任性。你看神野君也很困扰的。"
        show aiyi_dzf_b1 b1 b1_s2
        play voice "voice/爱衣/110102570.ogg"
        aiyi "小桃的奶奶说过，大姐姐是傲娇所以会摆出相反的态度。"
        show aiyi_dzf_b1 b1 b1_n1
        play voice "voice/爱衣/110102580.ogg"
        aiyi "所以大姐姐的真心其实是想和大哥哥一起洗澡的~"
        me01 "翔子，没想到你......"
        hide xz_dsf_b2 with None
        pause 0.1 hard
        show xz_dsf_b1 b1 b1_a1 onlayer m2 at flu_down(0.35, 20):
            xpos 0.5
        play voice "voice/翔子/010105900.ogg"
        xz "才不是！"
        show aiyi_dzf_b1 b1 b1_h1
        play voice "voice/爱衣/110102590.ogg"
        aiyi "刚才那是“没有错”的意思喔~"
        hide xz_dsf_b1
        show xz_dsf_b2 b2 b2_ga2 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010105910.ogg"
        xz "所、所以说......"
        $ flcam.move(-2250, 0, 900, duration=1.5)
        pause 0.5 hard
        show aiyi_dzf_b1 b1 b1_n1
        play voice "voice/爱衣/110102600.ogg"
        aiyi "和大哥哥一起洗吧？"
        hide xz_dsf_b2
        show xz_dsf_b3 b3 b3_h1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010105920.ogg"
        xz "也、也是呢，一起洗吧~"
        show aiyi_dzf_b1 b1 b1_h1 at flu_down(0.35, 20):
            xpos 0.3
        play voice "voice/爱衣/110102610.ogg"
        aiyi "好！"
        hide xz_dsf_b3 with None
        pause 0.1 hard
        show xz_dsf_b1 b1 b1_sp3 onlayer m2 at flu_down(0.15, 20):
            xpos 0.5
        play voice "voice/翔子/010105930.ogg"
        xz "等等，不是反着来的吗？！"
        show aiyi_dzf_b1 b1 b1_n1
        play voice "voice/爱衣/110102620.ogg"
        aiyi "大哥哥，太好了呢~"
        hide xz_dsf_b1
        show xz_dsf_b3 b3 b3_c1 onlayer m2:
            xpos 0.5
        play voice "voice/翔子/010105940.ogg"
        xz "神、神野君......"
        me01 "我还是先回自己的房间去了。"
        stop music fadeout 5.0
        pause 1.0 hard
        scene black
        with slowerdissolve
        pause 2.0 hard
        jump day209.myroom_event01
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
            camera_pos (scale(3097), scale(-1024), 400)
            screen_pos (0.5, 1.0)
            screen_direction right
            move _("卧室") jump day209.myroom_event01

label day209.sleep:
    menu:
        "早点休息":
            if not seen_living_room:
                window mode thought
                me01 "睡觉之前还是先去看看翔子她们的情况吧。"
                $ flcam.move(0, -100, 400, duration=3.0)
                pause 0.5 hard
                jump investigate
            $ flcam.move(0, -300, 1000, duration=1.5)
            show xz_dsf_b3 b3 b3_h1
            play voice "voice/翔子/010001080.ogg"
            xz "晚安~"
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
    jump day209.ritroom

label day209.ritroom:
    default seen_day209_ritroom = False
    play music ritroom_day fadein 3.0 if_changed
    play ambience1 ritroom_fireplace fadein 3.0 if_changed

    if not seen_day209_ritroom:
        scene set ritfrontyard spring day:
            mid spring day
            frontl spring day
            frontr spring day
        $ flcam.move(0, 0, 400)
        $ flcam.move(0, 0, 0, duration=1.5)
        with dissolve
        pause 3.0 hard

        scene set ritroom day:
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
        ritona "真亏你没有忘记修炼的事情啊。"
        ritona "话不多说，今天也好好地提升自己吧。"
        ritona "今后还有更加严酷的战斗在等待着我们呢。"
        show ritona b3 fb1 fa0 fc02
        $ flcam.stop()
        $ camera_move(-5400, 100, 200, duration=3.0)
        pause 0.5 hard
        $ seen_day209_ritroom = True
    else:
        pause 0.5 hard
        scene black with dissolve
        pause 3.0 hard
        scene set ritroom day:
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
            sleep jump day209.sleep_memory
            shop jump day209.shop
            member jump day209.stats
            teleport jump day209.teleport
            callback jump day209.callback
            roleroom jump day209.roleroom

label day209.callback:
    default seen_day209_callback = False
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

    if not seen_day209_callback:
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

        $ seen_day209_callback = True
    
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
                    jump day209.ritroom
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
                    jump day209.ritroom
            "下次一定":
                window mode thgouth
                me01 "相遇即是缘，请好好珍惜这份来之不易的羁绊。"
                pause 0.5 hard
                $ window_animate_outro()
                stop movie
                hide movie
                stop music fadeout 1.0
                $ _skipping = True
                jump day209.ritroom


label day209.shop:
    hide investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene set only street day city3 xuejian
    with slowdissolve
    pause 1.0 hard
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
    jump day209.ritroom


label day209.stats:
    hide screen investigation_popup

    python:
        for role in local_config.party:
            role.hp = role.max_hp + role.extend_max_hp
            role.mp = role.max_mp
    $ local_config.current_mode == "Consumables"
    $ local_config.current_actor = local_config.party[0]

    call screen stats
    jump investigate


label day209.roleroom:
    hide screen investigation_popup
    scene black
    pause 1.0 hard
    $ flcam.move(0, 0, 0)

    python:
        local_config.start_init(local_config.player, local_config.party)
        local_config.next_story = "day209.ritroom"
    
    call info


label day209.teleport:
    hide screen investigation_popup

    python:
        current_message = ""
        
    call screen teleporter("209")
    jump investigate


label day209.sleep_memory:
    hide screen investigation_popup
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

            if (ms_average_level < 25) or (not all(breakout_flag)) or any([l < 5 for l in outfits_levels]):
                window mode thought
                me01 "下一次的敌人可能会比较棘手，还是去「异界」和「养成屋」多准备一下吧。"
                window mode thought
                me01 "确保队伍的平均等级在{color=#ff0000}25级突破{/color}以上、且装备等级均在5级以上比较稳妥。"
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


label day209.szl_event01:
    $ flcam.move(0, 0, 0)
    scene set only szl_cg room1
    play music second_105 fadein 3.0 if_changed
    with slowdissolve
    pause 0.5 hard
    play voice "voice/千波姐/161500170.ogg"
    qbj "呐，小凛......"
    play voice "voice/水之濑/051502050.ogg"
    szl "......"
    play voice "voice/千波姐/161500180.ogg"
    qbj "还在想神野君的事情吗？"
    pause 0.1 hard
    scene set only szl_cg room2
    with dissolve
    play voice "voice/水之濑/051502060.ogg"
    szl "{size=72}！{/size}"
    play voice "voice/千波姐/161500190.ogg"
    qbj "盯~"
    play voice "voice/水之濑/051502070.ogg"
    szl "为、为什么这样问？"
    play voice "voice/千波姐/161500200.ogg"
    qbj "也不知道为什么......直觉吧。"
    play voice "voice/水之濑/051502080.ogg"
    szl "想多了，怎么可能嘛。"
    play voice "voice/千波姐/161500210.ogg"
    qbj "什么嘛，猜错了吗？"
    pause 0.1 hard
    scene set only szl_cg room3
    with dissolve
    play voice "voice/水之濑/051502090.ogg"
    szl "是呀，肯定的啊。我只是在想，借的睡衣虽然有点不好意思，但果然还是有点紧......"
    pause 0.1 hard
    scene set only szl_cg room4
    with dissolve
    play voice "voice/千波姐/161500220.ogg"
    qbj "要不要换成T恤？"
    play voice "voice/水之濑/051502100.ogg"
    szl "没关系的这样就好......毕竟让我住下也挺突然的。"
    play voice "voice/千波姐/161500230.ogg"
    qbj "邀请的人是我，所以不用放在心上的~"
    play voice "voice/水之濑/051502110.ogg"
    szl "当然会在意的......本来只是为了打工帮忙才来找你商量的。"
    play voice "voice/千波姐/161500240.ogg"
    qbj "小凛啊，该说你是刻板呢，还是太过注重礼节了呢。"
    pause 0.1 hard
    scene set only szl_cg room5
    with dissolve
    play voice "voice/水之濑/051502120.ogg"
    szl "......我可不想被柚子你这么说。"
    pause 0.1 hard
    scene set only szl_cg room4
    $ flcam.move(1100, -1400, 450, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/水之濑/051502130.ogg"
    szl "还让你帮我介绍工作......话说回来也没能好好谢谢店长。"
    pause 0.1 hard
    scene set only szl_cg room3
    with dissolve
    play voice "voice/千波姐/161500250.ogg"
    qbj "店长对你的评价好像很高啊，明明只是扫除工作而已。"
    play voice "voice/千波姐/161500260.ogg"
    qbj "不仅如此，还说可以多给些工钱呢。"
    play voice "voice/水之濑/051502140.ogg"
    szl "多亏了柚子你认真的工作态度吧。"
    play voice "voice/千波姐/161500270.ogg"
    qbj "我倒是觉得是因为小凛的女仆装非常合适的关系。"
    play voice "voice/水之濑/051502150.ogg"
    szl "没有那回事......"
    play voice "voice/千波姐/161500280.ogg"
    qbj "是吗？"
    play voice "voice/水之濑/051502160.ogg"
    szl "有需要的话，还请继续通知我。"
    pause 0.1 hard
    scene set only szl_cg room1
    with dissolve
    play voice "voice/水之濑/051502170.ogg"
    szl "你该不会是真的喜欢女仆这个职业了吧。"
    play voice "voice/千波姐/161500290.ogg"
    qbj "......果然还是很害羞，所以只想尽可能做些低调的工作。"
    pause 0.1 hard
    scene set only szl_cg room6
    with dissolve
    play voice "voice/千波姐/161500300.ogg"
    qbj "但要是人手不够的话，果然还是会被分配到类似的工作。"
    play voice "voice/水之濑/051502180.ogg"
    szl "毕竟这就是柚子你嘛。"
    pause 0.1 hard
    scene set only szl_cg room4
    with dissolve
    play voice "voice/水之濑/051502190.ogg"
    szl "真是吃亏的性格。"
    pause 0.1 hard
    scene set only szl_cg room1
    $ flcam.move(3200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千波姐/161500320.ogg"
    qbj "但是，我真的吓了一跳。"
    play voice "voice/水之濑/051502250.ogg"
    szl "什么事？"
    play voice "voice/千波姐/161500330.ogg"
    qbj "在那之后小凛你就像着了魔一样，拉着神野君就走掉了。"
    pause 0.1 hard
    scene set only szl_cg room7
    with dissolve
    play voice "voice/水之濑/051502260.ogg"
    szl "所、所以说你搞错了啦！"
    play voice "voice/千波姐/161500340.ogg"
    qbj "但是我有种“就是那样”的感觉。"
    play voice "voice/水之濑/051502270.ogg"
    szl "不要让我说太多次，没有那种可能性......"
    play voice "voice/千波姐/161500350.ogg"
    qbj "什么嘛~"
    pause 0.1 hard
    scene set only szl_cg room8
    with dissolve
    play voice "voice/水之濑/051502280.ogg"
    szl "干嘛一脸遗憾的样子啊......说了是误会。"
    pause 0.1 hard
    scene set only szl_cg room9
    with dissolve
    play voice "voice/千波姐/161500370.ogg"
    qbj "难不成是明明有其他的约定，但还是勉强过来帮我的忙？"
    play voice "voice/千波姐/161500380.ogg"
    qbj "那个......和神野君的。"
    play voice "voice/水之濑/051502380.ogg"
    szl "那种约定，不可能会有的吧。"
    play voice "voice/水之濑/051502390.ogg"
    szl "我和他，又不是很亲密的关系......"
    play voice "voice/水之濑/051502400.ogg"
    szl "而且到现在，就连话都没有正经地说过。"
    play voice "voice/千波姐/161500390.ogg"
    qbj "唔、嘛......就因为听说这一点，所以我才会觉得你们是不是好上了。"
    pause 0.1 hard
    stop music fadeout 5.0
    scene set only szl_cg room10
    with dissolve
    play voice "voice/水之濑/051502420.ogg"
    szl "......听说？从哪里？"
    pause 0.5 hard
    play sound open_door4
    play music second_106 fadein 3.0 if_changed
    scene set only szl_cg room11
    $ flcam.move(0, 0, 0, duration=3.0, warper='ease_quad')
    with dissolve
    pause 2.5 hard
    play sound jing03
    play voice "voice/千波/211500350.ogg"
    qb "有人叫我？！"
    play voice "voice/水之濑/051502430.ogg"
    szl "......"
    pause 0.1 hard
    scene set only szl_cg room12
    with dissolve
    play voice "voice/千波姐/161500400.ogg"
    qbj "......难道你一直在偷听吗，千波？"
    play voice "voice/千波/211500360.ogg"
    qb "听说大胸姐姐要来过夜。"
    play voice "voice/千波/211500370.ogg"
    qb "那我也不得不来参加这场睡衣派对了~"
    pause 0.1 hard
    scene set only szl_cg room13
    with dissolve
    play voice "voice/水之濑/051502440.ogg"
    szl "......谁也没有邀请你。"
    pause 0.1 hard
    scene set only szl_cg room14
    $ flcam.move(-2200, -1400, 450, duration=0.5, warper='ease_quad')
    with dissolve
    with vpunch 
    pause 0.1 hard
    play sound jing01
    play voice "voice/千波/211500380.ogg"
    qb "{size=72}什么！{/size}"
    play voice "voice/水之濑/051502450.ogg"
    szl "不要大吵大闹，已经很晚了。"
    pause 0.1 hard
    scene set only szl_cg room15
    with dissolve
    play voice "voice/千波姐/161500410.ogg"
    qbj "关系真的越来越好了呢，小凛和千波......"
    play voice "voice/千波姐/161500420.ogg"
    qbj "但是，小凛说的对，千波快去睡觉吧。"
    pause 0.1 hard
    scene set only szl_cg room16
    with dissolve
    play voice "voice/千波/211500390.ogg"
    qb "大声说话和熬夜，对美容是有好处的。"
    play voice "voice/水之濑/051502460.ogg"
    szl "我觉得一般都是反过来的......"
    play voice "voice/千波/211500400.ogg"
    qb "大胸姐姐你从刚才开始就一直在说凉君男的事。"
    play voice "voice/水之濑/051502470.ogg"
    szl "......"
    stop music fadeout 5.0
    pause 0.1 hard
    scene set only szl_cg room13
    with dissolve
    play voice "voice/千波姐/161500430.ogg"
    qbj "等、等下千波，适可而止......"
    play voice "voice/水之濑/051502480.ogg"
    szl "他也总是......像这样和你说话的吗？"
    play voice "voice/千波姐/161500440.ogg"
    qbj "......"
    play music second_105 fadein 3.0 if_changed
    play voice "voice/千波/211500410.ogg"
    qb "因为凉君男的兴趣就是搭讪幼儿园的小孩子嘛~"
    play voice "voice/水之濑/051502490.ogg"
    szl "你们那么经常见面吗？"
    play voice "voice/千波/211500420.ogg"
    qb "因为他总是来接送爱衣的关系。"
    pause 0.1 hard
    scene set only szl_cg room17
    $ flcam.move(-4200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    pause 1.0 hard
    play voice "voice/千波/211500430.ogg"
    qb "而且，他也已经拜倒在我的裙下了~"
    play voice "voice/水之濑/051502500.ogg"
    szl "你看起来就是个小不点，所以应该不会有这回事......"
    play voice "voice/水之濑/051502510.ogg"
    szl "呐......你有没有听说过，他以前的事情？"
    pause 0.1 hard
    scene set only szl_cg room13
    with dissolve
    play voice "voice/千波/211500440.ogg"
    qb "这倒没有。"
    play voice "voice/千波/211500450.ogg"
    qb "大胸姐姐，你总是在说凉君男的事。"
    pause 0.1 hard
    scene set only szl_cg room18
    with dissolve
    play voice "voice/水之濑/051502520.ogg"
    szl "才没有这回事......"
    play voice "voice/千波/211500460.ogg"
    qb "大胸姐姐难道你很在意凉君男吗？"
    pause 0.1 hard
    scene set only szl_cg room19
    with dissolve
    play voice "voice/水之濑/051502530.ogg"
    szl "{size=72}怎么可能！{/size}"
    pause 0.1 hard
    scene set only szl_cg room20
    with dissolve
    with vpunch 
    play sound jing04
    play voice "voice/千波/211500470.ogg"
    qb "为什么要对我大喊大叫啊！"
    pause 0.1 hard
    scene set only szl_cg room21
    $ flcam.move(0, 0, 0, duration=3.0, warper='ease_quad')
    with dissolve
    pause 2.5 hard
    play voice "voice/千波姐/161500450.ogg"
    qbj "那个二位......已经很晚了哟~"
    play voice "voice/千波/211500480.ogg"
    qb "都是大胸姐姐的错，害我被姐姐骂了！"
    pause 0.1 hard
    scene set only szl_cg room22
    with dissolve
    play voice "voice/水之濑/051502540.ogg"
    szl "......"
    pause 0.1 hard
    scene set only szl_cg room23
    with dissolve
    play voice "voice/水之濑/051502550.ogg"
    szl "......我看起来真的有那么在意神野君吗？"
    pause 0.1 hard
    scene set only szl_cg room24
    with dissolve
    play voice "voice/千波/211500490.ogg"
    qb "大胸姐姐果然还是很在意凉君男呢。"
    play voice "voice/水之濑/051502560.ogg"
    szl "才没有这回事......"
    pause 0.1 hard
    scene set only szl_cg room25
    with dissolve
    play voice "voice/千波/211500500.ogg"
    qb "难不成你是在嫉妒我和凉君男的关系？"
    play voice "voice/水之濑/051502570.ogg"
    szl "所以说，单凭你这个小不点......"
    pause 0.1 hard
    scene set only szl_cg room23
    $ flcam.move(-4200, -2800, 800, duration=1.5, warper='ease_quad')
    with dissolve
    with vpunch
    pause 1.0 hard
    play sound jing04
    play voice "voice/千波/211500510.ogg"
    qb "不要像凉君男一样张口闭口都是“小不点”啊！"
    play voice "voice/水之濑/051502580.ogg"
    szl "......他也是这样说的啊。（小声）"
    play voice "voice/水之濑/051502590.ogg"
    szl "是吗。（小声）"
    stop music fadeout 5.0
    pause 1.0 hard
    $ flcam.move(0, 0, 0)
    scene black 
    with slowerdissolve
    pause 2.0 hard
    $ suppress_overlay = True
    jump day210
