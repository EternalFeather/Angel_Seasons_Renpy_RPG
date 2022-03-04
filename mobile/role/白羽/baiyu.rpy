define baiyu = Character(_('姬神白羽'), image="baiyu")
define baiyu_yjf_b1 = Character(_('姬神白羽'), image="baiyu_yjf_b1")


define composite baiyu_yjf_b1:
    path pick_actor_path("role/白羽/研究服", "role/白羽/half/研究服")
    transform:
        pos (0.5, 0.91)
        anchor (0.5, 2478./3474.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(629, 263)

init python:
    side_actor_ypos['baiyu'] = 0.475
    investigation.call_actor_ypos['baiyu_yjf_b1'] = 0.115

