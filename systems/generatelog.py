import random
import globals
from kivymd.icon_definitions import md_icons

def createlog(playersonlog, amtofhackers, codeplayer):

    if amtofhackers == None:

        amtofhackers = createhackeramt()

    if codeplayer != None:

        codetemplist = list(globals.coderlist)
        codetemplist.remove(codeplayer)

        templog = random.sample(codetemplist, ((playersonlog - 1) - amtofhackers)) + random.sample(list(globals.hackerlist), amtofhackers)
        templog.append(codeplayer)

    else:
        templog = random.sample(list(globals.coderlist), (playersonlog - amtofhackers)) + random.sample(list(globals.hackerlist), amtofhackers)

    tempcolorlog = []

    for x in templog:
        tempcolorlog.append(globals.playerlist[x]["color"])

    tempcolorlog.sort()

    if playersonlog == 4:
        strtemplog = f"[color={globals.colordefs[tempcolorlog[0]]}][size=30sp][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                     f"[color={globals.colordefs[tempcolorlog[1]]}][size=30sp][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                     f"[color={globals.colordefs[tempcolorlog[2]]}][size=30sp][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                     f"[color={globals.colordefs[tempcolorlog[3]]}][size=30sp][font=Icons]{md_icons['folder-account']}[/font][/color] "
    else:
        strtemplog = f"[color={globals.colordefs[tempcolorlog[0]]}][size=30sp][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                     f"[color={globals.colordefs[tempcolorlog[1]]}][size=30sp][font=Icons]{md_icons['folder-account']}[/font][/color] " \
                     f"[color={globals.colordefs[tempcolorlog[2]]}][size=30sp][font=Icons]{md_icons['folder-account']}[/font][/color] "

    return strtemplog

def createhackeramt():

    if globals.players == 9:
        if random.random() < (1 / ((globals.players + globals.aiamt) - 1)):
            if random.random() < (1 / ((globals.players + globals.aiamt) - 2)):
                amtbadlog = 3
            else:
                amtbadlog = 2

        else:
            amtbadlog = 1

    else:
        if random.random() < (1 / ((globals.players + globals.aiamt) - 1)):
            amtbadlog = 2
        else:
            amtbadlog = 1

    return amtbadlog