
default investigation.label = None


default investigation.menu = None


default investigation.callee = None


default investigation.inventory = list()

python early in investigation:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    """The investigation mode of SILENCE THE PEDANT. Implements
    statements to invoke the mode, start calls, define items, and
    manage the inventory.
    """

    default_camera_bounds = ((0, 0, 0), (0, 0, 0))
    default_menu_camera_pos = (0, 0, 0)
    default_menu_screen_pos = (0.5, 0.5)
    default_menu_screen_layer = 'screens'


    def iv_parse(lexer):
        from collections import OrderedDict, defaultdict
        
        lexer.expect_block('investigation statement')
        lexer.require(':')
        lexer.expect_eol()
        
        parse = object()
        parse.label = None
        parse.camera_bounds_expr = None
        parse.scene_objects = defaultdict(list)
        parse.call_records = OrderedDict()
        parse.menu = object()

        parse.menu.object_tag = None
        parse.menu.camera_pos = None
        parse.menu.screen_pos = None
        parse.menu.screen_direction = None
        parse.menu.screen_layer = None
        parse.menu.move_records = []
        parse.menu.sleep_label = None
        parse.menu.shop_label = None
        parse.menu.member_label = None
        parse.menu.teleport_label = None
        parse.menu.memory_label = None
        parse.menu.callback_label = None
        parse.menu.room_label = None
        
        block_lexer = lexer.subblock_lexer()
        while block_lexer.advance():
            if block_lexer.keyword('bounds'):
                if parse.camera_bounds_expr:
                    block_lexer.error('camera bounds specified multiple times')
                first = block_lexer.require(block_lexer.simple_expression)
                block_lexer.require('to')
                second = block_lexer.require(block_lexer.simple_expression)
                parse.camera_bounds_expr = (first, second)
            elif block_lexer.keyword('menu'):
                
                if parse.menu.object_tag:
                    block_lexer.error('menu object specified multiple times')
                parse.menu = iv_parse_menu(block_lexer)
            elif block_lexer.keyword('object'):
                layer, object_parse = iv_parse_object(block_lexer)
                parse.scene_objects[layer].append(object_parse)
            elif block_lexer.keyword('call'):
                call_parse = iv_parse_call(block_lexer)
                parse.call_records[call_parse.tag] = call_parse
            else:
                block_lexer.error('not recognized')
        
        
        if parse.menu:
            menu_object = object()
            menu_object.tag = parse.menu.object_tag
            menu_object.focus_mask_expr = None
            menu_object.action = ('menu', None)
            menu_object.showif_expr = None
            
            parse.scene_objects[parse.menu.screen_layer].append(menu_object)
        
        return parse

    def iv_parse_menu(lexer, require_tag=True):
        menu_parse = object()
        menu_parse.object_tag = None
        menu_parse.camera_pos = None
        menu_parse.screen_pos = None
        menu_parse.screen_direction = None
        menu_parse.screen_layer = None
        menu_parse.move_records = []
        menu_parse.sleep_label = None
        menu_parse.shop_label = None
        menu_parse.memory_label = None
        menu_parse.member_label = None
        menu_parse.teleport_label = None
        menu_parse.callback_label = None
        menu_parse.room_label = None
        
        if require_tag:
            menu_parse.object_tag = lexer.require(lexer.image_name_component)
        lexer.require('onlayer')
        menu_parse.screen_layer = lexer.require(lexer.name)
        lexer.require(':')
        lexer.expect_eol()
        
        block_lexer = lexer.subblock_lexer()
        while block_lexer.advance():
            if block_lexer.keyword('camera_pos'):
                menu_parse.camera_pos = block_lexer.require(
                    block_lexer.simple_expression)
            elif block_lexer.keyword('screen_pos'):
                menu_parse.screen_pos = block_lexer.require(
                    block_lexer.simple_expression)
            elif block_lexer.keyword('screen_direction'):
                menu_parse.screen_direction = block_lexer.require(
                    '(left)|(right)')
            elif block_lexer.keyword('move'):
                caption_expr = block_lexer.require(
                    block_lexer.simple_expression)
                block_lexer.require('jump')
                label = block_lexer.require(block_lexer.label_name)
                menu_parse.move_records.append((caption_expr, label))
            elif block_lexer.keyword('sleep'):
                block_lexer.require('jump')
                menu_parse.sleep_label = block_lexer.require(
                    block_lexer.label_name)
            elif block_lexer.keyword('shop'):
                block_lexer.require('jump')
                menu_parse.shop_label = block_lexer.require(
                    block_lexer.label_name)
            elif block_lexer.keyword('member'):
                block_lexer.require('jump')
                menu_parse.member_label = block_lexer.require(
                    block_lexer.label_name)
            elif block_lexer.keyword('teleport'):
                block_lexer.require('jump')
                menu_parse.teleport_label = block_lexer.require(
                    block_lexer.label_name)
            elif block_lexer.keyword('memory'):
                block_lexer.require('jump')
                menu_parse.memory_label = block_lexer.require(
                    block_lexer.label_name)
            elif block_lexer.keyword('callback'):
                block_lexer.require('jump')
                menu_parse.callback_label = block_lexer.require(
                    block_lexer.label_name)
            elif block_lexer.keyword('roleroom'):
                block_lexer.require('jump')
                menu_parse.room_label = block_lexer.require(
                    block_lexer.label_name)
        
        return menu_parse

    def iv_parse_object(lexer):
        object_parse = object()
        object_parse.tag = None
        object_parse.focus_mask_expr = None
        object_parse.action = None
        object_parse.showif_expr = None
        
        object_parse.tag = lexer.require(lexer.image_name_component)
        
        lexer.require('onlayer')
        layer = lexer.require(lexer.name)
        
        if lexer.match('jump'):
            jump_label = lexer.require(lexer.label_name)
            object_parse.action = ('jump', jump_label)
        elif lexer.match('action'):
            action_expr = lexer.require(lexer.simple_expression)
            object_parse.action = ('action', action_expr)
        else:
            lexer.error('investigation object must specify an action')
        
        if lexer.match(':'):
            lexer.expect_eol()
            block_lexer = lexer.subblock_lexer()
            while block_lexer.advance():
                if block_lexer.keyword('focus_mask'):
                    if object_parse.focus_mask_expr is not None:
                        block_lexer.error('focus_mask specified multiple times')
                    object_parse.focus_mask_expr = block_lexer.require(
                        block_lexer.simple_expression)
                elif block_lexer.keyword('showif'):
                    if object_parse.showif_expr is not None:
                        block_lexer.error('showif specified multiple times')
                    object_parse.showif_expr = block_lexer.require(
                        block_lexer.simple_expression)
                else:
                    block_lexer.error('not recognized')
        
        return (layer, object_parse)

    def iv_parse_call(lexer):
        call_parse = object()
        call_parse.tag = None
        call_parse.label = None
        call_parse.showif_expr = None
        call_parse.sensitive_expr = None
        
        call_parse.tag = lexer.require(lexer.image_name_component)
        
        lexer.require('jump')
        call_parse.label = lexer.require(lexer.label_name)
        
        if lexer.match(':'):
            lexer.expect_eol()
            block_lexer = lexer.subblock_lexer()
            
            while block_lexer.advance():
                if block_lexer.keyword('showif'):
                    if call_parse.showif_expr is not None:
                        block_lexer.error('showif specified multiple times')
                    call_parse.showif_expr = block_lexer.require(
                        block_lexer.simple_expression)
                elif block_lexer.keyword('sensitive'):
                    if call_parse.sensitive_expr is not None:
                        block_lexer.error('sensitive specified multiple times')
                    call_parse.sensitive_expr = block_lexer.require(
                        block_lexer.simple_expression)
                else:
                    block_lexer.error('not recognized')
        
        return call_parse

    def iv_execute(parse):
        global label
        label = parse.label

    def iv_next(parse):
        return 'investigate'

    renpy.register_statement(
        'investigation',
        parse=iv_parse,
        execute=iv_execute,
        lint=None, 
        next=iv_next,
        block=True)




