from kivymd.uix.screen import MDScreen
from main import MDApp
import globals

class PlayerWindow(MDScreen):
    from systems.generatelists import playersetup

    def gridset(self):

        tempvariable = []

        for x in range(9):
            tempvariable.append(f"but{x + 1}")

        for x in tempvariable:
            self.manager.get_screen("colorselect").ids[x].size_hint = 1, 1

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