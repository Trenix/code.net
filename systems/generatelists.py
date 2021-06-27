import globals
import random

def playersetup(self):

    for x in range(globals.players):
        globals.playerlist[f"player {x+1}"] = {"hacker": False}

# Setup for AI
    if globals.players == 4 or globals.players == 5:
        globals.playerlist["AI"] = {"hacker": False}
        globals.playerlist["AI"]["computer"] = True
        globals.playerlist["AI"]["color"] = "AI"

# Set players as not computer
        for num in range(globals.players):
            globals.playerlist[f"player {num+1}"]["computer"] = False

# No computers on logs
        for x in range(globals.players):
            if globals.playerlist[f"player {x+1}"]["computer"] == False:
                globals.notai.append(f"player {x+1}")


# Randomly set players to be hacker and create hacker list
    globals.hackerlist = random.sample(list(globals.playerlist.keys()), globals.amtbad)

    for x in globals.hackerlist:
        globals.playerlist[x]["hacker"] = True

# Create coder list
    for x in range(globals.players):
        if globals.playerlist[f"player {x + 1}"]["hacker"] == False:
            globals.coderlist.append(f"player {x + 1}")
    if globals.players == 4 or globals.players == 5:
        if globals.playerlist["AI"]["hacker"] == False:
            globals.coderlist.append("AI")

# Set hacker allies
    if globals.players <= 8:
        globals.playerlist[globals.hackerlist[0]]["allies"] = globals.hackerlist[1]
        globals.playerlist[globals.hackerlist[1]]["allies"] = globals.hackerlist[0]
    else:
        globals.playerlist[globals.hackerlist[0]]["allies"] = globals.hackerlist[1], globals.hackerlist[2]
        globals.playerlist[globals.hackerlist[1]]["allies"] = globals.hackerlist[0], globals.hackerlist[2]
        globals.playerlist[globals.hackerlist[2]]["allies"] = globals.hackerlist[0], globals.hackerlist[1]

# Get color tracker ready
    globals.colortracker = globals.players
