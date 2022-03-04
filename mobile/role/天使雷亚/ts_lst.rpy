define lst = Character(_('莉斯特·F·艾斯特雷亚'), image="ts_lst")
define ts_lst_ssz_b2 = Character(_('莉斯特·F·艾斯特雷亚'), image="ts_lst_ssz_b2")


define composite ts_lst_ssz_b1:
    path pick_actor_path("role/天使雷亚/死神装", "role/天使雷亚/half/死神装")
    transform:
        pos (0.45, 1.08)
        anchor (0.45, 2478./2924.)
        zoom scale_sprite_zoom(0.305)
    position body
    position fa:
        pos scale_sprite_offset(485, 260)

define composite ts_lst_ssz_b2:
    path pick_actor_path("role/天使雷亚/死神装", "role/天使雷亚/half/死神装")
    transform:
        pos (0.38, 1.08)
        anchor (0.38, 2478./2924.)
        zoom scale_sprite_zoom(0.305)
    position body
    position fa:
        pos scale_sprite_offset(472, 226)

define composite ts_lst_ssz_b3:
    path pick_actor_path("role/天使雷亚/死神装", "role/天使雷亚/half/死神装")
    transform:
        pos (0.6, 1.04)
        anchor (0.6, 2478./2924.)
        zoom scale_sprite_zoom(0.285)
    position body
    position fa:
        pos scale_sprite_offset(1212, 215)

define composite ts_lst_ssz_b1_d:
    path pick_actor_path("role/天使雷亚/死神镰刀", "role/天使雷亚/half/死神镰刀")
    transform:
        pos (0.4, 1.08)
        anchor (0.4, 2478./2924.)
        zoom scale_sprite_zoom(0.305)
    position body
    position fa:
        pos scale_sprite_offset(1065, 260)

define composite ts_lst_ssz_b2_d:
    path pick_actor_path("role/天使雷亚/死神镰刀", "role/天使雷亚/half/死神镰刀")
    transform:
        pos (0.5, 1.005)
        anchor (0.5, 2478./3224.)
        zoom scale_sprite_zoom(0.305)
    position body
    position fa:
        pos scale_sprite_offset(1021, 488)

init python:
    side_actor_ypos['ts_lst'] = 0.575
    investigation.call_actor_ypos['ts_lst_ssz_b2'] = 0.115


transform basicfade_lst_b1_d_flow:
    easein 0.25 ypos 1.08
    easein 0.25 ypos 0.95
