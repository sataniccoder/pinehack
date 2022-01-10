import os

if os.geteuid()==0:
  pass
else:
  print("[!] user needs to be root!")
  print("[!] re-run as root!")
  quit()


# this is the config for the program
from mod.system.read_config import read
from mod.system.iface_handler import display_interface, managed_mode, monitor_mode
from mod.system.banners import main_banner as banner_main, wifi_banner
from mod.system.clean import clean

# these are the menu imports for the program
from mod.network_tools.network_menu import menu as network
from mod.wifi_tools.wifi_menu import menu as wifi

config = read()

def valid_loop(msg):
        valid = False
        while not valid:
            try:
                op = int(input(msg))
                valid = True
            except ValueError:
                print("[!] must be INT not STR [!]")
        return op



print(banner_main(config))

try:
    while True:
        op = valid_loop("enter option: ")
        
        if op == 1:
            print("[*] running installer...")
            os.system("python installer.py")
       
        elif op == 2:
            iface = display_interface()
            num = 0
            for i in iface:
                print(str(num)+") "+i)
                num += 1
            iface_num = valid_loop("enter number for iface: ")
            config["iface"] = iface[iface_num]
            print("[+] new iface set for this run, change in config for futer")
            os.system("clear")
            print(banner_main(config))

        elif op == 3:
            print("[*] putting "+config["iface"]+" into monitor mode...")
            monitor_mode(config["mon"], config["iface"])
        elif op == 4:
            print("[*] putting "+config["iface"]+" into managed mode...")
            managed_mode(config["mon"], config["iface"])

        elif op == 5:
            network(config)
            os.system("clear")
            print(banner_main(config)) 
        elif op == 6:
            wifi()
            os.system("clear")
            print(banner_main(config)) 
        elif op == 7:
            pass

        elif op == 0:
            clean()
            print("[!] user quit, bye...")
            quit()
        else:
            print("[!] must be a valid option [!]")
            
except KeyboardInterrupt:
    clean()
    print("[!] user quit, exting...")
    quit()



