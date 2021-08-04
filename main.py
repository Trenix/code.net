from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.icon_definitions import md_icons
from displays.playeramount import PlayerWindow
from displays.revealdirections import *
from displays.welcome import WelcomeWindow
from kivymd.uix.screen import MDScreen
from displays.loadsetup import LoadingScreen
from displays.colorselect import ColorSelectScreen
from systems.generatelog import createlog
from systems.generateplayerlog import createplayerlog
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from globals import * #might have to remove this?
import random
import globals

Window.size = (400, 800)

class RevealPopup(MDDialog):
    pass

class Tab(MDFloatLayout, MDTabsBase):
    pass

# Add toggle to iconbuttons
class MDFillRoundFlatIconButtonToggle(MDFillRoundFlatIconButton, MDToggleButton):
    pass

class MainWindow(MDScreen):

#Logs per each round.

    def r1l1(self):
        self.ids.startround.disabled = False
        self.ids.round1reveal.disabled = True

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

        if self.ids.round2reveal2.disabled == True:
            self.ids.startround.disabled = False

        self.ids.round2reveal1.disabled = True

        if random.random() < 0.7:

            self.ids.round2sum1.text = "At least one hacker is among the following."
            log = createlog(3)
            self.ids.round2sub1.text = log

        else:
            self.ids.round2sub1.text = f"[color=#c62828][size=30][font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/color][/font][/size]"
            self.ids.round2sum1.text = "[color=#c62828]The log has been corrupted![/color]"

    def r2l2(self):

        if self.ids.round2reveal1.disabled == True:
            self.ids.startround.disabled = False

        self.ids.round2reveal2.disabled = True

        if random.random() < 0.7:

            self.ids.round2sum2.text = "At least one hacker is among the following."
            log = createlog(3)
            self.ids.round2sub2.text = log

        else:
            self.ids.round2sub2.text = f"[color=#c62828][size=30][font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/font] [font=Icons]{md_icons['folder-alert']}[/color][/font][/size]"
            self.ids.round2sum2.text = "[color=#c62828]The log has been corrupted![/color]"

    def r3l1(self):
        self.ids.round3reveal1.disabled = True

        LogPopup.title = f"{globals.playerlist[globals.playerlogrev[0]]['color']}'s Log"
        log = createplayerlog()
        temppop = LogPopup()
        temppop.ids.log1sub.text = log + "."
        temppop.open()

    def r3l2(self):
        self.ids.round3reveal2.disabled = True
        LogPopup.title = f"{globals.playerlist[globals.playerlogrev[1]]['color']}'s Log"
        log = createplayerlog()
        temppop = LogPopup()
        temppop.ids.log1sub.text = log + "."
        temppop.open()

    def nextround(self):

# Round 1
        if self.ids.currentround.text == f"[size=30][font=Icons]{md_icons['circle-outline']}{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]":
            self.ids.currentround.text = f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]"
            self.ids.startround.disabled = True
            self.ids.mainpanel.switch_tab(f"[font=Button]ROUND 1[/font]")


#Tab displays activated
            self.ids.round1reveal.disabled = False
            self.ids.round1show.opacity = 1

# Round 2
        elif self.ids.currentround.text == f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}{md_icons['circle-outline']}[/font][/size]":
            self.ids.currentround.text = f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color]{md_icons['circle-outline']}[/font][/size]"
            self.ids.startround.disabled = True
            self.ids.mainpanel.switch_tab(f"[font=Button]ROUND 2[/font]")

#Tab displays activated
            self.ids.round2reveal1.disabled = False
            self.ids.round2reveal2.disabled = False
            self.ids.round2show.opacity = 1

# Round 3
        else:
            self.ids.currentround.text = f"[color=#FFFFFF][size=30][font=Icons]{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}{md_icons['circle-slice-8']}[/color][/font][/size]"
            self.ids.startround.disabled = True
            self.ids.mainpanel.switch_tab(f"[font=Button]ROUND 3[/font]")

# Tab displays activated
            self.ids.round3reveal1.disabled = False
            self.ids.round3reveal2.disabled = False
            self.ids.round3show.opacity = 1

# Sets what players are provided logs, ais will not get logs.
            if globals.players <= 5:
                globals.playerlogrev = random.sample(list(globals.notai), 2)
            else:
                globals.playerlogrev = random.sample(list(globals.playerlist.keys()), 2)

# Display what players have encrypted logs, only revealed on round 3.
            self.ids.round3reveal1.text = f"Reveal {globals.playerlist[globals.playerlogrev[0]]['color']}'s Log"
            self.ids.round3reveal2.text = f"Reveal {globals.playerlist[globals.playerlogrev[1]]['color']}'s Log"

            tempcolorlog = []

            for x in globals.playerlogrev:
                tempcolorlog.append(globals.playerlist[x]["color"])

            self.ids.round3sum1.text = f"[color={globals.colordefs2[tempcolorlog[0]]}][size=30][font=Icons]{md_icons['folder-key']}[/font] [font=Icons]{md_icons['folder-key']}[/font][/color][/size]"
            self.ids.round3sum2.text = f"[color={globals.colordefs2[tempcolorlog[1]]}][size=30][font=Icons]{md_icons['folder-key']}[/font] [font=Icons]{md_icons['folder-key']}[/font][/color][/size]"

class LogPopup(Popup):
    pass

class WindowManager(ScreenManager):
# Read keys in these screens
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)

# Go back if pressing back in app or esc in Windows 10
    def on_key(self, window, key, *args):
        if key == 27:  # the esc key
            if self.current_screen.name == "welcome":
                return False  # exit the app from this page
            elif self.current_screen.name == "player":
                self.current = "welcome"
                self.transition.direction = "right"

                # Reset toggle on buttons
                for x in range(6):
                    self.get_screen("player").ids[f"butt{x + 1}"].state = "normal"

                return True  # do not exit the app

            elif self.current_screen.name == "colorselect":

                globals.colortracker = globals.players
                globals.playercounter = 1

                #Clear colorselect screen
                for x in range(9):
                    self.get_screen("colorselect").ids[f"but{x + 1}"].icon = "circle-outline"

                self.current = "player"
                self.transition.direction = "right"
                globals.playerlist.clear()
                return True  # do not exit the app

class codenetApp(MDApp):
#Global Variables Between KV and PY

    arehacker = StringProperty("")
    identitydes = StringProperty("")

    def build(self):
        pass

if __name__ == "__main__":
    codenetApp().run()