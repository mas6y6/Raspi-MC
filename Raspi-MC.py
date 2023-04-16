from subprocess import *
import os
import time
from getkey import getkey, keys
print("Loading GUI setup")

#run("wget https://piston-data.mojang.com/v1/objects/8f3112a1049751cc472ec13e397eade5336ca7ae/server.jar",shell=True,stdout=None)

cwd = os.getcwd()

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

os.system("clear")
print("=====================================")
print()
print("Downloading GUI menu from github...")
print()
print("=====================================")

os.mkdir("gui")

os.chdir("gui")

#Downloads GUI script

os.system("")

os.chdir(cwd)

time.sleep(2)
os.system("clear")
