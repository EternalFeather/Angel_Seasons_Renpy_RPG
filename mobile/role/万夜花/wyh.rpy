define wyh = Character(_('南星万夜花'), image="wyh")
define wyh_wnf_b1 = Character(_('南星万夜花'), image="wyh_wnf_b1")


define composite wyh_xsf_b1:
    path pick_actor_path("role/万夜花/夏私服", "role/万夜花/half/夏私服")
    transform:
        pos (0.415, 0.95)
        anchor (0.415, 2478./3624.)
        zoom scale_sprite_zoom(0.295)
    position body
    position fa:
        pos scale_sprite_offset(378, 198)

define composite wyh_wnf_b1:
    path pick_actor_path("role/万夜花/巫女服", "role/万夜花/half/巫女服")
    transform:
        pos (0.5, 0.95)
        anchor (0.5, 2478./3624.)
        zoom scale_sprite_zoom(0.295)
    position body
    position fa:
        pos scale_sprite_offset(677, 199)

init python:
    side_actor_ypos['wyh'] = 0.475
    investigation.call_actor_ypos['wyh_wnf_b1'] = 0.115

