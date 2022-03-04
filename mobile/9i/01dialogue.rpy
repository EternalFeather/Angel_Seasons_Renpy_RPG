init:
    default _window_animation = None
    default _window_mode = None
    default _prev_window_mode = None
    default _window_outro_who = None
    default _window_outro_what = None

python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def window_mode_callback(mode, old_modes):
        """Mode callback for dialogue animation/styling. Determines
        when dialogue animations should be played.
        """
        dialogue_modes = ('say', 'nvl', 'menu', 'nvl_menu')
        entering_dialogue = (mode in dialogue_modes
            and old_modes[0] not in dialogue_modes)
        leaving_dialogue = (mode not in dialogue_modes
            and old_modes[0] in dialogue_modes)

        if renpy.in_rollback():
            return

        if leaving_dialogue:
            window_animate_outro()
        
        if entering_dialogue:
            store._window_animation = 'in'

    renpy.config.mode_callbacks.append(window_mode_callback)

    def window_animate_outro(next_mode=None):
        """Triggers the outro animation for the previous say to
        whichever mode the next say will use.
        """
        
        if (not isinstance(
                _window_outro_who,
                (ADVAutoCharacter, NVLAutoCharacter))
            or _window_outro_what is None):
            return
        
        
        current_window_mode = store._window_mode
        store._window_mode = store._prev_window_mode
        
        
        last_who = _window_outro_who
        
        store._window_animation = 'out'
        if isinstance(last_who, NVLAutoCharacter):
            store.nvl_list = store.nvl_list[:-1]
        last_who(
            _window_outro_what + config.extend_interjection,
            interact=False,
            _call_done=False)
        
        
        
        in_rollback = (
            renpy.game.after_rollback
            and renpy.exports.roll_forward_info() is not None)
        if not in_rollback and config.skipping != 'fast':
            
            context = renpy.game.context()
            context_mode_state = context.use_modes
            context.use_modes = False
            
            settings_for_mode = store._window_modes.get(store._window_mode, {})
            delays_for_prev_mode = settings_for_mode.get('outro_delays') or {}
            renpy.pause(
                delays_for_prev_mode.get(next_mode)
                or delays_for_prev_mode.get(None)
                or 0.0,
                hard=True)
            
            context.use_modes = context_mode_state
        
        
        store._prev_window_mode = store._window_mode
        store._window_mode = current_window_mode
        store._window_animation = None

    class ADVAutoCharacter(renpy.character.ADVCharacter):
        """Automatic animation/styling ADV character. Applies specified
        styles and animations to widgets shown when interacting.
        """
        def __call__(self, what, interact=True, _call_done=True, **kwargs):
            """Does a say with automatic dialogue animation/styles
            applied. The flow of execution between this class and the
            base `ADVCharacter` class is as follows.
            # * Here; automatically set dialogue mode to `narration` if
            #   the narrator is the sayer.
            #  * Base `__call__` runs. Mode switch to `say`. Extra
            #    keyword arguments are passed as `display_args`.
            #   * Base `do_add` runs. Nothing interesting happens.
            #   * Base `do_display` runs; it takes `display_args`.
            #     * This `do_show` runs; handles the other args; if
            #       appropriate, `animation` keyword argument to
            #       screen is set to intro/outro transform.
            #      * Show function runs.
            # * This `do_done` runs; resets animation state and records
            #   contents of the say.
            #   * Base `do_done` runs.
            """
            if self is store.narrator:
                store._window_mode = 'narration'
            
            
            changing_say = (store._window_animation == 'continue'
                and store._prev_window_mode != store._window_mode)
            if changing_say and not renpy.in_rollback():
                window_animate_outro(next_mode=store._window_animation)
                store._window_animation = 'in'
            
            
            settings_for_mode = (
                store._window_modes.get(store._window_mode, {}))
            display_args_for_mode = (
                settings_for_mode.get('display_args')
                or {})
            merged_args = display_args_for_mode.copy()
            merged_args.update(kwargs)
            
            target = (Character(kind=self, **merged_args) if merged_args else self)
            return super(ADVAutoCharacter, target).__call__(
                what,
                interact=interact,
                _call_done=_call_done)
        
        def do_show(self, who, what):
            """Called by `do_display`. Applies the current dialogue
            mode's styles and animations to the say screen and then
            shows it.
            """
            return self.show_function(
                who,
                what,
                who_args=merge_window_mode_props(self, 'who_args'),
                what_args=merge_window_mode_props(self, 'what_args'),
                window_args=merge_window_mode_props(self, 'window_args'),
                screen=self.screen,
                **merge_show_args(self))
        
        def do_done(self, who, what):
            """Resets the dialogue animation state and records the
            contents of this say so that outros can be played.
            """
            store._prev_window_mode = store._window_mode
            store._window_mode = None
            store._window_animation = 'continue'
            
            store._window_outro_who = self
            store._window_outro_what = what
            
            return super(ADVAutoCharacter, self).do_done(who, what)
        
        def do_extend(self):
            """Called when extending the previous line. Reverts the
            window mode to what it was on the previous line, and stops
            the intro from playing twice.
            """
            store._window_mode = store._prev_window_mode
            store._window_animation = 'continue'
            return super(ADVAutoCharacter, self).do_extend()

    def merge_window_mode_props(character, attr):
        """Utility function; creates a copy of `character.attr` and
        merges in the corresponding values from dialogue mode settings.
        """
        settings_for_mode = store._window_modes.get(store._window_mode)
        if not settings_for_mode:
            
            return getattr(character, attr)
        else:
            merged = getattr(character, attr).copy()
            merged.update(settings_for_mode.get(attr) or {})
            return merged

    def merge_show_args(character):
        """Utility function; creates a copy of `character.show_args`
        and merges in the corresponding values from dialogue mode
        settings. If the intro/outro flags are set, gets the
        appropriate transform and puts it under the `animation` key.
        """
        show_args = character.show_args.copy()
        
        settings_for_mode = store._window_modes.get(store._window_mode, {})
        show_args.update(settings_for_mode.get('show_args', {}))
        
        if store._window_animation == 'in':
            intros_by_prev_mode = settings_for_mode.get('intros') or {}
            intro_for_mode = (
                intros_by_prev_mode.get(store._prev_window_mode)
                or intros_by_prev_mode.get(None))
            if intro_for_mode is not None:
                show_args.update(animation=intro_for_mode)
        elif store._window_animation == 'out':
            
            
            outros_by_prev_mode = settings_for_mode.get('outros') or {}
            outro_for_mode = (
                outros_by_prev_mode.get(store._prev_window_mode)
                or outros_by_prev_mode.get(None)
                or store.invisible)
            show_args.update(animation=outro_for_mode)
        
        return show_args

    adv = ADVAutoCharacter(kind=adv)



