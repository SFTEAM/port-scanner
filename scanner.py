import socket
import threading
import os
import sys
import concurrent.futures
import colorama 
from colorama import Fore
from colorama import *
from sys import exit
 
print_lock = threading.Lock()
 
os.system("cls & title port scanner made by mkay")

print(f"Click CNTRL + BREAK if you dont want to scan anymore ports.")
def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip,port))
        scanner.close()
        with print_lock:
            print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] {port} is open")
    except:
        pass

ip = input(f"[{Fore.YELLOW}INPUT{Fore.RESET}] IP: ")

with concurrent.futures.ThreadPoolExecutor(max_workers=450) as executor:
    for port in range(65000):
        executor.submit(scan, ip, port + 1)
      
# tool developed by mkay