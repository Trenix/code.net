from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from displays.dialogcode import RematchDialog
import globals


class EndGame(MDScreen):
    from systems.openinformation import openinfo

    def setresults(self):

        for x in globals.hackerlist:
            self.manager.get_screen("endgame").ids.hackers.text += f"[color={globals.colordefs[globals.playerlist[x]['color']]}][size=25sp][font=Icons]{md_icons['account']}[/font][/size][/color]"

        for x in globals.coderlist:
            self.manager.get_screen("endgame").ids.coders.text += f"[color={globals.colordefs[globals.playerlist[x]['color']]}][size=25sp][font=Icons]{md_icons['account']}[/font][/size][/color]"

        for num in range(4):
            self.manager.get_screen("endgame").ids[f'action_{num}'].text =\
            f" [color={globals.colordefs[globals.playerlist[list(globals.playeractions)[num]]['color']]}]" \
            f"{globals.playerlist[list(globals.playeractions)[num]]['color']}[/color] " \
            f"[color={globals.actionicons[globals.playeractions[list(globals.playeractions)[num]]['Action']]['color']}][font=Icons]{md_icons[globals.actionicons[globals.playeractions[list(globals.playeractions)[num]]['Action']]['icon']]}[/font][/color] [color={globals.playeractions[list(globals.playeractions)[num]]['TargetColor']}]{globals.playeractions[list(globals.playeractions)[num]]['Target']}[/color]"

    def opendialog(self):
        RematchDialog().open()

    def refresh(self):
        self.ids.hackers.text = f" [color=#c62828][size=22sp][font=Icons]{md_icons['shield-bug']}[/font][/size][/color] Hackers: "
        self.ids.coders.text = f" [color=#1565c0][size=22sp][font=Icons]{md_icons['shield-lock']}[/font][/size][/color] Coders: "

        globals.coderlist.clear()
        globals.hackerlist.clear()
        globals.notai.clear()