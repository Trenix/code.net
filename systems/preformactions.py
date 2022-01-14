import globals

def disablewidgets(tempactiondialog):

    tempactiondialog.ids.addbuttons.disabled = True
    tempactiondialog.ids.okaction.disabled = False

def codeaction(self, tempactiondialog, button):
    disablewidgets(tempactiondialog)

    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['Target'] = 'All Logs'
    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['TargetColor'] = "#FFFFFF"

    for x in range(3):
        globals.loginfo[f"log {x + 1}"]['code'] = list(globals.playeractions)[globals.nextplayer]

    tempactiondialog.ids.actionresult.text += f"Your digital footprint has been [color={globals.colordefs['Red']}]added[/color] to all the logs."

#------------------------------------------------------

def analyzelog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['Target'] = globals.logbuttonword[lognumber]
    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['TargetColor'] = "#FFFFFF"

    if globals.loginfo[f"log {lognumber}"]['hackers'] == 1:
        tempactiondialog.ids.actionresult.text = f"There is [color={globals.colordefs['Red']}]one[/color] hacker in the {globals.lognumberword[lognumber]} log."
    else:
        tempactiondialog.ids.actionresult.text += f"There are [color={globals.colordefs['Red']}]{globals.numbertoword[globals.loginfo[f'log {lognumber}']['hackers']]}[/color] hackers in the {globals.lognumberword[lognumber]} log."

def analyzeplayer(self, tempactiondialog, player, button):

    disablewidgets(tempactiondialog)

    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['Target'] = globals.playerlist[player]['color']
    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['TargetColor'] = globals.colordefs[globals.playerlist[player]['color']]

    if globals.playerlist[player]['hacker']:
        tempactiondialog.ids.actionresult.text += f"[color={globals.colordefs[globals.playerlist[player]['color']]}]{globals.playerlist[player]['color']}[/color] is a [color={globals.colordefs['Red']}]hacker[/color]."
    else:
        tempactiondialog.ids.actionresult.text += f"[color={globals.colordefs[globals.playerlist[player]['color']]}]{globals.playerlist[player]['color']}[/color] is a [color={globals.colordefs['Blue']}]coder[/color]."

def backuplog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['Target'] = globals.logbuttonword[lognumber]
    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['TargetColor'] = "#FFFFFF"

    globals.loginfo[f"log {lognumber}"]['backedup'] = True
    tempactiondialog.ids.actionresult.text += f"A [color={globals.colordefs['Blue']}]backup[/color] was created for the {globals.lognumberword[lognumber]} log."

def hacklog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['Target'] = globals.logbuttonword[lognumber]
    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['TargetColor'] = "#FFFFFF"

    globals.loginfo[f"log {lognumber}"]['hacked'] = True
    tempactiondialog.ids.actionresult.text += f"You attempt to [color={globals.colordefs['Red']}]removed[/color] a hacker's digital footprint from the {globals.lognumberword[lognumber]} log."

def corruptlog(self, tempactiondialog, lognumber, button):

    disablewidgets(tempactiondialog)

    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['Target'] = globals.logbuttonword[lognumber]
    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['TargetColor'] = "#FFFFFF"

    globals.loginfo[f"log {lognumber}"]['corrupted'] = True
    tempactiondialog.ids.actionresult.text += f"You attempt to [color={globals.colordefs['Red']}]corrupt[/color] the {globals.lognumberword[lognumber]} log."

def hackplayer(self, tempactiondialog, player, button):

    disablewidgets(tempactiondialog)

    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['Target'] = globals.playerlist[player]['color']
    globals.playeractions[list(globals.playeractions)[globals.nextplayer]]['TargetColor'] = globals.colordefs[
        globals.playerlist[player]['color']]

    tempactiondialog.ids.actionresult.text += f"[color={globals.colordefs[globals.playerlist[player]['color']]}]{globals.playerlist[player]['color']}[/color]'s action is [color={globals.colordefs['Blue']}]{globals.playeractions[player]['Action']}[/color]."