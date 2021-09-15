from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.menu import MDDropdownMenu
from kivymd.icon_definitions import md_icons
import globals
from main import MDApp

class LoadingScreen(MDScreen):

    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)

        #Add darker green
        MDApp.get_running_app().theme_cls.colors["Green"]["900"] = "#003300"

        #Set colors to use throughout app
        MDApp.get_running_app().theme_cls.set_colors("Green", "800", "600", "900", "Lime", "600", "100", "900")

        #Set Fonts
        LabelBase.register(name="H1", fn_regular="font/JetBrainsMono-Light.ttf")
        theme_font_styles.append('H1')
        MDApp.get_running_app().theme_cls.font_styles["H1"] = ["H1", 96, False, -1.5]

        LabelBase.register(name="H2", fn_regular="font/JetBrainsMono-Light.ttf")
        theme_font_styles.append('H2')
        MDApp.get_running_app().theme_cls.font_styles["H2"] = ["H2", 60, False, -0.5]

        LabelBase.register(name="H3", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('H3')
        MDApp.get_running_app().theme_cls.font_styles["H3"] = ["H3", 48, False, 0]

        LabelBase.register(name="H4", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('H4')
        MDApp.get_running_app().theme_cls.font_styles["H4"] = ["H4", 34, False, 0.25]

        LabelBase.register(name="H5", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('H5')
        MDApp.get_running_app().theme_cls.font_styles["H5"] = ["H5", 24, False, 0]

        LabelBase.register(name="H6", fn_regular="font/JetBrainsMono-Medium.ttf")
        theme_font_styles.append('H6')
        MDApp.get_running_app().theme_cls.font_styles["H6"] = ["H6", 20, False, 0.15]

        LabelBase.register(name="Subtitle1", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('Subtitle1')
        MDApp.get_running_app().theme_cls.font_styles["Subtitle1"] = ["Subtitle1", 16, False, 0.15]

        LabelBase.register(name="Subtitle2", fn_regular="font/JetBrainsMono-Medium.ttf")
        theme_font_styles.append('Subtitle2')
        MDApp.get_running_app().theme_cls.font_styles["Subtitle2"] = ["Subtitle2", 14, False, 0.1]

        LabelBase.register(name="Body1", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('Body1')
        MDApp.get_running_app().theme_cls.font_styles["Body1"] = ["Body1", 16, False, 0.5]

        LabelBase.register(name="Body2", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('Body2')
        MDApp.get_running_app().theme_cls.font_styles["Body2"] = ["Body2", 14, False, 0.25]

        LabelBase.register(name="Button", fn_regular="font/JetBrainsMono-Medium.ttf")
        theme_font_styles.append('Button')
        MDApp.get_running_app().theme_cls.font_styles["Button"] = ["Button", 14, True, 1.25]

        LabelBase.register(name="Caption", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('Caption')
        MDApp.get_running_app().theme_cls.font_styles["Caption"] = ["Caption", 12, False, 0.4]

        LabelBase.register(name="Overline", fn_regular="font/JetBrainsMono-Regular.ttf")
        theme_font_styles.append('Overline')
        MDApp.get_running_app().theme_cls.font_styles["Overline"] = ["Overline", 10, True, 1.5]

        # Add items to the menu

      #   templist = ["Lore", "Alignments", "Players", "Rounds", "Item", "Log"]
      #   menu_items = [
      #       {
      #           "viewclass": "OneLineListItem",
      #           "text": f"[color=#FFFFFF][font=Icons]{md_icons['shield']}[/font] {x}[/color]",
      #           "height": 56,
      #       } for x in templist
      #   ]
      #
      # # Create Dropdown
      #
      #   globals.infodropdown = MDDropdownMenu(
      #       items=menu_items,
      #       width_mult=2.8,
      #       background_color=MDApp.get_running_app().theme_cls.primary_color,
      #   )
      #   globals.infodropdown.bind()

        Clock.schedule_once(self.start_loadbar, 0.1)

    def start_loadbar(self, dt):
        #Timer to allow load for initial startup. Default is 3.3
        Clock.schedule_once(self.nextscreen, 3.3)

        self.ids.loadbar.start()

    def nextscreen(self, dt):
        self.manager.current = "welcome"