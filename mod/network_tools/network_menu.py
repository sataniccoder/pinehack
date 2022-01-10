import os

from mod.system.banners import network_banner
from mod.system.iface_handler import display_interface, managed_mode, monitor_mode

from mod.network_tools.network_mod.scan import scan

def valid_loop(msg):
        valid = False
        while not valid:
            try:
                op = int(input(msg))
                valid = True
            except ValueError:
                print("[!] must be INT not STR [!]")
        return op

def menu(config):
    os.system("clear")
    print(network_banner(config))
    
    while True:
        op = valid_loop("enter option: ")
       
        if op == 1:
            iface = display_interface()
            num = 0
            for i in iface:
                print(str(num)+") "+i)
                num += 1
            iface_num = valid_loop("enter number for iface: ")
            config["iface"] = iface[iface_num]
            print("[+] new iface set for this run, change in config for futer")
            os.system("clear")
            print(network_banner(config))

        elif op == 2:
            print("[*] putting "+config["iface"]+" into monitor mode...")
            monitor_mode(config["mon"], config["iface"])
        elif op == 3:
            print("[*] putting "+config["iface"]+" into managed mode...")
            managed_mode(config["mon"], config["iface"])
        
        elif op == 4:
            scan()

        elif op == 0:
            print("[!] user quit, bye...")
            break
        else:
            print("[!] must be a valid option [!]")
