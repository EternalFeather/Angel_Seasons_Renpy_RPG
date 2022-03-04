define ycnn = Character(_('一诚奶奶'), image="ycnn")
define ycnn_sf_b1 = Character(_('一诚奶奶'), image="ycnn_sf_b1")


define composite ycnn_sf_b1:
    path pick_actor_path("role/一诚奶奶/私服", "role/一诚奶奶/half/私服")
    transform:
        pos (0.5, 0.92)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.265)
    position body
    position fa:
        pos scale_sprite_offset(212, 262)

init python:
    side_actor_ypos['ycnn'] = 0.475
    investigation.call_actor_ypos['ycnn_sf_b1'] = 0.115

