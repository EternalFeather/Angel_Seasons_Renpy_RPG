
init python:
    class DelayRun(renpy.Displayable):
        
        def __init__(self, delay, functions, **kwargs):
            super(DelayRun, self).__init__(**kwargs)
            self.delay = delay
            if not isinstance(functions, list):
                functions = [functions]
            self.functions = functions
        
        def render(self, width, height, st, at):
            
            
            render = renpy.Render(0, 0)
            
            
            return render
        
        def event(self, ev, x, y, st):
            if st >= self.delay:
                if renpy.game.interface.drawn_since(st - self.delay):
                    for function in self.functions:
                        function()
                    self.functions = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
