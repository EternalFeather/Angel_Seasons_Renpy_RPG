define tyt = Character(_('藤原瞳'), image="tyt")
define tyt_wnf_b1 = Character(_('藤原瞳'), image="tyt_wnf_b1")


define composite tyt_wnf_b1:
    path pick_actor_path("role/藤原瞳/巫女服", "role/藤原瞳/half/巫女服")
    transform:
        pos (0.55, 0.98)
        anchor (0.55, 2478./3424.)
        zoom scale_sprite_zoom(0.275)
    position body
    position fa:
        pos scale_sprite_offset(431, 387)

init python:
    side_actor_ypos['tyt'] = 0.475
    investigation.call_actor_xpos['tyt_wnf_b1'] = 0.53
    investigation.call_actor_ypos['tyt_wnf_b1'] = 0.115

