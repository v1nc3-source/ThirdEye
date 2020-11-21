#!/usr/bin/env/
from termcolor import colored
import scapy.all as scapy
import time
import subprocess


############### external animation ##############################################
subprocess.call("python3 /root/eye.py | lolcat -a -d 1 -F 0.2 -f ", shell=True) #CHANGE THIS DIRECTORY
subprocess.call("python3 /root/nma.py | lolcat -a -d 50 -F 0.2 -f ", shell=True)######################
#################################################################################


##### set the target ############################################################
print("             ")

iptoscan = input(" TARGET >> ")
try:
	print("                                             ")
	##### NMAP QUICK TCP ################################################
	print(colored("################ 𝓝 𝓜 𝓐 𝓟   𝓠 𝓤 𝓘 𝓒 𝓚   𝓣 𝓒 𝓟  #####################################", "red"))
	subprocess.call("grc nmap -Pn -sC -sV -T4 -oA quick " + iptoscan, shell=True)
	print("                                             ")
	##### NMAP VULNERABILITY SCAN ################################################
	print(colored("################ 𝓝 𝓜 𝓐 𝓟  𝓥 𝓤 𝓛 𝓝 𝓔 𝓡 𝓐 𝓑 𝓘 𝓛 𝓘 𝓣 𝓨  𝓢 𝓒 𝓐 𝓝  ####################", "red"))
	subprocess.call("grc  nmap -Pn --script vuln " + iptoscan, shell=True)
	print("                                             ")
	
	##### NMAP FULL-TCP COMMAND ################################################
	print(colored("################ 𝓝 𝓜 𝓐 𝓟  𝓕 𝓤 𝓛 𝓛 - 𝓣 𝓒 𝓟  #########################################", "red"))
	subprocess.call("grc nmap -Pn -sC -sV -p- -T4 -oA full " + iptoscan, shell=True)
	print("                                             ")
	
	##### GOBUSTER FULL SCAN ################################################
	print(colored("################ 𝓖 𝓞 𝓑 𝓤 𝓢 𝓣 𝓔 𝓡  𝓕 𝓤 𝓛 𝓛  𝓢 𝓒 𝓐 𝓝  #################################", "red"))
	subprocess.call("grc gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .txt,.php -u 		"+ 	iptoscan, shell=True)
	print("                                             ")


except KeyboardInterrupt:
    print(colored("  <> Detected CTRL + C", "blue"))
    time.sleep(0.5)
    print(colored("            Goodbye!", "green"))
    time.sleep(0.5)




