from kivymd.uix.screen import MDScreen
from displays.dialogcode import ActionDialog
import globals
import random

class ActionScreen(MDScreen):

    def setactionplayers(self):

        # Collect players randomly that will have actions and then sort them
        templist = []

        if globals.players <= 5:
            for player in random.sample(list(globals.notai), 4):
                templist.append(player)
        else:
            for player in random.sample(list(globals.playerlist), 4):
                templist.append(player)

        templist.sort()

        for player in templist:
            globals.playeractionlist[player] = {"Action": None}

        for x in range(4):
            self.ids.mainscreenmanager.get_screen("actionscreen").ids[f'act{x + 1}'].color = globals.colordefs[globals.playerlist[list(globals.playeractionlist)[x]]["color"]]

        nextplayeraction = globals.playerlist[list(globals.playeractionlist)[0]]["color"]
        self.ids.mainscreenmanager.get_screen("actionscreen").ids.nextplayer.text = f"It's {nextplayeraction}'s turn."

        # prevent repetition
        tempcoder = random.sample(list(globals.coderactionlist), 4)
        temphacker = random.sample(list(globals.hackeractionlist), 3)
        tempcodertracker = 0
        temphackertracker = 0

        for x in globals.playeractionlist:
            if globals.playerlist[x]["hacker"]:
                globals.playeractionlist[x]["Action"] = temphacker[temphackertracker]
                temphackertracker += 1
            else:
                globals.playeractionlist[x]["Action"] = tempcoder[tempcodertracker]
                tempcodertracker += 1

        globals.nextplayer = 0

    def beginaction(self):

        tempactiondialog = ActionDialog()
        nextplayeraction = globals.playerlist[list(globals.playeractionlist)[0]]["color"]
        tempactiondialog.ids.actiontitle.text = f"{nextplayeraction}'s Action"
        tempactiondialog.ids.whataction.text = globals.playeractionlist[globals.nextplayer]

        if globals.nextplayer < 4:

            self.ids.whataction.text = globals.playeractionlist[globals.nextplayer]["Action"]

            if globals.playeractionlist[globals.nextplayer]["Code"]:
                self.ids.actiondesc.text = "You code for the day. No meaningful action is performed."

            elif globals.playeractionlist[globals.nextplayer]["Analyze Log"]:
                self.ids.actiondesc.text = "Select a log to reveal exactly how many hackers are found within it, during the time you checked it."

            elif globals.playeractionlist[globals.nextplayer]["Encrypt Log"]:
                self.ids.actiondesc.text = "Select a log which prevents hackers from tampering with it."

            elif globals.playeractionlist[globals.nextplayer]["Analyze Player"]:
                self.ids.actiondesc.text = "Select a player to check their alignment."

            elif globals.playeractionlist[globals.nextplayer]["Backup Log"]:
                self.ids.actiondesc.text = "Select a log to prevent it from being corrupted."

            elif globals.playeractionlist[globals.nextplayer]["Hack Digital Footprint"]:
                self.ids.actiondesc.text = "Select a log to replace the digital footprint of a hacker with a coder."

            elif globals.playeractionlist[globals.nextplayer]["Corrupt Log"]:
                self.ids.actiondesc.text = "Select a log to corrupt it."

            elif globals.playeractionlist[globals.nextplayer]["Infect Software"]:
                self.ids.actiondesc.text = "If a coder uses an analyze player action, it will malfunction and will provide the wrong results."

            elif globals.playeractionlist[globals.nextplayer]["DDOS Server"]:
                self.ids.actiondesc.text = "A coder will be prevented from preforming their action."

        else:
            pass

        tempactiondialog.open()

    def actiontracker(self):
        globals.nextplayer += 1