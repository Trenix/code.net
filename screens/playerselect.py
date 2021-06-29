from kivymd.uix.screen import MDScreen
from main import MDApp
import globals

class PlayerWindow(MDScreen):
    from systems.generatelists import playersetup

    def setplayervars(self):

        # 4 players
        if self.ids.butt1.state == "down":
            globals.amtbad = 2
            globals.players = 4
            globals.aiamt = 1
            self.nextscreen()

        # 5 players
        elif self.ids.butt2.state == "down":
            globals.amtbad = 2
            globals.players = 5
            globals.aiamt = 1
            self.nextscreen()

        # 6 players
        elif self.ids.butt3.state == "down":
            globals.amtbad = 2
            globals.players = 6
            self.nextscreen()

        # 7 players
        elif self.ids.butt4.state == "down":
            globals.amtbad = 2
            globals.players = 7
            self.nextscreen()

        # 8 players
        elif self.ids.butt5.state == "down":
            globals.amtbad = 2
            globals.players = 8
            self.nextscreen()

        # 9 players
        elif self.ids.butt6.state == "down":
            globals.amtbad = 3
            globals.players = 9
            self.nextscreen()

    def nextscreen(self):

        self.manager.current = "colorselect"
        self.manager.transition.direction = "left"

        self.playersetup()

# Set grid for next screen
        tempvariable = []

        for x in range(9):
            tempvariable.append(f"but{x + 1}")

        for x in tempvariable:
            self.manager.get_screen("colorselect").ids[x].size_hint = 1, 1