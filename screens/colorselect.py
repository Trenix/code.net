import globals
from kivymd.uix.screen import MDScreen

class ColorSelectScreen(MDScreen):

    def ColorSelect(self, instance):

        if globals.colortracker > 0 and instance.icon == "brush":
            globals.playerlist[f"player {globals.playercounter}"]["color"] = instance.text
            instance.icon = "numeric-" + str(globals.playercounter) + "-circle-outline"
            globals.playercounter += 1
            globals.colortracker -= 1
        print(globals.colortracker)
        print(globals.playercounter)
        print(globals.playerlist)

    def ClearTracker(self):
        globals.playercounter = 1
        globals.colortracker = 0

        tempvariable = []

        for x in range(9):
            tempvariable.append(f"but{x + 1}")

        for x in tempvariable:
            self.manager.get_screen("colorselect").ids[x].icon = "brush"