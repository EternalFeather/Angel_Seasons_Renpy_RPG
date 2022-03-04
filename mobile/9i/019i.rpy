

python early:

    demo = True

init -998 python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals


    config.default_afm_time = 10
    config.default_afm_enable = False
    config.default_fullscreen = False
    config.default_text_cps = 50
    config.save_physical_size = False


    def get_default_language():
        """Used to select a default translation on first run. Tries for
        the current Steam language, English, and then Japanese, in that
        order.
        """
        
        STEAM_LANGUAGES = {
            'schinese': 'simplified_chinese',
            'tchinese': 'traditional_chinese'
        }
        
        kl = renpy.known_languages()
        
        if steam and steam.initialized:
            sl = steam.get_current_game_language()
            sl = STEAM_LANGUAGES.get(sl, sl)
            if sl in kl:
                return sl
        elif 'english' in kl:
            return 'english'
        else:
            return None
    config.default_language = get_default_language()

    def get_window_title():
        """Used to set the window caption.
        """
        if getattr(store, 'demo', False):
            return config.name + ' demo'
        else:
            return config.name
    config.window_title = get_window_title()

    config.quit_action = [Hide("main_menu"), Quit()]
    config.help = None
    config.has_music = True
    config.has_sound = True
    config.has_voice = False
    _game_menu_screen = 'navigation'

    config.after_load_transition = dissolve
    config.end_game_transition = dissolve
    config.end_splash_transition = dissolve
    config.exit_transition = Dissolve(0.1, alpha=True)
    config.main_game_transition = dissolve
    config.game_main_transition = dissolve
    config.intra_transition = dissolve


    config.replay_scope = {'_game_menu_screen': 'replay_navigation'}
    config.enter_replay_transition = dissolve
    config.exit_replay_transition = dissolve


    config.autosave_slots = 8
    config.quicksave_slots = 8
    config.thumbnail_width = scale(357)
    config.thumbnail_height = scale(201)



    def _on_save(json):
        json['game_version'] = config.version
    config.save_json_callbacks = [_on_save]


    config.hard_rollback_limit = 200
    config.image_cache_size = 80
    config.rollback_length = 256
    config.narrator_menu = True
    config.old_substitutions = False



    adv = ADVAutoCharacter(
        None,
        ctc='ctc_animation',
        ctc_position='fixed')
    name_only = Character(None, kind=adv)
    narrator = Character(
        '',
        kind=adv,
        what_style='say_narration',
        window_style='say_narration_window')



    config.keymap['dismiss'].append('mousedown_5')






    def _hide(name, layer='master'):
        for l in _3d_layers:
            if renpy.showing(name, l):
                renpy.hide(name, l)
        renpy.hide(name, 'texture')
        renpy.hide(name, layer)
    config.hide = _hide

    def _scene(layer='master'):
        for l in _3d_layers:
            renpy.scene(l)
        renpy.scene('texture')
        renpy.scene(layer)
    config.scene = _scene

    class DynamicTagLayerDict(dict):
        """Custom mapping for `config.tag_layer` which returns the layer
        a tag is on if it's already showing.
        """
        def get_showing(self, tag):
            for layer in renpy.config.layers:
                if renpy.game.context().images.showing(layer, (tag,)):
                    return layer
        
        def __getitem__(self, tag):
            return (
                self.get_showing(tag)
                or super(DynamicTagLayerDict, self).__getitem__(tag))
        
        def get(self, tag, default=None):
            return (
                self.get_showing(tag)
                or super(DynamicTagLayerDict, self).get(tag, default))
    config.tag_layer = DynamicTagLayerDict()



init -1 python hide:
    if demo:
        achievement.backends = []
    else:
        achievement.backends = [
            x
            for x in achievement.backends
            if not isinstance(x, achievement.PersistentBackend)
            ]


label quit:
    python:
        suppress_overlay = True
        for channel in renpy.audio.audio.channels:
            
            if not isinstance(channel, basestring): continue
            
            if channel == 'movie': continue
            renpy.sound.stop(channel=channel, fadeout=0.5)
    scene black
    scene onlayer screens
    with dissolve
    return





python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def parse_multiline_string(lexer):
        """Parses a triple-quoted string that's been indented to
        match the surrounding block.
        """
        import re
        
        
        delim = lexer.require(r'([\'"])\1\1')
        rest = lexer.rest()
        if not rest.endswith(delim):
            lexer.require(delim)
        
        
        
        
        
        string = lexer.text[3:-3]
        lines = string.split('\n')
        base_indent = len(re.match(r'^ *', lines[-1]).group())
        strip_re = '^ {{0,{}}}'.format(base_indent)
        
        return '\n'.join(
            re.sub(strip_re, '', line)
            for line in lines)
        
