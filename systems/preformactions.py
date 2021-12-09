import globals

def disablewidgets(tempactiondialog):

    tempactiondialog.ids.addbuttons.disabled = True
    tempactiondialog.ids.okaction.disabled = False

def codeaction(self, tempactiondialog, button):
    disablewidgets(tempactiondialog)

    for x in range(3):
        globals.loginfo[f"log {x + 1}"]['code'] = globals.playeractionlist[globals.nextplayer]

    tempactiondialog.ids.actionresult.text = "Your digital footprint has been added to all the logs."

#------------------------------------------------------

def analyzelog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    if globals.loginfo[f"log {lognumber}"]['hackers'] == 0:
        tempactiondialog.ids.actionresult.text = f"There is [color={globals.colordefs['Red']}]no hacker[/color] in the {globals.lognumberword[lognumber]} log."
    elif globals.loginfo[f"log {lognumber}"]['hackers'] == 1:
        tempactiondialog.ids.actionresult.text = f"There is [color={globals.colordefs['Red']}]one hacker[/color] in the {globals.lognumberword[lognumber]} log."
    else:
        tempactiondialog.ids.actionresult.text = f"There are [color={globals.colordefs['Red']}]{globals.numbertoword[globals.loginfo[f'log {lognumber}']['hackers']]} hackers[/color] in the {globals.lognumberword[lognumber]} log."

def analyzeplayer(self, tempactiondialog, player, button):

    disablewidgets(tempactiondialog)

    if globals.playerlist[player]['hacker']:
        tempactiondialog.ids.actionresult.text = f"[color={globals.colordefs[globals.playerlist[player]['color']]}]{globals.playerlist[player]['color']}[/color] is a [color={globals.colordefs['Red']}]hacker[/color]."
    else:
        tempactiondialog.ids.actionresult.text = f"[color={globals.colordefs[globals.playerlist[player]['color']]}]{globals.playerlist[player]['color']}[/color] is a [color={globals.colordefs['Blue']}]coder[/color]."

def backuplog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    globals.loginfo[f"log {lognumber}"]['backedup'] = True
    tempactiondialog.ids.actionresult.text = f"A backup was created for the {globals.lognumberword[lognumber]} log."

def hacklog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    globals.loginfo[f"log {lognumber}"]['hacked'] = True
    tempactiondialog.ids.actionresult.text = f"A hacker's digital footprint from the {globals.lognumberword[lognumber]} will be removed."

def corruptlog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    globals.loginfo[f"log {lognumber}"]['corrupted'] = True
    tempactiondialog.ids.actionresult.text = f"You attempt to corrupt the {globals.lognumberword[lognumber]} log."

def hackplayer(self, tempactiondialog, player, button):

    disablewidgets(tempactiondialog)

    tempactiondialog.ids.actionresult.text = f"[color={globals.colordefs[globals.playerlist[player]['color']]}]{globals.playerlist[player]['color']}[/color]'s action is [color={globals.colordefs['Blue']}]{globals.playeractions[player]['Action']}[/color]."