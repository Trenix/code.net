import globals

def openinfo(self):
    #     # globals.infodropdown.caller = button
    #     # globals.infodropdown.open()
    globals.lastscreen = self.manager.current
    self.manager.transition.direction = 'up'
    self.manager.current = "maininfo"