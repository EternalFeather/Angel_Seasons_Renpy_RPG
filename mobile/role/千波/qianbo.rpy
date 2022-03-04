define qb = Character(_('泽村千波'), image="qb")


define composite qianbo_dzf_b1:
    path pick_actor_path("role/千波/冬制服", "role/千波/half/冬制服")
    transform:
        pos (0.45, 0.985)
        anchor (0.45, 2478./3024.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(38, 0)

define composite qianbo_dzf_b2:
    path pick_actor_path("role/千波/冬制服", "role/千波/half/冬制服")
    transform:
        pos (0.45, 0.985)
        anchor (0.45, 2478./3024.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(38, 0)

define composite qianbo_dsf_b1:
    path pick_actor_path("role/千波/冬私服", "role/千波/half/冬私服")
    transform:
        pos (0.45, 0.985)
        anchor (0.45, 2478./3024.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(38, 0)

define composite qianbo_dsf_b2:
    path pick_actor_path("role/千波/冬私服", "role/千波/half/冬私服")
    transform:
        pos (0.45, 0.985)
        anchor (0.45, 2478./3024.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(38, 0)

init python:
    side_actor_ypos['qb'] = 0.475
    investigation.call_actor_ypos['qb'] = 0.115

