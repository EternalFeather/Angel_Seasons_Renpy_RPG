
define investigation.preg1 = _("{image=m1}点击推进剧情（提示 ： 下角方的菜单中有功能辅助按钮，可以方便游戏时使用。）")
define investigation.preg2 = _("{image=m1}点击带有黄色下划线的字体即可跳转至相关介绍，能够帮助玩家大大们更好地理解世界观哟。")
define investigation.preg3 = _("{image=m1}点击地点触发剧情。")
define investigation.preg4 = _("{image=m1}点击人物查看/使用道具。")
define investigation.preg5 = _("{image=m2}点击下方菜单唤出战时菜单使用「煮鸡蛋」恢复生命值。")
define investigation.hint1 = _("{image=m1}点击指定人物或道具即可激活操作。")
define investigation.hint2 = _("{image=m1}点击弗兰可激活菜单。")
define investigation.hint3 = _("{image=m1}拖动符文到魔法阵中激活召唤仪式。")
define investigation.hint_xz = _("{image=m1}点击青木翔子可激活菜单。")
define investigation.hint_szl = _("{image=m1}想办法对水之濑凛的太刀做些手脚。")

image m1 = imagescale(2700)("9i/interface/m1.png")
image m2 = imagescale(2700)("9i/interface/m2.png")

screen investigation_popup(string):
    zorder + 1
    label string style_prefix "iv_popup" at basicfade
init:
    style iv_popup_label is default:
        xcenter 0.5
        yalign 0.1
        xsize scale(990)
        yminimum scale(120)
        background Frame("9i/interface/investigation/hint frame.png")
    style iv_popup_label_text is text:
        xcenter 0.5
        ycenter 0.5
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(18)
        color "#fff"
        outlines [(scale(3.0), "#4f4f4f")]

screen investigation_menu():
    tag iv
    modal True
    zorder -2

    default parse = investigation.index[investigation.label]
    default ivmenu = parse.menu
    default button_positions = [
        (scale(30), scale(0)),
        (scale(91), scale(109)),
        (scale(0), scale(109)*2),
        (scale(60), scale(109)*3),
        (scale(-29), scale(109)*4),
        (scale(-500), scale(-50)),
        (scale(-439), scale(59)),
        (scale(-530), scale(168)),
        (scale(-469), scale(277)),
        (scale(-559), scale(386)),
    ]
    $ pos_iter = iter(button_positions)
    $ idx_iter = iter(xrange(len(button_positions)))
    $ tf_mult = (-1 if ivmenu.screen_direction == 'left' else 1)

    key "game_menu" action investigation.ExitIvMenu()

    on "show" action [
        Hide("iv_item_notify"),
        Play(channel="audio", file="9i/interface/click1.ogg")
    ]

    use aerolinguistics()
    transform at iv_menu_inter(xzoom=tf_mult), unscale_by_layer(layer=ivmenu.screen_layer):
        fixed style_prefix "iv" at iv_pos(
            screen_pos=eval(ivmenu.screen_pos),
            screen_direction=ivmenu.screen_direction,
            xpos_offset=0.08,
            ypos_offset=-0.47):
            textbutton _("{#iv}通信") pos next(pos_iter):
                at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                action Show(
                    "investigation_call_menu",
                    _layer=ivmenu.screen_layer)
                sensitive parse.call_records
            textbutton _("{#iv}物品") pos next(pos_iter):
                at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                action Show(
                    "investigation_item_menu",
                    _layer=ivmenu.screen_layer)
                sensitive investigation.inventory
            textbutton _("{#iv}移动") pos next(pos_iter):
                at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                action Show(
                    "investigation_move_menu",
                    _layer=ivmenu.screen_layer)
                sensitive ivmenu.move_records
            textbutton _("{#iv}就寝") pos next(pos_iter):
                if ivmenu.sleep_label:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                else:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult), invisible
                action investigation.IvJump(ivmenu.sleep_label)
                sensitive bool(ivmenu.sleep_label)
                activate_sound "9i/interface/click1.ogg"
            textbutton _("{#iv}时空之境") pos next(pos_iter):
                if ivmenu.memory_label:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                else:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult), invisible
                action investigation.IvJump(ivmenu.memory_label)
                sensitive bool(ivmenu.memory_label)
                activate_sound "9i/interface/click1.ogg"
            textbutton _("{#iv}商店") pos next(pos_iter):
                if ivmenu.shop_label:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                else:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult), invisible
                action investigation.IvJump(ivmenu.shop_label)
                sensitive bool(ivmenu.shop_label)
                activate_sound "9i/interface/click1.ogg"
            textbutton _("{#iv}队伍") pos next(pos_iter):
                if ivmenu.member_label:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                else:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult), invisible
                action investigation.IvJump(ivmenu.member_label)
                sensitive bool(ivmenu.member_label)
                activate_sound "9i/interface/click1.ogg"
            textbutton _("{#iv}异界") pos next(pos_iter):
                if ivmenu.teleport_label:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                else:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult), invisible
                action investigation.IvJump(ivmenu.teleport_label)
                sensitive bool(ivmenu.teleport_label)
                activate_sound "9i/interface/click1.ogg"
            textbutton _("{#iv}召唤") pos next(pos_iter):
                if ivmenu.callback_label:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                else:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult), invisible
                action investigation.IvJump(ivmenu.callback_label)
                sensitive bool(ivmenu.callback_label)
                activate_sound "9i/interface/click1.ogg"
            textbutton _("{#iv}养成屋") pos next(pos_iter):
                if ivmenu.room_label:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult)
                else:
                    at iv_menu_button_show(idx=next(idx_iter), xzoom=tf_mult), invisible
                action investigation.IvJump(ivmenu.room_label)
                sensitive bool(ivmenu.room_label)
                activate_sound "9i/interface/click1.ogg"
            

    $ del pos_iter
    $ del idx_iter

