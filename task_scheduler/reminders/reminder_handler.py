import pandas as pd
from datetime import datetime as dt
import time
import tkinter as tk
import os
import time
import threading

class RemindersHandler:
    def __init__(self, path):
        self.path = path
        self.next_reminder = {"time": None,"date":None, "message" : None}
        self.reminders = pd.read_csv(path)
        self.reminders['time'] = pd.to_datetime(self.reminders['time'], format="%Y-%m-%d %H:%M:%S")
        self.sort_reminders()
        self.update_next_reminder()
    def sort_reminders(self):
        self.reminders.sort_values('time', inplace=True, ignore_index=True,  ascending=True)
    def update_next_reminder(self):
        self.next_reminder['time'] = str(self.reminders.iloc[0]['time'].time())
        self.next_reminder['date'] = str(self.reminders.iloc[0]['time'].date())
        self.next_reminder['message'] = self.reminders.iloc[0]['message']
    def view_reminders(self):
        records = list(self.reminders.to_records(index = True))
        for index, time, message in records:
            t = pd.to_datetime(str(time))
            print(f"{index}. Time: {t.time()}\n   Date: {t.date()}\n   Message: {message}")
    def start(self):
        print("Welcome to Reminders ⏰")
        time.sleep(0.5)
        while True:
            time.sleep(0.5)
            self.view_reminders()
            print("Options { u : update a reminder    d : delete a reminder    q : back to main   a : add new reminder }")
            pmt = input("➤➤➤   ")
            if pmt == "q":
                return

            elif pmt == "u":
                self.handle_update()
            
            elif pmt == "a":
                self.handle_add()
            elif pmt == "d":
                self.handle_delete()
            else:
                print("Please enter a valid option.")

    def save_to_server(self):
        self.reminders.to_csv(self.path, header=True, index=False, mode='w')
        

                
    def update_reminder(self, index, newtime, newmessage):
        self.reminders.iloc[index, self.reminders.columns.get_loc('time')] = dt.strptime(newtime, "%Y-%m-%d %H:%M:%S" )
        self.reminders.iloc[index, self.reminders.columns.get_loc('message')] = newmessage
        self.sort_reminders()
    def get_time_and_date_from_index(self, index):
        t = str(self.reminders.iloc[index, self.reminders.columns.get_loc('time')].time())
        d = str(self.reminders.iloc[index, self.reminders.columns.get_loc('time')].date())
        m = self.reminders.iloc[index, self.reminders.columns.get_loc('message')]
        return (t, d, m)
    def handle_update(self):
        print("Enter the index of the reminder you want to update:")
        idx = input("➤➤➤   ")
        t,d,m = self.get_time_and_date_from_index(int(idx))
        print(f"Enter new time, empty to keep the old one, old one is {t}:")
        tm = input("➤➤➤   ")
        print(f"Enter new date, empty to keep the old one, old one is {d}:")
        dt = input("➤➤➤   ")
        print(f'Enter new message, empty to keep the old one, old one is\n“{m}”:')
        msg = input("➤➤➤   ")
        self.update_reminder(int(idx), f"{dt} {tm}", msg)
        print("Reminder has been updated successfully!")


    def get_next_reminder(self):
        return self.next_reminder    
    def reminder_thread(self):
        next_reminder = self.get_next_reminder()
        while True:
            time.sleep(1)
            t = str(dt.now().replace(microsecond=0).time())
            d = str(dt.now().replace(microsecond=0).date())
            if next_reminder['time'] == t and next_reminder['date'] == d:
                beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
                beep(50)
                window = tk.Tk()
                greeting = tk.Label(text=f"\n\n{next_reminder['message']}",width=40, height=20)
                greeting.pack()
                window.mainloop()
                break
    def start_reminder_thread(self):
        reminder = threading.Thread(target=self.reminder_thread)
        reminder.start()  

    def add_reminder(self, time, message):
        self.reminders = self.reminders.append({"time": dt.strptime(time, "%Y-%m-%d %H:%M:%S" ), "message": message}, ignore_index=True)
        self.sort_reminders()
        self.update_next_reminder()
    def handle_add(self):
        print("Enter time for new reminder, should follow HH:MM:SS, and in 24 hrs. format: (c) to cancel")
        tm = input("➤➤➤   ")
        if tm == "c": return "c"
        print("Enter date for new reminder, should follow YYYY-MM-DD: (c) to cancel")
        dt = input("➤➤➤   ")
        if dt == "c": return "c"
        print("Enter message for new reminder, leave empty if no message is needed: (c) to cancel")
        msg = input("➤➤➤   ")
        if msg == "c": return "c"
        self.add_reminder(f"{dt} {tm}", msg)
        print("Your new reminder has been saved successfully!")

 
    def delete_reminder(self, index):
        self.reminders.drop(index, inplace=True)
        self.reminders.reset_index(drop=True, inplace=True)
        self.sort_reminders()  
    def handle_delete(self):
        print("Enter the index of the reminder you want to delete:")
        idx = input("➤➤➤   ")
        self.delete_reminder(int(idx))
        print("Reminder has been deleted successfully!")


