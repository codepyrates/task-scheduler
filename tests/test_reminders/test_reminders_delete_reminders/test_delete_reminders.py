import pytest
from task_scheduler.reminders.reminder_handler import RemindersHandler
from tests.test_reminders.reminders_mocker import reminder_mocker

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

def  test_delete_reminder_by_number_of_remaining_reminders(reminder_handler):
    expected = 1
    reminder_handler.delete_reminder(1)
    actual = len(reminder_handler.reminders)
    assert actual == expected
    

def test_delete_reminder_by_value_of_remaining_reminders(reminder_handler):
    expected = "this a reminder"
    reminder_handler.delete_reminder(1)
    actual = reminder_handler.reminders.iloc[0]['message']
    assert actual == expected
    
def  test_delete_reminder_scenario_1(reminder_handler):
    diffs = reminder_mocker(reminder_handler.start, path="./tests/test_reminders/test_reminders_delete_reminders/delete_reminder_scenario_1.txt")
    assert not diffs, diffs