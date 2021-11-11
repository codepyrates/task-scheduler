from os import path
import pytest
from task_scheduler.notes.notes import  NotesHandler, Notes
from tests.test_reminders.reminders_mocker import reminder_mocker

@pytest.fixture
def notes_handler():
    nh = NotesHandler()
    return nh

def test_notes_scenario_add_1(notes_handler):
    diffs = reminder_mocker(notes_handler.start, path="./tests/test_notes/scenario_1.txt")
    assert not diffs, diffs
    
def test_notes_scenario_delete_1(notes_handler):
    diffs = reminder_mocker(notes_handler.start, path="./tests/test_notes/scenario_delete_1.txt")
    assert not diffs, diffs
    
def test_notes_scenario_update_1(notes_handler):
    diffs = reminder_mocker(notes_handler.start, path="./tests/test_notes/scenario_update_1.txt")
    assert not diffs, diffs
    
def test_notes_scenario_invalid_1(notes_handler):
    diffs = reminder_mocker(notes_handler.start, path="./tests/test_notes/test_scnario_invalid_entry_1.txt")
    assert not diffs, diffs
    
def test_notes_scenario_quit(notes_handler):
    diffs = reminder_mocker(notes_handler.start, path="./tests/test_notes/scenario_quit.txt")
    assert not diffs, diffs