import os

from mod.system.banners import wifi_banner
from mod.system.iface_handler import display_interface, managed_mode, monitor_mode

from mod.wifi_tools.wifi_mod.nmcli import main as nmcli
from mod.wifi_tools.wifi_mod.wifi_recon import recon

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
    print(wifi_banner(config))
    
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
            print(wifi_banner(config))

        elif op == 2:
            print("[*] putting "+config["iface"]+" into monitor mode...")
            monitor_mode(config["mon"], config["iface"])
        elif op == 3:
            print("[*] putting "+config["iface"]+" into managed mode...")
            managed_mode(config["mon"], config["iface"])
        
        elif op == 4:
            nmcli(config["iface"])
            os.system("clear")
            print(wifi_banner(config))
        elif op == 5:
            recon(config)
            os.system("clear")
            print(wifi_banner(config))
        elif op == 0:
            print("[!] user quit, bye...")
            break
        else:
            print("[!] must be a valid option [!]")
