import os

from mod.wifi_tools.wifi_mod.nmcli import get_wifi
from mod.system.iface_handler import display_interface, managed_mode, monitor_mode

def valid_loop(msg):
        valid = False
        while not valid:
            try:
                op = int(input(msg))
                valid = True
            except ValueError:
                print("[!] be INT not STR [!]")
        return op


def recon(config):
    os.system("clear")
    print("BETA TOOL!\nNOT FULLY DEVELOPET!\nSOME TOOLS MAY NOT WORK!\n")
    op = valid_loop("1) scan via nmcli\n2) scan via airodump-ng\n3) quit beta wifi recon (we undersand)\nenter option: ")
    if op == 1:
        wifi_list = get_wifi(config["iface"])
        for i in wifi_list:
            print(i)
        input("[+] hit enter to quit")
    elif op == 2:
        print("[*] putting "+config["iface"]+" into monitor mode...")
        monitor_mode(config["mon"], config["iface"])
        print("[-] done!")
        print("[*] starting scanning press CTRL+C to stop...")
        cmd = "airodump-ng "+config["iface"]
        os.system(cmd)
    elif op == 3:
        print("understanble")
    else:
        pass
        
