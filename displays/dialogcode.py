from kivymd.uix.dialog import MDDialog
import globals

class ActionDialog(MDDialog):
    pass

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
    pass