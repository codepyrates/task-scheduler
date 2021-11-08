import pytest
from flo import mocker
from task_scheduler.topic_search.websites_to_search import britannica_search 

pytestmark = [pytest.mark.version_2]


def test_britannica_search():
    # game = list_of_websites('animal')
    diffs = mocker(britannica_search, path="tests/search_test/test_britannica_search.txt")
    assert not diffs, diffs