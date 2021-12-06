from kivymd.app import MDApp
from kivy.core.window import Window
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
from displays.dialogcode import LogDialog
from displays.dialogcode import IdentityDialog
from displays.dialogcode import ConfirmDialog
from displays.dialogcode import ActionDialog
from displays.information import MainInfo
from displays.action import ActionScreen
from kivy.clock import Clock
import random
import globals

KIVY_DPI=320
KIVY_METRICS_DENSITY=2

Window.size = (720, 1280)

class Tab(MDFloatLayout, MDTabsBase):
    pass

# Add toggle to iconbuttons
class MDFillRoundFlatIconButtonToggle(MDFillRoundFlatIconButton, MDToggleButton):
    pass

class MainWindow(MDScreen):
    from systems.openinformation import openinfo

    def resettimer(self):

        self.ids.mainscreenmanager.get_screen("timescreen").ids.timer.text = "[font=H4][size=40sp]00:00[/size][/font]"
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

# May be used, sets players less on log rather than specific amount.
#            templog = sorted(random.sample(list(globals.coderlist), ((globals.players + globals.aiamt) - tempamthacker) - playerslesslog) + random.sample(list(globals.hackerlist), tempamthacker))
#            playerslesslog = 2

# Logs per each round.

    def r3l1(self):
        self.ids.round3reveal1.disabled = True

        # Check if logs are complete before being allowed to move to next round
        if self.ids.round3reveal2.disabled == True and globals.time == 0:
            self.ids.roundregulator.icon = "square-rounded-outline"
            self.ids.roundregulator.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]
        elif self.ids.round3reveal2.disabled == True:
            self.ids.roundregulator.icon = "stop"

        temppop = LogDialog()
        temppop.ids.playerlogtitle.text = f"{globals.playerlist[globals.playerlogrev[0]]['color']}'s Log"
        temppop.open()

    def r3l2(self):

        self.ids.round3reveal2.disabled = True

        # Check if logs are complete before being allowed to move to next round
        if self.ids.round3reveal1.disabled == True and globals.time == 0:
            self.ids.roundregulator.icon = "square-rounded-outline"
            self.ids.roundregulator.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]
        elif self.ids.round3reveal1.disabled == True:
            self.ids.roundregulator.icon = "stop"

        temppop = LogDialog()
        temppop.ids.playerlogtitle.text = f"{globals.playerlist[globals.playerlogrev[1]]['color']}'s Log"
        temppop.open()

# Configure timer

    def settime(self, time):

        globals.time = time
        minutes, seconds = divmod(globals.time, 60)
        self.ids.mainscreenmanager.get_screen("timescreen").ids.timer.text = "[font=H4][size=40sp]" + "{:02}:{:02}".format(int(minutes), int(seconds)) + "[/font][/size]"
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
            self.ids.mainscreenmanager.get_screen("timescreen").ids.timer.text = "[font=H4][size=40sp]" + "{:02}:{:02}".format(int(minutes), int(seconds)) + "[/size][/font]"


    def nextround(self):

# Round 1
        if self.ids.currentround.text == f"[size=30sp][font=Icons]{md_icons['circle-outline']}{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]":

            # Alter displays
            self.ids.currentround.text = f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]"
            self.ids.mainpanel.switch_tab(f"[size=22sp][font=Icons]{md_icons['folder-search']}[/font][/size][size=15sp][font=Button] ROUND 1[/font][/size]")
            self.settime(60) # 1 minute
            self.ids.roundregulator.icon = "stop"

            # Reveal log
            log = createlog(4)
            self.ids.round1sub.text = log

