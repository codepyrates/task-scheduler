import numpy as np
import pytest
from task_scheduler.reminders.reminder_handler import RemindersHandler

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminders.csv")
    return rmh
@pytest.mark.xfail
def test_add_reminder(reminder_handler):
    expected = "latest reminder"
    reminder_handler.add_reminder("2022-12-31 22:22:22", "latest reminder")
    actual = reminder_handler.reminders.iloc[2]['message']
    assert actual == expected