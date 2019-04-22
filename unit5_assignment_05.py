__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
import string

def prune_either_or(sentence):
    if sentence==None:
        return sentence

    str=sentence.split()

    try:

        i = str.index("either")

        j=str.index("or")

        if (i+1!=j) and (i!=0):

            return (" ".join(str[:i])+" "+" ".join(str[i+1:j]))

        else:

            return sentence

    except ValueError:

        return sentence


def test_prune_either_or_student():
    assert "blah something" == prune_either_or("blah either something or somethingelse")
    assert "we can eat" == prune_either_or("we can either eat or talk")
    assert "Two mythical cities eitheron and oregon" == prune_either_or("Two mythical cities eitheron and oregon")
    assert "We can go to a movie" == prune_either_or("We can go either to a movie or to a hotel")
    assert "We can go either way" == prune_either_or("We can go either way")

    assert "either this or that" == prune_either_or("either this or that")
    assert "either way is fine" == prune_either_or("either way is fine")

    assert "It is neither here nor there" == prune_either_or("It is neither here nor there")
    assert "Two mythical cities eitheron and oregon" == prune_either_or("Two mythical cities eitheron and oregon")
    assert "Two cities either and oregon" == prune_either_or("Two cities either and oregon")
    assert "Some random either or test" == prune_either_or("Some random either or test")
    assert None == prune_either_or(None)

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
