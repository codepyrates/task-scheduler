import pytest
from task_scheduler.reminders.reminder_handler import RemindersHandler
from tests.test_reminders.reminders_mocker import reminder_mocker

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminders.csv")
    return rmh

def test_view_reminder_scenario_1(reminder_handler):
    diffs = reminder_mocker(reminder_handler.view_reminders, path="tests/test_reminders/test_reminders_view_reminders/view_reminders.txt")
    assert not diffs, diffs