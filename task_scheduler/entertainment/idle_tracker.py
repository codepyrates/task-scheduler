from pynput.mouse import Controller
from termcolor import colored
import time
import os
import sys
from task_scheduler.entertainment.game import mahjongg

def launch_entertainment():
    mahjongg()
def idle_tracker():
    mouse = Controller()
    init = mouse.position
    period = 0
    while True:
        time.sleep(0.1)
        period += 1
        final = mouse.position
        if (init == final) and (period > 70):
            #launch_entertainment()
            #print("idle")
            idle_tracker()
        elif init != final:
            time.sleep(0.1)
            init = final
            period = 0  