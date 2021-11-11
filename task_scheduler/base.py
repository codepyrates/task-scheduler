import builtins
import time
import threading
import os
import random
from art import tprint
from termcolor import colored
from terminaltables import SingleTable
from pynput import keyboard
from pynput import mouse
from task_scheduler.reminders.reminder_handler import RemindersHandler
from task_scheduler.group.group_app import main_scenario
from task_scheduler.notes.notes import NotesHandler
from task_scheduler.entertainment.idle_tracker import idle_tracker
from task_scheduler.topic_search.main_search_of_topics import search_main
from task_scheduler.entertainment.game import mahjongg
from task_scheduler.main.main import main

os.system("clear")
kbd = keyboard.Controller()


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
        options = "Options { r : reminders    a : app grouping    s : search    n : notes    q : quit}"
        options = colored(options, 'cyan', attrs=['bold'])
        print(options)
        pmt = input("➤➤➤   ")
        if pmt == "q":
            print("See you soon.")
            raise ValueError
        elif pmt == "r":
            rmh.start()
        elif pmt == "a":
            apps = main_scenario()
            rmh.add_app_group(apps)
        elif pmt == "n":
            nh.start()
        elif pmt == "s":
            result = search_main()
            nh.add_note("", result)
            search_main()
        elif pmt.strip() == "z":
            raise SystemError

        else:
            print("Please enter a valid option.")
        time.sleep(0.25)


def idle_tracker():
    ms = mouse.Controller()
    init = ms.position
    period = 0
    while True:
        time.sleep(0.1)
        period += 1
        final = ms.position
        if (init == final) and (period > 70):
            kbd.press("z")
            kbd.release("z")
            time.sleep(0.5)
            kbd.press(keyboard.Key.enter)
            kbd.release(keyboard.Key.enter)
            time.sleep(3600)
            idle_tracker()
        elif init != final:
            time.sleep(0.1)
            init = final
            period = 0


def mahjongg():
    """[the function how give the user mahjongg game]
    """
    os.system('clear')
    welcome = "Welcome to Mahjong by CodePyrates."
    welcome = colored(welcome, 'green', attrs=['bold'])
    msg = ""
    for l in welcome:
        msg += l
        print(msg, end="\r")
        time.sleep(0.075)
    time.sleep(0.25)
    os.system('clear')
    instruction = "Just try to match the letters by entering the number of a cell."
    instruction = colored(instruction, 'green', attrs=['bold'])
    msg = ""
    for l in instruction:
        msg += l
        print(msg, end="\r")
        time.sleep(0.075)
    time.sleep(0.25)
    os.system('clear')
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    letters = [*letters, *letters]
    characters = [*letters]
    random.shuffle(letters)

    initial = [
        [" 0", " 1", " 2", " 3"],
        [" 4", " 5", " 6", " 7"],
        [" 8", " 9", "10", "11"],
        ["12", "13", "14", "15"]
    ]
    backup = [*initial]

    correct = []

    grid = SingleTable(initial)
    grid.inner_row_border = True
    print(grid.table)

    turn = 1

    while True:
        try:
            first_choice = int(input("First Letter   ➤   "))

            first = letters[first_choice]

        except:
            if first_choice == 16:
                raise SyntaxError
            continue

        for i in range(4):
            for j in range(4):
                if str(first_choice) == initial[i][j].strip():
                    initial[i][j] = colored(
                        " " + letters[int(first_choice)], 'green', attrs=['bold'])
                    grid = SingleTable(initial)
                    grid.inner_row_border = True
        os.system('clear')
        print(grid.table)
        second_choice = int(input("Second Letter   ➤   "))
        second = letters[second_choice]
        for i in range(4):
            for j in range(4):
                if str(second_choice) == initial[i][j].strip():
                    initial[i][j] = colored(
                        " " + letters[int(second_choice)], 'green', attrs=['bold'])
                    grid = SingleTable(initial)
                    grid.inner_row_border = True
        os.system('clear')
        print(grid.table)
        if letters[first_choice] == letters[second_choice]:
            correct.extend([first_choice, second_choice])
        else:
            n = 0
            for i in range(4):
                for j in range(4):
                    if (first_choice == n) or (second_choice == n):
                        initial[i][j] = " " + \
                            str(n).strip() if len(
                                str(n).strip()) < 2 else str(n)
                    n += 1
            grid = SingleTable(initial)
            grid.inner_row_border = True
            time.sleep(0.75)
        turn += 1
        if len(correct) == 16:
            print(f"Game is over!\nYour score is {turn}")
            break
        os.system('clear')
        print(grid.table)


def base():
    skip = False
    while True:
        try:
            main(skip)

        except SystemError:
            skip = True
            try:
                mahjongg()

            except:
                continue
        except ValueError:
            break


if __name__ == "__main__":
    base()
