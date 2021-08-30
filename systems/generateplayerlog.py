import random
import globals
from kivymd.icon_definitions import md_icons

def createplayerlog():

    tempplayerlog = random.sample(list(globals.coderlist), 1) + random.sample(list(globals.hackerlist), 1)

    tempplayercolorlog = []

    for x in tempplayerlog:
        tempplayercolorlog.append(globals.playerlist[x]["color"])

    tempplayercolorlog.sort()

    strtempplayerlog = f"[color={globals.colordefs2[tempplayercolorlog[0]]}][size=30][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                 f"[color={globals.colordefs2[tempplayercolorlog[1]]}][size=30][font=Icons]{md_icons['folder-account']}[/font][/color] "

    return strtempplayerlog