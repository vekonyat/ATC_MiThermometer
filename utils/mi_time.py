"""
Support for Xiaomi Mijia Bluetooth Termometer.
Sends current time to Lywsd003MMC
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

DEVICE = "xx:xx:xx:xx:xx:xx"   # MAC address of your device

date_num = int(time.time()+3605) #current time

print(date_num)
print(hex(date_num))
# Run gatttool interactively. pexpect and gatttool needed.
child = pexpect.spawn("gatttool -I")

# Connect to the device.
print("Connecting to:")
print(DEVICE)
NOF_REMAINING_RETRY = 20
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
   + '{:02x}'.format(date_num >> 16 & 0xFF) + '{:02x}'.format(date_num >> 24 & 0xFF) 

print(command)
child.sendline(command)
child.expect("Characteristic value was written successfully", timeout=10)
print("done!")
child.sendline("disconnect")
child.sendline("exit")
