from kivymd.uix.screen import MDScreen
import globals

class PlayerInfo(MDScreen):

    def close(self):
        self.manager.transition.direction = 'down'
        self.manager.current = "player"

class MainInfo(MDScreen):

    def close(self):
        self.manager.transition.direction = 'down'
        self.manager.current = globals.lastscreen