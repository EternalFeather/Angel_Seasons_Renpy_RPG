
transform upd_bgscale:
    size (config.screen_width, config.screen_height)


init -1500 python in fake_updater:
    import threading
    import time

    class Fake_Updater(threading.Thread):
        # self.message is set to the error message.
        ERROR = "ERROR"

        # Checking to see if an update is necessary.
        CHECKING = "CHECKING"

        # We are up to date. The update process has ended.
        # Calling proceed will return to the main menu.
        UPDATE_NOT_AVAILABLE = "UPDATE NOT AVAILABLE"

        # An update is available.
        # The interface should ask the user if he wants to upgrade, and call .proceed()
        # if he wants to continue.
        UPDATE_AVAILABLE = "UPDATE AVAILABLE"

        # Preparing to update by packing the current files into a .update file.
        # self.progress is updated during this process.
        PREPARING = "PREPARING"

        # Done. The update completed successfully.
        # Calling .proceed() on the updater will trigger a game restart.
        DONE = "DONE"

        # The update was cancelled.
        CANCELLED = "CANCELLED"

        def __init__(self):

            threading.Thread.__init__(self)

            self.state = Fake_Updater.UPDATE_AVAILABLE

            self.message = None

            self.progress = None

            self.can_proceed = True

            self.can_cancel = True

            self.proceeded = False

            self.cancelled = False

            self.condition = threading.Condition()

        def run(self):
            if self.state == self.ERROR:
                renpy.full_restart()

            elif self.state == self.CANCELLED:
                renpy.full_restart()

            elif self.state == self.DONE:
                renpy.quit(relaunch=True)

            elif self.state == self.UPDATE_AVAILABLE:
                with self.condition:
                    self.proceeded = True
                    self.condition.notify_all()

            renpy.invoke_in_thread(self.proceed)
            time.sleep(.1)

            return

        def proceed(self):
            def simulate_progress():
                for i in range(0, 30):
                    self.progress = i / 30.0
                    time.sleep(.1)

                    if self.cancelled:
                        self.cancel()
            
            self.can_proceed = False
            self.progress = 0.0
            self.state = self.PREPARING
            renpy.restart_interaction()

            simulate_progress()

            self.state = self.DONE
            renpy.restart_interaction()

            return

        def cancel(self):
            if not self.can_cancel:
                return

            renpy.quit(relaunch=False)


    def update():
        global installed_packages_cache
        installed_packages_cache = None

        u = Fake_Updater()
        ui.timer(.1, repeat=True, action=renpy.restart_interaction)
        renpy.call_screen("updater", u=u)


screen updater:
    add At(Movie(size=(1920, 1080)), upd_bgscale)
    on "show" action Play("movie", "updater/update_ms2.mp4", loop = 1)
    on "hide" action [Stop("movie"), Hide("movie")]
    on "replaced" action [Stop("movie"), Hide("movie")]

    frame:
        style_group "updater"

        background At("updater/upd_overlay.png", upd_bgscale)

        xalign 0.5

        ypos 0
        xfill True

        has vbox

        if u.progress is not None:
            bar value u.progress range 1.0 style "updater_bar"

        null height 10

        if u.state == u.CHECKING:
            text "确认更新情况。。。"
        elif u.state == u.PREPARING:
            text "正在更新。。。"
        elif u.state == u.DONE:
            text "更新已完成"
        elif u.state == u.CANCELLED:
            text "更新已取消，正在重启。。。"

        if u.message is not None:
            null height 10
            text "[u.message!q]"

        if u.can_proceed or u.can_cancel:
            null height 10

        if u.can_proceed:
            textbutton "点击检查更新" action u.run xfill True
        elif u.state == u.DONE:
            add "click_continue"
            textbutton "进入游戏" action Return()
#            if u.can_cancel:
#                textbutton "退出游戏" action u.cancel xfill True


style updater_text:
    font "9i/fonts/浪漫雅圆.ttf"
    size 18
    color "#ffffff"
    text_align 0.5
    xalign 0.5
    xmaximum 720

style updater_button:
    background None
    xalign 0.5
    xmaximum 270

style updater_button_text take update_text:
    idle_color "#9cdce3"
    hover_color "#ffffff"
    selected_color "#ffffff"

style updater_bar:
    left_bar Frame("updater/upd_bar_left.png", left = 1, top = 0)
    thumb None
    bar_resizing True
    ymaximum 4

style updater_vbox:
    xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
