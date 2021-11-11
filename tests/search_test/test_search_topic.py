from difflib import diff_bytes
import pytest
from flo import mocker
from task_scheduler.topic_search.websites_to_search import *

def test_britannica_search():
    diffs = mocker(britannica_search, "./tests/search_test/test_britannica_search.txt", 'animal')
    assert not diffs, diffs

def test_wikipedia_search():
    diffs = mocker(wikipedia_search,"./tests/search_test/test_wikipedia_search.txt", "cat" )
    assert not diffs, diffs

def test_citizendium_search():
    diffs = mocker(citizendium_search, "./tests/search_test/test_citizendium_search.txt", "fish")
    assert not diffs, diffs


def test_list_of_websites():
    diffs = mocker(list_of_websites, path="./tests/search_test/test_list_of_websites.txt")
    assert not diffs, diffs    

def test_wikipedia():
    expected = "The cat (Felis catus) is a domestic species of small carnivorous mammal.[1][2] It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family.[4] A cat can either be a house cat, a farm cat or a feral cat; the latter ranges freely and avoids human contact.[5] Domestic cats are valued by humans for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various cat registries.[6]"
    actual = wikipedia_search()
    assert expected == actual
    
def test_britannica():
    expected = "animal, (kingdom Animalia), any of a group of multicellular eukaryotic organisms (i.e., as distinct from bacteria, their deoxyribonucleic acid, or DNA, is contained in a membrane-bound nucleus). They are thought to have evolved independently from the unicellular eukaryotes. Animals differ from ..."
    actual = britannica_search()
    assert actual == expected
    
def test_citizendium():
    expected = "Any aquatic vertebrate animal that is typically ectothermic (or cold-blooded), covered with scales, and equipped with two sets of paired fins and several unpaired fins. Fish are abundant in the sea and in fresh water, with species being known from mountain streams (e.g., char and gudgeon) as well as in the deepest depths of the ocean (e.g., gulpers and anglerfish)."
    actual = citizendium_search()
    assert actual == expected
    
def test_list_search():
    diff = mocker(list_of_websites, "./tests/search_test/wiki_joker.txt", "joker")
    assert  not diff, diff
    
def test_list_search_2():
    diff = mocker(list_of_websites, "./tests/search_test/citi_joker.txt", "joker")
    assert  not diff, diff