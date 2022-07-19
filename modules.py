
from main import *
global target
global interface
global packetsize
global threads_count

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
            print("set interface <interface>    ---  sets bluetooth interface to use for attack")
            print("run                          ---  starts attack")
            print("stop                         ---  stops all data flow")
            print("exit                         ---  returns to the parent module")

        if cmd == "set" and subcmd == "target":

            target = arg
            print(target + " ---> target\n")


        if cmd == "set" and subcmd == "threads":
            
            threads_count = arg
            print(threads_count + " ---> threads\n")

        if cmd == "set" and subcmd == "packetsize":
            
            packetsize = arg
            print(packetsize + " ---> packet size\n")

        if cmd == "set" and subcmd == "interface" :
            
            interface = arg
            print(interface + " ---> bluetooth interface\n")

        if cmd == "run":
            jam(threads_count, packetsize)

        if cmd == "exit":
            main()

        if cmd == "stop":
            for i in threads_ar:
                i.stop()
                i.join()
            


