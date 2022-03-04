define nurse = Character(_('护士'), image="nurse")
define nurse_dzf_b1 = Character(_('护士'), image="nurse_dzf_b1")


define composite nurse_dzf_b1:
    path pick_actor_path("role/护士/冬制服", "role/护士/half/冬制服")
    transform:
        pos (0.5, 0.98)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.315)
    position body
    position fa:
        pos scale_sprite_offset(199, 333)

init python:
    side_actor_ypos['nurse'] = 0.475
    investigation.call_actor_ypos['nurse_dzf_b1'] = 0.115

