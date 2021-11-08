def test_initializing_a_reminder_handler_instance():
    expected = "ReminderHandler"
    rmh = ReminderHandler("tests/test_reminder/reminder.csv")
    actual = rmh.__class__.__name__
    assert actual == expected    