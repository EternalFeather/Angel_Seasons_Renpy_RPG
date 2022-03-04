
label equip_outfit:
    if len(local_config.party) == 0:
        window mode thougth
        "必须至少有一名队员才能进行装备编辑操作。"
        return

    python:
        end_outfit_deal = False
        call_outfit_detail = False
        selected_outfit_before = None
        selected_outfit_index = None
        selected_outfit = None
        selected_outfit_off = False
        heroine = local_config.party[0]
        outfit_ingame_page = 1
        page = 1

        while not end_outfit_deal:
            renpy.show_screen("outfit_nonmodal", heroine=heroine)

            if not call_outfit_detail:
                page = 1
                chosen_outfit = None
                selected_outfit = None
                selected_outfit_before = None
                selected_outfit_index = None
                selected_outfit_off = False
                heroine, outfit_ingame_page = renpy.call_screen("outfit_changer", heroine=heroine, outfit_ingame_page=outfit_ingame_page)
            else:
                if len(local_config.player.equipments) > 0:
                    items = local_config.player.equipments[selected_outfit_index]
                    items.sort(key=attrgetter("number"))
                else:
                    items = []
                if selected_outfit_before is not None:
                    items = [item for item in items if item != selected_outfit_before]
                    items += [selected_outfit_before]

                item_per_page = 9

                page_amount = int(math.ceil(len(items) / float(item_per_page)))

                # if selected_outfit_before is not None:
                #     page = page_amount
                if page == page_amount:
                    paginated = items[(page - 1) * item_per_page:]
                else:
                    paginated = items[(page - 1) * item_per_page:(page - 1) * item_per_page + item_per_page]

                renpy.call_screen("inventory", heroine=heroine, page=page, paginated=paginated, page_amount=page_amount, selected_outfit_index=selected_outfit_index, selected_outfit_before=selected_outfit_before, outfit_ingame_page=outfit_ingame_page)
                if selected_outfit is not None:
                    if selected_outfit_before:
                        selected_outfit_before.equip_off(heroine)
                        selected_outfit.equip_on(heroine)
                    else:
                        selected_outfit.equip_on(heroine)
                elif selected_outfit_off:
                    if selected_outfit_before:
                        selected_outfit_before.equip_off(heroine)
                        
        renpy.hide("outfit_nonmodal")
        end_outfit_deal = False
        call_outfit_detail = False
        selected_outfit_before = None
        selected_outfit_index = None
        heroine = local_config.party[0]
        outfit_ingame_page = 1
        page = 1

    $ renpy.retain_after_load()
    call screen roleroom
