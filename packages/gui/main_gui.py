import os
import time
from getkey import getkey, keys

def main_menu():
    while True:
        key = getkey()
        os.system("clear")
        print("========== Main menu ==========")
        print()
        print("1. Start Server")
        print("2. Server Settings")
        print("3. Plugins")
        print("4. Worlds")
        print("5. Exit")
        print()
        print("Input the number of the item")
        print("===============================")
        output = key
    return output