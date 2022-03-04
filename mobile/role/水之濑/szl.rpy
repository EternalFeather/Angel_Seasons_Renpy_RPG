define szl = Character(_('水之濑凛'), image="szl")
define szl_dzf_b2 = Character(_('水之濑凛'), image="szl_dzf_b2")
define szl_dsf_b2 = Character(_('水之濑凛'), image="szl_dsf_b3")


define composite szl_dzf_b1:
    path pick_actor_path("role/水之濑/冬制服", "role/水之濑/half/冬制服")
    transform:
        pos (0.33, 0.942)
        anchor (0.33, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(382, 291)

define composite szl_dzf_b2:
    path pick_actor_path("role/水之濑/冬制服", "role/水之濑/half/冬制服")
    transform:
        pos (0.5, 0.942)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(918, 236)

define composite szl_dzf_b3:
    path pick_actor_path("role/水之濑/冬制服", "role/水之濑/half/冬制服")
    transform:
        pos (0.55, 0.95)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.280)
    position body
    position fa:
        pos scale_sprite_offset(674, 0)

define composite szl_dzf_knife_b1:
    path pick_actor_path("role/水之濑/冬制服佩刀", "role/水之濑/half/冬制服佩刀")
    transform:
        pos (0.33, 0.942)
        anchor (0.33, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(382, 291)

define composite szl_dzf_knife_b2:
    path pick_actor_path("role/水之濑/冬制服佩刀", "role/水之濑/half/冬制服佩刀")
    transform:
        pos (0.5, 0.942)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(918, 236)

define composite szl_dzf_knife_b3:
    path pick_actor_path("role/水之濑/冬制服佩刀", "role/水之濑/half/冬制服佩刀")
    transform:
        pos (0.55, 0.952)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.290)
    position body
    position fa:
        pos scale_sprite_offset(659, 87)

define composite szl_dzf_knife_b1_rune:
    path pick_actor_path("role/水之濑/冬制服佩刀", "role/水之濑/half/冬制服佩刀")
    transform:
        pos (0.33, 0.942)
        anchor (0.33, 2478./3424.)
        zoom scale_sprite_zoom(0.270)
    position rune
    position body:
        pos scale_sprite_offset(150, 167)
    position fa:
        pos scale_sprite_offset(533, 457)

define composite szl_dzf_knife_b2_rune:
    path pick_actor_path("role/水之濑/冬制服佩刀", "role/水之濑/half/冬制服佩刀")
    transform:
        pos (0.5, 0.942)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position rune
    position body:
        pos scale_sprite_offset(158, 164)
    position fa:
        pos scale_sprite_offset(1075, 400)

define composite szl_dzf_knife_b3_rune:
    path pick_actor_path("role/水之濑/冬制服佩刀", "role/水之濑/half/冬制服佩刀")
    transform:
        pos (0.55, 0.932)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.280)
    position rune
    position body:
        pos scale_sprite_offset(152, 146)
    position fa:
        pos scale_sprite_offset(811, 230)

define composite szl_dsf_b1:
    path pick_actor_path("role/水之濑/冬私服", "role/水之濑/half/冬私服")
    transform:
        pos (0.33, 0.942)
        anchor (0.33, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(381, 290)

define composite szl_dsf_b2:
    path pick_actor_path("role/水之濑/冬私服", "role/水之濑/half/冬私服")
    transform:
        pos (0.5, 0.942)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(914, 236)

define composite szl_dsf_b3:
    path pick_actor_path("role/水之濑/冬私服", "role/水之濑/half/冬私服")
    transform:
        pos (0.55, 0.950)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.280)
    position body
    position fa:
        pos scale_sprite_offset(674, 0)

define composite szl_dsf_knife_b1:
    path pick_actor_path("role/水之濑/冬私服佩刀", "role/水之濑/half/冬私服佩刀")
    transform:
        pos (0.33, 0.942)
        anchor (0.33, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(381, 291)

define composite szl_dsf_knife_b2:
    path pick_actor_path("role/水之濑/冬私服佩刀", "role/水之濑/half/冬私服佩刀")
    transform:
        pos (0.5, 0.942)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(913, 236)

define composite szl_dsf_knife_b3:
    path pick_actor_path("role/水之濑/冬私服佩刀", "role/水之濑/half/冬私服佩刀")
    transform:
        pos (0.55, 0.932)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.295)
    position body
    position fa:
        pos scale_sprite_offset(633.5, 198)

init python:
    side_actor_ypos['szl'] = 0.475
    investigation.call_actor_ypos['szl_dzf_b2'] = 0.115
    investigation.call_actor_ypos['szl_dsf_b2'] = 0.115

