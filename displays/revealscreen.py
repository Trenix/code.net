from kivymd.uix.screen import MDScreen
from popups.poprev import RevealPopup
from main import MDApp
import globals


class PlayerReveal(MDScreen):

    def reveal(self):

        if globals.savedpopup == None:
            globals.savedpopup = RevealPopup()

        if self.ids.whatplayer.text == f"Pass the phone to Player {globals.playercounter}." and globals.playerlist[f"player {globals.playercounter}"]["hacker"] == True and globals.playercounter <= globals.players:
            ally = globals.playerlist[f"player {globals.playercounter}"]["allies"]
            if globals.players <= 8:
                MDApp.get_running_app().arehacker = f"Player {globals.playercounter}, you are a [color=#FF0000]hacker[/color] and your\nally is {ally}."
                globals.savedpopup.open()
            else:
                MDApp.get_running_app().arehacker = f"Player {globals.playercounter}, you are a [color=#FF0000]hacker[/color] and your\nallies are {ally[0]} and {ally[1]}."
                globals.savedpopup.open()


        elif self.ids.whatplayer.text == f"Pass the phone to Player {globals.playercounter}." and globals.playerlist[f"player {globals.playercounter}"]["hacker"] == False and globals.playercounter <= globals.players:
            MDApp.get_running_app().arehacker = f"Player {globals.playercounter}, you are a [color=#00FFFF]coder[/color]."
            globals.savedpopup.open()

        if globals.playercounter < globals.players:
            globals.playercounter += 1
            self.ids.whatplayer.text = f"Pass the phone to Player {globals.playercounter}."

        elif globals.playercounter == globals.players:
            globals.playercounter += 1
            self.ids.whatplayer.text = "Now that all players know their roles, place your device in the middle of everyone."
            self.ids.endreveal.text = "Next"

        else:
            self.manager.current = "main"