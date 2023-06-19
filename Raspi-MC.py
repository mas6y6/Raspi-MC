from subprocess import *

run("pip install tqdm",shell=True)
run("pip install getkey",shell=True)

from tqdm import *
import os
import time
from getkey import getkey, keys
cwd = os.getcwd()

found = False
dirs = os.listdir()
for i in range(len(dirs)):
    s = i - 1
    if dirs[s] == "paper.jar":
        found = True
        break

def download_pack():
    run("rm -rf packages",shell=True)
    run("git clone https://github.com/mas6y6pro/Raspi-MC.git --branch files --single-branch",shell=True)
    run("cp -r ./Raspi-MC/packages ./",shell=True)
    run("rm -rf Raspi-MC",shell=True)

def setup():
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
    print("You need to have git and java 17 installed to install paper")
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
    download_pack()

    time.sleep(2)

    os.system("clear")

    os.chdir(cwd)
    print("=====================================")
    print()
    print("Downloading Paper MC 1.19.4 ...")
    print()
    print("=====================================")

    run("wget https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/545/downloads/paper-1.19.4-545.jar",shell=True)
    os.rename("paper-1.19.4-545.jar","paper.jar")

    os.system("clear")

    os.chdir(cwd)
    print("=====================================")
    print()
    print("Running paper...")
    print()
    print("=====================================")

    run("java -jar paper.jar nogui",shell=True)

if found == False:
    setup()

import packages.gui as gui
import packages.server as server

while True:
    output = gui.main_menu()
    if output == "8":
        #Stops main menu
        break
    elif output == "1":
        gui.alert()
        os.system("clear")
        server.start()