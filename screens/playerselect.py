from kivymd.uix.screen import MDScreen
import globals

class PlayerWindow(MDScreen):
    from systems.generatelists import playersetup

    def fourp(self):

        globals.amtbad = 2
        globals.players = 4
        globals.aiamt = 1

        self.playersetup()

    def fivep(self):

        globals.amtbad = 2
        globals.players = 5
        globals.aiamt = 1

        self.playersetup()

    def sixp(self):

        globals.amtbad = 2
        globals.players = 6

        self.playersetup()

    def sevenp(self):

        globals.amtbad = 2
        globals.players = 7

        self.playersetup()

    def eightp(self):

        globals.amtbad = 2
        globals.players = 8

        self.playersetup()

    def ninep(self):

        globals.amtbad = 3
        globals.players = 9

        self.playersetup()