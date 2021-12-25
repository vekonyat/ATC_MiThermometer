"""
Support for Xiaomi Mijia Bluetooth Termometer.
Sends zero time to Lywsd003MMC 
It works as a stopwatch 
"""
import logging
import sys
#import urllib.request
#import base64
import time
from datetime import datetime, timedelta
from threading import Lock, current_thread
import re
from subprocess import PIPE, Popen, TimeoutExpired
import signal
import os
import pexpect

DEVICE = "A4:C1:38:31:35:83"   # address of your device

#date_num = int(sys.argv[1])  #If script is called with time data

date_num = 35 # If script is called wi

print(date_num) # just for debug
print(hex(date_num)) # just for debug 
# Run gatttool interactively.
child = pexpect.spawn("gatttool -I") # pexpect and gatttool should be installed

# Connect to the device.
print("Connecting to:") # for debug
print(DEVICE) #for debug
NOF_REMAINING_RETRY = 20 # number of retries
while True:
    try:
        child.sendline("connect {0}".format(DEVICE))
        child.expect("Connection successful", timeout=5)
    except pexpect.TIMEOUT:
        NOF_REMAINING_RETRY = NOF_REMAINING_RETRY-1
        if (NOF_REMAINING_RETRY>0):
            print("timeout, retry...")
            continue
        else:
            print("timeout, giving up.")
            break
    else:
        print("Connected!")
        break

command = "char-write-req 2d 23" + '{:02x}'.format(date_num & 0xFF) + '{:02x}'.format(date_num >> 8 & 0xFF) \
   + '{:02x}'.format(date_num >> 16 & 0xFF) + '{:02x}'.format(date_num >> 24 & 0xFF)  # writes time to device
#command = "char-write-req 2d 22" + '{:02x}'.format(deg_num & 0xFF) + '{:02x}'.format(deg_num >> 8 & 0xFF) + "0000D002A0" # would send external data to device
print(command)
child.sendline(command)
child.expect("Characteristic value was written successfully", timeout=10)
print("done!")
child.sendline("disconnect")
child.sendline("exit")


