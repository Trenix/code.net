from kivymd.uix.screen import MDScreen
from main import IdentityDialog
import globals

class PlayerReveal(MDScreen):
    from systems.openinformation import openinfo

    def reveal(self):

        if globals.revealtracker <= globals.players:
            playercolor = globals.playerlist[f"player {globals.revealtracker}"]["color"]

            if self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == True and globals.revealtracker <= globals.players:
                ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
                if globals.players <= 8:
                    tempdialog = IdentityDialog()
                    tempdialog.ids.whatcolor.text = "[u]Color[/u]: " + playercolor
                    tempdialog.ids.arehacker.text = "[u]Faction[/u]: Hacker"
                    tempdialog.ids.haveallies.text = "[u]Ally[/u]: " + globals.playerlist[ally]["color"]
                    tempdialog.ids.identitydes.text = "[u]Objective[/u]: Keep your and your ally's identity hidden and have the coders trust you and distrust each other."
                    tempdialog.open()
                else:
                    tempdialog = IdentityDialog()
                    tempdialog.ids.whatcolor.text = "[u]Color[/u]: " + playercolor
                    tempdialog.ids.arehacker.text = "[u]Faction[/u]: Hacker"
                    tempdialog.ids.haveallies.text = "[u]Ally[/u]: " + globals.playerlist[ally[0]]["color"] + ", " + globals.playerlist[ally[1]]["color"]
                    tempdialog.ids.identitydes.text = "[u]Objective[/u]: Keep your identity hidden and have the coders trust you and your allies while making them distrust each other."
                    tempdialog.open()

            elif self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == False and globals.revealtracker <= globals.players:
                tempdialog = IdentityDialog()
                tempdialog.ids.identity.remove_widget(tempdialog.ids.haveallies)
                tempdialog.ids.whatcolor.text = "[u]Color[/u]: " + playercolor
                tempdialog.ids.arehacker.text = "[u]Faction[/u]: Coder"
                if globals.amtbad == 2:
                    amthackers = "two"
                else:
                    amthackers = "three"
                tempdialog.ids.identitydes.text = f"[u]Objective[/u]: Find the {amthackers} hackers among the players and distrust them, while indentifying and trusting other coders."
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