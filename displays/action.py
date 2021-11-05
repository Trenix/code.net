from kivymd.uix.screen import MDScreen
from displays.dialogcode import ActionDialog
from kivymd.uix.button import MDRoundFlatIconButton
from functools import partial
from kivy.utils import get_color_from_hex
from kivy.uix.widget import Widget
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
            globals.playeractions[player] = {"Action": None}

        # Set indicators to color for players that have an action.
        for x in range(4):
            self.ids.mainscreenmanager.get_screen("actionscreen").ids[f'act{x + 1}'].color = globals.colordefs[globals.playerlist[list(globals.playeractions)[x]]["color"]]

        nextplayeraction = globals.playerlist[list(globals.playeractions)[0]]["color"]
        self.ids.mainscreenmanager.get_screen("actionscreen").ids.nextplayer.text = f"It's {nextplayeraction}'s turn."

        # prevent repetition and set actions for players
        tempcoder = random.sample(list(globals.coderactionlist), 4)
        temphacker = random.sample(list(globals.hackeractionlist), 3)
        tempcodertracker = 0
        temphackertracker = 0

        for x in globals.playeractions:
            if globals.playerlist[x]["hacker"]:
                globals.playeractions[x]["Action"] = temphacker[temphackertracker]
                temphackertracker += 1
            else:
                globals.playeractions[x]["Action"] = tempcoder[tempcodertracker]
                tempcodertracker += 1

        globals.nextplayer = 0
        globals.playeractionlist = list(globals.playeractions)

    def beginaction(self):

        tempactiondialog = ActionDialog()
        nextplayeraction = globals.playerlist[globals.playeractionlist[globals.nextplayer]]["color"]
        tempactiondialog.ids.actiontitle.text = f"{nextplayeraction}'s Action"
        tempactiondialog.ids.whataction.text = globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"]

        if globals.nextplayer < 4:

            if globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "Code":
                pass

                tempactiondialog.ids.actiondesc.text = "You will code for the day. No meaningful action will be performed."

                tempbutton = MDRoundFlatIconButton(
                    font_style="Button",
                    theme_text_color="Custom",
                    text="Code",
                    icon="file",
                    line_color=get_color_from_hex("#FFFFFF"),
                    icon_color=get_color_from_hex("#FFFFFF"),
                    text_color=get_color_from_hex("#FFFFFF"),

                    # Below function includes an additional argument, being the button itself.
                    on_release=partial(self.codeaction, tempactiondialog)
                )

                tempactiondialog.ids.addbuttons.add_widget(Widget())
                tempactiondialog.ids.addbuttons.add_widget(tempbutton)
                tempactiondialog.ids.addbuttons.add_widget(Widget())

            # elif globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "Analyze Log":

            # tempactiondialog.ids.actiondesc.text = "Select a log to reveal exactly how many hackers are found within it, during the time you checked it."
            #
            # tempbutton = MDRoundFlatIconButton(
            #     font_style="Button",
            #     theme_text_color="Custom",
            #     text="Code",
            #     text_color=get_color_from_hex("#FFFFFF"),
            #     pos_hint={"center_x": 0.5},
            # )
            #
            # tempbutton.bind(on_release=partial(self.codeaction, tempactiondialog.ids))
            # tempactiondialog.ids.addbuttons.add_widget(tempbutton)

            # elif globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "Encrypt Log":
            #     tempactiondialog.ids.actiondesc.text = "Select a log which prevents hackers from tampering with it."
            #     tempbutton = MDRoundFlatIconButton(
            #         font_style="Button",
            #         theme_text_color="Custom",
            #         text="Code",
            #         text_color=get_color_from_hex("#FFFFFF"),
            #         pos_hint={"center_x": 0.5},
            #     )
            #
            #     tempbutton.bind(on_release=partial(self.codeaction, tempactiondialog.ids))
            #     tempactiondialog.ids.addbuttons.add_widget(tempbutton)
            #
            # elif globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "Analyze Player":
            #     tempactiondialog.ids.actiondesc.text = "Select a player to check their alignment."
            #
            #     tempbutton = MDRoundFlatIconButton(
            #         font_style="Button",
            #         theme_text_color="Custom",
            #         text_color=get_color_from_hex("#FFFFFF"),
            #         text="Code",
            #         pos_hint={"center_x": 0.5},
            #     )
            #
            #     tempbutton.bind(on_release=partial(self.codeaction, tempactiondialog.ids))
            #     tempactiondialog.ids.addbuttons.add_widget(tempbutton)
            #
            # elif globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "Backup Log":
            #     tempactiondialog.ids.actiondesc.text = "Select a log to prevent it from being corrupted."
            #
            #     tempbutton = MDRoundFlatIconButton(
            #         font_style="Button",
            #         theme_text_color="Custom",
            #         text="Code",
            #         text_color=get_color_from_hex("#FFFFFF"),
            #         pos_hint={"center_x": 0.5},
            #     )
            #
            #     tempbutton.bind(on_release=partial(self.codeaction, tempactiondialog.ids))
            #     tempactiondialog.ids.addbuttons.add_widget(tempbutton)
            #
            # elif globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "Hack Digital Footprint":
            #     tempactiondialog.ids.actiondesc.text = "Select a log to replace the digital footprint of a hacker with a coder."
            #
            #     tempbutton = MDRoundFlatIconButton(
            #         font_style="Button",
            #         theme_text_color="Custom",
            #         text="Code",
            #         text_color=get_color_from_hex("#FFFFFF"),
            #         pos_hint={"center_x": 0.5},
            #     )
            #
            #     tempbutton.bind(on_release=partial(self.codeaction, tempactiondialog.ids))
            #     tempactiondialog.ids.addbuttons.add_widget(tempbutton)
            #
            # elif globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "Corrupt Log":
            #     tempactiondialog.ids.actiondesc.text = "Select a log to corrupt it."
            #
            #     tempbutton = MDRoundFlatIconButton(
            #         font_style="Button",
            #         theme_text_color="Custom",
            #         text_color=get_color_from_hex("#FFFFFF"),
            #         text="Code",
            #         pos_hint={"center_x": 0.5},
            #     )
            #
            #     tempbutton.bind(on_release=partial(self.codeaction, tempactiondialog.ids))
            #     tempactiondialog.ids.addbuttons.add_widget(tempbutton)
            #
            # elif globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "Infect Software":
            #     tempactiondialog.ids.actiondesc.text = "If a coder preforms the analyze player or analyze log action, it will provide the wrong results."
            #
            #     tempbutton = MDRoundFlatIconButton(
            #         font_style="Button",
            #         theme_text_color="Custom",
            #         text="Code",
            #         text_color=get_color_from_hex("#FFFFFF"),
            #         pos_hint={"center_x": 0.5},
            #     )
            #
            #     tempbutton.bind(on_release=partial(self.codeaction, tempactiondialog.ids))
            #     tempactiondialog.ids.addbuttons.add_widget(tempbutton)
            #
            # elif globals.playeractions[globals.playeractionlist[globals.nextplayer]]["Action"] == "DDOS Server":
            #     tempactiondialog.ids.actiondesc.text = "A coder will be prevented from preforming their action."
            #
            #     tempbutton = MDRoundFlatIconButton(
            #         font_style="Button",
            #         theme_text_color="Custom",
            #         text="Code",
            #         text_color=get_color_from_hex("#FFFFFF"),
            #         pos_hint={"center_x": 0.5},
            #     )
            #
            #     tempbutton.bind(on_release=partial(self.codeaction, tempactiondialog.ids))
            #     tempactiondialog.ids.addbuttons.add_widget(tempbutton)

        else:
            pass

        tempactiondialog.open()

    def codeaction(self, tempactiondialog, button):

        tempactiondialog.ids.actionresult.text = "Code has been complete."
        button.disabled = True
        tempactiondialog.ids.okaction.disabled = False

    def actiontracker(self):
        globals.nextplayer += 1