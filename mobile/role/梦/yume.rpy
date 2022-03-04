define yume = Character(_('青木翔子（梦）'), image='yume')
define yume_sy_b2 = Character(_('青木翔子（梦）'), image='yume_sy_b2')
define yume_sf_b2 = Character(_('青木翔子（梦）'), image='yume_sf_b2')


define composite yume_sy_b1:
    path pick_actor_path("role/梦/睡衣", "role/梦/half/睡衣")
    transform:
        pos (0.4, 0.97)
        anchor (0.4, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(186, 267)

define composite yume_sy_b2:
    path pick_actor_path("role/梦/睡衣", "role/梦/half/睡衣")
    transform:
        pos (0.5, 0.97)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(283, 218)

define composite yume_sf_b1:
    path pick_actor_path("role/梦/私服", "role/梦/half/私服")
    transform:
        pos (0.5, 0.97)
        anchor (0.5, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(363, 267)

define composite yume_sf_b2:
    path pick_actor_path("role/梦/私服", "role/梦/half/私服")
    transform:
        pos (0.6, 0.97)
        anchor (0.6, 2478./3424.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(460, 217)

init python:
    side_actor_ypos['yume'] = 0.475
    investigation.call_actor_ypos['yume_sy_b2'] = 0.115
    investigation.call_actor_ypos['yume_sf_b2'] = 0.115
