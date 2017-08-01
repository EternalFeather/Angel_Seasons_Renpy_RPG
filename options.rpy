
init -1 python hide:
    
    config.language = "english"
    config.developer = True

    config.screen_width = 1280
    config.screen_height = 720

    config.window_title = u"The Seasons Of Angel"

    config.name = "TheSeasonsOfAngel"
    config.version = u"v5.12"

    layout.button_menu()

    config.layers = [ 'master', 'texture', 'transient', 'screens', 'overlay' ]

    config.window_icon = "images/system/icon.png"
    config.mouse = {"default" : [ ( "ui/cursor.png", 0, 0) ],}

    config.quit_action = Quit(confirm=True)

    config.image_cache_size = 80


    theme.roundrect(
        
        widget = "#FFFFFF",

        
        widget_hover = "#898989",

        
        widget_text = "#ffffff",

        
        
        widget_selected = "#737373",

        
        disabled = "#F0F2F2",

        
        disabled_text = "#FBFBFB",

        
        label = "#D9D9D9",

        
        frame = "#ffffff",

        

        rounded_window = False,

        )


    style.window.background = "ui/adv_txtbox.png"

    style.window.left_padding = 0.2
    style.window.right_padding = 0.2
    style.window.top_padding = 0.77
    style.window.bottom_padding = 0.01

    

    style.window.yminimum = 720


    config.has_sound = True



    config.has_music = True



    config.has_voice = False


    #config.main_menu_music = "bgm/begin.ogg"
    if persistent.gamecomplete == True and persistent.fanwai == False:
        
        config.main_menu_music = "bgm/end.ogg"

    elif persistent.gamecomplete == False and persistent.fanwai == False:

        config.main_menu_music = "bgm/begin.ogg"

    elif persistent.gamecomplete == True and persistent.fanwai == True:

        config.main_menu_music = "bgm/op.ogg"



    config.help = "README.html"



    config.enter_transition = dissolve


    config.exit_transition = dissolve


    config.intra_transition = dissolve


    config.main_game_transition = dissolve


    config.game_main_transition = dissolve


    config.end_splash_transition = dissolve


    config.end_game_transition = dissolve


    config.after_load_transition = dissolve


    config.window_show_transition = dissolve


    config.window_hide_transition = dissolve





python early:

    config.save_directory = "TheSeasonsOfAngel-1446282186"

init -1 python hide:
    

    config.default_fullscreen = False

   
    config.default_text_cps = 50

   

    config.save_physical_size = False


    style.default.drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]


    style.frame.background = None
    style.frame.ypadding = 0
    style.frame.xpadding = 0


    style.nvl_window.background = "ui/nvl_txtbox.png"
    style.say_window.background = "ui/adv_txtbox.png"
    style.nvl_window.xmaximum = 800
    style.nvl_vbox.box_spacing = 25
    style.default.line_leading = 8
    style.default.line_spacing = 4
    style.default.size = 21

    style.alertwindow = Style(style.default)
    style.alertwindow.background = "ui/yesno_box.png"
    style.alertwindow.xmaximum = 650
    style.alertwindow.ymaximum = 500
    style.alertwindow.xpadding = 0
    style.alertwindow.ypadding = 0

    style.yesno_prompt.xalign = 0.5
    style.yesno_prompt.yalign = 0.38
    style.yesno_prompt_text.color = "#FFFFFF"
    style.yesno_prompt_text.outlines = [(2,"#addcec")]
    style.yesno_prompt_text.size = 19
    style.yesno_prompt_text.drop_shadow = None

    style.yesno_prompt_button = Style(style.default)
    style.yesno_prompt_button.xalign = 0.5

    style.menubutton = Style(style.default)
    style.menubutton.xalign = 0.5
    style.menubutton_text.color = "#FFFFFF"
    style.menubutton_text.size = 36
    style.menubutton_text.hover_color = "#0066FF"
    style.menubutton_text.selected_color = "#0066FF"

    config.thumbnail_width = 238
    config.thumbnail_height = 134

    style.ruby_style = Style(style.default)
    style.ruby_style.size = 5
    style.ruby_style.yoffset = -25

    style.default.ruby_style = style.ruby_style


    style.say_label.outlines = [(2, "#000000")]

    config.keymap['dismiss'].append('mousedown_5')
    
init python:
    @renpy.pure
    class Language(Action, DictEquality):
        """
        :doc: language_action

        Changes the language of the game to `language`.

        `language`
            A string giving the language to translate to, or None to use
            the default language of the game script.
        """
        
        alt = "Language [text]"
        
        def __init__(self, language):
            self.language = language
        
        def __call__(self):
            if not multi_language:
                return
            renpy.change_language(self.language)
        
        def get_selected(self):
            return _preferences.language == self.language
        
        def get_sensitive(self):
            if self.language is None:
                return True
            
            return self.language in renpy.known_languages()

init python:




    build.directory_name = "TheSeasonsOfAngel"




    build.executable_name = "TheSeasonsOfAngel"



    build.include_update = False

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/log.txt', None)
    build.classify('**.rpy', None)
    build.classify('dialogue.txt', None)
    build.classify('errors.txt', None)
    build.classify('log.txt', None)
    build.classify('traceback.txt', None)

    build.classify('game/developer.rpy', None)
    build.classify('game/developer.rpyc', None)
    build.classify('game/presplash.png', 'update')
    build.classify('game/images/system/icon.png', 'update')



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.ttc', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/**.tsv', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.mkv', 'archive')
    build.classify('game/**.webm', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')