import pytest
from task_scheduler.reminders.reminder_handler import RemindersHandler

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminders.csv")
    return rmh
@pytest.mark.xfail
def test_update_reminder(reminder_handler):
    expected = "2021-11-08 11:11:11"
    reminder_handler.update_reminder(0, "2021-11-08 11:11:11", "new message")
    actual = str(reminder_handler.reminders.iloc[0]['time'])
    assert actual == expected
    