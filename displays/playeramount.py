from kivymd.uix.screen import MDScreen
import globals

class PlayerWindow(MDScreen):
    from systems.generatelists import playersetup

    def setplayervars(self):

        # 4 players
        if self.ids.butt1.state == "down":
            globals.amtbad = 2
            globals.players = 4
            globals.aiamt = 1
            self.manager.get_screen("colorselect").ids.strplayeramt.text = "4 Players"
            self.nextscreen()

        # 5 players
        elif self.ids.butt2.state == "down":
            globals.amtbad = 2
            globals.players = 5
            globals.aiamt = 1
            self.manager.get_screen("colorselect").ids.strplayeramt.text = "5 Players"
            self.nextscreen()

        # 6 players
        elif self.ids.butt3.state == "down":
            globals.amtbad = 2
            globals.players = 6
            self.manager.get_screen("colorselect").ids.strplayeramt.text = "6 Players"
            self.nextscreen()

        # 7 players
        elif self.ids.butt4.state == "down":
            globals.amtbad = 2
            globals.players = 7
            self.manager.get_screen("colorselect").ids.strplayeramt.text = "7 Players"
            self.nextscreen()

        # 8 players
        elif self.ids.butt5.state == "down":
            globals.amtbad = 2
            globals.players = 8
            self.manager.get_screen("colorselect").ids.strplayeramt.text = "8 Players"
            self.nextscreen()

        # 9 players
        elif self.ids.butt6.state == "down":
            globals.amtbad = 3
            globals.players = 9
            self.manager.get_screen("colorselect").ids.strplayeramt.text = "9 Players"
            self.nextscreen()

    def refresh(self):

        # Reset toggle on buttons
        for x in range(6):
            self.ids[f"butt{x + 1}"].state = "normal"

    def previousscreen(self):

        self.manager.current = "welcome"
        self.manager.transition.direction = "right"

        self.refresh()

    def nextscreen(self):

        self.manager.current = "colorselect"
        self.manager.transition.direction = "left"

        self.refresh()
        self.playersetup()

# Set grid for next screen
        for x in range(9):
            self.manager.get_screen("colorselect").ids[f"but{x + 1}"].size_hint = 1, 1