init:
    transform iv_pos(screen_pos, screen_direction, xpos_offset=0.0, ypos_offset=0.0):
        xpos (screen_pos[0]
            + xpos_offset * (-1.0
                if screen_direction == 'left'
                else 1.0))
        ypos (screen_pos[1] + ypos_offset)
        xanchor (1.0
            if screen_direction == 'left'
            else 0.0)
        yanchor 1.0

    transform iv_menu_button_show(idx, xzoom=1):
        alpha 0
        xoffset scale(30 * xzoom)
        yoffset scale(-30)
        (0.05 * idx)
        parallel:
            linear 0.1 alpha 1
        parallel:
            subpixel True
            easein_cubic 0.2 xoffset scale(0) yoffset scale(0)
    transform iv_menu_inter(xzoom=1):
        on replace:
            alpha 0
            linear 0.2 alpha 1
        on replaced:
            0.15
            alpha 0
        on hide:
            parallel:
                linear 0.2 alpha 0
            parallel:
                subpixel True
                easeout_cubic 0.2 xoffset scale(-30 * xzoom) yoffset scale(30)

    style iv_fixed is fixed:
        xfit True
        yfit True
    style iv_button is default:
        xsize int(scale(446.5))
        ysize int(scale(171.5))
        background imagescale(1080)("9i/interface/investigation/menu button.png")
        hover_background Fixed(
            imagescale(1080)("9i/interface/investigation/menu button.png"),
            imagescale(1080)("9i/interface/investigation/menu button hover.png"))
        hover_sound "9i/interface/click3.ogg"
    style iv_button_text is text:
        xcenter scale(187)
        ycenter 0.49
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(27)
        color "#eddc9a"
        insensitive_color "#eddc9a7f"
        outlines [(scale(2.0), "#0d0d23", scale(0.0), scale(1.5))]


init:
    transform iv_submenu_inter:
        on show:
            iv_submenu_show
        on replace:
            iv_submenu_show
        on replaced:
            iv_submenu_hide
        on hide:
            iv_submenu_hide
    transform iv_submenu_show:
        subpixel True
        alpha 0
        zoom 0.5
        parallel:
            linear 0.15 alpha 1
        parallel:
            easein_cubic 0.15 zoom 1.0
    transform iv_submenu_hide:
        subpixel True
        parallel:
            linear 0.15 alpha 0
        parallel:
            easeout_cubic 0.15 zoom 0.5
    transform iv_submenu_inner_show:
        alpha 0
        0.1
        linear 0.15 alpha 1

