"""
Support for Xiaomi Mijia Bluetooth Termometer.
Turn off clock mode without web flasher in Linux
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

command = "char-write-req 2d 55820000002804BF7C31B83C "

print(command)
child.sendline(command)
child.expect("Characteristic value was written successfully", timeout=10)
print("done!")
child.sendline("disconnect")
child.sendline("exit")


