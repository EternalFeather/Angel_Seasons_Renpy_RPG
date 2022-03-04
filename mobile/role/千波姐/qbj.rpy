define qbj = Character(_('泽村柚子'), image="qbj")
define qbj_dzf_b1 = Character(_('泽村柚子'), image="qbj_dzf_b1")


define composite qbj_dzf_b1:
    path pick_actor_path("role/千波姐/冬制服", "role/千波姐/half/冬制服")
    transform:
        pos (0.5, 0.95)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(390, 240)

init python:
    side_actor_ypos['qbj'] = 0.475
    investigation.call_actor_ypos['qbj_dzf_b1'] = 0.115

