from kivymd.uix.screen import MDScreen
from main import IdentityDialog
from kivymd.icon_definitions import md_icons
import globals

class PlayerReveal(MDScreen):

    def reveal(self):

        if globals.revealtracker <= globals.players:
            playercolor = globals.playerlist[f"player {globals.revealtracker}"]["color"]

            if self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == True and globals.revealtracker <= globals.players:
                ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
                if globals.players <= 8:
                    tempdialog = IdentityDialog()
                    tempdialog.ids.whatcolor.text = f"[font=Icons]{md_icons['brush']}[/font]" + " [u]Color[/u]: " + playercolor
                    tempdialog.ids.arehacker.text = f"[font=Icons]{md_icons['emoticon-devil']}[/font]" + " [u]Faction[/u]: Hacker"
                    tempdialog.ids.haveallies.text = f"[font=Icons]{md_icons['emoticon-wink']}[/font]" + " [u]Ally[/u]: " + globals.playerlist[ally]["color"]
                    tempdialog.ids.identitydes.text = f"[font=Icons]{md_icons['script']}[/font]" + " [u]Objective[/u]: Keep your identity hidden and have the coders trust you and your ally while making them distrust each other."
                    tempdialog.open()
                else:
                    tempdialog = IdentityDialog()
                    tempdialog.ids.whatcolor.text = f"[font=Icons]{md_icons['brush']}[/font]" + " [u]Color[/u]: " + playercolor
                    tempdialog.ids.arehacker.text = f"[font=Icons]{md_icons['emoticon-devil']}[/font]" + " [u]Faction[/u]: Hacker"
                    tempdialog.ids.haveallies.text = f"[font=Icons]{md_icons['emoticon-wink']}[/font]" + " [u]Ally[/u]: " + globals.playerlist[ally[0]]["color"] + ", " + globals.playerlist[ally[1]]["color"]
                    tempdialog.ids.identitydes.text = f"[font=Icons]{md_icons['script']}[/font]" + " [u]Objective[/u]: Keep your identity hidden and have the coders trust you and your allies while making them distrust each other."
                    tempdialog.open()

            elif self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == False and globals.revealtracker <= globals.players:
                tempdialog = IdentityDialog()
                tempdialog.ids.identity.remove_widget(tempdialog.ids.haveallies)
                tempdialog.ids.whatcolor.text = f"[font=Icons]{md_icons['brush']}[/font]" + " [u]Color[/u]: " + playercolor
                tempdialog.ids.arehacker.text = f"[font=Icons]{md_icons['emoticon']}[/font]" + " [u]Faction[/u]: Coder"
                if globals.amtbad == 2:
                    amthackers = "two"
                else:
                    amthackers = "three"
                tempdialog.ids.identitydes.text = f"[font=Icons]{md_icons['script']}[/font]" + f" [u]Objective[/u]: Find the {amthackers} hackers among the team and distrust them, while indentifying and trusting other coders."
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