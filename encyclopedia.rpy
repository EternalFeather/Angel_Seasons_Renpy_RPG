
init:
    $ style.default.font = u"浪漫雅圆.ttf"
    $ style.default.language = "eastasian"

screen encyclopedia:
    
    
    key "e" action Language("english")
    key "j" action Language(None)
    modal True
    key "game_menu" action [Hide('encyclopedia'), Hide('encyc_category'), Hide('encyclopediaentry'), Play("sound", "se_sys/open.ogg")]
    window id "encyclopedia" at basicfade:
        xpadding 0
        ypadding 0
        background None
        add "images/system/encyclopedia/encyc_bg2.png"
        # add "images/system/encyclopedia/encyc_flourish.png" at fpflourishlower
        add "Images/system/encyclopedia/encyc_overlay.png" at fpoverlay
        add "Images/system/encyclopedia/title2_logo1.png" at encyctitletext
        viewport id "encyclopedia":
            mousewheel True
            area (50, 150, 600, 800)
            has vbox spacing 10
            if persistent.encyclopedia1 == True:
                textbutton _("出场人物") action [Show('encyclopedia_cat1'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("菜单介绍") action [Show('encyclopedia_cat2'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            # if persistent.encyclopedia1 == True:
            #     textbutton _("快捷栏介绍") action [Show('encyclopedia_cat3'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("CG操作") action [Show('encyclopedia_cat4'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("其他") action [Show('encyclopedia_cat5'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"


        imagebutton auto "images/system/encyclopedia/back2_%s.png" action [Hide('encyclopedia'), Hide('encyc_category'), Hide('encyclopediaentry'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") xalign 0.05 yalign 0.95






screen encyclopedia_cat1 tag encyc_category:

    window id "encyclopedia_cat1" at basicfade:
        xpadding 0
        ypadding 0
        background None
        has viewport id "encyclopedia":
            mousewheel True
            area (250, 230, 600, 800)
        vbox spacing 10:
            if persistent.encyclopedia1 == True:
                textbutton _("神野凉") action [Show('encyclopedia_sanneajrizda'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("莉斯特") action [Show('encyclopedia_rughzenhaide'), Play("sound", "voice/1000001.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("青木翔子") action [Show('encyclopedia_vhastoralkat'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("日向怜") action [Show('encyclopedia_outerpole'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("一诚总司") action [Show('encyclopedia_outerpole2'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("翔子母亲") action [Show('encyclopedia_outerpole3'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("翔子父亲") action [Show('encyclopedia_outerpole4'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("神秘邻居") action [Show('encyclopedia_outerpole5'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"






screen encyclopedia_cat2 tag encyc_category:

    window id "encyclopedia_cat2" at basicfade:
        xpadding 0
        ypadding 0
        background None
        has viewport id "encyclopedia":
            mousewheel True
            area (250, 230, 600, 800)
        vbox spacing 10:
            if persistent.encyclopedia1 == True:
                textbutton _("TEXT SPEED") action [Show('encyclopedia_mana'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("MESSAGE SKIP") action [Show('encyclopedia_colouredmana'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("AFTER CHOICES") action [Show('encyclopedia_purifiedmana'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("AUTO MESSAGE SPEED") action [Show('encyclopedia_pole'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("UNDER BUTTON") action [Show('encyclopedia_manastream'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"



# screen encyclopedia_cat3 tag encyc_category:

#     window id "encyclopedia_cat3" at basicfade:
#         xpadding 0
#         ypadding 0
#         background None
#         has viewport id "encyclopedia":
#             mousewheel True
#             area (250, 230, 600, 800)
#         vbox spacing 10:
#             if persistent.encyclopedia1 == True:
#                 textbutton _("AUTO") action [Show('encyclopedia_manakravte'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             # if persistent.encyclopedia1 == True:
#             #     if _preferences.language == "japanese":
#             #         textbutton _("シフト") action [Show('encyclopedia_shift'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             # if persistent.encyclopedia1 == True:
#             #     if _preferences.language == "japanese":
#             #         textbutton _("コミット") action [Show('encyclopedia_kommit'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             # if persistent.encyclopedia1 == True:
#             #     if _preferences.language == "japanese":
#             #         textbutton _("ブレス") action [Show('encyclopedia_bless'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             # if persistent.encyclopedia1 == True:
#             #     if _preferences.language == "japanese":
#             #         textbutton _("シグニチャー") action [Show('encyclopedia_signature'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             if persistent.encyclopedia1 == True:
#                 textbutton _("SKIP") action [Show('encyclopedia_transmitteline'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             if persistent.encyclopedia1 == True:
#                 textbutton _("Q·Save") action [Show('encyclopedia_battlekravte'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             if persistent.encyclopedia1 == True:
#                 textbutton _("Q·Load") action [Show('encyclopedia_pathdown'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             if persistent.encyclopedia1 == True:
#                 textbutton _("Menu") action [Show('encyclopedia_kazagenngo'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             if persistent.encyclopedia1 == True:
#                 textbutton _("Blog") action [Show('encyclopedia_minddive'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
#             if persistent.encyclopedia1 == True:
#                 textbutton _("Tool") action [Show('encyclopedia_minddive2'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"


screen encyclopedia_cat4 tag encyc_category:

    window id "encyclopedia_cat4" at basicfade:
        xpadding 0
        ypadding 0
        background None
        has viewport id "encyclopedia":
            mousewheel True
            area (250, 230, 600, 800)
        vbox spacing 10:
            if persistent.encyclopedia1 == True:
                textbutton _("BOOK") action [Show('encyclopedia_sediment'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("MUSIC") action [Show('encyclopedia_transidian'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("TITLE SCREEN") action [Show('encyclopedia_sain'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"


screen encyclopedia_cat5 tag encyc_category:

    window id "encyclopedia_cat5" at basicfade:
        xpadding 0
        ypadding 0
        background None
        has viewport id "encyclopedia":
            mousewheel True
            area (250, 230, 600, 800)
        vbox spacing 10:
            if persistent.encyclopedia1 == True:
                textbutton _("SCREEN") action [Show('encyclopedia_vilseriol'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("Readback") action [Show('encyclopedia_sekqule'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"
            if persistent.encyclopedia1 == True:
                textbutton _("Introduction") action [Show('encyclopedia_mri'), Play("sound", "se_sys/open.ogg")] hovered Play("sound", "se_sys/select.ogg") style "encyclopedia_button"






screen encyclopedia_blank tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("维基百科") size 40 drop_shadow None
        text _("fault -milestone one-") style "encyclopedia_text"
        null height 40
        text _("这里说明了用语")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_sanneajrizda tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("神野凉") size 40 drop_shadow None
        text _("神は涼し") style "encyclopedia_text"
        add "images/system/encyclopedia/staf1.png" xalign 0.95 yalign 0.0
        null height 5
        text _("　樱华中学三年级学生。现在寄宿在青梅竹马青木翔子家中。童年时从小镇搬到了大城市，数年过后又搬回来了。临走前与翔子许下了再会的约定，并借助樱花树作为羁绊的见证。学习成绩好，但是却被翔子说不是“优等生”。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_rughzenhaide tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("莉斯特·F·艾斯特雷亚") size 40 drop_shadow None
        text _("りこの特·F·エースッター雷亚") style "encyclopedia_text"
        add "images/system/encyclopedia/staf2.png" xalign 0.95 yalign 0.0
        null height 5
        text _("　一个外表总是一副冷漠，内心其实很单纯的爱哭鬼。超喜欢七夕的故事，总是出现在凉许愿的樱花树下。拿着大镰刀自称天使，但却是为了实现凉君的愿望而一直在这里等待她。拥有凉和翔子两人儿时的记忆，行为举止时常让凉想起儿时的片段。{p}\n\n   【可以捅你吗！？】")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_vhastoralkat tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("青木翔子") size 40 drop_shadow None
        text _("靑木翔子") style "encyclopedia_text"
        add "images/system/encyclopedia/staf3.png" xalign 0.95 yalign 0.0
        null height 5
        text _("  凉的青梅竹马，傲娇的金发双马尾妹纸。和凉一道在樱花中学三年级上学，在学校担任学生会干部成员，拥有自己的社团和后援团。不擅长应付突发事件，为此经常被捉弄。儿时与离开小镇的凉许下了约定，并继续担任巫女守护者樱花神木。{p}\n\n    【吵死了！笨蛋凉君！】　")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_outerpole tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("日向怜") size 40 drop_shadow None
        text _("ひなた怜") style "encyclopedia_text"
        add "images/system/encyclopedia/staf4.png" xalign 0.95 yalign 0.0
        null height 5
        text _("  就读于樱华中学三年级的学生，翔子社（？）社员之一，是翔子在学校的后援团团长。反感一切接近翔子的男性，时常因为吃醋而哭着跑掉。{p}\n\n   【你......和翔子酱是什么关系！】 ")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_outerpole2 tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("一诚总司") size 40 drop_shadow None
        text _("一誠そうじ") style "encyclopedia_text"
        add "images/system/encyclopedia/staf5.png" xalign 0.95 yalign 0.0
        null height 5
        text _("  同样就读于樱华中学三年级的男子，性格开朗又时常健忘（总是忘记凉的名字）。喜欢摄影，身边经常带着相机，但由于喜欢拍摄一些奇怪的镜头而被翔子踩碎。{p}\n\n   【呐新来的！你和莉斯特酱是什么关系啊？】 ")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_outerpole3 tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("翔子母亲") size 40 drop_shadow None
        text _("翔子のおかあさ") style "encyclopedia_text"
        add "images/system/encyclopedia/staf6.png" xalign 0.95 yalign 0.0
        null height 5
        text _("  翔子的母亲。是个面带笑容连生气的时候都不改色的体贴的人。后因工作关系离开了小镇。{p}\n\n   【啊拉啊拉，真是个好孩子呢。】 ")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_outerpole4 tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("翔子父亲") size 40 drop_shadow None
        text _("翔子のおとうさん") style "encyclopedia_text"
        add "images/system/encyclopedia/staf7.png" xalign 0.95 yalign 0.0
        null height 5
        text _("  翔子的父亲。是一个做事沉稳的人，在家经常帮忙做家务，因此时常裹着一条围裙。很欣赏勤劳肯干的人。后因为工作关系离开了小镇。{p}\n\n   【拜托你了，神野君。】 ")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_outerpole5 tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("神秘邻居") size 40 drop_shadow None
        text _("謎の隣人") style "encyclopedia_text"
        add "images/system/encyclopedia/staf8.png" xalign 0.95 yalign 0.0
        null height 5
        text _("  言行和举止充满神秘感的邻居，在凉搬到翔子家不久便搬到了附近。在莉斯特决定帮助凉君的时候出现，封印了莉斯特的感情，并告诉她关于天使的事情。从年龄上看还是小孩子，却有着高度的觉悟。{p}\n\n   【天使所指的，就是这么回事啊......】 ")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600


screen encyclopedia_innerpole tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("インナーポール") size 40 drop_shadow None
        text _("INNER-POLE") style "encyclopedia_text"
        null height 40
        text _(" 　インナーポール")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_alliance tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("アライアンス") size 40 drop_shadow None
        text _("THE ALLIANCE") style "encyclopedia_text"
        null height 40
        text _(" 　ルゼンハイドを始めとする同盟。サンアリズタ大陸の８割は加盟しており、隣の大陸まで浸透している。各国は平和協定を結んでおり、定められた戒律の元で政治を行なっているが、それぞれの国の文化を尊重する形になっており、不都合が生じた場合退出するのも自由。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_kravters_rank tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("クラフターズランク") size 40 drop_shadow None
        text _("THE ALLIANCE") style "encyclopedia_text"
        null height 40
        text _(" 　ルゼンハイドを始めとする同盟。サンアリズタ大陸の８割は加盟しており、隣の大陸まで浸透している。各国は平和協定を結んでおり、定められた戒律の元で政治を行なっているが、それぞれの国の文化を尊重する形になっており、不都合が生じた場合退出するのも自由。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_kravte_master tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("クラフトマスター") size 40 drop_shadow None
        text _("KRAVTE MASTER") style "encyclopedia_text"
        null height 40
        text _(" 　またの名を『クインクラフター』。４つ全てのマナ系統を全てマスターし、時代に貢献する唯一無二のクラフトを生み出した者のみが授けられる、クインの称号を得たクラフターの事を指す。またクインはアライアンス内の最高勲章である。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_alliance tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("アライアンス") size 40 drop_shadow None
        text _("THE ALLIANCE") style "encyclopedia_text"
        null height 40
        text _(" 　ルゼンハイドの近隣国であり、アライアンスの加盟国（加盟番号２）。アライアンス内では、ルゼンハイドの次の古株。ルゼンハイド王国の古きからの戦友国でもある。ヴァストアルカの協力がなければアライアンスは成立されなかった。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600





screen encyclopedia_mana tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("TEXT SPEED") size 40 drop_shadow None
        text _("文字显现速度") style "encyclopedia_text"
        null height 40
        text _("　通过改变菜单栏TEXT SPEED的进度条，可以改变对话时文字显现的速度，当进度条填满时，文字显现速度最快。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_manastream tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("UNDER BUTTON") size 40 drop_shadow None
        text _("菜单底部选项") style "encyclopedia_text"
        null height 40
        text _("　能够通过点击“18X”或者“General”来切换游戏的18X和全年龄版本，注意该设置一旦运行将会退回开始界面重新载入，请保存好游戏或是与游戏一开始的时候设置。游戏退出后，下次运行默认保留该选择。 ")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_colouredmana tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("MESSAGE SKIP") size 40 drop_shadow None
        text _("信息跳过选项") style "encyclopedia_text"
        null height 40
        text _("　当该选项选择“READ MESSAGE”的时候，只有当已阅读过的内容才会被跳过。当选择了“ALL MESSAGE”的时候，未读过的文字和过场均可跳过。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_purifiedmana tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("AFTER CHOICES") size 40 drop_shadow None
        text _("选项跳读设置") style "encyclopedia_text"
        null height 40
        text _("　用于设置选项之后是否能够进行跳过动作。 ")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_pole tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("AUTO MESSAGE SPEED") size 40 drop_shadow None
        text _("自动浏览速度") style "encyclopedia_text"
        null height 40
        text _("　可通过进度条控制自动阅读浏览游戏的停顿间隙和速度。 ")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_manakravte tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("マナクラフト") size 40 drop_shadow None
        text _("MANAKRAVTE") style "encyclopedia_text"
        null height 40
        text _("　大気のマナ（カラードマナ）と己の体内に秘められたマナ（ピュリファイドマナ）を使用し、様々な現象を起こす技術。戦闘から医療、農業から情報技術まで様々な分野で社会を変えつつある。マナクラフトは大きく分けて、即座にブレスしなければならない『オフィア』と、時間をかけゆっくりとブレスする『ディヴィオ』の二種類が存在する。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_shift tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("シフト") size 40 drop_shadow None
        text _("SHIFT") style "encyclopedia_text"
        null height 40
        text _("　周囲のマナを任意のマナの比率に変動させる技術。大抵の場合は、シナジーを誘発させるために使われる。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_kommit tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("コミット") size 40 drop_shadow None
        text _("KOMMIT") style "encyclopedia_text"
        null height 40
        text _("　シフトで動こした外気のマナや、自分のマナ等を一定の場所に固定させる技術。コミットされたマナはコミットしたクラフターが意図的に解除するか、任意のクラフトを発動しマナを消費するまで、解くことは普通出来ない。無理矢理コミットを壊す方法も存在するが、膨大な量のマナを使用する上時間がかかる。基本的に大きな範囲のマナをコミットするのは非情に難しいとされており、それなりの技術が必要となる。コミットには色々な細工することが可能であり、踏み入れた相手の体内のマナバランスを崩し、殺害すること等も可能である。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_bless tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("ブレス") size 40 drop_shadow None
        text _("BLESS") style "encyclopedia_text"
        null height 40
        text _("　マナクラフトを発動する際のプロセスの名称。言葉そのものは『祝福を』という意味を持つ。由来はヴィビリアの聖書に登場する『マナの神々の力を借り、己のマナを通じ、現世に奇跡の祝福（bless）を』という話の契約の儀式から来ている。マナクラフトはこの契約を模範した技術とされているため、クラフトを使う際は加護の意も込め、ブレスと呼ばれている。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_battlekravte tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("バトルクラフト") size 40 drop_shadow None
        text _("BATTLE KRAVTE") style "encyclopedia_text"
        null height 40
        text _("　戦闘で使わるクラフト全般。オフィア系のクラフトが殆どであるため、特殊な訓練を重ねなければ実戦では使えない。バトルクラフトを使う人間は、体内のピュリファイドマナをバトルクラフト用に変質させる『エグザルテーション』と呼ばれる儀式の一種を受けている事が多い。この儀式は、体内のマナが子供から大人へ変わる最も不安定な時期を狙い強行的に変質させるものであるため、思春期の間に受けなければならない。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_signature tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("シグニチャー") size 40 drop_shadow None
        text _("SIGNATURE") style "encyclopedia_text"
        null height 40
        text _("　それぞれの人間が持つマナの特別な質。指紋のようなもので同じシグニチャーを持つ人間は二人として存在しないが、特例もある。クラフトを使うと必ずどこかにシグニチャーが残るため、これを見てクラフターを判定することが出来る。シグニチャーをマスク（偽造）出来るクラフターもいる。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600


screen encyclopedia_sekqule tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("READBACK") size 40 drop_shadow None
        text _("剧情回放") style "encyclopedia_text"
        null height 40
        text _("　通过鼠标滚轮或是手机点击屏幕左半部分打开剧情回放，可以查看之前的部分对话和剧情内容。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600



screen encyclopedia_blank tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("アンサイクロペディア") size 40 drop_shadow None
        text _("fault -milestone one-") style "encyclopedia_text"
        null height 40
        text _("ここに用語説明が入ります")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600






screen encyclopedia_kazagenngo tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("風言語") size 40 drop_shadow None
        text _("AERO-LINGUISTICS") style "encyclopedia_text"
        null height 40
        text _("　己のマナを使い、発する言葉を音の波長ではなく、意志の波長に変換するコミュニケーションクラフトの一種。外交を重視する政治態勢を築くためルゼンハイド６世により開発された。ヒアリングは話してるうちに後から追いついてくる仕組みになっており会話の初めは一方通行。どれだけ迅速にこの会話の同調が出来るかはその者のコミュニケーション能力次第であり、当人の言語力のセンスが試される。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_pathdown tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("パスダウン") size 40 drop_shadow None
        text _("PATH-DOWN") style "encyclopedia_text"
        null height 40
        text _("　マナポールのエネルギーを借りて行う、王族しか使えない記憶移転のクラフト。前代の経験から記憶や意志を直接子孫に受け継がすことが出来る。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_transmitteline tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("通信ライン") size 40 drop_shadow None
        text _("TRANSMITTE-LINE") style "encyclopedia_text"
        null height 40
        text _("音の波長を伝達するために人工的に引くマナラインの一種。一般的には互いのシグニチャーを受け入れたもの達しか引けないが例外もある。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_minddive tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("マインドダイブ") size 40 drop_shadow None
        text _("MIND-DIVE") style "encyclopedia_text"
        null height 40
        text _("　王族特有のクラフトの一つ。他人の記憶のマナを直接読み取ることが出来る。相手側の意識と無意識がどれだけ記憶を見せるか否かを判断する権限を持つため、見せたくない記憶がある場合、マインドダイブした者でもその閉ざされた記憶を読み取ることは出来ない。その代わり記憶のマナを直接読み取っているため、情報を改竄することが出来ない。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600




screen encyclopedia_sain tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("TITLE SCREEN") size 40 drop_shadow None
        text _("返回") style "encyclopedia_text"
        null height 40
        text _("　通过该按钮可以退出ALBUM界面。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_sediment tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("BOOK") size 40 drop_shadow None
        text _("CG鉴赏") style "encyclopedia_text"
        null height 40
        text _("　可以在此浏览游戏过程中出现的CG图片和视频。游戏出现的CG会自动解锁，通过点击图例可以分段浏览图片。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_transidian tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("MUSIC") size 40 drop_shadow None
        text _("音乐鉴赏") style "encyclopedia_text"
        null height 40
        text _("　通过点击留声机可以打开音乐鉴赏，欣赏游戏过程中的bgm。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600


screen encyclopedia_mri tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("INTRODUCTION") size 40 drop_shadow None
        text _("其他介绍") style "encyclopedia_text"
        null height 40
        text _("　游戏的运行方式和大多数gal游戏相似，具体的细节可使用菜单的ENCYCLOPEDIA来打开介绍查看，祝您游戏愉快！")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600







screen encyclopedia_vilseriol tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("SCREEN") size 40 drop_shadow None
        text _("界面优化") style "encyclopedia_text"
        null height 40
        text _("　游戏进行过程中会分不同的阶段（四季），不同的阶段主界面背景会随之变化，通关第一部分之后会显示新的按钮进入下一部分游戏并解锁新的CG。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600

screen encyclopedia_quinorder tag encyclopediaentry:

    viewport id "vp" at quickfade:
        mousewheel True
        area (550, 50, 585, 600)
        has vbox spacing 10
        text _("クインオーダー") size 40 drop_shadow None
        text _("QUIN-KRAVTER'S CHIVLARIC ORDER") style "encyclopedia_text"
        null height 40
        text _("　ルゼンハイド国の騎士団。騎士団とは昔の名誉システムの名前を借りたものであり、その実態はないと一般的には思われているが、実際はルゼンハイド国の諜報機関として機能している。多くのメンバーがクアッド以上の称号を得たクラフトの達人。")
    vbar value YScrollValue("vp") xpos 1150 ypos 50 ymaximum 600







init -2 python:

    style.encyclopedia_button = Style(style.default)
    style.encyclopedia_button.insensitive_background = ("images/system/encyclopedia/button_idle.png")
    style.encyclopedia_button.idle_background = ("images/system/encyclopedia/button_idle.png")
    style.encyclopedia_button.hover_background = ("images/system/encyclopedia/button_hover.png")
    style.encyclopedia_button.xminimum = 170
    style.encyclopedia_button.yminimum = 21
    style.encyclopedia_button_text.color = "#745a4b"
    style.encyclopedia_button_text.drop_shadow = None
    style.encyclopedia_button_text.size = 18
    style.encyclopedia_button_text.xalign = 1.0



    style.encyclopedia_button_secondary = Style(style.default)
    style.encyclopedia_button_secondary_text.color = "#FFFFFF"
    style.encyclopedia_button_secondary_text.drop_shadow = (2,2)
    style.encyclopedia_button_secondary_text.size = 48
    style.encyclopedia_button_secondary_text.xalign = 0.0



    style.encyclopedia_text.color = "#FFFFFF"
    style.encyclopedia_text.drop_shadow = None
    style.encyclopedia_text.size = 18
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
