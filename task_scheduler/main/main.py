from art import tprint
from termcolor import colored
import time
import threading


def welcome():
    welcome = "Welcome, this is"
    welcome = colored(welcome, 'cyan', attrs=['bold'])
    msg = ""
    for l in welcome:
        print(msg, end="\r")
        msg += l
        time.sleep(0.05)
    time.sleep(0.25)
    print("\n")
    tprint("Anton")
    welcome = "your assistant and scheduler."
    welcome = colored(welcome, 'cyan', attrs=['bold'])
    msg = ""
    for l in welcome:
        print(msg, end="\r")
        msg += l
        time.sleep(0.05)
    time.sleep(0.25)
    print("\n")

def reminder_thread():
    pass

def entertainment_thread():
    pass