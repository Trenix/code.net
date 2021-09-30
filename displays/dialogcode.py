from kivymd.uix.dialog import MDDialog
from systems.generateplayerlog import createplayerlog
import globals

class IdentityDialog(MDDialog):
    pass

class ConfirmDialog(MDDialog):
    pass

class RematchDialog(MDDialog):
    pass

class LogDialog(MDDialog):

    def revealplayerlog(self):

        # Creates player log based on the title of the popup
        if self.ids.playerlogtitle.text == f"{globals.playerlist[globals.playerlogrev[0]]['color']}'s Log":
            log = createplayerlog(globals.playerlogrev[0])
        else:
            log = createplayerlog(globals.playerlogrev[1])
        self.ids.log1sub.text = log
        self.ids.playerlogbutton.disabled = True