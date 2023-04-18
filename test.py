from subprocess import *
import os
import time
from getkey import getkey, keys

def download_pack():
    run("git clone https://github.com/mas6y6pro/Raspi-MC.git --branch files --single-branch",shell=True)
    run("cp -r ./Raspi-MC/packages ./",shell=True)
    run("rm -rf Raspi-MC",shell=True)

download_pack()

import packages.gui as gui
import packages.server as server

download_pack()

while True:
    output = gui.main_menu()
    if output == "8":
        #Stops main menu
        break
    elif output == "1":
        if gui.confirm("Do you agree with the minecraft EULA (required to start server)"):
            os.system("clear")
            server.start()