# Round 2
        elif self.ids.currentround.text == f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]":

            #set log information for actions
            for x in range(3):
                globals.loginfo[f"log {x + 1}"] = {"hackers": createhackeramt()}
                globals.loginfo[f"log {x + 1}"]['protected'] = False
                globals.loginfo[f"log {x + 1}"]['corrupted'] = False

            ActionScreen.setactionplayers(self)
            self.ids.mainscreenmanager.current = "actionscreen"

            # Alter displays
            self.ids.currentround.text = f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}[/font][/size]"
            self.ids.mainpanel.switch_tab(f"[size=22sp][font=Icons]{md_icons['folder-search']}[/font][/size][size=15sp][font=Button] ROUND 2[/font][/size]")
            self.ids.roundregulator.icon = "square-rounded-outline"
            # self.settime(360)
            #
            # # Attempt Reveal First Log
            # if random.random() < 0.7:
            #
            #     log = createlog(3)
            #     self.ids.round2sub1.text = log
            #
            # else:
            #     self.ids.round2sub1.text = f"[color=#c62828][size=30sp][font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/color][/font][/size]"
            #     self.ids.round2sum1.text = "[color=#c62828]The log has been corrupted![/color]"
            #
            # # Attempt Reveal Second Log
            # if random.random() < 0.7:
            #
            #     log = createlog(3)
            #     self.ids.round2sub2.text = log
            #
            # else:
            #     self.ids.round2sub2.text = f"[color=#c62828][size=30sp][font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/color][/font][/size]"
            #     self.ids.round2sum2.text = "[color=#c62828]The log has been corrupted![/color]"
            #
            # # Attempt Reveal Third Log
            # if random.random() < 0.7:
            #
            #     log = createlog(3)
            #     self.ids.round2sub3.text = log
            #
            # else:
            #     self.ids.round2sub3.text = f"[color=#c62828][size=30sp][font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/color][/font][/size]"
            #     self.ids.round2sum3.text = "[color=#c62828]The log has been corrupted![/color]"

# Round 3
        else:
            self.ids.currentround.text = f"[color=#FFFFFF][size=30sp][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]"
            self.ids.mainpanel.switch_tab(f"[size=22sp][font=Icons]{md_icons['folder-search']}[/font][/size][size=15sp][font=Button] ROUND 3[/font][/size]")
            self.ids.roundregulator.icon = "square-rounded-outline"
            self.settime(300)

# Tab displays activated
            self.ids.round3reveal1.disabled = False
            self.ids.round3reveal2.disabled = False

# Sets what players are provided logs, ais will not get logs.
            if globals.players <= 5:
                globals.playerlogrev = random.sample(list(globals.notai), 2)
            else:
                globals.playerlogrev = random.sample(list(globals.playerlist), 2)

    # Reveal who's log it is.
            self.ids.playerlog1.text = "[font=H4][size=20sp]" + f"{globals.playerlist[globals.playerlogrev[0]]['color']}" + "'s Log[/size][/font]"
            self.ids.playerlog2.text = "[font=H4][size=20sp]" + f"{globals.playerlist[globals.playerlogrev[1]]['color']}" + "'s Log[/size][/font]"
            self.ids.round3sum1.text_color = globals.colordefs[globals.playerlist[globals.playerlogrev[0]]['color']]
            self.ids.round3sum2.text_color = globals.colordefs[globals.playerlist[globals.playerlogrev[1]]['color']]

    def nextscreen(self):

        EndGame.setalignments(self)
        self.manager.current = "endgame"
        self.manager.transition.direction = "left"

        # Reset folders
        self.ids.round1sub.text = f"[size=30sp][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"
        self.ids.round2sub1.text = f"[size=30sp][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"
        self.ids.round2sub2.text = f"[size=30sp][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"
        self.ids.round2sub3.text = f"[size=30sp][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"

        # Reset possible log corruption text
        self.ids.round2sum1.text = "At least one hacker is among the following."
        self.ids.round2sum2.text = "At least one hacker is among the following."
        self.ids.round2sum3.text = "At least one hacker is among the following."

        # Reset player logs
        self.ids.playerlog1.text = "[font=H4][size=20sp]Player Log[/size][/font]"
        self.ids.playerlog2.text = "[font=H4][size=20sp]Player Log[/size][/font]"

        # Reset round indicator and navigator
        self.ids.currentround.text = f"[size=30sp][font=Icons]{md_icons['circle-outline']}{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]"
        self.ids.roundregulator.right_action_items = []
        self.ids.roundregulator.icon = "play"

        # Set tab back to round 1
        self.ids.mainpanel.switch_tab(
    f"[size=22sp][font=Icons]{md_icons['folder-search']}[/font][/size][size=15sp][font=Button] ROUND 1[/font][/size]")

class codenetApp(MDApp):
#Global Variables Between KV and PY
    import globals

    def build(self):
        pass

if __name__ == "__main__":
    codenetApp().run()