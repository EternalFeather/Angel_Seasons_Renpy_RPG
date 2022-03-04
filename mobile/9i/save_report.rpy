init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def invoke_save_report():
        
        
        take_report_screenshot()
        renpy.show_screen('save_report')
        renpy.restart_interaction()

    renpy.config.keymap['save_report'] = 'alt_K_F1'
    renpy.config.underlay[0].keymap['save_report'] = invoke_save_report

screen save_report():
    modal True
    zorder +9001
    frame style_prefix "saverep" at saverep_inter:
        has vbox
        label _("Save a bug report here?")
        hbox:
            textbutton _("Save bug report"):
                action [SaveReport(), Hide("save_report")]
            textbutton _("Cancel"):
                action Hide("save_report")
                keysym "game_menu"
init:
    transform saverep_inter:
        on show:
            subpixel True
            alpha 0
            yzoom 0.5
            parallel:
                linear 0.2 alpha 1
            parallel:
                easeout 0.1 yzoom 1.0
        on hide:
            linear 0.1 alpha 0

    style saverep_frame is default:
        xcenter 0.5
        ycenter 0.5
        xfill True
        ypadding scale(60)
        background Solid("#1717177f")
    style saverep_vbox is vbox xcenter 0.5 spacing scale(30)
    style saverep_text is text color "#fff"
    style saverep_label is default xcenter 0.5
    style saverep_label_text is saverep_text size scale(30)
    style saverep_hbox is hbox xcenter 0.5 spacing scale(15)
    style saverep_button is button size_group "saverep"
    style saverep_button_text is takerep_text xcenter 0.5

screen _exception_actions(traceback_fn, tt, *args):
    textbutton _("Save bug report"):
        action SaveReport(take_traceback=bool(traceback_fn))
        hovered tt.action(_("Saves the game along with troubleshooting info. Submitting these helps us fix bugs."))

init python:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    class SaveReport(renpy.ui.Action):
        """Saves a bug report and reveals it in the file explorer.
        """
        def __init__(self, take_traceback=False):
            self.take_traceback = take_traceback
        
        def __call__(self):
            import datetime
            import os
            
            outname = '{game} v{version} report on {datetime}.save'.format(
                game='StP',
                version=renpy.config.version,
                datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H%M%Z'))
            
            savepath = build_report(
                take_screenshot=False,
                take_traceback=self.take_traceback)
            for out_try in self.iter_filenames(outname):
                outpath = os.path.join(os.path.dirname(savepath), outname)
                if os.path.exists(outpath): continue
                os.rename(savepath, outpath)
                break
            
            renpy.run(renpy.store.Reveal(outpath))
        
        @staticmethod
        def iter_filenames(name):
            import itertools
            import os
            pre, ext = os.path.splitext(name)
            yield (0, name)
            for i in itertools.count(1):
                yield (i, '{pre} ({i}){ext}'.format(pre=pre, i=i, ext=ext))

    def take_report_screenshot():
        """Takes a new savegame screenshot at the virtual resolution.
        """
        import pygame
        
        logical_size = (renpy.config.screen_width, renpy.config.screen_height)
        
        drawable_size = pygame.display.get_drawable_size()
        renpy.display.interface.lose_screenshot()
        renpy.display.interface.take_screenshot(scale=logical_size)

    def build_report(take_screenshot=True, take_traceback=False):
        """Saves a report savegame. Returns the path to the file.
        """
        import json
        import os
        from zipfile import ZipFile
        
        if take_screenshot:
            take_report_screenshot()
        
        renpy.loadsave.save('report', extra_info=save_name)
        savepath = renpy.loadsave.location.newest('report').filename('report')
        
        
        
        renpy.display.interface.lose_screenshot()
        
        with ZipFile(savepath, mode='a') as savefile:
            savefile.write(
                filename=os.path.join(renpy.config.logdir, 'log.txt'),
                arcname='log.txt')
            if take_traceback:
                savefile.write(
                    filename=os.path.join(renpy.config.logdir, 'traceback.txt'),
                    arcname='traceback.txt')
            
            def get_script_location():
                c = renpy.game.context(0)
                c_stack = c.get_return_stack()
                id_ = c_stack[-1] if c_stack else c.current
                node = renpy.game.script.namemap.get(id_)
                return (node.filename, node.linenumber) if node else None
            
            props = {
                'game_version': renpy.config.version,
                'renpy_version': renpy.version_string,
                'renpy_version_tuple': renpy.version_tuple,
                'script_location': get_script_location(),
                'bookmark': getattr(renpy.store, '_last_bookmark', None)
            }
            savefile.writestr('reportdata', json.dumps(props, ensure_ascii=False))
        
        return savepath
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
