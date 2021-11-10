# import pytest
from mocker_group_app_feature import mocker
from task_scheduler.group.group_app import *
# pytestmark = [pytest.mark.version_2]


def test_get_app():
    diffs = mocker(main_senario, path="tests/test_group_app/senario.txt")
    assert not diffs, diffs

def test_middle_senario():
    diffs = mocker(main_senario, path="tests/test_group_app/senario2.txt")
    assert  diffs, diffs

def test_full_senario():
    diffs = mocker(main_senario, path="tests/test_group_app/senario3.txt")
    assert  diffs, diffs

def test_failier_input():
    diffs = mocker(main_senario, path="tests/test_group_app/senario4.txt")
    assert  diffs, diffs

def test_output_input_long_senario():
    diffs = mocker(main_senario, path="tests/test_group_app/senario5.txt")
    assert  diffs, diffs

def test_error_senario():
    diffs = mocker(main_senario, path="tests/test_group_app/senario6.txt")
    assert  diffs, diffs
# add senario for all cases will see in group app feature