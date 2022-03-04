python early:
    from __future__ import unicode_literals

    config.window_title = '(Fault | Favorite | Yozi) - 天使的季节v3.12.127'
    config.name = '(Fault | Favorite | Yozi) - 天使的季节v3.12.127'
    config.version = '3.12.127'
    config.window_icon = 'icon.png'

    config.save_directory = 'project_written_fstp'
    config.mouse = {"default" : [ ( "cursor.png", 0, 0) ],}

    config.screen_width = 1920
    config.screen_height = 1080
    config.cache_surfaces = False
    config.default_fullscreen = False
    config.use_cpickle = False


init -1 python hide:
    persistent.skip_delay = 25
    persistent.mouse_hide_time = 30
    persistent.window_opacity = 0.8
    persistent.gl_resize = True
    persistent.battlespeed = 1.0
    persistent.inserts = True
    persistent.in_battle = False
    persistent.while_inserts = "slow"
    persistent.turnback = False
    persistent.lowres = False
    persistent.xp = 5.0
    # 道具掉落率
    persistent.drop_rate = 3
    # 开发者通道
    persistent.development = True
    persistent.readback = False
    persistent.game_clear = False
    # 概率表（道具、装备、角色）
    persistent.ratio_table = {
        "items": 0.3,
        "equips": 0.6,
        "role": 0.1
    }
    persistent._set_default_preferences = True

    renpy.music.register_channel("battle_music", mixer="sfx", loop=False, file_prefix="9i/interface/battle/battle_music/", file_suffix=".mp3")
    renpy.music.register_channel("sfx", mixer="sfx", loop=False, file_prefix="9i/interface/battle/sfx/", file_suffix=".mp3")

    config.default_music_volume = 0.8
    config.default_sfx_volume = 0.8
    config.default_voice_volume = 0.8

    config.window_auto_hide = ['scene', 'call screen', 'show screen']


init -10 python:
    block = renpy.block_rollback

    def cache_image(folder):
        for file in renpy.list_files():
            if file.startswith('{}/'.format(folder)):
                if file.endswith('.png'):
                    renpy.cache_pin(file)

    def get_icons(param):
        if param <= 0:
            return("00%")
        elif param == 1:
            return("25%")
        elif param == 2:
            return("50%")
        elif param == 3:
            return("75%")
        else:
            return("100%")

    def get_icons_v2(param):
        if not param or param == 0.0:
            return("00%")
        elif 0 < param < 0.1:
            return("0%d%%" % round(param * 100))
        elif -0.1 < param < 0:
            return("-0%d%%" % -round(param * 100))
        else:
            return("%d%%" % round(param * 100))

    def target_change(enemy, reverse=False):
        if not reverse:
            next = (enemy.index(local_config.partytarget) + 1)
            if next >= len(enemy) or next > 2:
                next = 0
            while True:
                if enemy[next].hp > 0:
                    local_config.partytarget = enemy[next]
                    return
                else:
                    next += 1
                    if next >= len(enemy):
                        next = 0
        else:
            next = (enemy.index(local_config.partytarget) - 1)
            if next < 0:
                next = min(len(enemy)-1, 2)
            while True:
                if enemy[next].hp > 0:
                    local_config.partytarget = enemy[next]
                    return
                else:
                    next -= 1
                    if next < 0:
                        next = min(len(enemy)-1, 2)

    def store_yvalue(y):
        global yvalue
        yvalue = int(y)

    def _shake_function(trans, st, at, dt=0.5, dist=128):
        if st <= dt:
            trans.xoffset = int((dt-st) * dist * (0.5 - renpy.random.random()) * 2)
            trans.yoffset = int((dt-st) * dist * (0.5 - renpy.random.random()) * 2)
            return 0.01
        else:
            return None

    def detective_dragged(drags, drop):
        if drop and drop.drag_name == "Pooler":
            store.detect_drop = True
            store.drag_name = drags[0].drag_name
        return True


init -999 python:
    import os
    import math
    import pygame
    from copy import copy
    from operator import attrgetter

    os.environ['SDL_VIDEO_CENTERED'] = '1'