screen investigation_move_menu():
    tag iv
    modal True
    zorder -1
    default parse = investigation.index[investigation.label]
    default ivmenu = parse.menu
    key "game_menu" action Show(
        "investigation_menu",
        _layer=ivmenu.screen_layer)

    use aerolinguistics()
    transform at unscale_by_layer(layer=ivmenu.screen_layer):
        frame style_prefix "iv_move" at iv_pos(screen_pos=eval(ivmenu.screen_pos), screen_direction=ivmenu.screen_direction, xpos_offset=0.05, ypos_offset=-0.42), iv_submenu_inter:
            label _("{#iv}位置")
            vbox:
                for caption, label in ivmenu.move_records:
                    textbutton eval(caption) action investigation.IvJump(label)
init:
    style iv_move_frame is default:
        xsize scale(629)
        ysize int(scale(552.5))
        background imagescale(1080)("9i/interface/investigation/move frame.png")
    style iv_move_label is default:
        xcenter 0.5
        ycenter scale(72)
    style iv_move_label_text is text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(40)
        color "#402d24"
    style iv_move_vbox is vbox:
        xcenter 0.5
        ypos scale(151)
    style iv_move_button is default:
        xcenter 0.5
        xfill True
        hover_background imagescale(1080)(
            Image(
                "9i/interface/investigation/move button hover.png",
                xcenter=0.48,
                ycenter=0.5))
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click3.ogg"
    style iv_move_button_text is text:
        xcenter 0.5
        ycenter 0.52
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(30)
        color "#402d24"
        outlines [(scale(6.0), "#0000")]
        hover_color "#eddc9a"
        hover_outlines [
            (scale(6.0), "#ff881f07"),
            (scale(4.5), "#ff881f17"),
            (scale(3.0), "#ff881f2f"),
            (scale(1.5), "#ff881f3f")
        ]
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click3.ogg"

screen investigation_call_menu():
    tag iv
    modal True
    zorder -1

    default parse = investigation.index[investigation.label]
    default ivmenu = parse.menu

    key "game_menu" action Show(
        "investigation_menu",
        _layer=ivmenu.screen_layer)

    on "show" action Play(channel="audio", file="9i/interface/paper_slide.ogg")
    on "replace" action Play(channel="audio", file="9i/interface/paper_slide.ogg")
    on "hide" action Play(channel="audio", file="9i/interface/paper_slide_reverse.ogg")
    on "replaced" action Play(channel="audio", file="9i/interface/paper_slide_reverse.ogg")

    transform at unscale_by_layer(layer=ivmenu.screen_layer):
        frame style_prefix "iv_call" at iv_pos(screen_pos=eval(ivmenu.screen_pos), screen_direction=ivmenu.screen_direction, xpos_offset=0.05, ypos_offset=-0.33), iv_submenu_inter:
            has fixed at iv_submenu_inner_show
            label _("{#iv}通讯录")
            use investigation_call_menu_button(record=parse.call_records.get('xz_dsf_b3'), pos=(pscale(197.5), pscale(121.5)), style="iv_call_button")



            use investigation_call_menu_button(record=parse.call_records.get('liuli_dsf_b2'), pos=(pscale(370.5), pscale(121.5)), style="iv_call_button")



            use investigation_call_menu_button(record=parse.call_records.get('yj_dsf_b1'), pos=(pscale(544.5), pscale(121.5)), style="iv_call_yj_button")



            use investigation_call_menu_button(record=parse.call_records.get('lhx_dsf_b2'), pos=(pscale(718), pscale(121.5)), style="iv_call_lhx_button")



            use investigation_call_menu_button(record=parse.call_records.get('qcls_zf_b1'), pos=(pscale(294.5), pscale(431.5)), style="iv_call_button")



            use investigation_call_menu_button(record=parse.call_records.get('szl_dsf_b2'), pos=(pscale(468.5), pscale(432.5)), style="iv_call_button")



            use investigation_call_menu_button(record=parse.call_records.get('jsqd_dsf_b1'), pos=(pscale(643.5), pscale(431.5)), style="iv_call_button")

            textbutton _("{#iv}close") style "iv_call_close_button":
                action Show(
                    "investigation_menu",
                    _layer=ivmenu.screen_layer
                )


screen investigation_call_menu_button(record, pos, style):
    button pos pos:
        if record:
            action investigation.IvJump(record.label)
            if (eval(record.showif_expr) if record.showif_expr else True):
                style style
            else:
                style "iv_call_button"
            if record.sensitive_expr:
                sensitive eval(record.sensitive_expr)
        else:
            style "iv_call_button"
