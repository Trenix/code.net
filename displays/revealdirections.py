from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from main import IdentityDialog
from kivy.utils import get_color_from_hex
import globals

class PlayerReveal(MDScreen):
    from systems.openinformation import openinfo

    def reveal(self):

        if globals.revealtracker <= globals.players:
            playercolor = globals.playerlist[f"player {globals.revealtracker}"]["color"]
            tempdialog = IdentityDialog()
            tempdialog.ids.identitycard.md_bg_color = get_color_from_hex(globals.colordefs[playercolor])

            if self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == True and globals.revealtracker <= globals.players:

                tempdialog.ids.whatcolor.text = "[u]Color[/u]: " + f"[size=22sp][color={globals.colordefs[playercolor]}][font=Icons]{md_icons['account']}[/font][/color][/size] " + playercolor
                tempdialog.ids.arehacker.text = "[u]Alignment[/u]: " + f"[size=22sp][color={globals.colordefs['Red']}][font=Icons]{md_icons['shield-bug']}[/font][/color][/size] " + "Hacker"
                tempdialog.ids.whattarget.text += f"[size=22sp][color={globals.colordefs[globals.playerlist[globals.target[0]]['color']]}][font=Icons]{md_icons['target-account']}[/font][/color][/size] {globals.playerlist[globals.target[0]]['color']}"
                tempdialog.ids.identitydes.text = "[u]Objective[/u]: Keep your alignment and it's members hidden. Work with your alignment to gain the trust of coders and have them distrust each other. Gain extra points by having coders acuse the target as a hacker."

                if globals.players <= 8:
                    ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
                    allycolor = globals.playerlist[ally]['color']

                    tempdialog.ids.haveallies.text = "[u]Ally[/u]: " + f"[size=22sp][color={globals.colordefs[allycolor]}][font=Icons]{md_icons['account-plus']}[/font][/color][/size] " + globals.playerlist[ally]["color"]

                else:
                    ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
                    allycolor1 = globals.playerlist[ally[0]]['color']
                    allycolor2 = globals.playerlist[ally[1]]['color']

                    tempdialog.ids.haveallies.text = "[u]Allies[/u]: " + f"[size=22sp][color={globals.colordefs[allycolor1]}][font=Icons]{md_icons['account-plus']}[/font][/color][/size] " + allycolor1 + ", " + f"[size=22sp][color={globals.colordefs[allycolor2]}][font=Icons]{md_icons['account-plus']}[/font][/color][/size] " + allycolor2

            elif self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == False and globals.revealtracker <= globals.players:

                tempdialog.ids.identity.remove_widget(tempdialog.ids.haveallies)
                tempdialog.ids.identity.remove_widget(tempdialog.ids.whattarget)
                tempdialog.ids.whatcolor.text = "[u]Color[/u]: " + f"[size=22sp][color={globals.colordefs[playercolor]}][font=Icons]{md_icons['account']}[/font][/color][/size] " + playercolor
                tempdialog.ids.arehacker.text = "[u]Alignment[/u]: " + f"[size=22sp][color={globals.colordefs['Blue']}][font=Icons]{md_icons['shield-lock']}[/font][/color][/size] " + "Coder"
                tempdialog.ids.identitydes.text = f"[u]Objective[/u]: Identify other coders and work together to discover the {globals.numbertoword[globals.amtbad]} hackers among the players."

            tempdialog.open()

    def trackplayer(self):

        if globals.revealtracker < globals.players:
            self.ids.nextplayer.text = "It's " + globals.playerlist[f"player {globals.revealtracker + 1}"]["color"] + "'s turn!"
            self.ids[f"ind{globals.revealtracker}"].icon = "circle-outline"
            globals.revealtracker += 1
            self.ids[f"ind{globals.revealtracker}"].icon = "circle-slice-8"

        elif globals.revealtracker == globals.players:
            self.ids.nextplayer.text = "Pass the phone to the host."
            self.ids[f"ind{globals.revealtracker}"].icon = "circle-outline"
            globals.revealtracker += 1
            self.ids.revtool.icon = "square-rounded-outline"
            self.ids.revtool.right_action_items = [["chevron-right", lambda x: self.nextscreen()]]

    def nextscreen(self):
        if globals.revealtracker > globals.players:
            self.manager.transition.direction = "left"
            self.manager.current = "main"

        # Reset code for new game if it occurs.
        self.manager.get_screen("reveal").ids['ind1'].icon = "circle-slice-8"

        for x in range(globals.players + 1, 10):
            self.manager.get_screen("reveal").ids[f"ind{x}"].icon = 'circle-outline'
            self.manager.get_screen("reveal").ids[f"ind{x}"].parent.size_hint = 1, 1

        self.ids.revtool.right_action_items = []
        self.ids.revtool.icon = "card-account-details"
        globals.revealtracker = 1

    def rematchreset(self):
        # Set up tracker for revealing
        for x in range(globals.players):
            self.ids[f"ind{x + 1}"].color = globals.colordefs[
                globals.playerlist[f"player {x + 1}"]["color"]]

        for x in range(globals.players + 1, 9 + 1):
            self.ids[f"ind{x}"].icon = ''