import random
import globals

def createplayerlog():
    tempplayerlog = random.sample(list(globals.coderlist), 1) + random.sample(list(globals.hackerlist), 1)

    tempplayercolorlog = []

    for x in tempplayerlog:
        tempplayercolorlog.append(globals.playerlist[x]["color"])

    tempplayercolorlog.sort()

    strtempplayerlog = '[b]' + ', '.join(str(x) for x in tempplayercolorlog) + '[/b]'

    return strtempplayerlog