init python:
    register_actor_image("9i/interface/battle/settings/actors.tsv")
    register_outfit_image(False)
    item_list = read_item("9i/interface/battle/settings/items.tsv")
    skill_list = read_skill("9i/interface/battle/settings/skills.tsv")
    actor_list = read_actor("9i/interface/battle/settings/actors.tsv")
    buff_list = read_buff("9i/interface/battle/settings/buff.tsv")
    outfit_list = read_outfit("9i/interface/battle/settings/outfits.tsv")
    cache_image("9i/interface/battle/system")


define config.layers = [
    'bg',
    'bg2',
    'bg_f',
    'bg_f2',
    'master',
    'b1',
    'b2',
    'm1',
    'm2',
    'f1',
    'f2',
    'enemy_ef',
    'fg',
    'fg_f',
    'tutorial',
    'texture',
    'transient',
    'healing',
    'damage',
    'damage_element',
    'buff_element',
    'screens',
    'ani'
    'overlay',
]

define config.top_layers = ['key']
default _3d_layers = {
    'b1': 2200,
    'b2': 2200,
    'm1': 1849,
    'm2': 1849,
    'f1': 1280,
    'f2': 1280
}
define _viewers.fps_keymap = True
define _viewers.default_rot = True
define _viewers.default_warper = 'power_in_time_warp_real'
default f_teleporter = 12
image halfblack = "#000c"

init -999 python:
    gui.init(width=1920, height=1080)

define annotator = Character(None, kind=adv, show_bg=Frame("9i/interface/battle/system/textbox2.png", 18, 18))
define stranger = Character(_('？？？'))
define me01 = Character(_('神野凉'))
define mel = Character(_('梅尔·M·科莉娅'))
define fl = Character(_('弗兰·A·克里伍德'))

image bottom_black = "9i/interface/battle/system/bottom_bar.png"

