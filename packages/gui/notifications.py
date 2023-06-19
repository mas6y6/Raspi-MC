import os
from getkey import getkey, keys

if __name__ == "__main__":
    print("The current process has been Terminated")
    exit()



def Error(Error, Info):
    os.system("clear")
    print("============ Error =============")
    print()
    print(Error)
    print()
    print(Info)
    print()
    print('Press "enter" to close')
    print("==============================")
    input()
    os.system("clear")

def loading(info):
    os.system("clear")
    print("==============================")
    print()
    print(info)
    print()
    print("==============================")

def confirm(info):
    while True:
        os.system("clear")
        print("==============================")
        print()
        print(info)
        print()
        print("Y/n")
        print()
        print("==============================")
        key = getkey()
        if key == "Y":
            output = True
            break
        elif key == "n":
            output = False
            break
        else:
            pass
    os.system("clear")
    return output