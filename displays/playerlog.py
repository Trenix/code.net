from kivymd.uix.screen import MDScreen
from displays.dialogcode import LogDialog
from main import MDApp
from systems.generateplayerlog import createplayerlog
from kivymd.icon_definitions import md_icons
from kivy.utils import get_color_from_hex
import globals

class PlayerLogScreen(MDScreen):

    def trackplayer(self):
        if globals.revealtracker < 2:
            self.ids[f'log{globals.revealtracker}'].icon = "circle-outline"
            globals.revealtracker += 1
            self.ids[f'log{globals.revealtracker}'].icon = "circle-slice-8"
            self.ids.nextplayer.text = f"It's {globals.playerlist[globals.playerlogrev[globals.revealtracker - 1]]['color']}'s turn."
        else:
            self.ids.reveallog.disabled = True
            self.ids[f'log{globals.revealtracker}'].icon = "circle-outline"
            self.ids.nextplayer.text = "Pass the phone to the host."
            MDApp.get_running_app().root.get_screen("main").ids.roundregulator.icon = "check"

    def beginreveal(self):
        temppop = LogDialog()
        playercolor = globals.playerlist[globals.playerlogrev[globals.revealtracker - 1]]['color']

        temppop.ids.whatplayer.text = f"{playercolor}'s Log"

        # Create player log, set background color to player who owns log
        temppop.ids.logcard.md_bg_color = get_color_from_hex(globals.colordefs[playercolor])
        log, logtext = createplayerlog(globals.playerlogrev[globals.revealtracker - 1])

        temppop.ids.log1sub.text = log
        temppop.ids.log1subtext.text = logtext
        temppop.open()