import random
import globals

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

    strtemplog = '[b]' + ', '.join(str(x) for x in tempcolorlog) + '[/b]'

    return strtemplog