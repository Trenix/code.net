from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from main import IdentityDialog
import globals

class PlayerReveal(MDScreen):
    from systems.openinformation import openinfo

    def reveal(self):

        if globals.revealtracker <= globals.players:
            playercolor = globals.playerlist[f"player {globals.revealtracker}"]["color"]

            if self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == True and globals.revealtracker <= globals.players:
                tempdialog = IdentityDialog()
                tempdialog.ids.whatcolor.text = "[u]Color[/u]: " + f"[size=22][color={globals.colordefs2[playercolor]}][font=Icons]{md_icons['account']}[/font][/color][/size] " + playercolor
                tempdialog.ids.arehacker.text = "[u]Alignment[/u]: " + f"[size=22][color=#c62828][font=Icons]{md_icons['shield-bug']}[/font][/color][/size] " + "Hacker"
                tempdialog.ids.identitydes.text = "[u]Objective[/u]: Keep your alignment and it's members hidden. Work with your alignment to gain the trust of coders and have them distrust each other."

                if globals.players <= 8:
                    ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
                    allycolor = globals.playerlist[ally]['color']

                    tempdialog.ids.haveallies.text = "[u]Ally[/u]: " + f"[size=22][color={globals.colordefs2[allycolor]}][font=Icons]{md_icons['account-plus']}[/font][/color][/size] " + globals.playerlist[ally]["color"]
                    tempdialog.open()

                else:
                    ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
                    allycolor1 = globals.playerlist[ally[0]]['color']
                    allycolor2 = globals.playerlist[ally[1]]['color']
                    tempdialog.ids.haveallies.text = "[u]Allies[/u]: " + f"[size=22][color={globals.colordefs2[allycolor1]}][font=Icons]{md_icons['account-plus']}[/font][/color][/size] " + allycolor1 + ", " + f"[size=22][color={globals.colordefs2[allycolor2]}][font=Icons]{md_icons['account-plus']}[/font][/color][/size] " + allycolor2
                    tempdialog.open()

            elif self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == False and globals.revealtracker <= globals.players:
                tempdialog = IdentityDialog()
                tempdialog.ids.identity.remove_widget(tempdialog.ids.haveallies)
                tempdialog.ids.whatcolor.text = "[u]Color[/u]: " + f"[size=22][color={globals.colordefs2[playercolor]}][font=Icons]{md_icons['account']}[/font][/color][/size] " + playercolor
                tempdialog.ids.arehacker.text = "[u]Alignment[/u]: " + f"[size=22][color=#1565c0][font=Icons]{md_icons['shield-lock']}[/font][/color][/size] " + "Coder"
                if globals.amtbad == 2:
                    amthackers = "two"
                else:
                    amthackers = "three"
                tempdialog.ids.identitydes.text = f"[u]Objective[/u]: Identify other coders and work together to discover the {amthackers} hackers among the players."
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