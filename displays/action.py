from kivymd.uix.screen import MDScreen
from displays.dialogcode import ActionDialog
from functools import partial
from kivy.utils import get_color_from_hex
from main import MDApp
from kivymd.icon_definitions import md_icons
import globals
import random

class ActionScreen(MDScreen):
    from systems.preformactions import codeaction
    from systems.preformactions import analyzelog
    from systems.preformactions import disablewidgets
    from systems.preformactions import analyzeplayer
    from systems.preformactions import backuplog
    from systems.preformactions import hacklog
    from systems.preformactions import corruptlog
    from systems.preformactions import hackplayer

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
            globals.playeractions[player] = {"Target": None}
            globals.playeractions[player] = {"TargetColor": None}

        # Set indicators to color for players that have an action.
        for x in range(4):
            self.ids.mainscreenmanager.get_screen("actionscreen").ids[f'act{x + 1}'].color = globals.colordefs[globals.playerlist[list(globals.playeractions)[x]]["color"]]

        self.ids.mainscreenmanager.get_screen("actionscreen").ids.nextplayer.text = f"It's {globals.playerlist[list(globals.playeractions)[0]]['color']}'s turn."

        # prevent repetition and set actions for players
        tempcoder = random.sample(globals.coderactionlist, 4)
        temphacker = random.sample(globals.hackeractionlist, 3)
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

    def beginaction(self):

        tempactiondialog = ActionDialog()
        playeractionlist = list(globals.playeractions)
        nextplayeraction = globals.playerlist[playeractionlist[globals.nextplayer]]["color"]

        tempactiondialog.ids.actioncard.md_bg_color = get_color_from_hex(globals.colordefs[nextplayeraction])
        tempactiondialog.ids.whatplayer.text = f"{nextplayeraction}'s Action"
        tempactiondialog.ids.whataction.text += f"{globals.playeractions[playeractionlist[globals.nextplayer]]['Action']}"

        # If action is hacker or coder action, they will get the correct icon.
        if globals.playeractions[playeractionlist[globals.nextplayer]]["Action"] in globals.coderactionlist:
            tempactiondialog.ids.whaticon.text_color = get_color_from_hex(globals.colordefs['Blue'])

        else:
            tempactiondialog.ids.whaticon.text_color = get_color_from_hex(globals.colordefs['Red'])

        # Every player must press a button to preform an action to prevent cheating.
        if globals.playeractions[playeractionlist[globals.nextplayer]]["Action"] == "Code":

            tempactiondialog.ids.whaticon.icon = globals.actionicons['Code']['icon']
            tempactiondialog.ids.actiondesc.text += "Select code to put your digital footprint on all the logs."
            tempactiondialog.ids.whatpriority.text += f"[color={globals.colordefs['Green']}][size=22sp][font=Icons]{md_icons['chevron-triple-up']}[/font][/size][/color] High"

            tempactiondialog.ids.addbuttons.data = [
                {
                    'theme_text_color': 'Custom',
                    'text_color': get_color_from_hex("#FFFFFF"),
                    "text": f"[size=22sp][font=Icons]{md_icons[globals.actionicons['Code']['icon']]}[/font][/size][b][size=14sp] CODE[/b]",
                    "line_color": get_color_from_hex("#FFFFFF"),
                    "on_release": partial(self.codeaction, tempactiondialog)
                }
            ]

        elif globals.playeractions[playeractionlist[globals.nextplayer]]["Action"] == "Analyze Log":

            tempactiondialog.ids.whaticon.icon = 'folder-search'
            tempactiondialog.ids.actiondesc.text += "Select a log to reveal exactly how many hackers are found within it during the time you have checked it."
            tempactiondialog.ids.whatpriority.text += f"[color={globals.colordefs['Green']}][size=22sp][font=Icons]{md_icons['chevron-triple-up']}[/font][/size][/color] High"

            tempactiondialog.ids.addbuttons.data = [
                {
                    'theme_text_color': 'Custom',
                    'text_color': get_color_from_hex("#FFFFFF"),
                    "text": f"[size=22sp][font=Icons]{md_icons['folder']}[/font][/size][b][size=14sp] " + globals.logbuttonword[num].upper() + "[/size][/b]",
                    "line_color": get_color_from_hex("#FFFFFF"),
                    "on_release": partial(self.analyzelog, tempactiondialog, num)
                } for num in range(1, 4)
            ]

        elif globals.playeractions[playeractionlist[globals.nextplayer]]["Action"] == "Analyze Player":

            tempactiondialog.ids.whaticon.icon = 'account-search'
            tempactiondialog.ids.actiondesc.text += "Select a player to reveal their alignment."
            tempactiondialog.ids.whatpriority.text += f"[color={globals.colordefs['Green']}][size=22sp][font=Icons]{md_icons['chevron-triple-up']}[/font][/size][/color] High"

            # Cannot analyze AI or yourself.
            templist = list(filter(
                lambda player: player != "AI" and player != playeractionlist[globals.nextplayer], globals.playerlist)
            )

            tempactiondialog.ids.addbuttons.data = [
                {
                    'theme_text_color': 'Custom',
                    'text_color': get_color_from_hex("#FFFFFF"),
                    "text": f"[size=22sp][color={globals.colordefs[globals.playerlist[player]['color']]}][font=Icons]{md_icons['account']}[/font][/color][/size][b][size=14sp] " + globals.playerlist[player]['color'].upper() + '[/size][/b]',
                    "line_color": get_color_from_hex("#FFFFFF"),
                    "on_release": partial(self.analyzeplayer, tempactiondialog, player)
                } for player in templist
            ]

        elif globals.playeractions[playeractionlist[globals.nextplayer]]["Action"] == "Backup Log":

            tempactiondialog.ids.whaticon.icon = 'folder-download'
            tempactiondialog.ids.actiondesc.text += "Select a log to prevent it from being corrupted."
            tempactiondialog.ids.whatpriority.text += f"[color={globals.colordefs['Green']}][size=22sp][font=Icons]{md_icons['chevron-triple-up']}[/font][/size][/color] High"

            tempactiondialog.ids.addbuttons.data = [
                {
                    'theme_text_color': 'Custom',
                    'text_color': get_color_from_hex("#FFFFFF"),
                    "text": f"[size=22sp][font=Icons]{md_icons['folder']}[/font][/size][b][size=14sp] " +
                            globals.logbuttonword[num].upper() + "[/size][/b]",
                    "line_color": get_color_from_hex("#FFFFFF"),
                    "on_release": partial(self.backuplog, tempactiondialog, num)
                } for num in range(1, 4)
            ]

        elif globals.playeractions[playeractionlist[globals.nextplayer]]["Action"] == "Hack Log":

            tempactiondialog.ids.whaticon.icon = 'folder-network'
            tempactiondialog.ids.actiondesc.text += "Select a log to replace the digital footprint of one hacker with a coder."
            tempactiondialog.ids.whatpriority.text += f"[color={globals.colordefs['Red']}][size=22sp][font=Icons]{md_icons['chevron-up']}[/font][/size][/color] Low"

            tempactiondialog.ids.addbuttons.data = [
                {
                    'theme_text_color': 'Custom',
                    'text_color': get_color_from_hex("#FFFFFF"),
                    "text": f"[size=22sp][font=Icons]{md_icons['folder']}[/font][/size][b][size=14sp] " +
                            globals.logbuttonword[num].upper() + "[/size][/b]",
                    "line_color": get_color_from_hex("#FFFFFF"),
                    "on_release": partial(self.hacklog, tempactiondialog, num)
                } for num in range(1, 4)
            ]

        elif globals.playeractions[playeractionlist[globals.nextplayer]]["Action"] == "Corrupt Log":

            tempactiondialog.ids.whaticon.icon = 'folder-remove'
            tempactiondialog.ids.actiondesc.text += "Select a log in an attempt to corrupt it."
            tempactiondialog.ids.whatpriority.text += f"[color={globals.colordefs['Red']}][size=22sp][font=Icons]{md_icons['chevron-up']}[/font][/size][/color] Low"

            tempactiondialog.ids.addbuttons.data = [
                {
                    'theme_text_color': 'Custom',
                    'text_color': get_color_from_hex("#FFFFFF"),
                    "text": f"[size=22sp][font=Icons]{md_icons['folder']}[/font][/size][b][size=14sp] " +
                            globals.logbuttonword[num].upper() + "[/size][/b]",
                    "line_color": get_color_from_hex("#FFFFFF"),
                    "on_release": partial(self.corruptlog, tempactiondialog, num)
                } for num in range(1, 4)
            ]

        elif globals.playeractions[playeractionlist[globals.nextplayer]]["Action"] == "Hack Player":

            tempactiondialog.ids.whaticon.icon = 'account-network'
            tempactiondialog.ids.actiondesc.text += "Select a player to hack to reveal their action."
            tempactiondialog.ids.whatpriority.text += f"[color={globals.colordefs['Green']}][size=22sp][font=Icons]{md_icons['chevron-triple-up']}[/font][/size][/color] High"

            # Create list that includes players with actions, but not hackers or AI
            templist = list(
                filter(
                lambda player: player != "AI" and player not in globals.hackerlist, globals.playeractions
                )
            )

            tempactiondialog.ids.addbuttons.data = [
                {
                    'theme_text_color': 'Custom',
                    'text_color': get_color_from_hex("#FFFFFF"),
                    "text": f"[size=22sp][color={globals.colordefs[globals.playerlist[player]['color']]}][font=Icons]{md_icons['account']}[/font][/color][/size][b][size=14sp] " + globals.playerlist[player]['color'].upper() + '[/size][/b]',
                    "line_color": get_color_from_hex("#FFFFFF"),
                    "on_release": partial(self.hackplayer, tempactiondialog, player)
                } for player in templist
            ]

        tempactiondialog.open()

    def actiontracker(self):

        if globals.nextplayer < 4 - 1:
            self.ids[f'act{globals.nextplayer + 1}'].icon = "circle-outline"
            globals.nextplayer += 1
            self.ids[f'act{globals.nextplayer + 1}'].icon = "circle-slice-8"
            self.ids.nextplayer.text = f"It's {globals.playerlist[list(globals.playeractions)[globals.nextplayer]]['color']}'s turn."

        else:
            self.ids.useaction.disabled = True
            self.ids[f'act{globals.nextplayer + 1}'].icon = "circle-outline"
            self.ids.nextplayer.text = "Pass the phone to the host."
            MDApp.get_running_app().root.get_screen("main").ids.roundregulator.icon = "check"