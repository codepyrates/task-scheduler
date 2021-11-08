import pytest
from task_scheduler.reminder.reminder_handler import RemindersHandler
from tests.test_reminders.reminders_mocker import reminder_mocker

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminder.csv")
    return rmh

def  test_delete_reminder_by_number_of_remaining_reminders(reminder_handler):
    expected = 1
    reminder_handler.delete_reminder(1)
    actual = len(reminder_handler.reminders)
    assert actual == expected
    
    