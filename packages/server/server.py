import os
from tkinter.filedialog import askopenfilename
import shutil
import time

def _grab_old_prop_data():
    with open("server.properties","r") as tet:
        data = tet.readlines()
        return data

def settings_world(difficulty="easy",gamemode="survival",hardcore=False,seed=""):
    data = _grab_old_prop_data()
    os.remove("server.properties")

    data[7] = f"difficulty={difficulty}\n"

    data[18] = f"gamemode={gamemode}\n"
    if hardcore == True:
        data[21] = f"hardcore=true\n"

    else:
        data[21] = f"hardcore=false\n"

    data[26] = f"level-seed={seed}\n"

    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

def settings_server(ip="",motd="A minecraft server",port=25565):
    data = _grab_old_prop_data()
    os.remove("server.properties")

    data[47] = f"server-ip={ip}\n"
    data[32] = f"motd={motd}\n"
    data[48] = f"server-port={port}\n"
    data[39] = f"query.port={port}\n"

    with open("server.properties","w") as e:
        for i in range(len(data)):

            e.write(data[i])

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