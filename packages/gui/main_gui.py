import os
from getkey import getkey, keys

def main_menu():
    while True:
        os.system("clear")
        print("============== Main Menu ==============")
        print()
        print("1. Start Server")
        print("2. Server Settings")
        print("3. World Settings")
        print("4. Plugins")
        print("5. Logs")
        print("6. Crash Reports")
        print("7. More info")
        print("8. Exit")
        print()
        print("=======================================")
        key = getkey()
        if key == "1" or key == "2" or key == "3" or key == "4" or key == "5" or key == "6" or key == "7" or key == "8":
            output = key
            break
        else:
            output = None
    os.system("clear")
    return output

def Server_settings():
    while True:
        os.system("clear")
        print("============ Server Settings ============")
        print()
        print("1. Bukkit")
        print("2. Spigot")
        print("3. IP Settings")
        print("4. Exit")
        print()
        print("=======================================")
        key = getkey()
        if key == "1" or key == "2" or key == "3" or key == "4":
            output = key
            break
        else:
            output = None
    os.system("clear")
    return output