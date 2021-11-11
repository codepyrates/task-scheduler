import time
import threading
import builtins
import os
from pynput.keyboard import Controller, Key
kbd = Controller()
real_input = builtins.input

def mock_input(*args):
    return "q"


kill_a = False
kill_b = False
def A():
    n = 0
    global kill_a, kill_b
    while not kill_a:
        time.sleep(1)
        print("A")
        n += 1
        pmt = input("> ")
        if kill_a or n > 3:
            kill_a = True
            kill_b = False
            b = threading.Thread(target=B)
            b.start()
            break
        
def B():
    n = 0
    while True:
        time.sleep(1)
        print("B")
        n+=1
        global kill_b, kill_a
        if kill_b or n > 3: 
            kill_b = True
            kill_a = False
            a = threading.Thread(target=A)
            a.start()
            break

class A:
    def __init__(self):
        self.kill = False
    def start(self):
        n = 0
        global kill_a, kill_b
        while not self.kill:
            time.sleep(1)
            #print("A")
            n += 1
            pmt = self.inp("> ")
            if pmt == "q":
                print(pmt)
                kill_a = True
                kill_b = False
                b = threading.Thread(target=B)
                b.start()
                break
    def stop(self):
        self.kill = True
    def inp(self, *args):
        return real_input(*args)
    
class B:
    def __init__(self):
        self.kill = False
    def start(self):
        n = 0
        while not self.kill:
            time.sleep(1)
            print("B")
            n+=1
            global kill_b, kill_a
            if kill_b or n > 3: 
                kill_b = True
                kill_a = False
                a = threading.Thread(target=A)
                a.start()
                break

    def stop(self):
        exit()
aa = A()
bb = B()
a = threading.Thread(target=aa.start)
b = threading.Thread(target=bb.start)
a.start()
time.sleep(5)
os.system("echo q")
kbd.press(Key.enter)
kbd.release(Key.enter)



try:
    #builtins.input = mock_input
    aa.inp = mock_input
except:
    a.join()
    print("done")
exit()
