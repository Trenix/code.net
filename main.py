from kivymd.app import MDApp
# from kivy.core.window import Window
from kivymd.icon_definitions import md_icons
from displays.playeramount import PlayerWindow
from displays.revealdirections import *
from displays.welcome import WelcomeWindow
from kivymd.uix.screen import MDScreen
from displays.loadsetup import LoadingScreen
from displays.colorselect import ColorSelectScreen
from displays.endgame import EndGame
from systems.screenmanager import WindowManager
from systems.generatelog import createlog
from systems.generatelog import createhackeramt
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from displays.dialogcode import IdentityDialog
from displays.dialogcode import ConfirmDialog
from displays.dialogcode import ActionDialog
from displays.information import MainInfo
from displays.action import ActionScreen
from displays.playerlog import PlayerLogScreen
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
import random
import globals

# KIVY_DPI = 320
# KIVY_METRICS_DENSITY = 2
#
# Window.size = (720, 1280)

class Tab(MDFloatLayout, MDTabsBase):
    pass

# Add toggle to iconbuttons
class MDFillRoundFlatIconButtonToggle(MDFillRoundFlatIconButton, MDToggleButton):
    pass

class MainWindow(MDScreen):
    from systems.openinformation import openinfo

    def resettimer(self):

        self.ids.mainscreenmanager.get_screen("timescreen").ids.timer.text = "00:00"
        globals.timer.cancel()

        if self.ids.currentround.text == f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]":
            self.ids.roundregulator.icon = "square-rounded-outline"
            self.ids.roundregulator.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]

        else:
            self.ids.roundregulator.icon = "play"

    def mainactioncheck(self):

        if self.ids.roundregulator.icon == "play":
            self.nextround()
        elif self.ids.roundregulator.icon == "stop":
            ConfirmDialog().open()
        elif self.ids.roundregulator.icon == "check" and self.ids.currentround.text == f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}[/font][/size]":

            # Round 2 - Reveal All 3 Logs
            for num in range(3):

                if globals.loginfo[f"log {num + 1}"]["hacked"] == True:
                    globals.loginfo[f"log {num + 1}"]["hackers"] = globals.loginfo[f"log {num + 1}"]["hackers"] - 1

                if globals.loginfo[f"log {num + 1}"]["backedup"] == True:

                    log, logtext = createlog(3, globals.loginfo[f"log {num + 1}"]["hackers"], globals.loginfo[f"log {num + 1}"]["code"])

                    self.ids[f"round2sub{num + 1}"].text = log
                    self.ids[f"round2sub{num + 1}text"].text = logtext

                elif globals.loginfo[f"log {num + 1}"]["corrupted"] == False:

                    if random.random() < 0.85:
                        # Upon Success
                        log, logtext = createlog(3, globals.loginfo[f"log {num + 1}"]["hackers"], globals.loginfo[f"log {num + 1}"]["code"])

                        self.ids[f"round2sub{num + 1}"].text = log
                        self.ids[f"round2sub{num + 1}text"].text = logtext

                    else:
                        self.ids[f"round2sub{num + 1}"].text = f"[color={globals.colordefs['Red']}][size=30sp][font=Icons]{md_icons['file-alert']}[/font] [font=Icons]{md_icons['file-alert']}[/font] [font=Icons]{md_icons['file-alert']}[/color][/font][/size]"
                        self.ids[f"round2sum{num + 1}"].text = f"[color={globals.colordefs['Red']}]The log has been corrupted![/color]"
                        self.ids[f"logtitle{num + 1}"].text = f"[font=Icons]{md_icons['folder-alert']}[/font] {globals.logbuttonword[num + 1]}"
                        self.ids[f"logtitle{num + 1}"].canvas.before.get_group(f'{num + 1}')[0].rgb = get_color_from_hex(globals.colordefs['Red'])

                else:
                    self.ids[f"round2sub{num + 1}"].text = f"[color={globals.colordefs['Red']}][size=30sp][font=Icons]{md_icons['file-alert']}[/font] [font=Icons]{md_icons['file-alert']}[/font] [font=Icons]{md_icons['file-alert']}[/color][/font][/size]"
                    self.ids[f"round2sum{num + 1}"].text = f"[color={globals.colordefs['Red']}]The log has been corrupted![/color]"
                    self.ids[f"logtitle{num + 1}"].text = f"[font=Icons]{md_icons['folder-alert']}[/font] {globals.logbuttonword[num + 1]}"
                    self.ids[f"logtitle{num + 1}"].canvas.before.get_group(f'{num + 1}')[0].rgb = get_color_from_hex(globals.colordefs['Red'])

            self.settime(360)
            self.ids.roundregulator.icon = "stop"
            self.ids.mainscreenmanager.current = "timescreen"

        # Round 3 Check
        elif self.ids.roundregulator.icon == "check" and self.ids.currentround.text == f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]":
            self.settime(300)
            self.ids.roundregulator.icon = "stop"
            self.ids.mainscreenmanager.current = "timescreen"

# Configure timer
    def settime(self, time):

        globals.time = time
        minutes, seconds = divmod(globals.time, 60)
        self.ids.mainscreenmanager.get_screen("timescreen").ids.timer.text =\
            "{:02}:{:02}".format(int(minutes), int(seconds))
        globals.timer = Clock.schedule_interval(self.activatetime, 1)

    def activatetime(self, dt):
        if globals.time == 0:

            globals.timer.cancel()

        # Check if moving to the results screen
            if self.ids.currentround.text == f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]" and self.ids.roundregulator.icon == "stop":
                self.ids.roundregulator.icon = "square-rounded-outline"
                self.ids.roundregulator.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]

            elif self.ids.roundregulator.icon == "stop":
                self.ids.roundregulator.icon = "play"

        else:
            globals.time -= 1
            minutes, seconds = divmod(globals.time, 60)
            self.ids.mainscreenmanager.get_screen("timescreen").ids.timer.text =\
                "{:02}:{:02}".format(int(minutes), int(seconds))

    def nextround(self):

