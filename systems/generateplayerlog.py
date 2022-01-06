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

    # Create icons and text for log.
    strtemplog = ''
    strtemplogtext = ''

    for num in range(2):
        if num != 1:
            strtemplog += f"[size=30sp][color={globals.colordefs[tempplayercolorlog[num]]}][font=Icons]{md_icons['file-account']}[/font][/color] [/size]"
            strtemplogtext += f'{tempplayercolorlog[num]}, '
        else:
            strtemplog += f"[color={globals.colordefs[tempplayercolorlog[num]]}][size=30sp][font=Icons]{md_icons['file-account']}[/size][/font][/color]"
            strtemplogtext += f'{tempplayercolorlog[num]}.'

    return strtemplog, strtemplogtext