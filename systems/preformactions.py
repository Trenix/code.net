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

    if globals.hackerperlog[lognumber] == None:

        globals.hackerperlog[lognumber] = self.amthacker()

        # if lognumber == 1:
        #     globals.log1hacker = sethacker
        # elif lognumber == 2:
        #     globals.log2hacker = sethacker
        # else:
        #     globals.log3hacker = sethacker

        disablewidgets(tempactiondialog)


        if globals.hackerperlog[lognumber] == 1:
            tempactiondialog.ids.actionresult.text = f"There is one hacker in the {globals.lognumberword[lognumber]} log."
        else:
            tempactiondialog.ids.actionresult.text = f"There are {globals.numbertoword[globals.hackerperlog[lognumber]]} hackers in the {globals.lognumberword[lognumber]} log."



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