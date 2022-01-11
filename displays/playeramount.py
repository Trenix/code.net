from kivymd.uix.screen import MDScreen
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

            self.manager.get_screen("main").ids.hacker_identifer.badge_icon = "numeric-2-circle-outline"
            self.manager.get_screen("main").ids.coder_identifer.badge_icon = "numeric-3-circle-outline"
            self.manager.get_screen("main").ids.ai_identifer.badge_icon = "numeric-1-circle-outline"
            self.manager.get_screen("main").ids.player_identifer.badge_icon = "numeric-4-circle-outline"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 5 players
        elif self.ids.butt2.state == "down":
            globals.amtbad = 2
            globals.players = 5
            globals.aiamt = 1

            self.manager.get_screen("main").ids.hacker_identifer.badge_icon = "numeric-2-circle-outline"
            self.manager.get_screen("main").ids.coder_identifer.badge_icon = "numeric-4-circle-outline"
            self.manager.get_screen("main").ids.ai_identifer.badge_icon = "numeric-1-circle-outline"
            self.manager.get_screen("main").ids.player_identifer.badge_icon = "numeric-5-circle-outline"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 6 players
        elif self.ids.butt3.state == "down":
            globals.amtbad = 2
            globals.players = 6
            globals.aiamt = 0

            self.manager.get_screen("main").ids.hacker_identifer.badge_icon = "numeric-2-circle-outline"
            self.manager.get_screen("main").ids.coder_identifer.badge_icon = "numeric-4-circle-outline"
            self.manager.get_screen("main").ids.ai_identifer.badge_icon = "numeric-0-circle-outline"
            self.manager.get_screen("main").ids.player_identifer.badge_icon = "numeric-6-circle-outline"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 7 players
        elif self.ids.butt4.state == "down":
            globals.amtbad = 2
            globals.players = 7
            globals.aiamt = 0

            self.manager.get_screen("main").ids.hacker_identifer.badge_icon = "numeric-2-circle-outline"
            self.manager.get_screen("main").ids.coder_identifer.badge_icon = "numeric-5-circle-outline"
            self.manager.get_screen("main").ids.ai_identifer.badge_icon = "numeric-0-circle-outline"
            self.manager.get_screen("main").ids.player_identifer.badge_icon = "numeric-7-circle-outline"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 8 players
        elif self.ids.butt5.state == "down":
            globals.amtbad = 2
            globals.players = 8
            globals.aiamt = 0

            self.manager.get_screen("main").ids.hacker_identifer.badge_icon = "numeric-2-circle-outline"
            self.manager.get_screen("main").ids.coder_identifer.badge_icon = "numeric-6-circle-outline"
            self.manager.get_screen("main").ids.ai_identifer.badge_icon = "numeric-0-circle-outline"
            self.manager.get_screen("main").ids.player_identifer.badge_icon = "numeric-8-circle-outline"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

        # 9 players
        elif self.ids.butt6.state == "down":
            globals.amtbad = 3
            globals.players = 9
            globals.aiamt = 0

            self.manager.get_screen("main").ids.hacker_identifer.badge_icon = "numeric-3-circle-outline"
            self.manager.get_screen("main").ids.coder_identifer.badge_icon = "numeric-6-circle-outline"
            self.manager.get_screen("main").ids.ai_identifer.badge_icon = "numeric-0-circle-outline"
            self.manager.get_screen("main").ids.player_identifer.badge_icon = "numeric-9-circle-outline"

            self.manager.get_screen("colorselect").ids.remainder.text = f"Remainder: {globals.players}"

            self.nextscreen()

    def previousscreen(self):

        self.manager.current = "welcome"
        self.manager.transition.direction = "right"

    def nextscreen(self):

        self.manager.current = "colorselect"
        self.manager.transition.direction = "left"

        for x in range(6):
            self.ids[f"butt{x + 1}"].state = "normal"

        self.playersetup()