from roku import Roku

roku = Roku('192.168.43.137')

roku.home()


def activity(roku):
    apps = []
    indexes = []
    data_dict = {}
    for items in roku.apps:
        apps.append(items.name)
    for item in range(len(apps)):
        indexes.append(item)
    pair = zip(indexes,apps)
    for x in pair:
        data_dict.setdefault(x[0],[]).append(x[1])
    selection = input("Which Application would you like to launch Big-Dick-Brad?" "\n")
    for key, value in data_dict.items():
        if str(selection) == str(key):
            print("you chose: %s " %(value) + "\n")
            activity(roku)
        elif selection == value:
            print("you chose: %s" %(value) + "\n")
            activity(roku)
activity(roku)
'''
    elif selection not in data_dict:
        print('no')
activity(roku)
'''
