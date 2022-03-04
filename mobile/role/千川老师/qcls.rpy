define qcls = Character(_('千川老师'), image="qcls")
define qcls_zf_b1 = Character(_('千川老师'), image="qcls_zf_b1")


define composite qcls_zf_b1:
    path pick_actor_path("role/千川老师/制服", "role/千川老师/half/制服")
    transform:
        pos (0.44, 0.92)
        anchor (0.44, 2478./3424.)
        zoom scale_sprite_zoom(0.280)
    position body
    position fa:
        pos scale_sprite_offset(283, 238)

define composite qcls_zf_b2:
    path pick_actor_path("role/千川老师/制服", "role/千川老师/half/制服")
    transform:
        pos (0.51, 0.92)
        anchor (0.51, 2478./3424.)
        zoom scale_sprite_zoom(0.278)
    position body
    position fa:
        pos scale_sprite_offset(288, 238)

define composite qcls_zf_b1_rune:
    path pick_actor_path("role/千川老师/制服", "role/千川老师/half/制服")
    transform:
        pos (0.44, 0.92)
        anchor (0.44, 2478./3424.)
        zoom scale_sprite_zoom(0.280)
    position rune
    position body:
        pos scale_sprite_offset(165.5, 299.5)
    position fa:
        pos scale_sprite_offset(446, 535)

define composite qcls_zf_b2_rune:
    path pick_actor_path("role/千川老师/制服", "role/千川老师/half/制服")
    transform:
        pos (0.51, 0.92)
        anchor (0.51, 2478./3424.)
        zoom scale_sprite_zoom(0.278)
    position rune
    position body:
        pos scale_sprite_offset(163, 162.5)
    position fa:
        pos scale_sprite_offset(450, 398)


init python:
    side_actor_ypos['qcls'] = 0.475
    investigation.call_actor_ypos['qcls_zf_b1'] = 0.115