init:
    style iv_call_frame is default:
        xsize scale(1087)
        ysize scale(798)
        background imagescale(1080)("9i/interface/investigation/call frame.png")
    style iv_call_label is default:
        xcenter 0.5
        ycenter scale(87)
        xsize scale(349)
        ysize int(scale(40.5))
        background imagescale(1080)("9i/interface/investigation/call caption.png")
    style iv_call_label_text is text:
        xcenter 0.5
        ycenter 0.55
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(24)
        color "#eddc9a"
        outlines [
            (scale(2.0), "#0e0e24"),
            (scale(2.0), "#0e0e24", scale(0.0), scale(1.5))
        ]
    style iv_call_button is default:
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click3.ogg"
        child imagescale(1080)("9i/interface/investigation/call button.png")
        foreground imagescale(1080)(
            Image(
                "9i/interface/investigation/call pin.png",
                pos=(pscale(56), pscale(-15.5))))
        hover_foreground Fixed(
            imagescale(1080)("9i/interface/investigation/call button hover.png"),
            imagescale(1080)(
                Image(
                    "9i/interface/investigation/call pin.png",
                    pos=(pscale(56), pscale(-15.5)))),
            fit_first=True)
        
    style iv_call_yj_button is iv_call_button:
        child imagescale(1080)(
            "9i/interface/investigation/call button yj.png")
        insensitive_child imagescale(1080)(
            "9i/interface/investigation/call button yj disabled.png")
    style iv_call_lhx_button is iv_call_button:
        child imagescale(1080)(
            "9i/interface/investigation/call button lhx.png")
        insensitive_child imagescale(1080)(
            "9i/interface/investigation/call button lhx disabled.png")

screen investigation_call_nvl(dialogue, items=None, animation=None):
    tag iv
    zorder -1

    default parse = investigation.index.get(investigation.label)
    default ivmenu = (investigation.menu or parse.menu)
    default callee = renpy.python.py_eval(investigation.callee)
    python:
        callee_imspec = None
        if investigation.callee is not None:
            callee_imspec = ' '.join(
                (
                    (investigation.callee,)
                    + renpy.game.context().images.get_attributes(
                        layer='master',
                        tag=investigation.callee)
                )
                or ())

    key "rollback" action NullAction()

    use aerolinguistics()
    transform at unscale_by_layer(layer=ivmenu.screen_layer):
        fixed fit_first True style_prefix "iv_call_nvl":
            at (animation or iv_call_no_inter), iv_pos(screen_pos=eval(ivmenu.screen_pos), screen_direction=ivmenu.screen_direction, xpos_offset=0.05, ypos_offset=-0.33)
            frame style "iv_call_nvl_dialogue_frame":
                has viewport mousewheel True scrollbars None yinitial 1.0
                vbox:
                    null height scale(81)
                    for who, what, who_id, what_id, window_id in dialogue[:-2]:
                        transform at iv_call_bubble_prev_show(who, callee):
                            window id window_id:
                                style investigation.call_window_style(who, callee)
                                text what id what_id
                    for who, what, who_id, what_id, window_id in dialogue[-2:-1]:
                        transform at (
                            iv_call_bubble_prev_show(who, callee)
                            if items
                            else iv_call_bubble_to_prev_show(who, callee)):
                            window id window_id:
                                style investigation.call_window_style(who, callee)
                                text what id what_id
                    for who, what, who_id, what_id, window_id in dialogue[-1:]:
                        transform at (
                            iv_call_bubble_to_prev_show(who, callee)
                            if items
                            else iv_call_bubble_current_show(who, callee)):
                            window id window_id:
                                style investigation.call_window_style(who, callee)
                                text what id what_id
                    null height scale(81)
            if items:
                hbox style_prefix "iv_call_nvl_menu":
                    for caption, action, chosen in items:
                        textbutton caption action action at iv_call_button_show
            if investigation.callee and ivmenu.screen_direction and callee_imspec:
                frame style_prefix "iv_call_actor" at iv_call_actor_pos(ivmenu.screen_direction):


                    fixed at (
                        iv_call_actor_dir(ivmenu.screen_direction),
                        renpy.partial(
                            AlphaMask,
                            mask=imagescale(1080)(
                                "9i/interface/investigation/actor mask.png"))):
                        add callee_imspec at iv_call_actor_sprite(investigation.callee)
                    label callee.name
