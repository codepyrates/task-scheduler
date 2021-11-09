from art import tprint
from termcolor import colored
import time
import threading
import subprocess
import os
import webbrowser
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

def main():
    welcome()
    reminder_th = threading.Thread(target=reminder_thread, daemon=True)
    entertainment_th = threading.Thread(
        target=entertainment_thread, daemon=True)
    reminder_th.start()
    entertainment_th.start()
    while True:
        pass

if __name__ == "__main__":
    
    #main()
    
