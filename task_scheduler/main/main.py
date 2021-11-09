from art import tprint
from termcolor import colored
import time
import threading
import subprocess
import os
import webbrowser
from task_scheduler.reminders.reminder_handler import RemindersHandler
from task_scheduler.group.group_app import main_scenario
from task_scheduler.notes.notes import NotesHandler,Notes
os.system("clear")
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
    nh = NotesHandler()
    rmh = RemindersHandler("./reminders.csv")
    reminder_th = threading.Thread(target=rmh.reminder_thread, daemon=True)
    entertainment_th = threading.Thread(
        target=entertainment_thread, daemon=True)
    reminder_th.start()
    entertainment_th.start()
    while True:
        os.system("clear")
        print("Options { r : reminders    a : app grouping    s : search   n : notes    e : entertainment    q : quit}")
        pmt = input("➤➤➤   ")
        if pmt == "q":
            print("See you soon.")
            exit()
        elif pmt == "r":
            rmh.start()
        elif pmt == "a":
            main_scenario()
        elif pmt == "n":
            nh.start()
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    
    main()
    
