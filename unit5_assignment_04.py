__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''
def left_binary_search(input,value):
    low=0
    high=len(input)-1
    k=-1
    result=k
    result=left_binary_search1(input, low, high, value, k)
    return result

def left_binary_search1(input,low,high, value,k):
    if low<=high:
        mid = (low + high) // 2
        if input[mid]==value:
            k=mid
            return left_binary_search1(input,low,mid-1,value,k)
        elif value<input[mid]:
            return left_binary_search1(input,low,mid-1,value,k)
        else:
            return left_binary_search1(input,mid+1,high,value,k)
    return k

# write your own exhaustive tests :)
def test_left_binary_search_student():
    input=[1, 2, 3, 3, 4, 4, 5]
    assert 2 == left_binary_search(input,3)
    assert 4 == left_binary_search(input,4)
    input = range(10)
    for index, value in enumerate(input):
        assert index == left_binary_search(input, value)
    assert -1 == left_binary_search(input, -10)
    assert -1 == left_binary_search(input, 100)
    input=[1,1,1,1]
    assert 0 == left_binary_search(input, 1)

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)
