





init -3 python:

    config.locked = False
    config.readback_buffer_length = 100
    config.readback_full = True
    config.readback_disallowed_tags = ["size"]
    config.readback_choice_prefix = ">> "
    config.locked = True
    style.readback_window.background = None
    style.readback_window.align = (.5, .2)
    style.readback_window.top_padding = 100
    style.readback_window.left_padding = 200
    style.readback_window.right_padding = 200
    style.readback_window.xminimum = 1280
    style.readback_window.ymaximum = 650
    style.readback_text.color = "#4d4d4d"
init -2 python:
    def delete_last_line():
        global readback_buffer
        del readback_buffer[-1]
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            return
        def do_extend(self):
            delete_last_line()
            super(ReadbackADVCharacter, self).do_extend()
            return
    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            return
        def do_extend(self):
            delete_last_line()
            super(ReadbackNVLCharacter, self).do_extend()
            return
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)
    config.nvl_show_display_say = say_wrapper
    adv = ReadbackADVCharacter()
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter
    def voice(filename, **kwargs):
        if not config.has_voice:
            return
        fn = config.voice_filename_format.format(filename=filename)
        _voice.play = fn
        store.current_voice = fn
    def menu(items, **add_input):
        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
            else:
                newitems.append((label, val))
        rv = renpy.display_menu(newitems, **add_input)
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
    def nvl_screen_dialogue():
        """
             Returns widget_properties and dialogue for the current NVL
             mode screen.
             """
        widget_properties = { }
        dialogue = [ ]
        for i, entry in enumerate(nvl_list):
            if not entry:
                continue
            who, what, kwargs = entry
            if i == len(nvl_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"
            else:
                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i
            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]
            dialogue.append((who, what, who_id, what_id, window_id))
        return widget_properties, dialogue
    def nvl_menu(items):
        renpy.mode('nvl_menu')
        if nvl_list is None:
            store.nvl_list = [ ]
        screen = None
        if renpy.has_screen("nvl_choice"):
            screen = "nvl_choice"
        elif renpy.has_screen("nvl"):
            screen = "nvl"
        if screen is not None:
            widget_properties, dialogue = nvl_screen_dialogue()
            rv = renpy.display_menu(
                    items,
                    widget_properties=widget_properties,
                    screen=screen,
                    scope={ "dialogue" : dialogue },
                    choice_style=style.nvl_menu_choice,
                    choice_chosen_style=style.nvl_menu_choice_chosen,
                    choice_button_style=style.nvl_menu_choice_button,
                    choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                    type="nvl",
                    )
            for label, val in items:
                if rv == val:
                    store.current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
        ui.layer("transient")
        ui.clear()
        ui.close()
        ui.vbox(style=_m1_readback__s(style.nvl_vbox))
        for i in nvl_list:
            if not i:
                continue
            who, what, kw = i
            rv = renpy.show_display_say(who, what, **kw)
        renpy.display_menu(items, interact=False,
                               window_style=_m1_readback__s(style.nvl_menu_window),
                               choice_style=_m1_readback__s(style.nvl_menu_choice),
                               choice_chosen_style=_m1_readback__s(style.nvl_menu_choice_chosen),
                               choice_button_style=_m1_readback__s(style.nvl_menu_choice_button),
                               choice_chosen_button_style=_m1_readback__s(style.nvl_menu_choice_chosen_button),
                               )
        ui.close()
        roll_forward = renpy.roll_forward_info()
        rv = ui.interact(roll_forward=roll_forward)
        renpy.checkpoint(rv)
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
    readback_buffer = []
    current_line = None
    current_voice = None
    def store_say(who, what):
        global readback_buffer, current_voice
        if preparse_say_for_store(what):
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()
    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"
    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp)
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)
    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]
    def readback_catcher():
        ui.add(renpy.Keymap(rollback=(SetVariable("yvalue", 1.0), ShowMenu("text_history"))))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))
    if config.readback_full:
        config.rollback_enabled = False
        config.overlay_functions.append(readback_catcher)
init python:
    yvalue = 1.0
    class NewAdj(renpy.display.behavior.Adjustment):
        def change(self,value):
            if value > self._range and self._value == self._range:
                return Return()
            else:
                return renpy.display.behavior.Adjustment.change(self, value)
    def store_yvalue(y):
        global yvalue
        yvalue = int(y)
screen text_history tag menu:

    modal True
    add 'images/ssel_bg.bmp'
    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []
    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]
    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):
        $ lines_to_show = readback_buffer + [current_line]
    else:
        $ lines_to_show = readback_buffer
    $ adj = NewAdj(changed = store_yvalue, step = 300)
    window:
        style_group "readback"
        has side "c r"
        viewport:
            mousewheel True
            draggable True
            yinitial yvalue
            yadjustment adj
            has vbox
            for line in lines_to_show:
                if line[0] and line[0] != " ":
                    label line[0]
                if not line[2]:
                    text line[1]
                else:
                    textbutton line[1] action Play("voice", line[2])
                null height 8
        bar adjustment adj style 'vscrollbar'
    # hbox yalign .8 xalign .5:
        # style_group "arc"
    imagebutton auto "images/system/gallery/title_screen_%s.png" xalign 0.97 yalign 0.95 action Return() hovered Play("sound", "se_sys/select.ogg")
    # key 'pad_x_press' action Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
