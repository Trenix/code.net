import globals
import random

def disablewidgets(tempactiondialog):

    tempactiondialog.ids.addbuttons.disabled = True
    tempactiondialog.ids.okaction.disabled = False

def codeaction(self, tempactiondialog, button):
    tempactiondialog.ids.actionresult.text = "Code has been complete."
    button.disabled = True
    tempactiondialog.ids.okaction.disabled = False

#------------------------------------------------------

def analyzelog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    if globals.hackerperlog[lognumber] == None:
        globals.hackerperlog[lognumber] = self.amthacker()

    if globals.hackerperlog[lognumber] == 1:
        tempactiondialog.ids.actionresult.text = f"There is [color={globals.colordefs['Red']}]one hacker[/color] in the {globals.lognumberword[lognumber]} log."
    else:
        tempactiondialog.ids.actionresult.text = f"There are [color={globals.colordefs['Red']}]{globals.numbertoword[globals.hackerperlog[lognumber]]} hackers[/color] in the {globals.lognumberword[lognumber]} log."

def amthacker(self):

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

#------------------------------------------------------

def analyzeplayer(self, tempactiondialog, player, button):

    if globals.playerlist[player]['hacker']:
        tempactiondialog.ids.actionresult.text = f"[color={globals.colordefs[globals.playerlist[player]['color']]}]{globals.playerlist[player]['color']}[/color] is a [color={globals.colordefs['Red']}]hacker[/color]."
    else:
        tempactiondialog.ids.actionresult.text = f"[color={globals.colordefs[globals.playerlist[player]['color']]}]{globals.playerlist[player]['color']}[/color] is a [color={globals.colordefs['Blue']}]coder[/color]."

    disablewidgets(tempactiondialog)