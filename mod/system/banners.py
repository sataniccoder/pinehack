def main_banner(config):
    banner = """

V0.1   _              _                _    
 _ __ (_)_ __   ___  | |__   __ _  ___| | __
| '_ \| | '_ \ / _ \ | '_ \ / _` |/ __| |/ /
| |_) | | | | |  __/ | | | | (_| | (__|   < 
| .__/|_|_| |_|\___| |_| |_|\__,_|\___|_|\_\ 
|_|=========================================
[IFACE] """+config["iface"]+"""
[MON MODE] """+config["mon"]+"""
-------------------[INFO]-------------------
[1] install (if not done already)
[2] change iface
[3] put into monitor mode
[4] put into managed mode
-------------------[MENU]-------------------
[5] network tools
[6] wifi exploits
[7] other tools
------------------[OTHER]-------------------
[0] quit program
--------------------------------------------

    """
    return banner

def network_banner(config):
    banner = """
            _                      _    
 _ __   ___| |___      _____  _ __| | __
| '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ /
| | | |  __/ |_ \ V  V / (_) | |  |   < 
|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\ 
========================================      
[IFACE] """+config["iface"]+"""
[MON MODE] """+config["mon"]+"""
-------------------[INFO]-------------------
[1] change iface
[2] put into monitor mode
[3] put into managed mode                                     
-------------------[MENU]-------------------
[4] scapy scan 
[5] port scan (one ip, NOT WORKING)
[6] SSH bruteforce (NOT WORKING)
------------------[OTHER]-------------------
[0] exit network program
--------------------------------------------

    """
    return banner
def wifi_banner(config):
    banner = """
          _  __ _                     _    
__      _(_)/ _(_) ___ _ __ __ _  ___| | __
\ \ /\ / / | |_| |/ __| '__/ _` |/ __| |/ /
 \ V  V /| |  _| | (__| | | (_| | (__|   < 
  \_/\_/ |_|_| |_|\___|_|  \__,_|\___|_|\_\ 
============================================      
[IFACE] """+config["iface"]+"""
[MON MODE] """+config["mon"]+"""
-------------------[INFO]-------------------
[1] change iface
[2] put into monitor mode
[3] put into managed mode                                     
-------------------[MENU]-------------------
[4] wifi recon
[5] nmcli attack 
[6] aircrack-ng automated
[7] wps attack menu
------------------[OTHER]-------------------
[0] exit network program
-------------------------------------------- 
    """
    return banner