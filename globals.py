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
# colordefs = {"Red": [198/255, 40/255, 40/255, 1], "Pink": [173/255, 20/255, 87/255, 1],
#              "Purple": [106/255, 27/255, 154/255, 1], "Blue": [21/255, 101/255, 192/255, 1],
#              "Green": [46/255, 125/255, 50/255, 1], "Yellow": [249/255, 168/255, 37/255, 1],
#              "Orange": [239/255, 108/255, 0/255, 1], "Brown": [78/255, 52/255, 46/255, 1],
#              "Grey": [66/255, 66/255, 66/255, 1], "AI": [255/255, 255/255, 255/255, 1]}
#900 Color
colordefs = {"Red": "#b71c1c", "Pink": "#880e4f", "Purple": "#4a148c", "Blue": "#0d47a1",
             "Green": '#1b5e20', "Yellow": '#f57f17', "Orange": '#e65100', "Brown": '#3e2723',
             "Grey": '#212121', "AI": '#FFFFFF'}
time = 0
timer = 0
lastscreen = None
hackeractionlist = ["Hack Digital Footprint", "Corrupt Log", "Infect Software", "DDOS Server"]
coderactionlist = ["Code", "Analyze Log", "Encrypt Log", "Analyze Player", "Backup Log"]
playeractions = {}
playeractionlist = []
# infodropdown = None