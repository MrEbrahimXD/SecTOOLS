import colorama
from colorama import Fore, Back, Style
import subprocess
import os
from sys import intern

from colorama.ansi import clear_line





def calling_nmap():
  print("Calling Nmap")
  print("Starting Nmap")
  print("Enter your scan type : 1.Stealthy Scan , 2.TCP scan , 3.Full scan , 4.List HOST scan")
  k = int(input())
  if k == 1:
    print("Choosed : Stealthy scan , Enter your target IP Address")
    target1 = str(input())
    os.system(f"sudo nmap -sS {target1}")
    print("Done Scanning !")
  elif k == 2:
    print("Choosed : TCP Scan , Enter your target IP address")
    target2 = str(input())
    os.system(f"sudo nmap -sT {target2}")
    print("Done Scanning!")
  elif k == 3:
    print("Choosed : Full TCP scan , Enter you target IP Address")
    target3 = str(input())
    os.system(f"sudo nmap -A {target3}")
  elif k == 4:
    print("Choosed : list HOST Scan")
    print("Enter your router IP Address  , Find it by <route -n> command")
    targetr = str(input())
    os.system(f"sudo nmap -sL {targetr}")
  else:
    print("Invalid choose , Please run the program again and choose from <1 to 4>")

def run_sniffing():
  print("Starting Sniffing ") 
  print("Enter your router IP Address Exp:192.168.0.1 Or 10.0 0.1")
  router1 = str(input())
  print("Enter your target IP Address <LAN IP address> , Found by nmap list scan") 
  target_ip = str(input())
  print("""Starting ettercap 
  You have to launch wireshark after starting ettercap by 
  <sudo wireshark>""")
  os.system(f"sudo ettercap -T -S -i eth0 -M arp:remote /{router1}// /{target_ip}//")
  print("Done your request")

def scan_webserver():
  print("Choose 1.Nikto or 2.dirb")
  web_scan = int(input())
  if web_scan == 1:
    print("Starting nikto")
    print("Enter target Webserver :")
    target_webserver = str(input())
    print("Scanning Webserver")
    os.system(f"sudo nikto --host {target_webserver}")
    print("Done scanning with Nikto")
  if web_scan == 2:
    print("Stating dirb..")
    print("Enter your target full Web Address : ")
    target_ip_dirb = str(input())
    os.system(f"sudo dirb {target_ip_dirb}")
    print("Done scanning using dirb !")

    

def req_install():
  print("Installing requirement for running other programs...")
  os.system("sudo apt update && sudo apt install wireshark -y && sudo apt install nmap -y && sudo apt install ettercap-text-only -y && sudo apt install nikto -y")

def apache2_webserver():
  print("Starting apache2 webserver...")
  os.system("sudo systemctl start apache2")
  print("you can edit the webserver by entering <edit> command")
  edit = str(input())
  if edit == "edit":
    print("jumping to /var/www/html")
    os.system("cd /var/www/html")
    print("editing the file with? 1.nano , 2.gedit ")
    editors = int(input())
    if editors == 1: 
      print("Editing with nano")
      os.system("nano /var/www/html/index.html")
    elif editors == 2:
      print("Editing with gedit")
      os.system("gedit /var/www/html/index.html")
    else:
      print("Invalid option.")
  else:
    print("Invalid option , Please enter [edit] next time")


#Defining burpsuite , uses later
def run_burpsuite():
  print("Running BurpSuite..")
  os.system("sudo burpsuite")


def start_nginx():
  print("starting nginx webserver...")
  os.system("sudo systemctl start nginx")

print(Fore.RED + """ 
   _____        _______ ____   ____  _       _____ 
  / ____|      |__   __/ __ \ / __ \| |     / ____|
 | (___   ___  ___| | | |  | | |  | | |    | (___  
  \___ \ / _ \/ __| | | |  | | |  | | |     \___ \ 
  ____) |  __/ (__| | | |__| | |__| | |____ ____) |
 |_____/ \___|\___|_|  \____/ \____/|______|_____/

""")
print(Style.RESET_ALL)
print("Welcome to SecTOOLS")
print("GO SUDO IT !!!!")
print(Fore.RED+"""WARNING : Don't use this tool to hack anyone Permission ,
only use it when you have Permission or use it in your network only
Don't hack anyone, I'm not responsible for any offensive works.""")
print(Style.RESET_ALL)
print("""**************************************************


Created By MrEbrahimXD 


github.com/MrEbrahimXD


https://www.youtube.com/channel/UC-_knpocmKPGJ2hGKUGL7_Q

**************************************************


""")

print(Fore.GREEN+ """Choose from 


[1] Network scanning with Nmap 

[2] Sniffing attack with Wireshark and ettercap

[3] Scanning Webservers with Nikto and dirb

[4] Starting Webservers With apache2 and nginx

[5] Webserver analysis with BurpSuite

[0] For installing required files and tools

""")      

lol = int(input())

if lol == 1:
  calling_nmap()
elif lol == 2:
  run_sniffing()
elif lol == 3:
  scan_webserver()
elif lol == 4:
  print("Choose from 1.Apache2 2.nginx")
  choose_webserver = input()
  if choose_webserver == 1:
    print("Starting Apache2 webserver...")
    apache2_webserver()
  if choose_webserver == 2:
    print("Starting nginx Webserver !")
    start_nginx()
elif lol == 5:
  print("Starting BurpSuite ! ")
  run_burpsuite()
elif lol == 0:
  print("Installing required tools and packages")
  req_install()
else:
  print("Invalid Option.")
  
  
  
