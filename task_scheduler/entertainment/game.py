from terminaltables import SingleTable
from termcolor import colored
import time
import os
import time
import random

os.system('clear')
welcome = "Welcome to Mahjong by CodePyrates."
welcome = colored(welcome, 'green', attrs=['bold'])
msg = ""
for l in welcome:
    msg+=l
    print(msg, end="\r")
    time.sleep(0.075)
time.sleep(0.25)
os.system('clear')
instruction = "Just try to match the letters by entering the number of a cell."
instruction = colored(instruction, 'green', attrs=['bold'])
msg = ""
for l in instruction:
    msg+=l
    print(msg, end="\r")
    time.sleep(0.075)
time.sleep(0.25)
os.system('clear')
letters = ["A","B","C","D","E","F","G","H"]
letters = [*letters,*letters]
characters = [*letters]
random.shuffle(letters)

initial = [
    [" 0", " 1", " 2", " 3"],
    [" 4", " 5", " 6", " 7"],
    [" 8"," 9","10","11"],
    ["12","13","14","15"]
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
        continue
    for i in range(4):
        for j in range(4):
            if str(first_choice) == initial[i][j].strip():
                initial[i][j] =  colored(" " + letters[int(first_choice)], 'green', attrs=['bold'])
                grid = SingleTable(initial)
                grid.inner_row_border = True
    os.system('clear')
    print(grid.table)
    second_choice = int(input("Second Letter   ➤   "))
    second = letters[second_choice]
    for i in range(4):
        for j in range(4):
            if str(second_choice) == initial[i][j].strip():
                initial[i][j] =  colored(" " + letters[int(second_choice)], 'green', attrs=['bold'])
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
                    initial[i][j] = " " + str(n).strip() if len(str(n).strip()) < 2 else str(n)
                n+=1
        grid = SingleTable(initial)
        grid.inner_row_border = True
        time.sleep(0.75)
    turn += 1
    if len(correct) == 16:
        print(f"Game is over!\nYour score is {turn}")
        break
    os.system('clear')
    print(grid.table)
        

