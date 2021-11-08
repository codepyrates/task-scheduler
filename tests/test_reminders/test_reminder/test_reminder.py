def test_initializing_a_reminder_handler_instance():
    expected = "ReminderHandler"
    rmh = ReminderHandler("tests/test_reminder/reminder.csv")
    actual = rmh.__class__.__name__
    assert actual == expected    

def test_number_of_rows_in_reminders_instance_variable():
    expected = 2
    rmh = ReminderHandler("tests/test_reminder/reminder.csv")
    actual = len(rmh.reminders)
    assert actual == expected
    

    