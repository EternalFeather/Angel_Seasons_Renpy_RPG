define ycxt = Character(_('一诚小桃'), image="ycxt")
define ycxt_dzf_b1 = Character(_('一诚小桃'), image="ycxt_dzf_b1")


define composite ycxt_dzf_b1:
    path pick_actor_path("role/小桃/冬制服", "role/小桃/half/冬制服")
    transform:
        pos (0.5, 1.07)
        anchor (0.5, 2478./2824.)
        zoom scale_sprite_zoom(0.270)
    position body
    position fa:
        pos scale_sprite_offset(0, 198)

define composite ycxt_dzf_b2:
    path pick_actor_path("role/小桃/冬制服", "role/小桃/half/冬制服")
    transform:
        pos (0.46, 1.07)
        anchor (0.46, 2478./2824.)
        zoom scale_sprite_zoom(0.270)
    position body
    position fa:
        pos scale_sprite_offset(0, 198)

init python:
    side_actor_ypos['ycxt'] = 0.475
    investigation.call_actor_ypos['ycxt_dzf_b1'] = 0.115

