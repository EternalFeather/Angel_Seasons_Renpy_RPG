
screen outfit_nonmodal(heroine=None):
    add "9i/interface/battle/system/bg-splash.jpg"

    # 左下角角色显示
    if heroine.name in ["一诚小桃", "日向爱衣"]:
        frame:
            background None
            foreground None
            xalign -2.35
            yalign 0.3

            add "9i/interface/battle/actors/" + heroine.objectname + "/default/default.png" at heroine_status_not_focus
    else:
        frame:
            background None
            foreground None
            xalign -1.35
            yalign 0.2

            add "9i/interface/battle/actors/" + heroine.objectname + "/default/default.png" at heroine_status_not_focus
    
    # 显示角色形象
    frame:
        background None
        foreground None
        xalign 0.18
        yalign 0.8

        add "9i/interface/battle/actors/" + heroine.objectname + "/default/default.png" at heroine_status_focus

    key "game_menu" action NullAction()


screen outfit_changer(heroine=None, outfit_ingame_page=1):
    python:
        name = heroine.name

    # 装备栏
    frame:
        background None
        foreground None
        xalign 0.8
        yalign 0.5

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 100

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 30
                
                text name:
                    size 130
                    font "9i/fonts/浪漫雅圆.ttf"
                    text_align 0.5
                    xalign 0.5
                    outlines [(1, "#0009", 1, 1), (1, "#000d")]

                text "(请选择需要选择的装备进行操作)":
                    font "9i/fonts/浪漫雅圆.ttf"
                    size 35 
                    text_align 0.5
                    xalign 0.5
                    outlines [(1, "#0009", 1, 1), (1, "#000d")]

                python:
                    list_all_outfit = {name: heroine.outfits[name] for name in ["武器", "防具", "项链", "戒指", "法杖", "宝石"]}
                    grid_x = 3
                    grid_y = 2
                    total_grid = grid_x * grid_y
                    page_amount = len(local_config.party)

                frame:
                    background "#916e704c"
                    xalign 0.5
                    yalign 0.5
                    xpadding 50
                    ypadding 50
                    xmaximum 900
                    ymaximum 600

                    vbox:
                        spacing 30

                        grid grid_x grid_y:       
                            xalign 0.5
                            yalign 0.5 
                            spacing 50

                            for i, (category, outfit) in enumerate(list_all_outfit.items()):
                                # 有装备
                                if outfit is not None:
                                    python:
                                        block_size = 180
                                        outfit_name = outfit.name
                                        outfit_image = "9i/interface/battle/outfits/%s/%s.png" % (category, "_".join(outfit.objectname.split("_")[1:]))
                                        outfit_image_size = imagebuilder.getFillSize(outfit_image, (block_size + 1, block_size + 1))

                                    imagebutton:
                                        activate_sound "9i/interface/click2.ogg"
                                        background "#00000044"
                                        hover_foreground "#ffffff44"
                                        idle im.Crop(im.Scale(outfit_image, outfit_image_size[0], outfit_image_size[1]), (0, 0, block_size, block_size))
                                        action [Return([heroine, outfit_ingame_page]), SetVariable("call_outfit_detail", True), SetVariable("selected_outfit_before", outfit), SetVariable("selected_outfit_index", category)]
                                else:
                                    python:
                                        block_size = 180
                                        outfit_image = "9i/interface/battle/outfits/mask.png"
                                        outfit_image_size = imagebuilder.getFillSize(outfit_image, (block_size + 1, block_size + 1))

                                    imagebutton:
                                        activate_sound "9i/interface/click2.ogg"
                                        background "#00000044"
                                        hover_foreground "#ffffff44"
                                        idle im.Crop(im.Scale(outfit_image, outfit_image_size[0], outfit_image_size[1]), (0, 0, block_size, block_size))
                                        action [Return([heroine, outfit_ingame_page]), SetVariable("call_outfit_detail", True), SetVariable("selected_outfit_index", category)]

                        frame:
                            xalign 0.5
                            yalign 0.9
                            background None
                            foreground None

                            hbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 10

                                for page in range(1, page_amount + 1):
                                    textbutton str(page) action Return([local_config.party[page - 1], page]) text_align 0.5 text_size 35 xpadding 20 ypadding 20                                 

    use template_navigation_back(back_action=[Return([None, None]), SetVariable("end_outfit_deal", True)])

    key "game_menu" action NullAction()
    # use template_navigation_back(back_action=[Return([heroine, outfit_ingame_page]), SetVariable("call_cardgame", True)])


