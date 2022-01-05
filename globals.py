aiamt = 0
amtbad = 0
players = 0
nextplayer = 0
playerlist = {}
playercounter = 1
popupWindow = None
colortracker = 0
notai = []
hackerlist = []
coderlist = []
playerlogrev = []
revealtracker = 1
#700 Color
colordefs = {"Red": "#d32f2f", "Pink": "#c2185b", "Purple": "#7b1fa2", "Blue": "#1976d2",
             "Green": '#689f38', "Yellow": '#fbc02d', "Orange": '#f57c00', "Brown": '#5d4037',
             "Grey": '#616161', "AI": '#FFFFFF'}
time = 0
timer = 0
lastscreen = None
hackeractionlist = ["Hack Log", "Corrupt Log", "Hack Player"]
coderactionlist = ["Code", "Analyze Log", "Analyze Player", "Backup Log"]
actionicons = {"Hack Log": {'icon': 'folder-network', 'color': '#d32f2f'},
               "Corrupt Log": {'icon': 'folder-cancel', 'color': '#d32f2f'},
               "Hack Player": {'icon': 'account-network', 'color': '#d32f2f'},
               "Code": {'icon': 'language-python', 'color': "#1976d2"},
               "Analyze Log": {'icon': 'folder-search', 'color': "#1976d2"},
               "Analyze Player": {'icon': 'account-search', 'color': "#1976d2"},
                "Backup Log": {'icon': 'folder-download', 'color': "#1976d2"}}
playeractions = {}
loginfo = {}
numbertoword = {1: 'one', 2: 'two', 3: 'three'}
lognumberword = {1: 'first', 2: 'second', 3: 'third'}
logbuttonword = {1: 'First Log', 2: 'Second Log', 3: 'Third Log'}
# infodropdown = None