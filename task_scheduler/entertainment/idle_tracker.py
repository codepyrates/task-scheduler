from pynput.mouse import Controller
from termcolor import colored
import time

def idle_tracker():
    mouse = Controller()
    init = mouse.position
    period = 0
    while True:
        time.sleep(0.1)
        period += 1
        final = mouse.position
        print(final)
        if (init == final) and (period > 70):
            
            idle_tracker()
        elif init != final:
            time.sleep(0.1)
            init = final
            period = 0  