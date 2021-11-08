import numpy as np
import pytest
from task_scheduler.reminders.reminder_handler import RemindersHandler

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminders.csv")
    return rmh

def test_initializing_a_reminder_handler_instance(reminder_handler):
    expected = "RemindersHandler"
    actual = reminder_handler.__class__.__name__
    assert actual == expected   