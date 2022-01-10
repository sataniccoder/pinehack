import netifaces
import os

def display_interface():
    iface = netifaces.interfaces()
    return iface

def monitor_mode(method, iface):
    if method == "ifconfig":
        os.system("airmon-ng check kill")
        cmd1 = "ifconfig "+iface+" down"
        os.system(cmd1)
        cmd2 = "iwconfig "+iface+" mode monitor"
        os.system(cmd2)
        cmd3 = "ifconfig "+iface+" up"
        os.system(cmd3)
    else:
        os.system("airmon-ng check kill")
        cmd1 = "airmon-ng start "+iface
        os.system(cmd1)

def managed_mode(method, iface):
    if method == "ifconfig":
        os.system("airmon-ng check kill")
        cmd1 = "ifconfig "+iface+" down"
        os.system(cmd1)
        cmd2 = "iwconfig "+iface+" mode managed"
        os.system(cmd2)
        cmd3 = "ifconfig "+iface+" up"
        os.system(cmd3)
    else:
        os.system("airmon-ng check kill")
        cmd1 = "airmon-ng stop "+iface
        os.system(cmd1)