
screen disable_inputs_for_replay():
    if persistent._in_replay:
        key "game_menu" action ReplayKeymap()

screen disable_inputs():

    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")
    key "K_SPACE" action Hide("nonexistent_screen")

    key "mousedown_4" action Hide("nonexistent_screen")
    key "K_PAGEUP" action Hide("nonexistent_screen")
    key "mousedown_5" action Hide("nonexistent_screen")
    key "K_PAGEDOWN" action Hide("nonexistent_screen")

    key "mouseup_3" action Hide("nonexistent_screen")
    key "mouseup_1" action Hide("nonexistent_screen")

    key "K_ESCAPE" action Hide("nonexistent_screen")


init python:
    class ReplayKeymap(Action):
        def __call__(self):
            if not renpy.get_screen("yesno_prompt"):
                layout.yesno_screen(message=_("确定要终止回忆吗？"), yes=renpy.full_restart)
            else:
                renpy.hide_screen("yesno_prompt")
                return True

    def set_replay_scene(name):
        if name not in persistent.replays:
            persistent.replays.append(name)
        renpy.save(name)

    def end_replay():
        if persistent._in_replay:
            persistent._in_replay = None
            renpy.full_restart()

    class MyReplay(Action):
        def __init__(self, name, id):
            self.name = name
            self.id = id
        
        def __call__(self):
            if self.get_sensitive():
                persistent._in_replay = self.id
                persistent.test=self.id
                renpy.load(self.name)
        
        def get_sensitive(self):
            return renpy.can_load(self.name)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
