define jsqd = Character(_('姬神千冬'), image="jsqd")
define jsqd_dsf_b1 = Character(_('姬神千冬'), image="jsqd_dsf_b1")


define composite jsqd_dsf_b1:
    path pick_actor_path("role/千冬/冬私服", "role/千冬/half/冬私服")
    transform:
        pos (0.6, 0.98)
        anchor (0.6, 2478./2824.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(825, 415)

init python:
    side_actor_ypos['jsqd'] = 0.475
    investigation.call_actor_ypos['jsqd_dsf_b1'] = 0.115