init -999 python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    class NVLAutoCharacter(NVLCharacter):
        """Automatic animation/styling NVL character. Applies specified
        styles and animations to widgets shown when interacting.
        """
        def __init__(self, *args, **kwargs):
            super(NVLAutoCharacter, self).__init__(*args, **kwargs)
            self.show_fn = self.show_core
        
        def __call__(self, what, interact=True, _call_done=True, **kwargs):
            """Does a say with automatic dialogue animation/styles
            applied. NVL execution flow is slightly different.
            `do_add` doesn't actually add the text to show to the
            NVL list; that happens in `push_nvl_list`, which is
            called by `do_display` right before `show_core`.
            This is 6.99.13 behavior; in earlier versions, `do_add`
            handles both.
            """
            
            if store._window_mode is None:
                store._window_mode = 'nvl'
            
            
            changing_dialogue = (store._window_animation == 'continue'
                and store._prev_window_mode != store._window_mode)
            if changing_dialogue and not renpy.in_rollback():
                window_animate_outro(next_mode=store._window_animation)
                store._window_animation = 'in'
            
            
            settings_for_mode = (
                store._window_modes.get(store._window_mode, {}))
            display_args_for_mode = (
                settings_for_mode.get('display_args')
                or {})
            merged_args = display_args_for_mode.copy()
            merged_args.update(kwargs)
            
            target = (Character(kind=self, **merged_args) if merged_args else self)
            return super(NVLAutoCharacter, target).__call__(
                what,
                interact=interact,
                _call_done=_call_done)
        
        def push_nvl_list(self, who, what):
            """Called by `NVLCharacter.do_display` right before showing
            the screen. Handles styles and animations for the current
            line, and adds it to the NVL list.
            """
            kwargs = merge_show_args(self)
            
            if 'animation' in kwargs:
                del kwargs['animation']
            kwargs['properties'] = merge_window_mode_props(self, 'properties')
            kwargs['what_args'] = merge_window_mode_props(self, 'what_args')
            kwargs['who_args'] = merge_window_mode_props(self, 'who_args')
            kwargs['window_args'] = merge_window_mode_props(self, 'window_args')
            
            store.nvl_list.append((who, what, kwargs))
        
        if renpy.version_tuple < (6, 99, 13, 2919):
            def do_add(self, who, what):
                """Called by the base `__call__` of `ADVCharacter`. Pushes
                the current dialogue mode's styles and animation onto the
                NVL queue.
                """
                store.nvl_list = store.nvl_list or list()
                
                kwargs = merge_show_args(self)
                
                if 'animation' in kwargs:
                    del kwargs['animation']
                kwargs['what_args'] = merge_window_mode_props(self, 'what_args')
                kwargs['who_args'] = merge_window_mode_props(self, 'who_args')
                kwargs['window_args'] = merge_window_mode_props(self, 'window_args')
                
                store.nvl_list.append((who, what, kwargs))
                
                while (config.nvl_list_length
                    and (len(nvl_list) > config.nvl_list_length)):
                    nvl_list.pop(0)
        
        def show_core(self, who=None, what=None, **kwargs):
            """Called by the base `do_display` of `NVLCharacter`.
            Exists solely because the base implementation is hardcoded
            to always show the `nvl` screen.
            """
            
            _m1_dialogue__nvl_screen_dialogue = store._m1_00nvl_mode__nvl_screen_dialogue
            
            widget_properties, dialogue, show_args = _m1_dialogue__nvl_screen_dialogue()
            kwargs.update(show_args)
            
            kwargs.setdefault('layer', renpy.config.nvl_layer)
            layer = kwargs.pop('layer')
            
            
            
            animation = merge_show_args(self).get('animation')
            if animation:
                kwargs.update(animation=animation)
            
            renpy.show_screen(
                self.screen,
                _layer=layer,
                _transient=True,
                _widget_properties=widget_properties,
                dialogue=dialogue,
                **kwargs)
            renpy.shown_window()
            
            return renpy.get_widget(
                screen=self.screen,
                id='what',
                layer=layer)
        
        def do_done(self, who, what):
            """Resets the dialogue animation state and records the
            contents of this say so that outros can be played.
            """
            
            store._prev_window_mode = store._window_mode
            store._window_mode = None
            store._window_animation = 'continue'
            
            store._window_outro_who = self
            store._window_outro_what = what
            
            return super(NVLAutoCharacter, self).do_done(who, what)
        
        def do_extend(self):
            """Called when extending the previous line. Reverts the
            window mode to what it was on the previous line, and stops
            the intro from playing twice.
            """
            
            store._window_mode = store._prev_window_mode
            store._window_animation = 'continue'
            return super(NVLAutoCharacter, self).do_extend()


    nvl = nvl_narrator = NVLAutoCharacter(kind=nvl)


