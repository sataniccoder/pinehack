import os

if os.geteuid()==0:
  pass
else:
  print("[!] user needs to be root!")
  print("[!] re-run as root!")
  quit()

p = ["python", "python-pip", "aircrack-ng", "wifi-tools", "gcc"]
a = ["python3", "python3-pip", "aircrack-ng", "wifi-tools", "gcc"]
pip = ["scapy", "netifaces"]

def pac():
    global p, pip
    print("updating system...")
    os.system("pacman -Syy")
    print("installing packges...")
    for i in p:
        cmd = "pacman -S "+i
        print("installing "+i+"...")
        os.system(cmd)
    print("nistalling pip packages...")
    for i in pip:
        cmd = "pip install "+i
        print("installing "+i+"...")
        os.system(cmd)
    print("done!")
    print("you can now run pine hack!")
    quit()  

def apt():
    global a, pip
    print("updating system...")
    os.system("apt-get update")
    print("installing packges...")
    for i in p:
        cmd = "apt-get install "+i
        print("installing "+i+"...")
        os.system(cmd)
    print("nistalling pip packages...")
    for i in pip:
        cmd = "pip3 install "+i
        print("installing "+i+"...")
        os.system(cmd)
    print("done!")
    print("you can now run pine hack!")
    quit() 


ap = input("does your system use apt or pacman [apt/pac] ")

if ap == "pac":
    pac()
elif ap == "apt":
    apt()
else:
    print("[!] pac or apt not "+apt+" [!]")
    quit()