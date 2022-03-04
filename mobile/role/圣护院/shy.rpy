define shy = Character(_('圣护院'), image="shy")
define shy_yjf_b1 = Character(_('圣护院'), image="shy_yjf_b1")


define composite shy_yjf_b1:
    path pick_actor_path("role/圣护院/研究服", "role/圣护院/half/研究服")
    transform:
        pos (0.4, 0.91)
        anchor (0.4, 2478./3524.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(471, 291)

init python:
    side_actor_ypos['shy'] = 0.475
    investigation.call_actor_xpos['shy_yjf_b1'] = 0.2
    investigation.call_actor_ypos['shy_yjf_b1'] = 0.115

