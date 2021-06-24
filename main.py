from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from screens.playerselect import *
from screens.revealscreen import *
from popups.poprev import *
from kivymd.uix.screen import MDScreen
from systems.generatelog import *
from systems.generateplayerlog import *
from globals import *
from kivymd.font_definitions import theme_font_styles
from kivy.core.text import LabelBase
from kivy.clock import Clock
import random
import globals

Window.size = (400, 800)

class WelcomeWindow(Screen):
    pass

class MainWindow(Screen):

#Logs per each round.

    def r1l1(self):
        self.ids.startround.disabled = False
        self.ids.round1reveal.disabled = True

        if random.random() < 0.7:

            self.ids.round1sum.text = "At least one hacker is among the following."
            log = createlog(4)
            self.ids.round1sub.text = log + "."

# May be used, sets players less on log rather than specific amount.
#            templog = sorted(random.sample(list(globals.coderlist), ((globals.players + globals.aiamt) - tempamthacker) - playerslesslog) + random.sample(list(globals.hackerlist), tempamthacker))
#            playerslesslog = 2
#-----------------------------------------------

        else:
            self.ids.round1sub.text = "[b]Log Retrieval Failed[/b]"
            self.ids.round1sum.text = "Unfortunately, the log files have been corrupted."

    def r2l1(self):

        if self.ids.round2reveal2.disabled == True:
            self.ids.startround.disabled = False

        self.ids.round2reveal1.disabled = True

        if random.random() < 0.7:

            self.ids.round2sum1.text = "At least one hacker is among the following."
            log = createlog(3)
            self.ids.round2sub1.text = log + "."

        else:
            self.ids.round2sub1.text = "[b]Log Retrieval Failed[/b]"
            self.ids.round2sum1.text = "Unfortunately, the log files have been corrupted."


    def r2l2(self):

        if self.ids.round2reveal1.disabled == True:
            self.ids.startround.disabled = False

        self.ids.round2reveal2.disabled = True

        if random.random() < 0.7:

            self.ids.round2sum2.text = "At least one hacker is among the following."
            log = createlog(3)
            self.ids.round2sub2.text = log + "."

        else:
            self.ids.round2sub2.text = "[b]Log Retrieval Failed[/b]"
            self.ids.round2sum2.text = "Unfortunately, the log files have been corrupted."

    def r3l1(self):
        self.ids.round3reveal1.disabled = True

        LogPopup.title = f"{globals.playerlist[globals.playerlogrev[0]]['color']}'s Log"
        log = createplayerlog()
        temppop = LogPopup()
        temppop.ids.log1sub.text = log + "."
        temppop.open()

    def r3l2(self):
        self.ids.round3reveal2.disabled = True
        LogPopup.title = f"{globals.playerlist[globals.playerlogrev[1]]['color']}'s Log"
        log = createplayerlog()
        temppop = LogPopup()
        temppop.ids.log1sub.text = log + "."
        temppop.open()

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

        if globals.players < 5:
            globals.playerlogrev = random.sample(list(globals.notai), 2)
        else:
            globals.playerlogrev = random.sample(list(globals.playerlist.keys()), 2)

        self.ids.round3reveal1.text = f"{globals.playerlist[globals.playerlogrev[0]]['color']}'s Log"
        self.ids.round3reveal2.text = f"{globals.playerlist[globals.playerlogrev[1]]['color']}'s Log"

class LogPopup(Popup):
    pass

class WindowManager(ScreenManager):
    pass

class LoadingScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.nextscreen, 5)

        LabelBase.register(name="H1", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('H1')
        MDApp.get_running_app().theme_cls.font_styles["H1"] = ["H1", 16, False, 0.15]
        print("works")

    def nextscreen(self, dt):
        self.manager.current = "welcome"


class codenetApp(MDApp):
    import globals
# use import globals not the bottom shit
#Global Variables Between KV and PY

    arehacker = StringProperty("")
    buttonname = StringProperty("")

    def build(self):
# Set Fonts
       # LabelBase.register(name="H1", fn_regular="font/JetBrainsMono-Regular.ttf")

       # theme_font_styles.append('H1')
       # self.theme_cls.font_styles["H1"] = ["H1", 16, False, 0.15]


      #  LabelBase.register(name='Subtitle1', fn_regular="font/JetBrainsMono-Regular.ttf")
      #  theme_font_styles.append('Subtitle1')
      #  self.theme_cls.font_styles['Subtitle1'] = ['JetBrainsMono', 16, False, 0.15]


        print(self.theme_cls.font_styles)
        #self.theme_cls.theme_style = "Dark"

        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Blue"
        pass

if __name__ == "__main__":
    codenetApp().run()