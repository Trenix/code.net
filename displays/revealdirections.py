from kivymd.uix.screen import MDScreen
from main import RevealPopup
from main import codenetApp
# from kivymd.icon_definitions import md_icons
import globals

class PlayerReveal(MDScreen):

    def reveal(self):

        if globals.revealtracker <= globals.players:

            if self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == True and globals.revealtracker <= globals.players:
                ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
                if globals.players <= 8:
                    codenetApp.get_running_app().arehacker = "[u]Faction[/u]: Hacker\n[u]Ally[/u]: " + globals.playerlist[ally]["color"]
                    codenetApp.get_running_app().identitydes = "[u]Objective[/u]: Keep your identity hidden and have the coders trust you and your ally while making them distrust each other."
                    RevealPopup().open()
                else:
                    codenetApp.get_running_app().arehacker = "[u]Faction[/u]: Hacker\n[u]Allies[/u]: " + globals.playerlist[ally[0]]["color"] + ", " + globals.playerlist[ally[1]]["color"]
                    codenetApp.get_running_app().identitydes = "[u]Objective[/u]: Keep your identity hidden and have the coders trust you and your allies while making them distrust each other."
                    RevealPopup().open()

            elif self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == False and globals.revealtracker <= globals.players:
                codenetApp.get_running_app().arehacker = "[u]Faction[/u]: Coder"
                codenetApp.get_running_app().identitydes = f"[u]Objective[/u]: Find the {globals.amtbad} hackers among the team and distrust them, while indentifying and trusting other coders."
                RevealPopup().open()

            if globals.revealtracker < globals.players:
                self.ids[f"ind{globals.revealtracker}"].icon = "circle-outline"
                globals.revealtracker += 1
                self.ids[f"ind{globals.revealtracker}"].icon = "circle-slice-8"

            elif globals.revealtracker == globals.players:
                self.ids[f"ind{globals.revealtracker}"].icon = "circle-outline"
                globals.revealtracker += 1
                self.ids.revtool.icon = "square-rounded-outline"
                self.ids.revtool.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]

    def nextscreen(self):
        if globals.revealtracker > globals.players:
            self.manager.current = "main"