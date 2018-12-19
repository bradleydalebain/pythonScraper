from roku import Roku
from pprint import pprint
roku = Roku('192.168.43.137')

def go_home(roku):
    selection = input('press \'h\' to navigate home')
    if selection == 'h':
        roku.home(roku)

def action(roku, selection):
    roku.apps[int(selection)].launch()
    app_select(roku)
    home(roku)

def app_select(roku):
    apps = []
    indexes = []
    data_dict = {}
    for items in roku.apps:
        apps.append(items.name)
    for item in range(len(apps)):
        indexes.append(item)
    sel = list(zip(indexes, apps))
    pprint(sel)
    selection = input("Enter the # corresponding to the app to launch, or enter \'h\' for more home navigation commands" "\n")
    pair = zip(indexes,apps)
    for x in pair:
        data_dict.setdefault(x[0],[]).append(x[1])
    for key, value in data_dict.items():
        if str(selection) == str(key):
            print("you chose: %s " %(value) + "\n")
            action(roku, selection)
        elif str(selection) == 'h':
            home(roku)

def home(roku):
    roku.home()
    app_select(roku)

app_select(roku)
