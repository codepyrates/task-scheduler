from art import tprint
from termcolor import colored
import time
import threading
import subprocess
import os
import webbrowser
from task_scheduler.reminders.reminder_handler import RemindersHandler
from task_scheduler.group.group_app import main_scenario
from task_scheduler.notes.notes import NotesHandler, Notes
from task_scheduler.entertainment.idle_tracker import idle_tracker
from task_scheduler.topic_search.main_search_of_topics import search_main
os.system("clear")


def welcome():
    """[Welcome function how welcome of the user]
    """
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


def main(skip):
    """[the main its a base function in app that make you start deal with app]
    """
    nh = NotesHandler()
    rmh = RemindersHandler("./task_scheduler/reminders/reminders.csv")
    if not skip:
        welcome()
        reminder_th = threading.Thread(target=rmh.reminder_thread, daemon=True)
        entertainment_th = threading.Thread(
            target=idle_tracker, daemon=True)
        reminder_th.start()
        entertainment_th.start()
    while True:
        os.system("clear")
        options = "Options { r : reminders    a : app grouping    s : search   n : notes    e : entertainment    q : quit}"
        options = colored(options, 'cyan', attrs=['bold'])
        print(options)
        pmt = input("➤➤➤   ")
        if pmt == "q":
            print("See you soon.")
            exit()
        elif pmt == "r":
            rmh.start()
        elif pmt == "a":
            apps = main_scenario()
            rmh.add_app_group(apps)
        elif pmt == "n":
            nh.start()
        elif pmt == "s":
            result = search_main()
            nh.add_note("",result)
            search_main()
        elif pmt == "*":
            exit()
        else:
            print("Please enter a valid option.")
        time.sleep(0.25)

if __name__ == "__main__":

    main(True)
