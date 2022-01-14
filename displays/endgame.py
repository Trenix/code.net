from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from displays.dialogcode import RematchDialog
import globals


class EndGame(MDScreen):
    from systems.openinformation import openinfo

    def setresults(self):
        print(globals.playeractions)
    # Adds icons for alignment reveal.
        self.manager.get_screen("endgame").ids.hackers.text += "".join(
            map(lambda x:
                f"[color={globals.colordefs[globals.playerlist[x]['color']]}][size=22sp][font=Icons]"
                f"{md_icons['account']}[/font][/size][/color]", globals.hackerlist
                )
        )

        self.manager.get_screen("endgame").ids.coders.text += "".join(
            map(lambda x:
                f"[color={globals.colordefs[globals.playerlist[x]['color']]}][size=22sp][font=Icons]{md_icons['account']}[/font][/size][/color]", globals.coderlist
                )
        )

    # Adds text for alignment reveal
        self.manager.get_screen("endgame").ids.hackers.text += " " + ", ".join(
            map(lambda x: globals.playerlist[x]['color'], globals.hackerlist)) + "."

        self.manager.get_screen("endgame").ids.coders.text += " " + ", ".join(
            map(lambda x: globals.playerlist[x]['color'], globals.coderlist)) + "."

    # Reavel target
        self.manager.get_screen("endgame").ids.thetarget.text +=\
            f"[size=22sp][color={globals.colordefs[globals.playerlist[globals.target[0]]['color']]}]" \
            f"[font=Icons]{md_icons['account']}[/font][/color][/size] {globals.playerlist[globals.target[0]]['color']}"

    # Reveals actions
        for num in range(4):
            self.manager.get_screen("endgame").ids[f'action_{num}'].text =\
            f" [color={globals.colordefs[globals.playerlist[list(globals.playeractions)[num]]['color']]}]" \
            f"{globals.playerlist[list(globals.playeractions)[num]]['color']}[/color] " \
            f"[size=22][color={globals.actionicons[globals.playeractions[list(globals.playeractions)[num]]['Action']]['color']}][font=Icons]{md_icons[globals.actionicons[globals.playeractions[list(globals.playeractions)[num]]['Action']]['icon']]}[/font][/color][/size] [color={globals.playeractions[list(globals.playeractions)[num]]['TargetColor']}]{globals.playeractions[list(globals.playeractions)[num]]['Target']}[/color]"

    def opendialog(self):
        RematchDialog().open()

    def refresh(self):
        self.ids.hackers.text = f" [color=#c62828][size=22sp][font=Icons]{md_icons['shield-bug']}[/font][/size][/color] Hackers: "
        self.ids.coders.text = f" [color=#1565c0][size=22sp][font=Icons]{md_icons['shield-lock']}[/font][/size][/color] Coders: "
        self.ids.thetarget.text = f" [size=22sp][font=Icons]{md_icons['target-account']}[/font][/size] Target: "

        globals.revealtracker = 1
        globals.coderlist.clear()
        globals.hackerlist.clear()
        globals.notai.clear()
        globals.playeractions.clear()