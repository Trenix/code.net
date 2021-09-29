from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
import globals


class EndGame(MDScreen):
    from systems.openinformation import openinfo

    def setalignments(self):

        for x in globals.hackerlist:
            self.manager.get_screen("endgame").ids.hackers.text += f"[color={globals.colordefs2[globals.playerlist[x]['color']]}][size=25][font=Icons]{md_icons['account']}[/font][/size][/color]"

        for x in globals.coderlist:
            self.manager.get_screen("endgame").ids.coders.text += f"[color={globals.colordefs2[globals.playerlist[x]['color']]}][size=25][font=Icons]{md_icons['account']}[/font][/size][/color]"
