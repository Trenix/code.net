import random
import globals

def createlog(playersonlog):

    if globals.players == 9:
        tempamthacker = random.randint(1, 3)
    else:
        tempamthacker = random.randint(1, 2)

    templog = random.sample(list(globals.coderlist), (playersonlog - tempamthacker)) + random.sample(list(globals.hackerlist), tempamthacker)

    tempcolorlog = []

    for x in templog:
        tempcolorlog.append(globals.playerlist[x]["color"])

    tempcolorlog.sort()

    strtemplog = '[b]' + ', '.join(str(x) for x in tempcolorlog) + '[/b]'

    return strtemplog