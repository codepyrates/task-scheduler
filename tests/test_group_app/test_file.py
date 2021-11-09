# import pytest
from mocker_group_app_feature import mocker
from task_scheduler.group.group_app import *
# pytestmark = [pytest.mark.version_2]


def test_get_app():
    diffs = mocker(main_senario, path="tests/test_group_app/senario.txt")
    assert not diffs, diffs

def test_full_senario():
    diffs = mocker(main_senario, path="tests/test_group_app/senario2.txt")
    assert not diffs, diffs

# def test_wikipedia_search():
#     diffs = mocker(wikipedia_search, path="tests/search_test/test_wikipedia_search.txt")
#     assert not diffs, diffs

# def test_citizendium_search():
#     diffs = mocker(citizendium_search, path="tests/search_test/test_citizendium_search.txt")
#     assert not diffs, diffs


# def test_list_of_websites():
#     diffs = mocker(list_of_websites, path="tests/search_test/test_list_of_websites.txt")
#     assert not diffs, diffs    