from kivymd.uix.screen import MDScreen

class PlayerInfo(MDScreen):

    def close(self):
        self.manager.transition.direction = 'down'
        self.manager.current = "player"