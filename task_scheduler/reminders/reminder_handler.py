import pandas as pd
from datetime import datetime as dt

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