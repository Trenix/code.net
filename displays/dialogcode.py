from kivymd.uix.dialog import MDDialog
from systems.generateplayerlog import createplayerlog
from kivymd.icon_definitions import md_icons
import globals

class IdentityDialog(MDDialog):
    pass

class ConfirmDialog(MDDialog):
    pass

class RematchDialog(MDDialog):
    from systems.generatelists import playersetup

    def rematch(self):
        # Save color before clearing and creating a new list
        tempcolorsave = []

        for x in range(globals.players):
            tempcolorsave.append(globals.playerlist[f"player {x + 1}"]["color"])

        # Create new list and add saved colors back
        self.playersetup()

        for x in range(globals.players):
            globals.playerlist[f"player {x + 1}"]["color"] = tempcolorsave[x]

    def newgame(self):
        globals.playerlist.clear()

class LogDialog(MDDialog):

    def revealplayerlog(self):

        # Creates player log based on the title of the popup
        if self.ids.playerlogtitle.text == f"{globals.playerlist[globals.playerlogrev[0]]['color']}'s Log":
            log = createplayerlog(globals.playerlogrev[0])
        else:
            log = createplayerlog(globals.playerlogrev[1])
        self.ids.log1sub.text = log
        self.ids.playerlogbutton.disabled = True