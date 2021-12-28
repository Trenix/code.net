from kivymd.uix.screen import MDScreen
from displays.dialogcode import LogDialog
from main import MDApp
from systems.generateplayerlog import createplayerlog
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
        temppop.ids.playerlogtitle.text = f"{globals.playerlist[globals.playerlogrev[globals.revealtracker - 1]]['color']}'s Log"

        # Creates player log based on the title of the popup
        if temppop.ids.playerlogtitle.text == f"{globals.playerlist[globals.playerlogrev[0]]['color']}'s Log":
            log = createplayerlog(globals.playerlogrev[0])
        else:
            log = createplayerlog(globals.playerlogrev[1])

        temppop.ids.log1sub.text = log
        temppop.open()