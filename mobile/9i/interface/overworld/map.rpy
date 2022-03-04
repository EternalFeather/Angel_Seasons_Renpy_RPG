default _overworld_label = None

define overworld.camera_positions = {
    "cloqks": (9500, -4600, 2800),
    "road1": (10200, -500, 2800),
    "road2": (4170, -2550, 2800),
    "kindergarden": (11500, -3800, 2800),
    "school": (2500, -5800, 2800),
    "shenshe": (-200, -7100, 2800),
    "laboratory": (8500, -6150, 2800),
    "bridge": (400, -550, 2800),
    "rocket": (-9000, -8000, 2800)
}
define overworld.button_positions = {
    "cloqks": (0.955, 0.195),
    "road1": (1.045, 0.435),
    "road2": (0.641, 0.315),
    "kindergarden": (1.061, 0.295),
    "school": (0.483, 0.201),
    "shenshe": (0.405, -0.028),
    "laboratory": (0.679, 0.031),
    "bridge": (0.480, 0.433),
    "rocket": (0.080, -0.108)
}

screen rughzenhaide(**kwargs):
    layer "b1"

    default label_captions = {
        "cloqks": _("{#map}钟楼广场"),
        "road1": _("{#map}旧城区街道"),
        "road2": _("{#map}新城区街道"),
        "kindergarden": _("{#map}幼儿园"),
        "school": _("{#map}学校"),
        "shenshe": _("{#map}神社"),
        "laboratory": _("{#map}星天宫研究所"),
        "bridge": _("{#map}大桥"),
        "rocket": _("{#map}宇宙研究中心")
    }
    default label_transforms = {
        "hover": map_label_hover,
        "unhover": map_label_idle
    }

    default status = (None, "cloqks", True)

    fixed style_prefix "map":
        transform at unscale_by_layer("b1"):
            textbutton label_captions[status[1]] style "map_label":
                at label_transforms.get(status[0], map_label_null)(status[1])
                action NullAction()
                sensitive status[2]
        for location, value in kwargs.iteritems():
            python:
                label, condition = (
                    (value, None)
                    if isinstance(value, unicode)
                    else value)
                enabled = (condition is None or eval(condition))
            transform at (map_button_show if enabled else map_button_show_disabled):
                button at map_button_inter(location), unscale_by_layer("b1"):
                    if not enabled:
                        style "map_disabled_button"
                    action (Return(label) if enabled else NullAction())
                    hovered SetScreenVariable(
                        name="status",
                        value=("hover", location, enabled))
                    unhovered SetScreenVariable(
                        name="status",
                        value=("unhover", location, enabled))
init:
    transform side_map(tag):
        subpixel True
        xpos 0.28
        ypos (0.32 + side_actor_ypos.get(tag, 0.5))
        yanchor 0.0
        xzoom -1
        zoom 0.7

    transform map_button_inter(location):
        subpixel True
        pos overworld.button_positions[location]
        on idle:
            map_button_idle
        on hover:
            map_button_hover
    transform map_button_show:
        subpixel True
        transform_anchor True
        additive 1.0
        alpha 0.0
        zoom 1.6
        parallel:
            subpixel True
            easeout_cubic 1.0 yoffset scale(15) additive 0.25
            easein_cubic 1.0 yoffset scale(0) additive 0.0
            3.0
            repeat
        parallel:
            easein 1.0 additive 0.0
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easein_cubic 0.7 zoom 1.0
        on hide:
            linear 0.3 alpha 0
    transform map_button_show_disabled:
        subpixel True
        transform_anchor True
        additive 1.0
        alpha 0.0
        zoom 1.6
        parallel:
            easein 1.0 additive 0.0
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easein_cubic 0.7 zoom 1.0
        on hide:
            linear 0.3 alpha 0
    transform map_button_idle:
        additive 1.0
        easein 0.3 additive 0.0
    transform map_button_hover:
        easein 0.3 additive 1.0
    transform map_label_null(location):
        subpixel True
        pos overworld.button_positions[location]
        alpha 0
    transform map_label_hover(location):
        subpixel True
        crop_relative True
        pos overworld.button_positions[location]
        xoffset scale(0)
        crop (0.0, 0.0, 0.0, 1.0)
        parallel:
            linear 0.3 alpha 1
        parallel:
            power_in_time_warp_real 1.2 xoffset scale(60) crop (0.0, 0.0, 1.0, 1.0)
    transform map_label_idle(location):
        subpixel True
        pos overworld.button_positions[location]
        linear 0.3 alpha 0

    style map_button is default:
        xanchor 0.5
        yanchor 0.5
        child imagescale(1080)("9i/interface/overworld/icon.png")
    style map_disabled_button is map_button:
        child imagescale(1080)(im.Grayscale("9i/interface/overworld/icon.png"))
    style map_label is default:
        yanchor 0.5
        xminimum scale(294)
        ysize scale(86)
        xpadding scale(12)
        background Frame("9i/interface/overworld/label.png")
        insensitive_background Frame(
            im.Grayscale(
                "9i/interface/overworld/label.png"))
    style map_label_text is text:
        xcenter 0.5
        ycenter 0.5
        font "9i/fonts/浪漫雅圆.ttf"
        size scale(30)
        line_leading scale(9)
        line_spacing scale(-9)
        color "#fff"
        outlines [(scale(3.0), "#4e1c06")]
        insensitive_outlines [(scale(3.0), "#4f4f4f")]

init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def map_xy_express(duration):
        from renpy.curry import partial
        return partial(map_xy_express_impl, duration / 3)
    def map_xy_express_impl(duration, st, at):
        import random
        return 125 * max(1 - (st / duration) ** 0.25, 0) * (random.random() - 0.5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
