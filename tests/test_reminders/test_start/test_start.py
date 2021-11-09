import numpy as np
import pytest
from task_scheduler.reminder.reminder_handler import RemindersHandler
from tests.test_reminders.reminders_mocker import reminder_mocker

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminder.csv")
    return rmh

def test_start_scenario_1(reminder_handler):
    diffs = reminder_mocker(reminder_handler.start, path="tests/test_reminders/test_start/start.txt")
    assert not diffs, diffs
    