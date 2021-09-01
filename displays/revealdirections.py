from kivymd.uix.screen import MDScreen
from main import RevealPopup
from main import codenetApp
import globals

class PlayerReveal(MDScreen):

    def reveal(self):

        if globals.revealtracker <= globals.players:

            if self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == True and globals.revealtracker <= globals.players:
                ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
                if globals.players <= 8:
                    tempdialog = RevealPopup()
                    tempdialog.ids.arehacker.text = "[u]Faction[/u]: Hacker\n[u]Ally[/u]: " + globals.playerlist[ally]["color"]
                    tempdialog.ids.identitydes.text = "[u]Objective[/u]: Keep your identity hidden and have the coders trust you and your ally while making them distrust each other."
                    tempdialog.open()
                else:
                    tempdialog = RevealPopup()
                    tempdialog.ids.arehacker.text = "[u]Faction[/u]: Hacker\n[u]Allies[/u]: " + globals.playerlist[ally[0]]["color"] + ", " + globals.playerlist[ally[1]]["color"]
                    tempdialog.ids.identitydes.text = "[u]Objective[/u]: Keep your identity hidden and have the coders trust you and your allies while making them distrust each other."
                    tempdialog.open()

            elif self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == False and globals.revealtracker <= globals.players:
                tempdialog = RevealPopup()
                tempdialog.ids.arehacker.text = "[u]Faction[/u]: Coder"
                tempdialog.ids.identitydes.text = f"[u]Objective[/u]: Find the {globals.amtbad} hackers among the team and distrust them, while indentifying and trusting other coders."
                tempdialog.open()

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