init -999 python in investigation:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def index_investigations():
        from collections import OrderedDict
        
        def get_location(node):
            
            
            filename = node.filename
            linenumber = node.linenumber
            if filename.startswith('/'):
                filename = 'game' + filename
            if filename.endswith('c'):
                filename = filename[:-1]
            return (filename, linenumber)
        
        
        all_labels = sorted((
            node
            for name, node in renpy.game.script.namemap.iteritems()
            if isinstance(name, basestring)),
            key=get_location)
        
        def iter_nodes(label):
            for node in label.block:
                if (isinstance(node, renpy.ast.UserStatement)
                    and node.get_name() == 'investigation'):
                    yield node
                elif isinstance(node, renpy.ast.Init):
                    for subnode in iter_nodes(node):
                        yield subnode
        
        
        investigations = OrderedDict()
        for label in all_labels:
            investigations_in_label = list(iter_nodes(label))
            
            if not investigations_in_label: continue
            elif len(investigations_in_label) > 1:
                raise Exception('multiple investigations in label {name}'.format(
                    name=label.name))
            
            investigation = investigations_in_label[0]
            
            
            
            
            
            name, parse = investigation.parsed
            parse.label = label.name
            
            investigations[label.name] = parse
        
        return investigations

    index = index_investigations()





label investigate:

    $ renpy.choice_for_skipping()

    $ renpy.block_rollback()




    $ renpy.pause(0, hard=True)


    show screen investigation
    $ investigation.add_scene_objects()

    while True:
        $ ui.interact()



