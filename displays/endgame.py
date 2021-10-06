from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from displays.dialogcode import RematchDialog
import globals


class EndGame(MDScreen):
    from systems.openinformation import openinfo

    def setalignments(self):

        for x in globals.hackerlist:
            self.manager.get_screen("endgame").ids.hackers.text += f"[color={globals.colordefs2[globals.playerlist[x]['color']]}][size=25][font=Icons]{md_icons['account']}[/font][/size][/color]"

        for x in globals.coderlist:
            self.manager.get_screen("endgame").ids.coders.text += f"[color={globals.colordefs2[globals.playerlist[x]['color']]}][size=25][font=Icons]{md_icons['account']}[/font][/size][/color]"

    def opendialog(self):
        RematchDialog().open()

    def refresh(self):
        self.ids.hackers.text = f" [color=#c62828][size=22][font=Icons]{md_icons['shield-bug']}[/font][/size][/color] Hackers: "
        self.ids.coders.text = f" [color=#1565c0][size=22][font=Icons]{md_icons['shield-lock']}[/font][/size][/color] Coders: "

        globals.coderlist.clear()
        globals.hackerlist.clear()
        globals.notai.clear()