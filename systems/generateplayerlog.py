import random
import globals
from kivymd.icon_definitions import md_icons

def createplayerlog(logplayer):

    tempplayerlog = []

    temphackerlist = globals.hackerlist.copy()
    tempcoderlist = globals.coderlist.copy()

    if globals.playerlist[logplayer]['hacker'] == True:
        temphackerlist.remove(logplayer)
    else:
        tempcoderlist.remove(logplayer)

    newhackerlist = random.sample(list(temphackerlist), 1)
    newcoderlist = random.sample(list(tempcoderlist), 1)

    tempplayerlog.extend(newhackerlist + newcoderlist)

    tempplayercolorlog = []

    for x in tempplayerlog:
        tempplayercolorlog.append(globals.playerlist[x]["color"])

    tempplayercolorlog.sort()

    strtempplayerlog = f"[color={globals.colordefs[tempplayercolorlog[0]]}][size=30sp][font=Icons]{md_icons['file-account']}[/font][/color] " \
                 f"[color={globals.colordefs[tempplayercolorlog[1]]}][size=30sp][font=Icons]{md_icons['file-account']}[/font][/color] "

    return strtempplayerlog