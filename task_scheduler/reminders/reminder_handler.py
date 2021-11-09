import pandas as pd
from datetime import datetime as dt
import time

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
            elif pmt == "a":
                self.handle_add()
            else:
                print("Please enter a valid option.")
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

            elif pmt == "d":
                self.handle_delete()
            else:
                print("Please enter a valid option.")
    def delete_reminder(self, index):
        self.reminders.drop(index, inplace=True)
        self.reminders.reset_index(drop=True, inplace=True)
        self.sort_reminders()  
    def handle_delete(self):
        print("Enter the index of the reminder you want to delete:")
        idx = input("➤➤➤   ")
        self.delete_reminder(int(idx))
        print("Reminder has been deleted successfully!")

