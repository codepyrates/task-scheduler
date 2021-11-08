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
    
def test_number_of_rows_in_reminders_instance_variable(reminder_handler):
    expected = 2
    actual = len(reminder_handler.reminders)
    assert actual == expected
    
def test_number_of_columns_in_reminders_instance_variable(reminder_handler):
    expected = 2
    actual = len(reminder_handler.reminders.columns)
    assert actual == expected