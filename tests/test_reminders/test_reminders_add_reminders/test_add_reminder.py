import numpy as np
import pytest
from task_scheduler.reminders.reminder_handler import RemindersHandler
from tests.test_reminders.reminders_mocker import reminder_mocker

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminders.csv")
    return rmh

def test_add_reminder(reminder_handler):
    expected = "latest reminder"
    reminder_handler.add_reminder("2022-12-31 22:22:22", "latest reminder")
    actual = reminder_handler.reminders.iloc[2]['message']
    assert actual == expected

def  test_delete_reminder_scenario_1(reminder_handler):
    diffs = reminder_mocker(reminder_handler.start, path="tests/test_reminders/test_reminders_add_reminders/add_reminder_scenario_1.txt")
    assert not diffs, diffs