screen inventory(heroine, page, paginated, page_amount, selected_outfit_index=None, selected_outfit_before=None, outfit_ingame_page=1):
    modal True
    on "show" action SetVariable("chosen_outfit", None)

    frame at battle_equipment_chooser_show_hide:
        xpadding 40 ypadding 40 background "#446688aa"

        hbox:
            spacing 30
            use inventory_itemlist(paginated, page, page_amount)
            if chosen_outfit is None:
                use inventory_showcase(heroine, selected_outfit_before, selected_outfit_before)
            else:
                use inventory_showcase(heroine, chosen_outfit, selected_outfit_before)

    use template_navigation_back(back_action=[Return(None), SetVariable("call_outfit_detail", False)])

    key "game_menu" action NullAction()


screen inventory_itemlist(items, page, page_amount):
    frame:
        foreground None
        background "#00000044"
        xpadding 20
        ypadding 20
        xsize 1000
        ysize 1000
        ymargin 27
        left_margin 40

        frame:
            background None
            foreground None
            xalign 0.5
            ymargin 27

            python:
                grid_x = 3
                # if page == page_amount:
                #     items_amount = len(items) + 1
                # else:
                items_amount = len(items)
                extra_spots = grid_x - (items_amount % grid_x) if items_amount % grid_x != 0 else 0
                total_grid = extra_spots + items_amount
                grid_y = total_grid / grid_x

            grid grid_x grid_y:  
                xalign 0.5      
                spacing 20

                for item in items:
                    python:
                        block_size = 240
                        item_image = "9i/interface/battle/outfits/%s/%s.png" % (item.category, "_".join(item.objectname.split("_")[1:]))
                        item_image_size = imagebuilder.getFillSize(item_image,  (block_size + 1, block_size + 1))

                    frame:
                        background "#ffffff44"
                        foreground None
                        xalign 0.5
                        yalign 0.5

                        imagebutton:
                            activate_sound "9i/interface/click2.ogg"
                            if item == chosen_outfit:
                                foreground "#ffffff33"
                            hover_background "#ffffff44"
                            idle im.Crop(im.Scale(item_image, item_image_size[0], item_image_size[1]), (0, 0, block_size, block_size))
                            action SetVariable("chosen_outfit", item)
                
                # if page == page_amount:
                #     # 空位
                #     python:
                #         block_size = 240
                #         item_image = "9i/interface/battle/outfits/mask.png"
                #         item_image_size = imagebuilder.getFillSize(item_image,  (block_size + 1, block_size + 1))

                #     frame:
                #         background "#ffffff44"
                #         foreground None
                #         xalign 0.5
                #         yalign 0.5

                #         imagebutton:
                #             activate_sound "9i/interface/click2.ogg"
                #             background "#00000080"
                #             hover_background "#ffffff44"
                #             idle im.Crop(im.Scale(item_image, item_image_size[0], item_image_size[1]), (0, 0, block_size, block_size))
                #             action [Return(), SetVariable("selected_outfit_off", True), SetVariable("chosen_outfit", None), SetVariable("call_outfit_detail", False)]

                # 无道具补位
                if extra_spots > 0:
                    for _ in range(extra_spots):
                        frame:
                            background None
                            foreground None
                            xalign 0.5
                            yalign 0.5

                            imagebutton:
                                idle Null()

            use inventory_pagination(items, page_amount)

    key "game_menu" action NullAction()


screen inventory_pagination(items, page_amount):
    if page_amount != 1:
        frame:
            foreground None
            yalign 1.15
            xalign 0.5
            hbox:
                for nowpage in range(1, page_amount + 1):
                    textbutton "[nowpage]": 
                        xpadding 22
                        ypadding 11
                        background "#c27fa644"
                        hover_background "#c27fa688"
                        selected_background "#00000064"
                        text_size 30
                        if nowpage != page:
                            action [SetVariable("page", nowpage), Return()]

    key "game_menu" action NullAction()


