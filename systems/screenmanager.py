from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

class WindowManager(ScreenManager):
# Read keys in these screens
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)

# Go back if pressing back in app or esc in Windows 10
    def on_key(self, window, key, *args):
        if key == 27:  # the esc key
            if self.current_screen.name == "welcome":
                return False  # exit the app from this page
            elif self.current_screen.name == "player":
                self.current = "welcome"
                self.transition.direction = "right"

                # Reset toggle on buttons
                for x in range(6):
                    self.get_screen("player").ids[f"butt{x + 1}"].state = "normal"

                return True  # do not exit the app

            elif self.current_screen.name == "colorselect":

                globals.colortracker = globals.players
                globals.playercounter = 1

                #Clear colorselect screen
                for x in range(9):
                    self.get_screen("colorselect").ids[f"but{x + 1}"].icon = "circle-outline"

                self.current = "player"
                self.transition.direction = "right"
                globals.playerlist.clear()
                return True  # do not exit the app