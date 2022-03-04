define liuli = Character(_('花山院琉璃'), image="liuli")
define liuli_dsf_b2 = Character(_('花山院琉璃'), image="liuli_dsf_b2")
define liuli_dzf_b2 = Character(_('花山院琉璃'), image="liuli_dzf_b2")
define liuli_yzf_b2 = Character(_('花山院琉璃'), image="liuli_yzf_b2")


define composite liuli_dzf_b1:
    path pick_actor_path("role/琉璃/冬制服", "role/琉璃/half/冬制服")
    transform:
        pos (0.5, 1.0)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(165, 246)

define composite liuli_dzf_b2:
    path pick_actor_path("role/琉璃/冬制服", "role/琉璃/half/冬制服")
    transform:
        pos (0.7, 1.0)
        anchor (0.7, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(479, 228)

define composite liuli_dzf_b3:
    path pick_actor_path("role/琉璃/冬制服", "role/琉璃/half/冬制服")
    transform:
        pos (0.5, 1.0)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(213, 201)

define composite liuli_dzf_b1_rune:
    path pick_actor_path("role/琉璃/冬制服", "role/琉璃/half/冬制服")
    transform:
        pos (0.5, 1.0)
        anchor (0.5, 2478./3309.)
        zoom scale_sprite_zoom(0.275)
    position rune
    position body:
        pos scale_sprite_offset(164, 167)
    position fa:
        pos scale_sprite_offset(329, 410)

define composite liuli_dzf_b2_rune:
    path pick_actor_path("role/琉璃/冬制服", "role/琉璃/half/冬制服")
    transform:
        pos (0.6, 1.0)
        anchor (0.6, 2478./3289.)
        zoom scale_sprite_zoom(0.275)
    position rune
    position body:
        pos scale_sprite_offset(141, 162)
    position fa:
        pos scale_sprite_offset(621, 392)

define composite liuli_dzf_b3_rune:
    path pick_actor_path("role/琉璃/冬制服", "role/琉璃/half/冬制服")
    transform:
        pos (0.5, 1.0)
        anchor (0.5, 2478./3296.)
        zoom scale_sprite_zoom(0.275)
    position rune
    position body:
        pos scale_sprite_offset(162, 162)
    position fa:
        pos scale_sprite_offset(375, 364)

define composite liuli_dsf_b1:
    path pick_actor_path("role/琉璃/冬私服", "role/琉璃/half/冬私服")
    transform:
        pos (0.5, 1.0)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(165, 246)

define composite liuli_dsf_b2:
    path pick_actor_path("role/琉璃/冬私服", "role/琉璃/half/冬私服")
    transform:
        pos (0.7, 1.0)
        anchor (0.7, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(483, 230)

define composite liuli_dsf_b3:
    path pick_actor_path("role/琉璃/冬私服", "role/琉璃/half/冬私服")
    transform:
        pos (0.5, 1.0)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(238, 201)

define composite liuli_wnf_b1:
    path pick_actor_path("role/琉璃/巫女服", "role/琉璃/half/巫女服")
    transform:
        pos (0.55, 1.0)
        anchor (0.55, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(170, 244)

define composite liuli_wnf_b2:
    path pick_actor_path("role/琉璃/巫女服", "role/琉璃/half/巫女服")
    transform:
        pos (0.65, 1.0)
        anchor (0.65, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(633, 228)

define composite liuli_wnf_b3:
    path pick_actor_path("role/琉璃/巫女服", "role/琉璃/half/巫女服")
    transform:
        pos (0.65, 1.0)
        anchor (0.65, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(625, 198)

define composite liuli_yzf_b1:
    path pick_actor_path("role/琉璃/宇宙服", "role/琉璃/half/宇宙服")
    transform:
        pos (0.53, 1.0)
        anchor (0.53, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(165, 244)

define composite liuli_yzf_b2:
    path pick_actor_path("role/琉璃/宇宙服", "role/琉璃/half/宇宙服")
    transform:
        pos (0.68, 1.0)
        anchor (0.68, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(486, 232)

define composite liuli_yzf_b3:
    path pick_actor_path("role/琉璃/宇宙服", "role/琉璃/half/宇宙服")
    transform:
        pos (0.58, 1.0)
        anchor (0.58, 2478./3224.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(215, 198)

init python:
    side_actor_ypos['liuli'] = 0.475
    investigation.call_actor_ypos['liuli_dsf_b2'] = 0.115
    investigation.call_actor_ypos['liuli_dzf_b2'] = 0.115
    investigation.call_actor_ypos['liuli_yzf_b2'] = 0.115