screen inventory_showcase(heroine, item, selected_outfit_before):
    frame:
        background "#00000044"
        foreground None
        xsize 750
        ysize 1000
        ymargin 27
        right_margin 40

        frame:
            background None
            foreground None
            xalign 0.5
            yalign 0.5
            xsize 700
            ysize 800

            if item is not None:
                python:
                    item_width = 320
                    item_image = "9i/interface/battle/outfits/%s/%s.png" % (item.category, "_".join(item.objectname.split("_")[1:]))
                    item_image_size = imagebuilder.getFullWidth(item_image, item_width)
                    double_description = item.double_effect[2]
                    if item.category not in ["宝石", "法杖"]:
                        forth_description = item.forth_effect[1]
                    else:
                        forth_description = "无"

                    # 主属性名称
                    prime_attribute = copy(item.prime_attribute)
                    prime_attribute_name = list(prime_attribute.keys())[0]
                    prime_attribute_number = prime_attribute[prime_attribute_name]
                    if isinstance(prime_attribute_number, float):
                        prime_attribute_number = get_icons_v2(prime_attribute_number)
                    
                    # 副属性
                    minor_attributes = copy(item.minor_attributes)
                    for name, value in minor_attributes.items():
                        if isinstance(value, float):
                            value = get_icons_v2(value)
                        minor_attributes[name] = (value, 55 - 2 * len(str(value)) - 4 * len(name))

                    # 升级所需经验值
                    level = item.level
                    rarity = item.rarity
                    if level == 15:
                        experience = "Max"
                    else:
                        experience = (2000 + 500 * rarity) + level * (1000 + 250 * rarity)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 50
                    xsize 650
                    xfill True

                    frame:
                        background None
                        foreground None
                        xalign 0.5
                        yalign 0.5
                        xsize 650
                        ymaximum 300
                        xfill True
                        yfill True

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 30
                            xsize 650
                            xfill True

                            text "[item.name] Lv.[item.level]" style "frame_title" size 60 xalign 0.5 text_align 0.5 xfill True
                            # text "[item.description]":
                            #     xalign 0.5
                            #     text_align 0.5
                            #     xfill True
                            #     size 35
                            #     italic True

                            frame:
                                background "#00000033"
                                foreground None
                                xpadding 20
                                ypadding 20
                                xalign 0.5
                                yalign 0.5
                                xsize 600
                                xfill True

                                vbox:
                                    yalign 0.5

                                    text "[prime_attribute_name] +[prime_attribute_number]" text_align 0.5 size 40 xalign 0.5
                                    null height 30

                                    grid 1 4:
                                        for name, (number, sp_number) in minor_attributes.items():
                                            text "  [name]" + " " * sp_number + "+[number]" text_align 0.0 size 35 xalign 0.0
                                        for _ in xrange(4 - len(minor_attributes)):
                                            text Null()

                            text "2件套属性: [double_description]":
                                xalign 0.0
                                text_align 0.0
                                xfill True
                                size 35
                                italic True
                            
                            if item.category not in ["宝石", "法杖"]:
                                text "4件套属性: [forth_description]":
                                    xalign 0.0
                                    text_align 0.0
                                    xfill True
                                    size 35
                                    italic True
                            
                            if local_config.player.equip_experience >= experience:
                                text "升级所需经验值: [local_config.player.equip_experience] / [experience]"
                            else:
                                text "升级所需经验值: {color=#CD87D0}[local_config.player.equip_experience]{/color} / [experience]"
                                
                            hbox xfill True:
                                if item != selected_outfit_before:
                                    textbutton "装备":
                                        xalign 0.0
                                        yalign 1.0
                                        action [Return(), SetVariable("selected_outfit", item), SetVariable("chosen_outfit", None), SetVariable("call_outfit_detail", False)]
                                        style "activity"
                                else:
                                    textbutton "卸下":
                                        xalign 0.0
                                        yalign 1.0
                                        action [Return(), SetVariable("selected_outfit_off", True), SetVariable("chosen_outfit", None), SetVariable("call_outfit_detail", False)]
                                        style "activity"

                                textbutton "强化":
                                    xalign 0.5
                                    yalign 1.0
                                    if local_config.player.equip_experience >= experience:
                                        if item == selected_outfit_before:
                                            action [Function(item.equip_off, who=heroine), Function(item.level_up, who=local_config.player, experience=experience), Function(item.equip_on, who=heroine)]
                                        else:
                                            action Function(item.level_up, who=local_config.player, experience=experience)
                                    else:
                                        action NullAction()
                                    style "activity"

                                if not item.locked:
                                    textbutton "上锁":
                                        xalign 1.0
                                        yalign 1.0
                                        action SetField(item, "locked", True)
                                        style "activity"
                                else:
                                    textbutton "解锁":
                                        xalign 1.0
                                        yalign 1.0
                                        action SetField(item, "locked", False)
                                        style "activity"
                                

                                textbutton "出售":
                                    xalign 1.0
                                    yalign 1.0
                                    if item.locked or item == selected_outfit_before:
                                        action NullAction()
                                    else:
                                        action [Function(item.sell, who=heroine), Return(), SetVariable("chosen_outfit", None)]
                                    style "activity"

    key "game_menu" action NullAction()
