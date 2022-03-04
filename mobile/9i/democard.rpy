
label democard:
    if not demo:
        return

    $ renpy.run(Show('democardbase', transition=slowdissolve))

    show screen democardbase


    $ renpy.choice_for_skipping()



    python:
        while demo:
            if ui.interact(mouse='screen', type='screen'): break

    $ renpy.run(Hide('democardbase', transition=slowdissolve))
    pause 1.5 hard



    if not demo:
        return
    else:
        $ renpy.full_restart()

screen democardbase():
    modal True

    on "update" action If(not demo, Return())

    key "K_ESCAPE" action Return()

    use democard(purchase_action=DemoCardPurchase(), title_action=Return())


init 1000:
    if not renpy.has_screen('democard'):
        screen democard(purchase_action, title_action):
            on "show" action Return()
            on "replace" action Return()
init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    class DemoCardPurchase(renpy.ui.Action):
        """
        Runs when selecting the purchase option in the demo card.
        Opens the appropriate web page for the edition, and then closes
        the game. (Steam goes back to the menu instead, because the store
        page opens in the overlay.)
        """
        def __call__(self):
            persistent.democard_reload = True
            
            if steam and steam.initialized:
                steam.activate_overlay_to_store(STEAM_APPID)
                renpy.full_restart()
            else:
                renpy.run(OpenURL(STORE_URL))
                renpy.quit()



    if persistent.democard_reload:
        del persistent.democard_reload
        config.auto_load = renpy.newest_slot()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
