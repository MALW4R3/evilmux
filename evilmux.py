#!/usr/bin/env python
# -- coding: utf-8 --
import os,sys
import time

os.system('clear')
time.sleep(1)
os.system('cat banner1.txt')
time.sleep(1)
os.system('clear')
os.system('cat banner2.txt')
time.sleep(1)
os.system('clear')
os.system('cat banner3.txt')
time.sleep(1)
os.system('clear')
os.system('cat banner4.txt')
time.sleep(1)
os.system('clear')
os.system('cat banner.txt')
print('\n\n')
print('BY : APT47\n\n')
print('[1] METASEC')
print('[2] NEBULA')
print('[3] XTRACK')
print('[4] CRACKWARE')
print('[5] DDOS\n')
print('[00] EXIT \n\n')
METASEC = input('termux@evil : ')

if METASEC == '1' or METASEC == '01':
    print('คุณต้องการที่จะติดตั้ง METASEC หรือเปล่า (yes/no)')
L = input('termux@evil/METASEC/ : ')

if L == "yes" or L == "YES":
    os.system('cd METASEC')
    os.system('sh setup.sh')
    os.system('metasec')



