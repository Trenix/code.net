from kivymd.uix.screen import MDScreen

class WelcomeWindow(MDScreen):
    from systems.openinformation import openinfo

    def nextscreen(self):
        self.manager.current = "player"
        self.manager.transition.direction = "left"