screen investigation():
    layer "master"



    default clamp = True
    default invert_drag = True



    default camera = (
        investigation.InvestigationCamera(
            investigation.label,
            invert_drag,
            clamp)
        or None)

    key "mouseup_3" action NullAction()
    key "dismiss" action NullAction()
    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "hide_windows" action NullAction()
    key "q" action ToggleScreenVariable("clamp")
    key "w" action ToggleScreenVariable("invert_drag")

    if (camera and (camera.tl or camera.br)):
        add camera



screen investigation_layer(layer):
    default parse = investigation.index[investigation.label]
    default objects = parse.scene_objects.get(layer) or list()
    default context = renpy.game.context()

    for obj in objects:
        python:
            from __future__ import division
            from __future__ import unicode_literals

            displayable = context.scene_lists.get_displayable_by_tag(layer, obj.tag)
            disp_placement = None
            disp_bounds = None
            disp_mask = None
            if displayable:
                disp_placement = renpy.get_placement(displayable)
                disp_bounds = renpy.get_image_bounds(obj.tag, layer=layer)
                if obj.focus_mask_expr:
                    disp_mask = Transform(
                        eval(obj.focus_mask_expr),
                        zoom=getattr(displayable, 'zoom', 1))
            action_type, action_arg = obj.action
        if (displayable
            and disp_placement
            and disp_bounds
            and (eval(obj.showif_expr)
                if obj.showif_expr is not None
                else True)):
            ivmwrapper obj.tag layer:
                button style "default" xysize (int(disp_bounds[2]), int(disp_bounds[3])):
                    add (
                        (iv_object_inter if obj.tag not in dir(c) else iv_actor_inter)(
                            disp_mask
                                if obj.focus_mask_expr
                                else AlphaMask(Solid("#fff"), displayable)))

                    focus_mask (disp_mask
                        if obj.focus_mask_expr
                        else displayable)
                    if action_type == 'jump':
                        action investigation.IvJump(label=action_arg)
                    elif action_type == 'menu':
                        action investigation.EnterIvMenu()
                    else:
                        action eval(action_arg)
                pos (disp_placement.xpos, disp_placement.ypos)
                anchor (disp_placement.xanchor, disp_placement.yanchor)
                offset (disp_placement.xoffset, disp_placement.yoffset)
init:
    transform iv_object_inter:
        alpha 0.0
        additive 1.0
        on hover:
            alpha 0.0
            easein 0.15 alpha 0.1
            block:
                linear 1.5 alpha 0.06
                linear 1.5 alpha 0.1
                repeat
        on start:
            easein 0.15 alpha 0.0
            block:
                3.5
                alpha 0.1
                linear 1.0 alpha 0.0
                repeat
        on idle:
            easein 0.15 alpha 0.0
            block:
                3.5
                alpha 0.1
                linear 1.0 alpha 0.0
                repeat
    transform iv_actor_inter:
        alpha 0.0
        additive 1.0
        on hover:
            alpha 0.0
            easein 0.15 alpha 0.1
            block:
                linear 1.5 alpha 0.06
                linear 1.5 alpha 0.1
                repeat
        on start:
            easein 0.15 alpha 0.0
        on idle:
            easein 0.15 alpha 0.0
