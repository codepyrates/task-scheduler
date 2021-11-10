import numpy as np
import pytest
from task_scheduler.reminders.reminder_handler import RemindersHandler
from tests.test_reminders.reminders_mocker import reminder_mocker


# I have to rewrite to the csv file I am using since everytime add is added, the file gets updated.
def test_reset_reminders_csv():
    with open("./tests/test_reminders/reminders.csv" ,"w") as f:
        f.write("""time,message
2021-11-09 00:55:00,this is just a test
2021-12-09 10:10:10,this a reminder
2021-12-23 22:22:22,new reminder
                """)
    assert True
    
@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminders.csv")
    return rmh

def  test_add_reminder_scenario_1(reminder_handler):
    diffs = reminder_mocker(reminder_handler.start, path="./tests/test_reminders/test_reminders_add_reminders/add_reminder_scenario_1.txt")
    assert not diffs, diffs