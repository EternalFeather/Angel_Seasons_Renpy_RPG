define dh = Character(_('神野大和'), image="dh")
define dh_zf_b1 = Character(_('神野大和'), image="dh_zf_b1")


define composite dh_zf_b1:
    path pick_actor_path("role/神野大和/制服", "role/神野大和/half/制服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2728./3824.)
        zoom scale_sprite_zoom(0.305)
    position body
    position fa:
        pos scale_sprite_offset(507, 253)

init python:
    side_actor_ypos['dh'] = 0.475
    investigation.call_actor_ypos['dh_zf_b1'] = 0.115

