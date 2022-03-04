define lingyin = Character(_('青木铃音'), image="lingyin")
define lingyin_dsf_b1 = Character(_('青木铃音'), image="lingyin_dsf_b1")
define lingyin_dzf_b1 = Character(_('青木铃音'), image="lingyin_dzf_b1")
define lingyin_xsf_b1 = Character(_('青木铃音'), image="lingyin_xsf_b1")
define lingyin_xzf_b1 = Character(_('青木铃音'), image="lingyin_xzf_b1")


define composite lingyin_xzf_b1:
    path pick_actor_path("role/青木铃音/夏制服", "role/青木铃音/half/夏制服")
    transform:
        pos (0.36, 0.97)
        anchor (0.36, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(265, 252)

define composite lingyin_xzf_b2:
    path pick_actor_path("role/青木铃音/夏制服", "role/青木铃音/half/夏制服")
    transform:
        pos (0.55, 0.97)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(547, 204)

define composite lingyin_xsf_b1:
    path pick_actor_path("role/青木铃音/夏私服", "role/青木铃音/half/夏私服")
    transform:
        pos (0.36, 0.97)
        anchor (0.36, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(262, 251)

define composite lingyin_xsf_b2:
    path pick_actor_path("role/青木铃音/夏私服", "role/青木铃音/half/夏私服")
    transform:
        pos (0.55, 0.97)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(548, 206)

define composite lingyin_sz_b1:
    path pick_actor_path("role/青木铃音/水着", "role/青木铃音/half/水着")
    transform:
        pos (0.36, 0.97)
        anchor (0.36, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(265, 252)

define composite lingyin_sz_b2:
    path pick_actor_path("role/青木铃音/水着", "role/青木铃音/half/水着")
    transform:
        pos (0.55, 0.97)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(550, 205)

define composite lingyin_wnf_b1:
    path pick_actor_path("role/青木铃音/巫女服", "role/青木铃音/half/巫女服")
    transform:
        pos (0.36, 0.97)
        anchor (0.36, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(268, 251)

define composite lingyin_wnf_b2:
    path pick_actor_path("role/青木铃音/巫女服", "role/青木铃音/half/巫女服")
    transform:
        pos (0.55, 0.97)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(543, 208)

define composite lingyin_dzf_b1:
    path pick_actor_path("role/青木铃音/冬制服", "role/青木铃音/half/冬制服")
    transform:
        pos (0.36, 0.97)
        anchor (0.36, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(265.5, 251)

define composite lingyin_dzf_b2:
    path pick_actor_path("role/青木铃音/冬制服", "role/青木铃音/half/冬制服")
    transform:
        pos (0.55, 0.97)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(548, 205)

define composite lingyin_dsf_b1:
    path pick_actor_path("role/青木铃音/冬私服", "role/青木铃音/half/冬私服")
    transform:
        pos (0.36, 0.97)
        anchor (0.36, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(265.5, 251)

define composite lingyin_dsf_b2:
    path pick_actor_path("role/青木铃音/冬私服", "role/青木铃音/half/冬私服")
    transform:
        pos (0.55, 0.97)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(543.5, 206)

init python:
    side_actor_ypos['lingyin'] = 0.475
    investigation.call_actor_ypos['lingyin_dzf_b1'] = 0.115
    investigation.call_actor_ypos['lingyin_dsf_b1'] = 0.115
    investigation.call_actor_ypos['lingyin_xzf_b1'] = 0.115
    investigation.call_actor_ypos['lingyin_xsf_b1'] = 0.115