python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals


    def window_mode_parse(lexer):
        mode = ' '.join(iter(lexer.word, None))
        lexer.expect_eol()
        return mode

    def window_mode_execute(parse):
        global _window_mode
        _window_mode = parse

    renpy.register_statement(
        'window mode',
        parse=window_mode_parse,
        execute=window_mode_execute)

    @renpy.parser.statement('')
    def say_decomposed_parser(lexer, location):
        from renpy.ast import Say, Show, UserStatement
        from renpy.parser import image_word_regexp
        from renpy.parser import Lexer, parse_block, say_statement
        
        nodes = list()
        
        
        mode_checkpoint = lexer.checkpoint()
        if lexer.match(r'!'):
            lexer.revert(mode_checkpoint)
            win_mode = lexer.match(r'![A-Za-z_][A-Za-z0-9_]*')
            
            if win_mode is None:
                lexer.error('no dialogue mode specified')
            
            
            
            mode_block = [
                (
                    lexer.filename,
                    lexer.number,
                    'window mode ' + win_mode[1:],
                    []
                )
            ]
            mode_lexer = Lexer(
                mode_block,
                init=lexer.init,
                init_offset=lexer.init_offset,
                global_label=lexer.global_label)
            nodes.extend(parse_block(mode_lexer))
        
        
        
        
        
        
        
        
        say_checkpoint = lexer.checkpoint()
        say_who = None
        show_tag = None
        show_start_attrs = ()
        show_end_attrs = ()
        
        first_string = lexer.string()
        if lexer.keyword('with'):
            lexer.require(lexer.simple_expression)
        
        
        
        
        is_two_arg_say = first_string is None or not lexer.eol()
        lexer.revert(say_checkpoint)
        
        def match_attr_tokens():
            checkpoint = lexer.checkpoint()
            attr = lexer.image_name_component()
            
            
            
            if attr != '-':
                return attr
            else:
                lexer.revert(checkpoint)
                return None
        
        if is_two_arg_say:
            
            
            say_who = lexer.dotted_name()
            say_start_pos = lexer.pos
            say_is_string = False
            if say_who is None and lexer.string():
                say_who = lexer.text[say_start_pos:lexer.pos]
                say_is_string = True
            
            if say_who is None:
                lexer.error('expected statement.')
            
            
            
            try:
                if not say_is_string:
                    if '.' not in say_who:
                        show_tag = say_who
                    
                    else:
                        show_tag = say_who.split('.')[-1]
            except Exception as e:
                lexer.error(say_who)
            
            show_start_attrs = tuple(iter(match_attr_tokens, None))
            if lexer.match(r'->'):
                show_end_attrs = tuple(iter(match_attr_tokens, None))
                if not show_end_attrs:
                    lexer.error('no image attributes supplied to end with')
        
        rest = lexer.rest()
        
        
        lexer.advance()
        
        
        def make_show_attrs_block(tokens, tag):
            line = 'show {tag} {attrs}'.format(tag=tag, attrs=' '.join(tokens))
            return [location + (line, [])]
        
        if show_tag and show_start_attrs:
            show_start_attr_lexer = Lexer(
                make_show_attrs_block(show_start_attrs, show_tag),
                init=lexer.init,
                init_offset=lexer.init_offset,
                global_label=lexer.global_label)
            nodes.extend(parse_block(show_start_attr_lexer))
        
        
        
        
        say_line = ('{who} {rest}'.format(who=say_who, rest=rest)
            if say_who is not None
            else rest)
        say_lexer = Lexer(
            [location + (say_line, [])],
            init=lexer.init,
            init_offset=lexer.init_offset,
            global_label=lexer.global_label)
        say_lexer.advance()
        nodes.append(say_statement(say_lexer, location))
        
        if show_tag and show_end_attrs:
            show_end_attr_lexer = Lexer(
                make_show_attrs_block(show_end_attrs, show_tag),
                init=lexer.init,
                init_offset=lexer.init_offset,
                global_label=lexer.global_label)
            nodes.extend(parse_block(show_end_attr_lexer))
        
        return nodes
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
