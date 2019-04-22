__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
import inspect
import os
from unit6utils import get_temp_dir

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
def inside(l,r):
    o = 0
    for o in range(len(r)):
        if l in r[o]:
            return False
    return True
def anagram_sort(source, destination):
    f=open(source,"rt")
    l=f.readlines()
    lines=list()
    for i in range(len(l)):
        if l[i][0] in string.ascii_letters:
            p=l[i]
            lines.append(p)
    k=list(lines[-1])
    k.append("\n")
    lines.remove(lines[-1])
    k="".join(k)
    lines.append(k)
    r=list()
    j=0
    while j in range(len(lines)):
        i=0
        a=0
        while i in range(j,len(lines)):
            if i!=j:
                d=0
                m=list()
                if are_anagrams(lines[j],lines[i]):
                    a=1
                    if inside(lines[i],r):
                        m.append(lines[i])
                        lines.remove(lines[i])
                        i=i-1
                    else:
                        o=0
                        d=1
                        for o in range(len(r)):
                            if lines[i] in r[o]:
                                r[o].append(lines[i])
                        lines.remove(lines[i])
                        i=i-1
                    if inside(lines[j],r):
                        m.append(lines[j])

                if (len(m)>0) and (d==0):
                    o = 0
                    d = 1
                    if len(m)==1:
                        for o in range(len(r)):
                            if lines[j] in r[o]:
                                r[o].append(m[0])
                    else:
                        r.append(m)
            i=i+1

        if a==0:
            x=list()
            x.append(lines[j])
            r.append(x)
        lines.remove(lines[j])
        j=-1
        j=j+1


    f.close()
    i=0
    for i in range(len(r)):
        r[i].sort(key=lambda s: s.lower())
    r.sort(key=lambda s:s[0].lower())
    r.sort(key=lambda s:len(s),reverse=True)

    import itertools

    from more_itertools import flatten
    r=list(flatten(r))
    r="".join(r)
    f1=open(destination,"wb")
    f1.write(r.encode())
    f1.close()

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
