from kivymd.uix.screen import MDScreen
from popups.poprev import RevealPopup
from main import MDApp
# from kivymd.icon_definitions import md_icons
import globals

class PlayerReveal(MDScreen):

    def reveal(self):

        if self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == True and globals.revealtracker <= globals.players:
            ally = globals.playerlist[f"player {globals.revealtracker}"]["allies"]
            if globals.players <= 8:
                MDApp.get_running_app().arehacker = "[u]Faction[/u]: Hacker\n[u]Ally[/u]: " + globals.playerlist[ally]["color"]
                MDApp.get_running_app().identitydes = "[u]Objective[/u]: Keep your identity hidden and have the coders trust you and your ally while making them distrust each other."
                RevealPopup().open()
            else:
                MDApp.get_running_app().arehacker = f"Player {globals.revealtracker}, you are a hacker and your\nallies are {ally[0]} and {ally[1]}."
                RevealPopup().open()


        elif self.ids[f"ind{globals.revealtracker}"].icon == "circle-slice-8" and globals.playerlist[f"player {globals.revealtracker}"]["hacker"] == False and globals.revealtracker <= globals.players:
            MDApp.get_running_app().arehacker = "[u]Faction[/u]: Coder"
            MDApp.get_running_app().identitydes = f"[u]Objective[/u]: Find the {globals.amtbad} hackers among the team and distrust them, while indentifying and trusting other coders."
            RevealPopup().open()

        if globals.revealtracker < globals.players:
            self.ids[f"ind{globals.revealtracker}"].icon = "circle-outline"
            globals.revealtracker += 1
            self.ids[f"ind{globals.revealtracker}"].icon = "circle-slice-8"

            # self.ids.whatplayer.text = f"Pass the phone to Player {globals.playercounter}."
        #
        # elif globals.playercounter == globals.players:
        #     globals.playercounter += 1
        #     self.ids.whatplayer.text = "Now that all players know their roles, place your device in the middle of everyone."
        #     self.ids.endreveal.text = "Next"
        #
        # else:
        #     self.manager.current = "main"