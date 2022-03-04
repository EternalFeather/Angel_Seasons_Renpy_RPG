define yczs = Character(_('一诚总司'), image="yczs")
define yczs_dzf_b1 = Character(_('一诚总司'), image="yczs_dzf_b1")
define yczs_xzf_b1 = Character(_('一诚总司'), image="yczs_xzf_b1")
define yczs_xsf_b1 = Character(_('一诚总司'), image="yczs_xsf_b1")


define composite yczs_xzf_b1:
    path pick_actor_path("role/一诚总司/夏制服", "role/一诚总司/half/夏制服")
    transform:
        pos (0.48, 0.95)
        anchor (0.48, 2478./3444.)
        zoom scale_sprite_zoom(0.295)
    position body
    position fa:
        pos scale_sprite_offset(540, 305)

define composite yczs_sz_b1:
    path pick_actor_path("role/一诚总司/水着", "role/一诚总司/half/水着")
    transform:
        pos (0.48, 0.95)
        anchor (0.48, 2478./3444.)
        zoom scale_sprite_zoom(0.295)
    position body
    position fa:
        pos scale_sprite_offset(542, 303)

define composite yczs_xsf_b1:
    path pick_actor_path("role/一诚总司/夏私服", "role/一诚总司/half/夏私服")
    transform:
        pos (0.48, 0.95)
        anchor (0.48, 2478./3444.)
        zoom scale_sprite_zoom(0.295)
    position body
    position fa:
        pos scale_sprite_offset(540, 303)

define composite yczs_dzf_b1:
    path pick_actor_path("role/一诚总司/冬制服", "role/一诚总司/half/冬制服")
    transform:
        pos (0.48, 0.95)
        anchor (0.48, 2478./3444.)
        zoom scale_sprite_zoom(0.295)
    position body
    position fa:
        pos scale_sprite_offset(550, 304)

init python:
    side_actor_ypos['yczs'] = 0.475
    investigation.call_actor_ypos['yczs_dzf_b1'] = 0.115
    investigation.call_actor_ypos['yczs_xzf_b1'] = 0.115
    investigation.call_actor_ypos['yczs_xsf_b1'] = 0.115