init python in investigation:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    @renpy.pure
    def call_window_style(who, callee):
        is_callee_name = (

            who == callee.name
            or any(
                who == stl.translations.get(callee.name)
                for stl in renpy.game.script.translator.strings.itervalues()))
        return ('iv_call_send_window'
            if not is_callee_name
            else 'iv_call_recv_window')

    @renpy.pure
    def call_window_xalign(who, callee):
        ivmenu = (menu or index[label].menu)
        is_callee_name = (
            who == callee.name
            or any(
                who == stl.translations.get(callee.name)
                for stl in renpy.game.script.translator.strings.itervalues()))
        return float(
            not is_callee_name
            if ivmenu.screen_direction != 'right'
            else is_callee_name)
init -999 python in investigation:
    call_actor_xpos = _dict()
    call_actor_ypos = _dict()
    renpy.const('investigation.call_actor_xpos')
    renpy.const('investigation.call_actor_ypos')
init:


    transform iv_call_no_inter:
        subpixel True
        zoom 1.0
    transform iv_call_actor_pos(direction):
        xpos (pscale(-214.5) if direction == 'left' else pscale(946.5))
    transform iv_call_actor_dir(direction):
        xzoom (1 if direction == 'left' else -1)
    transform iv_call_actor_sprite(tag):
        subpixel True
        xpos investigation.call_actor_xpos.get(tag, 0.5)
        ypos investigation.call_actor_ypos.get(tag, 0.1)
        yanchor 0.0
        xzoom -1
        zoom 1.15

    transform iv_call_bubble_prev_show(who, callee):
        xalign investigation.call_window_xalign(who, callee)
        alpha 0.7
    transform iv_call_bubble_to_prev_show(who, callee):
        xalign investigation.call_window_xalign(who, callee)
        easein 0.2 alpha 0.7
    transform iv_call_bubble_current_show(who, callee):
        crop_relative True
        xalign investigation.call_window_xalign(who, callee)
        alpha 0
        crop (investigation.call_window_xalign(who, callee), 0.0, 0.0, 1.0)
        parallel:
            linear 0.2 alpha 1
        parallel:
            subpixel True
            power_in_time_warp_real 0.8 crop (0.0, 0.0, 1.0, 1.0)
    transform iv_call_button_show:
        subpixel True
        crop_relative True
        alpha 0.5
        crop (0.5, 0.0, 0.0, 1.0)
        parallel:
            linear 0.3 alpha 1
        parallel:
            subpixel True
            crop_relative True
            power_in_time_warp_real 0.8 crop (0.0, 0.0, 1.0, 1.0)

    style iv_call_text is text:
        xmaximum scale(465)
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(30)
    style iv_call_hyperlink is iv_call_text:
        color encyclopedia.hyperlink_color
        underline True

    style iv_call_nvl_dialogue_frame is iv_call_frame:
        xpadding scale(188)
        ypadding scale(12)
        foreground imagescale(1080)("9i/interface/investigation/call mask.png")
    style iv_call_nvl_vbox is vbox:
        xfill True
        spacing scale(37)
    style iv_call_dialogue is iv_call_text:
        line_leading scale(3)
        line_spacing scale(3)
        line_overlap_split scale(6)
        color "#372710"
        hyperlink_functions encyclopedia.get_hyperlink_functions(
            style.iv_call_hyperlink)
    style iv_call_window is default:
        xmaximum scale(600)
        xpadding scale(39)
        ypadding scale(21)
    style iv_call_send_window is iv_call_window:
        background Frame("9i/interface/investigation/window send.png")
    style iv_call_nvl_menu_hbox is hbox:
        xcenter 0.5
        ycenter 0.9
    style iv_call_nvl_menu_button is default:
        xcenter 0.5
        ycenter 0.5
        xminimum scale(236)
        background imagescale(1080)(
            Image(
                "9i/interface/investigation/close button.png",
                yalign=1.0))
        hover_background imagescale(1080)(
            Image(
                "9i/interface/investigation/close button hover.png",
                yalign=1.0))
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click3.ogg"
    style iv_call_nvl_menu_button_text is iv_call_text:
        xcenter 0.5
        ycenter 0.5
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(24)
        color "#ffe8c4"
        outlines [(scale(2.0), "#2b2d21")]
        hover_color "#ffd799"
        hover_outlines [(scale(2.0), "#e7910a")]
    style iv_call_recv_window is iv_call_window:
        background Frame("9i/interface/investigation/window recv.png")
    style iv_call_actor_frame is default:
        xpos int(scale(-214.5))
        ypos int(scale(88.5))
        xsize scale(355)
        ysize scale(606)
        background imagescale(1080)("9i/interface/investigation/actor frame.png")
    style iv_call_actor_label is default:
        xcenter 0.49
        ycenter scale(541)
        xsize int(scale(327.5))
        ysize scale(60)
        background imagescale(1080)("9i/interface/investigation/actor caption.png")
    style iv_call_actor_label_text is text:
        xcenter 0.5
        ycenter 0.52
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(27)
        color "#eddc9a"
        outlines [
            (scale(2.0), "#0d0d23"),
            (scale(2.0), "#0d0d23", scale(0.0), scale(1.5))
        ]

