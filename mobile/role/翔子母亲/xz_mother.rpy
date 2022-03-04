define xz_mother = Character(_('翔子母亲'), image="xz_mother")
define xz_mother_xsf_b1 = Character(_('翔子母亲'), image="xz_mother_xsf_b1")


define composite xz_mother_xsf_b1:
    path pick_actor_path("role/翔子母亲/夏私服", "role/翔子母亲/half/夏私服")
    transform:
        pos (0.5, 0.97)
        anchor (0.5, 2478./3444.)
        zoom scale_sprite_zoom(0.305)
    position body
    position fa:
        pos scale_sprite_offset(383, 228)

init python:
    side_actor_ypos['xz_mother'] = 0.475
    investigation.call_actor_ypos['xz_mother_xsf_b1'] = 0.115
