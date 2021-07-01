from kivymd.uix.screen import MDScreen

class WelcomeWindow(MDScreen):
    def nextscreen(self):

        # Set grid for next screen
        tempvariable = []

        for x in range(6):
            tempvariable.append(f"butt{x + 1}")

        for x in tempvariable:
            self.manager.get_screen("player").ids[x].size_hint = 1, 1

        self.manager.current = "player"
        self.manager.transition.direction = "left"