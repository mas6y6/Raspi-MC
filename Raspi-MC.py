from subprocess import *
import os
import time
from getkey import getkey, keys
cwd = os.getcwd()

found = False
dirs = os.listdir()
for i in range(len(dirs)):
    s = i - 1
    if dirs[s] == "spigot-1.19.4.jar":
        found = True
        break

def setup():
    print("Loading GUI setup")
    os.system("clear")
    print("=====================================")
    print()
    print("Welcome to the Raspi-MC (spigot mc)")
    print()
    print("A minecraft server installer")
    print()
    print("Version 1.0 / MC Version 1.19.4")
    print()
    print("This will install spigot mc server And prevent all the hassle of making it function")
    print("For more info click here: https://www.spigotmc.org/")
    print()
    print('Press "enter" to continue')
    print()
    print("=====================================")
    input()
    os.system("clear")

    os.system("clear")
    print("=====================================")
    print()
    print("You need to have github and java 17 installed to install spigot")
    print()
    print('Press "enter" to continue')
    print()
    print("=====================================")
    input()
    os.system("clear")
    print("=====================================")
    print()
    print("Downloading GUI menu from github...")
    print()
    print("=====================================")
    run("git clone https://github.com/mas6y6pro/Raspi-MC.git --branch files --single-branch",shell=True)
    run("cp -r ./Raspi-MC/packages ./",shell=True)
    run("rm -rf Raspi-MC",shell=True)

    time.sleep(2)

    os.system("clear")

    os.chdir(cwd)
    print("=====================================")
    print()
    print("Downloading Spigot MC 1.19.4 ...")
    print()
    print("=====================================")

    #run("wget https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/514/downloads/paper-1.19.4-514.jar",shell=True)

    os.system("clear")

    os.chdir(cwd)
    print("=====================================")
    print()
    print("Running Spigot...")
    print()
    print("=====================================")

    #run("java -jar paper.jar nogui",shell=True)

if found == False:
    setup()

import packages.gui as system
import packages.server as server

while True:
    output = system.main_menu()
    if output == "8":
        #Stops main menu
        break
    elif output == "1":
        os.system("clear")
        server.start()