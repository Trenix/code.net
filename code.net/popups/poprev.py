from main import *
import globals

class RevealPopup(Popup):

    def ColorTrack(self):
        globals.colortracker = 0
        self.ids.exitcolor.disabled = True


    def ColorSelect(self):
        if globals.colortracker == 0:
            globals.playerlist[f"player {globals.playercounter - 1}"]["color"] = App.get_running_app().buttonname
            self.ids[App.get_running_app().buttonname].disabled = True
            self.ids.exitcolor.disabled = False
            globals.colortracker = 1

    #TODO: Allow players to change their color incase of an accidental click.