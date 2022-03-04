

init 1 python:



    flcam = camera.flcam = camera.FreeLookCamera()
    config.underlay.append(flcam)

init python in camera:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    import renpy.store as store
    from renpy.display.core import Displayable
    from renpy.python import NoRollback
    from renpy.store import scale
    from renpy.store import _LAYER_Z
    from renpy.store import camera_move, camera_relative_move, camera_moves
    from renpy.store import camera_pop_move
    from renpy.store import layer_move, layer_moves, all_moves

    def chained_express(funcs, st, at):
        return sum(func(st, at) for func in funcs)
    def chain_express(*funcs):
        from renpy.curry import partial
        return partial(chained_express, funcs)

    def freelook_x_express(st, at):
        df = int(st * 60) - flcam.xf
        
        
        
        
        if (df < 60):
            for i in xrange(df):
                flcam.xo = flcam.xo + (flcam.xo1 - flcam.xo) * 0.05
            flcam.xf += df
        else:
            flcam.xo = flcam.xo1
            flcam.xf = df
        return flcam.xo

    def freelook_y_express(st, at):
        df = int(st * 60) - flcam.yf
        if (df < 60):
            for i in xrange(df):
                flcam.yo += (flcam.yo1 - flcam.yo) * 0.05
            flcam.yf += df
        else:
            flcam.yo = flcam.yo1
            flcam.yf = df
        return flcam.yo

    def freelook_z_express(st, at):
        df = int(st * 60) - flcam.zf
        if (df < 60):
            for i in xrange(df):
                flcam.zo += (flcam.zo1 - flcam.zo) * 0.05
            flcam.zf += df
        else:
            flcam.zo = flcam.zo1
            flcam.zf = df
        return flcam.zo

    @renpy.pure
    class FreeLookCamera(Displayable, NoRollback):
        """
        Camera wrapper which adds free look to standard camera operations.
        """
        
        
        
        
        xspan = scale(64)
        yspan = scale(36)
        zspan = scale(0)
        
        def __init__(self,
            xspan=None, yspan=None, zspan=None,
            x_express=None, y_express=None, z_express=None,
            *args, **kwargs):
            super(FreeLookCamera, self).__init__(*args, **kwargs)
            
            
            
            
            
            if xspan is not None:
                self.xspan = xspan
            if yspan is not None:
                self.yspan = yspan
            if zspan is not None:
                self.zspan = zspan
            
            
            
            self.x_express = x_express or freelook_x_express
            self.y_express = y_express or freelook_y_express
            self.z_express = z_express or freelook_z_express
            
            
            self.xo = 0.0
            self.yo = 0.0
            self.zo = 0.0
            
            
            
            self.xo1 = 0.0
            self.yo1 = 0.0
            self.zo1 = 0.0
            
            
            
            
            
            
            self.xf = 0
            self.yf = 0
            self.zf = 0
            
            
            
            self.running = False
        
        def render(self, width, height, st, at):
            return renpy.Render(width, height)
        
        def event(self, ev, x, y, st):
            
            if self.running is False:
                self.running = True
                self.on_tick(x, y, st)
                self.xo = self.xo1
                self.yo = self.yo1
                self.zo = self.zo1 = 0.0
            
            
            if renpy.map_event(ev, "mousedown_4"):
                self.on_zoom(self.zspan, x, y, st)
            if renpy.map_event(ev, "mousedown_5"):
                self.on_zoom(0.0, x, y, st)
            
            
            return self.on_tick(x, y, st)
        
        def expressify(self, kwargs):
            x_express = (
                chain_express(kwargs.pop('x_express'), self.x_express)
                if 'x_express' in kwargs
                else self.x_express)
            y_express = (
                chain_express(kwargs.pop('y_express'), self.y_express)
                if 'y_express' in kwargs
                else self.y_express)
            z_express = (
                chain_express(kwargs.pop('z_express'), self.z_express)
                if 'z_express' in kwargs
                else self.z_express)
            return (x_express, y_express, z_express)
        
        def move(self, *args, **kwargs):
            x_express, y_express, z_express = self.expressify(kwargs)
            camera_move(
                *args,
                x_express=x_express,
                y_express=y_express,
                z_express=z_express,
                **kwargs)
        
        def relmove(self, *args, **kwargs):
            x_express, y_express, z_express = self.expressify(kwargs)
            camera_relative_move(
                *args,
                x_express=x_express,
                y_express=y_express,
                z_express=z_express,
                **kwargs)
        
        def popmove(self, *args, **kwargs):
            x_express, y_express, z_express = self.expressify(kwargs)
            camera_pop_move(
                *args,
                x_express=x_express,
                y_express=y_express,
                z_express=z_express,
                **kwargs)
        
        def moves(self, *args, **kwargs):
            x_express, y_express, z_express = self.expressify(kwargs)
            camera_moves(
                *args,
                x_express=x_express,
                y_express=y_express,
                z_express=z_express,
                **kwargs)
        
        def layer_move(self, *args, **kwargs):
            x_express, y_express, z_express = self.expressify(kwargs)
            layer_move(
                *args,
                x_express=x_express,
                y_express=y_express,
                z_express=z_express,
                **kwargs)
        
        def layer_moves(self, *args, **kwargs):
            x_express, y_express, z_express = self.expressify(kwargs)
            layer_moves(
                *args,
                x_express=x_express,
                y_express=y_express,
                z_express=z_express,
                **kwargs)
        
        def all_moves(self, *args, **kwargs):
            x_express, y_express, z_express = self.expressify(kwargs)
            all_moves(
                *args,
                x_express=x_express,
                y_express=y_express,
                z_express=z_express,
                **kwargs)
        
        def start(self):
            """
            Starts the free look function at the current camera position.
            """
            
            
            
            
            self.move(
                store._camera_x,
                store._camera_y,
                store._camera_z)
        
        def stop(self):
            """
            Stops the camera at the current free look offset.
            """
            camera_move(
                store._camera_x + self.xo,
                store._camera_y + self.yo,
                store._camera_z + self.zo)
        
        def on_zoom(self, target_z, x, y, st):
            self.zo1 = target_z
            
            
            
            ax, ay, az = screen_to_camera_space(
                store._camera_x + self.xo,
                store._camera_y + self.yo,
                store._camera_z + self.zo,
                x,
                y)
            
            
            
            
            dx = ax - store._camera_x - self.xo
            dy = ay - store._camera_y - self.yo
            os = _LAYER_Z / (_LAYER_Z - store._camera_z - self.zo)
            cs = _LAYER_Z / (_LAYER_Z - store._camera_z - self.zo1)
            s = cs / os
            self.xo1 = ax + dx / s
            self.yo1 = ay + dy / s
        
        def on_tick(self, x, y, st):
            from renpy.config import screen_width, screen_height
            
            
            
            
            
            bs = _LAYER_Z / (_LAYER_Z - store._camera_z)
            os = _LAYER_Z / (_LAYER_Z - store._camera_z - self.zo)
            bw = 12.5 * screen_width / bs
            bh = 12.5 * screen_height / bs
            ow = 12.5 * screen_width / os
            oh = 12.5 * screen_height / os
            xspan = bw + self.xspan - ow
            yspan = bh + self.yspan - oh
            
            
            
            self.xo1 = xspan * 2.0 * (x / screen_width - 0.5)
            self.yo1 = yspan * 2.0 * (y / screen_height - 0.5)



default _camera_stack = list()

init -1 python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def camera_pop():
        return _camera_stack.pop()

    def camera_pop_move(*args, **kwargs):
        x, y, z, r = camera_pop()
        camera_move(x, y, z, r, *args, **kwargs)

    def camera_push():
        _camera_stack.append(
            (_camera_x, _camera_y, _camera_z, _camera_rotate))

init -1 python in camera:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def screen_to_camera_space(camera_x, camera_y, camera_z, mouse_x, mouse_y):
        """
        Transforms a point from mouse cursor coordinates to camera
        coordinates relative to the current camera position.
        """
        from renpy.config import screen_width, screen_height
        
        
        
        
        
        s = _LAYER_Z / (_LAYER_Z - camera_z)
        return (
            camera_x + 12.5 * (mouse_x - 0.5 * screen_width) / s,
            camera_y + 12.5 * (mouse_y - 0.5 * screen_height) / s,
            camera_z)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