screen investigation_item_menu():
    tag iv
    modal True
    zorder -1

    default parse = investigation.index[investigation.label]
    default ivmenu = parse.menu

    default item = investigation.item_registry[investigation.inventory[0]]

    key "game_menu" action Show(
        "investigation_menu",
        _layer=ivmenu.screen_layer)

    on "show" action Play(channel="audio", file="9i/interface/paper_slide.ogg")
    on "replace" action Play(channel="audio", file="9i/interface/paper_slide.ogg")
    on "hide" action Play(channel="audio", file="9i/interface/paper_slide_reverse.ogg")
    on "replaced" action Play(channel="audio", file="9i/interface/paper_slide_reverse.ogg")

    use aerolinguistics()
    transform at unscale_by_layer(layer=ivmenu.screen_layer):
        fixed style_prefix "iv" at iv_pos(screen_pos=eval(ivmenu.screen_pos), screen_direction=ivmenu.screen_direction, xpos_offset=0.05, ypos_offset=-0.33), iv_submenu_inter:
            frame style_prefix "iv_item_info":
                has fixed at iv_submenu_inner_show, Flatten
                label "[item.name]"
                textbutton _("{#iv}使用") style "iv_item_info_red_button":
                    if (investigation.label in item.use_button):
                        action [
                            Hide("investigation_item_menu"),
                            investigation.IvJump(
                                item.use_button[investigation.label].label)
                        ]
                        sensitive (
                            eval(item.use_button[investigation.label].condition)
                            if item.use_button[investigation.label].condition
                            else True)
                textbutton _("{#iv}查看") style "iv_item_info_blue_button":
                    if (investigation.label in item.examine_button):
                        action [
                            Hide("investigation_item_menu"),
                            investigation.IvJump(
                                item.examine_button[investigation.label].label)
                        ]
                        sensitive (
                            eval(item.examine_button[investigation.label].condition)
                            if item.examine_button[investigation.label].condition
                            else True)
                frame style "iv_item_info_icon_frame":
                    add "[item.icon]" at iv_item_icon
                text "[item.description]" style "iv_item_info_description_text"
                textbutton _("{#iv}close") style "iv_item_close_button":
                    action Show(
                        "investigation_menu",
                        _layer=ivmenu.screen_layer
                    )
            frame style_prefix "iv_item_list":
                has hbox at iv_submenu_inner_show
                for spec in investigation.inventory:
                    if spec not in ["fire tiny", "water tiny", "ice tiny", "light tiny", "wind tiny", "rock tiny", "fire big", "water big", "ice big", "light big", "wind big", "rock big"]:
                        $ list_item = investigation.item_registry[spec]
                        button:
                            action SetScreenVariable('item', value=list_item)
                            add list_item.icon at iv_item_list_button
                            selected list_item == item
