from tests.test_reminders.reminders_mocker import reminder_mocker
from task_scheduler.group.group_app import *



def test_scenario_1():
    diffs = reminder_mocker(main_scenario, path="./tests/test_group_app/senario.txt")
    assert not diffs, diffs

def test_scenario_2():
    diffs = reminder_mocker(main_scenario, path="./tests/test_group_app/senario2.txt")
    assert not diffs, diffs