python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    import sys



    if not any(
        (isinstance(i, renpy.loader.RenpyImporter)
            and i.prefix == '9i/python-packages/')
        for i in sys.meta_path):
        sys.meta_path.insert(
            2,
            renpy.loader.RenpyImporter(prefix='9i/python-packages/'))





    try:
        renpy.load_module('9i/developer/i18n')
    except Exception as e:
        pass
    try:
        renpy.load_module('9i/developer/i18n_spreadsheet')
    except Exception as e:
        pass



init -999 python:
    from __future__ import absolute_import

    try:
        import _renpysteam as steam
        steam.init()
    except Exception as e:
        steam = None



init -999 python:
    from __future__ import division

    SCALE = config.screen_height / 1080

    def scale(x):
        """Scales the input value from Full HD (1920x1080) to the
        configured screen resolution.
        """
        if isinstance(x, int):
            return int(x * SCALE)
        elif isinstance(x, long):
            return long(x * SCALE)
        else:
            return x * SCALE

    def pscale(x):
        """Scales a position to screen resolution from Full HD.
        """
        from renpy.display.core import absolute
        return absolute(x * SCALE)

init -999:


    transform imagescale(x):
        subpixel True
        zoom SCALE * 1080 / x





    transform unscale(depth, z):
        zoom (depth - z) / _LAYER_Z





    transform screenspace(pos, layer):
        function screenspace_fn(pos=pos, layer=layer)
init -999 python:
    def unscale_by_layer(layer):
        return unscale(depth=_3d_layers.get(layer, _LAYER_Z), z=_camera_z)

    def screenspace_fn(pos, layer):
        """Transform function.
        Positions a displayable in 3D space at the given coordinates in
        screen space and to appear at its original size, given a camera
        at the origin.
        Used for layout of multi-layer assets such as sets.
        """
        layer_zoom = scale(_3d_layers[layer] / _LAYER_Z)
        def _screenspace(transform, st, at):
            from renpy.display.core import absolute
            x, y = pos
            transform.subpixel = True
            
            
            transform.pos = (
                absolute(x * layer_zoom - 1920 * (layer_zoom * 0.5 - 0.5)),
                absolute(y * layer_zoom - 1080 * (layer_zoom * 0.5 - 0.5)))
            transform.anchor = (0, 0)
            transform.zoom = layer_zoom
        return _screenspace


python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    class BasicFrame(renpy.display.core.Displayable):
        def __init__(
                self,
                fill_color,
                outer_border_color = None,
                inner_border_color = None,
                *args,
                **kwargs):
            super(BasicFrame, self).__init__(*args, **kwargs)
            
            self.fill_color = Color(fill_color)
            self.outer_border_color = Color(outer_border_color)
            self.inner_border_color = Color(inner_border_color)
        
        def __repr__(self):
            args = [self.fill_color]
            if self.outer_border_color:
                args.append(self.outer_border_color)
            if self.inner_border_color:
                args.append(self.inner_border_color)
            
            return "BasicFrame({})".format(", ".join(
                [
                    "\"#{:02x}{:02x}{:02x}{:02x}\"".format(*color)
                    for color in args
                ]))
        
        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            rc = r.canvas()
            rs = rc.get_surface()
            
            rs.fill(self.fill_color)
            
            if self.outer_border_color:
                rc.rect(
                    self.outer_border_color,
                    (0, 0, width - 1, height - 1),
                    1)
            
            if self.inner_border_color and width > 3 and height > 3:
                rc.rect(
                    self.inner_border_color,
                    (1, 1, width - 3, height - 3),
                    1)
            
            return r


