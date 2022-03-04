

python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def parse_pause(lx):
        delay = lx.simple_expression()
        hard = bool(lx.keyword('hard')) if delay is not None else None
        return dict(delay=delay, hard=hard)

    def lint_pause(p):
        if p['delay']:
            _try_eval(p['delay'], 'pause statement')

    def execute_pause(arg):
        if arg['delay']:
            delay = renpy.python.py_eval(arg['delay'])
            if arg['hard']:
                renpy.pause(delay, hard=True)
            else:
                renpy.with_statement(Pause(delay))
        else:
            renpy.pause()

    renpy.register_statement(
        'pause',
        parse=parse_pause,
        lint=lint_pause,
        execute=execute_pause)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