## This section contains information about how to build your project into
## distribution files.
init python:
    nobody = Actor("nobody", "Nobody")
    mp_log = MultiPersistent("angel.renpy.org")

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Angel_Seasons"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Angel_Seasons"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = True

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('errors.txt', None)
    build.classify('log.txt', None)
    build.classify('traceback.txt', None)
    build.classify('请读我.txt', None)
    
    ## 游戏打包
    # 语音(voice/ogg)
    build.archive('voice', 'all')
    build.classify('game/voice/**.ogg', 'voice')

    # 视频(video/webm)
    build.archive('video', 'all')
    build.classify('game/video/**.webm', 'video')

    # 更新相关(updater/png&webm)
    build.archive('updater', 'all')
    build.classify('game/updater/upd_bar_left.png', 'updater')
    build.classify('game/updater/upd_overlay.png', 'updater')
    build.classify('game/updater/update_ms2.webm', 'updater')
    build.classify('game/updater/updater.rpyc', 'updater')

    # 教学图片(tutorial/png&jpg)
    build.archive('tutorial', 'all')
    build.classify('game/tutorial/**.jpg', 'tutorial')
    build.classify('game/tutorial/**.png', 'tutorial')
    build.classify('game/tutorial/tutorial.rpyc', 'tutorial')

    # 转场特效(transform/png)
    build.archive('transform', 'all')
    build.classify('game/transform/**.png', 'transform')
    build.classify('game/transform/trans.rpyc', 'transform')

    # 界面(title/png&txt)
    build.archive('title', 'all')
    build.classify('game/title/system/start/**.png', 'title')
    build.classify('game/title/tlcredits/**.png', 'title')
    build.classify('game/title/system/**.png', 'title')
    build.classify('game/title/system/**.txt', 'title')
    build.classify('game/title/system/second_menu.rpyc', 'title')
    build.classify('game/title/**.rpyc', 'title')
    build.classify('game/title/**.txt', 'title')
    build.classify('game/title/**.png', 'title')

    # 声音(sound/ogg&wav)
    build.archive('sound', 'all')
    build.classify('game/sound/first_version/**.wav', 'sound')
    build.classify('game/sound/first_version/**.ogg', 'sound')
    build.classify('game/sound/second_version/**.wav', 'sound')
    build.classify('game/sound/system/**.ogg', 'sound')
    build.classify('game/sound/system/**.wav', 'sound')
    build.classify('game/sound/**.wav', 'sound')
    build.classify('game/sound/**.ogg', 'sound')
    build.classify('game/sound/sound.rpyc', 'sound')

    # 角色(role/py&json&rpyc&csv&png)
    build.archive('role', 'all')
    build.classify('game/role/**.png', 'role')
    build.classify('game/role/**.csv', 'role')
    build.classify('game/role/**.rpyc', 'role')
    build.classify('game/role/auto_deal.py', 'role')
    build.classify('game/role/name_deal.py', 'role')
    build.classify('game/role/zip_images.py', 'role')
    build.classify('game/role/name_maps.json', 'role')

    # 背景音乐(music/ogg&mp3&wav&)
    build.archive('music', 'all')
    build.classify('game/music/first_version/**.ogg', 'music')
    build.classify('game/music/second_version/**.ogg', 'music')
    build.classify('game/music/**.ogg', 'music')
    build.classify('game/music/**.mp3', 'music')
    build.classify('game/music/**.wav', 'music')
    build.classify('game/music/music.rpyc', 'music')

    # 道具图(items/png)
    build.archive('items', 'all')
    build.classify('game/items/**.png', 'items')
    build.classify('game/items/**.rpyc', 'items')

    # 场景图(images/py&jpg&png&rpyc)
    build.archive('images', 'all')
    build.classify('game/images/zip_images.py', 'items')
    build.classify('game/images/**.jpg', 'items')
    build.classify('game/images/**.rpyc', 'items')
    build.classify('game/images/**.png', 'items')

    # 战斗相关(battle_shell/rpyc | 9i/interface/battle/rpyc&txt&py&mp3&tsv&ogg&jpg)
    build.archive('battle', 'all')
    build.classify('game/battle_shell/**.rpyc', 'battle')
    build.classify('game/9i/interface/battle/**.rpyc', 'battle')
    build.classify('game/9i/interface/battle/**.txt', 'battle')
    build.classify('game/9i/interface/battle/atk_calculate.py', 'battle')
    build.classify('game/9i/interface/battle/**.mp3', 'battle')
    build.classify('game/9i/interface/battle/**.tsv', 'battle')
    build.classify('game/9i/interface/battle/**.ogg', 'battle')
    build.classify('game/9i/interface/battle/**.jpg', 'battle')
    build.classify('game/9i/interface/battle/**.png', 'battle')

    # 动画(anime/png)
    build.archive('anime', 'all')
    build.classify('game/anime/**.png', 'anime')
    build.classify('game/anime/ani.rpyc', 'anime')

    # 系统相关(
    # game/png
    # 9i/rpyc
    # 9i/interface/ogg&wav&webm&png&mp3 
    # 9i/interface/settings/png&jpg
    # 9i/interface/saveload/png&jpg&webm
    # 9i/interface/quickmenu/png
    # 9i/interface/overworld/png
    # 9i/interface/mainmenu/png
    # 9i/interface/investigation/png
    # 9i/interface/gallery/png
    # 9i/interface/encyclopedia/png&webm
    # 9i/interface/effects/png
    # 9i/interface/confirm/png
    # 9i/fonts/otf&ttf
    # 9i/dialogue/png
    # )

    build.archive('system_files', 'all')
    build.classify('game/9i/interface/settings/**.jpg', 'system_files')
    build.classify('game/9i/interface/settings/**.png', 'system_files')
    build.classify('game/9i/interface/settings/**.rpyc', 'system_files')
    build.classify('game/9i/interface/saveload/**.webm', 'system_files')
    build.classify('game/9i/interface/saveload/**.png', 'system_files')
    build.classify('game/9i/interface/saveload/**.jpg', 'system_files')
    build.classify('game/9i/interface/saveload/**.rpyc', 'system_files')
    build.classify('game/9i/interface/quickmenu/**.png', 'system_files')
    build.classify('game/9i/interface/quickmenu/**.rpyc', 'system_files')
    build.classify('game/9i/interface/overworld/**.png', 'system_files')
    build.classify('game/9i/interface/overworld/**.rpyc', 'system_files')
    build.classify('game/9i/interface/mainmenu/**.png', 'system_files')
    build.classify('game/9i/interface/mainmenu/**.rpyc', 'system_files')
    build.classify('game/9i/interface/investigation/**.rpyc', 'system_files')
    build.classify('game/9i/interface/investigation/**.png', 'system_files')
    build.classify('game/9i/interface/gallery/**.png', 'system_files')
    build.classify('game/9i/interface/gallery/**.rpyc', 'system_files')
    build.classify('game/9i/interface/encyclopedia/bg.webm', 'system_files')
    build.classify('game/9i/interface/encyclopedia/**.png', 'system_files')
    build.classify('game/9i/interface/encyclopedia/encyclopedia1.rpyc', 'system_files')
    build.classify('game/9i/interface/encyclopedia/encyclopedia_main.rpyc', 'system_files')
    build.classify('game/9i/interface/effects/**.png', 'system_files')
    build.classify('game/9i/interface/effects/effects.rpyc', 'system_files')
    build.classify('game/9i/interface/confirm/**.png', 'system_files')
    build.classify('game/9i/interface/**.ogg', 'system_files')
    build.classify('game/9i/interface/**.png', 'system_files')
    build.classify('game/9i/interface/**.mp3', 'system_files')
    build.classify('game/9i/interface/**.wav', 'system_files')
    build.classify('game/9i/interface/**.webm', 'system_files')
    build.classify('game/9i/dialogue/**.png', 'system_files')
    build.classify('game/9i/dialogue/screens.rpyc', 'system_files')
    build.classify('game/9i/fonts/**.otf', 'system_files')
    build.classify('game/9i/fonts/**.ttf', 'system_files')
    build.classify('game/9i/**.rpyc', 'system_files')
    build.classify('game/presplash.png', 'system_files')
    build.classify('game/camera.png', 'system_files')
    build.classify('game/cursor.png', 'system_files')
    build.classify('game/icon.png', 'system_files')
    build.classify('game/itemsign.png', 'system_files')

    # 介绍(9i/splash/png&webm)
    build.archive('splash', 'all')
    build.classify('game/9i/splash/**.png', 'splash')
    build.classify('game/9i/splash/01splash.rpyc', 'splash')
    build.classify('game/9i/splash/sp_logo_reveal.webm', 'splash')

    # room(9i/interface/room/rpyc&png&jpg&ogg)
    build.archive('room', 'all')
    build.classify('game/9i/interface/room/**.png', 'room')
    build.classify('game/9i/interface/room/**.ogg', 'room')
    build.classify('game/9i/interface/room/**.jpg', 'room')
    build.classify('game/9i/interface/room/**.rpyc', 'room')

    # 剧情脚本
    build.archive('story_scripts', 'all')
    build.classify('game/**.rpyc', "story_scripts")

    # ---- Old version ----
    # build.archive("scripts", "all")
    # build.archive("images", "all")
    # build.archive("uitool", "all")
    # build.archive("music", "all")
    # build.archive("video", "all")

    # build.classify('game/**.rpy', "scripts")
    # build.classify('game/**.rpyc', "scripts")

    

    # build.classify('game/**.png', 'images')
    # build.classify('game/**.jpg', 'images')
    # build.classify('game/**.mp3', 'music')
    # build.classify('game/**.ogg', 'music')
    # build.classify('game/**.wav', 'music')
    # build.classify('game/**.ttf', 'uitool')
    # build.classify('game/**.ttc', 'uitool')
    # build.classify('game/**.otf', 'uitool')
    # build.classify('game/**.tsv', 'uitool')
    # build.classify('game/**.webm', 'video')

    ## To archive files, classify them as 'archive'.

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    