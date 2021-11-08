import numpy as np

def test_initializing_a_reminder_handler_instance():
    expected = "ReminderHandler"
    rmh = RemindersHandler("tests/test_reminder/reminder.csv")
    actual = rmh.__class__.__name__
    assert actual == expected    

def test_number_of_rows_in_reminders_instance_variable():
    expected = 2
    rmh = RemindersHandler("tests/test_reminder/reminder.csv")
    actual = len(rmh.reminders)
    assert actual == expected
    
def test_number_of_columns_in_reminders_instance_variable():
    expected = 2
    rmh = RemindersHandler("tests/test_reminder/reminder.csv")
    actual = len(rmh.reminders.columns)
    assert actual == expected
    
def test_dtype_of_time_column_reminders_instance_variable_is_datetime():
    expected = np.datetime64
    rmh = ReminderHandler("tests/test_reminder/reminder.csv")
    actual = rmh.reminders.time.dtype
    assert actual == expected
    