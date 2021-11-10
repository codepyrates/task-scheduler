import pytest
from flo import mocker
from task_scheduler.topic_search.websites_to_search import *

def test_britannica_search():
    diffs = mocker(britannica_search, path="/home/hamza/task-scheduler/tests/search_test/test_britannica_search.txt")
    assert not diffs, diffs

def test_wikipedia_search():
    diffs = mocker(wikipedia_search, path="/home/hamza/task-scheduler/tests/search_test/test_wikipedia_search.txt")
    assert not diffs, diffs

def test_citizendium_search():
    diffs = mocker(citizendium_search, path="/home/hamza/task-scheduler/tests/search_test/test_citizendium_search.txt")
    assert not diffs, diffs


def test_list_of_websites():
    diffs = mocker(list_of_websites, path="/home/hamza/task-scheduler/tests/search_test/test_list_of_websites.txt")
    assert not diffs, diffs    
