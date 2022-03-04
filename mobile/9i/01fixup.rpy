define persistent.fixups = set(_persistent_fixups)

python early:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    _persistent_fixups = dict()

    def fixup_persistent(name):
        """Decorator. Mark a function as a fixup for persistent data.
        """
        def _fixup_persistent(fn):
            _persistent_fixups[name] = fn
            return fn
        return _fixup_persistent



init 999 python hide:
    for fixup in set(_persistent_fixups) - persistent.fixups:
        _persistent_fixups[fixup]()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
