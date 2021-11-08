import numpy as np
import pytest

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("tests/test_reminder/reminder.csv")
    return rmh
def test_initializing_a_reminder_handler_instance(reminder_handler):
    expected = "ReminderHandler"
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
    
def test_dtype_of_time_column_reminders_instance_variable_is_datetime(reminder_handler):
    expected = np.datetime64
    actual = reminder_handler.reminders.time.dtype
    assert actual == expected
    
def test_sort_reminders(reminder_handler):
    expected = "First reminder"
    reminder_handler.sort_reminders()
    actual = reminder_handler.reminders.iloc[0].message
    assert actual == expected

def test_update_next_reminder(reminder_handler):
    expected = "First reminder"
    reminder_handler.sort_reminders()
    reminder_handler.update_next_reminder()
    actual = reminder_handler.next_reminder['message']
    assert actual == expected
    