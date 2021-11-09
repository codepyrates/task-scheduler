import pytest
from task_scheduler.reminders.reminder_handler import RemindersHandler
from tests.test_reminders.reminders_mocker import reminder_mocker

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminders.csv")
    return rmh

def test_update_reminder(reminder_handler):
    expected = "2021-11-08 11:11:11"
    reminder_handler.update_reminder(0, "2021-11-08 11:11:11", "new message")
    actual = str(reminder_handler.reminders.iloc[0]['time'])
    assert actual == expected
    
def  test_update_reminder_scenario_1(reminder_handler):
    diffs = reminder_mocker(reminder_handler.start, path="tests/test_reminders/test_reminders_update_reminders/update_reminder_scenario_1.txt")
    assert not diffs, diffs