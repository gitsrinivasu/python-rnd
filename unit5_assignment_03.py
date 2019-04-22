__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
# all the original letters exactly once
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if first==None or second==None:
        return False
    if len(first)==0 and len(second)==0 :
        return True
    first=first.lower()
    second=second.lower()
    second1=list(second)
    le=len(second)
    lf=len(first)
    for j in range(len(first)):
        if first[j]==" ":
            continue
        c=0
        k=0
        for i in range(len(second)):
            if second[i] == " ":
                continue
            elif second[i]==first[j]:
                k=i
                c=1
        if c==0:
            return False
        else:
            if k+1<len(second):
                second = second[:k]+second[k+1:]
            else:
                second=second[:k]

    l=j
    for j in range(len(second1)):
        if second1[j]==" ":
            continue
        c=0
        k=0
        for i in range(len(first)):
            if first[i] == " ":
                continue
            elif first[i]==second1[j]:
                k=i
                c=1
        if c==0:
            return False
        else:
            if k+1<len(first):
                first = first[:k]+first[k+1:]
            else:
                first=first[:k]
    if j==le-1 and l==lf-1:
        return True

    return False



# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert False == are_anagrams("pipt","tip")
    assert True == are_anagrams("adultery","true lady")
    assert True == are_anagrams("","")
    assert False == are_anagrams("pit",None)
    assert True == are_anagrams("Slate","Least")

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
