define lhx = Character(_('立花希'), image="lhx")
define lhx_dsf_b2 = Character(_('立花希'), image="lhx_dsf_b2")
define lhx_dzf_b2 = Character(_('立花希'), image="lhx_dzf_b2")


define composite lhx_dsf_b1:
    path pick_actor_path("role/立花希/冬私服", "role/立花希/half/冬私服")
    transform:
        pos (0.58, 1.02)
        anchor (0.58, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(574, 270)

define composite lhx_dsf_b1_rune:
    path pick_actor_path("role/立花希/冬私服", "role/立花希/half/冬私服")
    transform:
        pos (0.55, 1.02)
        anchor (0.55, 2478./3284.)
        zoom scale_sprite_zoom(0.285)
    position rune
    position body:
        pos scale_sprite_offset(149, 169)
    position fa:
        pos scale_sprite_offset(723, 436)

define composite lhx_dsf_b2:
    path pick_actor_path("role/立花希/冬私服", "role/立花希/half/冬私服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(382, 233)

define composite lhx_dsf_b2_rune:
    path pick_actor_path("role/立花希/冬私服", "role/立花希/half/冬私服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2478./3284.)
        zoom scale_sprite_zoom(0.285)
    position rune
    position body:
        pos scale_sprite_offset(159, 167)
    position fa:
        pos scale_sprite_offset(541, 396) 

define composite lhx_dsf_b3:
    path pick_actor_path("role/立花希/冬私服", "role/立花希/half/冬私服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(349, 272)

define composite lhx_dsf_b3_rune:
    path pick_actor_path("role/立花希/冬私服", "role/立花希/half/冬私服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2478./3284.)
        zoom scale_sprite_zoom(0.285)
    position rune
    position body:
        pos scale_sprite_offset(157, 164)
    position fa:
        pos scale_sprite_offset(505, 435)

define composite lhx_dzf_b1:
    path pick_actor_path("role/立花希/冬制服", "role/立花希/half/冬制服")
    transform:
        pos (0.55, 1.02)
        anchor (0.55, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(574, 270)

define composite lhx_dzf_b2:
    path pick_actor_path("role/立花希/冬制服", "role/立花希/half/冬制服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(382, 233)

define composite lhx_dzf_b3:
    path pick_actor_path("role/立花希/冬制服", "role/立花希/half/冬制服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(349, 272)

define composite lhx_zf_b1:
    path pick_actor_path("role/立花希/制服", "role/立花希/half/制服")
    transform:
        pos (0.55, 1.02)
        anchor (0.55, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(441, 272)

define composite lhx_zf_b2:
    path pick_actor_path("role/立花希/制服", "role/立花希/half/制服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(302, 235)

define composite lhx_zf_b3:
    path pick_actor_path("role/立花希/制服", "role/立花希/half/制服")
    transform:
        pos (0.5, 1.02)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(214, 273)

init python:
    side_actor_ypos['lhx'] = 0.475
    investigation.call_actor_xpos['lhx_dzf_b2'] = 0.48
    investigation.call_actor_xpos['lhx_dsf_b2'] = 0.48
    investigation.call_actor_ypos['lhx_dzf_b2'] = 0.115
    investigation.call_actor_ypos['lhx_dsf_b2'] = 0.115

