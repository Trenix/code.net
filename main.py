from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from screens.playerselect import *
from screens.revealscreen import *
from popups.poprev import *
from globals import *
import random

Window.size = (360, 800)

class WelcomeWindow(Screen):
    pass

class MainWindow(Screen):

#Logs per each round.

    def r1l1(self):
        self.ids.startround.disabled = False
        self.ids.round1reveal.disabled = True

        if random.random() < 0.7:

            self.ids.round1sum.text = "At least one hacker is among the following."

            # Log Generation
            if globals.players == 9:
                tempamthacker = random.randint(1, 3)
            else:
                tempamthacker = random.randint(1, 2)

            amtplayerlog = 4
            templog = random.sample(list(globals.coderlist), (amtplayerlog - tempamthacker)) + random.sample(list(globals.hackerlist), tempamthacker)

# May be used, sets players less on log rather than specific amount.
#            templog = sorted(random.sample(list(globals.coderlist), ((globals.players + globals.aiamt) - tempamthacker) - playerslesslog) + random.sample(list(globals.hackerlist), tempamthacker))
#            playerslesslog = 2
#-----------------------------------------------

            tempcolorlog = []

            for x in templog:
                tempcolorlog.append(globals.playerlist[x]["color"])

            tempcolorlog.sort()

            strtemplog = '[b]' + ', '.join(str(x) for x in tempcolorlog) + '[/b]'

            self.ids.round1sub.text = strtemplog + "."
#TODO: Temporarily set to show only color text, need to add colors names with their actual color.


        else:
            self.ids.round1sub.text = "[b]Log Retrieval Failed[/b]"
            self.ids.round1sum.text = "Unfortunately, the log files have been corrupted."

#TODO: Make it so that round 1 will have 4 players always ON LOG, round 2 will have 3 always ON LOG, round 3 will have 2 players always on log.


    def r2l1(self):

        if self.ids.round2reveal2.disabled == True:
            self.ids.startround.disabled = False

        self.ids.round2reveal1.disabled = True

        if random.random() < 0.7:

            self.ids.round2sum1.text = "At least one hacker is among the following."

            # Log Generation
            if globals.players == 9:
                tempamthacker = random.randint(1, 3)
            else:
                tempamthacker = random.randint(1, 2)

            amtplayerlog = 3
            templog = random.sample(list(globals.coderlist), (amtplayerlog - tempamthacker)) + random.sample(list(globals.hackerlist), tempamthacker)

            tempcolorlog = []

            for x in templog:
                tempcolorlog.append(globals.playerlist[x]["color"])

            tempcolorlog.sort()

            strtemplog = '[b]' + ', '.join(str(x) for x in tempcolorlog) + '[/b]'

            self.ids.round2sub1.text = strtemplog + "."

        else:
            self.ids.round2sub1.text = "[b]Log Retrieval Failed[/b]"
            self.ids.round2sum1.text = "Unfortunately, the log files have been corrupted."


    def r2l2(self):

        if self.ids.round2reveal1.disabled == True:
            self.ids.startround.disabled = False

        self.ids.round2reveal2.disabled = True

        if random.random() < 1:

            self.ids.round2sum2.text = "At least one hacker is among the following."

            # Log Generation
            if globals.players == 9:
                tempamthacker = random.randint(1, 3)
            else:
                tempamthacker = random.randint(1, 2)

            amtplayerlog = 3
            templog = random.sample(list(globals.coderlist), (amtplayerlog - tempamthacker)) + random.sample(list(globals.hackerlist), tempamthacker)

            tempcolorlog = []

            for x in templog:
                tempcolorlog.append(globals.playerlist[x]["color"])

            tempcolorlog.sort()

            strtemplog = '[b]' + ', '.join(str(x) for x in tempcolorlog) + '[/b]'

            self.ids.round2sub2.text = strtemplog + "."

        else:
            self.ids.round2sub2.text = "[b]Log Retrieval Failed[/b]"
            self.ids.round2sum2.text = "Unfortunately, the log files have been corrupted."


    def nextround(self):

# Round 1
        if self.ids.currentround.text == "[b]Current Round:[/b] 0":
            self.ids.currentround.text = "[b]Current Round:[/b] 1"
            self.ids.startround.disabled = True
            self.ids.mainpanel.switch_to(self.ids.tab1)


#Tab displays activated
            self.ids.round1reveal.disabled = False
            self.ids.round1show.opacity = 1

# Round 2
        elif self.ids.currentround.text == "[b]Current Round:[/b] 1":
            self.ids.currentround.text = "[b]Current Round:[/b] 2"
            self.ids.startround.disabled = True
            self.ids.mainpanel.switch_to(self.ids.tab2)

#Tab displays activated
            self.ids.round2reveal1.disabled = False
            self.ids.round2reveal2.disabled = False
            self.ids.round2show.opacity = 1

# Round 3
        else:
            self.ids.currentround.text = "[b]Current Round:[/b] 3"
            self.ids.startround.disabled = True
            self.ids.mainpanel.switch_to(self.ids.tab3)

#Tab displays activated
            self.ids.round3reveal1.disabled = False
            self.ids.round3reveal2.disabled = False
            self.ids.round3show.opacity = 1


# ----- This has to go to round 3, where logs are not revealed
#            if globals.players < 5:
#                revealplayer = random.sample(list(globals.notai), 1)
#            else:
#                revealplayer = random.sample(list(globals.playerlist.keys()), 1)
#
#            for x in revealplayer:
#                self.ids.round1player.text = f"{globals.playerlist[x]['color']}'s Log"
# ------ This has to go to round 3, where logs are not revealed


class WindowManager(ScreenManager):
    pass

class MyApp(App):

#Global Variables Between KV and PY

    arehacker = StringProperty("")
    buttonname = StringProperty("")

    def build(self):
        pass

if __name__ == "__main__":
    MyApp().run()