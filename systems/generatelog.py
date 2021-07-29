import random
import globals
from kivymd.icon_definitions import md_icons

def createlog(playersonlog):

    if globals.players == 9:
        if random.random() < (1 / ((globals.players + globals.aiamt) - 1)):
            if random.random() < (1 / ((globals.players + globals.aiamt) - 2)):
                amtbadlog = 3
            else:
                amtbadlog = 2
        else:
            amtbadlog = 1

            tempamthacker = random.randint(1, amtbadlog)
    else:
        if random.random() < (1 / ((globals.players + globals.aiamt) - 1)):
            amtbadlog = 2
        else:
            amtbadlog = 1

        tempamthacker = random.randint(1, amtbadlog)

    templog = random.sample(list(globals.coderlist), (playersonlog - tempamthacker)) + random.sample(list(globals.hackerlist), tempamthacker)

    tempcolorlog = []

    for x in templog:
        tempcolorlog.append(globals.playerlist[x]["color"])

    tempcolorlog.sort()

    if playersonlog == 4:
        strtemplog = f"[color=#FFFFFF] [size=30][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                     f"[color={globals.colordefs[tempcolorlog[1]]}] [size=30][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                     f"[color={globals.colordefs[tempcolorlog[2]]}] [size=30][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                     f"[color={globals.colordefs[tempcolorlog[3]]}] [size=30][font=Icons]{md_icons['folder-account']}[/font][/color] "

    # strtemplog = '[b]' + ', '.join(str(x) for x in tempcolorlog) + '[/b]'

    return strtemplog