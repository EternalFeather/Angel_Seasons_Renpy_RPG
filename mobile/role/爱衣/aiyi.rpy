define aiyi = Character(_('日向爱衣'), image="aiyi")
define aiyi_dzf_b1 = Character(_('日向爱衣'), image="aiyi_dzf_b1")


define composite aiyi_dzf_b1:
    path pick_actor_path("role/爱衣/冬制服", "role/爱衣/half/冬制服")
    transform:
        pos (0.55, 1.0)
        anchor (0.55, 2478./2824.)
        zoom scale_sprite_zoom(0.245)
    position body
    position fa:
        pos scale_sprite_offset(423, 262)

define composite aiyi_dzf_b1_rune:
    path pick_actor_path("role/爱衣/冬制服", "role/爱衣/half/冬制服")
    transform:
        pos (0.55, 1.0)
        anchor (0.55, 2478./2974.)
        zoom scale_sprite_zoom(0.245)
    position rune
    position body:
        pos scale_sprite_offset(180, 185)
    position fa:
        pos scale_sprite_offset(602, 451)

define composite aiyi_sy_b1:
    path pick_actor_path("role/爱衣/睡衣", "role/爱衣/half/睡衣")
    transform:
        pos (0.55, 1.0)
        anchor (0.55, 2478./2824.)
        zoom scale_sprite_zoom(0.245)
    position body
    position fa:
        pos scale_sprite_offset(424, 261)

define composite aiyi_sy_b2:
    path pick_actor_path("role/爱衣/睡衣", "role/爱衣/half/睡衣")
    transform:
        pos (0.55, 1.0)
        anchor (0.55, 2478./2824.)
        zoom scale_sprite_zoom(0.245)
    position body
    position fa:
        pos scale_sprite_offset(424, 264)

init python:
    side_actor_ypos['aiyi'] = 0.475
    investigation.call_actor_ypos['aiyi_dzf_b1'] = 0.115

