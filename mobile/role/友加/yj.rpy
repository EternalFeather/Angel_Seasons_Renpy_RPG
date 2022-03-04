define yj = Character(_('植澄友加'), image="yj")
define yj_dsf_b1 = Character(_('植澄友加'), image="yj_dsf_b1")
define yj_dzf_b1 = Character(_('植澄友加'), image="yj_dzf_b1")
define yj_tcf_b1 = Character(_('植澄友加'), image="yj_tcf_b1")


define composite yj_dzf_b1:
    path pick_actor_path("role/友加/冬制服", "role/友加/half/冬制服")
    transform:
        pos (0.4, 0.95)
        anchor (0.4, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(612, 274)

define composite yj_dzf_b2:
    path pick_actor_path("role/友加/冬制服", "role/友加/half/冬制服")
    transform:
        pos (0.55, 0.95)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(1107, 223)

define composite yj_dzf_b3:
    path pick_actor_path("role/友加/冬制服", "role/友加/half/冬制服")
    transform:
        pos (0.55, 0.95)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(969.5, 220)

define composite yj_dzf_b1_rune:
    path pick_actor_path("role/友加/冬制服", "role/友加/half/冬制服")
    transform:
        pos (0.4, 0.955)
        anchor (0.4, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position rune
    position body:
        pos scale_sprite_offset(170.5, 162.5)
    position fa:
        pos scale_sprite_offset(780, 437)

define composite yj_dzf_b2_rune:
    path pick_actor_path("role/友加/冬制服", "role/友加/half/冬制服")
    transform:
        pos (0.55, 0.955)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position rune
    position body:
        pos scale_sprite_offset(169.5, 170.5)
    position fa:
        pos scale_sprite_offset(1275, 393)

define composite yj_tcf_b1:
    path pick_actor_path("role/友加/体操服", "role/友加/half/体操服")
    transform:
        pos (0.4, 0.95)
        anchor (0.4, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(612, 274)

define composite yj_tcf_b2:
    path pick_actor_path("role/友加/体操服", "role/友加/half/体操服")
    transform:
        pos (0.55, 0.95)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(1096, 220)

define composite yj_tcf_b3:
    path pick_actor_path("role/友加/体操服", "role/友加/half/体操服")
    transform:
        pos (0.55, 0.95)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(971.5, 225)

define composite yj_dsf_b1:
    path pick_actor_path("role/友加/冬私服", "role/友加/half/冬私服")
    transform:
        pos (0.4, 0.95)
        anchor (0.4, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(610, 275)

define composite yj_dsf_b2:
    path pick_actor_path("role/友加/冬私服", "role/友加/half/冬私服")
    transform:
        pos (0.55, 0.95)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(1104, 223)

define composite yj_dsf_b3:
    path pick_actor_path("role/友加/冬私服", "role/友加/half/冬私服")
    transform:
        pos (0.55, 0.95)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(974.5, 223)

define composite yj_dsf_b2_rune:
    path pick_actor_path("role/友加/冬私服", "role/友加/half/冬私服")
    transform:
        pos (0.55, 0.95)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position rune
    position body:
        pos scale_sprite_offset(169.5, 170.5)
    position fa:
        pos scale_sprite_offset(1271, 394)

init python:
    side_actor_ypos['yj'] = 0.475
    investigation.call_actor_xpos['yj_dsf_b1'] = 0.2
    investigation.call_actor_ypos['yj_dsf_b1'] = 0.115
    investigation.call_actor_ypos['yj_dzf_b1'] = 0.115
    investigation.call_actor_ypos['yj_tcf_b1'] = 0.115

