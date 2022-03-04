define xshz = Character(_('学生会长'), image="xshz")
define xshz_xzf_b1 = Character(_('学生会长'), image="xshz_xzf_b1")


define composite xshz_xzf_b1:
    path pick_actor_path("role/学生会长/夏制服", "role/学生会长/half/夏制服")
    transform:
        pos (0.5, 0.965)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(498, 232)

init python:
    side_actor_ypos['xshz'] = 0.475
    investigation.call_actor_ypos['xshz_xzf_b1'] = 0.115

