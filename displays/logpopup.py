from kivymd.uix.dialog import MDDialog
from systems.generateplayerlog import createplayerlog

class LogDialog(MDDialog):

    def revealplayerlog(self):
        log = createplayerlog()
        self.ids.log1sub.text = log
        self.ids.playerlogbutton.disabled = True