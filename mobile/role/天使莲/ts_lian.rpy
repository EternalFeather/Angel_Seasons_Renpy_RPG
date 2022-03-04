define ts_lian = Character(_('克丽丝·X·米尔圣玛莲'), image="ts_lian")
define cyl = Character(_('苍衣莲'), image="cyl")
define ts_lian_ssz_b1 = Character(_('克丽丝·X·米尔圣玛莲'), image="ts_lian_ssz_b1")


define composite ts_lian_ssz_b1:
    path pick_actor_path("role/天使莲/死神装", "role/天使莲/half/死神装")
    transform:
        pos (0.55, 1.02)
        anchor (0.55, 2478./2824.)
        zoom scale_sprite_zoom(0.270)
    position body
    position fa:
        pos scale_sprite_offset(558, 262)

init python:
    side_actor_ypos['ts_lian'] = 0.475
    investigation.call_actor_ypos['ts_lian_ssz_b1'] = 0.115

