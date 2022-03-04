define xfe = Character(_('希菲尔·M·克里斯蒂恩'), image="ts_xfe")
define ts_xfe_yjz_b2 = Character(_('希菲尔·M·克里斯蒂恩'), image="ts_xfe_yjz_b2")


define composite ts_xfe_yjz_b1:
    path pick_actor_path("role/天使希菲尔/妖精装", "role/天使希菲尔/half/妖精装")
    transform:
        pos (0.43, 1.02)
        anchor (0.43, 2478./2924.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(384, 365)

define composite ts_xfe_yjz_b2:
    path pick_actor_path("role/天使希菲尔/妖精装", "role/天使希菲尔/half/妖精装")
    transform:
        pos (0.5, 1.0)
        anchor (0.5, 2478./3024.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(747, 355)

define composite ts_xfe_yjz_b3:
    path pick_actor_path("role/天使希菲尔/妖精装", "role/天使希菲尔/half/妖精装")
    transform:
        pos (0.55, 1.0)
        anchor (0.55, 2478./3024.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(790, 329)

init python:
    side_actor_ypos['ts_xfe'] = 0.475
    investigation.call_actor_ypos['ts_xfe_yjz_b2'] = 0.115

