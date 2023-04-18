import os
from tkinter.filedialog import askopenfilename
import time
import subprocess
#SETTINGS

def start():
    subprocess.run("clear")
    print("Starting Server..")
    subprocess.run("java -jar paper.jar nogui")


def _grab_old_prop_data():
    with open("server.properties","r") as tet:
        data = tet.readlines()
        return data

def hardcore(bool):
    data = _grab_old_prop_data()
    os.remove("server.properties")
    if hardcore == True:
        data[45] = f"hardcore=true\n"

    else:
        data[45] = f"hardcore=false\n"
    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

def gamemode(mode):
    data = _grab_old_prop_data()
    os.remove("server.properties")
    data[5] = f"gamemode={gamemode}\n"
    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

def seed(seed):
    data = _grab_old_prop_data()
    os.remove("server.properties")
    data[4] = f"level-seed={seed}\n"
    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

def diff(difficulty):
    data = _grab_old_prop_data()
    os.remove("server.properties")
    data[16] = f"difficulty={difficulty}\n"
    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

def ip(ip):
    data = _grab_old_prop_data()
    os.remove("server.properties")
    data[28] = f"server-ip={ip}\n"

    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

def motd(motd):
    data = _grab_old_prop_data()
    os.remove("server.properties")
    data[11] = f"motd={motd}\n"

    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

def port(port):
    data = _grab_old_prop_data()
    os.remove("server.properties")
    data[31] = f"server-port={port}\n"
    data[12] = f"query.port={port}\n"

    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

#END OF SETTINGS

def upload_plugin():
    print("Upload window has opened")
    dir = askopenfilename(title='Upload Plugin',
    filetypes=[("Spigot Plugin", "*.jar")]
    )
    if dir == "":
        print("To plugin has been uploaded")
    else:
        print(f"Uploading {dir}...")
        os.chdir("plugins")
        os.system(f'cp "{dir}" "{os.getcwd()}"')
        os.chdir("..")
        print("Upload complete...")
        print("Sleeping for 5 Seconds before returning to main menu")
        time.sleep(5)