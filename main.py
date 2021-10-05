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
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from displays.dialogcode import LogDialog
from displays.dialogcode import IdentityDialog
from displays.dialogcode import ConfirmDialog
from displays.information import MainInfo
from kivy.clock import Clock
import random
import globals

Window.size = (400, 800)

class Tab(MDFloatLayout, MDTabsBase):
    pass

# Add toggle to iconbuttons
class MDFillRoundFlatIconButtonToggle(MDFillRoundFlatIconButton, MDToggleButton):
    pass

class MainWindow(MDScreen):
    from systems.openinformation import openinfo

    def resettimer(self):

        self.ids.timer.text = "[font=H4][size=30]00:00[/size][/font]"
        globals.timer.cancel()

        if self.ids.currentround.text == f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]":
            self.ids.roundregulator.icon = "square-rounded-outline"
            self.ids.roundregulator.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]

        else:
            self.ids.roundregulator.icon = "play"

    def mainactioncheck(self):

        if self.ids.roundregulator.icon == "play":
            self.nextround()
        elif self.ids.roundregulator.icon == "stop":
            ConfirmDialog().open()

#Logs per each round.

    def r1l1(self):

        self.ids.round1reveal.disabled = True

        # Check if logs are complete before being allowed to move to next round
        if globals.time == 0:
            self.ids.roundregulator.icon = "play"
        else:
            self.ids.roundregulator.icon = "stop"

        if random.random() < 0.7:

            self.ids.round1sum.text = "At least one hacker is among the following."
            log = createlog(4)
            self.ids.round1sub.text = log

# May be used, sets players less on log rather than specific amount.
#            templog = sorted(random.sample(list(globals.coderlist), ((globals.players + globals.aiamt) - tempamthacker) - playerslesslog) + random.sample(list(globals.hackerlist), tempamthacker))
#            playerslesslog = 2
#-----------------------------------------------

        else:
            self.ids.round1sub.text = f"[color=#c62828][size=30][font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/color][/font][/size]"
            self.ids.round1sum.text = "[color=#c62828]The log has been corrupted![/color]"

    def r2l1(self):

        self.ids.round2reveal1.disabled = True

        # Check if logs are complete before being allowed to move to next round
        if self.ids.round2reveal2.disabled == True and globals.time == 0:
            self.ids.roundregulator.icon = "play"
        elif self.ids.round2reveal2.disabled == True:
            self.ids.roundregulator.icon = "stop"

        if random.random() < 0.7:

            self.ids.round2sum1.text = "At least one hacker is among the following."
            log = createlog(3)
            self.ids.round2sub1.text = log

        else:
            self.ids.round2sub1.text = f"[color=#c62828][size=30][font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/color][/font][/size]"
            self.ids.round2sum1.text = "[color=#c62828]The log has been corrupted![/color]"

    def r2l2(self):

        self.ids.round2reveal2.disabled = True

        # Check if logs are complete before being allowed to move to next round
        if self.ids.round2reveal1.disabled == True and globals.time == 0:
            self.ids.roundregulator.icon = "play"
        elif self.ids.round2reveal1.disabled == True:
            self.ids.roundregulator.icon = "stop"

        if random.random() < 0.7:

            self.ids.round2sum2.text = "At least one hacker is among the following."
            log = createlog(3)
            self.ids.round2sub2.text = log

        else:
            self.ids.round2sub2.text = f"[color=#c62828][size=30][font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/color][/font][/size]"
            self.ids.round2sum2.text = "[color=#c62828]The log has been corrupted![/color]"

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

    def settime(self):

        globals.time = 300 # 5 minutes
        minutes, seconds = divmod(globals.time, 60)
        self.ids.timer.text = "[font=H4][size=30]" + "{:02}:{:02}".format(int(minutes), int(seconds)) + "[/font][/size]"
        globals.timer = Clock.schedule_interval(self.activatetime, 1)

    def activatetime(self, dt):
        if globals.time == 0:

            globals.timer.cancel()

        # Check if moving to the next screen
            if self.ids.currentround.text == f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]" and self.ids.roundregulator.icon == "stop":
                self.ids.roundregulator.icon = "square-rounded-outline"
                self.ids.roundregulator.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]

            elif self.ids.roundregulator.icon == "stop":
                self.ids.roundregulator.icon = "play"

        else:
            globals.time -= 1
            minutes, seconds = divmod(globals.time, 60)
            self.ids.timer.text = "[font=H4][size=30]" + "{:02}:{:02}".format(int(minutes), int(seconds)) + "[/size][/font]"


    def nextround(self):

# Round 1
        if self.ids.currentround.text == f"[size=30][font=Icons]{md_icons['circle-outline']}{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]":
            self.ids.currentround.text = f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]"
            self.ids.mainpanel.switch_tab(f"[size=22][font=Icons]{md_icons['folder-search']}[/font][/size][size=15][font=Button] ROUND 1[/font][/size]")
            self.ids.roundregulator.icon = "square-rounded-outline"
            self.settime()

#Tab displays activated
            self.ids.round1reveal.disabled = False

# Round 2
        elif self.ids.currentround.text == f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]":
            self.ids.currentround.text = f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}[/font][/size]"
            self.ids.mainpanel.switch_tab(f"[size=22][font=Icons]{md_icons['folder-search']}[/font][/size][size=15][font=Button] ROUND 2[/font][/size]")
            self.ids.roundregulator.icon = "square-rounded-outline"
            self.settime()

#Tab displays activated
            self.ids.round2reveal1.disabled = False
            self.ids.round2reveal2.disabled = False

# Round 3
        else:
            self.ids.currentround.text = f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]"
            self.ids.mainpanel.switch_tab(f"[size=22][font=Icons]{md_icons['folder-search']}[/font][/size][size=15][font=Button] ROUND 3[/font][/size]")
            self.ids.roundregulator.icon = "square-rounded-outline"
            self.settime()

# Tab displays activated
            self.ids.round3reveal1.disabled = False
            self.ids.round3reveal2.disabled = False

# Sets what players are provided logs, ais will not get logs.
            if globals.players <= 5:
                globals.playerlogrev = random.sample(list(globals.notai), 2)
            else:
                globals.playerlogrev = random.sample(list(globals.playerlist), 2)

    def nextscreen(self):

        EndGame.setalignments(self)
        self.manager.current = "endgame"
        self.manager.transition.direction = "left"

        # Reset folders
        self.ids.round1sub.text = f"[size=30][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"
        self.ids.round2sub1.text = f"[size=30][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"
        self.ids.round2sub2.text = f"[size=30][font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font] [font=Icons]{md_icons['folder']}[/font][/size]"

        # Reset possible log corruption text
        self.ids.round1sum.text = "At least one hacker is among the following."
        self.ids.round2sum1.text = "At least one hacker is among the following."
        self.ids.round2sum2.text = "At least one hacker is among the following."

        # Reset round indicator and navigator
        self.ids.currentround.text = f"[size=30][font=Icons]{md_icons['circle-outline']}{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]"
        self.ids.roundregulator.right_action_items = []
        self.ids.roundregulator.icon = "play"

        # Set tab back to round 1
        self.ids.mainpanel.switch_tab(
    f"[size=22][font=Icons]{md_icons['folder-search']}[/font][/size][size=15][font=Button] ROUND 1[/font][/size]")

class codenetApp(MDApp):
#Global Variables Between KV and PY

    def build(self):
        pass

if __name__ == "__main__":
    codenetApp().run()