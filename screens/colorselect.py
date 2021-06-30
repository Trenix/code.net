import globals
from kivymd.uix.screen import MDScreen

class ColorSelectScreen(MDScreen):

    def ColorSelect(self, instance):
# Sets colors to players in a sequence
        if globals.colortracker > 0 and instance.icon == "brush":
            globals.playerlist[f"player {globals.playercounter}"]["color"] = instance.text
            instance.icon = "numeric-" + str(globals.playercounter) + "-circle-outline"
            globals.playercounter += 1
            globals.colortracker -= 1

# Clicking last color selected, will clear it
        elif instance.icon != "brush" and instance.icon == ("numeric-" + str(globals.playercounter - 1) + "-circle-outline"):
            instance.icon = "brush"
            globals.playercounter -= 1
            globals.colortracker += 1

    def RefreshTracker(self):

        tempvariable = []

        for x in range(9):
            tempvariable.append(f"but{x + 1}")

        for x in tempvariable:
            self.manager.get_screen("colorselect").ids[x].icon = "brush"

        globals.colortracker = globals.players
        globals.playercounter = 1

    def Continue(self):
        if globals.colortracker == 0:
            self.manager.current = "reveal"
            self.manager.transition.direction = "left"

    def ClearTracker(self):
        globals.playercounter = 1

        tempvariable = []

        for x in range(9):
            tempvariable.append(f"but{x + 1}")

        for x in tempvariable:
            self.manager.get_screen("colorselect").ids[x].icon = "brush"