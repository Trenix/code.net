from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
import globals

class PlayerWindow(MDScreen):
    from systems.generatelists import playersetup
    from systems.openinformation import openinfo

    def selectcheck(self, instance):
        if instance.state == 'down':
            self.ids.bottomplayertoolbar.right_action_items = [["chevron-right", lambda x: self.setplayervars()]]
        else:
            self.ids.bottomplayertoolbar.right_action_items = []

    def setplayervars(self):

        # 4 players
        if self.ids.butt1.state == "down":
            globals.amtbad = 2
            globals.players = 4
            globals.aiamt = 1
            self.manager.get_screen("main").ids.playeridentifer.text = f"[size=22][font=Icons]{md_icons['account-circle']}{md_icons['numeric-1-circle']}[color=#2e7d32]{md_icons['account-supervisor-circle']}{md_icons['numeric-4-circle']}[/color][/font]"

            self.manager.get_screen("main").ids.alignmentidentifer.text = f"[size=22][font=Icons][color=#c62828]{md_icons['shield-bug']}{md_icons['numeric-2-circle']}[/color][color=#1565c0]{md_icons['shield-lock']}{md_icons['numeric-3-circle']}[/color][/font]"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 5 players
        elif self.ids.butt2.state == "down":
            globals.amtbad = 2
            globals.players = 5
            globals.aiamt = 1

            self.manager.get_screen("main").ids.playeridentifer.text = f"[size=22][font=Icons]{md_icons['account-circle']}{md_icons['numeric-1-circle']}[color=#2e7d32]{md_icons['account-supervisor-circle']}{md_icons['numeric-5-circle']}[/color][/font]"

            self.manager.get_screen("main").ids.alignmentidentifer.text = f"[size=22][font=Icons][color=#c62828]{md_icons['shield-bug']}{md_icons['numeric-2-circle']}[/color][color=#1565c0]{md_icons['shield-lock']}{md_icons['numeric-4-circle']}[/color][/font]"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 6 players
        elif self.ids.butt3.state == "down":
            globals.amtbad = 2
            globals.players = 6
            globals.aiamt = 0
            self.manager.get_screen("main").ids.playeridentifer.text = f"[size=22][font=Icons]{md_icons['account-circle']}{md_icons['numeric-0-circle']}[color=#2e7d32]{md_icons['account-supervisor-circle']}{md_icons['numeric-6-circle']}[/color][/font]"

            self.manager.get_screen("main").ids.alignmentidentifer.text = f"[size=22][font=Icons][color=#c62828]{md_icons['shield-bug']}{md_icons['numeric-2-circle']}[/color][color=#1565c0]{md_icons['shield-lock']}{md_icons['numeric-4-circle']}[/color][/font]"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 7 players
        elif self.ids.butt4.state == "down":
            globals.amtbad = 2
            globals.players = 7
            globals.aiamt = 0
            self.manager.get_screen("main").ids.playeridentifer.text = f"[size=22][font=Icons]{md_icons['account-circle']}{md_icons['numeric-0-circle']}[color=#2e7d32]{md_icons['account-supervisor-circle']}{md_icons['numeric-7-circle']}[/color][/font]"

            self.manager.get_screen("main").ids.alignmentidentifer.text = f"[size=22][font=Icons][color=#c62828]{md_icons['shield-bug']}{md_icons['numeric-2-circle']}[/color][color=#1565c0]{md_icons['shield-lock']}{md_icons['numeric-5-circle']}[/color][/font]"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 8 players
        elif self.ids.butt5.state == "down":
            globals.amtbad = 2
            globals.players = 8
            globals.aiamt = 0
            self.manager.get_screen("main").ids.playeridentifer.text = f"[size=22][font=Icons]{md_icons['account-circle']}{md_icons['numeric-0-circle']}[color=#2e7d32]{md_icons['account-supervisor-circle']}{md_icons['numeric-8-circle']}[/color][/font]"

            self.manager.get_screen("main").ids.alignmentidentifer.text = f"[size=22][font=Icons][color=#c62828]{md_icons['shield-bug']}{md_icons['numeric-2-circle']}[/color][color=#1565c0]{md_icons['shield-lock']}{md_icons['numeric-6-circle']}[/color][/font]"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 9 players
        elif self.ids.butt6.state == "down":
            globals.amtbad = 3
            globals.players = 9
            globals.aiamt = 0

            self.manager.get_screen("main").ids.playeridentifer.text = f"[size=22][font=Icons]{md_icons['account-circle']}{md_icons['numeric-0-circle']}[color=#2e7d32]{md_icons['account-supervisor-circle']}{md_icons['numeric-9-circle']}[/color][/font]"

            self.manager.get_screen("main").ids.alignmentidentifer.text = f"[size=22][font=Icons][color=#c62828]{md_icons['shield-bug']}{md_icons['numeric-3-circle']}[/color][color=#1565c0]{md_icons['shield-lock']}{md_icons['numeric-6-circle']}[/color][/font]"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

    def previousscreen(self):

        self.manager.current = "welcome"
        self.manager.transition.direction = "right"

    def nextscreen(self):

        self.manager.current = "colorselect"
        self.manager.transition.direction = "left"

        self.playersetup()

# Set grid for next screen
        for x in range(9):
            self.manager.get_screen("colorselect").ids[f"but{x + 1}"].size_hint = 1, 1