# Round 1
        if self.ids.currentround.text == f"[size=30sp][font=Icons]{md_icons['circle-outline']}{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]":

            # Alter displays
            self.ids.currentround.text = f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]"
            self.ids.mainpanel.switch_tab("archive-lock", search_by="icon")

            self.settime(60) # 1 minute
            self.ids.roundregulator.icon = "stop"

            # Reveal log
            log, logtext = createlog(4, None, None)
            self.ids.round1sub.text = log
            self.ids.round1subtext.text = logtext

# Round 2
        elif self.ids.currentround.text == f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]":

            # Set log information for actions
            for x in range(1, 4):
                globals.loginfo[f"log {x}"] = {"hackers": createhackeramt()}
                globals.loginfo[f"log {x}"]['backedup'] = False
                globals.loginfo[f"log {x}"]['corrupted'] = False
                globals.loginfo[f"log {x}"]['hacked'] = False
                globals.loginfo[f"log {x}"]['code'] = None

            # Alter displays
            ActionScreen.setactionplayers(self)
            self.ids.mainscreenmanager.current = "actionscreen"

            self.ids.currentround.text = f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}[/font][/size]"
            self.ids.mainpanel.switch_tab("archive", search_by="icon")
            self.ids.roundregulator.icon = "square-rounded-outline"

# Round 3
        else:
            self.ids.currentround.text = f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]"
            self.ids.mainpanel.switch_tab("archive-eye", search_by="icon")
            self.ids.roundregulator.icon = "square-rounded-outline"

            # Sets what players are provided logs, ais will not get logs.
            if globals.players <= 5:
                globals.playerlogrev = random.sample(list(globals.notai), 2)
            else:
                globals.playerlogrev = random.sample(list(globals.playerlist), 2)

            num = 1
            for player in globals.playerlogrev:
                self.ids.mainscreenmanager.get_screen("playerlogscreen").ids[f'log{num}'].color = globals.colordefs[globals.playerlist[player]['color']]
                num += 1

            # Reveal who's log it is.
            for num in range(1, 3):
                self.ids[f'playerlog{num}'].text = f"[font=Icons]{md_icons['folder-eye']}[/font] {globals.playerlist[globals.playerlogrev[num - 1]]['color']}'s Log"
                self.ids[f'playerlog{num}'].text_size = None, None
                self.ids[f'playerlog{num}'].canvas.before.get_group(f'{num}')[0].rgb = get_color_from_hex(globals.colordefs[globals.playerlist[globals.playerlogrev[num - 1]]['color']])

            # Prepare log tracker
            globals.revealtracker = 1
            self.ids.mainscreenmanager.get_screen("playerlogscreen").ids.nextplayer.text = f"It's {globals.playerlist[globals.playerlogrev[globals.revealtracker - 1]]['color']}'s turn."

            # Change main screen
            self.ids.mainscreenmanager.current = "playerlogscreen"

    def nextscreen(self):

        EndGame.setresults(self)
        self.manager.transition.direction = "left"
        self.manager.current = "endgame"

        # Reset Phases
        self.ids.mainscreenmanager.get_screen('actionscreen').ids.useaction.disabled = False
        self.ids.mainscreenmanager.get_screen('actionscreen').ids.act1.icon = 'circle-slice-8'
        self.ids.mainscreenmanager.get_screen('playerlogscreen').ids.reveallog.disabled = False
        self.ids.mainscreenmanager.get_screen('playerlogscreen').ids.log1.icon = 'circle-slice-8'

        # Reset Round 1 Logs
        self.ids.round1sub.text = f"[size=30sp][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"
        self.ids.round1subtext.text = " "

        # Reset Round 2 Logs
        for num in range(1, 4):
            self.ids[f'round2sub{num}'].text = f"[size=30sp][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"
            self.ids[f'round2sub{num}text'].text = " "
            self.ids[f'round2sum{num}'].text = "At least one hacker is among the following."
            self.ids[f'logtitle{num}'].canvas.before.get_group(f'{num}')[0].rgb = MDApp.get_running_app().theme_cls.primary_color
            self.ids[f'logtitle{num}'].text = f"[font=Icons]{md_icons['folder']}[/font] {globals.logbuttonword[num]}"

        # Reset Round 3 Logs
        for num in range(1, 3):
            self.ids[f'playerlog{num}'].text = f"[font=Icons]{md_icons['folder-eye']}[/font] Player Log"
            self.ids[f'playerlog{num}'].text_size = None, None
            self.ids[f'playerlog{num}'].canvas.before.get_group(f'{num}')[0].rgb = MDApp.get_running_app().theme_cls.primary_color

        # Reset round indicator and navigator
        self.ids.currentround.text = f"[size=30sp][font=Icons]{md_icons['circle-outline']}{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]"
        self.ids.roundregulator.right_action_items = []
        self.ids.roundregulator.icon = "play"

        # Set tab back to round 1
        self.ids.mainpanel.switch_tab("archive-lock", search_by="icon")

class codenetApp(MDApp):
#Global Variables Between KV and PY
    import globals

    def build(self):
        pass

if __name__ == "__main__":
    codenetApp().run()