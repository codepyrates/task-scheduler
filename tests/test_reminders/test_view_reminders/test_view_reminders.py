import pytest
from task_scheduler.reminder.reminder_handler import RemindersHandler
from tests.test_reminders.reminder_mocker import reminder_mocker

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminder.csv")
    return rmh

def test_view_reminder_scenario_1(reminder_handler):
    diffs = reminder_mocker(reminder_handler.start, path="view_reminders.txt")
    assert not diffs, diffs