init python in investigation:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    @renpy.pure
    class IvJump(renpy.ui.Action, renpy.store.DictEquality):
        """Action for jumping to a label from investigation mode.
        Handles cleanup for the mode.
        """
        
        def __init__(self, label):
            self.label = label
        
        def __call__(self):
            screen = renpy.get_screen('investigation', layer='master')
            menu_screen_layer = index[label].menu.screen_layer
            
            
            
            
            
            
            if not renpy.get_screen('iv', layer=menu_screen_layer):
                
                
                
                
                
                
                camera = screen.scope['camera']
                renpy.store.camera_move(
                    camera.x if camera.x is not None else renpy.store._camera_x,
                    camera.y if camera.y is not None else renpy.store._camera_y,
                    camera.z if camera.z is not None else renpy.store._camera_z)
            
            
            renpy.hide_screen('investigation', layer='master')
            renpy.hide_screen('iv', layer=menu_screen_layer)
            remove_scene_objects()
            
            
            renpy.checkpoint()
            renpy.block_rollback()
            
            renpy.jump(self.label)

    menu_camera_move_duration = 1.0
    menu_camera_move_warper = 'power_in_time_warp_real'

    @renpy.pure
    class EnterIvMenu(renpy.ui.Action):
        """Moves the camera to the menu position and shows the
        investigation menu screen."""
        def __call__(self):
            from renpy.python import py_eval
            menu_screen_layer = index[label].menu.screen_layer
            
            screen = renpy.get_screen('investigation', layer='master')
            camera = screen.scope['camera']

            camera = screen.scope['camera']
            renpy.store.camera_move(
                camera.x if camera.x is not None else renpy.store._camera_x,
                camera.y if camera.y is not None else renpy.store._camera_y,
                camera.z if camera.z is not None else renpy.store._camera_z)
            renpy.store.camera_push()
            renpy.store.flcam.move(
                *py_eval(index[label].menu.camera_pos),
                duration=menu_camera_move_duration,
                warper=menu_camera_move_warper)
            renpy.show_screen('investigation_menu', _layer=menu_screen_layer)
            remove_scene_objects()
            renpy.restart_interaction()
        
        def predict(self):
            renpy.predict_screen('investigation_menu')

    @renpy.pure
    class ExitIvMenu(renpy.ui.Action):
        """Moves the camera back to its original position before
        opening the investigation menu, and hides the menu screen.
        """
        def __call__(self):
            menu_screen_layer = index[label].menu.screen_layer
            
            renpy.hide_screen('investigation_menu', layer=menu_screen_layer)
            renpy.show_screen('investigation')
            renpy.store.flcam.stop()
            renpy.store.camera_pop_move(
                duration=menu_camera_move_duration,
                warper=menu_camera_move_warper)
            add_scene_objects()
            renpy.restart_interaction()

    def add_scene_objects():
        """Adds displayables for the investigation to the scene.
        """
        for layer, objects in index[label].scene_objects.iteritems():
            if not objects: continue
            renpy.show_screen('investigation_layer', layer=layer, _layer=layer)

    def remove_scene_objects():
        """Removes investigation displayables from the scene.
        """
        for layer in index[label].scene_objects:
            renpy.hide_screen('investigation_layer', layer=layer)

    @renpy.pure
    class InvestigationCamera(renpy.Displayable):
        """
        Handles investigation mode camera movement.
        """
        DEFAULT_MODE = object()
        FREELOOK_MODE = object()
        
        ZOOM_VSCALE = renpy.store.scale(3.5)
        ZOOM_HSCALE = (renpy.store.scale(3.5)
            * renpy.config.screen_width
            / renpy.config.screen_height)
        
        def __init__(self, label, invert_drag, clamp, mode=DEFAULT_MODE, *args, **kwargs):
            from math import cos, pi
            from renpy.python import py_eval
            
            super(InvestigationCamera, self).__init__(*args, **kwargs)
            
            
            parse = index[label]
            
            camera_bounds = (
                tuple(map(py_eval, parse.camera_bounds_expr))
                if parse.camera_bounds_expr is not None
                else default_camera_bounds)
            
            
            self.tl = camera_bounds[0][0:2]
            self.br = camera_bounds[1][0:2]
            z_n = int((camera_bounds[1][2] - camera_bounds[0][2]) // 100)
            self.zoom_levels = [
                (camera_bounds[0][2]
                    + (camera_bounds[1][2] - camera_bounds[0][2])
                        * cos((1 - z_i/z_n) * pi / 2))
                for z_i in range(1, z_n + 1)
            ]
            self.drag_scale = -1 if invert_drag else 1
            self.clamp = clamp
            self.mode = mode
            
            
            
            self.running = False
            
            
            self.x = None
            self.y = None
            self.z = None
            
            
            
            self.x1 = None
            self.y1 = None
            self.z1 = None
            
            
            
            
            
            
            self.xf = 0
            self.yf = 0
            self.zf = 0
            
            
            
            self.cursor_coords = None
        
        def render(self, width, height, st, at):
            return renpy.Render(width, height)
        
        def event(self, ev, x, y, st):
            
            
            
            
            global _wrapper_click
            
            
            
            if not self.running:
                self.running = True
                
                self.x = self.x1 = float(renpy.store._camera_x)
                self.y = self.y1 = float(renpy.store._camera_y)
                
                
                
                if self.mode is not InvestigationCamera.FREELOOK_MODE:
                    self.z = self.z1 = float(renpy.store._camera_z)
                else:
                    self.z = float(renpy.store._camera_z)
                    self.move_freelook_express()
            
            
            if _deferred_events:
                devs = _deferred_events[:]
                del _deferred_events[:]
                for dev in devs:
                    self.event(dev, x, y, st)
            
            
            
            if self.mode is InvestigationCamera.FREELOOK_MODE:
                if renpy.map_event(ev, "mousedown_4"):
                    self.freelook_zoom_in(x, y, st)
                if renpy.map_event(ev, "mousedown_5"):
                    self.freelook_zoom_out(x, y, st)
                return self.freelook_periodic(x, y, st)
            
            
            
            if renpy.map_event(ev, "mousedown_3"):
                self.begin_follow(x, y, st)
            elif renpy.map_event(ev, "mousedown_4"):
                self.on_zoom_in(x, y, st)
            elif renpy.map_event(ev, "mousedown_5"):
                self.on_zoom_out(x, y, st)
            elif renpy.map_event(ev, "mouseup_3"):
                self.end_follow(x, y, st)
                
                
                
                
                _wrapper_click = None
            
            
            
            return self.on_periodic(x, y, st)
        
        def begin_follow(self, x, y, st):
            self.cursor_coords = (x, y)
            self.move_express()
        
        def end_follow(self, x, y, st):
            self.cursor_coords = None
        
        def on_zoom_in(self, x, y, st):
            from renpy import store
            
            for zl in self.zoom_levels:
                if zl > self.z1:
                    self.z1 = zl
                    break
            else: return
            
            
            
            
            ax, ay = self.screen_to_camera_space(x, y)
            
            
            
            
            dx, dy = (self.x - ax, self.y - ay)
            os = store._LAYER_Z / (store._LAYER_Z - self.z)
            cs = store._LAYER_Z / (store._LAYER_Z - self.z1)
            s = cs / os
            x1, y1 = (ax + dx / s, ay + dy / s)
            self.set_destination(x1, y1, self.z1)
            
            self.move_express()
        
        def on_zoom_out(self, x, y, st):
            from renpy import store
            
            
            for zl in reversed(self.zoom_levels):
                if zl < self.z1:
                    self.z1 = zl
                    break
            else: return
            
            ax, ay = self.screen_to_camera_space(x, y)
            
            dx, dy = (self.x - ax, self.y - ay)
            os = store._LAYER_Z / (store._LAYER_Z - self.z)
            cs = store._LAYER_Z / (store._LAYER_Z - self.z1)
            s = cs / os
            x1, y1 = (ax + dx / s, ay + dy / s)
            self.set_destination(x1, y1, self.z1)
            
            self.move_express()
        
        def on_periodic(self, x, y, st):
            from renpy.store import scale, _LAYER_Z
            
            
            
            if self.cursor_coords:
                cx, cy = self.cursor_coords
                s = _LAYER_Z / (_LAYER_Z - self.z)
                dx, dy = (
                    scale(12.5) * self.drag_scale * (x - cx) / s,
                    scale(12.5) * self.drag_scale * (y - cy) / s)
                x1, y1 = (self.x1 + dx, self.y1 + dy)
                self.set_destination(x1, y1, self.z1)
                self.cursor_coords = (x, y)
            
            return None
        
        
        
        
        
        def freelook_zoom_in(self, x, y, st):
            from renpy.store import _LAYER_Z
            
            self.z1 = 175
            
            
            
            
            ax, ay = self.screen_to_camera_space(x, y)
            
            
            
            
            dx, dy = (self.x - ax, self.y - ay)
            os = _LAYER_Z / (_LAYER_Z - self.z)
            cs = _LAYER_Z / (_LAYER_Z - self.z1)
            s = cs / os
            x1, y1 = (ax + dx / s, ay + dy / s)
            self.set_destination(x1, y1, self.z1)
        
        def freelook_zoom_out(self, x, y, st):
            from renpy.store import _LAYER_Z
            
            self.z1 = 100
            
            ax, ay = self.screen_to_camera_space(x, y)
            
            dx, dy = (self.x - ax, self.y - ay)
            os = _LAYER_Z / (_LAYER_Z - self.z)
            cs = _LAYER_Z / (_LAYER_Z - self.z1)
            s = cs / os
            x1, y1 = (ax + dx / s, ay + dy / s)
            self.set_destination(x1, y1, self.z1)
        
        def freelook_periodic(self, x, y, st):
            from renpy.config import screen_width, screen_height
            from renpy.store import _LAYER_Z
            
            s = _LAYER_Z / (_LAYER_Z - self.z)
            left, top = self.tl
            right, bottom = self.br
            x1 = left + (right - left) * (x / screen_width)
            y1 = top + (bottom - top) * (y / screen_height)
            self.set_destination(x1, y1, self.z1)
            
            return None
        
        def move_express(self):
            """
            Restarts the interaction and begins moving the camera.
            """
            self.xf, self.yf, self.zf = (0, 0, 0)
            renpy.store.camera_move(
                0, 0, 0,
                x_express=self.x_express,
                y_express=self.y_express,
                z_express=self.z_express)
            renpy.restart_interaction()
        
        def move_freelook_express(self):
            """
            Restarts the interaction and begins moving the camera.
            Copypasta for freelook mode.
            """
            self.xf, self.yf, self.zf = (0, 0, 0)
            renpy.store.camera_move(
                0, 0, 0,
                x_express=self.x_freelook_express,
                y_express=self.y_freelook_express,
                z_express=self.z_freelook_express)
            renpy.restart_interaction()
        
        def set_destination(self, x, y, z):
            if self.clamp:
                self.x1 = min(max(
                    self.tl[0] - z * InvestigationCamera.ZOOM_HSCALE, x),
                    self.br[0] + z * InvestigationCamera.ZOOM_HSCALE)
                self.y1 = min(max(
                    self.tl[1] - z * InvestigationCamera.ZOOM_VSCALE, y),
                    self.br[1] + z * InvestigationCamera.ZOOM_VSCALE)
            else:
                self.x1 = x
                self.y1 = y
            self.z1 = z
        
        def x_express(self, st, at):
            x = self.x
            df = int(st * 60) - self.xf
            for i in xrange(df):
                x = x + (self.x1 - x) * 0.1
            self.xf += df
            self.x = x
            return x
        
        def y_express(self, st, at):
            y = self.y
            df = int(st * 60) - self.yf
            for i in xrange(df):
                y = y + (self.y1 - y) * 0.1
            self.yf += df
            self.y = y
            return y
        
        def z_express(self, st, at):
            z = self.z
            df = int(st * 60) - self.zf
            for i in xrange(df):
                z = z + (self.z1 - z) * 0.1
            self.zf += df
            self.z = z
            return z
        
        def x_freelook_express(self, st, at):
            x = self.x
            df = int(st * 60) - self.xf
            for i in xrange(df):
                x = x + (self.x1 - x) * 0.05
            self.xf += df
            self.x = x
            return x
        
        def y_freelook_express(self, st, at):
            y = self.y
            df = int(st * 60) - self.yf
            for i in xrange(df):
                y = y + (self.y1 - y) * 0.05
            self.yf += df
            self.y = y
            return y
        
        def z_freelook_express(self, st, at):
            z = self.z
            df = int(st * 60) - self.zf
            for i in xrange(df):
                z = z + (self.z1 - z) * 0.05
            self.zf += df
            self.z = z
            return z
        
        def screen_to_camera_space(self, x, y):
            """
            Transforms a point from mouse cursor coordinates to camera
            coordinates relative to the current camera position.
            """
            from renpy.config import screen_width, screen_height
            from renpy.store import _LAYER_Z
            
            
            
            
            
            s = _LAYER_Z / (_LAYER_Z - self.z)
            return (
                self.x + 12.5 * (x - 0.5 * screen_width) / s,
                self.y + 12.5 * (y - 0.5 * screen_height) / s)
init -998 python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    class IvCallCharacter(NVLAutoCharacter):
        """Slightly customized NVL subclass to handle calls.
        """
        def __init__(self, name, **kwargs):
            kwargs.setdefault('who_style', 'iv_call_actor_label_text')
            kwargs.setdefault('what_style', 'iv_call_dialogue')
            super(IvCallCharacter, self).__init__(
                who=name,
                screen='investigation_call_nvl',
                **kwargs)
            self.show_fn = self.show_core
            
            
            del self.window_args['style']
        
        def __call__(self, what, interact=True, _call_done=True, **kwargs):
            
            
            store._window_mode = 'call'
            
            
            super(IvCallCharacter, self).__call__(
                what,
                interact=interact,
                _call_done=_call_done,
                **kwargs)
        
        def show_core(self, who=None, what=None, **kwargs):
            """Call show function. Identical to the base one, except it
            also needs to figure out which layer to put the screen on.
            """
            
            _m1_investigation__nvl_screen_dialogue = store._m1_00nvl_mode__nvl_screen_dialogue
            
            ivmenu = (investigation.menu
                or investigation.index[investigation.label].menu)
            
            widget_properties, dialogue, show_args = _m1_investigation__nvl_screen_dialogue()
            kwargs.update(show_args)
            
            
            
            animation = merge_show_args(self).get('animation')
            if animation:
                kwargs.update(animation=animation)
            
            renpy.show_screen(
                self.screen,
                _layer=ivmenu.screen_layer,
                _transient=True,
                _widget_properties=widget_properties,
                dialogue=dialogue,
                **kwargs)
            renpy.shown_window()
            
            return renpy.get_widget(
                screen=self.screen,
                id='what',
                layer=ivmenu.screen_layer)
            
init 999 python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    auto_generate_store = 'store.c'
    characters = {
        (k, v)
        for k, v in store.__dict__.iteritems()
        if isinstance(v, ADVCharacter)
    }
    bases = set([
        ('adv', adv),
        ('name_only', name_only),
        ('narrator', narrator),
        ('nvl', nvl),
        ('nvl_narrator', nvl_narrator)
    ])

    renpy.ast.create_store(auto_generate_store)
    namespace, _special = renpy.ast.get_namespace(auto_generate_store)
    for k, v in (characters ^ bases):
        if k not in renpy.python.store_dicts[auto_generate_store]:
            namespace.set(k, IvCallCharacter(name=v.name))
python early in investigation:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def call_start_parse(lexer):
        parse = object()
        parse.imspec = tuple(iter(lexer.image_name_component, None))
        if not parse.imspec:
            lexer.require(lexer.image_name_component)
        parse.menu = None
        
        block_cp = lexer.checkpoint()
        if lexer.keyword('onlayer'):
            lexer.revert(block_cp)
            parse.menu = iv_parse_menu(lexer, require_tag=False)
        else:
            lexer.expect_eol()
        
        return parse

    def call_start_execute(parse):
        global callee, menu
        callee = parse.imspec[0]
        renpy.show(
            ' '.join(parse.imspec),
            at_list=[renpy.store.invisible],
            layer='master')
        if parse.menu:
            menu = parse.menu

    renpy.register_statement(
        'investigation call',
        parse=call_start_parse,
        execute=call_start_execute,
        block=False)

    renpy.register_statement(
        'investigation call block',
        parse=call_start_parse,
        execute=call_start_execute,
        block=True)

    def call_end_execute(parse):
        global callee, menu
        
        
        call_menu(((_("{#iv}CLOSE"), True),))
        
        outro_delays = renpy.store._window_modes['call'].get(
            'outro_delays', dict())
        outro_delay = (
            outro_delays.get(renpy.store._prev_window_mode)
            or outro_delays.get(None)
            or 0)
        renpy.pause(outro_delay, hard=True)
        renpy.pause(0, hard=True)
        
        
        renpy.hide(callee, layer='master')
        callee = None
        menu = None
        
        renpy.block_rollback()

    def call_menu(items):
        
        _m1_investigation__nvl_screen_dialogue = renpy.store._m1_00nvl_mode__nvl_screen_dialogue
        
        renpy.mode('nvl_menu')
        
        renpy.store.nvl_list = renpy.store.nvl_list or list()
        
        widget_properties, dialogue, show_args = _m1_investigation__nvl_screen_dialogue()
        scope = show_args.copy()
        scope["dialogue"] = dialogue

        
        return call_display_menu(
            items,
            widget_properties=widget_properties,
            screen='investigation_call_nvl',
            scope=scope,
            type='nvl')
        
        roll_forward = renpy.roll_forward_info()
        
        rv = ui.interact(roll_forward=roll_forward)
        renpy.checkpoint(rv)
        
        return rv

    def call_display_menu(
        items,
        interact=True,
        with_none=None,
        scope={},
        widget_properties=None,
        screen='choice',
        type='menu', 
        **kwargs):
        from renpy.exports import MenuEntry
        
        if interact:
            renpy.exports.mode(type)
            renpy.exports.choice_for_skipping()
        
        
        choices = [value for label, value in items if value]
        
        
        roll_forward = renpy.exports.roll_forward_info()
        if roll_forward not in choices:
            roll_forward = None
        
        
        if renpy.config.auto_choice_delay:
            renpy.ui.pausebehavior(
                renpy.config.auto_choice_delay,
                random.choice(choices))
        
        
        location = renpy.game.context().current
        
        
        if (renpy.exports.in_fixed_rollback()
            and renpy.config.fix_rollback_without_choice):
            renpy.ui.saybehavior()
        
        
        item_actions = list()
        
        props = widget_properties or dict()
        
        for (label, value) in items:
            if not label:
                value = None
            
            if value is not None:
                action = renpy.ui.ChoiceReturn(label, value, location)
                chosen = action.get_chosen()
            else:
                action = None
                chosen = False
            
            if renpy.config.choice_screen_chosen:
                me = MenuEntry((label, action, chosen))
            else:
                me = MenuEntry((label, action))
            
            me.caption = label
            me.action = action
            me.chosen = chosen
            
            item_actions.append(me)
            
            ivmenu = (menu or index[renpy.store.investigation.label].menu)
            renpy.exports.show_screen(
                screen,
                items=item_actions,
                _widget_properties=props,
                _transient=True,
                _layer=ivmenu.screen_layer,
                **scope)
        
        renpy.exports.shown_window()
        
        if interact:
            rv = renpy.ui.interact(
                mouse='menu',
                type=type,
                roll_forward=roll_forward)
            
            renpy.exports.checkpoint(rv)
            
            if with_none is None:
                with_none = renpy.config.implicit_with_none
            
            if with_none:
                renpy.game.interface.do_with(None, None)
            
            return rv
        
        return None

    renpy.register_statement(
        'investigation call end',
        parse=lambda lx: None,
        execute=call_end_execute)


python early in investigation:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    from collections import namedtuple

    item_registry = dict()

    ItemButtonRecord = namedtuple('ItemButtonRecord', ('label', 'condition'))
    class Item(object):
        def __init__(self, spec, name, icon, description, use_button, examine_button):
            self.spec = spec
            self.name_by_translation = {None: name}
            self.icon = icon
            self.description_by_translation = {None: description}
            self.use_button = use_button
            self.examine_button = examine_button
        
        def __repr__(self):
            return '<Item {spec}>'.format(spec=self.spec)
        
        @property
        def name(self):
            return self.name_by_translation.get(
                renpy.game.preferences.language,
                self.name_by_translation[None])
        
        @property
        def description(self):
            return self.description_by_translation.get(
                renpy.game.preferences.language,
                self.description_by_translation[None])

    def define_item_parse(lx, translating=False):
        from collections import OrderedDict
        import re
        from renpy.parser import parse_simple_expression_list
        
        params = dict()
        
        if translating:
            params['translation'] = lx.require(lx.word)
        
        params['spec'] = ' '.join(
            (lx.require(lx.name),) + tuple(iter(lx.name, None)))
        lx.require(':')
        lx.expect_block('define item statement')
        lx.expect_eol()
        
        sblx = lx.subblock_lexer()
        sblx.advance()
        sblx.require('name')
        params['name_expr'] = sblx.require(sblx.simple_expression)
        sblx.expect_eol()
        
        if not translating:
            sblx.advance()
            sblx.require('icon')
            
            params['icon'] = (
                sblx.string()
                or ' '.join(renpy.parser.parse_image_name(sblx, nodash=True)))
            sblx.expect_eol()
        
        sblx.advance()
        params['description'] = renpy.store.parse_multiline_string(sblx)
        
        if not translating:
            use_records = params['use_records'] = dict()
            examine_records = params['examine_records'] = dict()
            
            while sblx.advance():
                which = sblx.keyword('use') or sblx.keyword('examine')
                if not which:
                    sblx.error('expected either use or examine')
                
                sblx.require('in')
                labels = parse_simple_expression_list(sblx)
                
                sblx.require('jump')
                label = sblx.require(sblx.label_name)
                
                condition = (
                    sblx.require(sblx.simple_expression)
                    if sblx.keyword('if')
                    else None)
                
                record = ItemButtonRecord(label, condition)
                if which == 'use':
                    for label in labels:
                        use_records[label] = record
                elif which == 'examine':
                    for label in labels:
                        examine_records[label] = record
        
        return params

    def define_item_execute(params, translating=False):
        spec = params['spec']
        item = item_registry.get(spec)
        name = renpy.python.py_eval(params['name_expr'])
        
        
        
        
        if translating:
            tl = params['translation']
            
            if item is None:
                item = item_registry[spec] = Item(
                    spec=spec,
                    name=None,
                    icon=None,
                    description=None,
                    use_button=dict(),
                    examine_button=dict())
            
            item.name_by_translation[tl] = name
            item.description_by_translation[tl] = params['description']
        elif item is None:
            item = item_registry[spec] = Item(
                spec=spec,
                name=name,
                icon=params['icon'],
                description=params['description'],
                use_button=params['use_records'],
                examine_button=params['examine_records'])
        else:
            item.name_by_translation[None] = name
            item.icon = params['icon']
            item.description_by_translation[None] = params['description']
            item.use_button = params['use_records']
            item.examine_button = params['examine_records']

    renpy.register_statement(
        'define item',
        parse=define_item_parse,
        execute=define_item_execute,
        block=True,
        init=True)

    renpy.register_statement(
        'translate define item',
        parse=renpy.partial(define_item_parse, translating=True),
        execute=renpy.partial(define_item_execute, translating=True),
        block=True,
        init=True)

    def inventory_add_parse(lx):
        item_spec = ' '.join(
            (lx.require(lx.name),) + tuple(iter(lx.name, None)))
        lx.expect_eol()
        return item_spec

    def inventory_add_execute(a):
        item_tag = a.split(' ')[0]
        for i, spec in enumerate(inventory):
            if spec.split(' ')[0] == item_tag:
                inventory[i] = a
                break
        else:
            inventory.append(a)
        renpy.show_screen('iv_item_notify', spec=a)
        renpy.restart_interaction()

    renpy.register_statement(
        'inventory add',
        parse=inventory_add_parse,
        execute=inventory_add_execute)

    def inventory_remove_parse(lx):
        item_tag = lx.require(lx.name)
        lx.expect_eol()
        return item_tag

    def inventory_remove_execute(a):
        for i, spec in enumerate(inventory):
            if spec.split(' ')[0] == a:
                del inventory[i]
                break
        renpy.restart_interaction()

    renpy.register_statement(
        'inventory remove',
        parse=inventory_remove_parse,
        execute=inventory_remove_execute)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