init -997:
    image movie = Movie(
         size=(config.screen_width, config.screen_height),
         xcenter=0.5,
         ycenter=0.5)

    image ctc_animation:
        xcenter 0.74
        ycenter 0.93
        imagescale(720)
        "9i/dialogue/ctc 1.png"
        block:
            "9i/dialogue/ctc 1.png" with slowdissolve
            1.0
            "9i/dialogue/ctc 2.png" with slowdissolve
            1.0
            repeat



    transform lfade(duration):
        alpha 0
        linear duration alpha 1
        on replace:



            alpha 1
        on hide:
            linear duration alpha 0

    transform delayfade(dt, ft):
        alpha 0
        dt
        linear ft alpha 1

    define qfade = lfade(0.1)
    define basicfade = lfade(0.3)
    define slowfade = lfade(3.0)
    define ultraslowfade = lfade(6.0)


    define dissolve = Dissolve(0.5, alpha=True)
    define slowdissolve = Dissolve(1.0, alpha=True)
    define slowerdissolve = Dissolve(3.0, alpha=True)
    define ultraslowdissolve = Dissolve(6.0, alpha=True)


    transform vslide(y, t):
        subpixel True
        yoffset y
        ease t yoffset scale(0)

    transform visible:
        alpha 1
    transform invisible:
        alpha 0



    transform popup:
        xalign 0.5
        on show:
            alpha 0 yalign 0.7
            ease 0.25 alpha 1 yalign 0.5
        on hide:
            ease 0.5 alpha 0.0 yalign 0.7





    define side_actor_ypos = _dict()




    transform side_left(tag, xp=0.13, xzoom=-1):
        subpixel True
        xpos xp
        ypos side_actor_ypos.get(tag, 0.5)
        yanchor 0.0
        xzoom xzoom
        zoom 1.8
    transform side_left_v2(tag):
        subpixel True
        xpos 0.165
        ypos side_actor_ypos.get(tag, 0.5)
        yanchor 0.0
        xzoom -1
        zoom 1.6
    transform side_left_v3(tag):
        subpixel True
        xpos 0.1
        ypos side_actor_ypos.get(tag, 0.5)
        yanchor 0.0
        xzoom -1
        zoom 1.8

    transform side_right(tag, xp=0.87):
        subpixel True
        xpos xp
        ypos side_actor_ypos.get(tag, 0.5)
        yanchor 0.0
        zoom 1.8
    transform side_right_v2(tag):
        subpixel True
        xpos 0.835
        ypos side_actor_ypos.get(tag, 0.5)
        yanchor 0.0
        zoom 1.6
    transform side_right_v3(tag):
        subpixel True
        xpos 0.93
        ypos side_actor_ypos.get(tag, 0.5)
        yanchor 0.0
        zoom 1.8

    image sidegradation:
        "9i/dialogue/side gradation.png"
        imagescale(720)
        yalign 1.0
        basicfade
        on hide:


            alpha 0



python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def cutscene(path, background='black'):
        """Plays the movie file at the specified path, clearing the
        scene to black or the provided image name before and after.
        """
        renpy.scene()
        renpy.show(background, layer='master')
        renpy.movie_cutscene(path)
        renpy.scene()
        renpy.show(background, layer='master')

    def cutscene_parse(lx):
        path_expr = lx.require(lx.simple_expression)
        bg_type, bg_param = (None, None)
        if lx.keyword('background'):
            bg_type, bg_param = (('expr', lx.require(lx.simple_expression))
                if lx.keyword('expression')
                else ('name', renpy.parser.parse_image_name(lx, nodash=True)))
        lx.expect_eol()
        return (path_expr, bg_type, bg_param)

    def cutscene_execute(params):
        path_expr, bg_type, bg_param = params
        path = renpy.python.py_eval(path_expr)
        if bg_type is 'expr':
            cutscene(path, background=renpy.python.py_eval(bg_param))
        elif bg_type is 'name':
            cutscene(path, background=' '.join(bg_param))
        else:
            cutscene(path)


    renpy.register_statement(
        'cutscene',
        parse=cutscene_parse,
        execute=cutscene_execute,
        lint=None)

init -999 python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    class Reveal(renpy.ui.Action):
        def __init__(self, path):
            self.path = path
        
        def __call__(self):
            import os
            import subprocess
            
            if renpy.windows:
                subprocess.Popen('explorer /select,"' + self.path + '"')
            elif renpy.macintosh:
                subprocess.Popen(['open', '-R', self.path])
            else:
                subprocess.Popen(['xdg-open', os.path.basepath(self.path)])

    class ReplayMovie(renpy.ui.Action):
        """For gallery use. Plays the specified movie file.
        Sensitive only if the movie in question has been seen before.
        """
        def __init__(self, path, background=None):
            self.path = path
            self.background = background
        
        def __call__(self):
            if self.background is None:
                cutscene(self.path)
            else:
                cutscene(self.path, background=self.background)
        
        def get_sensitive(self):
            return self.path in persistent._seen_audio
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
