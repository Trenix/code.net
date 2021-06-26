from kivy.uix.popup import Popup
from main import MDApp
import globals

class RevealPopup(Popup):

    def ColorTrack(self):
        globals.colortracker = 0
        self.ids.exitcolor.disabled = True


    def ColorSelect(self):
        if globals.colortracker == 0:
            globals.playerlist[f"player {globals.playercounter - 1}"]["color"] = MDApp.get_running_app().buttonname
            self.ids[MDApp.get_running_app().buttonname].disabled = True
            self.ids.exitcolor.disabled = False
            globals.colortracker = 1