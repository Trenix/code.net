import globals
from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex

class ColorSelectScreen(MDScreen):
    from systems.openinformation import openinfo

    def ColorSelect(self, instance):
# Sets colors to players in a sequence
        if globals.colortracker > 0 and instance.icon == "circle":
            globals.playerlist[f"player {globals.playercounter}"]["color"] = instance.text
            instance.icon = "numeric-" + str(globals.playercounter) + "-circle"
            globals.playercounter += 1
            globals.colortracker -= 1
            self.ids.remainder.text = f"Remainder: {globals.colortracker}"
            if globals.colortracker == 0:
                self.ids.colorbottomtoolbar.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]

# Clicking last color selected, will clear it
        elif instance.icon != "circle" and instance.icon == ("numeric-" + str(globals.playercounter - 1) + "-circle"):
            instance.icon = "circle"
            globals.playercounter -= 1
            globals.colortracker += 1
            self.ids.remainder.text = f"Remainder: {globals.colortracker}"
            self.ids.colorbottomtoolbar.right_action_items = []

    def RefreshTracker(self):

        for x in range(9):
            self.ids[f"but{x + 1}"].icon = "circle"

        globals.colortracker = globals.players
        globals.playercounter = 1
        self.ids.colorbottomtoolbar.right_action_items = []
        self.ids.remainder.text = f"Remainder: {globals.colortracker}"

    def nextscreen(self):

        #Setup tracker
        self.manager.get_screen("reveal").ids.setgrid.cols = globals.players

        # Create indicator icons
        for x in range(2, 10):
            self.manager.get_screen("reveal").ids[f"ind{x}"].icon = 'circle-outline'
            self.manager.get_screen("reveal").ids[f"ind{x}"].parent.size_hint = 1, 1

        # Remove indicator icons
        for x in range(globals.players + 1, 10):
            self.manager.get_screen("reveal").ids[f"ind{x}"].icon = ''
            self.manager.get_screen("reveal").ids[f"ind{x}"].parent.size_hint = 0, 0

        # Set colors
        for x in range(globals.players):
            self.manager.get_screen("reveal").ids[f"ind{x + 1}"].color = get_color_from_hex(globals.colordefs[globals.playerlist[f"player {x + 1}"]["color"]])

        self.manager.get_screen("reveal").ids.nextplayer.text = "It's " + globals.playerlist["player 1"]["color"] + "'s turn!"

        self.manager.current = "reveal"
        self.manager.transition.direction = "left"
        self.RefreshTracker()

    def previousscreen(self):
        self.manager.current = "player"
        self.manager.transition.direction = "right"
        self.ids.colorbottomtoolbar.right_action_items = []
        self.RefreshTracker()
        globals.playerlist.clear()
        globals.coderlist.clear()
        globals.hackerlist.clear()
        globals.notai.clear()