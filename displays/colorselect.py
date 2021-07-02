import globals
from kivymd.uix.screen import MDScreen
from kivymd.uix.progressbar import MDProgressBar


class ColorSelectScreen(MDScreen):

    def ColorSelect(self, instance):
# Sets colors to players in a sequence
        if globals.colortracker > 0 and instance.icon == "circle-outline":
            globals.playerlist[f"player {globals.playercounter}"]["color"] = instance.text
            instance.icon = "numeric-" + str(globals.playercounter) + "-circle-outline"
            globals.playercounter += 1
            globals.colortracker -= 1

# Clicking last color selected, will clear it
        elif instance.icon != "circle-outline" and instance.icon == ("numeric-" + str(globals.playercounter - 1) + "-circle-outline"):
            instance.icon = "circle-outline"
            globals.playercounter -= 1
            globals.colortracker += 1

    def RefreshTracker(self):

        tempvariable = []

        for x in range(9):
            tempvariable.append(f"but{x + 1}")

        for x in tempvariable:
            self.ids[x].icon = "circle-outline"

        globals.colortracker = globals.players
        globals.playercounter = 1

    def nextscreen(self):

        if globals.colortracker == 0:
            self.manager.current = "reveal"
            self.manager.transition.direction = "left"

        #Setup tracker
        #
        # if globals.players == 4:
        #     self.manager.get_screen("reveal").ids.setgrid.cols = 4
        #
        #     for x in range(4):
        #         tempvar =
        #
        #     for x in range(4):
        #         self.manager.get_screen("reveal").ids.setgrid.add_widget(MDProgressBar(value=100, id=f"track{x+1}"))
        #     #print(self.manager.get_screen("reveal").ids)



            #
            # tempvariable = []
            # for x in range(5, 9):
            #     tempvariable.append(f"ind{x}")
            #
            # for x in tempvariable:
            #     self.manager.get_screen("reveal").ids.setgrid.remove_widget(self.manager.get_screen("reveal").ids[x])

    def previousscreen(self):
        self.manager.current = "player"
        self.manager.transition.direction = "right"

        self.RefreshTracker()