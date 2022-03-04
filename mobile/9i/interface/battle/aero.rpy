
init -999 python hide:
    config.keymap['aerolinguistics'] = ['A']


init python in aero:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    @renpy.pure
    def get_button_angle(i, n):
        """Gets the position in degrees of the i-th skill on the
        wheel, for n languages total."""
        if n == 1:
            return 0.
        elif n == 2:
            if i == 1:
                return -60.
            else:
                return +60.
        elif n <= 6:
            return [-60., 60., -90., 90., -120., 120.][i - 1]
        else:
            interval = 360 / n
            return interval * -0.5 + (i - 1) * interval
