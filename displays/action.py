from kivymd.uix.screen import MDScreen
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

        print(globals.playeractionlist)