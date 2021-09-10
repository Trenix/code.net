import globals
from kivymd.icon_definitions import md_icons
from kivymd.uix.screen import MDScreen

class ColorSelectScreen(MDScreen):

    def ColorSelect(self, instance):
# Sets colors to players in a sequence
        if globals.colortracker > 0 and instance.icon == "circle-outline":
            globals.playerlist[f"player {globals.playercounter}"]["color"] = instance.text
            instance.icon = "numeric-" + str(globals.playercounter) + "-circle-outline"
            globals.playercounter += 1
            globals.colortracker -= 1
            self.ids.remainder.text = f"[size=22][font=Icons]{md_icons['account-group']}[/font][/size] Players: {globals.players}\n[size=22][font=Icons]{md_icons['counter']}[/font][/size] Remainder: {globals.colortracker}"

# Clicking last color selected, will clear it
        elif instance.icon != "circle-outline" and instance.icon == ("numeric-" + str(globals.playercounter - 1) + "-circle-outline"):
            instance.icon = "circle-outline"
            globals.playercounter -= 1
            globals.colortracker += 1
            self.ids.remainder.text = f"[size=22][font=Icons]{md_icons['account-group']}[/font][/size] Players: {globals.players}\n[size=22][font=Icons]{md_icons['counter']}[/font][/size] Remainder: {globals.colortracker}"

    def RefreshTracker(self):

        for x in range(9):
            self.ids[f"but{x + 1}"].icon = "circle-outline"

        globals.colortracker = globals.players
        globals.playercounter = 1
        self.ids.remainder.text = f"[size=22][font=Icons]{md_icons['account-group']}[/font][/size] Players: {globals.players}\n[size=22][font=Icons]{md_icons['counter']}[/font][/size] Remainder: {globals.colortracker}"

    def nextscreen(self):

        if globals.colortracker == 0:
            self.manager.current = "reveal"
            self.manager.transition.direction = "left"

            #Setup tracker
            self.manager.get_screen("reveal").ids.setgrid.cols = globals.players

            # Destroy widgets not in play
            for x in range(globals.players + 1, 9 + 1):
                self.manager.get_screen("reveal").ids.setgrid.remove_widget(self.manager.get_screen("reveal").ids[f"ind{x}"])

            # Set colors
            for x in range(globals.players):
                self.manager.get_screen("reveal").ids[f"ind{x + 1}"].color = globals.colordefs[globals.playerlist[f"player {x + 1}"]["color"]]

    def previousscreen(self):
        self.manager.current = "player"
        self.manager.transition.direction = "right"

        self.RefreshTracker()
        globals.playerlist.clear()
        globals.coderlist.clear()
        globals.hackerlist.clear()
        globals.notai.clear()