init:
    transform iv_item_icon:
        xcenter 0.5
        ycenter 0.5
        size (scale(183), scale(183))
    transform iv_item_list_button:
        xcenter 0.5
        ycenter 0.5
        size (scale(72), scale(72))

    style iv_item_text is text:
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(24)
        color "#402d24"
    style iv_item_frame is default:
        xsize scale(240)
        ysize scale(240)
        background imagescale(1080)("9i/interface/investigation/item frame.png")

    style iv_item_info_frame is default:
        xsize int(scale(904.5))
        ysize int(scale(631.5))
        background imagescale(1080)(
            "9i/interface/investigation/inventory item frame.png")
    style iv_item_info_label is default:
        xcenter 0.5
        ycenter scale(74)
    style iv_item_info_icon_frame is iv_item_frame:
        xcenter 0.5
        ypos int(scale(133.5))
        foreground imagescale(1080)(
            Image(
                "9i/interface/investigation/item pin.png",
                xpos=int(scale(104.5)),
                ypos=int(scale(-15.5))))
    style iv_item_info_label_text is iv_item_text:
        size scale(43)
    style iv_item_info_description_text is iv_item_text:
        xpos scale(78)
        ypos scale(388)
        xmaximum scale(744)
    style iv_item_info_button_text is iv_item_text:
        xcenter 0.5
        ycenter 0.52
        size scale(32)
        color "#fdf3d3"
        outlines [
            (scale(2.0), "#331b0b"),
            (scale(2.0), "#331b0b", scale(0.0), scale(1.5))
        ]
    style iv_item_info_red_button is default:
        xpos scale(135)
        ypos scale(230)
        xsize scale(253)
        ysize scale(78)
        background imagescale(1080)("9i/interface/investigation/item button red.png")
        insensitive_background imagescale(1080)(im.Grayscale("9i/interface/investigation/item button red.png"))
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click3.ogg"
    style iv_item_info_red_button_text is iv_item_info_button_text:
        xcenter scale(111)
        hover_outlines [
            (scale(2.0), "#ffaf16"),
            (scale(2.0), "#ffaf16", scale(0.0), scale(1.5))
        ]
    style iv_item_info_blue_button is default:
        xpos scale(514)
        ypos scale(224)
        xsize scale(261)
        ysize scale(84)
        background imagescale(1080)("9i/interface/investigation/item button blue.png")
        insensitive_background imagescale(1080)(im.Grayscale("9i/interface/investigation/item button blue.png"))
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click3.ogg"
    style iv_item_close_button is default:
        xcenter 0.5
        ycenter 0.85
        xminimum scale(236)
        background imagescale(1080)(
            Image(
                "9i/interface/investigation/close button.png",
                yalign=1.0))
        hover_background imagescale(1080)(
            Image(
                "9i/interface/investigation/close button hover.png",
                yalign=1.0))
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click3.ogg"
    style iv_call_close_button is default:
        xcenter 0.5
        ycenter 0.95
        xminimum scale(236)
        background imagescale(1080)(
            Image(
                "9i/interface/investigation/close button.png",
                yalign=1.0))
        hover_background imagescale(1080)(
            Image(
                "9i/interface/investigation/close button hover.png",
                yalign=1.0))
        activate_sound "9i/interface/click1.ogg"
        hover_sound "9i/interface/click3.ogg"
    style iv_item_info_blue_button_text is iv_item_info_button_text:
        xcenter scale(150)
        hover_outlines [
            (scale(2.0), "#23d3ff"),
            (scale(2.0), "#23d3ff", scale(0.0), scale(1.5))
        ]
    style iv_item_info_buttons_hbox is hbox:
        xcenter 0.5
        ycenter 0.85
    style iv_item_list_frame is default:
        ypos int(scale(630.5))
        xsize int(scale(904.5))
        ysize scale(137)
        background imagescale(1080)(
            "9i/interface/investigation/inventory list frame.png")
    style iv_item_list_hbox is hbox:
        xcenter 0.5
        ycenter 0.5
    style iv_item_list_button is default:
        selected_foreground imagescale(1080)(
            Image(
                "9i/interface/investigation/inventory list button hover.png",
                xcenter=scale(36),
                ycenter=scale(36)))


screen iv_item_notify(spec):
    zorder +1

    default item = investigation.item_registry[spec]

    on "show" action Play("audio", "9i/interface/bwoop.mp3")

    timer 3.0 action Hide("iv_item_notify")
    transform at iv_item_notify_inter:
        frame style "iv_item_frame":
            add item.icon at iv_item_icon

init:
    transform iv_item_notify_inter:
        xcenter 0.5
        ycenter 0.18
        on show:
            subpixel True
            alpha 0
            zoom 0.0
            parallel:
                linear 0.2 alpha 1
            parallel:
                subpixel True
                easein_bounce 0.5 zoom 1.0
        on hide:
            linear 0.5 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
